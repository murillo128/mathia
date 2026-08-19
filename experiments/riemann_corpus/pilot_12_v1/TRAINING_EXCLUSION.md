# Evaluation-only exclusion

The exact accepted prompts, answer keys, source-grounded justifications, perturbations, and transfer cases in this directory are frozen evaluation material. They are not eligible for any later learner training corpus, prompt-tuning corpus, preference data, retrieval context, or teacher-demonstration export.

The candidate files intentionally preserve rejected cases as audit evidence. `selection.json` and `freeze.json` identify the accepted evaluation subset. A future experiment may expose an accepted task's `model_visible_prompt` to a learner only at evaluation time after the relevant learner checkpoint and training data have been frozen.

Audit metadata such as source/unit provenance and the probed mechanism is scorer-side information. Expected answers and justifications are never model-visible during evaluation. Scoring uses the discrete core answer; prose similarity to Codex is not a target.

If an accepted prompt or answer is placed in learner-visible training material, that task is contaminated and must not be reported as held out. A replacement requires a new version and freeze; this v1 record must remain intact.

This exclusion does not authorize training, inference, GPU use, or changes to issue #32.
