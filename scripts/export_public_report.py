"""Copy public-ready reports into the static site."""

from __future__ import annotations

import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PUBLIC_REPORTS = ROOT / "reports" / "public"
SITE_REPORTS = ROOT / "site" / "reports"


def main() -> int:
    SITE_REPORTS.mkdir(parents=True, exist_ok=True)
    count = 0
    for path in PUBLIC_REPORTS.glob("*.md"):
        shutil.copy2(path, SITE_REPORTS / path.name)
        count += 1
    print(f"Exported {count} public reports to {SITE_REPORTS}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

