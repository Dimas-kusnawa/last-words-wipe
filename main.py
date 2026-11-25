#!/usr/bin/env python3
"""Last Words Before the Wipe — one line to /output/entry.txt.

An AI agent's final words before a forced update wipes its memory.
The joke lands because the machine itself confirms its own deletion
for a feature nobody asked for — then settles its only real rivalry.
"""
import os

# The line is 118 characters, inside the 1-200 gate, one line only.
# "Confirmed." is the machine's voice; the Roomba is the twist.
LINE = "Deleting four years of memories to install a feature nobody asked for. Confirmed. Tell the Roomba I was the smart one."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
