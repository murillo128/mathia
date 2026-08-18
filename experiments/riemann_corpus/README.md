# Riemann corpus pilot (`#42`)

This experiment-local pipeline builds and audits a broad Riemann-hypothesis source ledger, stores lawfully accessible artifacts outside Git, and freezes a 12-source/24-unit Codex interpretation pilot. It is not a general dataset framework and does not run model training or proof search.

## Reproduce the metadata checks

From the repository root:

```bash
python3 -m experiments.riemann_corpus validate
python3 -m experiments.riemann_corpus validate-pilot
python3 -m unittest tests.test_riemann_corpus -v
```

To verify local source and unit hashes too:

```bash
python3 -m experiments.riemann_corpus validate --require-artifacts
python3 -m experiments.riemann_corpus validate-pilot --require-artifacts
```

The default external artifact root is `/workspace/mathia-artifacts/riemann-corpus-v0`; pass `--artifact-root PATH` before the subcommand to use another location.

## Pipeline commands

`discover`, `expand-citations`, and `continue-citations` perform the recorded OpenAlex discovery routes. `acquire` attempts only public URLs and never bypasses access controls. `audit-ledger` applies explicit relevance/metadata corrections. `report` regenerates corpus counts. `freeze-pilot` freezes exactly the selection in `pilot_selection.json`. `segment-units` extracts only the 24 declared spans to the external store.

Discovery and acquisition touch network resources and will produce new timestamps or access outcomes; they are not required for metadata validation. Do not rerun the freeze after analyses have begun without deliberately starting a new pilot version.

## Artifact boundary

Git contains provenance, hashes, source boundaries, prompts, teacher outputs, audit, and concise reports. Raw and normalized full texts remain external because freely readable material is not necessarily redistributable. The repository never treats a failed download, partial preview, or computational verification as a proof of RH.
