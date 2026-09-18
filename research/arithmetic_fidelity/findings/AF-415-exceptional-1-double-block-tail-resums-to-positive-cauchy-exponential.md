# AF-415 — The exceptional-1 double-block tail resums to a positive Cauchy exponential

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `ARITHMETIC-FIDELITY` · `DOUBLE-SCALING` · `SCHUR-CAUCHY` · `UNIFORM-TAIL` · `NO-NOVELTY-CLAIM`

## Claim

Continue the AF-414 notation for the part of the Euler-log Cauchy--Binet expansion that contains the exceptional exponent `1`. For every partition `\lambda` with `\ell(\lambda)\le n`, let

\[
k_i=i+\lambda_{n+1-i},\qquad d=|\lambda|,
\]

and write the exact normalized contribution from AF-414 as

\[
\frac{T_{n,\lambda}(x)}{T_{n,\varnothing}(x)}
=
(-1)^d\left(\frac{x}{2\pi}\right)^{2d}
 s_\lambda(1^n)^2 R_{n,\lambda},
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

Define the entire normalized exceptional-`1` double-block sector

\[
S_n(c)
=
\sum_{\ell(\lambda)\le n}
(-q_n)^{|\lambda|}s_\lambda(1^n)^2R_{n,\lambda},
\qquad
q_n=\frac{a}{n^2},
\qquad
a=\frac{c^2}{4\pi^2}.
\tag{3}
\]

Then for every `A<\infty`, uniformly for `a\in[0,A]`,

\[
\boxed{
S_n(c)\longrightarrow e^{-a}
=
\exp\!\left(-\frac{c^2}{4\pi^2}\right).
}
\tag{4}
\]

Equivalently, for the original `x=c/n` scaling and `c` in compact subsets of `(0,\infty)`, the **full partition tail** inside the exceptional-`1`, double-rank-two Cauchy--Binet sector has a positive finite limit after normalization by the AF-412 leading contribution.

Thus the formal exponential identified degree-by-degree in AF-414 is an actual resummed limit for this whole sector. The opposite-sign first correction from AF-414 does not create a sign obstruction after the complete exceptional-`1` partition family is summed: it belongs to the Taylor expansion of the positive limit `e^{-c^2/(4\pi^2)}`.

This does **not** give the diagonal limit of the full derivative-Hankel determinant. Exponent sets that omit `1` and determinant sectors using fewer than two entries from the rank-two singular block remain outside `(3)`.

## 1. The unperturbed partition sum is exactly Cauchy

Remove the perturbation factor `R_{n,\lambda}` and define

\[
U_n(q)=
\sum_{\ell(\lambda)\le n}
(-q)^{|\lambda|}s_\lambda(1^n)^2.
\tag{5}
\]

The Schur Cauchy identity

\[
\sum_\lambda s_\lambda(X)s_\lambda(Y)
=
\prod_{i,j}(1-X_iY_j)^{-1}
\tag{6}
\]

with `X=(\sqrt q,\ldots,\sqrt q)` and `Y=(-\sqrt q,\ldots,-\sqrt q)` gives

\[
\boxed{
U_n(q)=(1+q)^{-n^2}.
}
\tag{7}
\]

Indeed, homogeneity gives

\[
s_\lambda(X)s_\lambda(Y)
=(-q)^{|\lambda|}s_\lambda(1^n)^2.
\]

For `q=a/n^2`, therefore,

\[
U_n(a/n^2)
=
\left(1+\frac{a}{n^2}\right)^{-n^2}
\longrightarrow e^{-a},
\tag{8}
\]

uniformly for `a` in every compact interval `[0,A]`.

Equation `(7)` is classical Schur-function mathematics. The remaining issue is whether the exact Euler-log perturbation `R_{n,\lambda}` can be removed uniformly over the **unbounded** partition family; AF-414 established this only partition-by-partition and degree-by-degree.

## 2. A uniform exponential bound for the Euler-log perturbation

Put

\[
\delta_i=k_i-i=\lambda_{n+1-i}\ge0,
\qquad
\sum_i\delta_i=|\lambda|=d.
\]

Since `\zeta(s)` is decreasing for real `s>1` and `k_i\ge i`,

\[
0<\frac{\zeta(2k_i)}{\zeta(2i)}\le1.
\tag{9}
\]

Also

\[
\frac{k_i}{i}=1+\frac{\delta_i}{i}
\le1+\delta_i\le2^{\delta_i},
\tag{10}
\]

and

\[
\frac{2k_i-1}{2i-1}
=1+\frac{2\delta_i}{2i-1}
\le1+2\delta_i\le3^{\delta_i}.
\tag{11}
\]

Substituting `(9)`--`(11)` into `(2)` yields the crude but uniform estimate

\[
\boxed{
0<R_{n,\lambda}\le72^{|\lambda|}.
}
\tag{12}
\]

No constant depending on `n`, the partition shape, or its length occurs in `(12)`. This is the missing summability resource: the exact perturbation grows at most exponentially in the excess degree, while the diagonal scaling contributes `n^{-2d}`.

## 3. The positive Cauchy majorant gives a uniform degree tail

The positive specialization of the same Cauchy identity gives, for `0\le t<1`,

\[
\sum_{\ell(\lambda)\le n}
t^{|\lambda|}s_\lambda(1^n)^2
=(1-t)^{-n^2}.
\tag{13}
\]

Hence the degree-`d` coefficient is exactly

\[
[t^d](1-t)^{-n^2}
=\frac{(n^2)_d}{d!},
\tag{14}
\]

where `(n^2)_d=n^2(n^2+1)\cdots(n^2+d-1)` is the rising factorial.

Fix `A<\infty` and let `0\le a\le A`. By `(12)`, the absolute tail of `(3)` above degree `D` is bounded by

\[
\sum_{d>D}
\frac{(n^2)_d}{d!}
\left(\frac{72a}{n^2}\right)^d.
\tag{15}
\]

For `n` large enough that `144A/n^2\le1/2`, insert a factor `2^{-d}2^d` and use `(13)`:

\[
\begin{aligned}
\sum_{d>D}
\frac{(n^2)_d}{d!}
\left(\frac{72a}{n^2}\right)^d
&\le
2^{-D}
\sum_{d\ge0}
\frac{(n^2)_d}{d!}
\left(\frac{144A}{n^2}\right)^d\\
&=
2^{-D}
\left(1-\frac{144A}{n^2}\right)^{-n^2}\\
&\le
2^{-D}e^{288A}.
\end{aligned}
\tag{16}
\]

The same majorant, with `R_{n,\lambda}=1`, also controls the absolute tail of `(5)`. Thus both the exact perturbed series and the classical Cauchy series have degree tails that vanish as `D\to\infty` **uniformly in all sufficiently large `n` and uniformly for `a\in[0,A]`**.

The numerical constant `72` is deliberately not optimized; only an exponential-in-degree bound independent of `n` is needed.

## 4. Finite heads converge by AF-414

For every fixed `D`, only finitely many partitions satisfy `|\lambda|\le D`. AF-414 proves for each such partition that

\[
R_{n,\lambda}\to1,
\tag{17}
\]

and that

\[
\frac{s_\lambda(1^n)}{n^{|\lambda|}}
\to\frac1{H_\lambda}.
\tag{18}
\]

Because this family is finite, the convergence of the degree-`D` head of `S_n(c)-U_n(a/n^2)` is uniform for `a\in[0,A]`. Combining that finite-head convergence with `(16)` gives

\[
\lim_{n\to\infty}
\sup_{0\le a\le A}
\left|S_n(c)-U_n(a/n^2)\right|=0.
\tag{19}
\]

Finally `(8)` and `(19)` prove `(4)`.

This is precisely the limit/sum interchange that AF-414 was not entitled to make from fixed-degree convergence alone.

## 5. Arithmetic-fidelity interpretation

AF-414 exposed a genuine bounded-complexity failure of leading-term dominance: every fixed excess degree survives on `x=c/n`, and the first survivor has the opposite sign. AF-415 shows that the corresponding **unbounded** complexity family is nevertheless controlled once its complete relational organization is retained. The whole exceptional-`1` partition family is not an arbitrary collection of dangerous corrections; Schur Cauchy structure supplies an exact global resummation, and the Euler-log deviation from that classical model is uniformly summable.

This is a useful refinement of the line's compression theme. A local or fixed-complexity audit can correctly detect loss of dominance without determining the global sign after all surviving structure is restored. Here the richer partition organization turns the apparent alternating obstruction into the positive factor `e^{-a}`.

No rational-prime discriminator is present in this theorem. Its value for Arithmetic Fidelity is methodological and structural: it closes one concrete uniformity gate in a representation where bounded-complexity evidence alone was insufficient.

## Prior-art and novelty audit

The Schur Cauchy identity and its use to normalize measures on partitions are classical. I. G. Macdonald, *Symmetric Functions and Hall Polynomials*, 2nd ed., Oxford University Press (1995), Chapter I, is a standard source for the Cauchy identity. Andrei Okounkov, **“Infinite wedge and random partitions,”** *Selecta Mathematica (N.S.)* 7(1), 57--81 (2001), arXiv:`math/9907127`, introduced the Schur measure and uses the same Cauchy normalization framework for products of Schur specializations.

No novelty is claimed for `(6)`, `(7)`, `(13)`, the negative-binomial coefficient formula `(14)`, or the elementary generating-function tail device. A targeted prior-art search did not locate the specific perturbed sum `(3)` arising from AF-414's Euler-log derivative-Hankel Cauchy--Binet sector, nor the uniform bound `(12)` and resulting limit `(4)` for that specialization. The durable contribution is therefore the exact specialization and uniform-tail closure, not the underlying Schur technology.

## Boundaries and falsification checks

- The theorem controls only exponent sets **containing the exceptional exponent `1`** inside the double-rank-two Cauchy--Binet sector identified in AF-412/AF-414.
- Exponent sets omitting `1` are not included in `S_n(c)` and may have different large-order coefficient growth.
- Determinant terms using one or zero entries from the rank-two logarithmic block are not included; their powers of `u=-\log x` still require a uniform diagonal estimate.
- The result is locally uniform for fixed `c` ranges. It makes no claim when `c=c_n` grows with `n`.
- At the normalized-series level `a=0` is harmless and gives `S_n=1`; the original coordinate has `x=e^t>0`, so the geometric left-tail scaling uses `c>0`.
- The constant `72` is only a majorant and carries no threshold significance.
- Positivity of the limit `e^{-a}` does not imply eventual positivity of the **full** derivative-Hankel determinant on the diagonal until the omitted sectors are controlled relative to the same normalization.
- Nothing here proves all-order total positivity, identifies a zeta-zero mechanism, or implies RH.

## Consequence for the research line

The partition-tail part of `CLUE-left-tail-diagonal-order-drift-scale` is now closed: fixed-degree convergence does extend to the complete exceptional-`1` double-block family, and its normalized diagonal limit is the positive Cauchy exponential.

The clue itself remains live because its decisive test is broader. The next load-bearing gates are now cleanly separated: control exponent sets that omit `1`, and control the one-/zero-singular-block determinant sectors on `x=c/n`. Only after those terms are compared with the positive factor `(4)` can the full diagonal sign or asymptotic be decided.
