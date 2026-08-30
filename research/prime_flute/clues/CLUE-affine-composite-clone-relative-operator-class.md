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

PF-118 materially narrows the remaining local geometric gate. For each matched one-cusp pant, the exact arc distance tends to zero in both directions. Alessandrini--Disarlo's finite-type theorem therefore supplies continuous marking-compatible boundary-respecting Lipschitz maps both ways whose optimal Lipschitz constants tend to `1`; in the prime-to-clone direction the logarithmic optimal costs are even summable. Thus **mere existence of asymptotically near-isometric boundary-respecting Lipschitz maps on individual pants is no longer the missing theorem**.

The unresolved step is stronger and more specific. The optimal maps used in PF-118 are not known to be injective, and the cited theorem does not prescribe a common boundary parametrization on each cuff. Consequently PF-118 does not yet give homeomorphisms, bilipschitz common-manifold identifications, or restrictions from adjacent pants that agree after zero-twist gluing. Any surviving obstruction must therefore occur in injectivity/boundary coherence, in the accumulation of the shrinking seam mode under gluing or Dirichlet energy, or in genuinely nonlocal operator behavior.

## Research question

Can the canonical prime/shift-clone matching be realized by **boundary-coherent homeomorphic or bilipschitz pant maps with distortion tending to one**, so that the maps glue to a common-manifold comparison whose metric-norm and volume-density defects vanish at infinity? If not, what exact geometric or energetic mechanism prevents this despite PF-118's two-sided local arc-Lipschitz convergence and the summable controls already established in PF-106--PF-114?

The first operator target remains compactness of a natural relative resolvent, not trace class. PF-112 already proves that under any smooth non-isometric common-manifold identification the first relative resolvent cannot be `S_1` for the generic two-dimensional microlocal reason.

## Why it may matter

This is the sharpest current test of whether the full exact cotangent endpoint geometry is operator-theoretically distinguishable from an explicit all-composite surface. A positive gluing/strong-equivalence theorem would show that the prime-specific sampled deformation is perturbative at the level of essential spectral data. A negative theorem would have to expose a genuine infinite-surface amplification mechanism that is invisible to endpoint displacement, canonical separators, collars, pant-local closed words, returning waves, and even the full local arc metric.

Either outcome is useful: it separates a real global Laplacian effect from coordinate amplification such as the nonsummable additive cuff circumference or relative seam scale.

## Decisive test

A positive resolution must do all of the following:

1. construct, or prove existence of, homeomorphic/bilipschitz maps `P_n -> P_n^+` and inverses with distortion `1+o(1)` on the one-cusp pants despite unbounded finite cuffs;
2. prescribe or control their restrictions to each finite cuff strongly enough that the two adjacent pant maps can be made identical there under the zero-twist marking;
3. glue them to a global homeomorphism and verify uniform metric equivalence plus metric-norm and volume-density ratios tending to `1` on the complete tail, including collars and cusp regions;
4. only then invoke an appropriate operator theorem, for example Georgescu--Golénia strong equivalence, to deduce compact relative resolvent/equality of essential spectra.

A negative resolution should exhibit a specific obstruction: a boundary-coherence modulus that stays away from `1`, a weakly-null/Weyl sequence, a cross-pant energy amplification, or another invariant showing that no such strong-equivalence identification can exist. PF-118 rules out treating the local arc spectrum itself as that obstruction.

Wave/scattering equivalence is a separate stronger test. Güneysu--Thalmaier requires a global weighted metric-deviation integral involving inverse unit-ball volume; PF-108's unweighted collar integral does not verify it. If compactness survives, do not return to `S_1` of the first resolvent: test `S_p`, `p>1`, higher resolvent powers, or heat differences separately before defining determinant/spectral-shift objects.

## Evidence boundary

This clue is not evidence that the two complete surfaces are quasiconformally equivalent, asymptotically isometric, strongly equivalent, compact-resolvent perturbations, wave-equivalent, or spectrally equivalent. PF-118 proves only a finite-pant statement in the category of continuous boundary-respecting Lipschitz maps; it explicitly stops before injectivity, prescribed cuff parametrizations, gluing, metric-density control, or any operator conclusion.

The closest prior art leaves exactly this gap:

- Minsky gives uniform finite bilipschitz control for bounded additive pants-length changes with unbounded cuffs and cusp limits, but the audited statement does not quantify a `K(C) -> 1` modulus as `C -> 0`;
- Bishop gives boundary-affine quasiconformal maps with distortion tending to `1`, but assumes a uniform upper bound on the boundary lengths;
- Buser--Makover--Muetzel--Silhol give boundary-coherent cusp degeneration uniformly in the other two cuff lengths, but perturb the short third boundary rather than the two unbounded finite cuffs;
- Saric's asymptotically conformal Fenchel--Nielsen theorem assumes an upper-bounded pants decomposition, which the distinguished prime-flute decomposition is not;
- Whitney--Saric bounded ideal triangulations cannot supply an alternate bounded-shear chart because PF-110 proves that zero systole obstructs their existence here;
- PF-115--PF-116 show that coarse Gromov hyperbolicity cannot distinguish prime from clone.

No audited theorem located so far combines the four features now required simultaneously:

```text
one cusp per pant
+ unbounded perturbed finite cuffs
+ homeomorphic/bilipschitz distortion -> 1
+ prescribed coherent cuff boundary maps.
```

## Research disposition

**Accepted as an active research direction, not as proof of operator equivalence.** PF-118 resolves the earlier subquestion of whether the matched pants are intrinsically close in the local arc/Lipschitz sense: they are, in both directions. The clue is therefore narrowed to the **homeomorphism + boundary-coherence + global-gluing** bridge and to a possible nonlocal obstruction at that bridge. Compactness remains the first unresolved operator gate; first-resolvent trace class is already closed negatively by PF-112.
