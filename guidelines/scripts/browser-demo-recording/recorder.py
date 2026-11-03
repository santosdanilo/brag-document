import base64
import json
import os
import threading
import time

from websocket import create_connection


class Recorder:
    """Continuous CDP screencast recorder for one page target."""

    def __init__(self, ws_url, outdir, fps=15, quality=75):
        self.ws = create_connection(ws_url, max_size=None)
        self.outdir = outdir
        os.makedirs(outdir, exist_ok=True)
        self.fps = fps
        self.quality = quality
        self._id = 0
        self._send_lock = threading.Lock()
        self._pending = {}
        self.frame_idx = 0
        self.started_at = None
        self.manifest = []
        self._stop = threading.Event()
        self._thread = None
        self._alive = True
        self._thread = threading.Thread(target=self._reader, daemon=True)
        self._thread.start()

    def _next_id(self):
        with self._send_lock:
            self._id += 1
            return self._id

    def cmd(self, method, timeout=30, **params):
        if not self._alive:
            raise RuntimeError("ws closed")
        mid = self._next_id()
        ev = threading.Event()
        slot = [ev, None]
        self._pending[mid] = slot
        msg = {"id": mid, "method": method, "params": params}
        with self._send_lock:
            self.ws.send(json.dumps(msg))
        got = ev.wait(timeout)
        res = slot[1]
        self._pending.pop(mid, None)
        if not got:
            raise TimeoutError(method)
        if res and "error" in res:
            raise RuntimeError(str(res["error"])[:300])
        return res.get("result") if res else None

    def _reader(self):
        while not self._stop.is_set():
            try:
                raw = self.ws.recv()
            except Exception:
                self._alive = False
                break
            if not raw:
                continue
            try:
                msg = json.loads(raw)
            except Exception:
                continue
            if "id" in msg:
                slot = self._pending.get(msg["id"])
                if slot:
                    slot[1] = msg
                    slot[0].set()
            elif msg.get("method") == "Page.screencastFrame":
                self._handle_frame(msg["params"])

    def _handle_frame(self, params):
        idx = self.frame_idx
        self.frame_idx += 1
        with open(os.path.join(self.outdir, f"{idx:06d}.jpg"), "wb") as f:
            f.write(base64.b64decode(params["data"]))
        self.manifest.append({"frame": idx, "ts": params["metadata"].get("timestamp")})
        try:
            with self._send_lock:
                self.ws.send(
                    json.dumps(
                        {
                            "id": 900000 + idx % 90000,
                            "method": "Page.screencastFrameAck",
                            "params": {"sessionId": params["sessionId"]},
                        }
                    )
                )
        except Exception:
            pass

    def evaluate(self, expr, await_promise=False, timeout=120):
        res = self.cmd(
            "Runtime.evaluate",
            timeout=timeout,
            expression=expr,
            returnByValue=True,
            awaitPromise=await_promise,
        )
        if res.get("exceptionDetails"):
            raise RuntimeError(str(res["exceptionDetails"])[:400])
        return res["result"].get("value")

    def navigate(self, url):
        self.cmd("Page.navigate", url=url)

    def wait_load(self, timeout=25):
        start = time.time()
        while time.time() - start < timeout:
            try:
                if self.evaluate("document.readyState") == "complete":
                    return True
            except Exception:
                pass
            time.sleep(0.3)
        return False

    def start(self):
        self.cmd("Page.enable")
        self.cmd("Runtime.enable")
        self.started_at = time.time()
        self.cmd(
            "Page.startScreencast",
            format="jpeg",
            quality=self.quality,
            maxWidth=1280,
            maxHeight=720,
            everyCompositedFrames=True,
        )

    def stop(self):
        try:
            self.cmd("Page.stopScreencast", timeout=5)
        except Exception:
            pass
        self._stop.set()
        time.sleep(0.3)
        try:
            self.ws.close()
        except Exception:
            pass
        with open(os.path.join(self.outdir, "manifest.json"), "w") as f:
            json.dump(
                {"started_at": self.started_at, "fps": self.fps, "frames": self.manifest},
                f,
            )
        return self.outdir, self.frame_idx

    def screenshot(self, path, quality=75):
        res = self.cmd("Page.captureScreenshot", format="jpeg", quality=quality, timeout=20)
        with open(path, "wb") as f:
            f.write(base64.b64decode(res["data"]))
        return path

    def type_slow(self, selector, text, delay=0.08):
        self.evaluate(f"document.querySelector({json.dumps(selector)}).focus()")
        for ch in text:
            self.cmd("Input.insertText", text=ch)
            time.sleep(delay + (0.14 if ch == " " else 0))

    def click_label(self, label, sel="button", exact=False):
        js = """((sel, label, exact) => {
            const els = [...document.querySelectorAll(sel)];
            const el = exact ? els.find(e => e.innerText.trim() === label)
                             : els.find(e => e.innerText.trim().startsWith(label));
            if (!el) return false;
            el.click();
            return true;
        })"""
        return self.evaluate(f"{js}({json.dumps(sel)}, {json.dumps(label)}, {str(exact).lower()})")

    def scroll_to(self, y_target, step=8, pause=0.045):
        self.evaluate(
            f"""(async () => {{
                const max = document.body.scrollHeight;
                for (let y = window.scrollY; y < {y_target}; y += {step}) {{ window.scrollTo(0, y); await new Promise(r=>setTimeout(r,{int(pause*1000)})); }}
                window.scrollTo(0, {y_target});
                return true;
            }})()""",
            await_promise=True,
        )

    def scroll_top(self, pause=0.035, step=12):
        self.evaluate(
            f"""(async () => {{
                for (let y = window.scrollY; y > 0; y -= {step}) {{ window.scrollTo(0, Math.max(0, y)); await new Promise(r=>setTimeout(r,{int(pause*1000)})); }}
                window.scrollTo(0, 0);
                return true;
            }})()""",
            await_promise=True,
        )

    def page_text_len(self):
        return self.evaluate(
            "document.body ? document.body.innerText.length : 0"
        )
