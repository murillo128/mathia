# NB-157 — Three-height balancing annihilates the macroscopic Gamma tariff

**Date:** 2026-09-16  
**Status:** DERIVED + LITERATURE-CHECKED + FRONTIER-CHANGING

`NB-156` bounded the completed-logarithmic-derivative background of a vertically macroscopic signed sampler by the absolute envelope

\[
D_G+C_G\log\frac{G}{H_G}.
\]

That estimate is sufficient but not intrinsic. The apparent Gamma tariff is carried, to first order, by one signed scalar moment of the sampled heights. Once that moment is exposed, it can be cancelled exactly by one additional linear constraint. In particular, a three-height sampler can have zero total mass and zero leading Gamma moment with bounded coefficients even when its lowest sampled height is only a fixed power of `G`.

## Claim

Retain the `NB-156` geometry. Let `\mu_G` be a finite real signed measure supported on

\[
K_G\subset\{w=u+iv:\ a_G\le u\le A,\ |v|\le B_G\},
\qquad 0<a_G\le A,
\]

with

\[
\mu_G(K_G)=0,
\qquad H_G:=G-B_G\to\infty.
\]

Write

\[
V_G:=\|\mu_G\|_{\rm TV},
\qquad
Q_G(\rho):=\Re\int_{K_G}\frac{d\mu_G(w)}{1+w+iG-\rho}.
\]

Suppose a positive-ordinate target packet `F_G` contains `d_G\ge\kappa\log G` zeros and `Q_G(\rho)\ge q_G>0` on `F_G`. Set

\[
C_G:=\frac{V_G}{q_G},
\qquad D_G:=\frac{C_G}{a_G},
\]

and define the normalized logarithmic-height defect

\[
J_G:=\frac1{q_G}\left|\int_{K_G}\log\!\left(\frac{G+\Im w}{G}\right)d\mu_G(w)\right|.
\]

Then

\[
\boxed{\sum_\rho Q_G(\rho)=\frac12\int_{K_G}\log\!\left(\frac{G+\Im w}{G}\right)d\mu_G(w)+O_A\!\left(\frac{V_G}{a_G}\right).}
\]

Consequently the negative charge carried by positive-ordinate zeros outside `F_G` obeys

\[
\boxed{A_G^-\ge q_G\left(\kappa\log G-\frac12J_G-O_A(D_G)\right).}
\]

Hence `D_G+J_G=o(\log G)` forces

\[
A_G^-\ge(\kappa-o(1))q_G\log G.
\]

The localization and population conclusions of `NB-156` remain unchanged: a fixed positive fraction of this adverse charge lies inside

\[
|\gamma-G|\le B_G+O_{A,\kappa}(C_G+1),
\]

and that window contains at least

\[
\Omega_{A,\kappa}\!\left(\frac{\log G}{D_G}\right)
\]

adverse zeros.

In particular, if the sampler is **Gamma-balanced**,

\[
\boxed{\int_{K_G}\log\!\left(\frac{G+\Im w}{G}\right)d\mu_G(w)=0,}
\]

then the vertical Gamma cost disappears from the leading conservation budget. The adverse-packet obstruction survives whenever `D_G=o(\log G)`, irrespective of the size of `\log(G/H_G)`, provided only `H_G\to\infty`.

Moreover this leading Gamma term is rank one on the mass-zero sampler space. A nontrivial two-height signed sampler cannot simultaneously have zero mass and zero logarithmic-height moment when the two heights differ, whereas three heights suffice with coefficients of bounded total variation.

## Derivación

Put

\[
s(w)=1+w+iG=\sigma+i t,
\qquad t=G+\Im w.
\]

Throughout the support,

\[
1+a_G\le\sigma\le1+A,
\qquad H_G\le t\le2G-H_G,
\]

so `t\to\infty` uniformly because `H_G\to\infty`.

The mass-zero condition lets us difference the Hadamard expansion of `\xi'/\xi` before summing over zeros. The regularizing constants therefore cancel and the resulting zero sum is absolutely convergent for each `G`, giving

\[
\sum_\rho Q_G(\rho)=\Re\int_{K_G}\frac{\xi'}{\xi}(s(w))\,d\mu_G(w).
\]

Use

\[
\frac{\xi'}{\xi}(s)=\frac1s+\frac1{s-1}-\frac12\log\pi+\frac12\psi\!\left(\frac s2\right)+\frac{\zeta'}{\zeta}(s).
\]

The constant term vanishes after integration. Uniform Stirling in the bounded horizontal strip gives

\[
\Re\psi\!\left(\frac{\sigma+i t}{2}\right)=\log t+O_A(t^{-1}),
\]

hence

\[
\Re\int_{K_G}\frac12\psi\!\left(\frac{s(w)}2\right)d\mu_G(w)=\frac12\int_{K_G}\log t\,d\mu_G(w)+O_A\!\left(\frac{V_G}{H_G}\right).
\]

Because `\mu_G(K_G)=0`, the common reference `\log G` can be subtracted exactly:

\[
\int_{K_G}\log t\,d\mu_G(w)=\int_{K_G}\log\!\left(\frac tG\right)d\mu_G(w).
\]

On `\Re s=1+u`, absolute convergence of the Euler product gives

\[
\left|\frac{\zeta'}{\zeta}(1+u+i t)\right|\ll\frac1u,
\]

so its integrated contribution is `O(V_G/a_G)`. The rational terms `1/s` and `1/(s-1)` contribute `O_A(V_G/H_G)`, which is eventually absorbed by `O_A(V_G/a_G)`. Combining the pieces proves the boxed conservation law.

The target packet contributes at least `\kappa q_G\log G`. Negative-ordinate zeros contribute only

\[
O_A\!\left(V_G\frac{\log H_G}{H_G}\right)=o_A\!\left(\frac{V_G}{a_G}\right),
\]

because every sampled ordinate is at least `H_G` and the Poisson kernel against the reflected zero set has quadratic vertical decay. Rearranging the absolutely convergent zero identity therefore yields

\[
A_G^-\ge q_G\left(\kappa\log G-\frac12J_G-O_A(D_G)\right).
\]

For localization, once `|\gamma-G|` lies beyond the vertical support by a distance `r`, the integrated kernel is `O_A(V_G/r^2)`. Summing the standard `O(\log T)` zero count over unit shells gives the same tail estimate as in `NB-156`; taking the excess radius to be a sufficiently large multiple of `C_G+1` leaves a fixed fraction of the adverse mass inside

\[
|\gamma-G|\le B_G+O_{A,\kappa}(C_G+1).
\]

Every individual zero satisfies

\[
|Q_G(\rho)|\le\frac{V_G}{a_G}=q_GD_G,
\]

so adverse charge `\gg q_G\log G` requires `\Omega(\log G/D_G)` actual zeros.

It remains to identify the rank-one nature of the Gamma term. For a two-height sampler

\[
\mu_G=c(\delta_{w_1}-\delta_{w_2}),
\]

with sampled heights `t_1\ne t_2`, mass zero is automatic but

\[
\int\log(t/G)\,d\mu_G=c\log(t_1/t_2)\ne0
\]

unless `c=0`. Thus two distinct heights cannot cancel both moments nontrivially.

For three fixed exponents `0<\theta_1<\theta_2<\theta_3\le1`, sample at

\[
t_j=G^{\theta_j},
\qquad w_j=a+i(t_j-G)
\]

for any fixed `a>0`, and choose

\[
c_1=\theta_3-\theta_2,
\qquad c_2=-(\theta_3-\theta_1),
\qquad c_3=\theta_2-\theta_1.
\]

Then

\[
\sum_{j=1}^3c_j=0,
\qquad \sum_{j=1}^3c_j\theta_j=0.
\]

Since `\log(t_j/G)=(\theta_j-1)\log G`, these identities imply

\[
\sum_{j=1}^3c_j\log(t_j/G)=0.
\]

The coefficients, and hence their total variation, are independent of `G`. The lowest sampled height is `H_G=G^{\theta_1}`, so this construction sits precisely in the regime where the absolute envelope from `NB-156` can be of order `\log G`, yet the leading Gamma contribution vanishes identically.

This algebraic construction certifies only the cost of Gamma balancing. It does **not** certify that the resulting sampler gives a useful target charge `q_G`; its conditioning `C_G=V_G/q_G` may still diverge.

## Verificación

The sharpened law reproduces `NB-156` by taking absolute values. Indeed

\[
J_G\le C_G\sup_{H_G\le t\le2G-H_G}\left|\log\frac tG\right|\le C_G\left(\log\frac{G}{H_G}+\log2\right).
\]

Because `C_G\le A D_G`, the harmless `C_G\log2` term is absorbed into `D_G`, recovering the previous budget `D_G+C_G\log(G/H_G)`.

The new statement is strictly sharper whenever the signed height moment cancels. For example, if `H_G=G^\theta` with fixed `0<\theta<1` and `C_G=O(1)`, the `NB-156` envelope pays `(1-\theta)C_G\log G`, while exact Gamma balance sets the actual leading term to zero. The same separation holds for `H_G=(\log G)^B`: the absolute envelope is asymptotic to `C_G\log G`, but a balanced sampler still pays only the Euler/conditioning term `O(D_G)`.

The two-height and three-height checks are exact finite-dimensional identities, not asymptotic approximations. The only asymptotic input in the Gamma extraction is uniform Stirling for `t\ge H_G\to\infty`; the arithmetic side uses only the absolutely convergent Euler product in `\Re s>1` and the same zero-counting tail control already used in `NB-156`.

A focused prior-art audit for signed Poisson/logarithmic-derivative combinations, finite differences of the digamma term, and Guinand--Weil/Poisson-kernel treatments of `\zeta'/\zeta` found standard explicit-formula and extremal-kernel uses, but no target-conditioned statement identifying this normalized signed log-height moment as the sole leading macroscopic Gamma defect. No new external result is load-bearing here, so `SOURCES.md` requires no addition.

## Consecuencia

The macroscopic vertical Gamma tariff of `NB-156` is not an unavoidable cost of sampling over a large height range. It is the absolute-value envelope of one linear functional,

\[
\mu_G\longmapsto\int\log\!\left(\frac{G+\Im w}{G}\right)d\mu_G(w),
\]

on the mass-zero sampler space. One extra signed degree of freedom can annihilate that leading term.

Therefore vertical support reaching polynomially smaller heights is **not**, by itself, a new escape resource. If `D_G=o(\log G)` and the logarithmic-height defect is also `o(\log G)`, the target packet still exports logarithmic adverse zero mass and an `\Omega(\log G/D_G)` adverse population. To exploit macroscopic vertical sampling as a genuine escape, a future construction must deliberately retain `J_G=\Omega(\log G)` (or already pay `D_G=\Omega(\log G)`) while simultaneously preserving useful target charge and obtaining enough signed cancellation on the von-Mangoldt/Nyman side. The next frontier is therefore not vertical range itself, but the compatibility between target conditioning, the log-height moment, and arithmetic signed cancellation.
