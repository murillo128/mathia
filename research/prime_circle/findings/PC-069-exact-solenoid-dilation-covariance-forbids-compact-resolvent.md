# PC-069 — exact solenoid dilation covariance forbids compact resolvent

**Status:** `EXACT-DERIVED` + `DECISIVE-NEGATIVE` for the branch that asks a compact-resolvent Prime-Circle operator on the full compatible solenoid to transform by a pure scalar under an intrinsic power/dilation automorphism.

## Claim

PC-064 identifies the compatible all-level Prime-Circle refinement with the arithmetic solenoid

\[
\Sigma_{\mathbb Q}\cong\widehat{\mathbb Q},
\qquad
L^2(\Sigma_{\mathbb Q})
=\overline{\operatorname{span}}\{\chi_q:q\in\mathbb Q\}.
\]

For every integer `m>=2`, the coordinatewise power map

\[
D_m((x_n)_n)=(x_n^m)_n
\]

is an automorphism of `\Sigma_{\mathbb Q}`. Its Haar-Koopman unitary

\[
V_m f=f\circ D_m
\]

acts on the Pontryagin basis by

\[
\boxed{V_m\chi_q=\chi_{mq}.}
\]

Let `H` be a densely defined self-adjoint operator on `L^2(\Sigma_{\mathbb Q})` with compact resolvent, and suppose its domain is invariant under `V_m` and that for some real scalar `c`

\[
\boxed{V_m^*HV_m=cH.}
\]

Then no such `H` exists.

Thus the intrinsic all-level dilation symmetry cannot be retained as an exact homogeneous unitary covariance of an ordinary compact-resolvent Hilbert–Pólya candidate. This obstruction does **not** assume that `H` is translation-invariant, diagonal in the rational characters, a scalar function of the PC-065/067 operators, or commuting with leaf/fiber coordinates. It therefore cuts across one of the principal escape classes left open by PC-068.

The surviving options must break at least one hypothesis: pure scalar covariance, unitary two-sided dilation on the full solenoid, ordinary compact resolvent, or the full `L^2(\Sigma_{\mathbb Q})` representation.

## 1. The power map becomes an automorphism on the full compatible solenoid

Write the universal solenoid as the inverse limit of circles with bonding maps

\[
\pi_{a,b}:S^1\to S^1,
\qquad
\pi_{a,b}(z)=z^{b/a}
\quad(a\mid b).
\]

If `x=(x_n)_n` is compatible, then `(x_n^m)_n` is also compatible. More strongly, unlike the degree-`m` map on one circle, the map `D_m` is invertible on the full inverse limit. For `y\in\Sigma_{\mathbb Q}` define

\[
(D_m^{-1}y)_n=y_{mn}.
\]

Compatibility gives

\[
y_{mn}^{m}=y_n,
\]

and hence

\[
D_mD_m^{-1}=D_m^{-1}D_m=I.
\]

Equivalently, Pontryagin duality identifies `D_m` with multiplication by `m` on the discrete group `\mathbb Q`, and multiplication by `m` is an automorphism of `\mathbb Q` with inverse multiplication by `1/m`.

This distinction matters. The finite-level circle map is a noninvertible covering, whereas **completion across all compatible levels turns the same power operation into a two-sided solenoid automorphism**.

## 2. Nonzero rational characters form bilateral shift orbits

For `q\ne0`, the orbit

\[
\mathcal O_m(q)=\{m^kq:k\in\mathbb Z\}
\]

is infinite. The closed span

\[
\mathcal H_q
=\overline{\operatorname{span}}
\{\chi_{m^kq}:k\in\mathbb Z\}
\]

is invariant under `V_m`, and after identifying `\chi_{m^kq}` with the standard basis vector `e_k` of `\ell^2(\mathbb Z)`, the restriction of `V_m` is the bilateral shift.

Consequently `V_m` has no nonconstant eigenvectors. Indeed, if

\[
V_m f=\lambda f,
\qquad |\lambda|=1,
\]

then Fourier coefficients along each nonzero orbit have constant modulus. Square summability forces every coefficient on every infinite orbit to vanish. The only singleton orbit is `q=0`, so

\[
\boxed{\operatorname{Eig}(V_m)=\mathbb C\,\mathbf 1}
\]

in the sense that the only point-spectrum vectors are constants, with eigenvalue `1`.

A useful stronger corollary is

\[
\boxed{
\text{every finite-dimensional }V_m\text{-invariant subspace is contained in }\mathbb C\mathbf1.
}
\]

To see this, a finite-dimensional invariant subspace of a unitary is automatically mapped onto itself, so the finite-dimensional unitary restriction has an eigenvector. After removing the constant direction if present, any nonzero remainder would provide a forbidden nonconstant eigenvector.

The same statements hold for every positive power `V_m^r`, because it acts by `q\mapsto m^rq` and has the same bilateral-orbit structure away from `q=0`.

## 3. Non-unit scaling factors force a finite spectral accumulation point

Assume

\[
V_m^*HV_m=cH
\]

as an equality of self-adjoint operators with `V_m\operatorname{Dom}(H)=\operatorname{Dom}(H)`.

If `c=0`, unitary conjugacy immediately gives `H=0`, whose resolvent is a nonzero scalar multiple of the identity and is not compact on this infinite-dimensional Hilbert space.

Now suppose `c\ne0` and `|c|\ne1`. A self-adjoint compact-resolvent operator on an infinite-dimensional Hilbert space has a complete discrete eigenbasis, finite-dimensional eigenspaces, and no finite accumulation point in its spectrum. It cannot be identically zero, so choose

\[
H\psi=\lambda\psi,
\qquad \lambda\ne0.
\]

The covariance relation gives

\[
HV_m^k\psi=c^k\lambda\,V_m^k\psi,
\qquad k\in\mathbb Z.
\]

If `|c|<1`, take `k\to+\infty`; if `|c|>1`, take `k\to-\infty`. In either case there are infinitely many distinct eigenvalues converging to `0`:

\[
|c^k\lambda|\longrightarrow0.
\]

This contradicts compact resolvent. Therefore

\[
\boxed{|c|\ne1\quad\Longrightarrow\quad\text{no compact-resolvent }H.}
\]

This part of the obstruction is representation-independent: an invertible unitary implementing exact nontrivial scaling already creates a two-sided eigenvalue orbit with a forbidden finite accumulation point.

## 4. The isometric cases `c=1` and `c=-1` also fail on `L^2(\Sigma_Q)`

The remaining cases use the specific Prime-Circle solenoid representation.

### `c=1`

Now `H` commutes with `V_m`. Every eigenspace `E_\lambda(H)` is therefore `V_m`-invariant. Compact resolvent makes each such eigenspace finite-dimensional, so Section 2 forces

\[
E_\lambda(H)\subseteq\mathbb C\mathbf1.
\]

But the eigenspaces of a self-adjoint compact-resolvent operator must span the whole infinite-dimensional Hilbert space. They cannot all lie in the one-dimensional constant subspace. Contradiction.

### `c=-1`

Applying the covariance twice gives

\[
(V_m^2)^*H V_m^2=H.
\]

Thus every eigenspace of `H` is finite-dimensional and invariant under `V_m^2`. Since `V_m^2` also has no finite-dimensional invariant subspace outside the constants, the same contradiction follows.

Combining all cases,

\[
\boxed{
\forall m\ge2,\ \forall c\in\mathbb R:\qquad
V_m^*HV_m=cH
\ \text{and compact resolvent are incompatible on }L^2(\Sigma_{\mathbb Q}).
}
\]

There is a small useful extension. If instead

\[
V_m^*HV_m=cH+dI
\]

with `c\ne1`, then setting

\[
K=H-\frac{d}{1-c}I
\]

reduces the relation to `V_m^*KV_m=cK`; scalar shifts preserve compact resolvent. Hence **every affine law with `c\ne1` is ruled out as well**. The genuinely different affine case is the additive law `c=1`, considered in the boundary analysis below.

## 5. Diagonal homogeneous energies are only the visible special case

If one had already diagonalized in rational characters,

\[
H\chi_q=E(q)\chi_q,
\]

then exact covariance becomes a functional equation such as

\[
E(mq)=cE(q)
\]

(up to the chosen conjugation convention). The same obstruction is then visible directly: one of the two sequences `m^kq` or `m^{-k}q` has bounded, or even vanishing, energy whenever `|c|\ne1`; for `|c|=1`, infinitely many characters repeat the same bounded energy scale.

PC-069 is stronger because it does **not** assume such diagonalization. Arbitrary matrix mixing among rational characters is allowed. The contradiction comes from compactness plus the exact unitary dilation law itself.

## 6. Prior-art and novelty audit

No historical novelty is claimed for the functional-analytic ingredients. The discreteness properties of self-adjoint compact-resolvent operators, bilateral shifts, and unitary similarity are standard.

The arithmetic dynamics is also classical. PC-010 already establishes that the abstract roots-of-unity power/refinement structure is the cyclotomic/Bost–Connes tower, so the power map is not new Prime-Circle data. PC-064's contribution is to identify the **compatible geometric completion** with the arithmetic solenoid `\widehat{\mathbb Q}`, where multiplication by `m` is promoted to a genuine automorphism and therefore acts unitarily in both time directions.

Two neighboring spectral literatures were checked explicitly:

- Henri Moscovici, *Local index formula and twisted spectral triples*, Clay Mathematics Proceedings 11 (2010), 465–500, arXiv:0902.0835, uses the established notion of a scaling automorphism implemented by a unitary satisfying `UDU^*=\mu(U)D`. Thus exact scalar covariance is a standard noncommutative-geometric pattern rather than an invented wrapper.
- Valeriano Aiello, Daniele Guido and Tommaso Isola, *Spectral triples for noncommutative solenoidal spaces from self-coverings*, Journal of Mathematical Analysis and Applications 448:2 (2017), 1378–1412, DOI `10.1016/j.jmaa.2016.11.066`, arXiv:1604.08619, obtain semifinite spectral triples in solenoidal self-covering limits. Together with the proper-length solenoid work already anchored in `SOURCES.md` for PC-068, this is consistent with the fact that ordinary compact-resolvent geometry on an infinite compatible covering tower needs extra structure.

Targeted searches did not identify the exact statement above as an RH criterion or as a theorem specialized to the universal arithmetic-solenoid character action. That absence is **not** a novelty proof. The durable contribution here is the Prime-Circle-specific no-go obtained by combining the exact compatible power automorphism with ordinary compact-resolvent spectral requirements.

There is also an important Bost–Connes control. In the standard one-sided representation the multiplicative semigroup is represented by isometries rather than the two-sided Haar-Koopman unitary used here, and the usual Hamiltonian has logarithmic/additive scaling behavior. PC-069 therefore does not repackage the Bost–Connes partition function and does not rule out that classical semigroup mechanism.

## 7. Boundary of the obstruction

The theorem is deliberately narrow about the covariance law even though it is broad about the operator itself.

It does **not** rule out:

- the genuinely additive/cocycle case `V_m^*HV_m=H+dI` with `d\ne0`;
- a one-sided semigroup/isometry representation instead of the invertible solenoid automorphism;
- a semifinite spectral triple or another framework not requiring ordinary compact resolvent;
- symmetry breaking by the common anchor, primitive/old decomposition, or another embedded geometric datum;
- a proper global height/adelic scale derived independently from Prime-Circle geometry;
- nonlinear determinants or matrix data before a unitary symmetry reduction;
- or the global primitive-root uniformization/accessory branch of PC-017.

The additive boundary is genuine, not cosmetic. On a single bilateral orbit `\ell^2(\mathbb Z)`, the number operator

\[
Ne_k=k e_k
\]

has compact resolvent and the bilateral shift `S` satisfies

\[
S^*NS=N+I.
\]

So the present proof cannot be extended to pure additive covariance by a scalar shift. On the full `\mathbb Q` character set, any such construction would still need additional intrinsic data to separate the infinitely many dilation orbits and make global energy balls finite.

The one-sided boundary is equally real. On `\ell^2(\mathbb N_0)`, let

\[
He_k=m^k e_k,
\qquad
Se_k=e_{k+1}.
\]

Then `H` has compact resolvent and the unilateral shift isometry satisfies

\[
S^*HS=mH.
\]

Thus multiplicative covariance can coexist with compact resolvent once the inverse dilation direction is removed. PC-069 is specifically powered by the **two-sided automorphism that appears after taking the full compatible solenoid limit**.

## 8. Exact audit tests

The finding can be falsified at several independent points.

1. Starting from the inverse-limit definition of `\Sigma_{\mathbb Q}`, verify that `D_m((x_n))=(x_n^m)` is invertible with `(D_m^{-1}y)_n=y_{mn}`.
2. Under Pontryagin duality, verify that the Koopman unitary sends `\chi_q` to `\chi_{mq}`.
3. For every `q\ne0`, identify the `m^\mathbb Zq` orbit subspace with `\ell^2(\mathbb Z)` and recover the bilateral shift.
4. Prove that `V_m` and every `V_m^r`, `r\ge1`, have no finite-dimensional invariant subspace outside the constants.
5. For `0<|c|\ne1`, iterate the covariance on any nonzero eigenvalue of a putative compact-resolvent `H` and exhibit a spectral sequence converging to `0`.
6. For `c=1`, use finite-dimensional eigenspaces plus item 4; for `c=-1`, repeat with `V_m^2`.
7. Verify that `V_m^*HV_m=cH+dI`, `c\ne1`, reduces by a scalar shift to the pure-scaling theorem.
8. Check the boundary model `S^*NS=N+I` on `\ell^2(\mathbb Z)` and the unilateral model `S^*HS=mH` with `He_k=m^ke_k` on `\ell^2(\mathbb N_0)` to confirm that additive covariance and one-sided multiplicative covariance are genuinely outside the theorem.

Failure of items 1–7 would invalidate the obstruction. Item 8 prevents overextending it.

## Consequence for the Prime-Circle program

PC-068 showed that regular commuting leaf–fiber calculus cannot supply a compact-resolvent operator on the full rational-character space. A natural response was to keep the full all-level symmetry but abandon commuting scalar calculus and seek a more complicated operator that still transforms homogeneously under refinement.

PC-069 closes that response:

\[
\boxed{
\text{full compatible Prime-Circle solenoid}
+\text{ exact two-sided power dilation}
+\text{ pure scalar operator covariance}
\not\Longrightarrow
\text{ordinary compact-resolvent RH operator}.
}
\]

The next viable operator mechanism must therefore obtain discreteness by **breaking pure dilation covariance or changing the spectral framework**, and that break must be justified by intrinsic embedded Prime-Circle geometry rather than inserted solely to manufacture a desired zeta spectrum.
