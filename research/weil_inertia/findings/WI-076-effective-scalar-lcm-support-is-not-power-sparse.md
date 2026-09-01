# WI-076 — Bienvenu forces the effective Yang scalar-lcm support to be non-power-sparse

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE + PRIOR-ART-REDIRECTION`. This finding does **not** certify the Yang--Yang one-sided fourth-moment candidate and does not change Mathia's current unconditional simple-critical proportion. It closes the cardinality version of the scalar-modulus escape left open by WI-075: after the actual von-Mangoldt/source weights are imposed, the scalar support is still large. Already on one fixed coprime base pair occurring in the Yang source,

\[
\boxed{\#\mathcal L^{\rm eff}(X)\gg \frac{X}{(\log X)^4}.}
\]

Consequently the effective scalar support cannot satisfy `O(X^{1-delta})` for any fixed `delta>0`. The global two-dimensional lcm-incidence family of WI-071 is power-sparse in its ambient square, but **its nonzero weighted projection to the scalar modulus is not power-sparse**. Thus a scalar sparse-large-sieve strategy cannot obtain its required power-scale localization gain merely from support cardinality. A weighted/additive-energy theorem, cancellation in the scalar weights, or a labelled transform retaining the reduced direction `(r,q)` remains live.

## 1. Exact source object and the fixed-slope subfamily

The pinned public source remains

`JoshuaHKU/zeta-0.7947-reproduction@d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8`, especially `scripts/t2_swaps.py`.

For coprime prime-power bases `(b_1,b_2)`, the exact swapped `S1` geometry is

\[
m'=m-b_1k,\qquad n'=n-b_2k,
\tag{1}
\]

with nonzero contribution only when

\[
\Lambda(m)\Lambda(m-b_1k)\Lambda(n)\Lambda(n-b_2k)>0
\tag{2}
\]

and the source windows, translated windows, nonzero lock and nonzero shift conditions are all satisfied. The physical shifts are

\[
(h_1,h_2)=(b_1k,b_2k),
\]

so because `(b_1,b_2)=1`,

\[
L:=\operatorname{lcm}(|h_1|,|h_2|)=b_1b_2|k|.
\tag{3}
\]

Take one fixed coprime pair that occurs in the source, for example

\[
(b_1,b_2)=(5,7).
\tag{4}
\]

This pair is in every fixed polylogarithmic coefficient range for all sufficiently large `X`, and it is explicitly among the prime-power base values handled by the public `t2_swaps.py` family. On the positive-shift interior used below, (3) becomes the injective map

\[
\boxed{L=35k.}
\tag{5}
\]

Hence a lower bound for the number of source-effective positive `k` values immediately gives the same lower bound for distinct effective scalar moduli.

## 2. WI-050 plus Bienvenu gives positive total mass of order `X^3`

WI-050 reconstructed the unsliced fixed-base source as the four affine-linear forms

\[
\Psi_{b_1,b_2}(m,n,k)
=
\bigl(m,\ m-b_1k,\ n,\ n-b_2k\bigr)
\tag{6}
\]

on a source convex body. It also exhibited a one-sided interior convex subbody `K^*_{b_1,b_2}(X)` avoiding both deleted hyperplanes `k=0` and `j=b_1n-b_2m=0`, with coordinate widths

\[
\asymp \frac{X}{b_2},\qquad
\asymp \frac{X}{b_1},\qquad
\asymp \frac{X}{b_1b_2}.
\tag{7}
\]

For the fixed pair (4), therefore,

\[
\operatorname{Vol}K^*_{5,7}(X)\asymp X^3.
\tag{8}
\]

Pierre-Yves Bienvenu's *A higher-dimensional Siegel--Walfisz theorem*, Acta Arith. 179 (2017), Theorem 1.3, applies to admissible finite-complexity affine-linear systems with fixed or polylogarithmic coefficients on convex bodies of volume `\gg N^d(\log N)^{-A}`. WI-050 checked these hypotheses for the exact Yang system and identified Bienvenu's Euler product with the positive Yang local factor `E_2(b_1,b_2)`.

Applying that established input to the fixed interior body gives

\[
\begin{aligned}
W(X)
&:=\sum_{(m,n,k)\in\mathbf Z^3\cap K^*_{5,7}(X)}
\Lambda(m)\Lambda(m-5k)\Lambda(n)\Lambda(n-7k)\\
&=\operatorname{Vol}K^*_{5,7}(X)\,E_2(5,7)\,(1+o(1)).
\end{aligned}
\tag{9}
\]

Since the local product is nonzero and positive,

\[
\boxed{W(X)\gg X^3.}
\tag{10}
\]

This is an unconditional asymptotic consequence of Bienvenu's theorem on a fixed-coefficient subfamily; it does not assume any pointwise twin-prime or four-prime Hardy--Littlewood conjecture.

## 3. A trivial multiplicity bound converts the first moment into near-linear support

For each positive integer `k`, let

\[
W_k(X)
:=\sum_{(m,n):(m,n,k)\in K^*_{5,7}(X)}
\Lambda(m)\Lambda(m-5k)\Lambda(n)\Lambda(n-7k).
\tag{11}
\]

All terms are nonnegative, and

\[
W(X)=\sum_k W_k(X).
\tag{12}
\]

Every linear form appearing in `K^*_{5,7}(X)` is `O(X)`. Hence for a fixed source constant `C`,

\[
0\le\Lambda(\ell)\le\log(CX)
\tag{13}
\]

for every positive argument occurring in (11). For fixed `k`, both `m` and `n` lie in intervals of length `O(X)`, so the number of lattice pairs in the slice is at most `O(X^2)`. Therefore, uniformly in `k`,

\[
\boxed{W_k(X)\ll X^2(\log X)^4.}
\tag{14}
\]

Define the actual nonzero weighted shift support in this subfamily by

\[
\mathcal K^{\rm eff}_{5,7}(X)
:=\{k>0:W_k(X)>0\}.
\tag{15}
\]

Combining (10), (12), and (14) gives

\[
X^3
\ll W(X)
\le
\#\mathcal K^{\rm eff}_{5,7}(X)\,
O\!\left(X^2(\log X)^4\right),
\]

hence

\[
\boxed{
\#\mathcal K^{\rm eff}_{5,7}(X)
\gg \frac{X}{(\log X)^4}.
}
\tag{16}
\]

This is exactly the multiplicity control missing from the warning in WI-075. A first moment alone would not imply positive-density support, because the mass could concentrate on a sparse set of shifts; the elementary `L^\infty` bound (14) is enough, however, to rule out **power** concentration.

Via the injective scalar projection (5),

\[
\boxed{
\#\mathcal L^{\rm eff}_{5,7}(X)
\gg \frac{X}{(\log X)^4},
\qquad
\mathcal L^{\rm eff}_{5,7}(X)
:=\{35k:k\in\mathcal K^{\rm eff}_{5,7}(X)\}.
}
\tag{17}
\]

The full Yang effective scalar support contains this fixed-base subfamily, so it satisfies the same lower bound.

## 4. Power sparsity is impossible

For every fixed `delta>0`,

\[
\frac{X/(\log X)^4}{X^{1-\delta}}
=
\frac{X^\delta}{(\log X)^4}
\longrightarrow\infty.
\tag{18}
\]

Thus (17) implies

\[
\boxed{
\mathcal L^{\rm eff}(X)
\text{ is not }O(X^{1-\delta})
\text{ for any fixed }\delta>0.
}
\tag{19}
\]

This resolves the support-cardinality uncertainty deliberately left open in WI-075. The actual von-Mangoldt restrictions can delete a logarithmic proportion of candidate scalar moduli, but they cannot make the effective family power-sparse: the published finite-complexity prime-pattern theorem already forces `X^{1-o(1)}` distinct scalar values on one fixed slope.

The conclusion is stronger than the ambient set-theoretic observation `L=rq|k|`. It uses the genuine source weights and windows. It is also weaker than a positive-density theorem: (16) does **not** prove `#K_eff \gg X`, and no such claim is needed for the present barrier.

## 5. Consequence for the sparse scalar-large-sieve route

WI-071 showed that the two-dimensional physical-shift incidence set has only `O(X(log X)^2)` points in an ambient square of area `asymp X^2`, so an ambient two-dimensional prime-pattern estimate would need a power-scale localization gain. WI-075 asked whether projecting to the scalar modulus `L` and then discarding zero-weight values might reveal a genuinely sparse one-dimensional family suitable for sparse-moduli large-sieve technology.

Equation (19) closes the **cardinality** version of that escape. The effective scalar family has counting exponent one. In particular, one cannot obtain a fixed power saving simply by claiming that only `X^{1-delta}` scalar moduli carry Yang weight.

This does **not** rule out the large-sieve direction itself. Baker--Munsch--Shparlinski's large-sieve bounds for sparse scalar sequences depend on additive-energy information, not just on cardinality, and a Yang-specific weighted transform could exploit cancellation or unusually low energy. Likewise, a regrouping by `L` that retains the reduced labels `(r,q)` can still use the polylogarithmic representation multiplicity from WI-075. The surviving targets are therefore

\[
\boxed{
\text{weighted/additive-energy cancellation}
\quad\text{or}\quad
\text{labelled scalar structure},
}
\tag{20}
\]

not power sparsity of the set of nonzero scalar moduli.

## 6. Prior-art and novelty boundary

No novelty is claimed for Bienvenu's theorem, the elementary inequality `Lambda(n)<=log n`, the support estimate `sum a_k <= (#supp a) max a_k` for nonnegative weights, or the observation that `X/log^A X` dominates every `X^{1-delta}`. The published theorem-level input is:

- Pierre-Yves Bienvenu, **A higher-dimensional Siegel--Walfisz theorem**, *Acta Arithmetica* 179 (2017), 79--100, DOI `10.4064/aa8600-10-2016`, arXiv:1607.06625, Theorem 1.3.
- Roger C. Baker, Marc Munsch and Igor E. Shparlinski, **Additive energy and a large sieve inequality for sparse sequences**, *Mathematika* 68 (2022), 362--399, DOI `10.1112/mtk.12140`, arXiv:2103.12659. This is cited only to delimit what remains live: its general sparse-moduli framework uses additive-energy structure, so (19) is not presented as a no-go for every scalar large-sieve argument.

The durable Mathia deduction is the source-interface consequence obtained by combining WI-050's already-audited Yang/Bienvenu asymptotic with WI-075's exact scalar projection: **the same fixed low-coefficient regime that is analytically controllable also certifies enough genuinely nonzero `k` values to forbid any power-sparse effective scalar support.** A bounded search of the current `weil_inertia` corpus found no existing finding making this support lower-bound deduction; WI-075 explicitly left it as an unresolved gate. No priority claim is made.

## 7. Falsification and remaining gates

1. **Source membership.** The argument needs one fixed coprime prime-power pair with nonzero source weight and the macroscopic interior geometry audited in WI-050. The public source explicitly includes such pairs; `(5,7)` is a concrete example.
2. **Bienvenu interface.** If the four-form system or interior convex body failed Bienvenu's hypotheses, (10) would fail. WI-050 checked finite complexity, admissibility, coefficient size, positive local product and source-volume hypotheses; the present deduction uses that established finding rather than silently reasserting a new prime-pattern theorem.
3. **No positive-density claim.** The trivial slice bound yields only `X/(log X)^4`. Improving this to `cX` would require materially stronger multiplicity information and is not asserted.
4. **Energy/weights remain open.** A scalar large-sieve theorem normalized to a weighted energy or exploiting cancellation may still be useful even for an `X^{1-o(1)}` support.
5. **Labelled transforms remain open.** Keeping `(r,q)` attached to `L` is outside the unlabelled cardinality obstruction.
6. **This does not close the Yang covariance clue.** The one-sided fourth-moment route still needs control of the post-local-main covariance in the power-coefficient region isolated by WI-054/WI-055. This finding only prevents one proposed scalar-sparsity shortcut from acquiring a power gain by zero-weight pruning.