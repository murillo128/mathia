# Intuition-fertility pre-test v0 — non-independent self-audit

## Status

**Verdict: REVISE before independent review.**

This is an internal design audit performed in the same research context that produced the proposal. It is intentionally **not** the fresh-context independent review required to close #30. Its purpose is to remove obvious defects before spending an independent review on them.

## Material findings

### F1 — rank-nullity input leaked the intended quotient representation — FIXED

The first draft of the Mathia-visible rank-nullity statement said that the ambient ranks satisfy the "usual quotient-rank behavior". That already points the generator toward the quotient viewpoint which the task is supposed to elicit.

The panel statement was changed to mention only that the relevant rank hypotheses are available. The quotient/kernel/range interpretation remains private in the audit reference.

### F2 — factual control alone does not isolate generic strategy priming — MUST FIX

`factual_control` controls theorem-specific vocabulary and extra text, but it does not test whether **any** mathematical-strategy rhetoric helps qwen-lean. A model may respond to a generic comment such as "look for an invariant, decomposition, or equivalent representation" without the hint containing theorem-specific intuition.

Add a required `generic_strategy_control`: a bounded, strategy-shaped but theorem-independent hint rendered through the exact same comment interface. Its purpose is to estimate uplift from generic mathematical deliberation/priming rather than from a theorem-specific mechanism.

The primary reference comparison should therefore inspect relevant intuition against both `factual_control` and `generic_strategy_control`, not only the unguided baseline.

### F3 — several named targets are deliberately easy wrappers — ACCEPT AS CALIBRATION, NOT PRIMARY EVIDENCE

`Subgroup.card_subgroup_dvd_card`, `LinearMap.rank_range_add_rank_ker`, and `MulAction.card_orbit_mul_card_stabilizer_eq_card_group` live in theorem neighborhoods containing the structural machinery that makes them short to formalize. They may be near ceiling for a competent qwen-lean checkpoint.

They remain useful as channel/floor calibration: if a compact relevant hint cannot affect even a tractable target, the interface may be ineffective. They must not carry the main claim that intuition helps hard proof generation.

The hard items (`Function.Embedding.schroeder_bernstein_of_rel` and `HallMarriageTheorem.hall_hard_inductive`) should carry more weight when interpreting non-ceiling behavior. The compact-image item adds domain diversity but may also be easy.

### F4 — exact qwen-lean target exposure is unresolved — BLOCKING

The Phase-2 manifest proves that qwen-lean assigns whole file/components to `train`, `validation`, and `heldout`, and that current SFT fitting uses train records. The repository does not publish the full record-level split artifact, so the split of the six proposed targets cannot be resolved from Mathia's GitHub context alone.

This is a real pre-freeze blocker, not a reason to weaken the rule. Before the independent audit, query the actual Phase-2 artifact used by qwen-lean. Any `train` target must be replaced under #30.

The lookup is CPU-only and does not require the shared GPU.

### F5 — current qwen-lean does whole-proof sampling, not interactive proof search — FIXED

Earlier planning language described the reward as "proof-search fertility" and proposed intermediate-lemma/search-cost signals. The inspected qwen-lean implementation currently renders a complete-proof continuation request and verifies generated Lean continuations.

The v0 hard signal has been corrected to **verified whole-proof generation fertility**. Primary metrics are verified candidate yield and pass@k under matched sampling. Candidate rank/tokens to first verified proof are secondary cost proxies, not tactic-search complexity.

### F6 — theorem documentation and formal target must remain separate — FIXED/ONGOING

The user explicitly wants documented theorems, not proof strings alone. `INTUITION_FERTILITY_SOURCES_V0.md` now records human-readable course/text references for each candidate.

These sources must remain private from primary intuition generation. They may be used after outputs/results are frozen to interpret whether a strategy resembles a documented mechanism. Future use as training data requires separate licensing review.

### F7 — Schröder-Bernstein documentation is not identical to the formal target — ACCEPT WITH EXPLICIT FAITHFULNESS CHECK

The private target `Function.Embedding.schroeder_bernstein_of_rel` strengthens the familiar two-injections theorem with a relation `R` that the resulting bijection must respect. Standard expositions mostly document the ordinary theorem.

The Mathia-visible statement includes the relation obligations explicitly. The stable-partition/piecewise-map intuition plausibly extends because each branch inherits one of the assumed `R` relations, but the independent reviewer must check this is a faithful conceptual bridge rather than importing an intuition for a different theorem.

### F8 — cross-theorem control can be genuinely useful — ACCEPT, DO NOT FORCE NULL EFFECT

The strongest cross-theorem pairs intentionally share mechanisms: Lagrange/orbit-stabilizer, rank-nullity/compact-image transport, Schröder-Bernstein/Hall. Some cross hints may improve a target through legitimate transfer.

That is not a defect. The control tests relevance/specificity and may itself reveal transfer. The experiment must not define success as `cross_theorem_strategy = zero uplift`. Strong evidence instead requires that appropriate strategies produce a selective pattern not reproduced uniformly by unrelated/generic guidance.

### F9 — `select` and `generalize` are underrepresented in the theorem panel — ACCEPT FOR THIS PRE-TEST

The theorem panel is a channel calibration, not a benchmark intended to score every conceptual dimension. `select` is most visible in the compactness item; `generalize/weaken` is only weakly represented in the Hall item.

Do not add weak theorem items merely to make a coverage table look balanced. Later concept/dimension training design can build dedicated tasks once #32 shows that the intuition-fertility channel is useful.

### F10 — natural-language comment is out of the qwen-lean SFT prompt distribution — CONTROLLED BUT STILL A LIMITATION

The proposed intervention inserts the strategy as a Lean comment before the exact declaration. Current qwen-lean SFT prompts contain the proof request and declaration without such a strategic comment.

This distribution shift could itself help or hurt. `factual_control` and the new `generic_strategy_control`, rendered through the same comment format and comparable lengths, are necessary to separate comment/OOD effects from strategy specificity. The result remains conditional on this interface until transfer is tested.

### F11 — whole-proof yield can be noisy at low candidate count — #32 FREEZE CONCERN

The small Phase-4 heldout contract currently uses few candidates per theorem. Per-intuition fertility will be too noisy if #32 blindly reuses that count.

Do not freeze a count in #30, but require #32 to choose a candidate budget large enough to estimate theorem/condition yield on this very small panel, subject to available compute. The exact budget must be frozen before comparative results.

### F12 — direct proof/theorem-name memorization by the intuition generator remains possible — ACCEPTED CALIBRATION LIMITATION

Hiding the theorem name and using notation variants reduces trivial retrieval cues but cannot remove Qwen base pretraining exposure. This is acceptable because #32 asks whether useful strategic ability already exists and whether there is headroom, not whether Qwen rediscovered a novel theorem.

A later post-training evaluation will need less canonical or protected tasks to support claims of generalization.

## Required fixes before independent review

- add `generic_strategy_control` to the scientific contract and issue #30;
- resolve all six proposed targets against the actual qwen-lean Phase-2 split/checkpoint lineage;
- replace any train-exposed target deliberately;
- after replacement, verify documentation, Mathia-visible statement, factual control, cross pairing, and leakage reference for the exact retained panel;
- then run the fresh-context independent adversarial review.

## Non-blocking questions to preserve

- whether `select` should later be supervised as a conceptual move or mainly learned through downstream fertility;
- whether concepts and dimensions should be trained in strictly sequential stages or interleaved while preserving separate evaluation;
- whether whole-proof yield remains a useful reward once qwen-lean gains interactive proof-state search;
- whether solver-specific fertility transfers to another formal worker or qwen-lean checkpoint.
