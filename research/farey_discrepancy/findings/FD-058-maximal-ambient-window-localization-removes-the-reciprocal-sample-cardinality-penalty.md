# FD-058 — maximal ambient-window localization removes the reciprocal-sample cardinality penalty

**Status:** `EXACT-DERIVED + LITERATURE-DERIVED + SOURCE-SPECIFIC + MAXIMAL-SHORT-INTERVAL + RECIPROCAL-FLOOR-SAMPLING + ZERO-FRONTIER + ADDITIVE-TRANSFER + ROUTE-REFINEMENT`.

`FD-057` proves a sharp statement about **pointwise-start cardinality**: if a reciprocal-floor transfer must itself start outside one common exceptional set, then the realizable sample has only `X/R_X` points and a schematic exceptional law `X R_X^{-c+o(1)}` beats that sample by cardinality only for `c>1`.

That threshold is real for that proof paradigm, but it is not the correct threshold for a **maximal** short-interval theorem. The maximal truncation already present in Theorem 1.1(i) of Matomäki--Radziwiłł--Shao--Tao--Teräväinen allows the desired reciprocal-floor interval to sit as a subinterval of a larger nonexceptional ambient interval. A fixed realizable transfer interval of length `asymp R_X` is contained in a real interval of ambient starts of length `asymp R_X`. Thus maximality restores corridor-scale localization even though the transfer endpoint itself lies in a sparse set.

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
H_X:=4R_X
\]

and the real containing-start interval

\[
J_X:=[X-H_X,x_q].
\]

Every real `y\in J_X` produces an ambient interval `(y,y+H_X]` containing the entire desired transfer interval `(x_q,X]`. Since `h_q<= (2+o(1))R_X`, its Lebesgue measure satisfies

\[
\boxed{
m(J_X)=H_X-h_q
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

holds outside a measurable exceptional set `\mathcal F_X` with

\[
m(\mathcal F_X)=o(R_X),
\tag{3}
\]

then **this one fixed reciprocal-floor transfer is already good**. Indeed (1)--(3) imply that `J_X` cannot be contained in `\mathcal F_X`, so there is a nonexceptional real containing start `y`; the consecutive integer interval `(x_q,X]` is one of the subintervals in (2), hence

\[
\boxed{
\mathcal H(x_q)=\mathcal H(X)+o(A_X).
}
\tag{4}
\]

No counting over the sparse set `\mathscr S_X` from `FD-057` is needed.

For a schematic power-saving exceptional law

\[
m(\mathcal F_X)
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

for every arithmetic progression `P` inside a nonexceptional ambient interval of length `H`, outside a measurable set of real starts of Lebesgue measure

\[
O_{K',\varepsilon}
\!\left(\frac X{(\log X)^{K'}}\right).
\tag{8}
\]

Let `J_X` be the real containing-start interval above and choose

\[
D=(\log X)^C
\]

with `C>B+2`. For every `d<=D`, put

\[
X_d:=\frac{X}{2d},
\qquad
H_d:=\frac{H_X}{d}.
\]

Since `H_X=o(X)`, for all sufficiently large `X` and every `y\in J_X`,

\[
\frac yd\in[X_d,2X_d].
\]

Choose a fixed `epsilon>0` below both `Theta-1/3` and `1-Theta`. Uniformly for polylogarithmic `d`, the lengths `H_d` lie in the range of (7), because `H_X=X^{\Theta+o(1)}` and `\log(X/d)\sim\log X`. Applying the theorem at scale `X_d` and length `H_d` gives a measurable exceptional set

\[
E_d\subset[X_d,2X_d],
\qquad
m(E_d)
\ll_{K',\varepsilon}
\frac{X/d}{(\log X)^{K'}}.
\]

Pull it back under the real scaling map by defining

\[
B_d:=\{y\in J_X:y/d\in E_d\}.
\]

Lebesgue scaling gives the exact Jacobian factor

\[
\boxed{
m(B_d)
=d\,m\!\left(E_d\cap(J_X/d)\right)
\le d\,m(E_d)
\ll_{K',\varepsilon}
\frac X{(\log X)^{K'}}.
}
\tag{9}
\]

Hence the simultaneous bad set for all small divisors obeys

\[
\boxed{
m\!\left(\bigcup_{d\le D}B_d\right)
\ll
\frac{DX}{(\log X)^{K'}}.
}
\tag{10}
\]

Now take a real `y\in J_X` outside this union and any consecutive integer subinterval `I\subset(y,y+H_X]`. From the exact convolution,

\[
\sum_{n\in I}c(n)
=
\sum_{d\le 2X}\frac1d
\sum_{\substack{m:\ dm\in I}}\mu(m).
\tag{11}
\]

For each `d<=D`, the set

\[
P_{d,I}:=\{m\in\mathbb Z:dm\in I\}
\]

is itself a consecutive arithmetic progression contained exactly in

\[
(y/d,(y+H_X)/d]\cap\mathbb Z.
\]

Therefore the maximal star norm controls every inner sum in (11) simultaneously for that same real `y`, with no discretization of the exceptional set and no endpoint-rounding argument. The small-divisor contribution is uniformly, for every such `I`,

\[
\begin{aligned}
\sum_{d\le D}\frac1d
\left|
\sum_{m\in P_{d,I}}\mu(m)
\right|
&\ll
\sum_{d\le D}
\frac1d
\frac{H_X/d}{(\log X)^{K'}}\\
&\ll
\frac{H_X}{(\log X)^{K'}}.
\end{aligned}
\tag{12}
\]

For `d>D`, no cancellation is needed. Trivial counting gives

\[
\begin{aligned}
\sum_{d>D}\frac1d
\#P_{d,I}
&\ll
H_X\sum_{d>D}\frac1{d^2}
+
\sum_{D<d\le2X}\frac1d\\
&\ll
\frac{H_X}{D}+\log X.
\end{aligned}
\]

Combining these bounds and choosing `K'` larger than `C+K` yields the source-level maximal statement: for every fixed `K>0`, outside a measurable set of real starts of Lebesgue measure

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

after taking `C>B+2` and `K'>B+2` as well. Thus the exact `c=(n\mapsto1/n)*mu` convolution preserves the maximal character needed by the ambient-window argument, at only polylogarithmic exceptional-measure cost.

## 2. Why the 2026 theorem still does not close the zero-frontier gap

The improvement is structural, not yet sufficient numerically. From (13), for every fixed `K`,

\[
\frac{X(\log X)^{-K}}{R_X}
=
X^{1-\Theta+o(1)}(\log X)^{-K-B}
\longrightarrow\infty.
\tag{15}
\]

So the available exceptional-measure budget can still cover the entire real containing-start interval `J_X` from (1). The published theorem therefore does **not** certify a good ambient window around a prescribed zero-frontier spike.

What changes is the target for future quantitative almost-all input. A maximal theorem with an exceptional law of the schematic power form (5), and with enough analytic saving to make the maximal source error `o(A_X)`, would cross the localization barrier as soon as (6) holds. Near the critical line this still demands an exponent approaching one, but for every fixed `Theta>1/2` it is strictly weaker than the `c>1` point-sample requirement from `FD-057`.

This distinction matters because the strongest modern Möbius almost-all statements are naturally formulated with maximal truncation. The adaptive Farey endpoint does not need to avoid the bad set itself; it only needs to be **coverable by one nearby good ambient window**.

## 3. Adversarial checks and exact boundary

There is no contradiction with `FD-057`. Its theorem is explicitly a cardinality statement for a common exceptional set of the represented starts themselves. Under that oracle, the sample really has only `X/R_X` points and `c>1` is sharp at the exponent level. `FD-058` changes the admissible use of the analytic input: maximality supplies a real interval of ambient starts of length `asymp R_X` for each fixed represented interval.

The containment is one-sided and exact. If real `y\in[X-H_X,x_q]`, then `y<=x_q<X<=y+H_X`, so `(x_q,X]` is a consecutive arithmetic progression inside the ambient interval. This is precisely allowed by the `*`-norm definition in the 2026 theorem; no interpolation, discretization, or persistence-of-badness assumption is used.

The convolution transfer does not silently union polynomially many exceptional sets. The large-`d` tail is handled trivially, so only `D=(log X)^C` scaled Möbius problems are needed. Their exceptional sets are pulled back under real scaling, each paying exactly the Jacobian factor `d`; after cancellation with the scale `X/d` in the theorem, every `B_d` costs `O(X/(log X)^{K'})` in Lebesgue measure. The simultaneous union therefore costs only the polylogarithmic factor `D`, absorbable because the literature theorem allows an arbitrary fixed logarithmic exponent.

The fixed condition `Theta<1` is used only to keep `H_X=X^(Theta+o(1))` within a genuine short-interval range with one fixed margin. The near-critical regime `1/2<Theta<=0.55` targeted by `FD-055`--`FD-057` satisfies this automatically. The finding does not claim a power-saving exceptional estimate that is not presently known, nor does it prove positive nonsquarefree occupation.

## 4. Prior-art boundary and consequence for the live route

The load-bearing external result remains Theorem 1.1(i) of Kaisa Matomäki, Maksym Radziwiłł, Xuancheng Shao, Terence Tao and Joni Teräväinen, *Higher uniformity of arithmetic functions in short intervals II. Almost all intervals*, Inventiones Mathematicae **244** (2026), 967--1091, DOI `10.1007/s00222-026-01408-6`, already anchored in `SOURCES.md`. Its maximal arithmetic-progression norm, interval range, and logarithmic exceptional-measure estimate are used exactly as published. No novelty is claimed for Dirichlet convolution, divisor splitting, real-variable pullback, or maximal truncation themselves.

A targeted prior-art search around maximal Möbius short intervals, the Dirichlet series `zeta(s+1)/zeta(s)`, Farey discrepancy, and reciprocal/floor-selected starts did not locate the present ambient-window localization argument or its application to this adaptive Jordan transfer. No new external theorem is load-bearing, so `SOURCES.md` remains unchanged.

The durable strategic correction is therefore narrow but important. The live target after `FD-057` is **not necessarily** a theorem that sees the sparse reciprocal-floor sample directly, nor is `c>1` unavoidable. For maximal short-interval input, one can localize through containing ambient windows and return to the corridor exponent

\[
\boxed{
\frac{1-\Theta}{\Theta}.
}
\]

The current 2026 logarithmic exceptional bound is still far too large, so the zero-frontier occupation problem remains open. But future work should distinguish two genuinely different localization regimes: pointwise-start theorems pay the inverse-length `c>1` penalty; maximal ambient-window theorems pay only the corridor-scale threshold (6).