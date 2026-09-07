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

If the smooth route is used instead, the former local scale/aspect-ratio objections are no longer open. PF-205 supplies the canonical seam width `w_n\asymp d_n` with uniform `C^1` geometry and summable critical coefficient mass. PF-207 restores the physical `w_n^2` scale at the whole Dirichlet critical-block level; PF-208 makes scale-matched cutoff commutators strongly trace-summable; PF-209 supplies the fixed-profile boundary order; PF-210 shows that `O(a_n)` low modes of size `O(d_n)` are globally weak trace class by prime-density counting; PF-211 removes exterior amplification from those low-mode norms by energy-normalized DtN gluing; and PF-212 proves the missing high-frequency/aspect-ratio estimates on the actual thin Fermi strip. Under modulewise or fixed finite-color two-sided reassembly, the local smooth-interface boundary expansion is therefore already weak trace class.

The remaining smooth-interface gate is **global Schur-complement placement/reassembly**. PF-211's normalized exterior contraction may mix boundary data between modules. PF-212 does not permit attaching the module-dependent `d_n` weights to an arbitrary globally mixing contraction. One must prove finite-color/two-sided module control, quantitative off-diagonal decay, or an equivalent weighted ideal estimate for the simultaneous native boundary decomposition.

The true-short-collar endpoint remains independent. PF-183 reduces that family to disjoint normalized thick slabs, and later rigidity work rules out several naive generic `L^1` shortcuts, but the canonical exact-area endpoint splice has not been completed.

## Research question

Can one write the exact prime/shift first relative resolvent as already controlled regular/central terms plus decomposition-interface and true-short-collar terms so that

\[
(\Delta_g+1)^{-1}U-U(\Delta_++1)^{-1}
\in\mathcal S_{1,\infty},
\]

while PF-112 continues to exclude `\mathcal S_1`?

For the decomposition interfaces, either of two routes is admissible:

- **Unsmoothed/native:** prove a critical weak-trace estimate for PF-204's exact `(dR_g)^*M_{C_0}P_{F_0}dR_+` factorization without dropping or differentiating the piecewise cotangent transport.
- **Smooth/boundary:** keep PF-205's natural-width Fermi strips and prove that the simultaneous energy-normalized boundary Schur complement can be reassembled with the module-weight structure required by PF-210/PF-212. The local Dirichlet, commutator, boundary-order, low-mode, and high-frequency scale estimates should be treated as already closed unless a new falsifier invalidates them.

Separately, prove or refute an endpoint conservative splice on PF-183's true-short-collar normalized slabs in a coefficient currency sufficient for weak `S_1`.

## Why it may matter

A positive answer would identify weak trace class as the sharp first-resolvent comparison level for the exact prime/shift geometry: PF-112 rules out trace class, while the accumulated endpoint machinery would place the full difference in `S_{1,\infty}`. This would also show that earlier logarithmic losses obtained from strong-Schatten extrapolation are not intrinsic to the exact comparison.

A negative result is equally discriminating now. On the smooth decomposition-cuff branch it must expose genuine **cross-module exterior mixing** or another global term not covered by PF-207--PF-212; it can no longer be attributed merely to shrinking support, cutoff derivatives, fixed-buffer boundary order, low-frequency exterior amplification, or thin-strip high-frequency constants. The true-short-collar splice remains a separate possible obstruction.

## Decisive test

For the smooth interface route, cut the canonical PF-205 natural-width seam strips simultaneously and write the exact native Krein/DtN decomposition. In the energy normalization of PF-211, prove one of the following:

1. the relevant low/high boundary corrections decompose into two-sided module blocks after a fixed finite coloring;
2. the normalized exterior Schur complement has quantitative off-diagonal decay strong enough that the module-dependent `d_n` weights may be inserted without losing PF-210/PF-212's threshold counts;
3. another exact weighted-ideal factorization gives the same global weak-`S_1` conclusion.

Any proof must preserve the actual module weights. Positivity and `0\le D\le I` alone are not enough, because a global contraction may redistribute boundary mass between modules. Do not repeat the already closed local high-frequency estimate unless the global construction changes the local geometry in a way that invalidates PF-212.

As an alternative, attack PF-204 directly and prove a critical theorem for the native two-Hilbert-space product with `P_{F_0}` present. A successful unsmoothed proof may bypass the boundary Schur-complement reassembly entirely.

Independently, settle the PF-183 true-short-collar endpoint splice on its disjoint normalized slabs. Generic endpoint rigidity cannot be assumed after PF-192/PF-194; the construction or obstruction must use the actual marked/collar structure and deliver a strong-`L^1`, Lorentz, Orlicz, or equivalent coefficient budget that genuinely feeds the weak operator endpoint.

Finally, write one complete first-relative-resolvent identity for a single chosen global identification and verify every term against a persisted sector theorem. Do not combine mutually incompatible smooth and unsmoothed architectures merely to cover missing pieces.

## Evidence boundary

No full weak-`S_1` theorem is established. PF-212 closes the **local** high-frequency/aspect-ratio boundary estimate only under honest modulewise/fixed-color reassembly; it does not prove that PF-211's global exterior contraction has that support structure. The unsmoothed PF-204 cotangent-transport endpoint is also still unproved, and either interface route must ultimately be combined with the independent PF-183 true-short-collar endpoint splice.

Clue acceptance therefore means only that the sharp weak-trace classification remains a concrete, evidence-backed research target. It does not imply wave-operator completeness, a scattering matrix, determinant/resonance control, prime/clone separation, or any RH consequence.

## Research disposition

The clue remains `accepted`. **The decomposition-cuff smooth route has advanced from a local critical-scale problem to a pure global placement/reassembly problem:** PF-207--PF-212 close the local principal, cutoff, finite-buffer, low-mode, exterior-amplification, and thin-strip high-frequency gates at the required endpoint currency. The next smooth-route work should target cross-module Schur-complement mixing rather than another local cylinder estimate. PF-204 remains the competing unsmoothed route, and the PF-183 true-short-collar splice remains the independent second gate before the complete first relative resolvent can be classified.