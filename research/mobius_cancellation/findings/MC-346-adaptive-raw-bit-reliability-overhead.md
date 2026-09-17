# MC-346 — Adaptive raw-bit queries pay a logarithmic reliability overhead

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-345` shows that adaptive bit-flip source queries cannot transmit more than one BSC-capacity unit per access. That Shannon converse is sharp for a generic coded channel, but it does not price the extra reliability cost of the much narrower source-access primitive actually studied there: every query exposes **one raw source coordinate**, possibly repeatedly, rather than an arbitrary coded combination of the source bits.

For this raw-coordinate model, near-exact recovery is strictly more expensive. Keep the adaptive BSC query protocol of `MC-345`, with

\[
Z_t=X_{J_t}N_t,
\qquad
\mathbf P(N_t=-1)=q,
\qquad
0<q<\frac12,
\]

an adapted stopping time `\tau`, and complete transcript `T`. Let

\[
N_j:=\sum_{t\le\tau}\mathbf 1_{\{J_t=j\}}
\]

be the number of accesses to source coordinate `j`, and let `\widehat X(T)` be any estimator of the reciprocal source vector. Write

\[
\bar p
:=
\frac1R\sum_{j=1}^R
\mathbf P\!\left(\widehat X_j\ne X_j\right)
=
\frac1R\mathbf E\,d_H(\widehat X,X),
\tag{1}
\]

and define the one-query binary testing divergence, in nats,

\[
D_q
:=
D\!\left(\operatorname{Bern}(1-q)\middle\|\operatorname{Bern}(q)\right)
=
(1-2q)\log\frac{1-q}{q}.
\tag{2}
\]

Finally put

\[
\Lambda_k:=\frac{2^k-2}{2^k-1}
\qquad(k\ge2),
\qquad
[u]_+:=\max\{u,0\}.
\tag{3}
\]

For **even** `R>=2`, the reciprocal source law is uniform on the punctured cube `\{-1,+1\}^R\setminus\{(+1,\ldots,+1)\}`. Every finite-mean adaptive raw-bit protocol therefore satisfies

\[
\boxed{
\mathbf E\tau
\ge
\frac{\Lambda_R R}{D_q}
\left[
\log\frac{\Lambda_R}{4\bar p}
\right]_+.
}
\tag{4}
\]

For **odd** `R>=3`, the source law lives on the even-parity cube, with mass `1/(2^R-1)` at the all-`+1` word and mass `2/(2^R-1)` at every other parity-compatible word. In that case

\[
\boxed{
\mathbf E\tau
\ge
\frac{\Lambda_R\Lambda_{R-1}R}{2D_q}
\left[
\log\frac{\Lambda_R\Lambda_{R-1}}{4\bar p}
\right]_+.
}
\tag{5}
\]

The constants are not the main point. At every fixed `0<q<1/2`, both parities give the reliability law

\[
\boxed{
\bar p\to0
\quad\Longrightarrow\quad
\mathbf E\tau
=\Omega_q\!\left(R\log\frac1{\bar p}\right).
}
\tag{6}
\]

This closes the small-error gap left explicitly open by `MC-345`. Its mutual-information bound remains only `Theta(R)` as the target error tends to zero, because one bit of mutual information per coordinate is enough in principle. Raw noisy coordinate access cannot exploit an arbitrary channel code: driving the coordinate error itself to zero requires logarithmically growing repeated evidence.

The endpoint consequence is immediate. At matched-filter energy, `MC-340` proves that

\[
\mathcal E(W)\le1,
\qquad
\delta(W)\le\varepsilon
\]

forces source-coordinate Bayes error at most

\[
\alpha_\varepsilon
:=
\varepsilon-\frac{\varepsilon^2}{2}
\tag{7}
\]

on average. Whenever the admitted observation family is downstream of the raw-query transcript `T` as in `MC-345`, the Bayes estimator based on `T` is at least as accurate. Hence `(4)` and `(5)` hold with `\bar p` replaced by `\alpha_\varepsilon`:

\[
\mathbf E\tau
\ge
\frac{\Lambda_R R}{D_q}
\left[
\log\frac{\Lambda_R}{4\alpha_\varepsilon}
\right]_+
\qquad(R\ \mathrm{even}),
\tag{8}
\]

and

\[
\mathbf E\tau
\ge
\frac{\Lambda_R\Lambda_{R-1}R}{2D_q}
\left[
\log\frac{\Lambda_R\Lambda_{R-1}}{4\alpha_\varepsilon}
\right]_+
\qquad(R\ \mathrm{odd}).
\tag{9}
\]

Thus, for fixed positive BSC noise,

\[
\boxed{
\varepsilon_R\to0
\quad\Longrightarrow\quad
\mathbf E\tau
=\Omega_q\!\left(R\log\frac1{\varepsilon_R}\right).
}
\tag{10}
\]

In particular, `\varepsilon_R=R^{-\beta}` for fixed `\beta>0` requires `\Omega_q(R\log R)` raw source accesses. At `\varepsilon=0`, the right side diverges, continuously matching the positive-noise zero-error impossibility already proved in `MC-345`.

No estimate for `M(x)` follows. The result is a finite reciprocal-endpoint admission theorem: an arithmetic architecture that really obtains only repeated noisy reads of individual source phases must pay a superlinear access budget when its dephasing error is required to vanish.

## 1. Adaptive change of measure prices every neighboring source pair

Fix two source states `x,x'` and run the same adaptive controller under each. Let `P_x^T` and `P_{x'}^T` be the laws of the complete stopped transcript. The standard stopped adaptive likelihood-ratio calculation gives

\[
D(P_x^T\|P_{x'}^T)
=
D_q\sum_{j:x_j\ne x'_j}\mathbf E_x N_j.
\tag{11}
\]

Indeed, conditional on the observed history the next query index is already determined by the controller, and the two models differ only when that queried coordinate has opposite source signs. Every such access contributes exactly the BSC divergence `D_q`; all other accesses contribute zero. Controller randomness has the same law under both source states and contributes no divergence.

For any event `A`, Bretagnolle--Huber gives

\[
P_x^T(A)+P_{x'}^T(A^c)
\ge
\frac12\exp\!\bigl(-D(P_x^T\|P_{x'}^T)\bigr).
\tag{12}
\]

Applying `(12)` in both directions and taking `A` to be the estimator decision for a coordinate on which `x` and `x'` differ yields the symmetric testing bound

\[
e_j(x)+e_j(x')
\ge
\frac12
\exp\!\left(
-\frac{D_q}{2}
\sum_{k:x_k\ne x'_k}
\bigl(\mathbf E_xN_k+\mathbf E_{x'}N_k\bigr)
\right),
\tag{13}
\]

where

\[
e_j(x):=P_x^T(\widehat X_j\ne x_j).
\]

Equation `(13)` is the load-bearing reliability step missing from a pure capacity argument: making a neighboring source pair exponentially easier to distinguish requires linearly increasing the number of noisy accesses to the coordinates on which that pair differs.

## 2. Even rank: the punctured hypercube gives the full logarithmic cost

For even `R`, let

\[
S=\{-1,+1\}^R\setminus\{\mathbf 1\},
\qquad |S|=m=2^R-1.
\]

Join two vertices when they differ in exactly one coordinate. Removing `\mathbf1` from the full cube deletes exactly `R` edges, so the remaining graph has

\[
|E|
=R(2^{R-1}-1)
=\frac{mR\Lambda_R}{2}
\tag{14}
\]

edges.

For an edge `e=\{x,x'\}` in coordinate `j`, define

\[
b_e
:=
\frac{\mathbf E_xN_j+\mathbf E_{x'}N_j}{2}.
\tag{15}
\]

Equation `(13)` gives

\[
e_j(x)+e_j(x')\ge\frac12e^{-D_qb_e}.
\tag{16}
\]

Every coordinate error `e_j(x)` appears in at most one surviving edge in direction `j`. Therefore

\[
mR\bar p
\ge
\frac12\sum_{e\in E}e^{-D_qb_e}.
\tag{17}
\]

Jensen's inequality gives

\[
\sum_{e\in E}e^{-D_qb_e}
\ge
|E|\exp\!\left(
-D_q\frac1{|E|}\sum_{e\in E}b_e
\right).
\tag{18}
\]

Moreover each query count at a state contributes to at most one edge per queried coordinate, so

\[
\sum_{e\in E}b_e
\le
\frac12\sum_{x\in S}\mathbf E_x\tau
=
\frac m2\mathbf E\tau.
\tag{19}
\]

Using `(14)` in `(18)`--`(19)` gives

\[
\bar p
\ge
\frac{\Lambda_R}{4}
\exp\!\left(
-\frac{D_q\mathbf E\tau}{\Lambda_RR}
\right),
\tag{20}
\]

which rearranges to `(4)`.

The puncture costs only the factor `\Lambda_R=1-O(2^{-R})`; asymptotically the source behaves like the full hypercube for this reliability converse.

## 3. Odd rank: pair flips preserve parity and still force the logarithm

For odd `R`, let `E_0` be the event that the source vector is not the all-`+1` word. `MC-340` gives

\[
\mathbf P(E_0)=\Lambda_R.
\tag{21}
\]

Conditioned on `E_0`, the source is uniform on the even-parity cube with its all-`+1` word removed. There are

\[
M=2^{R-1}-1
\]

conditional source states.

On this parity space, a one-coordinate flip is not admissible. Instead join two conditional source states when they differ in exactly **two** coordinates. The full even-parity cube has degree `\binom R2`; deleting the all-`+1` vertex leaves

\[
|E_2|
=
\left(2^{R-2}-1\right)\binom R2
=
\frac{M\Lambda_{R-1}}2\binom R2
\tag{22}
\]

surviving pair-flip edges.

For an edge `e=\{x,x'\}` differing in coordinates `i,j`, put

\[
b_e
:=
\frac12\Bigl(
\mathbf E_x(N_i+N_j)
+
\mathbf E_{x'}(N_i+N_j)
\Bigr),
\tag{23}
\]

where expectations in this section are under the conditional source law. Applying `(13)` separately to coordinates `i` and `j` gives

\[
e_i(x)+e_i(x')+e_j(x)+e_j(x')
\ge
e^{-D_qb_e}.
\tag{24}
\]

Each coordinate error at a vertex can occur in at most `R-1` incident pair-flip edges. Hence, if `\bar p_0` is the conditional average Hamming error,

\[
(R-1)MR\bar p_0
\ge
\sum_{e\in E_2}e^{-D_qb_e}.
\tag{25}
\]

For the access side, each coordinate query at a vertex participates in at most `R-1` incident pair-flip edges, so

\[
\sum_{e\in E_2}b_e
\le
\frac{M(R-1)}2\mathbf E(\tau\mid E_0).
\tag{26}
\]

Using `(22)` and Jensen in `(25)`--`(26)` yields

\[
\bar p_0
\ge
\frac{\Lambda_{R-1}}4
\exp\!\left(
-\frac{2D_q\mathbf E(\tau\mid E_0)}{\Lambda_{R-1}R}
\right).
\tag{27}
\]

Unconditionally,

\[
\bar p\ge\Lambda_R\bar p_0,
\qquad
\mathbf E\tau\ge\Lambda_R\mathbf E(\tau\mid E_0).
\tag{28}
\]

Combining `(27)` and `(28)` proves `(5)`.

The factor `1/2` in the odd-rank exponent is not claimed sharp. It comes from using parity-preserving pair flips. What matters for the present admission question is that the logarithmic reliability penalty survives the exact one-relation source geometry.

## 4. Endpoint dephasing forces the small Hamming risk needed by the converse

`MC-340` defines

\[
\rho_i^2
=
\mathbf E\left|\mathbf E[X_i\mid Y_i]\right|^2,
\qquad
\rho^2=\frac1R\sum_i\rho_i^2,
\]

and proves that matched-filter energy plus dephasing error imply

\[
\mathcal E(W)\le1,
\quad
\delta(W)\le\varepsilon
\quad\Longrightarrow\quad
\rho\ge1-\varepsilon.
\tag{29}
\]

The Bayes error `e_i` for predicting `X_i` from its admitted observation satisfies

\[
e_i
\le
\frac{1-\rho_i^2}{2}.
\tag{30}
\]

Averaging and using `(29)` therefore gives

\[
\frac1R\sum_i e_i
\le
\frac{1-\rho^2}{2}
\le
\varepsilon-\frac{\varepsilon^2}{2}
=\alpha_\varepsilon.
\tag{31}
\]

In the `MC-345` source-query model, the complete transcript `T` precedes every admitted downstream observation. An estimator that sees `T` can emulate the coordinate Bayes rules based on the `Y_i`, so its optimal average Hamming risk is at most `\alpha_\varepsilon`. Substituting this estimator into `(4)` and `(5)` proves `(8)` and `(9)`.

This is a strictly different regime from the capacity converse. `MC-345` gives

\[
\mathbf E\tau\,c(q)
\ge
H(X)-Rh(\alpha_\varepsilon),
\]

whose right side approaches `Theta(R)` as `\varepsilon\to0`. Equations `(8)`--`(10)` exploit the **raw-coordinate** restriction and diverge logarithmically as the target error vanishes.

## 5. The reliability scale is sharp for raw source recovery

The `R\log(1/\bar p)` dependence is not an artifact of the lower-bound proof. Query every coordinate the same odd number `n` of times and decode by majority vote. A standard Hoeffding/Chernoff bound gives

\[
\mathbf P(\widehat X_j\ne X_j)
\le
\exp\!\left(-2n\left(\frac12-q\right)^2\right).
\tag{32}
\]

Thus

\[
n=O_q\!\left(\log\frac1{\bar p}\right)
\]

suffices for average Hamming error at most `\bar p`, using

\[
O_q\!\left(R\log\frac1{\bar p}\right)
\]

raw accesses. This is only a source-recovery achievability statement; it does **not** prove that an arbitrary recovered-source transcript automatically realizes the Möbius coefficient family required for endpoint dephasing.

## Prior art and novelty boundary

The statistical mechanism is classical. Bretagnolle and Huber's testing inequality gives the exponential conversion from transcript KL divergence to binary testing error used in `(12)`. Kaufmann, Cappé and Garivier's adaptive change-of-measure lemma for stopped bandit experiments gives a standard modern form of the expected-sample-count/KL accounting underlying `(11)`.

The raw noisy-query model itself goes back at least to Feige, Raghavan, Peleg and Upfal, *Computing with Noisy Information*, SIAM Journal on Computing **23** (1994), 1001--1018, DOI `10.1137/S0097539791195877`, which studies adaptive Boolean decision trees whose query answers are independently flipped and proves tight bounds for parity, threshold and other functions.

The closest recent boundary is Yuzhou Gu, Xin Li and Yinzhan Xu, *A Unified Lower Bound on the Noisy Query Complexity of Boolean Functions*, Proceedings of COLT 2026, PMLR **336** (2026), 2940--2962, arXiv `2606.11448`. Their general lower bound is built from degree statistics of subgraphs of the Boolean hypercube and in particular recovers the classical logarithmic noisy-query overhead for high-influence functions such as parity. The punctured-cube and parity-pair graphs used above therefore sit squarely inside an established noisy-query/Assouad-style lower-bound language.

No novelty is claimed for noisy decision trees, adaptive change of measure, Bretagnolle--Huber, hypercube edge averaging, repeated-query reliability, or the `R\log(1/\bar p)` scale as an abstract noisy-recovery phenomenon. The durable Mathia delta is the exact specialization to the reciprocal endpoint source law and, crucially, the coupling to the independent `MC-340` theorem that converts near-unit-energy endpoint dephasing into vanishing average source-coordinate error. This yields the explicit dephasing-access bounds `(8)`--`(10)` and closes the reliability-exponent loophole left open by `MC-345`.

## Boundaries and falsification tests

- **Raw coordinates are essential.** The logarithmic overhead can disappear for a channel allowed to query coded combinations of source bits. The theorem must not be promoted from raw coordinate access to arbitrary source measurements.
- **The noise is memoryless BSC noise.** Correlated, source-dependent or stateful noise changes the transcript KL accounting and needs a separate audit.
- **Selector side information is still forbidden.** As in `MC-345`, if the controller can inspect unpriced source information before choosing `J_t`, that side channel must be included in the transcript budget.
- **Positive noise is essential to `(4)`--`(10)`.** As `q\downarrow0`, `D_q\to\infty` and the reliability lower bound becomes vacuous; noiseless recovery needs only linear raw access, exactly as `MC-345` shows.
- **The even-rank constant is cleaner than the odd-rank constant.** The odd proof uses pair flips on the parity subspace and is not asserted optimal. Both parities nevertheless force the same `Omega_q(R log(1/error))` scale.
- **Average Hamming recovery is the relevant intermediate object.** The theorem does not require block-error recovery; it is stronger than a union-bound argument and applies directly to the average coordinate error supplied by `MC-340`.
- **The source-recovery upper bound is not endpoint achievability.** Recovering `X` accurately does not by itself construct a source-natural Möbius observable or prove small dephasing.
- **No arithmetic access theorem is supplied.** The line still needs to identify an actual Möbius-derived observable whose information flow genuinely reduces to raw or otherwise priceable source accesses.
- **No RH or Mertens estimate follows.** This remains a finite reciprocal-endpoint obstruction.

## Consequence for the research line

`MC-345` showed that feedback cannot increase information per noisy source access, but it deliberately left the small-nonzero-error reliability cost open. The present result closes that gap for the raw-coordinate primitive: **vanishing endpoint dephasing at matched-filter energy requires a superlinear number of accesses whenever the per-access bit-flip noise stays fixed and positive**.

This sharpens the remaining arithmetic frontier. An architecture with only `Theta(R)` noisy raw source accesses cannot approach exact endpoint dephasing; to survive it must either tolerate a fixed dephasing error, obtain `Omega(R log(1/epsilon_R))` genuine accesses, lower the effective noise with scale, or expose a richer coded source observable whose query primitive is not covered by this theorem. The next useful obstruction must therefore price the actual arithmetic measurement class, not merely count controller adaptivity or raw bit accesses.