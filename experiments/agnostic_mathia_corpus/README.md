# Domain-agnostic Mathia corpus v1 (`#44`)

This experiment-local package builds and validates the finite domain-agnostic
Mathia corpus required by issue `#44`. It contains a working 28-ecosystem coverage
map, a 28-source inventory, 25 hash-bound sources used by 98 traceable semantic
units, and at least one proof or worked development in every ecosystem. The release
also contains linked source-grounded interpretations, eighteen accepted cross-source
syntheses, negative and evaluation-only evidence, four geometry sidecars,
adaptive-acquisition and candidate-level saturation logs, fresh adversarial QA, and
a frozen final report. The eligible rendering is roughly thirty-five thousand words.

The owner saturation audit is represented directly in the release. Fourteen named
depth gaps received targeted source-grounded developments, and arithmetic geometry,
stochastic processes, partial differential equations, and numerical analysis each
received three distinct mechanisms. The post-expansion stop log names the next
candidate in every ecosystem and explains which included mechanism it would repeat;
unit counts alone never trigger saturation.

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
  --riemann-artifact-root /workspace/mathia-artifacts/riemann-corpus-v0 \
  validate --require-artifacts
```

`acquire` downloads only the declared public or author-hosted URLs, records exact
hashes and effective URLs, and stores all source artifacts outside Git. It does not
bypass access controls. `build` deterministically rematerializes the release from
the curated catalogs, acquisition snapshot, sidecars, and recorded QA. The
`review_content_freeze.json` binds the exact candidate seen by fresh QA while
excluding QA rows, the final report, and the final freeze to avoid a self-reference;
every QA row and the final freeze must reference that manifest. The freeze also
binds the complete issue `#42` Riemann release used in the compatibility dry run.

## Artifact and licensing boundary

Git contains short independently written mathematical restatements, exact source
locators, hashes, attribution and license boundaries, conceptual derivatives,
audits, and small original SVG schematics. Full source artifacts remain in the
external artifact root. Open sources retain their GFDL or Creative Commons terms.
For copyrighted but author-hosted references, only metadata, locators, and original
mathematical restatements are committed.

The records conform to the canonical `mathia-interchange-v1` contract and use the
origin-blind renderer in [`../mathia_corpus`](../mathia_corpus/). The synthetic mixed
manifest is generated from the actual full issue `#42` Riemann release and this full
issue `#44` release. It is only a compatibility and deduplication dry run; its equal
exhaustive passes over eligible records choose no future training ratio.
