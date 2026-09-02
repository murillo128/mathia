# PL-116 — Profinite Galois towers do not evade Frobenius scalarization under canonical central harmonic analysis

## Claim

`PL-115` leaves open a natural escape from its fixed-finite-Galois no-go: let the Galois extension grow through an infinite tower, so that the finite set of character channels is replaced by the full representation theory of a profinite Galois group. That enlargement is real, but **by itself it still does not produce a canonical operator-valued coupling of the prime coordinates** if the construction uses only the intrinsic Frobenius data and respects Galois conjugacy.

Let `L/Q` be a (possibly infinite) Galois extension unramified outside a finite set `S`, and let

`G = Gal(L/Q)`

with its profinite topology and normalized Haar measure. For `p notin S`, the intrinsic prime datum is a Frobenius conjugacy class `C_p` in `G`; choosing a prime of `L` over `p` chooses a representative, and changing that choice conjugates it. Consequently any prime-local scalar kernel depending only on the canonical Frobenius datum is a class function on `G`.

If `kappa in L^1(G)` is such a class function and `T_kappa` denotes convolution by `kappa` on `L^2(G)`, then Peter--Weyl decomposes `L^2(G)` into irreducible representation blocks and, on every irreducible continuous unitary representation `pi`, the Fourier multiplier

`hat{kappa}(pi) = integral_G kappa(g) pi(g^{-1}) dg`

is a scalar multiple of the identity. Indeed conjugacy invariance gives

`pi(h) hat{kappa}(pi) pi(h)^{-1} = hat{kappa}(pi)`

for every `h in G`, and Schur's lemma gives

`hat{kappa}(pi) = lambda_pi I`.

Moreover every continuous finite-dimensional complex representation of a profinite Galois group factors through a finite quotient. Thus passing from one finite Galois group to an inverse-limit tower produces **more scalar Artin/character channels**, but no irreducible matrix dynamics survives a canonical central convolution. In particular the trivial representation remains a one-dimensional reducing channel; in standard Artin `L`-theory its `L`-function is the base-field zeta function (for `Q`, the Riemann zeta function).

Therefore the route

`growing/profinite Galois tower + canonical Frobenius-class harmonic analysis -> irreducible operator-valued zeta channel -> RH rigidity`

is obstructed. The inverse limit removes the finite-dimensionality objection of `PL-115`, but it does **not** remove scalarization: canonicity forces the kernel into the center of the convolution algebra, and the center acts scalarly on each irreducible channel.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + DECISIVE-NEGATIVE` for conjugacy-invariant/class-function convolution or equivalent central harmonic analysis on a profinite Galois group. No novelty is claimed for Frobenius conjugacy classes, Peter--Weyl, Schur's lemma, profinite factorization of complex Artin representations, or Artin `L`-functions. The durable contribution is the line-specific closure of the most direct **profinite/growing-tower** escape explicitly left open by `PL-115`.

## 1. The infinite tower really is larger than the fixed finite case

Write the profinite Galois group as an inverse limit

`G = lim_<- G_i`,

where each `G_i = Gal(L_i/Q)` is a finite Galois quotient. The space of conjugacy-invariant functions on `G` need not be finite-dimensional, so the finite character-basis argument of `PL-115` cannot simply be repeated with a fixed finite sum. A priori this is therefore a genuine escape attempt rather than a restatement of the fixed-group result.

The crucial replacement is compact-group harmonic analysis. Peter--Weyl gives a Hilbert decomposition

`L^2(G) ~= direct_sum_hat_{pi in G^} V_pi tensor V_pi^*`

through the continuous finite-dimensional irreducible unitary representations of `G`. For a profinite group these representations factor through finite quotients, but there may be infinitely many inequivalent quotients and irreducibles across the tower. Rank growth is therefore present at the level of the *family* of channels.

What fails is the inference that this rank growth supplies noncommuting matrix information to the canonical Frobenius channel.

## 2. Canonical Frobenius dependence is central

For a finite Galois extension, a rational prime determines Frobenius only up to conjugacy; this is the gauge point used in `PL-115`. The same compatibility survives the inverse limit. For an unramified `p`, choosing a prime of `L` above `p` yields compatible Frobenius representatives in the finite quotients. Another choice conjugates the compatible family. Hence a scalar datum intrinsically attached to `p` through Frobenius alone can depend only on the resulting conjugacy class.

Let `kappa:G->C` be integrable and conjugacy invariant. Define left convolution

`(T_kappa f)(x) = integral_G kappa(g) f(g^{-1}x) dg`.

For an irreducible continuous unitary representation `pi`, its Fourier multiplier is

`hat{kappa}(pi)=integral_G kappa(g) pi(g^{-1}) dg`.

For any `h in G`, Haar invariance and the substitution `g -> hgh^{-1}` give

`pi(h) hat{kappa}(pi) pi(h)^{-1}
 = integral_G kappa(h^{-1}gh) pi(g^{-1}) dg
 = hat{kappa}(pi)`.

Thus `hat{kappa}(pi)` lies in the commutant of the irreducible representation. Over `C`, Schur's lemma gives exactly

`hat{kappa}(pi)=lambda_pi I_{V_pi}`.

This is the compact/profinite analogue of the finite character scalarization in `PL-115`. The matrix coefficient space `V_pi tensor V_pi^*` may have dimension greater than one, but a central convolution does not use that matrix freedom: it only assigns the scalar `lambda_pi` to the irreducible type.

## 3. The inverse limit is a union of finite Artin channels, not a new complex matrix channel

A second structural fact makes the relation to `PL-115` sharp. A continuous complex finite-dimensional representation of the absolute/profinite Galois group has finite image and therefore factors through some finite Galois quotient. Jack Thorne states this explicitly for `G_Q`: every continuous `rho:G_Q->GL_n(C)` factors through `Gal(K/Q)` for a finite Galois extension `K/Q`.

Accordingly, each Peter--Weyl/Artin channel in the profinite tower is already visible at a finite stage. Passing to the inverse limit can make the set of channels unbounded, but it does not create a single irreducible complex representation that coherently sees infinitely many finite stages with new matrix degrees of freedom.

This distinction matters for the `PL-115` escape. A growing tower can defeat a **uniform finite-channel count**, but if the observable remains central then its harmonic action still has the diagonal form

`T_kappa |_(pi-block) = lambda_pi I`.

The tower is therefore an infinite scalar direct sum, not a canonical noncommutative carrier for the Riemann divisor.

## 4. Relation to Artin `L`-functions and the zeta channel

For a finite quotient and a complex representation `rho`, the standard Artin Euler factor is built from the characteristic polynomial of `rho(Frob_p)`; this is well-defined precisely because it is conjugacy invariant. Thorne's exposition emphasizes both points: Frobenius at an unramified rational prime is intrinsically a conjugacy class, and the determinant defining the local Artin factor depends only on that class.

The trivial representation is one-dimensional. Its Artin `L`-function is the Dedekind zeta function of the base field; for the base field `Q` this is the ordinary Riemann zeta function. Thus any central profinite harmonic model that is subsequently read through ordinary Artin `L`-data contains the Riemann-zeta channel as a scalar block from the start.

This does **not** mean that all Artin channels are trivial or that their analytic continuation is elementary. It means only that central harmonic analysis does not generate an operator relation that mixes the scalar Riemann channel with higher-dimensional representation spaces. Any theorem constraining the Riemann zeros would still need an additional relation between the scalars `lambda_pi`, or between their associated `L`-functions, that is not supplied by Peter--Weyl decomposition itself.

The scalarization argument is purely representation-theoretic and does not use analytic continuation. Artin Euler products are invoked only in their ordinary convergence domain when identifying the classical channels; no termwise Euler-product continuation into the critical strip is assumed.

## 5. Prior-art and novelty audit

The ingredients are classical or standard.

- **Jack A. Thorne**, “Reciprocity and symmetric power functoriality,” *Current Developments in Mathematics 2021* (International Press, 2023), 95--162. In section 2.4 he explains that Frobenius for a rational prime is a conjugacy class and that Artin local factors are conjugacy-invariant determinants; in section 2.5 he writes `G_Q` as the profinite inverse limit of finite Galois groups and explicitly states that every continuous complex finite-dimensional representation of `G_Q` factors through a finite quotient.
- **Alain Robert**, *Introduction to the Representation Theory of Compact and Locally Compact Groups*, London Mathematical Society Lecture Note Series 80, Cambridge University Press, 1983, especially Chapters 4--7. This is a standard Peter--Weyl, regular-representation, convolution, and character-theory anchor for compact groups.
- The finite Frobenius/class-function/Artin specialization and its nearest number-theoretic literature were already audited in `PL-115`, including Fiorilli--Jouve, Coleman, and Alberts.

No search located a theorem stated in the exact `prime_lattice` language above, but the no-go is an immediate synthesis of these standard structures. It must therefore be treated as a **route classification**, not as a new theorem in compact representation theory or Galois theory.

## 6. Adversarial boundaries

1. **Only central/conjugacy-invariant harmonic analysis is ruled out.** A genuinely noncentral kernel on `G` has matrix-valued Fourier multipliers `hat{kappa}(pi)` and is not covered. However, Frobenius conjugacy classes alone do not canonically specify such a kernel; additional frame, decomposition-group, local-vector, or transport data must be supplied and justified.
2. **Cross-isotypic operators are not ruled out.** An operator not given by central convolution may couple distinct Peter--Weyl blocks. Such a coupling is precisely extra global structure and must prove its arithmetic canonicity rather than being freely chosen.
3. **Non-archimedean coefficient representations are different.** Continuous `p`-adic Galois representations need not factor through finite quotients; Thorne explicitly contrasts them with complex Artin representations. A `p`-adic/cohomological construction is outside this finding and would need a separate route audit.
4. **An unbounded family can still carry deep information.** The finding does not say that infinitely many Artin `L`-functions are equivalent to finitely many. It says that merely taking their profinite inverse-limit representation space leaves the canonical central action block-scalar.
5. **Chebotarev density is not the mechanism.** Density/equidistribution of Frobenius classes may constrain averages of the scalar channels but is neither used nor claimed to force critical-line zero localization.
6. **The no-go is not a theorem about arbitrary global Galois constructions.** Cohomology, trace formulas, deformation spaces, compatible `ell`-adic systems, automorphic reciprocity, or target-relative operators can provide additional coupling not present in class-function convolution.

## Consequence for the research line

`PL-115` showed that one fixed nonabelian Galois group does not rescue prime-pair geometry from scalar character decomposition, but explicitly left growing Galois complexity as an escape. The direct inverse-limit repair can now be narrowed:

`fixed finite Galois group -> finitely many scalar character channels` (`PL-115`), while

`profinite Galois tower + canonical conjugacy-invariant convolution -> infinitely many possible irreducible channels, each still scalar on its Peter--Weyl block` (`PL-116`).

Thus **growth in the number or dimensions of Galois representations is not enough**. A viable local-global continuation must identify a canonical structure that is not central: a cross-representation coupling, a target-relative constraint, compatible non-archimedean/cohomological data, or another mechanism whose matrix content survives the conjugacy gauge and actually imposes a falsifiable restriction on the scalar Riemann-zeta channel.