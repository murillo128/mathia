# MC-370 — Average Hamming-shell stability needs only an L2 imbalance tariff

**Status:** `EXACT-DERIVED` · `FRONTIER-ADVANCE` · `RESOLUTION-TARIFF` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-369` gave a sharp **statewise** stability condition for the Hamming-shell quotient of the exact prime-shell bias: if

\[
\left\|d-\frac1R\mathbf 1\right\|_1<\frac1R,
\]

then every punctured-cube source state quantizes to its original Hamming level. That worst-case requirement is stronger than what the endpoint energy obstruction actually needs. If one only asks that the quantizer fail on a sufficiently small fraction of source modes, a substantially weaker `L^2` imbalance condition is enough.

Keep the even-rank endpoint notation of `MC-368`–`MC-369`:

\[
X\sim\operatorname{Unif}\!\left(\{\pm1\}^R\setminus\{(+1,\ldots,+1)\}\right),
\qquad
T=\sum_{i=1}^R d_iX_i,
\qquad
 d_i=\frac1R+\varepsilon_i,
\qquad
\sum_i\varepsilon_i=0.
\tag{1}
\]

Let `J={i:X_i=-1}`, `K=|J|`, and let `L` be the index of a nearest balanced Hamming level

\[
b_\ell=1-\frac{2\ell}{R}
\]

to `T`, with any fixed deterministic tie rule. Write

\[
\sigma:=\|\varepsilon\|_2,
\qquad
p_{\rm bad}:=\mathbf P(L\ne K),
\qquad
c_R:=\frac{2^R}{2^R-1}.
\tag{2}
\]

Then the exact perturbation identity from `MC-369`,

\[
T=b_K-2\varepsilon(J),
\qquad
\varepsilon(J)=\sum_{i\in J}\varepsilon_i,
\tag{3}
\]

and Hoeffding's classical inequality give

\[
\boxed{
p_{\rm bad}
\le
2c_R\exp\!\left(-\frac{1}{2R^2\sigma^2}\right)
}
\tag{4}
\]

for `sigma>0`; at exact balance `p_bad=0`.

More importantly, rare shell-crossing errors can increase the **aggregate own-phase predictability** by only a controlled amount. Put

\[
a_R
:=
\frac{2^R-R}{R(2^R-1)}
=\frac1R+O(2^{-R}).
\tag{5}
\]

Then

\[
\boxed{
\frac1R\sum_{i=1}^R
\left\|\mathbf E[X_i\mid L]\right\|_2^2
\le
a_R+2p_{\rm bad}.
}
\tag{6}
\]

The actual endpoint cells have weights `d_i`, so the weighted leakage relevant to the prime-average dephasing problem satisfies

\[
\boxed{
\rho_d^2
:=
\sum_{i=1}^R d_i
\left\|\mathbf E[X_i\mid L]\right\|_2^2
\le
(1+R\sigma)\bigl(a_R+2p_{\rm bad}\bigr).
}
\tag{7}
\]

The `MC-338` Cauchy--Schwarz argument extends verbatim to unequal endpoint-cell weights when its leakage is replaced by `rho_d`. Therefore any coefficient family whose source-cell coefficients are measurable from `L` obeys

\[
\boxed{
\delta(W)
\ge
\left(1-\sqrt{\mathcal E(W)}\,\rho_d\right)_+,
}
\tag{8}
\]

and exact all-mode dephasing requires

\[
\boxed{
\mathcal E(W)\ge\rho_d^{-2}.
}
\tag{9}
\]

Combining `(4)`–`(9)` yields a useful phase boundary. For any fixed `eta>0`, if

\[
\boxed{
\|d-R^{-1}\mathbf1\|_2^2
\le
\frac{1}{2(1+\eta)R^2\log R},
}
\tag{10}
\]

then

\[
p_{\rm bad}
=O(R^{-1-\eta}),
\qquad
\rho_d^2
\le\frac{1+o(1)}R,
\tag{11}
\]

and hence

\[
\boxed{
\mathcal E(W)\ge(1-o(1))R
}
\tag{12}
\]

for exact dephasing through the quantized shell-bias channel.

This is genuinely weaker than the statewise `L^1` admission condition of `MC-369`. For example, with half the coordinates equal to `+a` and half equal to `-a`, choosing

\[
a\asymp\frac{1}{R^{3/2}\sqrt{\log R}}
\]

gives the `L^2` scale in `(10)` while

\[
\|\varepsilon\|_1
\asymp\frac1{\sqrt{R\log R}}
\gg\frac1R.
\tag{13}
\]

Thus many individual source states may cross Hamming boundaries even when the statewise margin has already failed, yet their total source-mode mass is too small to remove the linear dephasing-energy tariff.

The result does **not** show that rational-prime defect counts satisfy `(10)`, and it does not justify the Hamming-shell quotient as the canonical observation architecture. Exact-real access to `T` remains subject to the complete subset-sum side channel of `MC-368`. No estimate for `M(x)` and no zero-free result follows.

## 1. Shell-crossing is a Rademacher-tail event

Under the uniform full sign cube, let `J` be the corresponding uniform random subset of `[R]`. Since `sum_i epsilon_i=0`,

\[
\varepsilon(J)
=\sum_i\varepsilon_i\mathbf1_{i\in J}
=\frac12\sum_i\varepsilon_iY_i,
\tag{14}
\]

where the `Y_i` are independent Rademacher signs.

Adjacent balanced Hamming levels are separated by `2/R`. Therefore a nearest-level quantizer can return `L!=K` only if the perturbation in `(3)` reaches at least the half-gap:

\[
|2\varepsilon(J)|\ge\frac1R,
\qquad\text{hence}\qquad
|\varepsilon(J)|\ge\frac1{2R}.
\tag{15}
\]

Hoeffding's two-sided inequality for independent bounded summands gives

\[
\mathbf P_{\rm cube}
\left(
|\varepsilon(J)|\ge\frac1{2R}
\right)
\le
2\exp\!\left(-\frac1{2R^2\sigma^2}\right).
\tag{16}
\]

The deleted all-`+1` source state corresponds to `J=emptyset`, for which `epsilon(J)=0`, so it never belongs to the event in `(15)`. Passing from the full cube to the punctured cube therefore only multiplies the probability by

\[
c_R=\frac{2^R}{2^R-1},
\]

which proves `(4)`.

This is the precise place where average stability differs from `MC-369`. The statewise theorem controls

\[
\max_J|\varepsilon(J)|=\frac12\|\varepsilon\|_1.
\]

The present theorem instead uses concentration of the same subset sum under the actual uniform source-mode law. Coherent worst-case subsets may exist, but they are harmless for the quadratic endpoint tariff if their total source probability is sufficiently small.

## 2. Rare misquantization can explain only rare slice variance

The main issue is not merely bounding `P(L!=K)`: a rare transcript value could in principle carry disproportionate information about a source coordinate. The fixed-Hamming-slice geometry prevents such a rare set from contributing more than its share of the total quadratic variation, up to an absolute factor.

Fix `K=k` and put

\[
b_k=1-\frac{2k}{R},
\qquad
V:=X-b_k\mathbf1.
\tag{17}
\]

On the `k`-slice,

\[
\sum_iV_i=0
\]

pointwise and

\[
\|V\|_2^2
=R(1-b_k^2)
=:C_k
\tag{18}
\]

is constant. Let

\[
q_k:=\mathbf P(L\ne k\mid K=k).
\]

Consider a refinement of the transcript that reveals the full source vector `X` on the bad event `{L!=k}` and reveals only a single symbol on its complement. Given `K=k`, this refined transcript determines `L`, so conditional-expectation contraction implies that it can only increase the explained `V`-energy.

If `q_k<=1/2`, direct conditioning on the bad set and its complement gives

\[
\mathbf E\left[
\left\|\mathbf E[V\mid K=k,L]\right\|_2^2
\middle|K=k
\right]
\le
\frac{q_k}{1-q_k}C_k
\le2q_kC_k.
\tag{19}
\]

Indeed, if `m_B=E[V|B,K=k]`, the good-set mean is `-q_k m_B/(1-q_k)` because the whole slice mean of `V` is zero, while Jensen gives `||m_B||^2<=C_k`. If `q_k>1/2`, ordinary projection contraction gives the stronger crude bound `<=C_k<=2q_kC_k`. Thus `(19)` holds for every `q_k`.

Now conditioning on the richer pair `(K,L)` can only increase prediction relative to conditioning on `L` alone. Since `1^T E[V|K,L]=0`, the baseline and residual pieces are orthogonal pointwise:

\[
\left\|
\mathbf E[X\mid K,L]
\right\|_2^2
=
Rb_K^2
+
\left\|
\mathbf E[V\mid K,L]
\right\|_2^2.
\tag{20}
\]

Averaging `(19)`–`(20)` over `K`, using `C_K<=R`, and writing `p_bad=E[q_K]`, gives

\[
\sum_i
\left\|\mathbf E[X_i\mid L]\right\|_2^2
\le
R\mathbf E[b_K^2]+2Rp_{\rm bad}.
\tag{21}
\]

The punctured-cube identity already used in `MC-369` is

\[
\mathbf E[b_K^2]
=a_R,
\]

so division by `R` proves `(6)`.

The factor `2` is not asserted sharp. The point is structural: a shell-crossing set of source probability `p_bad` contributes only `O(p_bad)` to the **average squared own-phase predictability**, rather than causing the exact-real discontinuity of `MC-368`.

## 3. Unequal endpoint masses require a weighted leakage, not equal-cell bookkeeping

`MC-338` stated its leakage-energy inequality for equally populated source cells. The endpoint partition here has actual proportions `d_i`, so it is useful to record the exact weighted form rather than silently importing equal-cell notation.

Let `D_i` be the endpoint cells, `|D_i|/N=d_i`, and for a coefficient matrix `W` define the cell average

\[
g_i(a):=\frac1{|D_i|}\sum_{r\in D_i}w_{a,r}.
\tag{22}
\]

If coefficients in cell `i` are measurable from the quantized observation `L`, then `g_i in L^2(sigma(L))`. The normalized endpoint output and coefficient energy satisfy

\[
F_W(a)=\sum_i d_iX_i(a)g_i(a),
\tag{23}
\]

and Jensen gives

\[
\sum_i d_i\|g_i\|_2^2
\le
\mathcal E(W).
\tag{24}
\]

Taking the source-mode mean in `(23)` and applying Cauchy--Schwarz in the weighted `d_i` measure gives

\[
|\mathbf E F_W|
\le
\sqrt{\mathcal E(W)}
\left(
\sum_i d_i
\|\mathbf E[X_i\mid L]\|_2^2
\right)^{1/2}
=
\sqrt{\mathcal E(W)}\,\rho_d.
\tag{25}
\]

If `delta(W)=||F_W-1||_2`, then `|E F_W|>=1-delta(W)`, proving `(8)`–`(9)`.

To connect the weighted leakage to `(6)`, note that

\[
d_{\max}
\le\frac1R+\|\varepsilon\|_\infty
\le\frac1R+\sigma.
\tag{26}
\]

Hence

\[
\rho_d^2
\le
d_{\max}
\sum_i\|\mathbf E[X_i\mid L]\|_2^2
\le
(1+R\sigma)(a_R+2p_{\rm bad}),
\]

which is `(7)`.

This weighted extension also clarifies why exact statewise collapse in `MC-369` restored the equal-balance tariff despite unequal prime counts: once `L=K` identically, every coordinate has the same conditional predictability `a_R`, so `sum_i d_i a_R=a_R` exactly.

## 4. The logarithmic L2 window restores the linear energy tariff

Assume `(10)` for fixed `eta>0`. Then

\[
\frac{1}{2R^2\sigma^2}
\ge
(1+\eta)\log R,
\]

so `(4)` gives

\[
p_{\rm bad}
\le2c_RR^{-1-\eta}.
\tag{27}
\]

Also

\[
R\sigma
\le
\frac1{\sqrt{2(1+\eta)\log R}}
=o(1).
\tag{28}
\]

Combining `(5)`, `(7)`, `(27)` and `(28)` yields

\[
\rho_d^2
\le
(1+o(1))
\left(
\frac1R+O(R^{-1-\eta})
\right)
=
\frac{1+o(1)}R.
\tag{29}
\]

Equation `(9)` then proves `(12)`.

The scale comparison with `MC-369` is substantial. Worst-case statewise decoding demanded `||epsilon||_1<1/R`. The average-energy result tolerates diffuse errors of total variation much larger than this. For the balanced-sign example following `(12)`, Cauchy--Schwarz is essentially saturated and `(13)` exceeds `1/R` by a factor `asymp sqrt(R/log R)`.

This does not make the arithmetic step easy: at the critical endpoint rank `R asy log log y`, condition `(10)` asks for a quantitative mean-square equidistribution of the `R` defect-cell masses on a scale roughly

\[
\|d-R^{-1}\mathbf1\|_2
\lesssim
\frac1{R\sqrt{\log R}}.
\]

But it replaces the **uniform over all subsets** `L^1` admission test by an average-source `L^2` test with an explicit concentration tariff. That is a materially different arithmetic target.

## 5. Prior art and novelty boundary

The probability input is classical. Wassily Hoeffding, *Probability Inequalities for Sums of Bounded Random Variables*, Journal of the American Statistical Association **58** (1963), no. 301, 13–30, DOI `10.1080/01621459.1963.10500830`, proves the bounded-independent-summand tail inequality specialized in `(16)`. The subset-sum/Hamming-shell context remains within the classical Littlewood--Offord landscape already audited in `MC-369` through Tao--Vu, *Additive Combinatorics*, Chapter 7.

The Hilbert-space input in Section 2 is only conditional expectation as orthogonal projection plus the law of total variance/explained variance; Section 3 is the weighted Cauchy--Schwarz form of the already-audited `MC-338` mechanism. A targeted search on 18 September 2026 for Hamming-shell quantization, weighted Rademacher subset sums, conditional coordinate predictability, and rare shell-crossing errors located the classical concentration ingredients but no source stating the endpoint-specific composition `(4)`–`(12)`.

**No standalone novelty claim is made.** The durable delta is the exact composition relevant to the current arithmetic endpoint: subgaussian control of finite-resolution shell errors, a quadratic leakage bound for rare misquantization, and the resulting `L^2` imbalance scale sufficient to preserve the linear dephasing-energy obstruction.

## Boundaries and falsification tests

- **Finite-resolution observation is still load-bearing.** The theorem applies to the nearest-Hamming-level transcript `L` (or a coarsening). If coefficients see exact `T`, `MC-368` still permits complete source recovery from arbitrarily tiny imbalance.
- **The result is average, not statewise.** Equation `(10)` does not imply `L=K` for every source state. Rare coherent subsets can cross boundaries; the theorem proves only that their aggregate quadratic predictability cost is small.
- **Uniform punctured-cube source law is load-bearing.** Hoeffding is applied to a uniform random subset before deleting the empty subset. A differently weighted source-mode ensemble needs its own concentration estimate.
- **The weighted leakage is necessary for unequal cells.** Replacing `rho_d^2` by an unweighted average without controlling `d_max` would not justify the prime-average energy conclusion.
- **The logarithmic `L^2` scale is sufficient, not claimed sharp.** Better anti-concentration or use of the actual imbalance profile may improve `(10)`. Conversely a single coordinate perturbation of size comparable to `1/R` gives a constant shell-crossing probability, so no theorem depending only on `||epsilon||_2` can ignore the `1/R` geometric scale.
- **Arithmetic equidistribution remains missing.** Nothing here proves `(10)` for the actual Legendre defect partition of `MC-296`; establishing or refuting that mean-square cell-balance estimate is now a concrete arithmetic frontier.
- **Canonical resolution remains missing.** The theorem prices what happens *if* the coefficient architecture observes only the Hamming-shell quotient. It does not prove that such coarsening is forced by a natural analytic construction.
- **No Mertens consequence.** This is an endpoint admission theorem, not an estimate for `M(x)` and not a zero-free-region argument.

## Consequence for the research line

The finite-resolution branch no longer requires the worst-case `L^1` balance condition of `MC-369` in order to retain a strong endpoint obstruction. For quadratic coefficient energy, it is enough that the actual defect-cell distribution be `L^2`-close to uniform on the subgaussian scale `(10)`: shell-crossing then occurs on only `O(R^{-1-eta})` of source modes, aggregate own-phase leakage stays `(1+o(1))/R`, and exact dephasing still costs `(1-o(1))R` normalized energy.

The surviving arithmetic question is therefore sharper and potentially more tractable: determine whether the actual endpoint partition can satisfy a mean-square cell-imbalance bound near `1/(R^2 log R)` in squared `L^2` norm, and separately justify a canonical observation resolution at the Hamming-shell scale. Failure of either condition returns to the exact-real side channel; success of both preserves the linear energy barrier without demanding statewise equal-cell decoding.