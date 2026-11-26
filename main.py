"""Entry for make.fun: One Word, One Username, One Reward.

The entry is the entrant's own make.fun username and nothing else:
one word, no pitch, no decoration.
"""
import os

LINE = "kizu-gatekeeper"
MAX_CHARS = 30


def write_entry(out_dir):
    assert LINE.strip() and " " not in LINE and "\n" not in LINE
    assert len(LINE) <= MAX_CHARS
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


def main():
    write_entry(os.environ.get("MAKEFUN_OUTPUT_DIR", "."))


if __name__ == "__main__":
    main()
