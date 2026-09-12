# MC-253 — Heath-Brown gives bounded-order shell parity pseudorandomness, but it is rank-blind

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `MATCHED-CODING-CONTROL`, `FRONTIER-REFINEMENT`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

Continue the quadratic shell matrix from `MC-238` and `MC-252`. Put

\[
\mathcal P_y=\{p\le y:p\text{ odd prime}\},
\qquad
\mathcal R_y=\{r:y<r\le2y,\ r\text{ prime}\},
\]

and

\[
A_{p,r}=\frac{1-(\frac pr)}2\in\mathbb F_2.
\tag{1}
\]

`MC-252` showed that if the shell condition `r\in(y,2y]` is removed, arbitrary finite binary matrices can be realized by genuine Legendre symbols. The natural next question is therefore whether tight shell localization forces a usable non-generic constraint on `(1)`.

It does force one, unconditionally: every **fixed-order parity projection** of the shell columns is asymptotically balanced for almost all column subsets.

For a fixed integer `t>=1` and a `t`-element subset `T\subset\mathcal R_y`, define

\[
B_y(T)
:=
\sum_{p\in\mathcal P_y}
\prod_{r\in T}\left(\frac pr\right).
\tag{2}
\]

For every fixed `t` and every `\eta>0`, Heath-Brown's quadratic large-sieve theorem implies

\[
\boxed{
\sum_{\substack{T\subset\mathcal R_y\\|T|=t}}
|B_y(T)|^2
\ll_{t,\eta}
\frac{y^{t+1+\eta}}{\log y}.
}
\tag{3}
\]

Since

\[
k_y:=|\mathcal P_y|\sim\frac y{\log y},
\qquad
N_y:=|\mathcal R_y|\sim\frac y{\log y},
\tag{4}
\]

we obtain

\[
\boxed{
\frac1{\binom{N_y}{t}}
\sum_{|T|=t}
\left|\frac{B_y(T)}{k_y}\right|^2
\ll_{t,\eta}
y^{-1+\eta}(\log y)^{t+1}.
}
\tag{5}
\]

In particular, for every fixed `\varepsilon>0`,

\[
\frac{
\#\{T\in\binom{\mathcal R_y}{t}:|B_y(T)|\ge\varepsilon k_y\}
}{\binom{N_y}{t}}
\longrightarrow0.
\tag{6}
\]

For `t=1`, almost every shell column has Hamming weight `(1/2+o(1))k_y`. For `t=2`, almost every pair of shell columns has Hamming distance `(1/2+o(1))k_y`. More generally, almost every fixed-size XOR of columns is balanced across the lower-prime rows.

This is genuine information supplied by the tight shell that the separated-prime universality construction of `MC-252` does not preserve.

However, the same derivation exposes a decisive limitation: **bounded-order parity pseudorandomness does not force large `\mathbb F_2` rank.** There are explicit binary matrices with `N\asymp k`, rank only `\asymp\log k`, exactly balanced pairwise column differences, and fixed-order parity biases whose normalized mean square is `O_t(1/k)`. Thus even the strongest qualitative reading of `(5)` is compatible with a logarithmic-rank matched control.

Consequently the route

\[
\text{shell localization}
\Rightarrow
\text{bounded-order Legendre balance}
\Rightarrow
\text{high shell-code rank}
\]

fails at its final implication. To attack the full-generation gate left by `MC-246` and `MC-252`, one needs information whose order grows with `y`, a genuinely stronger structural restriction on the shell code, or direct signed cancellation of the exact rough Möbius coset. Pairwise near-orthogonality alone cannot do it.

No bound for `M(X)`, no improvement of the blind-rank lower bounds, and no proof of `H=G` is obtained here.

## 1. Heath-Brown controls every fixed shell parity order

Heath-Brown's quadratic large sieve states that for positive `M,N`, arbitrary complex coefficients `a_n`, and odd square-free outer moduli,

\[
\sum_{m\le M}^{*}
\left|
\sum_{n\le N}^{*}a_n\left(\frac nm\right)
\right|^2
\ll_{\delta}
(MN)^\delta(M+N)
\sum_{n\le N}^{*}|a_n|^2,
\tag{7}
\]

for every fixed `\delta>0`; the stars denote restriction to positive odd square-free integers. This is Theorem 1 of D. R. Heath-Brown, *A mean value estimate for real character sums*, Acta Arithmetica 72 (1995), 235--275, DOI `10.4064/aa-72-3-235-275`.

A recent formulation by Marc Munsch, Igor Shparlinski, Yu-Chen Sun and Yixiu Xiao, *A large sieve inequality for sums of Legendre symbols over short intervals*, arXiv:`2604.23661v3` (5 August 2026), records the corresponding arbitrary-weight initial-interval consequence as their equation (1.1):

\[
M_2(Q;\boldsymbol\alpha,0,h)
\le(hQ)^{o(1)}(Q+h)h.
\tag{8}
\]

For `(3)`, apply `(7)` with

\[
N=y,
\qquad
M=(2y)^t,
\qquad
a_n=\mathbf 1_{\{n\in\mathcal P_y\}}.
\tag{9}
\]

For every `T\in\binom{\mathcal R_y}{t}`, the integer

\[
m_T:=\prod_{r\in T}r
\tag{10}
\]

is odd, square-free, and at most `(2y)^t`. Moreover Jacobi-symbol multiplicativity gives

\[
\sum_{n\le y}^{*}a_n\left(\frac n{m_T}\right)
=
\sum_{p\in\mathcal P_y}
\prod_{r\in T}\left(\frac pr\right)
=B_y(T).
\tag{11}
\]

The left side of `(3)` is therefore a nonnegative sub-sum of the left side of `(7)`. Also

\[
\sum_{n\le y}^{*}|a_n|^2=k_y\asymp\frac y{\log y}.
\tag{12}
\]

For fixed `t`, `(M+N)\ll_t y^t`. Given the `\eta` in `(3)`, choose the fixed exponent in `(7)` small enough that `(MN)^\delta\ll_t y^\eta`. Equations `(7)`--`(12)` then give `(3)`.

Finally,

\[
\binom{N_y}{t}
\asymp_t
\left(\frac y{\log y}\right)^t,
\tag{13}
\]

so dividing `(3)` by `(13)` and by `k_y^2\asymp y^2/(\log y)^2` proves `(5)`. Markov's inequality gives `(6)`.

The argument uses the shell twice in an essential way: the number of available column subsets is `\asymp(y/\log y)^t`, while every product modulus is only `O_t(y^t)`. This quantitative coupling disappears in the CRT realization of `MC-252`, where prescribed columns may live at exponentially or arbitrarily larger primes.

## 2. The parity sums are exactly Hamming/Fourier observables of the shell code

Write `c_r\in\mathbb F_2^{\mathcal P_y}` for the column of `(1)`. Since

\[
(-1)^{A_{p,r}}=\left(\frac pr\right),
\tag{14}
\]

we have for every fixed-size subset `T`

\[
B_y(T)
=
\sum_{p\in\mathcal P_y}
(-1)^{\sum_{r\in T}A_{p,r}}.
\tag{15}
\]

If `w(T)` denotes the Hamming weight of the XOR `\sum_{r\in T}c_r`, then

\[
B_y(T)=k_y-2w(T),
\qquad
\frac{w(T)}{k_y}
=\frac12-\frac{B_y(T)}{2k_y}.
\tag{16}
\]

Thus `(5)` is a bounded-order Fourier-uniformity statement for the actual shell columns.

For `t=1`, `(16)` says almost every column contains asymptotically equal numbers of quadratic residues and non-residues among lower primes. For `t=2`, `w(\{r,s\})` is the Hamming distance between `c_r` and `c_s`, so almost every pair is asymptotically at relative distance `1/2`.

A blind vector supported on `T` would satisfy `w(T)=0`, hence `B_y(T)=k_y`. Therefore `(3)` also bounds the number of blind vectors of any fixed support `t`. But this is not competitive with `MC-242`, which already excludes all blind supports below a quantity tending to infinity. The new content here is not a better minimum-distance theorem; it is the broader shell-localized parity-balance law and its exact information limit.

## 3. A logarithmic-rank Walsh control has stronger bounded-order balance

The tempting next inference would be that many nearly orthogonal shell columns must have nearly full binary rank. That inference is false.

Let

\[
V=\mathbb F_2^d,
\qquad k=|V|=2^d,
\]

index the rows by `x\in V` and the columns by nonzero `a\in V`. Define

\[
C_{x,a}=x\cdot a\in\mathbb F_2.
\tag{17}
\]

There are

\[
N=2^d-1\asymp k
\tag{18}
\]

columns, but the column space is the image of the linear map

\[
a\longmapsto(x\mapsto x\cdot a),
\]

so

\[
\boxed{\operatorname{rank}_{\mathbb F_2}C=d=\log_2 k.}
\tag{19}
\]

For distinct column labels `a_1,\ldots,a_t`, the parity bias is

\[
\sum_{x\in V}
(-1)^{x\cdot(a_1+\cdots+a_t)}.
\tag{20}
\]

Finite Fourier orthogonality gives

\[
\sum_{x\in V}(-1)^{x\cdot b}
=
\begin{cases}
k,&b=0,\\0,&b\ne0.
\end{cases}
\tag{21}
\]

Hence every pair of distinct columns has **exactly** Hamming distance `k/2`, despite the logarithmic rank `(19)`. More generally, for fixed `t`, a nonzero bias occurs only when

\[
a_1+\cdots+a_t=0.
\tag{22}
\]

Among `t`-element subsets of the `N` nonzero labels, at most `O_t(N^{t-1})` satisfy `(22)`, because the first `t-1` labels determine the last. Therefore

\[
\frac1{\binom Nt}
\sum_{|T|=t}
\left|\frac{B_C(T)}k\right|^2
=O_t\!\left(\frac1N\right)
=O_t\!\left(\frac1k\right).
\tag{23}
\]

At the shell scale `k_y\asymp N_y\asymp y/\log y`, the control `(23)` is at least as pseudorandom at every fixed parity order as the qualitative consequence `(5)`, yet its binary rank is only logarithmic.

This is the decisive falsification test. Pairwise distance, bounded-order parity balance, and even exact Walsh orthogonality away from a `1/N` fraction of additive relations do not force a large `\mathbb F_2` span.

## 4. Relation to the current generation frontier

`MC-246` identified the exact full blind quotient `G/H`: proving `H=G` removes all blind characters, while any residual quotient leaves a rough Möbius coset requiring signed cancellation. `MC-243` and `MC-251` showed that generic minimum-distance coding information gives only sublinear rank pressure. `MC-252` then proved that bare Legendre-symbol arithmetic without shell localization is universal enough to realize arbitrary low-codimension binary codes.

The present finding tests the most immediate way shell localization could repair that failure. Heath-Brown does indeed convert the shell into a strong mean-square parity law. But `(17)`--`(23)` show that this law lives at the wrong information level for generation: it controls **bounded-order Fourier statistics**, whereas rank failure can hide in higher-order additive relations among columns.

The next useful theorem must therefore cross one of the following boundaries:

- control parity products whose support `t=t(y)` grows far enough to see the possible blind relations;
- prove a shell-specific algebraic/analytic statement that rules out low-dimensional column spans without passing only through bounded-order moments;
- or bypass generation and directly prove signed cancellation for the exact rough Möbius coset from `MC-246`.

The first route is quantitatively nontrivial. In `(7)`, allowing `t` to grow also makes `M=(2y)^t` grow, while the factor `(MN)^\delta` is only controlled for fixed `\delta`; the standard `\ll_\delta` theorem does not provide the uniform dependence needed to send `t` to infinity. One cannot silently turn the fixed-`t` consequence into a growing-order theorem.

## 5. Prior-art and novelty audit

The analytic input is classical. Heath-Brown's 1995 theorem is the quadratic large sieve for real character sums used in `(7)`. Munsch--Shparlinski--Sun--Xiao, arXiv:`2604.23661v3`, explicitly restate its arbitrary-weight initial-interval consequence as equation (1.1) and develop new shifted-interval analogues; their abstract also emphasizes almost-all equidistribution of residues and non-residues for the short-interval problem they study.

The Walsh control `(17)`--`(23)` is standard finite-vector-space character orthogonality, equivalently the elementary character-table/simplex-code mechanism. No novelty is claimed for quadratic large-sieve estimates, Hamming-distance interpretations, Walsh characters, or low-rank binary constructions.

The durable Mathia delta is the **frontier classification** obtained by putting these standard mechanisms against the exact shell code of `MC-238`: tight localization does force strong fixed-order parity pseudorandomness, but that entire information class is compatible with logarithmic binary rank. This prevents pairwise or any other bounded-order Legendre balance theorem from being mistaken for the missing generation argument.

Primary sources:

- D. R. Heath-Brown, *A mean value estimate for real character sums*, Acta Arithmetica 72 (1995), no. 3, 235--275. DOI: `10.4064/aa-72-3-235-275`.
- Marc Munsch, Igor Shparlinski, Yu-Chen Sun and Yixiu Xiao, *A large sieve inequality for sums of Legendre symbols over short intervals*, arXiv:`2604.23661v3`, revised 5 August 2026, https://arxiv.org/abs/2604.23661.

## 6. Boundaries and falsification checks

- **Fixed-order only.** Equation `(3)` is proved for every fixed `t`; no uniform estimate in growing `t` is claimed.
- **Average over shell subsets.** The result controls almost all `t`-subsets, not every subset. A small exceptional family may contain all exact blind relations.
- **Odd-prime row.** The Heath-Brown application omits the single row `p=2`; adding or deleting one row is immaterial to the asymptotic balance statements but no exact claim about that row is hidden.
- **No rank gain.** The Walsh control gives a concrete matrix with `N\asymp k`, perfect pairwise balance, fixed-order mean-square bias `O_t(1/k)`, and rank only `\log_2 k`. Therefore no rank lower bound stronger than the existing frontier is inferred from `(5)`.
- **No shell-code realization of the Walsh control.** The control is deliberately abstract. It shows insufficiency of the bounded-order statistic, not that the actual Legendre shell has logarithmic rank.
- **No circular zero input.** Heath-Brown's theorem is unconditional; no zero-free region, GRH, or reciprocal-`L` continuation is used.
- **No Möbius amplitude claim.** The result concerns the residue-symbol code that governs the blind sector. It gives no cancellation estimate for the rough Möbius coset itself.

## Updated frontier

`MC-252` isolated shell localization as load-bearing. This finding shows exactly one substantial thing that localization buys for free from classical quadratic large-sieve theory: **all fixed parity orders look random on average**. It also shows why that is still not the missing theorem.

The generation problem is now more sharply separated into information levels. Bounded-order shell statistics can be excellent while global `\mathbb F_2` rank remains tiny. Any successful continuation must detect growing-order additive relations among shell columns, exploit a structure not reducible to bounded-order parity moments, or abandon generation in favor of direct signed rough-coset cancellation.