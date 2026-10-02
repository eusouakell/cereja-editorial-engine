# Multiformat agentic content factory

Status: **architecture and contracts only**. No end-to-end autonomous factory is claimed.

## Core decision

The newsletter is not the object from which every other channel is mechanically cut.

The shared canonical working object is the **Editorial Packet**:

```text
KNOWLEDGE SYSTEM
        ↓
EDITORIAL PACKET
thesis + context + evidence + intent
        ↓
CONTENT TOKENS
        ↓
CHANNEL COMPOSITION
        ↓
CHANNEL-SPECIFIC EVALS
        ↓
HUMAN APPROVAL
        ↓
PUBLISH
        ↓
LEARN BACK
```

## Proposed role pipeline

```text
SIGNAL SCOUT / RESEARCHER
        ↓
TOKENIZER
extracts candidate semantic units
        ↓
EDITORIAL CURATOR
selects what belongs to the edition
        ↓
THESIS BUILDER + DEVIL'S ADVOCATE
structures argument and material tension
        ↓
CANONICAL COMPOSER
builds the Editorial Packet and newsletter candidate
        ↓
┌────────────────┬────────────────┬────────────────┐
│ LINKEDIN       │ INSTAGRAM      │ OTHER FORMAT   │
│ renderer       │ renderer       │ renderer       │
│ metapost       │ visual magazine│ video/slides...│
└────────────────┴────────────────┴────────────────┘
        ↓
SOURCE + VOICE + CHANNEL-FIT + RIGHTS EVALS
        ↓
KELL APPROVES / REVISES / REJECTS
        ↓
ARCHIVIST WRITES BACK
```

## Context isolation

Renderers should receive the **minimum sufficient authoritative context** for their job.

Example:

An Instagram renderer may need:
- selected tokens;
- approved thesis;
- Cereja voice constraints;
- visual format contract;
- channel constraints;
- rights metadata.

It should not receive the full research corpus by default.

## Publication independence

LinkedIn and Instagram are sibling outputs from the packet, not child summaries of the newsletter.

They may:
- emphasize different tokens;
- use different structure;
- omit material irrelevant to the channel.

They may not:
- invent evidence;
- silently alter claim scope;
- create an unreviewed new thesis;
- publish without human approval.

## Learning loop

After publication, record:
- what tokens were actually used;
- what Kell rewrote or removed;
- which gates fired;
- effort/time if intentionally measured;
- channel outcome metrics only when they are available and appropriately interpreted.

Observed editorial use should drive future taxonomy and templates.
