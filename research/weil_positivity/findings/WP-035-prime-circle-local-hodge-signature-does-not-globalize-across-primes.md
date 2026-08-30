# WP-035 — Prime-Circle local Hodge signature does not globalize across primes

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE` for the direct attempt to reinterpret the renormalized Prime-Circle boundary birth operator of `WP-034` as a Hodge-index/intersection form with one global degree direction, or to repair that interpretation by adjoining only a fixed finite-dimensional archimedean/global sector while preserving the finite block.

`WP-034` leaves an initially attractive intersection-theoretic possibility. On a single prime-power ray the exact local operator `H_{p,A}` has precisely one positive eigenvalue, while every other nonzero eigenvalue is nonpositive. This resembles the signature pattern behind the Hodge index theorem: one positive direction, with negative definiteness on a primitive complement. The resemblance is real **locally**, but it fails as soon as independent prime directions are assembled.

Already on squarefree divisor boxes the Prime-Circle operator is a Kronecker sum of the one-prime forms. Its positive index is not one: it becomes at least two on `D(30)` and is unbounded along primorial exhaustions. Consequently no single degree-zero hyperplane, nor any family of primitive subspaces of uniformly bounded codimension, can make the Weil-signed finite block nonpositive on all arithmetic cutoffs. Adding a fixed finite-dimensional archimedean block cannot change that conclusion; if the finite block is retained as a principal restriction, its positive subspaces survive verbatim, and if the archimedean variables are eliminated by Schur complement, only a bounded-rank perturbation is produced.

Thus the local Lorentzian/Hodge-looking signature of each prime ray is **not** a global intersection-form mechanism. A surviving Hodge/cohomological route must introduce genuinely nonseparable cross-prime/global structure of unbounded or infinite rank before the sign theorem is applied. The full-rank scalar shift that does make the finite operator sign-definite is exactly the already-audited `WP-034` sign-flipped Poisson/GCD completion and does not generate the archimedean Gamma sector.

## 1. One prime ray really does have Hodge-index-like inertia

For a prime `p` and exponent cutoff `A>=1`, `PC-057` and `WP-034` give the exact spectrum

\[
\operatorname{Spec}(H_{p,A})
=
(\log p)
\left(
\{-A\}
\cup
\left\{
\frac1{p-1}-j:
0\le j<A
\right\}
\right).
\tag{1}
\]

The `j=0` eigenvalue is

\[
\kappa_p:=\frac{\log p}{p-1}>0.
\tag{2}
\]

All remaining eigenvalues are negative except for the harmless exceptional zero when `p=2` and `j=1`. Therefore

\[
\boxed{n_+(H_{p,A})=1}
\tag{3}
\]

for every prime `p` and every `A>=1`.

This is stronger than mere indefiniteness. On each isolated prime ray there exists a codimension-one complement to the unique positive eigenvector on which the form is nonpositive. Up to sign convention, this is exactly the elementary inertia pattern one would hope for if `H_{p,A}` were to play the role of a local intersection form and a single distinguished direction were to play the role of degree or polarization.

That local analogy is therefore worth testing rather than dismissing from the outset.

## 2. Squarefree globalization gives an exact subset-sum spectrum

Let

\[
N=\prod_{p\in P}p
\tag{4}
\]

be squarefree. No prime-power depth is needed for the obstruction. On the divisor box `D(N)`, `PC-057` gives the normalized finite boundary operator as the Kronecker sum

\[
\boxed{
C_N=\bigoplus_{p\in P}^{\rm Kron}H_{p,1}.
}
\tag{5}
\]

For `A=1`, the two local eigenvalues are

\[
\kappa_p=\frac{\log p}{p-1},
\qquad
-\log p.
\tag{6}
\]

Define

\[
\kappa(P)=\sum_{p\in P}\kappa_p,
\qquad
\beta_p:=\kappa_p+\log p
=\frac{p\log p}{p-1}.
\tag{7}
\]

Because eigenvalues of a Kronecker sum add, the global eigenvectors are indexed by subsets `S subseteq P`, where `S` records the primes at which the negative local eigenvalue is chosen. Their eigenvalues are exactly

\[
\boxed{
\lambda_S
=
\kappa(P)-\sum_{p\in S}\beta_p.
}
\tag{8}
\]

The all-positive local choice `S=emptyset` gives the top eigenvalue `kappa(P)>0`. The crucial question is whether every other subset mode is nonpositive, as a genuine one-positive-direction Hodge form would require. Equation (8) shows that this fails.

## 3. The failure already occurs on `D(30)`

Take

\[
N=30=2\cdot3\cdot5.
\]

The top eigenvalue is positive. More importantly, switch only the `p=2` factor to its negative local mode. Equation (8) gives

\[
\begin{aligned}
\lambda_{\{2\}}
&=
\frac{\log3}{2}
+
\frac{\log5}{4}
-
\log2\\
&=
\frac14\log\frac{45}{16}
>0.
\end{aligned}
\tag{9}
\]

Thus `C_30` has at least two linearly independent positive eigenvectors:

\[
\boxed{n_+(C_{30})\ge2.}
\tag{10}
\]

This is an exact finite certificate. No asymptotic estimate, analytic continuation, zeta zero, or numerical spectral computation is involved.

It immediately kills the most literal Hodge-index reinterpretation. For any codimension-one subspace `W subset D(30)`, dimension counting forces `W` to intersect the two-dimensional positive spectral subspace nontrivially. Hence the restriction of `C_30` to `W` still has a positive vector. There is **no choice of one global degree direction** whose orthogonal/primitive complement makes this finite form nonpositive.

## 4. The positive index is actually unbounded

The finite witness is not an isolated accident. Let

\[
P_r=\{p_1,\ldots,p_r\}
\]

be the first `r` primes and `N_r=prod_{p in P_r}p`. Then

\[
\kappa(P_r)
=
\sum_{p\in P_r}\frac{\log p}{p-1}.
\tag{11}
\]

This diverges as `r -> infinity`. Indeed, for all sufficiently large primes,

\[
\frac{\log p}{p-1}\ge\frac1p,
\tag{12}
\]

and Euler's prime harmonic series diverges.

Now fix any integer `m`. The numbers

\[
\beta_{p_1},\ldots,\beta_{p_m}
\]

are fixed. For all sufficiently large `r`, equation (11) exceeds all of them. Equation (8) then implies

\[
\lambda_{\{p_i\}}
=
\kappa(P_r)-\beta_{p_i}>0
\qquad(1\le i\le m),
\tag{13}
\]

in addition to `lambda_emptyset>0`. These are mutually orthogonal eigenmodes in the tensor divisor-Haar basis. Therefore

\[
\boxed{
\sup_r n_+(C_{N_r})=\infty.
}
\tag{14}
\]

So globalization does not merely change signature `(1,*)` to `(2,*)` once. The number of positive directions grows without bound as more finite places are admitted.

The same argument also shows that prime powers are not responsible for the failure. It is already forced by assembling many **squarefree, depth-one** prime directions.

## 5. No bounded-codimension primitive condition can restore a Hodge sign

Let `V_N^+` denote the positive spectral subspace of `C_N`, so

\[
\dim V_N^+=n_+(C_N).
\]

Suppose one tries to define a canonical primitive space `W_N` by imposing at most `d` global linear conditions, with `d` independent of the arithmetic cutoff. Then

\[
\operatorname{codim}W_N\le d.
\]

If `n_+(C_N)>d`, the elementary dimension inequality gives

\[
\dim(V_N^+\cap W_N)
\ge n_+(C_N)-d>0.
\tag{15}
\]

Every nonzero vector in that intersection has strictly positive `C_N`-energy. Hence `C_N|_{W_N}` cannot be nonpositive.

Combining (14) and (15),

\[
\boxed{
\text{any primitive restriction making all }C_N\text{ nonpositive must have unbounded codimension.}
}
\tag{16}
\]

This is the precise obstruction to importing the surface Hodge-index pattern. A single polarization/degree direction, or any fixed finite list of global constraints, is insufficient.

## 6. A fixed finite-dimensional archimedean sector cannot repair the inertia

There are two natural ways a finite-dimensional infinite-place sector could be attached while preserving the finite arithmetic block.

First, let a putative global pairing on

\[
\mathcal H_N^{\rm fin}\oplus\mathcal H_\infty
\]

have block matrix

\[
\mathcal Q_N
=
\begin{pmatrix}
C_N&B_N\\
B_N^*&A_\infty
\end{pmatrix},
\qquad
\dim\mathcal H_\infty=d<\infty.
\tag{17}
\]

The restriction of `mathcal Q_N` to vectors `(v,0)` is exactly `C_N`. Therefore every positive subspace of `C_N` remains a positive subspace of the full form:

\[
\boxed{
n_+(\mathcal Q_N)\ge n_+(C_N).}
\tag{18}
\]

Adjoining extra coordinates cannot turn a principal restriction with arbitrarily many positive directions into an index-one form.

Second, suppose the archimedean variables are eliminated and produce an effective finite response by Schur complement. Whenever the relevant archimedean block is invertible, the correction has the form

\[
C_N
-
B_NA_\infty^{-1}B_N^*.
\tag{19}
\]

Its difference from `C_N` has rank at most `d`. For any Hermitian rank-`d` perturbation `R`, intersecting the positive spectral subspace of `C_N` with `ker R` gives the elementary inertia bound

\[
\boxed{
n_+(C_N+R)\ge n_+(C_N)-d.}
\tag{20}
\]

Because (14) is unbounded, no fixed `d` can reduce these effective finite forms to nonpositive forms, or to forms with uniformly bounded positive index.

Thus a **fixed finite-dimensional** archimedean/global correction cannot turn the Prime-Circle finite birth block into a Hodge-index mechanism while keeping that block as the finite arithmetic input.

## 7. The full-rank scalar escape is exactly the already-known sign flip

There is an important control. The preceding result must not be misread as saying that no correction can control the positive index. `WP-034` already gives one:

\[
\kappa_N
:=
\sum_{p\mid N}\frac{\log p}{p-1},
\tag{21}
\]

and, because the largest Kronecker-sum eigenvalue is `kappa_N`,

\[
\boxed{
\kappa_N I-C_N\succeq0.
}
\tag{22}
\]

This correction is **full rank**, not a degree-one or finite-rank Hodge correction. Its local interior block is the critical Poisson/GCD kernel plus the nonnegative height diagonal identified in `WP-034`, and its off-diagonal finite-prime sign is opposite to the Weil-signed block carried by `C_N`.

Moreover `kappa_N` diverges as more primes are included and is the local `s=1` Euler-log-derivative normalization already audited in `WP-034`; it is not an independently generated Gamma/digamma contribution from the infinite place.

So (22) is exactly the control one would expect if the obstruction were merely an artifact of using the wrong sign theorem. It confirms instead that the available sign-definite completion is the **existing Poisson/pole route**, not a hidden one-positive-direction intersection form.

## 8. Matched controls and adversarial escape tests

### 8.1 Restrict to one prime ray

This preserves (3) and genuinely gives index one. But a one-ray exhaustion is not cofinal in the arithmetic divisor lattice and omits all other finite places. It cannot represent the global finite Weil term.

### 8.2 Remove the top eigenvector only

Once `n_+(C_N)>=2`, deleting any single direction leaves a positive direction by (15). The exact `N=30` certificate already defeats this repair.

### 8.3 Choose a different global degree vector

The obstruction is inertia, not the identity of the proposed degree vector. No codimension-one hyperplane can remove a positive spectral subspace of dimension at least two, irrespective of how the hyperplane is chosen.

### 8.4 Add one archimedean coordinate with arbitrary coupling

Equation (18) rules this out if the finite block remains a principal restriction. Equation (20) rules out eliminating that coordinate by Schur complement as a rank-one repair once the finite positive index exceeds one, and (14) rules out any fixed number of such coordinates globally.

### 8.5 Let the archimedean sector be infinite-dimensional

This is a genuine escape and is **not** ruled out. An infinite-dimensional boundary, scattering, cohomological, or semilocal sector can induce infinite-rank changes to the effective finite form. But such a mechanism must be derived from Mathia and must also produce the Gamma/polar structure; it is no longer the simple local-Hodge-signature globalization tested here.

### 8.6 Change the finite block before applying the sign theorem

Also open. A genuinely nonseparable construction can introduce mixed cross-prime terms before restriction to the finite-place sector. This is precisely what the Kronecker-sum form (5) lacks. The finding only rules out treating the already-derived `C_N` as the finite principal/intersection block and expecting a bounded number of global directions to supply the missing Hodge theorem.

## 9. Prior art and novelty boundary

The comparison theorem itself is classical. For divisor classes on a smooth projective surface, the Hodge index theorem gives one positive direction and a negative-definite primitive complement; the function-field Weil proof uses that global surface/intersection structure on correspondences. Those are already recorded in `SOURCES.md` through the arithmetic-surface and function-field intersection controls used by `WP-011`.

The inertia facts used above are elementary finite-dimensional linear algebra: positive index is invariant under congruence, a codimension-`d` restriction cannot remove more than `d` independent positive directions, and a rank-`d` perturbation cannot reduce positive index by more than `d`. No novelty is claimed for those principles.

The Mathia-specific result is the exact **local-to-global mismatch** forced by `PC-057`: every isolated Prime-Circle ray has the tempting index-one pattern, yet their canonical arithmetic assembly is a Kronecker sum whose positive index is already greater than one at `N=30` and is unbounded on squarefree primorial boxes. That is the opposite behavior from the single global polarization required by a direct Hodge-index explanation.

`PC-058` strengthens the structural interpretation: the exact finite-radius radial family shares a fixed tensor divisor-Haar basis, so this proliferation of independent prime modes is not an artifact of diagonalizing only the first renormalized boundary coefficient. Ordinary radial functional calculus does not introduce the missing cross-prime eigenspace mixing.

## 10. Consequence for the Weil-positivity search

The surviving requirement can now be stated more sharply:

```text
Prime-Circle local birth forms
    -> each prime separately has one positive direction
    -> canonical Kronecker-sum assembly
    -> positive index grows without bound
    -> no one-degree / bounded-codimension Hodge primitive space
    -> no fixed finite-dimensional archimedean Schur repair.
```

Therefore a future intersection/cohomological route cannot obtain global Weil positivity merely by declaring the local Prime-Circle birth forms to be intersection matrices and adding one global degree or infinite-place coordinate. It must create **nonseparable mixed structure before the sign theorem**: an infinite-rank boundary response, a true global correspondence/cohomology object, or another operation that changes the finite-place inertia while still deriving the exact finite coefficients and the archimedean Gamma/polar terms from the same geometry.

This complements `WP-011`: Prime Lattice's naive vertical cycles are null for arithmetic-surface intersection, while Prime Circle now supplies nontrivial Weil-signed local forms that look Hodge-like one prime at a time but fail the global Hodge signature when the primes are assembled.

## 11. Exact falsification tests

The claim can be falsified by any failure of the following checks:

1. the local spectrum is (1), hence `n_+(H_{p,A})=1`;
2. on a squarefree divisor box the global operator is the Kronecker sum (5);
3. its subset-mode eigenvalues are exactly (8);
4. for `N=30`, equation (9) is positive, so `n_+(C_30)>=2`;
5. `kappa(P_r)` diverges on primorials, making the singleton-substitution modes (13) positive for arbitrarily many fixed primes;
6. hence the positive index is unbounded as in (14);
7. a codimension-`d` primitive restriction cannot remove more than `d` positive directions;
8. a fixed `d`-dimensional archimedean Schur complement changes the finite block by rank at most `d` and obeys (20);
9. the full-rank shift (22) is the existing `WP-034` Poisson/GCD sign flip rather than a new archimedean/Hodge completion.
