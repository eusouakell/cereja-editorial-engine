# Distinctiveness / authorship gate

Status: **proposed human semantic eval**.

Purpose: detect when a Cereja draft is grammatically competent but editorially generic — the kind of text that could plausibly have been produced for any newsletter, by any general-purpose model, from a tidy prompt.

This is **not an AI detector** and does not claim to identify whether a model wrote a passage. See [the anti-AI skill reference audit](../references/anti-ai-distinctiveness.md) for which anti-slop observations Cereja adopts and which detector-evasion tactics it explicitly rejects.

The question is:

> Does this piece preserve Kell's actual curiosity, selection logic, specific repertoire and uneven editorial rhythm — or has execution flattened those into generic model composition?

## Inputs

Review against:

- the current edition briefing;
- Kell's supplied/interviewed observations;
- approved voice guidance;
- section briefings actually used;
- evidence/source packet;
- relevant archive examples;
- the draft under review.

Do not score a draft from text alone when the production context is available.

## Gate 1 — authorship evidence

For every first-person or personal claim, ask:

- Did Kell actually say/write this?
- Is it preserved closely enough that its meaning and attitude have not been normalized?
- Did a model invent a plausible feeling, memory, recommendation, test result or reaction?

### Fail conditions

- invented first-person experience;
- invented affection/disgust/nostalgia;
- "I tested", "I loved", "I keep using" without evidence;
- a personal anecdote manufactured only to make the prose feel human.

A model cannot manufacture authorship evidence.

## Gate 2 — concrete objects before interpretation

Each developed block should contain something concrete:

- a person;
- work;
- experiment;
- company;
- object;
- scene;
- tool;
- number;
- quote;
- observed event;
- source.

A paragraph made only of abstractions, implications and "what this tells us" is a risk even when the sentences are elegant.

### Diagnostic

Remove the adjectives and transitions.

Is there still something specific to learn or picture?

If not, revise the reporting/curation before revising style.

## Gate 3 — discovery path, not thesis repetition

The draft should reveal how one object led to another.

Useful transitions may carry:

- a name;
- image;
- word;
- mechanism;
- question;
- memory;
- contradiction;
- cultural reference.

Not every section must prove the opening thesis.

### Fail patterns

- every section restates the same conclusion;
- five examples arranged as support for one pre-decided claim;
- every transition explains the editorial strategy instead of simply moving;
- a cultural reference exists only to decorate the thesis.

The edition may have a path, a detour and a radar without forcing them into one argument.

## Gate 4 — asymmetry

Human curation is rarely perfectly balanced.

Check for unnecessary symmetry:

- every section same length;
- same paragraph count;
- same opener pattern;
- same "fact → interpretation → takeaway" rhythm;
- three/five-item lists created because the format feels complete;
- every block ending with a mini-conclusion.

Cherry Bomb may expand. On Fire may be terse. AiaiAI may be direct. ALT+TAB may wander.

Do not add disorder artificially. Preserve the differences created by the material.

## Gate 5 — over-completion

A draft can become generic because it tries to cover everything.

Ask:

- Did the model preserve lower-priority points simply because they existed in research?
- Would Kell likely omit some material because another discovery is more interesting?
- Is a tangent being forced back into the main thesis?
- Does every source receive equal treatment regardless of editorial value?

Editing includes leaving material out.

A complete research summary is not automatically a good Cereja edition.

## Gate 6 — significance narration

Flag sentences whose main job is to announce that the previous sentence matters.

Examples of risky functions:

- announcing "the real point";
- telling the reader "this is what matters";
- summarizing an implication already visible;
- naming a moment as surprising, uncomfortable or important instead of showing the evidence/reaction;
- ending a section with a moral because the model expects closure.

Prefer the concrete detail, Kell's actual reaction or a clean stop.

Do not ban every explicit interpretation. Interpretation belongs where Kell has something specific to say.

## Gate 7 — generic model vocabulary

Do not police individual words mechanically.

Flag **clusters** of abstract, polished vocabulary that replace concrete meaning.

Typical warning categories:

- inflated importance: pivotal, crucial, transformative, game-changing;
- frictionless-tech language: seamless, robust, cutting-edge;
- abstract terrain: landscape, ecosystem, realm, journey;
- ceremonial verbs: underscore, showcase, leverage, harness, foster;
- generic conclusions: "in conclusion", "ultimately", "the key takeaway";
- explanatory throat-clearing: "it's important to note", "when it comes to", "let's unpack".

A flagged word may stay if it is the most accurate choice.

The failure is a piece that could swap its nouns and still read the same.

## Gate 8 — rhetorical templates

Review for repeated templates that models produce easily:

- "não é X, é Y";
- "não apenas X, mas Y";
- triads without material reason;
- title/subtitle pairs built as slogans;
- rhetorical questions inserted on schedule;
- em-dash cadence repeated paragraph after paragraph;
- sentence fragments used as performance rather than thought;
- artificial punchline endings;
- calls to action that sound like engagement bait.

Kell may naturally use any of these once.

The issue is template density and predictability.

## Gate 9 — sentence and paragraph texture

Read aloud.

Look for:

- every sentence carrying the same polish;
- transitions that are too complete;
- no abrupt-but-understandable movement;
- all paragraphs equally shaped;
- no place where the reporting itself controls rhythm.

Do **not** intentionally add typos, lowercase text, punctuation errors or fake rambling to simulate humanity.

Natural texture should come from real source material, editing decisions and Kell's language.

## Gate 10 — ending integrity

A Cereja ending does not need to synthesize the whole edition.

Possible valid endings:

- a question;
- a link;
- a small observation;
- a direct invitation;
- a lingering detail;
- a short goodbye.

### Flag

- moral-of-the-story recap;
- generic optimism/pessimism;
- explanation of what the reader "should take away";
- repeated thesis;
- engagement bait unrelated to the actual conversation.

## Gate 11 — human-source preservation

When Kell supplies rough text, interview answers, voice notes or sentences:

1. identify which wording carries real authorship information;
2. preserve it where it works;
3. edit only as much as necessary for clarity/fit;
4. do not normalize every sentence into the same polished register;
5. never treat awkwardness as automatically disposable.

The goal is not to preserve errors for detector behavior.

The goal is to avoid replacing the author's actual language with statistically average editorial prose.

## Review result

Use one of:

### PASS
The draft is specific, authored and structurally varied enough to proceed.

### REVISE — CONTENT
Genericity is coming from weak selection, insufficient evidence or no real discovery path. Do not fix this only with line editing.

### REVISE — VOICE
The material is strong, but Kell's actual reactions/language have been flattened or invented.

### REVISE — COMPOSITION
The piece is over-symmetrical, over-complete or thesis-driven across every block.

### REVISE — LANGUAGE
The composition works, but generic model vocabulary/templates are visibly accumulating.

## Review record

Draft/version:
Edition:
Reviewer:
Briefing/version:
Voice guidance/version:

Evidence of Kell's authorship used:
- 

Distinctive concrete objects:
- 

Genericity findings:
- 

Decision:
- PASS / REVISE — CONTENT / VOICE / COMPOSITION / LANGUAGE

Suggested intervention:
- 

What must remain human-approved:
- personal experience;
- thesis/opinion;
- publication decision.

## Anti-pattern

Do not ask:

> "Can an AI detector catch this?"

Ask:

> "Could this exact editorial reasoning, selection and voice plausibly belong to anyone else?"

If yes, the problem is authorship/distinctiveness, not detector score.
