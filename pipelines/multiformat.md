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
│ LINKEDIN       │ INSTAGRAM                         │ OTHER FORMAT   │
│ renderer       │ storyteller → strategist → format │ renderer       │
│ metapost       │ planner → visual → executor       │ video/slides...│
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

Instagram is intentionally decomposed in V0. The Storyteller receives source/evidence and authorship context; the Strategist receives the approved story plus channel evidence; the Format Planner receives the approved story + channel brief; the Visual Storyteller receives the approved outline + Flame/rights constraints; the executor receives only approved implementation artifacts.

No specialist should receive the full research corpus by default unless a concrete evidence gap requires escalation.

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
