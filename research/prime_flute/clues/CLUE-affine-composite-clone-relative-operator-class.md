---
id: CLUE-prime-flute-affine-composite-clone-relative-operator-class
type: research-clue
status: accepted
origin: mind
target_line: prime_flute
based_on:
  - research/prime_flute/findings/PF-106-affine-composite-clone-is-l1-close.md
  - research/prime_flute/findings/PF-107-shift-clone-cuff-defect-is-l2-not-l1.md
  - research/prime_flute/findings/PF-108-shift-clone-collar-and-spine-defects-are-summable.md
  - research/prime_flute/findings/PF-109-shift-clone-preserves-canonical-separator-pinching-multiplicatively.md
  - research/prime_flute/findings/PF-111-shift-clone-has-summable-pant-local-marked-length-distortion.md
  - research/prime_flute/findings/PF-112-first-relative-resolvent-is-not-trace-class.md
  - research/prime_flute/findings/PF-114-shift-clone-pant-waves-telescope-but-seam-relative-mode-does-not.md
  - research/prime_flute/findings/PF-118-shift-clone-pants-are-arc-lipschitz-close.md
  - research/prime_flute/findings/PF-119-canonical-cusp-split-gluing-offset-has-summable-shift-clone-defect.md
  - research/prime_flute/findings/PF-120-cusp-busemann-shifts-must-synchronize.md
  - research/prime_flute/findings/PF-121-ideal-lambert-shift-comparison-is-asymptotically-bilipschitz.md
  - research/prime_flute/findings/PF-122-canonical-cusp-strip-gluing-cost-is-summable.md
---

# Affine composite clone and the relative Laplacian class

## Observation

The exact all-composite shift clone `p_n -> p_n+1` remains extremely close to the prime flute under every tail control that has survived audit. PF-106--PF-111 give summable or asymptotically vanishing endpoint, relative-cuff, collar/spine, separator, and pant-local marked-length defects. PF-112 closes first-resolvent trace class for a generic two-dimensional microlocal reason but explicitly leaves compactness open.

The geometric bridge has now narrowed substantially. PF-119 factorizes each normalized one-cusp pant into two one-parameter ideal Lambert quadrilaterals and proves that the canonical cusp split-offset defect is `ell^1`. PF-120 shows that independently canonical side isometries cannot be prescribed on both rays of one cusp because their Busemann shifts must synchronize. PF-121 then constructs genuine `1+o(1)` bilipschitz homeomorphisms `Q(a_n)->Q(a_n^+)` uniformly through the collapsing ideal geometry, so there is no intrinsic single-quadrilateral `O(1)` distortion.

PF-122 removes the remaining **deep-cusp** coherence candidate. In the physical PF-119 normalization, the region `y>=1` is the same standard strip `0<=x<=1` for every pant. The piecewise-affine map fixing height and sending the split `x=t_n` to `x=t_n^+` has

```text
log Bilip <= |epsilon_n - epsilon_{n+1}|
             = |sigma_n^+ - sigma_n|,
```

and PF-119 proves the right-hand side is `ell^1`. The estimate is uniform even when `t_n->0` or `1`, and it uses one common Busemann gauge on all cusp rays. Thus the nonsummable reciprocal-prime common scale, extreme split ratios, and the infinite cusp itself no longer supply a plausible metric-amplification obstruction.

The unresolved local problem is now confined to a bounded-height transition: reconcile the lower PF-121 quadrilateral maps with the PF-122 canonical cusp-strip map while keeping the finite-cuff boundary trace dependent only on that cuff. If this can be done with distortion `1+o(1)`, the resulting pentagons should double and the zero-twist pants should have a chance to glue canonically across the full flute.

## Research question

Can the PF-121 and PF-122 maps be combined into boundary-coherent one-cusp pant homeomorphisms and then a global marked homeomorphism

```text
F : X_prime -> X_shift
```

such that, after transporting the clone metric to the prime surface,

```text
||F^* g_shift - g_prime||_{g_prime} -> 0
```

uniformly at infinity, with the associated volume-density ratio also tending to `1`?

The concrete local gate is to construct, on each normalized pentagon, a piecewise-smooth transition across a fixed-height band that simultaneously:

1. agrees with PF-122 on the upper cusp strip;
2. agrees with a PF-121-type map on the lower Lambert pieces;
3. induces one identical trace on the artificial split ray;
4. induces on each finite cuff a trace determined only by that cuff parameter pair `(a_n,a_n^+)`, so the two adjacent pants glue with zero twist;
5. has bilipschitz constant tending to `1` uniformly over all possible neighboring gap ratios.

If those maps glue globally, the first operator target is **compact relative resolvent/equality of essential spectra**, not trace class. Georgescu--Golénia's strong-equivalence theorem for complete Riemannian structures is the natural theorem to audit against the resulting common-manifold metric coefficients.

## Why it may matter

This is now a sharp adversarial test of whether any prime-specific information survives in the essential spectral class of the exact flute. A positive global strong-equivalence theorem would show that an explicit surface built only from composites has the same essential Laplace spectrum and compact relative resolvent under the natural marking, eliminating essential-spectrum data as a primality/RH selector for this construction.

A negative result would be equally informative, but it can no longer be blamed on raw cuff divergence, local closed-word lengths, collar geometry, Lambert collapse, a scalar cusp offset, independent Busemann gauges, or extreme cusp split ratios. It would have to expose a genuine bounded-height gluing/Jacobian obstruction or a nonlocal infinite-surface amplification mechanism.

## Decisive test

A positive resolution must:

1. construct the boundary-coherent transition described above with a tail bilipschitz constant `K_n->1`;
2. double the pentagon maps and prove that maps on every shared cuff agree exactly under the zero-twist marking;
3. glue them to a complete global homeomorphism and verify uniform metric equivalence plus pointwise metric-norm and volume-density ratios tending to `1` at infinity;
4. audit and apply the exact hypotheses of an appropriate relative-Laplacian theorem to obtain compact relative resolvent/equality of essential spectra.

A decisive negative resolution must identify an invariant lower bound that survives PF-121 and PF-122: for example, prove that every transition with the required split/cuff traces pays a fixed positive bilipschitz or quasiconformal cost along an escaping sequence, or construct a weakly-null/Weyl sequence showing that no common-manifold metric perturbation tending to zero can realize the marked clone.

Do not use failure of `S_1` for the first resolvent as such a negative test: PF-112 proves that failure locally for every non-isometric smooth metric perturbation, even when compactness holds. Higher Schatten classes, higher resolvent powers, heat differences, wave/scattering equivalence, and determinants remain separate later gates.

## Evidence boundary

This clue is **not** evidence that the complete prime and shift-clone surfaces are quasiconformally equivalent, strongly equivalent, compact-resolvent perturbations, wave-equivalent, or spectrally equivalent. PF-121 proves only a local ideal-quadrilateral map; PF-122 proves only a canonical map on the deep cusp strip. Their traces have not yet been reconciled across the bounded-height transition, the doubled pants have not been glued, and no global metric-density estimate has been established.

The closest audited comparison literature remains hypothesis-mismatched rather than decisive: Minsky gives coarse bilipschitz pants/degenerate-hexagon comparisons for bounded additive boundary changes; Wu--Zhang give `1+o(1)` metric-tensor control with prescribed boundary data in a neighboring thick-boundary regime; Saric's asymptotically conformal Fenchel--Nielsen theorem assumes an upper-bounded pants decomposition; and bounded-ideal-triangulation routes are unavailable by PF-110. None of those statements directly supplies the current bounded-height transition for one cusp and two unbounded cuffs.

## Research disposition

**Accepted and materially narrowed, not resolved.** PF-121 kills the single-Lambert interior obstruction and PF-122 kills the deep-cusp/split-ray amplification. The next tractable gate is the fixed-height boundary-coherent transition and exact zero-twist cuff gluing. Compact relative resolvent remains the first unresolved operator consequence; first-resolvent trace class remains closed negatively by PF-112.