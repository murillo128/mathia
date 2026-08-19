# Riemann → Mathia corpus (`#42`)

This experiment-local pipeline builds and audits a broad Riemann-hypothesis
source ledger, stores lawfully accessible source text outside Git, preserves the
12-source pilot and its repair/behavioral evidence unchanged, and packages the
usable acquired corpus as linked source, Mathia-interpretation, and synthesis
objects. It is not a general dataset framework and does not run model training,
GPU work, or proof search.

## Reproduce the metadata checks

From the repository root:

```bash
python3 -m experiments.riemann_corpus validate
python3 -m experiments.riemann_corpus validate-pilot
python3 -m experiments.riemann_corpus validate-continuation
python3 -m experiments.riemann_corpus.full_corpus validate-release
python3 -m unittest tests.test_riemann_corpus -v
python3 -m unittest tests.test_riemann_full_corpus -v
```

To verify local source and unit hashes too:

```bash
python3 -m experiments.riemann_corpus validate --require-artifacts
python3 -m experiments.riemann_corpus validate-pilot --require-artifacts
python3 -m experiments.riemann_corpus validate-continuation --require-artifacts
python3 -m experiments.riemann_corpus.full_corpus validate-units --require-artifacts
python3 -m experiments.riemann_corpus.full_corpus validate-objects --require-artifacts
```

The default external artifact root is `/workspace/mathia-artifacts/riemann-corpus-v0`; pass `--artifact-root PATH` before the subcommand to use another location.

## Pipeline commands

`discover`, `expand-citations`, and `continue-citations` perform the recorded OpenAlex discovery routes. `acquire` attempts only public URLs and never bypasses access controls. `audit-ledger` applies explicit relevance/metadata corrections. `report` regenerates corpus counts. `freeze-pilot` freezes exactly the selection in `pilot_selection.json`. `segment-units` extracts only the 24 declared spans to the external store.

`segment-continuation-units`, `snapshot-continuation-v0`, `freeze-continuation`, and `continuation-manifest` build the versioned Checkpoint H–M evidence under `pilot_12_v1` without modifying the original pilot. Discovery and acquisition touch network resources and will produce new timestamps or access outcomes; they are not required for metadata validation. Do not rerun either freeze after analyses have begun without deliberately starting a new pilot version.

`experiments.riemann_corpus.full_corpus` owns Checkpoints N–S. The first
segmentation pass guarantees one coherent coverage span per usable non-pilot
source; the separate non-quota expansion then permits zero to four further
units according to mathematical richness and extraction quality. This two-step
lineage preserves the initial coverage evidence without imposing equal final
unit counts. Four raw interpretation passes, two synthesis tracks, stratified
independent audit, shared-interchange packaging, freeze, report, and release
manifest remain inspectable under `full_corpus_v1/`.

The final trainable manifest includes accepted source units, interpretations,
and syntheses only. Quarantined/rejected interpretations, raw teacher passes,
critics, behavioral tasks, and audit records remain provenance or evaluation
evidence and cannot enter the positive manifest accidentally.

## Artifact boundary

Git contains provenance, hashes, source boundaries, prompts, teacher outputs, audit, and concise reports. Raw and normalized full texts remain external because freely readable material is not necessarily redistributable. The repository never treats a failed download, partial preview, or computational verification as a proof of RH.
