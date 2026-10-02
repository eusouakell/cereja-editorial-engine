# Sensors

**Descriptive + feedback**

Sensors capture what happened during research, composition, review and publication.

## Editorial Sensors

| Sensor | Status | Signal |
|---|---|---|
| selected context IDs | documented in packet contract | what context was used |
| evidence IDs | documented in packet contract | what evidence supported composition |
| token IDs selected per format | documented | what semantic material was used |
| renderer-introduced claim | proposed | new factual content appeared |
| rights metadata state | documented | attribution/reuse state |
| review outcomes | documented | review history |
| human edits | planned learn-back | what the editor changed |
| rejected wording/pattern | planned learn-back | recurring failure modes |
| publication outcome | planned | which artifact actually shipped |
| channel-specific deltas | planned | how formats diverged |
| context payload/trace | planned | what each role received/called |

## Learn-back

Human edits should be treated first as observations, not immediate canonical rules.

```text
EDIT
→ SENSOR
→ repeated pattern / explanation
→ review
→ possible Guide / Guard / Check update
```

One edit should not silently rewrite the voice system.
