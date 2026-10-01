"""Prepare inputs only: no network, API calls, model runs or semantic evaluation."""
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def digest(data):
    return hashlib.sha256(data).hexdigest()

def checked_path(relative):
    path = (ROOT / relative).resolve()
    if not path.is_relative_to(ROOT):
        raise ValueError("Path outside pilot directory")
    return path

def build():
    lock = json.loads((ROOT / "lock.json").read_text(encoding="utf-8"))
    sources = {}
    ids = set()
    for item in lock["files"]:
        if item["id"] in ids:
            raise ValueError("Duplicate source ID")
        ids.add(item["id"])
        data = checked_path(item["path"]).read_bytes()
        if digest(data) != item["sha256"]:
            raise ValueError("Snapshot hash mismatch: " + item["id"])
        sources[item["id"]] = data.decode("utf-8")
    corpus = lock["corpus_ids"]
    selected = lock["selected_ids"]
    if not set(selected).issubset(corpus):
        raise ValueError("Selected sources must belong to frozen corpus")
    conditions = {"A": [], "B": corpus, "C": selected,
                  "D": selected + ["editorial-checklist"]}
    outputs = {}
    manifest = {"corpus_version": lock["corpus_version"],
                "assembly_method": "manual selection; deterministic concatenation",
                "execution_status": "not_run", "measured_results": None,
                "lock_sha256": digest((ROOT / "lock.json").read_bytes()),
                "conditions": {}}
    for label, context_ids in conditions.items():
        text = sources["fixed-task"]
        for sid in context_ids:
            text += "\n\n---\nCONTEXT RECORD: " + sid + "\n\n" + sources[sid]
        data = text.encode("utf-8")
        outputs[label + ".md"] = data
        manifest["conditions"][label] = {
            "source_ids": ["fixed-task"] + context_ids,
            "input_sha256": digest(data), "input_bytes": len(data)}
    outputs["manifest.json"] = (json.dumps(manifest, indent=2) + "\n").encode("utf-8")
    return outputs

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    outputs = build()  # Validate every snapshot before any write.
    outdir = ROOT / "inputs"
    if args.check:
        for name, data in outputs.items():
            if not (outdir / name).is_file() or (outdir / name).read_bytes() != data:
                raise ValueError("Generated input differs or is missing: " + name)
        print("PASS: four inputs and manifest match verified snapshots")
    else:
        outdir.mkdir(exist_ok=True)
        for name, data in outputs.items():
            (outdir / name).write_bytes(data)
        print("Prepared four inputs and manifest; no model execution")

if __name__ == "__main__":
    main()

