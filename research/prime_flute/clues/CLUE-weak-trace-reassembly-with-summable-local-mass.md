---
id: CLUE-prime-flute-weak-trace-reassembly-with-summable-local-mass
type: research-clue
status: accepted
origin: research-watch
target_line: prime_flute
based_on:
  - research/prime_flute/findings/PF-112-first-relative-resolvent-is-not-trace-class.md
  - research/prime_flute/findings/PF-183-disjoint-thick-collar-slabs-remove-multiplicity-from-schatten-splice-budget.md
  - research/prime_flute/findings/PF-189-complete-short-collar-central-sector-is-weak-trace-class.md
  - research/prime_flute/findings/PF-201-global-to-local-cwikel-factorization-removes-regular-body-off-diagonal-remainder.md
  - research/prime_flute/findings/PF-204-native-two-hilbert-factorization-removes-rough-resolvent.md
  - research/prime_flute/findings/PF-205-natural-width-cuff-smoothing-is-C1-uniform-and-critical-orlicz-summable.md
  - research/prime_flute/findings/PF-210-prime-density-makes-logarithmic-rank-low-modes-weak-trace-class.md
  - research/prime_flute/findings/PF-211-energy-normalized-dtn-gluing-removes-exterior-amplification-from-low-mode-gate.md
  - research/prime_flute/findings/PF-212-thin-fermi-boundary-frequency-split-closes-local-high-mode-gate.md
  - research/prime_flute/findings/PF-213-summable-schur-off-diagonal-decay-closes-smooth-interface-reassembly-gate.md
  - research/prime_flute/findings/PF-214-simultaneous-seam-precision-is-block-jacobi-and-uniform-adjacent-hopping-would-force-exponential-schur-locality.md
  - research/prime_flute/findings/PF-215-thin-pant-corridors-force-normalized-adjacent-hopping-to-diverge.md
  - research/prime_flute/findings/PF-216-positive-shift-pant-compression-has-a-growing-mass-floor.md
  - research/prime_flute/findings/PF-217-tangential-boundary-screening-erases-the-raw-pant-mass-floor-after-shorting.md
  - research/prime_flute/findings/PF-218-raw-mass-damping-cannot-accompany-summable-low-schur-transport.md
  - research/prime_flute/findings/PF-219-no-fixed-polylogarithmic-weakening-restores-damped-low-schur-transport.md
  - research/prime_flute/findings/PF-220-coefficient-adjacent-low-recoupling-is-weak-trace-without-schur-locality.md
  - research/prime_flute/findings/PF-221-coefficient-weight-transfer-reduces-to-a-reciprocal-prime-schur-commutator.md
---

# Can the exact first relative resolvent be completed at the weak-trace endpoint?

## Observation

The first relative resolvent cannot be trace class by PF-112, while several exact sectors already sit at the natural two-dimensional weak endpoint. PF-189 controls the complete fixed-central short-collar sector. PF-196--PF-201 control the regular Lambert-body critical sector. PF-203/PF-204 provide an exact unsmoothed native factorization for decomposition interfaces, while PF-205--PF-213 develop a competing smooth boundary route through natural-width seams, prime-density low-mode counting, energy-normalized DtN gluing, high-frequency control, and an abstract Schur-reassembly criterion.

PF-214--PF-219 sharply constrain the smooth Schur route. The simultaneous exterior precision is block Jacobi, but its adjacent normalized hopping diverges. A compensating raw constant-mode mass/conductance floor exists, yet tangential screening destroys every fixed positive fraction of that floor after the correct variational shorting. Passing the screening vectors through the inverse shows that the scalar low compression `PDP` cannot carry raw-`q_n` endpoint damping with summable propagation, and PF-219 rules out every fixed polylogarithmic weakening of the same scalar architecture.

PF-220 separates that negative scalar statement from the actual recoupling word. Insert the low/high identity immediately next to the physical seam coefficient in the exact PF-211/PF-212 expansion. Whenever the coefficient-adjacent boundary slot remains low, the middle local block has rank `O(1+L_n)` and norm `O(d_n)`; PF-210 therefore makes the complete block family weak trace class **before** the nonlocal low compressions `PDP` act. Bounded left/right multiplication by those compressions preserves `S_{1,\infty}`. Thus arbitrary low-to-low Schur nonlocality is not itself the remaining obstruction.

PF-220 also gives a general leakage bound. For every positive contraction `D`, low projection `P`, high projection `H=I-P`, and PF low prime weight `W_d=\bigoplus_nd_nP_n`,

\[
HDPW_d^{1/2},\;W_d^{1/2}PDH\in\mathcal S_{2,\infty}.
\]

This follows from `PDHDP\le PDP-(PDP)^2\le P/4` and PF-210's `W_d\in S_{1,\infty}`. The bound is deliberately one-sided in weight placement. In the unresolved physical words the coefficient is attached to the module reached on the **coefficient side after Schur transport**, so positivity alone does not move the prime weight to the low source endpoint.

PF-221 now makes that weight-transfer failure exact. Use the canonical full-module boundary weight `\Omega=\bigoplus_nP_n^{-1}I_{\mathcal B_n}` and factor every local seam coefficient as the corresponding bulk module weight times a uniformly bounded coefficient. Module locality of the normalized Poisson factor gives, for a coefficient-adjacent leakage word,

\[
PDH\Omega=\Omega PDH+P[D,\Omega]H.
\]

The transferred first term is already weak trace because `\Omega P\in S_{1,\infty}`. Hence the entire remaining cost of moving the coefficient envelope to the low endpoint is the bounded Schur commutator `P[D,\Omega]H`. Its exact module kernel is

\[
\Pi_m[D,\Omega]\Pi_n
=(P_n^{-1}-P_m^{-1})\Pi_mD\Pi_n,
\]

so same-module mixing cancels and transported blocks are charged reciprocal-prime **differences**, not absolute prime weights. PF-214 further shows on bounded truncations that this commutator is sourced by adjacent block-Jacobi edges weighted by `P_n^{-1}-P_{n+1}^{-1}`. PF-215's divergent raw hopping therefore does not by itself decide the new gate; it supplies no matching upper estimate for the difference-weighted edge commutator.

The smooth frontier is therefore no longer “find a better scalar damping for `PDP`” or even the broader “move a prime weight through `PDH`.” It is the narrower **reciprocal-prime Schur-commutator problem** carried by `P[D,\Omega]H` and its adjoint, with the PF-212 local high/Dirichlet ideal structure kept in its actual noncommutative order. The unsmoothed PF-204 route and the independent PF-183 true-short-collar route remain live alternatives.

## Research question

Can one write the exact prime/shift first relative resolvent as already controlled regular/central terms plus decomposition-interface and true-short-collar terms so that

\[
(\Delta_g+1)^{-1}U-U(\Delta_++1)^{-1}
\in\mathcal S_{1,\infty},
\]

while PF-112 continues to exclude `\mathcal S_1`?

For the smooth decomposition-interface route, do the **difference-weighted Schur commutators** exposed by PF-221 satisfy the weak ideal bounds required by the exact PF-211/PF-212 cross-frequency words? Concretely, can the block-Jacobi structure of `K`, the adjacent factors

\[
P_n^{-1}-P_{n+1}^{-1}
=\frac{P_{n+1}-P_n}{P_nP_{n+1}},
\]

and the available local high/Dirichlet smoothing control `P[D,\Omega]H` (or its adjoint) at the required endpoint? The coefficient-adjacent `P/P` sectors and the transferred `\Omega PDH` main terms are already closed and should not be re-proved.

For the competing unsmoothed route, can PF-204's exact native two-Hilbert factorization be placed directly at the critical weak endpoint without differentiating the piecewise cotangent transport? Independently, can the PF-183 true-short-collar normalized slabs be spliced in a coefficient currency sufficient for weak `S_1`?

## Why it may matter

A positive answer would identify weak trace class as the sharp first-resolvent comparison level for the exact prime/shift geometry: PF-112 rules out trace class while the accumulated endpoint machinery would place the full difference in `S_{1,\infty}`.

PF-217--PF-221 make the remaining smooth test substantially more discriminating. Raw pant conductance, raw onsite coercivity, raw-`q` inverse damping, fixed polylog relaxations of that scalar damping, and coefficient-adjacent low-to-low transport are no longer live obstructions. PF-221 further shows that the physical coefficient can be transferred to the low endpoint except for one commutator whose kernel sees reciprocal-prime differences. A failure at this stage would therefore be a genuine obstruction to the coefficient-weighted cross-frequency mechanism rather than an artifact of scalar compression, absolute-weight placement, or an overstrong uniform-hopping hypothesis.

## Decisive test

Work with the exact PF-211/PF-212 simultaneous-cut expansion and split every low-containing boundary word by inserting `I=P+H` immediately next to the physical coefficient. Discard from the open gate the coefficient-adjacent `P/P` pieces already covered by PF-220.

For every surviving coefficient-adjacent term containing `PDH` or `HDP`, factor the established `O(P_n^{-1})` coefficient envelope through the module-local Poisson factor exactly as in PF-221. The transferred `\Omega PDH/HDP\Omega` piece is already weak trace. Isolate the commutator remainder and prove the ideal estimate required by that exact word for

\[
P[D,\Omega]H
\quad\text{or}\quad
H[D,\Omega]P,
\qquad
\Omega=\bigoplus_nP_n^{-1}I_{\mathcal B_n}.
\]

A positive route may work directly with the bounded block formula

\[
\Pi_m[D,\Omega]\Pi_n
=(P_n^{-1}-P_m^{-1})\Pi_mD\Pi_n,
\]

or may first justify the full form/operator version of `[D,\Omega]=-D[K,\Omega]D` and exploit PF-214's adjacent support

\[
\Pi_{n+1}[K,\Omega]\Pi_n
=(P_n^{-1}-P_{n+1}^{-1})\Pi_{n+1}K\Pi_n.
\]

If using the precision-side identity, explicitly prove the form-domain/extension step: PF-215 permits unbounded neighboring precision blocks and forbids silently treating `[K,\Omega]` as a uniformly bounded Jacobi matrix. Likewise, do not infer an upper estimate from PF-215's lower bound merely because the reciprocal-prime difference heuristically cancels the expected thin-corridor scale.

A negative result should construct a PF-compatible family showing that even after the reciprocal-prime endpoint difference and the two Schur factors/local PF-212 smoothing are retained, the commutator remainder is too large for the required weak endpoint.

As alternatives, attack PF-204's unsmoothed native factorization directly at weak `S_1`, or settle the PF-183 conservative true-short-collar splice. A complete success must ultimately use one coherent global identification and one exact first-relative-resolvent identity; incompatible smooth and unsmoothed architectures cannot simply be combined to cover missing terms.

## Evidence boundary

No full weak-`S_1` theorem is established. PF-220 closes the coefficient-adjacent low sectors and proves a source-weighted abstract weak-`S_2` leakage estimate. PF-221 closes only the **transferred-weight main term** and identifies the exact Schur-commutator remainder. It does not prove `P[D,\Omega]H` belongs to any Schatten ideal, justify an unbounded full-space `[K,\Omega]` operator without further domain work, or establish the heuristic cancellation suggested by the adjacent reciprocal-prime difference.

PF-213's unweighted Schur decay, PF-204's unsmoothed endpoint, and the PF-183 true-short-collar endpoint also remain unresolved. Clue acceptance means only that the sharp weak-trace classification remains a concrete, evidence-backed target. It does not imply wave-operator completeness, a scattering matrix, determinant/resonance control, prime/clone separation, or any RH consequence.

## Research disposition

The clue remains `accepted`. PF-217--PF-219 remove scalar low-Schur damping, PF-220 closes coefficient-adjacent `P/P` sectors, and PF-221 reduces the remaining coefficient-weight transfer to the reciprocal-prime Schur commutator `P[D,\Omega]H` and its adjoint. The next smooth-route test is therefore an edge/difference-weighted commutator estimate or counterexample, while PF-204 and PF-183 remain independent competing/complementary endpoint routes.