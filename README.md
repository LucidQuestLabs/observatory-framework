# Observatory Framework

Observatory Framework is a human-in-the-loop, evidence-led research and accountability system for turning fragmented public-interest evidence into structured observations, reviewed ledgers, and source-backed dossiers.

The first reference use case is investigation of AI data centers and related infrastructure: permitting, energy, water, land use, environmental risk, governance, public incentives, and community impact. The framework is intentionally agent-agnostic and portable across Codex, Claude, ChatGPT, local LLMs, GitHub workflows, Google Drive, NotebookLM, databases, dashboards, and static publishing.

## Core Loop

```text
Source -> Observation -> Review -> Ledger -> Dossier -> Next Question
```

Agents propose reviewable artifacts. Humans approve, reject, annotate, escalate, or publish. Approved observations are appended, not silently mutated.

## Baseline Corpus

The baseline corpus is the reusable operating system for future investigations:

- `PROJECT_BRIEF.md` explains purpose, scope, and MVP boundaries.
- `docs/founding_decisions.md` anchors current operating decisions and open founding questions.
- `sops/` defines repeatable workflows.
- `schemas/` defines portable JSON schemas for sources, observations, entities, facilities, review packets, dossiers, and action items.
- `prompts/` gives role prompts for agentic frameworks.
- `templates/` gives starter documents for targets, sources, observations, review packets, dossiers, briefings, and corrections.
- `ledger/` stores append-only JSONL registries.
- `review/` stores incoming and resolved human-review packets.
- `targets/` stores target-specific investigation workspaces.
- `snags/` stores process snags, blockers, surprises, and iteration lessons.
- `docs/` stores architecture, roadmap, data dictionary, glossary, and deployment notes.
- `site/` provides a minimal static public surface for Netlify or other static hosts.
- `.github/workflows/validate.yml` validates the corpus on GitHub pushes and pull requests.

## MVP Success Criteria

The MVP is complete when it can produce, review, preserve, and summarize one mini-dossier for a target facility, company, jurisdiction, or infrastructure cluster. A mini-dossier should include target identity, source list, proposed and approved observations, confidence ratings, open questions, and human-approved summary language.

## Working Rules

- Preserve evidence before interpreting it.
- Keep observations atomic and source-backed.
- Mark confidence and interpretation level on every observation.
- Keep raw source, observation, interpretation, recommendation, review status, and publication status distinct.
- Treat approved observations as append-only records.
- Use careful public-interest language and avoid unsupported accusations.
- Keep public, restricted, private, and embargoed materials clearly marked.
- Capture workflow snags early so the process improves without burying friction in chat history.

## Publishing

The static public surface lives in `site/` and is configured for Netlify through `netlify.toml`. See `docs/github_publish_flow.md` for the GitHub-to-Netlify setup and push process.
