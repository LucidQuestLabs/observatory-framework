# SOP 00: Master Workflow

## Purpose

Coordinate the end-to-end Observatory loop from target definition through source intake, observation extraction, human review, ledger preservation, report generation, and follow-up questions.

## Inputs

- Target or issue scope.
- Existing target profile, if any.
- Source files, source URLs, or source discovery tasks.
- Relevant schemas and templates.
- Human review constraints.

## Procedure

1. Define the target, jurisdiction, and research scope.
2. Create or update the target profile.
3. Register sources before extracting claims.
4. Process raw sources into usable text, excerpts, tables, or section references.
5. Extract atomic observations with source IDs, source locations, confidence, interpretation level, review status, and publication status.
6. Prepare a review packet that separates evidence, interpretation, contradictions, open questions, and recommended next actions.
7. Human reviewer approves, rejects, clarifies, escalates, or restricts proposed observations.
8. Append approved observations to the relevant target ledger and the global ledger.
9. Generate briefings or dossiers only from approved observations unless explicitly marked draft/internal.
10. Record corrections, supersessions, unresolved contradictions, and next research actions.

## Outputs

- `target_profile.md`
- `sources.md` or source registry entries
- `observations_pending.md` or JSONL pending observations
- `review_packet.md`
- Approved, rejected, or clarification records
- Updated ledgers
- Draft or final dossier
- Open questions and next actions

