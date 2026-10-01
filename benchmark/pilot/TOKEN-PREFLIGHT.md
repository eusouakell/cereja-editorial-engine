# Token preflight before any model benchmark

User decision, 2026-10-01: no paid API execution now. Model comparison is deferred. Token measurement and context selection remain local preparation work.

## Reproduce without an API

Install the free local tokenizer and prepare its public vocabulary table once:
```
python -m pip install -r benchmark/pilot/requirements-token-audit.txt
python -c "import tiktoken; tiktoken.get_encoding('o200k_base')"
python benchmark/pilot/token_audit.py
python benchmark/pilot/token_audit.py --max-plain-text-tokens 2000
```

Package/table setup requires internet, but sends no corpus content. The audit itself requires a cached table and refuses uncached downloads. No key, API client or model is configured. A budget is an explicit local planning choice, not a model context-window guarantee. Exit code 2 indicates an exceeded budget; source hash mismatch also fails. The script never truncates.

The [recorded audit](token-audit-v01.json) counts exact plain-text strings under the named encoding and package version. It does not count message wrappers, tools, output, reasoning, images or total billable request usage. No model has been selected, so do not label these counts as exact usage for a particular model. [Official token-counting guidance](https://developers.openai.com/api/docs/guides/token-counting).

## Optimization already measured

C selects the scoped study record from B's three-record corpus. D retains that evidence and adds review instructions. Compare C/B and D/B only as input-size differences. A has no evidence and is a baseline, not the recommended smallest useful bundle. Selection was manual; it is not an automatically optimized router.

Do not delete attribution, population, methods, date, limits, required instructions or counterevidence to meet a budget. Keep the current corpus frozen. Any shorter rewrite or different selection belongs in a new corpus version with a change log and semantic coverage review; remeasure every condition from that same version. Never claim that a lower token count improved quality without actual output review.

## Before resuming a paid comparison

1. Approve the research scope and broaden evidence/counterevidence.
2. Review per-source contribution, duplication and task relevance.
3. Choose a model/version and validate its tokenizer and full request budget.
4. Reserve output and reasoning capacity as applicable; use one output budget across conditions.
5. If estimating money, use verified current prices and declared input/output assumptions, not guessed prices.
6. Record run settings and hashes; run and review outputs only after explicit authorization to resume paid calls.

Voice scoring and publication approval remain independent human decisions. No model scores or editorial results exist in this token audit.

## Recorded plain-text counts

| Condition | Tokens under o200k_base |
|---|---:|
| A | 143 |
| B | 1370 |
| C | 464 |
| D | 599 |

Manual selection removes 906 tokens (66.13%) in C versus B. D removes 771 (56.28%) versus B while retaining its checklist. These are measured input-size differences for creativity-v01, not quality improvements or billed usage. Hashes and package version are recorded in the JSON audit.

