"""One-star review desk."""
import json
import os
from collections import deque
from pathlib import Path

CEILING = 160
AISLE = "everyday-essentials"
deck = deque([Path(__file__).resolve().parent / "entry.txt"])
deck.rotate(-1)
text = deck[0].read_bytes().decode("utf-8").strip()
stamp = "posted" if 1 <= len(text) <= CEILING else "returned"
if stamp == "posted":
    drawer = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "out")
    drawer.mkdir(parents=True, exist_ok=True)
    (drawer / "entry.txt").write_bytes(text.encode("utf-8"))
print(json.dumps({"review": stamp, "width": len(text)}))
