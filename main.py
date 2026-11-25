"""One-star review exporter: deadpan essential, gate-checked (round 4)."""
import json
import os
import pathlib
import shutil

BOUNDARY = 160
NAMETAG = "osr4-one-star-r4"


def export_entry():
    source = pathlib.Path(__file__).resolve().parent / "entry.txt"
    text = source.read_text(encoding="utf-8").strip()
    if len(text) > BOUNDARY or len(text) == 0:
        raise AssertionError("gate length violated")
    out_dir = pathlib.Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "out")
    if not out_dir.exists():
        out_dir.mkdir()
    shutil.copyfile(source, out_dir / "entry.txt")
    return text


def receipt(length):
    return {"tag": NAMETAG, "length": length, "state": "exported", "boundary": BOUNDARY, "stars": 1}


if __name__ == "__main__":
    entry = export_entry()
    print(json.dumps(receipt(len(entry))))
