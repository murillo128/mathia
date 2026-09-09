# FD-005 — Möbius total-sum compatibility still does not improve the leading Franel--Mertens dual constant

**Status:** `EXACT-DERIVED + AFFINE-MOBIUS-CONSTRAINT + SHARP-CONSTRAINED-DUALITY + NEGATIVE/OBSTRUCTION + PRIOR-ART-AUDITED`. `FD-003` identifies the complete quadratic Franel discrepancy with the normalized square-GCD form

\[
K_N(d,e)=\frac{\gcd(d,e)^2}{de}
\]

on the divisor-scale Mertens vector

\[
m_d=\mathbf M\!\left(\left\lfloor\frac Nd\right\rfloor\right),
\qquad 1\le d\le N,
\]

and computes the unrestricted sharp coordinate constant `C_N -> zeta(2)`. `FD-004` then imposes the exact Dirichlet-hyperbola block constancy of this vector and proves that the restricted constant still tends to `zeta(2)`.

The physical Mertens staircase satisfies a stronger exact compatibility,

\[
\boxed{
\sum_{d=1}^N
\mathbf M\!\left(\left\lfloor\frac Nd\right\rfloor\right)=1.
}
\tag{1}
\]

This additional affine constraint is still insufficient to improve the leading scalar-dual coefficient. Let `H_N` be the `FD-004` subspace of vectors constant on equal `floor(N/d)` fibers and define

\[
S_N:=\{w\in H_N:\mathbf 1^Tw=0\},
\qquad
A_N:=\{v\in H_N:\mathbf 1^Tv=1\}.
\tag{2}
\]

Put

\[
\Lambda_N:=
\sup_{0\ne w\in S_N}
\frac{w_1^2}{w^TK_Nw},
\qquad
\Xi_N:=
\sup_{v\in A_N}
\frac{v_1^2}{v^TK_Nv}.
\tag{3}
\]

Then

\[
\boxed{
\Lambda_N\le\Xi_N\le\Gamma_N\le C_N,
}
\tag{4}
\]

where `Gamma_N` is the block-constant sharp constant of `FD-004`, and moreover

\[
\boxed{
\Lambda_N\longrightarrow\zeta(2),
\qquad
\Xi_N\longrightarrow\zeta(2).
}
\tag{5}
\]

More quantitatively, with

\[
R_N:=\max\{r:r(r+1)\le N\}\asymp\sqrt N,
\]

one has

\[
\boxed{
0\le\zeta(2)-\Lambda_N
\ll \frac{(\log N)^2}{\sqrt N},
\qquad
0\le\zeta(2)-\Xi_N
\ll \frac{(\log N)^2}{\sqrt N}.
}
\tag{6}
\]

Thus the exact block structure **plus** the exact total-sum Möbius identity still leave asymptotically sharp directions for extracting `M(N)` from the Franel--Mertens GCD energy. In the Franel normalization, the optimal leading coefficient supplied by these two constraints alone still tends to

\[
12\zeta(2)=2\pi^2.
\]

Any genuine cumulative-side gain must therefore use stronger compatibility among the actual Mertens values than equal-floor block constancy and the single identity (1), or the line must retain ordered Farey information before cumulative shell collapse.

## 1. The physical staircase satisfies the affine constraint exactly

By definition,

\[
\mathbf M(y)=\sum_{n\le y}\mu(n).
\]

Therefore

\[
\begin{aligned}
\sum_{d=1}^N\mathbf M(\lfloor N/d\rfloor)
&=\sum_{d\le N}\sum_{n\le N/d}\mu(n)\\
&=\sum_{n\le N}\mu(n)\left\lfloor\frac Nn\right\rfloor\\
&=\sum_{k\le N}\sum_{n\mid k}\mu(n)\\
&=1.
\end{aligned}
\tag{7}
\]

The last step is the elementary Möbius identity

\[
\sum_{n\mid k}\mu(n)=\mathbf1_{k=1}.
\]

Hence the physical vector `m` lies in the affine slice `A_N` of (2), not merely in the block-constant subspace `H_N`.

This recurrence is classical in algorithms for isolated Mertens values. Deléglise--Rivat use the same floor-quotient Möbius structure in their elementary computation of `M(x)`. Equation (7) is proved here directly; no algorithmic complexity result is imported.

## 2. The sharp zero-sum coordinate norm has an exact projection formula

The first `R_N` coordinates are singleton floor fibers by `FD-004`. Consequently every vector supported on `{1,\ldots,R_N}` belongs to `H_N`, and every such vector with coordinate sum zero belongs to `S_N`.

Fix an integer `R>=2` and let `K_R` be the `R x R` principal square-GCD matrix. Define

\[
C_R:=e_1^TK_R^{-1}e_1,
\qquad
A_R:=e_1^TK_R^{-1}\mathbf1,
\qquad
B_R:=\mathbf1^TK_R^{-1}\mathbf1.
\tag{8}
\]

The `K_R`-orthogonal complement of the Euclidean zero-sum hyperplane

\[
\{w:\mathbf1^Tw=0\}
\]

is spanned by `K_R^{-1}\mathbf1`, because

\[
\langle w,K_R^{-1}\mathbf1\rangle_{K_R}
=w^T\mathbf1.
\]

Project the unrestricted Riesz representer `K_R^{-1}e_1` onto that zero-sum hyperplane. The squared norm of the projected representer is therefore

\[
\boxed{
C_R^{(0)}
:=\sup_{\substack{0\ne w\in\mathbb R^R\\\mathbf1^Tw=0}}
\frac{w_1^2}{w^TK_Rw}
=C_R-\frac{A_R^2}{B_R}.
}
\tag{9}
\]

This is an exact constrained Hilbert-space identity, not an asymptotic estimate. The correction is nonnegative, so the affine information can improve the finite constant. The question is whether it removes a fixed part of the limiting `zeta(2)` coefficient. It does not.

## 3. Smith--Jordan inversion evaluates all three terms

`FD-003` gives

\[
K_R^{-1}
=D E^{-1}J^{-1}(E^{-1})^TD,
\tag{10}
\]

where `D=diag(1,\ldots,R)`, `J=diag(J_2(1),\ldots,J_2(R))`, and

\[
(E^{-1})_{r,d}
=\mu(d/r)\mathbf1_{r\mid d}.
\]

The first term is already known:

\[
\boxed{
C_R=\sum_{r\le R}\frac{\mu(r)^2}{J_2(r)}.
}
\tag{11}
\]

For the remaining terms, note that

\[
((E^{-1})^TD\mathbf1)_r
=\sum_{d\mid r}d\,\mu(r/d)
=\varphi(r).
\tag{12}
\]

Substitution into (10) gives the exact formulas

\[
\boxed{
A_R
=\sum_{r\le R}\frac{\mu(r)\varphi(r)}{J_2(r)},
}
\tag{13}
\]

and

\[
\boxed{
B_R
=\sum_{r\le R}\frac{\varphi(r)^2}{J_2(r)}.
}
\tag{14}
\]

Equation (13) can also be read directly from the first row of the inverse. No cancellation estimate for the Mertens function enters these identities.

## 4. The projection correction is only `O((log R)^2/R)`

First bound the numerator in (9). When `\mu(r)\ne0`, `r` is squarefree and

\[
\frac{\varphi(r)}{J_2(r)}
=\prod_{p\mid r}\frac1{p+1}
\le\frac1r.
\tag{15}
\]

Hence

\[
\boxed{|A_R|\le\sum_{r\le R}\frac1r\ll\log R.}
\tag{16}
\]

The denominator in (9) is actually linear in `R`. Put

\[
f(n):=\frac{\varphi(n)^2}{J_2(n)}
=\prod_{p\mid n}\frac{p-1}{p+1}.
\tag{17}
\]

Write `f=\mathbf1*g` in Dirichlet-convolution notation, where `g` is multiplicative, supported on squarefree integers, and

\[
g(p)=-\frac2{p+1}.
\tag{18}
\]

Then

\[
\sum_{d\ge1}\frac{|g(d)|}{d}
=\prod_p\left(1+\frac2{p(p+1)}\right)<\infty,
\tag{19}
\]

while

\[
b:=\sum_{d\ge1}\frac{g(d)}d
=\prod_p\left(1-\frac2{p(p+1)}\right)>0.
\tag{20}
\]

Therefore

\[
\begin{aligned}
B_R
&=\sum_{n\le R}f(n)\\
&=\sum_{d\le R}g(d)\left\lfloor\frac Rd\right\rfloor
=bR+o(R).
\end{aligned}
\tag{21}
\]

For completeness, the error statement follows only from the absolute convergence in (19): the truncated coefficient sum in (20) tends to `b`, and `\sum_{d\le R}|g(d)|=o(R)` by the elementary Kronecker/partial-summation consequence of `\sum |g(d)|/d<\infty`. No prime number theorem or zero-free region is used.

Combining (16) and (21),

\[
\boxed{
0\le\frac{A_R^2}{B_R}
\ll\frac{(\log R)^2}{R}.
}
\tag{22}
\]

Together with the `FD-003` tail bound

\[
0\le\zeta(2)-C_R\le\frac{\zeta(2)}R,
\tag{23}
\]

formula (9) yields

\[
\boxed{
0\le\zeta(2)-C_R^{(0)}
\ll\frac{(\log R)^2}{R}.
}
\tag{24}
\]

Thus the exact zero-sum condition removes only a vanishing part of the sharp coordinate norm on growing principal blocks.

## 5. The zero-sum extremizers embed inside the true hyperbola quotient

Take `R=R_N`. Since all indices `1<=d<=R_N` are singleton floor fibers, every `R`-vector realizing or approximating the supremum in (9), padded by zeros through coordinate `N`, belongs to `S_N`. Therefore

\[
\boxed{C_{R_N}^{(0)}\le\Lambda_N.}
\tag{25}
\]

On the other hand `S_N subset H_N subset R^N`, so

\[
\Lambda_N\le\Gamma_N\le C_N\le\zeta(2).
\tag{26}
\]

Equations (24)--(26) prove

\[
\boxed{
\Lambda_N\to\zeta(2).
}
\tag{27}
\]

Since `R_N\asymp\sqrt N`, they also give the quantitative bound in (6).

This is the key obstruction. The block-constant class contains an expanding family of **zero-total-sum** directions whose coordinate dual constants already approach the unrestricted Smith-matrix limit.

## 6. Passing from the zero-sum tangent space to the physical affine slice

The affine slice `A_N` is nonempty: `e_1 in H_N` and `\mathbf1^Te_1=1`. For any nonzero `w in S_N`, consider

\[
v_t=e_1+t w.
\tag{28}
\]

Then `v_t in A_N` for every real `t`, and positive definiteness gives

\[
\lim_{|t|\to\infty}
\frac{(v_t)_1^2}{v_t^TK_Nv_t}
=rac{w_1^2}{w^TK_Nw}.
\tag{29}
\]

Taking the supremum first over `t` and then over `w` gives

\[
\boxed{\Lambda_N\le\Xi_N.}
\tag{30}
\]

The reverse ambient bound is immediate because `A_N subset H_N`:

\[
\Xi_N\le\Gamma_N.
\tag{31}
\]

Together with (27) and `Gamma_N->zeta(2)` from `FD-004`, this proves

\[
\boxed{\Xi_N\to\zeta(2).}
\tag{32}
\]

The affine identity (1) therefore does not remove the asymptotically dangerous dual directions. It merely translates the zero-sum tangent family; along large multiples of those tangent directions the fixed affine offset is negligible in the quadratic ratio.

## 7. Consequence for the Franel--Mertens extraction

For the actual Mertens vector,

\[
m\in A_N,
\qquad
m_1=\mathbf M(N),
\]

and `FD-003` gives

\[
12\left(M_N\mathfrak F_N+\frac1{12}\right)
=m^TK_Nm.
\tag{33}
\]

If one uses **only** membership in `A_N` to bound the first coordinate by this energy, the sharp homogeneous scalar coefficient is `Xi_N`:

\[
|\mathbf M(N)|^2
\le
12\Xi_N\left(M_N\mathfrak F_N+\frac1{12}\right).
\tag{34}
\]

Equations (5)--(6) show that its leading constant is still

\[
12\Xi_N\longrightarrow2\pi^2.
\tag{35}
\]

This closes the next obvious cumulative relaxation after `FD-004`. The exact floor-quotient block structure and the exact total-sum recurrence together are not enough to improve the leading scalar extraction from the complete Franel energy.

The result does **not** say that (34) is sharp for actual Möbius values. The extremizing affine vectors in Section 6 are arbitrary real block-constant vectors satisfying only one Möbius identity, not genuine Mertens staircases. Stronger relations remain available because all coordinates arise as partial sums of one common `{−1,0,1}` Möbius sequence and satisfy many linked divisor/floor recurrences. Those are now the cumulative-side information that a further theorem must use.

Nor does this finding rule out a useful nonhomogeneous inequality exploiting the fixed affine offset, or a theorem whose main gain is not a scalar coordinate extraction. It rules out a narrower but important shortcut: **adding the single exact identity (1) to hyperbola-block constancy cannot change the leading homogeneous dual constant.** Ordered gaps, adjacency, mediant ancestry, and refinement chronology remain untouched.

## 8. Prior art, audit, and evidence boundary

The floor-quotient recurrence (7) is classical Möbius inversion and is used in the computation of isolated Mertens values; Marc Deléglise and Joël Rivat, *Computing the Summation of the Möbius Function*, Experimental Mathematics **5**(4) (1996), 291--295, DOI `10.1080/10586458.1996.10504594`, is a primary computational prior-art boundary. Smith/Jordan GCD-matrix inversion and the unrestricted coordinate norm are already anchored in `FD-003` and `SOURCES.md`. Formula (9) is ordinary constrained Riesz-representer projection, and the mean-value argument for (21) is elementary absolutely convergent multiplicative convolution.

A targeted search across Mertens floor-quotient recurrences, GCD-matrix inversion, and constrained quadratic forms did not locate the specific `FD-003`/`FD-004` splice (9)--(32). That absence is not evidence of novelty. The durable Mathia contribution is the line-specific negative boundary: the first stronger exact Möbius compatibility explicitly left open in `FD-004` can be imposed and still does not alter the asymptotic scalar dual coefficient.

The proof was stress-tested against four failure modes. First, the affine class is not illegally rescaled: the large parameter multiplies a zero-sum tangent direction, so (28) remains in `A_N` exactly. Second, the lower-bound witness is supported only on the rigorously singleton range `R_N`; no freedom beyond that range is assumed. Third, (21) does not use cancellation of `mu` or the prime number theorem. Fourth, finite improvement is not confused with asymptotic improvement: `C_R^(0)<C_R` can be strict, but (24) proves that the difference relevant to the limiting coefficient vanishes.

No new bound for the true Mertens function, Franel discrepancy, ordered Farey statistic, or RH is proved. The next cumulative-side question must impose stronger source compatibility than block constancy plus the total-sum identity, while the independent pre-cumulative route remains the search for an ordered Farey invariant that survives collapse to the classical scalar discrepancy.
