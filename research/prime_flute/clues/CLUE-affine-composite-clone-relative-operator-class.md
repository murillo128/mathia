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
  - research/prime_flute/findings/PF-123-asymptotic-metric-equivalence-forces-compact-relative-resolvent.md
  - research/prime_flute/findings/PF-124-lambert-cuff-trace-is-zero-twist-coherent.md
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

PF-123 audits the operator end of the bridge. Georgescu--Golénia's Riemannian specialization proves that, once a common-manifold metric comparison has uniformly equivalent coefficients tending to one at infinity and volume-density ratio tending to one, the corresponding Laplacians have compact resolvent difference under the canonical bounded identification and therefore equal essential spectrum. No `ell^1` or quantitative rate is required at that stage.

PF-124 removes the finite-cuff part of the remaining geometric coherence problem. The explicit PF-121 Lambert map induces a half-cuff arclength trace `T_(a,a')` depending only on the matched cuff pair, with bilipschitz constant `1+O(a'-a)`. Reflecting that trace across the two seam feet gives a full-cuff homeomorphism that commutes **exactly** with the canonical zero-twist orientation reversal. Therefore pant doubling and gluing across shared finite cuffs require no additional choice and introduce no twist mismatch. The unresolved problem is confined to the bounded-height reconciliation of the two Lambert maps along the artificial split ray.

## Research question

Can the PF-121 and PF-122 maps be combined into a boundary-coherent normalized pentagon homeomorphism and then a global marked homeomorphism

```text
F : X_prime -> X_shift
```

such that, after transporting the clone metric to the prime surface,

```text
||F^* g_shift - g_prime||_{g_prime} -> 0
```

uniformly at infinity, with the associated volume-density ratio also tending to `1`?

The concrete local gate is now to construct, on each normalized pentagon, a piecewise-smooth transition across a fixed-height band that simultaneously:

1. agrees with PF-122 on the upper cusp strip;
2. agrees with PF-121-type maps on the lower Lambert pieces while preserving PF-124's fixed finite-cuff traces;
3. induces one identical trace on the artificial split ray from the left and right pieces;
4. has bilipschitz constant tending to `1` uniformly over all possible neighboring gap ratios.

PF-124 shows that once one such pentagon map exists, reflection gives the second half of each pant and the finite-cuff maps glue exactly under the zero-twist marking. If the resulting global map satisfies the displayed metric/density convergence, PF-123 supplies **compact relative resolvent/equality of essential spectra** with no further integrability hypothesis. First-resolvent trace class remains a separate, already negative gate by PF-112.

## Why it may matter

This is now a sharp adversarial test of whether any prime-specific information survives in the essential spectral class of the exact flute. A positive global asymptotic-equivalence construction, combined with PF-123, would show that an explicit surface built only from composites has the same essential Laplace spectrum and compact relative resolvent under the natural bounded identification, eliminating essential-spectrum data as a primality/RH selector for this construction.

A negative result would be equally informative, but it can no longer be blamed on raw cuff divergence, local closed-word lengths, collar geometry, Lambert collapse, a scalar cusp offset, independent Busemann gauges, extreme cusp split ratios, finite-cuff parametrization, zero-twist accumulation, or a hidden operator-theoretic summability requirement. It would have to expose a genuine bounded-height split-ray/Jacobian obstruction or a nonlocal infinite-surface amplification mechanism.

## Decisive test

A positive resolution must:

1. construct the bounded-height split-ray transition above with a tail bilipschitz constant `K_n->1`, preserving the PF-124 cuff traces;
2. reflect the pentagon maps and use PF-124's exact commuting cuff square to obtain a complete zero-twist global homeomorphism;
3. verify uniform metric equivalence plus pointwise metric-norm and volume-density ratios tending to `1` at infinity;
4. invoke PF-123's audited Georgescu--Golénia bridge to obtain compact relative resolvent/equality of essential spectra.

A decisive negative resolution must identify an invariant lower bound that survives PF-121, PF-122, and PF-124: for example, prove that every bounded-height transition with the required split trace and fixed cuff traces pays a positive bilipschitz or quasiconformal cost along an escaping sequence, or construct a weakly-null/Weyl sequence showing that no common-manifold metric perturbation tending to zero can realize the marked clone.

Do not use failure of `S_1` for the first resolvent as such a negative test: PF-112 proves that failure locally for every non-isometric smooth metric perturbation, even when compactness holds. Higher Schatten classes, higher resolvent powers, heat differences, wave/scattering equivalence, and determinants remain separate later gates.

## Evidence boundary

This clue is **not** evidence that the complete prime and shift-clone surfaces are quasiconformally equivalent, strongly equivalent, compact-resolvent perturbations, wave-equivalent, or spectrally equivalent. PF-121 gives the local Lambert maps, PF-122 gives the canonical deep-cusp strip map, and PF-124 proves that their finite-cuff traces can be chosen coherently across the zero-twist chain. The left/right Lambert traces have **not** yet been reconciled on the artificial split ray through the bounded-height transition, so no complete pentagon map and no global metric-density estimate has been established.

The geometric comparison literature remains hypothesis-mismatched rather than decisive: Minsky gives coarse bilipschitz pants/degenerate-hexagon comparisons for bounded additive boundary changes; Wu--Zhang give `1+o(1)` metric-tensor control with prescribed boundary data in a neighboring thick-boundary regime; Saric's asymptotically conformal Fenchel--Nielsen theorem assumes an upper-bounded pants decomposition; and bounded-ideal-triangulation routes are unavailable by PF-110. None of those statements directly supplies the current bounded-height split-ray transition for one cusp and two unbounded cuffs. By contrast, the **operator** implication after such a transition is no longer an open literature bridge: PF-123 audits it directly from Georgescu--Golénia.

## Research disposition

**Accepted and materially narrowed, not resolved.** PF-121 kills the single-Lambert interior obstruction, PF-122 kills the deep-cusp/split-ray amplification, PF-123 removes the downstream compact-resolvent theorem as an independent unknown, and PF-124 kills finite-cuff/zero-twist coherence as a separate gate. The remaining decisive local question is the fixed-height reconciliation of the two Lambert maps on their artificial split ray while retaining `K_n->1`; after that, reflection and cuff gluing are already controlled. First-resolvent trace class remains closed negatively by PF-112.