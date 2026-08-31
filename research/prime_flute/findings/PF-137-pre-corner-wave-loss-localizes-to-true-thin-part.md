# PF-137 — pre-corner wave loss localizes to the true thin part

**Status:** `EXACT-DERIVED + NEGATIVE/BOUNDARY`. PF-136 constructs a boundary-coherent correction on the long pre-first-corner Lambert sectors with summable strong-`L^1` metric deviation, but leaves a sharper Güneysu--Thalmaier concern: if one pessimistically replaces the ambient unit-ball volume by the narrow split-strip width `H`, the inverse-volume factor can remove PF-136's area cancellation and leave a term of scale `M_n|c_n|`, whose summability is not known. The present observation removes that quantity as a **standalone geometric obstruction**. On every fixed injectivity-radius-thick part of the prime flute, ambient unit balls have a uniform positive hyperbolic area, so PF-136's unweighted strong-`L^1` estimate automatically implies the required inverse-volume weighted estimate there. Consequently any genuine failure of the wave-weight criterion must be supported where the **ambient surface itself** is Margulis-thin; the small width of an internal Lambert/split chart is irrelevant unless it coincides with true injectivity-radius collapse. This does not prove global wave operators, because noncanonical short-geodesic thin components and their compatibility with the global comparison remain uncontrolled.

## Claim

Let `(X,g)` be the exact prime flute and let `E` be the union of the long pre-first-corner sectors on which PF-136 applies its split-trace correction. After the fixed local smoothing already allowed there, write

\[
h=C^*g
\]

for the corrected metric on `E`, and let `\delta_{g,h}` be the Güneysu--Thalmaier zeroth-order metric deviation. PF-136 proves

\[
\boxed{
\int_E \delta_{g,h}\,d\mu_g<\infty.
}
\tag{1}
\]

Fix any `0<epsilon<1` and define the ambient thick and thin portions of `E` by

\[
E_{\ge\epsilon}:=
\{x\in E:\operatorname{inj}_g(x)\ge\epsilon\},
\qquad
E_{<\epsilon}:=E\setminus E_{\ge\epsilon}.
\tag{2}
\]

Put

\[
r_\epsilon:=\frac12\min\{1,\epsilon\},
\qquad
v_\epsilon:=2\pi(\cosh r_\epsilon-1)>0.
\tag{3}
\]

Then every `x in E_{>=epsilon}` satisfies

\[
\boxed{
\mu_g(B_g(x,1))\ge v_\epsilon.
}
\tag{4}
\]

Hence

\[
\boxed{
\int_{E_{\ge\epsilon}}
\mu_g(B_g(x,1))^{-1}
\delta_{g,h}(x)\,d\mu_g(x)
\le
v_\epsilon^{-1}
\int_E\delta_{g,h}\,d\mu_g
<\infty.
}
\tag{5}
\]

Therefore, if the complete Güneysu--Thalmaier weighted integral for this comparison diverges, then for every fixed sufficiently small `epsilon` its divergent contribution must occur in the **true ambient thin set** `inj_g<epsilon`; it cannot be forced merely by the coordinate narrowing `H_{*,n}(tau)->0` inside PF-136's split half-strips.

Equivalently, the residual estimate

\[
M_n|c_n|
\tag{6}
\]

from the pessimistic substitution `mu(B(x,1)) ~ H` is not an intrinsic necessary cost on the thick part. It becomes relevant only after proving that the points carrying that cost actually lie in an ambient thin component whose unit-ball volume collapses at the corresponding scale.

For `epsilon` below a two-dimensional Margulis constant, the classical thick--thin theorem gives the geometric interpretation: the ambient thin set of a complete hyperbolic surface is a disjoint union of cusp regions and neighborhoods of sufficiently short simple closed geodesics. PF-129 already gives a summable inverse-volume budget for the synchronized cusp family, while PF-128 gives the matching local estimate for standard collars **when** their core lengths are controlled by the PF-109 canonical separator comparison. PF-137 does not extend PF-128 to every possible short simple closed geodesic. Thus the surviving global wave gate is the genuinely thin noncanonical collar sector, plus the smooth global assembly/interface problem.

## 1. Thick ambient geometry gives a uniform unit-ball volume floor

Take `x in E_{>=epsilon}`. By definition of the injectivity radius, the geodesic ball

\[
B_g(x,r_\epsilon)
\]

is embedded. Since the prime flute has constant curvature `-1`, this ball is isometric to a hyperbolic disk of radius `r_epsilon`. Its area is exactly

\[
\mu_g(B_g(x,r_\epsilon))
=
2\pi(\cosh r_\epsilon-1)
=v_\epsilon.
\tag{7}
\]

Because `r_epsilon<=1`,

\[
B_g(x,r_\epsilon)\subset B_g(x,1),
\]

which proves (4). No bounded-geometry theorem, finite-type hypothesis, pants decomposition, or prime-gap estimate enters this step.

Combining (4) with the nonnegative deviation in PF-136 immediately gives (5). Thus the inverse-volume factor is harmless wherever the **ambient injectivity radius** stays above a fixed threshold.

This point is easy to miss in the normalized Lambert coordinates. PF-136 uses an internal half-strip of transverse width `H(\tau)` and the derivative of its correction contains `|q|/H`. The fact that this internal chart is narrow does not imply

\[
\mu_g(B_g(x,1))\asymp H(\tau).
\]

A unit ball is a ball in the complete surface, not in the artificially cut half-strip. It may cross the split ray, the Lambert splice, or another internal chart boundary. On the thick part, equation (4) proves that it must have order-one area regardless of how narrow that chosen coordinate sector becomes.

## 2. The `M_n|c_n|` endpoint is conditional, not intrinsic

PF-136's exact unweighted cancellation is

\[
\frac{|q|}{H}
\times
(H\,dr\,d\tau)
\longrightarrow
|q|\,dr\,d\tau,
\tag{8}
\]

and the resulting total metric mass is summable. The unresolved warning there inserted another factor `1/H` by imagining an ambient unit-ball area of order `H`. That produces

\[
\int\frac{|q(\tau)|}{H(\tau)}d\tau
\tag{9}
\]

and, at the scalar tail scale, the quantity `M_n|c_n|`.

PF-137 identifies the missing hypothesis in that heuristic. On `E_{>=epsilon}`, (4) gives instead

\[
\mu_g(B_g(x,1))^{-1}\le v_\epsilon^{-1},
\tag{10}
\]

so no additional `1/H` factor appears at all. Hence even a sequence with very small chart widths cannot create a weighted divergence there.

The estimate (9) can only be relevant on `E_{<epsilon}`, where actual short loops exist. This distinction is geometric rather than arithmetic:

```text
small split/Lambert chart width
    does not imply
small ambient unit-ball volume

small ambient unit-ball volume
    requires
true injectivity-radius collapse.
```

Thus trying to decide convergence of `sum M_n|c_n|` from consecutive prime-gap estimates is not yet the correct next arithmetic problem. One first has to identify a genuine Margulis-thin component that forces that weight.

## 3. What remains after thick--thin localization

Choose `epsilon` below a Margulis constant for hyperbolic surfaces. The standard thick--thin decomposition says that every component of `inj_g<epsilon` is a cusp component or a collar/tube around a short simple closed geodesic. This theorem is local and applies to complete hyperbolic surfaces; finite topological type is not needed for the elementary localization in (5).

The current prime/shift evidence covers important but not exhaustive parts of that thin geometry:

- PF-129 synchronizes **all cusp ends** through fixed Busemann slabs and proves a summable total inverse-volume wave weight.
- PF-128 proves that a **matched standard collar** has weighted cost `O(|log(L_+/L)|)`, and PF-109 makes this `O(P^-3)` for the PF-004 canonical separator family, even under pinching.
- PF-109 explicitly does not control every simple closed curve on the infinite flute. A short geodesic outside the canonical PF-004 family can therefore create a thin collar not yet covered by the matched-collar argument.

Consequently PF-137 does **not** complete the wave-operator clue. It removes only the false alternative in which the long pre-corner *coordinate width by itself* is treated as an ambient thinness invariant. A global proof still needs either:

1. a matched comparison for every short-geodesic Margulis collar intersecting the support of the correction, with summable weighted costs; or
2. a different global construction whose support avoids or is exactly isometric on the unresolved thin components;

and in either case the local maps must be assembled smoothly into one complete quasi-isometric marking satisfying the hypotheses of Güneysu--Thalmaier.

## 4. Adversarial stress tests

The statement survives the following failure modes.

**A narrow chart inside a thick region.** Let `H->0` only because an internal split is chosen close to another chart boundary. Equation (4) is unchanged: the ambient ball crosses that internal boundary and retains a fixed area floor. The proposed `1/H` wave penalty is then a coordinate artifact.

**A genuinely short noncanonical geodesic crossing the region.** Here `inj_g` can be small and (5) deliberately gives no bound on that portion. This does not refute PF-137; it identifies exactly the surviving thin component that must be controlled separately.

**A cusp entering the pre-corner support.** Again the point lies in the true thin set. PF-137 only localizes the issue; PF-129 is the separate result that supplies the summable cusp normalization.

**Target rather than source ball volumes.** The Güneysu--Thalmaier lower-Ricci corollary used in this line requires the weighted integrability condition for one of the two complete quasi-isometric metrics. Equation (5) uses the prime metric `g`, so no comparison between the source and target thick--thin decompositions is needed for this localization step.

**Finite head or smoothing.** A finite head has finite contribution under any fixed smooth quasi-isometric comparison on the relevant compact-height pieces. The PF-136 smoothing is local and preserves (1), so it does not affect (5).

## 5. Prior art and novelty audit

No novelty is claimed for the injectivity-radius definition, the hyperbolic disk-area formula, or the thick--thin/Margulis decomposition. The external scattering target remains B. Güneysu and A. Thalmaier, *Scattering theory without injectivity radius assumptions, and spectral stability for the Ricci flow*, Ann. Inst. Fourier 70 (2020), 437--456, DOI `10.5802/aif.3316`, already audited as S16. Their result is precisely why the ambient unit-ball volume, rather than the width of an internal coordinate strip, is the relevant weight.

For standard thick--thin background, Bruno Martelli, *An Introduction to Geometric Topology*, Chapter 4, gives the Margulis decomposition for complete hyperbolic manifolds and in dimension two identifies the thin components as truncated cusps and neighborhoods of short closed geodesics; arXiv:1610.02592. Directed checks found this standard geometry and the Güneysu--Thalmaier criterion, but no theorem that turns PF-136's particular Lambert split width into an ambient injectivity-radius estimate.

The durable Mathia content is therefore a project-specific **negative localization** obtained by composing PF-136's already-proved strong-`L^1` metric budget with the exact thick-part ball-area floor. It closes the tempting but unjustified branch

\[
\boxed{
H_{*,n}\text{ small}
\Longrightarrow
\mu(B(x,1))\asymp H_{*,n}
\Longrightarrow
M_n|c_n|\text{ is the unavoidable wave cost}.}
\tag{11}
\]

The first implication is false without an independent proof of ambient injectivity-radius collapse. No RH mechanism, new general scattering theorem, or wave-equivalence conclusion is claimed.

## 6. Audit / falsification core

A later adversary can check PF-137 through the following finite chain:

1. import only PF-136's proved summability `int_E delta dmu < infinity`;
2. fix `epsilon>0` and restrict to points with `inj_g>=epsilon`;
3. choose `r_epsilon=min(1,epsilon)/2` and use injectivity to identify the radius-`r_epsilon` ball with a disk in `H^2`;
4. compute its exact area `v_epsilon=2pi(cosh(r_epsilon)-1)` and obtain the uniform lower bound for the radius-one ambient ball;
5. multiply PF-136's unweighted integral by the constant `v_epsilon^-1` to prove (5);
6. conclude only that any remaining divergence is supported on the ambient thin part;
7. if the classical thick--thin description is invoked, keep separate the already-controlled cusp/canonical-collar sectors from **all other** short-geodesic collars;
8. do not infer complete wave operators until every thin component and the global smooth assembly are controlled.

A refutation would need a point with `inj_g>=epsilon` whose radius-one ball has arbitrarily small hyperbolic area, or a failure of PF-136's strong-`L^1` input. Producing a divergent noncanonical thin-collar contribution would not refute PF-137; it would identify the remaining obstruction that the finding explicitly isolates.
