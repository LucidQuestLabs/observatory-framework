# SOP 11: Snag Logging

## Purpose

Capture process friction before it disappears into chat history, commit notes, or memory. A snag is any blocker, surprise, ambiguity, tool failure, source problem, review bottleneck, or workflow lesson that should improve the next investigation loop.

## When to Log a Snag

- A source is inaccessible, paywalled, malformed, missing pages, or hard to cite.
- An agent cannot determine whether a claim is direct, inferred, or speculative.
- A reviewer rejects or clarifies an observation for a repeatable reason.
- A schema field is confusing, missing, or too broad.
- A script, dashboard, static export, or deployment step fails.
- A target requires legal, domain, or publication escalation.
- A process shortcut worked well enough to standardize.

## Procedure

1. Create a snag entry using `templates/snag_template.md`.
2. Assign severity: `minor`, `moderate`, `major`, or `blocking`.
3. Assign type: `source`, `schema`, `agent`, `review`, `ledger`, `report`, `deployment`, `ethics`, or `process`.
4. Record the current workaround, if any.
5. Define a next action and owner.
6. Link related sources, observations, review packets, scripts, or reports.
7. Revisit snags during repeatability tests and fold durable lessons into SOPs, schemas, or templates.

## Snag Lifecycle

- `open`: captured but not yet resolved.
- `triaged`: severity and next action assigned.
- `in_progress`: being addressed.
- `resolved`: fix or decision completed.
- `accepted`: known limitation retained intentionally.
- `superseded`: replaced by a later snag or broader process change.

## Output

Store project-wide snags in `snags/snag_log.md`. Store target-specific snags in the target workspace when the issue belongs to one investigation.

