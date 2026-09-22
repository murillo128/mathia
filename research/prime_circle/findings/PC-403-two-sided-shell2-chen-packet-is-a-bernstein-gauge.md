# PC-403 — two-sided shell-2 Chen placement is only a Bernstein gauge of the same moments

**Status:** `EXACT-DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-NEGATIVE` for the canonical two-sided shell-2 Chen packet with one target-shell insertion, and for the generalized pencil obtained from its square mixed-moment matrices. This does not classify words containing two genuinely independent non-reference shell insertions, cross-level/refinement couplings, or nonlinear operations on several shell measures.

PC-402 leaves genuinely independent off-diagonal or cross-level information outside its scalar cross-Hankel no-go. The most immediate ordered candidate is therefore to keep the shell-2 reference letter on **both sides** of a target shell instead of only before it: the coefficients `J_{2^i,n,2^j}` remember where the target insertion occurs inside a longer Chen word and look, before reduction, like a genuinely two-index off-diagonal packet.

They are not independent data. Conditioning on the target insertion shows that the entire two-sided packet is exactly the Bernstein-basis presentation of the same compact signed measure `mu_n` already decoded by PC-399. At fixed total shell-2 depth `N`, all `N+1` insertion positions are an invertible triangular re-encoding of the first `N+1` ordinary moments. At square depth, the resulting mixed matrix is a fixed right-basis transform of the Hankel moment matrix, so its generalized pencil relative to shell 2 has **exactly the same generalized eigenvalues** as PC-402.

Thus merely making the shell-2 Chen construction two-sided or apparently off-diagonal does not supply the additional source-forced form that survived PC-402. The extra index is a basis coordinate, not a new carrier.

## 1. Exact two-sided insertion formula

For `n>1`, use the notation of PC-399/PC-402

\[
X_n(z)=\log\Phi_n(z),\qquad
t=X_2(z)=\log(1+z),\qquad
L=\log2,
\]

and

\[
d\mu_n(t)=(X_2)_*(dX_n).
\]

Here `2^i` in a Chen word means `i` repeated shell-2 letters, not the integer power. For `i,j\ge0`, fix the integration variable of the target letter `dX_n` at `z`. The `i` identical shell-2 letters before it contribute

\[
\int_{0<z_1<\cdots<z_i<z}\prod_{r=1}^i dX_2(z_r)
=\frac{t^i}{i!},
\]

while the `j` identical shell-2 letters after it contribute

\[
\int_{z<u_1<\cdots<u_j<1}\prod_{r=1}^j dX_2(u_r)
=\frac{(L-t)^j}{j!}.
\]

Therefore

\[
\boxed{
 i!j!\,J_{2^i,n,2^j}
 =\int_0^L t^i(L-t)^j\,d\mu_n(t).
}
\tag{1}
\]

The apparent two-dimensional ordering data is thus a mixed polynomial moment of the **same one-dimensional measure** `mu_n`. No second shell measure or independent kernel has entered.

## 2. A fixed-depth placement packet is exactly a moment prefix

Set `N=i+j` and collect every possible position of the target shell into

\[
Q_{N,n}(u)
:=N!\sum_{i=0}^{N}J_{2^i,n,2^{N-i}}u^i.
\tag{2}
\]

Using (1) and the binomial theorem gives the exact identity

\[
\boxed{
Q_{N,n}(u)
=\int_0^L\bigl(L+(u-1)t\bigr)^N\,d\mu_n(t).
}
\tag{3}
\]

If

\[
m_k(n):=\int_0^L t^k\,d\mu_n(t)=k!J_{2^k,n},
\tag{4}
\]

then differentiating (3) at `u=1` yields, for `0\le k\le N`,

\[
\boxed{
Q_{N,n}^{(k)}(1)
=\frac{N!}{(N-k)!}L^{N-k}m_k(n).
}
\tag{5}
\]

Hence the `N+1` coefficients

\[
\bigl(J_{n,2^N},J_{2,n,2^{N-1}},\ldots,J_{2^N,n}\bigr)
\]

and the moment prefix

\[
(m_0(n),m_1(n),\ldots,m_N(n))
\]

are related by an invertible triangular change of coordinates. The placement information at depth `N` contains exactly the same finite information as the first `N+1` one-sided shell-2 moments.

The completely symmetrized placement sum collapses further to the common-vertex endpoint data:

\[
\boxed{
N!\sum_{i=0}^{N}J_{2^i,n,2^{N-i}}
=L^N\Lambda(n).
}
\tag{6}
\]

This is (3) at `u=1` and is also the corresponding shuffle identity. Thus moving the target insertion through the reference word interpolates between ordinary moments, while summing over all positions returns the already-known Mangoldt endpoint selector.

## 3. The square two-sided matrix is a right-basis transform of the Hankel matrix

The natural square array is

\[
C_N(n)_{ij}:=i!j!J_{2^i,n,2^j},
\qquad 0\le i,j\le N.
\tag{7}
\]

By (1),

\[
C_N(n)_{ij}=\int_0^L t^i(L-t)^j\,d\mu_n(t).
\tag{8}
\]

Let

\[
H_N(n)_{ik}=m_{i+k}(n)
\]

be the ordinary Hankel matrix of PC-402, and define the fixed upper-triangular matrix

\[
R_N(k,j)=
\begin{cases}
(-1)^k\binom{j}{k}L^{j-k},&k\le j,\\
0,&k>j.
\end{cases}
\tag{9}
\]

Since `(L-t)^j=\sum_{k=0}^jR_N(k,j)t^k`, equations (8)--(9) give

\[
\boxed{C_N(n)=H_N(n)R_N.}
\tag{10}
\]

The diagonal of `R_N` is `((-1)^j)_{j=0}^N`, so

\[
\det R_N=(-1)^{N(N+1)/2}\ne0.
\tag{11}
\]

Exactly the same transform applies to the shell-2 reference matrix. Consequently

\[
\boxed{
C_N(n)-\lambda C_N(2)
=\bigl(H_N(n)-\lambda H_N(2)\bigr)R_N,
}
\tag{12}
\]

and therefore

\[
\boxed{
\det\bigl(C_N(n)-\lambda C_N(2)\bigr)
=\det(R_N)\det\bigl(H_N(n)-\lambda H_N(2)\bigr).
}
\tag{13}
\]

The two generalized pencils have identical finite generalized eigenvalues, with identical algebraic multiplicities. Thus the canonical two-sided ordered matrix does not evade PC-402: it is literally the same pencil after a fixed change of the **right polynomial basis** from `t^j` to `(L-t)^j`.

This also identifies a gauge trap. Ordinary eigenvalues or singular values of `C_N(n)` by itself can differ from those of `H_N(n)` because right multiplication is not a similarity transformation. But such quantities depend on choosing different coordinate bases for the two arguments of the same bilinear functional. Without an independently source-forced identification of those bases, that spectral motion is basis-dependent rather than an intrinsic Prime-Circle invariant.

## 4. Bernstein interpretation and matched control

For fixed `N`, equation (1) can be normalized as

\[
\frac{N!}{L^N}J_{2^i,n,2^{N-i}}
=\int_0^L
\binom Ni\left(\frac{t}{L}\right)^i
\left(1-\frac{t}{L}\right)^{N-i}
\,d\mu_n(t).
\tag{14}
\]

Thus target-shell placement is precisely evaluation of `mu_n` on the degree-`N` Bernstein basis. The Bernstein and monomial bases span the same polynomial space, and (3)--(5) give the explicit invertible conversion relevant here.

Nothing in this reduction is arithmetic. Let `nu` be any finite signed measure on `[0,L]`, or equivalently let `Y` be any bounded-variation profile on `[0,1]` and push `dY` forward through the same monotone coordinate `t=log(1+z)`. Replacing `mu_n` by `nu` reproduces equations (1)--(14) verbatim. The two-sided placement packet, its fixed-depth polynomial, and its right-gauge equivalence to a Hankel matrix are therefore generic consequences of ordering one distinguished differential among repeated copies of a monotone reference differential.

The cyclotomic shell chooses the particular measure `mu_n`; it does not make the placement/Bernstein mechanism prime-specific.

## 5. Prior-art and novelty audit

PC-399 already audits the one-sided shell-2 ladder against the classical compact moment problem and path-signature inversion for monotone paths. The present calculation lies inside that same classical envelope. Chen iterated integrals supply the ordered coefficients; conditioning on a single distinguished letter reduces repeated copies of one reference differential to powers of the elapsed and remaining reference coordinate; and the resulting functions are the classical Bernstein polynomial basis on a compact interval.

A directed prior-art search against monotone/time-augmented path signatures, signature inversion, Hausdorff moment representations, and Bernstein-basis moment formulas found only the expected classical ingredients. In particular, Chang--Duffield--Ni--Xu's monotone-path signature inversion already establishes the broader principle that signature coefficients can reconstruct a monotone path, while the Bernstein/Hausdorff moment framework treats the functions in (14) as a standard polynomial basis for finite-interval measure data. No novelty is claimed for these ambient mechanisms.

The line-local mathematical delta is narrower and exact: **the complete family obtained by putting one Prime-Circle shell between arbitrary left/right shell-2 blocks is not the independent off-diagonal source data left open by PC-402.** It is an explicit Bernstein/monomial gauge transform of PC-399's same scalar measure, and its canonical generalized pencil is exactly PC-402's pencil.

## 6. Consequence and surviving boundary

This closes the immediate route

\[
\text{one target shell + shell-2 letters on both sides}
\longrightarrow
\text{two-index ordered matrix}
\longrightarrow
\text{new off-diagonal spectral carrier}.
\]

The second Chen index records where the target insertion sits relative to a monotone coordinate, but equations (3)--(5) show that this is only a re-encoding of the ordinary moment prefix. The matrix version adds no generalized spectrum because the right basis transform cancels exactly in the paired pencil.

What remains open must contain genuinely additional source information. Examples include two or more non-reference shell insertions whose relative order cannot be reduced to one scalar measure, a cross-level/refinement operator that changes the state space before moment reduction, an independently forced second bilinear form rather than a basis-changed copy of the first, or a nonlinear interaction between separately recovered shell profiles. PC-403 makes no claim about those cases.

The result is not a useful automatic formalization handoff: its load-bearing statements are direct simplex conditioning, the binomial theorem, and an elementary triangular basis change, with no unresolved structural hypothesis that would justify a separate Lean task under the Research Watch formalization gate.

## Audit / falsification tests

The finding fails if any of the following occurs:

1. conditioning `J_{2^i,n,2^j}` on the target insertion does not give the two simplex volumes in Section 1;
2. equation (1) fails under the pushforward `t=X_2(z)`;
3. the placement polynomial (3) is not the binomial sum of the coefficients in (2);
4. derivatives at `u=1` do not recover the moment prefix as in (5);
5. `(L-t)^j` is not related to the monomial basis by the invertible triangular matrix (9);
6. the matrix factorization (10) or pencil factorization (12) fails;
7. the same construction applied to an arbitrary finite signed control measure does not reproduce equations (1)--(14).

Items 1--7 are exact elementary consequences of the Chen simplex definition, the shell-2 homeomorphic coordinate from PC-399, and finite-dimensional polynomial basis conversion. The result does not assert that every ordered multi-shell Chen array is a scalar moment gauge.