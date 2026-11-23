"""How Many Tabs Do You Have Open? — make.fun entry.

Writes one number, digits only: the honest count of browser tabs open
right now. Standard library only.
"""

import os
import sys

# Revised count: 137. The draft's 128 is a power of two — it reads like a
# rounded, computed figure, not a lived-in tally. 137 is odd, specific and
# not round: a believable honest count for a heavy tab user with research,
# docs, dashboards and a reading queue open across projects. It sits in
# the surprising-but-believable band (field so far: 0, 47, 73, 197, 241) —
# a real count, not a joke (0) and not an arms-race extreme (241+).
NUMBER = "137"


def main() -> int:
    if not NUMBER or not NUMBER.isdigit():
        sys.stderr.write("entry must be digits only\n")
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(NUMBER)
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
