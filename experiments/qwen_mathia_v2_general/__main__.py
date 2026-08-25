from __future__ import annotations

import argparse
from pathlib import Path

from .core import (
    DesignConfig,
    build_architecture_audit,
    build_materialization,
    load_pinned_tokenizer,
    verify_committed_materialization,
    write_json,
)


PACKAGE = Path(__file__).resolve().parent


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Materialize the issue #55 Qwen-Mathia G-v2 design")
    parser.add_argument("--config", type=Path, default=PACKAGE / "config.json")
    parser.add_argument("--model-source", type=Path, required=True)
    parser.add_argument("--supplement-artifact-root", type=Path, required=True)
    subparsers = parser.add_subparsers(dest="command", required=True)

    materialize = subparsers.add_parser("materialize")
    materialize.add_argument("--manifest", type=Path, default=PACKAGE / "training_manifest.json")
    materialize.add_argument("--dedupe-report", type=Path, default=PACKAGE / "evidence" / "dedupe_report.json")
    materialize.add_argument(
        "--architecture-audit",
        type=Path,
        default=PACKAGE / "evidence" / "architecture_audit.json",
    )

    verify = subparsers.add_parser("verify")
    verify.add_argument("--manifest", type=Path, default=PACKAGE / "training_manifest.json")
    verify.add_argument("--dedupe-report", type=Path, default=PACKAGE / "evidence" / "dedupe_report.json")
    verify.add_argument(
        "--architecture-audit",
        type=Path,
        default=PACKAGE / "evidence" / "architecture_audit.json",
    )
    return parser


def main() -> int:
    args = _parser().parse_args()
    config = DesignConfig.load(args.config)
    tokenizer = load_pinned_tokenizer(config, args.model_source)
    if args.command == "materialize":
        manifest, dedupe, _targets = build_materialization(
            config,
            tokenizer,
            args.supplement_artifact_root,
        )
        architecture = build_architecture_audit(config, args.model_source)
        write_json(args.manifest, manifest)
        write_json(args.dedupe_report, dedupe)
        write_json(args.architecture_audit, architecture)
    elif args.command == "verify":
        verify_committed_materialization(
            config,
            tokenizer,
            args.supplement_artifact_root,
            args.manifest,
            args.dedupe_report,
        )
        observed = build_architecture_audit(config, args.model_source)
        import json

        committed = json.loads(args.architecture_audit.read_text(encoding="utf-8"))
        if json.dumps(observed, sort_keys=True, separators=(",", ":")) != json.dumps(
            committed, sort_keys=True, separators=(",", ":")
        ):
            raise ValueError("architecture audit does not reproduce from the pinned runtime")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
