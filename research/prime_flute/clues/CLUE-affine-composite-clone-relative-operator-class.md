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
---

# Affine composite clone and the relative Laplacian class

## Observation

After the canonical Möbius translation, the exact all-composite clone obtained from `q_n=p_n+1` has sampled endpoint displacement in `ell^1`, uniformly `O(P^-3)` all-span tail cross-ratio/separator distortion, and a natural piecewise-affine boundary matching whose derivative differs from the identity by an `L^1` function with vanishing tail mass. PF-106 explicitly stops short of converting this boundary control into an equivariant comparison of the two quotient surfaces.

PF-107 identifies a nonuniformity in the first intrinsic pants coordinate: for consecutive primes with left endpoint `p`, the matched distinguished cuff lengths satisfy `ell^+ - ell = 2/p + o(1/p)`. Hence the additive cuff defect is `ell^2` but not `ell^1`, even though the sampled endpoint displacement is `ell^1`. At the same time `(ell^+-ell)/ell = O(1/(p log p))`, so the **relative** cuff defect remains summable. The standard collar width has logarithmic relative defect `-1/p+o(1/p)`.

PF-108 and PF-109 remove two possible amplification mechanisms without completing the operator bridge. PF-108 proves exact `ell^1` control of the absolute standard-collar widths and canonical seam/spine distances, summable standard-collar area defects, and an explicit finite unweighted integrated collar distortion. PF-109 proves that every PF-004 canonical multi-gap separator in the tail is matched multiplicatively, with uniform `O(P^-3)` logarithmic length distortion even in the pinching limit. Thus neither the harmonic additive cuff defect nor zero-systole pinching in the canonical separator family currently supplies an obstruction to an asymptotically isometric comparison.

## Research question

Does this canonical marked boundary matching extend to a quasiconformal, asymptotically isometric, or otherwise analytically controlled group-equivariant surface comparison strong enough to imply that a natural relative resolvent, heat semigroup, or scattering difference is compact or belongs to a Schatten class? If not, what exact geometric mechanism prevents such a perturbative conclusion despite the summable endpoint and transverse defects?

## Why it may matter

This is the sharpest current control on the surviving exact prime-flute tail. A positive operator-class theorem would show that even the exact sampled cotangent geometry is perturbative relative to an all-composite surface and would force any arithmetic signal into a narrower relative spectral-shift/phase sector. A negative theorem would be at least as informative: it would exhibit a genuine nonlocal amplification mechanism of the infinite collapsing surface that is invisible in the endpoint, collar, spine, and canonical-separator comparisons.

## Decisive test

Either construct a canonical equivariant common-manifold comparison with tail metric/Jacobian distortion tending to zero and derive a compactness theorem for a specified relative Laplacian, or exhibit a Weyl-sequence/right-limit/energy obstruction proving that such compactness fails for the canonical matching. Schatten, wave, and scattering statements are separate stronger gates and should not be conflated with compact resolvent equivalence.

## Research-watch disposition

**Accepted as a fertile research direction, not as proof of any operator equivalence.** Directed prior-art audits have removed several apparent dead ends and now separate the compact-resolvent gate from the stronger scattering/wave gate.

First, the unbounded prime-flute cuffs are **not by themselves a local obstruction** to a uniform pants comparison. Minsky's Lemma 8.2 in *Bounded geometry for Kleinian groups* (Invent. Math. 146 (2001), 143--192, DOI `10.1007/s002220100163`) states that if corresponding boundary lengths of two hyperbolic pairs of pants differ by at most an absolute constant `C`, then their collar complements admit a `K(C)`-bilipschitz marked comparison; the right-angled-hexagon Lemma 8.3 is uniform in the sizes of the alternating sides and includes cusp limits. This is directly relevant because it shows that the fact that the distinguished prime-flute cuffs are not upper bounded does not automatically kill a piecewise geometric comparison. It does **not** state the asymptotic estimate `K(C)->1` as `C->0`, does not supply the required collar control by itself, and does not imply a global equivariant map or any relative spectral theorem.

Second, the strongest standard infinite-type Fenchel--Nielsen theorem located for asymptotically conformal maps does not close the gap. Šarić, *Fenchel-Nielsen coordinates for asymptotically conformal deformations* (Ann. Acad. Sci. Fenn. Math. 41 (2016), 167--176, DOI `10.5186/aasfm.2016.4112`), assumes an **upper-bounded geodesic pants decomposition**. That hypothesis fails for the distinguished prime-flute decomposition, so its conclusion cannot simply be imported to promote PF-106's summable boundary defect to an asymptotically conformal quotient map.

Third, collapsing injectivity radius is not an automatic operator-theoretic veto once a controlled common-manifold comparison has actually been built. Güneysu--Thalmaier, *Scattering theory without injectivity radius assumptions, and spectral stability for the Ricci flow* (Ann. Inst. Fourier 70 (2020), 437--456, DOI `10.5802/aif.3316`), prove existence and completeness of Laplace wave operators for quasi-isometric complete metrics under an integral metric-deviation criterion with no injectivity-radius lower bound. Under global Ricci lower bounds their criterion can be written using the inverse volume of unit balls as a weight. This remains the appropriate stronger target for wave/scattering equivalence, but it requires a group-equivariant common-manifold identification and the weighted surface integral; PF-108's collar-only unweighted estimate does not verify it.

Fourth, the compact-resolvent target is **strictly easier than the Güneysu--Thalmaier wave target**. Georgescu--Golénia, *Compact perturbations and stability of the essential spectrum of singular differential operators* (J. Operator Theory 59 (2008), 115--155), define two complete Riemannian structures on a common noncompact manifold to be strongly equivalent when they are uniformly equivalent and the pointwise norm-comparison bounds and volume-density ratio tend to `1` at infinity. Their Theorems 8.4--8.5 prove, via compactness of the resolvent difference, that Laplace operators of strongly equivalent complete Riemannian structures have the same essential spectrum. The proof is formulated for locally bounded measurable metrics on a `C^1` manifold and notes the analogous Lipschitz-manifold setting; it does not impose an injectivity-radius lower bound or an `L^1` metric-deviation hypothesis for this compact-resolvent conclusion.

This materially sharpens the clue: **if** the prime/composite pants-and-collar matching can be glued to a global marked map `f` for which `f^*g_+` and `g_E` are uniformly equivalent and their metric and area-density ratios tend uniformly to `1` along the flute end, then compact relative resolvent and equality of essential spectra follow from existing operator theory. One does not first need the weighted Güneysu--Thalmaier integral. This is only a conditional bridge: PF-106--PF-109 do not yet construct such an `f`, and Minsky's published lemma gives a uniform `K(C)` rather than the needed audited tail statement `K_n -> 1` after gluing.

PF-107--PF-109 make the remaining geometric bridge more quantitative. The exact cuff transform amplifies endpoint errors into the nonsummable additive law `ell_n^+-ell_n ~ 2/p_{n-1}`, but the relative cuff defect is summable; the absolute collar/spine and area-weighted collar defects are summable; and canonical separator pinching is preserved multiplicatively. Therefore a future compact-resolvent proof should target **uniform tail metric equivalence**, not an `ell^1` sum of raw cuff circumferences. Conversely, none of these estimates supplies the weakly-null sequence or limit-operator obstruction required to reject the clue.

The surviving research program is therefore precise:

1. build and glue marked tight-pants/collar maps for the exact `p_n -> p_n+1` deformation and prove a global common-manifold comparison with metric and area-density ratios tending uniformly to `1` along the end;
2. if step 1 succeeds, apply Georgescu--Golénia strong equivalence to obtain compact relative resolvent and equality of essential spectra;
3. separately test the stronger Güneysu--Thalmaier weighted metric-deviation criterion for wave operators and absolutely continuous spectral stability, keeping the shrinking/collapsing geometry explicit;
4. only after those gates, ask for Schatten or trace-class resolvent/heat differences and any relative scattering determinant or spectral-shift object;
5. in parallel, search for a weakly-null sequence, a noncanonical closed-curve amplification, gluing obstruction, or another limit-operator mechanism showing that the global tail metric ratio cannot tend to one despite PF-107--PF-109.

No located theorem simultaneously constructs the required global comparison for this unbounded-cuff, infinite-type, exact prime/composite deformation. The clue remains accepted because the local geometric comparison has credible prior art and there is now a theorem-level compact-resolvent payoff with clearly separated hypotheses, while the crucial equivariant/asymptotic-isometry bridge remains genuinely open.

## Evidence boundary

This clue is not evidence that the surfaces are relatively compact, trace-class comparable, wave-equivalent, or spectrally equivalent. PF-105 and PF-106 establish the marked endpoint, cross-ratio, separator, shear, and boundary-interpolation estimates; PF-107 adds the `ell^2 \ ell^1` additive cuff warning with `ell^1` relative cuffs; PF-108 proves summable transverse/collar quantities only on explicitly controlled pieces; and PF-109 removes canonical separator pinching as a relative-length amplification mechanism. Minsky supplies a uniform local pants/hexagon comparison under bounded **absolute boundary-length** differences; Šarić's asymptotically conformal Fenchel--Nielsen theorem has an upper-bounded-pants hypothesis unavailable here; Georgescu--Golénia applies only after a genuine strong equivalence of complete metrics on a common manifold has been established; and Güneysu--Thalmaier requires the stronger weighted metric-deviation hypothesis for wave operators. The required prime-flute quotient-surface bridge remains unproved.
