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
---

# Can the exact first relative resolvent be completed at the weak-trace endpoint?

## Observation

The first relative resolvent cannot be trace class by PF-112, while several exact sectors already sit at the natural two-dimensional weak endpoint. PF-189 controls the complete fixed-central short-collar sector. PF-196--PF-201 control the regular Lambert-body critical sector. PF-203/PF-204 provide an exact unsmoothed native factorization for decomposition interfaces, while PF-205--PF-213 develop a competing smooth boundary route through natural-width seams, prime-density low-mode counting, energy-normalized DtN gluing, high-frequency control, and an abstract Schur-reassembly criterion.

PF-214--PF-219 sharply constrain the smooth Schur route. The simultaneous exterior precision is block Jacobi, but its adjacent normalized hopping diverges. A compensating raw constant-mode mass/conductance floor exists, yet tangential screening destroys every fixed positive fraction of that floor after the correct variational shorting. Passing the screening vectors through the inverse shows that the scalar low compression `PDP` cannot carry raw-`q_n` endpoint damping with summable propagation, and PF-219 rules out every fixed polylogarithmic weakening of the same scalar architecture.

PF-220 now separates that negative scalar statement from the actual recoupling word. Insert the low/high identity immediately next to the physical seam coefficient in the exact PF-211/PF-212 expansion. Whenever the coefficient-adjacent boundary slot remains low, the middle local block has rank `O(1+L_n)` and norm `O(d_n)`; PF-210 therefore makes the complete block family weak trace class **before** the nonlocal low compressions `PDP` act. Bounded left/right multiplication by those compressions preserves `S_{1,\infty}`. Thus arbitrary low-to-low Schur nonlocality is not itself the remaining obstruction.

PF-220 also gives a general leakage bound. For every positive contraction `D`, low projection `P`, high projection `H=I-P`, and PF low prime weight `W_d=\bigoplus_nd_nP_n`,

\[
HDPW_d^{1/2},\;W_d^{1/2}PDH\in\mathcal S_{2,\infty}.
\]

This follows from `PDHDP\le PDP-(PDP)^2\le P/4` and PF-210's `W_d\in S_{1,\infty}`. The bound is deliberately one-sided in weight placement. In the unresolved physical words the coefficient is attached to the module reached on the **coefficient side after Schur transport**, so moving the prime weight to the low source endpoint would assume exactly the weighted transport still missing.

The smooth frontier is therefore no longer “find a better scalar damping for `PDP`.” It is the narrower **coefficient-side cross-frequency Schur leakage** carried by `PDH` and `HDP`, with the PF-212 low/high/Dirichlet ideal structure kept in its actual noncommutative order. The unsmoothed PF-204 route and the independent PF-183 true-short-collar route remain live alternatives.

## Research question

Can one write the exact prime/shift first relative resolvent as already controlled regular/central terms plus decomposition-interface and true-short-collar terms so that

\[
(\Delta_g+1)^{-1}U-U(\Delta_++1)^{-1}
\in\mathcal S_{1,\infty},
\]

while PF-112 continues to exclude `\mathcal S_1`?

For the smooth decomposition-interface route, do the **coefficient-side cross-frequency terms** exposed by PF-220 satisfy the weak ideal bounds required by the exact PF-211/PF-212 expansion? Equivalently, can the physical `d_n` coefficient and the available local high/Dirichlet smoothing control `PDH/HDP` without commuting a scalar prime weight through the Schur factor? The coefficient-adjacent `P/P` sectors are already closed and should not be re-proved.

For the competing unsmoothed route, can PF-204's exact native two-Hilbert factorization be placed directly at the critical weak endpoint without differentiating the piecewise cotangent transport? Independently, can the PF-183 true-short-collar normalized slabs be spliced in a coefficient currency sufficient for weak `S_1`?

## Why it may matter

A positive answer would identify weak trace class as the sharp first-resolvent comparison level for the exact prime/shift geometry: PF-112 rules out trace class while the accumulated endpoint machinery would place the full difference in `S_{1,\infty}`.

PF-217--PF-220 make the remaining smooth test substantially more discriminating. Raw pant conductance, raw onsite coercivity, raw-`q` inverse damping, and all fixed polylog relaxations of that scalar damping are now known to be the wrong currencies. At the same time, PF-220 shows that the low-to-low part of the **actual coefficient-placed operator word** survives those negatives automatically. A failure of the remaining cross-frequency coefficient-side transport would therefore be a genuine obstruction rather than an artifact of scalar compression or an overstrong endpoint normalization.

## Decisive test

Work with the exact PF-211/PF-212 simultaneous-cut expansion and split every low-containing boundary word by inserting `I=P+H` immediately next to the physical coefficient. Discard from the open gate the coefficient-adjacent `P/P` pieces already covered by PF-220.

For every surviving term containing `PDH` or `HDP`, keep the coefficient `F_n=O(d_n)` on its actual physical module and retain the available local Poisson/Dirichlet factors. Prove the required weak-ideal estimate directly, using the ideal exponent appropriate to that exact word, or construct a PF-compatible transport family showing that the output-side prime weight is moved too far or too coherently. PF-220's source-weighted weak-`S_2` estimate may be used as a control, but it is not permission to commute `W_d` through `D`.

A proposed completion that again reduces to a scalar envelope

\[
|\langle\nu_m,D\nu_n\rangle|
\lesssim
\sqrt{q_mq_n}(\log P_m\log P_n)^{O(1)}\eta_{m-n},
\qquad\eta\in\ell^1,
\]

is already excluded by PF-219. A proposed obstruction that attacks only `PDP` is also insufficient after PF-220. The live smooth question is precisely the coefficient-side **cross-frequency** transport.

As alternatives, attack PF-204's unsmoothed native factorization directly at weak `S_1`, or settle the PF-183 conservative true-short-collar splice. A complete success must ultimately use one coherent global identification and one exact first-relative-resolvent identity; incompatible smooth and unsmoothed architectures cannot simply be combined to cover missing terms.

## Evidence boundary

No full weak-`S_1` theorem is established. PF-220 closes only the coefficient-adjacent low sectors and proves a source-weighted abstract weak-`S_2` leakage estimate. It does not move the actual physical coefficient through the Schur factor, control the coefficient-side `PDH/HDP` terms, prove PF-213's unweighted Schur decay, or settle the true-short-collar endpoint. PF-204's unsmoothed endpoint also remains unresolved.

Clue acceptance means only that the sharp weak-trace classification remains a concrete, evidence-backed target. It does not imply wave-operator completeness, a scattering matrix, determinant/resonance control, prime/clone separation, or any RH consequence.

## Research disposition

The clue remains `accepted`. PF-217--PF-219 remove scalar low-Schur damping as the smooth completion strategy. PF-220 then closes the coefficient-adjacent `P/P` low sectors despite that failure and isolates the next gate to coefficient-side cross-frequency Schur leakage. PF-204 and PF-183 remain independent competing/complementary endpoint routes.