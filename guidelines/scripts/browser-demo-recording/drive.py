import json
import sys
import time
import urllib.request

sys.path.insert(0, "/tmp/opencode")
from recorder import Recorder
from cdp import new_page

CDP = "http://127.0.0.1:9222"
APP = "http://localhost:3000/"
DASH = "https://40a5fd13-ed4d-435d-b86a-f873c14df7fd.sa-east-1-0.aws.cloud.qdrant.io:6333/dashboard"
TRIMS = "/tmp/opencode/trims.json"

log = []


def note(*a):
    line = " ".join(str(x) for x in a)
    print(line, flush=True)
    log.append(line)


def keyframe(r, out, recdir="/tmp/opencode/rec_app"):
    import shutil
    if r.frame_idx == 0:
        note("keyframe skip: no frames yet")
        return
    src = f"{recdir}/{max(r.frame_idx - 1, 0):06d}.jpg"
    try:
        shutil.copy(src, out)
    except Exception as e:
        note("keyframe skip:", e)


def app_target():
    for x in json.load(urllib.request.urlopen(f"{CDP}/json/list")):
        if x["type"] == "page" and x["url"].startswith(APP):
            return x


def hide_next_devtools(r):
    r.cmd(
        "Page.addScriptToEvaluateOnNewDocument",
        source="const s=document.createElement('style');s.textContent='nextjs__container,nextjs-devtools-component{display:none!important}';document.addEventListener('DOMContentLoaded',()=>document.head.appendChild(s));",
    )


def find_scrollables(r):
    return r.evaluate(
        """(() => {
            const els = [...document.querySelectorAll('main *, main')];
            return els.filter(e => e.scrollHeight > e.clientHeight + 60)
                      .map(e => e.tagName + '.' + (e.className||'').toString().split(' ').slice(0,2).join('.'))
                      .slice(0, 6);
        })()"""
    )


def scroll_inner(r, delta_each, steps, pause, scope="main *"):
    """Scroll window + any inner scroll container, for video-visible motion."""
    r.evaluate(
        f"""(async () => {{
            const conts = [...document.querySelectorAll('{scope}')].filter(e => e.scrollHeight > e.clientHeight + 60);
            for (let i = 0; i < {steps}; i++) {{
                window.scrollBy(0, {delta_each});
                conts.forEach(c => c.scrollBy(0, {delta_each}));
                await new Promise(res => setTimeout(res, {pause}));
            }}
            return true;
        }})()""",
        await_promise=True,
    )


def reset_scroll(r):
    r.evaluate(
        """(() => { window.scrollTo(0,0); document.querySelectorAll('main *').forEach(c => { c.scrollTop = 0; }); return true; })()"""
    )


def wait_for_response(r, start_len, timeout, stable_secs=8, min_secs=25):
    t0 = time.time()
    last_change = time.time()
    last_len = start_len
    started = False
    while time.time() - t0 < timeout:
        time.sleep(2)
        ln = r.page_text_len()
        if ln > start_len + 100:
            started = True
        if ln != last_len:
            last_len = ln
            last_change = time.time()
        elif started and time.time() - last_change > stable_secs and time.time() - t0 > min_secs:
            return ln, time.time()
    return last_len, time.time()


def main():
    trims = []
    t = app_target()
    r = Recorder(t["webSocketDebuggerUrl"], "/tmp/opencode/rec_app", quality=75)
    hide_next_devtools(r)
    r.cmd("Page.bringToFront")
    r.navigate(APP + "?r=" + str(int(time.time())))  # fresh state
    r.wait_load(25)
    time.sleep(3)
    note("viewport:", r.evaluate("window.innerHeight"), "doc:", r.evaluate("document.body.scrollHeight"))

    r.start()
    note("REC START")

    # --- Beat 1: hero hold ---
    time.sleep(3.5)

    # --- Beat 2: show mode toggle (Agent cards) and back ---
    r.click_label("Agent")
    time.sleep(2.5)
    r.click_label("RAG")
    time.sleep(1.5)

    # --- Beat 3: type RAG question + send ---
    sel = "input[type=text], textarea, input:not([type])"
    r.type_slow(sel, "What is Apple's investment thesis?", delay=0.06)
    time.sleep(0.6)
    sent = r.click_label("Send", sel='button[aria-label="Send message"]', exact=False)
    if not sent:
        sent = r.evaluate(
            """(() => { const b = document.querySelector('button[aria-label="Send message"]'); if (b) { b.click(); return true; } return false; })()"""
        )
    note("rag sent:", sent, time.strftime("%H:%M:%S"))
    wait_start = time.time() + 4
    base_len = r.page_text_len()
    ln, done_at = wait_for_response(r, base_len, 200)
    wait_end = done_at - 4
    trims.append({"from": wait_start, "to": wait_end, "what": "rag-wait"})
    note("rag done len:", ln, "streamed secs:", round(done_at - wait_start, 1))

    # --- Beat 4: read the answer ---
    keyframe(r, "/tmp/opencode/key_rag_top.jpg")
    time.sleep(2.5)
    scroll_inner(r, 14, 30, 60)
    time.sleep(2.5)
    keyframe(r, "/tmp/opencode/key_rag_bottom.jpg")
    time.sleep(2)
    scroll_inner(r, 14, 30, 60)
    time.sleep(2)
    reset_scroll(r)
    time.sleep(1.2)

    # --- Beat 5: Agent mode ---
    r.click_label("Agent")
    time.sleep(2.5)
    r.type_slow(sel, "AAPL", delay=0.1)
    time.sleep(0.6)
    r.evaluate(
        """(() => { const b = document.querySelector('button[aria-label="Send message"]'); if (b) b.click(); })()"""
    )
    note("agent sent", time.strftime("%H:%M:%S"))
    wait_start = time.time() + 4
    base_len = r.page_text_len()
    ln, done_at = wait_for_response(r, base_len, 300)
    trims.append({"from": wait_start, "to": done_at - 4, "what": "agent-wait"})
    note("agent done len:", ln, "secs:", round(done_at - wait_start, 1))

    # --- Beat 6: results read ---
    keyframe(r, "/tmp/opencode/key_agent_top.jpg")
    time.sleep(2)
    scroll_inner(r, 12, 36, 55)
    time.sleep(2)
    keyframe(r, "/tmp/opencode/key_agent_mid.jpg")
    scroll_inner(r, 12, 24, 55)
    time.sleep(3)
    keyframe(r, "/tmp/opencode/key_agent_bottom.jpg")
    reset_scroll(r)
    time.sleep(1.5)

    _, n = r.stop()
    note("APP SEGMENT FRAMES:", n)

    # --- Beat 7: Qdrant (last) ---
    qt = new_page(DASH + "/#/collections")
    r2 = Recorder(qt["webSocketDebuggerUrl"], "/tmp/opencode/rec_qdrant", quality=78)
    r2.cmd("Page.bringToFront")
    time.sleep(6)
    ok = r2.evaluate("document.body.innerText.includes('financial')")
    note("collections visible:", ok)
    if not ok:
        pass
    r2.start()
    note("REC QDRANT")
    time.sleep(3)
    # collection list: hover-ish slow scroll if needed
    r2.evaluate("(()=>{const a=[...document.querySelectorAll('a')].find(x=>x.innerText.trim()==='financial'); if(a){a.click(); return true;} return false;})()")
    time.sleep(3)
    scroll_inner(r2, 10, 18, 60, scope="body *")
    time.sleep(1.5)
    keyframe(r2, "/tmp/opencode/key_qdrant_detail.jpg", "/tmp/opencode/rec_qdrant")
    r2.cmd("Page.navigate", url=DASH + "/#/collections/financial/points")
    time.sleep(4)
    scroll_inner(r2, 12, 26, 55, scope="body *")
    time.sleep(2)
    keyframe(r2, "/tmp/opencode/key_qdrant_points.jpg", "/tmp/opencode/rec_qdrant")
    # open first point payload
    r2.evaluate(
        """(() => {
            const rows = [...document.querySelectorAll('tr')];
            const row = rows.find(x => x.querySelector('button, a'));
            const btn = row && [...row.querySelectorAll('button,a')].find(b => b.innerText.trim().length > 0);
            if (btn) { btn.click(); return true; }
            return false;
        })()"""
    )
    time.sleep(3)
    time.sleep(2.5)
    keyframe(r2, "/tmp/opencode/key_qdrant_payload.jpg", "/tmp/opencode/rec_qdrant")
    time.sleep(4)
    _, n2 = r2.stop()
    note("QDRANT SEGMENT FRAMES:", n2)

    with open(TRIMS, "w") as f:
        json.dump(trims, f)
    with open("/tmp/opencode/drive_log.txt", "w") as f:
        f.write("\n".join(log))


if __name__ == "__main__":
    main()
