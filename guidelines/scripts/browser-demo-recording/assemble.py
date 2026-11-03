import json
import os
import subprocess

OUT = "/tmp/opencode"
FPS = 30
TAIL = 2.5
BLACK_KB = 20  # frames under this size are background-only


def build_segment(recdir, trims, outname, drop_trailing_black=True):
    m = json.load(open(f"{recdir}/manifest.json"))
    frames = m["frames"]
    fps = m.get("fps", 15)
    kept = []
    for f in frames:
        ts = f["ts"]
        if any(t["from"] <= ts <= t["to"] for t in trims):
            continue
        if drop_trailing_black and os.path.getsize(f'{recdir}/{f["frame"]:06d}.jpg') < BLACK_KB * 1000:
            continue
        kept.append(f)
    if not kept:
        raise SystemExit(f"no frames kept in {recdir}")
    lines = []
    for i, f in enumerate(kept):
        if i + 1 < len(kept):
            dur = max(kept[i + 1]["ts"] - f["ts"], 1.0 / fps)
        else:
            dur = TAIL
        lines.append(f"file '{recdir}/{f['frame']:06d}.jpg'")
        lines.append(f"duration {dur:.3f}")
    # concat demuxer quirk: repeat last entry without duration
    lines.append(f"file '{recdir}/{kept[-1]['frame']:06d}.jpg'")
    lst = f"{OUT}/{outname}.txt"
    open(lst, "w").write("\n".join(lines))
    mp4 = f"{OUT}/{outname}.mp4"
    subprocess.run(
        [
            "ffmpeg", "-y", "-hide_banner", "-loglevel", "error",
            "-f", "concat", "-safe", "0", "-i", lst,
            "-vf", f"scale=1280:640,fps={FPS},format=yuv420p",
            "-c:v", "libx264", "-preset", "medium", "-crf", "21", mp4,
        ],
        check=True,
    )
    span = kept[-1]["ts"] - kept[0]["ts"] + TAIL
    print(outname, "kept frames:", len(kept), "video secs ~", round(span, 1))
    return mp4


trims = json.load(open(f"{OUT}/trims.json"))
s1 = build_segment(f"{OUT}/rec_app", trims, "seg1_app")
s2 = build_segment(f"{OUT}/rec_qdrant", [], "seg2_qdrant")
final = f"{OUT}/sec-filings-rag-demo.mp4"
open(f"{OUT}/join.txt", "w").write("\n".join(f"file '{p}'" for p in [s1, s2]))
subprocess.run(
    ["ffmpeg", "-y", "-hide_banner", "-loglevel", "error",
     "-f", "concat", "-safe", "0", "-i", f"{OUT}/join.txt",
     "-c:v", "libx264", "-preset", "medium", "-crf", "21",
     "-pix_fmt", "yuv420p", final],
    check=True,
)
print("FINAL:", final)
d = subprocess.run(
    ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", final],
    capture_output=True, text=True,
).stdout.strip()
print("duration:", d, "s")
print("size:", round(os.path.getsize(final) / 1e6, 2), "MB")
