from __future__ import annotations

from sales_note_lint.models import Rule

PROJECT_NAME = 'sales-note-lint'
SUMMARY = 'Check sales call notes for missing next step, decision maker, and timeline.'
SAMPLE_RISK = 'decision_maker unknown next_step none timeline missing'
SAMPLE_CLEAN = 'decision_maker CTO next_step send proposal timeline 2w'
TEXT_FIELDS = ("text", "content", "description", "summary", "body", "notes", "message")
SUBJECT_FIELDS = ("id", "name", "path", "service", "endpoint", "field", "event")

RULES = (
    Rule(
        code='unknown-decision-maker',
        severity='high',
        pattern='decision_maker\\s+(unknown|none|missing)',
        message='decision maker missing',
        recommendation='identify buyer or sponsor',
    ),
    Rule(
        code='missing-next-step',
        severity='medium',
        pattern='next_step\\s+(none|missing|unknown)',
        message='next step missing',
        recommendation='record concrete follow-up',
    ),
    Rule(
        code='missing-timeline',
        severity='low',
        pattern='timeline\\s+(missing|none|unknown)',
        message='timeline missing',
        recommendation='capture buying timeline',
    ),
)
