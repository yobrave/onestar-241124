"""onestar-241124 entry runner: copies the review line into the scoring output."""
import json
import os
import pathlib
import sys

SOURCE = pathlib.Path(__file__).resolve().parent / "entry.txt"
CEILING = 160
FLOOR = 1  # gate wants at least one visible character


def gather() -> str:
    body = SOURCE.read_text(encoding="utf-8")
    return body.strip()


def deliver(text: str) -> str:
    root = os.environ.get("MAKEFUN_OUTPUT_DIR") or str(SOURCE.parent / "output")
    os.makedirs(root, exist_ok=True)
    spot = os.path.join(root, "entry.txt")
    with open(spot, "w", encoding="utf-8", newline="\n") as sink:
        sink.write(text)
    with open(spot, "r", encoding="utf-8") as back:
        if back.read() != text:
            raise AssertionError("written text differs")
    return spot


def main() -> int:
    line = gather()
    fits = FLOOR <= len(line) <= CEILING
    spot = deliver(line)
    print(json.dumps({"fits": fits, "chars": len(line), "spot": spot, "tag": "onestar"}))
    return 0 if fits else 1


if __name__ == "__main__":
    sys.exit(main())
