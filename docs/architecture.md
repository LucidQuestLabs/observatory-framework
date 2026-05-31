# Architecture

Observatory Framework uses plain files first, then scales toward databases, dashboards, and APIs.

## Layers

```text
Interface Layer
  Dashboard, CLI, Git PRs, Drive, Notion, Airtable, Slack, browser agents

Agent Layer
  Research, extraction, review assistant, contradiction, dossier, publication

Workflow Layer
  Task routing, review queues, approvals, escalation, audit trail

Data Layer
  Sources, observations, entities, facilities, ledgers, reports

Storage Layer
  Git, object storage, database, vector index, local archive

Governance Layer
  Access controls, redaction, publication policy, ethics, legal review
```

## MVP Storage

- Markdown for human-readable packets.
- JSONL for append-only ledgers.
- Git for change review and history.
- Local source folders for raw and processed evidence.

## Scale Path

1. Plain files and Git review.
2. SQLite or DuckDB for local querying.
3. Static public reports and Netlify deployment.
4. PostgreSQL/Supabase, object storage, search, and dashboard.
5. Multi-tenant workspaces and public/private intelligence products.

