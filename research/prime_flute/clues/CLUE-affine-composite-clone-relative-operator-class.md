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
---

# Affine composite clone and the relative Laplacian class

## Observation

After the canonical Möbius translation, the exact all-composite clone obtained from `q_n=p_n+1` has sampled endpoint displacement in `ell^1`, uniformly `O(P^-3)` all-span tail cross-ratio/separator distortion, and a natural piecewise-affine boundary matching whose derivative differs from the identity by an `L^1` function with vanishing tail mass. PF-106 explicitly stops short of converting this boundary control into an equivariant comparison of the two quotient surfaces.

PF-107 now identifies a nonuniformity in the first intrinsic pants coordinate: for consecutive primes with left endpoint `p`, the matched distinguished cuff lengths satisfy `ell^+ - ell = 2/p + o(1/p)`. Hence the additive cuff defect is `ell^2` but not `ell^1`, even though the sampled endpoint displacement is `ell^1`. At the same time `(ell^+-ell)/ell = O(1/(p log p))`, so the **relative** cuff defect remains summable. The standard collar width has logarithmic relative defect `-1/p+o(1/p)`. This sharpens the clue rather than resolving it: endpoint summability cannot be used as a linear proxy for pants/collar or operator summability, but asymptotic multiplicative closeness remains viable.

## Research question

Does this canonical marked boundary matching extend to a quasiconformal, asymptotically isometric, or otherwise analytically controlled group-equivariant surface comparison strong enough to imply that a natural relative resolvent, heat semigroup, or scattering difference is compact or belongs to a Schatten class? If not, what exact geometric mechanism prevents such a perturbative conclusion despite the summable endpoint defect?

## Why it may matter

This is the sharpest current control on the surviving exact prime-flute tail. A positive operator-class theorem would show that even the exact sampled cotangent geometry is perturbative relative to an all-composite surface and would force any arithmetic signal into a narrower relative spectral-shift/phase sector. A negative theorem would be at least as informative: it would exhibit a genuine nonlocal amplification mechanism of the infinite collapsing surface that is invisible in the endpoint `ell^1` comparison.

## Decisive test

Either construct a canonical equivariant comparison with quantitative metric/Jacobian control and derive a compactness/Schatten theorem for a specified relative Laplace/scattering object, or exhibit a Weyl-sequence/right-limit/energy obstruction proving that such compactness fails for the canonical matching. The statement must be operator-level; endpoint closeness alone is not enough.

## Research-watch disposition

**Accepted as a fertile research direction, not as proof of any operator equivalence.** A directed prior-art audit removes two apparent dead ends while exposing a sharper missing bridge.

First, the unbounded prime-flute cuffs are **not by themselves a local obstruction** to a uniform pants comparison. Minsky's Lemma 8.2 in *Bounded geometry for Kleinian groups* (Invent. Math. 146 (2001), 143--192, DOI `10.1007/s002220100163`) states that if corresponding boundary lengths of two hyperbolic pairs of pants differ by at most an absolute constant `C`, then their collar complements admit a `K(C)`-bilipschitz marked comparison; the right-angled-hexagon Lemma 8.3 is uniform in the sizes of the alternating sides and includes cusp limits. This is directly relevant because it shows that the fact that the distinguished prime-flute cuffs are not upper bounded does not automatically kill a piecewise geometric comparison. It does **not** state the asymptotic estimate `K(C)->1` as `C->0`, does not supply the required collar control by itself, and does not imply a global equivariant map or any relative spectral theorem.

Second, the strongest standard infinite-type Fenchel--Nielsen theorem located for asymptotically conformal maps does not close the gap. Šarić, *Fenchel-Nielsen coordinates for asymptotically conformal deformations* (Ann. Acad. Sci. Fenn. Math. 41 (2016), 167--176, DOI `10.5186/aasfm.2016.4112`), assumes an **upper-bounded geodesic pants decomposition**. That hypothesis fails for the distinguished prime-flute decomposition, so its conclusion cannot simply be imported to promote PF-106's summable boundary defect to an asymptotically conformal quotient map.

Third, collapsing injectivity radius is not an automatic operator-theoretic veto once a controlled common-manifold comparison has actually been built. Güneysu--Thalmaier, *Scattering theory without injectivity radius assumptions, and spectral stability for the Ricci flow* (Ann. Inst. Fourier 70 (2020), 437--456, DOI `10.5802/aif.3316`), prove existence and completeness of Laplace wave operators for quasi-isometric complete metrics under an integral metric-deviation criterion with no injectivity-radius lower bound. Under global Ricci lower bounds their criterion can be written using the inverse volume of unit balls as a weight. This provides a concrete downstream target for the prime/composite comparison, but it also shows why the `L^1` boundary estimate of PF-106 is insufficient on its own: one still needs a group-equivariant surface identification and a metric deviation satisfying the **weighted surface integral**, especially through the cusp-thin regions. Their theorem concerns wave operators and absolutely continuous spectrum; it does not imply compact or Schatten resolvent difference.

PF-107 makes the missing bridge more quantitative. The exact cuff transform has derivative asymptotic to `-2/h` as the logarithmic mesh `h` tends to zero, and this turns PF-106's summable endpoint defect into the nonsummable additive law `ell_n^+-ell_n ~ 2/p_{n-1}`. Therefore a future Güneysu--Thalmaier or Schatten test must estimate the metric deviation with its actual area/support weights through the pants and collars; summing endpoint errors or raw cuff-length changes is not a valid substitute. Conversely, because the relative cuff defect is summable and the absolute cuff difference tends to zero, PF-107 does not provide the Weyl-sequence or limit-operator obstruction required to reject the clue.

The surviving research program is therefore precise:

1. derive quantitative corresponding-cuff and collar comparison estimates from the exact `p_n -> p_n+1` deformation, using PF-107 rather than endpoint `ell^1` as the intrinsic input;
2. build and glue marked pants maps equivariantly, with tail dilatation/metric deviation tending to zero and explicit control in the cusp collars;
3. test the resulting deviation against a no-injectivity-radius scattering criterion such as Güneysu--Thalmaier, keeping the shrinking geometric support explicit;
4. only after that, ask the stronger compact/Schatten relative-resolvent or heat-kernel question;
5. in parallel, search for a weakly-null sequence or another limit-operator obstruction that would show a nonlocal amplification despite the matched tangent hull and summable endpoint defect.

No located theorem simultaneously covers this unbounded-cuff, infinite-type, exact prime/composite deformation and the required relative Laplacian class. The clue remains accepted because the local geometric comparison has credible prior art and the downstream spectral gate is theorem-level and falsifiable, while the crucial equivariant/integrability bridge remains genuinely open.

## Evidence boundary

This clue is not evidence that the surfaces are relatively compact, trace-class comparable, wave-equivalent, or spectrally equivalent. PF-105 and PF-106 establish the marked endpoint, cross-ratio, separator, shear, and boundary-interpolation estimates; PF-107 adds an intrinsic warning that additive cuff defects are `ell^2 \ ell^1` while relative cuff defects remain `ell^1`. Minsky supplies a uniform local pants/hexagon comparison under bounded **absolute boundary-length** differences; Šarić's asymptotically conformal Fenchel--Nielsen theorem has an upper-bounded-pants hypothesis unavailable here; and Güneysu--Thalmaier applies only after suitable quasi-isometric complete metrics on a common manifold satisfy its integral deviation hypothesis. The required prime-flute quotient-surface bridge remains unproved.
