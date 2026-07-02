# sales-note-lint

> Check sales call notes for missing next step, decision maker, and timeline.

## Field memo Overview

Check sales call notes for missing next step, decision maker, and timeline. It solves review drift by turning plain-text plans into deterministic CI-friendly findings.

## Input Contract

Accepts sales call note. The reader supports plain text, JSON, JSONL, and CSV so the
tool can fit into scripts, CI jobs, and review exports.

## CLI Walkthrough

```bash
python -m pip install -e ".[dev]"
sales-note-lint examples/sample.txt
sales-note-lint examples/sample.txt --json --fail-on medium
python -m sales_note_lint --help
```

## Rule Surface

| Rule | Severity | Meaning |
|---|---:|---|
| `unknown-decision-maker` | high | decision maker missing |
| `missing-next-step` | medium | next step missing |
| `missing-timeline` | low | timeline missing |

## Validation Notes

```bash
ruff check .
pytest
python -m sales_note_lint --help
```

Example risky input:

```text
decision_maker unknown next_step none timeline missing
```

Architecture: `cli.py` handles arguments, `core.py` reads and evaluates records, and
`rules.py` keeps the project-specific policy explicit.

License: MIT.
