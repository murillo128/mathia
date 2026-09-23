# NB-314 — Far-external projected dilation converges to a target-weighted rank-one channel

- **Date:** 2026-09-23
- **Status:** proved
- **Research line:** `nyman_beurling`
- **Depends on:** NB-290, NB-303, NB-308, NB-312, NB-313
- **Classification:** `EXACT-DERIVED + FIXED-SECTION-ASYMPTOTIC + PROJECTED-DILATION + FAR-EXTERNAL-DILATION + RANK-ONE-LIMIT + TARGET-CAPTURE-FACTOR + RECIPROCAL-SHELL-MEAN + NONUNIFORM-IN-N + PRIOR-ART-AUDITED`

## Claim

Let

\[
U_N:=\operatorname{span}\{g_2,\ldots,g_N\},
\qquad
T_{N,m}:=P_{U_N}A_m|_{U_N},
\qquad
\beta_{N+1}(m):=\|T_{N,m}\|,
\]

with the canonical Nyman generators and normalized integer dilation of `NB-290`. Fix `N>=2` and let `m->infinity` through the positive integers.

For `u in U_N`, put

\[
F_u(t):=u(1/t),
\qquad
P_N:=\operatorname{lcm}(2,\ldots,N),
\]

and define the reciprocal-period mean

\[
\mu_N(u)
:=
\frac1{P_N}\int_0^{P_N}F_u(t)\,dt.
\tag{1}
\]

Every `F_u` is `P_N`-periodic almost everywhere. Let `r_N in U_N` be the Riesz representer of `mu_N`,

\[
\mu_N(u)=\langle r_N,u\rangle,
\]

and let

\[
p_N:=P_{U_N}{\bf 1}.
\tag{2}
\]

Then, in operator norm on the finite-dimensional Hilbert space `U_N`,

\[
\boxed{
\sqrt m\,T_{N,m}
\longrightarrow
R_N,
\qquad
R_Nv:=\langle v,p_N\rangle r_N.
}
\tag{3}
\]

Thus the far-external projected dilation has an exact rank-one asymptotic, and its coefficient factorizes as

\[
\boxed{
L_N
:=
\lim_{m\to\infty}\sqrt m\,\beta_{N+1}(m)
=
\|P_{U_N}{\bf 1}\|_2\,
\|\mu_N\|_{U_N^*}.
}
\tag{4}
\]

If

\[
d_N:=\operatorname{dist}({\bf 1},U_N),
\]

then `||1||_2=1` gives the equivalent target-capture form

\[
\boxed{
L_N^2
=
(1-d_N^2)\,\|\mu_N\|_{U_N^*}^2.
}
\tag{5}
\]

This is a fixed-section theorem. It does **not** assert uniformity as `N->infinity`: the elementary averaging proof below uses the common reciprocal period `P_N`, which grows rapidly with `N`. Therefore (3)--(5) do not by themselves improve the moving-regime frontier from `NB-313`/`NB-303`, namely that decay of `beta` requires genuinely superlinear dilation while superquadratic dilation is sufficient.

## 1. Reciprocal profiles are periodic and have an explicit mean

For the canonical generator

\[
g_j(x)
=
\left\{\frac1{jx}\right\}
-
\frac1j\left\{\frac1x\right\},
\]

its reciprocal profile is

\[
F_{g_j}(t)
=
\left\{\frac tj\right\}
-
\frac1j\{t\}.
\tag{6}
\]

The first term is `j`-periodic and the second is `1`-periodic, hence `F_{g_j}` is `j`-periodic almost everywhere. Therefore every `u in U_N` has a bounded, piecewise continuous reciprocal profile with common period `P_N`.

Averaging (6) over one period of length `j` gives

\[
\begin{aligned}
\mu_N(g_j)
&=
\frac1j\int_0^j
\left(
\left\{\frac tj\right\}
-
\frac1j\{t\}
\right)dt\\
&=
\frac12-
\frac1{2j}
=
\boxed{\frac{j-1}{2j}}.
\end{aligned}
\tag{7}
\]

The notation `mu_N` is harmless although the value on `g_j` is independent of `N` once `j<=N`; `N` records the finite section on which the functional is being used.

The target functional is equally explicit. A change of variable gives

\[
\begin{aligned}
\langle g_j,{\bf 1}\rangle
&=
\int_0^1g_j(x)\,dx\\
&=
\frac1j\int_0^j\left\{\frac1y\right\}dy
-
\frac1j\int_0^1\left\{\frac1x\right\}dx\\
&=
\frac1j\int_1^j\frac{dy}{y}
=
\boxed{\frac{\log j}{j}}.
\end{aligned}
\tag{8}
\]

Thus the two linear functionals that will survive the far-external limit are both intrinsic and completely explicit: ordinary integration against the Nyman target and reciprocal-period averaging of the source profile.

## 2. A periodic averaging lemma

We use only the following elementary fixed-period fact. If `F` is bounded, `P`-periodic, and Riemann integrable on one period, with mean

\[
\overline F:=\frac1P\int_0^P F(s)\,ds,
\]

then for every `h in L^1([1,infinity))`,

\[
\boxed{
\int_1^\infty h(t)F(mt)\,dt
\longrightarrow
\overline F\int_1^\infty h(t)\,dt
}
\tag{9}
\]

as `m->infinity`.

For completeness, first take `h` to be the indicator of a bounded interval. Splitting that interval into full periods of `F(mt)`, whose length is `P/m`, plus at most two boundary fragments shows that the average tends to `overline F`; boundedness of `F` controls the boundary fragments. Finite step functions follow by linearity. For general `L^1` data, truncate the tail and approximate the compactly supported part in `L^1` by step functions. Since `||F(mt)||_infinity=||F||_infinity`, the approximation error is uniform in `m`. This proves (9) without any external input.

The fixed-period qualification matters. Nothing in this proof supplies a useful rate uniform in the rapidly growing periods `P_N`.

## 3. The projected dilation has a rank-one limit

For `u,v in U_N`, the normalized dilation satisfies

\[
\begin{aligned}
\sqrt m\,\langle A_mv,u\rangle
&=
\int_0^1 v(y)u(y/m)\,dy\\
&=
\int_1^\infty
v(1/t)F_u(mt)\,\frac{dt}{t^2}.
\end{aligned}
\tag{10}
\]

The function

\[
h_v(t):=v(1/t)t^{-2}
\]

belongs to `L^1([1,infinity))`: every element of the fixed finite span `U_N` is bounded. Applying (9) to `F_u` gives

\[
\sqrt m\,\langle A_mv,u\rangle
\longrightarrow
\mu_N(u)
\int_1^\infty v(1/t)\frac{dt}{t^2}.
\tag{11}
\]

Changing variables back to `y=1/t`,

\[
\int_1^\infty v(1/t)\frac{dt}{t^2}
=
\int_0^1v(y)\,dy
=
\langle v,{\bf 1}\rangle
=
\langle v,p_N\rangle.
\tag{12}
\]

Since `u in U_N`, projection does not change the tested inner product:

\[
\langle T_{N,m}v,u\rangle
=
\langle A_mv,u\rangle.
\]

Equations (11)--(12) therefore give

\[
\boxed{
\langle \sqrt m\,T_{N,m}v,u\rangle
\longrightarrow
\langle v,p_N\rangle
\langle r_N,u\rangle
=
\langle R_Nv,u\rangle.
}
\tag{13}
\]

Choose an orthonormal basis of the fixed finite-dimensional space `U_N`. Every matrix entry of `sqrt(m)T_{N,m}-R_N` tends to zero by (13), hence its Hilbert--Schmidt norm, and therefore its operator norm, tends to zero. This proves (3).

Because a rank-one operator `v -> <v,p_N>r_N` has norm `||p_N|| ||r_N||`, taking norms in (3) proves (4). Orthogonal decomposition of the unit target gives

\[
1=\|P_{U_N}{\bf 1}\|_2^2+d_N^2,
\]

which proves (5).

## 4. Exact finite Gram formula

Let

\[
G_N:=\bigl(\langle g_i,g_j\rangle\bigr)_{2\le i,j\le N},
\]

and define the coordinate vectors

\[
b_j:=\frac{\log j}{j},
\qquad
q_j:=\frac{j-1}{2j},
\qquad 2\le j\le N.
\tag{14}
\]

The finite independence of the canonical generators, also made explicit by the shell coefficient extractors of `NB-308`, makes `G_N` positive definite. Equations (7)--(8) therefore imply

\[
\|P_{U_N}{\bf 1}\|_2^2
=b^*G_N^{-1}b,
\qquad
\|\mu_N\|_{U_N^*}^2
=q^*G_N^{-1}q.
\tag{15}
\]

Consequently the asymptotic coefficient is an entirely finite Gram quantity:

\[
\boxed{
L_N^2
=
\bigl(b^*G_N^{-1}b\bigr)
\bigl(q^*G_N^{-1}q\bigr).
}
\tag{16}
\]

The first factor is exactly the captured target energy `1-d_N^2`. The second is the squared dual norm of the reciprocal-shell mean. Thus the far-external limit does not merely say `beta=Theta_N(m^{-1/2})`: it identifies the two finite-section susceptibilities whose product gives the exact leading coefficient.

## 5. The coefficient is already at least of square-root section scale

The rank-one formula contains the anchored channel of `NB-313` as a one-pair test. Taking source `g_2` and testing against `g_N`, equations (7)--(8) give

\[
L_N
\ge
\frac{
\langle g_2,{\bf 1}\rangle\,\mu_N(g_N)
}{
\|g_2\|_2\,\|g_N\|_2
}
=
\frac{\sqrt{\log2}}{2}
\frac{N-1}{N\|g_N\|_2},
\tag{17}
\]

where `||g_2||_2^2=log(2)/4` as recorded in `NB-312`.

Using the uniform edge-generator bound from `NB-313`,

\[
\|g_N\|_2^2
\le
\frac{1+\pi^2/6}{N},
\]

we obtain

\[
\boxed{
L_N
\ge
\frac{\sqrt{\log2}}
{2\sqrt{1+\pi^2/6}}
\left(1-\frac1N\right)\sqrt N.
}
\tag{18}
\]

Moreover `NB-312` gives

\[
N\|g_N\|_2^2
\longrightarrow
\log(2\pi)-\gamma,
\]

so

\[
\boxed{
\liminf_{N\to\infty}
\frac{L_N}{\sqrt N}
\ge
\frac{\sqrt{\log2}}
{2\sqrt{\log(2\pi)-\gamma}}
=
0.370752\ldots.
}
\tag{19}
\]

This is an iterated statement: `L_N` is first defined by the fixed-`N`, `m->infinity` limit, and only then is `N->infinity` considered. Equation (19) must not be read as a uniform moving-`N` asymptotic for `beta`.

## 6. What this changes, and what it does not

`NB-313` gave the robust external lower channel

\[
\beta_{N+1}(m)\gtrsim\sqrt{N/m}
\qquad(m\ge N),
\]

and showed that `beta->0` is impossible while `m/N` stays bounded. The present finding identifies the exact fixed-section mechanism behind the eventual `m^{-1/2}` behavior: after multiplying by `sqrt(m)`, every reciprocal oscillation with zero period mean averages away, leaving only the tensor product

\[
\text{ordinary target integral}
\ \otimes\ 
\text{reciprocal-period mean}.
\]

In particular, the finite Nyman target enters the far-external **source-overlap** operator through the exact factor `||P_{U_N}1||`. This is a genuine target-coupled identity, but it is not the target-aware certificate sought by the open clues. It does not show that the first-free Ford datum occupies the useful singular direction, nor does it control the moving future gain or prove a Nyman approximation rate.

The nonuniformity is the decisive boundary. Define the centered reciprocal profile

\[
\widetilde F_u:=F_u-\mu_N(u).
\]

Then the entire error in (3) has the exact bilinear form

\[
\left\langle
(\sqrt m\,T_{N,m}-R_N)v,u
\right\rangle
=
\int_1^\infty
v(1/t)\widetilde F_u(mt)\,\frac{dt}{t^2}.
\tag{20}
\]

For fixed `N` this tends to zero by periodic averaging. To turn the rank-one picture into a moving theorem one would need a quantitative estimate for (20) uniform over unit vectors `u,v in U_N` and over growing `N`, without paying the full common period `P_N`. That is now a precise mixing problem rather than an unspecified question about external overlap.

A useful falsifiable quantity is

\[
\varepsilon_N(m)
:=
\sup_{\|u\|=\|v\|=1}
\left|
\int_1^\infty
v(1/t)\widetilde F_u(mt)\,\frac{dt}{t^2}
\right|.
\tag{21}
\]

The present theorem is exactly `epsilon_N(m)->0` for each fixed `N`. Any moving-rank-one extension requires a regime with `epsilon_N(m_N)->0` as `N->infinity`. Conversely, a family keeping (21) bounded away from zero would prove that coherent zero-mean reciprocal structure survives the far-external averaging and would obstruct that extension.

## 7. Prior-art audit

A fresh structural search checked the classical discrete Nyman--Beurling/Baez-Duarte dilation literature, multiplicative autocorrelation of the fractional-part function (including Balazard--Martin), finite Gram formulations, and recent Gram-decay work. These sources provide the surrounding fractional-part, dilation, and Gram geometry, but the material reviewed did not exhibit the specific fixed-finite-section statement (3), its factorization (4)--(5), or the finite Gram product (16).

No external theorem is load-bearing for the proof: periodic averaging is proved above and all Nyman identities used are internal exact formulas. Accordingly this finding makes no bibliographic novelty claim and requires no new `SOURCES.md` dependency.

## 8. Consequence for the next discriminant

The source-side external problem now has two complementary descriptions. `NB-313` gives an `N`-uniform lower channel strong enough to rule out decay on bounded linear strips, while `NB-314` gives the exact eventual operator shape for every fixed finite section. The gap between them is precisely **uniform reciprocal-profile mixing as the section grows**.

Therefore another fixed-`N` refinement of the `m^{-1/2}` coefficient is unlikely to change the moving frontier. A substantive next step must either prove an `N`-uniform decay estimate for (21) in some genuinely superlinear regime, or construct coherent unit vectors whose centered reciprocal profiles defeat such averaging. Only after that source-side issue is controlled does target occupation remain as the separate RH-facing bridge.