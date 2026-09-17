# FD-186 — Prime detour cycles make physical-prime subcritical energy rigid

- **Date:** 2026-09-18
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** relational source rigidity / prime-detour cycle certificate / physical-prime classification / critical-energy lower bound
- **Depends on:** FD-181, FD-184, FD-185
- **Classification:** `EXACT-DERIVED + RELATIONAL-RIGIDITY + PRIME-DETOUR-CYCLE + PHYSICAL-PRIME-CLASSIFICATION`

## Claim

`FD-184` propagated one fixed coefficient defect through every fixed almost-prime rank and left growing-rank uniformity as the main source-side obstacle. That detour is unnecessary. The squarefree prime-extension graph contains a finite family of alternate paths which compares any changed composite directly with the unchanged prime layer. Repeating that finite certificate over fresh prime labels already costs the full critical `x/log x` energy scale.

Let `a` be a real-valued arithmetic source satisfying

\[
a(1)=1,
\qquad
a(n)=0\quad\text{whenever }\mu(n)=0,
\qquad
a(p)=-1\quad(p\text{ prime}).
\tag{1}
\]

For fixed `1<=q<infinity`, define

\[
\mathcal M_{a,q}(x)
:=
\sum_{(n,pn)\in E_x}
|a(pn)-a(p)a(n)|^q,
\tag{2}
\]

with

\[
E_x:=\{(n,pn):pn\le x,\ p\text{ prime},\ p\nmid n,\ \mu^2(n)=1\}.
\tag{3}
\]

If `a!=mu`, choose any squarefree `n_0` with `a(n_0)!=mu(n_0)`, put

\[
k:=\omega(n_0),
\qquad
\Delta:=|a(n_0)-\mu(n_0)|>0.
\tag{4}
\]

Because (1) fixes `1` and every prime, necessarily `k>=2`. Then for every sufficiently large `x`,

\[
\boxed{
\mathcal M_{a,q}(x)
\ge
\left(\pi(x/n_0)-k\right)
\frac{\Delta^q}{(k+1)^{q-1}}.
}
\tag{5}
\]

Consequently the prime number theorem gives

\[
\boxed{
\liminf_{x\to\infty}
\frac{\log x}{x}\mathcal M_{a,q}(x)
\ge
\frac{\Delta^q}
{n_0(k+1)^{q-1}}
>0.
}
\tag{6}
\]

Therefore

\[
\boxed{
\mathcal M_{a,q}(x)=o(x/\log x)
\quad\Longrightarrow\quad
a=\mu
}
\tag{7}
\]

on the physical-prime squarefree fibre. No perturbation-support hypothesis is required.

Combining (7) with the moved-prime tariff of `FD-185` gives a global dichotomy for arbitrary squarefree-supported sources. If

\[
\mathcal M_{a,q}(x)=o(x/\log x)
\tag{8}
\]

and `a!=mu`, then at least one prime coordinate must move. For every moved prime `p`, `FD-185` then gives

\[
\liminf_{x\to\infty}\frac{S(x)}x
\ge
\frac1{\zeta(2)(p+1)}>0,
\tag{9}
\]

where `S={n:a(n)!=mu(n)}`. In particular,

\[
\boxed{
S(x)=o(x),
\qquad
\mathcal M_{a,q}(x)=o(x/\log x)
\quad\Longrightarrow\quad
a=\mu.
}
\tag{10}
\]

Thus the growing-rank uniformity problem left by `FD-184` is not needed to settle the sublinear-support fibre: finite prime-detour cycles already close it.

## 1. Physical primes turn relation energy into ordinary edge energy

For every squarefree `n`, define

\[
c(n):=\frac{a(n)}{\mu(n)}.
\tag{11}
\]

Since `|mu(n)|=1` on this domain, (1) gives

\[
c(1)=1,
\qquad
c(p)=1\quad(p\text{ prime}).
\tag{12}
\]

If `p` is prime and `p\nmid n`, then

\[
\mu(pn)=-\mu(n),
\tag{13}
\]

so

\[
\begin{aligned}
a(pn)-a(p)a(n)
&=\mu(pn)c(pn)+a(n)\\
&=\mu(n)\bigl(c(n)-c(pn)\bigr).
\end{aligned}
\tag{14}
\]

Hence

\[
\boxed{
|a(pn)-a(p)a(n)|
=
|c(pn)-c(n)|.
}
\tag{15}
\]

The prime-extension energy is therefore exactly the Dirichlet `L^q` edge energy of `c` on the squarefree divisibility graph. Möbius is the constant field `c=1`.

For the chosen `n_0`, equation (4) becomes

\[
|c(n_0)-1|=\Delta.
\tag{16}
\]

No support information enters from this point onward.

## 2. Every fresh prime produces a finite detour certificate

Write

\[
n_0=p_1p_2\cdots p_k
\tag{17}
\]

with distinct primes, in any fixed order, and put

\[
d_j:=p_1\cdots p_j,
\qquad
d_0:=1,
\qquad
d_k=n_0.
\tag{18}
\]

Let `r` be any prime with

\[
r\nmid n_0,
\qquad
r\le x/n_0.
\tag{19}
\]

There are now two routes meeting at `n_0r`.

The first is the single prime-extension edge

\[
n_0\longrightarrow n_0r.
\tag{20}
\]

The second starts at the physical prime `r` and adds the fixed prime factors of `n_0`:

\[
r=d_0r
\longrightarrow d_1r
\longrightarrow\cdots
\longrightarrow d_kr=n_0r.
\tag{21}
\]

Every vertex in these routes is squarefree and at most `x`. Since `c(r)=1`, the triangle inequality around the detour gives

\[
\begin{aligned}
\Delta
&=|c(n_0)-c(r)|\\
&\le
|c(n_0)-c(n_0r)|
+
\sum_{j=1}^k
|c(d_jr)-c(d_{j-1}r)|.
\end{aligned}
\tag{22}
\]

There are `k+1` edge increments on the right. Hölder's inequality therefore implies

\[
\boxed{
|c(n_0)-c(n_0r)|^q
+
\sum_{j=1}^k
|c(d_jr)-c(d_{j-1}r)|^q
\ge
\frac{\Delta^q}{(k+1)^{q-1}}.
}
\tag{23}
\]

This is the load-bearing finite certificate. It does not ask where the perturbation support lies, how amplitudes behave away from `n_0`, or how many multiplicative ranks are populated. A changed composite and one unchanged fresh prime already force a fixed amount of `L^q` relation energy somewhere on this finite detour.

## 3. The detours for distinct fresh primes are edge-disjoint

The bound becomes critical-scale because the certificate can be repeated independently over all fresh prime labels.

For a given external prime `r`, the route (20) has label `r`, while every edge in (21) has one of the fixed labels `p_1,...,p_k`. For two distinct external primes `r` and `s`, an edge in the translated path (21) contains exactly one prime outside the fixed set `{p_1,...,p_k}` in both of its endpoints; unique factorization therefore identifies that external prime. Hence translated-path edges belonging to different `r` are distinct.

The direct edges (20) are distinct because their children `n_0r` are distinct. A direct edge cannot coincide with a translated-path edge because its prime label lies outside the prime support of `n_0`, whereas every translated-path label lies inside it. Thus the entire `(k+1)`-edge certificates are pairwise edge-disjoint as `r` varies.

Summing (23) over all primes `r<=x/n_0` not dividing `n_0` and using (15) gives exactly

\[
\mathcal M_{a,q}(x)
\ge
\left(
\pi(x/n_0)-\#\{p\mid n_0:p\le x/n_0\}
\right)
\frac{\Delta^q}{(k+1)^{q-1}}.
\tag{24}
\]

Dropping at most `k` excluded primes gives (5). The PNT then yields (6).

## 4. Why this bypasses the fixed-rank bootstrap

`FD-184` used one canonical upward path from `n_0` to a rank-`r` descendant. An unchanged terminal value then forced a bad edge somewhere on that path, and counting descendants required a convolution argument whose constants deteriorated with `r`. That proof naturally left a growing-rank uniformity problem.

The present certificate uses a different piece of graph geometry. Instead of pushing the defect ever farther upward, it closes a finite detour through the **already anchored prime layer**. The fresh prime `r` is known to satisfy `c(r)=1`, while `c(n_0)` differs from `1`; the two routes to `n_0r` cannot both have arbitrarily small edge variation. The number of edges in the certificate is fixed once `n_0` is fixed, so there is no growing-rank parameter to control.

This also explains why the physical-prime hypothesis is structural rather than cosmetic. If `c(r)` is allowed to move with `r`, the endpoint anchor in (22) disappears. `FD-185` shows exactly what that escape costs: a moved prime can have zero relation energy, but then its changed support has positive density. The two findings therefore splice without a gap and give (10).

## 5. Stress tests and boundaries

**The result is critical-scale, not a claim of sharp constant.** Equation (5) uses only one finite detour per external prime and may discard substantial additional edge energy. It proves that `o(x/log x)` is impossible on the physical-prime fibre, but does not claim that the coefficient in (6) is optimal or that `Theta(x/log x)` is attainable by a non-Möbius physical-prime source.

**No perturbation sparsity is used in (5)--(7).** Dense, signed and arbitrarily small later perturbations are permitted. The only fixed amplitude is the one witnessed at the chosen changed coordinate `n_0`. This is strictly stronger than the support-dependent conclusions of `FD-181` and the all-fixed-rank support propagation of `FD-184` on this fibre.

**Moving primes remain a genuine zero-energy escape.** `FD-185` gives explicit squarefree multiplicative sources obtained by changing one prime value; they have `M_(a,q)(x)=0` and positive-density changed support. Therefore relation energy alone cannot characterize Möbius on the unrestricted prime-coordinate fibre. The correct global statement is the zero-or-positive-density dichotomy (9)--(10), not unconditional rigidity.

**The theorem is source-side only.** `FD-182` still shows that exact dyadic midpoint observations can coexist with critical prime-extension energy. Nothing here derives relation energy from Farey observations, so the missing observation-to-relation bridge remains untouched.

**No RH consequence follows directly.** Even exact source identification under a declared relation hypothesis does not by itself supply the Franel--Landau critical discrepancy estimate or its conditioning.

## Representation audit

The normalization `c(n)=a(n)/mu(n)` is pointwise and isometric on squarefree coordinates: it neither mixes coefficients nor changes the magnitude of any prime-extension defect. Equation (15) shows that the auxiliary representation merely exposes the existing relation energy as an ordinary graph gradient. There is no cumulative inversion, spectral weighting, source-dependent basis or additional observation.

The generic mechanism is a finite-cycle consistency certificate: two routes with anchored endpoint values cannot both have small total edge variation, and edge-disjoint copies make the local obstruction extensive. The arithmetic splice is minimal: squarefree unique factorization creates the detours, physical prime values provide the anchors, and the PNT counts `Theta(x/log x)` fresh prime labels. The result would therefore transfer to other free commutative squarefree semilattices with a comparably large anchored generator layer.

All Farey spatial information is deliberately absent. The theorem strengthens the destination relation rigidity available to a future Farey observation bridge; it does not manufacture such a bridge.

## Prior-art audit

The only load-bearing asymptotic input is the prime number theorem, already anchored in `SOURCES.md`. The rest of the argument is the finite detour identity (22), Hölder and unique factorization, so no new external theorem is required.

A targeted search was made for Hyers--Ulam stability of multiplicative functional equations, property testing of multiplicativity, and expansion/rigidity on prime-divisibility graphs. General Hyers--Ulam work studies approximate multiplicative equations on semigroups or algebras under different global norms, while Helfgott--Radziwill's *Expansion, divisibility and parity* concerns a different additive prime-divisibility graph and spectral expansion. Neither source states the edge-disjoint squarefree prime-detour estimate (5), the physical-prime `o(x/log x)` classification (7), or the splice with the moved-prime tariff (10).

No direct prior-art match was found for this exact deterministic certificate. This is not a global novelty claim; it records that the Mathia-specific theorem follows elementarily and does not need an additional literature dependency. `SOURCES.md` therefore remains unchanged.

## Research consequence

The main source-side question after `FD-185` was whether the fixed-rank propagation of `FD-184` could be made uniform for growing multiplicative rank. For the sublinear-support/subcritical-energy classification that question is now bypassed completely. Once prime coordinates are physical, one changed composite already forces critical energy by a fixed finite detour; if a prime coordinate moves instead, `FD-185` forces positive-density changed support.

Thus

\[
S(x)=o(x)
\quad\text{and}\quad
\mathcal M_{a,q}(x)=o(x/\log x)
\]

leave **no non-Möbius escape at all** in the declared squarefree source class. The useful remaining source-side questions are quantitative rather than rank-uniform: determine the optimal critical-energy constant or stability modulus, and understand weighted notions appropriate to dense perturbations whose amplitudes tend to zero.

The observation-side frontier from `FD-182` is unchanged and becomes more sharply motivated: find the weakest additional Farey spatial data whose error controls the prime-extension energy below `x/log x`. If such a source-native bridge exists on a sublinear-support fibre, (10) would immediately turn it into exact Möbius rigidity without any growing-rank bootstrap.