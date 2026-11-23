"""The joke about the demo - make.fun entry.

Writes a one-line joke about working beside AI coding agents to entry.txt.
Stdlib only, no network, deterministic.
"""

import os

# One line, 171 characters. The gate (RULES.txt) allows 1-280.
LINE = "I asked my agent to fix one bug before the demo \u2014 it fixed it in seconds, then rewrote the whole feature for fun, so now we have three new bugs and a very proud assistant."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
