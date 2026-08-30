# Prime-flute research notes

This directory preserves high-signal findings from the exploratory **prime-circle / hyperbolic prime-flute** line so they can be reused later by Mathia, independent review, and Lean formalization.

It is intentionally separate from `experiments/riemann_corpus/`: the frozen Riemann corpus records sourced mathematical literature, while this directory records **our derived observations, candidate theorems, obstructions, and research dead ends** about one particular geometric construction.

Nothing here should silently be treated as a proved result. The strongest custom claims remain research notes until independently checked and, where practical, formalized.

## Geometric convention

For consecutive odd primes `p_n`, write

```text
g_n     = p_{n+1} - p_n
u_n     = cot(pi / p_n)
Delta_n = u_{n+1} - u_n
h_n     = log(u_n / u_{n-1})
```

The zero-twist tight flute is the Fuchsian surface obtained from the increasing endpoint sequence `u_n`. The `p=2` endpoint is degenerate under this coordinate, so formulas involving ratios normally start at `p=3`.

## Evidence labels

- **EXACT-DERIVED** — algebraic/hyperbolic identity derived directly from the explicit generators; intended to be checkable without prime-distribution input.
- **LITERATURE+DERIVED** — combines a published theorem with a new consequence for this construction.
- **NEGATIVE/OBSTRUCTION** — shows that a tempting route loses the prime information or cannot support the hoped-for spectral mechanism.
- **CONJECTURAL** — depends on an unproved prime-statistics model or conjecture.
- **NEEDS-AUDIT** — promising claim from the exploration whose exact hypotheses or source bridge still need independent checking.

These labels describe provenance, not mathematical importance.

## Files

- [`findings/`](findings/) — canonical positive and negative research findings, including derivations, evidence status, prior-art audits, and failure modes.
- [`LEAN_CANDIDATES.md`](LEAN_CANDIDATES.md) — a deliberately small queue of statements worth formalizing first.
- [`SOURCES.md`](SOURCES.md) — literature anchors used by the current notes.
- [`graph/index.md`](graph/index.md) — derived navigation and relation view; it is not a source of mathematical truth.

## Intended reuse

For **Mathia**, the most useful objects are not only successful bridges. Negative results expose reusable conceptual moves: identify a coboundary, detect telescoping, separate intrinsic from imported structure, recognize a universal invariant, or find a degenerating mode that invalidates a spectral analogy.

For **Lean**, priority should go first to finite algebraic/hyperbolic identities. Analytic-number-theory and infinite-surface spectral consequences should be split into a formalizable local lemma plus a clearly named external theorem assumption rather than encoded as an opaque monolith.

## Current high-level picture

The exploration repeatedly separates three regimes:

```text
one-dimensional / local reductions
    -> telescope, universalize, or recover a known prime Dirichlet series
    -> sharp quarter-plane propagation thresholds are not tail invariants:
       a single compact endpoint defect already reproduces them (PF-102)
    -> a full marked primitive-orbit completion cannot keep the selected 1/4 boundary:
       cusp-winding words P_m P_n^k force the universal Re(s)>1/2 barrier (PF-103)

projective multi-gap / tangent data
    -> retain genuinely relational gap information and can drive real spectral effects
    -> but are invariant under global integer dilation p_n -> K p_n
       and therefore have an all-composite clone (PF-099)

exact finite-scale cotangent geometry
    -> breaks that dilation gauge through the nonprojective endpoint defect
    -> first four-point Möbius-invariant correction appears at order P^-4 (PF-082)
    -> but the leading P^-4 normalized local scattering response is reproduced by
       any matched smooth endpoint control x - a/x + O(x^-3) (PF-101)
    -> and the continuous interpolation x -> cot(pi/x) between the sampled primes
       is not intrinsic: beyond-all-orders real-analytic perturbations can agree at
       every prime vertex while changing the continuum differential profile (PF-104)
    -> even using the full exact sampled values, the exact all-composite dilation clone
       V(Kp)/K has uniform tail cross-ratio and separator distortion O(P^-2), while
       the corresponding canonical fan-shear defect is absolutely summable (PF-105)
    -> an even closer all-composite shift clone p -> p+1, normalized by z -> z-1,
       has ell^1 sampled-vertex displacement and uniform all-span O(P^-3)
       cross-ratio/separator distortion (PF-106)
```

The exact cross-ratio of four endpoints remains the cleanest intrinsic bridge from several gaps to an actual separating geodesic. PF-099 sharpens its arithmetic interpretation: **the projective/tangent limit encodes gap shape, not primality specificity**. PF-101 adds a second control: although the exact cotangent geometry breaks the dilation gauge, **a finite asymptotic endpoint jet does not by itself supply a distinguished RH scale**. Matching the `1/x` jet moves the first local direct-scattering distinction from `P^-4` to `P^-6`, and matching further jets can postpone it again.

PF-104 narrows the surviving exact-map escape further. The hyperbolic surface is determined by the sampled endpoint sequence, not by an interpolation of the prime labels between those samples. One may perturb `cot(pi/x)` by a beyond-all-algebraic-orders real-analytic function that vanishes at every integer, hence at every prime, without moving a single orthogonal circle or changing the Fuchsian group. **Pointwise derivatives, Schwarzians, or other off-prime continuum data of the chosen cotangent interpolation are therefore not intrinsic prime-flute spectral data unless the construction is shown to descend to the discrete endpoint/group geometry.** Imposing an exterior-analytic germ can restore uniqueness by the identity theorem, but that regularity is an additional upstream structure rather than something selected by the prime-flute Laplacian.

PF-105 closes a different exact-geometry escape. If the all-composite labels `K p_n` are fed through the same exact endpoint law and the resulting surface is rescaled by the Möbius isometry `z -> z/K`, then **every marked four-point cross-ratio and every PF-004 canonical separator lying in the tail beginning at `P` differs from the prime surface by only `O(P^-2)`, uniformly even for blocks whose span grows with `P`**. The adjacent exact fan-shear difference is in `ell^1`. Thus the exact cotangent defect survives at finite scale but disappears from the full marked tail-equivalence class: pointed/right-limit, tangent-hull, and other continuous asymptotic cross-ratio invariants cannot distinguish the prime surface from this exact all-composite clone. PF-105 does not assert global isospectrality; a surviving mechanism would have to accumulate the vanishing defects nonlocally.

PF-106 makes that remaining boundary stricter. Shifting every odd prime label to `p_n+1` gives only even composites; after the hyperbolic translation `z -> z-1`, the resulting exact endpoint sequence differs from the prime sequence by a positive monotone displacement `d(p_n)=O(p_n^-2)` with `sum_n d(p_n)<infinity`. Its marked secant distortion is uniformly `O(P^-3)` on **every** interval in the tail, regardless of span, and hence so are all PF-004 cross-ratio and canonical-separator defects. The natural piecewise-affine boundary matching even has finite `L^1` derivative defect. This still does not prove compact or trace-class relative Laplacian behavior, but it means that any surviving global mechanism must be sensitive to the organization of an `ell^1`-small exact deformation rather than merely to asymptotic tail geometry.

PF-107--PF-114 refine that shift-clone test rather than converting it into an operator theorem. The additive cuff defect is `ell^2` but not `ell^1`, while relative cuff distortion, collar/seam additive data, area-weighted collar distortion, canonical separators, and the full marked closed-word spectrum inside each individual pant remain strongly controlled. The first relative resolvent nevertheless cannot be trace class for any non-isometric smooth marking for the generic two-dimensional microlocal reason in PF-112. PF-114 isolates the first nonsummable local relative mode in the cross-cuff seam, but leaves open whether shrinking support makes it harmless for compactness or scattering.

PF-115 and PF-116 close a separate coarse-geometric escape. Bounded perturbation of the train cuff coordinates first shows that the prime flute and the all-composite shift clone have the same Gromov-hyperbolicity class. Applying the full Portilla--Rodríguez--Tourís train criterion together with the exact cuff law and the unconditional Baker--Harman--Pintz gap envelope then determines that class: **both surfaces are not Gromov hyperbolic in their intrinsic Poincaré metrics**. Thus coarse Gromov-hyperbolicity or Gromov-boundary structure cannot supply the missing prime-specific RH mechanism. This does not settle the finer relative-Laplacian comparison.

PF-102 sharpens a different branch. The common `Re s=1/4` boundary of the selected all-block relative Ruelle sector and the direct cusp-scattering kernel does not require prime gaps, the cotangent tail, or even an infinite family of geometric defects: **one compactly supported endpoint perturbation on an otherwise regular flute already produces the same sharp boundary by propagation along arbitrarily long one-dimensional channels**. PF-103 closes the most natural completion escape: a faithful marked full primitive-orbit Ruelle/Selberg product must also contain primitive cusp-winding classes `P_m P_n^k`; their lengths are `2 log k + O(1)`, and a nontrivial exact/reference cusp coefficient leaves relative factors of size `k^{-2s}`. Thus **the full completion necessarily restores the universal `Re s>1/2` parabolic barrier**, the orbit-side counterpart of PF-015, rather than promoting the selected `1/4` boundary to a natural full dynamical invariant.

Any viable exact-geometry mechanism must therefore use information beyond universal cusp/propagation thresholds and beyond fixed finite perturbative jets, and it must be intrinsic to the **entire discrete exact endpoint/Fuchsian data** rather than to an off-prime interpolation of `cot(pi/x)`. PF-105/PF-106 add that merely passing to the asymptotic tail class, or even relying on a mechanism stable under the explicit summable shift-clone deformation, is insufficient: a genuinely global relative-operator effect would have to survive these controls.

The major negative lessons remain that ordinary Selberg/Ruelle products, uniformly expanding Bowen--Series operators, modular/Hecke inheritance, raw global scalar Laplace data, featureless relative backgrounds, universal cusp and quarter-plane propagation thresholds, naive full relative primitive-orbit completions, finite-jet scattering phase scales, off-prime cotangent-interpolation identities, asymptotic exact tail cross-ratio classes, and coarse Gromov-hyperbolicity encounter structural obstructions before they can plausibly encode the Riemann zeros.
