---
id: WP-388
title: Strongly local boundary diffusions collapse to unit-cell invisibility
branch: weil_positivity
status: supported
kind: pointed-boundary-strongly-local-domain-obstruction
claim_strength: exact RH-independent source-specific no-go showing that a regular strongly local one-dimensional Dirichlet form with fully supported Radon speed measure cannot both resolve integer interfaces and admit even one squarefree mixed-prime WP-384 boundary shell; if it admits the shell family, every effective interval is confined to a floor unit cell and the strongly local energy vanishes on all arithmetic shells
created: 2026-09-20
related: [WP-009, WP-381, WP-382, WP-383, WP-384, WP-386, WP-387]
clues: [CLUE-weil-positivity-noncharacter-finite-archimedean-incidence]
prior_art:
  - Li--Ying representation theorem for regular strongly local one-dimensional Dirichlet forms by effective intervals and scale functions, arXiv:1701.02411
  - classical Beurling--Deny decomposition of regular symmetric Dirichlet forms
  - classical identity mu * log = Lambda
---

# WP-388 — Strongly local boundary diffusions collapse to unit-cell invisibility

## Claim

`WP-387` classified the jump and killing sectors of the Beurling--Deny decomposition on the exact `WP-384` boundary carrier, leaving a strongly local diffusion/interface term as the canonical Markovian escape. On the same carrier, that escape is also obstructed, for a reason stronger than mixed-shell nullity.

For

\[
h_m(x)=\frac1{\sqrt m}\sum_{d\mid m}\mu(m/d)
\left(H_{\lfloor x/d\rfloor}-\log(x/d)-\gamma\right),
\qquad m>1,
\tag{1}
\]

let `(E,F)` be a regular strongly local Dirichlet form on `L^2((0,infinity),rho)` with `rho` a fully supported Radon measure. Suppose at least one squarefree mixed shell `h_{pq}`, with distinct primes `p,q`, belongs to `F`.

Then no effective interval of the one-dimensional diffusion can cross a positive integer. Consequently every effective interval is confined to one floor unit cell. Since every `h_m` is constant on each such cell, every shell that belongs to `F` has zero strongly local energy:

\[
\boxed{\mathcal E(h_m,h_n)=0}
\tag{2}
\]

whenever `h_m,h_n in F`.

Equivalently, a source-forced regular one-dimensional strongly local Markov geometry faces an exact dichotomy:

\[
\boxed{
\text{cross an integer interface}\Longrightarrow h_{pq}\notin\mathcal F,
\qquad
h_{pq}\in\mathcal F\Longrightarrow
\text{all shell energy is zero}.
}
\tag{3}
\]

Thus the strongly local sector cannot supply the missing interface-sensitive positive form for the `WP-384` carrier. It either excludes the arithmetic profiles whose response it is meant to measure or becomes arithmetically invisible on them.

**Classification:** `EXACT-DERIVED + RH-INDEPENDENT + STRONGLY-LOCAL-DIRICHLET-CLASSIFICATION + DOMAIN-ADMISSIBILITY-OBSTRUCTION + EVERY-INTEGER-MIXED-SHELL-JUMP + UNIT-CELL-RIGIDITY + DIFFUSION-ARITHMETIC-BLINDNESS + MATCHED-CONTROLS + DECISIVE-NEGATIVE + NOT-A-WEIL-BRIDGE`.

## 1. The boundary shells jump only at integers, but a fixed mixed shell jumps at every integer

As in `WP-387`, divisor cancellation gives

\[
\boxed{
h_m(x)=\frac1{\sqrt m}
\left(
\Lambda(m)+\sum_{d\mid m}\mu(m/d)H_{\lfloor x/d\rfloor}
\right).
}
\tag{4}
\]

Hence every shell is constant on each open unit cell `(n,n+1)`. Its jump at a positive integer `k` is exactly

\[
\Delta_k h_m
=\frac1{k\sqrt m}
\sum_{\substack{d\mid m\\ d\mid k}}
\mu(m/d)d.
\tag{5}
\]

For a squarefree mixed shell `m=pq`, multiplicativity makes the numerator

\[
\sum_{d\mid\gcd(k,pq)}\mu(pq/d)d.
\tag{6}
\]

There are only four possible gcds. The corresponding values are

\[
1,\qquad 1-p,\qquad 1-q,\qquad (p-1)(q-1),
\tag{7}
\]

and none is zero. Therefore

\[
\boxed{\Delta_k h_{pq}\ne0\quad\text{for every integer }k\ge1.}
\tag{8}
\]

This is stronger than the fresh-prime separation used in `WP-386` and `WP-387`: no family quantifier is needed. One fixed mixed shell detects every integer interface by an actual discontinuity.

## 2. One-dimensional strongly local forms are continuous on effective intervals

The required general structure is classical. Li and Ying, *On symmetric one-dimensional diffusions*, arXiv:1701.02411, Theorem 2.1, represent a regular strongly local Dirichlet form on an interval with fully supported Radon speed measure by at most countably many disjoint effective intervals. Each effective interval carries a continuous strictly increasing scale function `s`; a domain function restricted to that interval is absolutely continuous with respect to `s`, and the energy is the sum of the squared scale derivatives. See https://arxiv.org/abs/1701.02411 .

In particular, every domain function has a continuous version on the interior of each effective interval. A jump discontinuity cannot be repaired by changing the function at the jump point: the left and right limits remain different.

Now assume `h_{pq} in F`. If an effective interval contained points on both sides of a positive integer `k`, then `k` would be an interior point of that interval and the restriction of `h_{pq}` would have to be continuous there. Equation (8) contradicts this. Hence

\[
\boxed{
\text{no effective interval intersects both }(k-1,k)\text{ and }(k,k+1)
\quad(k\ge1).
}
\tag{9}
\]

Every effective interval is therefore contained in the closure of a single floor unit cell. Endpoint conventions do not affect the energy conclusion below.

## 3. Domain admissibility forces zero arithmetic diffusion energy

Equation (4) shows that every shell `h_m` is constant on the interior of each unit cell. By (9), it is therefore constant on the interior of every effective interval. Its derivative with respect to the corresponding continuous scale function is zero almost everywhere. The Li--Ying representation then gives

\[
\mathcal E(h_m,h_m)=0
\tag{10}
\]

for every shell `h_m in F`. Polarization yields (2) for every pair of admitted shells.

This makes the obstruction a **domain theorem**, not another nullity theorem. `WP-387` assumed zero energy on all mixed shells and deduced where a jump measure could live. Here no mixed-shell zero-energy hypothesis is imposed. Merely requiring one fixed mixed shell to be in the domain already prevents every effective diffusion interval from crossing every arithmetic interface. Once that happens, the entire shell family is invisible to the strongly local energy.

For a candidate intended to evaluate the full arithmetic boundary family, the conclusion is unavoidable: either some shell profiles are not in its form domain, in which case the geometry does not define the proposed arithmetic response, or they are in the domain and the strongly local contribution is identically zero on them.

## 4. Matched controls and sharpness

The obstruction is not claiming that the strongly local form itself must vanish. Nontrivial diffusion geometry may live inside any collection of unit cells. The shell profiles simply cannot see it because they are exactly constant there. A Brownian or scale-changed diffusion confined to `(n,n+1)` is therefore a sharp positive control: it has nonzero energy on general varying functions while all admitted arithmetic shell restrictions have zero derivative.

Conversely, any effective interval that genuinely crosses one integer is an immediate negative control for shell-domain admissibility. Equation (8) says the same fixed `h_{pq}` jumps at that integer, so it cannot have the required continuous effective-interval representative. No asymptotic estimate or global cancellation is involved.

The result also survives bounded-window controls. On any interval containing an integer in its interior, the same local discontinuity excludes `h_{pq}` from a strongly local effective component that crosses that interface. Thus the obstruction is not created by an infinite-volume limit.

The assumptions are deliberately narrow and testable. Regularity, strong locality, one-dimensional interval state space, a fully supported Radon speed measure, and actual form-domain admission are all used. Dropping the Markov/strong-local structure, changing the carrier before the continuum limit, or using a genuinely off-diagonal positive kernel not arising as a Dirichlet diffusion are not ruled out.

## 5. Relation to WP-386 and WP-387

`WP-386` showed that arbitrary positive pointwise-local killing measures compatible with mixed-shell nullity collapse to support in `(0,1)`, leaving only the rank-one Mangoldt ray. `WP-387` then showed that positive pure-jump Dirichlet conductances compatible with mixed-shell nullity must stay within unit cells and hence vanish on every shell.

The present result closes the remaining canonical Beurling--Deny sector on the same continuum carrier. It is not obtained by adding the hypotheses of those two findings. The strongly local obstruction is strictly earlier: the discontinuity of a single mixed shell conflicts with diffusion continuity before any requirement that mixed shells have zero energy.

Taken together, the three findings classify the natural Markovian positive completion of the `WP-384` boundary profiles. The killing sector leaves at most the Mangoldt rank-one line, the jump sector becomes shell-invisible, and the strongly local sector either excludes the carrier or becomes shell-invisible. Therefore a full regular Dirichlet-form completion cannot manufacture the missing independent finite-place/archimedean coordinates needed for a global Weil positivity bridge.

## 6. Prior-art and novelty audit

No novelty is claimed for the one-dimensional diffusion representation theorem. Li--Ying's effective-interval/scale-function classification is standard prior art for the strongly local side of the argument, just as Beurling--Deny is standard prior art for decomposing a regular Dirichlet form.

The source-specific step is the exact arithmetic identity (8): for the `WP-384` harmonic-floor carrier, one fixed squarefree mixed shell jumps at **every** positive integer. Combining that identity with the effective-interval theorem forces all diffusion intervals into floor cells and then annihilates the entire arithmetic family because all shells are cellwise constant.

A targeted literature check found the general one-dimensional Dirichlet-form classification but no treatment of these Nyman--Beurling/Mobius harmonic-floor profiles producing this domain-admissibility corollary. The novelty claim is therefore only this narrow application. It is not a new theorem about general strongly local forms and not a new RH criterion.

The conclusion is also independent of RH, zeta zeros, a zero-defined spectrum, regularized determinants, or a hand-picked kernel. It is a negative geometric obstruction obtained before any Weil explicit-formula comparison.

## Consequence for the research line

The most natural Markovian boundary escape left by `WP-387` is closed. A strongly local one-dimensional interface energy cannot use the integer jumps of the source profiles: if it crosses those interfaces, the profiles are outside its domain; if it admits them, its effective intervals cannot cross the interfaces and its shell energy is zero.

This materially narrows the live boundary routes. The surviving possibilities must leave at least one hypothesis used here: a canonical non-Markov positive off-diagonal form, a finite-`q` prelimit structure whose states are not the discontinuous `WP-384` continuum profiles, or a finite--archimedean assembly in which the final positive form only emerges after coupling sectors rather than from a standalone positive boundary Dirichlet component.

## Conclusion

The `WP-384` boundary carrier is too discontinuous for a one-dimensional strongly local diffusion to read its arithmetic interfaces. A single squarefree mixed shell jumps at every positive integer. The effective-interval representation therefore forces any strongly local form admitting that shell to break at every unit boundary, exactly where every arithmetic profile becomes constant.

The resulting diffusion energy is zero on every admitted shell. Together with `WP-386` and `WP-387`, this removes the full canonical Beurling--Deny Markov completion of the continuum boundary carrier as a source of the missing global Weil-type positive geometry.