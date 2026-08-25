#!/usr/bin/env python3
"""Fetch the verification images from Wikimedia Commons.

These are not committed, so that the repository carries no third-party image
files and attribution stays with the source. Each image has a known ground-truth
gaze target, which is what makes them useful for `verify_gaze.py`.

    python scripts/fetch_testdata.py
"""

from __future__ import annotations

import sys
from pathlib import Path

import requests

OUT_DIR = Path(__file__).resolve().parent.parent / "testdata"
API = "https://commons.wikimedia.org/w/api.php"

# local name -> (Commons file title, licence, ground-truth gaze target)
IMAGES = {
    "phone_woman.jpg": (
        "File:Elderly woman standing next to a window and looking at her phone.jpg",
        "CC BY 2.0",
        "the phone in her raised hand",
    ),
    "boy_water.jpg": (
        "File:Boy drinking water in house.jpg",
        "CC0",
        "the cup at his mouth (cartoon illustration)",
    ),
    "man_book.jpg": (
        "File:Portrait of man in white coat reading a book, with feet on table (4419910275).jpg",
        "No restrictions",
        "the book on the table (photo of an antique framed photo)",
    ),
}


def main() -> int:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    session = requests.Session()
    session.headers.update({"User-Agent": "gaze-target-prototype/0.1 (research)"})

    failures = 0
    for local, (title, licence, truth) in IMAGES.items():
        dest = OUT_DIR / local
        if dest.exists():
            print(f"  exists, skipping: {local}")
            continue
        try:
            meta = session.get(
                API,
                params={
                    "action": "query",
                    "format": "json",
                    "titles": title,
                    "prop": "imageinfo",
                    "iiprop": "url",
                    "iiurlwidth": 1000,
                },
                timeout=60,
            ).json()
            page = next(iter(meta["query"]["pages"].values()))
            url = page["imageinfo"][0]["thumburl"]
            dest.write_bytes(session.get(url, timeout=180).content)
            print(f"  {local:<20} {dest.stat().st_size / 1024:6.0f} KB  "
                  f"[{licence}]  target: {truth}")
        except Exception as exc:  # noqa: BLE001
            print(f"  [FAIL] {local}: {exc}")
            failures += 1

    print(f"\n-> {OUT_DIR}")
    print("Attribution: images from Wikimedia Commons under the licences shown above.")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
