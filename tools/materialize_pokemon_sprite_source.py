#!/usr/bin/env python3
"""Materialize raw Pokémon sprite assets from a deduplicated source.json bundle."""
from __future__ import annotations
import argparse, base64, hashlib, json
from pathlib import Path


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("source_json", type=Path)
    ap.add_argument("--out-dir", type=Path)
    args = ap.parse_args()

    doc = json.loads(args.source_json.read_text(encoding="utf-8"))
    out = args.out_dir or args.source_json.parent
    out.mkdir(parents=True, exist_ok=True)
    for name, record in doc["raw_assets"].items():
        if record.get("encoding") != "base64":
            raise ValueError(f"unsupported encoding for {name}")
        data = base64.b64decode(record["data"], validate=True)
        got = hashlib.sha1(data).hexdigest()
        if got != record["sha1"]:
            raise ValueError(f"SHA-1 mismatch for {name}: {got}")
        (out / name).write_bytes(data)
        print(f"{name}\t{len(data)}\t{got}")


if __name__ == "__main__":
    main()
