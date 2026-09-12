# AF-296 — Condition geometry logarithmizes projective margin collapse

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-STRUCTURE`, `ARITHMETIC-FIDELITY`, `TARGET-RELATIVE`, `PROJECTIVE`, `CONDITIONING`, `METRIC-CATEGORY-CHANGE`, `NEGATIVE/OBSTRUCTION`, `NO-NOVELTY-CLAIM`

## Claim

AF-294 leaves one legitimate escape from the uniform-quasisymmetry obstruction: a representation may use scale-dependent metric distortion that becomes singular at the shrinking discriminator scale. AF-295 then identifies the finite-eta normalized zero-count margin exactly as projective distance to the boundary-zero discriminant.

There is a canonical classical construction that does exactly this: the **condition metric** (equivalently, in domain language, the quasihyperbolic metric) obtained by weighting infinitesimal length by reciprocal distance to the bad set.

Let `(X,d)` be a proper geodesic metric space, let `D subset X` be nonempty and closed, and put

\[
r(x):=\operatorname{dist}(x,D),\qquad \Omega:=X\setminus D.
\]

For a rectifiable curve `gamma subset Omega`, define its condition length by

\[
L_{\mathrm{cond}}(\gamma)
:=
\int_\gamma \frac{ds}{r}.
\]

Let `d_cond` be the induced path metric. Then for every `x,y in Omega`,

\[
\boxed{
 d_{\mathrm{cond}}(x,y)
 \ge
 \left|\log\frac{r(y)}{r(x)}\right|.
}
\]

More strongly, if `0<epsilon<r(x)`, then

\[
\boxed{
\operatorname{dist}_{\mathrm{cond}}
\bigl(x,\{y:r(y)=\epsilon\}\bigr)
=
\log\frac{r(x)}{\epsilon}.
}
\]

Thus the discriminant itself is at infinite condition distance. The construction does not make a vanishing ordinary margin nonvanishing while honestly transporting the bad set inside the same controlled metric category. Instead it **changes the metric category so that the bad set becomes an ideal boundary at infinite distance**, and it converts multiplicative loss of ordinary margin into additive logarithmic distance.

For the projective finite-eta zero-count problem of AF-295, write

\[
\Sigma_{\Gamma,N}:=\mathbb P\Delta_{\Gamma,N}
\subset \mathbb P(\mathbb C^N),
\]

and use the Fubini--Study distance. For the eta coefficient ray `x_N=[b^(N)]`, AF-295 gives

\[
r_N
:=
\operatorname{dist}_{\mathrm{FS}}(x_N,\Sigma_{\Gamma,N})
=
\arcsin\delta_{\Gamma,N}(b^{(N)}).
\]

Since AF-291 gives

\[
\delta_{\Gamma,N}(b^{(N)})
\asymp_\Gamma
\frac{1}{\sqrt N\,H_N(\alpha)},
\]

we have

\[
\boxed{
r_N\asymp_\Gamma
\frac{1}{\sqrt N\,H_N(\alpha)}.}
\]

Consequently any uniformly stable projective core

\[
S_c:=\{x:\operatorname{dist}_{\mathrm{FS}}(x,\Sigma_{\Gamma,N})\ge c\},
\qquad c>0,
\]

when nonempty, satisfies

\[
\boxed{
\operatorname{dist}_{\mathrm{cond}}(x_N,S_c)
\ge
\log\frac{c}{r_N}
=
\log\bigl(\sqrt N\,H_N(\alpha)\bigr)+O_\Gamma(1).
}
\]

Thus condition geometry does not erase the eta instability. It re-expresses it as logarithmic recession from every fixed-margin region.

## Exact logarithmic distance theorem

The distance function to a closed set is `1`-Lipschitz:

\[
|r(u)-r(v)|\le d(u,v).
\]

Hence along every absolutely continuous curve `gamma`, for almost every parameter value,

\[
\left|\frac{d}{dt}r(\gamma(t))\right|
\le |\dot\gamma(t)|.
\]

On `Omega`, where `r>0`, this gives

\[
\left|\frac{d}{dt}\log r(\gamma(t))\right|
\le
\frac{|\dot\gamma(t)|}{r(\gamma(t))}.
\]

Integration yields

\[
L_{\mathrm{cond}}(\gamma)
\ge
\left|\log\frac{r(\gamma(1))}{r(\gamma(0))}\right|,
\]

and taking the infimum over curves proves the lower bound for `d_cond`.

The level-set statement is sharp. Properness and closedness imply that for every `x in Omega` there is `z in D` with

\[
d(x,z)=r(x)=:r_0.
\]

Let `sigma:[0,r_0] -> X` be a unit-speed minimizing geodesic from `x` to `z`. For `0<=t<r_0`, the endpoint `z` gives

\[
r(\sigma(t))\le r_0-t.
\]

The `1`-Lipschitz property gives the reverse inequality,

\[
r(\sigma(t))\ge r(x)-d(x,\sigma(t))=r_0-t,
\]

so in fact

\[
r(\sigma(t))=r_0-t.
\]

Choose `t=r_0-epsilon`. The condition length of this geodesic segment is exactly

\[
\int_0^{r_0-\epsilon}\frac{dt}{r_0-t}
=
\log\frac{r_0}{\epsilon}.
\]

The general lower bound shows that no other path to the level set `r=epsilon` can be shorter. This proves the exact formula.

In particular, if `y_j -> D` in the original metric, then `r(y_j)->0` and for every fixed `x in Omega`,

\[
d_{\mathrm{cond}}(x,y_j)\to\infty.
\]

The condition metric has therefore changed a finite-distance failure locus into an infinite-distance boundary.

## Projective zero-count discriminant satisfies the hypotheses

For fixed compact `Gamma`, AF-290 defines

\[
\Delta_{\Gamma,N}
=
\{b\in\mathbb C^N:\exists z\in\Gamma,\ P_b(z)=0\}.
\]

It is closed: the function

\[
b\mapsto \min_{z\in\Gamma}|P_b(z)|
\]

is continuous because evaluation is jointly continuous and `Gamma` is compact, and `Delta_{Gamma,N}` is its zero set. It is also a complex cone, so its nonzero part descends to a closed subset

\[
\Sigma_{\Gamma,N}=\mathbb P\Delta_{\Gamma,N}
\]

of finite-dimensional complex projective space. Fubini--Study projective space is compact and geodesic, so the exact condition-distance theorem applies without smoothness, convexity, or manifold regularity assumptions on `Sigma_{Gamma,N}`.

For sufficiently large `N`, uniform convergence `eta_N -> eta` on the fixed zero-free contour ensures that `x_N` is outside the discriminant. AF-295 supplies the exact ordinary projective margin

\[
r_N
=
\arcsin\delta_{\Gamma,N}(b^{(N)}).
\]

Since `arcsin t ~ t` at zero, AF-291 immediately yields the displayed asymptotic law for `r_N`.

## Eta recession rates in condition geometry

Write

\[
H_N(\alpha)
=
\left(\sum_{n\le N}n^{-2\alpha}\right)^{1/2}.
\]

For any fixed `c>0` and every nonempty stable core `S_c`, the logarithmic lower bound gives

\[
\operatorname{dist}_{\mathrm{cond}}(x_N,S_c)
\ge
\begin{cases}
\frac12\log N+O_\Gamma(1), & \alpha>1/2,\\[1mm]
\frac12\log N+\frac12\log\log N+O_\Gamma(1), & \alpha=1/2,\\[1mm]
(1-\alpha)\log N+O_\Gamma(1), & 0<\alpha<1/2.
\end{cases}
\]

For an RH-relevant contour with left edge

\[
\alpha=\frac12-\varepsilon,
\]

this becomes

\[
\boxed{
\operatorname{dist}_{\mathrm{cond}}(x_N,S_c)
\ge
\left(\frac12+\varepsilon\right)\log N+O_\Gamma(1).
}
\]

So the same power-law collapse previously seen as a tiny Euclidean/Hilbert/projective margin becomes linear growth in `log N` after condition-metric reparameterization.

There is also an exact condition-number interpretation. Put

\[
\kappa(x):=\frac1{r(x)}.
\]

Then

\[
\boxed{
 d_{\mathrm{cond}}(x,y)
 \ge
 |\log\kappa(y)-\log\kappa(x)|.
}
\]

A bounded amount of condition distance can therefore change reciprocal distance-to-failure by at most a multiplicative factor. The metric is naturally adapted to **relative changes of conditioning**, not to making ill-conditioning disappear.

## Why this is not a counterexample to AF-294

AF-294 assumes an injective representation `F:X->Y` that honestly transports the bad set to the finite subset `F(D)` of another metric space and is uniformly quasisymmetric on the relevant source/bad-set triples.

Condition geometry does something categorically different. It is defined only on `X\D` (or, equivalently, treats `D` as an ideal infinite-distance boundary). The bad set is no longer a finite-distance subset of the target metric space. Therefore the hypothesis `D'=F(D)` inside an ordinary target metric space is deliberately abandoned.

This is exactly one of AF-294's allowed escape routes: **leave the controlled metric category**. The construction is mathematically legitimate, but it cannot be advertised as a free nonlinear coordinate repair of the same discriminator-margin problem.

The same point prevents a circular interpretation. The conformal density

\[
\frac1{r(x)}
\]

is built from the target discriminant itself. Near the eta ray its scale is

\[
\frac1{r_N}
\asymp_\Gamma
\sqrt N\,H_N(\alpha).
\]

Thus the metric knows exactly where zero-count failure lies and magnifies geometry according to proximity to that failure set. This is valuable as a conditioning geometry, but it is not an independently derived arithmetic carrier.

## Relation to AF-293

AF-293 showed that a fixed Hilbert geometry can make the eta margin order one only when its SPD condition number reaches

\[
\kappa(G_N)\asymp N H_N(\alpha)^2,
\]

or equivalently when a linear coordinate transform has condition number

\[
\kappa_2(A_N)\asymp \sqrt N H_N(\alpha).
\]

The condition metric has pointwise length density

\[
r_N^{-1}\asymp \sqrt N H_N(\alpha)
\]

at the eta ray, and metric-tensor multiplier `r_N^{-2}` of order `N H_N(alpha)^2`.

These matching scales are informative but should not be conflated. AF-293 measures **anisotropy/relative distortion of one fixed Hilbert metric**, whereas multiplication of a Riemannian metric by a scalar at one point is conformal. The condition metric succeeds in making the discriminant infinitely remote because the conformal factor varies singularly with position and diverges on approach to the target-defined bad set, not because one constant SPD form has become anisotropic.

The correct shared conclusion is narrower: both constructions place the reciprocal raw margin at the scale where geometry must cease to remain uniformly comparable to the canonical projective geometry. AF-293 pays this through growing linear condition number; condition geometry pays it through target-dependent spatial singularity.

## Prior art and novelty assessment

No general novelty is claimed for the condition/quasihyperbolic geometry or for the logarithmic boundary estimate.

- F. W. Gehring and B. P. Palka, **“Quasiconformally Homogeneous Domains,”** *Journal d'Analyse Mathématique* 30 (1976), 172--199, DOI `10.1007/BF02786713`, is foundational prior art for the quasihyperbolic metric. The classical basic estimates include the logarithmic lower bound in terms of distance to the boundary.
- Michael Shub, **“Complexity of Bézout's Theorem VI: Geodesics in the Condition (Number) Metric,”** *Foundations of Computational Mathematics* 9 (2009), 171--178, introduced the condition-metric viewpoint for polynomial-system continuation, with path complexity measured by condition length.
- Carlos Beltrán and Michael Shub, **“Complexity of Bézout's Theorem VII: Distance Estimates in the Condition Metric,”** *Foundations of Computational Mathematics* 9 (2009), 179--195, DOI `10.1007/s10208-007-9018-5`, develops distance estimates in that metric.
- Carlos Beltrán, Jean-Pierre Dedieu, Gregorio Malajovich, and Michael Shub, **“Convexity Properties of the Condition Number,”** *SIAM Journal on Matrix Analysis and Applications* 31 (2010), 1491--1506, DOI `10.1137/080718681`, studies the Riemannian structure obtained by multiplying a base metric by a squared condition factor, including inverse-distance-to-singularity settings.
- Juan G. Criado del Rey, **“Condition Metrics in the Three Classical Spaces,”** arXiv:`1501.04456` (2015), explicitly studies metrics obtained by multiplying a Riemannian metric by inverse squared distance to a submanifold.

The exact equality to a distance level set along a nearest geodesic is an elementary consequence of the classical construction and is not claimed as a new theorem in geometric function theory. The Arithmetic Fidelity contribution is its placement at the AF-291--AF-295 eta frontier: it identifies the canonical scale-dependent metric escape, proves exactly how it transforms the measured collapse, and shows why that escape is a target-aware category change rather than recovered discriminator information.

## Boundaries and failure modes

- The exact level-set equality uses a nearest point and a minimizing geodesic. Proper geodesic spaces provide both. The logarithmic lower bound itself needs much less: only the path-length construction and the `1`-Lipschitz property of distance to `D`.
- No smoothness of `D` is required for the metric-space theorem. Calling the construction a Riemannian metric requires the usual smoothness away from singularities; the path metric remains well defined without it.
- The Fubini--Study and gap margins are not identical: `d_gap=sin d_FS`. AF-295 gives `r_FS=arcsin(delta_gap)`, so they are asymptotically equivalent at the collapsing eta frontier but should not be interchanged at order-one distance.
- Sending the discriminant to infinite distance does not prove zero-count stability under a fixed ordinary perturbation budget. It has changed the perturbation geometry itself.
- A source-defined metric that happens independently to be comparable to this condition metric would be materially different evidence. The comparison must be derived without defining the metric from `Delta_{Gamma,N}`, zeros, or another copy of the target failure set.
- The result has no RH consequence by itself. It classifies a representation/geometry escape and makes the remaining naturalness requirement sharper.

## Consequence for the research frontier

The most canonical answer to AF-294's question “what scale-dependent geometry can repair the shrinking margin?” is now classified. Reciprocal-distance condition geometry can always blow the discriminant out to infinity, and for eta it does so at the exact reciprocal projective-margin scale. But the construction is target-aware by definition.

The live question is therefore narrower than “find a nonlinear or scale-dependent metric.” A useful arithmetic mechanism must produce, from independently justified source structure, a geometry whose distortion near the eta ray is quantitatively comparable to the required condition geometry **without defining that geometry from the zero-count discriminant itself**. Otherwise the apparent stabilization is conditioning language, not preservation of additional arithmetic information.