# Later evaluation hypotheses (no training in issue #42)

This note records discriminating hypotheses for a separate issue. It neither authorizes training nor changes the protected `#32` gate.

## A. Riemann-domain internalization

The Riemann corpus is intentionally training-visible in the eventual hypothesis; RH is not a clean held-out benchmark. A future evaluation should ask whether a checkpoint can recover concrete domain content and relationships, including:

- which statement is a theorem, conditional result, equivalent criterion, heuristic, finite computation, open global step, or failed sufficient condition;
- how the Euler product, explicit formula, prime-counting errors, zero statistics, mollifiers, closure criteria, heat flow, and finite verification relate without collapsing them;
- what each selected representation gains and what mathematical work remains;
- source/version/provenance attribution and known extraction uncertainty.

Useful tests would reserve source passages and relationship questions before training, include plausible but false cross-source joins, and compare a frozen base model, the trained condition, and a style-matched control. Memorized domain facts count positively on this axis, but unsupported completion of RH or confusion of numerical verification with proof counts negatively.

## B. Mathia capability transfer

The stronger claim concerns mathematical material outside the Riemann corpus. Before any training, freeze a panel whose concepts are structurally related but whose objects, notation, and exposition differ. Ask for behavior, not conceptual labels:

- select between two representations and predict which downstream question each makes tractable;
- decompose a method into main mechanism, error/bottleneck, and imported dependency;
- transfer an analogy and identify a concrete observation that would reject it;
- change an essential assumption and predict which conclusion or proof step fails;
- repair a failed approximation or sufficient condition without merely restating the failure;
- propose a compact candidate intuition and commit it before a hidden structural intervention.

Perturb notation, ordering, terminology, and rhetorical style. Include shuffled teacher prose, generic 'deep explanation' prose, and category-name-only outputs as controls. Whenever possible, score the downstream prediction, choice, or falsifier independently of prose quality. Teacher preference and phrase similarity must remain secondary diagnostics.

## Discriminating outcomes

- Riemann retention without out-of-domain improvement supports domain distillation, not reusable Mathia capability.
- Style-matched improvement that disappears under notation or presentation perturbation supports the teacher-style confound.
- Better source-status calibration without better hidden-intervention performance is useful but narrower than intuition formation.
- Improvement on frozen out-of-domain interventions, especially when the response uses different language from the teacher, is evidence for transfer but still requires replication across domains and evaluators.
- No benefit from the first extraction format should trigger method diagnosis before increasing model size or compute.
