import base64
import json
import time
import urllib.parse
import urllib.request

from websocket import create_connection

CDP = "http://127.0.0.1:9222"


def targets():
    with urllib.request.urlopen(f"{CDP}/json/list") as r:
        return json.load(r)


def find_page(url_substring):
    for t in targets():
        if t["type"] == "page" and url_substring in t["url"]:
            return t
    return None


def new_page(url="about:blank"):
    q = urllib.parse.quote(url, safe=":/?&=")
    req = urllib.request.Request(f"{CDP}/json/new?{q}", method="PUT")
    with urllib.request.urlopen(req) as r:
        return json.load(r)


def close_page(target_id):
    urllib.request.urlopen(f"{CDP}/json/close/{target_id}")


class Page:
    def __init__(self, target):
        if isinstance(target, dict):
            ws_url = target["webSocketDebuggerUrl"]
        else:
            ws_url = target
        self.ws = create_connection(ws_url, max_size=None)
        self.id = 0

    def cmd(self, method, **params):
        self.id += 1
        self.ws.send(json.dumps({"id": self.id, "method": method, "params": params}))
        while True:
            msg = json.loads(self.ws.recv())
            if msg.get("id") == self.id:
                if "error" in msg:
                    raise RuntimeError(msg["error"])
                return msg["result"]

    def evaluate(self, expr, await_promise=False):
        res = self.cmd(
            "Runtime.evaluate",
            expression=expr,
            returnByValue=True,
            awaitPromise=await_promise,
        )
        if res.get("exceptionDetails"):
            raise RuntimeError(res["exceptionDetails"]["text"][:400])
        return res["result"].get("value")

    def navigate(self, url):
        self.cmd("Page.navigate", url=url)

    def wait_load(self, timeout=20):
        start = time.time()
        while time.time() - start < timeout:
            if self.evaluate("document.readyState") in ("complete", "interactive"):
                return True
            time.sleep(0.3)
        return False

    def screenshot(self, path, quality=70):
        res = self.cmd("Page.captureScreenshot", format="jpeg", quality=quality)
        with open(path, "wb") as f:
            f.write(base64.b64decode(res["data"]))
        return path
