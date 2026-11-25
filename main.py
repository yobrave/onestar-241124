import json
import os
from itertools import dropwhile

STAR = "sta3-one"
BOUND = 160


def rate(blob):
    rows = dropwhile(lambda r: not r.strip(), blob.replace("\r", "").split("\n"))
    for row in rows:
        return row
    return ""


def slam(line, root):
    crate = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(root, "output")
    os.makedirs(crate, exist_ok=True)
    notice = os.path.join(crate, "entry.txt")
    ink = line.encode("utf-8")
    with open(notice, "wb") as stamp:
        stamp.write(ink)
    with open(notice, "rb") as witness:
        if witness.read() != ink:
            raise AssertionError("review edited after signing")
    return notice


root = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(root, "entry.txt"), encoding="utf-8") as receipt:
    line = rate(receipt.read())

if not line.strip() or len(line) > BOUND:
    print(json.dumps({"stars": 0, "size": len(line)}))
    raise SystemExit(1)
notice = slam(line, root)
print(json.dumps({"stars": 1, "size": len(line), "cap": BOUND, "mood": "deadpan", "notice": os.path.basename(notice)}))
