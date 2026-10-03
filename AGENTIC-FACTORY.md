# Agentic Factory — Guides / Guards / Sensors / Checks

Cereja Editorial Engine uses four operational control types alongside semantic evals and human editorial gates.

| Layer | Responsibility | Current implementation |
|---|---|---|
| Guides | Instruct task execution and composition | `guides/`, `formats/`, packet/context contracts, agent role contracts |
| Guards | Prevent disallowed runtime states | `guards/`, `safety/`, escalation and privacy rules |
| Sensors | Observe run behavior and outcomes | `sensors/`, `metrics/`, routed-run manifests |
| Checks | Deterministic pass/fail rules | `checks/`, CI, structural packet validation |

## Downstream controls

**Semantic evals** handle qualities that cannot be proven mechanically, such as channel fit.

**Editorial gates** retain semantic and human authority for thesis, evidence scope, voice, originality, intellectual honesty, audience value and rights.

**Human approval** remains mandatory for publication.

## Control flow

```text
GUIDES
  ↓
GUARDS
  ↓
RESEARCH / ROUTE / COMPOSE
  ↓
SENSORS
  ↓
DETERMINISTIC CHECKS
  ↓
SEMANTIC EVALS
  ↓
EDITORIAL / HUMAN GATES
  ↓
PUBLISH
  ↓
LEARN BACK
```

## First executable check

`checks/editorial_packet.py` validates the minimum structural contract of an Editorial Packet without requiring model judgment.

CI runs repository tests on pushes and pull requests.

This does **not** mean packet quality is mechanically provable. Thesis quality, evidence adequacy, channel fit and publication approval remain downstream.
