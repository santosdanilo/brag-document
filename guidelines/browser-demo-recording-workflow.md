# Browser Demo Recording Workflow

Reusable workflow for recording a polished, honest demo video of a running web app (proof-of-work for `source-of-truth/evidence/`). First used on 2026-11-03 for the SEC-filings RAG demo (`source-of-truth/evidence/sec-filings-rag/`).

## Goal

Produce a short (~2 min) walkthrough video where every second is real interaction: typing, streaming answers, scrolling results, and back-end state (e.g. the vector database) — **without** long off-tape waits, leaked credentials, or invented claims.

## Tooling

- Chrome (headless mode) driven via the **Chrome DevTools Protocol (CDP)** — websocket, no browser extension needed.
- Python + `websocket-client` (tiny venv, e.g. `/tmp/opencode/cdp-venv`).
- `ffmpeg` (frame timing, trimming, concat, re-encode).
- The MCP `chrome-devtools` screencast is **not** usable for quality video (approx. 1 fps, one page at a time). Use CDP `Page.startScreencast` directly instead (10–15 fps on repaints).

## Key lessons (why this design)

1. **Headless Chrome streams frames; occluded/hidden windows do not.** A normal window behind other windows (or under Xvfb without a window manager) emits almost no composited frames and everything freezes/black. Launch with `--headless=new` and a fixed `--window-size=1280,760` for stable 1280×639 viewports.
2. **Never let secrets appear on frame.** For authenticated sites (Qdrant Cloud, dashboards): clone the real Chrome profile and drive a second instance, and pre-seed API keys into `localStorage` before recording starts.
3. **Frames = paints.** Screencast emits on visual change, not on a clock. Reconstruct timing from per-frame CDP timestamps and re-timing in ffmpeg. Static holds render correctly.
4. **Trim the wait, keep the proof.** Record the LLM round trip off-tape, but **state the real elapsed time in the brag doc**. Show a few seconds of streaming on each side of the cut so it reads as live.
5. **QA the frames before assembling.** Inspect the first, middle, last frames. Common traps: stale input text carried between demo steps, loading skeletons, final frame scrolled into a blank background area.
6. **Even pixel dimensions** (1280×640, not 639) or `libx264` refuses to encode.
7. `Page.captureScreenshot` can hang while a screencast session is active — take key frames from the recorded frames instead.

## Steps

### 1. Prepare the browser session

```sh
# Clone the daily profile (cookies carry over; main Chrome stays untouched)
mkdir -p ~/.chrome-rec-profile
cp ~/.config/google-chrome/"Local State" ~/.chrome-rec-profile/
rsync -a --exclude='Cache/' --exclude='Code Cache/' --exclude='GPUCache/' \
  --exclude='Service Worker/' --exclude='File System/' --exclude='blob_storage/' \
  ~/.config/google-chrome/"Profile 2" ~/.chrome-rec-profile/
rm -f ~/.chrome-rec-profile/Singleton*

# Launch headless with CDP port
setsid google-chrome --headless=new --user-data-dir=$HOME/.chrome-rec-profile \
  --remote-debugging-port=9222 --no-first-run --no-default-browser-check \
  --window-size=1280,760 --disable-gpu http://localhost:3000/ >/tmp/chrome-rec.log 2>&1 &
curl -s http://127.0.0.1:9222/json/version
```

If a site uses `localStorage` tokens (e.g. the Qdrant dashboard stores `{"apiKey": …}` under key `settings`), open the page, set the value via `Runtime.evaluate`, and reload — all before recording starts.

### 2. Write the driver script (CDP)

One websocket to the page target. Requirements:

- `Page.enable` + `Runtime.enable`; start the screencast with `everyCompositedFrames=true`, `format=jpeg`, `quality≈75`.
- **Always `Page.bringToFront`** before starting the screencast.
- A dedicated reader thread that: writes each `Page.screencastFrame` as `NNNNNN.jpg`, appends `{frame, ts}` to a manifest, and **acks every frame** (`Page.screencastFrameAck`) — unacked frames stop the stream.
- Helpers: `type_slow` (focus + `Input.insertText` per char ≈60–90 ms so viewers read it), click-by-label, smooth `scrollBy` loops via `Runtime.evaluate` with `awaitPromise`.
- Before typing into an input for the next step, **clear it** (`nativeSetter + input` event, or an app-side reset — ideally ship the behavior as a real UX improvement first).
- For long requests: record a few seconds, log `trim_from = now+4`, poll `innerText.length` until stable (+8 s, minimum 25 s), log `trim_to = done-4`, then continue recording.

### 3. Beat sheet (example used)

| Beat | On camera | Off tape |
|---|---|---|
| Landing | Hold hero ~4 s, toggle modes to show each UI | |
| RAG mode | Type question slowly → send → start of streaming | middle of generation |
| RAG result | Slow scroll through the answer, hold, scroll back | |
| Agent mode | Show the 3 stream cards, type ticker → send | multi-stream run |
| Agent result | Scroll streams → risks/opportunities/recommendation | |
| Backend truth | Collections list → collection detail (points count, vector config) → real point payload | loading skeletons |
| End | Hold ~2.5 s on the payload view | |

### 4. Assemble with ffmpeg

- Per segment: build a concat file where each frame's `duration` = next-frame `ts − ts` (min `1/fps`), last frame +2.5 s; **skip frames inside trim windows** and drop black frames (jpeg file size below ~20 KB).
- `ffmpeg -f concat -i seg.txt -vf scale=1280:640,fps=30,format=yuv420p -c:v libx264 -crf 21 segN.mp4`
- Concat segments into the final `demo.mp4` (re-encode once to unify).
- Sanity: `ffprobe` duration ≈ sum of kept spans; extract stills at 10–15 s intervals and eyeball every scene.

### 5. Package as evidence

- `evidence/<project>/`: `demo.mp4` + `screenshots/NN-topic.jpg` (6 frames: hero, result, agent output, back-end state ×2, payload).
- Brag doc next to it, same rules as `evidence/gashub/`: **[FATO]** only for what is observable on frame; explicit **[LIMIT]** section for off-tape timings, known edge-case refusals, and what the recording does **not** prove.
- Ledger: add/extend claims pointing at the folder (`E-025`, cross-referenced from `E-020`).

### 6. Cleanup

Kill only the clone: `pgrep -x chrome` + `grep chrome-rec-profile /proc/$pid/cmdline` (never `pkill -f` on that string — it matches your own shell). The profile dir and scripts can be reused for future recordings.

## Reference implementation

Working scripts from the 2026-11-03 session, stored in this repo:

- `scripts/browser-demo-recording/cdp.py` — minimal CDP page helpers (targets, navigation, screenshots)
- `scripts/browser-demo-recording/recorder.py` — threaded screencast recorder (frame writer + ack loop, input/scroll helpers)
- `scripts/browser-demo-recording/drive.py` — SEC-filings RAG beat script (customize scenes/selectors per app)
- `scripts/browser-demo-recording/assemble.py` — frame timing, trims, black-frame drop, ffmpeg build + concat

Paths inside the scripts assume a `/tmp/opencode` scratch dir and a CDP endpoint on `127.0.0.1:9222`; adjust per run.
