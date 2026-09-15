# MC-309 — Landau–Page forces half-occupancy in every low-cost moderate source cut

**Status:** `EXACT-DERIVED` · `LITERATURE+DERIVED` · `FRONTIER-REFINEMENT` · `NEGATIVE/OBSTRUCTION` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

Continue the exact one-defect Legendre-shell endpoint of `MC-307`–`MC-308` and the low-source-cost Landau–Page theorem of `MC-293`.

Fix linearly independent shell functionals

\[
\lambda_1,\ldots,\lambda_k
\]

with fixed lower-prime representatives `V_i`, put

\[
U=\bigcup_{i=1}^k V_i,
\qquad
a_p=(\mathbf 1_{p\in V_1},\ldots,\mathbf 1_{p\in V_k})\in\mathbf F_2^k,
\]

and for a source cut `J\subseteq U` retain the notation of `MC-308`

\[
P_J=\prod_{p\in J}p,
\qquad
B_J=\operatorname{span}\{a_p:p\in U\setminus J\},
\]

\[
W_J=\mathbf F_2^k/B_J,
\qquad
t_J=\dim W_J,
\]

and

\[
h_J=\left|\{0,q_J(e_1),\ldots,q_J(e_k)\}\right|.
\tag{1}
\]

Let

\[
\mathcal R_y
=\{r:y<r\le2y,\ r\text{ prime},\ r\equiv1\pmod4\},
\qquad N=|\mathcal R_y|.
\]

Write the selected endpoint sign bits as `s(r)\in\mathbf F_2^k`, with the convention of `MC-308`, so the exact one-defect condition gives

\[
s(r)\in E
:=\{\mathbf1,\mathbf1+e_1,\ldots,\mathbf1+e_k\}.
\tag{2}
\]

Push the empirical shell measure through the source-cut quotient:

\[
\nu_J(v)
:=\frac1N
\#\{r\in\mathcal R_y:q_J(s(r))=v\},
\qquad v\in W_J.
\tag{3}
\]

Then

\[
|\operatorname{supp}\nu_J|\le h_J.
\tag{4}
\]

The dual group of `W_J` is canonically

\[
W_J^*=B_J^\perp
\subseteq (\mathbf F_2^k)^*.
\]

For `x=(x_1,\ldots,x_k)\in B_J^\perp`, define

\[
\lambda_x:=\sum_{i=1}^k x_i\lambda_i.
\tag{5}
\]

Its normalized shell bias is exactly the Walsh coefficient of `\nu_J`:

\[
\boxed{
\widehat\nu_J(x)
=\sum_{v\in W_J}\nu_J(v)(-1)^{\langle x,v\rangle}
=\frac1N\sum_{r\in\mathcal R_y}(-1)^{\lambda_x(s(r))}.
}
\tag{6}
\]

Moreover every `x\in B_J^\perp` has a lower-prime representative supported entirely in `J`. Hence

\[
\boxed{
\mathcal Q(\lambda_x)\le P_J,
}
\tag{7}
\]

where `\mathcal Q` is the minimum source cost of `MC-293`.

Let

\[
D_y=\exp\!\left(\kappa\frac{\log y}{\log\log y}\right)
\tag{8}
\]

be the Landau–Page source threshold from `MC-293`, with its fixed sufficiently small absolute `\kappa>0`. Define

\[
\varepsilon_y
:=
\sup_{\substack{\lambda\ne0,\ \mathcal Q(\lambda)\le D_y\\
\lambda\ne\lambda_*(y)}}
\left|
\frac1N\sum_{r\in\mathcal R_y}(-1)^{\lambda(s(r))}
\right|,
\tag{9}
\]

where `\lambda_*(y)` is the possible unique Landau–Page exceptional shell functional and is omitted when no such mode exists. `MC-293` gives

\[
\varepsilon_y\ll(\log y)^{-2}.
\tag{10}
\]

Assume now

\[
P_J\le D_y.
\tag{11}
\]

Put `n_J=2^{t_J}`. Parseval plus Cauchy–Schwarz gives the exact occupancy inequalities

\[
\boxed{
\frac{n_J}{h_J}
\le
1+(n_J-1)\varepsilon_y^2
}
\tag{12}
\]

if the exceptional mode is absent from `B_J^\perp`, and in general

\[
\boxed{
\frac{n_J}{h_J}
\le
2+(n_J-2)\varepsilon_y^2.
}
\tag{13}
\]

Consequently, whenever

\[
2^{t_J}\varepsilon_y=o(1),
\tag{14}
\]

one has for all sufficiently large `y`

\[
\boxed{
 h_J=2^{t_J}
}
\tag{15}
\]

if the exceptional mode is absent, while unconditionally

\[
\boxed{
 h_J\ge2^{t_J-1}.
}
\tag{16}
\]

Since `\varepsilon_y\ll(\log y)^{-2}`, condition `(14)` certainly holds throughout

\[
2^{t_J}=o((\log y)^2).
\tag{17}
\]

In particular it holds in the critical-rank window modeled in `MC-306`, where `2^R\asymp\log y` and every source cut has `t_J\le R`.

This closes the **low-product, moderate-rank source-cut route** left open by `MC-308`. That finding obtains a positive polynomial source-cost exponent only when

\[
\frac{h_J}{2^{t_J}}<\frac12.
\tag{18}
\]

Equations `(11)`, `(14)`, and `(16)` show that `(18)` is impossible. A source cut capable of crossing the Brun–Titchmarsh half-occupancy threshold must therefore escape at least one of the following regimes:

- its prime product exceeds the Landau–Page scale `D_y`;
- its quotient dimension is so large that `2^{t_J}\varepsilon_y` is no longer small; or
- one supplies simultaneous character-cancellation information stronger than the present Landau–Page bound.

No estimate for `M(x)` and no zero-free region for `\zeta` follows.

## 1. Every quotient frequency is represented inside the retained source cut

For `x\in B_J^\perp`, the definition of `B_J` gives

\[
x\cdot a_p=0
\qquad(p\in U\setminus J).
\tag{19}
\]

For a shell prime `r`, the fixed representatives satisfy

\[
(-1)^{\lambda_i(s(r))}
=
\prod_{p\in V_i}\left(\frac pr\right).
\tag{20}
\]

Multiplying `(20)` over the indices with `x_i=1` yields

\[
(-1)^{\lambda_x(s(r))}
=
\prod_{p\in U}
\left(\frac pr\right)^{x\cdot a_p}
=
\prod_{p\in J}
\left(\frac pr\right)^{x\cdot a_p}.
\tag{21}
\]

Thus the square-free product of the source primes in `J` with `x\cdot a_p=1` is an ambient representative of `\lambda_x`. It divides `P_J`, proving `(7)`.

Because `\lambda_1,\ldots,\lambda_k` are linearly independent as shell functionals, every nonzero `x` gives a nonzero `\lambda_x`. Therefore, under `(11)`, every nontrivial quotient frequency is inside the low-source-cost family controlled by `MC-293`.

## 2. Quotient Fourier coefficients are the shell biases

The empirical measure `(3)` is a probability measure on the finite binary group `W_J`. For `x\in B_J^\perp`, the pairing with `q_J(s)` is well-defined because `x` annihilates `B_J`. Hence

\[
\widehat\nu_J(x)
=\frac1N\sum_{r\in\mathcal R_y}
(-1)^{\langle x,q_J(s(r))\rangle}
=\frac1N\sum_{r\in\mathcal R_y}
(-1)^{x\cdot s(r)}.
\tag{22}
\]

By `(5)`, `x\cdot s(r)=\lambda_x(s(r))`, proving `(6)`.

The exact endpoint support `(2)` implies

\[
\operatorname{supp}\nu_J
\subseteq q_J(E).
\tag{23}
\]

Translation by `q_J(\mathbf1)` does not change cardinality, and therefore

\[
|q_J(E)|
=
\left|\{0,q_J(e_1),\ldots,q_J(e_k)\}\right|
=h_J,
\tag{24}
\]

which proves `(4)`.

The useful point is that `MC-308`'s algebraic quotient-simplex occupancy now has an exact harmonic interpretation: **every surviving quotient frequency is a shell functional whose source can be paid entirely by the same cut `J`.**

## 3. Parseval converts low-conductor balance into a support lower bound

Write

\[
s_J:=|\operatorname{supp}\nu_J|.
\]

Since `\nu_J` is a probability measure, Cauchy–Schwarz gives

\[
\sum_{v\in W_J}\nu_J(v)^2\ge\frac1{s_J}\ge\frac1{h_J}.
\tag{25}
\]

With the unnormalized Walsh transform used in `(6)`, Parseval is

\[
\sum_{x\in W_J^*}|\widehat\nu_J(x)|^2
=2^{t_J}\sum_{v\in W_J}\nu_J(v)^2.
\tag{26}
\]

The trivial frequency contributes

\[
\widehat\nu_J(0)=1.
\tag{27}
\]

If the possible exceptional functional `\lambda_*(y)` does not belong to the quotient-frequency subspace `\{\lambda_x:x\in B_J^\perp\}`, every nonzero coefficient is at most `\varepsilon_y` in absolute value. Combining `(25)`–`(27)` gives `(12)`.

In general, `MC-293` permits at most one exceptional nonzero coefficient. Bounding that coefficient trivially by `1` and every other nonzero coefficient by `\varepsilon_y` gives `(13)`.

No zero-density or RH input has been added here. The arithmetic theorem is exactly `MC-293`; the passage from frequency balance to occupancy is finite Fourier Parseval and Cauchy–Schwarz.

## 4. Integrality turns the analytic estimates into exact occupancy thresholds

First suppose the exceptional mode is absent. Rearranging `(12)` gives

\[
h_J
\ge
\frac{n_J}{1+(n_J-1)\varepsilon_y^2}.
\tag{28}
\]

The deficit from full occupancy is bounded by

\[
0\le
n_J-
\frac{n_J}{1+(n_J-1)\varepsilon_y^2}
\le n_J^2\varepsilon_y^2.
\tag{29}
\]

Under `(14)`, the right side is `o(1)`. Since `h_J` is an integer at most `n_J`, equation `(15)` follows.

In the general case, `(13)` gives

\[
h_J
\ge
\frac{n_J}{2+(n_J-2)\varepsilon_y^2}.
\tag{30}
\]

For `t_J\ge1`, `n_J` is even, and

\[
0\le
\frac{n_J}{2}
-
\frac{n_J}{2+(n_J-2)\varepsilon_y^2}
\le
\frac{n_J^2\varepsilon_y^2}{4}
=o(1).
\tag{31}
\]

Thus the integer `h_J` must be at least `n_J/2`, proving `(16)`. The case `t_J=0` is trivial.

This is exactly the threshold relevant to `MC-308`: the possible single exceptional mode can leave at most a factor-two loss in the quotient occupancy, while a positive fixed Brun–Titchmarsh exponent needs **strictly more than** a factor-two compression.

## 5. The half-occupancy boundary is sharp for the available Fourier information

The factor `1/2` in `(16)` is not an artifact of the proof. Let `W` be any binary vector space of dimension `t\ge1`, choose a nonzero character `x_*\in W^*`, and let `\nu` be uniform on the index-two subgroup

\[
H=\ker x_*.
\]

Then

\[
|\operatorname{supp}\nu|=\frac{|W|}{2},
\]

while its Fourier transform is

\[
\widehat\nu(0)=1,
\qquad
\widehat\nu(x_*)=1,
\qquad
\widehat\nu(x)=0
\quad(x\ne0,x_*).
\tag{32}
\]

Thus **perfect cancellation of every nonexceptional frequency plus one uncontrolled exceptional mode is compatible with exact half-occupancy**. The finite Fourier information available from Landau–Page alone cannot force more.

This is only a harmonic matched control. It is not claimed that every such hyperplane measure can be realized by the Legendre incidence geometry of the endpoint problem. Its role is to show that any improvement beyond `(16)` must use arithmetic or incidence information not contained in the statement “all but one low-cost Fourier mode are small.”

## 6. Prior art and novelty boundary

The harmonic step is classical. Parseval, Cauchy–Schwarz, and support-versus-spectrum uncertainty on finite groups are standard Fourier-analysis mechanisms; the broader uncertainty-principle literature includes David L. Donoho and Philip B. Stark, *Uncertainty Principles and Signal Recovery*, SIAM Journal on Applied Mathematics **49** (1989), 906–931, DOI `10.1137/0149053`. No novelty is claimed for the inequality type or the half-support hyperplane extremizer.

The arithmetic input is exactly the already-audited Landau–Page/Siegel–Walfisz consequence stored in `MC-293`: below `D_y`, all but at most one shell functional have bias `O((\log y)^{-2})`. The source-cut quotient and the invariant `h_J/2^{t_J}` are exactly those of `MC-308`.

A targeted literature search on 15 September 2026 for finite-group uncertainty/support theorems combined with exceptional real Dirichlet characters, Siegel-zero/Landau–Page dichotomies, and sparse Legendre-pattern quotients found the classical ingredients separately but no source establishing this exact Mathia-specific composition. **No standalone novelty claim is made.** The durable delta is the exact implication from the already-persisted source-cut dictionary plus the Landau–Page one-exception theorem to the Brun–Titchmarsh half-occupancy barrier.

## Boundaries and falsification tests

- **The quasi-subpower product threshold is load-bearing.** Equation `(7)` only puts every quotient frequency under `MC-293` when `P_J\le D_y`. The theorem says nothing comparable for source cuts of polynomial product size.
- **Moderate quotient dimension is load-bearing for the exact integer threshold.** The quantitative inequalities `(12)`–`(13)` hold without `(14)`, but the exact conclusions `(15)`–`(16)` use `2^{t_J}\varepsilon_y=o(1)`.
- **The possible exceptional mode is not removed.** When it belongs to the quotient-frequency subspace, the present argument gives half-occupancy rather than full occupancy. The hyperplane control `(32)` shows this is sharp at the level of Fourier information used.
- **Algebraic and empirical occupancy are distinguished.** The empirical shell support may be smaller than the algebraic set `q_J(E)`, but `(25)` lower-bounds the empirical support first; since it is contained in `q_J(E)`, the same bound applies to `h_J`.
- **Representative dependence remains.** The incidence columns and `P_J` depend on the fixed lower-prime representatives exactly as in `MC-308`. The theorem is valid for each fixed choice and does not prove existence of a favorable or unfavorable minimum-representative cut.
- **No circular use of zeta nonvanishing occurs.** The only analytic zero information is the unconditional Landau–Page dichotomy already isolated in `MC-293`; no `1/\zeta(s)` continuation or RH-scale contour shift is used.
- **No Möbius estimate follows.** The result closes one low-cost source-cut mechanism inside the localized endpoint program; it does not itself control `M(x)`.

## Consequence for the research line

`MC-308` reduced the next source-side question to finding a cut with small product `P_J`, large quotient rank `t_J`, and quotient-simplex occupancy below half. `MC-309` shows that **the first and third requirements are incompatible throughout the Landau–Page source range at every moderate quotient dimension**. In the critical-rank window `2^R\asymp\log y`, this covers every possible quotient rank.

The incidence frontier therefore moves upward in arithmetic cost. A genuinely coercive next theorem must control cuts whose product already exceeds

\[
D_y=\exp\!\left(\kappa\frac{\log y}{\log\log y}\right),
\]

or replace individual low-conductor character balance by a simultaneous estimate strong enough to remain useful once the quotient has exponentially many frequencies. Reapplying another low-cost scalar or prime-by-prime sieve cannot cross the half-occupancy barrier established here.