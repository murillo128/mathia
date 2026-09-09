# FD-003 — Franel--Mertens GCD energy has an asymptotically sharp scalar dual bound

**Status:** `EXACT-DERIVED + CLASSICAL-GCD-MATRIX-FACTORIZATION + SUM-OF-SQUARES + OPTIMAL-DUAL-BOUND + NEGATIVE/OBSTRUCTION`. `FD-002` identifies the quadratic Franel discrepancy with the complete weighted square norm of the divisor-transformed Mertens spectrum. Expanding that spectrum exposes an exact normalized power-GCD matrix on the vector of divisor-scaled Mertens values. Classical Smith/Jordan factorization then gives a positive sum-of-squares decomposition, an explicit inverse coordinate norm, and a sharp boundary for extracting the single value `M(N)` from the full Franel energy by generic quadratic geometry alone.

The resulting finite bound is slightly stronger than the first-mode estimate in `FD-002`, but its constant converges exactly to the same `2 pi^2`. Moreover that constant is optimal over arbitrary real coefficient vectors for the GCD quadratic form. Therefore **no argument that uses only positivity, diagonalization, conditioning, or duality of this full cross-scale GCD energy can asymptotically improve the scalar Mertens extraction constant without exploiting additional arithmetic restrictions of the actual staircase vector `M(floor(N/d))` or pre-cumulative Farey ordering information.**

## 1. The full Franel spectrum is one normalized power-GCD quadratic form

Retain the notation of `FD-002`. Let

\[
0=x_0<x_1<\cdots<x_{M_N}=1,
\qquad
\mathfrak F_N
=\sum_{j=1}^{M_N}\left(x_j-\frac{j}{M_N}\right)^2,
\]

and write the Mertens function as

\[
\mathbf M(y)=\sum_{n\le y}\mu(n).
\]

For `1<=d<=N`, define the divisor-scale vector

\[
m_d:=\mathbf M\!\left(\left\lfloor\frac Nd\right\rfloor\right).
\tag{1}
\]

`FD-002` proves that, with

\[
\mathcal B_N(k)
=\sum_{\substack{d\mid k\\d\le N}} d\,m_d,
\tag{2}
\]

one has

\[
M_N\mathfrak F_N+\frac1{12}
=\frac1{2\pi^2}
\sum_{k\ge1}\frac{|\mathcal B_N(k)|^2}{k^2}.
\tag{3}
\]

Expand the nonnegative series before making any estimate. Absolute convergence is immediate for fixed `N`, because (2) is a finite divisor sum and the outer weight is `k^{-2}`. Thus

\[
\begin{aligned}
\sum_{k\ge1}\frac{|\mathcal B_N(k)|^2}{k^2}
&=\sum_{d,e\le N}de\,m_dm_e
  \sum_{\operatorname{lcm}(d,e)\mid k}\frac1{k^2}\\
&=\zeta(2)
  \sum_{d,e\le N}
  \frac{de}{\operatorname{lcm}(d,e)^2}m_dm_e\\
&=\zeta(2)
  \sum_{d,e\le N}
  \frac{\gcd(d,e)^2}{de}m_dm_e.
\end{aligned}
\tag{4}
\]

Since `zeta(2)=pi^2/6`, (3)--(4) give the exact identity

\[
\boxed{
12\left(M_N\mathfrak F_N+\frac1{12}\right)
=\sum_{d,e\le N}
K_N(d,e)m_dm_e,
\qquad
K_N(d,e):=\frac{\gcd(d,e)^2}{de}.
}
\tag{5}
\]

Thus the complete quadratic Franel spectrum is not merely controlled by a GCD kernel: after the `FD-002` normalization it **is exactly** the quadratic form of the normalized power-GCD matrix `K_N` evaluated on the physical divisor-scale Mertens vector (1).

## 2. Jordan factorization turns the cross-scale energy into exact squares

Let `J_2` be Jordan's second totient,

\[
J_2(r)=r^2\prod_{p\mid r}(1-p^{-2}),
\]

so that the elementary divisor identity

\[
n^2=\sum_{r\mid n}J_2(r)
\tag{6}
\]

holds. Applying (6) to `n=gcd(d,e)` gives

\[
K_N(d,e)
=\frac1{de}\sum_{r\mid d,\,r\mid e}J_2(r).
\tag{7}
\]

Substitution into (5) and regrouping finite sums yields the positive decomposition

\[
\boxed{
12\left(M_N\mathfrak F_N+\frac1{12}\right)
=\sum_{r\le N}J_2(r)
\left(
\sum_{\substack{d\le N\\r\mid d}}
\frac{\mathbf M(\lfloor N/d\rfloor)}{d}
\right)^2.
}
\tag{8}
\]

Writing `d=rs` makes the scale structure explicit:

\[
\boxed{
12\left(M_N\mathfrak F_N+\frac1{12}\right)
=\sum_{r\le N}\frac{J_2(r)}{r^2}
\left(
\sum_{s\le N/r}
\frac{\mathbf M(\lfloor N/(rs)\rfloor)}{s}
\right)^2.
}
\tag{9}
\]

This is an exact multiscale square decomposition. It does not introduce a new arithmetic source: every square is still a finite linear combination of Mertens values. Its value is structural. The positive and negative cross-terms in the GCD matrix of (5) are completely resolved into divisor-incidence coordinates before any inequality is taken.

For later duality it is useful to record the matrix factorization explicitly. Let

\[
D=\operatorname{diag}(1,2,\ldots,N),
\qquad
J=\operatorname{diag}(J_2(1),\ldots,J_2(N)),
\]

and let `E` be the divisor-incidence matrix

\[
E_{r,d}=\mathbf 1_{r\mid d}.
\tag{10}
\]

Then

\[
\boxed{K_N=D^{-1}E^TJE D^{-1}.}
\tag{11}
\]

In the natural increasing order, `E` is triangular with diagonal one. Hence `K_N` is positive definite and

\[
\boxed{
\det K_N
=\prod_{r=1}^N\frac{J_2(r)}{r^2}
=\prod_{r=1}^N\prod_{p\mid r}(1-p^{-2})>0.
}
\tag{12}
\]

Equations (11)--(12) are standard Smith/meet-matrix algebra specialized to the normalized square-GCD kernel; no novelty is claimed for the GCD-matrix factorization itself.

## 3. The exact optimal generic constant for extracting `M(N)`

The inverse of the divisor-incidence matrix is Möbius incidence:

\[
(E^{-1})_{r,d}
=\mu(d/r)\mathbf1_{r\mid d}.
\tag{13}
\]

From (11),

\[
K_N^{-1}
=D E^{-1}J^{-1}(E^{-1})^T D.
\tag{14}
\]

Therefore the first diagonal entry is

\[
\boxed{
C_N:=(K_N^{-1})_{1,1}
=\sum_{r\le N}\frac{\mu(r)^2}{J_2(r)}.
}
\tag{15}
\]

For every real vector `v in R^N`, Cauchy--Schwarz in the `K_N` inner product gives the sharp coordinate inequality

\[
\boxed{
v_1^2\le C_N\,v^TK_Nv.
}
\tag{16}
\]

The constant is optimal for the unrestricted quadratic problem: equality occurs for every nonzero scalar multiple of

\[
v=K_N^{-1}e_1.
\tag{17}
\]

Applying (16) to the actual vector (1), whose first coordinate is `m_1=M(N)`, and using (5), gives

\[
\boxed{
|\mathbf M(N)|^2
\le
12C_N\left(M_N\mathfrak F_N+\frac1{12}\right).
}
\tag{18}
\]

This improves the finite constant `2pi^2` obtained in `FD-002` by discarding all Fourier modes except `k=1`. The improvement is real but asymptotically vanishing.

Indeed `mu(r)^2/J_2(r)` is supported on squarefree integers and has Euler product

\[
\begin{aligned}
\sum_{r\ge1}\frac{\mu(r)^2}{J_2(r)}
&=\prod_p\left(1+\frac1{p^2-1}\right)\\
&=\prod_p(1-p^{-2})^{-1}
=\zeta(2)=\frac{\pi^2}{6}.
\end{aligned}
\tag{19}
\]

Consequently

\[
\boxed{C_N\uparrow\frac{\pi^2}{6},}
\qquad
\boxed{12C_N\uparrow2\pi^2.}
\tag{20}
\]

There is also an elementary rate sufficient for the present boundary statement. Since

\[
J_2(r)
=r^2\prod_{p\mid r}(1-p^{-2})
\ge\frac{r^2}{\zeta(2)},
\]

one has

\[
0\le\frac{\pi^2}{6}-C_N
\le\zeta(2)\sum_{r>N}\frac1{r^2}
\le\frac{\zeta(2)}N.
\tag{21}
\]

Thus the best possible constant supplied by the **entire unrestricted GCD quadratic geometry** converges to the simple first-Fourier-mode constant already present in `FD-002`.

## 4. What this rules out, and what it does not

The equality vector (17) is an arbitrary real coefficient vector. It is not asserted to be realizable as

\[
\left(\mathbf M(N),\mathbf M(\lfloor N/2\rfloor),\ldots,
\mathbf M(1)\right).
\]

Accordingly, (20) does **not** prove that the first-mode bound is arithmetically sharp for the true Möbius sequence. It proves a narrower but useful impossibility principle: an asymptotic improvement cannot come merely from treating (5) as a better-conditioned positive matrix, changing to its eigenbasis, applying generic Hilbert-space duality, or exploiting its cross-scale positive definiteness. Those operations see exactly the unrestricted norm whose sharp dual constant is (15).

Any stronger scalar extraction must use information absent from the generic GCD form. There are two honest possibilities within the Farey mandate. One is to prove quantitative restrictions on the physical staircase vector `m_d=M(floor(N/d))` strong enough to separate it from the generic extremizers (17); such a theorem is arithmetic input, not free matrix geometry. The other is to retain Farey ordering, adjacency, mediant ancestry, or refinement-path information **before** the cumulative discrepancy is compressed to the `FD-002` Mertens vector.

This boundary also applies to claims of multiscale gain from (8)--(9). The sum of squares is exact and potentially useful for estimates, but by itself it does not add a new arithmetic channel. A candidate must show either a genuinely stronger bound on one or more square coordinates using Farey/Möbius structure, or an information carrier that is not already determined by the vector (1).

## 5. Prior art and audit boundary

H. J. S. Smith, *On the Value of a Certain Arithmetical Determinant*, Proceedings of the London Mathematical Society **s1-7** (1875), 208--213, DOI `10.1112/plms/s1-7.1.208`, is the classical origin of GCD-matrix determinant factorization. The later GCD/meet-matrix literature, including Pentti Haukkanen, Wang Jun and Juha Sillanpää, *On Smith's determinant*, Linear Algebra and its Applications **258** (1997), 251--269, develops generalized Smith-matrix factorization and inverse structure. The identity `sum_(r|n) J_2(r)=n^2`, Möbius inversion of divisor incidence, and the coordinate duality (16) are classical arithmetic/linear-algebra ingredients.

The derivation above is included in full because the Mathia claim is not that GCD matrices are new. The line-specific delta is the exact splice with `FD-002`: it identifies the complete Franel--Mertens energy as this particular normalized power-GCD norm and computes the sharp unrestricted dual constant for the RH-facing scalar coordinate `M(N)`.

The main falsification checks are explicit. The factor `1/12` in (5) follows from `zeta(2)/(2pi^2)` and would change if the `FD-002` Fourier normalization changed. The incidence factorization uses all integers `1<=d<=N`, not only divisors of `N`; deleting indices changes the inverse constant. Equality in (16) is an unrestricted-vector statement and must not be promoted to an arithmetic Mertens extremizer. Finally, a finite improvement `C_N<zeta(2)` does not change the RH-critical exponent because (21) shows the gain vanishes at least at rate `O(1/N)`.

No new bound for the actual Mertens function, Franel discrepancy, Farey spectral allocation, or RH is established. The durable consequence is an exact multiscale factorization plus an asymptotic **no-free-gain boundary**: after the Farey discrepancy has been compressed to the `FD-002` divisor-scale Mertens vector, generic positive GCD-matrix geometry cannot improve the scalar extraction beyond the already visible first-mode constant at leading order.
