"""Build a simple dossier draft from a target's approved observations."""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("target_path", help="Path under targets, for example targets/data_centers/target_slug_example")
    args = parser.parse_args()

    target_dir = (ROOT / args.target_path).resolve()
    observations = read_jsonl(target_dir / "observations_approved.jsonl")
    grouped: dict[str, list[dict]] = defaultdict(list)
    for observation in observations:
        grouped[observation.get("category", "other")].append(observation)

    lines = [
        f"# Dossier Draft: {target_dir.name}",
        "",
        "## Executive Summary",
        "",
        "This dossier draft was generated from approved observations.",
        "",
        "## Key Findings",
        "",
    ]

    for category in sorted(grouped):
        lines.extend([f"## {category.title()} Observations", ""])
        for observation in grouped[category]:
            lines.append(f"- {observation['observation_text']} [{observation['observation_id']}]")
        lines.append("")

    lines.extend(["## Source Index", ""])
    source_ids = sorted({source_id for observation in observations for source_id in observation.get("source_ids", [])})
    for source_id in source_ids:
        lines.append(f"- {source_id}")

    output = target_dir / "dossier.md"
    output.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    print(f"Wrote {output}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

