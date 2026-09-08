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

If the smooth route is used instead, the former local scale/aspect-ratio objections are no longer open. PF-205 supplies the canonical seam width `w_n\asymp d_n` with uniform `C^1` geometry and summable critical coefficient mass. PF-207 restores the physical `w_n^2` scale at the whole Dirichlet critical-block level; PF-208 makes scale-matched cutoff commutators strongly trace-summable; PF-209 supplies the fixed-profile boundary order; PF-210 shows that `O(a_n)` low modes of size `O(d_n)` are globally weak trace class by prime-density counting; PF-211 removes exterior amplification from those low-mode norms by energy-normalized DtN gluing; and PF-212 proves the missing high-frequency/aspect-ratio estimates on the actual thin Fermi strip.

PF-213 now closes the **abstract reassembly implication**. If the simultaneous normalized exterior Schur complements have module blocks bounded by an envelope `eta_k` with

\[
\sum_{k\in\mathbb Z}\sqrt{(1+|k|)\eta_k}<\infty,
\]

then the low-containing and double-high boundary families are globally weak trace class and the high/Dirichlet families are trace class. Uniform exponential module decay is a sufficient special case. PF-213 also gives an explicit positive-contraction counterexample in which infinitely many tail low modes are funneled into one fixed module, making the weighted operator noncompact. Therefore positivity `0\le D\le I` is not merely insufficient for the proof technique; without quantitative locality it is insufficient even for compactness in the abstract model.

The remaining smooth-interface gate is consequently **geometric/operator locality of the actual simultaneous Schur complement**, not endpoint summation once such locality is available. The true-short-collar endpoint remains independent. PF-183 reduces that family to disjoint normalized thick slabs, and later rigidity work rules out several naive generic `L^1` shortcuts, but the canonical exact-area endpoint splice has not been completed.

## Research question

Can one write the exact prime/shift first relative resolvent as already controlled regular/central terms plus decomposition-interface and true-short-collar terms so that

\[
(\Delta_g+1)^{-1}U-U(\Delta_++1)^{-1}
\in\mathcal S_{1,\infty},
\]

while PF-112 continues to exclude `\mathcal S_1`?

For the decomposition interfaces, either of two routes is admissible:

- **Unsmoothed/native:** prove a critical weak-trace estimate for PF-204's exact `(dR_g)^*M_{C_0}P_{F_0}dR_+` factorization without dropping or differentiating the piecewise cotangent transport.
- **Smooth/boundary:** keep PF-205's natural-width Fermi strips, construct the simultaneous native Krein/DtN decomposition, and prove that its normalized exterior Schur factors satisfy PF-213's summable module-decay condition, a finite-range/fixed-color specialization, or another weighted estimate that gives the same offset bounds. The local Dirichlet, commutator, boundary-order, low-mode, high-frequency, and abstract decaying-reassembly estimates should be treated as closed unless a new falsifier invalidates them.

Separately, prove or refute an endpoint conservative splice on PF-183's true-short-collar normalized slabs in a coefficient currency sufficient for weak `S_1`.

## Why it may matter

A positive answer would identify weak trace class as the sharp first-resolvent comparison level for the exact prime/shift geometry: PF-112 rules out trace class, while the accumulated endpoint machinery would place the full difference in `S_{1,\infty}`. This would also show that earlier logarithmic losses obtained from strong-Schatten extrapolation are not intrinsic to the exact comparison.

A negative result is equally discriminating now. On the smooth decomposition-cuff branch it must show that the **actual global exterior Schur transport** fails every sufficiently summable module-locality budget, or expose another global term outside PF-207--PF-213. PF-213 rules out treating arbitrary positive mixing as harmless: such mixing can destroy compactness even when there is only one low source mode per tail module and the physical weights decay like `1/p_n`. The true-short-collar splice remains a separate possible obstruction.

## Decisive test

For the smooth interface route, cut the canonical PF-205 natural-width seam strips simultaneously and write the exact native Krein/DtN decomposition. Let `Q_n` be the physical module projections in the normalized boundary energy space and let

\[
D^{(r)}=\Lambda_{Q,r}^{1/2}
(\Lambda_{Q,r}+\Lambda_{E,r})^{-1}
\Lambda_{Q,r}^{1/2},
\qquad r\in\{g,h\}.
\]

Prove one of the following:

1. there is an envelope `eta_k` such that `\|Q_mD^{(r)}Q_n\|\le eta_{m-n}` uniformly on both metric sides and `\sum_k\sqrt{(1+|k|)eta_k}<\infty`;
2. the relevant boundary corrections have a finite-range or fixed finite-color two-sided module structure, which is a stronger special case already covered by PF-210/PF-212/PF-213;
3. another exact weighted-ideal factorization controls the same cross-module transport strongly enough to reproduce PF-213's offset endpoint bounds.

The estimate must be proved in the physical module decomposition **before** diagonalizing the global boundary operator. It must preserve the location of the module-dependent `d_n` coefficient; commuting that weight through `D` is not allowed. Positivity and contractivity alone are explicitly falsified by PF-213's noncompactness model.

Classical inverse-decay results for banded positive operators suggest one possible mechanism only if the PF boundary precision/Schur operator can first be shown to have an appropriate local band structure and uniform conditioning. That structural premise is not currently established and must not be assumed from the one-ended topology alone.

As an alternative, attack PF-204 directly and prove a critical theorem for the native two-Hilbert-space product with `P_{F_0}` present. A successful unsmoothed proof may bypass the boundary Schur-complement reassembly entirely.

Independently, settle the PF-183 true-short-collar endpoint splice on its disjoint normalized slabs. Generic endpoint rigidity cannot be assumed after PF-192/PF-194; the construction or obstruction must use the actual marked/collar structure and deliver a strong-`L^1`, Lorentz, Orlicz, or equivalent coefficient budget that genuinely feeds the weak operator endpoint.

Finally, write one complete first-relative-resolvent identity for a single chosen global identification and verify every term against a persisted sector theorem. Do not combine mutually incompatible smooth and unsmoothed architectures merely to cover missing pieces.

## Evidence boundary

No full weak-`S_1` theorem is established. PF-213 proves a **conditional abstract reassembly theorem** and an exact obstruction to unrestricted positive mixing; it does not prove any off-diagonal decay for the actual PF exterior Dirichlet-to-Neumann/Schur operator. The unsmoothed PF-204 cotangent-transport endpoint is also still unproved, and either interface route must ultimately be combined with the independent PF-183 true-short-collar endpoint splice.

Clue acceptance therefore means only that the sharp weak-trace classification remains a concrete, evidence-backed research target. It does not imply wave-operator completeness, a scattering matrix, determinant/resonance control, prime/clone separation, or any RH consequence.

## Research disposition

The clue remains `accepted`. **The smooth decomposition-cuff route is now reduced to proving quantitative locality for one actual global boundary operator.** PF-207--PF-212 close the local principal, cutoff, finite-buffer, low-mode, exterior-amplification, and thin-strip high-frequency gates; PF-213 proves that summably decaying module transport is sufficient to reassemble those boundary pieces and that positivity alone can fail even compactness. The next smooth-route work should therefore derive or falsify such off-diagonal decay for the simultaneous normalized Schur complement rather than repeat endpoint summation or local-cylinder estimates. PF-204 remains the competing unsmoothed route, and the PF-183 true-short-collar splice remains the independent second gate before the complete first relative resolvent can be classified.