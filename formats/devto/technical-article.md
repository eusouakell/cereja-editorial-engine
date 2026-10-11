# DEV.to — technical / build article

**Status:** pilot format contract

## Job

Publish inspectable technical knowledge: systems, workflows, agents, context engineering, evals, implementation decisions, failures and trade-offs.

DEV.to is closer to **how this was built/tested** than to **what Kell thinks about a theme**.

## Use when

- there is real technical/build substance;
- an artifact, architecture, workflow or experiment can be inspected;
- trade-offs and limitations can be stated honestly;
- a repo/demo/evidence path exists when relevant.

Do not convert an abstract newsletter essay into pseudo-technical content.

## Minimum inputs

- approved packet or Lab/build record;
- source/repository provenance;
- current-state boundaries;
- implementation evidence;
- discoverability notes;
- rights/security/privacy constraints.

## Preferred narrative

```text
PROBLEM
→ ASSUMPTION
→ APPROACH / ARCHITECTURE
→ IMPLEMENTATION
→ UNEXPECTED RESULT / TRADE-OFF
→ INVESTIGATION / CHANGE
→ CURRENT EVIDENCE
→ LIMITATIONS
→ WHAT WE'D DO NEXT
```

A straight reference/tutorial structure is valid when stronger.

## Technical honesty

Always distinguish:
- design vs implemented behavior;
- PoC vs production;
- proposed vs operating;
- observed evidence vs inference;
- current limitation vs future plan.

Never imply end-to-end automation or production maturity that is not demonstrated.

## Discoverability

Prefer precise problem/entity language over vague trend language.

Link:
- canonical repo/artifact;
- authoritative sources;
- related proof.

## Gate

- technically inspectable;
- no unsupported performance/security claims;
- code/architecture references are current;
- secrets/client/private context removed;
- limitations visible;
- useful without reading the newsletter;
- human approval required.
