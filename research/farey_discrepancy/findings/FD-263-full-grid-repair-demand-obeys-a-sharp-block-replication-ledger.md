# FD-263 — Full-grid repair demand obeys a sharp block-replication ledger

- **Date:** 2026-09-22
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** exact divisor-response inversion / location-sensitive repair demand / Mertens-block replication / amplitude-density phase constraint / route sharpening
- **Depends on:** FD-225, FD-260, FD-261, FD-262
- **Classification:** `EXACT-DERIVED + DIVISOR-REPLICATION + LOCATION-SENSITIVE-L1-BOUND + SOURCE-DEMAND-CERTIFICATE + AMPLITUDE-DENSITY-TRADEOFF + ROUTE-RESTRICTION`

## Claim

FD-262 showed that the canonical full-grid Mertens repair has at most `D log D` depth amplification after the largest block-Mertens forcing amplitude is factored out. Keeping the locations of those forcing blocks gives a strictly sharper statement: **a forcing block at index `q` is replicated into a deep coefficient band only as many times as `q` has multiples in that band**. In particular, a large isolated block near the deepest scale is copied only once.

Retain the FD-262 notation

\[
R_N(m)=M(mN)+2(\mathscr A c)(m),
\qquad
B_q(N)=M(qN)-M((q-1)N),
\]

and put

\[
F_N(q):=\Delta R_N(q)-B_q(N).
\]

FD-262 gives exactly

\[
2c_d=\sum_{q\mid d}F_N(q).
\tag{1}
\]

For an integer `x` with `2x<=D`, define the divisor-replication multiplicity

\[
m_x(q)
:=
\#\{d:x<d\le2x,\ q\mid d\}
=
\left\lfloor\frac{2x}{q}\right\rfloor
-
\left\lfloor\frac{x}{q}\right\rfloor.
\tag{2}
\]

Then

\[
\boxed{
\sum_{x<d\le2x}|c_d|
\le
\frac12\sum_{q\le2x}|F_N(q)|m_x(q).
}
\tag{3}
\]

Hence the negative repair demand satisfies the same bound. Since

\[
m_x(q)\le \frac{2x}{q},
\tag{4}
\]

one also has the harmonic form

\[
\boxed{
\sum_{x<d\le2x}(-c_d)_+
\le
x\sum_{q\le2x}\frac{|\Delta R_N(q)-B_q(N)|}{q}.
}
\tag{5}
\]

For the FD-225 canonical nearest-integer full-grid repair, `|\Delta R_N(q)|<=2`, so

\[
\boxed{
R_N^{\rm neg}(x)
\le
\frac12\sum_{q\le2x}|B_q(N)|m_x(q)
+O(x\log x)
}
\tag{6}
\]

and therefore

\[
\boxed{
R_N^{\rm neg}(x)
\le
x\sum_{q\le2x}\frac{|B_q(N)|}{q}
+O(x\log x).
}
\tag{7}
\]

This identifies the source quantity that a deeper-block strategy must make large: not the maximum block-Mertens increment, but its **divisor-replication-weighted variation**, equivalently at coarse scale its harmonic variation.

The location information is decisive. For `x<q<=2x`,

\[
m_x(q)=1.
\tag{8}
\]

Thus one huge deep block contributes only one copy of its amplitude to the absolute repair budget on that band. The factor `x log x` in FD-262 is realizable only by forcing distributed across many divisor scales; it cannot be attached to an isolated deep maximum.

Combining (6) with the FD-261 phase boundary gives a quantitative necessary condition for the remaining “stronger deep arithmetic forcing” route. Let `x\asymp D`, let `A_N=N^{\theta+o(1)}` be the arithmetic amplitude against which the first-row and deep-band demands are being compared, and consider forcing blocks in an index shell

\[
Q<q\le2Q,
\qquad Q=D^{\rho+o(1)}.
\]

Suppose a candidate family in that shell has

\[
K=D^{\kappa+o(1)}
\]

blocks, each of size at most

\[
A_ND^{\delta+o(1)}.
\]

Its entire contribution to the right side of (6) is at most

\[
\boxed{
A_ND^{1-\rho+\kappa+\delta+o(1)}.
}
\tag{9}
\]

Since necessarily `\kappa<=\rho`, same-amplitude forcing (`\delta=0`) remains at most linear in depth, independently of where the blocks are placed or how densely one fills a polynomial index scale. For such a family to supply a demand strong enough to cross the general FD-260 threshold

\[
\alpha>2-\beta,
\qquad
\beta=\log_2\frac32,
\]

it is necessary that

\[
\boxed{
\kappa+\delta-\rho
>
1-\beta
=0.4150374992\ldots .
}
\tag{10}
\]

At the deepest index scale `Q\asymp D`, this becomes

\[
\boxed{
\kappa+\delta>2-\beta
=1.4150374992\ldots .
}
\tag{11}
\]

So a polynomially large deep maximum is not enough if it occurs on too few block indices. The surviving arithmetic route requires a genuine **amplitude-density product**: large block-Mertens increments must be sufficiently amplified and sufficiently numerous in the replication measure at the same time.

## 1. Exact replication ledger

Starting from (1), triangle inequality gives for every `d` in the band

\[
|c_d|
\le
\frac12\sum_{q\mid d}|F_N(q)|.
\]

Summing over `x<d<=2x` and exchanging the two finite sums yields

\[
\begin{aligned}
\sum_{x<d\le2x}|c_d|
&\le
\frac12
\sum_{q\le2x}|F_N(q)|
\#\{d:x<d\le2x,\ q\mid d\}\\
&=
\frac12\sum_{q\le2x}|F_N(q)|m_x(q),
\end{aligned}
\]

which is (3). No average-order divisor estimate has entered. The kernel `m_x(q)` is the exact finite replication count of forcing coordinate `q` into this coefficient band.

For `q<=x`, one has `m_x(q)<=x/q+1<=2x/q`; for `x<q<=2x`, equation (8) gives `m_x(q)=1<=2x/q`. Hence (4) and then (5).

This refines the mechanism behind FD-262. The earlier maximum bound replaced every `|F_N(q)|` by one common supremum before summing the replication counts. Equation (3) keeps the forcing profile attached to its actual divisor multiplicity.

## 2. Canonical rounded repair and the harmonic block-Mertens norm

For the FD-225 target,

\[
R_N(m)=\varepsilon_m,
\qquad |\varepsilon_m|\le1,
\]

so `|\Delta R_N(q)|<=2`. Splitting `F_N=\Delta R_N-B_N` in (3) gives

\[
R_N^{\rm neg}(x)
\le
\frac12\sum_{q\le2x}|B_q(N)|m_x(q)
+
\sum_{q\le2x}m_x(q).
\tag{12}
\]

The residual term is exactly a divisor count in the coefficient band:

\[
\sum_{q\le2x}m_x(q)
=
\sum_{x<d\le2x}\tau(d)
\ll x\log x.
\tag{13}
\]

Equations (12)--(13) prove (6). Using (4) on the Mertens term proves (7).

Thus the natural arithmetic forcing norm for this route is

\[
\mathcal V_N(x)
:=
\sum_{q\le2x}\frac{|B_q(N)|}{q},
\tag{14}
\]

or, more precisely, its finite replication version

\[
\mathcal W_N(x)
:=
\sum_{q\le2x}|B_q(N)|m_x(q).
\tag{15}
\]

A single very large value of `\mathcal B_N(2x)=\max|B_q(N)|` need not make either quantity large at the scale suggested by the maximum. Deep indices have little replication; shallow indices have large replication but there are correspondingly fewer of them at each multiplicative scale.

This does not prove cancellation in `\mathcal V_N` or `\mathcal W_N`; absolute values deliberately remove cancellation. It says instead that **even an arithmetic lower-bound strategy must populate the correct weighted norm** before the positive-cushion ceiling can see a superlinear source demand.

## 3. Amplitude-density phase constraint

Take `x\asymp D`, as in the deepest band of FD-261. If `Q<q<=2Q`, then (2) gives uniformly

\[
m_x(q)\ll \frac DQ.
\tag{16}
\]

Therefore any subset `S` of `K` indices in that shell with

\[
|B_q(N)|\le A_ND^{\delta+o(1)}
\qquad(q\in S)
\]

contributes at most

\[
\frac12\sum_{q\in S}|B_q(N)|m_x(q)
\le
A_ND^{1-\rho+\kappa+\delta+o(1)},
\]

which proves (9).

FD-261 says that, at the same arithmetic amplitude exponent, the general nonnegative cushion theorem can improve the first-row obstruction only if the negative repair demand has depth exponent strictly larger than

\[
2-\beta=1.4150374992\ldots .
\]

Consequently a polynomially localized block family can be responsible for such a demand only if (10) holds.

There is a useful density formulation before taking exponents. If a shell `Q<q<=2Q` contains `K` relevant forcing blocks of typical amplitude at most `A_N T`, then their repair contribution is

\[
\ll A_ND\left(\frac KQ\right)T.
\tag{17}
\]

To reach `A_ND^{2-\beta+\epsilon}` from that shell one therefore needs

\[
\boxed{
\left(\frac KQ\right)T
\ge
D^{1-\beta+\epsilon-o(1)}.
}
\tag{18}
\]

The factor `K/Q` is the density of large forcing blocks inside their index scale. Since it is at most a constant, amplitudes must grow by at least the missing power `D^(1-beta)`; if that growth occurs only sparsely, the amplitude requirement is stronger by the reciprocal density.

The same conclusion applies to the total forcing at exponent level by decomposing `q<=D` into dyadic index shells and `|B_q|/A_N` into dyadic amplitude bins. At polynomial depth there are only logarithmically many index shells and logarithmically many possible amplitude bins because trivially `|B_q(N)|<=N`. These counts are subpower, so a total contribution larger than `A_ND^(2-beta+epsilon)` forces at least one shell/bin to satisfy (18) up to `D^o(1)`.

This sharpens the remaining alternative in FD-262. “A stronger Mertens block somewhere deeper” is not enough. A successful source theorem must force a polynomially large **replication-weighted population** of stronger blocks.

## 4. Sharpness and finite stress test

The replication kernel in (3) is not an artifact of the proof. For an abstract forcing vector supported at one index `q_0`,

\[
F(q_0)=A,
\qquad F(q)=0\ (q\ne q_0),
\]

formula (1) gives

\[
c_d=
\frac A2\mathbf 1_{q_0\mid d}.
\]

Hence

\[
\sum_{x<d\le2x}|c_d|
=
\frac{|A|}{2}m_x(q_0),
\tag{19}
\]

so (3) is an equality. For `q_0>x`, the forcing is copied exactly once. For `q_0=1`, it is copied into every coefficient in the band. The location dependence therefore cannot be removed from an operator-level estimate.

A finite audit was also repeated at the FD-262 parameters `N=100`, `D=32`, `x=16`, using the canonical nearest-integer target with ties rounded to even. Direct inversion gives

\[
\sum_{16<d\le32}|c_d|=57,
\qquad
\sum_{16<d\le32}(-c_d)_+=26.
\]

The exact replication ledger (3) gives the upper bound `177`. If all forcing coordinates are first replaced by the common bound `\max|B_q|+\max|\Delta R_q|=18`, the same exact divisor count gives `621`. The finite computation is not used in the proof; it checks the endpoint convention and demonstrates concretely how much information can be lost by moving the maximum outside the replication sum.

## 5. Prior-art boundary and consequence

The algebra in (1)--(5) is classical Dirichlet-convolution bookkeeping: convolution with the constant-one function is a divisor sum, Möbius inversion is classical, and exchanging the finite divisor/multiple sums is standard. A targeted literature search around weighted `l^1` norms for Dirichlet convolution, divisor-sum finite sections, Lambert-series coefficient transforms, and Mertens block sums found those expected general frameworks but no theorem matching the repository-specific repair ledger and its FD-261 amplitude-density phase consequence. No external theorem is load-bearing here, so `SOURCES.md` requires no update.

The result is an upper-bound route restriction, not the missing source lower bound. It does not prove that actual Mertens blocks fail (18), and it does not improve any known Mertens estimate. In particular, sufficiently many sufficiently amplified deep blocks could still make the weighted forcing large.

What changes is the target. FD-262 reduced the canonical full-grid inverse to at most linear-log depth growth at fixed maximum forcing amplitude. FD-263 shows exactly how the remaining arithmetic escape would have to defeat that ceiling: **large deep forcing must occupy enough block indices to overcome the loss of divisor replication at large `q`**. Isolated deep spikes, or even a polynomially sparse family whose amplitude does not compensate its density, cannot generate the superlinear negative slack demand required by FD-261.

**Verdict.** The full-grid source route is now controlled by a sharp location-sensitive ledger. At fixed arithmetic scale, every complete polynomial block-index shell contributes only `D^(1+o(1))` repair mass, irrespective of its location. To make general positive-cushion depletion beat the first-row obstruction, deeper Mertens forcing must acquire more than `D^(1-beta)` additional amplitude in a sufficiently dense replication-weighted family, with `1-beta=0.415037...`. The live arithmetic question is therefore a joint amplitude-and-density question for consecutive Mertens blocks, not a search for an isolated larger block maximum.
