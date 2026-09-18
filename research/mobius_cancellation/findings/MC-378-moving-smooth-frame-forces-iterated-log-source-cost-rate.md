# MC-378 — Moving smooth frame forces an iterated-log source-cost rate

**Status:** `LITERATURE+DERIVED` · `EXACT-DERIVED` · `FRONTIER-ADVANCE` · `SOURCE-COST` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

Continue the exact endpoint partition and common lower-prime source package of `MC-377`. Thus

\[
\mathcal R_y=D_1\sqcup\cdots\sqcup D_R,
\qquad R=R(y)\to\infty,
\]

has independent endpoint generators represented by lower-prime product sets `V_1,\ldots,V_R`, and

\[
U=\bigcup_{i=1}^R V_i,
\qquad
P=\prod_{p\in U}p
\tag{1}
\]

is the common source radical.

There are absolute constants `C_0,C_1>0` with the following property. Let `A=A(y)>=2` satisfy

\[
A^2=o(R),
\qquad
A\,2^{C_0A}=o(\log\log y).
\tag{2}
\]

Then an exact endpoint cannot satisfy

\[
P\le y^A
\tag{3}
\]

for all sufficiently large `y`. Equivalently, the fixed-`A` conclusion of `MC-377` is uniform throughout every moving range satisfying `(2)`.

A concrete consequence is that for some absolute `c>0`, every sufficiently large exact endpoint obeys

\[
\boxed{
\frac{\log P}{\log y}
\ge
c\min\left\{
\sqrt{\frac{R}{\log(R+2)}},
\ \log\log\log y
\right\}.
}
\tag{4}
\]

The rate is deliberately non-optimized. Its meaning is that the superpolynomial source-cost obstruction of `MC-377` is not merely qualitative: the exponent must grow at least on an explicit iterated-logarithmic/rank-controlled scale.

No estimate for `M(x)` follows.

## 1. Moving `A` costs only `O(A^2)` source dimensions

Assume `(3)`. Put

\[
\delta:=\frac1{16A},
\qquad
\theta:=\frac\delta2=\frac1{32A}.
\tag{5}
\]

Call a source prime rough when `p>y^\theta`. Since `\log P\le A\log y`,

\[
\#\{p\in U:p>y^\theta\}
\le \frac{A}{\theta}
=32A^2.
\tag{6}
\]

The moving smooth-character argument also has a moving finite exceptional set. In the notation of Cochrane--Granville--Zheng, the factorization depth below is `k=O(A)`, and

\[
\Delta(x,0,k)
\]

contains only fixed algebraic factors together with primes below `k+O(1)`. Hence the number of source-prime incidence columns meeting the relevant exceptional integer is `O(A)`.

As in `MC-377`, for each source prime let

\[
c_p=(\mathbf 1_{p\in V_1},\ldots,\mathbf 1_{p\in V_R})\in\mathbb F_2^R.
\]

Intersect the kernels of every rough-source column and every exceptional-source column. The resulting subspace `W` satisfies

\[
\boxed{
\dim W\ge R-C A^2,
\qquad
H:=|W|\ge 2^{R-CA^2}
}
\tag{7}
\]

for an absolute `C`. Every source character indexed by `W`, and every ambient pair modulus appearing in its prime-frame Gram matrix, is then supported only on primes

\[
p\le y^\theta
\tag{8}
\]

and avoids the exceptional primes needed by the smooth-modulus argument. Distinct rows still give nonprincipal off-diagonal pair characters because endpoint-generator independence is unchanged.

The first hypothesis in `(2)` is exactly what preserves an exponentially large frame after this moving codimension loss:

\[
H=2^{(1-o(1))R}.
\tag{9}
\]

## 2. The Cochrane--Granville--Zheng proof is uniform for `A 2^{CA} << log log y`

The fixed-parameter Corollary 2 used in `MC-377` is not enough by itself, because its displayed constant may depend on the fixed smoothness exponent. The required uniformity comes from the parameter dependence exposed in the proof.

Specialize Cochrane--Granville--Zheng Theorem 3 to

\[
f(x)=x,\qquad g(x)=0.
\]

For a differencing depth `k`, their theorem takes

\[
D=2^{k+1},
\qquad
\eta_3=\frac{\varepsilon}{2^{k+3}D}
=\frac{\varepsilon}{2^{2k+4}},
\tag{10}
\]

and requires, among other conditions,

\[
k2^k\ll\log\log Q^*,
\qquad
Q^*\ge(\log Q)^{12D},
\qquad
k<N^{\eta_3}.
\tag{11}
\]

Their Proposition 7 is important here because its iterated-differencing constant remains bounded after the final `2^k`-th root: the displayed constant is `<4` independently of `k`. In the proof of Theorem 3 the remaining `k`-dependence is explicit through `D`, `3^k`, and the hypotheses `(11)`.

Theorem 4 factors a `q^\delta`-smooth modulus using

\[
k<\frac2\delta=32A.
\tag{12}
\]

Its retained factor `Q` is at least a `\delta/2` power of the relevant primitive conductor. In the large-conductor branch used below, therefore,

\[
\log\log Q=\log\log y+O(\log A).
\tag{13}
\]

Consequently the first condition in `(11)` is uniform once

\[
A2^{C A}=o(\log\log y)
\tag{14}
\]

for a sufficiently large absolute `C`. The second and third conditions are then much weaker: `D=2^{O(A)}`, while `\log Q` and the interval length are positive powers of `y` up to the moving `1/A` exponent.

Tracing `(10)` through the `Q>(q')^{\delta/2}` step of Theorem 4 gives a primitive-character power saving of size at least

\[
\sigma_A:=2^{-C_1A}
\tag{15}
\]

for a suitable absolute `C_1`; polynomial factors in `A` are absorbed by increasing `C_1`. This is consistent with the paper's Remark 1, but the present deduction uses the displayed Theorem 3 conditions rather than treating the remark as a black-box uniform statement.

For an imprimitive nonprincipal character, use the same inclusion--exclusion reduction as the proof of their Corollary 2. If `q'` is the primitive conductor and `r` the extra squarefree ambient factor, the loss is at most `\tau(r)`. The classical divisor bound gives, uniformly for `q\le y^A`,

\[
\log\tau(r)
\ll \frac{A\log y}{\log\log y}.
\tag{16}
\]

After enlarging `C_0` relative to `C_1`, the second condition in `(2)` implies

\[
\frac{A}{\log\log y}=o(\sigma_A).
\tag{17}
\]

Thus `(16)` is swallowed by the `y^{-\sigma_A}` power saving. The small-primitive-conductor branch is handled by Pólya--Vinogradov exactly as in Corollary 2; the large-conductor branch invokes the moving Theorem 3/4 estimate above.

We obtain the following uniform specialized consequence: whenever `q\le y^A`, all prime factors of `q` are at most `y^\theta`, the moving exceptional primes have been removed, and an interval `J` has length

\[
|J|\ge y^{1-o(1)},
\]

then every nonprincipal character modulo `q` satisfies, after possibly decreasing `\sigma_A` by an absolute factor,

\[
\boxed{
\left|\sum_{n\in J}\chi(n)\right|
\ll |J|\,y^{-\sigma_A},
\qquad
\sigma_A\ge 2^{-C_1A}.
}
\tag{18}
\]

To check the smoothness/length hypotheses explicitly, if `q\ge |J|` then `(5)`, `(8)` and `|J|\ge y^{1-o(1)}` give

\[
P^+(q)\le y^{\delta/2}<q^\delta,
\]

while

\[
q^{\delta(1+1)}
\le y^{2A\delta}
=y^{1/8}
\ll |J|.
\tag{19}
\]

If `q<|J|`, ordinary Pólya--Vinogradov is already stronger than what the frame argument needs.

## 3. A moving Selberg cutoff preserves the saving

Return to the weighted off-diagonal sum from `MC-377`. Choose

\[
b:=\frac{\sigma_A}{100},
\qquad
B:=y^b.
\tag{20}
\]

Under `(2)`, `\sigma_A\log y\to\infty`, so `B\to\infty` despite `b\to0`. Expanding the Selberg weight `f=(1*g)^2` produces at most `B^2` ordinary character sums, each on an interval of length

\[
Y\ge \frac{2y}{B^2}
\gg y^{1-2b}.
\tag{21}
\]

For pair modulus `q<Y`, Pólya--Vinogradov gives the same strong small-modulus branch as `MC-377`. For `q\ge Y`, `(18)` applies. Therefore every off-diagonal pair in `W` satisfies

\[
\boxed{
|S_{I,J}|
\ll y^{1-c\sigma_A}
}
\tag{22}
\]

for an absolute `c>0`. The factor `B^2=y^{2b}` consumes only a fixed small fraction of the moving exponent.

The diagonal Selberg term can no longer be written as `O_A(1)` after prime-shell normalization. Keeping its moving dependence gives instead

\[
\frac{y/\log B+B^2}{y/\log y}
\ll \frac1b
\ll \sigma_A^{-1}.
\tag{23}
\]

This is the second load-bearing uniformity check in the clue leading to this finding.

## 4. The moving frame upper bound still contradicts rank

Let `V` be the `H\times |\mathcal R_y|` shell-character matrix for rows indexed by `W`, and let

\[
G=|\mathcal R_y|^{-1}VV^*.
\]

Exactly as in `MC-377`, row constancy on the `R` defect cells gives

\[
\operatorname{rank}V\le R,
\qquad
\operatorname{tr}G=H,
\qquad
\lambda_{\max}(G)\ge\frac HR.
\tag{24}
\]

Bombieri's lemma, `(22)`, `(23)`, and `|\mathcal R_y|\asymp y/\log y` give

\[
\boxed{
\lambda_{\max}(G)
\ll
\sigma_A^{-1}
+H y^{-c\sigma_A}\log y.
}
\tag{25}
\]

Under the contradiction assumption `P\le y^A`, source-incidence independence still gives

\[
R\le |U|\le\log_2P\ll A\log y.
\tag{26}
\]

Now divide `(25)` by `H`. By `(7)` and `A^2=o(R)`,

\[
\frac{\sigma_A^{-1}}H=o(R^{-1}),
\tag{27}
\]

because `\log\sigma_A^{-1}=O(A)=o(R)`. Also `(2)`, `(15)`, and `(26)` imply

\[
R\,y^{-c\sigma_A}\log y\to0:
\tag{28}
\]

indeed `\sigma_A\log y` dominates `\log R+\log\log y` by an exponential margin throughout the allowed `A` range. Equations `(24)`--`(28)` give

\[
\frac1R
\ll
\frac{\sigma_A^{-1}}H+y^{-c\sigma_A}\log y
=o(R^{-1}),
\]

a contradiction. This proves the moving statement `(2)`--`(3)`.

## 5. Extracting the explicit source exponent

Let

\[
L_3:=\log\log\log y
\]

and choose a sufficiently small absolute `c_0>0`. Set

\[
A_*(y)
:=c_0\min\left\{
\sqrt{\frac{R}{\log(R+2)}},
L_3
\right\}.
\tag{29}
\]

Both terms in the minimum tend to infinity. Moreover

\[
\frac{A_*^2}{R}
\le \frac{c_0^2}{\log(R+2)}	o0.
\tag{30}
\]

If `c_0` is small enough relative to `C_0`, then

\[
A_*2^{C_0A_*}
\ll
L_3(\log\log y)^\alpha
=o(\log\log y)
\tag{31}
\]

for some fixed `\alpha<1`. Hence `A_*` satisfies `(2)`. Applying the theorem with `A=A_*` excludes `P\le y^{A_*}` and proves `(4)`.

The `\log\log\log y` term comes from the displayed `k2^k` uniformity condition in Cochrane--Granville--Zheng Theorem 3. The rank term comes from the `O(A^2)` source-incidence codimension needed to remove primes above `y^{c/A}`. Neither is asserted to be an arithmetic optimum.

## Prior art and novelty boundary

The analytic input is Todd Cochrane, Andrew Granville and Junren Zheng, *Mixed incomplete character sums of rational functions with smooth moduli*, arXiv:`2601.10927v1` (16 January 2026), retained as `MC-S46`. The load-bearing pieces are Proposition 7, Theorem 3, the factorization in the proof of Theorem 4, and the imprimitive-character reduction in Corollary 2. As of the 18 September 2026 audit, arXiv still exposes only v1.

The paper itself states that its method permits a moving smoothness parameter and records in Remark 1 a broad lower scale for `\delta`; that statement is literature, not a Mathia result. The present proof uses the stricter displayed `k2^k\ll\log\log Q^*` condition from Theorem 3 and therefore obtains only the conservative `\log\log\log y` range needed for the prime-frame transfer.

A targeted fresh search found the established smooth-modulus character-sum literature but no published theorem phrased as the exact endpoint/source-incidence consequence `(4)`. **No standalone novelty claim is made.** The durable Mathia contribution is the audited transfer of explicit moving-parameter dependence through the `MC-377` kernel, Selberg, and frame argument.

## Boundaries and falsification tests

- **The rate is a proof rate, not an asserted optimum.** The `\log\log\log y` ceiling records the conservative Theorem 3 uniformity used here; a sharper reorganization of the smooth-modulus proof could improve it.
- **The rank condition is load-bearing.** If `A^2` is comparable with `R`, killing rough source columns may destroy the exponential row family, and this argument gives no contradiction.
- **The common radical remains load-bearing.** The conclusion concerns the union source cost `P`, not the minimum primitive conductor of every endpoint mode.
- **Imprimitive characters are not silently treated as primitive.** The primitive-conductor split and divisor-loss estimate are needed before the moving character bound is used.
- **The Selberg diagonal grows.** Its normalized cost is `O(\sigma_A^{-1})`; treating it as `O(1)` would invalidate the moving proof.
- **The exceptional integer moves with `A`.** Its source columns are removed explicitly at `O(A)` additional codimension cost.
- **The primary source is manuscript-level evidence.** A material revision of Cochrane--Granville--Zheng's moving-parameter proof would require re-auditing `(18)`.
- **No RH or Möbius bound is imported.** The argument is a source-realizability obstruction inside the exact endpoint branch and yields no estimate for `M(x)` or the zeta zero set.

## Consequence

`MC-377` left open the possibility that the source exponent `\log P/\log y` diverges arbitrarily slowly. This finding excludes that escape at least up to the explicit scale `(4)`. The next source-cost question is no longer whether any rate can be extracted, but whether the `\log\log\log y` limitation is intrinsic to the available smooth-character machinery or can be improved by a factorization/complete-sum argument that avoids the `k2^k` tariff while preserving the moving Selberg frame.