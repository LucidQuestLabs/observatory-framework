# Data Dictionary

## Source

A source is an artifact from which evidence may be extracted: permits, filings, meeting minutes, utility plans, property records, news articles, public records responses, satellite images, and other evidence-bearing materials.

See `schemas/source.schema.json`.

## Observation

An observation is a discrete source-backed statement extracted from one or more sources. Good observations are atomic, traceable, reviewable, and capable of being superseded later.

See `schemas/observation.schema.json`.

## Entity

An entity is a company, agency, developer, utility, landowner, contractor, municipality, law firm, community group, or other actor.

See `schemas/entity.schema.json`.

## Facility

A facility is a physical site or infrastructure asset: data center, substation, power plant, water facility, parcel, fiber route, or related buildout.

See `schemas/facility.schema.json`.

## Review Packet

A review packet is what an agent submits to a human reviewer. It includes sources, proposed observations, confidence levels, contradictions, open questions, and recommended next actions.

See `schemas/review_packet.schema.json`.

## Snag

A snag is a process record for blockers, surprises, ambiguity, tool failures, review friction, deployment issues, and lessons learned. Snags are not evidence claims and should not be mixed into approved observation ledgers.

See `templates/snag_template.md`.

