# NB-331 — Adaptive adjacent routing forces logarithmic resonance throughout the subquadratic regime

- **Date:** 2026-09-24
- **Status:** proved
- **Research line:** `nyman_beurling`
- **Depends on:** NB-304, NB-314, NB-327, NB-328, NB-329, NB-330
- **Classification:** `EXACT-DERIVED + SOURCE-SIDE + WEIGHTED-BILINEAR-MIXING + ADAPTIVE-INNER-ADJACENT-WITNESS + FULL-SUBQUADRATIC-COVERAGE + RANK-ONE-ERROR + LOGARITHMIC-RESONANCE + METHOD-DISCRIMINATOR + NON-TARGET-AWARE + PRIOR-ART-AUDITED`

## Claim

Let

\[
U_n:=\operatorname{span}\{g_2,\ldots,g_n\},
\qquad
T_{n,m}:=P_{U_n}A_m|_{U_n},
\]

and let `R_n` be the rank-one comparison operator from `NB-314`.

The one-cell estimate of `NB-330` is in fact independent of the ambient edge. More precisely, let

\[
8\le q\le n,
\qquad
\nu_q:=g_q-\frac{q-1}{q}g_{q-1},
\tag{1}
\]

and for integers `d>=1` and `0<=r<=d` put

\[
\rho:=\frac rd,
\qquad
m:=dq+r=d(q+\rho).
\tag{2}
\]

Define

\[
\mathcal F_{n;q,d,r}
:=
\left\langle
(\sqrt m\,T_{n,m}-R_n)g_2,\nu_q
\right\rangle.
\tag{3}
\]

Then

\[
\boxed{
\left|
\mathcal F_{n;q,d,r}
+\frac{\log2}{4q}
\right|
\le
\frac{28d}{q^2}.
}
\tag{4}
\]

Consequently, let `n->infinity` and let `m_n` be any integer sequence satisfying

\[
 n\le m_n=o(n^2).
\tag{5}
\]

There is an explicit adaptive adjacent witness `nu_(q_n) in U_n` for which

\[
\boxed{
q_n\,
\left\langle
(\sqrt{m_n}T_{n,m_n}-R_n)g_2,\nu_{q_n}
\right\rangle
\longrightarrow
-\frac{\log2}{4}.
}
\tag{6}
\]

In particular,

\[
\boxed{
\liminf_{n\to\infty}
\sqrt{\log n}\,
\|\sqrt{m_n}T_{n,m_n}-R_n\|
\ge
\frac{\sqrt{\log2}}{2\sqrt2}.
}
\tag{7}
\]

Thus the gaps left between the one-cell bands of `NB-330` do not create a faster-mixing subquadratic window. Every external subquadratic integer dilation admits a nearby inner adjacent direction carrying the same logarithmic resonance scale.

The conclusion is deliberately quantitative rather than qualitative: the lower bound in (7) is of order `1/sqrt(log n)` and therefore still tends to zero. It rules out `o(1/sqrt(log n))` rank-one error throughout `n<=m=o(n^2)`; it does **not** prove that the rank-one error stays bounded away from zero.

## 1. The `NB-330` cell computation is an intrinsic `q`-lemma

The proof of `NB-330` used `q=n-1`, but none of its one-cell algebra depends on `q` being the top inner index. The only ambient requirement is that the target witness belong to `U_n`, which is automatic when `q<=n`.

For `u in U_n`, the rank-one-error identity from `NB-314` pairs the reciprocal profile of the source against the centered reciprocal profile of the target. For the adjacent target (1),

\[
\widetilde F_q(z)
=
\left\{\frac zq\right\}
-\frac{q-1}{q}
\left\{\frac z{q-1}\right\}
-\frac1{2q}.
\tag{8}
\]

Hence

\[
\mathcal F_{n;q,d,r}
=
\int_0^\infty
F_{g_2}(t)\,\widetilde F_q(mt)\frac{dt}{t^2}.
\tag{9}
\]

Scale by the integer `d`. With

\[
A:=q+\rho,
\qquad
h_{q,\rho}(y):=\widetilde F_q(Ay),
\qquad
s_d(y):=F_{g_2}(y/d),
\tag{10}
\]

we obtain

\[
\mathcal F_{n;q,d,r}
=
d\int_0^\infty
s_d(y)h_{q,\rho}(y)\frac{dy}{y^2}.
\tag{11}
\]

Because `d` is an integer, `s_d` is constant on unit cells and selects alternating blocks of `d` cells, exactly as in `NB-327`--`NB-330`.

For

\[
1\le k\le K:=\left\lfloor\frac q4\right\rfloor,
\qquad y=k+x,
\qquad 0\le x<1,
\]

there is at most one carry in each fractional part in (8), uniformly for `rho in [0,1]`. The carry thresholds are

\[
\alpha_k
=
\frac{q-\rho k}{q+\rho},
\qquad
\beta_k
=
\frac{q-1-(1+\rho)k}{q+\rho}.
\tag{12}
\]

Substitution gives

\[
h_{q,\rho}(k+x)
=
-\mathbf1_{\{x\ge\alpha_k\}}
+\frac{q-1}{q}\mathbf1_{\{x\ge\beta_k\}}
-\frac{k+1/2}{q}.
\tag{13}
\]

The weighted carry integrals satisfy

\[
\int_{k+\alpha_k}^{k+1}\frac{dy}{y^2}
=
\frac{\rho}{q(k+1)},
\qquad
\frac{q-1}{q}
\int_{k+\beta_k}^{k+1}\frac{dy}{y^2}
=
\frac{1+\rho}{q(k+1)}.
\tag{14}
\]

Their phase dependence cancels before taking any limit. Including the baseline term yields the exact cell identity

\[
\boxed{
\int_k^{k+1}
h_{q,\rho}(y)\frac{dy}{y^2}
=
-\frac1{2q\,k(k+1)}.
}
\tag{15}
\]

This is precisely the mechanism isolated in `NB-330`, now stated at an arbitrary adjacent index `q` inside the section.

## 2. The finite estimate remains uniform in the ambient section

A selected source cell has value `1/2`, so the first `K` cells contribute

\[
I^{(0)}_{q,d,r}
=
-\frac d{4q}
\sum_{\substack{1\le k\le K\\
\lfloor k/d\rfloor\ \mathrm{odd}}}
\frac1{k(k+1)}.
\tag{16}
\]

The full selector sum telescopes block by block:

\[
d
\sum_{\substack{k\ge1\\
\lfloor k/d\rfloor\ \mathrm{odd}}}
\frac1{k(k+1)}
=
\log2.
\tag{17}
\]

Since `K+1>q/4`, truncating at `K` gives

\[
\left|
I^{(0)}_{q,d,r}
+\frac{\log2}{4q}
\right|
\le
\frac d{q^2}.
\tag{18}
\]

For the tail, write

\[
h_{q,\rho}(y)
=
\phi_q(Ay)
-\frac{q-1}{q}\phi_{q-1}(Ay),
\qquad
\phi_j(z):=\left\{\frac zj\right\}-\frac12.
\tag{19}
\]

On every unit cell `[J,J+1)`, the cell mean `b_J` satisfies

\[
|b_J|\le\frac{3}{2q},
\tag{20}
\]

because an interval of length `A=q+rho` contains a complete period of `phi_q` plus a remainder of length at most one, and a complete period of `phi_(q-1)` plus a remainder of length at most two. Subtracting `b_J`, the remaining mean-zero cell function has magnitude at most `3/2`; variation of the weight `(J+x)^(-2)` then gives the same estimate as `NB-330`. With `L=K+1>q/4`,

\[
|\mathcal T_{q,d,r}|
\le
\frac d2
\sum_{J=L}^\infty
\left(
\frac3{J^3}
+
\frac{3}{2qJ(J+1)}
\right)
\le
\frac{27d}{q^2}.
\tag{21}
\]

Combining (18) and (21) proves (4). Neither estimate contains the ambient edge `n`. The finite section enters only through the admissibility condition `q<=n`.

## 3. Every external subquadratic dilation has an admissible resonant cell

Let `m=m_n` satisfy (5). Choose explicitly

\[
\boxed{
d_n:=\left\lceil\frac{m_n}{n}\right\rceil,
\qquad
q_n:=\left\lfloor\frac{m_n}{d_n}\right\rfloor,
\qquad
r_n:=m_n-d_nq_n.
}
\tag{22}
\]

Then

\[
0\le r_n<d_n,
\qquad
m_n=d_nq_n+r_n,
\qquad
q_n\le n.
\tag{23}
\]

The last inequality follows from `d_n>=m_n/n`. There is also a uniform lower bound on the adaptive index. Put `x_n=m_n/n>=1`. Since `d_n<=x_n+1`,

\[
\frac{m_n}{d_n}
\ge
\frac{nx_n}{x_n+1}
\ge
\frac n2,
\]

and therefore

\[
\boxed{
\frac n2-1\le q_n\le n.
}
\tag{24}
\]

Thus `q_n` stays at linear depth inside the section and `log q_n~log n`. Meanwhile `m_n=o(n^2)` implies

\[
d_n
\le
\frac{m_n}{n}+1
=o(n),
\tag{25}
\]

so by (24)

\[
\boxed{
\frac{d_n}{q_n}\longrightarrow0.
}
\tag{26}
\]

Apply (4) with this adaptive quadruple. Multiplying by `q_n` gives

\[
\left|
q_n\mathcal F_{n;q_n,d_n,r_n}
+\frac{\log2}{4}
\right|
\le
28\frac{d_n}{q_n}
\longrightarrow0,
\tag{27}
\]

which proves (6).

This is the missing routing step after `NB-330`: instead of holding the witness fixed at `q=n-1` and asking whether `m` remains inside its single drift cell, move the adjacent witness to the quotient `q=floor(m/d)`. The chosen `q` always remains inside the finite section, and subquadraticity is exactly what makes the relative cell width `d/q` vanish.

## 4. The full subquadratic operator obstruction

`NB-304` gives, for the adaptive adjacent witness,

\[
\|\nu_{q_n}\|_2^2
\le
\frac{2H_{q_n-2}+1+\pi^2/18}{q_n^2},
\tag{28}
\]

while

\[
\|g_2\|_2=\frac{\sqrt{\log2}}2.
\tag{29}
\]

Consequently,

\[
\|\sqrt{m_n}T_{n,m_n}-R_n\|
\ge
\frac{|\mathcal F_{n;q_n,d_n,r_n}|}
{\|g_2\|_2\,\|\nu_{q_n}\|_2}.
\tag{30}
\]

Using (6), `H_q~log q`, and `log q_n~log n` from (24),

\[
\liminf_{n\to\infty}
\sqrt{\log n}\,
\|\sqrt{m_n}T_{n,m_n}-R_n\|
\ge
\frac{\sqrt{\log2}}{2\sqrt2},
\]

which is (7).

The exact-divisor lattice of `NB-327`, the sign-flipped neighboring lattice of `NB-328`, the one-cell interpolation of `NB-329`, and the phase-uniform inner routing of `NB-330` are therefore all shadows of a more global fact: **the adjacent family itself supplies a resonant witness at every external subquadratic integer scale once the witness index is allowed to adapt to the dilation.**

This closes the multi-cell gaps left by `NB-330`. The natural source-side boundary of this method is now genuinely quadratic. If `m` is comparable with `n^2`, the adaptive construction has `d` comparable with `q`; the error term `28d/q^2` in (4) is then the same `1/q` order as the main coefficient and no longer certifies a surviving sign or magnitude. The next discriminating question is therefore the critical scaling `m~lambda n^2`: does a refined adjacent calculation retain a nonzero profile there, or does this resonance finally wash out at quadratic scale?

## 5. Adversarial checks and prior-art boundary

The argument was pressure-tested at the points where the adaptive reindexing could have produced a false extension.

- The generalized cell estimate does not replace the ambient section by `U_q`. It keeps `T_(n,m)` and `R_n`; only the target witness is moved to `nu_q in U_n`. The `NB-314` bilinear identity therefore remains the correct one.
- The reciprocal mean subtraction in (8) is intrinsic to `nu_q`: `mu(nu_q)=1/(2q)`. It is independent of the ambient edge and matches the `R_n` pairing exactly.
- The carry calculation requires only `q>=8` and `k<=floor(q/4)`. The adaptive bound `q_n>=n/2-1` guarantees this for all sufficiently large `n`.
- The choice `d_n=ceil(m_n/n)` is essential: it simultaneously forces `q_n<=n` and keeps `q_n>=n/2-1`. Using `floor(m_n/n)` would fail the first property near the lower edge of each quotient band.
- Subquadraticity is used in exactly one place, to obtain `d_n/q_n->0`. At quadratic scale this implication fails, so the finding makes no claim for `m~lambda n^2`.
- The operator lower bound is logarithmic and tends to zero. It excludes a rank-one error `o(1/sqrt(log n))`, not convergence to zero itself.
- The result remains source-side. It does not show that the first-free Ford datum occupies the adaptive adjacent direction, does not bound finite-section target gain, and has no RH consequence by itself.

A fresh prior-art audit checked the nearby literature on integer dilations and multiplicative autocorrelation of the fractional-part function, together with work on Nyman--Beurling Gram structure. Balazard--Martin study the multiplicative autocorrelation through continued-fraction and Wilton-function structure; Alouges--Darses--Hillion study generalized Nyman--Beurling approximation and associated Gram matrices; Carvill studies multiscale Gram decay via Mellin smoothing. In the material inspected, none states the present finite-section adaptive quotient routing, the phase-uniform adjacent cell coefficient, or the resulting all-subquadratic logarithmic lower bound. This is an audit boundary, not a claim of bibliographic novelty.

External literature is not load-bearing for the proof. The result uses only persisted identities and estimates from `NB-304`, `NB-314`, and `NB-327`--`NB-330`, plus the explicit quotient choice (22). `SOURCES.md` therefore requires no update.

## Research consequence

The previous frontier asked whether the uncovered gaps between the bands `[d(n-1),dn]` might permit faster rank-one mixing. They do not: an adaptive inner adjacent witness fills every such gap whenever `m=o(n^2)`. The source-side transition question is consequently sharpened to the critical quadratic scale itself.

The durable statement from this finding is

\[
\boxed{
 n\le m_n=o(n^2)
\quad\Longrightarrow\quad
\liminf_{n\to\infty}
\sqrt{\log n}\,
\|\sqrt{m_n}T_{n,m_n}-R_n\|
\ge
\frac{\sqrt{\log2}}{2\sqrt2}.
}
\]

This is not a target-aware criterion and should not be read as progress on the remaining occupation problem. Its role is narrower: it removes the last arithmetic gaps from the adjacent-resonance mechanism below quadratic dilation and identifies `m~n^2`, rather than generic off-lattice drift, as the first scale where that mechanism can genuinely change character.
