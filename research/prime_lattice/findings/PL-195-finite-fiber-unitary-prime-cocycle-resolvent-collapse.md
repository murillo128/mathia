# PL-195 — Finite-fiber unitary prime cocycles collapse for self-adjoint resolvents

**Status:** negative result / structural collapse  
**Evidence class:** EXACT-DERIVED + LITERATURE-ADJACENT + DECISIVE-NEGATIVE  
**Research line:** `prime_lattice`

## Claim

Let

\[
\mathcal H=\ell^2(\mathbb N)\otimes \mathbb C^d,
\qquad 1\le d<\infty,
\]

and let the canonical prime shifts act only on the exponent-lattice coordinate,

\[
\widetilde S_p=S_p\otimes I_d,
\qquad S_p e_n=e_{pn}.
\]

Let `L=L^*` be a possibly unbounded self-adjoint operator on `mathcal H`, and put

\[
R=(L-i)^{-1}.
\]

Suppose that for every rational prime `p` there is a unitary matrix `U_p in U(d)` such that

\[
\boxed{
R\widetilde S_p=(S_p\otimes U_p)R.
}
\]

Then every local matrix cocycle is trivial:

\[
\boxed{U_p=I_d\qquad\text{for every prime }p.}
\]

Moreover there is a single invertible matrix `A` on `C^d` such that

\[
R=I_{\ell^2(\mathbb N)}\otimes A,
\]

and hence

\[
L=I_{\ell^2(\mathbb N)}\otimes K
\]

for a finite-dimensional self-adjoint matrix `K`. In particular `L` is bounded and has only finitely many spectral values. Therefore the most direct fixed-finite-dimensional operator-valued repair of the scalar covariance obstructions `PL-193` and `PL-194` cannot produce a Hilbert--Pólya spectrum.

The result is stronger than a statement that the matrices `U_p` merely commute or become simultaneously diagonalizable: the self-adjoint resolvent geometry forces every one of them to be the identity.

## 1. The finite vacuum fiber reduces the normal resolvent

Let

\[
E=e_1\otimes\mathbb C^d
\]

be the `d`-dimensional vacuum fiber. For `n>1`, choose any prime `p|n`. Since

\[
e_n\otimes\xi=\widetilde S_p(e_{n/p}\otimes\xi),
\]

the covariance gives

\[
R(e_n\otimes\xi)
=(S_p\otimes U_p)R(e_{n/p}\otimes\xi).
\]

The right side is supported on integer indices divisible by `p`, so it is orthogonal to `E`. Thus

\[
R^*E\subseteq E.
\]

Write `R` relative to `E\oplus E^\perp` as

\[
R=
\begin{pmatrix}
A&0\\
C&D
\end{pmatrix}.
\]

Because `R` is a resolvent of a self-adjoint operator, it is normal. The `E`-corner of `R^*R=RR^*` is

\[
A^*A+C^*C=AA^*.
\]

Now `E` is finite dimensional, so taking the ordinary matrix trace gives

\[
\operatorname{tr}(C^*C)
=\operatorname{tr}(AA^*)-\operatorname{tr}(A^*A)=0.
\]

Hence `C=0`. Therefore `E` reduces `R`, and

\[
R(e_1\otimes\xi)=e_1\otimes A\xi.
\]

Since a self-adjoint resolvent is injective, `A` is injective and therefore invertible in finite dimension.

This is the first place where finite fiber dimension matters. For an infinite-dimensional vacuum fiber the trace argument is unavailable, so the finding does not silently extend to arbitrary operator-valued cocycles.

## 2. Prime powers turn each matrix eigenphase into the scalar resolvent-circle problem

Fix a prime `p`. Iterating the exact covariance along its exponent axis gives, for every `k>=0`,

\[
R(e_{p^k}\otimes\xi)
=e_{p^k}\otimes U_p^kA\xi.
\]

Every self-adjoint resolvent at `i` satisfies the positive operator identity

\[
\boxed{
\operatorname{Im}R=R^*R.
}
\]

Apply the corresponding quadratic-form identity to `e_{p^k}\otimes\xi`. Unitarity of `U_p` gives

\[
\operatorname{Im}\langle U_p^kA\xi,\xi\rangle
=\|U_p^kA\xi\|^2
=\|A\xi\|^2.
\]

Diagonalize the finite-dimensional unitary `U_p` and take an eigenvector `xi` with

\[
U_p\xi=\omega\xi,
\qquad |\omega|=1.
\]

Set

\[
a=\langle A\xi,\xi\rangle,
\qquad q=\|A\xi\|^2>0.
\]

Up to the harmless choice of inner-product convention, the preceding identity becomes

\[
\operatorname{Im}(\omega^k a)=q
\qquad\text{for every }k\ge0.
\]

A nonconstant unit-circle orbit cannot have a strictly positive constant imaginary projection. If `omega` has infinite order, its powers have infinitely many limit points and the sine cannot stay constant. If `omega` has finite order, the level set of a fixed sine value contains at most two points modulo `2pi`; the only possible nontrivial orbit is order two, but `omega=-1` changes the sign of the imaginary part. Therefore

\[
\omega=1.
\]

Every eigenvalue of `U_p` is `1`, hence

\[
\boxed{U_p=I_d.}
\]

Since `p` was arbitrary, all prime matrices collapse independently. No cross-prime commutativity assumption is needed.

This step is the matrix-valued analogue of the scalar resolvent-circle obstruction in `PL-193`--`PL-194`, but the reduction is not obtained by assuming the matrices are simultaneously diagonal. The prime-power axis itself supplies all powers of each individual `U_p`, and the positive imaginary part of a self-adjoint resolvent kills every nontrivial eigenphase.

## 3. After the cocycle collapses, the Hamiltonian is only a repeated finite matrix

With `U_p=I_d`, the relation reduces to exact commutation

\[
R\widetilde S_p=\widetilde S_pR
\qquad\forall p.
\]

Because the vacuum fiber already reduces `R`, unique factorization gives for every integer `n`

\[
R(e_n\otimes\xi)
=e_n\otimes A\xi.
\]

Thus

\[
R=I\otimes A.
\]

The finite matrix `A` is invertible, so `R` is onto and `L` is actually bounded. Writing

\[
K=iI_d+A^{-1},
\]

we obtain

\[
L=I\otimes K.
\]

Because `L` is self-adjoint, `K=K^*`. Consequently

\[
\sigma(L)=\sigma(K),
\]

a finite set with at most `d` points. Infinite multiplicity is possible, but no unbounded sequence of zero heights can occur.

## 4. Prior-art and novelty audit

`PL-193` and `PL-194` already close the one-dimensional scalar versions: unit phases, and then arbitrary scalar weights, cannot survive the resolvent geometry except trivially. The present result tests the immediate next escape explicitly left open there: replace the scalar attached to each prime direction by a fixed finite-dimensional unitary matrix.

Vector-valued unilateral shifts, matrix/operator-valued Hardy multipliers, commutant lifting, and shift-intertwining operators are classical operator theory. A targeted literature audit around normal matrix-valued analytic Toeplitz operators, vector-valued shift intertwiners, and operator-valued `lambda`-commutation found extensive adjacent theory but no source asserting this exact simultaneous-prime self-adjoint-resolvent collapse. The proof above does not require a new external theorem: it uses only the one-sided divisibility support, finite-dimensional trace, spectral theorem for a unitary matrix, and the standard self-adjoint resolvent identity.

Accordingly, no abstract novelty claim is made for vector-valued shift theory. The durable contribution is the exact line-specific no-go statement: **finite internal matrix multiplicity does not evade scalar prime-covariance collapse once the carrier is required to be a genuine self-adjoint resolvent**.

No `SOURCES.md` update is required because no new external result is used as evidence for the theorem.

## 5. Adversarial boundaries and controls

The theorem is deliberately narrow in the places where a real escape could still live.

First, `d<infinity` is essential to the proof. Finite dimensionality is used both to turn `R^*E subset E` into a reducing vacuum fiber by a trace argument and to diagonalize each `U_p`. An infinite internal fiber, especially one with continuous unitary spectrum, is not covered.

Second, the local cocycles are **unitary**. Nonunitary operator weights, transfer operators, nonnormal scattering maps, or dissipative cocycles are outside the claim. `PL-194` treats arbitrary scalar nonunit weights, but that scalar argument does not automatically extend to matrices.

Third, the covariance is exact and imposed on the self-adjoint resolvent itself. Relations modulo compact/Schatten ideals, relative determinants, target-dependent compressions, and approximate covariance need separate analysis. In particular this theorem does not resolve the accepted local clue `CLUE-trace-class-prime-resolvent-cocycle`; it only removes the fixed-finite-dimensional exact-unitary-fiber branch from that clue's surviving operator-valued possibilities.

Fourth, the proof is **universal for any free one-sided multiplicative semigroup with a finite vacuum fiber**. It uses no special distributional property of the rational primes and no analytic continuation of `zeta`. That universality is a reason to treat the result as an obstruction, not as positive RH evidence.

Finally, target-relative Nyman/model-space actions can destroy the vacuum-support geometry used in the first step, while genuinely adelic constructions may carry infinite-dimensional local/global data. Those routes are not ruled out.

## Consequence for the research line

The sequence of covariance obstructions now has a clean next boundary:

\[
\text{scalar phase weights}
\subset
\text{arbitrary scalar weights}
\subset
\text{fixed finite-dimensional unitary prime matrices}
\]

all fail to produce a nontrivial self-adjoint zero Hamiltonian on the canonical one-sided exponent-lattice representation. The finite-matrix repair collapses even more strongly than might be expected: each prime matrix is individually forced to the identity by its own prime-power axis.

A genuinely distinct operator-valued prime mechanism must therefore leave at least one hypothesis of the theorem: **infinite internal multiplicity/continuous operator spectrum, nonunitary or nonnormal transport, target-relative compression, relative/Schatten rather than exact covariance, or additional completed global structure**. Merely replacing each scalar prime phase by a small matrix does not create the missing arithmetic rigidity.
