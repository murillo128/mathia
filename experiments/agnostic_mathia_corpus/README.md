# Domain-agnostic Mathia corpus v1 (`#44`)

This experiment-local package builds and validates the finite domain-agnostic
Mathia corpus required by issue `#44`. It contains a working 24-ecosystem coverage
map, a 22-source seed inventory, 19 hash-bound sources used by 72 traceable semantic
units, and one proof or worked development in every ecosystem. The release also
contains linked source-grounded interpretations, fourteen accepted cross-source
syntheses, negative and evaluation-only evidence, four geometry sidecars,
adaptive-acquisition and candidate-level saturation logs, fresh adversarial QA, and
a frozen final report. The eligible rendering is roughly twenty thousand words.

The release is a corpus, not a benchmark, model, permanent ontology, training-mix
decision, or authorization to train.

## Validate

From the repository root:

```bash
python3 -m experiments.agnostic_mathia_corpus validate
python3 -m unittest tests.test_agnostic_mathia_corpus -v
```

The first command validates the committed release without requiring bulky source
downloads. To recheck the exact external artifacts acquired for this release:

```bash
python3 -m experiments.agnostic_mathia_corpus \
  --artifact-root /workspace/mathia-artifacts/agnostic-corpus-v1 \
  validate --require-artifacts
```

`acquire` downloads only the declared public or author-hosted URLs, records exact
hashes and effective URLs, and stores all source artifacts outside Git. It does not
bypass access controls. `build` deterministically rematerializes the release from
the curated catalogs, acquisition snapshot, sidecars, and recorded QA. The
`review_content_freeze.json` manifest binds the exact candidate seen by fresh QA
while excluding QA rows, the final report, and the final freeze to avoid a
self-reference; every QA row and the final freeze must reference that manifest.

## Artifact and licensing boundary

Git contains short independently written mathematical restatements, exact source
locators, hashes, attribution and license boundaries, conceptual derivatives,
audits, and small original SVG schematics. Full source artifacts remain in the
external artifact root. Open sources retain their GFDL or Creative Commons terms.
For copyrighted but author-hosted references, only metadata, locators, and original
mathematical restatements are committed.

The shared interface and origin-blind renderer live in
[`../mathia_corpus`](../mathia_corpus/). The synthetic mixed manifest uses a
representative issue `#42` fixture because the issue `#42` corpus-scale release is
still underway; it is not a substitute for that release and chooses no future
sampling ratio.
