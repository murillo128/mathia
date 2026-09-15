# NB-134 — fixed multibase visibility still permits simultaneous superpolynomial annihilator collapse

**Status:** `EXACT-DERIVED + MATCHED-CONTROL + NB-127/NB-133-SPLICE + FIXED-MULTIBASE + POLYNOMIAL-HEIGHT + SIMULTANEOUS-RECURRENCE-VISIBILITY + VINOGRADOV-KOROBOV-COMPATIBLE + SUPERPOLYNOMIAL-MARGIN-COLLAPSE + ROUTE-NARROWING + REPRESENTATION-AUDIT`.

`NB-133` leaves several possible repairs for the visible-annihilator route, including coupling several multiplicatively independent geometric bases. `NB-127` had already shown that any fixed finite base family has arbitrarily high simultaneous near-aliases, but that result was global: the return heights were not yet spliced into the polynomial-height, logarithmic-rank regime where `NB-132` makes actual-zero recurrences visible and where `NB-133` matches the current zero-count and Vinogradov--Korobov envelopes.

That splice can be done exactly. For every fixed finite set of integer bases, there is an unbounded sequence of polynomial-height formal packets whose recurrence is visible **at every base simultaneously**, whose rank remains below the same shrinking-window numerical zero-count allowance used in `NB-133`, and whose real parts lie safely on the permitted side of the same Vinogradov--Korobov zero-free boundary. Nevertheless, the normalized `NB-124` annihilator margin is smaller than every power of the cutoff at **every base simultaneously**.

The mechanism is simple but consequential. Simultaneous Diophantine recurrence makes the center ordinate nearly aliased at all fixed bases with a polynomially small phase defect. The horizontal Vinogradov--Korobov depth is only polylogarithmically small, so it dominates that phase defect. A logarithmic number of roots can therefore sit within `O(eta_R)` of the missing harmonic root in every fixed base representation at once, and each scalar annihilator multiplies the same `Theta(log R)` small rootwise distances.

Thus **replacing one visible scalar annihilator by finitely many fixed visible scalar annihilators, or by standard finite aggregations of their margins, does not restore polynomial coercivity in the `NB-132` regime.** What remains open is genuinely joint information not reducible to those scalar margins, a number of bases growing with the cutoff, stronger actual-zero arrangement laws, or a different target-bearing functional.

## 1. Fixed multibase recurrence can recur at polynomial accuracy relative to its own height

Fix a finite nonempty set of integer bases

\[
\mathcal Q=\{q_1,\ldots,q_m\},
\qquad q_j\ge2,
\tag{1}
\]

and put

\[
q_*:=\max\mathcal Q.
\tag{2}
\]

`NB-127` proves by the elementary simultaneous Dirichlet pigeonhole argument that there is an unbounded sequence of ordinates `G_n` such that

\[
\varepsilon_n
:=
\max_{q\in\mathcal Q}|e^{iG_n\log q}-1|
\longrightarrow0.
\tag{3}
\]

More is available. If the bases have a nonzero exact common alias period, take integer multiples of it and then

\[
\varepsilon_n=0.
\tag{4}
\]

Otherwise, when `m>=2`, the same construction gives an unbounded sequence with

\[
\boxed{
\varepsilon_n\ll_{\mathcal Q}G_n^{-1/(m-1)}.
}
\tag{5}
\]

For `m=1`, exact aliasing again gives `(4)`.

Fix now `A>0`. Reparameterize the sequence by integers `R_n` satisfying

\[
R_n=(2G_n)^{1/A}+O(1).
\tag{6}
\]

Then

\[
\boxed{
G_n=\left(\frac12+o(1)\right)R_n^A.
}
\tag{7}
\]

In the nonexact case `(5)` becomes

\[
\boxed{
\varepsilon_n
\ll_{\mathcal Q,A}
R_n^{-A/(m-1)}.
}
\tag{8}
\]

This reparameterization is important. No return time near a preassigned height is being assumed. We first take the actual simultaneous return height supplied by `NB-127` and then define the cutoff from that height. The resulting packet is therefore genuinely at polynomial height relative to its own cutoff.

For readability write `R=R_n`, `G=G_n` and `epsilon_R=epsilon_n` along this subsequence.

## 2. Choose logarithmic rank inside every visible recurrence budget

Assume we are in a nonempty `NB-132`-type fixed-width visibility regime for the largest base: choose some fixed `W>0` such that

\[
A\left(\frac{W}{4\pi}+0.10076\right)
<
\frac1{\log q_*}.
\tag{9}
\]

Choose once and for all

\[
\boxed{
0<c<\min\left\{0.10076A,\frac1{\log q_*}\right\}.
}
\tag{10}
\]

Set

\[
d_R:=\lfloor c\log R\rfloor.
\tag{11}
\]

Since every `q in mathcal Q` satisfies `q<=q_*`, `(10)` gives

\[
\boxed{
d_R+1\le\log_q R
\qquad(q\in\mathcal Q)
}
\tag{12}
\]

for all sufficiently large `R`. Thus an order-`d_R` recurrence is fully visible inside the natural cutoff at **every** base in the fixed family.

Use the same explicit Vinogradov--Korobov scale as `NB-125`--`NB-133`, with `K_VK=53.989`:

\[
\eta_R
:=
\frac{2}
{K_{\rm VK}
(\log G)^{2/3}
(\log\log G)^{1/3}},
\qquad
\beta_R:=1-\eta_R.
\tag{13}
\]

Let

\[
\delta_R
:=
\frac{\eta_R}{d_R\log q_*}
\tag{14}
\]

and define `d_R` distinct simple formal right-half points

\[
\rho_{j,R}
:=
\beta_R+i(G+j\delta_R),
\qquad
0\le j<d_R.
\tag{15}
\]

Their total vertical diameter satisfies

\[
(d_R-1)\delta_R
<
\frac{\eta_R}{\log q_*}
=o(1),
\tag{16}
\]

so for every fixed `W>0` they eventually lie in a width-`W` band below height `R^A`, by `(7)`.

The same adversarial shrinking-window zero-count audit used in `NB-133` applies here. Over a window of width `O(eta_R)=o(1)` at height `G asymp R^A`, the main term in `N(T+H)-N(T)` is `o(log R)`, while the two Bellotti--Wong--Fiori endpoint errors permit at most

\[
(0.20152A+o(1))\log R
\tag{17}
\]

total zeros counted with multiplicity. Functional-equation symmetry leaves a right-half numerical allowance

\[
(0.10076A+o(1))\log R.
\tag{18}
\]

Because of `(10)`, the formal rank `d_R=c log R+O(1)` lies strictly below that allowance. This does not assert that the points `(15)` are zeta zeros; it shows that the same coarse local count used to justify the source-faithful rank scale does not reject the packet.

Likewise the horizontal location is compatible with Bellotti's zero-free law. Since `|Im rho_(j,R)|=G+o(1)`, the forbidden Vinogradov--Korobov depth is asymptotically `eta_R/2`, whereas

\[
1-\beta_R=\eta_R.
\tag{19}
\]

The packet therefore lies a fixed factor to the left of the excluded boundary, exactly as in `NB-133`.

## 3. Every base sees the same cluster near its missing harmonic root

For each `q in mathcal Q`, put

\[
r_q:=q^{-1},
\qquad
\lambda_{j,q}
:=q^{-\overline{\rho_{j,R}}}.
\tag{20}
\]

Then

\[
\lambda_{j,q}
=q^{-\beta_R}
 e^{iG\log q}
 e^{ij\delta_R\log q}.
\tag{21}
\]

Normalize the distance to the missing root by `|lambda_(j,q)|`. Since

\[
\frac{r_q}{|\lambda_{j,q}|}=q^{-\eta_R},
\]

we obtain

\[
\begin{aligned}
\frac{|r_q-\lambda_{j,q}|}{|\lambda_{j,q}|}
&=
\left|
q^{-\eta_R}
-e^{iG\log q}e^{ij\delta_R\log q}
\right|\\
&\le
|1-q^{-\eta_R}|
+|1-e^{iG\log q}|
+|1-e^{ij\delta_R\log q}|.
\end{aligned}
\tag{22}
\]

Uniformly for `q in mathcal Q` and `0<=j<d_R`,

\[
|1-q^{-\eta_R}|
\le
(\log q_*+o(1))\eta_R,
\tag{23}
\]

and by `(14)`,

\[
|1-e^{ij\delta_R\log q}|
\le
j\delta_R\log q
<\eta_R.
\tag{24}
\]

Finally `(8)` gives

\[
\varepsilon_R
=o(\eta_R)
\tag{25}
\]

in the nonexact case, because every negative power of `R` is smaller than the polylogarithmic scale `(13)`; `(25)` is trivial under exact aliasing.

Therefore there is a constant `C_mathcalQ>0`, independent of `R`, such that

\[
\boxed{
|r_q-\lambda_{j,q}|
\le
C_{\mathcal Q}\eta_R|\lambda_{j,q}|
\quad
(q\in\mathcal Q,\ 0\le j<d_R).
}
\tag{26}
\]

This is the multibase version of the phase cluster in `NB-133`. The simultaneous near-alias defect is actually smaller than the allowed radial depth, so adding finitely many fixed bases does not force any one of the scalar representations away from its missing root.

## 4. All visible scalar annihilator margins collapse superpolynomially at once

At each base define

\[
A_{R,q}(z)
:=
\prod_{j=0}^{d_R-1}(z-\lambda_{j,q})
=
\sum_{k=0}^{d_R}a_{k,q}z^k
\tag{27}
\]

and its normalized `NB-124` margin

\[
\mathfrak s_{R,q}
:=(1-r_q)
\frac{|A_{R,q}(r_q)|^2}
{\sum_{k=0}^{d_R}|a_{k,q}|^2r_q^k}.
\tag{28}
\]

Equation `(26)` gives

\[
|A_{R,q}(r_q)|
\le
(C_{\mathcal Q}\eta_R)^{d_R}
\prod_{j=0}^{d_R-1}|\lambda_{j,q}|.
\tag{29}
\]

The constant coefficient supplies the denominator lower bound

\[
\sum_{k=0}^{d_R}|a_{k,q}|^2r_q^k
\ge
|a_{0,q}|^2
=
\prod_{j=0}^{d_R-1}|\lambda_{j,q}|^2.
\tag{30}
\]

Hence, simultaneously for every fixed base,

\[
\boxed{
\mathfrak s_{R,q}
\le
(1-r_q)(C_{\mathcal Q}\eta_R)^{2d_R}.
}
\tag{31}
\]

Since `G asymp R^A`,

\[
\log\eta_R
=
-\frac23\log\log R
-\frac13\log\log\log R
+O_{A,\mathcal Q}(1),
\tag{32}
\]

and `d_R=c log R+O(1)`. Therefore

\[
\boxed{
\max_{q\in\mathcal Q}\log\mathfrak s_{R,q}
\le
-\left(\frac{4c}{3}+o(1)\right)
\log R\log\log R,
}
\tag{33}
\]

or equivalently

\[
\boxed{
\max_{q\in\mathcal Q}\mathfrak s_{R,q}
\le
R^{-(4c/3+o(1))\log\log R}
=o(R^{-M})
}
\tag{34}
\]

for every fixed `M>0`.

Together `(12)` and `(34)` are the key point: **every recurrence is visible, but every standard scalar missing-root certificate is simultaneously worse than every polynomial scale.** Consequently the same is true for the finite sum, maximum, every fixed `ell^p` norm, every finite product, and every fixed algebraic power combination of the margins.

For scale comparison, the formal packet's elementary Burnol target mass does not have this superpolynomial size. Each point has

\[
\delta_{j,R}
=
\frac{2\beta_R-1}
{\beta_R^2+(G+j\delta_R)^2}
\asymp R^{-2A}.
\tag{35}
\]

Since `d_R asymp log R` and `d_R delta_(j,R)=o(1)`, the finite Blaschke product identity gives

\[
\boxed{
1-|B_{F_R}(1)|^2
\asymp
\frac{\log R}{R^{2A}}.
}
\tag{36}
\]

Thus the simultaneous scalar annihilator margins can be superpolynomially smaller than the packet's own polynomial absolute-height target mass. The failure is conditioning of this certificate family, not absence of a polynomial absolute-height scale in the matched packet.

## 5. What fixed multibase sampling no longer buys

`NB-127` showed that finitely many bases are globally noncoercive because their labelled phase data have arbitrarily high near-returns. `NB-132` then restored recurrence visibility for genuine narrow packets at polynomial height, and `NB-133` showed that one visible base can still be superpolynomially ill-conditioned because radial depth and phase arrangement are separate resources.

The present construction shows that those two obstructions coexist in the same polynomial-height scaling regime. A simultaneous near-return can be chosen first, the cutoff can be tied to its actual height by `(6)`, and the `NB-133` phase cluster can then be placed around that center. No fixed base in `mathcal Q` is rescued: the common phase defect is polynomially smaller than the permitted horizontal depth, while the logarithmic rank remains visible at all bases.

This rules out a specific and natural repair of `NB-133`: **taking finitely many fixed `NB-124` annihilators and hoping that at least one has a polynomial missing-root margin.** It also rules out standard finite scalar aggregations of those margins.

The boundary matters. The finding does **not** rule out a genuinely joint cross-base functional that uses labelled relations between the same root across bases before forming a product, a singular rescaling calibrated to the simultaneous phase mismatch, or a number of bases that grows with `R`. It does not rule out an actual-zeta theorem showing that the simultaneous matched packet cannot occur because of a source law stronger than the current zero-count and zero-free envelopes. And, as in `NB-133`, small annihilator margins do not by themselves prove near-perfect Nyman target capture; `NB-124` supplies a one-sided certificate.

The live distinction is therefore sharper than “one base versus several bases.” The issue is whether the representation imports a **growing or genuinely joint arrangement resource** whose conditioning survives `Theta(log R)` roots approaching the harmonic target at Vinogradov--Korobov depth.

## 6. Adversarial and prior-art audit

Several possible loopholes were checked before canonicalization.

First, the simultaneous return heights are not assumed to occur near a preselected polynomial scale. Equation `(6)` defines the cutoff from the actual return height, so `(7)` is exact asymptotic bookkeeping rather than an unproved equidistribution statement. Second, a family with an exact common period only strengthens the construction; multiplicative independence is the harder near-alias case. Third, the recurrence budget is checked against `q_*`, so `(12)` really holds for every base rather than only for the anchor base used in the Diophantine argument.

Fourth, the phase error from simultaneous recurrence is `o(eta_R)`, not merely `o(1)`. This is what allows the radial Vinogradov--Korobov scale to dominate uniformly in `(26)`. Fifth, the shrinking-window zero-count audit is repeated at the packet's actual `o(1)` diameter and uses `c<0.10076A`, so the matched control does not regain the fixed-width loophole already closed in `NB-133`. Sixth, all points are simple; no multiplicity is used. Functional-equation and conjugation partners may be adjoined if desired without changing the right-half positive-frequency packets entering `(27)`.

The simultaneous approximation input is classical Dirichlet/Kronecker recurrence, but the exact quantitative form needed here was already proved internally in `NB-127` by a pigeonhole argument, so no external approximation theorem is load-bearing. A targeted literature search found the expected neighboring themes: multiscale Nyman--Beurling ladders, including the `2^{-j}3^{-k}` Gram geometry studied by Hugh Carvill (arXiv:2510.18132), and the classical theory of simultaneous Diophantine approximation. No source located in that audit supplies the present splice between fixed multibase near-recurrence, `NB-132` polynomial-height recurrence visibility, Vinogradov--Korobov-compatible radial depth, and simultaneous collapse of every `NB-124` scalar margin. No new external theorem is required, so `SOURCES.md` needs no new anchor.

## Consequence

The conditioning frontier after `NB-133` narrows again. **A fixed finite collection of geometric bases is not enough if the proof ultimately reduces each base to its ordinary annihilator margin.** Even in the narrow polynomial-height regime where actual-zero counting makes every recurrence visible, the coarse source laws still permit a logarithmic matched packet for which all those margins collapse superpolynomially at once.

A viable next bridge must therefore obtain information that this construction does not preserve: a genuinely joint cross-base separator with a proved quantitative modulus, a base family whose complexity grows with the cutoff, an actual-zero anti-recurrence/anti-clustering theorem at the required shrinking scale, or a target-bearing certificate whose normalization does not multiply one small rootwise distance per visible zero state.