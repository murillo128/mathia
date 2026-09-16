# NB-167 — Capped Poisson transport unifies conditioning and Wasserstein conservation

**Date:** 2026-09-16  
**Status:** `DERIVED + SOURCE-SPECIFIC + SIGNED-CONSERVATION + TRUNCATED-WASSERSTEIN + POISSON-SCALE + NB-165/NB-166-REFINEMENT`.

`NB-165` controls compact signed conservation by total variation, while `NB-166` improves this to ordinary Jordan `W_1` transport. Both discard part of the geometry: total variation charges mass that almost cancels locally, whereas `W_1` keeps charging distance after the two signs are more than one Poisson width apart and a bounded analytic test has already saturated.

The natural compact interpolation is the Jordan transport for the truncated Poisson metric

\[
d_a(s,t):=\min\left\{1,\frac{|s-t|}{a}\right\}.
\]

Below one exterior width this is `W_1/a`; beyond one width it charges only the amount of unmatched signed mass. This is classical bounded-Lipschitz/Fortet--Mourier geometry, but here its cutoff is fixed by the exterior Poisson width and its test functions are the actual high-ordinate zeta source and zero kernels.

## Claim

Fix `A,B,kappa>0`. For arbitrarily large `G`, let `0<a_G<=A` and let `nu_G` be a finite real signed Borel measure supported on `[G-B,G+B]`, with zero total mass. Write

\[
\nu_G=\nu_G^+-\nu_G^-,
\qquad
m_G:=\nu_G^+(\mathbf R)=\nu_G^-(\mathbf R),
\qquad
V_G=2m_G.
\]

Define the capped Jordan transport

\[
\mathsf T_G
:=
\inf_{\pi\in\Pi(\nu_G^+,\nu_G^-)}
\iint
\min\left\{1,\frac{|s-t|}{a_G}\right\}
\,d\pi(s,t).
\]

For each nontrivial zero `rho=beta+i gamma`, counted with multiplicity, put

\[
Q_G(\rho)
:=
\Re\int
\frac{d\nu_G(t)}{1+a_G+it-\rho},
\qquad
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
W_G:=\mathsf W_1(\nu_G^+,\nu_G^-),
\qquad
\Theta_G:=\frac{2W_G}{q_Ga_G},
\qquad
\Xi_G:=\frac{\mathsf T_G}{q_G},
\]

and

\[
L_G:=\log G,
\qquad
L_{2,G}:=\log\log G,
\qquad
E_G:=\min\left\{\frac1{a_G},\frac{L_G}{L_{2,G}}\right\}.
\]

Then the following hold.

### 1. Capped transport refines both predecessor currencies

Since `d_a<=1` and `d_a<=|s-t|/a`,

\[
\mathsf T_G\le m_G,
\qquad
\mathsf T_G\le W_G/a_G,
\]

and therefore

\[
\boxed{
\Xi_G\le\frac12\min\{C_G,\Theta_G\}.
}
\]

Moreover the completed explicit-formula conservation remainder satisfies

\[
\boxed{
\sum_\rho Q_G(\rho)
=O_{A,B}(q_G\Xi_GE_G).
}
\]

Thus `NB-165` and `NB-166` are both corollaries of the capped estimate, while mixed short/long couplings can be substantially cheaper than either global summary.

### 2. The same capped transport controls every Poisson response

For every nontrivial zero,

\[
\boxed{
|Q_G(\rho)|\le\frac{\mathsf T_G}{x_\rho}.
}
\]

Consequently every target zero satisfies

\[
\boxed{
\Xi_G\ge x_\rho,
\qquad \rho\in F_G.
}
\]

This statement is height-free: no comparison between the target ordinates and `G` is needed. A zero-free-region lower bound such as `x_rho>=a_G+Delta_G` is used only later for adverse zeros already localized to height comparable with `G`.

### 3. A logarithmic target packet exports full adverse debt whenever `Xi_G E_G=o(log G)`

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
q_G\left(d_G-O_{A,B}(\Xi_GE_G)\right).
}
\]

Hence

\[
\boxed{
\Xi_GE_G=o(L_G)
\quad\Longrightarrow\quad
A_G^-\ge(\kappa-o(1))q_GL_G.
}
\]

In the extreme boundary layer `a_G << L_{2,G}/L_G`, it is enough that

\[
\boxed{\Xi_G=o(L_{2,G}),}
\]

even when both `C_G` and `Theta_G` are large.

### 4. Capped transport also localizes the debt and forces a divergent adverse population

There is `R_0=R_0(A,B)` such that, for sufficiently large fixed `D=D(A,B,kappa)`,

\[
R_G:=R_0+D\Xi_G
\]

satisfies under `Xi_GE_G=o(L_G)`

\[
\boxed{
\sum_{\substack{\rho\notin F_G\\ \gamma>0\\ |\gamma-G|\le R_G}}
(Q_G(\rho))_-
\gg_{A,B,\kappa}q_GL_G.
}
\]

Let

\[
\Delta_G
:=
\frac{1}
{53.989\,[\log(2G)]^{2/3}[\log\log(2G)]^{1/3}},
\]

using Bellotti's already anchored zero-free region. Since `R_G=o(G)`, every adverse zero in this window has `x_rho>=a_G+Delta_G` for large `G`. Therefore

\[
|Q_G(\rho)|
\le
\frac{q_G\Xi_G}{a_G+\Delta_G},
\]

and

\[
\boxed{
\#\{\rho\notin F_G:\gamma>0,\ |\gamma-G|\le R_G,\ Q_G(\rho)<0\}
\gg
\frac{L_G(a_G+\Delta_G)}{\Xi_G}.
}
\]

The right side tends to infinity under the sole conservation hypothesis `Xi_GE_G=o(L_G)`.

## Derivation

### High-ordinate analyticity is bounded-Lipschitz at one Poisson width

Put

\[
f_G(t):=\frac{\zeta'}{\zeta}(1+a_G+it).
\]

`NB-165` and `NB-166` give uniformly on `[G-B,G+B]`

\[
|f_G(t)|\ll_{A,B}E_G,
\qquad
|f_G'(t)|\ll_{A,B}\frac{E_G}{a_G}.
\]

Hence

\[
|f_G(s)-f_G(t)|
\le
\min\{2\|f_G\|_\infty,\|f_G'\|_\infty|s-t|\}
\ll_{A,B}E_Gd_{a_G}(s,t).
\]

Integrating against a Jordan coupling and minimizing gives

\[
\left|\int f_G(t)\,d\nu_G(t)\right|
\ll_{A,B}E_G\mathsf T_G.
\]

The completed Gamma and rational terms are cheaper: on the bounded high-ordinate interval their oscillation is `O_{A,B}(|s-t|/G)` or better, and bounded support implies `|s-t|<<_{A,B}d_{a_G}(s,t)`. Zero total mass cancels the Hadamard reference constants as in `NB-165/166`. This proves

\[
\sum_\rho Q_G(\rho)
=O_{A,B}(E_G\mathsf T_G)
=O_{A,B}(q_G\Xi_GE_G).
\]

### Poisson kernels lie in the same bounded-Lipschitz class

For

\[
K_{x,\gamma}(t)=\frac{x}{x^2+(t-\gamma)^2},
\]

one has

\[
0\le K_{x,\gamma}\le\frac1x,
\qquad
\|K'_{x,\gamma}\|_\infty
=\frac{9}{8\sqrt3\,x^2}<\frac1{x^2}.
\]

For a nontrivial zero `x_rho>=a_G`. If `|s-t|>=a_G`, the range bound gives

\[
|K(s)-K(t)|\le x_\rho^{-1}d_{a_G}(s,t).
\]

If `|s-t|<a_G`, the derivative bound gives

\[
|K(s)-K(t)|
<\frac{|s-t|}{x_\rho^2}
\le\frac1{x_\rho}\frac{|s-t|}{a_G}.
\]

Thus

\[
|K(s)-K(t)|\le\frac1{x_\rho}d_{a_G}(s,t),
\]

and coupling proves the pointwise `Q_G` estimate. On `F_G`, `Q_G(rho)>=q_G`, hence `Xi_G>=x_rho`.

### Debt, localization, and population

For `gamma<0`, the kernel is `O((G+|gamma|)^{-2})` and its derivative is `O((G+|gamma|)^{-3})` on the support interval. Splitting coupling pairs at distance `a_G` gives

\[
|Q_G(\rho)|\ll_{A,B}\frac{\mathsf T_G}{(G+|\gamma|)^2}.
\]

Riemann--von Mangoldt shell counting yields

\[
\sum_{\gamma<0}|Q_G(\rho)|
\ll_{A,B}\mathsf T_G\frac{L_G}{G},
\]

which is negligible compared with `q_GL_G` under `Xi_GE_G=o(L_G)`. Combining this with the conservation bound and the target contribution `q_Gd_G` proves the adverse-debt estimate.

For positive zeros with `|gamma-G|>=R>=R_0(A,B)`, the same bounded/derivative split gives

\[
|Q_G(\rho)|\ll_{A,B}\frac{\mathsf T_G}{|\gamma-G|^2}.
\]

Consequently

\[
\sum_{\substack{\gamma>0\\|\gamma-G|\ge R}}
|Q_G(\rho)|
\ll_{A,B}
\mathsf T_G\left(\frac{L_G}{R}+\frac{L_G}{G}\right).
\]

With `T_G=q_GXi_G`, choosing `R=R_0+DXi_G` and then `D` sufficiently large leaves a fixed fraction of the global adverse debt inside the stated window. Since `E_G` is bounded below by a positive constant depending only on `A`, the hypothesis gives `Xi_G=o(L_G)`, hence `R_G=o(G)`.

For the population bound, write `Xi_GE_G=epsilon_GL_G` with `epsilon_G->0`. If `E_G=1/a_G`, then

\[
\frac{L_G(a_G+\Delta_G)}{\Xi_G}\ge\epsilon_G^{-1}.
\]

If `E_G=L_G/L_{2,G}`, then `Xi_G=epsilon_G L_{2,G}` and

\[
\frac{L_G(a_G+\Delta_G)}{\Xi_G}
\ge
\frac{L_G\Delta_G}{\epsilon_GL_{2,G}}
\asymp
\frac{L_G^{1/3}}
{\epsilon_GL_{2,G}^{4/3}}
\longrightarrow\infty.
\]

## Representation and generalized-control audit

The capped-transport lemma is not arithmetic. Any bounded test `f` with `||f||_infty<=M` and `Lip(f)<=M/a` obeys

\[
\left|\int f\,d\nu\right|\ll M\mathsf T_a(\nu).
\]

Likewise the Poisson estimate is pure kernel geometry. The source-specific input is exactly that the actual high-ordinate `zeta'/zeta` belongs to this bounded-Lipschitz class with `M=O(E_G)`. A matched non-arithmetic control with the same sup-norm and derivative bounds therefore satisfies the same conservation inequality. The result identifies the signed geometry seen by the test class; it does not smuggle in an RH-strength source estimate.

The refinement is genuinely geometric. Two measures can have the same total variation but arbitrarily different capped transport, and they can have the same `W_1` but very different capped transport by reallocating a small amount of mass beyond the cutoff. A coupling may move most mass by `o(a_G)` while moving a tiny fraction a fixed macroscopic distance: total variation overcharges the first part, while uncapped `W_1/a_G` overcharges the second.

## What this changes after NB-165 and NB-166

The compact source budget is now

\[
\boxed{
\Xi_GE_G,
\qquad
\Xi_G=\mathsf T_G/q_G,
}
\]

where `T_G` measures the positive/negative Jordan mismatch that survives one Poisson width of resolution. At short distances it reduces to the transport currency of `NB-166`; at long distances it reduces to the mass currency of `NB-165`; mixed geometries can be much cheaper than either.

This tightens the surviving escape route. Large total variation is irrelevant when locally paired, and large ordinary `W_1` is irrelevant when carried by too little mass beyond one width. In the extreme boundary layer, defeating this conservation argument requires capped mismatch that is not `o(log log G)`, rather than merely making one predecessor parameter large.

The target inequality `Xi_G>=x_rho` supplies the complementary interpretation: `Xi_G` is an effective unresolved signed width in the same units as each target zero's Poisson scale. The open compact regime is therefore whether a logarithmic packet can coexist with enough **Poisson-resolution Jordan mismatch** to reach the source threshold while still avoiding the localized adverse population above.

## Prior-art and novelty audit

A fresh search found the classical bounded-Lipschitz/Fortet--Mourier/Dudley metrics and the equivalent truncated-Wasserstein viewpoint with cost `min(1,d)`. That metric technology is standard and is not claimed as new. Searches combining it with Nyman--Beurling approximation, signed Poisson sampling, and high-ordinate `zeta'/zeta` did not locate the present scale-specific transfer through target gain, signed zero conservation, localization, and adverse population.

No new external theorem is load-bearing. The Cully--Hugill--Leong high-ordinate bound, Bellotti zero-free region, and Riemann--von Mangoldt counting are already anchored in `SOURCES.md`; the capped-coupling inequalities above are proved directly. Therefore `SOURCES.md` is unchanged.

## Boundaries and failure modes

The sampler remains confined to one exterior vertical line and a bounded vertical interval. Growing vertical diameter or horizontal support requires scale-dependent bookkeeping. The condition `Xi_GE_G=o(log G)` is sufficient, not necessary: actual signed values of `zeta'/zeta` may cancel more strongly than this bounded-Lipschitz majorant records.

The target packet is conditional. No crowded off-critical packet is asserted to exist, and nothing here proves RH. Adverse zeros are counted with multiplicity, consistently with the preceding findings.