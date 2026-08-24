"""Command line entry point for the bounded issue #57 corpus."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Sequence

from .core import (
    EXPERIMENT_ROOT,
    finalize,
    freeze_contract,
    generate,
    materialize_sources,
    validate_finalized,
    validate_manifest,
    validate_source_snapshot,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=EXPERIMENT_ROOT)
    commands = parser.add_subparsers(dest="command", required=True)
    materialize = commands.add_parser("materialize-sources")
    materialize.add_argument("--qwen-repo", type=Path, required=True)
    commands.add_parser("validate-sources")
    commands.add_parser("freeze-contract")
    generation = commands.add_parser("generate")
    generation.add_argument("--workers", type=int, default=1)
    commands.add_parser("finalize")
    commands.add_parser("validate-finalized")
    commands.add_parser("validate-manifest")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    root = args.root.resolve()
    if args.command == "materialize-sources":
        result = materialize_sources(args.qwen_repo.resolve(), root)
    elif args.command == "validate-sources":
        sources, prompts = validate_source_snapshot(root)
        result = {"valid": True, "sources": len(sources), "prompts": len(prompts)}
    elif args.command == "freeze-contract":
        result = freeze_contract(root)
    elif args.command == "validate-manifest":
        result = validate_manifest(root)
    elif args.command == "generate":
        result = generate(root, workers=args.workers)
    elif args.command == "finalize":
        result = finalize(root)
    else:
        result = validate_finalized(root)
    print(json.dumps(result, indent=2, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

