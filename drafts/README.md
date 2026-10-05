# Newsletter drafts

This directory is the review surface for edition drafts before publication.

## Naming

Use:

`drafts/031.md`

for edition #31, and the same zero-padded pattern for future editions.

## What belongs here

A draft may contain:

- the newsletter text;
- clearly separated production notes;
- unresolved factual questions;
- links to the edition briefing / packet;
- a short revision log.

Do not mix private interview material into the public-facing draft unless Kell has approved that material for publication.

## Pull request contract

When a draft is ready for editorial review:

1. push it on a branch;
2. open a pull request to `main`;
3. the Agentic Factory routing adapter will classify `drafts/**` as an editorial-draft event;
4. run the routed semantic evals;
5. keep publication as Kell's human gate.

A merged draft is an archival/editorial artifact. It is not automatic authorization to publish to Substack.
