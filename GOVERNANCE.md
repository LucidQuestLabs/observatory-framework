# Governance

## Review Authority

Agents may create draft sources, proposed observations, review packets, and dossier drafts. Humans decide whether an observation is approved, rejected, needs clarification, superseded, restricted, or public-ready.

## Publication Authority

Public outputs should only use approved observations unless explicitly marked as draft or internal. Sensitive materials require redaction and, when appropriate, legal or editorial review before publication.

## Correction Policy

Approved observations should not be silently edited. Corrections, disputes, and refinements are recorded as new entries in `ledger/corrections.jsonl` or as new observations that reference `supersedes` and `superseded_by`.

## Access Modes

- `public`: suitable for public release.
- `restricted`: available to trusted reviewers or partners.
- `private`: internal only.
- `embargoed`: held for later release or legal/editorial review.

