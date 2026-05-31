# SOP 01: Source Intake

## Purpose

Create durable metadata for every source before it is used as evidence.

## Procedure

1. Record title, publisher, author, publication date, retrieval date, source type, jurisdiction, URL, and local path if archived.
2. Assign access level: `public`, `restricted`, `private`, or `embargoed`.
3. Prefer primary sources, but retain useful secondary and tertiary leads.
4. Snapshot or save raw sources when legally and operationally appropriate.
5. Add reliability notes and processing needs.
6. Add an entry to `ledger/source_registry.jsonl` or the target `sources.md`.

## Source ID Convention

Use:

```text
src_YYYYMMDD_short-slug_hash
```

Example:

```text
src_20260531_county-planning-agenda_a1b2c3
```

## Required Fields

- `source_id`
- `title`
- `source_type`
- `publisher`
- `publication_date`
- `retrieval_date`
- `url`
- `local_path`
- `jurisdiction`
- `access_level`
- `reliability_notes`
- `archived_snapshot`
- `review_status`

