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
checks for unmistakable Lean/formal implementation leakage, followed by two
fresh independent blinded semantic classifiers that each see only public
theorem context and the candidate. Acceptance requires unanimous semantic
acceptance. Tool use is provenance, not an eligibility failure. No rejected
output is rewritten or sanitized.

Calibration revisions 0 and 1 are preserved as immutable
`CALIBRATION_REVISE` evidence. Revision 0 admitted several compact but complete
derivations and treated an interim-message/web/final-message trace as a failure.
Revision 1 corrected extraction but still admitted three cosmetically shortened
complete routes. Revision 2 corrected that boundary but was
`CALIBRATION_BLOCKED` at 18/24 because composite-theorem generations still
sketched every clause. Those 28 + 31 + 34 attempts are not eligible for the
final corpus. Revision 3 passed calibration and completed all 650 tasks, but its
exact-target final audit returned `REVISE`: a broad tactic-word hard check
falsely rejected ordinary prose, and the single semantic classifier admitted
several near-complete elementary routes. Its 738 attempts and derived release
artifacts remain immutable, evaluation-only evidence and are not eligible for
the final corpus. The active `calibration-r4` contract restarts generation in a
disjoint capture tree, limits hard checks to unmistakable syntax, and requires
unanimous independent semantic review with an explicit substantive-bridge
check.

The exact active generator instruction, reviewer instruction, 8+16 evenly spaced
calibration membership, candidate caps (128/160/192 Qwen tokens), maximum-two
retry policy, and online circuit breakers were frozen before calibration. The
24-task r4 calibration received a fresh `CALIBRATION_PASS` at 22/24 and selected
the 128-token cap. The authorized full run then completed all remaining 626
tasks without a circuit breaker or runtime miss. The frozen candidate release
contains 611 accepted intuitions and 39 explicit missing-intuition records from
746 attempts. A fresh independent final audit returned `PASS` on exact target
`584cc5319ecb1f1862b88bd81adbe69d1cd30000`; the bound verdict is preserved in
`final_revision_1_review.json`. This technical pass makes the pull request ready
for human review but is not merge authorization.

## Reproduction and validation

Use the environment containing the pinned Qwen tokenizer:

```text
PYTHONPATH=. /workspace/.venvs/qwen45/bin/python -m experiments.frontier_assisted_intuition_corpus_v1 materialize-sources
PYTHONPATH=. /workspace/.venvs/qwen45/bin/python -m experiments.frontier_assisted_intuition_corpus_v1 prepare-calibration-revision
PYTHONPATH=. /workspace/.venvs/qwen45/bin/python -m experiments.frontier_assisted_intuition_corpus_v1 validate-sources
PYTHONPATH=. /workspace/.venvs/qwen45/bin/python -m experiments.frontier_assisted_intuition_corpus_v1 freeze-contract
PYTHONPATH=. /workspace/.venvs/qwen45/bin/python -m experiments.frontier_assisted_intuition_corpus_v1 generate-calibration --workers 4
PYTHONPATH=. /workspace/.venvs/qwen45/bin/python -m experiments.frontier_assisted_intuition_corpus_v1 finalize-calibration
# Publish and obtain the required fresh CALIBRATION_PASS review, then record calibration_review_calibration_r4.json.
PYTHONPATH=. /workspace/.venvs/qwen45/bin/python -m experiments.frontier_assisted_intuition_corpus_v1 generate-full --workers 4
PYTHONPATH=. /workspace/.venvs/qwen45/bin/python -m experiments.frontier_assisted_intuition_corpus_v1 finalize
PYTHONPATH=. /workspace/.venvs/qwen45/bin/python -m experiments.frontier_assisted_intuition_corpus_v1 validate-finalized
```

The release makes no qwen-lean, Lean-proof, Mathia, planner, or downstream
fertility claim. A ready decision authorizes only a separate preregistered
fertility experiment.
