# NB-160 — Poisson-width sign separation forces a routine adverse zero reservoir

**Date:** 2026-09-16  
**Status:** EXACT-DERIVED + SOURCE-SPECIFIC + MEASURE-VALUED + TARGET-CONDITIONED + DECISIVE-METHOD-BOUNDARY

`NB-159` ruled out every fixed finite sampler on polynomially separated height atoms: zero total mass forces a lower negative atom, polynomial separation makes its Poisson lobe locally dominant, and a fixed-width Riemann--von Mangoldt count fills that lobe with `Omega(log G)` actual zeta zeros. The obvious remaining loophole was cardinality: perhaps a growing number of atoms, or even a continuous signed height distribution, could dilute every individual adverse lobe enough to avoid the reservoir.

That loophole is not real while the positive and negative Jordan supports remain separated by more than a sufficiently large fixed number of Poisson widths. Finiteness and atomicity were inessential in `NB-159`. The obstruction is instead geometric: a negative signed mass distribution at polynomial height automatically sees `Theta(log G)` zero density locally, while a separated positive distribution contributes only a `1/Delta` far-tail after summing over zeros. Thus any bounded-conditioning zero-mass sampler whose two sign supports stay uniformly separated already carries `Omega(log G)` adverse zeros, independently of whether either sign consists of one atom, growing cardinality, or a continuum.

## Claim

Fix `a>0`, a target-window radius `h>0`, a conditioning constant `C>=2`, and `theta_0>0`. For every sufficiently large `G`, let `nu_G` be a finite real signed Borel measure supported on

\[
[H_G,G],
\qquad
H_G\ge G^{\theta_0},
\]

with Jordan decomposition

\[
\nu_G=\nu_G^+-\nu_G^-.
\]

Assume:

1. zero total mass,
   \[
   \nu_G(\mathbb R)=0;
   \]
2. a distinguished positive top atom,
   \[
   \nu_G^+(\{G\})\ge c_G>0;
   \]
3. bounded conditioning,
   \[
   V_G:=\|\nu_G\|_{\rm TV}\le Cc_G;
   \]
4. separated Jordan supports,
   \[
   \Delta_G:=\operatorname{dist}(\operatorname{supp}\nu_G^+,\operatorname{supp}\nu_G^-)
   \ge\Delta_0.
   \]

For a nontrivial zeta zero `rho=beta+i gamma`, define

\[
Q_G(\rho)
:=
\int_{H_G}^{G}
\frac{1+a-\beta}{(1+a-\beta)^2+(\gamma-t)^2}
\,d\nu_G(t).
\]

There exists a fixed threshold

\[
\Delta_0=\Delta_0(a,h,C,\theta_0)
\]

such that every family satisfying the hypotheses with this separation has the following properties.

### 1. The target window keeps positive order-`c_G` charge

There is `q_+=q_+(a,h,C)>0` such that every nontrivial zero with

\[
|\gamma-G|\le h
\]

satisfies

\[
\boxed{Q_G(\rho)\ge q_+c_G.}
\]

### 2. The negative support generates an unconditional routine adverse reservoir

Put

\[
E_G:=\{\gamma>0:\operatorname{dist}(\gamma,\operatorname{supp}\nu_G^-)\le1\}.
\]

Then, independently of whether a special target packet exists near `G`,

\[
\boxed{
\sum_{\substack{\rho\ {m nontrivial}\\ \gamma\in E_G}}
(Q_G(\rho))_-
\gg_{a,C,\theta_0} c_G\log G.
}
\]

Moreover each individual zero contributes at most `O_{a,C}(c_G)` adverse charge, so

\[
\boxed{
\#\{\rho:\gamma\in E_G,\ Q_G(\rho)<0\}
=\Omega_{a,C,\theta_0}(\log G).
}
\]

Consequently allowing the number of sampling heights to grow, or replacing the atoms by arbitrary finite signed measures, does not repair the zero-mass exterior selector while the positive and negative Jordan supports remain separated by a sufficiently large fixed additive distance. Any surviving height-geometry escape must make the two signs interlace or collapse on the `O(1)` Poisson-width scale (or abandon one of the other hypotheses, such as bounded conditioning or polynomial lower height).

## Derivation

Write

\[
P_x(y):=\frac{x}{x^2+y^2},
\qquad
x:=1+a-\beta.
\]

For a nontrivial zero, `0<beta<1`, so

\[
a<x<a+1.
\]

Also, because `nu_G` has zero total mass, its Jordan masses agree:

\[
M_G^+:=\nu_G^+(\mathbb R)
=
\nu_G^-(\mathbb R)=:M_G^-,
\qquad
M_G^++M_G^-=V_G.
\]

Hence

\[
c_G\le M_G^-=M_G^+\le \frac C2c_G.
\]

### Target dominance does not use atomicity

Define the fixed positive constant

\[
m_h:=
\min_{a\le x\le a+1,\ |y|\le h}P_x(y)>0.
\]

If `|gamma-G|<=h`, the distinguished top atom contributes at least `m_h c_G`. Every point of the negative support is at distance at least `Delta_G` from `G`; therefore

\[
|\gamma-t|\ge\Delta_G-h
\qquad
(t\in\operatorname{supp}\nu_G^-).
\]

Using `P_x(y)<=(a+1)/y^2`,

\[
\int P_x(\gamma-t)\,d\nu_G^-(t)
\le
\frac{(a+1)M_G^-}{(\Delta_G-h)^2}
\le
\frac{C(a+1)c_G}{2(\Delta_G-h)^2}.
\]

All remaining positive mass only helps. Choosing `Delta_0>h+1` so that the final quantity is at most `m_hc_G/2` gives

\[
Q_G(\rho)\ge\frac{m_h}{2}c_G.
\]

Thus one may take `q_+=m_h/2`.

### Every negative mass element sees logarithmically many nearby zeros

Let

\[
m_1:=
\min_{a\le x\le a+1,\ |y|\le1}P_x(y)>0.
\]

The Bellotti--Wong explicit Riemann--von Mangoldt remainder already anchored in `SOURCES.md` gives, uniformly for large `t`,

\[
N(t+1)-N(t-1)
\ge
\left(\frac1\pi-0.20152+o(1)\right)\log t.
\]

Since `1/pi-0.20152>0`, there is a fixed `kappa_0>0` for which

\[
N(t+1)-N(t-1)\ge\kappa_0\log t
\]

throughout `[H_G,G]` once `G` is large. Because `H_G>=G^{theta_0}`,

\[
\log t\ge\theta_0\log G.
\]

For every fixed `t` in the negative support, all zeros with `|gamma-t|<=1` belong to `E_G`, and each carries negative raw Poisson potential at least `m_1`. Tonelli's theorem therefore gives

\[
\begin{aligned}
A_G^-
&:=
\sum_{\substack{\rho\\\gamma\in E_G}}
\int P_{1+a-\beta}(\gamma-t)\,d\nu_G^-(t)\\
&\ge
m_1\int
\bigl(N(t+1)-N(t-1)\bigr)
\,d\nu_G^-(t)\\
&\ge
m_1\kappa_0\theta_0\,M_G^-\log G.
\end{aligned}
\]

This is the measure-valued replacement for selecting one adverse atom in `NB-159`.

### Separated positive mass has only a `1/Delta_G` zero-summed tail

If `s` belongs to the positive support and `gamma in E_G`, then some `t` in the negative support satisfies `|gamma-t|<=1`. Hence

\[
|\gamma-s|\ge\Delta_G-1.
\]

A standard consequence of the same explicit zero-counting estimate is the uniform Poisson-tail bound

\[
\sum_{\substack{\rho\\\gamma>0,\ |\gamma-s|\ge R}}
P_{1+a-\beta}(\gamma-s)
\ll_a
\frac{\log G}{R},
\qquad
s\in[H_G,G],\quad 1\le R\le G.
\]

Indeed, partition the ordinates into unit intervals about `s`. Riemann--von Mangoldt gives `O(log(u+2))` zeros in each such interval, while `P_x(y)=O_a(y^{-2})`; summing the resulting `n^{-2}` tail from `n>=R` gives the displayed `1/R` factor. The part above height comparable with `G` is smaller and is absorbed by the same bound.

Taking `R=Delta_G-1`, the total positive cross-talk on the adverse set is therefore

\[
\begin{aligned}
A_G^+
&:=
\sum_{\substack{\rho\\\gamma\in E_G}}
\int P_{1+a-\beta}(\gamma-s)\,d\nu_G^+(s)\\
&\ll_a
\frac{M_G^+\log G}{\Delta_G-1}.
\end{aligned}
\]

Since `M_G^+=M_G^-`, choose the fixed separation threshold `Delta_0` still larger, if necessary, so that this upper bound is at most half of the lower bound for `A_G^-`. Then

\[
\sum_{\substack{\rho\\\gamma\in E_G}}Q_G(\rho)
=A_G^+-A_G^-
\le
-c_0M_G^-\log G
\]

for some `c_0=c_0(a,theta_0)>0`. Consequently

\[
\sum_{\substack{\rho\\\gamma\in E_G}}
(Q_G(\rho))_-
\ge
c_0M_G^-\log G
\ge
c_0c_G\log G.
\]

Finally, at any one zero,

\[
(Q_G(\rho))_-
\le
\int P_{1+a-\beta}(\gamma-t)\,d\nu_G^-(t)
\le
\frac{M_G^-}{a}
\le
\frac{C}{2a}c_G.
\]

Dividing the total adverse charge by this per-zero maximum forces `Omega(log G)` distinct adverse zeros.

## What this changes after NB-159

The fixed-cardinality hypothesis in `NB-159` was an artifact of the atomwise proof, not the actual boundary. The relevant geometric condition is separation of the two Jordan signs. Under bounded conditioning, a negative continuum cannot be made harmless by spreading it over more heights: every infinitesimal piece still samples a local zero density of order `log G`, and integration preserves that total cost. Conversely, the positive sign can only cancel this routine reservoir through its Poisson tails, whose zero-summed strength falls like `1/Delta_G`.

Therefore **growing cardinality by itself is no longer a live escape route**. Nor is replacing a finite atomic sampler by a continuous signed measure. A genuinely different height construction must put positive and negative mass within `O(1)` of one another often enough that the local zero populations are shared and the Jordan pieces cannot be estimated separately. That points specifically toward collapsing/interlaced sign geometry, rather than merely denser sampling on separated bands.

The result does not exclude such interlacing, does not treat lower heights with `log H_G=o(log G)`, and does not address ill-conditioned measures with `V_G/c_G` growing. It also deliberately takes absolute Jordan pieces on the zero side; a future argument that couples the signed sampler to the von Mangoldt/Nyman observable before this separation could exploit cancellation unavailable here.

## Source and prior-art audit

The load-bearing zero-density input is exactly the Bellotti--Wong explicit Riemann--von Mangoldt remainder already recorded in `SOURCES.md`; no new source is required. Titchmarsh remains the background source for the standard logarithmic-derivative/zero formalism used throughout this branch.

A fresh prior-art check found nearby but different Poisson-kernel frameworks: Bruna--Melnikov study completeness of translates of the Poisson kernel, while Chirre--Molero use Guinand--Weil together with extremal Poisson majorants/minorants to bound the logarithmic derivative of zeta on `Re(s)=1` under RH. Neither supplies the target-conditioned Jordan-support statement above, and neither is load-bearing for the proof. `SOURCES.md` therefore does not need an update.

## Boundary

This is a source-specific obstruction theorem for the present signed exterior-sampling architecture, not a theorem that rules out all Nyman--Beurling strategies. Its exact scope is: fixed horizontal offset, zero total signed mass, a positive top atom with bounded total-variation conditioning, polynomially high vertical support, and a sufficiently large fixed separation between positive and negative Jordan supports. Within that scope, atomicity and fixed cardinality are unnecessary.

The next unresolved geometric regime is now precise: **positive and negative supports separated by only `O(1)` Poisson widths, especially genuinely interlaced or collapsing configurations in which the same local zeros can see both signs at comparable strength**. That is the natural place to test whether signed cancellation can finally survive the routine zero background.