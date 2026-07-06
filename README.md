![Sales Note Lint cover](assets/readme-cover.svg)

# Sales Note Lint

> Check sales call notes for missing next step, decision maker, and timeline

This is a review desk for sales operations. The useful part is not a dashboard; it is the tiny repeatable moment where vague records become specific findings.

## Finding catalog for `sales-note-lint`

| Finding | Level | Why it matters |
| --- | --- | --- |
| `unknown-decision-maker` | high | decision maker missing |
| `missing-next-step` | medium | next step missing |
| `missing-timeline` | low | timeline missing |

## Try the sample

```bash
git clone https://github.com/mertefekurt/sales-note-lint.git
cd sales-note-lint
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
```

```bash
sales-note-lint examples/sample.txt
sales-note-lint examples/sample.txt --json
```

## Reading the output

- Markdown is meant for humans reviewing a change.
- JSON is meant for CI, scripts, or saved reports.
- `--fail-on` lets the repo decide how strict a gate should be.
