# MC-324 — Endpoint pair spectrum forces a quartic common-source radical

**Status:** `EXACT-DERIVED` · `LITERATURE+DERIVED` · `DECISIVE-NEGATIVE` · `FRONTIER-ADVANCE` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

Continue the exact reciprocal endpoint partition of `MC-296` and the fixed lower-prime source-incidence package of `MC-312`. Let

\[
L=\langle\lambda_1,\ldots,\lambda_R\rangle\cong\mathbf F_2^R,
\qquad R\to\infty,
\tag{1}
\]

where the endpoint defects are equal, so for every `I\subseteq[R]`,

\[
x_{\lambda_I}
=(-1)^{|I|}\left(1-\frac{2|I|}{R}\right).
\tag{2}
\]

Choose **any fixed common lower-prime product representatives**

\[
V_i\subseteq\{p\le y:p\text{ odd prime}\}
\qquad(1\le i\le R)
\tag{3}
\]

for the independent generators `lambda_i`. Put

\[
U:=\bigcup_{i=1}^R V_i,
\qquad
P:=\prod_{p\in U}p,
\qquad
n:=|U|.
\tag{4}
\]

No common-modulus analytic estimate is assumed for `P`.

Then the varying-modulus prime Halász–Montgomery bound of `MC-323`, applied not to the generators but to their **pair sums**, forces

\[
\boxed{
\liminf_{y\to\infty}\frac{\log P}{\log y}\ge4.
}
\tag{5}
\]

Equivalently, for every fixed `eta>0`, an exact reciprocal endpoint realization inside a common source package with

\[
P\le y^{4-\eta}
\tag{6}
\]

is impossible for all sufficiently large `y`.

More quantitatively, for every fixed `delta\in(0,2)`,

\[
\boxed{
\log P
\ge
\left(4-2\delta-O\!\left(\frac1R\right)
      -O_\delta\!\left(\frac1{R^2}\right)\right)\log y.
}
\tag{7}
\]

The mechanism is a weighted Plotkin double count. For every pair `i<j`, the symmetric-difference representative

\[
V_i\triangle V_j
\tag{8}
\]

represents `lambda_i+lambda_j`; write

\[
m_{ij}:=\prod_{p\in V_i\triangle V_j}p.
\tag{9}
\]

The exact endpoint law `(2)` gives

\[
\boxed{
x_{\lambda_i+\lambda_j}=1-\frac4R,}
\tag{10}
\]

so for large `R` every pair mode has fixed prime-shell bias, say at least `1/2` in magnitude. Distinct unordered pairs give distinct shell functionals because the `lambda_i` are independent.

`MC-323` therefore implies that, for every fixed `delta>0`, all but `O_delta(1)` of the `binom(R,2)` pair modes have minimum primitive source conductor larger than `y^(2-delta)`. Since their package representatives `(8)` need not be minimal but satisfy

\[
\mathcal Q(\lambda_i+\lambda_j)\le m_{ij},
\tag{11}
\]

all but `O_delta(1)` pairs obey

\[
\boxed{m_{ij}>y^{2-\delta}.}
\tag{12}
\]

On the other hand, if

\[
a_p:=\#\{i:p\in V_i\},
\tag{13}
\]

then each source prime `p` occurs in exactly `a_p(R-a_p)` pairwise symmetric differences. Hence

\[
\sum_{1\le i<j\le R}\log m_{ij}
=
\sum_{p\in U}a_p(R-a_p)\log p
\le
\frac{R^2}{4}\log P.
\tag{14}
\]

Combining `(12)` and `(14)` gives `(7)` and then `(5)`.

This is materially stronger than the first-order source-redundancy result of `MC-312`. If the common package also satisfies the natural source-prime cap

\[
Z:=\max U
\le y^{(1+o(1))/R},
\tag{15}
\]

then `P\le Z^n` and `(5)` force

\[
\boxed{n\ge(4-o(1))R.}
\tag{16}
\]

Thus the natural-scale endpoint needs asymptotically **four source coordinates per endpoint rank**, not merely the `2R-o(R)` coordinates forced by the generalized-Hamming-weight argument of `MC-312`.

The result also extends the useful source-package horizon beyond the common-modulus prime Halász–Montgomery barrier of `MC-322`. `MC-322` directly rules out a growing fixed-bias family when the whole common modulus is below `y^(3-delta)`. The present argument does not feed `P` into that fixed-modulus estimate. Instead it applies the varying-modulus theorem to the individual primitive pair characters, then uses source-code geometry to recover a lower bound on the **total** common radical. This rules out every fixed common-radical exponent below `4`, including the interval between the cubic analytic horizon and the new quartic source threshold.

No estimate for `M(x)` follows.

## 1. Pair modes remain maximally biased

For the reciprocal endpoint, `MC-296` proves the complete selected Fourier profile `(2)`. Taking `I={i,j}` gives

\[
x_{\lambda_i+\lambda_j}
=1-\frac4R.
\tag{17}
\]

Hence for `R>=8`,

\[
|x_{\lambda_i+\lambda_j}|\ge\frac12.
\tag{18}
\]

The pair modes are distinct. If

\[
\lambda_i+\lambda_j
=
\lambda_k+\lambda_\ell,
\tag{19}
\]

then

\[
\lambda_i+\lambda_j+\lambda_k+\lambda_\ell=0.
\]

Independence of the basis `lambda_1,...,lambda_R` forces the two unordered pairs to coincide.

As established in `MC-301`, every nonzero shell functional has a minimizing lower-prime product representative that yields a primitive real Dirichlet character of odd squarefree conductor `mathcal Q(lambda)`, distinct functionals yield distinct primitive characters, and its normalized prime-shell average equals `x_lambda`. Therefore the complete pair family satisfies the distinctness, cubefree-conductor, and fixed-bias hypotheses needed by `MC-323`.

Fix `delta in (0,2)` and apply equation `(8)` of `MC-323` with `tau=1/2` to the pair family. It gives

\[
\#\left\{
\{i,j\}:i<j,
\mathcal Q(\lambda_i+\lambda_j)\le y^{2-\delta}
\right\}
=O_\delta(1).
\tag{20}
\]

For each pair, multiplying the two fixed package representatives `(3)` cancels common prime factors modulo squares, so `V_i triangle V_j` represents `lambda_i+lambda_j`. Consequently `(11)` holds, and `(20)` immediately gives `(12)` for all but `O_delta(1)` pairs.

The distinction between the **minimum primitive conductor** and the **chosen package representative** is important. The analytic theorem constrains the former. The inequality `mathcal Q<=m_ij` then transfers that lower bound to every package realization of the same pair mode; no claim that the symmetric-difference product is itself the minimal conductor is needed.

## 2. Weighted Plotkin double counting turns pair cost into total radical cost

For a source prime `p in U`, let `a_p` be as in `(13)`. Among the `R` generator representatives, exactly `a_p` contain `p` and `R-a_p` do not. Therefore `p` belongs to `V_i triangle V_j` for exactly

\[
a_p(R-a_p)
\tag{21}
\]

unordered pairs `{i,j}`.

Taking logarithms in `(9)` and summing over pairs gives the exact identity

\[
\sum_{i<j}\log m_{ij}
=
\sum_{p\in U}a_p(R-a_p)\log p.
\tag{22}
\]

Since

\[
a_p(R-a_p)\le\frac{R^2}{4},
\tag{23}
\]

we obtain

\[
\sum_{i<j}\log m_{ij}
\le
\frac{R^2}{4}\sum_{p\in U}\log p
=
\frac{R^2}{4}\log P.
\tag{24}
\]

This is the ordinary Plotkin column-counting argument with the `p`-th binary coordinate assigned positive weight `log p` instead of unit Hamming weight.

Now `(12)` supplies the lower bound

\[
\sum_{i<j}\log m_{ij}
>
\left(\binom R2-O_\delta(1)\right)
(2-\delta)\log y.
\tag{25}
\]

Combining `(24)` and `(25)` yields

\[
\frac{\log P}{\log y}
>
\frac{4(2-\delta)}{R^2}
\left(\binom R2-O_\delta(1)\right).
\tag{26}
\]

Since

\[
\frac4{R^2}\binom R2
=2\left(1-\frac1R\right),
\tag{27}
\]

we obtain

\[
\frac{\log P}{\log y}
\ge
(4-2\delta)\left(1-\frac1R\right)
-O_\delta(R^{-2}),
\tag{28}
\]

which is `(7)`.

Because `delta>0` is arbitrary but fixed, first take `y->infinity` for each fixed `delta` and then let `delta->0`. This proves `(5)` without inserting a forbidden moving `delta(y)` into Schlage-Puchta's estimate.

## 3. Natural source scale now costs four ranks

Let `Z=max U`. Trivially

\[
P\le Z^n.
\tag{29}
\]

Under `(15)`,

\[
\log P
\le
n\frac{1+o(1)}R\log y.
\tag{30}
\]

Combining `(30)` with `(5)` gives

\[
\frac nR\ge4-o(1),
\]

which proves `(16)`.

This changes the coding frontier exposed in `MC-312`–`MC-314`. Those findings used high-rank source cuts and generalized Hamming weights to force approximately `2R` coordinates at the natural scale, then found that generic rate-one-half binary codes can match the coarse generalized-weight profile. The present argument uses a different resource: the **arithmetic fixed bias of all degree-two endpoint modes**. Varying-modulus prime cancellation turns that pair spectrum into an almost-everywhere lower bound on pairwise weighted source distance, and the Plotkin average-distance ceiling then forces twice as much total logarithmic source mass.

In coding language, the `R` incidence rows are not merely required to generate a high-generalized-weight `[n,R]` code. Almost every pair of rows must be separated by weighted Hamming distance exceeding `(2-delta)log y`. A codebook with `R` growing rows cannot sustain that average pairwise distance unless the total coordinate weight is asymptotically at least `4 log y`.

## 4. Prior art and novelty boundary

The analytic input is exactly the already audited Schlage-Puchta varying-modulus prime Halász–Montgomery theorem used in `MC-323`: Jan-Christoph Schlage-Puchta, *Primes in short arithmetic progressions*, Acta Arithmetica **106** (2003), 143–149, DOI `10.4064/aa106-2-4`, Theorem 3. No strengthening of that theorem is asserted here.

The coding input is the classical Plotkin bound and its standard proof by summing all pairwise Hamming distances column by column: Morris Plotkin, *Binary codes with specified minimum distance*, IRE Transactions on Information Theory **6** (1960), 445–450, DOI `10.1109/TIT.1960.1057584`. In a binary codebook column containing `a` ones and `R-a` zeros, that column contributes `a(R-a)` to the unordered pair-distance sum and is maximized at `R^2/4`. Equation `(22)` is the immediate positively weighted version with coordinate weight `log p`; no new coding bound is claimed.

A targeted literature search on 16 September 2026 found the Plotkin pair-distance mechanism, generalized Plotkin variants, and the prime-character estimates separately, but no source asserting the arithmetic composition `(20)`–`(28)` for reciprocal endpoint source packages. **No standalone novelty claim is made.** The durable delta is the exact composition of the already audited endpoint pair spectrum, Schlage-Puchta's varying-modulus conductor count, and the weighted Plotkin source-incidence identity.

## Boundaries and falsification tests

- **Exact reciprocal endpoint bias is load-bearing.** The use of `tau=1/2` in `(20)` comes from the exact pair coefficient `1-4/R`. A perturbed endpoint must preserve a growing family of pair modes with a fixed nonzero bias before this argument applies unchanged.
- **A common representative package is load-bearing only for the Plotkin step.** The analytic estimate is applied to individual primitive pair characters of possibly different moduli. The common package is used afterward to realize every pair as a symmetric difference of the same source coordinates and to define the total radical `P`.
- **Cubefree primitive pair conductors are load-bearing for the near-quadratic varying-modulus horizon.** They hold here because minimizing lower-prime products yield odd squarefree primitive real characters, as audited in `MC-301` and `MC-323`.
- **The exponent gap is fixed.** Equation `(20)` is valid for each fixed `delta>0`; the quartic liminf follows by quantifying over all fixed `delta`, not by taking a moving `delta(y)` inside the analytic theorem.
- **Chosen representatives need not be minimal.** This is harmless in the required direction: `mathcal Q(lambda_i+lambda_j)<=m_ij`, so a lower bound for the minimum conductor forces the package pair product to be at least as large.
- **The theorem does not rule out quartic-or-larger packages.** It proves a source-mass floor, not nonexistence of every possible common representation. A mechanism that genuinely pays `P>=y^(4-o(1))`, uses a much larger source-coordinate set, or abandons a common source package is outside this particular no-go.
- **The natural-scale coordinate conclusion depends on the cap `(15)`.** Without it, `(5)` constrains total logarithmic source mass but not the raw coordinate count `n`.
- **No Möbius realization is asserted.** The endpoint remains a conditional candidate geometry. This finding further restricts that candidate; it gives no estimate for the actual Mertens function.
