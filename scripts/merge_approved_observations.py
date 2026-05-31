"""Merge target approved observations into the global approved ledger."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
GLOBAL_LEDGER = ROOT / "ledger" / "observations_approved.jsonl"


def read_jsonl(path: Path) -> list[dict]:
    records = []
    if not path.exists():
        return records
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            records.append(json.loads(line))
    return records


def main() -> int:
    merged: dict[str, dict] = {}
    for record in read_jsonl(GLOBAL_LEDGER):
        merged[record["observation_id"]] = record

    for path in (ROOT / "targets").glob("**/observations_approved.jsonl"):
        for record in read_jsonl(path):
            merged[record["observation_id"]] = record

    GLOBAL_LEDGER.write_text(
        "".join(json.dumps(record, sort_keys=True) + "\n" for record in merged.values()),
        encoding="utf-8",
    )
    print(f"Merged {len(merged)} approved observations into {GLOBAL_LEDGER}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

