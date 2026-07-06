# Sales Note Lint

![Sales Note Lint cover](assets/readme-cover.svg)

> Check sales call notes for missing next step, decision maker, and timeline

![stack](https://img.shields.io/badge/stack-Python-16a34a?style=flat-square) ![python](https://img.shields.io/badge/python-3.11-dc2626?style=flat-square) ![license](https://img.shields.io/badge/license-MIT-7c3aed?style=flat-square) ![ci](https://img.shields.io/badge/ci-GitHub%20Actions-0891b2?style=flat-square)

## At a glance

| Area | Detail |
| --- | --- |
| Focus | sales operations |
| Command | `sales-note-lint` |
| Formats | text, JSON, JSONL, CSV |
| Output | Markdown table or JSON |

## What it checks

| Rule | Severity | What it catches |
| --- | --- | --- |
| `unknown-decision-maker` | high | decision maker missing |
| `missing-next-step` | medium | next step missing |
| `missing-timeline` | low | timeline missing |

## Try it locally

```bash
python -m pip install -e ".[dev]"
sales-note-lint examples/sample.txt
sales-note-lint examples/sample.txt --json --fail-on medium
```

## Notes from the code

`rules.py` keeps the project policy explicit, while `core.py` handles parsing and report rendering. The CLI stays thin on purpose so the checks are easy to test.

## Verify

```bash
python -m pip install -e ".[dev]"
ruff check .
pytest
python -m sales_note_lint --help
```
