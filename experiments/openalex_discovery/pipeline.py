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
AGNOSTIC_RELEASE = REPO_ROOT / "experiments" / "agnostic_mathia_corpus" / "release_v1"
RUN_EVIDENCE = Path(__file__).resolve().parent / "run_v1"
SNAPSHOT_BUCKET = "openalex"
SNAPSHOT_JSONL_MANIFEST = "data/jsonl/manifest.json"
SNAPSHOT_PARQUET_MANIFEST = "data/parquet/manifest.json"
SNAPSHOT_JSONL_WORKS_PREFIX = "data/jsonl/works/"
SNAPSHOT_PARQUET_WORKS_PREFIX = "data/parquet/works/"
FREE_FRACTION_FLOOR = 0.20
PIPELINE_VERSION = "openalex-offline-discovery-v1"
REDUCTION_ID = "openalex-work-locator-v4"
RIEMANN_MECHANISM_TITLE_PATTERN = (
    r"((\briemann (hypothesis|zeta( function)?)\b|\bzeta zeros?\b|"
    r"\bzeros? (of|for) (the )?(riemann )?zeta( function)?\b|"
    r"\b(dirichlet|dedekind|hecke|automorphic|artin|rankin[ -]selberg) "
    r"l[ -]functions?\b|\bzeros? (of|for) (the )?l[ -]functions?\b|"
    r"\bl[ -]functions? zeros?\b).{0,80}"
    r"\b(random matrices?|random matrix theory|unitary ensembles?|quantum chaos|"
    r"computation|computational|compute|computing|verification|verify|history|historical|"
    r"equivalent|criteria?|explicit formulae?|moments?|mollifiers?|spectral|primes?)\b|"
    r"\b(random matrices?|random matrix theory|unitary ensembles?|quantum chaos|"
    r"computation|computational|compute|computing|verification|verify|history|historical|"
    r"equivalent|criteria?|explicit formulae?|moments?|mollifiers?|spectral|primes?)\b"
    r".{0,80}(\briemann (hypothesis|zeta( function)?)\b|\bzeta zeros?\b|"
    r"\bzeros? (of|for) (the )?(riemann )?zeta( function)?\b|"
    r"\b(dirichlet|dedekind|hecke|automorphic|artin|rankin[ -]selberg) "
    r"l[ -]functions?\b|\bzeros? (of|for) (the )?l[ -]functions?\b|"
    r"\bl[ -]functions? zeros?\b))"
)


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
    agnostic: Path
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
            agnostic=actual_root / "agnostic_mathia",
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


# These are bounded retrieval lenses copied from the frozen #44 coverage map in
# operational form.  They rank candidates; they are not an ontology or a claim
# that an OpenAlex title establishes a mathematical mechanism.
AGNOSTIC_LENS_PATTERNS: dict[str, str] = {
    "quotients_and_factorization": (
        r"(quotient (space|group|ring|module)|factorization theorem|kernel and image|"
        r"universal property of (the )?quotient)"
    ),
    "symmetry_and_actions": (
        r"(group action|orbit stabilizer|burnside lemma|polya enumeration|symmetry group)"
    ),
    "decomposition_and_canonical_forms": (
        r"(canonical form|jordan form|primary decomposition|irreducible decomposition|"
        r"structure theorem)"
    ),
    "duality_objects_and_constraints": (
        r"(duality theorem|dual space|pontryagin duality|serre duality|annihilator|"
        r"lagrange duality)"
    ),
    "invariants_and_classification": (
        r"(classification theorem|complete invariant|characteristic class|"
        r"classification of|isomorphism invariant)"
    ),
    "local_to_global": (
        r"(local to global|local global|descent theorem|gluing theorem|hasse principle|"
        r"sheaf cohomology)"
    ),
    "compactness_completeness_existence": (
        r"(compactness theorem|completeness theorem|existence theorem|fixed point theorem|"
        r"weak compactness)"
    ),
    "stability_perturbation_deformation": (
        r"(stability theorem|perturbation theory|deformation theory|structural stability|"
        r"homotopy stability)"
    ),
    "transforms_and_spectralization": (
        r"(spectral theorem|fourier transform|laplace transform|wavelet transform|"
        r"spectral decomposition|diagonalization)"
    ),
    "dimension_intersection_transversality": (
        r"(transversality theorem|intersection theory|dimension theorem|codimension|"
        r"bezout theorem)"
    ),
    "curvature_local_global": (
        r"(gauss bonnet|curvature and topology|comparison geometry|sectional curvature|"
        r"geodesic curvature)"
    ),
    "convexity_separation_optimization": (
        r"(separation theorem|supporting hyperplane|convex duality|convex optimization|"
        r"farkas lemma)"
    ),
    "projectivization_and_compactification": (
        r"(compactification|projectivization|projective completion|points at infinity|"
        r"one point compactification)"
    ),
    "moduli_and_parameter_spaces": (
        r"(moduli space|parameter space|moduli stack|deformation space|"
        r"classification space)"
    ),
    "homotopy_and_obstruction": (
        r"(obstruction theory|homotopy group|homotopy type|fundamental group|"
        r"homotopy equivalence)"
    ),
    "conditioning_independence_concentration": (
        r"(concentration inequality|conditional expectation|independence and|"
        r"large deviation|martingale concentration)"
    ),
    "combinatorial_generation_extremal_bijection": (
        r"(extremal combinatorics|bijective proof|matching theorem|ramsey theorem|"
        r"enumerative combinatorics)"
    ),
    "recursion_and_generating_functions": (
        r"(generating function|generating functions|recurrence relation|"
        r"coefficient extraction|recursive structure)"
    ),
    "universal_properties_and_canonicality": (
        r"(universal property|adjunction|adjoint functor|canonical construction|"
        r"representable functor)"
    ),
    "finite_infinite_transfer": (
        r"(finite to infinite|compactness method|finite character|inverse limit|"
        r"direct limit)"
    ),
    "exact_approximate_completion": (
        r"(completion theorem|best approximation|dense subspace|approximation theorem|"
        r"exact and approximate)"
    ),
    "auxiliary_objects_and_relaxations": (
        r"(convex relaxation|semidefinite relaxation|auxiliary function|"
        r"certificate of infeasibility|linear programming relaxation)"
    ),
    "counterexamples_and_boundary_phenomena": (
        r"(counterexample|counterexamples|failure of|boundary phenomenon|"
        r"necessary but not sufficient)"
    ),
    "geometricization_and_representation_change": (
        r"(geometric representation|geometric interpretation|incidence geometry|"
        r"geometrization|change of representation)"
    ),
    "arithmetic_geometry": (
        r"(elliptic curve|arithmetic geometry|isogeny|frobenius endomorphism|"
        r"rational points)"
    ),
    "stochastic_processes": (
        r"(stochastic process|martingale|hitting time|markov process|"
        r"optional stopping)"
    ),
    "partial_differential_equations": (
        r"(partial differential equation|maximum principle|fundamental solution|"
        r"weak solution|shock wave)"
    ),
    "numerical_analysis": (
        r"(numerical analysis|backward error|forward error|convergence rate|"
        r"numerical stability)"
    ),
}


AGNOSTIC_FAMILY_RULES: tuple[tuple[str, tuple[str, ...], str, str], ...] = (
    (
        "p_adic_hodge_and_etale",
        ("arithmetic_geometry", "local_to_global"),
        r"(p adic hodge|etale cohomology|anabelian geometry|perfectoid)",
        "deeper arithmetic-geometric local/global machinery",
    ),
    (
        "derived_and_higher_structures",
        (
            "decomposition_and_canonical_forms",
            "homotopy_and_obstruction",
            "universal_properties_and_canonicality",
        ),
        r"(derived categor|higher categor|infinity categor|derived algebraic geometry)",
        "higher or derived representation machinery absent from the bounded source panel",
    ),
    (
        "optimal_transport_geometry",
        (
            "duality_objects_and_constraints",
            "convexity_separation_optimization",
            "geometricization_and_representation_change",
        ),
        r"(optimal transport|wasserstein geometr)",
        "geometric/dual representation of optimization and probability",
    ),
    (
        "stochastic_calculus_and_coupling",
        ("stochastic_processes", "conditioning_independence_concentration"),
        r"(stochastic calculus|ito calculus|stochastic coupling|coupling method)",
        "deeper stochastic mechanism than finite-state stopping examples",
    ),
    (
        "stochastic_pde_bridge",
        ("stochastic_processes", "partial_differential_equations"),
        r"(stochastic partial differential|spde|feynman kac)",
        "cross-frontier stochastic/PDE bridge",
    ),
    (
        "microlocal_and_inverse_pde",
        ("partial_differential_equations", "transforms_and_spectralization"),
        r"(microlocal analysis|inverse problem.*partial differential|"
        r"calderon inverse problem)",
        "PDE representation and inverse-problem family beyond the bounded release",
    ),
    (
        "geometric_numerical_integration",
        ("numerical_analysis", "stability_perturbation_deformation"),
        r"(geometric numerical integration|symplectic integrator|backward error analysis)",
        "structure-preserving numerical mechanism",
    ),
    (
        "certified_numerics",
        ("numerical_analysis", "exact_approximate_completion"),
        r"(interval arithmetic|validated numerics|computer assisted proof)",
        "explicit exact-versus-approximate certification boundary",
    ),
    (
        "persistent_and_applied_homology",
        ("homotopy_and_obstruction", "invariants_and_classification"),
        r"(persistent homology|topological data analysis|mapper algorithm)",
        "new use of invariants across topology and data",
    ),
    (
        "tropical_and_toric_geometry",
        (
            "geometricization_and_representation_change",
            "moduli_and_parameter_spaces",
            "arithmetic_geometry",
        ),
        r"(tropical geometry|toric geometry|tropicalization)",
        "representation change with arithmetic/geometric bridges",
    ),
    (
        "noncommutative_geometry",
        (
            "geometricization_and_representation_change",
            "duality_objects_and_constraints",
        ),
        r"(noncommutative geometry|spectral triple)",
        "operator-algebraic geometricization family",
    ),
    (
        "explicit_failure_and_obstruction",
        ("counterexamples_and_boundary_phenomena", "homotopy_and_obstruction"),
        r"(counterexample|failure of.*conjecture|obstruction theory)",
        "source family centered on failure boundaries rather than positive exemplars",
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


def validate_external_layout(layout: Layout) -> dict[str, Any]:
    """Verify every operational path is rooted on the declared volume."""

    evidence = volume_evidence(layout.volume)
    volume_root = layout.volume.resolve()
    operational_root = layout.root.resolve()
    if operational_root == volume_root or not operational_root.is_relative_to(
        volume_root
    ):
        raise PipelineError(
            f"operational root {operational_root} is not beneath volume {volume_root}"
        )
    existing_parent = operational_root
    while not existing_parent.exists():
        existing_parent = existing_parent.parent
    root_device = os.stat(existing_parent).st_dev
    if root_device != evidence["volume_device"]:
        raise PipelineError(
            f"operational root parent {existing_parent} is on device {root_device}, "
            f"not volume device {evidence['volume_device']}"
        )
    return {
        **evidence,
        "operational_root": str(operational_root),
        "operational_root_existing_parent": str(existing_parent),
        "operational_root_device": root_device,
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


def _verify_agnostic_release(release: Path = AGNOSTIC_RELEASE) -> list[str]:
    errors: list[str] = []
    freeze_path = release / "freeze.json"
    if not freeze_path.is_file():
        return [f"missing {freeze_path}"]
    freeze = json.loads(freeze_path.read_text(encoding="utf-8"))
    for item in freeze.get("files", []):
        path = REPO_ROOT / item["path"]
        if not path.is_file():
            errors.append(f"missing {item['path']}")
        elif path.stat().st_size != item["bytes"]:
            errors.append(f"byte mismatch {item['path']}")
        elif sha256_file(path) != item["sha256"]:
            errors.append(f"hash mismatch {item['path']}")
    for item in freeze.get("source_tree", []):
        path = REPO_ROOT / item["path"]
        if not path.is_file() or sha256_file(path) != item["sha256"]:
            errors.append(f"source tree mismatch {item['path']}")
    return errors


def build_agnostic_seed_records(
    release: Path = AGNOSTIC_RELEASE,
) -> list[dict[str, Any]]:
    coverage = json.loads((release / "coverage_map.json").read_text(encoding="utf-8"))
    ecosystems_by_source: dict[str, list[str]] = defaultdict(list)
    for ecosystem in coverage["ecosystems"]:
        for source_id in ecosystem["seed_source_ids"]:
            ecosystems_by_source[source_id].append(ecosystem["ecosystem_id"])
    for record in load_jsonl(release / "records.jsonl"):
        ecosystem_id = (record.get("corpus_local_audit") or {}).get("ecosystem_id")
        if not ecosystem_id:
            continue
        for source_id in record.get("source_ids") or []:
            ecosystems_by_source[source_id].append(ecosystem_id)
    records = []
    for row in load_jsonl(release / "source_inventory.jsonl"):
        canonical_url = row.get("canonical_url") or ""
        acquisition_url = row.get("acquisition_url") or ""
        doi = next(
            (
                normalized_doi(url)
                for url in (canonical_url, acquisition_url)
                if "doi.org/" in url
            ),
            None,
        )
        records.append(
            {
                "source_id": row["source_id"],
                "title": row["title"],
                "title_normalized": normalized_title(row["title"]),
                "authors": row.get("authors") or [],
                "year": None,
                "openalex_id": None,
                "doi": doi,
                "canonical_url": canonical_url,
                "acquisition_url": acquisition_url,
                "acquisition_status": row.get("acquisition_status"),
                "artifact_sha256": (row.get("acquisition") or {}).get(
                    "artifact_sha256"
                ),
                "used_unit_ids": row.get("used_unit_ids") or [],
                "ecosystem_ids": sorted(set(ecosystems_by_source[row["source_id"]])),
                "conceptual_value": row.get("conceptual_value"),
            }
        )
    return sorted(records, key=lambda row: row["source_id"])


def prepare_agnostic_seeds(
    layout: Layout, release: Path = AGNOSTIC_RELEASE
) -> dict[str, Any]:
    layout.create()
    errors = _verify_agnostic_release(release)
    if errors:
        raise PipelineError("invalid #44 release: " + "; ".join(errors))
    freeze_path = release / "freeze.json"
    freeze = json.loads(freeze_path.read_text(encoding="utf-8"))
    coverage_path = release / "coverage_map.json"
    saturation_path = release / "saturation_log.json"
    inventory_path = release / "source_inventory.jsonl"
    records = build_agnostic_seed_records(release)
    seed_path = layout.agnostic / "seeds.jsonl"
    write_jsonl(seed_path, records)
    summary = {
        "generated_at": utc_now(),
        "release_id": freeze["release_id"],
        "freeze_id": freeze["freeze_id"],
        "freeze_sha256": sha256_file(freeze_path),
        "inventory_path": str(inventory_path.relative_to(REPO_ROOT)),
        "inventory_sha256": sha256_file(inventory_path),
        "coverage_map_id": json.loads(coverage_path.read_text())["map_id"],
        "coverage_map_sha256": sha256_file(coverage_path),
        "saturation_log_id": json.loads(saturation_path.read_text())[
            "saturation_log_id"
        ],
        "saturation_log_sha256": sha256_file(saturation_path),
        "pipeline_source_revision": _run(["git", "rev-parse", "HEAD"]).stdout.strip(),
        "release_git_revision": _run(
            ["git", "log", "-1", "--format=%H", "--", str(release)]
        ).stdout.strip(),
        "seed_count": len(records),
        "doi_count": sum(bool(row["doi"]) for row in records),
        "ecosystem_count": len(
            json.loads(coverage_path.read_text(encoding="utf-8"))["ecosystems"]
        ),
        "seed_path": str(seed_path),
        "seed_sha256": sha256_file(seed_path),
        "release_verification_errors": [],
    }
    write_json(layout.agnostic / "seed_summary.json", summary)
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
    legacy_uncertainty = connection.execute(
        "SELECT value FROM state_metadata "
        "WHERE key='legacy_untracked_interrupted_upper_bound_bytes'"
    ).fetchone()
    if not legacy_uncertainty:
        upper_bound = connection.execute(
            "SELECT coalesce(sum(input_bytes),0) FROM shards "
            "WHERE coalesce(reduction_id,'legacy')!=? AND status!='complete'",
            (REDUCTION_ID,),
        ).fetchone()[0]
        connection.execute(
            "INSERT INTO state_metadata(key,value) VALUES "
            "('legacy_untracked_interrupted_upper_bound_bytes',?)",
            (str(upper_bound),),
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
    legacy_untracked_upper_bound = int(
        connection.execute(
            "SELECT value FROM state_metadata "
            "WHERE key='legacy_untracked_interrupted_upper_bound_bytes'"
        ).fetchone()[0]
    )
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
        "legacy_untracked_interrupted_download_upper_bound_bytes": (
            legacy_untracked_upper_bound
        ),
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
SET threads=2;
SET temp_directory={sql_quote(str(layout.tmp / "duckdb_spill"))};
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
SET threads=2;
SET temp_directory={sql_quote(str(layout.tmp / "duckdb_spill"))};
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


def _map_seed_candidates(
    seed: dict[str, Any],
    by_oa: dict[str, list[dict[str, Any]]],
    by_doi: dict[str, list[dict[str, Any]]],
    by_title: dict[str, list[dict[str, Any]]],
) -> tuple[str, list[dict[str, Any]]]:
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
        if year_matches:
            selected = year_matches
            method = "title_author_year"
        elif author_matches:
            selected = author_matches
            method = "title_author"
        else:
            selected = []
            method = "title_unresolved"
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
            "snapshot_object_etag": matches[candidate_id].get("snapshot_object_etag"),
        }
        for candidate_id in sorted(matches)
    ]
    status = (
        "resolved"
        if len(candidate_rows) == 1
        else ("unresolved" if not candidate_rows else "ambiguous")
    )
    return status, candidate_rows


def _write_seed_mapping(
    seeds: list[dict[str, Any]],
    candidates: list[dict[str, Any]],
    output_root: Path,
) -> dict[str, Any]:
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
    for seed in seeds:
        status, candidate_rows = _map_seed_candidates(seed, by_oa, by_doi, by_title)
        unselected_title_evidence = []
        if status == "unresolved":
            for candidate in by_title.get(seed.get("title_normalized"), []):
                unselected_title_evidence.append(
                    {
                        "openalex_id": candidate["id"],
                        "title": candidate.get("title"),
                        "authors": candidate.get("authors") or [],
                        "year": candidate.get("publication_year"),
                        "evidence": "exact_title_failed_author_or_uniqueness_gate",
                        "snapshot_object": candidate.get("snapshot_object"),
                        "snapshot_object_etag": candidate.get("snapshot_object_etag"),
                    }
                )
        mappings.append(
            {
                "source_id": seed["source_id"],
                "seed_title": seed["title"],
                "seed_openalex_id": seed.get("openalex_id"),
                "seed_doi": seed.get("doi"),
                "status": status,
                "candidates": candidate_rows,
                "unselected_title_evidence": sorted(
                    unselected_title_evidence,
                    key=lambda row: row["openalex_id"],
                ),
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
    mapping_path = output_root / "seed_mapping.jsonl"
    write_jsonl(mapping_path, mappings)
    resolved_path = output_root / "resolved_seed_ids.jsonl"
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
        "resolved_seed_mappings": len(resolved_ids),
        "resolved_openalex_ids": len({row["openalex_id"] for row in resolved_ids}),
        "seed_count": len(mappings),
        "status_counts": dict(sorted(counts.items())),
        "candidate_rows": len(candidates),
    }
    write_json(output_root / "seed_mapping_summary.json", summary)
    return summary


def resolve_seed_mappings(layout: Layout, duckdb: Path) -> dict[str, Any]:
    """Resolve every #42 seed against the fully scanned snapshot with ambiguity evidence."""

    output = layout.riemann / "seed_resolution_candidates.jsonl"
    query = f"""
SET threads=2;
SET temp_directory={sql_quote(str(layout.tmp / "duckdb_spill"))};
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
    return _write_seed_mapping(
        load_jsonl(layout.riemann / "seeds.jsonl"),
        load_jsonl(output),
        layout.riemann,
    )


def resolve_agnostic_mappings(layout: Layout, duckdb: Path) -> dict[str, Any]:
    """Resolve the exact merged #44 inventory against the shared offline index."""

    seeds_path = layout.agnostic / "seeds.jsonl"
    if not seeds_path.is_file():
        raise PipelineError("run prepare-agnostic-seeds before resolving #44")
    seeds = load_jsonl(seeds_path)
    openalex = _list_literal(
        sorted({row["openalex_id"] for row in seeds if row.get("openalex_id")})
    )
    dois = _list_literal(sorted({row["doi"] for row in seeds if row.get("doi")}))
    titles = _list_literal(sorted({row["title_normalized"] for row in seeds}))
    output = layout.agnostic / "seed_resolution_candidates.jsonl"
    database = layout.reduced / "openalex.duckdb"
    query = f"""
SET threads=2;
SET temp_directory={sql_quote(str(layout.tmp / "duckdb_spill"))};
COPY (
 WITH candidates AS (
  SELECT *,trim(lower(regexp_replace(coalesce(title,''),'[^a-zA-Z0-9]+',' ','g'))) AS normalized
  FROM openalex_works
 )
 SELECT id,doi,title,authors,publication_year,snapshot_object,snapshot_object_etag
 FROM candidates
 WHERE id IN {openalex}
    OR lower(regexp_replace(coalesce(doi,''),'^https?://(?:dx\\.)?doi\\.org/','')) IN {dois}
    OR normalized IN {titles}
 ORDER BY id
) TO {sql_quote(str(output))} (FORMAT JSON,ARRAY false);
"""
    result = _run([str(duckdb), str(database)], input_text=query)
    if result.returncode:
        raise PipelineError(result.stderr.strip())
    return _write_seed_mapping(seeds, load_jsonl(output), layout.agnostic)


def _graph_scalar(duckdb: Path, database: Path, query: str) -> int:
    result = _run([str(duckdb), str(database), "-noheader", "-csv", "-c", query])
    if result.returncode:
        raise PipelineError(result.stderr.strip())
    return int(result.stdout.strip())


def _resolved_ids_sql(path: Path) -> str:
    ids = sorted({row["openalex_id"] for row in load_jsonl(path)})
    if not ids:
        return "SELECT CAST(NULL AS VARCHAR) AS id WHERE false"
    return (
        "SELECT col0 AS id FROM (VALUES "
        + ",".join(f"({sql_quote(identifier)})" for identifier in ids)
        + ")"
    )


def _populate_reverse_citers(
    layout: Layout,
    duckdb: Path,
    database: Path,
    destination_table: str,
    frontier_table: str,
    *,
    math_only: bool,
) -> None:
    """Populate reverse citations in shard-bounded transactions.

    Unnesting every retained citation list into one global DISTINCT can exceed
    DuckDB's memory limit before the join is applied. Each source Parquet shard
    is independently deduplicated here and inserted into a keyed table, which
    preserves the exact set while bounding the largest operator to one shard.
    """

    if not destination_table.isidentifier() or not frontier_table.isidentifier():
        raise PipelineError("invalid internal graph table name")
    create = _run(
        [str(duckdb), str(database)],
        input_text=(
            "SET threads=1;\n"
            "SET memory_limit='3GB';\n"
            f"SET temp_directory={sql_quote(str(layout.tmp / 'duckdb_spill'))};\n"
            "SET preserve_insertion_order=false;\n"
            f"CREATE OR REPLACE TABLE {destination_table}(id VARCHAR PRIMARY KEY);\n"
        ),
    )
    if create.returncode:
        raise PipelineError(
            f"failed to initialize {destination_table}: "
            f"{create.stderr.strip() or create.stdout.strip()}"
        )
    parts = sorted((layout.reduced / "works_parts").glob("part_*.parquet"))
    if not parts:
        raise PipelineError("no reduced Parquet parts available for graph expansion")
    math_clause = "AND w.math_adjacent" if math_only else ""
    batch_size = 32
    for offset in range(0, len(parts), batch_size):
        statements = []
        for part in parts[offset : offset + batch_size]:
            statements.append(
                f"""
INSERT OR IGNORE INTO {destination_table}
SELECT DISTINCT w.id
FROM read_parquet({sql_quote(str(part))}, hive_partitioning=false) w,
     unnest(w.referenced_works) AS reference(id)
JOIN {frontier_table} f ON f.id=reference.id
WHERE w.referenced_works IS NOT NULL {math_clause};
"""
            )
        result = _run(
            [str(duckdb), str(database)],
            input_text=(
                "SET threads=1;\n"
                "SET memory_limit='3GB';\n"
                f"SET temp_directory={sql_quote(str(layout.tmp / 'duckdb_spill'))};\n"
                "SET preserve_insertion_order=false;\n" + "".join(statements)
            ),
        )
        if result.returncode:
            last = min(offset + batch_size, len(parts))
            raise PipelineError(
                f"reverse-citation shards {offset + 1}-{last} failed: "
                f"{result.stderr.strip() or result.stdout.strip() or 'no DuckDB diagnostic'}"
            )


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
    resolved_sql = _resolved_ids_sql(resolved_seed_ids)
    mechanism_title_match = (
        "regexp_matches(lower(coalesce(w.title,'')),"
        + sql_quote(RIEMANN_MECHANISM_TITLE_PATTERN)
        + ")"
    )
    initial_sql = f"""
SET threads=1;
SET memory_limit='3GB';
SET temp_directory={sql_quote(str(layout.tmp / "duckdb_spill"))};
SET preserve_insertion_order=false;
CREATE OR REPLACE TABLE graph_acceptance AS
WITH resolved AS (
  {resolved_sql}
)
SELECT w.id,0::INTEGER AS graph_pass,
  CASE WHEN r.id IS NOT NULL THEN 'exact_resolved_seed'
       WHEN w.text_score>=3 THEN 'global_high_confidence_text'
       ELSE 'global_high_confidence_mechanism_title' END AS acceptance_reason
FROM openalex_works w LEFT JOIN resolved r USING(id)
WHERE w.exclusion_rule IS NULL AND NOT coalesce(w.is_retracted,false)
  AND (r.id IS NOT NULL
       OR ((w.text_score>=3 OR {mechanism_title_match})
           AND w.math_adjacent AND NOT coalesce(w.is_paratext,false)));
CREATE OR REPLACE TABLE semantic_review_ids(
  id VARCHAR PRIMARY KEY, first_graph_pass INTEGER, reason VARCHAR
);
CREATE OR REPLACE TABLE graph_inspection(
  id VARCHAR, graph_pass INTEGER, disposition VARCHAR,
  PRIMARY KEY(id,graph_pass)
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
SET threads=1;
SET memory_limit='3GB';
SET temp_directory={sql_quote(str(layout.tmp / "duckdb_spill"))};
SET preserve_insertion_order=false;
CREATE OR REPLACE TABLE graph_frontier AS
SELECT id FROM graph_acceptance WHERE graph_pass={pass_number - 1};
CREATE OR REPLACE TABLE graph_frontier_references AS
SELECT DISTINCT unnest(w.referenced_works) AS id
FROM openalex_works w JOIN graph_frontier f USING(id)
WHERE w.referenced_works IS NOT NULL;
"""
        result = _run([str(duckdb), str(database)], input_text=sql)
        if result.returncode:
            raise PipelineError(
                f"graph pass {pass_number} frontier failed with exit "
                f"{result.returncode}: "
                f"{result.stderr.strip() or result.stdout.strip() or 'no DuckDB diagnostic'}"
            )
        _populate_reverse_citers(
            layout,
            duckdb,
            database,
            "graph_reverse_citers",
            "graph_frontier",
            math_only=True,
        )
        sql = f"""
SET threads=1;
SET memory_limit='3GB';
SET temp_directory={sql_quote(str(layout.tmp / "duckdb_spill"))};
SET preserve_insertion_order=false;
CREATE OR REPLACE TABLE graph_adjacent AS
SELECT DISTINCT id FROM (
  SELECT id FROM graph_frontier_references
  UNION ALL SELECT id FROM graph_reverse_citers
);
CREATE OR REPLACE TABLE graph_novel AS
SELECT w.* FROM openalex_works w JOIN graph_adjacent a USING(id)
WHERE NOT EXISTS (SELECT 1 FROM graph_acceptance g WHERE g.id=w.id);
INSERT OR IGNORE INTO graph_inspection
SELECT id,{pass_number},
  CASE WHEN exclusion_rule IS NOT NULL THEN 'rejected_false_positive'
       WHEN math_adjacent AND NOT coalesce(is_retracted,false)
         AND NOT coalesce(is_paratext,false)
         AND (text_score>0 OR {mechanism_title_match})
         THEN 'accepted_contextual_text'
       WHEN math_adjacent AND NOT coalesce(is_retracted,false)
         AND NOT coalesce(is_paratext,false) THEN 'graph_only_review'
       ELSE 'rejected_out_of_scope' END
FROM graph_novel w;
INSERT OR IGNORE INTO semantic_review_ids
SELECT id,{pass_number},'citation_adjacent_without_deterministic_text_signal'
FROM graph_novel w
WHERE exclusion_rule IS NULL AND text_score=0 AND NOT {mechanism_title_match}
  AND math_adjacent AND NOT coalesce(is_retracted,false)
  AND NOT coalesce(is_paratext,false);
INSERT INTO graph_acceptance
SELECT id,{pass_number},'citation_adjacent_contextual_text'
FROM graph_novel w
WHERE exclusion_rule IS NULL AND (text_score>0 OR {mechanism_title_match})
  AND math_adjacent
  AND NOT coalesce(is_retracted,false) AND NOT coalesce(is_paratext,false);
"""
        result = _run([str(duckdb), str(database)], input_text=sql)
        if result.returncode:
            raise PipelineError(
                f"graph pass {pass_number} failed with exit {result.returncode}: "
                f"{result.stderr.strip() or result.stdout.strip() or 'no DuckDB diagnostic'}"
            )
        frontier = _graph_scalar(
            duckdb, database, "SELECT count(*) FROM graph_frontier"
        )
        adjacent = _graph_scalar(
            duckdb, database, "SELECT count(*) FROM graph_adjacent"
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
        previous_frontier_overlap = _graph_scalar(
            duckdb,
            database,
            "SELECT count(*) FROM graph_adjacent a JOIN graph_acceptance g USING(id) "
            f"WHERE g.graph_pass={pass_number - 1}",
        )
        passes.append(
            {
                "pass": pass_number,
                "frontier_size": frontier,
                "candidates_inspected": inspected,
                "newly_accepted": accepted,
                "duplicates_or_known": adjacent - inspected,
                "false_positive_exclusions": excluded,
                "semantic_review_queue_new": queue_new,
                "graph_only_not_promoted": max(0, inspected - accepted - excluded),
                "frontier_overlap_previous": previous_frontier_overlap,
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
    inspection_path = output / "graph_inspection.parquet"
    edges_path = output / "citation_edges.parquet"
    duplicates_path = output / "duplicate_groups.parquet"
    export_sql = f"""
SET threads=1;
SET memory_limit='3GB';
SET temp_directory={sql_quote(str(layout.tmp / "duckdb_spill"))};
SET preserve_insertion_order=false;
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
 SELECT i.*,w.snapshot_object,w.snapshot_object_etag,w.scan_pass
 FROM graph_inspection i JOIN openalex_works w USING(id)
 ORDER BY graph_pass,id
) TO {sql_quote(str(inspection_path))} (FORMAT parquet,COMPRESSION zstd);
COPY (
 SELECT w.id AS citing_work_id,unnest(w.referenced_works) AS cited_work_id,
   g.graph_pass,w.snapshot_object,w.snapshot_object_etag,w.scan_pass
 FROM openalex_works w JOIN graph_acceptance g USING(id)
 WHERE w.referenced_works IS NOT NULL
 ORDER BY citing_work_id,cited_work_id
) TO {sql_quote(str(edges_path))} (FORMAT parquet,COMPRESSION zstd);
COPY (
 SELECT coalesce(nullif(lower(regexp_replace(w.doi,'^https?://(?:dx\\.)?doi\\.org/','')),''),
                 nullif(lower(regexp_replace(w.title,'[^a-zA-Z0-9]+',' ','g')),''),
                 w.id) AS duplicate_key,
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
        "graph_inspection",
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
    counts["graph_inspection_unique"] = int(
        _duckdb_scalar(
            duckdb,
            f"SELECT count(DISTINCT id) FROM read_parquet({sql_quote(str(inspection_path))})",
        )
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
            "agent_iterations": 0,
            "candidates_per_agent_batch": [],
            "estimated_agent_input_tokens": 0,
            "estimated_agent_output_tokens": 0,
            "cached_agent_decisions": 0,
            "policy": (
                "Graph-only ambiguous records are preserved in a queue and are not promoted. "
                "No agent decision is needed for the frozen deterministic accepted tier."
            ),
        },
    }
    summary["counts"]["discovered_unique"] = (
        passes[0]["newly_accepted"] + counts["graph_inspection_unique"]
    )
    write_json(output / "summary.json", summary)
    if not saturated:
        raise PipelineError(
            f"graph expansion still yielded new contextual works at pass {max_passes}"
        )
    return summary


def _agnostic_list_expression(items: Iterable[tuple[str, str]]) -> str:
    expressions = [
        f"CASE WHEN regexp_matches(title_norm,{sql_quote(pattern)}) "
        f"THEN {sql_quote(identifier)} END"
        for identifier, pattern in items
    ]
    return "list_filter([" + ",".join(expressions) + "], x -> x IS NOT NULL)"


def expand_agnostic_graph(
    layout: Layout, duckdb: Path, max_passes: int = 6
) -> dict[str, Any]:
    """Build the separate #44-seeded frontier from the shared offline index."""

    output = layout.agnostic / "graph_v1"
    output.mkdir(parents=True, exist_ok=True)
    database = layout.reduced / "openalex.duckdb"
    resolved_path = layout.agnostic / "resolved_seed_ids.jsonl"
    if not database.is_file() or not resolved_path.is_file():
        raise PipelineError(
            "build-index and resolve-agnostic must precede graph expansion"
        )
    family_patterns = [(rule[0], rule[2]) for rule in AGNOSTIC_FAMILY_RULES]
    lens_conditions: list[tuple[str, str]] = []
    for ecosystem_id, pattern in AGNOSTIC_LENS_PATTERNS.items():
        related_family_patterns = [
            rule[2] for rule in AGNOSTIC_FAMILY_RULES if ecosystem_id in rule[1]
        ]
        combined = "(" + "|".join([pattern, *related_family_patterns]) + ")"
        lens_conditions.append((ecosystem_id, combined))
    combined_prefilter = (
        "("
        + "|".join(
            [
                *AGNOSTIC_LENS_PATTERNS.values(),
                *(rule[2] for rule in AGNOSTIC_FAMILY_RULES),
            ]
        )
        + ")"
    )
    lens_expression = _agnostic_list_expression(lens_conditions)
    family_expression = _agnostic_list_expression(family_patterns)
    resolved_sql = _resolved_ids_sql(resolved_path)
    universe_sql = f"""
SET threads=1;
SET memory_limit='3GB';
SET temp_directory={sql_quote(str(layout.tmp / "duckdb_spill"))};
SET preserve_insertion_order=false;
CREATE OR REPLACE TABLE agnostic_resolved_ids AS
{resolved_sql};
CREATE OR REPLACE TABLE agnostic_scored AS
WITH base AS (
 SELECT w.*,trim(lower(regexp_replace(coalesce(w.title,''),'[^a-zA-Z0-9]+',' ','g'))) AS title_norm
 FROM openalex_works w
 WHERE (w.math_adjacent AND NOT coalesce(w.is_retracted,false)
   AND NOT coalesce(w.is_paratext,false) AND coalesce(w.cited_by_count,0)>=2
   AND regexp_matches(trim(lower(regexp_replace(coalesce(w.title,''),'[^a-zA-Z0-9]+',' ','g'))),
                      {sql_quote(combined_prefilter)}))
   OR EXISTS (SELECT 1 FROM agnostic_resolved_ids r WHERE r.id=w.id)
)
SELECT *,{lens_expression} AS lens_ids,{family_expression} AS family_ids
FROM base;
CREATE OR REPLACE TABLE agnostic_lens_ranked AS
SELECT id,ecosystem_id,row_number() OVER (
 PARTITION BY ecosystem_id ORDER BY
   CASE WHEN open_access.is_oa OR coalesce(has_fulltext,false) THEN 1 ELSE 0 END DESC,
   coalesce(cited_by_count,0) DESC,id) AS lens_rank
FROM agnostic_scored,unnest(lens_ids) AS lens(ecosystem_id)
WHERE NOT EXISTS (SELECT 1 FROM agnostic_resolved_ids r WHERE r.id=agnostic_scored.id);
CREATE OR REPLACE TABLE agnostic_family_ranked AS
SELECT id,family_id,row_number() OVER (
 PARTITION BY family_id ORDER BY
   CASE WHEN open_access.is_oa OR coalesce(has_fulltext,false) THEN 1 ELSE 0 END DESC,
   coalesce(cited_by_count,0) DESC,id) AS family_rank
FROM agnostic_scored,unnest(family_ids) AS family(family_id)
WHERE NOT EXISTS (SELECT 1 FROM agnostic_resolved_ids r WHERE r.id=agnostic_scored.id);
CREATE OR REPLACE TABLE agnostic_selected_ids AS
SELECT id,list(DISTINCT selection_basis ORDER BY selection_basis) AS selection_basis
FROM (
 SELECT id,'lens_ranked' AS selection_basis FROM agnostic_lens_ranked WHERE lens_rank<=50
 UNION ALL
 SELECT id,'global_family' AS selection_basis FROM agnostic_family_ranked WHERE family_rank<=10
) selected GROUP BY id;
CREATE OR REPLACE TABLE agnostic_hit_universe AS
SELECT s.*,selected.selection_basis
FROM agnostic_scored s JOIN agnostic_selected_ids selected USING(id);
CREATE OR REPLACE TABLE agnostic_work_cache AS
SELECT * FROM agnostic_hit_universe
UNION ALL
SELECT w.*,[]::VARCHAR[] AS selection_basis
FROM agnostic_scored w JOIN agnostic_resolved_ids USING(id)
WHERE NOT EXISTS (SELECT 1 FROM agnostic_hit_universe u WHERE u.id=w.id);
CREATE OR REPLACE TABLE agnostic_acceptance AS
SELECT w.id,0::INTEGER AS graph_pass,'exact_resolved_seed' AS acceptance_reason
FROM agnostic_work_cache w JOIN agnostic_resolved_ids USING(id)
UNION ALL
SELECT u.id,0::INTEGER,'global_new_family_candidate' AS acceptance_reason
FROM agnostic_hit_universe u
WHERE list_contains(u.selection_basis,'global_family')
  AND NOT EXISTS (SELECT 1 FROM agnostic_resolved_ids r WHERE r.id=u.id);
CREATE OR REPLACE TABLE agnostic_inspection(
  id VARCHAR, graph_pass INTEGER, in_hit_universe BOOLEAN, disposition VARCHAR,
  PRIMARY KEY(id,graph_pass)
);
"""
    result = _run([str(duckdb), str(database)], input_text=universe_sql)
    if result.returncode:
        raise PipelineError(f"agnostic universe failed: {result.stderr.strip()}")
    initial = _graph_scalar(
        duckdb, database, "SELECT count(*) FROM agnostic_acceptance"
    )
    seed_count = _graph_scalar(
        duckdb,
        database,
        "SELECT count(*) FROM agnostic_acceptance "
        "WHERE acceptance_reason='exact_resolved_seed'",
    )
    passes: list[dict[str, Any]] = [
        {
            "pass": 0,
            "frontier_size": initial,
            "newly_accepted": initial,
            "selection": "resolved #44 seeds plus bounded global candidate-family rules",
        }
    ]
    saturated = False
    for pass_number in range(1, max_passes + 1):
        sql = f"""
SET threads=1;
SET memory_limit='3GB';
SET temp_directory={sql_quote(str(layout.tmp / "duckdb_spill"))};
SET preserve_insertion_order=false;
CREATE OR REPLACE TABLE agnostic_frontier AS
SELECT id FROM agnostic_acceptance WHERE graph_pass={pass_number - 1};
CREATE OR REPLACE TABLE agnostic_forward AS
SELECT DISTINCT unnest(w.referenced_works) AS id
FROM agnostic_work_cache w JOIN agnostic_frontier f USING(id)
WHERE w.referenced_works IS NOT NULL;
CREATE OR REPLACE TABLE agnostic_reverse AS
SELECT DISTINCT u.id
FROM agnostic_hit_universe u,unnest(u.referenced_works) AS reference(id)
JOIN agnostic_frontier f ON f.id=reference.id
WHERE u.referenced_works IS NOT NULL;
CREATE OR REPLACE TABLE agnostic_adjacent AS
SELECT DISTINCT candidate.id FROM (
 SELECT id FROM agnostic_forward UNION ALL SELECT id FROM agnostic_reverse
) adjacent JOIN agnostic_hit_universe candidate USING(id);
INSERT OR IGNORE INTO agnostic_inspection
SELECT a.id,{pass_number},true,
  CASE WHEN known.id IS NOT NULL THEN 'already_accepted'
       ELSE 'bounded_rule_candidate' END
FROM agnostic_adjacent a
LEFT JOIN agnostic_acceptance known USING(id);
INSERT INTO agnostic_acceptance
SELECT u.id,{pass_number},'citation_adjacent_coverage_lens'
FROM agnostic_hit_universe u JOIN agnostic_adjacent a USING(id)
WHERE NOT EXISTS (SELECT 1 FROM agnostic_acceptance known WHERE known.id=u.id);
"""
        result = _run([str(duckdb), str(database)], input_text=sql)
        if result.returncode:
            raise PipelineError(
                f"agnostic graph pass {pass_number} failed with exit "
                f"{result.returncode}: "
                f"{result.stderr.strip() or result.stdout.strip() or 'no DuckDB diagnostic'}"
            )
        frontier = _graph_scalar(
            duckdb, database, "SELECT count(*) FROM agnostic_frontier"
        )
        accepted = _graph_scalar(
            duckdb,
            database,
            f"SELECT count(*) FROM agnostic_acceptance WHERE graph_pass={pass_number}",
        )
        adjacent = _graph_scalar(
            duckdb, database, "SELECT count(*) FROM agnostic_adjacent"
        )
        novel = _graph_scalar(
            duckdb,
            database,
            "SELECT count(*) FROM agnostic_adjacent a WHERE NOT EXISTS "
            "(SELECT 1 FROM agnostic_acceptance known WHERE known.id=a.id "
            f"AND known.graph_pass<{pass_number})",
        )
        passes.append(
            {
                "pass": pass_number,
                "frontier_size": frontier,
                "candidates_inspected": adjacent,
                "newly_accepted": accepted,
                "duplicates_or_known": adjacent - novel,
                "false_positive_exclusions": 0,
                "graph_only_not_promoted": max(0, novel - accepted),
                "new_mathematical_viewpoints_confirmed": 0,
                "interpretation": (
                    "Title/graph evidence ranks a retrieval candidate; source-level novelty "
                    "remains unconfirmed for downstream mathematical inspection."
                ),
            }
        )
        if accepted == 0:
            saturated = True
            passes[-1]["saturated"] = True
            break
    if not saturated:
        raise PipelineError(
            f"agnostic graph still yielded candidates at pass {max_passes}"
        )
    accepted_path = output / "accepted_candidates.parquet"
    audit_only_path = output / "audit_only_candidates.parquet"
    edges_path = output / "citation_edges.parquet"
    inspection_path = output / "graph_inspection.parquet"
    duplicates_path = output / "duplicate_groups.parquet"
    export_sql = f"""
SET threads=1;
SET memory_limit='3GB';
SET temp_directory={sql_quote(str(layout.tmp / "duckdb_spill"))};
SET preserve_insertion_order=false;
COPY (
 SELECT w.*,a.graph_pass,a.acceptance_reason,
   CASE WHEN a.acceptance_reason='exact_resolved_seed' THEN 10000
        ELSE 500 + list_count(coalesce(u.family_ids,[]))*50
          + list_count(coalesce(u.lens_ids,[]))*10
          + least(coalesce(w.cited_by_count,0),1000)/10
          + CASE WHEN w.open_access.is_oa OR coalesce(w.has_fulltext,false)
                 THEN 200 ELSE 0 END END AS priority_score,
   coalesce(u.lens_ids,[]) AS ecosystem_lens_ids,
   coalesce(u.family_ids,[]) AS candidate_family_ids,
   coalesce(u.selection_basis,[]) AS selection_basis,
   CASE WHEN a.acceptance_reason='exact_resolved_seed' THEN 'already_represented_seed'
        ELSE 'candidate_unconfirmed_requires_source_validation' END AS saturation_status
 FROM agnostic_work_cache w JOIN agnostic_acceptance a USING(id)
 LEFT JOIN agnostic_hit_universe u USING(id)
 ORDER BY priority_score DESC,id
) TO {sql_quote(str(accepted_path))} (FORMAT parquet,COMPRESSION zstd);
COPY (
 SELECT u.*,'not_connected_in_bounded_graph_closure' AS audit_disposition
 FROM agnostic_hit_universe u
 WHERE NOT EXISTS (SELECT 1 FROM agnostic_acceptance a WHERE a.id=u.id)
 ORDER BY coalesce(cited_by_count,0) DESC,id
) TO {sql_quote(str(audit_only_path))} (FORMAT parquet,COMPRESSION zstd);
COPY (
 SELECT w.id AS citing_work_id,unnest(w.referenced_works) AS cited_work_id,
   a.graph_pass,w.snapshot_object,w.snapshot_object_etag,w.scan_pass
 FROM agnostic_work_cache w JOIN agnostic_acceptance a USING(id)
 WHERE w.referenced_works IS NOT NULL
 ORDER BY citing_work_id,cited_work_id
) TO {sql_quote(str(edges_path))} (FORMAT parquet,COMPRESSION zstd);
COPY (
 SELECT i.*,w.snapshot_object,w.snapshot_object_etag,w.scan_pass
 FROM agnostic_inspection i JOIN agnostic_hit_universe w USING(id)
 ORDER BY graph_pass,id
) TO {sql_quote(str(inspection_path))} (FORMAT parquet,COMPRESSION zstd);
COPY (
 SELECT coalesce(nullif(lower(regexp_replace(w.doi,'^https?://(?:dx\\.)?doi\\.org/','')),''),
                 nullif(lower(regexp_replace(w.title,'[^a-zA-Z0-9]+',' ','g')),''),
                 w.id) AS duplicate_key,
        list(w.id ORDER BY w.id) AS work_ids,count(*) AS work_count
 FROM agnostic_work_cache w JOIN agnostic_acceptance a USING(id)
 GROUP BY duplicate_key HAVING count(*)>1
 ORDER BY work_count DESC,duplicate_key
) TO {sql_quote(str(duplicates_path))} (FORMAT parquet,COMPRESSION zstd);
"""
    result = _run([str(duckdb), str(database)], input_text=export_sql)
    if result.returncode:
        raise PipelineError(f"agnostic export failed: {result.stderr.strip()}")
    counts = {}
    artifacts = []
    for name, path in (
        ("accepted_candidates", accepted_path),
        ("audit_only_candidates", audit_only_path),
        ("citation_edges", edges_path),
        ("graph_inspection", inspection_path),
        ("duplicate_groups", duplicates_path),
    ):
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
    lens_csv = _run(
        [
            str(duckdb),
            str(database),
            "-csv",
            "-c",
            """
SELECT ecosystem_id,count(DISTINCT u.id) AS count
FROM agnostic_hit_universe u,unnest(u.lens_ids) lens(ecosystem_id)
WHERE NOT EXISTS (
  SELECT 1 FROM agnostic_acceptance a
  WHERE a.id=u.id AND a.acceptance_reason='exact_resolved_seed'
)
GROUP BY ecosystem_id ORDER BY ecosystem_id;
""",
        ],
    )
    if lens_csv.returncode:
        raise PipelineError(lens_csv.stderr.strip())
    observed_lenses = {
        row["ecosystem_id"]: int(row["count"])
        for row in csv.DictReader(lens_csv.stdout.splitlines())
    }
    lens_counts = {
        ecosystem_id: observed_lenses.get(ecosystem_id, 0)
        for ecosystem_id in AGNOSTIC_LENS_PATTERNS
    }
    family_csv = _run(
        [
            str(duckdb),
            str(database),
            "-csv",
            "-c",
            """
SELECT family_id,count(DISTINCT u.id) AS count
FROM agnostic_hit_universe u,unnest(u.family_ids) family(family_id)
WHERE NOT EXISTS (
  SELECT 1 FROM agnostic_acceptance a
  WHERE a.id=u.id AND a.acceptance_reason='exact_resolved_seed'
)
GROUP BY family_id ORDER BY family_id;
""",
        ],
    )
    if family_csv.returncode:
        raise PipelineError(family_csv.stderr.strip())
    family_counts = {
        row["family_id"]: int(row["count"])
        for row in csv.DictReader(family_csv.stdout.splitlines())
    }
    family_rationales = {rule[0]: rule[3] for rule in AGNOSTIC_FAMILY_RULES}
    family_candidate_count = int(
        _duckdb_scalar(
            duckdb,
            f"SELECT count(*) FROM read_parquet({sql_quote(str(accepted_path))}) "
            "WHERE acceptance_reason!='exact_resolved_seed' "
            "AND list_count(candidate_family_ids)>0",
        )
    )
    duplicate_or_represented = _graph_scalar(
        duckdb,
        database,
        """
WITH ranked AS (
 SELECT w.id,a.acceptance_reason,
   row_number() OVER (
     PARTITION BY coalesce(
       nullif(lower(regexp_replace(w.doi,'^https?://(?:dx\\.)?doi\\.org/','')),''),
       nullif(lower(regexp_replace(w.title,'[^a-zA-Z0-9]+',' ','g')),''),
       w.id
     )
     ORDER BY CASE WHEN a.acceptance_reason='exact_resolved_seed' THEN 0 ELSE 1 END,w.id
   ) AS duplicate_rank
 FROM agnostic_work_cache w JOIN agnostic_acceptance a USING(id)
)
SELECT count(*) FROM ranked
WHERE acceptance_reason='exact_resolved_seed' OR duplicate_rank>1;
""",
    )
    summary = {
        "generated_at": utc_now(),
        "graph_version": "openalex-agnostic-mathia-graph-v1",
        "seed_works_in_snapshot": seed_count,
        "saturated": saturated,
        "passes": passes,
        "counts": counts,
        "candidate_counts_by_ecosystem_lens": lens_counts,
        "candidate_families": [
            {
                "family_id": family_id,
                "candidate_count": family_counts.get(family_id, 0),
                "evidence_scope": family_rationales[family_id],
                "novelty_status": "candidate_unconfirmed_requires_source_validation",
            }
            for family_id in sorted(family_rationales)
        ],
        "saturation_prior": {
            "confirmed_material_challenges": 0,
            "candidate_challenges_pending_source_validation": family_candidate_count,
            "interpretation": (
                "OpenAlex title/citation evidence cannot establish a genuinely distinct "
                "mathematical mechanism; #42 must inspect handed-off text."
            ),
        },
        "duplicate_or_already_represented": duplicate_or_represented,
        "duplicate_count_definition": (
            "Unique accepted works that are resolved frozen seeds or rank after the "
            "canonical work in a normalized DOI/title duplicate group."
        ),
        "semantic_review": {
            "works_reviewed_by_agent": 0,
            "agent_batches": 0,
            "agent_iterations": 0,
            "candidates_per_agent_batch": [],
            "estimated_agent_input_tokens": 0,
            "estimated_agent_output_tokens": 0,
            "cached_agent_decisions": 0,
            "policy": "No metadata-only candidate was promoted to confirmed conceptual novelty.",
        },
        "artifacts": artifacts,
    }
    write_json(output / "summary.json", summary)
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
    with raw_path.open("rb") as raw_stream:
        is_pdf = raw_stream.read(5) == b"%PDF-"
    if is_pdf or "pdf" in content_type:
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
    host_last_request: dict[str, float] | None = None,
) -> bool:
    parsed = urllib.parse.urlparse(url)
    origin = f"{parsed.scheme}://{parsed.netloc}"
    if origin not in cache:
        parser = urllib.robotparser.RobotFileParser(f"{origin}/robots.txt")
        try:
            import requests

            _throttle_host(url, host_last_request)
            response = requests.get(
                f"{origin}/robots.txt",
                headers={"User-Agent": user_agent},
                timeout=15,
            )
            if response.status_code == 200:
                parser.parse(response.text.splitlines())
            elif response.status_code in {401, 403, 429} or response.status_code >= 500:
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


def _throttle_host(
    url: str,
    host_last_request: dict[str, float] | None,
    minimum_interval: float = 0.75,
) -> None:
    if host_last_request is None:
        return
    host = urllib.parse.urlparse(url).netloc.lower()
    elapsed = time.monotonic() - host_last_request.get(host, 0)
    if elapsed < minimum_interval:
        time.sleep(minimum_interval - elapsed)
    host_last_request[host] = time.monotonic()


def _download_url(
    url: str,
    target: Path,
    *,
    user_agent: str,
    robots_cache: dict[str, urllib.robotparser.RobotFileParser],
    host_last_request: dict[str, float] | None = None,
    timeout: int = 90,
    max_bytes: int = 512 * 1024 * 1024,
) -> dict[str, Any]:
    import requests

    headers = {
        "User-Agent": user_agent,
        "Accept": "application/pdf,text/html,text/plain,*/*;q=0.2",
    }
    current_url = url
    for _redirect_count in range(6):
        if not _robots_allowed(
            current_url, user_agent, robots_cache, host_last_request
        ):
            raise PipelineError("robots_disallowed")
        _throttle_host(current_url, host_last_request)
        with requests.get(
            current_url,
            headers=headers,
            timeout=timeout,
            stream=True,
            allow_redirects=False,
        ) as response:
            if response.status_code in {301, 302, 303, 307, 308}:
                location = response.headers.get("Location")
                if not location:
                    raise PipelineError("redirect_without_location")
                current_url = urllib.parse.urljoin(response.url, location)
                if urllib.parse.urlparse(current_url).scheme not in {"http", "https"}:
                    raise PipelineError("redirect_to_unsupported_scheme")
                continue
            if response.status_code == 429 or response.status_code >= 500:
                retry = response.headers.get("Retry-After")
                raise PipelineError(
                    f"retryable_http_{response.status_code};retry_after={retry}"
                )
            if response.status_code >= 400:
                raise PipelineError(f"terminal_http_{response.status_code}")
            target.parent.mkdir(parents=True, exist_ok=True)
            partial = target.with_suffix(target.suffix + ".part")
            try:
                downloaded_bytes = 0
                with partial.open("wb") as stream:
                    for chunk in response.iter_content(chunk_size=1024 * 1024):
                        if chunk:
                            downloaded_bytes += len(chunk)
                            if downloaded_bytes > max_bytes:
                                raise PipelineError(
                                    f"response_exceeds_max_bytes_{max_bytes}"
                                )
                            stream.write(chunk)
                if partial.stat().st_size < 1_000:
                    raise PipelineError("response_too_small")
                os.replace(partial, target)
            except Exception as error:
                downloaded_bytes = max(
                    downloaded_bytes,
                    partial.stat().st_size if partial.is_file() else 0,
                )
                partial.unlink(missing_ok=True)
                try:
                    error.downloaded_bytes = downloaded_bytes
                except (AttributeError, TypeError):
                    pass
                raise
            return {
                "effective_url": response.url,
                "content_type": response.headers.get("Content-Type", "")
                .split(";", 1)[0]
                .lower(),
                "content_length": target.stat().st_size,
                "license_header": response.headers.get("License"),
            }
    raise PipelineError("too_many_redirects")


def _export_candidates_json(duckdb: Path, parquet: Path, path: Path) -> None:
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
    stream: str = "riemann",
) -> dict[str, Any]:
    """Acquire public full text with persistent per-route state and no agent calls."""

    if stream not in {"riemann", "agnostic_mathia"}:
        raise PipelineError(f"unknown acquisition stream: {stream}")
    stream_root = layout.riemann if stream == "riemann" else layout.agnostic
    work_root = stream_root / "acquisition_v1"
    raw_root = work_root / "raw"
    normalized_root = work_root / "normalized"
    work_root.mkdir(parents=True, exist_ok=True)
    candidate_path = work_root / "candidates.jsonl"
    _export_candidates_json(
        duckdb, stream_root / "graph_v1" / "accepted_candidates.parquet", candidate_path
    )
    all_records = load_jsonl(candidate_path)
    seeds = load_jsonl(stream_root / "seeds.jsonl")
    agnostic_release_identity: dict[str, Any] | None = None
    if stream == "agnostic_mathia":
        seed_summary = json.loads(
            (stream_root / "seed_summary.json").read_text(encoding="utf-8")
        )
        agnostic_release_identity = {
            "release_id": seed_summary["release_id"],
            "freeze_id": seed_summary["freeze_id"],
            "freeze_sha256": seed_summary["freeze_sha256"],
            "coverage_map_id": seed_summary["coverage_map_id"],
            "coverage_map_sha256": seed_summary["coverage_map_sha256"],
        }
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
    mapping_path = stream_root / "seed_mapping.jsonl"
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
    state_path = layout.state / f"acquisition_{stream}.sqlite3"
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
    user_agent = "MathiaOpenAlexDiscovery/1.0 (+https://github.com/murillo128/mathia)"
    host_last_request: dict[str, float] = {}
    robots_cache: dict[str, urllib.robotparser.RobotFileParser] = {}
    duplicate_map: dict[str, list[str]] = defaultdict(list)
    duplicates_parquet = stream_root / "graph_v1" / "duplicate_groups.parquet"
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
                        diagnostics = json.loads(prior[1]) if prior[1] else {}
                        acquired = (raw_matches[0], norm, prior[2], url, diagnostics)
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
                    host_last_request=host_last_request,
                )
                content_type = response["content_type"]
                with raw.open("rb") as raw_stream:
                    is_pdf = raw_stream.read(5) == b"%PDF-"
                suffix = (
                    ".pdf"
                    if is_pdf
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
                        json.dumps(diagnostics, sort_keys=True),
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
                downloaded_bytes = max(
                    getattr(error, "downloaded_bytes", 0),
                    (
                        retained_download.stat().st_size
                        if retained_download.is_file()
                        else 0
                    ),
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
            if stream == "riemann":
                relevance = {
                    "filter_decision": record.get("filter_decision"),
                    "text_score": record.get("text_score"),
                    "graph_pass": record.get("graph_pass"),
                    "acceptance_reason": record.get("acceptance_reason"),
                    "mechanism_tags": text_relevance(record.get("title"))["rules"],
                    "cites_known_seed": bool(record.get("cites_seed")),
                }
            else:
                lens_ids = set(record.get("ecosystem_lens_ids") or [])
                relevance = {
                    "graph_pass": record.get("graph_pass"),
                    "acceptance_reason": record.get("acceptance_reason"),
                    "ecosystem_lens_ids": sorted(lens_ids),
                    "candidate_family_ids": record.get("candidate_family_ids") or [],
                    "selection_basis": record.get("selection_basis") or [],
                    "saturation_status": record.get("saturation_status"),
                    "frozen_seed_release": agnostic_release_identity,
                    "related_frozen_seed_evidence": [
                        {
                            "source_id": seed["source_id"],
                            "used_unit_ids": seed.get("used_unit_ids") or [],
                            "ecosystem_ids": seed.get("ecosystem_ids") or [],
                        }
                        for seed in seeds
                        if lens_ids & set(seed.get("ecosystem_ids") or [])
                    ],
                    "novelty_boundary": (
                        "OpenAlex metadata ranks this candidate but does not confirm "
                        "a new mathematical mechanism."
                    ),
                }
            successes.append(
                {
                    "source_id": seed_source_by_oa.get(
                        work_id, f"openalex_{stream}_{safe}"
                    ),
                    "openalex_id": work_id,
                    "title": record.get("title"),
                    "authors": record.get("authors") or [],
                    "year": record.get("publication_year"),
                    "type": record.get("type"),
                    "doi": normalized_doi(record.get("doi")),
                    "ids": record.get("ids") or {},
                    "open_access": record.get("open_access") or {},
                    "candidate_public_locations": urls,
                    "priority": record.get("priority_score"),
                    "relevance": relevance,
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
                    "source_version": (
                        (record.get("best_oa_location") or {}).get("version")
                        or (record.get("primary_location") or {}).get("version")
                    ),
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
    connection.close()
    result = {
        "updated_at": utc_now(),
        "stream": stream,
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
    layout: Layout,
    version: str = "riemann_fulltext_v1",
    stream: str = "riemann",
) -> dict[str, Any]:
    if stream not in {"riemann", "agnostic_mathia"}:
        raise PipelineError(f"unknown handoff stream: {stream}")
    source_root = (
        layout.riemann if stream == "riemann" else layout.agnostic
    ) / "acquisition_v1"
    target = layout.handoffs / version
    staging = layout.handoffs / f".{version}.partial"
    if target.exists():
        raise PipelineError(f"immutable handoff already exists: {target}")
    if staging.exists():
        raise PipelineError(f"incomplete handoff staging directory exists: {staging}")
    acquired = load_jsonl(source_root / "acquired.jsonl")
    if not acquired:
        raise PipelineError("cannot freeze a handoff with no usable full text")
    try:
        (staging / "raw").mkdir(parents=True)
        (staging / "normalized").mkdir()
        frozen_rows = []
        for row in acquired:
            raw_source = Path(row["raw_path"])
            normalized_source = Path(row["normalized_path"])
            staged_raw = staging / "raw" / raw_source.name
            staged_normalized = staging / "normalized" / normalized_source.name
            final_raw = target / "raw" / raw_source.name
            final_normalized = target / "normalized" / normalized_source.name
            shutil.copyfile(raw_source, staged_raw)
            shutil.copyfile(normalized_source, staged_normalized)
            if sha256_file(staged_raw) != row["raw_sha256"]:
                raise PipelineError(f"raw copy hash mismatch: {staged_raw}")
            if sha256_file(staged_normalized) != row["normalized_sha256"]:
                raise PipelineError(
                    f"normalized copy hash mismatch: {staged_normalized}"
                )
            frozen = dict(row)
            frozen["raw_path"] = str(final_raw)
            frozen["normalized_path"] = str(final_normalized)
            frozen["handoff_version"] = version
            frozen_rows.append(frozen)
        manifest = staging / "manifest.jsonl"
        write_jsonl(manifest, frozen_rows)
        files = []
        for path in sorted(item for item in staging.rglob("*") if item.is_file()):
            files.append(
                {
                    "path": str(path.relative_to(staging)),
                    "bytes": path.stat().st_size,
                    "sha256": sha256_file(path),
                }
            )
        content = {
            "handoff_version": version,
            "stream": stream,
            "pipeline_version": PIPELINE_VERSION,
            "frozen_at": utc_now(),
            "source_count": len(frozen_rows),
            "manifest_sha256": sha256_file(manifest),
            "files": files,
            "consumer_contract": (
                "Issue #42 reads normalized_path locally with zero network requests; this "
                "directory must be retained or copied before /mnt/openalex is detached."
            ),
            "immutable": True,
        }
        content["freeze_id"] = (
            "openalex_handoff_" + hashlib.sha256(canonical_json(content)).hexdigest()
        )
        write_json(staging / "freeze.json", content)
        os.replace(staging, target)
    except Exception:
        if staging.exists():
            shutil.rmtree(staging)
        raise
    os.chmod(target, 0o555)
    for directory, _, filenames in os.walk(target):
        os.chmod(directory, 0o555)
        for filename in filenames:
            os.chmod(Path(directory) / filename, 0o444)
    return content


def verify_handoff(path: Path) -> list[str]:
    errors = []
    root = path.resolve()
    freeze_path = path / "freeze.json"
    if not freeze_path.is_file():
        return ["missing freeze.json"]
    freeze = json.loads(freeze_path.read_text())
    claimed_freeze_id = freeze.get("freeze_id")
    freeze_payload = dict(freeze)
    freeze_payload.pop("freeze_id", None)
    expected_freeze_id = (
        "openalex_handoff_" + hashlib.sha256(canonical_json(freeze_payload)).hexdigest()
    )
    if claimed_freeze_id != expected_freeze_id:
        errors.append("freeze id mismatch")
    for item in freeze["files"]:
        target = (path / item["path"]).resolve()
        if not target.is_relative_to(root):
            errors.append(f"handoff file path escapes root: {item['path']}")
        elif not target.is_file():
            errors.append(f"missing {item['path']}")
        elif target.stat().st_size != item["bytes"]:
            errors.append(f"byte mismatch {item['path']}")
        elif sha256_file(target) != item["sha256"]:
            errors.append(f"hash mismatch {item['path']}")
    manifest = path / "manifest.jsonl"
    if manifest.is_file():
        if sha256_file(manifest) != freeze.get("manifest_sha256"):
            errors.append("manifest hash mismatch")
        manifest_rows = load_jsonl(manifest)
        if len(manifest_rows) != freeze.get("source_count"):
            errors.append("manifest source count mismatch")
        for row in manifest_rows:
            for prefix in ("raw", "normalized"):
                target = Path(row[f"{prefix}_path"]).resolve()
                if not target.is_relative_to(root):
                    errors.append(
                        f"{prefix} artifact path escapes handoff for {row['source_id']}"
                    )
                elif (
                    not target.is_file()
                    or sha256_file(target) != row[f"{prefix}_sha256"]
                ):
                    errors.append(f"{prefix} artifact mismatch for {row['source_id']}")
    else:
        errors.append("missing manifest.jsonl")
    return errors


def execution_brief(layout: Layout) -> dict[str, Any]:
    snapshot = json.loads((layout.snapshot / "works_snapshot.json").read_text())
    seeds = json.loads((layout.riemann / "seed_summary.json").read_text())
    agnostic_seeds = json.loads(
        (layout.agnostic / "seed_summary.json").read_text(encoding="utf-8")
    )
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
        "agnostic_seed_release": {
            "release_id": agnostic_seeds["release_id"],
            "freeze_id": agnostic_seeds["freeze_id"],
            "freeze_sha256": agnostic_seeds["freeze_sha256"],
            "inventory_sha256": agnostic_seeds["inventory_sha256"],
            "coverage_map_id": agnostic_seeds["coverage_map_id"],
            "coverage_map_sha256": agnostic_seeds["coverage_map_sha256"],
            "saturation_log_id": agnostic_seeds["saturation_log_id"],
            "saturation_log_sha256": agnostic_seeds["saturation_log_sha256"],
            "seed_count": agnostic_seeds["seed_count"],
            "ecosystem_count": agnostic_seeds["ecosystem_count"],
        },
        "runtime": runtime,
        "invariants": [
            "bulk/cache/temp/reduced/full-text bytes stay under /mnt/openalex",
            "abort before crossing the 20% attached-volume free-space floor",
            "OpenAlex metadata is discovery evidence, not trainable mathematical source text",
            "issue #42 corpus and freeze files are never rewritten by this pipeline",
            "only hash-bound usable local text enters a frozen full-text handoff",
            "Riemann and agnostic Mathia use separate graph and handoff namespaces",
            "the #44 ecosystems are frozen retrieval lenses, not a permanent ontology",
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
    agnostic_handoff_version: str = "agnostic_mathia_fulltext_v1",
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
        "agnostic_seed_summary": layout.agnostic / "seed_summary.json",
        "agnostic_seed_mapping_summary": layout.agnostic / "seed_mapping_summary.json",
        "agnostic_seed_mapping": layout.agnostic / "seed_mapping.jsonl",
        "agnostic_graph": layout.agnostic / "graph_v1" / "summary.json",
        "agnostic_acquisition": layout.agnostic / "acquisition_v1" / "summary.json",
        "agnostic_unavailable": layout.agnostic
        / "acquisition_v1"
        / "discovery_only_unavailable.jsonl",
        "agnostic_handoff": layout.handoffs / agnostic_handoff_version / "freeze.json",
        "agnostic_handoff_manifest": layout.handoffs
        / agnostic_handoff_version
        / "manifest.jsonl",
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
    agnostic_seeds = json.loads(required["agnostic_seed_summary"].read_text())
    agnostic_mapping = json.loads(required["agnostic_seed_mapping_summary"].read_text())
    agnostic_graph = json.loads(required["agnostic_graph"].read_text())
    agnostic_acquisition = json.loads(required["agnostic_acquisition"].read_text())
    agnostic_handoff = json.loads(required["agnostic_handoff"].read_text())
    agnostic_handoff_errors = verify_handoff(layout.handoffs / agnostic_handoff_version)
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
        for manifest_key in ("handoff_manifest", "agnostic_handoff_manifest")
        for row in load_jsonl(required[manifest_key])
        for key in ("raw_path", "normalized_path")
    )
    retained_paths.extend(
        path.resolve() for path in layout.root.rglob("*") if path.is_file()
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
            agnostic_graph.get("saturated") is True,
            handoff["source_count"] > 0,
            agnostic_handoff["source_count"] > 0,
            not handoff_errors,
            not agnostic_handoff_errors,
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
        "agnostic_seed_summary.json": required["agnostic_seed_summary"],
        "agnostic_seed_mapping_summary.json": required["agnostic_seed_mapping_summary"],
        "agnostic_seed_mapping.jsonl": required["agnostic_seed_mapping"],
        "agnostic_graph_summary.json": required["agnostic_graph"],
        "agnostic_acquisition_summary.json": required["agnostic_acquisition"],
        "agnostic_discovery_only_unavailable.jsonl": required["agnostic_unavailable"],
        "agnostic_handoff_freeze.json": required["agnostic_handoff"],
        "agnostic_handoff_manifest.jsonl": required["agnostic_handoff_manifest"],
        "query.sql": required["query"],
    }
    for name, source in copy_names.items():
        shutil.copyfile(source, output / name)
    scan_peak_used = scan.get("peak_observed_volume_used_bytes") or 0
    peak_observed_used = max(scan_peak_used, end_volume["used_bytes"])
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
            "end_used_bytes": end_volume["used_bytes"],
            "filesystem_reserved_bytes": end_volume["filesystem_reserved_bytes"],
            "scan_peak_observed_used_bytes": scan_peak_used,
            "peak_observed_used_bytes": peak_observed_used,
            "reduced_index_bytes": scan["reduced_bytes_total"],
            "handoff_bytes": sum(item["bytes"] for item in handoff["files"])
            + sum(item["bytes"] for item in agnostic_handoff["files"]),
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
            "full_text_bytes": acquisition["network_bytes_downloaded"]
            + agnostic_acquisition["network_bytes_downloaded"],
            "total_tracked_bytes": scan["network_bytes_total_all_reductions"]
            + acquisition["network_bytes_downloaded"]
            + agnostic_acquisition["network_bytes_downloaded"],
            "legacy_untracked_interrupted_download_upper_bound_bytes": scan[
                "legacy_untracked_interrupted_download_upper_bound_bytes"
            ],
            "total_possible_upper_bound_bytes": scan[
                "network_bytes_total_all_reductions"
            ]
            + acquisition["network_bytes_downloaded"]
            + agnostic_acquisition["network_bytes_downloaded"]
            + scan["legacy_untracked_interrupted_download_upper_bound_bytes"],
        },
        "seeds": mapping,
        "riemann_counts": {
            "discovered": graph["counts"]["discovered_unique"],
            "relevant": graph["counts"]["accepted_candidates"],
            "full_text_acquired": acquisition["full_text_acquired"],
            "normalized_usable": acquisition["normalized_usable"],
            "handoff_ready": handoff["source_count"],
            "duplicate_groups": graph["counts"]["duplicate_groups"],
            "discovery_only_unavailable": acquisition["discovery_only_unavailable"],
        },
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
        "agnostic_mathia": {
            "seeds": agnostic_seeds,
            "mapping": agnostic_mapping,
            "graph": {
                "counts": agnostic_graph["counts"],
                "passes": agnostic_graph["passes"],
                "saturated": agnostic_graph["saturated"],
                "candidate_counts_by_ecosystem_lens": agnostic_graph[
                    "candidate_counts_by_ecosystem_lens"
                ],
                "candidate_families": agnostic_graph["candidate_families"],
                "saturation_prior": agnostic_graph["saturation_prior"],
                "duplicate_or_already_represented": agnostic_graph[
                    "duplicate_or_already_represented"
                ],
            },
            "acquisition": agnostic_acquisition,
            "counts": {
                "discovered": agnostic_graph["counts"]["accepted_candidates"]
                + agnostic_graph["counts"]["audit_only_candidates"]
                - agnostic_graph["seed_works_in_snapshot"],
                "relevant": agnostic_graph["counts"]["accepted_candidates"]
                - agnostic_graph["seed_works_in_snapshot"],
                "full_text_acquired": agnostic_acquisition["full_text_acquired"],
                "normalized_usable": agnostic_acquisition["normalized_usable"],
                "handoff_ready": agnostic_handoff["source_count"],
                "duplicate_or_already_represented": agnostic_graph[
                    "duplicate_or_already_represented"
                ],
                "discovery_only_unavailable": agnostic_acquisition[
                    "discovery_only_unavailable"
                ],
            },
            "handoff": {
                "version": agnostic_handoff_version,
                "source_count": agnostic_handoff["source_count"],
                "freeze_id": agnostic_handoff["freeze_id"],
                "verification_errors": agnostic_handoff_errors,
                "external_path": str(layout.handoffs / agnostic_handoff_version),
            },
        },
        "agent_efficiency": {
            "works_processed_deterministically": scan["works_processed_total"],
            "works_sent_to_agent_semantic_review": 0,
            "agent_review_fraction": 0.0,
            "agent_review_batches": 0,
            "agent_review_iterations": 0,
            "candidates_per_agent_batch": [],
            "estimated_agent_input_tokens": 0,
            "estimated_agent_output_tokens": 0,
            "candidates_decided_without_llm": graph["counts"]["accepted_candidates"]
            + graph["counts"]["rejected_candidates"]
            + agnostic_graph["counts"]["accepted_candidates"]
            + agnostic_graph["counts"]["audit_only_candidates"],
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
            "agnostic_handoff_hashes_valid": not agnostic_handoff_errors,
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
- Peak observed attached-volume usage: {peak_observed_used:,} bytes (scan peak {scan_peak_used:,}; end usage {end_volume["used_bytes"]:,}).
- Tracked network: {report["network"]["total_tracked_bytes"]:,} bytes, plus at most {report["network"]["legacy_untracked_interrupted_download_upper_bound_bytes"]:,} untracked bytes from two interrupted pre-ledger shards; reduced index: {scan["reduced_bytes_total"]:,} bytes.
- Root-disk used-byte change during the captured run: {root_growth:+,}; no bulk artifact path points there.

## Riemann graph and handoff

- #42 seeds: {seeds["relevant_seed_count"]}; mapping states: {json.dumps(mapping["status_counts"], sort_keys=True)}.
- Accepted candidates: {graph["counts"]["accepted_candidates"]:,}; rejected false-positive evidence: {graph["counts"]["rejected_candidates"]:,}; graph-only review queue: {graph["counts"]["semantic_review_queue"]:,}.
- Adaptive expansion saturated: `{graph["saturated"]}` after {len(graph["passes"]) - 1} citation pass(es).
- Full text acquired / normalized / handoff ready: {acquisition["full_text_acquired"]} / {acquisition["normalized_usable"]} / {handoff["source_count"]}.
- Discovery-only unavailable in the attempted priority slice: {acquisition["discovery_only_unavailable"]}.
- Frozen handoff: `{handoff["freeze_id"]}` at `{layout.handoffs / handoff_version}`.

Every handed-off row names and hashes local raw and normalized bytes. #42 consumes those paths with zero network requests. OpenAlex abstracts and metadata remain discovery-only and are not promoted to Mathia source units.

## Agnostic Mathia frontier

- Frozen #44 seed: `{agnostic_seeds["release_id"]}` / `{agnostic_seeds["freeze_id"]}`; mapping states: {json.dumps(agnostic_mapping["status_counts"], sort_keys=True)}.
- Accepted graph rows: {agnostic_graph["counts"]["accepted_candidates"]:,}; audit-only unconnected rows: {agnostic_graph["counts"]["audit_only_candidates"]:,}; adaptive closure saturated: `{agnostic_graph["saturated"]}`.
- Confirmed material challenges to the #44 saturation prior from metadata alone: {agnostic_graph["saturation_prior"]["confirmed_material_challenges"]}; candidate challenges pending source validation: {agnostic_graph["saturation_prior"]["candidate_challenges_pending_source_validation"]}.
- Full text acquired / normalized / handoff ready: {agnostic_acquisition["full_text_acquired"]} / {agnostic_acquisition["normalized_usable"]} / {agnostic_handoff["source_count"]}.
- Discovery-only unavailable in the attempted priority slice: {agnostic_acquisition["discovery_only_unavailable"]}; duplicate/already represented seeds: {agnostic_graph["duplicate_or_already_represented"]}.
- Frozen handoff: `{agnostic_handoff["freeze_id"]}` at `{layout.handoffs / agnostic_handoff_version}`.

The 28 #44 ecosystems are retrieval and gap-audit lenses, not a permanent ontology. Candidate-family matches remain explicitly unconfirmed: the downstream source reader, not OpenAlex metadata, must decide whether they expose a genuinely new mathematical mechanism.

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
    sub.add_parser("prepare-agnostic-seeds")
    sub.add_parser("brief")
    scan = sub.add_parser("scan")
    scan.add_argument("--start", type=int, default=0)
    scan.add_argument("--limit", type=int)
    sub.add_parser("build-index")
    sub.add_parser("resolve-seeds")
    sub.add_parser("resolve-agnostic")
    sub.add_parser("expand-graph")
    sub.add_parser("expand-agnostic-graph")
    acquire = sub.add_parser("acquire")
    acquire.add_argument("--max-candidates", type=int, default=100)
    acquire.add_argument("--max-successes", type=int, default=25)
    acquire_agnostic = sub.add_parser("acquire-agnostic")
    acquire_agnostic.add_argument("--max-candidates", type=int, default=100)
    acquire_agnostic.add_argument("--max-successes", type=int, default=25)
    freeze = sub.add_parser("freeze-handoff")
    freeze.add_argument("--version", default="riemann_fulltext_v1")
    freeze_agnostic = sub.add_parser("freeze-agnostic-handoff")
    freeze_agnostic.add_argument("--version", default="agnostic_mathia_fulltext_v1")
    verify = sub.add_parser("verify-handoff")
    verify.add_argument("path", type=Path)
    stage = sub.add_parser("stage-evidence")
    stage.add_argument("--output", type=Path, required=True)
    stage.add_argument("--handoff-version", default="riemann_fulltext_v1")
    stage.add_argument(
        "--agnostic-handoff-version", default="agnostic_mathia_fulltext_v1"
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    layout = Layout.from_root(args.volume, args.root)
    layout_evidence = validate_external_layout(layout)
    if args.command == "preflight":
        result = layout_evidence
    elif args.command == "snapshot":
        result = snapshot_inventory(layout)
    elif args.command == "prepare-seeds":
        result = prepare_seeds(layout)
    elif args.command == "prepare-agnostic-seeds":
        result = prepare_agnostic_seeds(layout)
    elif args.command == "brief":
        result = execution_brief(layout)
    elif args.command == "scan":
        result = scan_snapshot(layout, args.duckdb, start=args.start, limit=args.limit)
    elif args.command == "build-index":
        result = build_offline_index(layout, args.duckdb)
    elif args.command == "resolve-seeds":
        result = resolve_seed_mappings(layout, args.duckdb)
    elif args.command == "resolve-agnostic":
        result = resolve_agnostic_mappings(layout, args.duckdb)
    elif args.command == "expand-graph":
        result = expand_graph(layout, args.duckdb)
    elif args.command == "expand-agnostic-graph":
        result = expand_agnostic_graph(layout, args.duckdb)
    elif args.command == "acquire":
        result = acquire_fulltext(
            layout,
            args.duckdb,
            max_candidates=args.max_candidates,
            max_successes=args.max_successes,
        )
    elif args.command == "acquire-agnostic":
        result = acquire_fulltext(
            layout,
            args.duckdb,
            max_candidates=args.max_candidates,
            max_successes=args.max_successes,
            stream="agnostic_mathia",
        )
    elif args.command == "freeze-handoff":
        result = freeze_handoff(layout, args.version)
    elif args.command == "freeze-agnostic-handoff":
        result = freeze_handoff(layout, args.version, stream="agnostic_mathia")
    elif args.command == "stage-evidence":
        result = stage_evidence(
            layout,
            args.output,
            args.handoff_version,
            args.agnostic_handoff_version,
        )
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
