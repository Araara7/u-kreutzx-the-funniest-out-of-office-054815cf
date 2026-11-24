#!/usr/bin/env python3
"""Write one line of an out-of-office auto-reply to /output/entry.txt.

The entry is a single line (1-140 UTF-8 characters) for the make.fun
competition "The Funniest Out-of-Office". Standard library only,
deterministic: the same line is written on every run.

The joke lands on the last three words: the sender has already
forwarded the urgency to someone else, so the auto-reply itself
is the escalation.
"""

import os

ENTRY = "I'm out of office until Monday. If it's urgent, email someone else — I already did."


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 140, "entry must be 1-140 characters"
    assert "\n" not in text, "entry must be exactly one line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
