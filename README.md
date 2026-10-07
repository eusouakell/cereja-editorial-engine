# Cereja Editorial Engine

**Governed AI-assisted editorial workflow and multiformat content system for Cereja Flamejante.**

The engine does not start from a newsletter and mechanically cut it into smaller posts.

Its shared working object is an **Editorial Packet**: approved thesis or open question, relevant context, evidence, intent, constraints and human decisions.

```text
NÚCLEO
knowledge · evidence · thesis · voice
        +
EDITORIAL PACKET
        ↓
CONTENT TOKENS
        ↓
FORMAT COMPOSITION
        ↓
CHANNEL EVALS
        ↓
HUMAN APPROVAL
        ↓
PUBLISH
        ↓
LEARN BACK
```

Visual outputs can also consume [**Flame**](https://github.com/eusouakell/cereja-knowledge-system/tree/main/brand/flame), the Cereja Design System.

## Operating mode

Current mode: **AUDIT + ASSISTED COMPOSITION**.

The engine does not automate Kell's opinion, create a new thesis without approval or publish autonomously.

Agent roles and pipelines documented here are system contracts under validation, not claims that every stage already runs end to end.

## Agentic Factory controls

The canonical cross-repository Factory lives in [eusouakell/agentic-factory](https://github.com/eusouakell/agentic-factory). This engine consumes that model and implements it for editorial work.

The engine now distinguishes four operational control types:

- **Guides** instruct execution;
- **Guards** block disallowed runtime states;
- **Sensors** observe;
- **Checks** validate deterministic rules.

Semantic evals and editorial/human gates remain downstream rather than being renamed into those categories.

Read the [local Factory mapping](AGENTIC-FACTORY.md) and the [canonical Agentic Factory](https://github.com/eusouakell/agentic-factory).

## Multiformat model

```text
EDITORIAL PACKET
      ↓
CONTENT TOKENS
      ↓
┌────────────────┬────────────────┬────────────────┬──────────────┐
│ NEWSLETTER     │ LINKEDIN       │ INSTAGRAM      │ STORIES      │
│ quinzenal      │ metapost       │ visual magazine│ research desk│
└────────────────┴────────────────┴────────────────┴──────────────┘
      ↓
CHANNEL-SPECIFIC EVALS
      ↓
HUMAN APPROVAL
```

Newsletter is the richest recurring publication, but it is **not** the canonical object from which every channel must be derived.

Each channel should be composed natively from the same approved packet.

## Content tokens

Content tokens are semantic editorial units such as:

- signal;
- evidence;
- thesis;
- counterpoint;
- question;
- cultural reference;
- example;
- metaphor;
- recommendation;
- CTA;
- transition.

They carry provenance and state. They are not approved snippets of copy and they are unrelated to LLM tokenizer tokens.

Read [tokens/README.md](tokens/README.md).

## Format contracts

Current format contracts include:

- [quinzenal newsletter](formats/newsletter/quinzenal-cereja.md);
- [newsletter briefing](formats/newsletter/brief-template.md) and [section briefings](formats/newsletter/editorias/README.md);
- [LinkedIn metapost](formats/linkedin/metapost.md);
- [Instagram visual magazine](formats/instagram/revista-visual.md);
- [Instagram Specialist Pipeline V0](guides/instagram-specialist-pipeline-v0.md) — história → objetivo/formato → planner → direção visual → preflight → execução;
- [Stories research desk](formats/stories/research-desk.md);
- [Channel production specs](formats/production/README.md) — dimensions, aspect ratios, safe areas, export types and technical prerequisites.

Each renderer should receive the **minimum sufficient authoritative context** for its job, not the entire research corpus.

## Gates

Publication remains human-approved.

The system reviews:

- thesis integrity;
- evidence and claim scope;
- voice;
- originality;
- intellectual honesty;
- audience value;
- rights;
- channel fit.

Read [editorial gates](gates/editorial-gates.md) and [channel-fit evaluation](evals/channel-fit.md).

## Deterministic checks

The first mechanical control validates Editorial Packet structure:

```bash
python checks/editorial_packet.py packets/editorial-packet-template.md
python -m unittest discover -s tests -v
```

This check proves contract structure only. It does not score editorial quality.

## Current validation loop

The next useful proof is not more architecture.

It is a real returning edition of Cereja, followed by channel-native derivatives, with human edits and gate outcomes recorded as evidence.

That cycle should tell us:

- where the packet is insufficient;
- which context agents incorrectly guess;
- what Kell consistently changes;
- which format rules are stable enough to become skills;
- where the system creates overhead without value.

## Start here

- [System specification](SYSTEM-SPEC.md)
- [Canonical Agentic Factory](https://github.com/eusouakell/agentic-factory)
- [Local Factory controls](AGENTIC-FACTORY.md)
- [Multiformat pipeline](pipelines/multiformat.md)
- [Editorial Packet template](packets/editorial-packet-template.md)
- [Content tokens](tokens/README.md)
- [Format library](formats/README.md)
- [Context contract](router/context-contract.md)
- [Editorial gates](gates/editorial-gates.md)
- [Channel-fit evaluation](evals/channel-fit.md)
- [Editorial workflow roles — local](agents/registry.md)
- [Roadmap](roadmap/first-30-days.md)

## Evidence status

The [retrospective creativity/AI example](examples/creativity-ai/brief.md) demonstrates source boundaries and a pending human decision. It is not a completed model experiment.

The existing A/B/C/D model evaluation is still pending. [Local token preflight](benchmark/pilot/TOKEN-PREFLIGHT.md) measures prepared text and context-selection savings without claiming editorial-quality improvement.

Canonical knowledge, public evidence and Flame live in [Cereja Knowledge System](https://github.com/eusouakell/cereja-knowledge-system).

## Distribution and reader growth

Start with the [organic distribution plan](growth/distribution-plan.md) and [Audience & Growth Planner contract](agents/contracts/audience-growth-planner.md). Baselines, experiments and human publication gates remain explicit; these documents do not claim growth already achieved.

See the [media rights guard](guards/media-rights.md) before using photographs, audio, video or quotations in any channel.

## Rights

This repository is public but not currently open-licensed as a whole. See [RIGHTS.md](RIGHTS.md). Selected assets may receive scoped licenses after real publishing cycles show what should be open versus proprietary.
