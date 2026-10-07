# Channel production specifications

Status: **operational contract**.  
Last reviewed: **2026-10-07**.

This layer closes the gap between editorial/channel strategy and production execution.

It answers:

> What canvas, crop, safe area, export type and content prerequisites must a production asset satisfy before it can be considered channel-ready?

It does **not** define editorial strategy or Flame brand truth.

## Authority model

Each technical statement is tagged by evidence class:

- **official_verified** — supported by current official platform documentation;
- **official_adjacent** — official documentation for a related placement (for example, ads) used only as supporting evidence, not silently promoted to an organic-post rule;
- **house_standard** — Cereja Flamejante production default chosen for consistency, legibility or operational safety;
- **verify_in_app** — platform UI/crop/chrome is volatile enough that final preview must be checked in the current product before publication.

Platform constraints are volatile operational truth, not permanent brand canon.

## Current channel files

- [Instagram](instagram.md)
- [LinkedIn](linkedin.md)
- [Substack / newsletter](substack.md)
- [Web](web.md)

The machine-readable subset for deterministic tooling is in [specs.json](specs.json).

## Global production requirements

All visual assets should carry, when applicable:

- approved copy/provenance state;
- rights status for third-party media;
- alt text or accessible description;
- caption/subtitle/transcript for video when meaning depends on audio;
- final-size legibility check;
- export dimensions and format;
- source/editable artifact retained when available;
- current platform preview check when the spec is tagged `verify_in_app`.

## Brand application

Flame remains the authority for identity.

For small digital/social surfaces, the complete Cereja Flamejante signature must not be reduced past its optical legibility limit. When brand context is already established, prefer the official isolated flame, including negative use on suitable dark/colored areas.

See the canonical Flame brand/media rules in `cereja-knowledge-system`.

## Workflow placement

```text
APPROVED CONTENT / STORY
→ CHANNEL / FORMAT DECISION
→ ART DIRECTION
→ CHANNEL PRODUCTION SPEC
→ EXECUTION
→ TECHNICAL CHECKS
→ SEMANTIC / ACCESSIBILITY / RIGHTS REVIEW
→ HUMAN PUBLISH GATE
```

An Art Director does not invent dimensions. An executor does not improvise channel constraints. A deterministic check cannot replace final visual judgment.
