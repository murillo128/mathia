# FD-192 — Square-root-and-below dyadic Fourier nulls hide critical prime-extension energy

- **Date:** 2026-09-18
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** relational-observability obstruction / critical-band nullspace / prime-extension energy
- **Depends on:** FD-181, FD-189, FD-190, FD-191
- **Classification:** `EXACT-DERIVED + NULLSPACE-OBSTRUCTION + RELATION-ENERGY-BLINDNESS + CRITICAL-RATE-SEPARATION`

## Claim

`FD-190` and `FD-191` show that dyadic signed Farey Fourier bands through the square-root scale remain noninjective even after imposing strong coordinatewise Möbius fidelity. `FD-181` supplies the missing relational diagnostic: every fixed nonzero coefficient perturbation on the physical-prime fibre emits prime-extension multiplicativity energy of order `x/log x`.

Together they imply an exact observation-side no-go at the same rate that makes the relation energy rigid.

Fix

\[
0<\alpha\le\frac12,
\qquad
1\le q<\infty,
\qquad
0<\varepsilon<1,
\tag{1}
\]

and any prescribed finite prefix `X`. Then there exist composite squarefree integers

\[
X<u<v
\tag{2}
\]

and a real source

\[
a_\varepsilon(n)
=
\begin{cases}
\mu(u)+\varepsilon,&n=u,\\
\mu(v)-\varepsilon,&n=v,\\
\mu(n),&n\ne u,v,
\end{cases}
\tag{3}
\]

such that all of the following hold.

First, the complete dyadic signed Fourier-band history is **exactly** the Möbius history:

\[
\boxed{
\mathcal F_{2^m}^{a_\varepsilon}(k)
=
\mathcal F_{2^m}^{\mu}(k)
\qquad
(m\ge0,\ 1\le k\le 2^{\alpha m}).
}
\tag{4}
\]

Second, the coefficient perturbation is as small as possible up to cardinality:

\[
\boxed{
D_{a_\varepsilon,q}(x)
:=
\sum_{n\le x}|a_\varepsilon(n)-\mu(n)|^q
=2\varepsilon^q
\qquad(x\ge v).
}
\tag{5}
\]

In particular `D_(a_epsilon,q)(x)=o(x)`, while all primes retain `a(p)=-1`, all nonsquarefree coefficients remain zero, every squarefree coefficient retains the Möbius sign, and the source differs from Möbius at exactly two composite coordinates beyond the chosen prefix.

Nevertheless its true prime-extension multiplicativity energy from `FD-181`,

\[
\mathcal M_{a,q}(x)
:=
\sum_{\substack{n,pn\le x\\
\mu^2(n)=\mu^2(pn)=1\\
p\text{ prime}}}
|a(pn)-a(p)a(n)|^q,
\tag{6}
\]

satisfies the sharp fixed-support asymptotic

\[
\boxed{
\mathcal M_{a_\varepsilon,q}(x)
=
\left[
\varepsilon^q\!\left(\frac1u+\frac1v\right)+o(1)
\right]
\frac{x}{\log x}.
}
\tag{7}
\]

Thus a source can be **exactly invisible** to every retained signed Farey mode at every dyadic horizon while carrying a positive prime-extension defect at precisely the `x/log x` scale that `FD-181`, `FD-186` and `FD-187` identify as the rigidity threshold.

Equivalently, if

\[
Y_\alpha(a)
:=
\left(
\mathcal F_{2^m}^{a}(k)-\mathcal F_{2^m}^{\mu}(k)
\right)_{m\ge0,\ 1\le k\le2^{\alpha m}},
\tag{8}
\]

then `Y_alpha(a_epsilon)=0` but

\[
\lim_{x\to\infty}
\frac{\log x}{x}\,
\mathcal M_{a_\varepsilon,q}(x)
=
\varepsilon^q\!\left(\frac1u+\frac1v\right)>0.
\tag{9}
\]

Consequently **no deterministic post-processing of the complete square-root-or-smaller dyadic signed band can uniformly certify**

\[
\mathcal M_{a,q}(x)=o(x/\log x)
\tag{10}
\]

on this squarefree, prime-faithful, sign-faithful class. This remains true even after separately assuming the coefficient-amplitude condition `D_(a,q)(x)=o(x)` used with the relation energy in `FD-188`.

## 1. The null source exists on both sides of the critical endpoint

For `0<alpha<1/2`, `FD-190` proves that after any prescribed finite prefix there is an interval disjoint from the complete dyadic quotient-coordinate coverage

\[
\mathcal Q_\alpha
=
\left\{
\left\lfloor\frac{2^m}{k}\right\rfloor:
 m\ge0,
 1\le k\le2^{\alpha m}
\right\}
\tag{11}
\]

containing at least two composite squarefree coordinates `u<v`. The two-point perturbation (3) has cumulative perturbation supported only between `u` and `v-1`, entirely inside that unsampled interval. Divisor Möbius inversion of the signed Fourier coordinate therefore gives (4).

At the endpoint `alpha=1/2`, `FD-191` proves something stronger. Near every sufficiently large dyadic endpoint it constructs `Omega(sqrt X)` exact quotient holes `u` for which **both** `u` and `u+1` are composite squarefree. Taking

\[
v=u+1
\tag{12}
\]

makes the cumulative perturbation a single spike at the unsampled coordinate `u`, so the complete critical band again satisfies (4).

In both cases the source changes only the two increments in (3). Because `0<epsilon<1`, the signs of `mu(u)` and `mu(v)` are preserved regardless of their parities of prime-factor rank. Neither coordinate is prime, so every prime remains exactly physical. Equation (5) follows immediately.

The endpoint result matters here because the earlier formal Mersenne hole from `FD-189` was not enough: it did not preserve the squarefree physical fibre. `FD-191` supplies precisely the arithmetic-admissible two-coordinate collision needed for the relation-energy comparison.

## 2. Two invisible coefficient errors still emit full prime fans

Write

\[
\delta(n):=a_\varepsilon(n)-\mu(n).
\tag{13}
\]

For the source (3),

\[
\delta(u)=\varepsilon,
\qquad
\delta(v)=-\varepsilon,
\qquad
\delta(n)=0\quad(n\notin\{u,v\}).
\tag{14}
\]

Its support is finite, all prime coordinates are fixed, and the perturbation amplitudes are bounded. It therefore lies in the sharp fixed-prime regime of `FD-181`, where

\[
\mathcal M_{a,q}(x)
=
(C_{\delta,q}+o(1))\frac{x}{\log x},
\qquad
C_{\delta,q}
=
\sum_{\delta(n)\ne0}\frac{|\delta(n)|^q}{n}.
\tag{15}
\]

Here the constant is explicit:

\[
C_{\delta,q}
=
\varepsilon^q\left(\frac1u+\frac1v\right),
\tag{16}
\]

which proves (7)--(9).

The mechanism is worth keeping visible. For almost every fresh prime `p`, neither `p` nor `pu` is modified, so the edge `u -> pu` has defect exactly `epsilon`; the same holds with magnitude `epsilon` for the fan emitted by `v`. Only finitely many exceptional children or divisibility coincidences can affect lower-order terms. The Fourier-band cancellation between the two changed increments therefore does **not** cancel their relational defects: the band sees cumulative quotient samples, whereas prime-extension energy tests cross-coordinate consistency edge by edge.

Using the edge count from `FD-181`,

\[
|E_x|
=
\frac{x}{\zeta(2)}\log\log x+O(x),
\tag{17}
\]

the same example has normalized relation defect

\[
\left(
\frac{\mathcal M_{a_\varepsilon,q}(x)}{|E_x|}
\right)^{1/q}
=
\left[
\frac{\zeta(2)\varepsilon^q(1/u+1/v)+o(1)}
{\log x\,\log\log x}
\right]^{1/q}.
\tag{18}
\]

So the invisible source lands exactly on the rate separator already isolated by `FD-180`--`FD-181`; it is not merely a source with some unspecified nonzero relation error.

## 3. Data-only control cannot cross the rigidity threshold

Let `Phi_x` be any proposed nonnegative upper-control functional depending only on the complete retained band data `Y_alpha(a)` and suppose one wants

\[
\mathcal M_{a,q}(x)
\le
\Phi_x(Y_\alpha(a))
\tag{19}
\]

uniformly over the coordinatewise physical class above. The Möbius source and `a_epsilon` have exactly the same data, namely `Y_alpha=0`. Applying (19) to `a_epsilon` and using (7) forces

\[
\boxed{
\liminf_{x\to\infty}
\frac{\log x}{x}\,
\Phi_x(0)
\ge
\varepsilon^q\left(\frac1u+\frac1v\right)>0.
}
\tag{20}
\]

Hence `Phi_x(0)=o(x/log x)` is impossible. This statement is information-theoretic: allowing nonlinear estimators, adaptive algebra after acquisition, different norms on the retained coefficient vector, or arbitrarily expensive computation cannot help because the two sources have literally identical input data.

The obstruction is stronger than `FD-182`, which established the same qualitative separation for the much poorer dyadic midpoint ladder using an infinite sparse null source. Here the observation family contains **every signed Fourier mode through the sharp square-root cutoff**, while the indistinguishable source differs from Möbius at only two composite squarefree coordinates and can be made arbitrarily close to Möbius by sending `epsilon` to zero.

This also explains why the coefficient-mass currency from `FD-188` does not rescue the band. Equation (5) already gives `D_(a_epsilon,q)(x)=o(x)`. The missing hypothesis in the `D+M` rigidity mechanism is therefore exactly the relation-energy control, and (20) shows that the critical dyadic band cannot supply it by post-processing alone.

## Representation audit

No stronger source observable is inserted into the acquisition model. The only observed data are the signed dyadic Fourier coordinates already classified by `FD-189`--`FD-191`, and those data are identical for the two sources. The prime-extension energy is used only **afterward as a diagnostic** of what the observation kernel can hide.

This distinction is important. Replacing the band by the relation energy itself would be an added source-side observable and would evade the question by construction. Here the argument instead intersects the exact Farey-band kernel with the independently established source-side rigidity currency. The positive value (9) therefore measures a genuine blind direction of the specified Farey observation family.

The construction remains deliberately nonmultiplicative. Exact multiplicativity is a cross-coordinate restriction, and `FD-172`--`FD-174` already show that it can rigidify much thinner temporal data. The present theorem says only that **coordinatewise** restrictions—squarefree support, exact primes, exact signs, bounded amplitudes, finite support and vanishing normalized coefficient mass—cannot make the square-root-or-smaller dyadic Fourier band control multiplicativity defect.

## Prior-art and novelty boundary

The divisor/Fourier equivalence of the Farey field is already internal to `FD-117` and rests on the classical Ramanujan-sum shell arithmetic anchored in `SOURCES.md`. The prime-fan asymptotic is already proved in `FD-181` from the prime number theorem. No new external theorem is load-bearing here.

A targeted literature search for a Farey Fourier-band nullspace coupled to multiplicativity-defect energy, or for a square-root dyadic Farey observation theorem controlling prime-extension consistency, did not surface a matching result. Generic nullspace indistinguishability principles from inverse problems are of course classical and are not a novelty claim. The line-local contribution is the exact composition of the arithmetic-admissible band kernel from `FD-190`--`FD-191` with the critical `x/log x` relation-energy law from `FD-181`.

`SOURCES.md` is therefore unchanged.

## Boundary conditions and failure modes

The no-go concerns the **complete dyadic signed initial Fourier band** `k<=H^alpha` for `alpha<=1/2`. It does not cover non-dyadic horizon schedules, sparse high-frequency selections outside the initial band, consecutive-horizon denominator-shell measurements, or another Farey statistic that directly couples coordinates. Those are precisely ways to alter the observation family rather than post-process the same null data.

For `alpha>1/2`, `FD-189` tail-recovers the source from the complete dyadic band; once the remaining finite prefix is fixed, exact source nonidentifiability disappears. That is an identifiability statement only. It gives no stable estimate for `M_(a,q)`, no useful noise modulus, and no RH-critical Franel--Landau bound.

The constant in (7) depends on the chosen hidden coordinates and can be made small by placing them very far out. This does not weaken the rate obstruction: after the source is fixed, the coefficient is a strictly positive constant and the relation energy remains asymptotic to that constant times `x/log x`. No uniform positive constant over all possible prefixes is claimed.

Finally, exact invisibility of a synthetic source does not assert that the physical Möbius source itself has large relation energy—it has zero. The theorem classifies what can be inferred **from the retained observation data over the stated admissible source class**.

## Research consequence

`FD-191` closed the last coordinatewise-fidelity loophole at the square-root endpoint. The present result closes the corresponding **relation-control loophole**: even the complete critical signed band cannot certify the subcritical prime-extension energy required by the source-side rigidity theorems, despite the competing source having only `O(1)` coefficient discrepancy.

The next observation-side step therefore cannot be a better estimator, nonlinear decoder, or norm applied to the same dyadic band. It must change at least one structural ingredient: the horizon schedule, the frequency-selection geometry, or the admissible source relations. The most relevant target remains a genuinely relation-sensitive Farey acquisition rule whose kernel excludes these two-coordinate squarefree nulls without simply reconstructing the entire source prefix.

## Related findings

- `FD-181` — sparse signed perturbations have an `x/log x` prime-extension defect floor, with a sharp fixed-prime asymptotic.
- `FD-182` — exact dyadic midpoint null data do not control prime-extension multiplicativity.
- `FD-187` — physical-prime defects have rank-uniform divisor-cube coercivity.
- `FD-188` — subcritical relation energy plus sublinear coefficient mass gives the moved-prime rigidity currency.
- `FD-189` — signed dyadic Fourier bands have a sharp square-root tail-recovery threshold on formal sources.
- `FD-190` — strict sub-square-root bands remain null under prime/sign/squarefree fidelity.
- `FD-191` — the critical square-root endpoint still has a large arithmetic-admissible nullspace.
