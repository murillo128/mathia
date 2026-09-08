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
  - research/prime_flute/findings/PF-222-reciprocal-prime-schur-commutator-is-compact-by-one-seam-decoupling.md
  - research/prime_flute/findings/PF-223-qualitative-cut-smoothing-does-not-force-weak-trace-schur-transport.md
---

# Can the exact first relative resolvent be completed at the weak-trace endpoint?

## Observation

The first relative resolvent cannot be trace class by PF-112, while several exact sectors already sit at the natural two-dimensional weak endpoint. PF-189 controls the complete fixed-central short-collar sector. PF-196--PF-201 control the regular Lambert-body critical sector. PF-203/PF-204 provide an exact unsmoothed native factorization for decomposition interfaces, while PF-205--PF-213 develop a competing smooth boundary route through natural-width seams, prime-density low-mode counting, energy-normalized DtN gluing, high-frequency control, and a sufficient Schur-reassembly criterion.

PF-214--PF-219 sharply constrain the smooth Schur route. The simultaneous exterior precision is block Jacobi, but its adjacent normalized hopping diverges. Raw constant-mode coercivity does not survive tangential shorting in a form that can produce summable scalar damping, and no fixed polylogarithmic weakening repairs that architecture. PF-220 then separates this negative scalar statement from the actual recoupling word: coefficient-adjacent low blocks already form a weak-trace family before nonlocal low compressions act, while a general source-weighted low/high leakage factor is weak `S_2`.

PF-221 makes the remaining coefficient placement issue exact. With

\[
\Omega=\bigoplus_nP_n^{-1}I_{\mathcal B_n},
\]

module locality gives

\[
PDH\Omega=\Omega PDH+P[D,\Omega]H.
\]

The transferred first term is already weak trace because `\Omega P\in S_{1,\infty}`. Thus the remaining smooth coefficient-transfer cost is the Schur commutator `P[D,\Omega]H` and its adjoint, whose module kernel is charged by reciprocal-prime differences rather than absolute prime weights.

PF-222 settles the first qualitative question about that remainder: it is compact. The reciprocal-prime weight has an exact norm-convergent prefix-cut decomposition, every fixed cut is decoupled by one smoothing pant DtN block, and therefore every `[D,E_j]` is trace class while `[D,\Omega]` is a norm limit of compact cut fluxes. Noncompactness is no longer a viable obstruction.

PF-223 then shows why compactness is not yet an endpoint theorem. An exact abstract countermodel retains the reciprocal-prime weight, positive block-Jacobi precision, fixed-edge finite rank, finite-rank prefix commutators, and even rank-one low sectors on every module, while `[D,\Omega]` remains compact but `P[D,\Omega]H` fails weak trace class. The failure comes from uncontrolled effective transport multiplicity at successively smaller operator scales. Hence **qualitative** one-seam smoothing and low rank cannot close the gate; the actual PF geometry must supply a position-dependent singular-value/counting estimate, most plausibly by inserting PF-212's physical frequency decay or an equivalent weighted cut-flux bound.

The smooth frontier is therefore narrower than “prove the commutator compact” and narrower than “find any Schatten estimate on each fixed cut.” It is a **quantitative reciprocal-prime cut-flux problem** for the actual thin-pant DtN geometry. The unsmoothed PF-204 route and the independent PF-183 true-short-collar route remain live alternatives.

## Research question

Can one write the exact prime/shift first relative resolvent as already controlled regular/central terms plus decomposition-interface and true-short-collar terms so that

\[
(\Delta_g+1)^{-1}U-U(\Delta_++1)^{-1}
\in\mathcal S_{1,\infty},
\]

while PF-112 continues to exclude `\mathcal S_1`?

For the smooth decomposition-interface route, can the exact norm-convergent flux expansion

\[
P[D,\Omega]H
=
\sum_{j\ge1}
(P_j^{-1}-P_{j+1}^{-1})P[D,E_j]H
\]

be placed in `\mathcal S_{1,\infty}` using **quantitative structure of the actual PF cut fluxes**? A successful estimate must couple the reciprocal-prime jump to singular-value decay/effective rank through the degenerating one-pant geometry. Fixed-edge compactness, fixed-edge membership in every `S_p`, rank-one/logarithmic low sectors, or operator-norm convergence of the series are not enough by PF-223.

For the competing unsmoothed route, can PF-204's exact native two-Hilbert factorization be placed directly at the critical weak endpoint without differentiating the piecewise cotangent transport? Independently, can the PF-183 true-short-collar normalized slabs be spliced in a coefficient currency sufficient for weak `S_1`?

## Why it may matter

A positive answer would identify weak trace class as the sharp first-resolvent comparison level for the exact prime/shift geometry: PF-112 rules out trace class while the accumulated endpoint machinery would place the full difference in `S_{1,\infty}`.

PF-217--PF-223 also make a future failure increasingly discriminating. Raw pant conductance, scalar low compression damping, fixed polylog relaxations, coefficient-adjacent low transport, absolute weight placement, and noncompactness of the reciprocal-prime commutator are all removed as explanations. PF-223 adds one more exclusion: an argument that uses only qualitative cut smoothing and small low rank cannot succeed. A negative result now has to survive the **actual** seam-frequency geometry and show that its quantitative singular-value accumulation is still too slow.

## Decisive test

Work with the exact PF-211/PF-212 simultaneous-cut expansion and the PF-222 prefix-flux identity. Keep the coefficient-adjacent `P/P` pieces and transferred `\Omega PDH/HDP\Omega` pieces outside the open gate because PF-220/PF-221 already control them.

For the remaining commutator words, derive a quantitative estimate for the actual operators

\[
P[D,E_j]H
\quad\text{and}\quad
H[D,E_j]P
\]

that uses the one-pant factorization behind PF-222 together with PF-212's low/high physical frequency split. An acceptable positive result could be a direct counting estimate for the full flux series, a weighted `S_1`/weak-`S_1` estimate whose `j`-dependence is summable after multiplication by `P_j^{-1}-P_{j+1}^{-1}`, or another factorization that prevents the large finite transport multiplicities exhibited by PF-223.

Do not replace this test by showing again that every fixed pant crossing is smoothing, every fixed cut commutator belongs to all `S_p`, or the full commutator is compact: PF-222 and PF-223 together prove those facts are below the required threshold. Likewise, PF-215's divergent raw hopping is only a lower-bound obstruction to uniform precision locality and does not supply the needed upper estimate.

A decisive negative continuation must be **PF-compatible in the stronger sense excluded from PF-223**: realize bad weak-`S_1` counting while respecting the genuine one-dimensional seam DtN singular-value decay, PF-212 physical frequency localization, and the actual prime-dependent thin-pant scales. An abstract block-Jacobi multiplicity construction alone no longer decides the line.

As alternatives, attack PF-204's unsmoothed native factorization directly at weak `S_1`, or settle the PF-183 conservative true-short-collar splice. A complete success must ultimately use one coherent global identification and one exact first-relative-resolvent identity; incompatible smooth and unsmoothed architectures cannot simply be combined to cover missing terms.

## Evidence boundary

No full weak-`S_1` theorem is established. PF-220 closes coefficient-adjacent low sectors. PF-221 isolates the reciprocal-prime Schur commutator. PF-222 proves that commutator is compact and gives its exact one-seam flux expansion. PF-223 proves only that the qualitative hypotheses underlying that compactness do not force weak trace class; its countermodel is not the canonical prime-flute DtN operator and intentionally omits the quantitative seam-frequency structure that may rescue the actual geometry.

PF-213's sufficient unweighted Schur-decay route, PF-204's unsmoothed endpoint, and the PF-183 true-short-collar endpoint also remain unresolved. Clue acceptance means only that the sharp weak-trace classification remains a concrete, evidence-backed target. It does not imply wave-operator completeness, a scattering matrix, determinant/resonance control, prime/clone separation, or any RH consequence.

## Research disposition

The clue remains `accepted`. PF-222 removes noncompactness of the reciprocal-prime Schur commutator as an obstruction. PF-223 then rules out upgrading that result to weak trace class from qualitative cut smoothing, block-Jacobi support, and low-rank counting alone. The next smooth-route test is now specifically a **quantitative PF cut-flux singular-value estimate** that retains the PF-212 seam-frequency structure; PF-204 and PF-183 remain independent competing/complementary endpoint routes.