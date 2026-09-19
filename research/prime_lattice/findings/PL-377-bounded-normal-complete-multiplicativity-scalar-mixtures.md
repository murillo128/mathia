# PL-377 — Bounded normal completely multiplicative representations disintegrate into scalar prime semicharacters

**Evidence:** `EXACT-DERIVED + STANDARD-GELFAND/SPECTRAL-THEOREM + SEMIGROUP-HARMONIC-PRIOR-ART + DECISIVE-NARROWING`.

**Parent finding:** `PL-376`.

**Related findings:** `PL-003`, `PL-011`, `PL-023`, `PL-374`, `PL-376`.

**Status:** `THE-INFINITE-DIMENSIONAL-ESCAPE-LEFT-BY-PL-376-DOES-NOT-OPEN-INSIDE-BOUNDED-NORMAL-EXACT-COMPLETE-MULTIPLICATIVITY: EVERY-BOUNDED-LINEAR-OBSERVABLE-IS-A-MEASURE-SUPERPOSITION-OF-SCALAR-COMPLETELY-MULTIPLICATIVE-SEMICHARACTERS; IN-THE-UNITARY-CASE-THIS-IS-LITERALLY-A-MEASURE-ON-THE-PRIME-TORUS. ANY-NEW-RH-RIGIDITY-MUST-ENTER-THROUGH-EXTRA-GLOBAL-RESTRICTIONS-ON-THAT-MEASURE/SUPPORT, NONNORMALITY, UNBOUNDEDNESS, NONLINEAR-OBSERVABLES, OR-FAILURE-OF-EXACT-COMPLETE-MULTIPLICATIVITY`.

## Claim

Let `H` be a complex Hilbert space and let

\[
\rho:\mathbb N_{>0}\longrightarrow B(H),
\qquad
\rho(1)=I,
\qquad
\rho(mn)=\rho(m)\rho(n).
\tag{PL377-1}
\]

Write `A_p=rho(p)` and assume that every `A_p` is a bounded normal operator. Complete multiplicativity and commutativity of the positive integers give

\[
A_pA_q=A_qA_p
\qquad(p,q\text{ prime}).
\tag{PL377-2}
\]

Because the operators are normal, Fuglede's theorem upgrades pairwise commutation to commutation with adjoints. Hence the unital `C*`-algebra

\[
\mathcal A=C^*(A_p:p\text{ prime})
\tag{PL377-3}
\]

is abelian. Let `X` be its Gelfand spectrum. For `x in X`, define

\[
\lambda_p(x)=x(A_p).
\tag{PL377-4}
\]

Then the Gelfand transform sends every arithmetic operator to the scalar function

\[
\widehat{\rho(n)}(x)
=
\prod_p\lambda_p(x)^{v_p(n)}
=:\chi_x(n).
\tag{PL377-5}
\]

For every fixed `x`, `chi_x` is a scalar completely multiplicative function. Thus the whole bounded normal operator representation is a continuous field of scalar prime-axis semicharacters.

More strongly, let `L` be any bounded linear functional on `mathcal A`; this includes every matrix coefficient `L(T)=<T xi,eta>`. By the commutative Gelfand--Naimark theorem and the Riesz--Markov representation theorem there is a finite complex regular Borel measure `mu_L` on `X` such that

\[
\boxed{
L(\rho(n))
=
\int_X \chi_x(n)\,d\mu_L(x).
}
\tag{PL377-6}
\]

If `L` is positive, `mu_L` is positive. Therefore **every bounded linear scalar readout of an infinite-dimensional bounded normal completely multiplicative prime representation is a measure superposition of scalar completely multiplicative channels**.

This is the infinite-dimensional normal analogue of the finite-dimensional scalarization in `PL-374`/`PL-376`, but with a potentially continuous measure of scalar channels rather than a finite sum or finite jet.

## 1. Why the generated operator algebra is abelian

Equation (PL377-2) alone says only that the prime generators commute as operators. To use `C*`-spectral theory one also needs the adjoints to commute. For bounded normal operators this follows from Fuglede's commutativity theorem: if `N` is normal and `TN=NT`, then `TN*=N*T`. Applying this to every pair `A_p,A_q` gives

\[
A_pA_q^*=A_q^*A_p,
\]

and taking adjoints gives all remaining mixed commutations. Consequently every `*`-polynomial in the prime operators commutes with every other one, and its norm closure `mathcal A` is a commutative unital `C*`-algebra.

The commutative Gelfand--Naimark theorem identifies

\[
\mathcal A\simeq C(X)
\tag{PL377-7}
\]

for a compact Hausdorff spectrum `X`. Since the set of primes is countable, `mathcal A` is separable, so `X` can in fact be taken compact metrizable; no finite-dimensionality is involved.

Now

\[
\rho(n)=\prod_p A_p^{v_p(n)}
\tag{PL377-8}
\]

with only finitely many nontrivial factors. Characters of `mathcal A` are multiplicative, so applying `x in X` to (PL377-8) gives exactly (PL377-5). The prime-exponent vector enters only through the monomial

\[
\chi_x(n)
=
\lambda(x)^{v(n)}.
\]

Thus normal exact complete multiplicativity has not produced an irreducibly operator-valued prime coupling: at each spectral point it is a scalar exponent-lattice character/semicharacter.

## 2. Unitary representations reduce literally to prime-torus harmonic analysis

Suppose in addition that every `A_p` is unitary. Then every Gelfand coordinate satisfies

\[
|\lambda_p(x)|=1,
\]

so the map

\[
x\longmapsto (\lambda_p(x))_p
\]

embeds the joint spectrum into the infinite prime torus `T^P` (possibly with relations, so the image need not be the full torus). Equation (PL377-6) becomes

\[
L(\rho(n))
=
\int_X
\prod_p z_p^{v_p(n)}\,d\mu_L(z).
\tag{PL377-9}
\]

This is precisely a Fourier--Stieltjes coefficient on the exponent lattice. Each integrand is a unimodular completely multiplicative prime-phase twist of the same Helson/Bohr type already used as a falsification control in `PL-003` and as the character basis of the Kronecker flow in `PL-011`.

Hence passing from a finite-dimensional unitary prime representation to an arbitrary bounded infinite-dimensional unitary one does **not** create a new source geometry. It replaces a finite orthogonal sum of scalar characters by a spectral measure over scalar characters on a compact subset of the prime torus.

A special measure can of course carry additional arithmetic information. For example the point mass at the all-ones character recovers the untwisted scalar channel. The conclusion is therefore not that measures on the prime torus are useless; it is that any useful rigidity must be a nontrivial theorem about the **specific measure/support/global boundary condition**, rather than a consequence of infinite-dimensional unitary complete multiplicativity itself.

## 3. Contractive case: Dirichlet series are mixtures of scalar Euler channels in the honest convergence half-plane

Assume the stronger uniform condition

\[
\|A_p\|\le 1
\qquad\text{for every prime }p.
\tag{PL377-10}
\]

Then `|lambda_p(x)|<=1`, hence `|chi_x(n)|<=1` for every `x,n`. For `sigma=Re(s)>1`, equation (PL377-6) may be summed under the integral by absolute domination:

\[
\sum_{n\ge1}
\frac{L(\rho(n))}{n^s}
=
\int_X
\left(
\sum_{n\ge1}\frac{\chi_x(n)}{n^s}
\right)d\mu_L(x).
\tag{PL377-11}
\]

For each `x`, unique factorization gives the absolutely convergent scalar Euler product

\[
\sum_{n\ge1}\frac{\chi_x(n)}{n^s}
=
\prod_p
\left(1-\lambda_p(x)p^{-s}\right)^{-1},
\qquad \Re(s)>1.
\tag{PL377-12}
\]

Thus

\[
\boxed{
F_L(s)
=
\int_X
\prod_p
\left(1-\lambda_p(x)p^{-s}\right)^{-1}
d\mu_L(x),
\qquad \Re(s)>1.
}
\tag{PL377-13}
\]

No continuation into `Re(s)<=1` follows from this formula. A continuation of the mixture, or an interchange of continuation with the spectral integral, requires an independent theorem. This is exactly the analytic-continuation boundary demanded by the Prime-Lattice mandate: the operator spectral theorem explains the source representation but does not transport Euler products into the critical strip.

## 4. Relation to classical semigroup harmonic analysis

The structural ingredients are classical prior art, not a novelty claim.

- The commutative Gelfand--Naimark theorem identifies a commutative unital `C*`-algebra with `C(X)`, and Riesz--Markov identifies bounded linear functionals on `C(X)` with complex regular Borel measures. A convenient operator-theoretic spectral-theorem reference is Markus Haase, “The Functional Calculus Approach to the Spectral Theorem,” arXiv:2003.06130, which develops joint functional calculus for strongly commuting normal operators: https://arxiv.org/abs/2003.06130.
- Edwin Hewitt and Herbert S. Zuckerman, “The `l^1`-Algebra of a Commutative Semigroup,” *Transactions of the American Mathematical Society* **83** (1956), 70--97, DOI `10.2307/1992906`, is classical semigroup-algebra prior art for bounded semicharacters of commutative semigroups: https://doi.org/10.2307/1992906.
- Christian Berg, Jens Peter Reus Christensen, and Paul Ressel, *Harmonic Analysis on Semigroups: Theory of Positive Definite and Related Functions*, Graduate Texts in Mathematics 100, Springer, 1984, DOI `10.1007/978-1-4612-1128-0`, develops integral representation of positive-definite functions on abelian semigroups in terms of multiplicative functions/semicharacters: https://doi.org/10.1007/978-1-4612-1128-0.

A targeted audit also found Boyu Li, “Normal Extensions of Representations of Abelian Semigroups,” *Canadian Mathematical Bulletin* **61**(4) (2018), 741--754, arXiv:1507.06698, as close modern operator-semigroup context: https://arxiv.org/abs/1507.06698. That work studies when abelian-semigroup representations admit commuting normal extensions.

No novelty is claimed for spectral disintegration itself. The durable `prime_lattice` delta is the exact boundary it imposes on the post-`PL-376` research fork: **infinite dimension alone is not an escape if the prime representation remains bounded, normal, and exactly completely multiplicative**. The operator layer then reduces to classical scalar semicharacter harmonic analysis.

## 5. Adversarial audit and exact boundary of the no-go

### A continuum of scalar channels is not the same as a finite sum

Equation (PL377-6) can involve an arbitrary finite complex measure on an infinite-dimensional spectrum. Such a continuum can exhibit cancellations unavailable to a finite scalar sum. The result therefore does not reduce every infinite-dimensional normal construction to `PL-374` literally, nor does it imply that the resulting Dirichlet series has simple analytic behavior.

What it does prove is that any such behavior is already expressible as **measure-level superposition of scalar completely multiplicative channels**. If an RH-relevant cancellation occurs, its extra content lies in a special restriction on `mu_L`, on the support `X`, or on how continuation acts on the integral; it is not irreducible non-scalar geometry of the normal representation.

### Normality is load-bearing

Commuting bounded operators need not generate an abelian `C*`-algebra unless their adjoints commute as well. Normality plus Fuglede supplies that missing `*`-commutation. A commuting nonnormal family can generate a nonselfadjoint operator algebra with extension, dilation, invariant-subspace, and pseudospectral structure that is not captured by (PL377-6). This finding does not close that route.

### Boundedness is load-bearing

For unbounded normal operators, pointwise commutation on a common domain is not enough. One needs strong/spectral commutation and careful domain control before a joint spectral theorem applies. `PL-377` therefore does not close the unbounded route highlighted after `PL-376`. If an unbounded construction merely has strongly commuting normal generators, an analogous joint spectral calculus is available, but the domain and observable questions must be proved separately rather than imported from the bounded theorem.

### Nonlinear observables are outside the linear measure formula

Norms, pseudospectra, Fredholm determinants of global combinations, nonlinear optimizations, boundary scattering constructions, and target-relative projections are not bounded linear functionals on `mathcal A` in the sense used in (PL377-6). They can introduce additional mathematics. As in `PL-376`, any gain must then be attributed to that extra nonlinear/global operation and audited independently.

### No rational-prime rigidity is generated automatically

The spectral coordinates `lambda_p(x)` may be chosen with enormous freedom. In the unitary case they are prime phases, exactly the ambient Helson freedom against which this line must test purported arithmetic mechanisms. A support relation among different primes can restrict that freedom, but such a relation is additional global input. Exact complete multiplicativity plus normality by themselves do not distinguish the rational-prime norm map from a generic free abelian prime-indexed semigroup.

## Consequence for `prime_lattice`

`PL-376` left “infinite-dimensional/unbounded global representation” as one of the surviving ways to escape finite Artinian scalar jets. The present result splits that branch sharply.

The **bounded normal** half is now reduced to the classical character space: prime operators become coordinate functions on a compact spectrum and every bounded linear observable is an integral of scalar completely multiplicative semicharacters. In the unitary case this is literally Bohr/Helson harmonic analysis on a compact subset of the infinite prime torus.

Therefore a genuinely new representation-theoretic mechanism must leave at least one of the assumptions used here: it must exploit nonnormal operator structure, genuinely unbounded/domain-sensitive geometry, controlled failure of exact complete multiplicativity, or a nonlinear/global/target-relative operation carrying independently justified rational-prime information. Merely replacing the finite matrices of `PL-376` by a bounded infinite-dimensional normal family does not create the missing RH mechanism.