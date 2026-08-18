"""Small, inspectable corpus pipeline for Mathia issue #42.

The JSONL ledger is experiment-local provenance, not a reusable dataset DSL.  Raw
and normalized full text live outside Git because most freely accessible sources
do not grant redistribution rights.
"""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import shutil
import subprocess
import sys
import tempfile
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Any, Iterable


HERE = Path(__file__).resolve().parent
DEFAULT_ARTIFACT_ROOT = Path("/workspace/mathia-artifacts/riemann-corpus-v0")
INVENTORY_PATH = HERE / "inventory.jsonl"
ROUTES_PATH = HERE / "discovery_routes.json"
CURATED_PATH = HERE / "curated_sources.json"
SCREENING_OVERRIDES_PATH = HERE / "screening_overrides.json"
METADATA_OVERRIDES_PATH = HERE / "metadata_overrides.json"
PILOT_SELECTION_PATH = HERE / "pilot_selection.json"
UNIT_PLAN_PATH = HERE / "unit_plan.json"
PILOT_ROOT = HERE / "pilot_12"
USER_AGENT = "Mathia-Riemann-Corpus/0.1 (research corpus; contact via github.com/murillo128/mathia)"

STOPWORDS = {
    "a",
    "and",
    "for",
    "function",
    "hypothesis",
    "of",
    "on",
    "the",
    "theory",
    "to",
}


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def canonical_json(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_jsonl(path: Path, values: Iterable[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = "".join(canonical_json(value) + "\n" for value in values)
    path.write_text(payload, encoding="utf-8")


def normalize_title(title: str) -> str:
    folded = unicodedata.normalize("NFKD", title).encode("ascii", "ignore").decode("ascii")
    return re.sub(r"[^a-z0-9]+", " ", folded.lower()).strip()


def is_nonclassical_title_neighbor(normalized_title: str) -> bool:
    """Reject recurring homonyms/other zeta theories unless RH is explicit in the title."""
    if title_contains_phrase(normalized_title, "riemann hypothesis"):
        return False
    return any(
        title_contains_phrase(normalized_title, phrase)
        for phrase in (
            "riemann surface",
            "riemann surfaces",
            "riemann liouville",
            "riemann hilbert",
            "hilbert class",
            "hurwitz zeta",
            "selberg zeta",
            "epstein zeta",
            "zeta function regularization",
        )
    )


def title_is_plausibly_relevant(title: str, route: dict[str, Any]) -> bool:
    normalized = normalize_title(title)
    if is_nonclassical_title_neighbor(normalized):
        return False
    title_tokens = set(normalized.split())
    query_tokens = {
        token
        for token in normalize_title(route["query"]).split()
        if token not in STOPWORDS and len(token) > 2
    }
    if route["route_id"] in {"nyman_beurling", "debruijn_newman", "hilbert_polya"}:
        return len(title_tokens & query_tokens) >= 1
    anchor = bool(title_tokens & {"riemann", "zeta"}) or {"l", "functions"} <= title_tokens
    return anchor and len(title_tokens & query_tokens) >= min(2, len(query_tokens))


def openalex_url(route: dict[str, Any]) -> str:
    if route.get("mode") == "title":
        parameters = {
            "filter": f'title.search:"{route["query"]}"',
            "per-page": route["per_page"],
            "sort": "cited_by_count:desc",
            "mailto": "codex@example.invalid",
        }
    else:
        parameters = {
            "search": route["query"],
            "filter": f'cited_by_count:>{max(0, int(route["min_citations"]) - 1)}',
            "per-page": route["per_page"],
            "mailto": "codex@example.invalid",
        }
    params = urllib.parse.urlencode(parameters)
    return "https://api.openalex.org/works?" + params


def fetch_openalex_ids(ids: Iterable[str]) -> list[dict[str, Any]]:
    identifiers = sorted({identifier.rsplit("/", 1)[-1] for identifier in ids})
    works: list[dict[str, Any]] = []
    for offset in range(0, len(identifiers), 40):
        batch = identifiers[offset : offset + 40]
        params = urllib.parse.urlencode(
            {
                "filter": "openalex_id:" + "|".join(batch),
                "per-page": 200,
                "mailto": "codex@example.invalid",
            }
        )
        works.extend(fetch_json("https://api.openalex.org/works?" + params).get("results") or [])
        time.sleep(0.1)
    return works


def fetch_json(url: str, timeout: int = 45) -> Any:
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT, "Accept": "application/json"})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return json.load(response)


def inverted_abstract(work: dict[str, Any]) -> str | None:
    inverted = work.get("abstract_inverted_index")
    if not inverted:
        return None
    positions: list[tuple[int, str]] = []
    for token, offsets in inverted.items():
        positions.extend((offset, token) for offset in offsets)
    return " ".join(token for _, token in sorted(positions))


def openalex_authors(work: dict[str, Any]) -> list[str]:
    names = []
    for authorship in work.get("authorships") or []:
        name = (authorship.get("author") or {}).get("display_name")
        if name:
            names.append(name)
    return names


def best_open_location(work: dict[str, Any]) -> dict[str, Any]:
    location = work.get("best_oa_location") or {}
    return {
        "landing_page_url": location.get("landing_page_url"),
        "pdf_url": location.get("pdf_url"),
        "license": location.get("license"),
        "version": location.get("version"),
        "source": (location.get("source") or {}).get("display_name"),
    }


def route_record(work: dict[str, Any], route: dict[str, Any]) -> dict[str, Any]:
    open_access = work.get("open_access") or {}
    location = best_open_location(work)
    cited = int(work.get("cited_by_count") or 0)
    plausible = title_is_plausibly_relevant(work.get("display_name") or "", route)
    core = plausible and cited >= int(route["min_citations"])
    status = "relevant" if core else "screened-out"
    if not plausible:
        reason = "title-search false positive: insufficient RH/zeta/mechanism overlap"
    elif cited < int(route["min_citations"]):
        reason = (
            "long-tail candidate below the route's predeclared citation cutoff; retained as a known "
            "candidate but not treated as established core literature"
        )
    else:
        reason = None
    openalex_id = (work.get("id") or "").rsplit("/", 1)[-1]
    return {
        "source_id": f"openalex_{openalex_id.lower()}",
        "title": work.get("display_name"),
        "authors": openalex_authors(work),
        "year": work.get("publication_year"),
        "version": f"OpenAlex work snapshot retrieved {utc_now()}",
        "identifiers": {
            key: value
            for key, value in {
                "openalex": work.get("id"),
                "doi": work.get("doi"),
                "pmid": (work.get("ids") or {}).get("pmid"),
            }.items()
            if value
        },
        "canonical_url": work.get("doi") or location["landing_page_url"] or work.get("id"),
        "acquisition_url": location["pdf_url"],
        "source_type": work.get("type") or "unknown",
        "tags": list(route["tags"]),
        "access_status": (
            f'openalex-{open_access.get("oa_status") or "oa"}'
            if open_access.get("is_oa")
            else "no-open-copy-located"
        ),
        "license": location["license"] or "not reported by OpenAlex; external local cache only",
        "discovery_methods": [f'OpenAlex title route {route["route_id"]}'],
        "discovery_routes": [route["route_id"]],
        "scope_status": status,
        "screening_reason": reason,
        "cited_by_count_at_discovery": cited,
        "openalex_type": work.get("type"),
        "openalex_oa": open_access,
        "openalex_best_location": location,
        "abstract": inverted_abstract(work),
        "pilot_candidate": False,
        "selected_for_pilot": False,
        "acquisition_status": "not-attempted" if core else "not-applicable-screened-out",
        "acquisition_warnings": [],
    }


def merge_record(existing: dict[str, Any], incoming: dict[str, Any]) -> dict[str, Any]:
    merged = dict(existing)
    for field in ("tags", "discovery_methods", "discovery_routes"):
        merged[field] = sorted(set(existing.get(field) or []) | set(incoming.get(field) or []))
    merged["cited_by_count_at_discovery"] = max(
        int(existing.get("cited_by_count_at_discovery") or 0),
        int(incoming.get("cited_by_count_at_discovery") or 0),
    )
    if existing.get("scope_status") != "relevant" and incoming.get("scope_status") == "relevant":
        merged["scope_status"] = "relevant"
        merged["screening_reason"] = None
        merged["acquisition_status"] = "not-attempted"
    return merged


def author_keys(record: dict[str, Any]) -> set[str]:
    keys = set()
    for author in record.get("authors") or []:
        normalized = normalize_title(author)
        if normalized:
            keys.add(normalized.split()[-1])
    return keys


def curated_match_id(
    candidate: dict[str, Any],
    curated: list[dict[str, Any]],
    doi_to_id: dict[str, str],
) -> str | None:
    candidate_doi = doi_key(candidate)
    if candidate_doi and candidate_doi in doi_to_id:
        return doi_to_id[candidate_doi]
    candidate_title = normalize_title(candidate.get("title") or "")
    candidate_authors = author_keys(candidate)
    candidate_year = candidate.get("year")
    for source in curated:
        if normalize_title(source["title"]) != candidate_title:
            continue
        if len(candidate_title.split()) < 4:
            continue
        source_year = source.get("year")
        if isinstance(source_year, int) and isinstance(candidate_year, int) and abs(source_year - candidate_year) > 2:
            continue
        if candidate_authors & author_keys(source):
            return source["source_id"]
    return None


def work_matches_curated(work: dict[str, Any], source: dict[str, Any]) -> bool:
    work_doi = (work.get("doi") or "").lower().removeprefix("https://doi.org/")
    source_doi = str((source.get("identifiers") or {}).get("doi") or "").lower()
    if source_doi and work_doi == source_doi:
        return True
    work_title = normalize_title(work.get("display_name") or "")
    source_title = normalize_title(source["title"])
    if work_title != source_title:
        return False
    work_year = work.get("publication_year")
    source_year = source.get("year")
    if isinstance(work_year, int) and isinstance(source_year, int) and abs(work_year - source_year) > 3:
        return False
    candidate = {"authors": openalex_authors(work)}
    return bool(author_keys(candidate) & author_keys(source))


def preserve_acquisition_state(
    record: dict[str, Any], previous: dict[str, dict[str, Any]]
) -> dict[str, Any]:
    old = previous.get(record["source_id"])
    if not old or old.get("acquisition_status") in {None, "not-attempted", "not-applicable-screened-out"}:
        return record
    preserved = dict(record)
    for key, value in old.items():
        if (
            key.startswith("acquisition")
            or key.startswith("artifact")
            or key.startswith("normalized")
            or key == "media_type"
        ):
            preserved[key] = value
    return preserved


def curated_record(source: dict[str, Any]) -> dict[str, Any]:
    return {
        **source,
        "scope_status": "relevant",
        "screening_reason": None,
        "selected_for_pilot": False,
        "acquisition_status": "not-attempted",
        "acquisition_warnings": [],
        "discovery_routes": [],
        "cited_by_count_at_discovery": None,
    }


def doi_key(record: dict[str, Any]) -> str | None:
    doi = (record.get("identifiers") or {}).get("doi")
    if not doi:
        return None
    return doi.lower().removeprefix("https://doi.org/")


def discover(artifact_root: Path) -> None:
    previous = {record["source_id"]: record for record in load_jsonl(INVENTORY_PATH)}
    routes = load_json(ROUTES_PATH)
    curated = [curated_record(source) for source in load_json(CURATED_PATH)]
    records: dict[str, dict[str, Any]] = {source["source_id"]: source for source in curated}
    doi_to_id = {key: source["source_id"] for source in curated if (key := doi_key(source))}
    discovery_log: list[dict[str, Any]] = []
    raw_root = artifact_root / "discovery" / "openalex"
    raw_root.mkdir(parents=True, exist_ok=True)

    for index, route in enumerate(routes, start=1):
        url = openalex_url(route)
        print(f"[{index}/{len(routes)}] discover {route['route_id']}", flush=True)
        data = fetch_json(url)
        write_json(raw_root / f"{route['route_id']}.json", data)
        new_unique = 0
        new_relevant = 0
        overlap = 0
        false_positive = 0
        for work in data.get("results") or []:
            candidate = route_record(work, route)
            candidate_doi = doi_key(candidate)
            matched_id = curated_match_id(candidate, curated, doi_to_id)
            if matched_id:
                records[matched_id] = merge_record(records[matched_id], candidate)
                overlap += 1
                continue
            source_id = candidate["source_id"]
            if source_id in records:
                records[source_id] = merge_record(records[source_id], candidate)
                overlap += 1
                continue
            records[source_id] = candidate
            if candidate_doi:
                doi_to_id[candidate_doi] = source_id
            new_unique += 1
            if candidate["scope_status"] == "relevant":
                new_relevant += 1
            elif candidate["screening_reason"].startswith("title-search false positive"):
                false_positive += 1
        discovery_log.append(
            {
                "route_id": route["route_id"],
                "query": route["query"],
                "retrieved": len(data.get("results") or []),
                "new_unique": new_unique,
                "new_relevant": new_relevant,
                "overlap_with_prior_routes_or_curated": overlap,
                "new_false_positive": false_positive,
                "openalex_total_matching": (data.get("meta") or {}).get("count"),
                "retrieved_at": utc_now(),
                "api_url": url,
            }
        )
        time.sleep(0.1)

    # Preserve previously inspected citation candidates so clean citation rebuilds and every
    # retained response remain auditable even when a candidate is not reached again.
    for source_id, old in previous.items():
        if source_id in records:
            continue
        if old.get("artifact_relpath") or any(
            method.startswith("pilot citation expansion round ")
            for method in old.get("discovery_methods") or []
        ):
            records[source_id] = old

    apply_screening_overrides(records.values())
    records = {
        source_id: preserve_acquisition_state(record, previous)
        for source_id, record in records.items()
    }
    ordered = sorted(records.values(), key=lambda item: (item["scope_status"] != "relevant", item["source_id"]))
    write_jsonl(INVENTORY_PATH, ordered)
    write_json(HERE / "discovery_log.json", discovery_log)
    print(
        f"wrote {len(ordered)} unique records: "
        f"{sum(item['scope_status'] == 'relevant' for item in ordered)} relevant, "
        f"{sum(item['scope_status'] != 'relevant' for item in ordered)} screened out",
        flush=True,
    )


def citation_tags(title: str) -> list[str]:
    normalized = normalize_title(title)
    tags = {"citation-expansion"}
    mappings = {
        "riemann": "rh",
        "zeta": "zeta",
        "zero": "zeros",
        "prime": "primes-zeros",
        "mollif": "mollifier",
        "density": "zero-density",
        "random matr": "random-matrix",
        "spectr": "spectral",
        "newman": "debruijn-newman",
        "nyman": "nyman-beurling",
        "explicit": "explicit-formula",
        "comput": "computation",
    }
    for needle, tag in mappings.items():
        if needle in normalized:
            tags.add(tag)
    if title_contains_phrase(normalized, "l function") or title_contains_phrase(
        normalized, "l functions"
    ):
        tags.add("l-functions")
    return sorted(tags)


def title_contains_phrase(normalized_title: str, phrase: str) -> bool:
    """Match normalized words, never a suffix such as the `l function` in `rational functions`."""
    normalized_phrase = normalize_title(phrase)
    return re.search(rf"(?:^| ){re.escape(normalized_phrase)}(?: |$)", normalized_title) is not None


def citation_is_relevant(work: dict[str, Any]) -> bool:
    title = normalize_title(work.get("display_name") or "")
    if is_nonclassical_title_neighbor(title):
        return False
    direct = any(
        title_contains_phrase(title, phrase)
        for phrase in (
            "riemann hypothesis",
            "riemann zeta",
            "zeros of the zeta",
            "prime number theorem",
            "nyman beurling",
            "de bruijn newman",
            "l functions",
            "l function",
        )
    )
    foundational_neighbor = any(
        title_contains_phrase(title, phrase)
        for phrase in (
            "analytic number theory",
            "multiplicative number theory",
            "random matrices frobenius eigenvalues and monodromy",
            "number theory trace formulas and discrete groups",
        )
    )
    return direct or foundational_neighbor


def has_noncitation_discovery(record: dict[str, Any]) -> bool:
    return any(
        not method.startswith("pilot citation expansion round ")
        for method in record.get("discovery_methods") or []
    )


def reset_citation_discovery(records: Iterable[dict[str, Any]]) -> None:
    """Remove old citation routing before a clean breadth-first rebuild."""
    for record in records:
        methods = record.get("discovery_methods") or []
        if not any(method.startswith("pilot citation expansion round ") for method in methods):
            continue
        noncitation = [
            method for method in methods if not method.startswith("pilot citation expansion round ")
        ]
        record["discovery_methods"] = noncitation
        record.pop("citation_parent_openalex_ids", None)
        record["tags"] = [tag for tag in record.get("tags") or [] if tag != "citation-expansion"]
        if not noncitation and record.get("scope_status") != "duplicate":
            record["scope_status"] = "screened-out"
            record["screening_reason"] = "citation candidate not reached by the current clean expansion"


def authors_overlap(first: dict[str, Any], second: dict[str, Any]) -> bool:
    return bool(author_keys(first) & author_keys(second))


def normalize_dedupe_title(title: str) -> str:
    value = html.unescape(title)
    value = re.sub(r"<[^>]+>", " ", value)
    value = value.translate(str.maketrans({"ζ": " zeta ", "Ζ": " zeta ", "½": " 1/2 ", "’": "'"}))
    value = value.replace("'", "")
    value = re.sub(r"(?<=[A-Za-z])(?=\d)|(?<=\d)(?=[A-Za-z])", " ", value)
    return normalize_title(value)


def arxiv_keys(record: dict[str, Any]) -> set[str]:
    identifiers = record.get("identifiers") or {}
    locations = record.get("openalex_best_location") or {}
    candidates = [
        identifiers.get("arxiv"),
        identifiers.get("doi"),
        record.get("canonical_url"),
        record.get("acquisition_url"),
        locations.get("landing_page_url"),
        locations.get("pdf_url"),
    ]
    keys = set()
    for candidate in candidates:
        if not candidate:
            continue
        normalized = str(candidate).lower().replace("10.48550/arxiv.", "arxiv.org/abs/")
        match = re.search(
            r"arxiv\.org/(?:abs|pdf)/(?:[a-z-]+(?:\.[a-z-]+)?/)?(\d{4}\.\d{4,5}|\d+)",
            normalized,
        )
        if match:
            keys.add(match.group(1))
        elif re.fullmatch(r"\d{4}\.\d{4,5}", normalized):
            keys.add(normalized)
    return keys


def records_likely_same_work(first: dict[str, Any], second: dict[str, Any]) -> bool:
    if not authors_overlap(first, second):
        return False
    first_doi, second_doi = doi_key(first), doi_key(second)
    if first_doi and first_doi == second_doi:
        return True
    if arxiv_keys(first) & arxiv_keys(second):
        return True
    first_year, second_year = first.get("year"), second.get("year")
    if (
        isinstance(first_year, int)
        and isinstance(second_year, int)
        and abs(first_year - second_year) > 5
    ):
        return False
    first_title_tokens = normalize_dedupe_title(first.get("title") or "").split()
    second_title_tokens = normalize_dedupe_title(second.get("title") or "").split()
    if not first_title_tokens or not second_title_tokens:
        return False
    series_markers = {"i", "ii", "iii", "iv", "v", "vi", "vii", "viii", "ix", "x"}
    first_marker = first_title_tokens[-1] if first_title_tokens[-1] in series_markers else None
    second_marker = second_title_tokens[-1] if second_title_tokens[-1] in series_markers else None
    if first_marker != second_marker and (first_marker or second_marker):
        return False
    first_tokens = set(first_title_tokens)
    second_tokens = set(second_title_tokens)
    is_preprint_pair = "preprint" in {first.get("source_type"), second.get("source_type")} and (
        first.get("source_type") != second.get("source_type")
    )
    if not is_preprint_pair:
        return first_year == second_year and first_tokens == second_tokens
    if first_tokens == second_tokens:
        return True
    overlap = len(first_tokens & second_tokens) / max(len(first_tokens), len(second_tokens))
    return min(len(first_tokens), len(second_tokens)) >= 5 and overlap >= 0.9


def apply_duplicate_audit(records: Iterable[dict[str, Any]]) -> None:
    """Mark inspectable exact or preprint/published duplicates without merging topic neighbors."""
    materialized = list(records)
    for record in materialized:
        generated = record.get("duplicate_audit_generated")
        legacy_generated = str(record.get("screening_reason") or "").startswith(
            "high-confidence same-work match"
        )
        if generated or legacy_generated:
            record["scope_status"] = "relevant"
            for field in (
                "duplicate_of",
                "duplicate_audit_generated",
                "version_relationship",
                "screening_reason",
            ):
                record.pop(field, None)
        record.pop("alternate_version_source_ids", None)
    curated_ids = {source["source_id"] for source in load_json(CURATED_PATH)}
    relevant = [record for record in materialized if record.get("scope_status") == "relevant"]
    adjacency: dict[str, set[str]] = defaultdict(set)
    by_id = {record["source_id"]: record for record in materialized}
    for index, first in enumerate(relevant):
        for second in relevant[index + 1 :]:
            if records_likely_same_work(first, second):
                adjacency[first["source_id"]].add(second["source_id"])
                adjacency[second["source_id"]].add(first["source_id"])

    acquisition_rank = {
        "acquired-and-normalized": 4,
        "acquired-partial-preview-and-normalized": 3,
        "acquired-partial-webtext-and-normalized": 3,
    }
    publication_rank = {
        "article": 5,
        "book": 5,
        "book-chapter": 4,
        "conference-paper": 4,
        "preprint": 1,
    }
    visited: set[str] = set()
    for source_id in sorted(adjacency):
        if source_id in visited:
            continue
        pending = [source_id]
        cluster_ids: set[str] = set()
        while pending:
            current = pending.pop()
            if current in cluster_ids:
                continue
            cluster_ids.add(current)
            pending.extend(adjacency[current] - cluster_ids)
        visited.update(cluster_ids)
        cluster = [by_id[candidate_id] for candidate_id in sorted(cluster_ids)]
        canonical = max(
            cluster,
            key=lambda record: (
                record["source_id"] in curated_ids,
                publication_rank.get(record.get("source_type"), 2),
                acquisition_rank.get(record.get("acquisition_status"), 0),
                bool(doi_key(record)),
                int(record.get("cited_by_count_at_discovery") or 0),
                record["source_id"],
            ),
        )
        alternate_ids = []
        for duplicate in cluster:
            if duplicate is canonical:
                continue
            alternate_ids.append(duplicate["source_id"])
            duplicate["scope_status"] = "duplicate"
            duplicate["duplicate_of"] = canonical["source_id"]
            is_version_pair = "preprint" in {
                duplicate.get("source_type"),
                canonical.get("source_type"),
            }
            duplicate["version_relationship"] = (
                "preprint/published-version" if is_version_pair else "duplicate-record"
            )
            duplicate["duplicate_audit_generated"] = True
            duplicate["screening_reason"] = (
                "high-confidence same-work match by normalized title, nearby year, and overlapping "
                f"author identity; canonical record {canonical['source_id']}"
            )
        canonical["alternate_version_source_ids"] = sorted(alternate_ids)


def citation_record_is_relevant(record: dict[str, Any]) -> bool:
    work_like = {
        "display_name": record.get("title"),
        "cited_by_count": record.get("cited_by_count_at_discovery"),
    }
    return citation_is_relevant(work_like)


def citation_record(work: dict[str, Any], round_number: int, parents: list[str]) -> dict[str, Any]:
    route = {
        "route_id": f"citation_round_{round_number}",
        "query": "Riemann pilot bibliography/citation expansion",
        "min_citations": 0,
        "tags": citation_tags(work.get("display_name") or ""),
    }
    record = route_record(work, route)
    relevant = citation_is_relevant(work)
    record["scope_status"] = "relevant" if relevant else "screened-out"
    record["screening_reason"] = (
        None
        if relevant
        else (
            "citation-neighborhood candidate without a direct classical-RH or declared "
            "conceptual-neighbor title signal"
        )
    )
    record["acquisition_status"] = "not-attempted" if relevant else "not-applicable-screened-out"
    record["discovery_methods"] = [f"pilot citation expansion round {round_number}"]
    record["citation_parent_openalex_ids"] = sorted(parents)
    return record


def raw_openalex_works(artifact_root: Path) -> dict[str, dict[str, Any]]:
    works: dict[str, dict[str, Any]] = {}
    for path in (artifact_root / "discovery" / "openalex").glob("*.json"):
        for work in load_json(path).get("results") or []:
            works[work["id"]] = work
    return works


def expand_citations(artifact_root: Path) -> None:
    records = load_jsonl(INVENTORY_PATH)
    reset_citation_discovery(records)
    by_id = {record["source_id"]: record for record in records}
    curated = load_json(CURATED_PATH)
    pilot_sources = [source for source in curated if source.get("pilot_candidate")]
    raw_works = raw_openalex_works(artifact_root)
    seed_works: list[dict[str, Any]] = []
    seed_log = []
    for source in pilot_sources:
        matches = [work for work in raw_works.values() if work_matches_curated(work, source)]
        seed_works.extend(matches)
        seed_log.append(
            {
                "source_id": source["source_id"],
                "openalex_matches": [work["id"] for work in matches],
                "reference_count": sum(len(work.get("referenced_works") or []) for work in matches),
            }
        )

    parent_map: dict[str, set[str]] = defaultdict(set)
    for work in seed_works:
        for reference in work.get("referenced_works") or []:
            parent_map[reference].add(work["id"])
    round_one_works = fetch_openalex_ids(parent_map)
    citation_root = artifact_root / "discovery" / "citations"
    citation_root.mkdir(parents=True, exist_ok=True)
    write_jsonl(citation_root / "round1.jsonl", round_one_works)

    existing_openalex = {
        str((record.get("identifiers") or {}).get("openalex")): record["source_id"]
        for record in records
        if (record.get("identifiers") or {}).get("openalex")
    }
    round_one_new_relevant: list[dict[str, Any]] = []
    round_stats = []

    def integrate(works: list[dict[str, Any]], round_number: int, parents_by_work: dict[str, set[str]]) -> None:
        new_unique = new_relevant = overlap = 0
        for work in works:
            work_id = work["id"]
            source_id = existing_openalex.get(work_id)
            if source_id:
                record = by_id[source_id]
                was_noncitation = has_noncitation_discovery(record)
                record["discovery_methods"] = sorted(
                    set(record.get("discovery_methods") or []) | {f"pilot citation expansion round {round_number}"}
                )
                record["citation_parent_openalex_ids"] = sorted(
                    set(record.get("citation_parent_openalex_ids") or []) | parents_by_work.get(work_id, set())
                )
                if not was_noncitation and record.get("scope_status") != "duplicate":
                    relevant = citation_is_relevant(work)
                    record["scope_status"] = "relevant" if relevant else "screened-out"
                    record["screening_reason"] = (
                        None
                        if relevant
                        else (
                            "citation-neighborhood candidate without a direct classical-RH or "
                            "declared conceptual-neighbor title signal"
                            )
                        )
                if round_number == 1 and record.get("scope_status") == "relevant":
                    round_one_new_relevant.append(work)
                overlap += 1
                continue
            record = citation_record(work, round_number, sorted(parents_by_work.get(work_id, set())))
            by_id[record["source_id"]] = record
            existing_openalex[work_id] = record["source_id"]
            new_unique += 1
            if record["scope_status"] == "relevant":
                new_relevant += 1
                if round_number == 1:
                    round_one_new_relevant.append(work)
        round_stats.append(
            {
                "round": round_number,
                "references_requested": len(parents_by_work),
                "metadata_records_returned": len(works),
                "overlap_with_inventory": overlap,
                "new_unique_candidates": new_unique,
                "new_relevant": new_relevant,
            }
        )

    integrate(round_one_works, 1, parent_map)

    second_seeds = sorted(
        round_one_new_relevant,
        key=lambda work: int(work.get("cited_by_count") or 0),
        reverse=True,
    )[:24]
    second_parent_map: dict[str, set[str]] = defaultdict(set)
    for work in second_seeds:
        for reference in work.get("referenced_works") or []:
            second_parent_map[reference].add(work["id"])
    round_two_works = fetch_openalex_ids(second_parent_map)
    write_jsonl(citation_root / "round2.jsonl", round_two_works)
    integrate(round_two_works, 2, second_parent_map)

    apply_screening_overrides(by_id.values())
    apply_duplicate_audit(by_id.values())
    ordered = sorted(by_id.values(), key=lambda item: (item["scope_status"] != "relevant", item["source_id"]))
    write_jsonl(INVENTORY_PATH, ordered)
    write_json(
        HERE / "citation_expansion_log.json",
        {
            "generated_at": utc_now(),
            "pilot_seed_resolution": seed_log,
            "rounds": round_stats,
            "round_two_seed_openalex_ids": [work["id"] for work in second_seeds],
            "stopping_rule": (
                "Stop after two reference hops from the pilot spine; compare marginal new-relevant yield "
                "with overlap and retain unsearched reference tails as a known gap."
            ),
        },
    )
    print(json.dumps(round_stats, indent=2), flush=True)


def continue_citations(artifact_root: Path) -> None:
    records = load_jsonl(INVENTORY_PATH)
    by_id = {record["source_id"]: record for record in records}
    existing_openalex = {
        str((record.get("identifiers") or {}).get("openalex")): record["source_id"]
        for record in records
        if (record.get("identifiers") or {}).get("openalex")
    }
    citation_root = artifact_root / "discovery" / "citations"
    initial_log = load_json(HERE / "citation_expansion_log.json")
    prior_continuation = list(initial_log.get("continuation_rounds") or [])
    last_round = max((int(item["round"]) for item in prior_continuation), default=2)
    frontier = [
        work
        for work in load_jsonl(citation_root / f"round{last_round}.jsonl")
        if (
            (source_id := existing_openalex.get(work["id"]))
            and by_id[source_id].get("scope_status") == "relevant"
            and f"pilot citation expansion round {last_round}"
            in (by_id[source_id].get("discovery_methods") or [])
        )
    ]
    continuation_stats = []
    stop_reason = "twelve-round practical cap reached"
    for round_number in range(last_round + 1, 13):
        seeds = sorted(frontier, key=lambda work: int(work.get("cited_by_count") or 0), reverse=True)[:24]
        parent_map: dict[str, set[str]] = defaultdict(set)
        for work in seeds:
            for reference in work.get("referenced_works") or []:
                parent_map[reference].add(work["id"])
        works = fetch_openalex_ids(parent_map)
        write_jsonl(citation_root / f"round{round_number}.jsonl", works)
        new_frontier = []
        overlap = new_unique = new_relevant = 0
        for work in works:
            work_id = work["id"]
            source_id = existing_openalex.get(work_id)
            if source_id:
                record = by_id[source_id]
                was_noncitation = has_noncitation_discovery(record)
                record["discovery_methods"] = sorted(
                    set(record.get("discovery_methods") or [])
                    | {f"pilot citation expansion round {round_number}"}
                )
                record["citation_parent_openalex_ids"] = sorted(
                    set(record.get("citation_parent_openalex_ids") or []) | parent_map.get(work_id, set())
                )
                if not was_noncitation and record.get("scope_status") != "duplicate":
                    relevant = citation_is_relevant(work)
                    record["scope_status"] = "relevant" if relevant else "screened-out"
                    record["screening_reason"] = (
                        None
                        if relevant
                        else (
                            "citation-neighborhood candidate without a direct classical-RH or "
                            "declared conceptual-neighbor title signal"
                        )
                    )
                overlap += 1
                continue
            record = citation_record(work, round_number, sorted(parent_map.get(work_id, set())))
            by_id[record["source_id"]] = record
            existing_openalex[work_id] = record["source_id"]
            new_unique += 1
            if record["scope_status"] == "relevant":
                new_relevant += 1
                new_frontier.append(work)
        continuation_stats.append(
            {
                "round": round_number,
                "frontier_seeds": len(seeds),
                "references_requested": len(parent_map),
                "metadata_records_returned": len(works),
                "overlap_with_inventory": overlap,
                "new_unique_candidates": new_unique,
                "new_relevant": new_relevant,
            }
        )
        frontier = new_frontier
        overlap_ratio = overlap / len(works) if works else 1.0
        if new_relevant == 0:
            stop_reason = f"round {round_number} produced no new relevant source"
            break
        if new_relevant <= 5 and overlap_ratio >= 0.75:
            stop_reason = (
                f"round {round_number} produced {new_relevant} new relevant sources with "
                f"{overlap_ratio:.0%} inventory overlap"
            )
            break
    apply_screening_overrides(by_id.values())
    apply_duplicate_audit(by_id.values())
    ordered = sorted(by_id.values(), key=lambda item: (item["scope_status"] != "relevant", item["source_id"]))
    write_jsonl(INVENTORY_PATH, ordered)
    write_json(
        HERE / "citation_expansion_log.json",
        {
            **initial_log,
            "continuation_rounds": prior_continuation + continuation_stats,
            "observed_stop_reason": stop_reason,
        },
    )
    print(json.dumps({"rounds": continuation_stats, "stop_reason": stop_reason}, indent=2), flush=True)


def freeze_pilot() -> None:
    records = load_jsonl(INVENTORY_PATH)
    by_id = {record["source_id"]: record for record in records}
    selection = load_json(PILOT_SELECTION_PATH)
    if len(selection) != 12 or len({item["source_id"] for item in selection}) != 12:
        raise ValueError("pilot selection must contain exactly 12 unique sources")
    orders = sorted(item["selection_order"] for item in selection)
    if orders != list(range(1, 13)):
        raise ValueError("pilot selection_order values must be exactly 1..12")
    selected_ids = {item["source_id"] for item in selection}
    for record in records:
        record["selected_for_pilot"] = record["source_id"] in selected_ids
        if record["selected_for_pilot"]:
            chosen = next(item for item in selection if item["source_id"] == record["source_id"])
            if record.get("acquisition_status") != "acquired-and-normalized":
                raise ValueError(f"pilot source {record['source_id']} lacks normalized full text")
            record["pilot_selection_order"] = chosen["selection_order"]
            record["pilot_selection_rationale"] = chosen["rationale"]
            record["pilot_alternatives"] = chosen["alternatives"]
        else:
            for field in ("pilot_selection_order", "pilot_selection_rationale", "pilot_alternatives"):
                record.pop(field, None)
    write_jsonl(INVENTORY_PATH, records)
    frozen_sources = []
    for choice in sorted(selection, key=lambda item: item["selection_order"]):
        record = by_id[choice["source_id"]]
        frozen_sources.append(
            {
                "selection_order": choice["selection_order"],
                "source_id": record["source_id"],
                "title": record["title"],
                "authors": record["authors"],
                "year": record["year"],
                "version": record["version"],
                "identifiers": record["identifiers"],
                "canonical_url": record["canonical_url"],
                "artifact_relpath": record["artifact_relpath"],
                "normalized_relpath": record["normalized_relpath"],
                "artifact_sha256": record["artifact_sha256"],
                "normalized_sha256": record["normalized_sha256"],
                "normalized_page_count": record["normalized_page_count"],
                "license": record["license"],
                "selection_rationale": choice["rationale"],
                "alternatives": choice["alternatives"],
            }
        )
    frozen_identity = {
        "source_count": 12,
        "selection_rule": (
            "Exactly twelve lawfully acquired and normalized sources selected after Part I for "
            "heterogeneity of mathematical mechanism, era, and exposition; not statistical representativeness."
        ),
        "sources": frozen_sources,
    }
    payload = {
        "frozen_at": utc_now(),
        "inventory_sha256": sha256_file(INVENTORY_PATH),
        **frozen_identity,
    }
    # The source freeze identifies the selected bytes and rule, not a broad-ledger timestamp.
    # This lets an independently audited ledger be rebound without pretending unchanged source
    # artifacts or completed source-bound analyses are a different pilot.
    payload["freeze_id"] = "riemann_pilot12_" + sha256_bytes(
        canonical_json(frozen_identity).encode("utf-8")
    )
    write_json(HERE / "pilot_12" / "freeze.json", payload)
    print(payload["freeze_id"])


def segment_units(artifact_root: Path) -> None:
    """Extract frozen, contiguous semantic units without placing source text in Git."""
    freeze = load_json(PILOT_ROOT / "freeze.json")
    plan = load_json(UNIT_PLAN_PATH)
    selected = {source["source_id"]: source for source in freeze["sources"]}
    if len(plan) != 24 or len({unit["unit_id"] for unit in plan}) != 24:
        raise ValueError("unit plan must contain exactly 24 unique units")
    counts = Counter(unit["source_id"] for unit in plan)
    if set(counts) != set(selected) or set(counts.values()) != {2}:
        raise ValueError("unit plan must contain exactly two units from each frozen source")

    unit_root = artifact_root / "pilot_12" / "units"
    unit_root.mkdir(parents=True, exist_ok=True)
    manifest = []
    for unit in plan:
        source = selected[unit["source_id"]]
        normalized_path = artifact_root / source["normalized_relpath"]
        if sha256_file(normalized_path) != source["normalized_sha256"]:
            raise ValueError(f"normalized source hash drifted: {source['source_id']}")
        lines = normalized_path.read_text(encoding="utf-8").splitlines(keepends=True)
        start, end = int(unit["line_start"]), int(unit["line_end"])
        if start < 1 or end < start or end > len(lines):
            raise ValueError(f"invalid line range for {unit['unit_id']}: {start}-{end}")
        content = "".join(lines[start - 1 : end])
        if not content.endswith("\n"):
            content += "\n"
        unit_path = unit_root / f"{unit['unit_id']}.txt"
        unit_path.write_text(content, encoding="utf-8")
        page_markers = [
            int(match.group(1))
            for match in re.finditer(r"<!-- source-page: (\d+) -->", content)
        ]
        manifest.append(
            {
                **unit,
                "freeze_id": freeze["freeze_id"],
                "source_normalized_sha256": source["normalized_sha256"],
                "unit_artifact_relpath": unit_path.relative_to(artifact_root).as_posix(),
                "unit_sha256": sha256_file(unit_path),
                "unit_bytes": unit_path.stat().st_size,
                "source_page_markers_inside_unit": page_markers,
                "storage": "external-local-not-git",
            }
        )
    write_jsonl(PILOT_ROOT / "units.jsonl", manifest)
    print(f"segmented {len(manifest)} units from {len(selected)} frozen sources")


class VisibleTextParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.parts: list[str] = []
        self.hidden_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in {"script", "style", "noscript", "svg"}:
            self.hidden_depth += 1
        elif tag in {"p", "div", "section", "article", "h1", "h2", "h3", "h4", "li", "br"}:
            self.parts.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style", "noscript", "svg"} and self.hidden_depth:
            self.hidden_depth -= 1
        elif tag in {"p", "div", "section", "article", "li"}:
            self.parts.append("\n")

    def handle_data(self, data: str) -> None:
        if not self.hidden_depth:
            self.parts.append(data)

    def text(self) -> str:
        value = html.unescape("".join(self.parts))
        value = re.sub(r"[ \t]+", " ", value)
        value = re.sub(r"\n{3,}", "\n\n", value)
        return value.strip() + "\n"


def request_bytes(url: str, timeout: int = 90) -> tuple[bytes, str, str]:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "application/pdf,text/plain,text/html,application/xhtml+xml;q=0.9,*/*;q=0.2",
        },
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        content = response.read(80 * 1024 * 1024 + 1)
        if len(content) > 80 * 1024 * 1024:
            raise ValueError("artifact exceeds the 80 MiB per-source safety cap")
        return content, response.headers.get_content_type(), response.geturl()


def normalize_pdf(raw_path: Path, normalized_path: Path) -> tuple[int, list[str]]:
    warnings: list[str] = ["PDF extraction may degrade formulas, ligatures, or reading order; original retained"]
    with tempfile.TemporaryDirectory(prefix="mathia-riemann-") as temporary:
        extracted = Path(temporary) / "extracted.txt"
        completed = subprocess.run(
            ["pdftotext", "-enc", "UTF-8", "-layout", str(raw_path), str(extracted)],
            capture_output=True,
            text=True,
            check=False,
        )
        if completed.returncode:
            raise ValueError(f"pdftotext failed: {completed.stderr.strip()[:400]}")
        value = extracted.read_text(encoding="utf-8", errors="replace")
        pages = value.split("\f")
        if len(re.sub(r"\s+", "", value)) < 1000:
            if not shutil.which("pdftoppm") or not shutil.which("tesseract"):
                raise ValueError(
                    "PDF has no usable text layer and OCR tools pdftoppm/tesseract are unavailable"
                )
            image_prefix = Path(temporary) / "ocr-page"
            rendered = subprocess.run(
                ["pdftoppm", "-r", "240", "-png", str(raw_path), str(image_prefix)],
                capture_output=True,
                text=True,
                check=False,
            )
            if rendered.returncode:
                raise ValueError(f"pdftoppm OCR rendering failed: {rendered.stderr.strip()[:400]}")
            pages = []
            for image_path in sorted(Path(temporary).glob("ocr-page-*.png")):
                recognized = subprocess.run(
                    ["tesseract", str(image_path), "stdout", "-l", "eng"],
                    capture_output=True,
                    text=True,
                    check=False,
                )
                if recognized.returncode:
                    raise ValueError(
                        f"tesseract OCR failed for {image_path.name}: "
                        f"{recognized.stderr.strip()[:400]}"
                    )
                pages.append(recognized.stdout)
            value = "\f".join(pages)
            warnings.append(
                "OCR fallback used because the PDF text layer was empty; formulas and symbols are "
                "lower-confidence and must be checked against the scan"
            )
    rendered = []
    for index, page in enumerate(pages, start=1):
        if not page.strip() and index == len(pages):
            continue
        rendered.append(f"\n<!-- source-page: {index} -->\n\n{page.strip()}\n")
    normalized_path.write_text("".join(rendered).lstrip(), encoding="utf-8")
    if "�" in value:
        warnings.append("Unicode replacement characters found")
    return len(rendered), warnings


def normalize_html(raw_path: Path, normalized_path: Path) -> tuple[int, list[str]]:
    parser = VisibleTextParser()
    parser.feed(raw_path.read_text(encoding="utf-8", errors="replace"))
    normalized_path.write_text(parser.text(), encoding="utf-8")
    return 1, ["HTML visible-text extraction does not preserve every formula or layout feature"]


def acquire_one(record: dict[str, Any], artifact_root: Path) -> dict[str, Any]:
    updated = dict(record)
    updated["acquisition_attempted_at"] = utc_now()
    updated["acquisition_warnings"] = list(record.get("acquisition_warnings") or [])
    url = record.get("acquisition_url")
    if not url:
        updated["acquisition_status"] = "metadata-only-no-open-full-text-located"
        updated["acquisition_warnings"].append("No lawful open full-text URL located during discovery")
        return updated

    source_id = record["source_id"]
    raw_dir = artifact_root / "raw"
    normalized_dir = artifact_root / "normalized"
    raw_dir.mkdir(parents=True, exist_ok=True)
    normalized_dir.mkdir(parents=True, exist_ok=True)
    try:
        content, media_type, final_url = request_bytes(url)
        if content.startswith(b"%PDF-"):
            suffix = ".pdf"
            media_type = "application/pdf"
        elif media_type in {"text/html", "application/xhtml+xml"} or b"<html" in content[:1000].lower():
            suffix = ".html"
            media_type = "text/html"
        elif media_type in {"text/plain", "application/x-tex", "text/x-tex"}:
            suffix = ".txt" if media_type == "text/plain" else ".tex"
        else:
            raise ValueError(f"unsupported or suspicious media type {media_type!r}")
        raw_path = raw_dir / f"{source_id}{suffix}"
        raw_path.write_bytes(content)
        updated.update(
            {
                "acquisition_final_url": final_url,
                "media_type": media_type,
                "artifact_relpath": raw_path.relative_to(artifact_root).as_posix(),
                "artifact_sha256": sha256_file(raw_path),
                "artifact_bytes": raw_path.stat().st_size,
                "artifact_storage": "external-local-not-git",
            }
        )
        normalized_path = normalized_dir / f"{source_id}.txt"
        if media_type == "application/pdf":
            page_count, warnings = normalize_pdf(raw_path, normalized_path)
        elif media_type == "text/html":
            page_count, warnings = normalize_html(raw_path, normalized_path)
        else:
            value = content.decode("utf-8", errors="replace")
            normalized_path.write_text(value, encoding="utf-8")
            page_count, warnings = 1, []
        normalized_size = normalized_path.stat().st_size
        if normalized_size < 1000:
            raise ValueError(f"normalized text suspiciously short ({normalized_size} bytes)")
        updated.update(
            {
                "acquisition_status": "acquired-and-normalized",
                "normalized_relpath": normalized_path.relative_to(artifact_root).as_posix(),
                "normalized_sha256": sha256_file(normalized_path),
                "normalized_bytes": normalized_size,
                "normalized_page_count": page_count,
                "acquisition_warnings": sorted(set(updated["acquisition_warnings"] + warnings)),
            }
        )
    except (OSError, ValueError, urllib.error.URLError) as error:
        updated["acquisition_status"] = "acquisition-or-normalization-failed"
        updated["acquisition_warnings"].append(f"{type(error).__name__}: {error}")
    return updated


def acquire(artifact_root: Path, workers: int, retry_failed: bool) -> None:
    records = load_jsonl(INVENTORY_PATH)
    eligible = []
    for record in records:
        if record.get("scope_status") != "relevant":
            continue
        status = record.get("acquisition_status")
        if status == "not-attempted" or (retry_failed and status == "acquisition-or-normalization-failed"):
            eligible.append(record)
    print(f"acquiring {len(eligible)} relevant sources with {workers} workers", flush=True)
    updates: dict[str, dict[str, Any]] = {}
    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {executor.submit(acquire_one, record, artifact_root): record for record in eligible}
        for index, future in enumerate(as_completed(futures), start=1):
            updated = future.result()
            updates[updated["source_id"]] = updated
            print(f"[{index}/{len(eligible)}] {updated['source_id']}: {updated['acquisition_status']}", flush=True)
    final = [updates.get(record["source_id"], record) for record in records]
    write_jsonl(INVENTORY_PATH, final)
    print("inventory acquisition state updated", flush=True)


def apply_screening_overrides(records: Iterable[dict[str, Any]]) -> None:
    overrides = load_json(SCREENING_OVERRIDES_PATH)
    for record in records:
        if record["source_id"] in overrides:
            override = overrides[record["source_id"]]
            if isinstance(override, str):
                record["scope_status"] = "screened-out"
                record["screening_reason"] = override
            else:
                record["scope_status"] = override["scope_status"]
                record["screening_reason"] = override["reason"]
                if override.get("duplicate_of"):
                    record["duplicate_of"] = override["duplicate_of"]


def apply_metadata_overrides(records: Iterable[dict[str, Any]]) -> None:
    overrides = load_json(METADATA_OVERRIDES_PATH)
    for record in records:
        for key, value in overrides.get(record["source_id"], {}).items():
            record[key] = value


def retained_artifact_candidates(artifact_root: Path, source_id: str, kind: str) -> list[Path]:
    directory = artifact_root / kind
    return sorted(path for path in directory.glob(f"{source_id}.*") if path.is_file())


def add_orphaned_retained_responses(
    records: list[dict[str, Any]], artifact_root: Path
) -> None:
    """Recover ledger rows for retained responses omitted by a superseded discovery frontier."""
    known_ids = {record["source_id"] for record in records}
    retained_ids = {
        path.stem
        for kind in ("raw", "normalized")
        for path in (artifact_root / kind).glob("*")
        if path.is_file()
    }
    orphan_ids = sorted(retained_ids - known_ids)
    if not orphan_ids:
        return
    openalex_ids = {
        source_id: "W" + source_id.removeprefix("openalex_w")
        for source_id in orphan_ids
        if source_id.startswith("openalex_w")
    }
    try:
        works = fetch_openalex_ids(openalex_ids.values())
    except (OSError, ValueError, urllib.error.URLError):
        works = []
    works_by_id = {
        f"openalex_{work['id'].rsplit('/', 1)[-1].lower()}": work for work in works
    }
    route = {
        "route_id": "retained_response_reconciliation",
        "query": "retained response from superseded discovery frontier",
        "min_citations": sys.maxsize,
        "tags": ["retained-response"],
    }
    for source_id in orphan_ids:
        work = works_by_id.get(source_id)
        if work:
            record = route_record(work, route)
        else:
            record = {
                "source_id": source_id,
                "title": f"Metadata unresolved for retained response {source_id}",
                "authors": [],
                "year": None,
                "version": "retained response ledger reconciliation",
                "identifiers": {},
                "canonical_url": None,
                "acquisition_url": None,
                "source_type": "unknown",
                "tags": ["retained-response"],
                "access_status": "metadata-recovery-unavailable",
                "license": "not reported; external local cache only",
                "acquisition_warnings": [],
                "selected_for_pilot": False,
            }
        record.update(
            {
                "scope_status": "screened-out",
                "screening_reason": (
                    "retained response from a superseded discovery frontier; not reached by the "
                    "current clean citation expansion"
                ),
                "acquisition_status": "non-fulltext-response",
                "discovery_methods": ["retained response ledger reconciliation"],
                "pilot_candidate": False,
                "selected_for_pilot": False,
            }
        )
        record["acquisition_warnings"] = sorted(
            set(
                (record.get("acquisition_warnings") or [])
                + ["Retained response reconciled after the citation-frontier audit"]
            )
        )
        records.append(record)


def reconcile_retained_artifacts(records: Iterable[dict[str, Any]], artifact_root: Path) -> None:
    """Bind every retained download/normalization response to the ledger, including failures."""
    for record in records:
        raw_candidates = retained_artifact_candidates(artifact_root, record["source_id"], "raw")
        normalized_candidates = retained_artifact_candidates(
            artifact_root, record["source_id"], "normalized"
        )
        if len(raw_candidates) > 1 or len(normalized_candidates) > 1:
            raise ValueError(f"ambiguous retained artifacts for {record['source_id']}")
        if raw_candidates:
            raw_path = raw_candidates[0]
            record["artifact_relpath"] = raw_path.relative_to(artifact_root).as_posix()
            record["artifact_sha256"] = sha256_file(raw_path)
            record["artifact_bytes"] = raw_path.stat().st_size
            record["artifact_storage"] = "external-local-not-git"
            if not record.get("media_type"):
                record["media_type"] = {
                    ".pdf": "application/pdf",
                    ".html": "text/html",
                    ".txt": "text/plain",
                    ".tex": "application/x-tex",
                }.get(raw_path.suffix.lower(), "application/octet-stream")
        if normalized_candidates:
            normalized_path = normalized_candidates[0]
            record["normalized_relpath"] = normalized_path.relative_to(artifact_root).as_posix()
            record["normalized_sha256"] = sha256_file(normalized_path)
            record["normalized_bytes"] = normalized_path.stat().st_size
            markers = re.findall(
                r"<!-- source-page: (\d+) -->",
                normalized_path.read_text(encoding="utf-8", errors="replace"),
            )
            record["normalized_page_count"] = len(markers) or 1


def recover_short_scanned_pdfs(records: Iterable[dict[str, Any]], artifact_root: Path) -> None:
    for record in records:
        if record.get("scope_status") not in {"relevant", "duplicate"}:
            continue
        artifact_relpath = record.get("artifact_relpath")
        normalized_relpath = record.get("normalized_relpath")
        if not artifact_relpath or not normalized_relpath or record.get("media_type") != "application/pdf":
            continue
        normalized_path = artifact_root / normalized_relpath
        if normalized_path.stat().st_size >= 1000:
            continue
        raw_path = artifact_root / artifact_relpath
        page_count, warnings = normalize_pdf(raw_path, normalized_path)
        record.update(
            {
                "acquisition_status": "acquired-and-normalized",
                "normalized_sha256": sha256_file(normalized_path),
                "normalized_bytes": normalized_path.stat().st_size,
                "normalized_page_count": page_count,
                "acquisition_warnings": sorted(
                    set((record.get("acquisition_warnings") or []) + warnings)
                ),
            }
        )


def audit_ledger(artifact_root: Path) -> None:
    records = load_jsonl(INVENTORY_PATH)
    add_orphaned_retained_responses(records, artifact_root)
    reconcile_retained_artifacts(records, artifact_root)
    apply_metadata_overrides(records)
    for record in records:
        if "citation-expansion" not in (record.get("tags") or []):
            continue
        if citation_record_is_relevant(record):
            if record.get("scope_status") != "duplicate":
                record["scope_status"] = "relevant"
                record["screening_reason"] = None
                if record.get("acquisition_status") == "not-applicable-screened-out":
                    record["acquisition_status"] = "not-attempted"
        else:
            record["scope_status"] = "screened-out"
            record["screening_reason"] = (
                "citation-neighborhood candidate without an explicit RH/zeta/L-function/prime-number "
                "link or a declared foundational-neighbor title"
            )
            if record.get("acquisition_status") == "not-attempted":
                record["acquisition_status"] = "not-applicable-screened-out"
    apply_screening_overrides(records)
    apply_duplicate_audit(records)
    recover_short_scanned_pdfs(records, artifact_root)
    for record in records:
        status = record.get("acquisition_status")
        warnings = record.get("acquisition_warnings") or []
        last_warning = warnings[-1] if warnings else ""
        if status == "acquired-and-normalized" and record.get("media_type") == "text/html":
            record["acquisition_status"] = "acquired-partial-webtext-and-normalized"
            warnings.append("HTML response retained as partial web text; not counted as source full text")
        elif (
            status == "acquired-and-normalized"
            and record.get("source_type") == "book"
            and int(record.get("normalized_page_count") or 0) < 20
        ):
            record["acquisition_status"] = "acquired-partial-preview-and-normalized"
            warnings.append("Short book preview retained; not counted as source full text")
        elif status == "acquisition-or-normalization-failed":
            if "403" in last_warning:
                record["acquisition_status"] = "blocked-http-403"
            elif "429" in last_warning:
                record["acquisition_status"] = "blocked-http-429"
            elif "404" in last_warning:
                record["acquisition_status"] = "source-url-missing-http-404"
            elif "CERTIFICATE_VERIFY_FAILED" in last_warning:
                record["acquisition_status"] = "blocked-tls-validation"
            elif "timed out" in last_warning:
                record["acquisition_status"] = "download-timeout"
            elif "suspiciously short" in last_warning:
                record["acquisition_status"] = "non-fulltext-response"
            else:
                record["acquisition_status"] = "other-download-failure"
        record["acquisition_warnings"] = sorted(set(warnings))
    write_jsonl(INVENTORY_PATH, records)


def verify_artifacts(artifact_root: Path) -> list[str]:
    errors: list[str] = []
    records = load_jsonl(INVENTORY_PATH)
    referenced_paths: set[str] = set()
    for record in records:
        for path_field, hash_field in (
            ("artifact_relpath", "artifact_sha256"),
            ("normalized_relpath", "normalized_sha256"),
        ):
            if not record.get(path_field):
                continue
            referenced_paths.add(record[path_field])
            path = artifact_root / record[path_field]
            if not record.get(hash_field):
                errors.append(f"{record['source_id']}: {path_field} has no recorded {hash_field}")
            elif not path.is_file():
                errors.append(f"{record['source_id']}: missing {path_field} {path}")
            elif sha256_file(path) != record[hash_field]:
                errors.append(f"{record['source_id']}: hash mismatch for {path_field}")
    for kind in ("raw", "normalized"):
        directory = artifact_root / kind
        if not directory.is_dir():
            continue
        for path in directory.iterdir():
            if path.is_file() and path.relative_to(artifact_root).as_posix() not in referenced_paths:
                errors.append(f"unledgered retained artifact: {path}")
    return errors


def report(artifact_root: Path) -> dict[str, Any]:
    records = load_jsonl(INVENTORY_PATH)
    relevant = [record for record in records if record.get("scope_status") == "relevant"]
    acquired = [record for record in relevant if record.get("acquisition_status") == "acquired-and-normalized"]
    normalized = [
        record
        for record in relevant
        if record.get("acquisition_status")
        in {
            "acquired-and-normalized",
            "acquired-partial-preview-and-normalized",
            "acquired-partial-webtext-and-normalized",
        }
    ]
    screened_acquired = [
        record
        for record in records
        if record.get("scope_status") != "relevant"
        and record.get("acquisition_status")
        in {
            "acquired-and-normalized",
            "acquired-partial-preview-and-normalized",
            "acquired-partial-webtext-and-normalized",
        }
    ]
    discovery = load_json(HERE / "discovery_log.json")
    tag_counts = Counter(tag for record in relevant for tag in record.get("tags") or [])
    type_counts = Counter(record.get("source_type") or "unknown" for record in relevant)
    eras = Counter()
    for record in relevant:
        year = record.get("year")
        if not isinstance(year, int):
            eras["unknown"] += 1
        elif year < 1900:
            eras["pre-1900"] += 1
        elif year < 1950:
            eras["1900-1949"] += 1
        elif year < 2000:
            eras["1950-1999"] += 1
        else:
            eras["2000-present"] += 1
    status_counts = Counter(record.get("acquisition_status") or "unknown" for record in relevant)
    scope_counts = Counter(record.get("scope_status") or "unknown" for record in records)
    audited_citation_yield = Counter()
    for record in relevant:
        citation_rounds = []
        noncitation_methods = []
        for method in record.get("discovery_methods") or []:
            match = re.fullmatch(r"pilot citation expansion round (\d+)", method)
            if match:
                citation_rounds.append(int(match.group(1)))
            else:
                noncitation_methods.append(method)
        if citation_rounds and not noncitation_methods:
            audited_citation_yield[min(citation_rounds)] += 1
    citation_log_path = HERE / "citation_expansion_log.json"
    citation_log = load_json(citation_log_path)
    recorded_rounds = [
        int(item["round"])
        for item in (citation_log.get("rounds") or [])
        + (citation_log.get("continuation_rounds") or [])
    ]
    max_round = max(recorded_rounds, default=2)
    citation_yield = {
        str(round_number): audited_citation_yield[round_number]
        for round_number in range(1, max_round + 1)
    }
    stop_reason = citation_log.get("observed_stop_reason", "two-hop expansion completed")
    late_start = max(1, max_round - 2)
    late_yield = sum(
        audited_citation_yield[round_number] for round_number in range(late_start, max_round + 1)
    )
    if "cap reached" in stop_reason:
        saturation_interpretation = (
            f"The declared {max_round}-round practical cap was reached, with {late_yield} audited "
            f"citation-only relevant additions in rounds {late_start}-{max_round}. The route is "
            "not claimed saturated or complete."
        )
    else:
        saturation_interpretation = (
            f"Expansion stopped because {stop_reason}; this is practical saturation only under "
            "the declared route and title-level screen, not a completeness claim."
        )
    citation_log["post_screening_audit"] = {
        "audited_citation_only_marginal_relevant_yield": citation_yield,
        "interpretation": saturation_interpretation,
    }
    write_json(citation_log_path, citation_log)

    generated = {
        "generated_at": utc_now(),
        "inventory_sha256": sha256_file(INVENTORY_PATH),
        "artifact_root": str(artifact_root),
        "inventoried_unique_sources": len(records),
        "relevant_sources": len(relevant),
        "screened_out_candidates": len(records) - len(relevant),
        "scope_status_counts": dict(sorted(scope_counts.items())),
        "acquired_full_text": len(acquired),
        "normalized_texts": len(normalized),
        "partial_text_or_preview_normalized": len(normalized) - len(acquired),
        "screened_out_artifacts_preserved": len(screened_acquired),
        "acquisition_status_counts": dict(sorted(status_counts.items())),
        "source_type_counts": dict(sorted(type_counts.items())),
        "era_counts": dict(sorted(eras.items())),
        "tag_counts": dict(sorted(tag_counts.items())),
        "discovery_route_marginal_yields": discovery,
        "route_overlap_discoveries": sum(item["overlap_with_prior_routes_or_curated"] for item in discovery),
        "audited_citation_only_marginal_relevant_yield": citation_yield,
        "citation_saturation_interpretation": saturation_interpretation,
        "artifact_verification_errors": verify_artifacts(artifact_root),
        "storage_note": "Full text and normalized derivatives are retained outside Git at artifact_root.",
    }
    write_json(HERE / "corpus_report.json", generated)
    return generated


def validate_inventory(artifact_root: Path, require_artifacts: bool) -> list[str]:
    errors: list[str] = []
    records = load_jsonl(INVENTORY_PATH)
    ids = [record.get("source_id") for record in records]
    if len(ids) != len(set(ids)):
        errors.append("source_id values are not unique")
    required = {
        "source_id",
        "title",
        "authors",
        "year",
        "version",
        "identifiers",
        "canonical_url",
        "source_type",
        "tags",
        "access_status",
        "license",
        "acquisition_status",
        "acquisition_warnings",
        "scope_status",
    }
    for record in records:
        missing = sorted(required - set(record))
        if missing:
            errors.append(f"{record.get('source_id')}: missing {missing}")
        if record.get("scope_status") == "relevant" and record.get("acquisition_status") == "not-attempted":
            errors.append(f"{record.get('source_id')}: relevant source has no acquisition attempt")
        if record.get("scope_status") == "relevant":
            for field in ("title", "authors", "year", "canonical_url"):
                if not record.get(field):
                    errors.append(f"{record.get('source_id')}: relevant source has empty {field}")
        if record.get("acquisition_status") in {
            "acquired-and-normalized",
            "acquired-partial-preview-and-normalized",
            "acquired-partial-webtext-and-normalized",
        }:
            for field in (
                "artifact_relpath",
                "normalized_relpath",
                "artifact_sha256",
                "normalized_sha256",
            ):
                if not record.get(field):
                    errors.append(f"{record.get('source_id')}: acquired source missing {field}")
    by_id = {record["source_id"]: record for record in records}
    for record in records:
        if record.get("scope_status") != "duplicate":
            continue
        duplicate_of = record.get("duplicate_of")
        if not duplicate_of:
            errors.append(f"{record['source_id']}: duplicate record lacks duplicate_of")
        elif duplicate_of not in by_id:
            errors.append(f"{record['source_id']}: duplicate_of target is absent: {duplicate_of}")
    relevant = [record for record in records if record.get("scope_status") == "relevant"]
    for index, first in enumerate(relevant):
        for second in relevant[index + 1 :]:
            if records_likely_same_work(first, second):
                errors.append(
                    "unresolved relevant duplicate: "
                    f"{first['source_id']} and {second['source_id']}"
                )
    if require_artifacts:
        errors.extend(verify_artifacts(artifact_root))
    return errors


def validate_pilot(artifact_root: Path, require_artifacts: bool) -> list[str]:
    errors: list[str] = []
    freeze_path = PILOT_ROOT / "freeze.json"
    units_path = PILOT_ROOT / "units.jsonl"
    if not freeze_path.is_file() or not units_path.is_file():
        return ["pilot freeze.json or units.jsonl is missing"]
    freeze = load_json(freeze_path)
    units = load_jsonl(units_path)
    source_ids = [source["source_id"] for source in freeze.get("sources") or []]
    unit_ids = [unit.get("unit_id") for unit in units]
    if freeze.get("source_count") != 12 or len(source_ids) != 12 or len(set(source_ids)) != 12:
        errors.append("pilot freeze must contain exactly 12 unique sources")
    if freeze.get("inventory_sha256") != sha256_file(INVENTORY_PATH):
        errors.append("pilot freeze inventory_sha256 does not match committed inventory")
    if len(units) != 24 or len(set(unit_ids)) != 24:
        errors.append("pilot must contain exactly 24 unique semantic units")
    unit_counts = Counter(unit.get("source_id") for unit in units)
    if set(unit_counts) != set(source_ids) or set(unit_counts.values()) != {2}:
        errors.append("pilot must contain exactly two semantic units per frozen source")
    for unit in units:
        if unit.get("freeze_id") != freeze.get("freeze_id"):
            errors.append(f"{unit.get('unit_id')}: freeze_id mismatch")
        if unit.get("line_start", 0) < 1 or unit.get("line_end", 0) < unit.get("line_start", 0):
            errors.append(f"{unit.get('unit_id')}: invalid line boundaries")
        if require_artifacts:
            unit_path = artifact_root / str(unit.get("unit_artifact_relpath"))
            if not unit_path.is_file():
                errors.append(f"{unit.get('unit_id')}: external unit artifact missing")
            elif sha256_file(unit_path) != unit.get("unit_sha256"):
                errors.append(f"{unit.get('unit_id')}: external unit artifact hash mismatch")
    inventory = {record["source_id"]: record for record in load_jsonl(INVENTORY_PATH)}
    selected_in_inventory = {
        source_id for source_id, record in inventory.items() if record.get("selected_for_pilot")
    }
    if selected_in_inventory != set(source_ids):
        errors.append("inventory selected_for_pilot flags do not match the freeze")
    expected_units = set(unit_ids)
    for filename in (
        "pass1_spontaneous.jsonl",
        "pass2_directed.jsonl",
        "pass3_adversarial.jsonl",
        "pass4_revised.jsonl",
    ):
        path = PILOT_ROOT / "analyses" / filename
        if not path.is_file():
            errors.append(f"missing analysis pass: {filename}")
            continue
        rows = load_jsonl(path)
        ids = [row.get("unit_id") for row in rows]
        if len(rows) != 24 or set(ids) != expected_units or len(set(ids)) != 24:
            errors.append(f"{filename}: must cover each of the 24 units exactly once")
    provenance_path = PILOT_ROOT / "provenance.json"
    if not provenance_path.is_file():
        errors.append("pilot provenance.json is missing")
    elif load_json(provenance_path).get("freeze_id") != freeze.get("freeze_id"):
        errors.append("pilot provenance freeze_id mismatch")
    manifest_path = PILOT_ROOT / "analysis_manifest.json"
    if not manifest_path.is_file():
        errors.append("pilot analysis_manifest.json is missing")
    else:
        manifest = load_json(manifest_path)
        if manifest.get("freeze_id") != freeze.get("freeze_id"):
            errors.append("analysis manifest freeze_id mismatch")
        if manifest.get("units_manifest_sha256") != sha256_file(units_path):
            errors.append("analysis manifest units hash mismatch")
        if manifest.get("provenance_sha256") != sha256_file(provenance_path):
            errors.append("analysis manifest provenance hash mismatch")
        for group in ("prompts", "raw_analysis_outputs", "derived_outputs"):
            for entry in manifest.get(group) or []:
                path = PILOT_ROOT / entry["path"]
                if not path.is_file():
                    errors.append(f"analysis manifest path missing: {entry['path']}")
                elif sha256_file(path) != entry.get("sha256"):
                    errors.append(f"analysis manifest hash mismatch: {entry['path']}")
                if group == "raw_analysis_outputs" and path.is_file():
                    if len(load_jsonl(path)) != entry.get("record_count"):
                        errors.append(f"analysis manifest record count mismatch: {entry['path']}")
    return errors


def write_analysis_manifest() -> None:
    freeze = load_json(PILOT_ROOT / "freeze.json")
    analysis_files = [
        PILOT_ROOT / "analyses" / filename
        for filename in (
            "pass1_spontaneous.jsonl",
            "pass2_directed.jsonl",
            "pass3_adversarial.jsonl",
            "pass4_revised.jsonl",
        )
    ]
    prompt_files = sorted((PILOT_ROOT / "prompts").glob("*.md"))
    derived_files = [
        PILOT_ROOT / filename
        for filename in ("SYNTHESIS.md", "AUDIT.md", "FUTURE_EVALUATION.md", "REPORT.md")
    ]
    missing = [str(path) for path in analysis_files + prompt_files + derived_files if not path.is_file()]
    if missing:
        raise ValueError(f"cannot manifest missing files: {missing}")
    payload = {
        "generated_at": utc_now(),
        "freeze_id": freeze["freeze_id"],
        "units_manifest_sha256": sha256_file(PILOT_ROOT / "units.jsonl"),
        "provenance_sha256": sha256_file(PILOT_ROOT / "provenance.json"),
        "prompts": [
            {
                "path": path.relative_to(PILOT_ROOT).as_posix(),
                "sha256": sha256_file(path),
            }
            for path in prompt_files
        ],
        "raw_analysis_outputs": [
            {
                "path": path.relative_to(PILOT_ROOT).as_posix(),
                "sha256": sha256_file(path),
                "record_count": len(load_jsonl(path)),
            }
            for path in analysis_files
        ],
        "derived_outputs": [
            {
                "path": path.relative_to(PILOT_ROOT).as_posix(),
                "sha256": sha256_file(path),
            }
            for path in derived_files
        ],
    }
    write_json(PILOT_ROOT / "analysis_manifest.json", payload)
    print("analysis manifest written")


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--artifact-root", type=Path, default=DEFAULT_ARTIFACT_ROOT)
    subparsers = parser.add_subparsers(dest="command", required=True)
    subparsers.add_parser("discover")
    subparsers.add_parser("expand-citations")
    subparsers.add_parser("continue-citations")
    subparsers.add_parser("freeze-pilot")
    subparsers.add_parser("segment-units")
    subparsers.add_parser("analysis-manifest")
    acquire_parser = subparsers.add_parser("acquire")
    acquire_parser.add_argument("--workers", type=int, default=6)
    acquire_parser.add_argument("--retry-failed", action="store_true")
    subparsers.add_parser("audit-ledger")
    subparsers.add_parser("report")
    validate_parser = subparsers.add_parser("validate")
    validate_parser.add_argument("--require-artifacts", action="store_true")
    validate_pilot_parser = subparsers.add_parser("validate-pilot")
    validate_pilot_parser.add_argument("--require-artifacts", action="store_true")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    if args.command == "discover":
        discover(args.artifact_root)
    elif args.command == "expand-citations":
        expand_citations(args.artifact_root)
    elif args.command == "continue-citations":
        continue_citations(args.artifact_root)
    elif args.command == "freeze-pilot":
        freeze_pilot()
    elif args.command == "segment-units":
        segment_units(args.artifact_root)
    elif args.command == "analysis-manifest":
        write_analysis_manifest()
    elif args.command == "acquire":
        if not INVENTORY_PATH.exists():
            raise SystemExit("run discover first")
        acquire(args.artifact_root, workers=args.workers, retry_failed=args.retry_failed)
    elif args.command == "report":
        print(json.dumps(report(args.artifact_root), indent=2))
    elif args.command == "audit-ledger":
        audit_ledger(args.artifact_root)
        print("ledger screening and acquisition audit applied")
    elif args.command == "validate":
        errors = validate_inventory(args.artifact_root, args.require_artifacts)
        if errors:
            print("\n".join(f"ERROR: {error}" for error in errors), file=sys.stderr)
            return 1
        print("inventory validation passed")
    elif args.command == "validate-pilot":
        errors = validate_pilot(args.artifact_root, args.require_artifacts)
        if errors:
            print("\n".join(f"ERROR: {error}" for error in errors), file=sys.stderr)
            return 1
        print("pilot validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
