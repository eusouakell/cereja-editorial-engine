# Editorial Packet template

Status: **proposed working contract**.

The Editorial Packet is the shared canonical object for one editorial cycle. It is not the final newsletter draft.

```yaml
id: EP-030
status: draft

intent:
  question: "..."
  why_now: "..."
  audience: "..."
  publication_band: thought-leadership

thesis:
  thesis_ids: []
  approved_thesis: null
  open_question: null
  counterpoint_required: true

context:
  selected_context_ids: []
  excluded_context_ids: []
  exclusion_reasons: {}

evidence:
  evidence_ids: []
  unresolved_claims: []
  stale_or_revalidation_required: []

tokens:
  candidate_ids: []
  approved_for_composition: []

formats:
  newsletter: quinzenal-cereja
  linkedin: metapost
  instagram: revista-visual
  stories: research-desk

constraints:
  voice: []
  rights: []
  disclosure: []
  channel_specific: []

human_decisions:
  pending: []
  approved_by: null
  approved_at: null
```

## Lifecycle

```text
DRAFT PACKET
→ RESEARCH / EVIDENCE REVIEW
→ THESIS + COUNTERPOINT REVIEW
→ TOKEN SELECTION
→ HUMAN DECISIONS
→ READY FOR COMPOSITION
→ CHANNEL OUTPUTS
→ PUBLICATION REVIEW
→ ARCHIVE / LEARN BACK
```

A packet can be ready for one format and blocked for another if rights, evidence or channel constraints differ.

The packet stores references and decisions, not a forced copy of the entire research corpus.
