"""Deterministic OpenAlex snapshot reduction and Riemann handoff pipeline.

Bulk and full-text bytes stay on the explicitly supplied external volume.  The
repository contains only this implementation and compact, hash-bound evidence.
"""

from __future__ import annotations

import argparse
import csv
import dataclasses
import datetime as dt
import email.utils
import hashlib
import html
import json
import math
import mimetypes
import os
import re
import shutil
import sqlite3
import subprocess
import sys
import time
import urllib.parse
import urllib.robotparser
from collections import Counter, defaultdict
from html.parser import HTMLParser
from pathlib import Path
from typing import Any, Iterable, Sequence


REPO_ROOT = Path(__file__).resolve().parents[2]
DEFAULT_VOLUME = Path("/mnt/openalex")
DEFAULT_ROOT = DEFAULT_VOLUME / "openalex"
DEFAULT_DUCKDB = DEFAULT_ROOT / "python" / "duckdb"
INVENTORY = REPO_ROOT / "experiments" / "riemann_corpus" / "inventory.jsonl"
CORPUS_REPORT = REPO_ROOT / "experiments" / "riemann_corpus" / "corpus_report.json"
RUN_EVIDENCE = Path(__file__).resolve().parent / "run_v1"
SNAPSHOT_BUCKET = "openalex"
SNAPSHOT_JSONL_MANIFEST = "data/jsonl/manifest.json"
SNAPSHOT_PARQUET_MANIFEST = "data/parquet/manifest.json"
SNAPSHOT_JSONL_WORKS_PREFIX = "data/jsonl/works/"
SNAPSHOT_PARQUET_WORKS_PREFIX = "data/parquet/works/"
FREE_FRACTION_FLOOR = 0.20
PIPELINE_VERSION = "openalex-offline-discovery-v1"
REDUCTION_ID = "openalex-work-locator-v4"


class PipelineError(RuntimeError):
    """An expected integrity, storage, dependency, or acquisition failure."""


@dataclasses.dataclass(frozen=True)
class Layout:
    volume: Path
    root: Path
    snapshot: Path
    tmp: Path
    reduced: Path
    riemann: Path
    handoffs: Path
    logs: Path
    state: Path

    @classmethod
    def from_root(cls, volume: Path, root: Path | None = None) -> "Layout":
        actual_root = root or volume / "openalex"
        return cls(
            volume=volume,
            root=actual_root,
            snapshot=actual_root / "snapshot",
            tmp=actual_root / "tmp",
            reduced=actual_root / "reduced",
            riemann=actual_root / "riemann",
            handoffs=actual_root / "handoffs",
            logs=actual_root / "logs",
            state=actual_root / "state",
        )

    def create(self) -> None:
        for path in dataclasses.astuple(self)[2:]:
            Path(path).mkdir(parents=True, exist_ok=True)


def utc_now() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")


def canonical_json(value: Any) -> bytes:
    return (
        json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
        + "\n"
    ).encode()


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    data = json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    temp = path.with_suffix(path.suffix + ".tmp")
    temp.write_text(data, encoding="utf-8")
    os.replace(temp, path)


def write_jsonl(path: Path, values: Iterable[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_suffix(path.suffix + ".tmp")
    with temp.open("w", encoding="utf-8") as stream:
        for value in values:
            stream.write(json.dumps(value, sort_keys=True, ensure_ascii=False) + "\n")
    os.replace(temp, path)


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    with path.open(encoding="utf-8") as stream:
        return [json.loads(line) for line in stream if line.strip()]


def sha256_file(path: Path, block_size: int = 4 * 1024 * 1024) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        while block := stream.read(block_size):
            digest.update(block)
    return digest.hexdigest()


def normalized_openalex_id(value: str | None) -> str | None:
    if not value:
        return None
    match = re.search(r"(?:openalex\.org/)?(W\d+)$", value, re.IGNORECASE)
    return f"https://openalex.org/{match.group(1).upper()}" if match else None


def normalized_doi(value: str | None) -> str | None:
    if not value:
        return None
    lowered = value.strip().lower()
    for prefix in ("https://doi.org/", "http://doi.org/", "doi:"):
        if lowered.startswith(prefix):
            lowered = lowered[len(prefix) :]
            break
    return lowered.rstrip(" .") or None


def normalized_title(value: str | None) -> str:
    if not value:
        return ""
    return " ".join(re.sub(r"[^a-z0-9]+", " ", value.casefold()).split())


FALSE_POSITIVE_PATTERNS: tuple[tuple[str, re.Pattern[str]], ...] = (
    (
        "riemannian_or_surface_without_zeta_anchor",
        re.compile(
            r"(?:riemann(?:ian)? (?:surface|manifold|geometry|metric|mapping)|"
            r"moduli (?:space )?of riemann surfaces)",
            re.I,
        ),
    ),
    ("riemann_liouville", re.compile(r"riemann[–\- ]liouville", re.I)),
    ("riemann_hilbert", re.compile(r"riemann[–\- ]hilbert", re.I)),
    (
        "riemann_sum_or_integral",
        re.compile(r"riemann (?:sum|integral|integration)", re.I),
    ),
    (
        "unrelated_zeta_family",
        re.compile(
            r"(?:selberg|ihara|artin[–\- ]mazur|dynamical|topological|graph|"
            r"spectral) zeta (?:function|functions)",
            re.I,
        ),
    ),
)


def text_relevance(title: str | None, abstract: str | None = None) -> dict[str, Any]:
    """Return an auditable deterministic relevance tier for compact text evidence."""

    title_text = normalized_title(title)
    abstract_text = normalized_title(abstract)
    combined = f"{title_text} {abstract_text}"
    anchor = bool(
        re.search(
            r"riemann hypothesis|riemann zeta|zeta function|zeta zeros?|"
            r"zeros? of (?:the )?zeta|dirichlet l functions?|automorphic l functions?|"
            r"generalized riemann|de bruijn newman|nyman beurling|hilbert polya",
            combined,
        )
    )
    exclusion = None
    for name, pattern in FALSE_POSITIVE_PATTERNS:
        if pattern.search(title_text):
            if name == "unrelated_zeta_family" and re.search(
                r"riemann hypothesis|riemann zeta|number theory|prime", combined
            ):
                continue
            if name == "riemannian_or_surface_without_zeta_anchor" and re.search(
                r"riemann hypothesis|riemann zeta|zeta zeros", combined
            ):
                continue
            exclusion = name
            break

    score = 0
    rules: list[str] = []
    weighted = (
        (3, "riemann_hypothesis", r"riemann hypothesis"),
        (3, "riemann_zeta", r"riemann zeta"),
        (3, "generalized_rh", r"generalized riemann hypothesis"),
        (2, "zeta_zeros", r"(?:zeta.{0,24}zeros?|zeros?.{0,24}zeta)"),
        (2, "critical_line", r"critical line"),
        (2, "explicit_formula", r"explicit formula"),
        (2, "de_bruijn_newman", r"de bruijn newman"),
        (2, "nyman_beurling", r"nyman beurling"),
        (2, "hilbert_polya", r"hilbert polya"),
        (1, "zero_density", r"zero density"),
        (1, "pair_correlation", r"pair correlation"),
        (1, "mollifier", r"mollifier|mollification"),
        (1, "zeta_moments", r"moments? of (?:the )?(?:riemann )?zeta"),
        (1, "l_function_zeros", r"zeros?.{0,24}l functions?|l functions?.{0,24}zeros?"),
    )
    for weight, name, pattern in weighted:
        if re.search(pattern, combined):
            score += weight
            rules.append(name)
    if not anchor and score < 2:
        score = 0
        rules = []
    if exclusion:
        decision = "rejected_false_positive"
    elif score >= 3:
        decision = "high_confidence"
    elif score > 0:
        decision = "context_required"
    else:
        decision = "no_text_signal"
    return {
        "decision": decision,
        "score": score,
        "rules": rules,
        "exclusion": exclusion,
    }


def _run(
    command: Sequence[str], *, input_text: str | None = None
) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        command,
        input=input_text,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )


def volume_evidence(volume: Path) -> dict[str, Any]:
    volume = volume.resolve()
    findmnt = _run(
        [
            "findmnt",
            "-J",
            "-b",
            "-T",
            str(volume),
            "-o",
            "TARGET,SOURCE,FSTYPE,UUID,SIZE,USED,AVAIL,USE%,OPTIONS",
        ]
    )
    if findmnt.returncode:
        raise PipelineError(f"cannot resolve volume mount: {findmnt.stderr.strip()}")
    filesystems = json.loads(findmnt.stdout).get("filesystems", [])
    if len(filesystems) != 1:
        raise PipelineError(
            f"expected one mount for {volume}, found {len(filesystems)}"
        )
    mount = filesystems[0]
    if Path(mount["target"]).resolve() != volume:
        raise PipelineError(f"{volume} is not itself a mountpoint")
    root_device = os.stat("/").st_dev
    volume_device = os.stat(volume).st_dev
    if root_device == volume_device:
        raise PipelineError(f"{volume} resolves to the root filesystem")
    stats = os.statvfs(volume)
    total = stats.f_blocks * stats.f_frsize
    available = stats.f_bavail * stats.f_frsize
    floor = math.ceil(total * FREE_FRACTION_FLOOR)
    if available <= floor:
        raise PipelineError(
            f"volume free bytes {available} are below safety floor {floor}"
        )
    return {
        "checked_at": utc_now(),
        "mountpoint": str(volume),
        "source": mount["source"],
        "filesystem": mount["fstype"],
        "uuid": mount.get("uuid"),
        "mount_options": mount.get("options"),
        "capacity_bytes": total,
        "available_bytes": available,
        "used_bytes": (stats.f_blocks - stats.f_bfree) * stats.f_frsize,
        "filesystem_reserved_bytes": (stats.f_bfree - stats.f_bavail) * stats.f_frsize,
        "free_fraction_floor": FREE_FRACTION_FLOOR,
        "free_bytes_floor": floor,
        "root_device": root_device,
        "volume_device": volume_device,
    }


def assert_free_space(
    layout: Layout, required_temporary_bytes: int = 0
) -> dict[str, Any]:
    evidence = volume_evidence(layout.volume)
    remaining = evidence["available_bytes"] - required_temporary_bytes
    if remaining < evidence["free_bytes_floor"]:
        raise PipelineError(
            "free-space floor would be crossed: "
            f"available={evidence['available_bytes']} temporary={required_temporary_bytes} "
            f"floor={evidence['free_bytes_floor']}"
        )
    return evidence


def _volume_used_bytes(volume: Path) -> int:
    stats = os.statvfs(volume)
    return (stats.f_blocks - stats.f_bfree) * stats.f_frsize


def filesystem_usage(path: Path) -> dict[str, int]:
    stats = os.statvfs(path)
    return {
        "capacity_bytes": stats.f_blocks * stats.f_frsize,
        "used_bytes": (stats.f_blocks - stats.f_bfree) * stats.f_frsize,
        "available_bytes": stats.f_bavail * stats.f_frsize,
    }


def _s3_client() -> Any:
    try:
        import boto3
        from botocore import UNSIGNED
        from botocore.config import Config
    except ImportError as error:  # pragma: no cover - runtime dependency gate
        raise PipelineError(
            "boto3 and botocore are required for snapshot access"
        ) from error
    return boto3.client(
        "s3",
        config=Config(
            signature_version=UNSIGNED,
            connect_timeout=30,
            read_timeout=180,
            retries={"max_attempts": 10, "mode": "adaptive"},
        ),
    )


def _entity(manifest: dict[str, Any], name: str) -> dict[str, Any]:
    try:
        return next(item for item in manifest["entities"] if item["entity"] == name)
    except (KeyError, StopIteration) as error:
        raise PipelineError(f"snapshot manifest has no {name!r} entity") from error


def snapshot_inventory(layout: Layout) -> dict[str, Any]:
    """Measure and freeze current works object identities without downloading shards."""

    layout.create()
    volume = assert_free_space(layout)
    s3 = _s3_client()
    manifests: dict[str, dict[str, Any]] = {}
    manifest_objects: dict[str, dict[str, Any]] = {}
    for format_name, key in (
        ("jsonl", SNAPSHOT_JSONL_MANIFEST),
        ("parquet", SNAPSHOT_PARQUET_MANIFEST),
    ):
        response = s3.get_object(Bucket=SNAPSHOT_BUCKET, Key=key)
        body = response["Body"].read()
        manifests[format_name] = json.loads(body)
        manifest_objects[format_name] = {
            "key": key,
            "etag": response.get("ETag", "").strip('"'),
            "last_modified": response["LastModified"].isoformat(),
            "bytes": len(body),
            "sha256": hashlib.sha256(body).hexdigest(),
        }
        (layout.snapshot / f"{format_name}_manifest.json").write_bytes(body)

    support_objects: dict[str, dict[str, Any]] = {}
    for key in ("LICENSE.txt", "README.txt", "RELEASE_NOTES.txt"):
        response = s3.get_object(Bucket=SNAPSHOT_BUCKET, Key=key)
        body = response["Body"].read()
        support_objects[key] = {
            "etag": response.get("ETag", "").strip('"'),
            "last_modified": response["LastModified"].isoformat(),
            "bytes": len(body),
            "sha256": hashlib.sha256(body).hexdigest(),
        }
        (layout.snapshot / key).write_bytes(body)

    listed: dict[str, list[dict[str, Any]]] = {}
    for format_name, prefix, suffix in (
        ("jsonl", SNAPSHOT_JSONL_WORKS_PREFIX, ".gz"),
        ("parquet", SNAPSHOT_PARQUET_WORKS_PREFIX, ".parquet"),
    ):
        objects: list[dict[str, Any]] = []
        paginator = s3.get_paginator("list_objects_v2")
        for page in paginator.paginate(Bucket=SNAPSHOT_BUCKET, Prefix=prefix):
            for item in page.get("Contents", []):
                if item["Key"].endswith(suffix):
                    objects.append(
                        {
                            "key": item["Key"],
                            "bytes": item["Size"],
                            "etag": item.get("ETag", "").strip('"'),
                            "last_modified": item["LastModified"].isoformat(),
                        }
                    )
        objects.sort(key=lambda item: item["key"])
        listed[format_name] = objects

    summaries: dict[str, Any] = {}
    for format_name in ("jsonl", "parquet"):
        entity = _entity(manifests[format_name], "works")
        objects = listed[format_name]
        listed_bytes = sum(item["bytes"] for item in objects)
        if len(objects) != len(entity["files"]):
            raise PipelineError(
                f"{format_name} works object count disagrees with manifest: "
                f"{len(objects)} != {len(entity['files'])}"
            )
        if listed_bytes != entity["content_length"]:
            raise PipelineError(
                f"{format_name} works bytes disagree with manifest: "
                f"{listed_bytes} != {entity['content_length']}"
            )
        sizes = sorted(item["bytes"] for item in objects)

        def percentile(fraction: float) -> int:
            return sizes[min(len(sizes) - 1, int((len(sizes) - 1) * fraction))]

        summaries[format_name] = {
            "prefix": SNAPSHOT_JSONL_WORKS_PREFIX
            if format_name == "jsonl"
            else SNAPSHOT_PARQUET_WORKS_PREFIX,
            "work_records": entity["record_count"],
            "shard_count": len(objects),
            "bytes": listed_bytes,
            "size_distribution_bytes": {
                "min": sizes[0],
                "p25": percentile(0.25),
                "median": percentile(0.50),
                "p75": percentile(0.75),
                "p95": percentile(0.95),
                "max": sizes[-1],
            },
            "latest_last_modified": max(item["last_modified"] for item in objects),
        }

    safe_cache_capacity = volume["available_bytes"] - volume["free_bytes_floor"]
    mode = (
        "cache"
        if summaries["jsonl"]["bytes"] < safe_cache_capacity * 0.75
        else "stream"
    )
    if mode != "stream":
        raise PipelineError(
            "this implementation expects the measured issue-46 streaming decision"
        )
    parquet_records = {
        item["url"].removeprefix(f"s3://{SNAPSHOT_BUCKET}/"): item["meta"]
        for item in _entity(manifests["parquet"], "works")["files"]
    }
    parquet_objects = []
    for index, item in enumerate(listed["parquet"]):
        if item["key"] not in parquet_records:
            raise PipelineError(
                f"listed parquet object absent from manifest: {item['key']}"
            )
        parquet_objects.append({"index": index, **item, **parquet_records[item["key"]]})

    result = {
        "pipeline_version": PIPELINE_VERSION,
        "captured_at": utc_now(),
        "snapshot_date": manifests["parquet"]["date"],
        "bucket": SNAPSHOT_BUCKET,
        "manifest_objects": manifest_objects,
        "support_objects": support_objects,
        "works": summaries,
        "volume": volume,
        "root_filesystem_at_capture": filesystem_usage(Path("/")),
        "safe_cache_capacity_bytes": safe_cache_capacity,
        "mode": mode,
        "mode_reason": (
            "The compressed JSONL works snapshot exceeds the attached volume's entire "
            "safe cache capacity; stream one Parquet shard at a time and retain reduced parts."
        ),
        "temporary_space_requirement_bytes": summaries["parquet"][
            "size_distribution_bytes"
        ]["max"]
        * 2,
        "parquet_objects": parquet_objects,
    }
    write_json(layout.snapshot / "works_snapshot.json", result)
    return result


def build_seed_records(inventory_path: Path = INVENTORY) -> list[dict[str, Any]]:
    records = []
    for row in load_jsonl(inventory_path):
        if row.get("scope_status") != "relevant":
            continue
        identifiers = row.get("identifiers") or {}
        records.append(
            {
                "source_id": row["source_id"],
                "title": row["title"],
                "title_normalized": normalized_title(row["title"]),
                "authors": row.get("authors") or [],
                "year": row.get("year"),
                "openalex_id": normalized_openalex_id(identifiers.get("openalex")),
                "doi": normalized_doi(identifiers.get("doi")),
                "arxiv": identifiers.get("arxiv"),
                "canonical_url": row.get("canonical_url"),
                "acquisition_status": row.get("acquisition_status"),
                "tags": row.get("tags") or [],
            }
        )
    records.sort(key=lambda row: row["source_id"])
    return records


def prepare_seeds(layout: Layout, inventory_path: Path = INVENTORY) -> dict[str, Any]:
    layout.create()
    records = build_seed_records(inventory_path)
    seed_path = layout.riemann / "seeds.jsonl"
    write_jsonl(seed_path, records)
    summary = {
        "generated_at": utc_now(),
        "inventory_path": str(inventory_path.relative_to(REPO_ROOT)),
        "inventory_sha256": sha256_file(inventory_path),
        "source_revision": _run(["git", "rev-parse", "HEAD"]).stdout.strip(),
        "relevant_seed_count": len(records),
        "openalex_id_count": sum(bool(row["openalex_id"]) for row in records),
        "doi_count": sum(bool(row["doi"]) for row in records),
        "arxiv_count": sum(bool(row["arxiv"]) for row in records),
        "unresolved_without_openalex_or_doi": sum(
            not row["openalex_id"] and not row["doi"] for row in records
        ),
        "seed_path": str(seed_path),
        "seed_sha256": sha256_file(seed_path),
    }
    write_json(layout.riemann / "seed_summary.json", summary)
    return summary


def sql_quote(value: str) -> str:
    return "'" + value.replace("'", "''") + "'"


def _seed_lists(layout: Layout) -> tuple[list[str], list[str], list[str]]:
    records = load_jsonl(layout.riemann / "seeds.jsonl")
    openalex = sorted({row["openalex_id"] for row in records if row["openalex_id"]})
    dois = sorted({row["doi"] for row in records if row["doi"]})
    titles = sorted(
        {row["title_normalized"] for row in records if row["title_normalized"]}
    )
    return openalex, dois, titles


def _list_literal(values: Sequence[str]) -> str:
    return "[" + ",".join(sql_quote(value) for value in values) + "]"


def shard_reduction_sql(
    input_path: Path,
    output_path: Path,
    snapshot: dict[str, Any],
    shard: dict[str, Any],
    seed_openalex: Sequence[str],
    seed_dois: Sequence[str],
    seed_titles: Sequence[str],
) -> str:
    oa = _list_literal(seed_openalex)
    dois = _list_literal(seed_dois)
    titles = _list_literal(seed_titles)
    input_sql = sql_quote(str(input_path))
    output_sql = sql_quote(str(output_path))
    temp_sql = sql_quote(str(input_path.parent / "duckdb_spill"))
    snapshot_date = sql_quote(snapshot["snapshot_date"])
    object_key = sql_quote(shard["key"])
    object_etag = sql_quote(shard["etag"])
    # abstract_inverted_index is JSON text in the standard Parquet snapshot.
    return f"""
SET threads=1;
SET memory_limit='6GB';
SET temp_directory={temp_sql};
SET preserve_insertion_order=false;
COPY (
WITH source AS (
  SELECT
    w.*,
    trim(lower(regexp_replace(coalesce(w.title, ''), '[^a-zA-Z0-9]+', ' ', 'g'))) AS title_norm,
    lower(coalesce(w.abstract_inverted_index, '')) AS abstract_norm,
    coalesce(w.id IN {oa}, false) AS seed_oa_match,
    coalesce(lower(regexp_replace(coalesce(w.doi, ''), '^https?://(?:dx\\.)?doi\\.org/', '')) IN {dois}, false) AS seed_doi_match,
    coalesce(trim(lower(regexp_replace(coalesce(w.title, ''), '[^a-zA-Z0-9]+', ' ', 'g'))) IN {titles}, false) AS seed_title_match,
    coalesce(list_has_any(w.referenced_works, {oa}), false) AS cites_seed,
    coalesce(w.primary_topic.field.display_name = 'Mathematics', false)
      OR coalesce(list_contains(list_transform(w.topics, x -> x.field.display_name), 'Mathematics'), false)
      AS math_adjacent
  FROM read_parquet({input_sql}, hive_partitioning=false) w
), scored AS (
  SELECT *,
    CASE
      WHEN regexp_matches(title_norm, '(riemann hypothesis|riemann zeta|generalized riemann hypothesis|de bruijn newman|nyman beurling|hilbert polya)') THEN 3
      WHEN regexp_matches(title_norm, '(zeta).{0, 24}(zero|zeros|critical line|moment|mollif|pair correlation|zero density)')
        OR regexp_matches(title_norm, '(zero|zeros).{0, 24}(zeta|l function|l functions)') THEN 2
      WHEN regexp_matches(abstract_norm, '(riemann hypothesis|riemann zeta|generalized riemann hypothesis)') THEN 2
      WHEN regexp_matches(title_norm, '(explicit formula|zero density|pair correlation|mollifier|mollification)')
        AND regexp_matches(title_norm, '(zeta|l function|l functions|prime|zeros)') THEN 1
      ELSE 0
    END AS text_score,
    CASE
      WHEN regexp_matches(title_norm, '(riemann liouville|riemann hilbert|riemann sum|riemann integral|riemann integration)') THEN 'riemann_operator_or_calculus'
      WHEN regexp_matches(title_norm, '(riemann surface|riemann surfaces|riemannian manifold|riemannian geometry|riemannian metric)')
        AND NOT regexp_matches(title_norm, '(riemann hypothesis|riemann zeta|zeta zeros)') THEN 'riemann_geometry'
      WHEN regexp_matches(title_norm, '(selberg zeta|ihara zeta|dynamical zeta|topological zeta|graph zeta)')
        AND NOT regexp_matches(title_norm, '(riemann hypothesis|riemann zeta|prime)') THEN 'unrelated_zeta_family'
      ELSE NULL
    END AS exclusion_rule
  FROM source
), classified AS (
  SELECT *,
    seed_oa_match OR seed_doi_match AS seed_match,
    math_adjacent OR seed_oa_match OR seed_doi_match OR seed_title_match OR cites_seed
      OR text_score > 0 OR exclusion_rule IS NOT NULL AS retain_detail
  FROM scored
)
SELECT
  id, doi, title, publication_date, publication_year, language, type, cited_by_count,
  primary_topic.id AS primary_topic_id,
  primary_topic.display_name AS primary_topic_name,
  primary_topic.field.display_name AS primary_field_name,
  primary_topic.domain.display_name AS primary_domain_name,
  math_adjacent,
  seed_match, seed_oa_match, seed_doi_match, seed_title_match, cites_seed,
  text_score,
  CASE
    WHEN seed_match THEN 'exact_seed'
    WHEN seed_title_match THEN 'seed_title_candidate'
    WHEN exclusion_rule IS NOT NULL THEN 'rejected_false_positive'
    WHEN text_score >= 3 THEN 'high_confidence'
    WHEN text_score > 0 THEN 'context_required'
    WHEN cites_seed THEN 'citation_candidate'
    WHEN math_adjacent THEN 'math_index_only'
    ELSE 'catalog_only'
  END AS filter_decision,
  exclusion_rule,
  CASE WHEN retain_detail THEN list_transform(authorships, x -> coalesce(x.author.display_name, x.raw_author_name)) ELSE NULL END AS authors,
  CASE WHEN retain_detail THEN ids ELSE NULL END AS ids,
  CASE WHEN retain_detail THEN abstract_inverted_index ELSE NULL END AS abstract_inverted_index,
  CASE WHEN retain_detail THEN topics ELSE NULL END AS topics,
  CASE WHEN retain_detail THEN keywords ELSE NULL END AS keywords,
  CASE WHEN retain_detail THEN locations ELSE NULL END AS locations,
  CASE WHEN retain_detail THEN primary_location ELSE NULL END AS primary_location,
  CASE WHEN retain_detail THEN best_oa_location ELSE NULL END AS best_oa_location,
  CASE WHEN retain_detail THEN open_access ELSE NULL END AS open_access,
  CASE WHEN retain_detail THEN referenced_works ELSE NULL END AS referenced_works,
  CASE WHEN retain_detail THEN related_works ELSE NULL END AS related_works,
  CASE WHEN retain_detail THEN has_content ELSE NULL END AS has_content,
  CASE WHEN retain_detail THEN has_fulltext ELSE NULL END AS has_fulltext,
  is_retracted, is_paratext,
  {snapshot_date} AS snapshot_date,
  {object_key} AS snapshot_object,
  {object_etag} AS snapshot_object_etag,
  1 AS scan_pass
FROM classified
) TO {output_sql} (FORMAT parquet, COMPRESSION zstd, ROW_GROUP_SIZE 122880);
"""


def _state_connection(path: Path) -> sqlite3.Connection:
    connection = sqlite3.connect(path, timeout=60)
    connection.execute("PRAGMA journal_mode=WAL")
    connection.execute("PRAGMA busy_timeout=60000")
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS shards (
          object_key TEXT PRIMARY KEY,
          reduction_id TEXT,
          object_etag TEXT NOT NULL,
          input_bytes INTEGER NOT NULL,
          expected_records INTEGER NOT NULL,
          output_path TEXT,
          output_bytes INTEGER,
          output_sha256 TEXT,
          output_records INTEGER,
          network_bytes INTEGER NOT NULL DEFAULT 0,
          free_bytes_before INTEGER,
          peak_observed_used_bytes INTEGER,
          status TEXT NOT NULL,
          started_at TEXT,
          completed_at TEXT,
          error TEXT
        )
        """
    )
    columns = {row[1] for row in connection.execute("PRAGMA table_info(shards)")}
    if "reduction_id" not in columns:
        connection.execute("ALTER TABLE shards ADD COLUMN reduction_id TEXT")
    if "free_bytes_before" not in columns:
        connection.execute("ALTER TABLE shards ADD COLUMN free_bytes_before INTEGER")
    if "peak_observed_used_bytes" not in columns:
        connection.execute(
            "ALTER TABLE shards ADD COLUMN peak_observed_used_bytes INTEGER"
        )
    connection.execute(
        """
        CREATE TABLE IF NOT EXISTS download_events (
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          object_key TEXT NOT NULL,
          reduction_id TEXT NOT NULL,
          bytes INTEGER NOT NULL,
          completed_at TEXT NOT NULL
        )
        """
    )
    connection.execute(
        "CREATE TABLE IF NOT EXISTS state_metadata (key TEXT PRIMARY KEY, value TEXT)"
    )
    connection.execute("BEGIN IMMEDIATE")
    migrated = connection.execute(
        "SELECT 1 FROM state_metadata WHERE key='download_events_migrated_v1'"
    ).fetchone()
    if not migrated:
        connection.execute(
            "INSERT INTO download_events(object_key,reduction_id,bytes,completed_at) "
            "SELECT object_key,coalesce(reduction_id,'legacy'),network_bytes,"
            "coalesce(completed_at,started_at,?) FROM shards "
            "WHERE status='complete' AND network_bytes>0",
            (utc_now(),),
        )
        connection.execute(
            "INSERT INTO state_metadata(key,value) VALUES "
            "('download_events_migrated_v1',?)",
            (utc_now(),),
        )
    connection.commit()
    return connection


def _duckdb_scalar(duckdb: Path, query: str) -> str:
    result = _run([str(duckdb), "-noheader", "-csv", "-c", query])
    if result.returncode:
        raise PipelineError(f"DuckDB query failed: {result.stderr.strip()}")
    return result.stdout.strip()


def _verify_completed_part(
    connection: sqlite3.Connection, duckdb: Path, shard: dict[str, Any]
) -> bool:
    row = connection.execute(
        "SELECT reduction_id, object_etag, output_path, output_bytes, output_sha256, "
        "output_records, status "
        "FROM shards WHERE object_key=?",
        (shard["key"],),
    ).fetchone()
    if (
        not row
        or row[-1] != "complete"
        or row[0] != REDUCTION_ID
        or row[1] != shard["etag"]
    ):
        return False
    path = Path(row[2])
    if (
        not path.is_file()
        or path.stat().st_size != row[3]
        or sha256_file(path) != row[4]
    ):
        return False
    count = int(
        _duckdb_scalar(
            duckdb, f"SELECT count(*) FROM read_parquet({sql_quote(str(path))})"
        )
    )
    return count == row[5] == shard["record_count"]


def scan_snapshot(
    layout: Layout,
    duckdb: Path,
    *,
    start: int = 0,
    limit: int | None = None,
) -> dict[str, Any]:
    layout.create()
    if not duckdb.is_file():
        raise PipelineError(f"DuckDB CLI is missing: {duckdb}")
    snapshot_path = layout.snapshot / "works_snapshot.json"
    if not snapshot_path.is_file():
        raise PipelineError("run snapshot before scan")
    if not (layout.riemann / "seeds.jsonl").is_file():
        raise PipelineError("run prepare-seeds before scan")
    snapshot = json.loads(snapshot_path.read_text(encoding="utf-8"))
    openalex, dois, titles = _seed_lists(layout)
    parts = layout.reduced / "works_parts"
    parts.mkdir(parents=True, exist_ok=True)
    connection = _state_connection(layout.state / "scan.sqlite3")
    s3 = _s3_client()
    objects = snapshot["parquet_objects"][start:]
    if limit is not None:
        objects = objects[:limit]
    processed = skipped = failures = network_bytes = 0
    for shard in objects:
        output = parts / f"part_{shard['index']:04d}.parquet"
        temp = layout.tmp / f"scan_{shard['index']:04d}.parquet"
        if _verify_completed_part(connection, duckdb, shard):
            skipped += 1
            continue
        storage = assert_free_space(layout, shard["content_length"] * 2)
        connection.execute(
            "INSERT OR REPLACE INTO shards "
            "(object_key,reduction_id,object_etag,input_bytes,expected_records,free_bytes_before,"
            "status,started_at,error) VALUES (?,?,?,?,?,?,?,?,NULL)",
            (
                shard["key"],
                REDUCTION_ID,
                shard["etag"],
                shard["content_length"],
                shard["record_count"],
                storage["available_bytes"],
                "running",
                utc_now(),
            ),
        )
        connection.commit()
        try:
            partial = temp.with_suffix(".part")
            partial.unlink(missing_ok=True)
            temp.unlink(missing_ok=True)
            head = s3.head_object(Bucket=SNAPSHOT_BUCKET, Key=shard["key"])
            observed_etag = head.get("ETag", "").strip('"')
            if (
                head["ContentLength"] != shard["content_length"]
                or observed_etag != shard["etag"]
            ):
                raise PipelineError(
                    f"snapshot object changed after listing: {shard['key']} "
                    f"size={head['ContentLength']} etag={observed_etag}"
                )
            s3.download_file(SNAPSHOT_BUCKET, shard["key"], str(partial))
            if partial.stat().st_size != shard["content_length"]:
                raise PipelineError(
                    f"download size mismatch for {shard['key']}: "
                    f"{partial.stat().st_size} != {shard['content_length']}"
                )
            connection.execute(
                "INSERT INTO download_events(object_key,reduction_id,bytes,completed_at) "
                "VALUES (?,?,?,?)",
                (shard["key"], REDUCTION_ID, shard["content_length"], utc_now()),
            )
            connection.commit()
            os.replace(partial, temp)
            sql = shard_reduction_sql(
                temp, output, snapshot, shard, openalex, dois, titles
            )
            result = _run([str(duckdb)], input_text=sql)
            if result.returncode:
                raise PipelineError(result.stderr.strip() or result.stdout.strip())
            output_records = int(
                _duckdb_scalar(
                    duckdb,
                    f"SELECT count(*) FROM read_parquet({sql_quote(str(output))})",
                )
            )
            if output_records != shard["record_count"]:
                raise PipelineError(
                    f"reduced row count mismatch: {output_records} != {shard['record_count']}"
                )
            output_hash = sha256_file(output)
            peak_observed = _volume_used_bytes(layout.volume)
            connection.execute(
                "UPDATE shards SET reduction_id=?,output_path=?,output_bytes=?,output_sha256=?,"
                "output_records=?,network_bytes=?,peak_observed_used_bytes=?,status='complete',"
                "completed_at=?,error=NULL "
                "WHERE object_key=?",
                (
                    REDUCTION_ID,
                    str(output),
                    output.stat().st_size,
                    output_hash,
                    output_records,
                    shard["content_length"],
                    peak_observed,
                    utc_now(),
                    shard["key"],
                ),
            )
            connection.commit()
            processed += 1
            network_bytes += shard["content_length"]
        except Exception as error:
            failures += 1
            connection.execute(
                "UPDATE shards SET status='failed',error=? WHERE object_key=?",
                (str(error), shard["key"]),
            )
            connection.commit()
            raise
        finally:
            temp.unlink(missing_ok=True)
            temp.with_suffix(".part").unlink(missing_ok=True)
    counts = dict(
        connection.execute(
            "SELECT status,count(*) FROM shards WHERE reduction_id=? GROUP BY status",
            (REDUCTION_ID,),
        ).fetchall()
    )
    totals = connection.execute(
        "SELECT coalesce(sum(network_bytes),0),coalesce(sum(output_bytes),0),"
        "coalesce(sum(output_records),0),coalesce(max(peak_observed_used_bytes),0),"
        "coalesce(min(free_bytes_before),0) FROM shards "
        "WHERE reduction_id=? AND status='complete'",
        (REDUCTION_ID,),
    ).fetchone()
    network_current = connection.execute(
        "SELECT coalesce(sum(bytes),0) FROM download_events WHERE reduction_id=?",
        (REDUCTION_ID,),
    ).fetchone()[0]
    network_all = connection.execute(
        "SELECT coalesce(sum(bytes),0) FROM download_events"
    ).fetchone()[0]
    result = {
        "updated_at": utc_now(),
        "requested_start": start,
        "requested_limit": limit,
        "processed_this_run": processed,
        "skipped_verified_this_run": skipped,
        "failures_this_run": failures,
        "network_bytes_this_run": network_bytes,
        "state_counts": counts,
        "network_bytes_completed_outputs": totals[0],
        "network_bytes_current_reduction": network_current,
        "network_bytes_total_all_reductions": network_all,
        "reduced_bytes_total": totals[1],
        "works_processed_total": totals[2],
        "peak_observed_volume_used_bytes": totals[3],
        "minimum_free_bytes_before_shard": totals[4],
        "snapshot_work_records": snapshot["works"]["parquet"]["work_records"],
        "snapshot_shards": snapshot["works"]["parquet"]["shard_count"],
    }
    write_json(layout.state / "scan_status.json", result)
    return result


def _parts_glob(layout: Layout) -> str:
    return str(layout.reduced / "works_parts" / "part_*.parquet")


def build_offline_index(layout: Layout, duckdb: Path) -> dict[str, Any]:
    snapshot = json.loads((layout.snapshot / "works_snapshot.json").read_text())
    status = json.loads((layout.state / "scan_status.json").read_text())
    expected = snapshot["works"]["parquet"]["work_records"]
    if status["works_processed_total"] != expected:
        raise PipelineError(
            f"full scan incomplete: {status['works_processed_total']} of {expected} works"
        )
    database = layout.reduced / "openalex.duckdb"
    query_sql = layout.reduced / "query.sql"
    glob = _parts_glob(layout)
    query_text = f"""-- Generated by {PIPELINE_VERSION}; no network access is required.
CREATE OR REPLACE VIEW openalex_works AS
SELECT * FROM read_parquet({sql_quote(glob)}, hive_partitioning=false, union_by_name=true);
CREATE OR REPLACE VIEW math_works AS
SELECT * FROM openalex_works WHERE math_adjacent;
CREATE OR REPLACE VIEW riemann_text_candidates AS
SELECT * FROM openalex_works
WHERE filter_decision IN ('exact_seed','high_confidence','context_required','citation_candidate','rejected_false_positive');
"""
    query_sql.write_text(query_text, encoding="utf-8")
    result = _run([str(duckdb), str(database)], input_text=query_text)
    if result.returncode:
        raise PipelineError(result.stderr.strip())
    counts_query = f"""
SELECT filter_decision,count(*) AS count
FROM read_parquet({sql_quote(glob)}, hive_partitioning=false, union_by_name=true)
GROUP BY filter_decision ORDER BY filter_decision;
"""
    counts_result = _run([str(duckdb), "-csv", "-c", counts_query])
    if counts_result.returncode:
        raise PipelineError(counts_result.stderr.strip())
    rows = list(csv.DictReader(counts_result.stdout.splitlines()))
    counts = {row["filter_decision"]: int(row["count"]) for row in rows}
    result_summary = {
        "generated_at": utc_now(),
        "database": str(database),
        "query_sql": str(query_sql),
        "works": expected,
        "filter_decision_counts": counts,
        "database_bytes": database.stat().st_size,
        "query_sql_sha256": sha256_file(query_sql),
        "api_required": False,
    }
    write_json(layout.reduced / "index_summary.json", result_summary)
    return result_summary


def resolve_seed_mappings(layout: Layout, duckdb: Path) -> dict[str, Any]:
    """Resolve every #42 seed against the fully scanned snapshot with ambiguity evidence."""

    output = layout.riemann / "seed_resolution_candidates.jsonl"
    query = f"""
COPY (
 SELECT id,doi,title,authors,publication_year,seed_oa_match,seed_doi_match,
        seed_title_match,snapshot_object,snapshot_object_etag
 FROM read_parquet({sql_quote(_parts_glob(layout))}, hive_partitioning=false, union_by_name=true)
 WHERE seed_match OR seed_title_match ORDER BY id
) TO {sql_quote(str(output))} (FORMAT JSON, ARRAY false);
"""
    result = _run([str(duckdb)], input_text=query)
    if result.returncode:
        raise PipelineError(result.stderr.strip())
    candidates = load_jsonl(output)
    by_oa: dict[str, list[dict[str, Any]]] = defaultdict(list)
    by_doi: dict[str, list[dict[str, Any]]] = defaultdict(list)
    by_title: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for candidate in candidates:
        oa = normalized_openalex_id(candidate.get("id"))
        doi = normalized_doi(candidate.get("doi"))
        title = normalized_title(candidate.get("title"))
        if oa:
            by_oa[oa].append(candidate)
        if doi:
            by_doi[doi].append(candidate)
        if title:
            by_title[title].append(candidate)
    mappings = []
    resolved_ids = []
    for seed in load_jsonl(layout.riemann / "seeds.jsonl"):
        methods: dict[str, set[str]] = defaultdict(set)
        exact_oa = by_oa.get(seed.get("openalex_id"), [])
        exact_doi = by_doi.get(seed.get("doi"), [])
        if exact_oa:
            selected = exact_oa
            for candidate in selected:
                methods[candidate["id"]].add("openalex_id")
        elif exact_doi:
            selected = exact_doi
            for candidate in selected:
                methods[candidate["id"]].add("doi")
        else:
            title_candidates = by_title.get(seed.get("title_normalized"), [])
            seed_author_tokens = {
                normalized_title(author).split()[-1]
                for author in seed.get("authors") or []
                if normalized_title(author)
            }
            author_matches = []
            for candidate in title_candidates:
                candidate_author_tokens = {
                    normalized_title(author).split()[-1]
                    for author in candidate.get("authors") or []
                    if normalized_title(author)
                }
                if seed_author_tokens & candidate_author_tokens:
                    author_matches.append(candidate)
            seed_year = seed.get("year")
            year_matches = [
                candidate
                for candidate in author_matches
                if seed_year is not None
                and candidate.get("publication_year") is not None
                and abs(int(candidate["publication_year"]) - int(seed_year)) <= 1
            ]
            selected = year_matches or author_matches
            method = "title_author_year" if year_matches else "title_author"
            for candidate in selected:
                methods[candidate["id"]].add(method)
        matches = {candidate["id"]: candidate for candidate in selected}
        candidate_rows = [
            {
                "openalex_id": candidate_id,
                "title": matches[candidate_id].get("title"),
                "authors": matches[candidate_id].get("authors") or [],
                "year": matches[candidate_id].get("publication_year"),
                "match_methods": sorted(methods[candidate_id]),
                "snapshot_object": matches[candidate_id].get("snapshot_object"),
                "snapshot_object_etag": matches[candidate_id].get(
                    "snapshot_object_etag"
                ),
            }
            for candidate_id in sorted(matches)
        ]
        status = (
            "resolved"
            if len(candidate_rows) == 1
            else ("unresolved" if not candidate_rows else "ambiguous")
        )
        mappings.append(
            {
                "source_id": seed["source_id"],
                "seed_title": seed["title"],
                "seed_openalex_id": seed.get("openalex_id"),
                "seed_doi": seed.get("doi"),
                "status": status,
                "candidates": candidate_rows,
            }
        )
        if status == "resolved":
            resolved_ids.append(
                {
                    "openalex_id": candidate_rows[0]["openalex_id"],
                    "source_id": seed["source_id"],
                    "match_method": candidate_rows[0]["match_methods"][0],
                }
            )
    mapping_path = layout.riemann / "seed_mapping.jsonl"
    write_jsonl(mapping_path, mappings)
    resolved_path = layout.riemann / "resolved_seed_ids.jsonl"
    write_jsonl(
        resolved_path,
        sorted(resolved_ids, key=lambda row: (row["openalex_id"], row["source_id"])),
    )
    counts = Counter(row["status"] for row in mappings)
    summary = {
        "generated_at": utc_now(),
        "mapping_path": str(mapping_path),
        "mapping_sha256": sha256_file(mapping_path),
        "resolved_ids_path": str(resolved_path),
        "resolved_ids_sha256": sha256_file(resolved_path),
        "resolved_openalex_ids": len(resolved_ids),
        "seed_count": len(mappings),
        "status_counts": dict(sorted(counts.items())),
        "candidate_rows": len(candidates),
    }
    write_json(layout.riemann / "seed_mapping_summary.json", summary)
    return summary


def _graph_scalar(duckdb: Path, database: Path, query: str) -> int:
    result = _run([str(duckdb), str(database), "-noheader", "-csv", "-c", query])
    if result.returncode:
        raise PipelineError(result.stderr.strip())
    return int(result.stdout.strip())


def expand_graph(layout: Layout, duckdb: Path, max_passes: int = 12) -> dict[str, Any]:
    """Run deterministic local citation closure until no new contextual works appear."""

    output = layout.riemann / "graph_v1"
    output.mkdir(parents=True, exist_ok=True)
    database = layout.reduced / "openalex.duckdb"
    if not database.is_file():
        raise PipelineError("run build-index before expand-graph")
    resolved_seed_ids = layout.riemann / "resolved_seed_ids.jsonl"
    if not resolved_seed_ids.is_file():
        raise PipelineError("run resolve-seeds before expand-graph")
    initial_sql = f"""
SET threads=2;
SET memory_limit='8GB';
CREATE OR REPLACE TABLE graph_acceptance AS
WITH resolved AS (
  SELECT DISTINCT openalex_id AS id
  FROM read_json_auto({sql_quote(str(resolved_seed_ids))})
)
SELECT w.id,0::INTEGER AS graph_pass,
  CASE WHEN r.id IS NOT NULL THEN 'exact_resolved_seed'
       ELSE 'global_high_confidence_text' END AS acceptance_reason
FROM openalex_works w LEFT JOIN resolved r USING(id)
WHERE w.exclusion_rule IS NULL AND NOT coalesce(w.is_retracted,false)
  AND (r.id IS NOT NULL
       OR (w.text_score>=3 AND w.math_adjacent AND NOT coalesce(w.is_paratext,false)));
CREATE OR REPLACE TABLE semantic_review_ids(
  id VARCHAR PRIMARY KEY, first_graph_pass INTEGER, reason VARCHAR
);
"""
    result = _run([str(duckdb), str(database)], input_text=initial_sql)
    if result.returncode:
        raise PipelineError(result.stderr.strip())
    initial = _graph_scalar(duckdb, database, "SELECT count(*) FROM graph_acceptance")
    seed_count = _graph_scalar(
        duckdb,
        database,
        "SELECT count(*) FROM graph_acceptance "
        "WHERE acceptance_reason='exact_resolved_seed'",
    )
    passes: list[dict[str, Any]] = [
        {
            "pass": 0,
            "frontier_size": initial,
            "candidates_inspected": initial,
            "newly_accepted": initial,
            "duplicates_or_known": 0,
            "false_positive_exclusions": 0,
            "interpretation": (
                "Frozen #42 seeds plus global high-confidence mathematical title/abstract rules; "
                "this is deterministic discovery evidence, not a source-quality judgment."
            ),
        }
    ]
    saturated = False
    for pass_number in range(1, max_passes + 1):
        sql = f"""
SET threads=2;
SET memory_limit='8GB';
CREATE OR REPLACE TABLE graph_frontier AS
SELECT id FROM graph_acceptance WHERE graph_pass={pass_number - 1};
CREATE OR REPLACE TABLE graph_frontier_references AS
SELECT DISTINCT unnest(w.referenced_works) AS id
FROM openalex_works w JOIN graph_frontier f USING(id)
WHERE w.referenced_works IS NOT NULL;
CREATE OR REPLACE TABLE graph_reverse_citers AS
SELECT DISTINCT w.id
FROM openalex_works w, unnest(w.referenced_works) AS reference(id)
JOIN graph_frontier f ON f.id=reference.id
WHERE w.referenced_works IS NOT NULL;
CREATE OR REPLACE TABLE graph_adjacent AS
SELECT DISTINCT id FROM (
  SELECT id FROM graph_frontier_references
  UNION ALL SELECT id FROM graph_reverse_citers
);
CREATE OR REPLACE TABLE graph_novel AS
SELECT w.* FROM openalex_works w JOIN graph_adjacent a USING(id)
WHERE NOT EXISTS (SELECT 1 FROM graph_acceptance g WHERE g.id=w.id);
INSERT OR IGNORE INTO semantic_review_ids
SELECT id,{pass_number},'citation_adjacent_without_deterministic_text_signal'
FROM graph_novel
WHERE exclusion_rule IS NULL AND text_score=0 AND math_adjacent
  AND coalesce(cited_by_count,0)>=20 AND NOT coalesce(is_retracted,false);
INSERT INTO graph_acceptance
SELECT id,{pass_number},'citation_adjacent_contextual_text'
FROM graph_novel
WHERE exclusion_rule IS NULL AND text_score>0 AND math_adjacent
  AND NOT coalesce(is_retracted,false) AND NOT coalesce(is_paratext,false);
"""
        result = _run([str(duckdb), str(database)], input_text=sql)
        if result.returncode:
            raise PipelineError(
                f"graph pass {pass_number} failed: {result.stderr.strip()}"
            )
        frontier = _graph_scalar(
            duckdb, database, "SELECT count(*) FROM graph_frontier"
        )
        inspected = _graph_scalar(duckdb, database, "SELECT count(*) FROM graph_novel")
        accepted = _graph_scalar(
            duckdb,
            database,
            f"SELECT count(*) FROM graph_acceptance WHERE graph_pass={pass_number}",
        )
        excluded = _graph_scalar(
            duckdb,
            database,
            "SELECT count(*) FROM graph_novel WHERE exclusion_rule IS NOT NULL",
        )
        queue_new = _graph_scalar(
            duckdb,
            database,
            f"SELECT count(*) FROM semantic_review_ids WHERE first_graph_pass={pass_number}",
        )
        passes.append(
            {
                "pass": pass_number,
                "frontier_size": frontier,
                "candidates_inspected": inspected,
                "newly_accepted": accepted,
                "duplicates_or_known": max(0, inspected - accepted - excluded),
                "false_positive_exclusions": excluded,
                "semantic_review_queue_new": queue_new,
                "frontier_overlap_previous": 0,
            }
        )
        if accepted == 0:
            saturated = True
            passes[-1]["saturated"] = True
            passes[-1]["interpretation"] = (
                "No new citation-adjacent work satisfied the frozen contextual relevance rule."
            )
            break

    accepted_path = output / "accepted_candidates.parquet"
    rejected_path = output / "rejected_candidates.parquet"
    queue_path = output / "semantic_review_queue.parquet"
    edges_path = output / "citation_edges.parquet"
    duplicates_path = output / "duplicate_groups.parquet"
    export_sql = f"""
SET threads=2;
SET memory_limit='8GB';
COPY (
 SELECT w.*,g.graph_pass,g.acceptance_reason,
   CASE WHEN g.acceptance_reason='exact_resolved_seed' THEN 100 ELSE
     w.text_score*20 + least(coalesce(w.cited_by_count,0),500)/25
     + CASE WHEN g.graph_pass>0 THEN 15 ELSE 0 END
     + CASE WHEN w.open_access.is_oa THEN 5 ELSE 0 END END AS priority_score
 FROM openalex_works w JOIN graph_acceptance g USING(id)
 ORDER BY priority_score DESC,id
) TO {sql_quote(str(accepted_path))} (FORMAT parquet,COMPRESSION zstd);
COPY (
 SELECT * FROM openalex_works WHERE exclusion_rule IS NOT NULL
 ORDER BY exclusion_rule,id
) TO {sql_quote(str(rejected_path))} (FORMAT parquet,COMPRESSION zstd);
COPY (
 SELECT w.*,q.first_graph_pass,q.reason
 FROM openalex_works w JOIN semantic_review_ids q USING(id)
 WHERE NOT EXISTS (SELECT 1 FROM graph_acceptance g WHERE g.id=w.id)
 ORDER BY coalesce(w.cited_by_count,0) DESC,id
) TO {sql_quote(str(queue_path))} (FORMAT parquet,COMPRESSION zstd);
COPY (
 SELECT w.id AS citing_work_id,unnest(w.referenced_works) AS cited_work_id,
   g.graph_pass,w.snapshot_object,w.snapshot_object_etag,w.scan_pass
 FROM openalex_works w JOIN graph_acceptance g USING(id)
 WHERE w.referenced_works IS NOT NULL
 ORDER BY citing_work_id,cited_work_id
) TO {sql_quote(str(edges_path))} (FORMAT parquet,COMPRESSION zstd);
COPY (
 SELECT coalesce(nullif(lower(regexp_replace(w.doi,'^https?://(?:dx\\.)?doi\\.org/','')),''),
                 lower(regexp_replace(w.title,'[^a-zA-Z0-9]+',' ','g'))) AS duplicate_key,
        list(w.id ORDER BY w.id) AS work_ids,count(*) AS work_count
 FROM openalex_works w JOIN graph_acceptance g USING(id)
 GROUP BY duplicate_key HAVING count(*)>1
 ORDER BY work_count DESC,duplicate_key
) TO {sql_quote(str(duplicates_path))} (FORMAT parquet,COMPRESSION zstd);
"""
    result = _run([str(duckdb), str(database)], input_text=export_sql)
    if result.returncode:
        raise PipelineError(result.stderr.strip())
    names = (
        "accepted_candidates",
        "rejected_candidates",
        "semantic_review_queue",
        "citation_edges",
        "duplicate_groups",
    )
    artifacts = []
    counts = {}
    for name in names:
        path = output / f"{name}.parquet"
        counts[name] = int(
            _duckdb_scalar(
                duckdb, f"SELECT count(*) FROM read_parquet({sql_quote(str(path))})"
            )
        )
        artifacts.append(
            {
                "path": str(path),
                "bytes": path.stat().st_size,
                "sha256": sha256_file(path),
            }
        )
    accepted_json = output / "accepted_for_summary.jsonl"
    result = _run(
        [str(duckdb)],
        input_text=f"COPY (SELECT id,title,graph_pass FROM read_parquet({sql_quote(str(accepted_path))})) "
        f"TO {sql_quote(str(accepted_json))} (FORMAT JSON,ARRAY false);",
    )
    if result.returncode:
        raise PipelineError(result.stderr.strip())
    mechanisms_by_pass: dict[int, Counter[str]] = defaultdict(Counter)
    for row in load_jsonl(accepted_json):
        evidence = text_relevance(row.get("title"))
        mechanisms_by_pass[row["graph_pass"]].update(evidence["rules"])
    for item in passes:
        item["mechanism_tags"] = dict(
            sorted(mechanisms_by_pass.get(item["pass"], Counter()).items())
        )
    accepted_json.unlink()
    summary = {
        "generated_at": utc_now(),
        "graph_version": "openalex-riemann-graph-v1",
        "seed_works_in_snapshot": seed_count,
        "saturated": saturated,
        "max_passes": max_passes,
        "counts": counts,
        "passes": passes,
        "artifacts": artifacts,
        "semantic_review": {
            "works_reviewed_by_agent": 0,
            "agent_batches": 0,
            "cached_agent_decisions": 0,
            "policy": (
                "Graph-only ambiguous records are preserved in a queue and are not promoted. "
                "No agent decision is needed for the frozen deterministic accepted tier."
            ),
        },
    }
    write_json(output / "summary.json", summary)
    if not saturated:
        raise PipelineError(
            f"graph expansion still yielded new contextual works at pass {max_passes}"
        )
    return summary


class _TextExtractor(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []
        self.suppressed = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in {"script", "style", "nav"}:
            self.suppressed += 1
        elif tag in {"p", "div", "br", "li", "h1", "h2", "h3", "h4"}:
            self.parts.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style", "nav"} and self.suppressed:
            self.suppressed -= 1
        elif tag in {"p", "div", "li"}:
            self.parts.append("\n")

    def handle_data(self, data: str) -> None:
        if not self.suppressed:
            self.parts.append(data)


def normalize_artifact(
    raw_path: Path, normalized_path: Path, content_type: str
) -> dict[str, Any]:
    normalized_path.parent.mkdir(parents=True, exist_ok=True)
    warnings: list[str] = []
    if raw_path.read_bytes()[:5] == b"%PDF-" or "pdf" in content_type:
        result = _run(["pdftotext", "-layout", str(raw_path), str(normalized_path)])
        if result.returncode:
            raise PipelineError(f"pdftotext failed: {result.stderr.strip()}")
        warnings.append(
            "PDF text extraction may degrade formulas or reading order; raw retained"
        )
        media_type = "application/pdf"
    elif "html" in content_type or raw_path.suffix.lower() in {".html", ".htm"}:
        parser = _TextExtractor()
        parser.feed(raw_path.read_text(encoding="utf-8", errors="replace"))
        text = html.unescape("".join(parser.parts))
        text = re.sub(r"[ \t]+", " ", text)
        text = re.sub(r"\n{3,}", "\n\n", text).strip() + "\n"
        normalized_path.write_text(text, encoding="utf-8")
        warnings.append("HTML extraction removes navigation/script/style content")
        media_type = "text/html"
    else:
        text = raw_path.read_text(encoding="utf-8", errors="replace")
        normalized_path.write_text(text, encoding="utf-8")
        media_type = content_type or "text/plain"
    text = normalized_path.read_text(encoding="utf-8", errors="replace")
    printable = sum(char.isprintable() or char in "\n\r\t" for char in text)
    alphabetic = sum(char.isalpha() for char in text)
    metrics = {
        "bytes": normalized_path.stat().st_size,
        "lines": len(text.splitlines()),
        "characters": len(text),
        "words": len(re.findall(r"\b[^\W\d_][\w'’-]*\b", text, re.UNICODE)),
        "printable_ratio": round(printable / max(1, len(text)), 5),
        "alphabetic_ratio": round(alphabetic / max(1, len(text)), 5),
        "replacement_characters": text.count("\ufffd"),
    }
    minimum_bytes = 10_000 if media_type == "text/html" else 5_000
    minimum_words = 1_800 if media_type == "text/html" else 500
    if (
        metrics["bytes"] < minimum_bytes
        or metrics["words"] < minimum_words
        or metrics["alphabetic_ratio"] < 0.30
    ):
        raise PipelineError(f"normalized text failed quality floor: {metrics}")
    return {"media_type": media_type, "warnings": warnings, "quality": metrics}


def candidate_urls(record: dict[str, Any]) -> list[str]:
    urls: list[str] = []

    def add(value: Any) -> None:
        if (
            isinstance(value, str)
            and value.startswith(("http://", "https://"))
            and value not in urls
        ):
            urls.append(value)

    best = record.get("best_oa_location") or {}
    primary = record.get("primary_location") or {}
    open_access = record.get("open_access") or {}
    add(best.get("pdf_url"))
    add(open_access.get("oa_url"))
    add(primary.get("pdf_url"))
    for location in record.get("locations") or []:
        add((location or {}).get("pdf_url"))
    identifiers = record.get("ids") or {}
    arxiv = identifiers.get("arxiv") if isinstance(identifiers, dict) else None
    if arxiv:
        arxiv_id = arxiv.rsplit("/", 1)[-1]
        add(f"https://arxiv.org/pdf/{arxiv_id}")
    return urls


def _safe_id(openalex_id: str) -> str:
    value = normalized_openalex_id(openalex_id)
    if not value:
        raise PipelineError(f"invalid OpenAlex work ID: {openalex_id}")
    return value.rsplit("/", 1)[-1].lower()


def _robots_allowed(
    url: str,
    user_agent: str,
    cache: dict[str, urllib.robotparser.RobotFileParser],
) -> bool:
    parsed = urllib.parse.urlparse(url)
    origin = f"{parsed.scheme}://{parsed.netloc}"
    if origin not in cache:
        parser = urllib.robotparser.RobotFileParser(f"{origin}/robots.txt")
        try:
            import requests

            response = requests.get(
                f"{origin}/robots.txt",
                headers={"User-Agent": user_agent},
                timeout=15,
            )
            if response.status_code == 200:
                parser.parse(response.text.splitlines())
            elif response.status_code in {401, 403} or response.status_code >= 500:
                parser.disallow_all = True
            else:
                parser.allow_all = True
        except Exception:
            # A transiently unavailable robots policy is handled conservatively.
            parser = urllib.robotparser.RobotFileParser()
            parser.set_url(f"{origin}/robots.txt")
            parser.disallow_all = True
        cache[origin] = parser
    return cache[origin].can_fetch(user_agent, url)


def _download_url(
    url: str,
    target: Path,
    *,
    user_agent: str,
    robots_cache: dict[str, urllib.robotparser.RobotFileParser],
    timeout: int = 90,
) -> dict[str, Any]:
    import requests

    if not _robots_allowed(url, user_agent, robots_cache):
        raise PipelineError("robots_disallowed")
    headers = {
        "User-Agent": user_agent,
        "Accept": "application/pdf,text/html,text/plain,*/*;q=0.2",
    }
    response = requests.get(
        url, headers=headers, timeout=timeout, stream=True, allow_redirects=True
    )
    if response.status_code == 429 or response.status_code >= 500:
        retry = response.headers.get("Retry-After")
        raise PipelineError(
            f"retryable_http_{response.status_code};retry_after={retry}"
        )
    if response.status_code >= 400:
        raise PipelineError(f"terminal_http_{response.status_code}")
    target.parent.mkdir(parents=True, exist_ok=True)
    partial = target.with_suffix(target.suffix + ".part")
    with partial.open("wb") as stream:
        for chunk in response.iter_content(chunk_size=1024 * 1024):
            if chunk:
                stream.write(chunk)
    if partial.stat().st_size < 1_000:
        partial.unlink(missing_ok=True)
        raise PipelineError("response_too_small")
    os.replace(partial, target)
    return {
        "effective_url": response.url,
        "content_type": response.headers.get("Content-Type", "")
        .split(";", 1)[0]
        .lower(),
        "content_length": target.stat().st_size,
        "license_header": response.headers.get("License"),
    }


def _export_candidates_json(layout: Layout, duckdb: Path, path: Path) -> None:
    parquet = layout.riemann / "graph_v1" / "accepted_candidates.parquet"
    query = f"""
COPY (
 SELECT * FROM read_parquet({sql_quote(str(parquet))})
 ORDER BY priority_score DESC,id
) TO {sql_quote(str(path))} (FORMAT JSON, ARRAY false);
"""
    result = _run([str(duckdb)], input_text=query)
    if result.returncode:
        raise PipelineError(result.stderr.strip())


def acquire_fulltext(
    layout: Layout,
    duckdb: Path,
    *,
    max_candidates: int = 100,
    max_successes: int = 25,
) -> dict[str, Any]:
    """Acquire public full text with persistent per-route state and no agent calls."""

    work_root = layout.riemann / "acquisition_v1"
    raw_root = work_root / "raw"
    normalized_root = work_root / "normalized"
    work_root.mkdir(parents=True, exist_ok=True)
    candidate_path = work_root / "candidates.jsonl"
    _export_candidates_json(layout, duckdb, candidate_path)
    all_records = load_jsonl(candidate_path)
    seeds = load_jsonl(layout.riemann / "seeds.jsonl")
    acquired_oa = {
        row["openalex_id"]
        for row in seeds
        if row.get("openalex_id")
        and str(row.get("acquisition_status", "")).startswith("acquired")
    }
    acquired_doi = {
        row["doi"]
        for row in seeds
        if row.get("doi")
        and str(row.get("acquisition_status", "")).startswith("acquired")
    }
    seeds_by_source = {row["source_id"]: row for row in seeds}
    seed_source_by_oa: dict[str, str] = {}
    mapping_path = layout.riemann / "seed_mapping.jsonl"
    if mapping_path.is_file():
        for mapping in load_jsonl(mapping_path):
            if mapping["status"] == "resolved":
                seed_source_by_oa[mapping["candidates"][0]["openalex_id"]] = mapping[
                    "source_id"
                ]
    acquired_oa.update(
        openalex_id
        for openalex_id, source_id in seed_source_by_oa.items()
        if str(
            seeds_by_source.get(source_id, {}).get("acquisition_status", "")
        ).startswith("acquired")
    )
    seed_candidates = [
        row
        for row in all_records
        if row.get("id") in seed_source_by_oa
        and row.get("id") not in acquired_oa
        and normalized_doi(row.get("doi")) not in acquired_doi
    ]
    novel_candidates = [
        row for row in all_records if row.get("id") not in seed_source_by_oa
    ]
    seed_quota = min(len(seed_candidates), math.ceil(max_candidates * 0.6))
    records = (
        seed_candidates[:seed_quota] + novel_candidates[: max_candidates - seed_quota]
    )
    state_path = layout.state / "acquisition.sqlite3"
    connection = sqlite3.connect(state_path)
    connection.execute(
        """CREATE TABLE IF NOT EXISTS attempts(
          openalex_id TEXT, url TEXT, status TEXT, attempted_at TEXT,
          detail TEXT, effective_url TEXT, attempt_count INTEGER NOT NULL DEFAULT 0,
          next_attempt_at REAL, host TEXT, downloaded_bytes INTEGER NOT NULL DEFAULT 0,
          PRIMARY KEY(openalex_id,url))"""
    )
    attempt_columns = {
        row[1] for row in connection.execute("PRAGMA table_info(attempts)")
    }
    if "downloaded_bytes" not in attempt_columns:
        connection.execute(
            "ALTER TABLE attempts ADD COLUMN downloaded_bytes INTEGER NOT NULL DEFAULT 0"
        )
    successes: list[dict[str, Any]] = []
    prior_successes: dict[str, dict[str, Any]] = {}
    prior_manifest = work_root / "acquired.jsonl"
    if prior_manifest.is_file():
        for row in load_jsonl(prior_manifest):
            raw = Path(row["raw_path"])
            normalized = Path(row["normalized_path"])
            if (
                raw.is_file()
                and normalized.is_file()
                and sha256_file(raw) == row["raw_sha256"]
                and sha256_file(normalized) == row["normalized_sha256"]
            ):
                prior_successes[row["openalex_id"]] = row
    unavailable: list[dict[str, Any]] = []
    user_agent = (
        "MathiaOpenAlexDiscovery/1.0 (research; contact: codex@example.invalid)"
    )
    host_last_request: dict[str, float] = {}
    robots_cache: dict[str, urllib.robotparser.RobotFileParser] = {}
    duplicate_map: dict[str, list[str]] = defaultdict(list)
    duplicates_parquet = layout.riemann / "graph_v1" / "duplicate_groups.parquet"
    if duplicates_parquet.is_file():
        duplicates_json = work_root / "duplicate_groups.jsonl"
        result = _run(
            [str(duckdb)],
            input_text=f"COPY (SELECT work_ids FROM read_parquet({sql_quote(str(duplicates_parquet))})) "
            f"TO {sql_quote(str(duplicates_json))} (FORMAT JSON,ARRAY false);",
        )
        if result.returncode:
            raise PipelineError(result.stderr.strip())
        for group in load_jsonl(duplicates_json):
            for work_id in group["work_ids"]:
                duplicate_map[work_id].extend(
                    candidate for candidate in group["work_ids"] if candidate != work_id
                )
        duplicates_json.unlink()
    for record in records:
        if len(successes) >= max_successes:
            break
        work_id = record["id"]
        if work_id in prior_successes:
            successes.append(prior_successes[work_id])
            continue
        safe = _safe_id(work_id)
        urls = candidate_urls(record)
        route_errors = []
        acquired = None
        for url in urls:
            prior = connection.execute(
                "SELECT status,detail,effective_url,attempt_count,next_attempt_at,downloaded_bytes "
                "FROM attempts WHERE openalex_id=? AND url=?",
                (work_id, url),
            ).fetchone()
            if prior and prior[0] in {"success", "terminal"}:
                if prior[0] == "success":
                    raw_matches = sorted(raw_root.glob(f"{safe}.*"))
                    norm = normalized_root / f"{safe}.txt"
                    if raw_matches and norm.is_file():
                        acquired = (raw_matches[0], norm, prior[2], url, {})
                continue
            if prior and prior[0] == "retryable" and (prior[4] or 0) > time.time():
                route_errors.append(
                    {
                        "url": url,
                        "status": "cooldown",
                        "detail": prior[1],
                        "next_attempt_at": prior[4],
                    }
                )
                continue
            host = urllib.parse.urlparse(url).netloc.lower()
            elapsed = time.monotonic() - host_last_request.get(host, 0)
            if elapsed < 0.75:
                time.sleep(0.75 - elapsed)
            guessed = (
                mimetypes.guess_extension(mimetypes.guess_type(url)[0] or "") or ".bin"
            )
            raw = raw_root / f"{safe}{guessed}"
            normalized = normalized_root / f"{safe}.txt"
            downloaded_path: Path | None = None
            try:
                assert_free_space(layout, 2 * 1024 * 1024 * 1024)
                response = _download_url(
                    url,
                    raw,
                    user_agent=user_agent,
                    robots_cache=robots_cache,
                )
                host_last_request[host] = time.monotonic()
                content_type = response["content_type"]
                suffix = (
                    ".pdf"
                    if raw.read_bytes()[:5] == b"%PDF-"
                    else (".html" if "html" in content_type else ".txt")
                )
                final_raw = raw.with_suffix(suffix)
                if final_raw != raw:
                    os.replace(raw, final_raw)
                downloaded_path = final_raw
                diagnostics = normalize_artifact(final_raw, normalized, content_type)
                connection.execute(
                    "INSERT OR REPLACE INTO attempts "
                    "(openalex_id,url,status,attempted_at,detail,effective_url,attempt_count,"
                    "next_attempt_at,host,downloaded_bytes) VALUES (?,?,?,?,?,?,?,?,?,?)",
                    (
                        work_id,
                        url,
                        "success",
                        utc_now(),
                        None,
                        response["effective_url"],
                        (prior[3] if prior else 0) + 1,
                        None,
                        host,
                        (prior[5] if prior else 0) + final_raw.stat().st_size,
                    ),
                )
                connection.commit()
                acquired = (
                    final_raw,
                    normalized,
                    response["effective_url"],
                    url,
                    diagnostics,
                )
                break
            except Exception as error:
                detail = str(error)
                retryable = (
                    detail.startswith("retryable_http_")
                    or isinstance(error, TimeoutError)
                    or error.__class__.__name__
                    in {"Timeout", "ReadTimeout", "ConnectTimeout"}
                )
                status = "retryable" if retryable else "terminal"
                attempt_count = (prior[3] if prior else 0) + 1
                retry_value = detail.partition("retry_after=")[2].strip()
                retry_after = int(retry_value) if retry_value.isdigit() else 0
                if retry_value and not retry_after:
                    try:
                        retry_date = email.utils.parsedate_to_datetime(retry_value)
                        retry_after = max(
                            0,
                            math.ceil(
                                (
                                    retry_date.astimezone(dt.timezone.utc)
                                    - dt.datetime.now(dt.timezone.utc)
                                ).total_seconds()
                            ),
                        )
                    except (TypeError, ValueError, OverflowError):
                        retry_after = 0
                deterministic_jitter = (
                    int(hashlib.sha256(f"{work_id}|{url}".encode()).hexdigest()[:4], 16)
                    % 11
                )
                delay = max(
                    retry_after,
                    min(900, 5 * (2 ** min(attempt_count, 7)) + deterministic_jitter),
                )
                next_attempt = time.time() + delay if retryable else None
                retained_download = downloaded_path or raw
                downloaded_bytes = (
                    retained_download.stat().st_size
                    if retained_download.is_file()
                    else 0
                )
                connection.execute(
                    "INSERT OR REPLACE INTO attempts "
                    "(openalex_id,url,status,attempted_at,detail,effective_url,attempt_count,"
                    "next_attempt_at,host,downloaded_bytes) VALUES (?,?,?,?,?,?,?,?,?,?)",
                    (
                        work_id,
                        url,
                        status,
                        utc_now(),
                        detail,
                        None,
                        attempt_count,
                        next_attempt,
                        host,
                        (prior[5] if prior else 0) + downloaded_bytes,
                    ),
                )
                connection.commit()
                route_errors.append({"url": url, "status": status, "detail": detail})
                retained_download.unlink(missing_ok=True)
                normalized.unlink(missing_ok=True)
        if acquired:
            raw, normalized, effective_url, route, diagnostics = acquired
            successes.append(
                {
                    "source_id": seed_source_by_oa.get(work_id, f"openalex_{safe}"),
                    "openalex_id": work_id,
                    "title": record.get("title"),
                    "authors": record.get("authors") or [],
                    "year": record.get("publication_year"),
                    "type": record.get("type"),
                    "doi": normalized_doi(record.get("doi")),
                    "ids": record.get("ids") or {},
                    "priority": record.get("priority_score"),
                    "relevance": {
                        "filter_decision": record.get("filter_decision"),
                        "text_score": record.get("text_score"),
                        "graph_pass": record.get("graph_pass"),
                        "acceptance_reason": record.get("acceptance_reason"),
                        "mechanism_tags": text_relevance(record.get("title"))["rules"],
                        "cites_known_seed": bool(record.get("cites_seed")),
                    },
                    "snapshot": {
                        "date": record.get("snapshot_date"),
                        "object": record.get("snapshot_object"),
                        "object_etag": record.get("snapshot_object_etag"),
                        "pass": record.get("scan_pass"),
                    },
                    "raw_path": str(raw),
                    "raw_sha256": sha256_file(raw),
                    "raw_bytes": raw.stat().st_size,
                    "normalized_path": str(normalized),
                    "normalized_sha256": sha256_file(normalized),
                    "normalized_bytes": normalized.stat().st_size,
                    "normalized_lines": len(
                        normalized.read_text(errors="replace").splitlines()
                    ),
                    "acquisition_route": route,
                    "effective_url": effective_url,
                    "access_boundary": "publicly accessible; redistribution rights not inferred",
                    "license": (record.get("best_oa_location") or {}).get("license"),
                    "normalization": diagnostics,
                    "duplicate_relationships": sorted(
                        set(duplicate_map.get(work_id, []))
                    ),
                }
            )
        else:
            unavailable.append(
                {
                    "openalex_id": work_id,
                    "title": record.get("title"),
                    "priority": record.get("priority_score"),
                    "urls_considered": len(urls),
                    "route_errors": route_errors,
                    "status": "discovery_only_unavailable",
                }
            )
    write_jsonl(work_root / "acquired.jsonl", successes)
    write_jsonl(work_root / "discovery_only_unavailable.jsonl", unavailable)
    network_bytes = connection.execute(
        "SELECT coalesce(sum(downloaded_bytes),0) FROM attempts"
    ).fetchone()[0]
    result = {
        "updated_at": utc_now(),
        "candidates_considered": len(records),
        "full_text_acquired": len(successes),
        "normalized_usable": len(successes),
        "discovery_only_unavailable": len(unavailable),
        "agent_network_calls": 0,
        "network_bytes_downloaded": network_bytes,
        "acquired_manifest": str(work_root / "acquired.jsonl"),
        "unavailable_manifest": str(work_root / "discovery_only_unavailable.jsonl"),
    }
    write_json(work_root / "summary.json", result)
    return result


def freeze_handoff(
    layout: Layout, version: str = "riemann_fulltext_v1"
) -> dict[str, Any]:
    source_root = layout.riemann / "acquisition_v1"
    target = layout.handoffs / version
    freeze_path = target / "freeze.json"
    if target.exists():
        raise PipelineError(f"immutable handoff already exists: {target}")
    acquired = load_jsonl(source_root / "acquired.jsonl")
    if not acquired:
        raise PipelineError("cannot freeze a handoff with no usable full text")
    (target / "raw").mkdir(parents=True)
    (target / "normalized").mkdir()
    frozen_rows = []
    for row in acquired:
        raw_source = Path(row["raw_path"])
        normalized_source = Path(row["normalized_path"])
        raw_target = target / "raw" / raw_source.name
        normalized_target = target / "normalized" / normalized_source.name
        shutil.copyfile(raw_source, raw_target)
        shutil.copyfile(normalized_source, normalized_target)
        if sha256_file(raw_target) != row["raw_sha256"]:
            raise PipelineError(f"raw copy hash mismatch: {raw_target}")
        if sha256_file(normalized_target) != row["normalized_sha256"]:
            raise PipelineError(f"normalized copy hash mismatch: {normalized_target}")
        frozen = dict(row)
        frozen["raw_path"] = str(raw_target)
        frozen["normalized_path"] = str(normalized_target)
        frozen["handoff_version"] = version
        frozen_rows.append(frozen)
    manifest = target / "manifest.jsonl"
    write_jsonl(manifest, frozen_rows)
    files = []
    for path in sorted(item for item in target.rglob("*") if item.is_file()):
        files.append(
            {
                "path": str(path.relative_to(target)),
                "bytes": path.stat().st_size,
                "sha256": sha256_file(path),
            }
        )
    content = {
        "handoff_version": version,
        "pipeline_version": PIPELINE_VERSION,
        "frozen_at": utc_now(),
        "source_count": len(frozen_rows),
        "manifest_sha256": sha256_file(manifest),
        "files": files,
        "consumer_contract": (
            "Issue #42 reads normalized_path locally with zero network requests; this directory "
            "must be retained or copied before /mnt/openalex is detached."
        ),
        "immutable": True,
    }
    content["freeze_id"] = (
        "openalex_handoff_" + hashlib.sha256(canonical_json(content)).hexdigest()
    )
    write_json(freeze_path, content)
    os.chmod(target, 0o555)
    for directory, _, filenames in os.walk(target):
        os.chmod(directory, 0o555)
        for filename in filenames:
            os.chmod(Path(directory) / filename, 0o444)
    return content


def verify_handoff(path: Path) -> list[str]:
    errors = []
    freeze_path = path / "freeze.json"
    if not freeze_path.is_file():
        return ["missing freeze.json"]
    freeze = json.loads(freeze_path.read_text())
    for item in freeze["files"]:
        target = path / item["path"]
        if not target.is_file():
            errors.append(f"missing {item['path']}")
        elif target.stat().st_size != item["bytes"]:
            errors.append(f"byte mismatch {item['path']}")
        elif sha256_file(target) != item["sha256"]:
            errors.append(f"hash mismatch {item['path']}")
    manifest = path / "manifest.jsonl"
    if manifest.is_file():
        for row in load_jsonl(manifest):
            for prefix in ("raw", "normalized"):
                target = Path(row[f"{prefix}_path"])
                if (
                    not target.is_file()
                    or sha256_file(target) != row[f"{prefix}_sha256"]
                ):
                    errors.append(f"{prefix} artifact mismatch for {row['source_id']}")
    return errors


def execution_brief(layout: Layout) -> dict[str, Any]:
    snapshot = json.loads((layout.snapshot / "works_snapshot.json").read_text())
    seeds = json.loads((layout.riemann / "seed_summary.json").read_text())
    runtime: dict[str, Any] = {"python": sys.version, "platform": sys.platform}
    if DEFAULT_DUCKDB.is_file():
        version = _run([str(DEFAULT_DUCKDB), "--version"])
        runtime["duckdb"] = {
            "path": str(DEFAULT_DUCKDB),
            "version": version.stdout.strip(),
            "sha256": sha256_file(DEFAULT_DUCKDB),
            "distribution_url": (
                "https://github.com/duckdb/duckdb/releases/download/v1.3.2/"
                "duckdb_cli-linux-amd64.zip"
            ),
        }
    try:
        import boto3
        import botocore

        runtime["boto3"] = boto3.__version__
        runtime["botocore"] = botocore.__version__
    except ImportError:
        pass
    pdftotext = _run(["pdftotext", "-v"])
    runtime["pdftotext"] = (pdftotext.stderr or pdftotext.stdout).splitlines()[0]
    brief = {
        "pipeline_version": PIPELINE_VERSION,
        "issue": 46,
        "generated_at": utc_now(),
        "paths": dataclasses.asdict(layout),
        "snapshot_date": snapshot["snapshot_date"],
        "snapshot_manifest_sha256": snapshot["manifest_objects"]["parquet"]["sha256"],
        "mode": snapshot["mode"],
        "volume": snapshot["volume"],
        "seed_inventory_sha256": seeds["inventory_sha256"],
        "seed_source_revision": seeds["source_revision"],
        "seed_counts": {
            key: value for key, value in seeds.items() if key.endswith("_count")
        },
        "runtime": runtime,
        "invariants": [
            "bulk/cache/temp/reduced/full-text bytes stay under /mnt/openalex",
            "abort before crossing the 20% attached-volume free-space floor",
            "OpenAlex metadata is discovery evidence, not trainable mathematical source text",
            "issue #42 corpus and freeze files are never rewritten by this pipeline",
            "only hash-bound usable local text enters a frozen full-text handoff",
            "no LLM is used in snapshot scan, graph construction, acquisition, or normalization",
        ],
        "positive_stop": "OPENALEX_OFFLINE_DISCOVERY_READY",
        "blockers": [
            "OPENALEX_STORAGE_BLOCKER",
            "OPENALEX_SNAPSHOT_BLOCKER",
            "OPENALEX_RELEVANCE_BLOCKER",
            "OPENALEX_INTEGRITY_BLOCKER",
        ],
    }
    brief["paths"] = {key: str(value) for key, value in brief["paths"].items()}
    write_json(layout.state / "execution_brief.json", brief)
    return brief


def stage_evidence(
    layout: Layout,
    output: Path,
    handoff_version: str = "riemann_fulltext_v1",
) -> dict[str, Any]:
    """Stage compact Git-eligible evidence outside the worktree for apply_patch review."""

    if output.exists() and any(output.iterdir()):
        raise PipelineError(f"evidence staging directory is not empty: {output}")
    output.mkdir(parents=True, exist_ok=True)
    required = {
        "snapshot": layout.snapshot / "works_snapshot.json",
        "brief": layout.state / "execution_brief.json",
        "scan": layout.state / "scan_status.json",
        "index": layout.reduced / "index_summary.json",
        "seed_summary": layout.riemann / "seed_summary.json",
        "seed_mapping_summary": layout.riemann / "seed_mapping_summary.json",
        "seed_mapping": layout.riemann / "seed_mapping.jsonl",
        "graph": layout.riemann / "graph_v1" / "summary.json",
        "acquisition": layout.riemann / "acquisition_v1" / "summary.json",
        "unavailable": layout.riemann
        / "acquisition_v1"
        / "discovery_only_unavailable.jsonl",
        "handoff": layout.handoffs / handoff_version / "freeze.json",
        "handoff_manifest": layout.handoffs / handoff_version / "manifest.jsonl",
        "query": layout.reduced / "query.sql",
    }
    missing = [name for name, path in required.items() if not path.is_file()]
    if missing:
        raise PipelineError(f"cannot stage evidence; missing {', '.join(missing)}")
    snapshot = json.loads(required["snapshot"].read_text())
    scan = json.loads(required["scan"].read_text())
    index = json.loads(required["index"].read_text())
    seeds = json.loads(required["seed_summary"].read_text())
    mapping = json.loads(required["seed_mapping_summary"].read_text())
    graph = json.loads(required["graph"].read_text())
    acquisition = json.loads(required["acquisition"].read_text())
    handoff = json.loads(required["handoff"].read_text())
    handoff_errors = verify_handoff(layout.handoffs / handoff_version)
    end_volume = volume_evidence(layout.volume)
    end_root = filesystem_usage(Path("/"))
    root_growth = (
        end_root["used_bytes"] - snapshot["root_filesystem_at_capture"]["used_bytes"]
    )
    volume_root = layout.volume.resolve()
    scan_connection = sqlite3.connect(layout.state / "scan.sqlite3")
    retained_paths = [
        Path(row[0]).resolve()
        for row in scan_connection.execute(
            "SELECT output_path FROM shards WHERE reduction_id=? AND status='complete'",
            (REDUCTION_ID,),
        )
    ]
    retained_paths.extend(
        Path(row[key]).resolve()
        for row in load_jsonl(required["handoff_manifest"])
        for key in ("raw_path", "normalized_path")
    )
    external_path_errors = [
        str(path) for path in retained_paths if not path.is_relative_to(volume_root)
    ]
    full_scan_complete = scan["works_processed_total"] == snapshot["works"]["parquet"][
        "work_records"
    ] and scan["state_counts"] == {
        "complete": snapshot["works"]["parquet"]["shard_count"]
    }
    positive = all(
        (
            full_scan_complete,
            graph.get("saturated") is True,
            handoff["source_count"] > 0,
            not handoff_errors,
            index.get("api_required") is False,
            not external_path_errors,
        )
    )
    decision = (
        "OPENALEX_OFFLINE_DISCOVERY_READY" if positive else "OPENALEX_INTEGRITY_BLOCKER"
    )
    snapshot_summary = {
        key: value for key, value in snapshot.items() if key != "parquet_objects"
    }
    snapshot_summary["parquet_object_count"] = len(snapshot["parquet_objects"])
    write_json(output / "snapshot_summary.json", snapshot_summary)
    copy_names = {
        "seed_summary.json": required["seed_summary"],
        "execution_brief.json": required["brief"],
        "seed_mapping_summary.json": required["seed_mapping_summary"],
        "seed_mapping.jsonl": required["seed_mapping"],
        "graph_summary.json": required["graph"],
        "acquisition_summary.json": required["acquisition"],
        "discovery_only_unavailable.jsonl": required["unavailable"],
        "handoff_freeze.json": required["handoff"],
        "handoff_manifest.jsonl": required["handoff_manifest"],
        "query.sql": required["query"],
    }
    for name, source in copy_names.items():
        shutil.copyfile(source, output / name)
    report = {
        "generated_at": utc_now(),
        "pipeline_version": PIPELINE_VERSION,
        "final_decision": decision,
        "snapshot": {
            "date": snapshot["snapshot_date"],
            "jsonl_compressed_bytes": snapshot["works"]["jsonl"]["bytes"],
            "parquet_bytes_streamed": scan["network_bytes_current_reduction"],
            "parquet_bytes_all_reductions": scan["network_bytes_total_all_reductions"],
            "works_processed": scan["works_processed_total"],
            "shards_processed": scan["state_counts"].get("complete", 0),
            "manifest_sha256": snapshot["manifest_objects"]["parquet"]["sha256"],
            "mode": snapshot["mode"],
        },
        "storage": {
            "device": end_volume["source"],
            "filesystem": end_volume["filesystem"],
            "uuid": end_volume["uuid"],
            "mountpoint": end_volume["mountpoint"],
            "capacity_bytes": end_volume["capacity_bytes"],
            "free_bytes_floor": end_volume["free_bytes_floor"],
            "available_bytes_at_end": end_volume["available_bytes"],
            "peak_observed_used_bytes": scan.get("peak_observed_volume_used_bytes"),
            "reduced_index_bytes": scan["reduced_bytes_total"],
            "handoff_bytes": sum(item["bytes"] for item in handoff["files"]),
            "root_used_bytes_at_capture": snapshot["root_filesystem_at_capture"][
                "used_bytes"
            ],
            "root_used_bytes_at_end": end_root["used_bytes"],
            "root_used_growth_bytes": root_growth,
            "openalex_retained_path_errors": external_path_errors,
        },
        "network": {
            "snapshot_parquet_bytes": scan["network_bytes_current_reduction"],
            "superseded_or_retried_snapshot_bytes": scan[
                "network_bytes_total_all_reductions"
            ]
            - scan["network_bytes_current_reduction"],
            "full_text_bytes": acquisition["network_bytes_downloaded"],
            "total_tracked_bytes": scan["network_bytes_total_all_reductions"]
            + acquisition["network_bytes_downloaded"],
        },
        "seeds": mapping,
        "graph": {
            "counts": graph["counts"],
            "passes": graph["passes"],
            "saturated": graph["saturated"],
        },
        "acquisition": acquisition,
        "handoff": {
            "version": handoff_version,
            "source_count": handoff["source_count"],
            "freeze_id": handoff["freeze_id"],
            "verification_errors": handoff_errors,
            "external_path": str(layout.handoffs / handoff_version),
        },
        "agent_efficiency": {
            "works_processed_deterministically": scan["works_processed_total"],
            "works_sent_to_agent_semantic_review": 0,
            "agent_review_fraction": 0.0,
            "agent_review_batches": 0,
            "candidates_decided_without_llm": graph["counts"]["accepted_candidates"]
            + graph["counts"]["rejected_candidates"],
            "cached_semantic_decisions": 0,
            "agent_bottleneck": False,
        },
        "boundaries": {
            "openalex_metadata_trainable": False,
            "handoff_text_trainable_without_42_quality_gates": False,
            "issue_42_network_requests_required": False,
            "retention": (
                "Do not detach or delete /mnt/openalex until #42 has copied every consumed "
                "hash-bound handoff artifact into its own retained external store."
            ),
            "cleanup": (
                "Temporary shard files are deleted after each checkpoint. Reduced Parquet, scan "
                "state, and frozen handoff bytes are durable. Delete the disposable DuckDB zip/uv "
                "cache only after validation; never delete the frozen handoff automatically."
            ),
        },
        "validation": {
            "full_scan_complete": full_scan_complete,
            "handoff_hashes_valid": not handoff_errors,
            "offline_query_available": index.get("api_required") is False,
            "root_total_growth_observed": root_growth,
            "known_openalex_bulk_path_outside_volume": bool(external_path_errors),
        },
    }
    write_json(output / "run_report.json", report)
    markdown = f"""# OpenAlex offline discovery report

Final decision: `{decision}`

## Snapshot and storage

- OpenAlex snapshot: `{snapshot["snapshot_date"]}`; manifest SHA-256 `{snapshot["manifest_objects"]["parquet"]["sha256"]}`.
- Full works scan: {scan["works_processed_total"]:,} records in {scan["state_counts"].get("complete", 0):,} Parquet shards.
- Cache decision: streaming; compressed JSONL is {snapshot["works"]["jsonl"]["bytes"]:,} bytes versus {snapshot["safe_cache_capacity_bytes"]:,} safe cache bytes.
- Attached volume: `{end_volume["source"]}` / `{end_volume["uuid"]}` at `{end_volume["mountpoint"]}`; 20% floor {end_volume["free_bytes_floor"]:,} bytes.
- Tracked network: {report["network"]["total_tracked_bytes"]:,} bytes; reduced index: {scan["reduced_bytes_total"]:,} bytes.
- Root-disk used-byte change during the captured run: {root_growth:+,}; no bulk artifact path points there.

## Riemann graph and handoff

- #42 seeds: {seeds["relevant_seed_count"]}; mapping states: {json.dumps(mapping["status_counts"], sort_keys=True)}.
- Accepted candidates: {graph["counts"]["accepted_candidates"]:,}; rejected false-positive evidence: {graph["counts"]["rejected_candidates"]:,}; graph-only review queue: {graph["counts"]["semantic_review_queue"]:,}.
- Adaptive expansion saturated: `{graph["saturated"]}` after {len(graph["passes"]) - 1} citation pass(es).
- Full text acquired / normalized / handoff ready: {acquisition["full_text_acquired"]} / {acquisition["normalized_usable"]} / {handoff["source_count"]}.
- Discovery-only unavailable in the attempted priority slice: {acquisition["discovery_only_unavailable"]}.
- Frozen handoff: `{handoff["freeze_id"]}` at `{layout.handoffs / handoff_version}`.

Every handed-off row names and hashes local raw and normalized bytes. #42 consumes those paths with zero network requests. OpenAlex abstracts and metadata remain discovery-only and are not promoted to Mathia source units.

## Agent-compute accounting

The {scan["works_processed_total"]:,}-work scan, seed matching, graph passes, ranking, acquisition, normalization, hashes, and reports were deterministic. Zero candidates were sent to agent semantic review in zero batches; ambiguous graph-only records remain quarantined.

## Retention

Keep the frozen handoff until #42 has copied every consumed artifact into its own retained external store. Temporary shards are already deleted. The volume may be detached or deleted only after that explicit preservation step and a separate owner-authorized operation.
"""
    (output / "REPORT.md").write_text(markdown, encoding="utf-8")
    files = []
    for path in sorted(item for item in output.iterdir() if item.is_file()):
        files.append(
            {
                "path": path.name,
                "bytes": path.stat().st_size,
                "sha256": sha256_file(path),
                **(
                    {"record_count": len(load_jsonl(path))}
                    if path.suffix == ".jsonl"
                    else {}
                ),
            }
        )
    release = {
        "pipeline_version": PIPELINE_VERSION,
        "final_decision": decision,
        "generated_at": utc_now(),
        "files": files,
    }
    release["release_id"] = (
        "openalex_discovery_" + hashlib.sha256(canonical_json(release)).hexdigest()
    )
    write_json(output / "release_manifest.json", release)
    return release


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--volume", type=Path, default=DEFAULT_VOLUME)
    parser.add_argument("--root", type=Path)
    parser.add_argument("--duckdb", type=Path, default=DEFAULT_DUCKDB)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("preflight")
    sub.add_parser("snapshot")
    sub.add_parser("prepare-seeds")
    sub.add_parser("brief")
    scan = sub.add_parser("scan")
    scan.add_argument("--start", type=int, default=0)
    scan.add_argument("--limit", type=int)
    sub.add_parser("build-index")
    sub.add_parser("resolve-seeds")
    sub.add_parser("expand-graph")
    acquire = sub.add_parser("acquire")
    acquire.add_argument("--max-candidates", type=int, default=100)
    acquire.add_argument("--max-successes", type=int, default=25)
    freeze = sub.add_parser("freeze-handoff")
    freeze.add_argument("--version", default="riemann_fulltext_v1")
    verify = sub.add_parser("verify-handoff")
    verify.add_argument("path", type=Path)
    stage = sub.add_parser("stage-evidence")
    stage.add_argument("--output", type=Path, required=True)
    stage.add_argument("--handoff-version", default="riemann_fulltext_v1")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    layout = Layout.from_root(args.volume, args.root)
    if args.command == "preflight":
        result = volume_evidence(layout.volume)
    elif args.command == "snapshot":
        result = snapshot_inventory(layout)
    elif args.command == "prepare-seeds":
        result = prepare_seeds(layout)
    elif args.command == "brief":
        result = execution_brief(layout)
    elif args.command == "scan":
        result = scan_snapshot(layout, args.duckdb, start=args.start, limit=args.limit)
    elif args.command == "build-index":
        result = build_offline_index(layout, args.duckdb)
    elif args.command == "resolve-seeds":
        result = resolve_seed_mappings(layout, args.duckdb)
    elif args.command == "expand-graph":
        result = expand_graph(layout, args.duckdb)
    elif args.command == "acquire":
        result = acquire_fulltext(
            layout,
            args.duckdb,
            max_candidates=args.max_candidates,
            max_successes=args.max_successes,
        )
    elif args.command == "freeze-handoff":
        result = freeze_handoff(layout, args.version)
    elif args.command == "stage-evidence":
        result = stage_evidence(layout, args.output, args.handoff_version)
    else:
        errors = verify_handoff(args.path)
        result = {"valid": not errors, "errors": errors}
        print(json.dumps(result, indent=2, sort_keys=True))
        return int(bool(errors))
    display = result
    if args.command == "snapshot":
        display = {
            key: value for key, value in result.items() if key != "parquet_objects"
        }
        display["parquet_object_count"] = len(result["parquet_objects"])
    print(json.dumps(display, indent=2, sort_keys=True, default=str))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
