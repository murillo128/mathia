from __future__ import annotations

import argparse
from pathlib import Path

from .core import (
    QwenMathiaConfig,
    build_training_manifest,
    load_pinned_tokenizer,
    write_json,
)
from .runtime import (
    freeze_publication,
    run_preflight,
    run_technical_sanity,
    run_training,
    verify_hub_publication,
)


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Execute the bounded Qwen-Mathia v1 run"
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=Path(__file__).with_name("config.json"),
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    audit = subparsers.add_parser("audit")
    audit.add_argument("--output", type=Path, required=True)

    preflight = subparsers.add_parser("preflight")
    preflight.add_argument("--manifest", type=Path, required=True)
    preflight.add_argument("--artifact-dir", type=Path, required=True)
    preflight.add_argument("--output", type=Path, required=True)

    train = subparsers.add_parser("train")
    train.add_argument("--manifest", type=Path, required=True)
    train.add_argument("--output-dir", type=Path, required=True)

    sanity = subparsers.add_parser("sanity")
    sanity.add_argument("--manifest", type=Path, required=True)
    sanity.add_argument("--adapter-dir", type=Path, required=True)
    sanity.add_argument("--output", type=Path, required=True)

    freeze = subparsers.add_parser("freeze-publication")
    freeze.add_argument("--manifest", type=Path, required=True)
    freeze.add_argument("--training-summary", type=Path, required=True)
    freeze.add_argument("--preflight", type=Path, required=True)
    freeze.add_argument("--sanity", type=Path, required=True)
    freeze.add_argument("--run-dir", type=Path, required=True)
    freeze.add_argument("--publication-dir", type=Path, required=True)
    freeze.add_argument("--license-output", type=Path, required=True)
    freeze.add_argument("--upstream-model-card", type=Path, required=True)
    freeze.add_argument("--pr-url", required=True)

    verify = subparsers.add_parser("verify-hub")
    verify.add_argument("--manifest", type=Path, required=True)
    verify.add_argument("--publication-dir", type=Path, required=True)
    verify.add_argument("--revision", required=True)
    verify.add_argument("--clean-cache", type=Path, required=True)
    verify.add_argument("--local-sanity", type=Path, required=True)
    verify.add_argument("--output", type=Path, required=True)
    return parser


def main() -> int:
    args = _parser().parse_args()
    config = QwenMathiaConfig.load(args.config)
    if args.command == "audit":
        tokenizer = load_pinned_tokenizer(config)
        manifest, _examples = build_training_manifest(config, tokenizer)
        write_json(args.output, manifest)
    elif args.command == "preflight":
        run_preflight(config, args.manifest, args.artifact_dir, args.output)
    elif args.command == "train":
        run_training(config, args.manifest, args.output_dir)
    elif args.command == "sanity":
        run_technical_sanity(config, args.manifest, args.adapter_dir, args.output)
    elif args.command == "freeze-publication":
        freeze_publication(
            config,
            args.manifest,
            args.training_summary,
            args.preflight,
            args.sanity,
            args.run_dir,
            args.publication_dir,
            args.license_output,
            args.upstream_model_card,
            pr_url=args.pr_url,
        )
    elif args.command == "verify-hub":
        verify_hub_publication(
            config,
            args.manifest,
            args.publication_dir,
            args.revision,
            args.clean_cache,
            args.local_sanity,
            args.output,
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
