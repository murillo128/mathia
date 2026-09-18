# MC-372 — Central Hamming bias energy hits the quadratic conductor boundary

**Status:** `EXACT-DERIVED` · `LITERATURE+DERIVED` · `FRONTIER-ADVANCE` · `BALANCE-CONDUCTOR-DICHOTOMY` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

Continue the exact endpoint partition of `MC-296` and the unequal-defect setup of `MC-368`–`MC-371`. Let

\[
\lambda_1,\ldots,\lambda_R
\]

be linearly independent shell functionals with endpoint-cell weights

\[
d_i>0,
\qquad
\sum_{i=1}^R d_i=1,
\qquad
\lambda_I:=\sum_{i\in I}\lambda_i,
\qquad
 d(I):=\sum_{i\in I}d_i.
\]

The exact partition identity is

\[
x_{\lambda_I}
=(-1)^{|I|}\bigl(1-2d(I)\bigr).
\tag{1}
\]

Put

\[
\varepsilon_i:=d_i-\frac1R,
\qquad
\Delta_2
:=\sum_{i=1}^R\varepsilon_i^2
=\left\|d-\frac1R\mathbf1\right\|_2^2.
\tag{2}
\]

For every Hamming layer `0 <= k <= R`, define its normalized shell-bias energy

\[
A_k
:=
\binom Rk^{-1}
\sum_{|I|=k}|x_{\lambda_I}|^2.
\tag{3}
\]

Then one has the exact finite identity

\[
\boxed{
A_k
=
\left(1-\frac{2k}{R}\right)^2
+
\frac{4k(R-k)}{R(R-1)}\,\Delta_2.
}
\tag{4}
\]

In particular, when `R` is even, the middle Hamming layer removes the balanced baseline completely:

\[
\boxed{
A_{R/2}
=
\frac{R}{R-1}\,\Delta_2.
}
\tag{5}
\]

Thus the middle-layer character family is an **exact spectral meter for the endpoint `L^2` defect imbalance** that controls the average Hamming-quantization tariff in `MC-370`. No reconstruction or approximation is needed: the average squared prime-shell bias on `|I|=R/2` is precisely the missing `L^2` quantity, up to the factor `R/(R-1)`.

The already-audited varying-modulus prime Halász--Montgomery estimate of `MC-323` now yields a sharp balance-versus-conductor dichotomy. Fix `delta_0 in (0,2)` and let

\[
\mathcal C_R
:=\left\{I\subseteq[R]:|I|=\frac R2\right\},
\qquad
m_R:=|\mathcal C_R|=\binom R{R/2}.
\tag{6}
\]

For each nonempty `I`, let `\mathcal Q(\lambda_I)` be the minimum primitive lower-prime source conductor from the source-character dictionary of `MC-301`–`MC-323`, and put

\[
\theta_{\delta_0}
:=
\frac1{m_R}
\#\left\{
I\in\mathcal C_R:
\mathcal Q(\lambda_I)>y^{2-\delta_0}
\right\}.
\tag{7}
\]

Then there are constants `c_delta0,C_delta0>0`, inherited from `MC-323`, such that

\[
\boxed{
\frac{R}{R-1}\Delta_2
\le
\theta_{\delta_0}
+
\frac{C_{\delta_0}}{m_R}
+
C_{\delta_0}y^{-c_{\delta_0}}\log y.
}
\tag{8}
\]

Equivalently,

\[
\boxed{
\theta_{\delta_0}
\ge
\frac{R}{R-1}\Delta_2
-
\frac{C_{\delta_0}}{m_R}
-
C_{\delta_0}y^{-c_{\delta_0}}\log y.
}
\tag{9}
\]

So any endpoint `L^2` imbalance that survives above the analytic error floor must be paid for by a quantitatively comparable fraction of **middle-layer modes whose primitive conductors reach the quadratic boundary**. Conversely, if all but `o(1/(R^2\log R))` of the middle layer have fixed-subquadratic primitive conductor and `R=y^{o(1)}`, then `(8)` forces

\[
\Delta_2=o\!\left(\frac1{R^2\log R}\right),
\tag{10}
\]

which is more than enough for the `MC-370` average Hamming-shell stability condition.

The common source package explains why this does not currently close the endpoint. Continue the fixed representatives `V_i`, source radical

\[
P=\prod_{p\in U}p,
\]

and source-incidence weights of `MC-371`. For a source prime `p`, write

\[
a_p:=\#\{i:p\in V_i\},
\qquad
\nu_p:=\frac{\log p}{\log P},
\qquad
\mathcal B_R
:=\sum_{p\in U}\nu_p
\left(\frac{2a_p-R}{R}\right)^2.
\tag{11}
\]

For a middle-layer subset `I`, let

\[
V_I:=\mathop{\triangle}_{i\in I}V_i,
\qquad
m_I:=\prod_{p\in V_I}p.
\tag{12}
\]

Then the average logarithmic package cost satisfies the exact estimate

\[
\boxed{
\left|
\frac{1}{m_R\log P}
\sum_{I\in\mathcal C_R}\log m_I
-\frac12
\right|
\le
\frac{1}{2(R-1)}+rac{\mathcal B_R}{2}.
}
\tag{13}
\]

Therefore the quartic saturation regime of `MC-371`,

\[
\frac{\log P}{\log y}=4+o(1),
\qquad
\mathcal B_R=o(1),
\tag{14}
\]

forces

\[
\boxed{
\frac1{m_R}
\sum_{I\in\mathcal C_R}\log m_I
=(2+o(1))\log y.
}
\tag{15}
\]

The same central Hamming layer that measures defect imbalance exactly therefore lands, in the natural quartic-saturated source package, at **average package cost `y^(2+o(1))`**: precisely the individual-conductor boundary where the fixed-gap theorem of `MC-323` stops.

More quantitatively, for every fixed `delta_0 in (0,2)`, `(14)`–`(15)` and the trivial bound `m_I<=P=y^(4+o(1))` imply

\[
\boxed{
\frac1{m_R}
\#\left\{
I\in\mathcal C_R:
 m_I>y^{2-\delta_0}
\right\}
\ge
\frac{\delta_0}{2+\delta_0}-o(1).
}
\tag{16}
\]

This is a statement about the chosen package representatives, not minimum primitive conductors. A high `m_I` can still admit a cheaper alternative representative. That distinction is exactly the remaining escape.

Together `(5)`, `(8)`, and `(15)` identify a concrete post-`MC-371` bottleneck rather than merely restating that defect balance is missing: **the endpoint `L^2` defect is visible in one canonical Fourier layer, and current prime-family technology would control it if that layer sat a fixed power below quadratic conductor, while quartic source saturation places the natural package at the quadratic boundary itself.**

No estimate for `M(x)` follows.

## 1. Fixed-weight bias energy is a finite-population variance identity

Let `I` be uniformly distributed over the `k`-subsets of `[R]`, and put

\[
E_I:=\sum_{i\in I}\varepsilon_i.
\]

Because `sum_i epsilon_i=0`,

\[
\mathbf E E_I=0.
\tag{17}
\]

The inclusion probabilities are

\[
\mathbf P(i\in I)=\frac{k}{R},
\qquad
\mathbf P(i,j\in I)=\frac{k(k-1)}{R(R-1)}
\quad(i\ne j).
\tag{18}
\]

Also

\[
\sum_{i<j}\varepsilon_i\varepsilon_j
=-\frac12\sum_i\varepsilon_i^2
=-\frac12\Delta_2.
\tag{19}
\]

Hence

\[
\begin{aligned}
\mathbf E E_I^2
&=
\frac{k}{R}\Delta_2
+
2\frac{k(k-1)}{R(R-1)}
\sum_{i<j}\varepsilon_i\varepsilon_j\\
&=
\frac{k(R-k)}{R(R-1)}\Delta_2.
\end{aligned}
\tag{20}
\]

On the `k`-layer,

\[
d(I)=\frac{k}{R}+E_I,
\]

so `(1)` gives

\[
|x_{\lambda_I}|^2
=
\left(1-\frac{2k}{R}-2E_I\right)^2.
\tag{21}
\]

Averaging, using `(17)` and `(20)`, proves `(4)`. At `k=R/2`, the deterministic first term vanishes and `(5)` follows.

The mechanism is the standard finite-population correction for sampling without replacement, specialized to the endpoint weights. A targeted prior-art check found no reason to treat `(20)` as new probability theory. The durable delta is its composition with the exact endpoint Fourier profile and the source-conductor frontier, not the variance formula itself.

## 2. Prime Halász--Montgomery turns middle-layer energy into a conductor dichotomy

Split the middle layer as

\[
\mathcal C_R=\mathcal L\sqcup\mathcal H,
\]

where

\[
\mathcal L
=\{I:\mathcal Q(\lambda_I)\le y^{2-\delta_0}\},
\qquad
\mathcal H
=\mathcal C_R\setminus\mathcal L.
\tag{22}
\]

Independence of the `lambda_i` makes the `lambda_I` distinct and nonzero on this layer. By the already-audited source-character dictionary, their minimizing representatives give distinct primitive real characters of odd squarefree conductor, and their normalized dyadic prime-shell biases are exactly `x_(lambda_I)`.

Equation `(5)` of `MC-323` therefore applies to the low-conductor family `\mathcal L`:

\[
\sum_{I\in\mathcal L}|x_{\lambda_I}|^2
\le
C_{\delta_0}
\left(
1+|\mathcal L|y^{-c_{\delta_0}}\log y
\right).
\tag{23}
\]

For the high-conductor complement one only needs the trivial bound

\[
\sum_{I\in\mathcal H}|x_{\lambda_I}|^2
\le|\mathcal H|.
\tag{24}
\]

Adding `(23)` and `(24)`, using `|L|<=m_R`, dividing by `m_R`, and inserting `(5)` gives `(8)`. Rearrangement gives `(9)`.

Since

\[
m_R
=2^R\sqrt{\frac{2}{\pi R}}(1+o(1)),
\tag{25}
\]

one has `m_R^(-1)=o(1/(R^2 log R))` whenever `R->infinity`. For each fixed `delta_0`, the term `y^(-c_delta0) log y` is also `o(1/(R^2 log R))` when `R=y^(o(1))`. This proves `(10)` under the stated high-conductor-fraction hypothesis.

The significance is asymmetric. `MC-323` does not need to estimate every middle-layer mode separately: its `ell^2` family estimate matches exactly the `ell^2` defect quantity in `(5)`. The obstruction is not a mismatch of norms. It is that the relevant primitive conductors are not currently known to stay inside the theorem's fixed-subquadratic range.

## 3. The central source-package layer is asymptotically half loaded

For a fixed source prime `p`, let

\[
S_p:=\{i:p\in V_i\},
\qquad |S_p|=a_p.
\]

A middle-layer package representative contains `p` exactly when

\[
|I\cap S_p|\ \text{is odd}.
\]

Thus the fraction of middle-layer sets containing `p` is

\[
\pi_R(a_p)
=
\frac12\left(1-\kappa_{R/2}(a_p;R)\right),
\tag{26}
\]

where

\[
\kappa_{R/2}(a;R)
:=\frac{K_{R/2}(a;R)}{\binom R{R/2}}
\]

is the normalized binary Krawtchouk multiplier already used in `MC-265` and `MC-325`.

Krawtchouk duality and the central evaluation from `MC-265` give

\[
\kappa_{R/2}(a;R)
=0
\quad\text{for odd }a,
\tag{27}
\]

and for `a=2j`,

\[
\kappa_{R/2}(2j;R)
=(-1)^j
\frac{\binom{R/2}{j}}{\binom R{2j}}.
\tag{28}
\]

For `1<=a<=R-1`,

\[
\boxed{
|\kappa_{R/2}(a;R)|\le\frac1{R-1}.
}
\tag{29}
\]

Indeed the even ratio in `(28)` equals `1/(R-1)` at `j=1` and `j=R/2-1`; the ratio of consecutive magnitudes is

\[
\frac{2j+1}{R-2j-1},
\]

so the extrema on the interior occur at those endpoints. Odd `a` vanish identically.

The only nonzero source column not covered by `(29)` is the universal column `a=R`. Its logarithmic source-mass proportion is at most `\mathcal B_R`, because such a column contributes exactly `nu_p` to `(11)`. Therefore, averaging `(26)` with weights `nu_p` gives

\[
\left|
\sum_{p\in U}\nu_p\pi_R(a_p)-\frac12
\right|
\le
\frac1{2(R-1)}+rac{\mathcal B_R}{2}.
\tag{30}
\]

Finally, double-counting prime incidences over the middle layer gives

\[
\frac1{m_R}
\sum_{I\in\mathcal C_R}\log m_I
=
\log P
\sum_{p\in U}\nu_p\pi_R(a_p).
\tag{31}
\]

Equations `(30)`–`(31)` prove `(13)`, and `(14)` then gives `(15)`.

To prove `(16)`, let `q_R` be the proportion of middle-layer package representatives with `m_I>y^(2-delta_0)`. The low part contributes at most `(2-delta_0)log y` per mode, while every high mode satisfies `log m_I<=log P=(4+o(1))log y`. Hence `(15)` implies

\[
2+o(1)
\le
(1-q_R)(2-\delta_0)
+q_R(4+o(1)),
\]

and rearranging gives `(16)`.

## 4. Prior art and novelty boundary

No novelty is claimed for sampling-without-replacement variance, Krawtchouk duality, central Krawtchouk evaluations, or prime Halász--Montgomery. The finite-population variance identity behind `(4)` is standard. The Krawtchouk machinery in `(26)`–`(29)` was already audited in `MC-265` and `MC-325`. The varying-modulus prime-family estimate used in `(23)` is exactly the Schlage-Puchta/Klurman--Mangerel--Teräväinen input already audited in `MC-323` and `MC-S45`.

A targeted external search for the fixed-size sampling identity and its Krawtchouk formulation found only the standard finite-population-correction / hypergeometric framework; no novelty claim is made for either component.

The durable Mathia contribution is the composition at the current endpoint frontier: `(5)` identifies the middle Hamming bias energy with the precise `L^2` imbalance required by `MC-370`; `(8)` converts that imbalance into a quantitative fixed-subquadratic-conductor exception fraction using the already available prime-family theorem; and `(13)`–`(16)` show that quartic source saturation puts the natural package for the same modes exactly at average quadratic cost. This identifies the quadratic conductor boundary, rather than an unspecified missing balance theorem, as the next analytic interface.

## 5. Boundaries and falsification tests

- **The exact endpoint partition is load-bearing.** Equation `(1)` comes from the one-defect partition structure. A nearby endpoint law with overlapping defect cells has a different Fourier profile and need not satisfy `(4)`.
- **Even rank is load-bearing only for the exact middle-layer specialization.** The all-layer identity `(4)` holds for every `R` and `k`; `(5)`–`(16)` use `R` even so that `k=R/2` is an actual Hamming layer.
- **The exponent gap in `MC-323` is fixed.** Equations `(8)`–`(10)` hold for each fixed `delta_0>0`. They do not extend the varying-modulus theorem uniformly to `delta_0=delta_0(y)->0`, and they do not cross the quadratic conductor line.
- **Primitive conductor and package cost are different.** Equation `(8)` concerns the minimum primitive conductor `Q(lambda_I)`. Equations `(13)`–`(16)` concern one chosen symmetric-difference package `m_I`. A package with cost above `y^(2-delta_0)` may still have a cheaper alternative representative. Treating `(16)` as a lower bound for `theta_delta0` would be invalid.
- **Average package cost is not concentration.** Equation `(15)` alone does not say most `m_I` equal `y^(2+o(1))`; `(16)` is the only distributional conclusion drawn here and uses the independent ceiling `m_I<=P`.
- **The analytic noise floor matters.** If `Delta_2` is below `m_R^(-1)+y^(-c_delta0)log y`, `(9)` need not force any high-conductor middle mode.
- **The exact-real side channel remains.** Even if `(10)` admits the Hamming-shell quantizer of `MC-370`, exact access to the real bias statistic still has the subset-sum decoding escape of `MC-368`.
- **No Mertens or zero-free consequence.** The result prices one finite endpoint architecture. It neither constructs the endpoint nor turns its dephasing tariff into a bound for `M(x)`.

An audit can falsify the finding at three concrete points: failure of the finite-population identity `(4)`, failure of the source-character dictionary needed for `(23)`, or a counterexample to the interior central-Krawtchouk bound `(29)`. Each is an exact finite statement apart from the already-canonical analytic estimate inherited from `MC-323`.

## Consequence for the research line

`MC-371` left an explicit gap: quartic source-incidence balance `B_R->0` does not imply the endpoint-cell `L^2` balance required by `MC-370`. The present result locates the missing bridge more sharply.

The endpoint-cell imbalance is already encoded exactly in the middle Hamming layer. If almost all of those characters had primitive conductor a fixed power below `y^2`, existing prime Halász--Montgomery energy would force the required balance. But the quartic-saturated source package places that same middle layer at average cost `y^(2+o(1))`, and a positive fraction of the chosen package representatives lies above every fixed subquadratic cutoff.

The next useful analytic target is therefore specific: either prove that most middle-layer functionals admit **alternative primitive representatives** genuinely below the quadratic package scale, or strengthen the prime-family energy estimate to exploit the smooth/shared source architecture at the **quadratic boundary itself**. Another source-incidence average or another sparse fixed-bias Hamming layer will not address the norm that `MC-370 actually needs.