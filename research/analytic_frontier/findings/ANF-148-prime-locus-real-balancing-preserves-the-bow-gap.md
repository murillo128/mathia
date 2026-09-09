# ANF-148 — prime-locus real balancing preserves the bow gap

**Status:** `EXACT-DERIVED + PRIME-LOCUS-MATCHED-CONTROL + EXACT-TWIST + DIAGONAL-MATCHED + NEGATIVE/OBSTRUCTION + SOURCE-SPECIFIC-GATE`. `ANF-147` shows that real coefficients and the exact logarithmic carrier do not close the factor-`K` bow coherence gap, but its balancing vector is placed on an arbitrary positive-density interval and therefore leaves a stronger source objection: the load-bearing diagonal of `Lambda-Lambda^sharp` is concentrated on the actual primes, whose locations are arithmetically rigid and sparse. That objection still does not recover coefficient-general coercivity. For every prescribed real twist `U`, one can place real coefficients on a fixed positive fraction of the **actual primes** in the full-multiplicity bow interior, with pointwise size `O(log X)` and exact moving diagonal `(1+o(1))XK log X`, while every length-`K` moving sum is only a two-block boundary term. The resulting variance is `O(X log^2 X)=o(XK log X)`. With exactly the same prime support and pointwise magnitudes, another real sign assignment has variance at least the diagonal. Thus prime locations, prime-density sparsity, real coefficients, the exact carrier, coefficient-size scale, and the correct prime diagonal still leave the full bow coherence ambiguity. The next source theorem must use the **actual amplitude/sign law** of `Lambda-Lambda^sharp` (and/or its coupling to the rough composite part), not merely the fact that the diagonal lives on primes.

## 1. Group the actual bulk primes into exact real-balanced blocks

Let

\[
K=X^{1-2\epsilon+o(1)},
\qquad 0<\epsilon<\frac14,
\tag{1}
\]

and let `U` be an arbitrary prescribed real number; the intended bow specialization is `U asymp X^2`. As in `ANF-146`--`ANF-147`, write

\[
(A_{X,K}b)_j:=\sum_{r=1}^{K}b_{j+r},
\qquad X\le j<2X,
\tag{2}
\]

with the harmless integer convention for `X,K`. The coefficient sites

\[
X+K\le n\le2X
\tag{3}
\]

have exact moving multiplicity `K`.

Let

\[
p_1<p_2<\cdots<p_M
\tag{4}
\]

be the primes in (3). The prime number theorem and the trivial removal of the first `K=o(X/log X)` integers give

\[
\boxed{M=(1+o(1))\frac{X}{\log X}.}
\tag{5}
\]

Put

\[
B:=\left\lfloor\frac M3\right\rfloor.
\tag{6}
\]

For every `0<=q<B`, consider the three **actual prime sites**

\[
T_q:=\{p_{3q+1},p_{3q+2},p_{3q+3}\}
\tag{7}
\]

and their exact logarithmic carrier phases

\[
z_p:=p^{-iU},\qquad |z_p|=1.
\tag{8}
\]

Identifying `C` with `R^2`, the three vectors `z_p` are real-linearly dependent. Hence there is a nonzero real vector

\[
c^{(q)}=(c_1^{(q)},c_2^{(q)},c_3^{(q)})\in\mathbb R^3
\tag{9}
\]

such that

\[
\sum_{r=1}^{3}c_r^{(q)}z_{p_{3q+r}}=0.
\tag{10}
\]

Normalize it by `||c^(q)||_2=1`. Then

\[
|c_r^{(q)}|\le1,
\qquad
\sum_{r=1}^{3}|c_r^{(q)}|\le\sqrt3.
\tag{11}
\]

A nonzero relation among unit complex numbers cannot use only one site, so every block uses at least two primes.

Choose

\[
\lambda:=\sqrt3\log X
\tag{12}
\]

and define real coefficients supported only on these prime triples by

\[
a_{p_{3q+r}}:=\lambda c_r^{(q)},
\qquad
b_n:=a_n n^{-iU},
\tag{13}
\]

with `a_n=0` elsewhere. Thus

\[
\boxed{|a_n|\le\sqrt3\log X=O(\log X),}
\tag{14}
\]

which is on the same pointwise scale as the prime part of the actual residual. The support contains at least `2B=(2/3+o(1))X/log X` actual primes and no composite sites.

## 2. Prime gaps do not hurt: every moving sum is still only a two-block boundary

The primes in a triple need not be consecutive integers, and their gaps can be irregular. That does not affect the cancellation mechanism. Insert a cut immediately before `p_{3q+1}` for each `q>0`, thereby partitioning the integer span of the selected primes into consecutive blocks, each of whose nonzero coefficients are exactly one triple (7). By (10), every complete block has twisted sum zero.

A length-`K` interval is itself contiguous. Its intersection with this block partition consists of complete blocks plus at most one partial block at each endpoint. All complete blocks disappear exactly. Each partial block contributes at most

\[
\lambda\sum_{r=1}^{3}|c_r^{(q)}|
\le\sqrt3\lambda.
\tag{15}
\]

Therefore, **uniformly in every starting point and in the prescribed twist `U`**,

\[
\boxed{
\left|\sum_{j<n\le j+K}a_n n^{-iU}\right|
\le2\sqrt3\lambda
=6\log X.
}
\tag{16}
\]

The exact moving variance consequently obeys

\[
\boxed{
V_{X,K}(b)
:=\sum_{j=X}^{2X-1}
\left|\sum_{j<n\le j+K}b_n\right|^2
\le12\lambda^2X
=36X\log^2X.
}
\tag{17}
\]

No bound on prime gaps, no equidistribution of the carrier on the primes, and no Taylor approximation to `log n` enters. The coefficient relation is chosen directly against the exact phases at the actual prime sites.

## 3. The same construction carries the full bow prime diagonal

Every selected prime lies in the full-multiplicity interior (3). Therefore the exact moving diagonal is

\[
\begin{aligned}
D_{X,K}(b)
&:=\sum_{j=X}^{2X-1}\sum_{j<n\le j+K}|b_n|^2\\
&=K\sum_n|a_n|^2\\
&=K\lambda^2\sum_{q=0}^{B-1}\|c^{(q)}\|_2^2.
\end{aligned}
\tag{18}
\]

Using (5)--(6) and `lambda^2=3 log^2 X`,

\[
\boxed{
D_{X,K}(b)
=K\lambda^2B
=(1+o(1))XK\log X.
}
\tag{19}
\]

This is exactly the bow diagonal scale isolated in `ANF-102` and `ANF-145`. In particular the synthetic diagonal is not manufactured from a dense sea of small coefficients: it is carried on `asymp X/log X` **actual prime positions**, with the natural `log X` coefficient scale.

Combining (17) and (19),

\[
\boxed{
\frac{V_{X,K}(b)}{D_{X,K}(b)}
\le(36+o(1))\frac{\log X}{K}
=o(1).
}
\tag{20}
\]

Thus the exact prime locus can support a matched control whose moving variance is smaller than its prime-scale diagonal by essentially the entire short-interval factor, up to one logarithm. The irregular arithmetic spacing of the primes does not by itself restore the missing coercivity because the block argument is insensitive to the physical lengths of complete zero-sum blocks.

## 4. The same prime support and magnitudes also admit diagonal-scale energy

As in `ANF-147`, freeze the exact magnitudes

\[
u_n:=|a_n|
\tag{21}
\]

and the exact prime support from (13). For independent Rademacher signs `varepsilon_n`, put

\[
a_n^{(\varepsilon)}:=\varepsilon_nu_n,
\qquad
b_n^{(\varepsilon)}:=a_n^{(\varepsilon)}n^{-iU}.
\tag{22}
\]

For each fixed moving window, random-sign orthogonality kills every cross term, so after summing over windows,

\[
\boxed{
\mathbb E_\varepsilon V_{X,K}(b^{(\varepsilon)})
=D_{X,K}(b).
}
\tag{23}
\]

Hence some deterministic real sign assignment satisfies

\[
\boxed{
V_{X,K}(b^{(\varepsilon)})
\ge D_{X,K}(b)
=(1+o(1))XK\log X.
}
\tag{24}
\]

The low- and high-energy controls therefore have exactly the same prescribed logarithmic carrier, actual-prime support, pointwise coefficient magnitudes, real coefficient class, and moving diagonal. Their variances differ by a factor tending to infinity at least like `K/log X`.

This is a strictly more source-shaped obstruction than `ANF-147`: the balancing freedom no longer comes from choosing an arbitrary dense support. It survives after the coefficient locations are confined to the same sparse arithmetic set that carries the leading `Lambda^2` diagonal.

## 5. What this does and does not eliminate

The construction does **not** model the full residual `Lambda-Lambda^sharp`. On primes `p>R`, the actual coefficient is

\[
\Lambda(p)-\Lambda^\sharp(p)
=\log p-c_R>0,
\tag{25}
\]

so its sign is fixed and its magnitude is essentially prescribed. The synthetic control (13) instead chooses real signs and relative amplitudes after `U` is known. It also sets the rough-composite part of the residual to zero, whereas the real source contains the negative coefficient `-c_R` on integers coprime to `P(R)` that are not prime powers. These are decisive differences, not technicalities.

Accordingly the theorem does not show that the actual distinguished bow variance is small, nor does it rule out a theorem exploiting positivity of the prime coefficients, the fixed `-c_R` rough-composite amplitude, prime/rough cross-correlation, bilinear factorization, or consistency of the same arithmetic coefficients across a family of twists. It shows something narrower but useful: **knowing the exact prime locations that carry the diagonal is still not enough if the prime amplitudes/signs are subsequently treated as free real coefficients of the correct size.**

This removes a natural fallback after `ANF-147`. One cannot repair its arbitrary-support objection merely by restricting the matched control to primes. The next genuinely source-specific step must use the fixed coefficient law

\[
a_X(n)=\Lambda(n)-c_R1_{(n,P(R))=1}
\tag{26}
\]

before absolute values or coefficient-general vector balancing discard it. A promising formulation is therefore a signed prime-versus-rough correlation statement at the distinguished `U`, or a decomposition whose cross terms are preserved strongly enough to forbid the blockwise adaptive signs above.

## 6. Prior-art boundary and stress test

The only asymptotic input needed to place enough blocks is the classical prime number theorem, already load-bearing in `ANF-102`. The local cancellation is elementary two-dimensional linear algebra; the random-sign comparison is elementary orthogonality. A bounded prior-art audit found the expected neighboring Steinitz/vector-balancing literature, including modern matrix and colorful variants, but those results concern ordering or selecting bounded vectors and are not used here. The order of the primes is fixed, no vector is permuted, and each block is annihilated by its own real kernel. No new external theorem is therefore load-bearing and `SOURCES.md` needs no additional anchor.

The stress tests are exact. Prime gaps can be arbitrarily irregular without changing (16), because only the number of partially intersected blocks matters. Degenerate phase triples cause no problem: a normalized real kernel still exists and uses at least two sites. The coefficient scale (12) is chosen precisely so that the prime count (5) produces the bow diagonal (19); reducing the support below prime density while retaining the same pointwise scale would eventually lose that normalization. Finally, the construction is pointwise in `U`, just like `ANF-147`: its coefficients may depend on the distinguished twist, so it does not contradict the super-`X` twist-average barrier in `ANF-144`.

For `analytic_frontier`, the admissibility boundary is now sharper. `ANF-146` rules out support/magnitude-only box coercivity, `ANF-147` keeps the exact logarithmic carrier and real coefficients, and the present finding keeps the **actual prime locus and prime-density source scale** as well. What remains unavailable to the matched controls is no longer generic geometry: it is the concrete arithmetic law tying signs and amplitudes to primes and `R`-rough composites. That is the information a successful bow argument now has to preserve.