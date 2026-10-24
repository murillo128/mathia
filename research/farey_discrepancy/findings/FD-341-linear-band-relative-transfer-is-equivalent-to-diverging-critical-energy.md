# FD-341 — Linear-band relative transfer is equivalent to diverging critical energy

**Status:** LITERATURE+DERIVED + EXACT-FINITE-INEQUALITY + CONDITIONAL-EQUIVALENCE.

For the genuine Farey sequence, FD-339 makes divergence of `Q E_Q` necessary for vanishing relative rank/position coefficient error at its linear cutoff. That condition is also sufficient, simultaneously at every fixed linear cutoff. The missing input is a uniform truncation of the classical Mertens–sawtooth field: its bounded-quotient part has controlled fourth moment, while its complement has arbitrarily small amplitude compared with `Q` by unconditional Mertens cancellation.

This is an unconditional theorem **equating properties whose truth is not established here**. It neither proves nor disproves `Q E_Q -> infinity`, and supplies no new Franel upper bound. In particular, an absolute coefficient-error floor of order `Q^(-1/2)` is consistent with relative transfer if the total energy grows above `1/Q` by an unbounded factor.

## 1. Objects and the equivalence

Let `Q>=3`, and use the genuine Farey grid
\[
0=x_0<x_1<\cdots<x_N=1,\qquad
N=\sum_{b\le Q}\varphi(b),\qquad
D_k=x_k-k/N,
\]
\[
E_Q=\sum_{k=1}^{N-1}D_k^2,\qquad
V_Q=\sum_{k=1}^{N-1}D_k^4,\qquad K_Q=QE_Q.
\tag{1}
\]
Use exactly FD-337's coefficients:
\[
d_{2j}=\sqrt{2/N}\sum_{k=1}^{N-1}D_k\sin(2\pi jk/N),\qquad
a_j=-\frac{B_Q(j)}{\pi j\sqrt{2N}},
\]
\[
B_Q(j)=\sum_{b\mid j,\ b\le Q}bM(\lfloor Q/b\rfloor),
\qquad M(y)=\sum_{n\le y}\mu(n).
\tag{2}
\]
For an integer `1<=q<N/2`, set
\[
\mathcal R_Q(q)=\frac1{E_Q}\sum_{j=1}^q|d_{2j}-a_j|^2,
\qquad \mathcal U_Q=\frac{Q^2V_Q}{E_Q}.
\tag{3}
\]
Here `E_Q>0`. All cutoffs below lie below `N/2` for sufficiently large `Q`.

**Theorem.** Along any sequence of integer orders `Q -> infinity`, the following are equivalent:

1. `K_Q -> infinity`;
2. `mathcal U_Q -> 0`;
3. for every fixed `c>0`, `mathcal R_Q(floor(cQ)) -> 0`;
4. `mathcal R_Q(128Q-1) -> 0`.

The universal quantifier in (3) concerns each fixed `c`; no claim is made for an arbitrarily growing multiplier `c=c(Q)`. The equivalence also holds along subsequences, with all limits restricted to the same subsequence.

A quantitative input, valid for all sufficiently large `Q` and every integer `2<=R<=Q`, is
\[
\boxed{\mathcal U_Q\ll \frac{R}{K_Q}
                  +\frac1{\log^2(2R)}.}
\tag{4}
\]
The implied constant is independent of `Q,R` and depends only on a fixed classical bound `|M(y)| << y/log^2(2y)`. In particular, if `K_Q -> infinity`, choosing `R=floor(sqrt(K_Q))` eventually gives
\[
\mathcal U_Q\ll K_Q^{-1/2}+\log^{-2}K_Q,
\qquad
\mathcal R_Q(\lfloor cQ\rfloor)
\ll_c K_Q^{-1/2}+\log^{-2}K_Q.
\tag{5}
\]
The choice obeys `R<=Q`: Dress's bound gives `E_Q<=N/Q^2` and hence `K_Q<=N/Q=O(Q)`.

## 2. Exact counting field and fourth-moment identity

For `0<t<1`, let
\[
A_Q(t)=\#\{1\le k\le N:x_k\le t\},\qquad
H_Q(t)=A_Q(t)-Nt+\tfrac12.
\tag{6}
\]
Define `psi(u)={u}-1/2` and `S_L(t)=sum_(m=1)^L psi(mt)`, with `S_0=0`. Values at the finitely many discontinuities do not affect integrals or essential-supremum bounds. Möbius inversion gives
\[
\begin{aligned}
A_Q(t)&=\sum_{d\le Q}\mu(d)
                  \sum_{m\le Q/d}\lfloor mt\rfloor,\\
H_Q(t)&=-\sum_{d\le Q}\mu(d)S_{\lfloor Q/d\rfloor}(t)
       =-\sum_{m\le Q}M(\lfloor Q/m\rfloor)\psi(mt).
\end{aligned}
\tag{7}
\]
The centering follows from `sum_(d<=Q) mu(d) floor(Q/d)=1` and
`N=sum_(d<=Q) mu(d) L_d(L_d+1)/2`, `L_d=floor(Q/d)`.

The exact moment identities are
\[
\boxed{\int_0^1H_Q(t)^2dt=NE_Q+\frac1{12},}
\]
\[
\boxed{\int_0^1H_Q(t)^4dt=N^3V_Q+\frac N2 E_Q+\frac1{80}.}
\tag{8}
\]
To check the fourth-order normalization directly, on `[x_k,x_(k+1))` the field is `k+1/2-Nt`. Its values at the left and limiting right endpoints are `1/2-ND_k` and `-1/2-ND_(k+1)`. Integrating the fourth power and summing telescopes to
\[
\frac1{5N}\left\{
\sum_{k=1}^{N-1}
[(\tfrac12-ND_k)^5-(-\tfrac12-ND_k)^5]
+\frac1{16}\right\}.
\]
Expansion gives the second line of (8). The same calculation with cubes gives the first. Both identities actually hold for every strictly increasing grid with these endpoints; no probabilistic or Farey assumption is needed for this integration step. Equation (7), in contrast, is specific to the genuine Farey arithmetic.

## 3. A small uniform remainder and a controlled fourth moment

Fix `2<=R<=Q`. Split (7) as `H_Q=P_(Q,R)+W_(Q,R)`, where
\[
\begin{aligned}
P_{Q,R}(t)
&=-\sum_{k=1}^{R-1}M(k)
 [S_{\lfloor Q/k\rfloor}(t)-S_{\lfloor Q/(k+1)\rfloor}(t)]\\
&=-\sum_{k=1}^{R-1}\mu(k)S_{\lfloor Q/k\rfloor}(t)
  +M(R-1)S_{\lfloor Q/R\rfloor}(t),\\
W_{Q,R}(t)
&=-\sum_{m\le\lfloor Q/R\rfloor}
 M(\lfloor Q/m\rfloor)\psi(mt).
\end{aligned}
\tag{9}
\]
Thus `P` contains exactly the terms whose quotient `floor(Q/m)` is less than `R`; the cutoff remainder is retained, not discarded.

Put
\[
\beta_Q(R)=\frac1{2Q}
\sum_{m\le\lfloor Q/R\rfloor}|M(\lfloor Q/m\rfloor)|.
\tag{10}
\]
Then `||W_(Q,R)||_infinity<=Q beta_Q(R)`. The unconditional estimate
\[
|M(y)|\ll \frac{y}{\log^2(2y)}
\tag{11}
\]
implies, uniformly for `Q>=R>=2`,
\[
\boxed{\beta_Q(R)\ll\frac1{\log(2R)}.}
\tag{12}
\]
For a direct proof, partition the indices in (10) by
`2^j R <= Q/m < 2^(j+1)R`. There are at most `Q/(2^jR)` such indices. On each piece (11), extended to real arguments, bounds the numerator summand by a constant times `2^(j+1)R/log^2(2^(j+1)R)`. Dividing by `2Q` and summing gives
\[
\beta_Q(R)\ll\sum_{j\ge0}
      \frac1{\log^2(2^{j+1}R)}\ll\frac1{\log(2R)}.
\]
This avoids an invalid termwise replacement of a difference of floors by its main term. Merely using `M(y)=o(y)` would not justify the summability here.

Next, the classical sawtooth correlation, obtained by multiplying its `L^2` Fourier series, is
\[
\int_0^1\psi(at)\psi(bt)dt=\frac{\gcd(a,b)^2}{12ab}.
\tag{13}
\]
Consequently
\[
\begin{aligned}
\|S_L\|_2^2
&=\frac1{12}\sum_{a,b\le L}\frac{\gcd(a,b)^2}{ab}\\
&\le\frac L6\sum_{b\ge1}\frac{\mathsf H_b}{b^2}\le L,
\qquad \mathsf H_b=\sum_{a=1}^b\frac1a.
\end{aligned}
\tag{14}
\]
Indeed, write `(a,b)=d(u,v)` with coprime `(u,v)` and bound the number of possible `d` by `L/max(u,v)`, then drop coprimality. For the final loose bound, `mathsf H_b<=2 sqrt(b)` and `sum b^(-3/2)<=3` suffice. Since `||S_L||_infinity<=L/2`, this proves
\[
\|S_L\|_4\le L^{3/4}.
\tag{15}
\]
Minkowski applied to the second line of (9), together with `|mu|<=1`, `|M(R-1)|<=R` and `sum_(k<R) k^(-3/4)<=4R^(1/4)`, gives
\[
\|P_{Q,R}\|_4\le 5R^{1/4}Q^{3/4},\qquad
\boxed{\int_0^1|P_{Q,R}|^4\le625RQ^3.}
\tag{16}
\]
All constants here are deliberately loose. No cancellation among the finitely many terms of `P` is asserted.

## 4. Finite moment bound and completion of the equivalence

If `|H_Q|<=2Q beta_Q(R)`, then
`|H_Q|^4<=4Q^2 beta_Q(R)^2 |H_Q|^2`. Otherwise `|P_(Q,R)|>=|H_Q|/2`. Thus pointwise, almost everywhere,
\[
|H_Q|^4\le16|P_{Q,R}|^4
                +4Q^2\beta_Q(R)^2|H_Q|^2.
\tag{17}
\]
Combining (8), (16), and (17), and dropping the positive lower-degree terms in the fourth-moment identity, proves the fully finite inequality
\[
\boxed{
\mathcal U_Q\le
\frac{10000 RQ^5}{N^3E_Q}
+\frac{4\beta_Q(R)^2Q^4}{N^2}
 \left(1+\frac1{12NE_Q}\right).}
\tag{18}
\]
The totient asymptotic gives `N~3Q^2/pi^2`. Also, with `h=floor(N/(2Q))`, the first positive point `1/Q` yields
\[
D_k\ge\frac1{2Q}\quad(1\le k\le h),\qquad
E_Q\ge\frac h{4Q^2},\qquad V_Q\ge\frac h{16Q^4}.
\tag{19}
\]
In particular `NE_Q >> Q`. Equations (12), (18), and (19) give (4). If `K_Q -> infinity`, first fixing `R` and then letting `R -> infinity` proves `mathcal U_Q ->0`; alternatively use the admissible choice in (5). Conversely (19) implies
\[
\mathcal U_Q\ge\frac{h}{16Q^2E_Q}\gg\frac1{K_Q},
\tag{20}
\]
so (2) of the theorem implies (1).

FD-337's exact deterministic bound retains the fourth moment before applying the supremum estimate:
\[
\left(\sum_{j\le q}|d_{2j}-a_j|^2\right)^{1/2}
\le\frac{8\pi}{3}q\sqrt{V_Q}.
\tag{21}
\]
It follows that
\[
\mathcal R_Q(\lfloor cQ\rfloor)
\le(8\pi c/3)^2\mathcal U_Q.
\tag{22}
\]
This proves (2) implies (3), and (3) implies (4) by monotonicity in the cutoff. Finally FD-339 proves, for the genuine sequence,
\[
\liminf_{Q\to\infty}Q
 \sum_{j\le128Q-1}|d_{2j}-a_j|^2
\ge\frac{3}{2048\pi^2}>0.
\tag{23}
\]
If the relative error at that cutoff tends to zero, (23) forces `K_Q -> infinity`. This completes all four implications. It does not require a conjectural energy asymptotic.

## 5. Consequences and limits

Under any of the equivalent conditions, the normalized **band energies** also transfer at every fixed linear cutoff. In the notation
\[
E_q=\sum_{j\le q}d_{2j}^2,\qquad T_q=\sum_{j\le q}a_j^2,
\qquad T_\infty=E_Q+\frac1{12N},
\]
FD-002's total-energy identity and the triangle inequality give
\[
\left|\frac{E_q}{E_Q}-\frac{T_q}{T_\infty}\right|
\le 2\sqrt{\mathcal R_Q(q)}+\mathcal R_Q(q)
                      +\frac1{12NE_Q}\longrightarrow0
\quad(q=\lfloor cQ\rfloor).
\tag{24}
\]
The converse is **not** asserted for energy shares: vectors can remain separated while their norms agree. Likewise, (23) proves necessity at the specified cutoff and for the all-fixed-cutoff property, not at every smaller individual positive cutoff.

The arithmetic in (7) is essential. The rational controls of FD-338 need not admit the Mertens truncation (9)–(12), so this theorem is not a general statement about reflected grids with Dress-size displacement. Conversely, no new arithmetic carrier has been introduced: the proof works inside the existing Farey counting field and its classical divisor transform.

The new implication is **sufficiency** of diverging critical energy for linear-band coefficient transfer, together with the exact fourth-moment characterization. It changes the earlier one-way boundary into an equivalence. Neither the divergence condition nor its negation is established, and RH's usual `E_Q=O_epsilon(Q^(-1+epsilon))` does not decide between them. Bounded `K_Q` along a subsequence retains the coefficient obstruction there; unbounded `limsup K_Q` alone does not imply transfer along all orders. The larger-order spectral confirmation panel in the local gap-ordering clue remains untouched. No endpoint subtraction, new null ensemble, or claimed improvement of the RH-critical exponent is involved.

## 6. Audit and prior-art boundary

An independent implementation using exact rational arithmetic enumerated genuine grids for all `3<=Q<=40`. Direct gap integration verified both identities (8) at all 38 orders. Another 48 exact moment checks used the 24 non-reflected rational grids `x_k=(k/N)^p`, `2<=N<=13`, `p in {2,3}`, checking that reflection is unnecessary for (8). For the distinct choices `R` in `{2,3,min(Q,5),min(Q,8),Q}`, the Farey audit checked the exact decomposition and remainder bound at 34,784 gap midpoints, and 540 integrated/finite inequalities covering (16)–(18). Separately, exact integration over every discontinuity interval of `S_L`, for `1<=L<=50`, verified 100 second/fourth-moment statements, including equality with the GCD sum (14) and the bound (15). These checks validate finite constants, signs, quotient boundaries, and centering; the proof of the asymptotic equivalence is the analytic argument above, not extrapolation. No independent adversarial approval or Lean validation is claimed.

The only additional analytic input beyond FD-337/339 is the classical unconditional estimate (11). H. Davenport, *On Some Infinite Series Involving Arithmetical Functions (II)*, Quarterly Journal of Mathematics **os-8** (1937), 313–320, [DOI](https://doi.org/10.1093/qmath/os-8.1.313), is already anchored in SOURCES.md. The needed log-power estimate is also explicitly stated as equation (1.2) in Xiaoguang He and Bingrong Huang, *Exponential sums involving the Möbius function*, Acta Arithmetica **175**(3) (2016), 201–210, [DOI](https://doi.org/10.4064/aa8130-5-2016), [publisher PDF](https://www.impan.pl/shop/intranet.php?h=6534c91a557d4&p=91740&t=1697958170). Only its zero-frequency case with log exponent two is used; none of that paper's conditional exponential-sum results enters.

Möbius inversion, the sawtooth GCD integral, norm interpolation, and the ordered-grid moment calculation are classical mechanisms. P. Codecà and A. Perelli, *On the uniform distribution (mod 1) of the Farey fractions and l^p spaces*, Math. Ann. **279** (1988), 413–422, [institutional abstract](https://iris.unife.it/handle/11392/522882), and M. N. Huxley, *Identities involving Farey fractions*, Proc. Steklov Inst. Math. **276** (2012), 125–139, [primary record](https://www.mathnet.ru/eng/tm3374), are neighboring harmonic/discrete-continuous prior art. The former's abstract concerns integration errors for absolutely continuous test functions; it was not used to infer the present relative fourth-moment or cutoff theorem. Searches also compared empirical/quantile remainder theory, which supplies no deterministic sampling hypothesis for this Farey array. No priority claim is made from the absence of an identical formulation. The durable contribution is the explicit local equivalence and its finite inequality (18), rather than a new general Mertens, Fourier, or empirical-process theorem.
