# Content token schema

Status: **proposed contract**. No automated token extraction is claimed.

A content token should be inspectable and traceable.

```yaml
id: CT-0001
type: evidence
text: "..."
domain:
  - technology
source_ids:
  - EV-...
source_date: YYYY-MM-DD
claim_scope: "..."
confidence: supported
thesis_ids:
  - TH-...
reuse:
  allowed: true
  revalidate_before_publish: true
  expires_at: null
channel_notes:
  newsletter: null
  linkedin: null
  instagram: null
status: candidate
created_from: manual
human_review:
  required: true
  approved_by: null
  approved_at: null
```

## Required concepts

**Identity** — every reusable unit needs a stable ID.

**Type** — what editorial function the unit performs.

**Provenance** — source IDs and source dates stay attached to factual material.

**Scope** — preserve what the evidence actually supports.

**State** — candidate, reviewed, approved, superseded or rejected.

**Reuse rule** — publication history does not remove the need to revalidate stale or time-sensitive claims.

**Channel notes** — a token may be usable in one channel and inappropriate in another.

Human approval of a publication does not automatically convert every generated sentence into a canonical reusable token.
