# NB-166 — High-ordinate analyticity replaces conditioning by Poisson transport

**Date:** 2026-09-16  
**Status:** `LITERATURE+DERIVED + SOURCE-SPECIFIC + SIGNED-CONSERVATION + WASSERSTEIN + HIGH-ORDINATE-ANALYTICITY + NB-162/NB-165-SYNTHESIS`.

`NB-162` shows that, on a fixed exterior line, Jordan transport controls both the Poisson target response and the signed Euler response, but its Euler estimate uses the absolute Dirichlet series for the derivative and therefore pays the boundary scale `1/a_G`. `NB-165` independently shows that the actual high-ordinate value of `zeta'/zeta` is only `O(log G/log log G)` on `Re s>=1`, replacing the total-variation tariff `C_G/a_G` by `C_G min{1/a_G,log G/log log G}`.

The two improvements combine more strongly than either statement alone. Analyticity converts the high-ordinate pointwise bound of `NB-165` into a vertical Lipschitz bound of size `O((log G/log log G)/a_G)`. Pairing that derivative estimate with the optimal Jordan coupling from `NB-162` replaces **total-variation conditioning `C_G` by the scale-invariant transport number `Theta_G=C_G ell_G/a_G` in the entire signed conservation budget**. Consequently, arbitrarily large total variation is not itself an escape when the two Jordan signs interlace finely enough to keep `Theta_G` controlled.

## Claim

Fix `A,B,kappa>0`. For arbitrarily large `G`, let

\[
0<a_G\le A
\]

and let `nu_G` be a finite real signed Borel measure supported on

\[
[G-B,G+B]
\]

with zero total mass. Write

\[
\nu_G=\nu_G^+-\nu_G^-,
\qquad
m_G:=\nu_G^+(\mathbf R)=\nu_G^-(\mathbf R),
\qquad
V_G:=\|\nu_G\|_{\rm TV}=2m_G,
\]

and define the Jordan transport quantities

\[
W_G:=\mathsf W_1(\nu_G^+,\nu_G^-),
\qquad
\ell_G:=\frac{W_G}{m_G}.
\]

For every nontrivial zero `rho=beta+i gamma`, counted with multiplicity, put

\[
Q_G(\rho)
:=
\Re\int
\frac{d\nu_G(t)}{1+a_G+it-\rho}
=
\int
\frac{x_\rho}
{x_\rho^2+(t-\gamma)^2}
\,d\nu_G(t),
\]

where

\[
x_\rho:=1+a_G-\beta.
\]

Suppose a positive-ordinate target packet `F_G` satisfies

\[
d_G:=|F_G|\ge\kappa\log G,
\qquad
q_G:=\inf_{\rho\in F_G}Q_G(\rho)>0.
\]

Set

\[
C_G:=\frac{V_G}{q_G},
\qquad
\Theta_G:=\frac{C_G\ell_G}{a_G},
\]

so that exactly

\[
W_G=\frac{q_Ga_G\Theta_G}{2}.
\]

Finally write

\[
L_G:=\log G,
\qquad
L_{2,G}:=\log\log G,
\qquad
E_G:=\min\left\{\frac1{a_G},\frac{L_G}{L_{2,G}}\right\}.
\]

Then the following hold.

### 1. Transport, not total variation, governs the compact signed conservation remainder

There is a constant depending only on `A,B` such that

\[
\boxed{
\sum_\rho Q_G(\rho)
=O_{A,B}(q_G\Theta_GE_G).
}
\]

Thus the `NB-165` budget `C_GE_G` improves, on a fixed exterior line with finite Jordan transport, to

\[
\boxed{\Theta_GE_G.}
\]

In particular, the estimate is insensitive to how large `C_G` itself becomes, provided the mean positive-to-negative transport shrinks so that `C_G\ell_G/a_G` stays controlled.

### 2. A logarithmic target packet exports essentially full adverse debt whenever `Theta_GE_G=o(log G)`

Let

\[
A_G^-:=
\sum_{\substack{\rho\notin F_G\\ \gamma>0}}
(Q_G(\rho))_-.
\]

Then

\[
\boxed{
A_G^-
\ge
q_G\left(
 d_G-O_{A,B}(\Theta_GE_G)
\right).
}
\]

Hence, if

\[
\boxed{\Theta_GE_G=o(L_G),}
\]

then

\[
A_G^-
\ge
(\kappa-o(1))q_GL_G.
\]

This condition has the same boundary crossover as `NB-165`, but with `Theta_G` in place of `C_G`:

\[
a_G\gg \frac{L_{2,G}}{L_G}
\quad\Longrightarrow\quad
\frac{\Theta_G}{a_G}=o(L_G),
\]

while in the extreme boundary layer

\[
a_G\ll \frac{L_{2,G}}{L_G}
\quad\Longrightarrow\quad
\boxed{\Theta_G=o(L_{2,G})}
\]

is sufficient regardless of the total-variation conditioning.

### 3. The transport estimate also localizes the debt without paying `C_G`

There is `R_0=R_0(A,B)` such that, for a sufficiently large fixed constant `D=D(A,B,kappa)`, the radius

\[
R_G:=R_0+D\sqrt{a_G\Theta_G}
\]

satisfies under `Theta_GE_G=o(L_G)`

\[
\boxed{
\sum_{\substack{\rho\notin F_G\\ \gamma>0\\ |\gamma-G|\le R_G}}
(Q_G(\rho))_-
\gg_{A,B,\kappa}q_GL_G.
}
\]

Thus the `O(1+C_G)` localization radius from the total-variation argument in `NB-165` is not intrinsic to a transport-interlaced sampler. Once the Jordan cancellation is used before taking absolute values, the relevant radius is `O(1+sqrt(a_G Theta_G))`.

### 4. The localized debt still forces a divergent adverse zero population

Let

\[
\Delta_G
:=
\frac{1}
{53.989\,[\log(2G)]^{2/3}[\log\log(2G)]^{1/3}},
\]

using the Bellotti zero-free region already anchored in this line. Every localized zero obeys `1-beta>=Delta_G` for large `G`, and the transport form of the Poisson Lipschitz estimate gives

\[
|Q_G(\rho)|
\le
\frac{9}{16\sqrt3}
\frac{q_Ga_G\Theta_G}
{(a_G+\Delta_G)^2}.
\]

Consequently

\[
\boxed{
\#\left\{
\rho\notin F_G:
\gamma>0,
|\gamma-G|\le R_G,
Q_G(\rho)<0
\right\}
\gg
\frac{L_G(a_G+\Delta_G)^2}
{a_G\Theta_G}.
}
\]

Under the sole conservation hypothesis `Theta_GE_G=o(L_G)`, this lower bound tends to infinity.

## Derivation

### High-ordinate pointwise control becomes a derivative bound by Cauchy

Put

\[
f(s):=\frac{\zeta'}{\zeta}(s).
\]

For `t in [G-B,G+B]`, the function is holomorphic on the disc

\[
|z-(1+a_G+it)|\le a_G/2,
\]

because that disc remains in `Re z>1`. Cully--Hugill--Leong's uniform one-line estimate, already load-bearing in `NB-165`, gives throughout the disc for sufficiently large `G`

\[
|f(z)|
\ll_{A,B}
\frac{L_G}{L_{2,G}}.
\]

Cauchy's derivative estimate therefore yields

\[
\boxed{
|f'(1+a_G+it)|
\ll_{A,B}
\frac1{a_G}
\frac{L_G}{L_{2,G}}.
}
\]

Independently, absolute convergence of the differentiated Euler series gives

\[
|f'(1+a_G+it)|
\le
\sum_{n\ge2}
\frac{\Lambda(n)\log n}{n^{1+a_G}}
=
\left(\frac{\zeta'}{\zeta}\right)'(1+a_G)
\ll_A \frac1{a_G^2}.
\]

Taking the better estimate,

\[
\operatorname{Lip}_{[G-B,G+B]}
\left(t\mapsto f(1+a_G+it)\right)
\ll_{A,B}
\frac{E_G}{a_G}.
\]

This derivative estimate is the new bridge between `NB-162` and `NB-165`: the high-ordinate source cap survives differentiation at the cost of exactly one Poisson width.

### Optimal Jordan transport converts the derivative bound into the signed Euler budget

For any optimal coupling `pi_G` of `nu_G^+` and `nu_G^-`, zero total mass gives

\[
\int f(1+a_G+it)\,d\nu_G(t)
=
\iint
\left[
 f(1+a_G+is)-f(1+a_G+it)
\right]
\,d\pi_G(s,t).
\]

Hence

\[
\left|
\int f(1+a_G+it)\,d\nu_G(t)
\right|
\ll_{A,B}
\frac{E_G}{a_G}W_G.
\]

Since `W_G=q_Ga_GTheta_G/2`,

\[
\boxed{
\left|
\int
\frac{\zeta'}{\zeta}(1+a_G+it)
\,d\nu_G(t)
\right|
\ll_{A,B}
q_G\Theta_GE_G.
}
\]

The gain over `NB-165` is therefore not a new pointwise estimate for zeta. It comes from applying the existing high-ordinate estimate **before** destroying the signed geometry by total variation.

### The completed Gamma and rational terms are even cheaper in transport

The completed logarithmic derivative decomposes into the zeta logarithmic derivative, the digamma term, and rational/constant terms. On `t in [G-B,G+B]`, the vertical derivative of the digamma contribution is `O_{A,B}(1/G)` by Stirling, while the rational terms have derivative `O_{A,B}(1/G^2)`. Their integrals against the zero-mass measure are therefore

\[
O_{A,B}\left(\frac{W_G}{G}\right)
=
O_{A,B}\left(
q_G\frac{a_G\Theta_G}{G}
\right),
\]

which is absorbed by `O(q_GTheta_GE_G)`.

As in `NB-165`, zero total mass also cancels the reference constants in the Hadamard product, so termwise integration gives

\[
\sum_\rho Q_G(\rho)
=
\Re\int
\frac{\xi'}{\xi}(1+a_G+it)
\,d\nu_G(t).
\]

This proves the first claim.

### Negative ordinates are a transport tail, not a total-variation tail

For `rho=beta+i gamma` with `gamma<0`, the Poisson kernel

\[
K_\rho(t)
=
\frac{x_\rho}
{x_\rho^2+(t-\gamma)^2}
\]

has, uniformly for `t in [G-B,G+B]`,

\[
|K_\rho'(t)|
\ll_{A,B}
(G+|\gamma|)^{-3},
\]

because `a_G<x_\rho<1+A`. Thus

\[
|Q_G(\rho)|
\ll_{A,B}
\frac{W_G}{(G+|\gamma|)^3}.
\]

Riemann--von Mangoldt shell counting gives

\[
\sum_{\gamma<0}|Q_G(\rho)|
\ll_{A,B}
W_G\frac{L_G}{G^2}
\ll
q_Ga_G\Theta_G\frac{L_G}{G^2}.
\]

Under `Theta_GE_G=o(L_G)` this is negligible compared with `q_GL_G`; in fact it is already absorbed into the conservation remainder. Splitting the positive-ordinate zeros into the target packet and positive/negative response therefore gives

\[
A_G^-
\ge
q_Gd_G-O_{A,B}(q_G\Theta_GE_G),
\]

proving the adverse-debt estimate.

### Far positive ordinates decay one transport derivative faster

If `|gamma-G|>=R>=R_0(A,B)`, the same derivative calculation yields

\[
|Q_G(\rho)|
\ll_{A,B}
\frac{W_G}{|\gamma-G|^3}.
\]

Summing by Riemann--von Mangoldt shells gives, for `R=o(G)`,

\[
\sum_{\substack{\gamma>0\\|\gamma-G|\ge R}}
|Q_G(\rho)|
\ll_{A,B}
W_G\left(
\frac{L_G}{R^2}
+
\frac{L_G}{G^2}
\right).
\]

Substituting `W_G=q_Ga_GTheta_G/2` and taking

\[
R=R_0+D\sqrt{a_G\Theta_G}
\]

makes the first term at most `O(q_GL_G/D^2)`. The hypothesis `Theta_GE_G=o(L_G)` implies `a_GTheta_G=O_A(L_G)`, so `R=o(G)`. Choosing `D` sufficiently large leaves a fixed fraction of the global adverse debt inside the claimed window.

### Zero-free horizontal depth converts transport-localized debt into population

For every zero in that window, Bellotti's zero-free region gives

\[
x_\rho=1+a_G-\beta
\ge a_G+\Delta_G.
\]

The exact global Lipschitz constant of the Poisson kernel from `NB-162` is

\[
\operatorname{Lip}(K_{x,\gamma})
=
\frac{9}{8\sqrt3\,x^2}.
\]

Therefore

\[
|Q_G(\rho)|
\le
\frac{9}{8\sqrt3}
\frac{W_G}{(a_G+\Delta_G)^2}
=
\frac{9}{16\sqrt3}
\frac{q_Ga_G\Theta_G}{(a_G+\Delta_G)^2}.
\]

Dividing the localized `Omega(q_GL_G)` debt by this pointwise maximum proves the population bound.

It remains to check divergence from the same conservation hypothesis. Write

\[
\Theta_GE_G=\varepsilon_GL_G,
\qquad
\varepsilon_G\to0.
\]

If `E_G=1/a_G`, then

\[
\frac{L_G(a_G+\Delta_G)^2}{a_G\Theta_G}
\ge
\frac{L_Ga_G}{\Theta_G}
=
\varepsilon_G^{-1}
\to\infty.
\]

If `E_G=L_G/L_{2,G}`, then `Theta_G=epsilon_G L_{2,G}` and the elementary inequality

\[
\frac{(a_G+\Delta_G)^2}{a_G}
\ge4\Delta_G
\]

gives

\[
\frac{L_G(a_G+\Delta_G)^2}{a_G\Theta_G}
\ge
\frac{4\Delta_GL_G}{\varepsilon_GL_{2,G}}
\asymp
\frac{L_G^{1/3}}
{\varepsilon_GL_{2,G}^{4/3}}
\longrightarrow\infty.
\]

Thus the adverse population diverges in both branches.

## What this changes after NB-162 and NB-165

`NB-162` identified `Theta_G=C_G ell_G/a_G` as the scale-invariant price of Jordan transport, but its source estimate was still the boundary-only `Theta_G/a_G` tariff. `NB-165` then inserted the actual high-ordinate zeta bound, but only after passing to total variation, so its conservation condition remained `C_GE_G=o(log G)`.

The present result combines the two in the correct order:

\[
\boxed{
\text{high-ordinate analyticity}
+
\text{Jordan transport}
\quad\Longrightarrow\quad
\text{source cost }\Theta_GE_G.
}
\]

This matters most for strongly interlaced, badly conditioned samplers. A construction may have `C_G` arbitrarily large while its positive and negative masses lie at mean separation `ell_G\asymp a_G/C_G`, keeping `Theta_G=Theta(1)`. Total variation alone sees an enormous bill; the actual signed source sees only `O(q_GE_G)`. For a logarithmic target packet that is still `o(q_Glog G)` in every fixed-gap regime, and also throughout the saturated extreme-boundary regime because `L_G/L_{2,G}=o(L_G)`.

So increasing total variation while collapsing the two Jordan signs proportionally does not evade signed conservation. The surviving compact transport escape must make `Theta_G` itself large enough to compete with the target packet: at least logarithmic in the fixed/moderate-gap regime, and at least `log log G` once the high-ordinate cap is active. Alternatively it must leave the fixed-line compact setting or exploit a mechanism not represented by first-order Jordan transport.

## Prior-art and novelty audit

The ingredients are classical or already anchored. Kantorovich--Rubinstein transport is the mechanism used in `NB-162`. Cauchy's derivative estimate is classical complex analysis. Cully--Hugill--Leong provide the load-bearing uniform `O(log t/log log t)` bound for `zeta'/zeta` on `sigma>=1`; that source is already recorded in `SOURCES.md` by `NB-165`. Bellotti's explicit zero-free region and Riemann--von Mangoldt counting are also already anchored.

A fresh literature search across Nyman--Beurling criteria, signed/Poisson sampling, Wasserstein transport, and high-ordinate logarithmic-derivative estimates found the expected Nyman--Beurling literature, Bruna--Melnikov's work on translates of the Poisson kernel, and the explicit zeta logarithmic-derivative literature, but not this line-specific synthesis: differentiating the high-ordinate one-line bound by Cauchy, pairing it with the Jordan coupling, and propagating the resulting `C_G -> Theta_G` replacement through signed zero conservation, localization, and population. No novelty is claimed for any of the ingredients separately, and no new source anchor is required.

## Boundaries and failure modes

The sampler lies on one exterior vertical line and has bounded vertical support about height `G`. Horizontal transport or vertical diameters growing with `G` require separate bookkeeping. The result does not say that `Theta_GE_G=o(log G)` is necessary for adverse debt; it is a sufficient condition obtained from the available high-ordinate derivative majorant.

The target packet is conditional. No existence of a crowded off-critical packet is asserted, and nothing here proves RH. The adverse population is counted with multiplicity, as in `NB-165`.

The theorem also does not rule out samplers with `Theta_G` at or above the displayed threshold. Nor does it claim that the Cauchy-derived derivative bound is optimal. A stronger high-ordinate estimate for `(zeta'/zeta)'` would immediately sharpen the same transport argument.

Finally, large total variation is not declared harmless in general. It disappears here only because a quantified optimal coupling witnesses compensating positive and negative mass at the corresponding small transport scale. If no such coupling is cheap, `Theta_G` records that cost.

## Source map

- `NB-154`: zero-mass signed conservation and the original inverse-gap boundary tariff.
- `NB-160`--`NB-161`: sign-support separation and Jordan transport as the geometry of interlaced samplers.
- `NB-162`: target/Euler control by `Theta_G` using the absolute differentiated Euler series.
- `NB-165`: high-ordinate `zeta'/zeta` cap, compact signed conservation, localization, and Bellotti population conversion.
- Cully--Hugill--Leong (2024): uniform high-ordinate `O(log t/log log t)` bound on `zeta'/zeta` for `sigma>=1`.
- Bellotti (2024): explicit Vinogradov--Korobov zero-free region.

## Consequence for the line

For fixed-line compact signed samplers, **conditioning and interlacing are not independent resources once the actual high-ordinate zeta source is used. The conservation cost is controlled by `Theta_G min{a_G^{-1},log G/log log G}`, not `C_G min{a_G^{-1},log G/log log G}`.** Hence a logarithmic target packet exports essentially full adverse debt whenever that transport-normalized cost is `o(log G)`, with the debt localized on radius `O(1+sqrt(a_GTheta_G))` and carried by a divergent population of adverse zeros. The remaining compact regime must therefore pay directly in the scale-invariant transport number itself, rather than merely hiding large total variation inside finer Jordan interlacing.