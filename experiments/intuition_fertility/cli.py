"""Inspection and scoring CLI for frozen interchange bundles."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Sequence

from .canonical import canonical_json
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
    bundle = read_bundle(args.bundle)
    if args.command == "validate":
        print(
            json.dumps({"bundle_id": bundle.bundle_id, "valid": True}, sort_keys=True)
        )
        return 0
    _write_output(bundle.metrics().to_dict(), args.output)
    return 0
