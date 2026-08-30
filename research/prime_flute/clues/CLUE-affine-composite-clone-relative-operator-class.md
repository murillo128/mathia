---
id: CLUE-prime-flute-affine-composite-clone-relative-operator-class
type: research-clue
status: accepted
origin: mind
target_line: prime_flute
based_on:
  - research/prime_flute/findings/PF-105-exact-composite-clone-is-uniformly-tail-cross-ratio-equivalent.md
  - research/prime_flute/findings/PF-106-affine-composite-clone-is-l1-close.md
  - research/prime_flute/findings/PF-107-shift-clone-cuff-defect-is-l2-not-l1.md
  - research/prime_flute/findings/PF-108-shift-clone-collar-and-spine-defects-are-summable.md
  - research/prime_flute/findings/PF-109-shift-clone-preserves-canonical-separator-pinching-multiplicatively.md
  - research/prime_flute/findings/PF-110-zero-systole-obstructs-bounded-ideal-triangulations.md
  - research/prime_flute/findings/PF-111-shift-clone-has-summable-pant-local-marked-length-distortion.md
  - research/prime_flute/findings/PF-112-first-relative-resolvent-is-not-trace-class.md
  - research/prime_flute/findings/PF-113-relative-generator-right-limits-are-parabolic-gauge-data.md
  - research/prime_flute/findings/PF-114-shift-clone-pant-waves-telescope-but-seam-relative-mode-does-not.md
  - research/prime_flute/findings/PF-115-all-composite-shift-clone-has-the-same-gromov-hyperbolicity-class.md
  - research/prime_flute/findings/PF-116-prime-flute-is-not-gromov-hyperbolic.md
  - research/prime_flute/findings/PF-118-shift-clone-pants-are-arc-lipschitz-close.md
---

# Affine composite clone and the relative Laplacian class

## Observation

After the canonical Möbius translation, the all-composite shift clone `p_n -> p_n+1` is extremely close to the exact prime flute in every local or tail quantity so far tested. PF-106 gives `ell^1` sampled-endpoint displacement and uniform `O(P^-3)` all-span tail cross-ratio/separator distortion. PF-107--PF-109 give summable relative cuff distortion, summable absolute collar/spine and area-weighted defects, and multiplicative control of every canonical PF-004 separator. PF-111 removes amplification by the complete marked closed-word spectrum inside one pant, while PF-114 isolates the only presently exposed nonsummable local relative mode: the shrinking cross-cuff seam has

```text
log(S_n^+/S_n) = -1/p_n + o(1/p_n),
```

although its additive defect is summable.

PF-118 materially narrows the remaining local geometric gate. For each matched one-cusp pant, the exact arc distance tends to zero in both directions. Alessandrini--Disarlo's finite-type theorem therefore supplies continuous marking-compatible boundary-respecting Lipschitz maps both ways whose optimal Lipschitz constants tend to `1`; in the prime-to-clone direction the logarithmic optimal costs are even summable. Those optimal maps are not known to be injective or to prescribe a common cuff parametrization.

A closer prior-art audit removes **bare homeomorphism existence** as the main obstruction, but not the asymptotic near-isometry needed for operators. Minsky's Lemma 8.2 gives a homeomorphism between hyperbolic pairs of pants whenever corresponding boundary lengths differ by a bounded additive amount, explicitly allowing cusp limits and arbitrarily long finite cuffs. It maps standard collars to standard collars and is uniformly bilipschitz on the collar-trimmed core. However, the theorem provides only a coarse `K(C)` bound: it does not give `K(C) -> 1` as the additive error tends to zero, and its bilipschitz conclusion is stated on the trimmed core rather than the full collars.

Wu--Zhang's 2025 Proposition 8.7/8.18 supplies almost exactly the stronger kind of map desired here in a neighboring regime. If two boundary components are unchanged and each has length at least `2 arcsinh(1)`, while only the third bounded boundary is changed by relative amount `delta`, they construct a piecewise smooth homeomorphism that is the identity on the two unchanged boundaries and satisfies a metric-tensor estimate `1 +/- O(sqrt(delta))`; these maps glue because of the prescribed identity boundary data. Their proof is an explicit Fermi-coordinate pentagon/hexagon construction. It does **not** directly cover the prime-flute pants: in `P(A_n,B_n,0) -> P(A_n^+,B_n^+,0)` the cusp cannot be one of the two unchanged thick boundaries, while treating the cusp as the varied third boundary leaves its length identically zero and does not deform the two long finite cuffs. Thus the local gap is now a precise cusp-degenerate extension problem, not a generic lack of mapping technology.

## Research question

Can the Wu--Zhang Fermi-coordinate construction, or another equally explicit construction, be extended to the matched one-cusp pants

```text
P(A_n,B_n,0) -> P(A_n^+,B_n^+,0)
```

with both finite cuffs varying by the PF-107 asymptotics, so as to obtain boundary-coherent homeomorphic/bilipschitz maps with metric distortion `1+o(1)` and a prescribed normalized-arclength map on each finite cuff? If not, which altitude, modulus, seam, or energy estimate fails specifically in the ideal-vertex limit despite PF-118's two-sided arc-Lipschitz convergence?

If such maps exist and glue under the zero-twist marking, the next question is whether the resulting common-manifold comparison has metric-norm and volume-density defects tending to `1` on the complete tail. Only after that bridge is established should one invoke an operator theorem.

The first operator target remains compactness of a natural relative resolvent, not trace class. PF-112 already proves that under any smooth non-isometric common-manifold identification the first relative resolvent cannot be `S_1` for the generic two-dimensional microlocal reason.

## Why it may matter

This is the sharpest current test of whether the full exact cotangent endpoint geometry is operator-theoretically distinguishable from an explicit all-composite surface. A positive cusp-extension/gluing/strong-equivalence theorem would show that the prime-specific sampled deformation is perturbative at the level of essential spectral data. A negative theorem would have to expose a genuine infinite-surface amplification mechanism that is invisible to endpoint displacement, canonical separators, collars, pant-local closed words, returning waves, and even the full local arc metric.

Either outcome is useful: it separates a real global Laplacian effect from coordinate amplification such as the nonsummable additive cuff circumference or relative seam scale.

## Decisive test

A positive resolution must do all of the following:

1. adapt the Fermi-coordinate or equivalent pant construction to the one-cusp family and prove a full metric-tensor/bilipschitz estimate `1+o(1)` as `n -> infinity`, with constants that remain controlled through the ideal-vertex limit and the simultaneous perturbation of both unbounded finite cuffs;
2. prescribe normalized-arclength restrictions on each finite cuff, or prove an equivalent coherence statement, so that the two adjacent pant maps are identical there under the zero-twist marking;
3. glue the local maps to a global homeomorphism and verify uniform metric equivalence plus metric-norm and volume-density ratios tending to `1` on the complete tail, including collars and cusp regions;
4. only then invoke an appropriate operator theorem, for example Georgescu--Golénia strong equivalence, to deduce compact relative resolvent/equality of essential spectra.

The cheapest negative test is to inspect the Wu--Zhang pentagon/hexagon altitude estimates in the ideal-vertex limit. Their current lower-bound hypothesis on the two fixed sides prevents a direct cusp substitution. If the corresponding Fermi-coordinate Jacobian or altitude control necessarily loses an `O(1)` amount for the PF-107 perturbation, that yields the desired obstruction. Otherwise, carrying the estimate through the cusp limit is the most direct positive route.

A different negative resolution may exhibit a boundary-coherence modulus that stays away from `1`, a weakly-null/Weyl sequence, a cross-pant energy amplification, or another invariant showing that no such strong-equivalence identification can exist. PF-118 rules out treating the local arc spectrum itself as that obstruction.

Wave/scattering equivalence is a separate stronger test. Güneysu--Thalmaier requires a global weighted metric-deviation integral involving inverse unit-ball volume; PF-108's unweighted collar integral does not verify it. If compactness survives, do not return to `S_1` of the first resolvent: test `S_p`, `p>1`, higher resolvent powers, or heat differences separately before defining determinant/spectral-shift objects.

## Evidence boundary

This clue is not evidence that the two complete surfaces are quasiconformally equivalent, asymptotically isometric, strongly equivalent, compact-resolvent perturbations, wave-equivalent, or spectrally equivalent. PF-118 proves only a finite-pant statement in the category of continuous boundary-respecting Lipschitz maps; it explicitly stops before injectivity, prescribed cuff parametrizations, gluing, metric-density control, or any operator conclusion.

The closest prior art now isolates the missing hypothesis quite sharply:

- Minsky gives homeomorphisms for bounded additive pants-length changes with unbounded cuffs and cusp limits, mapping collars correspondingly and with uniform bilipschitz control on the collar-trimmed core, but the audited statement does not quantify a `K(C) -> 1` modulus and does not supply the required full-collar asymptotic metric estimate;
- Wu--Zhang give piecewise smooth homeomorphisms with metric tensor `1 +/- O(sqrt(delta))` and identity data on two unchanged cuffs, and use that identity data to glue maps globally, but require those unchanged cuffs to be uniformly thick and perturb only a bounded third boundary; their theorem therefore misses exactly the one-cusp/two-long-cuff deformation occurring here;
- Bishop gives boundary-affine quasiconformal maps with distortion tending to `1`, but assumes a uniform upper bound on the boundary lengths;
- Buser--Makover--Muetzel--Silhol give boundary-coherent cusp degeneration uniformly in the other two cuff lengths, but perturb the short third boundary rather than the two unbounded finite cuffs;
- Saric's asymptotically conformal Fenchel--Nielsen theorem assumes an upper-bounded pants decomposition, which the distinguished prime-flute decomposition is not;
- Whitney--Saric bounded ideal triangulations cannot supply an alternate bounded-shear chart because PF-110 proves that zero systole obstructs their existence here;
- PF-115--PF-116 show that coarse Gromov hyperbolicity cannot distinguish prime from clone.

No audited theorem located so far combines the four features now required simultaneously:

```text
one cusp per pant
+ two simultaneously perturbed unbounded finite cuffs
+ homeomorphic/bilipschitz metric distortion -> 1
+ prescribed coherent cuff boundary maps.
```

This is a theorem-hypothesis gap, not a novelty claim that such a cusp extension would be new.

## Research disposition

**Accepted as an active research direction, not as proof of operator equivalence.** The prior-art audit removes bare homeomorphism existence as the decisive issue and narrows the local bridge to a specific extension of near-isometric, boundary-coherent pant maps through one ideal vertex while both long finite cuffs move. Wu--Zhang supplies the closest constructive template; Minsky shows that cusp limits and unbounded cuffs are not by themselves topological obstructions. The clue remains unresolved until that cusp-extension estimate is proved or a concrete failure mechanism is exhibited. Compactness remains the first unresolved operator gate; first-resolvent trace class is already closed negatively by PF-112.
