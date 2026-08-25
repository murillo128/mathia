# Frontier-assisted intuition corpus v1

This directory is the bounded, evaluation-only artifact for
[`murillo128/mathia#59`](https://github.com/murillo128/mathia/issues/59).
It creates compact GPT-5.6 Sol / xhigh mathematical intuitions for the exact
244 + 406 qwen-lean Dataset-v2 validation population. Tools and public web
retrieval are allowed for mathematical understanding and are retained as raw
provenance. Privileged benchmark proofs, solver outputs, verifier feedback,
capability labels, and final-test tasks are not generator inputs.

Every record is `evaluation_only: true`, `training_eligible: false`, and
`artifact_role: frontier_assisted_reference`. This directory is never a
Mathia or qwen-lean training source.

The protocol has two distinct output-boundary layers: narrow deterministic
checks for unmistakable Lean/formal implementation leakage, followed by a
fresh blinded semantic classifier that sees only public theorem context and
the candidate. Tool use is provenance, not an eligibility failure. No rejected
output is rewritten or sanitized.

Calibration revisions 0 and 1 are preserved as immutable
`CALIBRATION_REVISE` evidence. Revision 0 admitted several compact but complete
derivations and treated an interim-message/web/final-message trace as a failure.
Revision 1 corrected extraction but still admitted three cosmetically shortened
complete routes. Revision 2 corrected that boundary but was
`CALIBRATION_BLOCKED` at 18/24 because composite-theorem generations still
sketched every clause. Those 28 + 31 + 34 attempts are not eligible for the
final corpus. The active `calibration-r3` contract keeps the r2 reviewer
unchanged while requiring one organizing lens for composite statements.

The exact active generator instruction, reviewer instruction, 8+16 evenly spaced
calibration membership, candidate caps (128/160/192 Qwen tokens), maximum-two
retry policy, and online circuit breakers are frozen before calibration. The
full run cannot start until the 24-task evidence is published and a fresh
read-only review records `CALIBRATION_PASS` in
`calibration_review_calibration_r3.json`.

## Reproduction and validation

Use the environment containing the pinned Qwen tokenizer:

```text
PYTHONPATH=. /workspace/.venvs/qwen45/bin/python -m experiments.frontier_assisted_intuition_corpus_v1 materialize-sources
PYTHONPATH=. /workspace/.venvs/qwen45/bin/python -m experiments.frontier_assisted_intuition_corpus_v1 prepare-calibration-revision
PYTHONPATH=. /workspace/.venvs/qwen45/bin/python -m experiments.frontier_assisted_intuition_corpus_v1 validate-sources
PYTHONPATH=. /workspace/.venvs/qwen45/bin/python -m experiments.frontier_assisted_intuition_corpus_v1 freeze-contract
PYTHONPATH=. /workspace/.venvs/qwen45/bin/python -m experiments.frontier_assisted_intuition_corpus_v1 generate-calibration --workers 4
PYTHONPATH=. /workspace/.venvs/qwen45/bin/python -m experiments.frontier_assisted_intuition_corpus_v1 finalize-calibration
# Publish and obtain the required fresh CALIBRATION_PASS review, then record calibration_review_calibration_r3.json.
PYTHONPATH=. /workspace/.venvs/qwen45/bin/python -m experiments.frontier_assisted_intuition_corpus_v1 generate-full --workers 4
PYTHONPATH=. /workspace/.venvs/qwen45/bin/python -m experiments.frontier_assisted_intuition_corpus_v1 finalize
PYTHONPATH=. /workspace/.venvs/qwen45/bin/python -m experiments.frontier_assisted_intuition_corpus_v1 validate-finalized
```

The release makes no qwen-lean, Lean-proof, Mathia, planner, or downstream
fertility claim. A ready decision authorizes only a separate preregistered
fertility experiment.
