"""Offline plain-text token audit. No API calls, output generation or billing estimates."""
import argparse
import hashlib
import json
from pathlib import Path
import importlib.metadata

ROOT = Path(__file__).resolve().parent
import prepare_inputs

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--encoding", default="o200k_base")
    parser.add_argument("--max-plain-text-tokens", type=int)
    args = parser.parse_args()
    if args.max_plain_text_tokens is not None and args.max_plain_text_tokens < 1:
        parser.error("Token budget must be positive")
    try:
        import tiktoken
        import tiktoken.load
    except ImportError:
        parser.error("Install requirements-token-audit.txt; no API key is needed")

    # Only cached tokenizer tables are allowed during the audit.
    def deny_download(path):
        raise RuntimeError("Tokenizer table is not cached. Prepare it before offline auditing.")
    tiktoken.load.read_file = deny_download
    enc = tiktoken.get_encoding(args.encoding)
    outputs = prepare_inputs.build()  # Verify all frozen source hashes.
    lock = json.loads((ROOT / "lock.json").read_text(encoding="utf-8"))
    report = {
        "corpus_version": lock["corpus_version"],
        "method": "offline plain-text tokenization",
        "encoding": enc.name,
        "tiktoken_version": importlib.metadata.version("tiktoken"),
        "model": None,
        "includes_request_overhead": False,
        "includes_output_or_reasoning_tokens": False,
        "api_calls": 0,
        "model_benchmark_status": "deferred_by_user",
        "semantic_quality_results": None,
        "max_plain_text_tokens": args.max_plain_text_tokens,
        "lock_sha256": hashlib.sha256((ROOT / "lock.json").read_bytes()).hexdigest(),
        "sources": {}, "conditions": {}, "selection_comparison": {}
    }
    count = lambda text: len(enc.encode(text, disallowed_special=()))
    for item in lock["files"]:
        text = prepare_inputs.checked_path(item["path"]).read_text(encoding="utf-8")
        report["sources"][item["id"]] = {"tokens": count(text), "sha256": item["sha256"]}
    for label in ("A", "B", "C", "D"):
        data = outputs[label + ".md"]
        tokens = count(data.decode("utf-8"))
        report["conditions"][label] = {
            "plain_text_tokens": tokens,
            "input_sha256": hashlib.sha256(data).hexdigest(),
            "within_plain_text_budget": None if args.max_plain_text_tokens is None
            else tokens <= args.max_plain_text_tokens
        }
    baseline = report["conditions"]["B"]["plain_text_tokens"]
    for label in ("C", "D"):
        current = report["conditions"][label]["plain_text_tokens"]
        report["selection_comparison"][label + "_vs_B"] = {
            "tokens_removed": baseline-current,
            "reduction_percent": round(100*(baseline-current)/baseline, 2) if baseline else None
        }
    print(json.dumps(report, indent=2))
    if any(x["within_plain_text_budget"] is False for x in report["conditions"].values()):
        raise SystemExit(2)  # Report first; never silently truncate evidence.

if __name__ == "__main__":
    main()

