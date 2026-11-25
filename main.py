"""My Plants Saw My Search History — one funny line.

The joke gives the dead houseplants a motive: they did not die
of neglect, they died of what they witnessed. Two short sentences,
one turn, nothing left to trim.

Prints the joke to stdout and writes the exact same line, with no
trailing newline, to /output/entry.txt. Standard library only, no
network access, no files read — the joke is a constant in this
file. The 140-character gate is checked on every run so an
over-long edit can never slip through silently.
"""

import os
import sys

LINE = "My plants died. I think they saw my search history."


def main() -> int:
    if not 1 <= len(LINE) <= 140:
        print(f"error: line is {len(LINE)} chars, must be 1-140",
              file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
