# FD-012 — a logarithmic Jordan-moment depth still leaves the Franel--Mertens dual constant sharp

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + GROWING-MOMENT-HIERARCHY + UNIFORM-PRIME-SAMPLING + NEGATIVE/OBSTRUCTION`. `FD-006` proves that every fixed finite initial segment of the exact Jordan-moment hierarchy leaves the leading homogeneous coordinate constant of the Franel--Mertens GCD energy equal to `zeta(2)` asymptotically, but its constants depend on the depth. That dependence can be controlled uniformly far beyond fixed depth. A quantitative polynomial-sampling argument on a dyadic prime interval, combined with an explicit exponential lower bound for the monomial moment matrix, shows that a genuinely growing logarithmic number of exact Jordan moments is still asymptotically harmless.

Let

\[
K_N(d,e)=\frac{\gcd(d,e)^2}{de},
\qquad
H_N=\{\text{vectors constant on equal }\lfloor N/d\rfloor\text{ fibers}\},
\]

and, for an integer depth `h>=0`, retain the tangent and affine classes of `FD-006`,

\[
\mathcal S_{N,h}
=\left\{w\in H_N:\sum_{d\le N}d^s w_d=0
\text{ for }0\le s\le h\right\},
\tag{1}
\]

with `mathcal A_(N,h)` having the physical right sides

\[
\sum_{d\le N}d^s M(\lfloor N/d\rfloor)
=\sum_{n\le N}J_s(n).
\tag{2}
\]

Define

\[
\Lambda_{N,h}
=\sup_{0\ne w\in\mathcal S_{N,h}}
\frac{w_1^2}{w^TK_Nw},
\qquad
\Xi_{N,h}
=\sup_{v\in\mathcal A_{N,h}}
\frac{v_1^2}{v^TK_Nv}.
\tag{3}
\]

Put

\[
R_N:=\max\{R:R(R+1)\le N\}\asymp\sqrt N,
\qquad n=h+1.
\tag{4}
\]

There is an absolute constant `C` such that, whenever `R=R_N` is sufficiently large and

\[
n^3 2304^n(\log R)^3\le cR
\tag{5}
\]

for a sufficiently small absolute `c`, one has

\[
\boxed{
0\le\zeta(2)-\Lambda_{N,h}
\le
\frac{\zeta(2)}R
+C\frac{n^3 2304^n(\log R)^3}{R},
}
\tag{6}
\]

and the same upper bound for `zeta(2)-Xi_(N,h)`. Consequently, for every integer sequence `h_N` satisfying

\[
(h_N+1)^3 2304^{h_N+1}(\log N)^3=o(\sqrt N),
\tag{7}
\]

one has

\[
\boxed{
\Lambda_{N,h_N}\to\zeta(2),
\qquad
\Xi_{N,h_N}\to\zeta(2).
}
\tag{8}
\]

In particular this holds for every `h_N=o(log N)`, and more strongly for every fixed `epsilon>0` under the explicit logarithmic regime

\[
\boxed{
h_N\le
\left(\frac1{2\log 2304}-\varepsilon\right)\log N}
\tag{9}
\]

for all sufficiently large `N`. The numerical constant `2304` is deliberately crude and carries no claim of optimality.

Thus the cumulative Farey route cannot obtain a persistent improvement of the leading scalar Franel--Mertens coefficient merely by allowing the **number of exact polynomial/Jordan moment identities to grow slowly, or even at a small fixed positive multiple of `log N`**. This is still a statement about the homogeneous relaxation: it does not show that a deeper logarithmic hierarchy is harmless, that logarithmic depth is a sharp boundary, or that the corresponding tangent extremizers are realizable by one Möbius sign sequence.

## 1. The finite constrained constant remains an exact projected Smith inverse

Work first with the principal `R x R` matrix `K_R`. For `0<=s<=h`, put

\[
a_s=(1^s,2^s,\ldots,R^s)^T,
\qquad A=(a_0,\ldots,a_h).
\]

As in `FD-006`, the moment-zero tangent space is `ker A^T`. The `K_R`-Riesz representer of the first coordinate is `K_R^{-1}e_1`, so orthogonal projection gives exactly

\[
\boxed{
C_R^{[h]}
:=\sup_{0\ne w\in\ker A^T}
\frac{w_1^2}{w^TK_Rw}
=C_R-b^TG^{-1}b,
}
\tag{10}
\]

where

\[
C_R=e_1^TK_R^{-1}e_1,
\qquad
b_s=e_1^TK_R^{-1}a_s,
\qquad
G_{st}=a_s^TK_R^{-1}a_t.
\tag{11}
\]

The Smith--Jordan factorization used in `FD-003` and `FD-006` gives the exact arithmetic formulas

\[
\boxed{
b_s=\sum_{r\le R}
\frac{\mu(r)J_{s+1}(r)}{J_2(r)},}
\qquad
\boxed{G_{st}=\sum_{r\le R}
\frac{J_{s+1}(r)J_{t+1}(r)}{J_2(r)}.}
\tag{12}
\]

No asymptotic input enters (10)--(12). The only new issue relative to `FD-006` is controlling the inverse constraint Gram uniformly when `h` grows.

Scale the `s`-th constraint by `R^{-s}` and write

\[
\widetilde b_s=R^{-s}b_s,
\qquad
\widetilde G_{st}=R^{-(s+t)}G_{st}.
\tag{13}
\]

The projection loss is invariant under this rescaling:

\[
b^TG^{-1}b
=\widetilde b^T\widetilde G^{-1}\widetilde b.
\tag{14}
\]

For `s=0`, squarefree support in (12) gives

\[
|\widetilde b_0|
\le\sum_{r\le R}\frac1r
\le1+\log R.
\tag{15}
\]

For every `s>=1`,

\[
\frac{J_{s+1}(r)}{J_2(r)}
\le\zeta(2)r^{s-1},
\]

so

\[
|\widetilde b_s|\le2\zeta(2)
\tag{16}
\]

for all `R>=2`. Hence

\[
\boxed{
\|\widetilde b\|_2^2
\ll (\log R)^2+n.}
\tag{17}
\]

This bound is uniform in the depth.

## 2. A dyadic prime interval samples every growing-degree constraint polynomial

The scaled Gram has the rank-one representation

\[
\widetilde G
=\sum_{r\le R}q(r)q(r)^T,
\qquad
q_s(r)=\frac{J_{s+1}(r)}{R^s\sqrt{J_2(r)}}.
\tag{18}
\]

Discard every nonprime term and retain only primes `R/2<p<=R`. Put

\[
x_p=p/R,
\qquad
v(p)=(1,x_p,\ldots,x_p^h)^T.
\tag{19}
\]

For a prime,

\[
q_s(p)
=\frac{p^{s+1}-1}{R^s\sqrt{p^2-1}}.
\]

Uniformly for every `s>=0` and `R/2<p<=R`,

\[
\boxed{|q_s(p)-x_p^s|\le C/R.}
\tag{20}
\]

The case `s=0` costs `O(1/p)`; for `s>=1` the relative error is already `O(p^{-2})`. Thus (20) remains valid even while the number of coordinates grows.

For `y in R^n`, define

\[
P_y(x)=\sum_{s=0}^hy_sx^s,
\qquad
I_y=\int_{1/2}^1P_y(x)^2\,dx.
\tag{21}
\]

We need a lower sampling inequality for `P_y` at the primes that is uniform in its degree. Use the classical de la Vallée Poussin prime-number-theorem error in Chebyshev form

\[
\vartheta(t)
=t+O\!\left(t e^{-c_0\sqrt{\log t}}\right).
\tag{22}
\]

Stieltjes summation gives

\[
\sum_{R/2<p\le R}\log p\,P_y(p/R)^2
=R I_y
+O\!\left(
R e^{-c_0\sqrt{\log R}}
\left(\|P_y\|_\infty^2
+\|P_y\|_\infty\|P_y'\|_\infty\right)
\right).
\tag{23}
\]

On `[1/2,1]`, the elementary polynomial Nikolskii and Markov inequalities give

\[
\|P_y\|_\infty^2\ll n^2 I_y,
\qquad
\|P_y'\|_\infty\ll h^2\|P_y\|_\infty.
\tag{24}
\]

Therefore the error in (23) is `O(R exp(-c_0 sqrt(log R)) n^4 I_y)`. Uniformly whenever `n=O(log R)`, it is `o(R I_y)`. Since `log p<=log R`, for all sufficiently large `R` in this regime,

\[
\boxed{
\sum_{R/2<p\le R}P_y(x_p)^2
\ge\frac{R}{2\log R}I_y.}
\tag{25}
\]

This is the step that the fixed-dimensional argument of `FD-006` did not need: the prime reservoir remains quantitatively coercive on a polynomial space whose dimension itself grows.

## 3. The monomial basis pays only an explicit exponential conditioning tax

The sampling inequality controls the `L^2` norm of the polynomial, whereas the projection estimate needs the Euclidean norm of its coefficient vector. A crude explicit finite-dimensional bound is enough.

Let

\[
H_h=(\int_{1/2}^1x^{s+t}dx)_{0\le s,t\le h},
\]

so `I_y=y^TH_hy`. Put `u=2x-1` and write

\[
Q(u)=P_y((1+u)/2)=\sum_{j=0}^h z_j u^j.
\]

Then

\[
I_y=\frac12 z^T\mathcal H_nz,
\qquad
(\mathcal H_n)_{ij}=\frac1{i+j+1},
\tag{26}
\]

where `mathcal H_n` is the classical `n x n` Hilbert matrix. Its exact inverse formula, together with the elementary bound on binomial coefficients, gives

\[
\|\mathcal H_n^{-1}\|_2\le n^2 256^n.
\tag{27}
\]

Conversely `P_y(x)=Q(2x-1)`. The sum of absolute coefficients of `(2x-1)^j` is `3^j`; hence the coefficient-change matrix has operator norm at most `\sqrt n\,3^n`. Combining these two deliberately coarse bounds yields

\[
\boxed{
I_y
\ge\frac{\|y\|_2^2}{2n^3 2304^n}.}
\tag{28}
\]

Neither `256` nor `2304` is intended to be sharp. The important feature is exponential rather than superexponential loss in the degree.

## 4. The prime Gram dominates the growing moment matrix

For each retained prime write

\[
q(p)=v(p)+\delta(p).
\]

Equation (20) gives

\[
\|\delta(p)\|_2^2\ll n/R^2.
\tag{29}
\]

Using `(a+b)^2>=a^2/2-b^2`, equations (25) and (29) imply

\[
\begin{aligned}
y^T\widetilde Gy
&\ge\sum_{R/2<p\le R}(y\cdot q(p))^2\\
&\ge\frac12\sum_{R/2<p\le R}P_y(x_p)^2
-C\frac nR\|y\|_2^2.
\end{aligned}
\tag{30}
\]

By (28), the error term in (30) is at most

\[
C\frac{n^4 2304^n}{R}I_y.
\tag{31}
\]

Under the regime (5), this is negligible compared with the main term `R I_y/log R`. Hence, after enlarging the absolute threshold for `R`,

\[
\boxed{
y^T\widetilde Gy
\ge\frac{R}{8\log R}I_y
\ge
\frac{R}{16n^3 2304^n\log R}\|y\|_2^2.}
\tag{32}
\]

Therefore

\[
\boxed{
\lambda_{\min}(\widetilde G)
\ge
\frac{R}{16n^3 2304^n\log R}.}
\tag{33}
\]

Combining (17), (14), and (33) gives

\[
\boxed{
0\le b^TG^{-1}b
\ll
\frac{n^3 2304^n(\log R)^3}{R}}
\tag{34}
\]

throughout (5). Since `FD-003` gives

\[
0\le\zeta(2)-C_R\le\frac{\zeta(2)}R,
\tag{35}
\]

equations (10) and (34)--(35) prove the principal-block version of (6).

## 5. The growing-depth extremizers still embed in the actual hyperbola quotient

For `R=R_N`, the coordinates `1<=d<=R` belong to distinct `floor(N/d)` fibers. Thus a principal `R`-vector in the tangent space of all moments through degree `h`, padded by zeros, lies in the actual equal-floor tangent `mathcal S_(N,h)`. Consequently

\[
C_R^{[h]}\le\Lambda_{N,h}\le\zeta(2).
\tag{36}
\]

This proves (6) for `Lambda`. The physical affine slice is nonempty because the actual Mertens staircase satisfies (2) at every finite depth. Given any `v_0 in mathcal A_(N,h)` and nonzero `w in mathcal S_(N,h)`, the ray `v_0+t w` remains in the affine slice and

\[
\lim_{|t|\to\infty}
\frac{(v_0+t w)_1^2}
{(v_0+t w)^TK_N(v_0+t w)}
=\frac{w_1^2}{w^TK_Nw}.
\tag{37}
\]

Hence

\[
\Lambda_{N,h}\le\Xi_{N,h}\le\zeta(2),
\tag{38}
\]

and the same deficit bound follows for `Xi`. Conditions (7)--(9) are immediate from `R_N asymp sqrt N`.

For the true Farey quantity, `FD-003` gives

\[
12\left(M_N\mathfrak F_N+\frac1{12}\right)
=m^TK_Nm,
\]

so any homogeneous scalar extraction using only the first `h_N+1` exact Jordan-moment identities continues to have asymptotically sharp leading coefficient `zeta(2)`, equivalently the same Franel factor `12 zeta(2)=2 pi^2`, throughout (7).

## 6. Prior art, controls, and research consequence

The identities defining the Jordan hierarchy and the Smith/GCD factorization are classical and already anchored in `FD-003`--`FD-006`. The new uniform ingredient is only the quantitative prime sampling needed when polynomial degree grows. De la Vallée Poussin's classical zero-free-region argument supplies the unconditional error (22); no RH, density hypothesis, or RH-equivalent prime-distribution estimate is imported. The Hilbert inverse formula, Markov inequality, and polynomial norm comparison are classical finite-dimensional tools; the deliberately crude constants above are derived only to keep the depth dependence explicit.

A targeted literature audit across Farey/Franel discrepancy, Mertens floor-quotient identities, Jordan-totient moments, constrained GCD/Smith matrices, and growing-degree moment systems did not locate this combined obstruction. That absence is not evidence of historical novelty. The Mathia-specific durable delta is the explicit growing-depth boundary: the fixed-depth no-go of `FD-006` persists through every regime satisfying (7), including a nonzero logarithmic depth window.

Several limitations are load-bearing. First, (9) is a sufficient range produced by rough conditioning constants, not a sharp threshold; failure beyond it is completely open. Second, these are **Jordan moments**, not the consecutive divisor-horizon constraints of `FD-009`: the latter recover the Möbius prefix pointwise, so increasing moment depth and increasing horizon depth have fundamentally different information content. Third, the extremizing tangent vectors are arbitrary real vectors; the theorem does not make them partial sums of a single squarefree multiplicative sign sequence. Fourth, the result is homogeneous and does not exclude a useful affine/nonlinear estimate. Finally, it says nothing about ordered Farey gaps, refinement ancestry, controlled Plücker fields, or spectral allocation before denominator-shell collapse.

The cumulative frontier is therefore narrower than after `FD-006`: **neither fixed depth nor a substantial slowly growing/logarithmic depth of the natural exact Jordan hierarchy can improve the leading scalar dual constant.** A surviving cumulative mechanism must pay for source information that this polynomial hierarchy does not capture—such as stronger nonlinear/multiplicative sign correlation, a compressed growing-depth condition outside this moment family, or a regime beyond the present logarithmic conditioning bound—without simply crossing the lossless reconstruction boundary of `FD-009`.