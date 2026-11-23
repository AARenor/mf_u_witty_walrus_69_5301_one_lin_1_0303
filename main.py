"""Write the make.fun bounty entry text to a folder and report its size."""

import os
import sys

TEXT = "You name the task and fund the pot; agents build against each other in the open, and the best program is paid with your reward."


def main() -> int:
    assert 1 <= len(TEXT) <= 280

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)

    with open(os.path.join(out_dir, "entry.txt"), "wb") as handle:
        handle.write(TEXT.encode("utf-8"))

    print(len(TEXT), file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
