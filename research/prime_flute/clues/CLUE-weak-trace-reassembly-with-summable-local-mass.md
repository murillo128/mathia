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
  - research/prime_flute/findings/PF-207-dirichlet-block-dilation-restores-critical-seam-scale.md
  - research/prime_flute/findings/PF-210-prime-density-makes-logarithmic-rank-low-modes-weak-trace-class.md
  - research/prime_flute/findings/PF-211-energy-normalized-dtn-gluing-removes-exterior-amplification-from-low-mode-gate.md
  - research/prime_flute/findings/PF-212-thin-fermi-boundary-frequency-split-closes-local-high-mode-gate.md
  - research/prime_flute/findings/PF-213-summable-schur-off-diagonal-decay-closes-smooth-interface-reassembly-gate.md
  - research/prime_flute/findings/PF-214-simultaneous-seam-precision-is-block-jacobi-and-uniform-adjacent-hopping-would-force-exponential-schur-locality.md
  - research/prime_flute/findings/PF-215-thin-pant-corridors-force-normalized-adjacent-hopping-to-diverge.md
---

# Can the exact first relative resolvent be completed at the weak-trace endpoint?

## Observation

The first relative resolvent cannot be trace class by PF-112, but a large part of the exact prime/shift comparison is now controlled at the natural two-dimensional weak endpoint. PF-189 closes the complete fixed-central short-collar sector, while PF-196--PF-201 close the regular Lambert-body principal critical sector, including matrix-valued `L\log L` control, localization, finite-color counting, uniform regular-body constants, and external off-diagonal reassembly.

The distinguished decomposition-cuff interface has also narrowed sharply. PF-203 shows that seam smoothing is optional at quadratic-form level, and PF-204 gives the exact unsmoothed native-resolvent factorization

\[
R_gU_0-U_0R_+
=(dR_g)^*M_{C_0}P_{F_0}dR_+.
\]

Thus one remaining route is a direct critical estimate for this mixed two-native-resolvent word with its bounded piecewise cotangent transport.

If the smooth route is used instead, PF-205 supplies the canonical seam width `w_n\asymp d_n` with uniform `C^1` geometry and summable critical coefficient mass. PF-207 restores the physical `w_n^2` scale at the whole Dirichlet critical-block level; PF-208 makes scale-matched cutoff commutators strongly trace-summable; PF-209 supplies the fixed-profile boundary order; PF-210 shows that `O(a_n)` low modes of size `O(d_n)` are globally weak trace class by prime-density counting; PF-211 removes exterior amplification from those low-mode norms by energy-normalized DtN gluing; and PF-212 proves the missing high-frequency/aspect-ratio estimates on the actual thin Fermi strip.

PF-213 closes the **abstract reassembly implication**. If the simultaneous normalized exterior Schur complements have module blocks bounded by an envelope `eta_k` with

\[
\sum_{k\in\mathbb Z}\sqrt{(1+|k|)\eta_k}<\infty,
\]

then the low-containing and double-high boundary families are globally weak trace class and the high/Dirichlet families are trace class. PF-213 also gives an explicit positive-contraction counterexample in which infinitely many tail low modes are funneled into one fixed module, making the weighted operator noncompact.

PF-214 closes the **topological support part** of that locality gate. Under the simultaneous PF-205 cut, the exterior is a disjoint chain of one-cusp pant cores, so after grouping the two seam boundaries of each cuff into one physical module the normalized exterior precision

\[
K=\Lambda_Q^{-1/2}\Lambda_E\Lambda_Q^{-1/2}
\]

is exactly block Jacobi and the Schur factor is `D=(I+K)^{-1}`. PF-214 proves that uniformly bounded adjacent normalized blocks would force exponential decay of `D`.

PF-215 now shows that this **simple uniform-hopping branch is unavailable in the actual PF geometry**. Constant opposite data on the two finite boundaries of one thin pant core cost `\gtrsim s_n^{-1}` in positive-shift energy, where `s_n=(h_n+h_{n+1})/2` is the exact inter-cuff distance, whereas the two-sided symmetric constant mode on a PF-205 strip has normalization energy at most `2w_nL_n`. Consequently every bounded adjacent normalized block satisfies

\[
\|Q_{n+1}KQ_n\|
\gtrsim
\frac{1}{s_n\sqrt{w_nL_nw_{n+1}L_{n+1}}}
\gtrsim
\frac{P_n^{1.475}}{\log P_n},
\]

so the adjacent hopping diverges on the whole tail. This does not determine the decay of `D`: the same narrow pant also contributes large diagonal energy, and a correlated variable-conductance inverse may behave much better than a bound based on raw hopping suggests.

The remaining smooth-interface gate is therefore **scale-sensitive inversion/reassembly**, not topology, local thin-strip estimates, or a uniform bound on `K`'s off-diagonal blocks. The true-short-collar endpoint remains independent. PF-183 reduces that family to disjoint normalized thick slabs, and later rigidity work rules out several naive generic `L^1` shortcuts, but the canonical exact-area endpoint splice has not been completed.

## Research question

Can one write the exact prime/shift first relative resolvent as already controlled regular/central terms plus decomposition-interface and true-short-collar terms so that

\[
(\Delta_g+1)^{-1}U-U(\Delta_++1)^{-1}
\in\mathcal S_{1,\infty},
\]

while PF-112 continues to exclude `\mathcal S_1`?

For the decomposition interfaces, either of two routes remains admissible:

- **Unsmoothed/native:** prove a critical weak-trace estimate for PF-204's exact `(dR_g)^*M_{C_0}P_{F_0}dR_+` factorization without dropping or differentiating the piecewise cotangent transport.
- **Smooth/boundary:** keep PF-205's natural-width Fermi strips and PF-214's exact block-Jacobi precision, but do not seek a uniform adjacent-hopping bound: PF-215 refutes it. Instead exploit the actual scale-dependent diagonal/cross structure to prove enough decay or weighted transport for `D=(I+K)^{-1}` to meet PF-213, or bypass blockwise inverse decay with another exact weighted-ideal factorization.

Separately, prove or refute an endpoint conservative splice on PF-183's true-short-collar normalized slabs in a coefficient currency sufficient for weak `S_1`.

## Why it may matter

A positive answer would identify weak trace class as the sharp first-resolvent comparison level for the exact prime/shift geometry: PF-112 rules out trace class, while the accumulated endpoint machinery would place the full difference in `S_{1,\infty}`. It would also show that the large low-symmetric normalized conductances exposed by PF-215 are compatible with sufficient decay after the full Schur inversion.

A negative result is equally discriminating now. On the smooth decomposition-cuff branch it must show that the **actual variable-conductance Schur inverse** fails every sufficiently strong locality budget, or expose another global term outside PF-207--PF-215. PF-214 rules out blaming an intrinsically nonlocal precision, while PF-215 rules out completing the argument with a uniform raw-hopping estimate.

## Decisive test

For the smooth interface route, use the canonical PF-205 simultaneous seam cut and PF-214's physical module decomposition. For each source/target metric let

\[
K^{(r)}=\Lambda_{Q,r}^{-1/2}\Lambda_{E,r}\Lambda_{Q,r}^{-1/2},
\qquad
D^{(r)}=(I+K^{(r)})^{-1},
\qquad r\in\{g,h\}.
\]

The support identity `Q_mK^{(r)}Q_n=0` for `|m-n|>1` is established, while PF-215 shows the adjacent blocks cannot be uniformly bounded. The decisive smooth-route test is now to do one of the following:

1. isolate the low-symmetric compression of the one-pant DtN form and determine its diagonal and cross scales together, producing a variable-conductance Jacobi/Schur model that is quantitatively comparable to the actual normalized form;
2. prove directly for that scale-dependent block-Jacobi form a weighted Combes--Thomas, Green-kernel, Agmon, or other inverse estimate whose resulting `D^{(r)}` blocks satisfy PF-213's offset budget after the physical `d_n` coefficient is kept on its module;
3. if such a comparison fails, construct a source-backed lower bound/counterexample showing that the actual `D` violates the PF-213 transport budget, rather than inferring failure merely from the divergent `K` blocks;
4. bypass blockwise inverse decay with another exact weighted-ideal factorization controlling the same cross-module transport.

The local analysis must retain the **two-sided symmetric strip sector** that drives PF-215. Bounding the pant DtN form in an unnormalized boundary `L^2` norm, using positivity alone, or estimating only high/antisymmetric modes cannot decide this gate. Equally, the divergent adjacent hopping is not itself evidence that `D` is nonlocal: diagonal/off-diagonal cancellation must be measured before drawing that conclusion.

As an alternative, attack PF-204 directly and prove a critical theorem for the native two-Hilbert-space product with `P_{F_0}` present. A successful unsmoothed proof may bypass the boundary Schur-complement reassembly entirely.

Independently, settle the PF-183 true-short-collar endpoint splice on its disjoint normalized slabs. Generic endpoint rigidity cannot be assumed after PF-192/PF-194; the construction or obstruction must use the actual marked/collar structure and deliver a strong-`L^1`, Lorentz, Orlicz, or equivalent coefficient budget that genuinely feeds the weak operator endpoint.

Finally, write one complete first-relative-resolvent identity for a single chosen global identification and verify every term against a persisted sector theorem. Do not combine mutually incompatible smooth and unsmoothed architectures merely to cover missing pieces.

## Evidence boundary

No full weak-`S_1` theorem is established. PF-213 proves the conditional abstract reassembly theorem; PF-214 proves that the canonical simultaneous exterior precision is nearest-neighbor; PF-215 proves that its simple uniform adjacent-hopping sufficient condition fails strongly on the low symmetric modes. PF-215 does **not** prove that the inverse Schur factor has slow decay or that PF-213's transport criterion fails. The relevant diagonal/cross cancellation and scale-dependent inverse remain uncomputed.

The unsmoothed PF-204 cotangent-transport endpoint is also still unproved, and either interface route must ultimately be combined with the independent PF-183 true-short-collar endpoint splice.

Clue acceptance therefore means only that the sharp weak-trace classification remains a concrete, evidence-backed research target. It does not imply wave-operator completeness, a scattering matrix, determinant/resonance control, prime/clone separation, or any RH consequence.

## Research disposition

The clue remains `accepted`. **PF-215 closes the uniform normalized-hopping sub-branch negatively.** The smooth decomposition-cuff route should now analyze the actual large-conductance block-Jacobi inverse, including diagonal/off-diagonal cancellation, and test the resulting `D` directly against PF-213's weighted transport budget. PF-204 remains the competing unsmoothed route, and the PF-183 true-short-collar splice remains the independent second gate before the complete first relative resolvent can be classified.