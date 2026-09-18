# AF-416 — The full left-tail diagonal has a positive Cauchy limit

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `ARITHMETIC-FIDELITY` · `DOUBLE-SCALING` · `FULL-DETERMINANT` · `SCHUR-CAUCHY` · `NO-NOVELTY-CLAIM`

## Claim

Let

\[
f(t)=-\log(1-e^{-e^t}),
\qquad
H_m(t)=(-1)^{m(m-1)/2}\det\bigl(f^{(i+j)}(t)\bigr)_{i,j=0}^{m-1}.
\]

Use the AF-412 left-tail decomposition

\[
x=e^t,
\qquad
v=-\log x,
\qquad
f=v+h(x),
\]

where

\[
h(x)=\frac{x}{2}-\sum_{k\ge1}\frac{B_{2k}}{2k(2k)!}x^{2k}
=\sum_{\alpha\in\mathcal A}c_\alpha x^\alpha,
\qquad
\mathcal A=\{1,2,4,6,\ldots\}.
\]

For `n>=1`, put

\[
m=n+3,
\qquad
r=n+1,
\qquad
S_n=n^2+n+1=1+r(r-1).
\]

Let `K_r>0` be the exact AF-412 coefficient of the smallest Cauchy--Binet exponent set `\{1,2,4,\ldots,2(r-1)\}`. Then for every compact interval

\[
0<c_-\le c\le c_+<\infty,
\]

one has, uniformly in `c`,

\[
\boxed{
\frac{H_{n+3}(\log(c/n))}
{K_{n+1}(c/n)^{n^2+n+1}}
\longrightarrow
\exp\!\left(-\frac{c^2}{4\pi^2}\right).
}
\tag{1}
\]

In particular, for every such compact interval there is `N=N(c_-,c_+)` such that

\[
H_{n+3}(\log(c/n))>0
\]

for all `n>=N` and all `c\in[c_-,c_+]`.

Thus the reciprocal-order scale isolated by AF-413 is a genuine competition scale, as AF-414 showed, but its **full** diagonal resummation is positive. AF-415 supplied the positive limit for the exceptional-`1` double-rank-two sector. The present result closes the two omitted classes from AF-415: exponent sets that omit `1`, and determinant sectors using only one or zero entries from the rank-two logarithmic block.

Equation `(1)` does not prove total positivity at all orders. It says that a bad large-order sequence cannot remain on any compact `nx=c` corridor in the left tail.

## 1. Exact determinant decomposition by singular-block usage

Write `E=x\,d/dx` and `h_j=E^j h`. AF-412 gives

\[
f=v+h_0,
\qquad
f'=-1+h_1,
\qquad
f^{(j)}=h_j\quad(j\ge2).
\]

Hence, with indices starting at zero,

\[
M_m:=\bigl(f^{(i+j)}\bigr)_{i,j=0}^{m-1}=B_m+U,
\qquad
B_m=(h_{i+j}),
\]

where `U` is supported on the upper-left `2 x 2` block

\[
U_{\{0,1\},\{0,1\}}=
\begin{pmatrix}v&-1\\-1&0\end{pmatrix}.
\tag{2}
\]

For `R>=1` and `s>=0`, define the shifted derivative-Hankel determinant

\[
D_R^{(s)}(x):=
\det\bigl(h_{a+b+s}(x)\bigr)_{a,b=0}^{R-1}.
\tag{3}
\]

Also let `Q_R(x)` be the `R x R` minor of `B_{R+1}` with row indices `1,\ldots,R` and column indices `0,2,3,\ldots,R`. Expanding `(2)` by the number of entries taken from `U` gives the exact identity

\[
\boxed{
\det M_{r+2}
=
D_{r+2}^{(0)}
+vD_{r+1}^{(2)}
+2Q_{r+1}
-D_r^{(4)}.
}
\tag{4}
\]

The four terms use respectively zero, one diagonal, one off-diagonal, and two singular-block directions. There are no other terms because `U_{11}=0` and the remaining entries of `U` vanish.

The last term is exactly the double-rank-two sector treated asymptotically in AF-412--AF-415. The first three terms are the missing determinant sectors in the accepted diagonal clue.

## 2. Cauchy--Binet form for the shifted determinants

Since

\[
h_j(x)=\sum_{\alpha\in\mathcal A}c_\alpha\alpha^j x^\alpha,
\]

Cauchy--Binet gives

\[
D_R^{(s)}(x)
=
\sum_{\substack{A\subset\mathcal A\\|A|=R}}
\left(\prod_{\alpha\in A}c_\alpha\alpha^s x^\alpha\right)
\Delta(A)^2.
\tag{5}
\]

For the two possible smallest support patterns define

\[
A_R^*=\{1,2,4,\ldots,2(R-1)\},
\qquad
A_R^0=\{2,4,\ldots,2R\},
\]

and let `E_R^{(s)}` and `F_R^{(s)}` be their respective signed terms in `(5)`. Every exponent set in `(5)` lies in exactly one of two classes: it contains the exceptional exponent `1`, or it is entirely even.

The Bernoulli/zeta coefficient formula is

\[
c_1=\frac12,
\qquad
c_{2k}=(-1)^k\frac{\zeta(2k)}{k(2\pi)^{2k}}.
\tag{6}
\]

This makes both classes uniformly summable on `x=c/n`.

### Exceptional-`1` class

For an exponent set containing `1`, write the remaining exponents as `2k_i`, `1\le i\le R-1`, with

\[
k_i=i+\lambda_{R-i}
\]

for a partition `\lambda` with `\ell(\lambda)\le R-1` and `d=|\lambda|`. The exact ratio to `E_R^{(s)}` is the AF-414 Schur/Vandermonde ratio with the power `4` replaced by `s`:

\[
\frac{T_{R,\lambda}^{(s)}}{E_R^{(s)}}
=
(-1)^d
\left(\frac{x}{2\pi}\right)^{2d}
 s_\lambda(1^{R-1})^2
 R_{R,\lambda}^{(s)},
\tag{7}
\]

where

\[
R_{R,\lambda}^{(s)}
=
\prod_{i=1}^{R-1}
\left(\frac{k_i}{i}\right)^{s-1}
\frac{\zeta(2k_i)}{\zeta(2i)}
\left(\frac{2k_i-1}{2i-1}\right)^2.
\tag{8}
\]

For `s\in\{0,2,4\}`, monotonicity of `\zeta` on `(1,\infty)` and the elementary bounds

\[
1+\delta\le2^\delta,
\qquad
1+2\delta\le3^\delta
\]

give

\[
0<R_{R,\lambda}^{(s)}\le \beta_s^{|\lambda|},
\qquad
\beta_0=9,
\quad
\beta_2=18,
\quad
\beta_4=72.
\tag{9}
\]

The positive Schur Cauchy identity therefore yields

\[
\sum_{\lambda}
\left|
\frac{T_{R,\lambda}^{(s)}}{E_R^{(s)}}
\right|
\le
\left(1-\beta_s\frac{x^2}{4\pi^2}\right)^{-(R-1)^2}
\tag{10}
\]

whenever the argument is below one. If `R=n+O(1)` and `x=c/n` with `c` in a fixed compact interval, the right side is bounded uniformly in `n` and `c`.

### All-even class

For an all-even exponent set write `k_i=i+\lambda_{R+1-i}`, `1\le i\le R`. Relative to `F_R^{(s)}` the odd-distance factors from `(8)` disappear. Thus

\[
\sum_{\lambda}
\left|
\frac{\widetilde T_{R,\lambda}^{(s)}}{F_R^{(s)}}
\right|
\le
\left(1-\widetilde\beta_s\frac{x^2}{4\pi^2}\right)^{-R^2},
\tag{11}
\]

with

\[
\widetilde\beta_0=1,
\qquad
\widetilde\beta_2=2,
\qquad
\widetilde\beta_4=8.
\]

Again this is uniformly bounded on `R=n+O(1)`, `x=c/n`, `c` compact.

The ratio of the two baseline terms is explicit:

\[
\boxed{
\frac{F_R^{(s)}}{E_R^{(s)}}
=
\frac{c_{2R}(2R)^s}{c_1}
 x^{2R-1}
\left[
\frac{4^{R-1}}{\binom{2R-2}{R-1}}
\right]^2.
}
\tag{12}
\]

The central-binomial estimate

\[
\binom{2k}{k}\ge\frac{4^k}{2k+1}
\]

shows that the square bracket in `(12)` grows at most polynomially. By `(6)`, the remaining factor contains `(x/2\pi)^{2R-1}` up to another polynomial in `R`. Hence

\[
\frac{F_R^{(s)}}{E_R^{(s)}}\longrightarrow0
\tag{13}
\]

faster than every inverse power of `n`, uniformly for `R=n+O(1)` and `c` in compact subsets of `(0,\infty)`.

Equations `(10)`--`(13)` prove two facts needed below: every `D_R^{(s)}` is uniformly bounded relative to its exceptional baseline, and the complete omitted-`1` sector is negligible there. This closes the omitted-exponent-set gate left by AF-415.

## 3. The double-block term keeps the AF-415 Cauchy limit

For the term `D_r^{(4)}`, with `r=n+1`, the exceptional baseline is precisely the AF-412 leading Cauchy--Binet term. Write

\[
E_r^{(4)}
=(-1)^{r(r-1)/2}K_r x^{1+r(r-1)}.
\tag{14}
\]

AF-415 proves that the complete exceptional-`1` part satisfies, locally uniformly for `c>0`,

\[
\frac{D_{r,\,1\in A}^{(4)}(c/n)}{E_r^{(4)}(c/n)}
\longrightarrow
\exp\!\left(-\frac{c^2}{4\pi^2}\right).
\tag{15}
\]

The all-even part is bounded relative to `F_r^{(4)}` by `(11)`, while `(13)` gives `F_r^{(4)}/E_r^{(4)}\to0`. Therefore the **full** shifted determinant obeys

\[
\boxed{
\frac{D_r^{(4)}(c/n)}{E_r^{(4)}(c/n)}
\longrightarrow
\exp\!\left(-\frac{c^2}{4\pi^2}\right)
}
\tag{16}
\]

locally uniformly on `(0,\infty)`.

## 4. The one-singular-block sectors vanish

The exceptional baselines of `D_{r+1}^{(2)}` and `D_r^{(4)}` differ by one additional exponent `2r`. Direct cancellation of the common weights and Vandermonde factors gives

\[
\frac{E_{r+1}^{(2)}}{E_r^{(4)}}
=
c_{2r}(2r)^2(2r-1)^2x^{2r}.
\tag{17}
\]

Hence

\[
\left|
\frac{E_{r+1}^{(2)}}{E_r^{(4)}}
\right|
=
4r(2r-1)^2\zeta(2r)
\left(\frac{x}{2\pi}\right)^{2r}.
\tag{18}
\]

For `x=c/n`, `r=n+1`, this tends to zero faster than every inverse power of `n`, uniformly for bounded `c`.

By `(10)`--`(13)`, `D_{r+1}^{(2)}/E_{r+1}^{(2)}` is uniformly bounded. Also `v=\log(n/c)=O(\log n)` uniformly for `c\in[c_-,c_+]`. Therefore

\[
\frac{vD_{r+1}^{(2)}}{E_r^{(4)}}\longrightarrow0.
\tag{19}
\]

For the off-diagonal minor `Q_R`, Cauchy--Binet gives a similarly explicit formula. If `A` is an `R`-element exponent set, the row alternant has powers `1,2,\ldots,R` and the column alternant has powers `0,2,3,\ldots,R`. Their product is

\[
\left(\prod_{\alpha\in A}\alpha^2\right)
\Delta(A)^2
\left(\sum_{\alpha\in A}\frac1\alpha\right).
\]

Thus

\[
Q_R
=
\sum_{|A|=R}
\left(\prod_{\alpha\in A}c_\alpha\alpha^2x^\alpha\right)
\Delta(A)^2
\left(\sum_{\alpha\in A}\frac1\alpha\right).
\tag{20}
\]

The smallest possible reciprocal sum majorizes every other one:

\[
\sum_{\alpha\in A}\frac1\alpha
\le
1+\frac12 H_{R-1}
=O(\log R).
\tag{21}
\]

Combining `(20)`--`(21)` with the absolute Schur bounds already used for `D_R^{(2)}` gives

\[
\frac{|Q_R|}{|E_R^{(2)}|}=O_c(\log R).
\tag{22}
\]

Taking `R=r+1` and using `(18)`,

\[
\frac{Q_{r+1}}{E_r^{(4)}}\longrightarrow0
\tag{23}
\]

locally uniformly in `c`. Both one-singular-block sectors in `(4)` are therefore negligible on the reciprocal-order diagonal.

## 5. The zero-singular-block sector also vanishes

The exceptional baseline of `D_{r+2}^{(0)}` adds the two exponents `2r` and `2r+2` to the baseline of `D_r^{(4)}`. Exact cancellation gives

\[
\frac{E_{r+2}^{(0)}}{E_r^{(4)}}
=
4r^2(2r-1)^2(2r+1)^2
c_{2r}c_{2r+2}x^{4r+2}.
\tag{24}
\]

Using `(6)`,

\[
\left|
\frac{E_{r+2}^{(0)}}{E_r^{(4)}}
\right|
=
4\frac{r}{r+1}(2r-1)^2(2r+1)^2
\zeta(2r)\zeta(2r+2)
\left(\frac{x}{2\pi}\right)^{4r+2}.
\tag{25}
\]

This again vanishes faster than every inverse power of `n` when `r=n+1` and `x=c/n`, uniformly for bounded `c`. Since `(10)`--`(13)` make `D_{r+2}^{(0)}/E_{r+2}^{(0)}` uniformly bounded,

\[
\frac{D_{r+2}^{(0)}}{E_r^{(4)}}\longrightarrow0.
\tag{26}
\]

This closes the zero-singular-block gate.

## 6. Assemble the full determinant

Divide `(4)` by `E_r^{(4)}`. Equations `(16)`, `(19)`, `(23)`, and `(26)` give

\[
\frac{\det M_{r+2}}{E_r^{(4)}}
\longrightarrow
-\exp\!\left(-\frac{c^2}{4\pi^2}\right)
\tag{27}
\]

locally uniformly for `c>0`.

Finally `m=r+2` and

\[
(-1)^{m(m-1)/2}
\bigl[-(-1)^{r(r-1)/2}\bigr]=1,
\]

because

\[
\frac{m(m-1)}2+1+\frac{r(r-1)}2
=r(r+1)+2
\]

is even. Combining this sign identity with `(14)` and `(27)` proves `(1)`.

## Arithmetic-fidelity interpretation

AF-414 correctly detected that bounded-complexity leading-term dominance fails on `x=c/n`: every fixed excess degree survives, and the first correction has the opposite sign. AF-415 then showed that the complete exceptional-`1` partition family restores a positive Schur-Cauchy exponential after resummation. AF-416 shows that this restoration survives the **whole determinant**: the omitted-`1` family and the one-/zero-singular-block sectors are separated from the leading sector by explicit super-polynomial baseline ratios.

This is a concrete fidelity lesson. A finite or fixed-complexity audit can reveal a genuine loss of dominance without determining the sign of the fully retained relational object. Here the sign becomes visible only after preserving the complete partition organization and all determinant sectors. The successful compression certificate is therefore not one leading monomial but a structured family together with its scale hierarchy.

The result is still source-analytic rather than prime-specific. No rational-prime discriminator enters the proof, and no RH implication follows from `(1)` without an independent theorem connecting this translation-sign hierarchy to continued zeta-zero geometry.

## Prior-art and novelty audit

The determinant multilinearity, Cauchy--Binet expansion, generalized Vandermonde/Schur identities, hook-content growth, and Schur Cauchy identity used here are classical. I. G. Macdonald, *Symmetric Functions and Hall Polynomials*, 2nd ed., Oxford University Press (1995), Chapter I, is a standard source for the Schur identities. Andrei Okounkov, **“Infinite wedge and random partitions,”** *Selecta Mathematica (N.S.)* 7(1), 57--81 (2001), arXiv:`math/9907127`, provides the classical Schur-measure normalization context used already in AF-415.

Bernoulli/Euler Hankel determinants are also established mathematics. Karl Dilcher and Lin Jiu, **“Hankel determinants of sequences related to Bernoulli and Euler polynomials,”** *International Journal of Number Theory* 18(2), 331--359 (2022), DOI `10.1142/S179304212250021X`, study many such sequence determinants. Double-scaling asymptotics for Hankel determinants occur in other varying-weight settings; for example Chao Min and Yang Chen, **“Painlevé V and the Hankel Determinant for a Singularly Perturbed Jacobi Weight,”** arXiv:`2006.14757`, analyze a different moment determinant under `n\to\infty`, `t\to0` scaling.

Those neighboring results do not supply `(1)`: this derivative-Hankel Euler-log matrix has a signed discrete Bernoulli germ plus the rank-two logarithmic block `(2)`, rather than a positive varying moment weight. A targeted search did not locate a theorem for this exact profile or the sector comparison `(17)`--`(26)`. No novelty claim is made; the durable contribution is the exact specialization and closure of the previously explicit AF-415 remainder classes using classical machinery.

## Boundaries and falsification checks

- The convergence is local uniformity for `c` in compact subsets of `(0,\infty)`. It does not treat `c=c_n\to0` or `c_n\to\infty`.
- The result closes the `x=c/n` corridor only. A large-order left-tail failure, if one exists, must migrate to a different joint scale.
- The positivity conclusion is for the full confluent determinant `H_{n+3}` on this diagonal. It is not an all-order total-positivity theorem for the translation kernel.
- The proof depends on the exact support `\{1,2,4,6,\ldots\}`, Bernoulli/zeta coefficient ratios, and the rank-two form `(2)`. Changing the analytic germ or singular-block rank can change both the baseline hierarchy and the resummed limit.
- The absolute Schur bounds prove uniform control but are intentionally crude; the constants `9,18,72` are majorants, not transition thresholds.
- Positivity of `(1)` supplies no arithmetic-prime discriminator and no RH consequence by itself.

## Consequence for the research line

`CLUE-left-tail-diagonal-order-drift-scale` is resolved positively: the exact full Euler-log derivative-Hankel determinant has the uniform positive limit `(1)` on the reciprocal-order left-tail corridor. The AF-414 opposite-sign correction survives at fixed excess degree but belongs to the Taylor expansion of a positive resummed object; the determinant sectors omitted by AF-415 vanish relative to that object.

The unresolved large-order question is therefore narrower than before. Any left-tail obstruction compatible with AF-217 must escape every compact `nx=c` corridor rather than arise from the natural reciprocal-order balance itself. Determining the next admissible joint scale, if any, is a separate research question and should not be inferred from `(1)` alone.