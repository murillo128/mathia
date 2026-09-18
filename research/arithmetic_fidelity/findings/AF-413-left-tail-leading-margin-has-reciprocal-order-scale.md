# AF-413 — Left-tail leading margin has a reciprocal-order balance scale

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `ARITHMETIC-FIDELITY` · `TOTAL-POSITIVITY` · `CONFLUENT-CERTIFICATE` · `LEFT-TAIL-ORDER-SCALE` · `NO-NOVELTY-CLAIM`

## Claim

Let

\[
f(t)=-\log(1-e^{-e^t}),
\qquad
H_m(t)=(-1)^{m(m-1)/2}\det\bigl(f^{(i+j)}(t)\bigr)_{i,j=0}^{m-1}.
\]

AF-412 proves that for every fixed `m>=3`, writing `x=e^t` and `n=m-3`,

\[
H_m(t)=K_{n+1}x^{n^2+n+1}(1+o_m(1))
\qquad(x\downarrow0),
\tag{1}
\]

with a positive coefficient `K_{n+1}` determined by the smallest Bernoulli scales in the analytic germ. That coefficient has the exact closed form

\[
\boxed{
K_{n+1}
=\frac{n!(2n)!^2G(n+1)^2}{2\pi^{n(n+1)}}
\prod_{k=1}^n\zeta(2k),
\qquad n\ge0,
}
\tag{2}
\]

where `G` is the Barnes `G`-function and empty products have value one.

Let

\[
P_\infty:=\prod_{k=1}^\infty\zeta(2k).
\]

This product converges to a finite positive constant. As `n\to\infty`,

\[
\boxed{
\begin{aligned}
\log K_{n+1}
={}&n^2\left(\log\frac n\pi-\frac32\right)
+5n\log\frac{2n}{e}
+\frac43\log n\\
&+C_*+\frac1{6n}+O(n^{-2}),
\end{aligned}
}
\tag{3}
\]

with

\[
C_*=\frac32\log(2\pi)+2\zeta'(-1)+\log P_\infty.
\tag{4}
\]

Consequently, if `S_n=n^2+n+1`,

\[
\boxed{
K_{n+1}^{1/S_n}
=\frac{n}{\pi e^{3/2}}
\left(1+O\left(\frac{\log n}{n}\right)\right).
}
\tag{5}
\]

Thus the **leading AF-412 monomial itself** has the root-normalized scale

\[
\boxed{
\left(K_{n+1}x^{S_n}\right)^{1/S_n}
\sim \frac{nx}{\pi e^{3/2}}.
}
\tag{6}
\]

At the coefficient level, the first natural large-order/small-`x` balance is therefore `x` of order `1/n`, equivalently `e^t` of order `1/m`.

Equation `(6)` is not a uniform asymptotic for `H_m` when `m` varies. AF-412 takes `x\downarrow0` at each fixed `m`; its remainder was not controlled uniformly in the determinant order. The new result identifies the scale at which a genuine double-scaling analysis must begin, but does not prove positivity or failure along that diagonal.

## 1. Start from the exact AF-412 coefficient

AF-412 splits

\[
f(t)=u+h(x),\qquad u=-\log x,
\]

where

\[
h(x)=\frac x2-\sum_{k\ge1}\frac{B_{2k}}{2k(2k)!}x^{2k}.
\]

Its leading Cauchy--Binet term at order `m=n+3` uses the exponent set

\[
\Lambda_{n+1}=\{1,2,4,\ldots,2n\}
\]

and gives

\[
K_{n+1}
=\left(\prod_{\lambda\in\Lambda_{n+1}}|c_\lambda|\lambda^4\right)
\Delta(\Lambda_{n+1})^2,
\tag{7}
\]

with

\[
c_1=\frac12,
\qquad
c_{2k}=-\frac{B_{2k}}{2k(2k)!}.
\tag{8}
\]

Euler's classical even-zeta formula, recorded for example in NIST DLMF §25.6.2, is

\[
\zeta(2k)=\frac{(2\pi)^{2k}|B_{2k}|}{2(2k)!}.
\]

Therefore

\[
|c_{2k}|=\frac{\zeta(2k)}{k(2\pi)^{2k}},
\qquad
|c_{2k}|(2k)^4
=\frac{16k^3\zeta(2k)}{(2\pi)^{2k}}.
\tag{9}
\]

The coefficient part of `(7)` is consequently explicit.

## 2. The Vandermonde is a Barnes-G superfactorial

Separate the distances from the exceptional exponent `1` and the distances among the even exponents:

\[
\Delta(1,2,4,\ldots,2n)
=\prod_{k=1}^n(2k-1)
\prod_{1\le i<j\le n}2(j-i).
\tag{10}
\]

The first product is

\[
\prod_{k=1}^n(2k-1)=\frac{(2n)!}{2^n n!}.
\tag{11}
\]

For the second,

\[
\prod_{1\le i<j\le n}(j-i)
=\prod_{j=2}^n(j-1)!
=G(n+1),
\tag{12}
\]

using the classical integer-value identity for Barnes `G` (NIST DLMF §5.17.2). Hence

\[
\Delta(\Lambda_{n+1})
=\frac{(2n)!}{2^n n!}
2^{n(n-1)/2}G(n+1).
\tag{13}
\]

Substituting `(9)` and `(13)` into `(7)` makes all powers of `2` cancel exactly and leaves `(2)`.

The low-order checks recover the coefficients already audited independently in AF-412:

\[
K_1=\frac12,
\qquad
K_2=\frac13,
\qquad
K_3=\frac{16}{15}.
\tag{14}
\]

## 3. Large-order asymptotics

The zeta product contributes only a constant at algebraic order. Indeed,

\[
0<\zeta(2k)-1
=\sum_{j\ge2}j^{-2k}
\le 4^{-k}+\int_2^\infty x^{-2k}\,dx,
\]

so `\sum_k\log\zeta(2k)` converges absolutely and

\[
\prod_{k=1}^n\zeta(2k)=P_\infty(1+O(4^{-n})).
\tag{15}
\]

Take logarithms in `(2)`. Stirling's expansion for `n!` and `(2n)!`, together with the Barnes-`G` asymptotic from NIST DLMF §5.17.5,

\[
\log G(n+1)
=\frac{n^2}{2}\log n-\frac{3n^2}{4}
+\frac n2\log(2\pi)-\frac1{12}\log n
+\zeta'(-1)+O(n^{-2}),
\tag{16}
\]

and one further Stirling term give `(3)`. In particular, the quadratic contribution is

\[
n^2\left(\log\frac n\pi-\frac32\right),
\]

while all remaining nonconstant terms are `O(n\log n)`. Since `S_n=n^2+n+1`, division by `S_n` and exponentiation yield `(5)`.

The constant in `(16)` can equivalently be written `1/12-\log A`, where `A` is the Glaisher--Kinkelin constant; DLMF §5.17.7 records `\log A=1/12-\zeta'(-1)`.

## 4. Arithmetic-fidelity interpretation

AF-411 and AF-412 prove that every fixed confluent order eventually becomes positive in the two Euler-log tails, while AF-217 still forces failure somewhere in the unbounded hierarchy. The only way an obstruction can escape into a tail is therefore through **order drift**.

AF-413 prices one piece of that drift on the left. The first surviving AF-412 determinant term is not merely `x^{\Theta(m^2)}` with an unspecified prefactor. Its coefficient grows on the same quadratic-exponential scale, and after the natural `S_n`-th root the balance is exactly linear in `nx` up to the universal constant `\pi e^{3/2}`.

This matters because fixed-order asymptotics can be misleading when the order is itself the hidden resource. A statement of the form `H_m(t)>0` for every fixed `m` sufficiently far left gives no information about a sequence `m=m(t)\to\infty`. Equation `(6)` identifies `x\asymp1/m` as the first diagonal on which the leading positive certificate and its rapidly growing coefficient must be analyzed together rather than separately.

The result is source-agnostic and creates no rational-prime discriminator. It is a quantitative structural fact about the full Euler-log confluent certificate.

## Prior-art and novelty audit

Every external ingredient in `(2)`--`(5)` is classical: Euler's Bernoulli formula for `\zeta(2k)`, the integer product and asymptotic expansion of Barnes `G`, Stirling asymptotics, and elementary convergence of `\prod\zeta(2k)`. AF-412 already supplied the Bernoulli/Cauchy--Binet coefficient `(7)`. No novelty is claimed for any of those ingredients or for their algebraic combination.

There is a substantial separate literature on double-scaling asymptotics of Hankel determinants, often leading to Painlevé equations for specific varying moment weights. For example, Min Chen, Yang Chen, and Engui Fan, *Perturbed Hankel determinant, correlation functions and Painlevé equations*, J. Math. Phys. 57, 023501 (2016), DOI `10.1063/1.4939276`, studies `n\to\infty`, `t\to0` scalings for a Pollaczek--Jacobi weight. That literature shows that large-order/small-parameter Hankel limits are a classical asymptotic genre; it does not, by itself, supply a double-scaling theorem for the present derivative-Hankel Euler-log family.

The durable Arithmetic Fidelity contribution is therefore deliberately narrow: the exact AF-412 coefficient can be simplified enough to expose a previously hidden order scale, and this turns the vague statement "the fixed-order asymptotic is nonuniform" into a precise next asymptotic regime to test.

## Boundaries and falsification checks

- The `o_m(1)` in AF-412 is fixed-order. Equations `(2)`--`(6)` do not make it uniform in `m`.
- Substituting `x=c/n` into the leading monomial does **not** prove `H_{n+3}(\log(c/n))` has that sign or magnitude. Terms that are higher order for each fixed `n` may have coefficients growing fast enough to compete on the diagonal.
- The scale `x\asymp1/n` is a coefficient-balance scale, not an asserted sharp positivity threshold `T_m^-`.
- `K_{n+1}` is a leading determinant coefficient, not by itself a condition number or a stable-recovery modulus.
- No conclusion about the compact order-five gate, all-order total positivity, the location of zeta zeros, or RH follows from this result.
- The exact product `(2)` is falsified immediately by the already established low-order values if any indexing, Barnes-`G`, or Bernoulli normalization is wrong; `(14)` supplies that audit.

## Consequence for the research line

The next left-tail question is no longer merely whether the thresholds in AF-412 deteriorate with order. It is whether the whole rank-two/Cauchy--Binet expansion admits a **uniform double-scaling limit** when

\[
n=m-3\to\infty,
\qquad
x=e^t\sim\frac c n.
\]

A positive uniform dominance theorem would exclude one concrete order-drift corridor for the all-order obstruction. A competing term of comparable size or opposite sign would identify the mechanism by which fixed-order positivity can fail to survive the large-order compression. The coefficient theorem above supplies the normalization for that test; it does not prejudge its outcome.