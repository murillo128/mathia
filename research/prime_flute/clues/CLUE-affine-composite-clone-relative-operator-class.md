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
---

# Affine composite clone and the relative Laplacian class

## Observation

After the canonical Möbius translation, the exact all-composite clone obtained from `q_n=p_n+1` has sampled endpoint displacement in `ell^1`, uniformly `O(P^-3)` all-span tail cross-ratio/separator distortion, and a natural piecewise-affine boundary matching whose derivative differs from the identity by an `L^1` function with vanishing tail mass. PF-106 explicitly stops short of converting this boundary control into an equivariant comparison of the quotient surfaces.

PF-107 identifies a nonuniformity in the first intrinsic pants coordinate: for consecutive primes with left endpoint `p`, the matched distinguished cuff lengths satisfy `ell^+ - ell = 2/p + o(1/p)`. Hence the additive cuff defect is `ell^2` but not `ell^1`, although the **relative** cuff defect is summable. PF-108 then proves exact `ell^1` control of absolute standard-collar widths and canonical seam/spine distances, summable collar-area defects, and a finite unweighted integrated collar distortion. PF-109 shows that every canonical PF-004 multi-gap separator is matched multiplicatively with uniform `O(P^-3)` logarithmic length distortion even in the pinching limit.

PF-110 closes the bounded-ideal-triangulation shortcut: Whitney--Šarić bounded ideal triangulations would force quasiconformal equivalence to a zero-shear quotient by a subgroup of `PSL_2(Z)`, hence a positive systole after the modular trace floor and Wolpert length distortion. The prime flute has zero systole, so no bounded ideal triangulation in that sense exists.

PF-111 removes pant-local word amplification. Thurston's pair-of-pants shrinking lemma, applied in both directions and then to the common-cusp limit, bounds the logarithmic length distortion of every nonperipheral closed word contained in one matched tight pant by the larger relative cuff defect. Those pant-local sup distortions are summable. PF-114 gives the complementary simple-arc split: the two returning waves have summable logarithmic distortion, while the cross-cuff seam retains the common shift mode `log(S_n^+/S_n)=-1/p_n+o(1/p_n)` and is not `ell^1`, despite its **additive** defect being summable. Thus any surviving obstruction must be cross-pant, a gluing/energy amplification of that shrinking seam mode, or genuinely nonlocal.

PF-112 closes the naive first-resolvent trace-class escalation independently of the tail problem. Under any smooth non-isometric common-manifold identification, a compactly localized first resolvent difference is a classical pseudodifferential operator of order `-2` with nonzero principal symbol in dimension two, with singular values at the critical `c/j` scale. Thus first-resolvent `S_1` is impossible even if compactness eventually holds. Global `S_p`, `p>1`, higher resolvent powers, heat differences, wave operators, and scattering remain separate gates.

PF-113 shows that the most obvious fixed-frame generator right-limit mismatch is parabolic gauge data, while its conjugacy-invariant angle mismatch is summable. PF-115 and PF-116 close a coarse-geometric shortcut: the exact prime flute and the all-composite shift clone have the same Gromov-hyperbolicity class, and that common class is **non-hyperbolic**. Coarse Gromov geometry therefore cannot decide the relative-Laplacian question.

## Research question

Does the canonical marked prime/composite matching extend directly to a quasiconformal, asymptotically isometric, or otherwise analytically controlled common-manifold comparison strong enough to imply compactness of a natural relative resolvent? If not, what exact nonlocal mechanism prevents such a conclusion despite the summable endpoint, transverse, area-weighted, canonical-separator, pant-local closed-word, and returning-wave defects?

The only currently exposed nonsummable local relative mode is the shrinking cross-cuff seam scale from PF-114. Compactness remains the first unresolved operator gate. If compactness is proved, PF-112 still forbids using the first resolvent difference as an ordinary trace-class determinant kernel.

## Why it may matter

This is the sharpest current test of whether the surviving exact cotangent tail is operator-theoretically distinguishable from an all-composite surface. A positive compactness theorem would show that the exact sampled prime geometry is perturbative relative to the clone at the level of essential spectral data. A negative theorem would expose a genuine amplification mechanism of the collapsing infinite surface that is invisible in all canonical local comparisons already audited.

## Decisive test

Either construct a canonical common-manifold comparison with tail metric-norm and area-density ratios tending uniformly to one and derive compactness for a specified relative Laplacian, or exhibit a Weyl-sequence/right-limit/energy/gluing obstruction proving that such a comparison or compactness conclusion fails for the canonical matching.

If compactness is proved, the next tests must respect PF-112: test `S_p`, `p>1`, for the first resolvent only where meaningful, and separately test higher resolvent powers or heat differences for trace-class behavior. Do not re-test first-resolvent `S_1` as though it were a tail-summability question.

## Research-watch disposition

**Accepted as a fertile research direction, not as proof of any operator equivalence.** The clue remains accepted after PF-110--PF-116 and the strengthened local-map prior-art audit below. No located theorem presently supplies the missing strong-equivalence map for this zero-systole, unbounded-cuff, one-cusp-per-pant tail.

### Local geometric route that survives

The unbounded cuffs are not by themselves a local bounded-distortion obstruction. Minsky's Lemma 8.2 in *Bounded geometry for Kleinian groups* (Invent. Math. 146 (2001), 143--192, DOI `10.1007/s002220100163`) reduces the pair-of-pants statement to the right-angled-hexagon Lemma 8.3. If corresponding alternating side lengths differ by at most a fixed additive `C`, the complements of the standard collars admit a `K(C)`-bilipschitz marked comparison, uniformly in the absolute side lengths and with cusp limits allowed.

However, a primary-source audit of the proof exposes the exact missing modulus. Minsky states only

```text
for each fixed C > 0, there exists K(C) < infinity.
```

The proof decomposes a hexagon into bands with metric `dx^2 + cosh^2(x) dy^2`, uses affine stretches when the band parameters stay away from zero, and handles small band parameters by passage to boundary cases. This proves a **uniform finite** bilipschitz constant for fixed `C`; it does not state or quantify

```text
K(C) -> 1 as C -> 0.
```

There is also a concrete reason not to extract such a modulus by naively affine-matching every band in Minsky's decomposition. A band parameter can tend to zero in the one-cusp boundary case, and two nearby pants can then have tiny corresponding artificial band widths whose ratio stays order-one away from `1`. An affine map forced to preserve those auxiliary band boundaries would inherit order-one distortion even though the intrinsic pants are becoming close. This is a **decomposition artifact**, not an intrinsic obstruction: a successful small-`C` proof must be allowed to remesh through the boundary case or use intrinsic coordinates rather than preserving all of Minsky's auxiliary bands.

The exact intrinsic seam gives a useful stress test. If a one-cusp pair of pants has finite boundary half-lengths `a,b` and `s` is the orthogeodesic joining them, the classical right-angled-hexagon identity gives

```text
sinh(s/2) = cosh((a-b)/2) / sqrt(sinh(a) sinh(b)).
```

Consequently

```text
d_a log sinh(s/2) = 0.5 tanh((a-b)/2) - 0.5 coth(a),
d_b log sinh(s/2) = -0.5 tanh((a-b)/2) - 0.5 coth(b).
```

Since `d log(s) / d log sinh(s/2) = tanh(s/2)/(s/2) <= 1`, on `a,b >= A > 0` one obtains

```text
|Delta log s| <= (1+coth(A))/2 * (|Delta a|+|Delta b|)
```

along any interpolation staying in that region. The Lipschitz constant tends to `1` as `A -> infinity`. Thus the **true shrinking seam does not amplify an `O(1/p)` additive boundary perturbation into an order-one local distortion**. For the prime/shift clone it gives `|log(s_n^+/s_n)|=O(1/p_n)`, consistent with PF-114. The mode is nonsummable, but it vanishes pointwise; whether global gluing or Dirichlet energy can accumulate it remains the operator question.

A second natural theorem has complementary strength and weakness. Bishop, *Quasiconformal mappings of Y-pieces* (Rev. Mat. Iberoam. 18 (2002), 627--652, DOI `10.4171/RMI/330`), Theorem 1.1, constructs boundary-affine quasiconformal maps and gives `K <= 1 + C(L) epsilon` when the changed boundary-length ratio has logarithm `epsilon`. The boundary-affine property is exactly what one would like for zero-twist gluing. But Bishop assumes every boundary length is bounded above by the same finite `L`; the paper gives no usable growth estimate for `C(L)` as `L -> infinity`. Taking `L=L_n` along the prime-flute cuffs therefore does **not** prove that `C(L_n) epsilon_n -> 0`.

Buser--Makover--Muetzel--Silhol, *Quasiconformal embeddings of Y-pieces* (Comput. Methods Funct. Theory 14 (2014), 431--452, DOI `10.1007/s40315-014-0062-2`, arXiv:1311.0687), supply another useful boundary case. Their Theorem 2.1 maps a Y-piece `Y_{l1,l2,epsilon}` with a short third boundary to a restricted cusp Y-piece `Y^{epsilon*}_{l1,l2}`, `epsilon*=2epsilon/pi`, by a boundary-coherent quasiconformal embedding with

```text
q_phi <= 1 + 2 epsilon^2,
```

and the bound is independent of the other two boundary lengths `l1,l2`. This shows that **cusp degeneration plus unbounded other cuffs is not itself an obstruction to near-conformal, boundary-coherent control**. It still does not solve the prime/clone problem, because the parameter being changed there is the short third boundary, whereas our missing estimate perturbs the two long finite cuffs while keeping the cusp.

The standard infinite-type Fenchel--Nielsen bridge has the same applicability problem in a different form. Šarić, *Fenchel-Nielsen coordinates for asymptotically conformal deformations* (Ann. Acad. Sci. Fenn. Math. 41 (2016), 167--176, DOI `10.5186/aasfm.2016.4112`), assumes an upper-bounded geodesic pants decomposition. That hypothesis fails for the distinguished prime-flute decomposition.

The useful synthesis is therefore precise rather than merely negative:

```text
Minsky:
    arbitrary/unbounded cuff sizes + cusp limits
    but only fixed-C bounded distortion;

Bishop:
    boundary-affine maps + distortion -> 1 for fixed L
    but L-bounded cuffs;

Buser--Makover--Muetzel--Silhol:
    boundary-coherent cusp degeneration + distortion -> 1
    uniformly in the other two cuff lengths
    but does not perturb those long cuffs;

prime/shift-clone tail needs:
    unbounded perturbed cuffs + cusp
    AND boundary-coherent distortion -> 1.
```

This is the exact local theorem that remains to be proved or refuted. It should not be hidden behind a generic appeal to pair-of-pants continuity, nor disproved by forcing a map to preserve auxiliary bands whose widths degenerate.

### Bounded-triangulation and coarse-hyperbolic routes are closed

Whitney--Šarić, *Bounded ideal triangulations of infinite Riemann surfaces* (J. London Math. Soc. 112 (2025), e70276, DOI `10.1112/jlms.70276`, arXiv:2502.05590), cannot provide an alternate coordinate chart here. PF-110 proves

```text
bounded ideal triangulation
    => quasiconformal to zero-shear PSL_2(Z) subgroup quotient
    => positive systole
    => impossible for the zero-systole prime flute.
```

Accordingly, no effort should be spent searching for a bounded-valence, bounded-base-shear triangulation of this surface. The failure is intrinsic, not a defect of the obvious infinite fan.

PF-115--PF-116 likewise show that coarse Gromov hyperbolicity provides no discriminator: prime and shift-clone share the same class and both fail to be Gromov hyperbolic. Any operator distinction must occur below this coarse level.

### Operator-theoretic gates after a direct common-manifold map

Georgescu--Golénia, *Compact perturbations and stability of the essential spectrum of singular differential operators* (J. Operator Theory 59 (2008), 115--155), define strong equivalence for complete Riemannian structures on a common noncompact manifold via uniform metric equivalence plus metric-norm and volume-density ratios tending to one at infinity. Their Theorems 8.4--8.5 yield compact resolvent comparison in the natural identified Hilbert spaces and equality of essential spectra. This is the appropriate first payoff **if** the missing direct prime/composite map is constructed.

Güneysu--Thalmaier, *Scattering theory without injectivity radius assumptions, and spectral stability for the Ricci flow* (Ann. Inst. Fourier 70 (2020), 437--456, DOI `10.5802/aif.3316`), provide a stronger wave/scattering gate for quasi-isometric complete metrics under an integral metric-deviation criterion with a unit-ball-volume weight. PF-108's collar-only unweighted integral does not verify that condition. Collapsing injectivity radius is not an automatic veto, but the weighted global estimate is a separate problem.

PF-112 supplies the operator-ideal boundary after any such map: strong equivalence may imply compactness, but it cannot make the first relative resolvent trace class. Any determinant-like continuation would need a justified higher-resolvent, heat, regularized, or other relative construction.

## Surviving research program

1. Prove or refute a **uniform small-additive pants comparison** for the relevant one-cusp tail: if the two finite boundary lengths differ by `C_n -> 0` while the lengths themselves are unbounded, construct boundary-coherent maps whose metric distortion tends to one uniformly. Quantify the intrinsic right-angled-hexagon/pentagon coordinates directly, and permit remeshing through Minsky's small-band boundary case instead of affine-matching every auxiliary band.
2. Use the exact seam estimate above as a falsification constraint: a proposed local obstruction cannot claim order-one amplification from the true cross-cuff seam itself. Conversely, do not silently replace PF-114's nonsummable `~1/p_n` **relative** seam mode by an `ell^1` budget; any global proof must show why shrinking support or metric/area weighting makes that mode harmless.
3. Glue the local maps across the zero-twist cuffs and verify metric-norm and volume-density ratios on the complete surface, including the cusp and collar regions. Buser--Makover--Muetzel--Silhol supplies evidence that the cusp boundary case can be controlled independently of the long cuff sizes, but not the missing long-cuff perturbation estimate. Do not infer global equivalence from pant-local length control alone.
4. If Georgescu--Golénia strong equivalence is obtained, derive compact relative resolvent and equality of essential spectra. Keep this conclusion separate from Schatten and relative-trace claims.
5. Separately test the Güneysu--Thalmaier weighted metric-deviation integral for wave operators and absolutely continuous spectral stability, with special attention to collapsing unit-ball volumes.
6. Do **not** pursue `S_1` of the first relative resolvent: PF-112 rules it out locally. If compactness survives, test `S_p`, `p>1`, and independently test higher resolvent powers or heat differences for trace-class behavior before defining any relative determinant or spectral-shift object.
7. In parallel, search for a weakly-null sequence, a **cross-pant** closed-curve/arc amplification, a gluing obstruction, or another limit-operator mechanism showing that global tail metric equivalence fails. PF-111, PF-113, and the returning-wave part of PF-114 remove several purely local candidates; PF-115--PF-116 remove the coarse-Gromov candidate.

## Evidence boundary

This clue is not evidence that the surfaces have compact relative resolvent, belong to any global Schatten perturbation class, are wave-equivalent, quasiconformally equivalent, asymptotically isometric, or spectrally equivalent. PF-105--PF-111 establish only the exact endpoint/cross-ratio, cuff-relative, transverse/collar, canonical-separator, and pant-local marked-length controls stated in those findings. PF-112 proves only the negative local statement about first-resolvent trace class. PF-113 removes a fixed-frame generator artifact but not the global operator gate. PF-114 proves a real nonsummable relative seam mode, but that mode tends to zero and its additive defect is summable; the exact seam differential estimate above rules out treating it as an order-one **local** amplification. PF-115--PF-116 show only that coarse Gromov hyperbolicity cannot distinguish prime and clone.

Minsky supplies fixed-`C` local pants/hexagon comparison but no audited `K(C)->1` modulus; Bishop supplies the needed affine-boundary normalization only under an upper cuff bound; Buser--Makover--Muetzel--Silhol supply a near-conformal boundary-coherent **short-boundary-to-cusp** comparison uniform in the other two cuff lengths, not a theorem for perturbing those unbounded cuffs; Šarić's asymptotically conformal Fenchel--Nielsen theorem assumes an upper-bounded pants decomposition; Georgescu--Golénia applies only after genuine strong equivalence is established; and Güneysu--Thalmaier requires a stronger weighted metric-deviation hypothesis for wave operators. The required quotient-surface bridge remains unproved.
