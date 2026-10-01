# Frozen public corpus — exploratory input preparation

Prepared: 2026-10-01. No model runs or human scores.

The three corpus files are short repository records, not mirrored newsletter bodies. Their exact source versions are in lock.json. CF-027 is historical editorial reference with unverified candidate links; EV-CREATIVITY-01 is a scoped external study record; voice-observations remains provisional. A merged documentation PR does not approve voice criteria or a newsletter.

C selects EV-CREATIVITY-01 only: sufficient for a narrow research brief, while excluding historical unverified links and unapproved voice criteria. This manual choice is deliberately inspectable, not a claim of optimal routing. B includes all three frozen records, including contextual distractions; it still contains no confidential content. D adds checklist.md to C. All four share task.md.

Run with Python 3:
```
python benchmark/pilot/prepare_inputs.py
python benchmark/pilot/prepare_inputs.py --check
```

The script verifies byte hashes and path boundaries before writing inputs. Generated inputs are local preparation artifacts, not model outputs; do not commit them as results. inputs/manifest.json records input hashes, selected IDs and byte counts. Bytes are not tokens or semantic quality. Relative links inside snapshots refer to original repositories; use lock.json provenance for source discovery, without browsing during runs.

Before execution record model/version, settings, output budget, date, run ID and frozen input hashes. No API/provider is configured by this change. Repeat runs before generalizing and use the measurement contract for human review. Broader primary evidence and counterevidence remain missing; this one-study corpus can expose limitations but cannot settle the topic.

Preserve these snapshots after starting a run. Add a new version directory for changes, and compare only conditions from the same corpus version.

