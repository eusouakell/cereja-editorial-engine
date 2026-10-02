# Engine specification

## System boundary

The **Cereja Knowledge System** stores canonical knowledge, evidence, thesis state and editorial history.

The **Cereja Editorial Engine** selects context, supports research and thesis work, composes editorial packets and channel outputs, applies review contracts and records publication outcomes.

The engine must not silently turn a historical publication into current truth.

## Canonical working object: Editorial Packet

A multiformat run should converge on an inspectable packet containing, at minimum:

- editorial intent;
- approved thesis or explicit open question;
- relevant context IDs;
- evidence IDs with scope/date;
- material counterpoint when required;
- selected audience;
- publication band;
- rights constraints;
- voice constraints;
- candidate content tokens;
- required human decisions.

The packet is the shared source for channel composition.

## Atomic content model

```text
CONTENT TOKEN
→ ATOM
→ MOLECULE
→ ORGANISM
→ FORMAT TEMPLATE
→ PUBLICATION
```

This is a composition model, not a requirement to fragment every piece of writing.

Content tokens are semantic units with provenance. They are not pre-approved copy fragments.

## Publication bands

### Light
Comments, micro-posts, rewrites of approved ideas.

Controls: voice, basic source check, rights.

### Editorial
LinkedIn metapost, Instagram carousel, newsletter section, derived article.

Controls: voice, thesis, evidence, originality, rights, audience value, channel fit.

### Thought Leadership
Main newsletter, new framework, talk, science/behavior interpretation, new consulting thesis.

Controls: all gates + counterargument + evidence scope + human approval.

## Channel composition

Channel outputs are sibling publications derived from the same approved Editorial Packet.

A renderer may:
- select different approved tokens;
- reorder material;
- shorten copy;
- adapt structure to the channel.

A renderer may not:
- invent evidence;
- broaden claim scope;
- create a new thesis without escalation;
- bypass rights checks;
- approve or publish autonomously.

## Escalation

The band can only move upward automatically.
Urgency cannot lower it.
A new thesis, science/health claim or client reference is never Light.

Any new claim or thesis introduced during channel adaptation returns to the relevant evidence/thesis gates.

## Human authority

Kell approves, revises or rejects publication.

Human approval of one publication does not automatically:
- approve all candidate tokens;
- approve the same wording for another channel;
- promote historical material into current canonical guidance.
