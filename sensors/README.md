# Sensors

Sensors observe what happened in a run. They do not approve or reject publication by themselves.

Current sensor candidates come from `metrics/` and the future routed-run manifest:

- selected and excluded context IDs;
- authority conflicts and stale-source warnings;
- evidence coverage observations;
- gate findings;
- human revision distance;
- research/draft/review time;
- review-loop count;
- token/context-budget observations.

## Rule

A sensor produces evidence for diagnosis and learning.

A threshold may later promote a stable sensor into a deterministic Check, but the raw observation itself is not a verdict.
