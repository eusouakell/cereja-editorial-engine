# Guards

Guards are hard boundaries that prevent a run from entering an invalid or disallowed state.

Current guard sources include:

- privacy and source-exclusion rules in `router/context-contract.md`;
- science/behavior/neurodivergence boundaries in `safety/`;
- rights constraints carried by the Editorial Packet;
- escalation rules in `SYSTEM-SPEC.md`.

## Important distinction

A **Guard** is a runtime boundary.

An **Editorial Gate** is a review/approval decision that may require semantic or human judgment.

For example:

- "private client data must not enter a renderer" → Guard;
- "does this argument have enough audience value?" → Editorial Gate;
- "new science/health claims must escalate" → Guard;
- "is the final interpretation intellectually honest?" → Editorial Gate.

The factory should not collapse these into one control type.
