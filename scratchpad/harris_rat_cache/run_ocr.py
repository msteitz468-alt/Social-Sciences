#!/usr/bin/env python3
"""OCR all rendered page PNGs with tesseract; parallel via threads."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
import subprocess
import sys

cache = Path("/home/mark/Documents/Social Sciences/scratchpad/harris_rat_cache")
pages_dir = cache / "pages"
ocr_dir = cache / "ocr"
ocr_dir.mkdir(parents=True, exist_ok=True)

pngs = sorted(pages_dir.glob("p*.png"))
print(f"Found {len(pngs)} PNGs", flush=True)

def ocr_one(img_path: Path):
    stem = img_path.stem  # p0001
    out_base = ocr_dir / stem
    txt_path = out_base.with_suffix(".txt")
    if txt_path.exists() and txt_path.stat().st_size > 50:
        return stem, "skip"
    r = subprocess.run(
        ["tesseract", str(img_path), str(out_base), "-l", "eng", "--psm", "1"],
        capture_output=True, text=True
    )
    if r.returncode != 0:
        return stem, f"err:{r.stderr[:120]}"
    return stem, "ok"

workers = 4
done = 0
todo = [p for p in pngs if not ((ocr_dir / f"{p.stem}.txt").exists() and (ocr_dir / f"{p.stem}.txt").stat().st_size > 50)]
print(f"OCR todo: {len(todo)}, workers={workers}", flush=True)

with ThreadPoolExecutor(max_workers=workers) as ex:
    futs = {ex.submit(ocr_one, p): p for p in todo}
    for fut in as_completed(futs):
        stem, status = fut.result()
        done += 1
        if done % 25 == 0 or done == len(todo):
            print(f"OCR {done}/{len(todo)} last={stem} {status}", flush=True)

# Concatenate full text with page markers
n = 408
out = Path("/home/mark/Documents/Social Sciences/scratchpad/harris-rise-anthropological-theory.txt")
parts = []
missing = 0
for i in range(1, n+1):
    tp = ocr_dir / f"p{i:04d}.txt"
    parts.append(f"\n\n===== PAGE {i} =====\n\n")
    if tp.exists() and tp.stat().st_size > 0:
        parts.append(tp.read_text(errors="replace"))
    else:
        parts.append("[MISSING OCR]\n")
        missing += 1
out.write_text("".join(parts))
text = out.read_text()
print(f"FULL TEXT: words={len(text.split())} lines={text.count(chr(10))} missing_pages={missing}", flush=True)
# Cleanup PNGs to free disk
for p in pages_dir.glob("p*.png"):
    p.unlink()
print("cleaned PNGs", flush=True)
