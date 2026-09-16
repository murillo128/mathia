# NB-159 — Finite polynomial-height zero-mass samplers force a routine adverse reservoir

**Date:** 2026-09-16  
**Status:** EXACT-DERIVED + SOURCE-SPECIFIC + MULTISCALE + TARGET-CONDITIONED + DECISIVE-METHOD-BOUNDARY

`NB-158` showed the failure of one explicit three-height Gamma-balanced sampler: its top atom keeps order-one charge on a target packet near height `G`, but a negative middle atom creates a lower fixed-width lobe already containing `Theta(log G)` actual zeta zeros. That left open whether adding more polynomially separated heights and more balancing conditions could repair selection.

For every **fixed finite** polynomial-height atomic sampler, the answer is no under the same bounded-conditioning regime. Once zero total mass is imposed to cancel the universal Hadamard background, any sampler with a nondegenerate positive top atom must place a comparable amount of negative atomic mass at at least one lower polynomial height. Polynomial separation makes that negative atom locally dominant, and the explicit Riemann--von Mangoldt remainder then guarantees `Omega(log G)` real zeta zeros in its unit lobe. Additional Gamma/Stirling moment cancellations do not affect this conclusion.

## Claim

Fix an integer `m>=2`, exponents

\[
0<\theta_1<\theta_2<\cdots<\theta_m=1,
\]

a horizontal offset `a>0`, and a target-window radius `h>0`. Put

\[
t_j=G^{\theta_j},
\qquad
w_j=a+i(t_j-G).
\]

Let

\[
\mu_G=\sum_{j=1}^m c_j(G)\,\delta_{w_j}
\]

be a real signed atomic measure satisfying

\[
\sum_{j=1}^m c_j(G)=0,
\qquad
c_m(G)>0.
\]

Write

\[
V_G:=\sum_{j=1}^m |c_j(G)|
\]

and assume the top atom is uniformly well-conditioned in total variation:

\[
\boxed{V_G\le C\,c_m(G)}
\]

for some fixed `C` and all sufficiently large `G`.

For every nontrivial zeta zero `rho=beta+i gamma`, define

\[
Q_G(\rho)
:=
\Re\int\frac{d\mu_G(w)}{1+w+iG-\rho}.
\]

Then the following hold.

### 1. The target lobe remains uniformly nondegenerate

There exists

\[
q_+=q_+(a,h,C)>0
\]

such that every nontrivial zero with

\[
|\gamma-G|\le h
\]

satisfies, for all sufficiently large `G`,

\[
\boxed{Q_G(\rho)\ge q_+\,c_m(G).}
\]

Hence the sampler has bounded target conditioning on every fixed target window, and therefore also on every polynomially shrinking target cell contained in such a window.

### 2. Some lower polynomial scale carries a uniformly negative lobe

For every sufficiently large `G` there is an index

\[
j(G)\in\{1,\ldots,m-1\}
\]

with

\[
c_{j(G)}(G)<0,
\qquad
|c_{j(G)}(G)|\ge\frac{c_m(G)}{m-1}.
\]

There is a constant

\[
q_-=q_-(a,m)>0
\]

such that every nontrivial zero satisfying

\[
|\gamma-t_{j(G)}|\le1
\]

obeys

\[
\boxed{Q_G(\rho)\le-q_-\,c_m(G)}
\]

for all sufficiently large `G`.

### 3. That adverse lobe is routinely populated by logarithmically many actual zeros

Using the Bellotti--Wong zero-counting remainder already anchored in `SOURCES.md`, uniformly over the finitely many possible indices `j(G)`,

\[
N(t_{j(G)}+1)-N(t_{j(G)}-1)
\ge
\left(\frac1\pi-0.20152+o(1)\right)
\log t_{j(G)}.
\]

Since `theta_{j(G)}>=theta_1>0`,

\[
\boxed{
N(t_{j(G)}+1)-N(t_{j(G)}-1)
=\Omega(\log G).
}
\]

Consequently the sampler contains, independently of any target packet at height `G`, an adverse zero reservoir carrying

\[
\boxed{\Omega\!\left(c_m(G)\log G\right)}
\]

negative charge.

Therefore no fixed finite collection of polynomially separated sampling heights can turn the zero-mass signed exterior-sampling architecture into a selector merely by adding more atoms or imposing finitely many additional linear moment cancellations. In particular, cancelling the leading Gamma moment, several Stirling moments, or any other finite family of coefficient constraints does not remove the routine adverse reservoir as long as the hypotheses above remain valid.

## Derivation

Write

\[
P_x(y):=\frac{x}{x^2+y^2},
\qquad
x:=1+a-\beta.
\]

For a nontrivial zeta zero, `0<beta<1`, hence

\[
a<x<a+1,
\]

and

\[
Q_G(\rho)
=
\sum_{j=1}^m c_j(G)P_x(\gamma-t_j).
\]

### Target dominance

If `|gamma-G|<=h`, then for every `j<m`,

\[
|\gamma-t_j|=G(1+o(1))
\]

uniformly over the fixed finite set of exponents. Therefore

\[
\sum_{j<m}c_j(G)P_x(\gamma-t_j)
=
O_{a,h}\!\left(\frac{V_G}{G^2}\right)
=
O_{a,h,C}\!\left(\frac{c_m(G)}{G^2}\right).
\]

Meanwhile

\[
c_m(G)P_x(\gamma-G)
\ge
c_m(G)
\min_{a\le x\le a+1,\ |y|\le h}P_x(y).
\]

The minimum is strictly positive. Thus, after absorbing the `O(G^{-2})` cross-scale contribution,

\[
Q_G(\rho)\ge q_+c_m(G)
\]

for some fixed `q_+>0`.

### A negative coefficient of target scale is unavoidable

Because the total mass is zero,

\[
\sum_{c_j>0}c_j
=
\sum_{c_j<0}|c_j|.
\]

The positive side contains `c_m`, so

\[
\sum_{j<m:\ c_j<0}|c_j|
\ge c_m.
\]

There are at most `m-1` lower atoms. Hence at least one index `j(G)<m` satisfies

\[
|c_{j(G)}(G)|\ge\frac{c_m(G)}{m-1}.
\]

This conclusion uses only zero total mass and the nondegenerate positive top atom. Any additional balancing equations can only further restrict the coefficients; they cannot remove this sign requirement.

### Polynomial separation makes that atom locally dominant

Fix the selected index `j=j(G)` and assume

\[
|\gamma-t_j|\le1.
\]

Because the exponents are fixed and strictly ordered, distinct sampling heights are polynomially separated. There is a constant `c_theta>0` such that, for all sufficiently large `G`,

\[
|t_k-t_j|\ge c_\theta G^{\theta_1}
\qquad(k\ne j).
\]

Hence the contribution of every other atom satisfies

\[
\left|
\sum_{k\ne j}c_k(G)P_x(\gamma-t_k)
\right|
\ll_{a,\theta}
V_GG^{-2\theta_1}
\ll_{a,\theta,C}
c_m(G)G^{-2\theta_1}.
\]

On the other hand, throughout `|gamma-t_j|<=1`,

\[
P_x(\gamma-t_j)
\ge
m_-(a)
:=
\min_{a\le x\le a+1,\ |y|\le1}P_x(y)>0.
\]

Since `c_j<0` and

\[
|c_j|\ge\frac{c_m}{m-1},
\]

the own-atom contribution is at most

\[
-\frac{m_-(a)}{m-1}c_m(G).
\]

The cross-scale term is `o(c_m(G))`. Therefore, for sufficiently large `G`,

\[
Q_G(\rho)
\le
-\frac{m_-(a)}{2(m-1)}c_m(G)
=:-q_-c_m(G).
\]

### Explicit zero counting fills the adverse lobe

Set `T=t_j`. The Bellotti--Wong estimate is

\[
\left|
N(T)-\frac{T}{2\pi}\log\frac{T}{2\pi e}
\right|
\le
0.10076\log T
+0.24460\log\log T
+8.08344.
\]

For fixed unit displacement,

\[
\frac{T+1}{2\pi}\log\frac{T+1}{2\pi e}
-
\frac{T-1}{2\pi}\log\frac{T-1}{2\pi e}
=
\frac1\pi\log T+O(1).
\]

Subtracting the endpoint errors gives

\[
N(T+1)-N(T-1)
\ge
\left(
\frac1\pi-2(0.10076)+o(1)
\right)\log T.
\]

The leading constant

\[
\frac1\pi-0.20152
=0.116789886\ldots
\]

is positive. Since

\[
T=G^{\theta_j},
\qquad
\theta_j\ge\theta_1,
\]

the unit lobe contains at least

\[
(0.116789886\ldots+o(1))\theta_1\log G
\]

zeros. Each carries negative sampler charge at most `-q_-c_m(G)`, proving an unconditional adverse contribution of order

\[
c_m(G)\log G.
\]

## Why extra moment cancellation does not help

The proof never uses the specific `NB-157` Gamma-balance equation

\[
\sum_jc_j\log(t_j/G)=0.
\]

Nor does it depend on how many additional finite linear constraints the coefficients satisfy. It needs only:

- a fixed finite set of distinct positive polynomial exponents;
- zero total sampler mass;
- a positive top atom that carries the target lobe;
- bounded total variation relative to that top atom.

Thus one may add enough polynomial-height atoms to annihilate any fixed finite list of Stirling/Gamma moments and the same mechanism survives. Zero mass itself forces comparable negative atomic mass somewhere below `G`; polynomial separation isolates one such negative atom; ordinary zero density fills its local lobe.

This converts the specific reservoir observed in `NB-158` into a finite-dimensional method boundary. The issue is not failure to cancel enough universal completed-zeta background terms. It is that finite polynomial multiscale cancellation realizes those cancellations through isolated signed atoms at heights where zeta already supplies logarithmically many zeros.

## Stress test and exact boundary

The hypotheses are substantive and identify the remaining escapes rather than hiding them.

The argument does **not** cover a number of atoms `m=m_G` tending to infinity. In that regime the largest forced negative coefficient can fall to the `c_m/m_G` scale, and the accumulated cross-lobe geometry needs a different analysis.

It also does not cover exponents whose separations collapse with `G`. Then distinct Poisson lobes may overlap and no single negative atom need dominate a unit neighborhood. Likewise, if the smallest occupied exponent tends to zero, the adverse height may become subpolynomial and the unit-window zero count need not remain `Theta(log G)`.

A non-atomic signed height distribution can spread negative mass without exposing a single atomic lobe of the form used here, and an unbounded ratio `V_G/c_m(G)` can swamp the target normalization. Finally, the theorem says nothing against an architecture that couples signs to a Nyman/von-Mangoldt observable before reducing the zero side to separate positive and negative Poisson charges.

These are genuine changes of hypothesis. Merely adding finitely many polynomially separated balancing heights is not.

## Prior-art boundary

The load-bearing external theorem is only the Bellotti--Wong explicit zero-counting estimate already anchored in `SOURCES.md`. A focused prior-art audit against the literature on translates and signed combinations of Poisson kernels, logarithmic derivatives of zeta, and extremal Poisson-kernel explicit-formula bounds found the standard analytic ingredients but not this target-conditioned finite-polynomial-height reservoir statement.

No novelty is claimed for the Poisson kernel, zero-mass cancellation, or Riemann--von Mangoldt zero counting individually. The line-local contribution is the exact splice showing that boundedly conditioned finite polynomial multiscale samplers cannot obtain selection by satisfying more universal moment constraints. No new external theorem is needed, so `SOURCES.md` is unchanged.

## Consequence

`NB-158` ruled out one three-height construction. This result rules out the entire fixed-finite polynomial-height atomic version of that repair. In particular, the natural response "add more heights and cancel more Gamma/Stirling moments" cannot solve the adverse-reservoir problem while zero mass, bounded target conditioning, and fixed polynomial scale separation remain in force.

The signed route must now spend a genuinely different resource: a growing number of heights, collapsing/continuous vertical geometry, a subpolynomial adverse scale with a different zero-counting regime, deliberately worse conditioning accompanied by useful prime-side cancellation, or source-specific Nyman/von-Mangoldt coupling before sign separation. The finite polynomial moment-cancellation ladder itself is closed.