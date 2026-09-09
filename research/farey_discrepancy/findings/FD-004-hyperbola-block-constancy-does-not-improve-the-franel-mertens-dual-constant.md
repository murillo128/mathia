# FD-004 — hyperbola-block constancy does not improve the Franel--Mertens dual constant

**Status:** `EXACT-DERIVED + STAIRCASE-CONSTRAINT + SHARP-RESTRICTED-DUALITY + NEGATIVE/OBSTRUCTION + DIRICHLET-HYPERBOLA-BOUNDARY`. `FD-003` shows that, after the quadratic Franel discrepancy is compressed to the divisor-scale vector

\[
m_d=\mathbf M\!\left(\left\lfloor\frac Nd\right\rfloor\right),
\qquad 1\le d\le N,
\]

generic positive GCD-matrix geometry cannot extract `M(N)=m_1` with an asymptotically better leading constant than the first Fourier mode. The actual vector is not generic, however: it is constant on every Dirichlet-hyperbola fiber `floor(N/d)=const`. That exact staircase constraint reduces the ambient dimension from `N` to `O(sqrt N)`.

This reduction is still not enough. Let

\[
K_N(d,e)=\frac{\gcd(d,e)^2}{de}
\]

be the `FD-003` Franel--Mertens kernel, and let `H_N` be the linear subspace of vectors constant on the fibers of `d mapsto floor(N/d)`. If

\[
\Gamma_N
:=\sup_{0\ne v\in H_N}
\frac{v_1^2}{v^T K_Nv},
\]

then

\[
\boxed{
C_{R_N}\le \Gamma_N\le C_N,
\qquad
R_N:=\max\{r:r(r+1)\le N\},
}
\]

where

\[
C_n=(K_n^{-1})_{1,1}
=\sum_{r\le n}\frac{\mu(r)^2}{J_2(r)}.
\]

Consequently

\[
\boxed{
\Gamma_N\longrightarrow\zeta(2)=\frac{\pi^2}{6},
\qquad
0\le \zeta(2)-\Gamma_N
\le \frac{\zeta(2)}{R_N}=O(N^{-1/2}).
}
\]

Thus even after imposing the exact `floor(N/d)` block structure, the optimal leading scalar-dual coefficient tends to the same value as the unrestricted GCD problem. In the Franel normalization, `12 Gamma_N -> 2 pi^2`. Any asymptotic improvement must use arithmetic compatibility stronger than hyperbola-block constancy, or retain ordered Farey information before the cumulative Mertens compression.

## 1. The physical Mertens vector lies in the hyperbola subspace

Define

\[
q_N(d):=\left\lfloor\frac Nd\right\rfloor,
\qquad
H_N:=\{v\in\mathbb R^N:q_N(d)=q_N(e)\Rightarrow v_d=v_e\}.
\tag{1}
\]

By definition,

\[
m_d=\mathbf M(q_N(d)),
\]

so the actual divisor-scale Mertens vector belongs to `H_N` exactly. No estimate or asymptotic approximation is involved.

The sharp coordinate constant on this restricted class is

\[
\Gamma_N
=\sup_{0\ne v\in H_N}
\frac{v_1^2}{v^TK_Nv}.
\tag{2}
\]

Because `K_N` is positive definite by the Smith/Jordan factorization in `FD-003`, the quotient is finite. Since `H_N subset R^N`, the unrestricted sharp bound of `FD-003` immediately gives

\[
\boxed{\Gamma_N\le C_N.}
\tag{3}
\]

The issue is whether the staircase restriction might lower this constant by a fixed amount. It does not.

## 2. The first `sqrt N` coordinates remain completely free

Put

\[
R_N:=\max\{r\ge1:r(r+1)\le N\}
=\left\lfloor\frac{\sqrt{1+4N}-1}{2}\right\rfloor.
\tag{4}
\]

For every `1<=d<=R_N`,

\[
\frac Nd-\frac N{d+1}
=\frac{N}{d(d+1)}\ge1.
\tag{5}
\]

Hence

\[
\left\lfloor\frac Nd\right\rfloor
>
\left\lfloor\frac N{d+1}\right\rfloor.
\tag{6}
\]

Monotonicity then shows that each index `d<=R_N` is a singleton fiber of `q_N`: no other index has the same value of `floor(N/d)`. Therefore **every vector supported on the first `R_N` coordinates automatically lies in `H_N`**.

This is the load-bearing observation. The hyperbola compression is large globally, but it leaves an expanding initial principal block completely unrestricted.

## 3. A principal-block extremizer gives the matching lower bound

Let `R=R_N` and take the unrestricted sharp coordinate extremizer for the `R x R` kernel,

\[
u^{(R)}:=K_R^{-1}e_1\in\mathbb R^R.
\tag{7}
\]

Pad it by zeros to a vector `v in R^N`. By Section 2, `v in H_N`. The upper-left `R x R` principal block of `K_N` is exactly `K_R`, so

\[
v^TK_Nv
=(u^{(R)})^TK_Ru^{(R)}
=e_1^TK_R^{-1}e_1
=C_R,
\tag{8}
\]

while

\[
v_1=e_1^TK_R^{-1}e_1=C_R.
\tag{9}
\]

Therefore

\[
\frac{v_1^2}{v^TK_Nv}=C_R,
\]

and hence

\[
\boxed{C_{R_N}\le\Gamma_N.}
\tag{10}
\]

Combining (3) and (10) proves the finite sandwich

\[
\boxed{C_{R_N}\le\Gamma_N\le C_N.}
\tag{11}
\]

No condition-number estimate, eigenvalue asymptotic, or numerical optimization enters this step.

## 4. The restricted constant has the same asymptotic limit

`FD-003` gives

\[
C_n
=\sum_{r\le n}\frac{\mu(r)^2}{J_2(r)}
\uparrow
\sum_{r\ge1}\frac{\mu(r)^2}{J_2(r)}
=\zeta(2).
\tag{12}
\]

It also records the elementary bound

\[
J_2(r)\ge\frac{r^2}{\zeta(2)}.
\tag{13}
\]

Thus

\[
0\le\zeta(2)-C_R
\le\zeta(2)\sum_{r>R}\frac1{r^2}
\le\frac{\zeta(2)}R.
\tag{14}
\]

Apply this with `R=R_N` and use (11):

\[
\boxed{
0\le\zeta(2)-\Gamma_N
\le\zeta(2)-C_{R_N}
\le\frac{\zeta(2)}{R_N}.
}
\tag{15}
\]

Since `R_N~sqrt N`,

\[
\boxed{
\Gamma_N=\zeta(2)+O(N^{-1/2})
}
\tag{16}
\]

with the understood one-sided sign `Gamma_N<=zeta(2)`.

The dimension reduction to the hyperbola quotient therefore does not create a leading-order dual gain. The reason is structural rather than numerical: the restricted class still contains larger and larger principal-coordinate copies of the unrestricted extremal problem.

## 5. Consequence for the Franel--Mertens extraction

`FD-003` proves the exact identity

\[
12\left(M_N\mathfrak F_N+\frac1{12}\right)
=m^TK_Nm.
\tag{17}
\]

Since the physical vector `m` lies in `H_N`, the sharp block-aware scalar inequality is

\[
\boxed{
|\mathbf M(N)|^2
\le
12\Gamma_N
\left(M_N\mathfrak F_N+\frac1{12}\right).
}
\tag{18}
\]

There may be a finite-`N` improvement because `Gamma_N` can be strictly smaller than `C_N`. But (15) forces

\[
12\Gamma_N\to12\zeta(2)=2\pi^2.
\tag{19}
\]

Thus a proof that uses the exact GCD energy together with **only** the fact that `M(floor(N/d))` is constant on equal-floor blocks cannot improve the RH-critical scalar extraction at leading order. Merely reducing the number of independent staircase coordinates to `O(sqrt N)` is not enough.

The actual Mertens staircase satisfies stronger compatibility that this theorem deliberately does not use. For example,

\[
\boxed{
\sum_{d=1}^N\mathbf M\!\left(\left\lfloor\frac Nd\right\rfloor\right)=1,
}
\tag{20}
\]

because

\[
\sum_{d\le N}\mathbf M(\lfloor N/d\rfloor)
=\sum_{n\le N}\mu(n)\left\lfloor\frac Nn\right\rfloor
=\sum_{k\le N}\sum_{n\mid k}\mu(n)=1.
\tag{21}
\]

Equation (20) is an exact Möbius compatibility condition, not part of the block-constancy relaxation. Further relations arise because the block values are not arbitrary constants but actual partial sums of one common Möbius sequence. Those are the remaining cumulative-side constraints that could still separate the physical staircase from the near-extremizers constructed in Section 3.

## 6. Prior art, audit, and evidence boundary

Grouping indices with equal values of `floor(N/d)` and the `O(sqrt N)` Dirichlet-hyperbola structure are classical number-theoretic devices; no novelty is claimed for them. Smith/Jordan GCD-matrix factorization, its inverse coordinate norm, and the limit `C_N->zeta(2)` are already anchored and derived in `FD-003`. The proof here uses only those established ingredients plus the elementary singleton-fiber observation (5)--(6).

A targeted literature search across GCD-matrix duality and Dirichlet-hyperbola/floor-quotient grouping did not identify the specific restricted-coordinate sandwich (11). That absence is not used as evidence of novelty. The Mathia-specific value is the negative boundary: the first obvious exact structural constraint of the physical `M(floor(N/d))` vector can be imposed completely and still leaves the scalar Franel dual constant asymptotically unchanged.

Several controls are essential. The lower-bound witness in Section 3 is an arbitrary real block-constant vector, **not** an actual Mertens staircase; the theorem therefore rules out gain from block constancy alone, not from all Möbius arithmetic. The singleton range is only `R_N~sqrt N`; claiming more free coordinates would be false because equal-floor blocks begin to merge beyond that scale. Equation (20) is not absorbed into `H_N` and may still matter. Finally, the result says nothing about ordered Farey gaps, mediant ancestry, refinement chronology, or the Plücker-type pre-cumulative carrier proposed in the local clue inbox.

No new estimate for the true Mertens function, Franel discrepancy, or RH is proved. The durable consequence is an exact no-free-gain theorem: **Dirichlet-hyperbola block constancy, despite its strong dimension reduction, cannot by itself improve the leading scalar dual constant of the Franel--Mertens GCD energy.**