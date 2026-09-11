# FD-058 — maximal ambient-window localization removes the reciprocal-sample cardinality penalty

**Status:** `EXACT-DERIVED + LITERATURE-DERIVED + SOURCE-SPECIFIC + MAXIMAL-SHORT-INTERVAL + RECIPROCAL-FLOOR-SAMPLING + ZERO-FRONTIER + ADDITIVE-TRANSFER + ROUTE-REFINEMENT`.

`FD-057` proves a sharp statement about **pointwise-start cardinality**: if a reciprocal-floor transfer must itself start outside one common exceptional set, then the realizable sample has only `X/R_X` points and a schematic exceptional law `X R_X^{-c+o(1)}` beats that sample by cardinality only for `c>1`.

That threshold is real for that proof paradigm, but it is not the correct threshold for a **maximal** short-interval theorem. The maximal truncation already present in Theorem 1.1(i) of Matomäki--Radziwiłł--Shao--Tao--Teräväinen allows the desired reciprocal-floor interval to sit as a subinterval of a larger nonexceptional ambient interval. A fixed realizable transfer interval of length `asymp R_X` has `asymp R_X` different ambient starts that contain it. Thus maximality restores corridor-scale localization even though the transfer endpoint itself lies in a sparse set.

More precisely, let

\[
c(n):=\Delta\mathcal H(n)
=\sum_{dm=n}\frac{\mu(m)}d,
\qquad
\mathcal H(x)=\sum_{n\le x}c(n),
\]

and take a false-RH zero-frontier spike sequence

\[
A_X:=|\mathcal H(X)|=X^{\Theta+o(1)},
\qquad \frac12<\Theta<1.
\]

Let

\[
R_X=A_XL_X,
\qquad L_X=(\log X)^B
\]

for fixed `B>=0`, and choose one squarefree host

\[
q\equiv2\pmod4,
\qquad
Q_X\le q\le2Q_X,
\qquad
Q_X:=\left\lfloor\frac X{R_X}\right\rfloor.
\]

Its nearest nonsquarefree row is `q+2`, and the sampled source endpoint is

\[
x_q:=\left\lfloor\frac{qX}{q+2}\right\rfloor,
\qquad
h_q:=X-x_q
=\left\lceil\frac{2X}{q+2}\right\rceil
\asymp R_X.
\]

Set the ambient length

\[
H_X:=4R_X.
\]

Every integer start

\[
y\in[X-H_X,x_q]
\]

produces an ambient interval `(y,y+H_X]` containing the entire desired transfer interval `(x_q,X]`. Since `h_q<= (2+o(1))R_X`, the number of such containing starts is at least

\[
\boxed{
H_X-h_q+O(1)
\ge (2-o(1))R_X.
}
\tag{1}
\]

Consequently, if a maximal source estimate of the form

\[
\sup_{I\subset(y,y+H_X]}
\left|\sum_{n\in I}c(n)\right|
=o(A_X)
\tag{2}
\]

holds outside an exceptional set `\mathcal F_X` with

\[
|\mathcal F_X|=o(R_X),
\tag{3}
\]

then **this one fixed reciprocal-floor transfer is already good**. Indeed (1)--(3) give a nonexceptional containing start `y`, and the consecutive interval `(x_q,X]` is one of the subintervals in (2), so

\[
\boxed{
\mathcal H(x_q)=\mathcal H(X)+o(A_X).
}
\tag{4}
\]

No counting over the sparse set `\mathscr S_X` from `FD-057` is needed.

For a schematic power-saving exceptional law

\[
|\mathcal F_X|
\ll X R_X^{-c+o(1)},
\tag{5}
\]

condition (3) is equivalent at the exponent level to

\[
1-c\Theta<\Theta,
\]

hence to

\[
\boxed{
 c>\frac{1-\Theta}{\Theta}.
}
\tag{6}
\]

Thus maximal ambient-window localization restores the `FD-056` corridor threshold. The inverse-length threshold `c>1` from `FD-057` remains the correct benchmark only for arguments that insist that the **reciprocal-floor start itself** be nonexceptional. It is not a universal requirement for almost-all input.

## 1. The published maximal Möbius theorem transfers to a maximal source theorem

The preceding argument would be less useful if maximality were lost when passing from `mu` to the physical shell coefficient `c`. It is not.

Theorem 1.1(i) of Matomäki--Radziwiłł--Shao--Tao--Teräväinen is already maximal: their notation

\[
\left|\sum_{n\in J}\mu(n)\right|^*
\]

takes the supremum over arithmetic progressions contained in the ambient interval. In particular it controls every consecutive subinterval. For every fixed `K'>0`, at lengths above `X^(1/3+epsilon)` it gives

\[
\left|\sum_{n\in P}\mu(n)\right|
\ll
\frac H{(\log X)^{K'}}
\tag{7}
\]

for every arithmetic progression `P` inside a nonexceptional ambient interval of length `H`, with exceptional measure

\[
O_{K',\varepsilon}
\!\left(\frac X{(\log X)^{K'}}\right).
\tag{8}
\]

Fix an ambient source window `(y,y+H_X]` with `y\asymp X`, and let `I` be any consecutive integer subinterval of it. From the exact convolution,

\[
\sum_{n\in I}c(n)
=
\sum_{d\le 2X}\frac1d
\sum_{\substack{m:\ dm\in I}}\mu(m).
\tag{9}
\]

Choose

\[
D=(\log X)^C
\]

with `C>B+2`. For every `d<=D`, the inner interval in (9) lies inside an ambient interval at scale `X/d` and length `H_X/d+O(1)`. Because `Theta>1/2` and `d` is only polylogarithmic, these lengths lie safely in the range of (7) for one fixed `epsilon>0`, after an inessential fixed-factor dyadic cover.

For each `d`, pull the exceptional set in (8) back under `y -> floor(y/d)`. Every exceptional scaled start has at most `d` integer preimages, while the scaled exceptional set has size

\[
O\!\left(
\frac{X/d}{(\log X)^{K'}}
\right).
\]

Hence the bad `y` contributed by one `d` are

\[
O\!\left(
\frac X{(\log X)^{K'}}
\right),
\]

and the union over `d<=D` has size

\[
O\!\left(
\frac{DX}{(\log X)^{K'}}
\right).
\tag{10}
\]

Outside this union, the small-divisor contribution to (9) is uniformly, for **every** subinterval `I`,

\[
\begin{aligned}
\sum_{d\le D}\frac1d
\left|
\sum_{dm\in I}\mu(m)
\right|
&\ll
\sum_{d\le D}
\frac1d
\frac{H_X/d+O(1)}{(\log X)^{K'}}\\
&\ll
\frac{H_X}{(\log X)^{K'}}+O(1).
\end{aligned}
\tag{11}
\]

For `d>D`, no cancellation is needed. Trivial counting gives

\[
\begin{aligned}
\sum_{d>D}\frac1d
\#\{m:dm\in I\}
&\ll
H_X\sum_{d>D}\frac1{d^2}
+
\sum_{D<d\le2X}\frac1d\\
&\ll
\frac{H_X}{D}+\log X.
\end{aligned}
\tag{12}
\]

Combining (9)--(12), and choosing `K'` larger than `C` by an arbitrary fixed amount, yields the source-level maximal statement: for every fixed `K>0`, outside a set of starts of size

\[
\boxed{
O_K\!\left(\frac X{(\log X)^K}\right),
}
\tag{13}
\]

one has uniformly over all consecutive `I\subset(y,y+H_X]`

\[
\boxed{
\left|\sum_{n\in I}c(n)\right|
\ll
\frac{H_X}{(\log X)^{K'} }
+
\frac{H_X}{D}
+
\log X
=o(A_X),
}
\tag{14}
\]

after taking `C>B+2` and `K'>B+2`. Thus the exact `c=(n\mapsto1/n)*mu` convolution preserves the maximal character needed by the ambient-window argument, at only polylogarithmic exceptional-set cost.

## 2. Why the 2026 theorem still does not close the zero-frontier gap

The improvement is structural, not yet sufficient numerically. From (13), for every fixed `K`,

\[
\frac{X(\log X)^{-K}}{R_X}
=
X^{1-\Theta+o(1)}(\log X)^{-K-B}
\longrightarrow\infty.
\tag{15}
\]

So the available exceptional budget can still cover the entire containing-start interval in (1). The published theorem therefore does **not** certify a good ambient window around a prescribed zero-frontier spike.

What changes is the target for future quantitative almost-all input. A maximal theorem with an exceptional law of the schematic power form (5), and with enough analytic saving to make the maximal source error `o(A_X)`, would cross the localization barrier as soon as (6) holds. Near the critical line this still demands an exponent approaching one, but for every fixed `Theta>1/2` it is strictly weaker than the `c>1` point-sample requirement from `FD-057`.

This distinction matters because the strongest modern Möbius almost-all statements are naturally formulated with maximal truncation. The adaptive Farey endpoint does not need to avoid the bad set itself; it only needs to be **coverable by one nearby good ambient window**.

## 3. Adversarial checks and exact boundary

There is no contradiction with `FD-057`. Its theorem is explicitly a cardinality statement for a common exceptional set of the represented starts themselves. Under that oracle, the sample really has only `X/R_X` points and `c>1` is sharp at the exponent level. `FD-058` changes the admissible use of the analytic input: maximality supplies `asymp R_X` alternative ambient starts for each fixed represented interval.

The containment is one-sided and exact. If `y in [X-H_X,x_q]`, then `y<=x_q<X<=y+H_X`, so `(x_q,X]` is a consecutive arithmetic progression inside the ambient interval. This is precisely allowed by the `*`-norm definition in the 2026 theorem; no interpolation between starts or assumption about persistence of badness is used.

The convolution transfer does not silently union polynomially many exceptional sets. The large-`d` tail is handled trivially, so only `D=(log X)^C` scaled Möbius problems are needed. Their pulled-back exceptional sets cost only a polylogarithmic factor, absorbable because the literature theorem allows an arbitrary fixed logarithmic exponent. Endpoint rounding changes the scaled ambient intervals by `O(1)` and is absorbed by the maximal estimate and the `O(log X)` tail term.

The fixed condition `Theta<1` is used only to keep `H_X=X^(Theta+o(1))` within a genuine short-interval range with one fixed margin. The near-critical regime `1/2<Theta<=0.55` targeted by `FD-055`--`FD-057` satisfies this automatically. The finding does not claim a power-saving exceptional estimate that is not presently known, nor does it prove positive nonsquarefree occupation.

## 4. Prior-art boundary and consequence for the live route

The load-bearing external result remains Theorem 1.1(i) of Kaisa Matomäki, Maksym Radziwiłł, Xuancheng Shao, Terence Tao and Joni Teräväinen, *Higher uniformity of arithmetic functions in short intervals II. Almost all intervals*, Inventiones Mathematicae **244** (2026), 967--1091, DOI `10.1007/s00222-026-01408-6`, already anchored in `SOURCES.md`. Its maximal arithmetic-progression norm, interval range, and logarithmic exceptional estimate are used exactly as published. No novelty is claimed for Dirichlet convolution, divisor splitting, or maximal truncation themselves.

A targeted prior-art search around maximal Möbius short intervals, the Dirichlet series `zeta(s+1)/zeta(s)`, Farey discrepancy, and reciprocal/floor-selected starts did not locate the present ambient-window localization argument or its application to this adaptive Jordan transfer. No new external theorem is load-bearing, so `SOURCES.md` remains unchanged.

The durable strategic correction is therefore narrow but important. The live target after `FD-057` is **not necessarily** a theorem that sees the sparse reciprocal-floor sample directly, nor is `c>1` unavoidable. For maximal short-interval input, one can localize through containing ambient windows and return to the corridor exponent

\[
\boxed{
\frac{1-\Theta}{\Theta}.
}
\]

The current 2026 logarithmic exceptional bound is still far too large, so the zero-frontier occupation problem remains open. But future work should distinguish two genuinely different localization regimes: pointwise-start theorems pay the inverse-length `c>1` penalty; maximal ambient-window theorems pay only the corridor-scale threshold (6).