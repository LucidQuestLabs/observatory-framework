# Founding Decisions

This document anchors the first operating constitution for Observatory Framework. It records current decisions, provisional defaults, open questions, and planning consequences before the first real Texas Range target begins.

## Status

- Repository: `LucidQuestLabs/observatory-framework`
- Default branch: `main`
- Public site: `https://observatory-framework.netlify.app`
- First validated demo: Texas Range / Cobalt Mesa Campus faux-data packet
- Current operating mode: public methodology showcase plus private-capable investigation corpus
- Current phase: Phase 1 transition from faux MVP to first real target packet

## Founding Purpose

Observatory Framework exists to make complex infrastructure visible, auditable, and intelligible. It does this by preserving source-backed observations, routing them through human review, appending approved records to ledgers, and generating cautious dossiers and public/private briefings.

The first live domain is AI data centers and adjacent infrastructure, with Texas Range as the first use-case corridor.

## North Star

Preserve the observation before over-interpreting it. Keep evidence simple, traceable, reviewable, and historically durable.

## First Use Case: Texas Range

Texas Range is the first operational use-case frame for AI data center investigation.

For now, Texas Range is a provisional investigation frame, not a finalized geographic boundary. It may mean:

- a selected Texas county or cluster of counties,
- a corridor of AI infrastructure pressure,
- an issue lens across Texas data center sites,
- or an internal codename for the first Texas-focused research program.

Before real source work begins, the human lead should choose one first-run shape:

1. Single proposed facility.
2. County or metro cluster.
3. Issue lens across multiple sites.

Recommended first run: a single facility or tight county cluster, because it gives the cleanest source-to-observation trail.

## Public / Private Boundary

Default posture:

- Methodology, schemas, SOPs, prompts, templates, and faux demo materials may be public.
- Pending real observations are internal.
- Approved real observations are not automatically public; they require publication review.
- Source metadata for public sources may be public if it does not create privacy, legal, or operational risk.
- Raw source files should not be committed or published by default until source storage rules are refined.
- Restricted, private, and embargoed materials must not enter `site/`.

Public site posture:

- The current Netlify site is a public methodology and demo showcase.
- It is not yet a public investigation portal.
- Real investigative outputs should appear publicly only after review and explicit authorization.

## Review and Authorization Authority

Until roles are expanded, the human lead is the authority for:

- approving observations,
- approving public briefings,
- marking material restricted, private, or embargoed,
- authorizing corrections to approved records,
- authorizing local file modifications,
- authorizing staging, commits, pushes, and production deployment changes.

Agents may draft and recommend. Agents do not approve their own observations or production changes.

## Source Storage Policy

Current default:

- Store source metadata in JSONL and target source files.
- Store small synthetic and public-demo materials in Git.
- Store bulky, copyrighted, sensitive, restricted, or embargoed raw sources outside Git unless explicitly authorized.
- Use local `sources/raw/private/` and `sources/raw/embargoed/` only as ignored or controlled local drop zones.
- Prefer summaries, extracted facts, citations, and source locations over republishing source material.

Open decision:

- Choose long-term storage for real raw sources: local archive, Google Drive, object storage, or another controlled repository.

## Faux Data Lifecycle

Faux data remains as a permanent demo fixture unless superseded by a clearer examples structure.

Rules:

- Faux data must remain clearly labeled.
- Faux observations must not be confused with real approved observations.
- Faux records may test ledgers, reports, site publishing, and validation behavior.
- Real target folders should be separate from faux target folders.

Possible future move:

- Move faux materials under `examples/` after the first real target packet exists.

## Evidence Language

Use careful source-grounded phrasing:

- The filing states...
- The record indicates...
- According to the agenda...
- This raises a question about...
- Further confirmation is needed...

Avoid unsupported accusations, motive claims, or legal conclusions.

## Technical Defaults

- Plain files first.
- Markdown for review packets, dossiers, and readable records.
- JSONL for append-only ledgers and registries.
- GitHub for version control and audit trail.
- Netlify for public static publishing.
- Python standard-library scripts for early validation and exports.
- No database until the file workflow proves repeatable across at least one real target.

## Validation Defaults

Before commit or push:

```powershell
python scripts\validate_observations.py
python -m py_compile scripts\validate_observations.py scripts\merge_approved_observations.py scripts\build_dossier.py scripts\source_snapshot_helper.py scripts\export_public_report.py
```

Validation currently allows matching mirrored records between target-local approved ledgers and the global approved ledger. It flags conflicting duplicate observation IDs.

## Deployment Defaults

- GitHub push to `main` publishes the Netlify static site.
- `site/` is public-facing.
- `reports/public/` may be exported to `site/reports/`.
- Manual Netlify deploy remains a fallback, not the preferred steady-state path.

## Snag Process

Snags are project-learning records, not evidence records.

Use snags for:

- source access problems,
- schema gaps,
- validation surprises,
- review friction,
- deployment issues,
- authorization boundary problems,
- process lessons worth folding into SOPs.

Resolved snags should either move to the resolved section or stay under open only when there is a remaining action.

## First Real Target Readiness Criteria

Before creating the first real target packet, confirm:

- Texas Range scope is chosen.
- Real target type is chosen.
- Raw source storage default is accepted.
- Publication posture is accepted.
- Human reviewer and publication approver are identified, even if both are the same person.

## Recommended Immediate Next Steps

1. Define the first Texas Range scope.
2. Create `docs/texas_range_intake_plan.md`.
3. Create a blank first-real-target workspace from templates.
4. Run source discovery only; do not extract observations until source registry entries exist.
5. Prepare the first real review packet with pending observations only.

## Open Founding Questions

1. What exact Texas geography or issue lens defines the first real target?
2. Should the first public-facing real output be a mini-dossier, issue briefing, map, or methodology note?
3. Where should real raw source files live?
4. Who besides the human lead can approve observations or publication?
5. Should faux data remain under `targets/` or move to `examples/` once the first real target exists?

