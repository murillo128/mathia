# WI-097 — Sparse Loewner--Bezout nullity is exactly the orbit three-resonance

**Status:** `EXACT-DERIVED + CLASSICAL-IDENTITY + LITERATURE+DERIVED + STRUCTURAL-CLASSIFICATION`. This finding does **not** change Mathia's current unconditional simple-critical zero proportion and does not certify or repair the Yang--Yang one-sided fourth-moment candidate. It resolves `CLUE-sparse-loewner-kernel-orbit-classification`: for the sparse equal-degree Bezout family exposed by the WI-087 formalization, the proposed translation-orbit criterion is exact, and the common factor can be written explicitly.

Let

\[
0<a<g,
\qquad d=g-a,
\qquad h=\gcd(a,d),
\qquad L=d/h,
\tag{1}
\]

and define

\[
P(X)=1+X^a+X^{a+g},
\qquad
Q(X)=1+X^g+X^{a+g}.
\tag{2}
\]

Let `B(a,g)` be the `(a+g) x (a+g)` Bezout matrix of `P,Q`, i.e. the coefficient matrix of

\[
\frac{P(X)Q(Y)-Q(X)P(Y)}{X-Y}.
\tag{3}
\]

Then

\[
\boxed{
\gcd(P,Q)=
\begin{cases}
X^{2h}+X^h+1,&3\mid L,\\
1,&3\nmid L,
\end{cases}}
\tag{4}
\]

where the gcd is taken monic over `C[X]` (equivalently `Q[X]`). Consequently the classical Bezoutian nullity theorem gives

\[
\boxed{
\dim_{\mathbf C}\ker B(a,g)=
\begin{cases}
2h,&3\mid L,\\
0,&3\nmid L.
\end{cases}}
\tag{5}
\]

Equivalently, `B(a,g)` is invertible exactly when the translation orbit length

\[
L=\frac{g-a}{\gcd(a,g-a)}
\tag{6}
\]

is **not** divisible by three. The earlier sufficient condition `(g-a) % 3 != 0` is therefore not the exact boundary: `3 | (g-a)` can still be nonsingular when the common factor of `a` and `g-a` removes the factor of three from the orbit length.

## 1. Every common root lies on the `d`-th roots of unity

Subtracting the two sparse polynomials gives

\[
P(X)-Q(X)=X^a-X^g=X^a(1-X^d).
\tag{7}
\]

A common root `xi` cannot be zero because `P(0)=Q(0)=1`. Hence every common root satisfies

\[
\boxed{\xi^d=1.}
\tag{8}
\]

Since `g=a+d`, equation (8) reduces the highest monomial to

\[
\xi^{a+g}=\xi^{2a+d}=\xi^{2a}.
\]

Thus at a common root

\[
0=P(\xi)=1+\xi^a+\xi^{2a}.
\tag{9}
\]

Putting `u=xi^a`, equation (9) says

\[
1+u+u^2=0,
\tag{10}
\]

so `u` is a nontrivial cube root of unity.

Conversely, any nonzero `xi` satisfying (8) and (10) is a root of both `P` and `Q`. Therefore the common-root set is exactly

\[
\{\xi:\ \xi^d=1,\ \xi^a\in\mu_3\setminus\{1\}\}.
\tag{11}
\]

This reduction is exact; no genericity, numerical rank test, or Ramanujan asymptotic enters.

## 2. The common roots are exactly the roots of `X^(2h)+X^h+1`

Write

\[
a=hA,
\qquad d=hL,
\qquad \gcd(A,L)=1.
\tag{12}
\]

For a root `xi` of (11), set `v=xi^h`. Then `v^L=1`, and

\[
v^A=\xi^a
\]

has order exactly three. Since exponentiation by `A` is an automorphism of the cyclic group `mu_L`, `v` itself has order three. Hence a common root can exist only if

\[
3\mid L,
\tag{13}
\]

and in that case it must satisfy

\[
\xi^h\in\mu_3\setminus\{1\}.
\tag{14}
\]

Conversely assume `3 | L` and (14). Because `gcd(A,L)=1`, one also has `3 \nmid A`; therefore `(xi^h)^A` is again a nontrivial cube root. Moreover `xi^d=(xi^h)^L=1`. So (11) holds.

The common-root set is thus precisely the zero set of

\[
\frac{X^{3h}-1}{X^h-1}=X^{2h}+X^h+1.
\tag{15}
\]

There are exactly `2h` such roots. They are all simple: `X^{3h}-1` is square-free over characteristic zero. More directly, any common root is a root of `P-Q=X^a(1-X^d)`, whose derivative is nonzero at every `d`-th root of unity, so no common factor of `P,Q` can contain that root with multiplicity greater than one. This proves the gcd formula (4).

## 3. Bezoutian nullity gives the proposed formula with no missing kernel equations

Both `P` and `Q` have degree

\[
n=a+g.
\]

For two degree-`n` polynomials, the classical main theorem on Bezoutians states that the nullity of their `n x n` Bezout matrix equals the number of common zeros counted with multiplicity, equivalently the degree of their gcd. Applying that theorem to (4) gives immediately

\[
\operatorname{nullity}B(a,g)=\deg\gcd(P,Q),
\]

which is exactly (5).

This bypasses the only uncertainty left in the clue's recurrence derivation. One does not need to prove separately that every solution of the cyclic recurrence reconstructs a full coefficient-kernel vector: the Bezoutian theorem identifies the complete kernel dimension from the polynomial gcd itself.

The orbit calculation nevertheless explains the same number. Translation by `a` on `Z/dZ` has `h` orbits, each of length `L`. On one orbit the recurrence exposed by the Lean proof is

\[
u_{j+1}+u_j+u_{j-1}=0.
\tag{16}
\]

Its characteristic polynomial is `T^2+T+1`; every nonzero solution is three-periodic. Hence a cyclic orbit contributes dimension two exactly when `3 | L`, and dimension zero otherwise. Across `h` orbits this gives `2h` or zero, in exact agreement with (5). The agreement is now a theorem-level consequence rather than a heuristic dimension count.

## 4. The earlier modulo-three condition is strictly weaker

WI-087 and its formalization used the sufficient nonsingularity condition

\[
3\nmid d.
\tag{17}
\]

Since `L | d`, (17) certainly implies `3 \nmid L`, but the converse fails. For example, take

\[
a=3,
\qquad g=6.
\]

Then `d=3`, `h=3`, and `L=1`. Equation (5) says `B(3,6)` is invertible even though `3 | d`. More generally, if the entire 3-adic factor of `d` is absorbed by `h=gcd(a,d)`, the sparse Bezoutian is nonsingular.

Conversely, singularity is not merely detected by a congruence: when `3 | L`, its nullity is quantized exactly as `2 gcd(a,d)` and its common factor is the explicit cyclotomic pullback `Phi_3(X^h)=X^(2h)+X^h+1`.

## 5. Relation to the prime Ramanujan obstruction chain

This result sharpens the algebraic classification of the special sparse Loewner family behind WI-087, but it does not undo WI-088--WI-096. Those later findings reduce the actual close-prime residual Ramanujan rank defect to the exact free-cycle count of a different partial-bijection model and show that extensive pairwise defect is confined to low-denominator boundary resonances and is metrically weak in aggregate.

The present theorem therefore closes a representation-level question rather than opening a new scalar pairwise escape. In particular, re-expressing the same pairwise defect through sparse Bezoutians cannot by itself evade WI-096's stopping rule. A useful continuation would need source-labelled or simultaneous multi-pair information, singular-value magnitudes, or the unsimplified locked four-prime covariance rather than another pairwise rank coordinate system.

The exact classification can still be useful as a consistency check when sparse rational interpolants occur in future multi-modulus constructions: singularity is governed by the reduced orbit length `L`, not by the raw exponent difference `d`.

## 6. Prior art and novelty boundary

The load-bearing matrix theorem is classical. S. Barnett, **A Note on the Bezoutian Matrix**, *SIAM Journal on Applied Mathematics* 22 (1972), 84--86, DOI `10.1137/0122009`, is already anchored in WI-087 for the Bezoutian/resultant machinery. Branko Curgus and Aad Dijksma, **A proof of the main theorem on Bezoutians**, arXiv:1208.2385, give a self-contained statement and proof that Bezoutian nullity equals the number of common zeros counted with multiplicity.

The cyclotomic part of the proof is elementary: it uses only the difference identity (7), the cyclic-group map `u -> u^A`, and the factorization `(X^(3h)-1)/(X^h-1)`. A targeted search for this exact paired sparse family, together with searches around trinomial gcds, roots of unity, Bezoutians, and Loewner rational interpolation, located the general classical ingredients but no direct statement of (4)--(6). That negative search is **not** used as a priority claim. The durable result is the exact derivation above and its resolution of the repository clue.

## 7. Research consequence

The clue's proposed orbit criterion is correct, but its program effect is primarily classificatory and negative:

\[
\boxed{
\text{sparse Loewner nullity}
=2\gcd(a,g-a)\cdot \mathbf 1_{\,3\mid (g-a)/\gcd(a,g-a)}.
}
\tag{18}
\]

There is no hidden finer singularity locus inside this three-term family. The raw `(g-a) mod 3` condition can be sharpened exactly, but once the reduced orbit length is used, the pairwise kernel is completely classified. Further work on the `weil_inertia` objective should therefore not spend cycles searching for additional nullity inside this same sparse Bezout family unless new simultaneous/source-labelled structure is added.
