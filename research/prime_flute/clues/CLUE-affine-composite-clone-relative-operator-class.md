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
  - research/prime_flute/findings/PF-119-canonical-cusp-split-gluing-offset-has-summable-shift-clone-defect.md
---

# Affine composite clone and the relative Laplacian class

## Observation

After the canonical Möbius translation, the all-composite shift clone `p_n -> p_n+1` is extremely close to the exact prime flute in every local or tail quantity so far tested. PF-106 gives `ell^1` sampled-endpoint displacement and uniform `O(P^-3)` all-span tail cross-ratio/separator distortion. PF-107--PF-109 give summable relative cuff distortion, summable absolute collar/spine and area-weighted defects, and multiplicative control of every canonical PF-004 separator. PF-111 removes amplification by the complete marked closed-word spectrum inside one pant, while PF-114 isolates the only presently exposed nonsummable local relative mode: the shrinking cross-cuff seam has

```text
log(S_n^+/S_n) = -1/p_n + o(1/p_n),
```

although its additive defect is summable.

PF-118 materially narrows the remaining local geometric gate. For each matched one-cusp pant, the exact arc distance tends to zero in both directions. Alessandrini--Disarlo's finite-type theorem therefore supplies continuous marking-compatible boundary-respecting Lipschitz maps both ways whose optimal Lipschitz constants tend to `1`; in the prime-to-clone direction the logarithmic optimal costs are even summable. Those optimal maps are not known to be injective or to prescribe a common cuff parametrization.

PF-119 removes a more specific candidate obstruction at the cusp-gluing level. A canonical half-pant normalization splits `P(2a,2b,0)` into two one-parameter ideal Lambert quadrilaterals `Q(a)` and `Q(b)`. Their relative cusp placement is the exact horocyclic split ratio

```text
Theta(a,b) = cosh(a) / cosh(b).
```

For the prime/shift-clone pair, the **single-quadrilateral chart-scale defect** remains of reciprocal-prime size and is not `ell^1`, but the actual adjacent cusp-split offset is its first difference and PF-119 proves

```text
sum_n |sigma_n^+ - sigma_n| < infinity.
```

Thus the nonsummable seam/common scale does not by itself create a nonsummable scalar cusp-gluing offset. Any surviving local obstruction must live in the metric/Jacobian behavior of the one-parameter quadrilateral map, in prescribed finite-cuff boundary data, or in a genuinely nonlocal operator effect.

A closer prior-art audit removes **bare homeomorphism existence** as the main obstruction, but not the asymptotic near-isometry needed for operators. Minsky's Lemma 8.2 gives a homeomorphism between hyperbolic pairs of pants whenever corresponding boundary lengths differ by a bounded additive amount, explicitly allowing cusp limits and arbitrarily long finite cuffs. It maps standard collars to standard collars and is uniformly bilipschitz on the collar-trimmed core. However, the theorem provides only a coarse `K(C)` bound: it does not give `K(C) -> 1` as the additive error tends to zero, and its bilipschitz conclusion is stated on the trimmed core rather than the full collars.

Wu--Zhang's 2025 Proposition 8.7/8.18 supplies almost exactly the stronger kind of map desired here in a neighboring regime. If two boundary components are unchanged and each has length at least `2 arcsinh(1)`, while only the third bounded boundary is changed by relative amount `delta`, they construct a piecewise smooth homeomorphism that is the identity on the two unchanged boundaries and satisfies a metric-tensor estimate `1 +/- O(sqrt(delta))`; these maps glue because of the prescribed identity boundary data. Their proof is an explicit Fermi-coordinate pentagon/hexagon construction. It does **not** directly cover the prime-flute pants: in `P(A_n,B_n,0) -> P(A_n^+,B_n^+,0)` the cusp cannot be one of the two unchanged thick boundaries, while treating the cusp as the varied third boundary leaves its length identically zero and does not deform the two long finite cuffs.

PF-119 shows that one need not attack that two-cuff cusp degeneration as an indivisible three-parameter problem. The exact half-pant factorization reduces the unresolved local bridge to a one-parameter map on `Q(a)` plus an already-controlled scalar interface offset.

## Research question

Can one construct piecewise smooth homeomorphisms

```text
Q(a_n) -> Q(a_n^+)
```

for the PF-119 canonical ideal Lambert quadrilaterals such that:

1. the metric tensor/bilipschitz distortion is `1+o(1)` uniformly as `a_n -> infinity`;
2. the finite-cuff side is mapped by normalized arclength, or by another boundary parametrization that is identical when the two adjacent pants are glued with zero twist;
3. the central vertical boundary map is compatible with the PF-119 cusp-chart scaling, so that the two quadrilateral maps assemble into a one-cusp pant homeomorphism without reintroducing an uncontrolled offset?

The exact model is unusually rigid:

```text
Q(a):
  vertical sides x=0,1
  cuff circle      |z|   = tanh(a)
  interface circle |z-1| = sech(a).
```

For the shift clone `a_n^+-a_n -> 0`; the outer radius `tanh(a)` changes only exponentially in `a`, while the small interface radius `sech(a)` changes multiplicatively by a factor tending to `1`. PF-119 proves that the relative translation needed when the `Q(a_n)` and `Q(a_{n+1})` charts are reassembled has summable defect. This makes an explicit Fermi-coordinate or patched-local-isometry construction the cheapest positive test.

If the quadrilateral maps can be built and doubled/assembled pantwise, the next question is whether the resulting complete-flute homeomorphism has metric-norm and volume-density defects tending to `1` on the whole tail. Only after that bridge is established should one invoke an operator theorem.

The first operator target remains compactness of a natural relative resolvent, not trace class. PF-112 already proves that under any smooth non-isometric common-manifold identification the first relative resolvent cannot be `S_1` for the generic two-dimensional microlocal reason.

## Why it may matter

This is the sharpest current test of whether the full exact cotangent endpoint geometry is operator-theoretically distinguishable from an explicit all-composite surface. A positive quadrilateral/pant/gluing/strong-equivalence theorem would show that the prime-specific sampled deformation is perturbative at the level of essential spectral data. A negative theorem would have to expose a genuine infinite-surface amplification mechanism that is invisible to endpoint displacement, canonical separators, collars, pant-local closed words, returning waves, the full local arc metric, and now also the canonical scalar cusp-split offset.

Either outcome is useful: it separates a real global Laplacian effect from coordinate amplification such as the nonsummable additive cuff circumference or relative seam scale.

## Decisive test

A positive resolution must do all of the following:

1. construct the one-parameter maps `Q(a_n) -> Q(a_n^+)` and inverses with a full metric-tensor/bilipschitz estimate `1+o(1)` whose constants remain controlled through the ideal vertex and the collapsing `sech(a_n)` interface circle;
2. prescribe normalized-arclength data on the finite-cuff side and compatible data on the central vertical, then use PF-119's summable cusp-offset defect to assemble the two quadrilaterals and their doubles into boundary-coherent one-cusp pant maps;
3. glue the pant maps to a global homeomorphism and verify uniform metric equivalence plus metric-norm and volume-density ratios tending to `1` on the complete tail, including collars and cusp regions;
4. only then invoke an appropriate operator theorem, for example Georgescu--Golénia strong equivalence, to deduce compact relative resolvent/equality of essential spectra.

The cheapest negative test is now internal to `Q(a)`: prove that every homeomorphism with the required finite-cuff and central-vertical boundary data has an `O(1)` lower bound on its metric-tensor or quasiconformal distortion even when `|a_n^+-a_n| -> 0`. A failure specifically in the Fermi-coordinate Jacobian, the collapsing interface circle, or the energy of the prescribed boundary interpolation would give the desired obstruction. PF-119 rules out blaming a nonsummable scalar relative cusp translation alone.

A different negative resolution may exhibit a weakly-null/Weyl sequence, a cross-pant energy amplification, or another invariant showing that no strong-equivalence identification can exist. PF-118 rules out treating the local arc spectrum itself as that obstruction.

Wave/scattering equivalence is a separate stronger test. Güneysu--Thalmaier requires a global weighted metric-deviation integral involving inverse unit-ball volume; PF-108's unweighted collar integral does not verify it. If compactness survives, do not return to `S_1` of the first resolvent: test `S_p`, `p>1`, higher resolvent powers, or heat differences separately before defining determinant/spectral-shift objects.

## Evidence boundary

This clue is not evidence that the two complete surfaces are quasiconformally equivalent, asymptotically isometric, strongly equivalent, compact-resolvent perturbations, wave-equivalent, or spectrally equivalent. PF-118 proves only a finite-pant statement in the category of continuous boundary-respecting Lipschitz maps; it explicitly stops before injectivity, prescribed cuff parametrizations, gluing, metric-density control, or any operator conclusion. PF-119 proves an exact cusp-normalized half-pant factorization and summability of one scalar interface-offset defect; it does **not** construct the required `Q(a)` homeomorphism or control its Jacobian.

The closest prior art now isolates the missing hypothesis quite sharply:

- Minsky gives homeomorphisms for bounded additive pants-length changes with unbounded cuffs and cusp limits, mapping collars correspondingly and with uniform bilipschitz control on the collar-trimmed core, but the audited statement does not quantify a `K(C) -> 1` modulus and does not supply the required full-collar asymptotic metric estimate;
- Wu--Zhang give piecewise smooth homeomorphisms with metric tensor `1 +/- O(sqrt(delta))` and identity data on two unchanged cuffs, and use that identity data to glue maps globally, but require those unchanged cuffs to be uniformly thick and perturb only a bounded third boundary; their theorem therefore misses the one-cusp/two-long-cuff deformation before the PF-119 factorization;
- Bishop gives boundary-affine quasiconformal maps with distortion tending to `1`, but assumes a uniform upper bound on the boundary lengths;
- Buser--Makover--Muetzel--Silhol give boundary-coherent cusp degeneration uniformly in the other two cuff lengths, but perturb the short third boundary rather than the two unbounded finite cuffs;
- Saric's asymptotically conformal Fenchel--Nielsen theorem assumes an upper-bounded pants decomposition, which the distinguished prime-flute decomposition is not;
- Whitney--Saric bounded ideal triangulations cannot supply an alternate bounded-shear chart because PF-110 proves that zero systole obstructs their existence here;
- PF-115--PF-116 show that coarse Gromov hyperbolicity cannot distinguish prime from clone.

No audited theorem located so far directly supplies the remaining one-parameter statement:

```text
canonical ideal Lambert Q(a)
+ a' - a -> 0 with a -> infinity
+ homeomorphic/bilipschitz metric distortion -> 1
+ prescribed finite-cuff and central-vertical boundary maps.
```

This is a theorem-hypothesis gap, not a novelty claim that such a quadrilateral comparison would be new.

## Research disposition

**Accepted as an active research direction, not as proof of operator equivalence.** PF-119 removes the canonical scalar cusp-gluing offset as a source of nonsummable amplification and factorizes the local problem into a one-parameter ideal-quadrilateral comparison. The next local gate is therefore explicit and falsifiable: prove or obstruct a boundary-controlled `1+o(1)` homeomorphic/bilipschitz map on `Q(a)`, then assemble and glue it. Compactness remains the first unresolved operator gate; first-resolvent trace class is already closed negatively by PF-112.
