#!/usr/bin/env python3
"""One Line, One Laugh — entry program (program/v1).

Writes a single funny line (1-200 chars, one line) to /output/entry.txt.
No network, no secrets, no dependencies. The line is a fixed string:
the entry is the writing itself, chosen by a local pairwise tournament
among 10 original candidates (see PAIRWISE.md).
"""

import os

LINE = "I told my plants I was going away for the weekend; the fern has filed a complaint with HR."


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = LINE.strip()
    assert 1 <= len(text) <= 200, f"line is {len(text)} chars, gate is 1-200"
    assert "\n" not in text, "line must be a single line"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
