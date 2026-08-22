# Riemann corpus v2 acquisition loop

This document records the experiment-local acquisition procedure required by
GitHub issue #42. It does not define a Mathia interchange format and does not
change `mathia-interchange-v1`.

## Durable state

`experiments/riemann_corpus/full_corpus_v2/acquisition_search.jsonl` is the
source/work ledger. It preserves every candidate route and every request
outcome. `acquisition_retry_state.json` is a derived, resumable queue view keyed
by source, candidate route, and host. New attempts record the attempt ordinal,
host, outcome class, `Retry-After` when present, backoff, next eligible time,
remaining alternate-route status, and terminal reason where applicable.

The queue has four outcome classes:

- `success` — usable full text was acquired and normalized;
- `temporary-retryable` — 429, transient 5xx, timeout, TLS, DNS, or connection
  failure;
- `route-specific-failure` — the current location is blocked, gated, metadata
  only, or not usable full text, so another lawful route must be sought;
- `terminal-for-route` — the exact URL is persistently absent or policy-blocked.

A terminal route is not a terminal work.

## Scheduler policy

Refresh the derived state without making requests:

```bash
PYTHONPATH=. python3 experiments/riemann_corpus/full_corpus_v2.py \
  write-acquisition-retry-state
```

Run one bounded host-aware sweep:

```bash
PYTHONPATH=. python3 experiments/riemann_corpus/full_corpus_v2.py \
  --round-id persistent-recovery-round-N \
  --per-host-limit 1 \
  --max-route-attempts 5 \
  run-acquisition-loop
```

The scheduler is sequential and conservative by default. It obeys
`Retry-After`; otherwise it uses exponential backoff with deterministic jitter.
It never sleeps the whole corpus because one host is cooling down. Eligible
work on another host, cached normalization, segmentation, and analysis may
continue. Both the attempt ledger and retry state are written after every
request, so stopping the command does not erase completed work.

The per-route attempt ceiling is an explicit conservative exhaustion policy,
not a global stop rule. A source cannot be called exhausted while another route
is unattempted, a temporary route is eligible/cooling, or the alternate-version
search is incomplete.

## Alternate-version recovery

Before classifying a work as unavailable, search by stable identifier, title,
and authorship for lawful arXiv/preprint, author-hosted, institutional,
proceedings, historical/public-domain, or publisher-authorized copies. Preserve
the version relationship and keep bibliographically distinct records distinct;
deduplicate mathematical evidence through canonical lineage and hashes.

Never bypass authentication, paywalls, robots policy, or access controls.

## Saturation gate

`record-acquisition-frontier` must fail while any source has:

- an incomplete alternate-version search;
- an unattempted or retry-eligible route;
- a host/route still cooling down.

The acquisition report must include the v1 recovery funnel: recovered by retry,
recovered through another lawful route, still pending, cooling, and exhausted
only after the recorded policy. A zero-attempt final sweep is valid evidence
only after all of these gates pass.

## Current-session OpenAlex handoff boundary

On 2026-08-20 the owner explicitly deferred all further OpenAlex API discovery
to a separate, independent Codex session after the current execution finishes.
This execution must not query the OpenAlex API or wait on its host cooldown.
The already captured discovery-host state and per-work pending statuses remain
in the retry-state artifact as handoff provenance; they must not be rewritten as
completed or exhausted merely to close the current run.

Direct lawful candidate URLs already present in the durable ledger may still be
normalized, inspected, and processed locally. The deferred OpenAlex backlog is
not acquisition-saturation evidence.

Issue #46 now owns the one-time OpenAlex scan and may publish two immutable
full-text handoff streams: `riemann_fulltext_vN` and
`agnostic_mathia_fulltext_vN`. Issue #42 consumes both streams strictly from
their frozen local manifests and artifacts, with zero repeated acquisition.
Riemann handoffs continue this release; agnostic handoffs form a separate
supplement parented to the immutable merged `agnostic-mathia-full-v1` release.
They are never inserted into the Riemann namespace.

The deterministic intake state is
`experiments/riemann_corpus/full_corpus_v2/execution/openalex_handoff_cutoff.json`.
It records each consumed handoff's immutable identity, manifest hash, preserved
artifact root, stream-specific disposition and processing metrics. Before a
final release is frozen, it must also record a finite immutable #46 cutoff and
exactly one disposition for every handoff published through that cutoff. A Git
manifest whose required local bytes have disappeared is not a valid consumed
handoff.

The finite cutoff is now frozen as
`issue46_cutoff_1436fb46a70e1c7221e65a40968ca3589f7a5c265c00feca59d1a0a33edce59d`.
It contains exactly the locally preserved `riemann_fulltext_v1` and
`agnostic_mathia_fulltext_v1` handoffs. Both streams remain
`copied_pending_analysis`, so finalization is still mechanically blocked until
their separate processing pipelines finish and update the derived state.
Metadata-only discovery candidates are not processable mathematical source
text and must not enter semantic-unit analysis.
