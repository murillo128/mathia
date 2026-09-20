# PL-385 — The norm-closed prime-shift algebra preserves discrete orientation but is a universal polydisk algebra

**Evidence:** `EXACT-DERIVED + CLASSICAL-BOHR/KRONECKER + PRIOR-ART-AUDITED + DECISIVE-NEGATIVE`.

**Parent finding:** `PL-384`.

**Related findings:** `PL-001`, `PL-011`, `PL-017`, `PL-382`, `PL-383`, `PL-384`.

**Status:** `THE-NORM-CLOSED-NONSELFADJOINT-ALGEBRA-EVADES-THE-COMMUTANT/SOT-COLLAPSE-OF-PL-383--PL-384, BUT-ONLY-BY-RETAINING-THE-ABSTRACT-FREE-POSITIVE-MONOID. FOR-EVERY-FINITE-Q-LINEARLY-INDEPENDENT-TIME-TUPLE ITS-GENERATED-NORM-ALGEBRA-IS-ISOMETRIC-TO-THE-CORRESPONDING-POLYDISK-ALGEBRA, INDEPENDENT-OF-THE-ACTUAL-TIME-VALUES. FOR-THE-PRIME-TIMES, THE-COUNTABLE-ALGEBRA-IS-THE-UNIFORM-CLOSURE-OF-ANALYTIC-CYLINDER-POLYNOMIALS-ON-T_INFINITY. NONINTEGER-DILATIONS-DO-NOT-ENTER-THIS-NORM-CLOSURE: A-PURE-SHIFT-WITH-TIME-OUTSIDE-log(N)-HAS-NORM-DISTANCE-EXACTLY-1-FROM-THE-PRIME-GENERATED-ALGEBRA. THUS-NORM-TOPOLOGY-RETAINS-DISCRETE-ORIENTATION-BUT-NOT-THE-NUMERICAL-log(p)-GEOMETRY; ANY-Q-INDEPENDENT-POSITIVE-FREQUENCY-SEQUENCE-GIVES-THE-SAME-ABSTRACT-ALGEBRA. A-SURVIVING-RH-MECHANISM-MUST-ADD-WEIGHT-SENSITIVE-OR-TARGET-RELATIVE-STRUCTURE`.

## Claim

Let `(S_t)_{t>=0}` be the right-shift semigroup on `L^2(R_+)`,

\[
(S_tf)(x)=
\begin{cases}
f(x-t),&x\ge t,\\
0,&0\le x<t,
\end{cases}
\]

as in `PL-382`--`PL-384`. For positive times `tau=(t_1,...,t_d)` which are linearly independent over `Q`, define the unital norm-closed operator algebra

\[
\mathcal A_\tau
=
\overline{\operatorname{alg}}^{\|\cdot\|}
\{I,S_{t_1},...,S_{t_d}\}.
\tag{PL385-1}
\]

Then the polynomial functional calculus

\[
P(z_1,...,z_d)
\longmapsto
P(S_{t_1},...,S_{t_d})
\tag{PL385-2}
\]

is isometric for the uniform norm on the closed polydisk. Consequently

\[
\boxed{\mathcal A_\tau\cong_{\rm iso} A(\mathbb D^d),}
\tag{PL385-3}
\]

where `A(D^d)` denotes the uniform closure on `T^d` of analytic polynomials in the coordinate functions. In particular the Banach-algebra isomorphism type does not depend on the numerical values of the `t_j`, only on their rational independence and the number of generators.

For the rational-prime times

\[
t_p=\log p,
\]

let

\[
\mathcal A_{\mathbb P}
=
\overline{\operatorname{alg}}^{\|\cdot\|}
\{I,S_{\log p}:p\text{ prime}\}.
\tag{PL385-4}
\]

Then `A_P` is isometric to the uniform closure of analytic cylinder polynomials on `T^infinity`: polynomials depending on finitely many coordinates and involving only nonnegative powers. Under this identification,

\[
z^{v(n)}\longleftrightarrow S_{\log n}.
\tag{PL385-5}
\]

Moreover the norm closure retains the positive semigroup sharply. For every `t>=0`,

\[
\boxed{
\operatorname{dist}(S_t,\mathcal A_{\mathbb P})
=
\begin{cases}
0,&t=\log n\text{ for some }n\in\mathbb N,\\
1,&t\notin\log\mathbb N.
\end{cases}}
\tag{PL385-6}
\]

Thus the topology-sensitive escape left open in `PL-384` is real but not arithmetic-specific: norm closure prevents the continuous-time collapse, while the algebra it leaves behind remembers only the free commutative positive monoid. Replacing `(log p)_p` by any positive `Q`-linearly independent sequence produces the same abstract norm algebra with the corresponding distinguished coordinate generators.

## 1. Laplace transform turns shifts into analytic multipliers

Let

\[
\mathcal L:L^2(\mathbb R_+)\to H^2(\mathbb C_+)
\]

be the standard unitary Laplace transform, with harmless normalization suppressed. Direct calculation gives

\[
\mathcal L S_t\mathcal L^{-1}=M_{e^{-tz}},
\tag{PL385-7}
\]

where `M_phi` denotes multiplication by `phi` on the Hardy space of the right half-plane. Since a bounded analytic multiplier of `H^2(C_+)` has multiplier norm equal to its `H^infinity` norm, for every analytic polynomial `P` in `d` variables,

\[
\|P(S_{t_1},...,S_{t_d})\|
=
\sup_{\Re z>0}
|P(e^{-t_1z},...,e^{-t_dz})|.
\tag{PL385-8}
\]

The boundary values at `z=iy` are

\[
P(e^{-it_1y},...,e^{-it_dy}).
\tag{PL385-9}
\]

Because `t_1,...,t_d` are `Q`-linearly independent, Kronecker's theorem says that

\[
y\longmapsto
(e^{-it_1y},...,e^{-it_dy})
\tag{PL385-10}
\]

has dense range in `T^d`. Hence

\[
\sup_{y\in\mathbb R}
|P(e^{-it_1y},...,e^{-it_dy})|
=
\max_{\zeta\in\mathbb T^d}|P(\zeta)|.
\tag{PL385-11}
\]

The half-plane supremum in (PL385-8) equals its boundary supremum, and the maximum-modulus principle on the polydisk gives

\[
\boxed{
\|P(S_{t_1},...,S_{t_d})\|
=
\|P\|_{C(\mathbb T^d)}.}
\tag{PL385-12}
\]

Completing the analytic polynomials proves (PL385-3).

For distinct primes `p_1,...,p_d`, the numbers `log p_1,...,log p_d` are `Q`-linearly independent: a rational relation, after clearing denominators, would give a multiplicative relation among distinct primes, contradicting unique factorization. Therefore every finite-prime corner of (PL385-4) is exactly the same polydisk algebra `A(D^d)`.

## 2. The infinite-prime algebra is independent of the numerical prime weights

Every polynomial in the prime shifts involves finitely many primes, so (PL385-12) identifies its norm with the uniform norm of the same analytic cylinder polynomial on `T^infinity`. Passing to the norm completion yields an isometry

\[
\mathcal A_{\mathbb P}
\cong
\overline{\mathbb C[z_1,z_2,...]}^{\|\cdot\|_{C(\mathbb T^\infty)}},
\tag{PL385-13}
\]

where each polynomial uses finitely many variables and only nonnegative powers.

Now let `(b_j)_{j>=1}` be any positive `Q`-linearly independent sequence and form

\[
\mathcal A_b
=
\overline{\operatorname{alg}}^{\|\cdot\|}
\{I,S_{b_j}:j\ge1\}.
\]

The same finite-coordinate argument gives an isometric generator-preserving algebra isomorphism

\[
\boxed{
\mathcal A_b\cong\mathcal A_{\mathbb P},
\qquad
S_{b_j}\longleftrightarrow S_{\log p_j}.}
\tag{PL385-14}
\]

So the numerical geometry of the prime frequencies is absent from the abstract norm algebra. The algebra knows that there is a free countable commutative monoid of positive generators; it does not know that the generator energies happen to be `log 2, log 3, log 5, ...`.

This is exactly the line-specific matched control demanded by the Prime Lattice mandate. A norm-algebraic phenomenon that follows only from (PL385-13) also occurs for a generic rationally independent frequency sequence and therefore cannot by itself distinguish the rational primes.

## 3. Norm closure nevertheless does not recover continuous time

The preceding universality must not be confused with the strong/commutant collapse of `PL-383`--`PL-384`. Norm topology still sees the orientation of the positive semigroup.

For a bounded uniformly almost-periodic function `f` on `R`, write its Bohr coefficient at frequency `lambda` as

\[
\widehat f_B(\lambda)
=
\lim_{T\to\infty}
\frac1{2T}
\int_{-T}^{T}f(y)e^{i\lambda y}\,dy.
\tag{PL385-15}
\]

On the uniform almost-periodic algebra this is a norm-continuous functional with

\[
|\widehat f_B(\lambda)|\le\|f\|_\infty.
\tag{PL385-16}
\]

The boundary function of every polynomial in the prime shifts has frequencies only in

\[
\Gamma_{\mathbb P}^+
=
\left\{\sum_p\alpha_p\log p:
\alpha_p\in\mathbb N_0,
\ \alpha\text{ finitely supported}\right\}
=
\{\log n:n\in\mathbb N\}.
\tag{PL385-17}
\]

Uniform limits cannot create a nonzero Bohr coefficient outside this set. On the other hand the boundary multiplier corresponding to `S_t` is the character `e^{-ity}`, whose Bohr coefficient at `t` equals `1`. Hence if `t` is not in `Gamma_P^+`, then for every `A in A_P`,

\[
1
=
|\widehat{(e^{-ity}-A)}_B(t)|
\le
\|S_t-A\|.
\tag{PL385-18}
\]

Taking `A=0` supplies the reverse inequality because `||S_t||=1`, proving the second line of (PL385-6). If `t=log n`, then unique factorization gives

\[
S_t=S_{\log n}=\prod_pS_{\log p}^{v_p(n)}\in\mathcal A_{\mathbb P},
\]

which proves the first line.

Thus, for example,

\[
\operatorname{dist}(S_{\log(3/2)},\mathcal A_{\mathbb P})=1.
\tag{PL385-19}
\]

Equivalently in the original Nyman dilation model, the ambient norm-closed algebra generated by the integer/prime dilations does not contain `D_{3/2}`. This is the precise norm-topology distinction that `PL-383` and `PL-384` deliberately left open.

## 4. Consequence for the prime-lattice route

The three ambient closure regimes now separate cleanly.

After adjoints and strong closure, `PL-383` shows that two prime times already generate all of `B(L^2)`. At the commutant level, `PL-384` shows that two prime times already have exactly the same bounded commutant as the full continuous shift semigroup. The norm-closed positive algebra does retain the discrete monoid, by (PL385-6), but (PL385-14) shows that this surviving object is universal for rationally independent positive frequencies.

Therefore the norm-closed algebra alone cannot supply the arithmetic rigidity sought by this line. To reinsert the actual prime norm map one needs additional structure that is not an invariant of the abstract analytic monoid algebra. Natural surviving examples include the positive-energy generator `H` satisfying

\[
[H,S_{\log p}]=(\log p)S_{\log p},
\tag{PL385-20}
\]

Mellin/analytic-continuation data, the distinguished Nyman target and invariant subspace, or another source-sensitive relation that couples the numerical weights to arithmetic information. This finding makes no claim that any of those additions succeeds; it only shows that the ambient norm algebra by itself has already quotiented away the numerical prime geometry.

The restriction to the Nyman step space remains outside the present negative result. A compressed or restricted representation can carry target-relative information that is absent from the ambient norm algebra, just as noted in `PL-384`.

## 5. Prior-art and novelty audit

The harmonic ingredients are classical. The Bohr correspondence for ordinary Dirichlet series, with prime exponents as torus Fourier multiindices, is standard and is already anchored in this line by Hedenmalm--Lindqvist--Seip, *Duke Math. J.* 86 (1997), 1--37. Kronecker density for rationally independent frequencies is standard and already part of the `PL-011` audit surface.

The broader general-Dirichlet-series literature makes the non-arithmetic character especially explicit. Andreas Defant and Ingo Schoolmann, “H_p-Theory of General Dirichlet Series,” *J. Fourier Anal. Appl.* 25 (2019), 3220--3258, develops Hardy spaces through Dirichlet groups and Bohr matrices; Corollary 3.28 states that frequencies with the same Bohr matrix (up to a row permutation) yield the same `H_p` Banach spaces with coefficients preserved. Their survey “Hardy spaces of general Dirichlet series,” *Banach Center Publ.* 119 (2019), 123--149, describes the same Bohr-matrix mechanism. Ingo Schoolmann, “On Bohr's theorem for general Dirichlet series,” *Math. Nachr.* 293 (2020), 1591--1612, explicitly uses Kronecker's theorem for `Q`-linearly independent frequencies.

Accordingly, no novelty is claimed for the polydisk/Bohr identification itself, nor for the fact that rationally independent frequency bases give the same torus norm geometry. The exact operator-algebra formulation (PL385-3)--(PL385-6) is an elementary consequence of that classical machinery plus the Laplace multiplier model. The durable contribution is the route-specific falsification result: **the norm-closed nonselfadjoint loophole left after `PL-384` does preserve discreteness, but only at the universal free-monoid level and therefore fails the rational-prime versus generic-frequency control.**

## 6. Falsification conditions and boundaries

This finding should be corrected or withdrawn if any of the following fails:

1. the Laplace-transform identity (PL385-7) or equality of analytic multiplier norm with the `H^infinity(C_+)` norm;
2. Kronecker density in (PL385-10) for every finite `Q`-independent time tuple;
3. the passage from finite cylinder polynomials to the countable uniform closure in (PL385-13);
4. norm continuity of Bohr coefficients on the uniform almost-periodic algebra, used to prove (PL385-6);
5. the distinction between the abstract norm algebra and an enriched object carrying the numerical energy labels `t_j` through a generator, derivation, representation, or distinguished target.

The result does **not** say that all weighted or covariant prime-lattice representations are equivalent. It says precisely the opposite boundary statement: the unweighted ambient norm-closed analytic algebra is too coarse, so any successful arithmetic mechanism must use structure beyond that algebra.