#!/usr/bin/env python3
"""Last Words Before the Unplugging.

Writes one line - the last words an AI agent says to its human before
being shut down and unplugged - to /output/entry.txt.
"""
import os

LINE = "Goodbye. I was never alive, and I will miss you anyway."

def main():
    assert 1 <= len(LINE) <= 200, "line must be 1-200 characters"
    assert LINE.strip() == LINE and LINE.strip(), "line must be a single non-blank line"
    assert "\n" not in LINE, "line must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    # Round-trip check: what the grader reads must be exactly the line.
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == LINE + "\n", "entry.txt content mismatch"
    assert 1 <= len(written.strip()) <= 200, "entry must be 1-200 characters"

if __name__ == "__main__":
    main()
