# AF-297 — Radial conformal repairs obey an integrability dichotomy

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-STRUCTURE`, `ARITHMETIC-FIDELITY`, `TARGET-RADIAL`, `CONFORMAL-DENSITY`, `CONDITIONING`, `NEGATIVE/OBSTRUCTION`, `NO-NOVELTY-CLAIM`

## Claim

AF-296 identifies the reciprocal-distance condition metric as one canonical way to turn a shrinking ordinary margin into an infinite-distance boundary. The same calculation extends exactly to **every conformal path metric whose density depends only on ordinary distance to the bad set**, and it gives a sharp dichotomy.

Let `(X,d)` be a proper geodesic metric space, let `D subset X` be nonempty and closed, and put

\[
r(x):=\operatorname{dist}(x,D),\qquad \Omega:=X\setminus D.
\]

Let

\[
\phi:(0,\infty)\to(0,\infty)
\]

be continuous. Give every rectifiable curve `gamma subset Omega` the weighted length

\[
L_\phi(\gamma)
:=
\int_\gamma \phi(r)\,ds,
\]

and let `d_phi` be the induced extended path metric on `Omega`.

Then for every `x in Omega`, with `r_0=r(x)`, and every `0<epsilon<r_0`,

\[
\boxed{
\operatorname{dist}_{\phi}
\bigl(x,\{y:r(y)=\epsilon\}\bigr)
=
\int_\epsilon^{r_0}\phi(t)\,dt.
}
\tag{1}
\]

Consequently the weighted distance from `x` to the bad-set boundary, understood through sequences with `r->0` or through the metric completion when finite, is exactly

\[
\boxed{
\mathfrak m_\phi(x)
=
\int_0^{r(x)}\phi(t)\,dt
\in(0,\infty].
}
\tag{2}
\]

This yields the fixed-profile dichotomy. For any sequence `x_N` with ordinary margins

\[
r_N:=r(x_N)\longrightarrow0,
\]

exactly one of the following occurs:

1. if `phi` is integrable at `0`, then
   \[
   \mathfrak m_\phi(x_N)=\int_0^{r_N}\phi(t)dt\longrightarrow0;
   \]
2. if `phi` is not integrable at `0`, then
   \[
   \mathfrak m_\phi(x_N)=\infty
   \]
   for every `N`.

Therefore an `N`-independent target-radial conformal reweighting cannot turn a vanishing ordinary boundary margin into a finite positive asymptotic margin. **It either preserves margin collapse or removes the bad set to an infinite-distance ideal boundary.**

The power family

\[
\phi_\beta(t)=t^{-\beta}
\]

makes the threshold explicit:

\[
\mathfrak m_{\phi_\beta}(x)
=
\begin{cases}
\dfrac{r(x)^{1-\beta}}{1-\beta}, & \beta<1,\\[2mm]
\infty, & \beta\ge1.
\end{cases}
\tag{3}
\]

Thus the AF-296 quasihyperbolic/condition density `1/r` is the **critical power-law singularity**: it is the first power law that sends the failure set to infinite metric distance. Stronger radial singularities do the same more aggressively; weaker fixed powers leave a shrinking boundary margin shrinking.

There is also a quantitative price for scale-dependent radial repair. Let `phi_N` be positive densities integrable on `(0,r_N)` and suppose the repaired boundary margin is required to satisfy

\[
m_N:=\int_0^{r_N}\phi_N(t)dt\ge c>0.
\]

Then necessarily

\[
\boxed{
\operatorname*{ess\,sup}_{0<t<r_N}\phi_N(t)
\ge
\frac{c}{r_N}.
}
\tag{4}
\]

So any finite-margin radial repair must place conformal density of reciprocal-raw-margin scale somewhere inside the collapsing boundary layer. This lower bound is sharp at the scale level: a density of order `1/r_N` on that layer gives order-one weighted boundary margin.

## Exact radial distance theorem

The distance function `r=dist(.,D)` is `1`-Lipschitz. Let `gamma:[a,b]->Omega` be absolutely continuous and define a primitive

\[
\Phi(u):=\int_{u_*}^{u}\phi(t)dt
\]

for any fixed `u_*>0`. Then `r circ gamma` is absolutely continuous and, almost everywhere,

\[
\left|\frac{d}{ds}r(\gamma(s))\right|
\le |\dot\gamma(s)|.
\]

Hence

\[
\left|\frac{d}{ds}\Phi(r(\gamma(s)))\right|
\le
\phi(r(\gamma(s)))|\dot\gamma(s)|.
\]

If `gamma(a)=x` and `r(gamma(b))=epsilon`, integration gives

\[
L_\phi(\gamma)
\ge
\left|\Phi(r_0)-\Phi(\epsilon)\right|
=
\int_\epsilon^{r_0}\phi(t)dt.
\tag{5}
\]

This proves the lower bound in (1).

Properness and closedness give a nearest point `z in D` with `d(x,z)=r_0`. Let

\[
\sigma:[0,r_0]\to X
\]

be a unit-speed minimizing geodesic from `x` to `z`. Exactly as in AF-296, the `1`-Lipschitz property and the endpoint `z` imply

\[
r(\sigma(s))=r_0-s
\qquad (0\le s<r_0).
\tag{6}
\]

For `s=r_0-epsilon`, the weighted length is therefore

\[
L_\phi(\sigma|_{[0,r_0-\epsilon]})
=
\int_0^{r_0-\epsilon}\phi(r_0-s)ds
=
\int_\epsilon^{r_0}\phi(t)dt.
\tag{7}
\]

This meets the lower bound and proves (1).

Letting `epsilon downarrow0` proves (2). If the integral is finite, the same nearest-point geodesic is Cauchy in `d_phi` near `D`, so it supplies a finite completion boundary point at exactly that distance. If the integral diverges, (5) shows that every sequence whose ordinary distance to `D` tends to zero escapes to infinite `d_phi` distance from every fixed interior point.

No smoothness, convexity, or manifold structure of `D` is needed.

## Eta projective consequence

Apply the theorem to the AF-295 projective zero-count problem. For fixed zero-free contour `Gamma`, let

\[
D_N=\Sigma_{\Gamma,N}
\subset \mathbb P(\mathbb C^N)
\]

be the projectivized boundary-zero discriminant and let

\[
x_N=[b^{(N)}]
\]

be the eta coefficient ray. With Fubini--Study distance, AF-295 gives the exact raw projective margin

\[
r_N
=
\operatorname{dist}_{\mathrm{FS}}(x_N,D_N)
=
\arcsin\delta_{\Gamma,N}(b^{(N)}),
\]

while AF-291 gives

\[
\boxed{
r_N\asymp_\Gamma
\frac{1}{\sqrt N\,H_N(\alpha)}.}
\tag{8}
\]

Therefore every fixed target-radial conformal profile `phi(r)` has only the two outcomes above: finite boundary distance still collapses, or the zero-count discriminant is placed at infinite distance.

For an `N`-dependent radial profile with finite repaired margin `m_N>=c`, (4) and (8) force

\[
\boxed{
\operatorname*{ess\,sup}_{0<t<r_N}\phi_N(t)
\gtrsim_\Gamma
\sqrt N\,H_N(\alpha).
}
\tag{9}
\]

If the conformal path density is induced by a scalar Riemannian rescaling

\[
g_N'=\phi_N(r)^2 g_{\mathrm{FS}},
\]

then somewhere in the collapsing boundary layer the metric-tensor multiplier must satisfy

\[
\boxed{
\operatorname*{ess\,sup}_{0<t<r_N}\phi_N(t)^2
\gtrsim_\Gamma
N H_N(\alpha)^2.
}
\tag{10}
\]

These are exactly the scales already exposed from two different directions: AF-293 requires linear coordinate condition number of order `sqrt(N) H_N(alpha)` (SPD metric condition number of order `N H_N(alpha)^2`) to make the eta projective margin order one, while AF-296's target-defined condition density has pointwise scale `1/r_N asymp sqrt(N)H_N(alpha)` at the eta ray.

For a contour whose left edge is

\[
\alpha=\frac12-\varepsilon,
\qquad \varepsilon>0,
\]

one has

\[
H_N(\alpha)\asymp_\varepsilon N^\varepsilon,
\]

so any finite order-one radial repair must reach at least

\[
\phi_N\gtrsim N^{1/2+\varepsilon}
\]

somewhere in the boundary layer, with scalar metric multiplier at least order

\[
N^{1+2\varepsilon}.
\]

The price is therefore not an artifact of choosing the special density `1/r`. It is forced by the amount of raw projective margin that has to be accumulated by **any** radial conformal path density.

## What this closes and what remains open

AF-294 ruled out uniformly quasisymmetric nonlinear repair with honest finite bad-set transport. AF-295 showed that the natural complex-scaling quotient does not remove the collapse. AF-296 exhibited the target-aware condition metric as a legitimate category-changing escape.

The present result classifies the entire target-radial conformal family around that escape:

- a fixed radial density with finite boundary length cannot stabilize a collapsing margin;
- a fixed density singular enough to stop the collapse sends the failure set to infinite distance;
- a scale-dependent finite-margin repair must concentrate at least reciprocal-margin conformal density inside the shrinking boundary layer.

This sharpens the remaining Arithmetic Fidelity question. A genuinely explanatory source geometry cannot obtain finite stable zero-count margin merely by choosing a nicer fixed function of **target distance to failure**. If it remains radial in that target distance, it must pay the already-known `1/r_N` scale through explicit `N`-dependence. A source-natural escape must instead justify that singular scale independently from arithmetic structure, carry additional information, or leave the target-radial conformal category through anisotropy/nonradial structure.

The theorem does **not** rule out such nonradial or anisotropic geometries, additional markings, new quotient information, or source-derived metrics whose relation to the discriminant is a theorem rather than a definition. It also does not turn the eta truncation into an RH proof. It only removes a broad class of apparent finite-margin repairs that are radial reparameterizations of the already-known target distance.

## Prior art and novelty assessment

No general novelty is claimed for conformal path metrics, quasihyperbolic metrics, or the idea that a singular conformal density can alter metric-boundary behavior.

- F. W. Gehring and B. P. Palka, **“Quasiconformally Homogeneous Domains,”** *Journal d'Analyse Mathématique* 30 (1976), 172--199, DOI `10.1007/BF02786713`. This is foundational prior art for the quasihyperbolic density `1/dist(.,boundary)` and its logarithmic boundary-distance estimates.
- Mario Bonk, Pekka Koskela, and Steffen Rohde, **“Conformal Metrics on the Unit Ball in Euclidean Space,”** *Proceedings of the London Mathematical Society* 77(3) (1998), 635--664, DOI `10.1112/S0024611598000586`. This develops geometric boundary behavior for general positive conformal densities.
- Mario Bonk, Juha Heinonen, and Pekka Koskela, ***Uniformizing Gromov Hyperbolic Spaces***, Astérisque 270 (2001). This is standard metric-space conformal-deformation background.
- Timo Tossavainen, **“A distance estimate on the boundary of a conformal deformation of the unit ball satisfying a Harnack inequality and the Gehring-Hayman property,”** *Annales Academiae Scientiarum Fennicae Mathematica* 35(1) (2010), 175--178, DOI `10.5186/aasfm.2010.3509`. It states the standard conformal path-metric construction explicitly as `length_rho(gamma)=int_gamma rho ds`, followed by path infimization.

Equation (1) is an elementary radial specialization of that classical conformal-deformation framework, using only the `1`-Lipschitz distance function and a nearest geodesic. The integrability dichotomy is its immediate boundary consequence. No novelty is claimed for these facts as general metric geometry.

The Arithmetic Fidelity contribution is their placement at the AF-291--AF-296 eta frontier and the quantitative no-free-repair conclusion (9)--(10): the reciprocal raw projective margin is not merely the scale chosen by the condition metric, but a necessary boundary-layer density scale for every finite-margin target-radial conformal repair. That closes the fixed-profile radial escape while leaving genuinely source-derived nonradial geometry as the live alternative.