# AF-414 — Fixed-excess left-tail sectors have a signed Plancherel limit

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `ARITHMETIC-FIDELITY` · `TOTAL-POSITIVITY` · `CONFLUENT-CERTIFICATE` · `DOUBLE-SCALING` · `PLANCHEREL-SECTOR` · `NO-NOVELTY-CLAIM`

## Claim

Let

\[
f(t)=-\log(1-e^{-e^t}),
\qquad
H_m(t)=(-1)^{m(m-1)/2}\det\bigl(f^{(i+j)}(t)\bigr)_{i,j=0}^{m-1}.
\]

AF-412 writes the left-tail profile as a rank-two logarithmic block plus an analytic Bernoulli germ and, for `m=n+3`, reduces the leading double-block sector to the `(n+1) x (n+1)` derivative-Hankel determinant

\[
L_{n+1}(x)=\det(h_{a+b+4}(x))_{a,b=0}^{n},
\qquad x=e^t,
\]

whose Cauchy--Binet expansion runs over exponent subsets of

\[
\mathcal A=\{1,2,4,6,\ldots\}.
\]

The AF-412 leading exponent set is

\[
A_0=\{1,2,4,\ldots,2n\}.
\]

Consider the part of the same Cauchy--Binet sector that still contains the exceptional exponent `1`. For a partition `\lambda` with `\ell(\lambda)\le n`, put

\[
k_i=i+\lambda_{n+1-i},\qquad 1\le i\le n,
\]

and

\[
A_\lambda=\{1,2k_1,\ldots,2k_n\}.
\]

If `d=|\lambda|` and `T_{n,\lambda}(x)` denotes the signed Cauchy--Binet contribution of `A_\lambda`, then the ratio to the leading contribution is exactly

\[
\boxed{
\frac{T_{n,\lambda}(x)}{T_{n,\varnothing}(x)}
=
(-1)^d\left(\frac{x}{2\pi}\right)^{2d}
 s_\lambda(1^n)^2
 R_{n,\lambda},
}
\tag{1}
\]

where

\[
R_{n,\lambda}
=
\prod_{i=1}^{n}
\left(\frac{k_i}{i}\right)^3
\frac{\zeta(2k_i)}{\zeta(2i)}
\left(\frac{2k_i-1}{2i-1}\right)^2.
\tag{2}
\]

For every fixed partition `\lambda`,

\[
R_{n,\lambda}\to1
\qquad(n\to\infty),
\]

and the hook-content formula gives

\[
s_\lambda(1^n)
=\prod_{\square\in\lambda}\frac{n+c(\square)}{h(\square)}
=\frac{n^d}{H_\lambda}\bigl(1+O_\lambda(n^{-1})\bigr),
\tag{3}
\]

with `H_\lambda=\prod_{\square\in\lambda}h(\square)`. Therefore on the AF-413 diagonal

\[
x=\frac cn,
\qquad c>0\text{ fixed},
\]

one has the exact fixed-partition limit

\[
\boxed{
\frac{T_{n,\lambda}(c/n)}{T_{n,\varnothing}(c/n)}
\longrightarrow
(-1)^d\frac{(c^2/4\pi^2)^d}{H_\lambda^2}.
}
\tag{4}
\]

For each fixed excess degree `d`, summing `(4)` over all partitions `\lambda\vdash d` gives

\[
\boxed{
\frac{\sum_{\lambda\vdash d}T_{n,\lambda}(c/n)}
{T_{n,\varnothing}(c/n)}
\longrightarrow
\frac{(-1)^d}{d!}
\left(\frac{c^2}{4\pi^2}\right)^d.
}
\tag{5}
\]

Indeed, the hook-length formula `f^\lambda=d!/H_\lambda` and the regular-representation identity `\sum_{\lambda\vdash d}(f^\lambda)^2=d!` imply

\[
\sum_{\lambda\vdash d}\frac1{H_\lambda^2}=\frac1{d!}.
\tag{6}
\]

Thus the fixed-excess sectors are distributed inside each degree by the ordinary Plancherel weights and their aggregate coefficients are exactly those of the formal exponential

\[
\exp\!\left(-\frac{c^2}{4\pi^2}\right).
\]

This is a **fixed-degree statement**. Equation `(5)` does not justify interchanging `n\to\infty` with the infinite sum over `d`, and therefore does not prove that the whole double-block sector converges to that exponential.

The first correction is already decisive. For `\lambda=(1)`, equivalently replacing the largest exponent `2n` by `2n+2`,

\[
\boxed{
\frac{T_{n,(1)}(x)}{T_{n,\varnothing}(x)}
=-\frac{(n+1)^3}{4\pi^2 n}
\left(\frac{2n+1}{2n-1}\right)^2
\frac{\zeta(2n+2)}{\zeta(2n)}x^2.
}
\tag{7}
\]

Hence

\[
\boxed{
\frac{T_{n,(1)}(c/n)}{T_{n,\varnothing}(c/n)}
\longrightarrow -\frac{c^2}{4\pi^2}.
}
\tag{8}
\]

For every fixed `c>0`, the AF-412 leading monomial therefore fails to be a relative-error asymptotic on the `x=c/n` diagonal even **inside its own double-rank-two Cauchy--Binet sector**: the unique first competing exponent family has opposite sign and nonzero limiting relative size. AF-413's reciprocal-order scale is consequently a genuine competition scale, not merely a dimensional balance suggested by the leading coefficient.

## 1. Partition parametrization of the fixed-excess sector

AF-412 writes the analytic germ as

\[
h(x)=\frac x2-\sum_{k\ge1}\frac{B_{2k}}{2k(2k)!}x^{2k}
=\sum_{\alpha\in\mathcal A}c_\alpha x^\alpha
\]

and obtains

\[
L_{n+1}(x)
=
\sum_{\alpha_0<\cdots<\alpha_n}
\left(\prod_{j=0}^{n}c_{\alpha_j}\alpha_j^4x^{\alpha_j}\right)
\Delta(\alpha_0,\ldots,\alpha_n)^2.
\tag{9}
\]

Restrict to terms with `\alpha_0=1`. The remaining exponents are even, so write them as `2k_1<\cdots<2k_n`. The baseline has `k_i=i`. Every increasing integer sequence above that baseline can be written uniquely as

\[
k_i=i+\lambda_{n+1-i}
\]

for a partition `\lambda` with at most `n` parts. Its total exponent exceeds the baseline by

\[
2\sum_{i=1}^{n}(k_i-i)=2|\lambda|.
\tag{10}
\]

Thus partitions are not decorative notation here: they index exactly the exponent families at a fixed Cauchy--Binet excess degree.

## 2. Exact normalized term formula

Euler's even-zeta formula, already used in AF-413, gives

\[
|c_{2k}|(2k)^4
=\frac{16k^3\zeta(2k)}{(2\pi)^{2k}}.
\tag{11}
\]

The sign of `c_{2k}` is `(-1)^k`. Relative to the baseline `k_i=i`, shifting by a partition of size `d` therefore contributes the sign `(-1)^d` and the scale factor `(x/2\pi)^{2d}`.

For the Vandermonde, separate the distances to the exceptional exponent `1` from the even-even distances:

\[
\Delta(1,2k_1,\ldots,2k_n)
=
\left(\prod_{i=1}^n(2k_i-1)\right)
2^{n(n-1)/2}\Delta(k_1,\ldots,k_n).
\tag{12}
\]

The powers of `2` cancel in the ratio with the baseline. The Weyl alternant formula gives

\[
\frac{\Delta(k_1,\ldots,k_n)}{\Delta(1,\ldots,n)}
=s_\lambda(1^n).
\tag{13}
\]

Combining `(11)`--`(13)` and squaring the Vandermonde ratio yields exactly `(1)` and `(2)`.

A direct low-excess audit is provided by `\lambda=(1)`. Then only `k_n=n+1` changes, `s_{(1)}(1^n)=n`, and `(1)` reduces algebraically to `(7)`. The Vandermonde ratio itself is

\[
\frac{\Delta(1,2,4,\ldots,2n-2,2n+2)}
{\Delta(1,2,4,\ldots,2n)}
=n\frac{2n+1}{2n-1},
\tag{14}
\]

which independently exposes the `n^2` growth that cancels the `x^2=c^2/n^2` suppression.

## 3. Fixed-partition and fixed-degree limits

For fixed `\lambda`, only finitely many of the largest indices `i` are shifted. Hence every factor in `(2)` tends to one: `k_i/i\to1`, `(2k_i-1)/(2i-1)\to1`, and `\zeta(2k_i)/\zeta(2i)\to1`. The hook-content formula gives `(3)`, so substituting `x=c/n` into `(1)` proves `(4)`.

For fixed `d`, there are only finitely many partitions of `d`, and for all sufficiently large `n` they all satisfy `\ell(\lambda)\le n`. The limit may therefore be summed term-by-term at that fixed degree. The classical hook-length formula identifies

\[
\frac{1/H_\lambda^2}{\sum_{\mu\vdash d}1/H_\mu^2}
=
\frac{(f^\lambda)^2}{d!},
\tag{15}
\]

which is exactly the Plancherel probability on partitions of `d`. Equation `(6)` then proves `(5)`.

The exponential pattern in `(5)` is consequently not a fitted approximation. It is forced, degree by degree, by the Schur/Weyl growth of the Vandermonde quotient and the Plancherel normalization of the partition shapes.

## 4. Arithmetic-fidelity interpretation

AF-412 proves that every fixed determinant order is eventually positive in the left tail. AF-413 then shows that the root-normalized leading coefficient compensates the shrinking coordinate when `nx` is order one. The present result identifies the mechanism hidden by that fixed-order statement: as the allowed determinant order grows, an entire hierarchy of nearby exponent configurations becomes visible at exactly the same physical scale.

The first omitted configuration is already order one relative to the nominal leading term and has the opposite sign. More generally, fixed excess degree `d` carries a coherent signed family whose relative mass survives the diagonal limit. Thus the failure of uniformity is not caused by one anomalously large coefficient; it has a structured combinatorial organization by partitions.

This is a concrete Arithmetic Fidelity phenomenon: a compression certificate can be asymptotically faithful at every bounded complexity while losing leading-term dominance when the complexity budget grows with the observation scale. The relevant resource is therefore not just the retained scalar value or the determinant order separately, but their joint scaling.

No rational-prime discriminator appears in `(1)`--`(8)`. The result concerns the Euler-log analytic source and the internal fidelity of its confluent translation certificate. Any RH relevance still requires an independent theorem linking the all-order translation-sign structure to the required continued zero geometry.

## Prior-art and novelty audit

The representation-theoretic ingredients are classical. The specialization `s_\lambda(1^n)` and its hook-content product are standard Schur-function/Weyl-dimension formulas; Christian Krattenthaler's *A Bijective Proof of the Hook-content Formula*, Electronic Journal of Combinatorics 3(2), R14 (1995/1996), DOI `10.37236/1272`, is one explicit source. The hook-length formula for `f^\lambda` goes back to Frame, Robinson, and Thrall, *The Hook Graphs of the Symmetric Group*, Canadian Journal of Mathematics 6 (1954), 316--324, DOI `10.4153/CJM-1954-030-1`. The identity `\sum_{\lambda\vdash d}(f^\lambda)^2=d!` is the classical decomposition of the regular representation of `S_d`; the resulting weights `(f^\lambda)^2/d!` are ordinary Plancherel measure.

Bernoulli/Euler Hankel determinants also have substantial prior art. Karl Dilcher and Lin Jiu, *Hankel Determinants of shifted sequences of Bernoulli and Euler numbers*, Contributions to Discrete Mathematics 18(2) (2023), 146--175, DOI `10.55016/ojs/cdm.v18i2.73995`, studies exact Hankel evaluations for Bernoulli/Euler-related sequences. AF-413 already records the separate classical literature on large-order/small-parameter double scaling of Hankel determinants.

No novelty is claimed for Schur functions, hook formulas, Plancherel measure, Bernoulli coefficient identities, Cauchy--Binet, or double-scaling Hankel methods. A targeted prior-art check did not locate a theorem that supplies `(1)`--`(8)` for the specific derivative-Hankel Euler-log family with AF-412's rank-two logarithmic block. The durable contribution is the exact specialization: it proves that the reciprocal-order scale found in AF-413 is populated by explicit opposite-sign competitors and identifies the fixed-excess partition law that organizes them.

## Boundaries and falsification checks

- Equations `(4)` and `(5)` hold with `\lambda` or `d` fixed while `n\to\infty`. They are not uniform when the excess degree grows with `n`.
- The formal exponential suggested by the coefficients in `(5)` is **not** established as the limit of the entire `1`-containing double-block sector. Such a statement requires a summable bound uniform in `d` before exchanging the limit and the infinite partition sum.
- Exponent sets that omit `1` are not controlled here. Their fixed-order powers are higher, but their large-order coefficients must be audited on the same diagonal before they can be discarded.
- The determinant expansion also contains terms using only one or zero entries from the rank-two logarithmic block. Their `u=-\log x` factors and larger analytic minors were lower order at fixed `n`; that does not by itself prove they are negligible for `x=c/n`.
- An opposite-sign correction does not imply that the double-block sector, still less the full determinant `H_m`, becomes negative. For small `c`, the degree-one correction is small even though it is asymptotically nonzero relative to the leading term.
- The exact formula `(7)` is independently falsifiable from the coefficient ratio `(11)` and the elementary Vandermonde ratio `(14)`; an indexing or sign error changes its low-`n` values immediately.
- The result does not decide the compact order-five gate, all-order total positivity, the location of zeta zeros, or RH.

## Consequence for the research line

The `x\asymp1/n` clue is now mathematically live for a stronger reason than AF-413's coefficient balance. Leading-term dominance actually breaks at the first neighboring exponent family, and every fixed excess degree survives with a signed Plancherel profile.

The remaining double-scaling problem is consequently sharper. One must control the partition tail as `d` grows, the exponent sets that omit the exceptional exponent `1`, and the one-/zero-singular-block determinant sectors on the same `x=c/n` scale. If those pieces are uniformly negligible or resum to a positive function, the left-tail obstruction is pushed elsewhere; if one of them becomes comparable with a different sign structure, it identifies the actual order-drift mechanism. Fixed-order asymptotics alone can no longer decide that question.