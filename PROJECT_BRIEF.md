# Project Brief

## Purpose

Observatory Framework makes complex infrastructure visible, auditable, and intelligible through structured evidence workflows. It is designed for public-interest investigations, civic accountability, environmental and resource analysis, policy review, strategic consulting, and human-supervised autonomous research.

## Reference Use Case

The initial MVP focuses on AI data centers and adjacent infrastructure:

- Data center campuses and proposed sites.
- Substations, transmission, backup generation, and grid load.
- Water withdrawals, cooling systems, wastewater, and water stress.
- Zoning, permits, land ownership, tax incentives, and annexation.
- Environmental filings, air permits, noise, heat, habitat, and community impacts.
- Corporate disclosures, utility filings, public meetings, and local reporting.

## Design Stance

The framework is:

- Human-in-the-loop by default.
- Evidence-led and source-traceable.
- Plain-file-first for portability.
- Append-only for approved observations.
- Public/private hybrid by design.
- Agentic-framework agnostic.
- Modular enough to become a dashboard, API, database-backed ledger, or consulting product later.

Current founding decisions and provisional defaults are recorded in `docs/founding_decisions.md`.

## MVP Boundary

The MVP does need a clear folder structure, stable schemas, source discipline, review workflow, append-only ledger, simple report generation, and agent SOPs.

The MVP does not need a polished dashboard, authentication, real-time scraping, complex ontology, legal-grade verification, or enterprise permissions.

The MVP should also keep a visible snag log. Snags are process artifacts, not evidence claims. They help the framework learn from blocked sources, review confusion, automation failures, and repeatable workflow friction.

## Definition of Done

An observation is done when it is atomic, source-backed, confidence-scored, interpretation-labeled, review-statused, and publication-statused.

A source is done when it has metadata, retrieval date, source type, access level, URL or local path, and relevance notes.

A review packet is done when it contains source list, proposed observations, confidence notes, contradictions, open questions, and a human checklist.

A dossier is done when it uses approved observations, preserves source mapping, separates findings from questions, and has clear next actions.
