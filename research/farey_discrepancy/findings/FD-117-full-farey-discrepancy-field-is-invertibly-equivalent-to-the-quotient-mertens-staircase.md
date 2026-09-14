# FD-117 — the full Farey discrepancy field is invertibly equivalent to the quotient Mertens staircase

**Status:** `LITERATURE+EXACT-DERIVED + REPRESENTATION-CLASSIFICATION + INVERTIBLE-MERTENS-EQUIVALENCE + MOVING-ANCHOR-COLLAPSE + NEGATIVE/ROUTE-RESTRICTION`.

`FD-116` left moving endpoints, growing endpoint denominators, and growing endpoint families as possible ways for the absolute-discrepancy common mode to escape the fixed-periodic-filter classification. At the level of the **complete cumulative Farey discrepancy field**, none of those changes creates an arithmetic source independent of the denominator-shell/Mertens frame.

For the interior Farey discrepancy of `FD-001`,

\[
D_N(x)
=
\#\{y\in\mathcal F_N^\circ:y\le x\}
-
C_Nx,
\qquad
C_N=\sum_{q=2}^N\varphi(q),
\tag{1}
\]

put

\[
s_m(x):=\lfloor mx\rfloor-mx,
\qquad
M(t):=\sum_{n\le t}\mu(n).
\tag{2}
\]

Then for every `N>=2` and every `0<=x<=1`,

\[
\boxed{
D_N(x)
=
x-\lfloor x\rfloor
+
\sum_{m\le N}
s_m(x)\,
M\!\left(\left\lfloor\frac Nm\right\rfloor\right).
}
\tag{3}
\]

Thus **the entire function** `x -> D_N(x)`, not merely a fixed rational anchor or a finite set of Fourier modes, is a deterministic affine linear image of the quotient-Mertens vector

\[
\mathbf M_N
=
\left(
M\!\left(\left\lfloor\frac Nm\right\rfloor\right)
\right)_{1\le m\le N}.
\tag{4}
\]

The reduction is also invertible. With the Fourier convention of `FD-001`, for every `1<=k<=N`,

\[
A_N(k)
:=
1+2\pi i k\,\widehat D_N(k)
=
\sum_{d\mid k}
d\,M\!\left(\left\lfloor\frac Nd\right\rfloor\right),
\tag{5}
\]

so divisor Möbius inversion gives

\[
\boxed{
M\!\left(\left\lfloor\frac Nk\right\rfloor\right)
=
\frac1k
\sum_{d\mid k}
\mu(k/d)\,
\left(
1+2\pi i d\,\widehat D_N(d)
\right).
}
\tag{6}
\]

Consequently the complete discrepancy field and the quotient-Mertens staircase contain exactly the same arithmetic information under these explicit finite transforms.

This closes the moving-anchor escape left by `FD-116` **at the information-source level**. An endpoint `x_N` may move arbitrarily with `N`, its denominator may grow, and one may evaluate `D_N` on an arbitrarily large predeclared endpoint family: all such values are evaluations of the same field (3). Even a deterministic endpoint-selection rule that inspects the complete same-horizon discrepancy field first produces only a nonlinear functional of `\mathbf M_N`; it does not manufacture a second arithmetic source.

The statement is deliberately not a smallness theorem. A moving endpoint, nonlinear selector, ordered minor, or refinement statistic may still reorganize the Mertens-controlled information in a way that makes a stronger estimate provable. What is ruled out is using moving/growing discrepancy coordinates themselves as evidence of an information carrier independent of the classical Möbius/Mertens channel.

## 1. Exact pointwise collapse

`FD-001` proves the shell identity

\[
e_q(x)
=
\sum_{m\mid q}
\mu(q/m)\,s_m(x),
\qquad
q\ge2,
\tag{7}
\]

and

\[
D_N(x)=\sum_{q=2}^Ne_q(x).
\tag{8}
\]

Temporarily include the formal `q=1` shell. It is

\[
e_1(x)=s_1(x)=\lfloor x\rfloor-x.
\tag{9}
\]

Since all sums are finite,

\[
\begin{aligned}
D_N(x)+e_1(x)
&=
\sum_{q\le N}
\sum_{m\mid q}
\mu(q/m)s_m(x)\\
&=
\sum_{m\le N}
s_m(x)
\sum_{r\le N/m}\mu(r)\\
&=
\sum_{m\le N}
s_m(x)
M\!\left(\left\lfloor\frac Nm\right\rfloor\right).
\end{aligned}
\tag{10}
\]

Subtracting (9) proves (3). The endpoint correction `x-floor(x)` is necessary only to keep the convention exact simultaneously at `x=1`; for `0<=x<1` it is simply `x`.

Equation (3) is stronger than the fixed-rational statement of `FD-116` in the relevant representation sense. Rationality is not used. No periodicity, bounded denominator, or fixed endpoint is required. If

\[
X_N=\{x_{N,1},\ldots,x_{N,K_N}\}\subset[0,1]
\tag{11}
\]

is any finite endpoint family, possibly with `K_N -> infinity` and with the points depending on `N`, then

\[
\boxed{
\bigl(D_N(x_{N,j})\bigr)_{j=1}^{K_N}
=
\mathbf c_N+B_N\mathbf M_N
}
\tag{12}
\]

for the deterministic matrix with entries

\[
(B_N)_{j,m}=s_m(x_{N,j})
\tag{13}
\]

and the endpoint correction vector `\mathbf c_N=(x_{N,j}-floor(x_{N,j}))_j`.

Thus increasing endpoint count or denominator only changes the observation matrix. It does not add a source coordinate outside `\mathbf M_N`.

## 2. The collapse is invertible

The one-way factorization above would still leave open the possibility that the quotient-Mertens representation is a very lossy overparameterization of the Farey field. It is not.

`FD-001` gives, for every nonzero Fourier mode,

\[
2\pi i k\,\widehat D_N(k)
=
\sum_{\substack{d\mid k\\d\le N}}
d\,M\!\left(\left\lfloor\frac Nd\right\rfloor\right)-1.
\tag{14}
\]

For `1<=k<=N`, every divisor of `k` is at most `N`, so (14) is exactly (5). Define

\[
B_N(d):=
d\,M\!\left(\left\lfloor\frac Nd\right\rfloor\right).
\tag{15}
\]

Then `A_N(k)=sum_(d|k) B_N(d)`. Ordinary divisor Möbius inversion therefore yields

\[
B_N(k)
=
\sum_{d\mid k}
\mu(k/d)A_N(d),
\tag{16}
\]

which is (6).

Hence the first `N` Fourier coefficients of `D_N` recover every entry of the indexed quotient staircase (4), while (3) recovers `D_N` from that staircase. In particular

\[
M(N)=1+2\pi i\,\widehat D_N(1),
\tag{17}
\]

the first-mode identity already isolated in `FD-001`, is only the first coordinate of a complete finite inversion.

There are many repeated entries in (4). If

\[
\mathcal Q_N
:=
\left\{
\left\lfloor\frac Nm\right\rfloor:
1\le m\le N
\right\},
\tag{18}
\]

then grouping (3) by equal floor quotients gives

\[
D_N(x)
=
x-\lfloor x\rfloor
+
\sum_{r\in\mathcal Q_N}
M(r)\,K_{N,r}(x),
\tag{19}
\]

where

\[
K_{N,r}(x)
:=
\sum_{\substack{m\le N\\\lfloor N/m\rfloor=r}}
s_m(x).
\tag{20}
\]

The elementary hyperbola decomposition gives

\[
|\mathcal Q_N|=2\sqrt N+O(1).
\tag{21}
\]

Because (6) recovers every quotient value, the formal affine source map in (19) is injective: the complete field has exactly the quotient-Mertens source rank `|\mathcal Q_N|`, not the number of endpoint samples used to observe it.

## 3. Moving and adaptive anchors do not create a second source

The representation consequence for the frontier after `FD-116` is broader than fixed rational periodicity.

A moving rational anchor `A_N=a_N/b_N` with `b_N -> infinity` is covered by (3) without any denominator restriction. So is an irrational endpoint, a family of endpoints whose cardinality grows faster than `sqrt(N)`, or the entire continuum of endpoint values. Such choices may produce complicated observation matrices, but the arithmetic coefficient vector remains the same quotient-Mertens staircase.

The same remains true for a deterministic selector that uses only the cumulative discrepancy field. If

\[
x_N=\mathcal S_N(D_N)
\tag{22}
\]

for any predeclared rule `\mathcal S_N`, then (3) first reconstructs the entire input field from `\mathbf M_N`; consequently

\[
D_N(x_N)
=
\mathcal T_N(\mathbf M_N)
\tag{23}
\]

for a deterministic, generally nonlinear functional `\mathcal T_N`. Adaptivity can change the functional class, but not the source information available to it.

Across horizons the corresponding statement is equally exact. The history

\[
(D_2,\ldots,D_N)
\tag{24}
\]

is reconstructible from the Mertens path `(M(1),...,M(N))` by (3), while (17) applied at each horizon reconstructs `M(n)` from `D_n`. Thus the full cumulative-discrepancy history and the ordinary Mertens history are mutually reconstructible by explicit finite formulas.

This does **not** imply that every useful Farey proof must look like a standard Mertens proof. A nonlinear geometric transform can expose coercivity, cancellation, positivity, or locality that is opaque in the source coordinates while remaining information-equivalent to them. The result only rejects the stronger claim that changing the endpoint schedule, denominator scale, family size, or same-field selection law creates a new arithmetic channel.

## 4. Stress tests, prior-art boundary, and research consequence

Two exact regression checks were used only to guard the bookkeeping. First, direct rational enumeration of `\mathcal F_N^\circ` agreed with (3), including `x=0` and `x=1`, for all tested horizons `2<=N<25` and a collection of fixed and moving rational endpoints. Second, using the Ramanujan-sum formula of `FD-001`, (6) recovered `M(floor(N/k))` for every pair `1<=k<=N<=100`. Neither computation is evidence for the theorem; (3) and (6) are finite algebraic identities.

The underlying Farey--Möbius connection is classical. García (2025), already anchored in `SOURCES.md`, gives exact Möbius/Mertens formulas for Farey rank and local discrepancy, including endpoints that need not be fixed Farey fractions. `FD-001` already contains the load-bearing shell identity (7) and Fourier formula (14). No novelty is claimed for Möbius inversion, the hyperbola floor-quotient set, or the fact that Farey discrepancy is controlled by Mertens data.

The durable Mathia delta is the **bidirectional representation classification at the current frontier**: composing the pointwise shell collapse with the inverse Fourier/divisor transform shows that the entire cumulative discrepancy field is not merely bounded by or expressible through Mertens; it is explicitly information-equivalent to the quotient-Mertens staircase. Therefore the moving-anchor, growing-denominator, and growing-family escapes left open by `FD-116` do not evade the known source frame.

For `CLUE-ordered-plucker-refinement-transfer.md`, this resolves the attempted independent-discrepancy-source route negatively. Any carrier built only from cumulative Farey discrepancy fields across one or many horizons is ultimately a transform of the Mertens path. A Plücker/refinement construction can still be valuable if it proves a **quantitatively stronger estimate for that same source**; nonzero minors, moving anchors, or growing observation dimension no longer suffice as evidence of source independence.

No stronger Franel--Landau estimate, Mertens bound, or RH consequence is proved here. No new external theorem is load-bearing, so `SOURCES.md` requires no change.
