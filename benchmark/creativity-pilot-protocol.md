# Creativity briefing pilot — measurement contract

Status: proposed protocol; no executions or scores. Kell approves the editorial direction before any public newsletter output.

## Fixed task

Prepare a 400–600 word Portuguese editorial brief on AI-assisted creativity with: question, scoped evidence, explicit inference, counterargument and a decision for Kell. Do not write in first person as Kell or invent a lived example.

## Controlled conditions

A: task only. B: task plus the complete **frozen, public pilot corpus**. C: task plus a manually selected bundle from that same corpus. D: C plus editorial review checklist. B is not the full newsletter archive. C selection is manual until the router implementation exists. D is checklist-assisted, not an automated semantic harness.

Create a source snapshot and hash per file before execution. Store the corpus, A/B/C/D inputs and manifests. Use the same model/version, settings and output budget; record date and run IDs. Log task time separately from research setup. One run per condition is exploratory, not a causal result; repeat conditions before generalizing.

## Human rubric

Blind condition labels for review where feasible. Score each criterion 0 (fails), 1 (partial), 2 (meets): claim/source fidelity, limits preserved, useful question, distinctness of angle, counterargument and editorial usefulness. Voice remains unscored until approved guidance exists. Two reviewers are preferable; record disagreements rather than averaging them away silently.

## Revision distance

Record the original draft sentence count N before editing. Match draft sentences to the approved revision. Let D be deleted draft sentences and M be substantially rewritten draft sentences, counting each once. Report 100 × (D + M) / N; N=0 means not applicable. Define substantial change as altered claim, interpretation, attribution or logical role; punctuation/spelling-only changes do not count. Record newly added sentences and structural changes separately, since this percentage does not capture them. A rejected draft has no approved revision: mark not approved, not 100%.

## Separate signals

Input token estimates, unsupported claims, source IDs, time and sentence annotations are inspectable signals. Term counts are not semantic quality. Angle similarity requires a stated method and human interpretation; do not equate lexical difference with originality. Never present external study results as Cereja outcomes.

Publication gate: HOLD until actual outputs, completed human review, model/settings and limits are recorded. Publish failures and negative results alongside successes.
