# Pilot-12 behavioral continuation (`#42`, Checkpoints H-M)

This directory continues the frozen `pilot_12` experiment without rewriting it. `v0_snapshot.json` hash-binds every v0 file. Three `_v1` unit records repair only the source spans named by Checkpoint H; their source text remains in the external artifact store.

The candidate files contain source-grounded in-Riemann probes and standard-mathematics transfer probes. Each record has a discrete base task, a cosmetic perturbation with the same answer, and a structural perturbation with a different answer. Strict failed rounds remain immutable negative evidence: round one is `candidate_behavioral_tasks_round1.json` plus `adversarial_review.jsonl`, and round two is `candidate_behavioral_tasks.json` plus `adversarial_review_round2.jsonl`. The bounded third round and its fresh review are separate final-candidate artifacts. `selection.json` chooses only accepted, objectively scored tasks, and `freeze.json` binds the resulting evaluation-only discriminator.

The exact accepted tasks and answer keys are excluded from future learner training by `TRAINING_EXCLUSION.md`. This package is experiment-local and is not a permanent dataset schema or taxonomy.

Validate metadata only:

```bash
python3 -m experiments.riemann_corpus validate-continuation
```

Also verify the three external repaired unit artifacts:

```bash
python3 -m experiments.riemann_corpus validate-continuation --require-artifacts
```
