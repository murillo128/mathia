"""Inspection and scoring CLI for frozen interchange bundles."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Sequence

from .canonical import canonical_json
from .checkpoint_a import DEFAULT_CHECKPOINT_A_PATH, read_checkpoint_a
from .checkpoint_a_v2 import DEFAULT_CHECKPOINT_A_V2_PATH, read_checkpoint_a_v2
from .checkpoint_b import DEFAULT_CHECKPOINT_B_PATH, read_checkpoint_b
from .interchange import read_bundle
from .panel import panel_snapshot


def _write_output(value: object, output: str | None) -> None:
    rendered = canonical_json(value) + "\n"
    if output is None:
        print(rendered, end="")
    else:
        Path(output).write_text(rendered, encoding="utf-8")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    panel = subparsers.add_parser("panel", help="materialize the accepted frozen panel")
    panel.add_argument("--include-private", action="store_true")
    panel.add_argument("--output")

    checkpoint_a = subparsers.add_parser(
        "checkpoint-a", help="strictly validate the Checkpoint-A pre-registration"
    )
    checkpoint_a.add_argument(
        "artifact", nargs="?", default=str(DEFAULT_CHECKPOINT_A_PATH)
    )

    checkpoint_a_v2 = subparsers.add_parser(
        "checkpoint-a-v2",
        help="strictly validate the separate Checkpoint-A v2 freeze",
    )
    checkpoint_a_v2.add_argument(
        "artifact", nargs="?", default=str(DEFAULT_CHECKPOINT_A_V2_PATH)
    )

    checkpoint_b = subparsers.add_parser(
        "checkpoint-b",
        help="strictly validate the frozen Checkpoint-B samples and leakage decisions",
    )
    checkpoint_b.add_argument(
        "artifact", nargs="?", default=str(DEFAULT_CHECKPOINT_B_PATH)
    )

    validate = subparsers.add_parser("validate", help="strictly validate a bundle")
    validate.add_argument("bundle")

    summarize = subparsers.add_parser("summarize", help="compute deterministic metrics")
    summarize.add_argument("bundle")
    summarize.add_argument("--output")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.command == "panel":
        _write_output(panel_snapshot(include_private=args.include_private), args.output)
        return 0
    if args.command == "checkpoint-a":
        freeze = read_checkpoint_a(args.artifact)
        print(json.dumps(freeze.to_summary(), sort_keys=True))
        return 0
    if args.command == "checkpoint-a-v2":
        freeze = read_checkpoint_a_v2(args.artifact)
        print(json.dumps(freeze.to_summary(), sort_keys=True))
        return 0
    if args.command == "checkpoint-b":
        freeze = read_checkpoint_b(args.artifact)
        print(json.dumps(freeze.to_summary(), sort_keys=True))
        return 0
    bundle = read_bundle(args.bundle)
    if args.command == "validate":
        print(
            json.dumps({"bundle_id": bundle.bundle_id, "valid": True}, sort_keys=True)
        )
        return 0
    _write_output(bundle.metrics().to_dict(), args.output)
    return 0
