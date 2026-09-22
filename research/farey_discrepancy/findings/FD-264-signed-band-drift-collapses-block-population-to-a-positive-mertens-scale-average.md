# FD-264 — Signed band drift collapses block population to a positive Mertens scale average

- **Date:** 2026-09-22
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** full-grid repair / signed band drift / exact replication kernel / Abel summation / Mertens scale average / source-side route pruning
- **Depends on:** FD-225, FD-260, FD-261, FD-262, FD-263
- **Classification:** `EXACT-DERIVED + SOURCE-SIDE-OBSTRUCTION + SIGNED-BAND-IDENTITY + POSITIVE-SCALE-AVERAGE + DEEP-POPULATION-CANCELLATION + ROUTE-PRUNING`

## Claim

FD-263 shows that the **absolute** repair mass in a divisor band is governed by the replication kernel

\[
m_x(q)
:=
\#\{d:x<d\le 2x,\ q\mid d\}
=
\left\lfloor\frac{2x}{q}\right\rfloor
-
\left\lfloor\frac{x}{q}\right\rfloor .
\]

For the **signed** band sum the same kernel has much stronger structure. For every positive integer `x`,

\[
\boxed{
 m_x(q)=
 \left\lfloor\frac{x}{q}+\frac12\right\rfloor
}
\tag{1}
\]

and hence `m_x(q)` is nonincreasing in `q`. Put `m_x(2x+1)=0` and

\[
w_x(q):=m_x(q)-m_x(q+1),
\qquad 1\le q\le 2x.
\tag{2}
\]

Then

\[
\boxed{
w_x(q)\ge0,
\qquad
\sum_{q\le2x}w_x(q)=x.
}
\tag{3}
\]

Thus

\[
\pi_x(q):=\frac{w_x(q)}x
\tag{4}
\]

is an exact probability measure on the scale indices `1,...,2x`.

For the FD-262--FD-263 full-grid repair, write

\[
R_N(m)=M(mN)+2(\mathscr A c)(m),
\qquad
B_q(N)=M(qN)-M((q-1)N),
\]

with `R_N(0)=M(0)=0`. The exact inverse is

\[
2c_d
=
\sum_{q\mid d}
\bigl(\Delta R_N(q)-B_q(N)\bigr).
\tag{5}
\]

Then the signed coefficient drift across the complete band satisfies the exact identity

\[
\boxed{
2\sum_{x<d\le2x}c_d
=
\sum_{q\le2x}w_x(q)
\bigl(R_N(q)-M(qN)\bigr).
}
\tag{6}
\]

Equivalently, with the positive averaging operator

\[
(\mathcal P_x A)
:=
\sum_{q\le2x}\pi_x(q)A(q),
\tag{7}
\]

one has

\[
\boxed{
\sum_{x<d\le2x}c_d
=
\frac{x}{2}
\left(
\mathcal P_x R_N
-
\mathcal P_x[M(N\,\cdot)]
\right).
}
\tag{8}
\]

For the canonical nearest-integer full-grid repair of FD-225, `|R_N(q)|\le1`. Therefore

\[
\boxed{
\left|
\sum_{x<d\le2x}c_d
+
\frac{x}{2}\mathcal P_x[M(N\,\cdot)]
\right|
\le\frac{x}{2}.
}
\tag{9}
\]

In particular, if

\[
R_N^-(x)
:=
\sum_{x<d\le2x}(-c_d)_+,
\]

then

\[
\boxed{
R_N^-(x)
\ge
\frac{x}{2}
\left(
\mathcal P_x[M(N\,\cdot)]-1
\right)_+.
}
\tag{10}
\]

The analogous positive-part inequality holds with `M` replaced by `-M`, and

\[
\sum_{x<d\le2x}|c_d|
\ge
\frac{x}{2}
\left(
\left|\mathcal P_x[M(N\,\cdot)]\right|-1
\right)_+.
\tag{11}
\]

The strategic consequence is negative but sharp: **block population cannot amplify a signed-band lower bound.** The weights in (7) have total mass one, so

\[
\left|\mathcal P_x[M(N\,\cdot)]\right|
\le
\max_{q\le2x}|M(qN)|.
\tag{12}
\]

Thus, after the arithmetic amplitude is factored out, every lower-bound strategy that sees the repair only through the signed band total has at most linear depth amplification `O(x)`. At `x\asymp D` this cannot supply the `D^{2-\beta}` demand required by FD-261 to make the general FD-260 positive-cushion ceiling beat the first-row obstruction, where

\[
\beta=\log_2\frac32,
\qquad
1-\beta=0.4150374992\ldots .
\]

The amplitude-density escape isolated by FD-263 therefore belongs intrinsically to an `l^1` or one-sided **within-band variation** problem. It cannot be recovered from a large negative signed band drift, even if many deep Mertens blocks are simultaneously large.

## 1. The replication count is a nearest-integer quotient

Write

\[
x=aq+r,
\qquad
0\le r<q.
\]

Then

\[
\begin{aligned}
m_x(q)
&=
\left(2a+\left\lfloor\frac{2r}{q}\right\rfloor\right)-a\\
&=
a+\mathbf 1_{\{r\ge q/2\}}\\
&=
\left\lfloor\frac{x}{q}+\frac12\right\rfloor,
\end{aligned}
\]

which proves (1). Since `x/q` decreases with `q`, the right-hand side is nonincreasing. Therefore the first assertion in (3) follows, and telescoping gives

\[
\sum_{q=1}^{2x}w_x(q)
=m_x(1)-m_x(2x+1)
=x.
\]

There are two useful exact consequences. First, for `x\le q\le2x`,

\[
m_x(q)=1.
\tag{13}
\]

Hence

\[
\boxed{
w_x(q)=0
\quad(x\le q<2x),
\qquad
w_x(2x)=1.
}
\tag{14}
\]

Second, for every `0\le Q<2x`,

\[
\boxed{
\sum_{q=Q+1}^{2x}w_x(q)
=m_x(Q+1)
=
\left\lfloor
\frac{x}{Q+1}+\frac12
\right\rfloor .
}
\tag{15}
\]

So the normalized tail of `\pi_x` is approximately `1/(Q+1)`, while the entire deepest index interval `(x,2x)` has zero interior weight. At fixed `q`,

\[
\frac{w_x(q)}x
\longrightarrow
\frac1q-\frac1{q+1}
=
\frac1{q(q+1)}.
\tag{16}
\]

Equation (15) makes the convergence tight, so `\pi_x` tends to the probability law `1/(q(q+1))` on fixed scale indices. In particular asymptotically one half of the signed-band averaging weight sits already at `q=1`, one sixth at `q=2`, and the remaining tail decays harmonically in the scale index.

This is qualitatively different from the absolute ledger of FD-263. There every forcing block in `(x,2x]` is copied once into the coefficient band. In the signed aggregate those copies telescope: for example,

\[
\sum_{x<q\le2x}B_q(N)m_x(q)
=
\sum_{x<q\le2x}B_q(N)
=M(2xN)-M(xN).
\tag{17}
\]

Thus a dense population of deep blocks can create large `l^1` repair mass, but its signed contribution depends only on its net endpoint increment.

## 2. Abel summation turns the signed ledger into a positive scale average

Let `A(0)=0` be any finite sequence. Since `w_x(q)=m_x(q)-m_x(q+1)`, ordinary discrete summation by parts gives

\[
\boxed{
\sum_{q=1}^{2x}
\bigl(A(q)-A(q-1)\bigr)m_x(q)
=
\sum_{q=1}^{2x}A(q)w_x(q).
}
\tag{18}
\]

Now sum the exact inverse (5) over `x<d\le2x` and exchange the finite divisor and multiple sums. Exactly as in FD-263,

\[
2\sum_{x<d\le2x}c_d
=
\sum_{q\le2x}
\bigl(\Delta R_N(q)-B_q(N)\bigr)m_x(q).
\tag{19}
\]

But

\[
B_q(N)
=
M(qN)-M((q-1)N),
\]

so applying (18) first to `R_N` and then to `M(qN)` proves (6)--(8).

No triangle inequality has been used. That is exactly why the logarithmic divisor replication visible in FD-262 and the amplitude-density ledger of FD-263 disappear from the signed total: they measure variation before cancellation, while (18) performs the cancellation explicitly.

For the canonical rounded target, `|R_N(q)|\le1`, and positivity of the weights gives

\[
|\mathcal P_xR_N|\le1.
\]

Equation (9) follows. Since

\[
\sum(-c_d)_+
\ge
\left(-\sum c_d\right)_+,
\]

(10) follows immediately; (11) is the corresponding total-variation statement.

## 3. Signed drift cannot supply the missing superlinear depth exponent

Suppose that on a family of horizons the relevant Mertens-prefix amplitude up to scale `2D` is bounded by

\[
\max_{q\le2D}|M(qN)|
\le
A_ND^{\delta+o(1)}.
\tag{20}
\]

Taking `x\asymp D`, equations (8) and (12) give

\[
\boxed{
\left|
\sum_{x<d\le2x}c_d
\right|
\le
A_ND^{1+\delta+o(1)}+O(D).
}
\tag{21}
\]

At the same arithmetic reference amplitude `A_N`, FD-261 requires a negative-slack demand larger than

\[
A_ND^{2-\beta+o(1)}
\]

before the general FD-260 cushion depletion can become decisive at or before the first-row scale. A signed-band argument can reach that exponent only if

\[
\boxed{
\delta>1-\beta
=0.4150374992\ldots .
}
\tag{22}
\]

In particular, **no amount of same-amplitude block density helps**. If all relevant Mertens prefixes remain within the same arithmetic power scale (`delta=0`), the signed aggregate is only linear in `D`, even if every one of the `O(D)` consecutive blocks is large. This is the signed counterpart of the FD-263 amplitude-density ledger: density is useful only before cancellation, in an `l^1` or one-sided coefficient statistic.

This distinction matters for the next source theorem. It is not enough to prove that the canonical repair has a negative *mean* on a deep divisor band. A mean-based lower bound is structurally capped at linear depth amplification. To exploit the FD-263 population mechanism one must prove that the repair oscillates with enough one-sided magnitude **inside** the band so that

\[
\sum_{x<d\le2x}(-c_d)_+
\]

is much larger than

\[
\left(-\sum_{x<d\le2x}c_d\right)_+.
\]

That is now the precise gap between the remaining arithmetic route and the already-settled full-grid average drift.

## 4. Finite stress test: the one-sided mass is genuinely invisible to the drift

Use the same audit point as FD-263: `N=100`, `x=16`, and the canonical nearest-integer target with ties rounded to even. The replication-jump weights are supported at

\[
q\in\{1,2,3,4,6,10,32\}
\]

with respective weights

\[
8,3,1,1,1,1,1.
\]

They are nonnegative and sum to `16`, exactly as (3) predicts. Direct computation gives

\[
\sum_qw_{16}(q)M(100q)=-3,
\qquad
\sum_qw_{16}(q)R_{100}(q)=7.
\]

Therefore (6) gives

\[
\sum_{16<d\le32}c_d=5.
\]

But direct inversion gives simultaneously

\[
\sum_{16<d\le32}(-c_d)_+=26,
\qquad
\sum_{16<d\le32}|c_d|=57.
\]

So the signed drift is not merely a loose proxy for the one-sided demand in this finite example: it even has the opposite orientation from the negative mass that a positive cushion must cover. The missing quantity is coefficient-level variation, not another estimate of the band mean.

The endpoint conventions were also checked for every integer `1\le x\le200`: the identity (1), monotonicity of `m_x`, positivity and total mass of `w_x`, and the Abel identity (18) all hold exactly. The finite checks are reproducibility guards only; the proof above is exact for every positive integer `x`.

## 5. Prior-art boundary and consequence

The ingredients of (1)--(3) and (18) are classical: floor-quotient divisor counting, finite Dirichlet-convolution bookkeeping, and ordinary Abel summation. Targeted searches around dyadic divisor intervals, Lambert/Dirichlet convolution prefix sums, floor-quotient grouping, and weighted Mertens averages found the expected classical frameworks but no source that packages this particular nearest-integer replication probability with the FD-225 repair inverse or its FD-260--FD-263 phase consequence. No external theorem is load-bearing, so `SOURCES.md` requires no update.

No novelty is claimed for the standalone floor or summation-by-parts identities. The useful new statement for this research line is the separation they expose:

- the **absolute** repair ledger retains block population and can in principle accumulate one-sided mass through many forcing indices;
- the **signed** repair drift is a positive probability average of Mertens prefix values and therefore cannot acquire any density amplification.

This is a route-pruning result, not the missing source lower bound. It does not show that the one-sided negative repair mass is small, nor does it rule out the FD-263 amplitude-density escape. Instead it says exactly what such an escape must prove: substantial within-band sign variation whose negative part survives after the signed average has cancelled.

**Verdict.** The canonical full-grid problem has two sharply different source observables. Signed band drift is head-weighted, probability-normalized, and at most linear in divisor depth at fixed arithmetic amplitude. The only remaining way for the FD-260 positive-cushion obstruction to improve the first-row boundary is through genuinely `l^1`/one-sided coefficient variation (or through a stronger cone such as FD-259), not through a large negative band mean.