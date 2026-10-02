# Cereja Editorial Engine

Governed AI-assisted editorial workflow and multiformat content system.

```text
KNOWLEDGE SYSTEM
→ CONTEXT ROUTING
→ RESEARCH
→ THESIS / COUNTERTHESIS
→ EDITORIAL PACKET
→ CONTENT TOKENS
→ FORMAT COMPOSITION
→ CHANNEL EVALS
→ HUMAN APPROVAL
→ PUBLISH
→ LEARN BACK
```

Initial mode: **AUDIT + ASSISTED COMPOSITION**.

The engine does not automate Kell's opinion or publication approval.

## Multiformat factory

The newsletter is the richest recurring publication, but it is not the object from which every other channel must be mechanically cut.

The shared working object is an **Editorial Packet**: approved thesis/open question, relevant context, evidence, intent and constraints.

From that packet, semantic [content tokens](tokens/README.md) can be composed into independent channel outputs through reusable [format contracts](formats/README.md).

```text
EDITORIAL PACKET
      ↓
CONTENT TOKENS
      ↓
┌───────────────┬───────────────┬───────────────┐
│ NEWSLETTER    │ LINKEDIN      │ INSTAGRAM     │
│ quinzenal     │ metapost      │ revista visual│
└───────────────┴───────────────┴───────────────┘
      ↓
CHANNEL-SPECIFIC EVALS
      ↓
HUMAN APPROVAL
```

Read the [multiformat pipeline](pipelines/multiformat.md).

## Release status

v0.2 adds a **documented multiformat architecture**: semantic token contracts, initial format library, channel-fit review and proposed specialized agent roles.

These are design contracts, not a claim of an autonomous production system. Token extraction, routing, rendering and publishing are not yet end-to-end automated. Publication remains human-approved. The existing A/B/C/D model evaluation is still pending; no measured editorial-quality advantage is claimed.

## Start here

- [System specification](SYSTEM-SPEC.md)
- [Multiformat pipeline](pipelines/multiformat.md)
- [Content tokens](tokens/README.md)
- [Format library](formats/README.md)
- [Context contract](router/context-contract.md)
- [Editorial gates](gates/editorial-gates.md)
- [Channel-fit evaluation](evals/channel-fit.md)
- [Benchmark protocol](benchmark/README.md)
- [First 30 days](roadmap/first-30-days.md)

## First inspectable example

Read the [retrospective creativity/AI brief](examples/creativity-ai/brief.md) and its [manual context manifest](examples/creativity-ai/manifest.json). This demonstrates source boundaries and a pending human decision, not automated routing or a completed model experiment.

Canonical knowledge design and public-source inventory live in [Cereja Knowledge System](https://github.com/eusouakell/cereja-knowledge-system).

## Current execution decision

Paid model runs remain deferred. [Local token preflight](benchmark/pilot/TOKEN-PREFLIGHT.md) measures prepared text and records context-selection savings without API calls.

The next practical learning loop is a **real returning newsletter edition plus channel-native derivatives**, with human edits and gate outcomes recorded as evidence. See the [roadmap](roadmap/first-30-days.md).
