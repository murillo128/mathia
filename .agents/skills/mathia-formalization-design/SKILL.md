---
name: mathia-formalization-design
description: Design a self-contained Mathia Lean formalization issue for autonomous Codex execution with adversarial Gate review, independent technical approval, post-approval fertility review, and direct-main publication.
---

# Mathia Lean Formalization Design

## Responsibility

Use this skill when Mathia wants to test, sharpen, falsify, retain, or structurally interrogate a mathematical claim as a checked Lean theorem.

This skill may also be invoked automatically by `mathia-research-watch` when a canonical finding has a stable, high-value, reusable Lean theorem core. In that case, issue creation is the handoff itself: do not stop at identifying the candidate and do not require separate user confirmation before creating the issue.

This is a thin specialization of:

```text
.agents/skills/design-github-issue/SKILL.md
```

Load that skill as the generic issue-design authority. The controlling Mathia issue owns the exact scientific question and theorem boundary. `mathia-formalization-executor` owns the reusable execution and subagent-orchestration procedure.

A formalization issue is a control-plane object, not a request to create a PR for later human review.

## Two legitimate formalization motives

Mathia formalization has two legitimate motives that may coexist:

```text
verification
fertility
```

**Verification** asks whether an important persisted theorem is stated correctly and can be kernel-checked with the intended hypotheses and conventions.

**Fertility** uses formalization as a structural observation surface. The target theorem may already be classical or prior art; the value is that forcing an exact formal proof can expose which hypotheses are truly consumed, which intermediate object carries the proof, whether an apparently symmetric argument is actually one-sided, or whether a hidden factorization, kernel/range description, normal form, quotient, invariant, alternate representation, or richer formal subproduct is doing the real work.

Prior-art status is therefore **not a disqualifier** for Lean. Novelty of the target theorem is neither required nor implied. A prior-art target is worth formalizing for fertility only when formalization is likely to create useful conceptual pressure rather than merely translate known prose.

Good fertility candidates include theorem surfaces where:

- the theorem sits on a structural boundary such as exact rank, equality, sharpness, kernel, image, dimension, injectivity/surjectivity, extremality, or classification;
- the informal argument admits multiple materially different representations or proof explanations;
- persisted hypotheses look stronger, more symmetric, or less canonical than the underlying mechanism may require;
- the proof is expected to pass through a reusable factorization, normal form, quotient, invariant, exact finite certificate, orbit space, kernel/range object, or other structure the finding does not foreground;
- several findings reuse the same bridge and an exact formal interface could reveal its minimal theorem boundary;
- an exceptional/counterexample regime is understood computationally or informally but its exact structural cause remains opaque.

Poor fertility candidates include routine identities whose expected formalization is only library lookup or syntactic translation, bulk prior-art transcription, theorem collections with no live structural question, and targets whose only benefit is documentation.

A fertility target must satisfy the same statement fidelity and proof-integrity standards as a verification target. It does **not** authorize the executor to invent a stronger theorem, broaden the issue during proof search, or treat an exposed pattern as evidence before the clue/research workflow validates it.

When useful, state the motive concisely as `verification`, `fertility`, or `verification + fertility`. Any target-specific fertility question written into the issue is a **minimum probe, not an exhaustive discovery checklist** for the later independent fertility reviewer.

## Issue type label

Every controlling issue created by this skill must carry the repository label `formalization` in addition to exactly one workflow-state label. Apply `formalization` at issue creation whenever the GitHub transport supports it; otherwise apply it immediately after creation before considering the handoff complete. The type label is orthogonal to workflow state and must be preserved across state transitions.

A newly created issue that is ready for autonomous execution should therefore normally carry both `formalization` and `execution-ready`. If it is created in another valid workflow state, keep `formalization` and use that single state label instead.

## Automatic research handoff and deduplication

Before creating an issue from Research Watch:

1. identify the exact canonical finding path and stable finding ID that motivate the formalization;
2. isolate the smallest theorem surface that is mathematically useful and faithful to the persisted finding;
3. decide whether the material value is verification, fertility, or both; for fertility, identify the structural pressure expected from formalization without predicting a discovery;
4. search existing open and closed Mathia issues for that finding ID, equivalent theorem surface, and distinctive target terminology;
5. inspect existing Mathia Lean source when relevant to determine whether the target is already formalized or already has a controlling issue;
6. if an equivalent issue or completed formalization exists, return that control object rather than creating a duplicate;
7. otherwise create the controlling Mathia issue immediately through `design-github-issue`.

Do not create or maintain `LEAN_CANDIDATES.md`, TODO files, or another formalization queue. A candidate ready for execution is represented by its GitHub issue; a candidate not ready remains ordinary research evidence.

Issue creation does not validate the mathematical claim. Gate 0 remains blocking.

## Autonomous execution contract

Every issue designed by this skill must be executable by a fresh Codex context using:

```text
.agents/skills/mathia-formalization-executor/SKILL.md
```

The normal formalization lifecycle is:

```text
approved issue
    -> fresh adversarial Gate-0 subagent
    -> Lean proof engineering
    -> Lean validation
    -> fresh final codex-independent-review subagent
    -> technical PASS / PASS_WITH_NOTES
    -> fresh post-approval formalization-fertility subagent
    -> direct commit to main
    -> close issue
```

The two final subagents have deliberately different jobs:

- `codex-independent-review` certifies the exact theorem/finding correspondence, proof integrity, ordinary-mathematics proof reconstruction, and unformalized boundary. It is read-only and does **not** create clues.
- `mathia-formalization-fertility-review` runs only after technical approval and independently searches the accepted Lean artifact for mathematical deltas, unused formal structure, richer intermediate objects, and clue-worthy subproducts.

Do not collapse these roles into one review. Technical approval must not depend on creativity, and clue search should inspect a frozen already-certified artifact without inheriting the technical reviewer's reasoning.

There is deliberately:

- no implementation PR;
- no user review/merge checkpoint after successful autonomous review;
- no committed Gate-0 report;
- no committed technical-review report;
- no committed fertility-review report;
- no durable feature branch required by the workflow.

A local branch/worktree may be used as scratch execution state, but it is not a publication artifact.

Generic PR/delivery boilerplate in an older issue does not override the current formalization procedure merely because the issue predates this skill revision. An issue may override the procedure only when it explicitly records a later target-specific reason rather than copied workflow text.

## Lean environment

Use the Lean tooling available on the execution machine together with Mathia's current local Lean/Lake setup.

Do **not** make a predetermined Lean or mathlib version part of the scientific contract. Record the actual environment only when useful for reproducibility or diagnosis.

If Mathia does not yet contain the Lean support required by a bounded formalization, the issue may authorize the **smallest Mathia-local Lean/Lake wiring** needed for that target. Do not turn this into a general formalization framework.

## Formalization Gate 0

Every nontrivial formalization issue must begin with a blocking **statement / adversarial / prior-art / mathlib-reuse gate** before proof implementation.

Gate 0 must independently reconstruct and attack the intended theorem surface, including as relevant:

- exact quantifiers and hypotheses;
- domains, side conditions, singularities, and definedness;
- normalization, sign, indexing, orientation, gauge, and convention choices;
- boundary and degenerate cases;
- fidelity between the canonical finding and the Lean target;
- whether the proposed target is weaker, stronger, or equivalent to the persisted claim;
- exact or stronger prior formalizations;
- reusable mathlib or existing Mathia Lean declarations;
- dependency/import choices.

For a fertility-motivated issue, Gate 0 must additionally distinguish **mathematical prior art** from **already-formalized/reuse-only**. A theorem being classical does not kill the issue; an existing formal theorem that already exposes the same exact structural interface normally does. If prior art is known, preserve that provenance and make no novelty claim.

Allowed outcomes are:

```text
safe progression
reuse-only / already formalized / no material delta
statement repair required
mathematical conflict / counterevidence
```

The review must be performed in a fresh subagent context that does not inherit the executor's hidden reasoning.

### Gate 0 is process evidence, not a repository artifact

Do not request or persist a companion Gate Markdown file. The executor records the frozen target and concise Gate verdict in the controlling issue when durable transport is useful; detailed scratch analysis remains ephemeral.

A negative Gate outcome is a successful scientific result when it prevents formalizing the wrong theorem.

## Lean-source provenance contract

Every principal new formalization module must contain a module-level Lean comment near the top stating, in ordinary mathematical language:

1. **the exact associated canonical finding path**;
2. **the theorem/result actually proved in this file**;
3. important surrounding claims explicitly **not** proved when that boundary could otherwise be misunderstood.

A natural shape is:

```lean
/-!
# <human theorem name>

Associated finding:
`research/<line>/findings/<finding>.md`

Formalized theorem boundary:
<concise ordinary-mathematics statement of what Lean proves>.

Not formalized:
<important surrounding claims, if any>.
-/
```

The exact prose may differ, but the finding link and mathematical theorem boundary are mandatory. Do not replace this with only an issue number, finding ID, or Gate-file reference.

## Formal success boundary

The issue must state enough target-specific mathematics to distinguish:

- fidelity of the Lean statement to the intended claim;
- formal proof success;
- validity of wider Mathia findings or research programs;
- novelty/prior-art status;
- surrounding analytic, geometric, asymptotic, computational, or representation bridges that remain outside Lean.

A compiling theorem never silently certifies unformalized prose.

For fertility-motivated formalization, success does **not** require a new clue or conceptual delta. A clean `NO_MATERIAL_FERTILITY_DELTA` after the **separate post-approval fertility review** is a valid result. The experiment is to apply conceptual pressure, not to manufacture novelty.

## Autonomous research return

Formalization is also an observation surface. Keep correctness challenges and separate research leads distinct.

### Challenge to the source finding

If Gate 0, Lean execution, final technical review, or post-approval fertility review exposes a material observation that could make the associated finding false, overstrong, under-specified, or unsafe, the executor invokes a fresh adversarial research subagent using:

```text
.agents/skills/mathia-research-adversarial/SKILL.md
.agents/skills/mathia-research-review/SKILL.md
```

That subagent owns any `.review.md` mutation under the normal review protocol. The formalization must not silently repair or weaken the theorem around the defect.

### Distinct research lead

Only **after technical approval**, the executor launches a fresh subagent using:

```text
.agents/skills/mathia-formalization-fertility-review/SKILL.md
.agents/skills/mathia-research-clues/SKILL.md
```

That subagent deliberately searches for semantic deltas and mathematical subproducts the canonical finding does not retain as first-class structure.

It must go beyond theorem-statement comparison. In particular it inspects formal intermediate objects such as quotients, subgroups, orbit spaces, kernels, ranges, normal forms, equivalences, decompositions, factorizations, order structures, and auxiliary invariants, asking what structure they possess, what part the final theorem consumes, and what information is discarded by reducing them to a cardinality, dimension, rank, scalar, or other endpoint.

If that unused structure yields a genuinely different falsifiable direction, the fertility reviewer may create or materially strengthen only a `status: proposed` clue through `mathia-research-clues`. Research Watch still owns later clue acceptance, rejection, resolution, and substantive findings.

A shorter tactic script, convenient library lemma, import simplification, or formal object with no concrete unresolved consequence is not clue-worthy.

The fertility reviewer may inspect a **bounded immediate mathematical neighborhood** of the formalized finding when necessary to turn a formal subproduct into a decisive question. It must not turn the stage into an open-ended Research Watch over the whole line.

## Lean proof-integrity contract

Unless the issue explicitly establishes a different proof boundary, successful formalization requires:

- the repository-native Lean build/check succeeds;
- no `sorry` or `admit` in accepted theorem dependencies;
- no new axioms introduced to discharge the target;
- no `unsafe` proof shortcuts;
- no floating-point/sample evidence used as proof premises;
- no unchecked generated/CAS certificates;
- `#print axioms` or equivalent trust-footprint inspection on principal theorems;
- theorem statements remain faithful to the Gate-0 accepted boundary;
- a fresh final `codex-independent-review` subagent reconstructs the theorem and proof as ordinary mathematics and checks correspondence with the associated finding;
- after technical `PASS`/`PASS_WITH_NOTES`, a separate fresh formalization-fertility subagent completes its audit before publication.

## Issue shape

Compose with `design-github-issue`; do not duplicate generic GitHub workflow text.

A Mathia Lean formalization issue should normally contain only the target-specific contract:

1. research provenance: exact finding path(s) and why the theorem matters;
2. intended formal theorem boundary;
3. formalization motive (`verification`, `fertility`, or both) when useful, including structural pressure without assuming a positive fertility outcome;
4. Gate-0 risks specific to this target;
5. any target-specific Lean setup/import constraints;
6. proof-integrity constraints beyond the defaults above, if any;
7. surrounding claims explicitly out of scope;
8. target-specific validation or review conditions beyond the executor defaults, if any.

Do not duplicate the generic post-approval fertility procedure inside each issue. If the issue names expected fertility questions, treat them as prompts for the final fertility subagent rather than a complete list of what it is allowed to notice.

End the issue with a compact execution pointer such as:

```text
Execute autonomously with `.agents/skills/mathia-formalization-executor/SKILL.md`.
No PR and no separate review artifacts. Publish only after the skill's fresh Gate-0, final technical-review, and post-approval fertility-review subagents complete successfully.
```

Do not prescribe a PR, merge step, Gate Markdown file, or manual review handoff unless the mathematical task has a specific exceptional reason for one.