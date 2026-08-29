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
---

# Affine composite clone and the relative Laplacian class

## Observation

After the canonical Möbius translation, the exact all-composite clone obtained from `q_n=p_n+1` has sampled endpoint displacement in `ell^1`, uniformly `O(P^-3)` all-span tail cross-ratio/separator distortion, and a natural piecewise-affine boundary matching whose derivative differs from the identity by an `L^1` function with vanishing tail mass. PF-106 explicitly stops short of converting this boundary control into an equivariant comparison of the quotient surfaces.

PF-107 identifies a nonuniformity in the first intrinsic pants coordinate: for consecutive primes with left endpoint `p`, the matched distinguished cuff lengths satisfy `ell^+ - ell = 2/p + o(1/p)`. Hence the additive cuff defect is `ell^2` but not `ell^1`, although the **relative** cuff defect is summable. PF-108 then proves exact `ell^1` control of absolute standard-collar widths and canonical seam/spine distances, summable collar-area defects, and a finite unweighted integrated collar distortion. PF-109 shows that every canonical PF-004 multi-gap separator is matched multiplicatively with uniform `O(P^-3)` logarithmic length distortion even in the pinching limit.

PF-110 materially changes one proposed bridge. Whitney--Šarić bounded ideal triangulations are **not available at all** on the prime flute: their Proposition 4.2 makes every surface with such a triangulation quasiconformal to a zero-shear quotient by a subgroup of `PSL_2(Z)`; integer traces give that quotient a positive systole, and Wolpert's quasiconformal length inequality preserves positivity of the systole. Since the prime flute has primitive geodesics tending to zero, its zero systole is an intrinsic obstruction to every bounded ideal triangulation in their sense. The previously proposed bounded-triangulation/shear route is therefore closed, not merely awaiting a better combinatorial construction.

PF-111 removes a different local amplification route. Thurston's pair-of-pants `Shrinking at the waist` lemma, applied in both directions and then to the common-cusp limit, shows that the **entire nonperipheral marked closed-geodesic spectrum inside each individual tight pant** is distorted by at most the larger of its two relative cuff defects. Because PF-107 makes those logarithmic cuff defects summable, the sequence of pant-local sup marked-length distortions is itself `ell^1`. Arbitrarily complicated words contained in one pant therefore cannot turn the shift-clone deformation into an order-one spectral distinction. Any surviving length/operator obstruction must be cross-pant or genuinely nonlocal.

PF-112 closes the most naive operator-ideal escalation independently of that global tail problem. For any smooth marked common-manifold identification under which the prime and shift-clone metrics are non-isometric, a compactly localized first resolvent difference has classical pseudodifferential order `-2` with nonzero principal symbol in dimension two. Its singular values therefore have the critical `c/j` asymptotics, so the **first resolvent difference can never be trace class `S_1`**. This is a local principal-symbol obstruction: no faster decay of the clone deformation at infinity can repair it. It leaves compactness and global `S_p`, `p>1`, open, and the local trace-class obstruction disappears for higher resolvent powers and fixed-time heat differences.

## Research question

Does the canonical marked prime/composite matching nevertheless extend **directly**, without a Whitney--Šarić bounded triangulation, to a quasiconformal, asymptotically isometric, or otherwise analytically controlled common-manifold comparison strong enough to imply compactness of a natural relative resolvent? If not, what exact nonlocal mechanism prevents such a perturbative conclusion despite the summable endpoint, transverse, area-weighted, canonical-separator, and pant-local marked-length defects?

Compactness remains the first unresolved operator gate. For the first resolvent, PF-112 rules out `S_1` a priori; only weaker global Schatten questions such as `S_p`, `p>1`, remain meaningful there. Higher resolvent powers, relative heat traces, wave operators, and scattering are separate gates and must not be inferred from compact resolvent equivalence.

## Why it may matter

This remains the sharpest current control on the surviving exact prime-flute tail. A positive compactness theorem would show that even the exact sampled cotangent geometry is perturbative relative to an all-composite surface at the level of essential spectral data. A negative theorem would be at least as informative: it would exhibit a genuine amplification mechanism of the infinite collapsing surface that is invisible in the endpoint, collar, spine, canonical-separator, and pant-local marked-length comparisons.

PF-110 improves the research value of the clue by removing a false shortcut. Any positive result now has to confront the actual unbounded-cuff, zero-systole quotient geometry rather than importing a bounded-shear coordinate chart whose existence is impossible here. PF-111 sharpens the adversarial side: a counterexample cannot be obtained merely by taking longer and longer words inside one matched pair of pants. PF-112 sharpens the positive side in a different way: even if a strong-equivalence map exists, an ordinary trace-class determinant built from the **first** relative resolvent is unavailable for generic two-dimensional metric reasons, so any determinant-like continuation must use a different regularization, higher resolvent powers, heat subtraction, or another justified relative object.

## Decisive test

Either construct a canonical equivariant/common-manifold comparison with tail metric and area-density ratios tending uniformly to one and derive compactness for a specified relative Laplacian, or exhibit a Weyl-sequence/right-limit/energy/gluing obstruction proving that such a comparison or compactness conclusion fails for the canonical matching.

If compactness is proved, the next tests must respect PF-112: test `S_p`, `p>1`, for the first resolvent only where meaningful, and separately test whether higher resolvent powers or heat differences satisfy a genuine global trace-class criterion. Do not re-test first-resolvent `S_1` as though it were a tail-summability question.

## Research-watch disposition

**Accepted as a fertile research direction, not as proof of any operator equivalence.** The clue remains accepted after PF-110--PF-112. PF-110 closes the bounded-ideal-triangulation route, PF-111 closes pant-local word amplification, and PF-112 closes first-resolvent trace class, but none decides the direct pants/collar gluing problem or compactness of the relative resolvent.

### Local geometric route that survives

The unbounded prime-flute cuffs are not by themselves a local obstruction. Minsky's Lemma 8.2 in *Bounded geometry for Kleinian groups* (Invent. Math. 146 (2001), 143--192, DOI `10.1007/s002220100163`) states that if corresponding boundary lengths of two hyperbolic pairs of pants differ by at most an absolute constant `C`, then their collar complements admit a `K(C)`-bilipschitz marked comparison; the right-angled-hexagon Lemma 8.3 is uniform in the sizes of the alternating sides and includes cusp limits. This does not itself state the needed audited tail estimate `K_n -> 1`, nor does it glue the local maps globally.

The strongest standard infinite-type Fenchel--Nielsen theorem located for asymptotically conformal maps also does not close the bridge. Šarić, *Fenchel-Nielsen coordinates for asymptotically conformal deformations* (Ann. Acad. Sci. Fenn. Math. 41 (2016), 167--176, DOI `10.5186/aasfm.2016.4112`), assumes an upper-bounded geodesic pants decomposition, unavailable for the distinguished prime-flute decomposition.

PF-107--PF-111 nevertheless make a direct gluing attempt quantitative: the raw additive cuff changes are non-`ell^1`, but relative cuff defects are summable; absolute collar/spine and collar-area defects are summable; canonical separator pinching is preserved multiplicatively; and every pant-local closed word has a summable uniform marked-length defect. A successful proof should therefore target **uniform tail metric equivalence on the complete pants/cusp pieces and compatibility across their glued cuffs**, not `ell^1` summability of raw cuff circumferences or local word-length estimates alone.

### Bounded-triangulation route is now closed

Whitney--Šarić, *Bounded ideal triangulations of infinite Riemann surfaces* (J. London Math. Soc. 112 (2025), e70276, DOI `10.1112/jlms.70276`, arXiv:2502.05590), had appeared to offer a way around the upper-bounded-pants obstruction. PF-110 audits their Proposition 4.2 together with the modular trace floor and Wolpert/Shiga quasiconformal length distortion and proves the stronger obstruction:

```text
bounded ideal triangulation
    => quasiconformal to zero-shear PSL_2(Z) subgroup quotient
    => positive systole
    => impossible for the zero-systole prime flute.
```

Accordingly, no effort should be spent searching for a bounded-valence, bounded-base-shear triangulation of the prime flute. The failure is intrinsic, not a defect of the obvious infinite fan. The Šarić--Wang--Wolfram square-summable diamond-shear theory likewise cannot be reached through this nonexistent bounded triangulation and remains irrelevant unless an independent boundary model is first justified.

### Operator-theoretic gates after a direct common-manifold map

Georgescu--Golénia, *Compact perturbations and stability of the essential spectrum of singular differential operators* (J. Operator Theory 59 (2008), 115--155), define strong equivalence for complete Riemannian structures on a common noncompact manifold via uniform metric equivalence plus metric-norm and volume-density ratios tending to one at infinity. Their Theorems 8.4--8.5 give compact resolvent difference and equality of essential spectra. This is the appropriate first payoff **if** a direct prime/composite map with those properties can be constructed.

PF-112 supplies a separate local gate that applies after any smooth non-isometric marked identification, regardless of what happens at infinity. The localized first resolvent difference is an order-`-2` classical pseudodifferential operator with nonzero principal symbol, which in dimension two sits at the weak trace-class threshold rather than in `S_1`. Thus strong equivalence could still imply compactness, but it cannot upgrade the first relative resolvent to trace class. Global `S_p`, `p>1`, remains possible in principle; higher resolvent powers and heat differences are locally trace-class-compatible and therefore require separate global tail analysis.

Güneysu--Thalmaier, *Scattering theory without injectivity radius assumptions, and spectral stability for the Ricci flow* (Ann. Inst. Fourier 70 (2020), 437--456, DOI `10.5802/aif.3316`), provide a stronger wave/scattering gate for quasi-isometric complete metrics under an integral metric-deviation criterion with a unit-ball-volume weight. PF-108's collar-only unweighted integral does not verify that condition. Collapsing injectivity radius is therefore not an automatic operator veto, but it makes the weighted global estimate a separate problem.

## Surviving research program

1. Construct and glue explicit marked tight-pants, collar, and cusp-region maps for the exact `p_n -> p_n+1` deformation, and prove or disprove that their metric and area-density ratios tend uniformly to one along the end. Audit the `K(C)->1` dependence needed from the local hexagon/pants maps rather than assuming it from Minsky's qualitative uniform lemma.
2. If strong equivalence in the Georgescu--Golénia sense is obtained, derive compact relative resolvent and equality of essential spectra. Keep this conclusion separate from every Schatten or relative-trace claim.
3. Separately test the stronger Güneysu--Thalmaier weighted metric-deviation integral for wave operators and absolutely continuous spectral stability, with special attention to the collapsing unit-ball volumes.
4. Do **not** pursue `S_1` of the first relative resolvent: PF-112 rules it out locally. If compactness survives, test whether the first relative resolvent lies in some global `S_p`, `p>1`; independently test higher resolvent powers or heat differences for trace-class behavior before defining any relative determinant or spectral-shift object.
5. In parallel, search for a weakly-null sequence, a **cross-pant** closed-curve/arc amplification, a pants/cusp gluing obstruction, or another limit-operator mechanism showing that global tail metric equivalence fails despite PF-107--PF-111.

No located theorem simultaneously constructs the required direct comparison for this zero-systole, unbounded-cuff, infinite-type exact prime/composite deformation. The clue therefore remains accepted, but its viable path is narrower and more explicit after PF-110--PF-112.

## Evidence boundary

This clue is not evidence that the surfaces have compact relative resolvent, belong to any global Schatten perturbation class, are wave-equivalent, or are spectrally equivalent. PF-105 and PF-106 establish endpoint, cross-ratio, separator, shear, and boundary-interpolation estimates; PF-107 gives the `ell^2 \ ell^1` additive cuff warning with `ell^1` relative cuffs; PF-108 proves summable transverse/collar quantities only on explicitly controlled pieces; PF-109 removes canonical separator pinching as a relative-length amplification mechanism; PF-110 **rules out**, rather than supplies, the Whitney--Šarić bounded-triangulation bridge; PF-111 controls all nonperipheral marked closed words **inside each individual pant** but not cross-pant geodesics or the gluing maps themselves; and PF-112 proves only the negative local statement that the first resolvent difference of non-identical smooth metrics is not trace class in dimension two. Minsky supplies only local pants/hexagon comparison; Georgescu--Golénia applies only after a genuine strong equivalence of complete metrics on a common manifold has been established; and Güneysu--Thalmaier requires the stronger weighted metric-deviation hypothesis for wave operators. The required prime-flute quotient-surface bridge remains unproved.
