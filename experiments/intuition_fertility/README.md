# Intuition-fertility harness

This package implements the deterministic CPU-side mechanics accepted in issue
#31. It does not run an intuition generator, qwen-lean, Lean, GPU inference,
training, or an AI quality judge.

The contract is split into three channels:

- `generator_payload(...)` exposes only the selected name-free theorem statement
  and the common intuition request;
- fixed factual/generic controls enter only through formal-worker condition cells;
- canonical declarations, Phase-2 records, pinned source provenance, and audit
  notes require the explicit private panel accessor or `panel --include-private`.

Core records are immutable and content-addressed. Canonical JSON uses sorted
object keys, while bundle arrays are sorted by their content IDs, so filesystem
and JSON object order do not affect scientific identities. The interchange is
provider-neutral; generator, model, tokenizer, worker, environment, budget,
sampling, and seed identities are supplied by the later run rather than chosen
here.

## #32 integration sequence

1. Use `generator_payload` for the frozen standard or genericity presentation.
2. Capture exact output with `IntuitionSample.capture` and a qwen-lean tokenizer
   adapter. The included whitespace adapter is synthetic and test-only.
3. Import a frozen leakage-only decision with `LeakageDecision.create`. Its
   classifier payload contains exactly the visible theorem statement and raw
   guidance. Uncertain or disputed decisions become `borderline`.
4. Build relevant and fixed cells, then bind adjacent/distant donors by exact
   frozen sample ID. Missing, non-strategic, or over-budget donors remain explicit
   ineligible cells.
5. Split the existing qwen-lean baseline into `PromptTemplate(prefix,
   declaration)`. Rendering inserts one escaped block comment immediately before
   the unchanged declaration; the baseline and non-intervention bytes remain in
   the prompt artifact for inspection.
6. Supply `FormalWorkerRun` identities and import each continuation with formal
   verification evidence. Only `accepted` evidence under the same frozen formal
   environment can produce `verified_proof`.
7. Store artifacts in `ExperimentBundle`; validate and score them with the CLI.

The comment renderer preserves the raw guidance record and deterministically
escapes only `/-` and `-/` inside the rendered copy. It never truncates, pads, or
rewrites a stored sample after classification or outcomes.

## Commands

From the repository root:

```bash
python3 -m experiments.intuition_fertility panel
python3 -m experiments.intuition_fertility panel --include-private
python3 -m experiments.intuition_fertility validate path/to/bundle.json
python3 -m experiments.intuition_fertility summarize path/to/bundle.json
python3 -m unittest discover -s experiments/intuition_fertility/tests -v
python3 -m compileall -q experiments/intuition_fertility
```

The summary retains theorem-level result cells, reports adjacent guidance only as
a transfer probe, marks length-ineligible relevant/distant comparisons, reports
all leakage labels by theorem/generator, and excludes calibration G from every
primary aggregate.
