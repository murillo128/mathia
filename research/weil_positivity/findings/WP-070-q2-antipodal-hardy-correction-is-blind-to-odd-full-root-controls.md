# WP-070 — the `q=2` antipodal Hardy correction is asymptotically invisible on odd full-root controls

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + CLASSICAL-HARDY-GEOMETRY` for the most direct positive `q=2` correction to the Hardy-shell branch. The proof combines the intrinsic positive antipodal shell from WP-061 with the canonical full-root null sequence from WP-068/WP-069. No zeta zeros, analytic continuation, fitted kernel, or RH-equivalent positivity criterion enters, and no theorem-level historical novelty is claimed for the Hardy/local-Dirichlet identities used below.

WP-069 left one exact escape condition for the positive Hardy-shell geometry. If a new positive finite/archimedean correction is to make the exact Mangoldt anchor finite-energy, it must see order-one energy on the normalized full-root controls

\[
X_N=\frac1{\log N}\sum_{\substack{d\mid N\\d>1}}\Gamma_d,
\qquad
Q_H(X_N)\to0,
\qquad
L(X_N)=1.
\]

WP-061 supplies the most canonical positive correction suggested by the independently distinguished `q=2` reflection channel: the primitive antipodal Hardy shell

\[
\Gamma_2=DHD\succ0,
\qquad
De_j=(-1)^j e_j.
\]

That correction does **not** satisfy WP-069's escape condition. On the odd-shell sector, define

\[
\boxed{
Q_2(B):=\operatorname{Tr}(B^*\Gamma_2B)
=\|H^{1/2}DB\|_{\mathcal S_2}^2\ge0.
}
\]

For every odd integer `N>=3`, the full-root shell combination

\[
B_N:=\sum_{\substack{d\mid N\\d>1}}\Gamma_d
\]

belongs to that separated odd sector and satisfies the exact estimate

\[
\boxed{Q_2(B_N)=O(\log N).}
\]

Consequently

\[
\boxed{
Q_2(X_N)\to0
\qquad(N\to\infty,\ N\text{ odd}),
}
\]

while `L(X_N)=1`. Hence for every fixed finite `alpha>=0`,

\[
Q_{H,2}^{(\alpha)}(B):=Q_H(B)+\alpha Q_2(B)
\]

still satisfies

\[
Q_{H,2}^{(\alpha)}(X_N)\to0,
\qquad
L(X_N)=1
\]

along odd `N`. The exact Mangoldt anchor therefore remains unbounded in this reflection-corrected positive topology. By the Cauchy--Schwarz argument of WP-069, no further regular positive extension preserving `Q_H+alpha Q_2` on this sector can represent `L` as polarization against a finite-energy vector.

The geometric reason is especially sharp. WP-068 writes `Q_H(B_N)` as an integral of local Dirichlet energies along the positive real radius of the disk. The antipodal correction `Q_2(B_N)` is exactly the same local Dirichlet energy sampled along the **negative** real radius. For odd full-root refinements the cyclotomic logarithm cancels at both endpoints `+1` and `-1` strongly enough that the normalized sequence is invisible to both halves. Thus adding the canonical positive reflection partner does not change the Hardy topology at the one sequence that a successful global correction is forced to detect.

## 1. The antipodal positive shell is the negative-radius Hardy energy

Let

\[
H_{jk}=\frac1{j+k+1},
\qquad
Ce_j(t)=t^j\quad(0<t<1),
\]

so `H=C^*C`. WP-061 gives

\[
\Gamma_2=DHD,
\qquad
De_j=(-1)^j e_j.
\]

For odd `N`, every divisor `d>1` of `N` is different from `2`, so the products needed for the separated-shell form are trace class and

\[
Q_2(B_N)
=\|CDB_N\|_{\mathcal S_2}^2.
\]

WP-068 gives the exact Hankel coefficients

\[
(B_N)_{jk}=b_N(j+k+1),
\qquad
b_N(m)=\frac{1-N\mathbf1_{N\mid m}}m,
\]

with generating function

\[
\boxed{
F_N(z)
=\sum_{m\ge1}b_N(m)z^m
=\log\frac{1-z^N}{1-z}
=g(z)-g(z^N),
\qquad
g(z)=-\log(1-z).
}
\]

For a real `a` with `|a|<1`, define the local divided-difference energy

\[
D_a(F)
:=
\left\|\frac{F(z)-F(a)}{z-a}\right\|_{H^2}^2.
\]

The `k`-th column of `CDB_N` is

\[
\sum_{j\ge0}(-1)^j b_N(j+k+1)t^j,
\]

which is exactly the `k`-th Taylor coefficient of the divided difference at `a=-t`. Therefore

\[
\boxed{
Q_2(B_N)=\int_0^1 D_{-t}(F_N)\,dt.
}
\tag{1}
\]

This is the exact antipodal companion of WP-068's identity

\[
Q_H(B_N)=\int_0^1D_t(F_N)\,dt.
\]

Thus `Q_H+Q_2` is not an arbitrary repair: on these full-root shells it is the local Dirichlet energy sampled on the full real diameter `(-1,1)`.

## 2. The negative-radius bulk contributes only `O(log N)`

For real `|a|<1`, the Hardy divided-difference identity gives

\[
D_a(F)
=
\frac{P_a(|F|^2)-|F(a)|^2}{1-a^2},
\]

where `P_a` denotes Poisson evaluation. For the base logarithm `g`, the coefficient calculation already used in WP-068 gives, now for every real `-1<a<1`,

\[
\boxed{
V_g(a):=P_a(|g|^2)-|g(a)|^2
=\zeta(2)+2\operatorname{Li}_2(a).
}
\tag{2}
\]

On the negative radius,

\[
0\le V_g(a)\le\zeta(2),
\qquad -1<a\le0.
\tag{3}
\]

If `N` is odd and `a=-t`, then `a^N` is again negative. Since `g(z^N)` has only frequencies divisible by `N`, its Poisson variance at `a` is exactly `V_g(a^N)`. Applying the elementary variance inequality to

\[
F_N=g-g(\,\cdot\,^N)
\]

gives

\[
P_a(|F_N|^2)-|F_N(a)|^2
\le2V_g(a)+2V_g(a^N)
\le4\zeta(2).
\]

Hence

\[
D_{-t}(F_N)
\le\frac{4\zeta(2)}{1-t^2}.
\]

Integrating only up to the natural boundary-layer scale gives the explicit bulk bound

\[
\boxed{
\int_0^{1-1/N}D_{-t}(F_N)\,dt
\le
2\zeta(2)\log(2N-1)
=
\frac{\pi^2}{3}\log(2N-1).
}
\tag{4}
\]

So any growth beyond logarithmic order could only come from a width-`1/N` neighborhood of the antipodal endpoint.

## 3. Odd full-root refinement cancels at the antipode

For odd `N`,

\[
\boxed{F_N(-1)=0,}
\]

because both `1-(-1)^N` and `1-(-1)` equal `2`. The endpoint cancellation can be quantified coefficientwise.

Let

\[
s_k
:=
\sum_{j\ge0}(-1)^j b_N(j+k+1)
\]

be the coefficient vector of the divided difference at `-1`, and put

\[
A_m:=\sum_{r=m+1}^{\infty}\frac{(-1)^r}{r}.
\]

If `q=floor(k/N)`, then oddness of `N` implies `(-1)^{N\ell}=(-1)^\ell`, and direct separation of the multiples of `N` gives the exact formula

\[
\boxed{
s_k=(-1)^{k+1}\bigl(A_k-A_q\bigr).}
\tag{5}
\]

The alternating-series remainder estimate gives

\[
|A_m|\le\frac1{m+1}.
\]

For `qN<=k<(q+1)N`, therefore,

\[
|s_k|
\le\frac1{k+1}+\frac1{q+1}
\le\frac2{q+1}.
\]

Summing blockwise yields

\[
\boxed{
D_{-1}(F_N)
:=\sum_{k\ge0}|s_k|^2
\le4N\sum_{q\ge0}\frac1{(q+1)^2}
=
\frac{2\pi^2}{3}N.
}
\tag{6}
\]

This endpoint estimate transfers uniformly through the thin radial layer. Let

\[
c_k=b_N(k+1)
\]

and let `S^*` be the backward shift. The divided-difference coefficient vector at `-t` is

\[
q(-t)=(I+tS^*)^{-1}c.
\]

At `t=1`, equation (5) says `s=q(-1)` and hence

\[
c=(I+S^*)s.
\]

Therefore

\[
q(-t)
=s+(1-t)(I+tS^*)^{-1}S^*s.
\]

Since

\[
\|(I+tS^*)^{-1}\|\le\frac1{1-t},
\]

we get

\[
\boxed{
D_{-t}(F_N)=\|q(-t)\|_2^2
\le4\|s\|_2^2
\le\frac{8\pi^2}{3}N.
}
\tag{7}
\]

Consequently the entire endpoint layer has bounded total mass:

\[
\boxed{
\int_{1-1/N}^1D_{-t}(F_N)\,dt
\le\frac{8\pi^2}{3}.
}
\tag{8}
\]

Combining (1), (4), and (8) proves

\[
\boxed{
Q_2(B_N)
\le
\frac{\pi^2}{3}\log(2N-1)+\frac{8\pi^2}{3}
=O(\log N)
}
\qquad(N\text{ odd}).
\tag{9}
\]

## 4. The canonical reflection correction fails WP-069's mandatory discriminator

Normalize as in WP-068:

\[
X_N=\frac{B_N}{\log N}.
\]

Equations (9) and WP-068's `Q_H(B_N)=O(log N)` give, along odd integers,

\[
Q_H(X_N)=O\!\left(\frac1{\log N}\right),
\qquad
Q_2(X_N)=O\!\left(\frac1{\log N}\right).
\]

At the same time the exact divisor identity remains

\[
L(X_N)
=\frac1{\log N}\sum_{\substack{d\mid N\\d>1}}\Lambda(d)
=1.
\]

Thus for every fixed finite `alpha>=0`,

\[
\boxed{
Q_{H,2}^{(\alpha)}(X_N)
=Q_H(X_N)+\alpha Q_2(X_N)
\longrightarrow0,
\qquad
L(X_N)=1.
}
\tag{10}
\]

The Mangoldt functional is therefore unbounded in the norm supplied by this positive reflection correction.

Now let `\widetilde q` be any positive semidefinite Hermitian extension whose restriction to the odd-shell sector is `Q_H+alpha Q_2`. If a finite-energy vector `a` represented the exact anchor,

\[
\widetilde q(B,a)=L(B),
\]

Cauchy--Schwarz applied to the odd sequence `X_N` would give

\[
1
=|L(X_N)|^2
\le
Q_{H,2}^{(\alpha)}(X_N)\,\widetilde q(a,a)
\longrightarrow0,
\]

a contradiction. Hence

\[
\boxed{
\text{the primitive `q=2` positive Hardy correction cannot regularize the exact Mangoldt anchor.}
}
\tag{11}
\]

This is stronger than observing that `Gamma_2` does not itself have Mangoldt support, as in WP-061. Even when `Gamma_2` is used only as an additional positive geometry while the exact arithmetic functional `L` is retained separately, it remains asymptotically invisible on the canonical full-root obstruction.

## 5. What the result does and does not rule out

The domain restriction is essential and deliberate. `Q_2` is used here on the **odd-shell sector**, where the full-root controls `B_N` involve no `Gamma_2` shell and the separated-shell trace-class hypotheses from PC-080/WP-061 apply. No claim is made that `Q_2(Gamma_2)` is finite or that `Q_2` defines a quadratic form on every shell in `A_0`. A purported global positive mechanism based on this correction must nevertheless restrict positively to the odd sector, so the odd null sequence is sufficient for the no-go above.

The result also does not identify `Gamma_2` with the full Riemann archimedean channel. WP-061 proves the opposite: the full-root `q=2` operator is

\[
\Gamma_1+\Gamma_2=-H+DHD,
\]

which is indefinite. The present calculation tests the **strongest canonical positive piece** suggested by that reflection geometry. Its failure does not add a sign theorem to the indefinite full-root operator.

The following materially different escapes remain outside the claim:

- a positive correction that changes the finite-shell topology by an order-one amount on the normalized full-root controls;
- a singular or infinite-energy boundary object with a separately justified renormalized sign;
- a test-dependent auxiliary state that changes the effective finite geometry;
- a graded, Krein, intersection, or cohomological mechanism whose final sign follows from a different theorem;
- a non-Hardy or nonlocal coupling not reducible to a finite multiple of the primitive antipodal form.

In particular, equation (10) is a discriminator, not a universal impossibility theorem: any future candidate that genuinely satisfies `liminf R(X_N)>0` lies outside this no-go and deserves separate analysis.

## 6. Prior-art and novelty audit

The analytic mechanism in Sections 1--3 is classical Hardy/local-Dirichlet geometry. Divided differences, Poisson variance identities, alternating-series bounds, and resolvent estimates for the backward shift are standard tools. The proof is written coefficientwise so that no external theorem beyond those elementary facts is needed.

A targeted literature comparison around local Dirichlet integrals, Hardy divided differences, cyclotomic logarithms, and reflection/antipodal sampling did not identify an external theorem asserting the Mathia-specific conclusion (9)--(11). That absence is **not** used as a novelty claim. The durable contribution is the internal synthesis of three already-canonical Mathia structures:

1. WP-061's intrinsic positive antipodal shell `Gamma_2=DHD`;
2. WP-068's exact full-root sequence and Mangoldt anchor;
3. WP-069's necessary order-one-energy criterion for any regular positive completion.

The result is not a reformulation of Weil positivity and does not use the completed zeta function. It closes one concrete Mathia-native positive repair because the candidate geometry fails an exact pre-arithmetic norm test.

## 7. Falsification tests

The claim has direct exact failure modes.

1. For an odd `N`, find an error in the identity `Q_2(B_N)=int_0^1 D_{-t}(F_N)dt`.
2. Find an odd `N` for which the endpoint coefficient identity (5) fails.
3. Show that either the bulk estimate (4) or endpoint-layer estimate (8) cannot hold uniformly, allowing `Q_2(B_N)` to grow faster than `O(log N)`.
4. Exhibit a finite `alpha>=0` for which `Q_H(X_N)+alpha Q_2(X_N)` does not tend to zero along odd `N`.
5. Exhibit a positive extension preserving that corrected finite form and a finite-energy vector representing `L`; this would contradict Cauchy--Schwarz and (10).

A construction that is singular on the odd full-root controls or changes their finite energy by order one does not falsify the finding; it is precisely the remaining escape.

## Research consequence

The two most canonical positive Hardy pieces now fail the same mandatory global-completion test:

\[
\boxed{
Q_H(X_N)\to0,
\qquad
Q_2(X_N)\to0,
\qquad
L(X_N)=1
\quad(N\to\infty,\ N\text{ odd}).
}
\]

So the independently distinguished reflection/antipodal structure does not supply the missing singular geometry by merely adding its positive primitive energy to the base Hardy Gram. A viable positive finite--archimedean construction must **change the topology**, not just symmetrize the existing Hardy geometry across the real diameter. The canonical full-root controls now test that requirement simultaneously at the anchor and antipode before any zeta-zero or explicit-formula input is allowed.