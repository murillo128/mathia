---
id: PA-separating-hyperplane-certificate
type: prior-art
canonical_name: "Separating-hyperplane certificate"
aliases:
  - "convex separation certificate"
kind: conceptual-mechanism
topics:
  - convexity
  - duality
  - certificates
---

# Separating-hyperplane certificate

## What it is

A separating hyperplane converts disjoint convex feasibility into one affine witness whose sign can be checked over each set.

## Relation to RH / Mathia research

It is a reusable bridge from a primal global-exclusion claim to a dual certificate and motivates searching for a supporting direction instead of comparing every cross-pair.

## Known scope and limits

Convexity gives the witness its global authority. Interlocking nonconvex components may defeat any single linear separator, and this note asserts no new RH application.

## Related prior art

- None recorded in the retained evidence used for this projection.

## Evidence and provenance

- **Agnostic Mathia v1 accepted object:** `experiments/agnostic_mathia_corpus/release_v1/records.jsonl#mathia_interpretation_b58b2394e112e71362c2c1c12731bb895ad814c934ae239fda7b967c41716c44`; source `boyd_vandenberghe_convex_2009`; unit `cso_separation`.
- **Projection decision:** `research/prior_art/catalog.json#PA-separating-hyperplane-certificate`.
