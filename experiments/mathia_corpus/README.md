# Shared Mathia corpus interchange v1

This experiment-local module implements the minimum compatibility boundary required
by issues `#42` and `#44`. It is not a permanent ontology or a training design.

The trainable roles are `source`, `interpretation`, and `synthesis`. Optional visual
representations are sidecars. Every object keeps stable identity, exact content hash,
source-span lineage, derivation, teacher provenance when applicable, acceptance and
training eligibility, licensing boundaries, and representation dependencies outside
the model-visible text.

The deterministic renderer exposes only mathematical source material and the linked
conceptual derivative. It never emits corpus origin, object IDs, quality state,
teacher identity, or other audit metadata. The mixer accepts records from any corpus
through this same interface, detects identical cross-corpus content hashes, and
deduplicates identical source objects while retaining genuinely different
interpretations.

Acceptance semantics are shared:

- `accepted`: eligible for the positive trainable manifest;
- `quarantined`: potentially useful but context, source, or representation quality is
  insufficient;
- `rejected`: unsuitable positive material;
- `evaluation_only`: QA or behavioral evidence that must not enter training.

An eligible text-only record cannot depend on an unavailable essential sidecar.
