# NB-158 — Polynomial-depth Gamma balancing keeps target charge but imports a routine adverse reservoir

**Date:** 2026-09-16  
**Status:** DERIVED + SOURCE-SPECIFIC + GAMMA-BALANCED + TARGET-CONDITIONED + ZERO-COUNTED + METHOD-BOUNDARY

`NB-157` showed that the macroscopic completed-Gamma cost is only a rank-one signed log-height moment and exhibited a three-height sampler that cancels it exactly. It left one load-bearing caveat open: the construction did not certify that the sampler retains useful charge on a target packet near height `G`; its normalized conditioning could in principle diverge.

That caveat can be closed for the explicit polynomial-depth construction. The same three-height sampler has uniformly positive `O(1)` charge on every zero in a bounded vertical window around `G`, while its total variation and boundary-normalized conditioning stay bounded. However, this does **not** produce a selector. The negative middle-height atom creates a fixed-width adverse lobe around `G^{theta_2}`, and the explicit Riemann--von Mangoldt remainder already guarantees `Theta(log G)` actual zeta zeros in that lobe for every sufficiently large `G`. Thus Gamma balancing can be target-well-conditioned, but it imports a routine logarithmic zero reservoir that can absorb the target-scale signed debt.

## Claim

Fix

\[
0<\theta_1<\theta_2<1,
\qquad a>0,
\qquad h>0.
\]

Set

\[
t_1=G^{\theta_1},
\qquad t_2=G^{\theta_2},
\qquad t_3=G,
\]

and sample at

\[
w_j=a+i(t_j-G).
\]

Use the `NB-157` coefficients

\[
c_1=1-\theta_2,
\qquad
c_2=-(1-\theta_1),
\qquad
c_3=\theta_2-\theta_1,
\]

with signed atomic measure

\[
\mu_G=\sum_{j=1}^3 c_j\delta_{w_j}.
\]

For a nontrivial zero `rho=beta+i gamma`, define

\[
Q_G(\rho)
:=
\Re\int\frac{d\mu_G(w)}{1+w+iG-\rho}.
\]

Then:

1. `mu_G` has zero mass and is exactly Gamma-balanced,

\[
\sum_jc_j=0,
\qquad
\sum_jc_j\log(t_j/G)=0,
\]

while

\[
V_G:=\|\mu_G\|_{\rm TV}=2(1-\theta_1).
\]

2. There is a constant

\[
q_+=q_+(a,h,\theta_1,\theta_2)>0
\]

such that, for all sufficiently large `G`, every nontrivial zero satisfying

\[
|\gamma-G|\le h
\]

obeys

\[
\boxed{Q_G(\rho)\ge q_+.}
\]

Hence any target packet in a bounded, and in particular polynomially shrinking, vertical window around `G` has uniformly bounded sampler conditioning:

\[
C_G:=\frac{V_G}{q_+}=O_{a,h,\theta_1,\theta_2}(1),
\qquad
D_G:=\frac{C_G}{a}=O(1),
\qquad
J_G=0.
\]

3. There is also a constant

\[
q_-=q_-(a,\theta_1,\theta_2)>0
\]

such that every nontrivial zero with

\[
|\gamma-t_2|\le1
\]

satisfies, for all sufficiently large `G`,

\[
\boxed{Q_G(\rho)\le-q_-.}
\]

Moreover the Bellotti--Wong explicit zero-counting remainder already anchored in `SOURCES.md` gives

\[
\boxed{
N(t_2+1)-N(t_2-1)
\ge
\left(\frac1\pi-0.20152+o(1)\right)\log t_2.
}
\]

Since

\[
\frac1\pi-0.20152=0.116789886\ldots>0,
\]

the middle lobe contains

\[
\boxed{\Omega(\log t_2)=\Omega(\log G)}
\]

actual positive-ordinate zeta zeros unconditionally. Its negative zero charge is therefore already `Omega(log G)` before any hypothesis about a target packet at height `G` is imposed.

Consequently the target-conditioning loophole left by `NB-157` is not the obstruction for this three-height family. The obstruction is instead that exact Gamma balancing purchases its cancellation by coupling the target scale to a lower-height negative lobe that ordinary zero density fills at precisely the logarithmic scale needed by the signed conservation law.

## Derivation

Write

\[
P_x(y):=\frac{x}{x^2+y^2},
\qquad
x:=1+a-\beta.
\]

For every nontrivial zeta zero, `0<beta<1`, hence

\[
a<x<a+1.
\]

The charge is exactly

\[
Q_G(\rho)
=
\sum_{j=1}^3 c_j P_x(\gamma-t_j).
\]

The two balancing identities are immediate:

\[
c_1+c_2+c_3=0
\]

and

\[
\sum_jc_j\theta_j=0,
\qquad \theta_3=1.
\]

Therefore

\[
\sum_jc_j\log(t_j/G)
=
\log G\sum_jc_j(\theta_j-1)
=0.
\]

Because `c_1,c_3>0` and `c_2<0`,

\[
V_G=c_1-c_2+c_3=2(1-\theta_1).
\]

For the target window `|gamma-G|<=h`, both lower sampling heights are at distance `(1+o(1))G`. Uniformly in `beta`,

\[
c_1P_x(\gamma-t_1)+c_2P_x(\gamma-t_2)=O_{a,h,\theta_1,\theta_2}(G^{-2}),
\]

so

\[
Q_G(\rho)
=(\theta_2-\theta_1)P_x(\gamma-G)+O(G^{-2}).
\]

Let

\[
m_+(a,h)
:=
\min_{a\le x\le a+1,\ |y|\le h}P_x(y)>0.
\]

Then for all sufficiently large `G`,

\[
Q_G(\rho)
\ge
\frac{\theta_2-\theta_1}{2}m_+(a,h)
=:q_+>0.
\]

This includes the microscopic cells of `NB-144`, because any window `h_G=G^{-B}` is eventually contained in the fixed window `|gamma-G|<=h`.

Now move to the middle sampling height. If `|gamma-t_2|<=1`, then

\[
|\gamma-t_1|=(1+o(1))t_2,
\qquad
|G-\gamma|=(1+o(1))G.
\]

Thus the two positive atoms contribute only

\[
c_1P_x(\gamma-t_1)+c_3P_x(\gamma-G)
=O_{a,\theta_1,\theta_2}(G^{-2\theta_2})+O(G^{-2}),
\]

whereas the negative middle atom remains order one. With

\[
m_-(a)
:=
\min_{a\le x\le a+1,\ |y|\le1}P_x(y)>0,
\]

we obtain

\[
Q_G(\rho)
\le
-\frac{1-\theta_1}{2}m_-(a)
=: -q_-<0
\]

for all sufficiently large `G`.

It remains to count the zeros that are forced into this adverse lobe independently of the target. Write

\[
M(T):=\frac{T}{2\pi}\log\frac{T}{2\pi e}.
\]

The Bellotti--Wong estimate recorded in `SOURCES.md` is

\[
|N(T)-M(T)|
\le
0.10076\log T
+0.24460\log\log T
+8.08344.
\]

For fixed unit displacement,

\[
M(T+1)-M(T-1)
=
\frac1\pi\log T+O(1).
\]

Subtracting the two endpoint errors gives

\[
N(T+1)-N(T-1)
\ge
\left(\frac1\pi-2(0.10076)+o(1)\right)\log T.
\]

The leading coefficient is positive. Taking `T=t_2=G^{theta_2}` yields

\[
N(t_2+1)-N(t_2-1)
\ge
(0.116789886\ldots+o(1))\theta_2\log G.
\]

Every one of these zeros lies in the uniformly negative middle lobe, so that lobe alone carries at least

\[
q_-(0.116789886\ldots+o(1))\theta_2\log G
\]

of adverse charge.

## Stress test

This result does not contradict the conservation theorem in `NB-157`; it explains concretely how its adverse charge can be paid. The top atom retains an order-one target charge, and the entire sampler has `J_G=0` and `D_G=O(1)`, so a target packet of `kappa log G` zeros activates the strongest bounded-conditioning form of the `NB-157` debt estimate. But the three-height construction has simultaneously manufactured a lower-height negative lobe whose occupancy is already `Theta(log G)` from unconditional zero counting alone.

The lower packet is therefore **not** a rare event forced by the target packet. A fixed-width interval around `t_2` contains logarithmically many zeros for every sufficiently large `t_2` under the current explicit Riemann--von Mangoldt remainder. The three-height sampler can transfer signed mass between the two scales without creating a contradiction or a new exceptional zero statistic.

This also blocks an iteration mirage. One might read the `NB-157` adverse-packet conclusion as a descent from `G` to `G^{theta_2}` and attempt to repeat it. But logarithmic occupancy in a fixed-width interval at the lower height is already routine; iterating that statement only walks through an unconditional background law. A useful descent would have to preserve a rarer feature of the target, such as its microscopic horizontal localization or a genuinely source-specific Nyman defect, not merely the total number of zeros.

## Prior-art boundary

The load-bearing external input is only the explicit Bellotti--Wong zero-counting remainder already anchored in `SOURCES.md`. The Poisson/logarithmic-derivative and Guinand--Weil literature audited for `NB-150`--`NB-157`, together with a fresh focused search for multihight signed Poisson differences and Gamma cancellation, contains the standard explicit-formula mechanisms but did not reveal this target-conditioned three-height splice. No new external theorem is needed, so `SOURCES.md` requires no change.

The algebraic Gamma cancellation and the target/adverse kernel estimates are line-local derivations. The statement should not be read as a new zero-spacing theorem: the lower adverse reservoir is deliberately certified by existing zero-counting information.

## Consequence

`NB-157` left open whether exact Gamma balance at polynomially separated heights might be unusable because the target charge collapses. It does not: one can cancel the leading Gamma moment while keeping `q_G`, `C_G`, and `D_G` uniformly controlled on the same microscopic target cells used by the current confluence route.

What fails is **selection**, not conditioning. The price of this particular Gamma-balanced geometry is a negative atom at an intermediate polynomial height, and a unit neighborhood of that atom is already populated by `Theta(log G)` real zeta zeros. Thus the next signed escape cannot be justified merely by adding enough height degrees of freedom to cancel the Gamma background. It must also prevent the compensating negative charge from landing in a routine zero reservoir, preserve the target's horizontal/microscopic structure through the sign change, or couple the sampler to the Nyman/von-Mangoldt observable before the zero charge is separated by sign.
