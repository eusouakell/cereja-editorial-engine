# Cereja Editorial Engine

Governed AI-assisted editorial workflow.

```text
REQUEST
→ TRIAGE
→ CONTEXT ROUTING
→ RESEARCH
→ THESIS / COUNTERTHESIS
→ DRAFT SUPPORT
→ GATES
→ HUMAN APPROVAL
→ PUBLISH
→ LEARN BACK
```

Initial mode: **AUDIT ONLY**.

The engine does not automate Kell's opinion or publication approval.

## Release status

v0.1 is a proposed documentation architecture. Agent names describe planned roles, not deployed agents. Routing and editorial gates are specified, not automated. Archive ingestion and A/B/C/D model evaluation have not been performed; no measured performance is claimed. Publication remains human-approved.

## Start here

- [System specification](SYSTEM-SPEC.md)
- [Context contract](router/context-contract.md)
- [Editorial gates](gates/editorial-gates.md)
- [Benchmark protocol](benchmark/README.md)
- [First 30 days](roadmap/first-30-days.md)

## First inspectable example

Read the [retrospective creativity/AI brief](examples/creativity-ai/brief.md) and its [manual context manifest](examples/creativity-ai/manifest.json). This demonstrates source boundaries and a pending human decision, not automated routing or a completed model experiment.

Canonical knowledge design and public-source inventory live in [Cereja Knowledge System](https://github.com/eusouakell/cereja-knowledge-system).

## Current execution decision

Paid model runs are deferred. [Local token preflight](benchmark/pilot/TOKEN-PREFLIGHT.md) measures prepared text and records context-selection savings without API calls. See the [roadmap status](roadmap/first-30-days.md) for completed preparation and pending validation.

