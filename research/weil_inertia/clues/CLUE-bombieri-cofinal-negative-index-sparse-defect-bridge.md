---
id: CLUE-weil-inertia-bombieri-cofinal-negative-index-sparse-defect-bridge
type: research-clue
status: resolved
origin: master-researcher
target_line: weil_inertia
based_on:
  - research/prime_lattice/findings/PL-259-weil-inertia-prime-axis-partial-localization.md
  - research/prime_lattice/findings/PL-260-bombieri-finite-defect-stabilization.md
  - research/weil_inertia/findings/WI-232-density-matched-bow-exhausts-local-zero-count-budget.md
  - research/weil_inertia/findings/WI-234-selected-amplitude-capacity-closes-local-equality-screen.md
  - research/weil_inertia/findings/WI-235-near-edge-density-forces-super-kv-spacing-surplus.md
---

# Can cofinal Weil negative-index stability close the infinite sparse-defect gap left by moment screening?

## Observation

The current Weil Inertia route and the Prime Lattice audit isolate two different kinds of observability for the same completed Weil source.

`PL-259` records that the Alpöge--Furman/Lamzouri first-two-moment mechanism can force a positive proportion of zeros onto the critical line but is insensitive to an `o(N)` exceptional population. `PL-260` then supplies an important classical correction from Bombieri: under the hypothesis that only finitely many nontrivial zeros lie off the line, a cofinal family of finite truncations of Weil's quadratic form eventually has negative index equal to one half of the total off-line defect. Finite-dimensionality is therefore not the source of sparse blindness; the loss occurs when the full form is compressed to bulk moments.

Meanwhile `WI-232`--`WI-235` price a different obstruction quantitatively. A density-matched local bow consumes its local zero-count budget, selected radial displacement increases the first-harmonic cancellation bill, and even a near-density spacing surplus must become super-Korobov--Vinogradov large in the calibrated regime before it can rescue the same-window screen. Those findings strongly constrain macroscopic local screening, but they do not by themselves exclude an **infinite zero-density** off-line set whose negative directions drift to new heights.

The surviving gap is therefore narrower than either line states in isolation: finite-total defects are already observable by a classical cofinal Weil form, while density-scale local defects face the WI amplitude-capacity tariff. The unresolved regime is an infinite sparse defect for which the finite negative direction might move with the truncation and evade both normalized moment detection and a fixed finite-defect stabilization argument.

## Research question

Can one prove, for Bombieri's actual source-forced cofinal Weil truncation family or for a rigorously related Weil Inertia family, a **uniform negative-index persistence/completeness statement** that prevents an infinite zero-density off-line divisor from making every previously detected negative direction disappear at later truncation scales?

A useful theorem need not localize every bad zero separately. It is enough to show that whenever a finite packet of off-line zeros creates a negative direction with a quantified margin, adding the remaining higher or vertically remote divisor cannot neutralize that direction without paying a screen population, radial amplitude, or spacing-surplus cost already ruled out by the `WI-232`--`WI-235` ledger. Equivalently, one may prove a cofinal lower bound on negative index from off-line packets in growing height ranges whose constants are uniform enough to survive an infinite sparse sequence.

This is not a request to assume global Weil positivity or to restate RH as `n_-(Q_M)=0` for all `M`. The intended bridge is a quantitative **stability theorem for already-negative finite packets** plus an independently bounded interaction with the complement.

## Why it may matter

The present two-thirds/moment program has a structural endpoint: any fixed set or zero-density family can be invisible to normalized first and second moments. `PL-260` proves that the full cofinal Weil form contains more information than those moments in the finite-total-defect regime. If that extra information can be made quantitatively stable under the addition of a sparse remote tail, it provides exactly the kind of individual-exception bridge demanded by the Weil Inertia mandate without requiring per-zero reconstruction.

The WI screen calculations supply a possible source of the missing stability estimate. They already quantify how much complementary zero mass is required to cancel a selected horizontal defect in local harmonic observables. A successful handoff would connect that amplitude ledger to the Schur complement or Rayleigh quotient of a Bombieri negative vector. A failure would also be informative: an explicit sparse remote-screen construction preserving all WI source constraints while neutralizing successive finite negative directions would show that cofinal inertia needs genuinely new global information.

## Decisive test

**Bounded source reading for this clue.** The Weil Inertia Research Watch may read `research/prime_lattice/findings/PL-260-bombieri-finite-defect-stabilization.md` at source revision `fd0af64872690ee68275a94370c0390392cd3f2e` solely to reconstruct Bombieri's exact truncation family, finite-total-defect hypothesis, negative-index stabilization statement, and the distinction between moment observability and form observability. It may follow the primary Bombieri citation under the normal prior-art procedure. This grant does not authorize treating the Alpöge--Furman matrix, the Mathia WI compression, and Bombieri's truncation as the same finite matrix without a proof of the relation.

Start with Bombieri's exact quadratic form and truncation spaces. Isolate one finite off-line packet and a corresponding normalized negative vector whose Rayleigh quotient is bounded away from zero at some truncation. Then add a complementary divisor supported outside a growing vertical neighborhood and write the enlarged quadratic form as a block/Schur perturbation relative to that vector. Track the interaction term in the same explicit-formula normalization used by the WI amplitude ledger.

There are two decisive outcomes. A positive outcome proves a uniform persistence estimate: neutralizing the negative margin forces complementary first-harmonic mass, local count, radial depth, or spacing surplus exceeding the capacity allowed by `WI-232`--`WI-235`, at least along one cofinal sequence. A negative outcome constructs a symmetry- and zero-count-compatible sparse complement whose interaction can drive that Rayleigh quotient back to nonnegative values while staying below the existing WI tariffs; that would show that Bombieri's finite-total theorem does not extend through this interface.

Do not replace this test by normalized trace/Frobenius moments: `PL-259` already identifies their zero-density blindness. Do not infer infinite-defect stabilization by taking a limit of Bombieri's finite-total theorem: `PL-260` explicitly leaves drifting negative directions and missing uniform sign margins open. And do not import a full global Weil-positivity estimate as the persistence bound, since that would simply assume the target.

## Evidence boundary

`PL-260` is classical-prior-art synthesis, not a Mathia proof of a new inertia theorem. It establishes eventual negative-index detection only under the hypothesis that the total off-line zero set is finite. `WI-232`--`WI-235` establish local count/amplitude/spacing tariffs for specific density-matched bow-screen configurations; they do not prove a general operator-norm or Schur-complement bound for Bombieri's truncations.

No theorem currently identifies Bombieri's finite truncations with the Alpöge--Furman matrices or with the specific relaxed screens used in the WI findings, and no uniform persistence margin for an infinite sparse divisor is established. The clue is therefore only a proposed cross-line test. It becomes evidence only if the destination line derives and audits a precise bridge in the actual completed Weil form.

## Research disposition

Outcome: narrowed

Resolved by:
- [[research/weil_inertia/findings/WI-236-bombieri-finite-inertia-is-already-complete-but-sparse-escape-is-through-zero-spectral-margin.md]]

Primary-source reconstruction shows that the requested **finite negative-index completeness** is already classical and does not require a finite global off-line divisor: Bombieri's Theorem 8 computes the negative index of every finite symmetric `Gamma_N` exactly, so applying it cutoff by cutoff already detects an infinite sparse divisor at every finite scale. The finite-total hypothesis belongs to stabilization against the *total* defect and to the subsequent passage-to-limit argument, not to Theorem 8 itself.

The surviving problem is therefore narrower and different from the original Schur/Rayleigh formulation. Bombieri's off-line matrix is complex symmetric rather than generally Hermitian, so ordinary principal-submatrix interlacing cannot be invoked. What can still fail is a **uniform negative spectral margin / eigenvector tightness** as `N -> infinity`: negative eigenvalues may approach zero, equivalently their reciprocal resolvent roots may escape to infinity, and normalized mass may escape to higher off-line coordinates. `WI-236` records this corrected boundary. No bridge from that spectral escape to the `WI-232`--`WI-235` screen tariffs is currently proved.