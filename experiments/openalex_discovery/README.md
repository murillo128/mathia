# Offline OpenAlex discovery (`#46`)

This experiment-local pipeline scans one declared OpenAlex snapshot into a
compact offline scholarly locator and a richer mathematics/Riemann subgraph.
It then acquires and normalizes public full text for a frozen handoff that issue
`#42` can consume without network requests.

OpenAlex metadata is discovery evidence, not mathematical source text and not a
third trainable Mathia corpus. Raw snapshot shards, reduced Parquet files,
downloaded works, and normalized full text stay on the attached volume. Git
contains only code and compact provenance, counts, hashes, and handoff indexes.

## External layout

The expected mount is `/mnt/openalex`; the pipeline refuses a path that is not
its own mountpoint or resolves to the root filesystem. It preserves at least
20% of the volume and checks the floor before every shard and acquisition.

```text
/mnt/openalex/openalex/
  snapshot/  tmp/  reduced/  riemann/  handoffs/  logs/  state/
```

## Deterministic execution

```bash
python3 -m experiments.openalex_discovery preflight
python3 -m experiments.openalex_discovery snapshot
python3 -m experiments.openalex_discovery prepare-seeds
python3 -m experiments.openalex_discovery brief
python3 -m experiments.openalex_discovery scan
python3 -m experiments.openalex_discovery build-index
python3 -m experiments.openalex_discovery resolve-seeds
python3 -m experiments.openalex_discovery expand-graph
python3 -m experiments.openalex_discovery acquire
python3 -m experiments.openalex_discovery freeze-handoff
python3 -m experiments.openalex_discovery verify-handoff \
  /mnt/openalex/openalex/handoffs/riemann_fulltext_v1
python3 -m experiments.openalex_discovery stage-evidence \
  --output /mnt/openalex/openalex/state/repo_evidence_v1
```

The full scan uses unsigned S3, downloads one Parquet shard to attached-volume
temporary storage, writes and hashes a reduced part, checkpoints it in
SQLite, deletes the shard, and resumes at the next unfinished object. The
all-work locator is deliberately narrow; nested abstracts, topics, locations,
and references are retained only for mathematics-adjacent, seed, textual, or
direct-citation rows. `reduced/openalex.duckdb` installs local views over the
Parquet parts and requires no OpenAlex API.

OpenAlex-ID and DOI equality are the only exact seed matches. Exact-title rows
are retained as resolution candidates, then checked against seed authors (with
publication year used as a tie-breaker); unresolved or ambiguous titles never
become seed truth. The scan database records every completed shard download as
an append-only event, including bytes from superseded reduction versions.

Acquisition uses deterministic public-route scheduling and text extraction.
It does not bypass authentication, paywalls, robots, or other access controls.
The frozen handoff is read-only and contains actual raw and normalized bytes,
not just URLs.
