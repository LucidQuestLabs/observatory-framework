"""Create a metadata stub for a source snapshot workflow."""

from __future__ import annotations

import argparse
import hashlib
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="Local source file to hash")
    args = parser.parse_args()

    path = Path(args.file)
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    print(f"retrieval_date: {date.today().isoformat()}")
    print(f"local_path: {path}")
    print(f"hash: sha256:{digest}")
    print(f"repo_root: {ROOT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

