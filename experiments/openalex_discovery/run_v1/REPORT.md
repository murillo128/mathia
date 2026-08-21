# OpenAlex offline discovery report

Final decision: `OPENALEX_OFFLINE_DISCOVERY_READY`

## Snapshot and storage

- OpenAlex snapshot: `2026-06-26`; manifest SHA-256 `10c1785b4a6f9757823fc6dd005a052716e2c510ea751659cab4bcfba4c35e2a`.
- Full works scan: 510,372,821 records in 2,446 Parquet shards.
- Cache decision: streaming; compressed JSONL is 665,688,383,258 bytes versus 402,612,364,902 safe cache bytes.
- Attached volume: `/dev/sdc` / `31bc41c2-d76b-45b3-8178-2d685bffb8fa` at `/mnt/openalex`; 20% floor 107,995,658,650 bytes.
- Peak observed attached-volume usage: 37,436,706,816 bytes (scan peak 36,961,906,688; end usage 37,436,706,816).
- Tracked network: 760,368,370,564 bytes, plus at most 606,176,445 untracked bytes from two interrupted pre-ledger shards; reduced index: 36,006,953,934 bytes.
- Root-disk used-byte change during the captured run: +20,463,026,176; no bulk artifact path points there.

## Riemann graph and handoff

- #42 seeds: 393; mapping states: {"ambiguous": 1, "resolved": 389, "unresolved": 3}.
- Accepted candidates: 11,753; rejected false-positive evidence: 25,155; graph-only review queue: 26,005.
- Adaptive expansion saturated: `True` after 3 citation pass(es).
- Full text acquired / normalized / handoff ready: 25 / 25 / 25.
- Discovery-only unavailable in the attempted priority slice: 162.
- Frozen handoff: `openalex_handoff_37e490bf05210c91ef3e9a721b3389373a4fac3182a06554ad9388f80b118b67` at `/mnt/openalex/openalex/handoffs/riemann_fulltext_v1`.

Every handed-off row names and hashes local raw and normalized bytes. #42 consumes those paths with zero network requests. OpenAlex abstracts and metadata remain discovery-only and are not promoted to Mathia source units.

## Agnostic Mathia frontier

- Frozen #44 seed: `agnostic-mathia-full-v1` / `freeze_eeeeb89af3d2ac75d1ff5dad5623b63d1d24dfbddb965beca2f1c4aac9f9867f`; mapping states: {"ambiguous": 2, "resolved": 5, "unresolved": 21}.
- Accepted graph rows: 321; audit-only unconnected rows: 946; adaptive closure saturated: `True`.
- Confirmed material challenges to the #44 saturation prior from metadata alone: 0; candidate challenges pending source validation: 168.
- Full text acquired / normalized / handoff ready: 25 / 25 / 25.
- Discovery-only unavailable in the attempted priority slice: 34; duplicate/already represented seeds: 5.
- Frozen handoff: `openalex_handoff_3d4d9dbc4f55086f956e8c1f3deff54814ecbe3618a24b8b8aa5d2850ab23132` at `/mnt/openalex/openalex/handoffs/agnostic_mathia_fulltext_v1`.

The 28 #44 ecosystems are retrieval and gap-audit lenses, not a permanent ontology. Candidate-family matches remain explicitly unconfirmed: the downstream source reader, not OpenAlex metadata, must decide whether they expose a genuinely new mathematical mechanism.

## Agent-compute accounting

The 510,372,821-work scan, seed matching, graph passes, ranking, acquisition, normalization, hashes, and reports were deterministic. Zero candidates were sent to agent semantic review in zero batches; ambiguous graph-only records remain quarantined.

## Retention

Keep the frozen handoff until #42 has copied every consumed artifact into its own retained external store. Temporary shards are already deleted. The volume may be detached or deleted only after that explicit preservation step and a separate owner-authorized operation.
