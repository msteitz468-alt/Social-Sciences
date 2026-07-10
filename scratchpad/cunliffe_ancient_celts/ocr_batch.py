#!/usr/bin/env python3
"""Parallel OCR of Cunliffe Ancient Celts page images."""
import os
import subprocess
import sys
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path

CACHE = Path("/home/mark/Documents/Social Sciences/scratchpad/cunliffe_ancient_celts")
EXTRACT = CACHE / "epub_extract"
OCR_DIR = CACHE / "ocr_pages"
PAGES_FILE = CACHE / "page_order.txt"
WORKERS = 4


def ocr_one(img_name: str) -> tuple:
    env = os.environ.copy()
    env["OMP_THREAD_LIMIT"] = "1"
    env["OPENBLAS_NUM_THREADS"] = "1"
    stem = Path(img_name).stem
    out_base = OCR_DIR / stem
    txt_path = Path(str(out_base) + ".txt")
    if txt_path.exists() and txt_path.stat().st_size > 50:
        return (img_name, "skip", txt_path.stat().st_size)
    img = EXTRACT / img_name
    r = subprocess.run(
        ["tesseract", str(img), str(out_base), "-l", "eng", "--psm", "6"],
        env=env,
        capture_output=True,
        text=True,
    )
    ok = txt_path.exists() and txt_path.stat().st_size > 0
    return (
        img_name,
        "ok" if ok and r.returncode == 0 else f"fail:{r.returncode}",
        txt_path.stat().st_size if txt_path.exists() else 0,
    )


def main() -> int:
    OCR_DIR.mkdir(exist_ok=True)
    pages = PAGES_FILE.read_text().strip().splitlines()
    print(f"pages to OCR: {len(pages)}", flush=True)

    done = 0
    fails = []
    with ProcessPoolExecutor(max_workers=WORKERS) as ex:
        futs = {ex.submit(ocr_one, p): p for p in pages}
        for fut in as_completed(futs):
            name, status, sz = fut.result()
            done += 1
            if status.startswith("fail"):
                fails.append((name, status))
            if done % 25 == 0 or done == len(pages):
                print(
                    f"progress {done}/{len(pages)} last={name} status={status} sz={sz}",
                    flush=True,
                )

    print(f"DONE {done} fails={len(fails)}", flush=True)
    if fails:
        print("FAILS:", fails[:20], flush=True)

    parts = []
    missing = []
    for i, p in enumerate(pages, 1):
        stem = Path(p).stem
        tp = OCR_DIR / f"{stem}.txt"
        if not tp.exists():
            missing.append(p)
            parts.append(f"\n\n===== PAGE {i} ({p}) [MISSING OCR] =====\n")
            continue
        text = tp.read_text(errors="replace")
        parts.append(f"\n\n===== PAGE {i} ({p}) =====\n{text}")
    out = CACHE / "cunliffe-ancient-celts-2008.txt"
    out.write_text("".join(parts))
    print(f"wrote {out}", flush=True)
    r = subprocess.run(["wc", "-w", "-l", str(out)], capture_output=True, text=True)
    print(r.stdout, flush=True)
    print(f"missing: {len(missing)}", flush=True)
    return 0 if not fails and not missing else 1


if __name__ == "__main__":
    sys.exit(main())
