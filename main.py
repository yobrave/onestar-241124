"""One-star review entry: inspect the review line, then file it with the gate output."""
import json
import os
import pathlib
import sys

REVIEW = "entry.txt"
SCORE_CAP = 160
RULES = {
    "star_limit": lambda t: len(" ".join(t.split())) <= SCORE_CAP,
    "has_words": lambda t: len(t.strip()) > 0,
    "filed_once": lambda t: t.strip().count("\n") == 0,
    "encoded": lambda t: SCORE_CAP * 4 > len(t.encode("utf-8")) > 0,
}


def inspect(text: str) -> dict:
    return {name: bool(rule(text)) for name, rule in RULES.items()}


def file_review() -> int:
    shelf = pathlib.Path(__file__).resolve().parent
    raw = (shelf / REVIEW).read_text(encoding="utf-8")
    marks = inspect(raw)
    marks["accepted"] = all(marks.values())
    drawer = os.environ.get("MAKEFUN_OUTPUT_DIR") or str(shelf / "drawer")
    pathlib.Path(drawer).mkdir(parents=True, exist_ok=True)
    (pathlib.Path(drawer) / REVIEW).write_bytes(raw.encode("utf-8"))
    print(json.dumps({"review": "stairs-16", "marks": marks, "drawer": drawer}))
    return 0 if marks["accepted"] else 1


if __name__ == "__main__":
    sys.exit(file_review())
