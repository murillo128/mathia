"""Canonical serialization and content identities used by the harness."""

from __future__ import annotations

import hashlib
import json
import math
from collections.abc import Mapping, Sequence
from typing import Any


class CanonicalizationError(ValueError):
    """Raised when a value cannot be represented by the frozen JSON contract."""


def _validate_json(value: Any, path: str = "$") -> None:
    if value is None or isinstance(value, (str, bool, int)):
        return
    if isinstance(value, float):
        if not math.isfinite(value):
            raise CanonicalizationError(f"{path}: non-finite floats are not allowed")
        return
    if isinstance(value, Mapping):
        for key, child in value.items():
            if not isinstance(key, str):
                raise CanonicalizationError(f"{path}: JSON object keys must be strings")
            _validate_json(child, f"{path}.{key}")
        return
    if isinstance(value, Sequence) and not isinstance(value, (str, bytes, bytearray)):
        for index, child in enumerate(value):
            _validate_json(child, f"{path}[{index}]")
        return
    raise CanonicalizationError(
        f"{path}: unsupported value type {type(value).__name__}"
    )


def canonical_json(value: Any) -> str:
    """Return the frozen UTF-8 JSON representation used for every identity."""

    _validate_json(value)
    return json.dumps(
        value,
        ensure_ascii=False,
        allow_nan=False,
        separators=(",", ":"),
        sort_keys=True,
    )


def text_sha256(text: str) -> str:
    """Hash exact UTF-8 text without normalization or whitespace changes."""

    if not isinstance(text, str):
        raise TypeError("text must be a string")
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def stable_id(kind: str, value: Any) -> str:
    """Build a namespaced content ID from canonical serialized input."""

    if not kind or any(
        character not in "abcdefghijklmnopqrstuvwxyz0123456789_" for character in kind
    ):
        raise ValueError(
            "identity kind must contain only lowercase ASCII letters, digits, or underscores"
        )
    digest = hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()
    return f"{kind}_{digest}"


def parse_canonical_object(serialized: str, *, field: str) -> dict[str, Any]:
    """Parse and verify an object previously stored as canonical JSON."""

    try:
        value = json.loads(serialized)
    except json.JSONDecodeError as error:
        raise ValueError(f"{field} is not valid JSON") from error
    if not isinstance(value, dict):
        raise ValueError(f"{field} must encode a JSON object")
    if canonical_json(value) != serialized:
        raise ValueError(f"{field} must use canonical JSON serialization")
    return value


def require_exact_keys(
    value: Mapping[str, Any],
    *,
    required: set[str],
    optional: set[str] | None = None,
    field: str = "record",
) -> None:
    """Reject missing and unknown interchange fields."""

    optional = optional or set()
    keys = set(value)
    missing = required - keys
    unknown = keys - required - optional
    if missing:
        raise ValueError(f"{field} is missing fields: {', '.join(sorted(missing))}")
    if unknown:
        raise ValueError(f"{field} has unknown fields: {', '.join(sorted(unknown))}")
