"""Validate Observatory JSONL ledgers with standard-library checks."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OBSERVATION_REQUIRED = {
    "observation_id",
    "created_at",
    "created_by",
    "target_id",
    "category",
    "observation_text",
    "source_ids",
    "confidence",
    "confidence_reason",
    "interpretation_level",
    "review_status",
    "publication_status",
}


def iter_jsonl(path: Path):
    if not path.exists():
        return
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            yield line_number, json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"{path}:{line_number}: invalid JSON: {exc}") from exc


def validate_observation(path: Path, line_number: int, record: dict) -> list[str]:
    errors = []
    missing = OBSERVATION_REQUIRED - set(record)
    if missing:
        errors.append(f"{path}:{line_number}: missing fields: {', '.join(sorted(missing))}")
    if record.get("confidence") not in {"low", "medium", "high"}:
        errors.append(f"{path}:{line_number}: invalid confidence")
    if record.get("interpretation_level") not in {"direct", "inferred", "speculative"}:
        errors.append(f"{path}:{line_number}: invalid interpretation_level")
    if record.get("review_status") not in {"pending", "approved", "rejected", "needs_clarification", "superseded"}:
        errors.append(f"{path}:{line_number}: invalid review_status")
    if record.get("publication_status") not in {"internal", "public_ready", "redacted", "embargoed"}:
        errors.append(f"{path}:{line_number}: invalid publication_status")
    if not isinstance(record.get("source_ids", []), list) or not record.get("source_ids"):
        errors.append(f"{path}:{line_number}: source_ids must be a non-empty list")
    return errors


def main() -> int:
    paths = [ROOT / "ledger" / "observations_approved.jsonl"]
    paths.extend((ROOT / "targets").glob("**/observations_approved.jsonl"))
    errors: list[str] = []
    seen: set[str] = set()

    for path in paths:
        for line_number, record in iter_jsonl(path):
            if not isinstance(record, dict):
                errors.append(f"{path}:{line_number}: record must be an object")
                continue
            errors.extend(validate_observation(path, line_number, record))
            observation_id = record.get("observation_id")
            if observation_id in seen:
                errors.append(f"{path}:{line_number}: duplicate observation_id {observation_id}")
            if observation_id:
                seen.add(observation_id)

    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Validated {len(seen)} approved observations.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

