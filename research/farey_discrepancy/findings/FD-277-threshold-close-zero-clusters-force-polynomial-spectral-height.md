# FD-277 — Threshold close-zero clusters force polynomial spectral height

- **Date:** 2026-09-22
- **Status:** proved spectral-height/background tariff conditional on RH and simple zeros
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** zeta-zero clusters / Riemann--von Mangoldt / argument excursions / reciprocal-log packing / spectral repair
- **Depends on:** FD-261, FD-273, FD-276
- **Classification:** `EXACT-DERIVED + RH-CONDITIONAL + SIMPLE-ZERO + LOAD-BEARING-S(T)-BOUND + SPECTRAL-HEIGHT-TARIFF`

## Claim

FD-276 shows that a complete reciprocal-log zero cluster can reach the FD-261 positive-capacity threshold only by spending exponent on cluster cardinality, on the desingularized background envelope, or on both. The cardinality alternative still leaves a possible escape: perhaps a cluster with roughly `log x / log log x` zeros can be packed into the reciprocal-log collar at low spectral height and thereby supply the missing repair scale with a tame background.

That escape is incompatible with the zero-counting formula. A reciprocal-log cluster large enough to satisfy the FD-276 cardinality tariff creates an abnormally large jump of the argument term `S(t)` across an interval of length `O(1/log log x)`. Under RH, the sharp Carneiro--Chandee--Milinovich bound on `S(t)` then forces such a cluster to occur at polynomial spectral height.

Keep the polynomial-depth regime

\[
x=N^{\lambda+o(1)},\qquad \lambda>0,
\tag{1}
\]

and write

\[
\beta:=\log_2\frac32,
\qquad
c:=1-\beta=0.4150374992788438\ldots,
\qquad
L:=\log(2Nx),
\qquad
\eta:=L^{-1}.
\tag{2}
\]

Let `C={1/2+i gamma_1,...,1/2+i gamma_m}` be a complete reciprocal-log cluster in the FD-276 partition, so every internal ordinate gap is `<2 eta`, and assume RH and simple zeros. Suppose this single cluster contributes at least the FD-261 threshold

\[
\sum_{x<d\le 2x}|Q_{\mathcal C}(N,d)|
\ge x^{2-\beta-o(1)},
\tag{3}
\]

while its collar background obeys, for some fixed `0<=delta<c`,

\[
\mathfrak B_{\mathcal C}(\eta)
\le x^{\delta+o(1)}.
\tag{4}
\]

Put

\[
q:=c-\delta>0,
\qquad
\Gamma:=\max_{\rho\in\mathcal C}|\operatorname{Im}\rho|.
\tag{5}
\]

Then

\[
\boxed{
\frac{\log \Gamma}{\log x}
\ge
\frac{2q}
{1+\dfrac{2q}{\pi(1+1/\lambda)}}
-o(1).
}
\tag{6}
\]

In particular, without using the value of `lambda`, since `1+1/lambda>=1`,

\[
\boxed{
\frac{\log \Gamma}{\log x}
\ge
\frac{2q}{1+2q/\pi}-o(1).
}
\tag{7}
\]

For a subpolynomial background, `delta=0`, this gives the universal numerical tariff

\[
\boxed{
\Gamma
\ge
x^{0.6565900638708717-o(1)}.
}
\tag{8}
\]

At the balanced depth `lambda=1`, the sharper form (6) gives

\[
\Gamma
\ge
x^{0.7332102032858479-o(1)}.
\tag{9}
\]

Thus a threshold-sized complete close-zero cluster with tame external background cannot live at subpolynomial or low polynomial spectral height. The size/background ledger of FD-276 acquires a third resource: **spectral height**. A cluster that does not pay polynomial background conditioning must occur high enough that the ordinary zero density can absorb a substantial fraction of its reciprocal-log packing, while the remaining excess fits inside the maximal RH-scale `S(t)` excursion.

## Evidence

### 1. FD-276 converts threshold repair into cluster cardinality

Under (3)--(4), FD-276 gives

\[
(m-1)\log(2L)
+\log \mathfrak B_{\mathcal C}(\eta)
\ge
(c-o(1))\log x.
\tag{10}
\]

Since (1) implies

\[
L=
\left(1+\frac1\lambda+o(1)\right)\log x,
\qquad
\log(2L)=\log\log x+O(1),
\tag{11}
\]

(4) and (10) yield

\[
\boxed{
m
\ge
(q-o(1))\frac{\log x}{\log\log x}.
}
\tag{12}
\]

This is exactly the growing-cluster branch left open by FD-276.

### 2. Reciprocal-log connectivity compresses those zeros into a tiny interval

Because `C` is one connected component of the FD-276 partition, every internal gap satisfies

\[
\gamma_{j+1}-\gamma_j<\frac2L.
\]

Hence its total ordinate diameter `h=gamma_m-gamma_1` obeys

\[
\boxed{
h<\frac{2(m-1)}L.}
\tag{13}
\]

For a threshold cluster, (12)--(13) already give `h=O(1/log log x)`. Thus all `m` zeros lie in a shrinking interval, even though `m` itself grows like `log x/log log x`.

### 3. Zero counting turns the packing into an `S(t)` excursion

Let `N_zeta(T)` count nontrivial zeros with ordinate in `(0,T]`, with multiplicity. Choose `t_-` immediately below `gamma_1` and `t_+` immediately above `gamma_m`, inside the two exterior gaps of the complete cluster. Let the endpoint offsets tend to zero after the estimate. Then

\[
N_\zeta(t_+)-N_\zeta(t_-)=m.
\tag{14}
\]

The Riemann--von Mangoldt formula is

\[
N_\zeta(t)
=
\frac{t}{2\pi}\log\frac{t}{2\pi}
-\frac{t}{2\pi}
+\frac78
+S(t)
+O(t^{-1}).
\tag{15}
\]

On the cluster interval, the derivative of the smooth term is

\[
\frac1{2\pi}\log\frac{t}{2\pi}.
\]

Using (13), and writing `Gamma` for the upper cluster height, (14)--(15) therefore imply

\[
\begin{aligned}
|S(t_+)|+|S(t_-)|
&\ge
m-
\frac{h}{2\pi}\log(2\Gamma)-O(1)\\
&\ge
m\left(1-
\frac{\log(2\Gamma)}{\pi L}
\right)-O(1).
\end{aligned}
\tag{16}
\]

The factor `1/pi` is important. FD-276 joins gaps smaller than `2 eta`, not `eta`; losing this factor of two would give an incorrect stronger constant.

Equation (16) is the structural bridge. A large reciprocal-log component is not merely a collection of small gaps: unless its height is itself large, it forces a large local excursion of the zero-counting error.

### 4. The sharp RH bound on `S(t)` forces spectral height

Carneiro, Chandee and Milinovich prove under RH that

\[
|S(t)|
\le
\left(\frac14+o(1)\right)
\frac{\log t}{\log\log t}.
\tag{17}
\]

This external theorem is load-bearing only at this final comparison step.

First, (12), (16), and (17) exclude `Gamma=x^{o(1)}`: the left side required by (16) is of order `log x/log log x`, while both the smooth zero-density contribution and the allowed `S` excursion are `o(log x/log log x)`.

Now suppose along a subsequence

\[
\Gamma=x^{\kappa+o(1)}
\tag{18}
\]

with finite positive `kappa`; if `kappa` is unbounded then (6) is automatic. From (11),

\[
\frac{\log(2\Gamma)}L
=
\frac{\kappa}{1+1/\lambda}+o(1).
\tag{19}
\]

Using (12) in (16), while (17) bounds the two endpoints together by

\[
|S(t_+)|+|S(t_-)|
\le
\left(\frac\kappa2+o(1)\right)
\frac{\log x}{\log\log x},
\tag{20}
\]

gives, whenever the parenthesis in (16) is positive,

\[
q\left(
1-
\frac{\kappa}{\pi(1+1/\lambda)}
\right)
\le
\frac\kappa2.
\tag{21}
\]

If that parenthesis is nonpositive, `kappa>=pi(1+1/lambda)` and the desired lower bound is already much weaker. Solving (21) yields exactly (6). Since the right side of (6) is minimized over `lambda>0` as `lambda` tends to infinity, (7) follows. Substituting `q=c` gives (8), while `lambda=1` gives (9).

## Stress tests

The first stress test is the reciprocal-log factor of two. FD-276 defines components by joining consecutive zeros whenever the gap is `<2/L`. Therefore a cluster with `m` nodes can occupy almost `2(m-1)/L`; its smooth expected zero count can consume as much as

\[
\frac{m\log\Gamma}{\pi L},
\]

not `m log Gamma/(2 pi L)`. Equation (16) deliberately uses the weaker, correct constant. At the universal subpolynomial-background boundary `kappa=0.6565900638708717...`, one checks numerically that

\[
c\left(1-\frac\kappa\pi\right)
=\frac\kappa2
=0.3282950319354358\ldots,
\]

so the constant closes exactly at the advertised point in the worst `lambda -> infinity` regime.

The second stress test is a high cluster. At `Gamma` comparable with `x`, the smooth term may account for a nontrivial fraction of the packed zeros and the sharp `S` bound has a full `log x/log log x` budget. The argument therefore does **not** exclude high close-zero clusters. This is intentional: the theorem is a height tariff, not a no-clustering theorem.

The third stress test is background trading. If

\[
\mathfrak B_{\mathcal C}(\eta)=x^{\delta+o(1)}
\]

with `delta` approaching `c`, then `q=c-delta` tends to zero and the height lower bound in (6)--(7) vanishes continuously. This matches FD-276: once the external background pays essentially all of the missing `1-beta` exponent, cluster cardinality and hence zero-count packing no longer need to be large.

The fourth stress test is aggregate coherence. Equations (6)--(8) concern a **single complete component whose own grouped packet is threshold-sized**. They do not rule out many individually subthreshold clusters adding coherently. That is the explicit aggregate loophole left by FD-276, and this finding does not silently close it.

## Prior-art check

The Riemann--von Mangoldt formula and the interpretation of `S(t)` as the zero-counting error are classical and are not claimed as new. The load-bearing modern input is the RH-conditional sharp estimate

\[
|S(t)|\le(1/4+o(1))\log t/\log\log t
\]

from Emanuel Carneiro, Vorrapan Chandee and Micah B. Milinovich, *Bounding S(t) and S_1(t) on the Riemann hypothesis*, Mathematische Annalen **356**(3) (2013), 939--968, DOI `10.1007/s00208-012-0876-z`, arXiv `1309.1526`. A fresh search also checked current close-gap and short-interval-zero literature. It found the standard relationship between local zero counts and `S(t)`, and recent work on small normalized gaps, but no result coupling the FD-276 reciprocal-log size/background repair tariff to the sharp `S(t)` constant to produce the spectral-height bound (6).

Accordingly, the `S(t)` theorem is added to `SOURCES.md`; the derivation from the FD-276 packet ledger to (6) is repository-specific.

## Implications

FD-273 says that threshold finite-packet coherence not already suppressed by separated-zero estimates must move toward the close-zero complement. FD-274 removes the internal reciprocal-derivative singularity of such close clusters. FD-275 removes frequency and packet differentiation as hidden power sources. FD-276 then says a complete reciprocal-log component must pay the exponent `1-beta` through cardinality and external background conditioning.

FD-277 now prices the cardinality resource itself. **A tame-background threshold cluster must also be high.** With subpolynomial background it cannot occur below spectral height `x^(0.656590...-o(1))`, uniformly over every fixed polynomial depth relation; at balanced depth the floor rises to `x^(0.733210...-o(1))`.

This does not yet kill the spectral route, but it substantially narrows its single-cluster branch. A surviving cluster must simultaneously be reciprocal-log dense, high in the zero spectrum, and sufficiently phase-aligned at the source-selected integer horizon. The remaining genuinely different loophole is aggregate: many complete components can each stay below the single-cluster threshold and perhaps add coherently. That is now the natural target for the next pass.

## Limitations

The result inherits RH and simple-zero assumptions from the reciprocal-log packet decomposition of FD-276. The `S(t)` upper bound (17) is conditional on RH but does not require simplicity by itself.

The finding controls only complete reciprocal-log components for which the FD-276 collar estimate applies and only when one component contributes at the threshold scale on its own. It does not control a packet remainder, multiple zeros, off-critical zeros when RH is dropped, or coherent accumulation across many individually subthreshold components.

The numerical exponents are asymptotic. They use a fixed polynomial-depth relation `x=N^(lambda+o(1))` and the asymptotic sharp constant `1/4` in (17); no finite-height explicit claim is made.
