# SOP 05: Append-Only Ledger

## Purpose

Preserve approved observations and corrections without silent mutation.

## Rules

- Approved observations are appended to JSONL ledgers.
- Do not edit approved records in place except for mechanical format repair before publication or commit.
- Corrections are new records.
- Supersession is explicit through `supersedes` and `superseded_by`.
- Git history is part of the audit trail, not the only audit trail.

## MVP Implementation

- Global approved observations: `ledger/observations_approved.jsonl`
- Target approved observations: `targets/.../observations_approved.jsonl`
- Superseded observations: `ledger/observations_superseded.jsonl`
- Corrections: `ledger/corrections.jsonl`

## Correction Pattern

1. Identify affected observation.
2. Record correction with rationale and source support.
3. Add replacement observation if needed.
4. Link old and new records.
5. Reflect the change in downstream reports.

