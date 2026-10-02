# Context contract

## Possible task inputs

- brand;
- editorial guidance;
- relevant worldview;
- thesis records;
- audience;
- current evidence;
- prior published applications;
- authorized project/offer context;
- approved Editorial Packet;
- selected content tokens;
- channel format contract;
- rights metadata.

## Exclude by default

- full newsletter archive;
- all consulting material;
- private client data;
- unrelated personal history;
- superseded theses;
- stale science;
- proprietary employer or client context;
- research sources not needed by the renderer;
- other channel drafts when they are not required.

## Required run manifest

Each future routed run should emit:

- selected context;
- excluded context;
- reasons for both;
- evidence IDs;
- thesis IDs;
- token IDs when used;
- publication band;
- target format/channel;
- required gates;
- unresolved human decisions.

## Renderer principle

A channel renderer should receive the **minimum sufficient authoritative context** for its job.

Example: an Instagram renderer may need selected tokens, thesis, voice constraints, visual format contract and rights metadata. It should not receive the full research corpus by default.

A format adaptation that introduces a new factual claim or thesis must escalate back to evidence/thesis review before publication.
