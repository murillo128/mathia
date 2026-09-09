# FD-006 — every fixed Jordan-moment hierarchy still leaves the Franel--Mertens leading dual constant unchanged

**Status:** `EXACT-DERIVED + FIXED-MOMENT-HIERARCHY + SHARP-CONSTRAINED-DUALITY + NEGATIVE/OBSTRUCTION + PNT-AUXILIARY`. `FD-003` identifies the complete quadratic Franel discrepancy with the normalized square-GCD form

\[
K_N(d,e)=\frac{\gcd(d,e)^2}{de}
\]

on the divisor-scale Mertens staircase

\[
m_d=\mathbf M\!\left(\left\lfloor\frac Nd\right\rfloor\right).
\]

`FD-004` shows that exact `floor(N/d)` block constancy does not improve the leading scalar-dual coefficient, and `FD-005` adds the exact compatibility `sum_d m_d=1` with the same negative outcome. That single identity belongs to a complete elementary hierarchy. For every fixed integer `h>=0`, the physical staircase satisfies

\[
\boxed{
\sum_{d=1}^N d^s\,
\mathbf M\!\left(\left\lfloor\frac Nd\right\rfloor\right)
=\sum_{n=1}^N J_s(n)
\qquad(0\le s\le h),
}
\tag{1}
\]

where `J_s` is Jordan's `s`-th totient for `s>=1`, and `J_0(n)=1_{n=1}`. Thus the `s=0` identity is exactly the total-sum constraint of `FD-005`, while `s=1` gives the cumulative Euler-totient constraint and higher `s` give cumulative Jordan-totient constraints.

Imposing **any fixed finite initial segment of this hierarchy still does not change the leading homogeneous coordinate constant**. Let `H_N` be the equal-floor block subspace of `FD-004`, let

\[
\mathcal S_{N,h}
:=\left\{w\in H_N:
\sum_{d=1}^N d^s w_d=0\text{ for }0\le s\le h
\right\},
\tag{2}
\]

and let `mathcal A_{N,h}` be the corresponding affine slice with right sides from (1). Define

\[
\Lambda_{N,h}
:=\sup_{0\ne w\in\mathcal S_{N,h}}
\frac{w_1^2}{w^T K_Nw},
\qquad
\Xi_{N,h}
:=\sup_{v\in\mathcal A_{N,h}}
\frac{v_1^2}{v^T K_Nv}.
\tag{3}
\]

Then for every fixed `h`,

\[
\boxed{
\Lambda_{N,h}\longrightarrow\zeta(2),
\qquad
\Xi_{N,h}\longrightarrow\zeta(2).
}
\tag{4}
\]

More quantitatively, with

\[
R_N:=\max\{R:R(R+1)\le N\}\asymp\sqrt N,
\]

one has

\[
\boxed{
0\le\zeta(2)-\Lambda_{N,h}
\ll_h\frac{(\log N)^3}{\sqrt N},
\qquad
0\le\zeta(2)-\Xi_{N,h}
\ll_h\frac{(\log N)^3}{\sqrt N}.
}
\tag{5}
\]

Consequently the exact hyperbola structure together with any **fixed number of polynomial/Jordan moment identities** still leaves asymptotically sharp directions for extracting `M(N)` from the Franel--Mertens GCD energy. In the Franel normalization, their optimal leading homogeneous coefficient remains

\[
12\zeta(2)=2\pi^2.
\]

The remaining cumulative route must therefore use compatibility of unbounded depth, a genuinely nonlinear restriction of the `{−1,0,1}` Möbius increments, or another source condition that does not reduce to finitely many fixed linear moments. Ordered Farey information before cumulative shell collapse remains a separate live route.

## 1. The Mertens staircase satisfies the whole Jordan-moment hierarchy exactly

For every integer `s>=0`, expand the Mertens function before changing order:

\[
\begin{aligned}
\sum_{d\le N}d^s\mathbf M(\lfloor N/d\rfloor)
&=\sum_{d\le N}d^s
  \sum_{r\le N/d}\mu(r)\\
&=\sum_{rd\le N}\mu(r)d^s\\
&=\sum_{n\le N}\sum_{r\mid n}
  \mu(r)\left(\frac nr\right)^s.
\end{aligned}
\tag{6}
\]

For `s>=1`, the inner divisor sum is exactly Jordan's totient

\[
J_s(n)=n^s\prod_{p\mid n}(1-p^{-s})
=\sum_{r\mid n}\mu(r)(n/r)^s.
\tag{7}
\]

For `s=0` it is `sum_(r|n) mu(r)=1_{n=1}`. This proves (1) with no asymptotic input.

The identities are not independent arithmetic miracles: they are the polynomial-weighted forms of the same Möbius divisor inversion behind `FD-005`. Their relevance is that they give a natural increasing family of exact linear constraints on the **actual** vector consumed by the Franel GCD energy, rather than an artificial relaxation chosen for convenient geometry.

## 2. The exact fixed-depth constrained coordinate norm is a projected Smith inverse

First work on a principal `R x R` square-GCD matrix `K_R`. For `0<=s<=h`, put

\[
a_s=(1^s,2^s,\ldots,R^s)^T
\]

and let `A_R` be the matrix with columns `a_0,...,a_h`. The moment-zero tangent space is

\[
V_{R,h}=\ker A_R^T.
\tag{8}
\]

Because `K_R` is positive definite, the Riesz representer of the first-coordinate functional is

\[
u_R=K_R^{-1}e_1.
\]

The `K_R`-orthogonal complement of `V_{R,h}` is the span of the vectors `K_R^{-1}a_s`. Therefore the squared norm of the projection of `u_R` onto `V_{R,h}` is

\[
\boxed{
C_R^{[h]}
:=\sup_{0\ne w\in V_{R,h}}
\frac{w_1^2}{w^T K_Rw}
=C_R-b_R^TG_R^{-1}b_R,
}
\tag{9}
\]

where

\[
C_R=e_1^TK_R^{-1}e_1,
\qquad
(b_R)_s=e_1^TK_R^{-1}a_s,
\qquad
(G_R)_{st}=a_s^TK_R^{-1}a_t.
\tag{10}
\]

The columns `a_s` are independent once `R>=h+1`, so `G_R` is positive definite. Formula (9) is exact finite-dimensional Hilbert geometry. For `h=0` it is precisely the zero-total-sum projection used in `FD-005`.

## 3. Smith--Jordan inversion converts every polynomial constraint to a Jordan totient

Use the divisor-incidence factorization of `FD-003`,

\[
K_R^{-1}
=D E^{-1}J^{-1}(E^{-1})^TD,
\tag{11}
\]

where `J=diag(J_2(1),...,J_2(R))` and

\[
(E^{-1})_{r,d}=\mu(d/r)\mathbf1_{r\mid d}.
\]

For a polynomial constraint column `a_s`,

\[
\left((E^{-1})^TD a_s\right)_r
=\sum_{d\mid r}d^{s+1}\mu(r/d)
=J_{s+1}(r).
\tag{12}
\]

The transformed first-coordinate vector is `mu(r)`. Hence the projection data in (10) have the exact arithmetic formulas

\[
\boxed{
(b_R)_s
=\sum_{r\le R}
\frac{\mu(r)J_{s+1}(r)}{J_2(r)},
}
\tag{13}
\]

and

\[
\boxed{
(G_R)_{st}
=\sum_{r\le R}
\frac{J_{s+1}(r)J_{t+1}(r)}{J_2(r)}.
}
\tag{14}
\]

Thus adding polynomial moments does not create an unrelated matrix problem. The same Jordan factorization that diagonalizes the Franel GCD energy also diagonalizes the constraint Gram matrix.

The numerator vector has a crude bound sufficient for the asymptotic result. For `s=0`, only squarefree `r` contribute to (13), and

\[
\frac{\varphi(r)}{J_2(r)}
=\prod_{p\mid r}\frac1{p+1}
\le\frac1r,
\]

so

\[
|(b_R)_0|\ll\log R.
\tag{15}
\]

For every fixed `s>=1`, when `mu(r)ne0`,

\[
\frac{J_{s+1}(r)}{J_2(r)}
=r^{s-1}
\prod_{p\mid r}
\frac{1-p^{-(s+1)}}{1-p^{-2}}
\le\zeta(2)r^{s-1},
\]

and therefore

\[
\boxed{|(b_R)_s|\ll_s R^s.}
\tag{16}
\]

## 4. The constraint Gram has enough mass on prime indices to make the projection loss vanish

Scale the `s`-th constraint by `R^{-s}`. This leaves the tangent space and the projection correction in (9) unchanged, while replacing `b_R,G_R` by

\[
\widetilde b_s=\frac{(b_R)_s}{R^s},
\qquad
\widetilde G_{st}=\frac{(G_R)_{st}}{R^{s+t}}.
\tag{17}
\]

Equations (15)--(16) give

\[
\boxed{\|\widetilde b\|^2\ll_h(\log R)^2.}
\tag{18}
\]

To lower-bound the Gram matrix, retain only prime indices `p` with `R/2<p<=R` in the nonnegative sum (14). For a prime,

\[
J_{s+1}(p)=p^{s+1}-1,
\qquad
J_2(p)=p^2-1,
\]

so uniformly for `0<=s,t<=h`,

\[
\frac{J_{s+1}(p)J_{t+1}(p)}
     {R^{s+t}J_2(p)}
=\left(\frac pR\right)^{s+t}+O_h(R^{-1}).
\tag{19}
\]

The prime number theorem and partial summation give, for each fixed integer `m>=0`,

\[
\frac{\log R}{R}
\sum_{R/2<p\le R}
\left(\frac pR\right)^m
\longrightarrow
\int_{1/2}^1x^m\,dx.
\tag{20}
\]

Therefore

\[
\frac{\log R}{R}\widetilde G_R
\succeq
H_h+o(1),
\qquad
(H_h)_{st}=\int_{1/2}^1x^{s+t}\,dx,
\tag{21}
\]

in the sense that the prime-index submatrix contribution converges entrywise to `H_h`. The moment matrix `H_h` is positive definite because

\[
y^TH_hy
=\int_{1/2}^1
\left(\sum_{s=0}^h y_sx^s\right)^2dx>0
\]

for every nonzero coefficient vector `y`. Since the dimension `h+1` is fixed, entrywise convergence implies a fixed spectral gap. Thus, for all sufficiently large `R`,

\[
\boxed{
\lambda_{\min}(\widetilde G_R)
\gg_h\frac R{\log R}.
}
\tag{22}
\]

Combining (18) and (22),

\[
\boxed{
0\le b_R^TG_R^{-1}b_R
=\widetilde b^T\widetilde G^{-1}\widetilde b
\ll_h\frac{(\log R)^3}{R}.
}
\tag{23}
\]

`FD-003` already gives

\[
0\le\zeta(2)-C_R\le\frac{\zeta(2)}R.
\tag{24}
\]

Equations (9), (23), and (24) therefore imply

\[
\boxed{
0\le\zeta(2)-C_R^{[h]}
\ll_h\frac{(\log R)^3}{R}.
}
\tag{25}
\]

The prime number theorem is used only as an unconditional auxiliary density statement ensuring that the fixed constraint family has a well-conditioned growing Gram reservoir. No zero-free quantitative error term, RH, or RH-equivalent estimate is imported.

## 5. The fixed-depth moment-zero extremizers embed in the true hyperbola quotient

Take `R=R_N` from `FD-004`. Every coordinate `1<=d<=R_N` is a singleton `floor(N/d)` fiber. Therefore every vector supported on the first `R_N` coordinates lies in `H_N`.

In particular, every `R_N`-vector in `V_{R_N,h}`, padded by zeros to length `N`, belongs to the physical tangent relaxation `mathcal S_{N,h}`. The principal block of `K_N` is exactly `K_{R_N}`. Hence

\[
\boxed{C_{R_N}^{[h]}\le\Lambda_{N,h}.}
\tag{26}
\]

The ambient inclusions give

\[
\mathcal S_{N,h}\subset H_N\subset\mathbb R^N,
\]

so

\[
\Lambda_{N,h}\le\Gamma_N\le C_N\le\zeta(2),
\tag{27}
\]

where `Gamma_N` is the block-constant constant of `FD-004`. Combining (25)--(27) proves

\[
\boxed{\Lambda_{N,h}\to\zeta(2)}
\tag{28}
\]

and the first estimate in (5).

This is the same structural reason behind `FD-004` and `FD-005`, now at arbitrary fixed depth: the hyperbola quotient leaves a growing initial principal block free, and finitely many global moment equations remove only a vanishing amount of the first-coordinate Riesz norm inside that block.

## 6. The corresponding physical affine slice has the same limiting constant

The affine slice `mathcal A_{N,h}` is nonempty because the actual Mertens staircase satisfies (1). Choose any `v_0 in mathcal A_{N,h}` and any nonzero `w in mathcal S_{N,h}`. Then

\[
v_t=v_0+t w\in\mathcal A_{N,h}
\qquad(t\in\mathbb R).
\tag{29}
\]

Positive definiteness gives

\[
\lim_{|t|\to\infty}
\frac{(v_t)_1^2}{v_t^TK_Nv_t}
=\frac{w_1^2}{w^TK_Nw}.
\tag{30}
\]

Taking suprema yields

\[
\boxed{\Lambda_{N,h}\le\Xi_{N,h}.}
\tag{31}
\]

Since `mathcal A_{N,h} subset H_N`,

\[
\Xi_{N,h}\le\Gamma_N\le\zeta(2).
\tag{32}
\]

Together with (28), this proves the second limit in (4) and the second estimate in (5).

For the physical vector, `FD-003` gives

\[
12\left(M_N\mathfrak F_N+\frac1{12}\right)
=m^TK_Nm,
\]

so any homogeneous scalar extraction that uses only membership in `mathcal A_{N,h}` has sharp coefficient `Xi_{N,h}` and therefore retains the limiting Franel factor `2 pi^2`.

## 7. Adversarial controls and what remains open

The theorem is deliberately **fixed-depth**. It does not say that a number of moment constraints `h=h(N)` growing with `N` is harmless. The constants hidden in (22)--(25) depend on `h`, and the moment matrix becomes increasingly ill-conditioned as degree grows. A growing hierarchy is therefore a genuinely different problem rather than a cosmetic extension of this proof.

The constrained extremizers are still arbitrary real vectors in the affine/tangent relaxation. They need not be realizable as partial sums of one common Möbius sequence. In particular this result does not use the increment law

\[
\mathbf M(n)-\mathbf M(n-1)=\mu(n)\in\{-1,0,1\},
\]

squarefree support, multiplicativity of `mu`, or linked nonlinear compatibility across floor quotients. Any one of those could in principle exclude the relaxed near-extremizers even though finitely many polynomial moments cannot.

The result also does not rule out a useful **nonhomogeneous** inequality exploiting the finite affine right sides in (1), nor an argument whose output is not a single-coordinate bound for `M(N)`. It rules out the specific leading-order shortcut pursued through `FD-003`--`FD-005`: fixed finite linear-moment information cannot improve the homogeneous scalar dual constant of the exact Franel GCD energy.

Finally, nothing here constrains ordered Farey gaps, mediant ancestry, refinement chronology, or a pre-cumulative antisymmetric carrier. Those routes retain information that the vector `M(floor(N/d))` has already forgotten.

## 8. Prior art and novelty boundary

The identities (6)--(7) are elementary Dirichlet-convolution formulas for Jordan totients. Equivalent Möbius/Faulhaber formulas for summatory Jordan totients are classical computational number theory; no novelty is claimed for the moment hierarchy itself. The `s=0` floor-quotient recurrence is already anchored through Deléglise--Rivat in `SOURCES.md`.

The Smith/Jordan GCD-matrix factorization, its inverse, and `C_R->zeta(2)` are classical and already anchored in `FD-003`. Formula (9) is standard finite-dimensional constrained Riesz projection. The only new auxiliary input needed for the fixed-depth asymptotic is the prime number theorem, used through the weighted dyadic-prime consequence (20); Donald J. Newman's 1980 proof is added to `SOURCES.md` as a primary theorem anchor.

A targeted search for Farey/Franel discrepancy with fixed Jordan-moment constraints, Mertens floor-quotient polynomial moments, and constrained Smith/GCD coordinate norms did not locate the combined obstruction (4). That absence is not used as evidence of historical novelty. The Mathia-specific delta is the exact boundary theorem: **the natural finite hierarchy extending `FD-005` can be imposed to arbitrary fixed depth and still removes only `o(1)` of the leading Franel--Mertens coordinate dual constant.**

No new bound on the true Mertens function, the Franel discrepancy, or RH is established. The theorem narrows the cumulative route by identifying what kind of additional arithmetic information must be qualitatively stronger than any fixed finite set of these exact linear moments.