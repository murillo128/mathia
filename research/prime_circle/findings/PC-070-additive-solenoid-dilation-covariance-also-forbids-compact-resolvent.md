# PC-070 — additive solenoid dilation covariance also forbids compact resolvent

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `DECISIVE-NEGATIVE` for the additive/cocycle covariance boundary left open by PC-069 on the full compatible Prime-Circle solenoid and its natural mean-zero subspace.

## Claim

PC-069 proves that the intrinsic power automorphism

\[
D_m:\Sigma_{\mathbb Q}\to\Sigma_{\mathbb Q},
\qquad m\ge2,
\]

with Haar-Koopman unitary

\[
V_m\chi_q=\chi_{mq},
\qquad q\in\mathbb Q,
\]

cannot satisfy a pure scalar covariance

\[
V_m^*HV_m=cH
\]

with an ordinary self-adjoint compact-resolvent operator `H`. It deliberately leaves the additive law

\[
\boxed{V_m^*HV_m=H+dI}
\]

open because on one bilateral-shift orbit the number operator gives an exact model of this relation.

For the **actual full Prime-Circle solenoid representation**, that escape is also impossible.

1. If `d\ne0`, there is no self-adjoint `H` on all of `L^2(\Sigma_{\mathbb Q})` satisfying the displayed operator equality at all. The obstruction is already the constant character, which is a fixed vector of `V_m`.
2. Even if the constant mode is removed and one works directly on

   \[
   L^2_0(\Sigma_{\mathbb Q})=\mathbf1^\perp,
   \]

   no self-adjoint **compact-resolvent** `H` can satisfy the same additive covariance for `d\ne0`. Additive covariance plus compact resolvent forces `V_m` to be a bilateral shift of finite multiplicity, whereas the solenoid dilation on the mean-zero rational characters is a bilateral shift of countably infinite multiplicity.
3. The case `d=0` is already the commuting `c=1` case of PC-069 and also has no compact-resolvent solution.

Consequently, combining PC-069 and PC-070, every scalar affine law

\[
\boxed{V_m^*HV_m=cH+dI}
\]

is incompatible with an ordinary compact-resolvent Prime-Circle Hamiltonian on the natural full solenoid representation. The surviving operator routes must break affine covariance, replace the two-sided solenoid automorphism by a one-sided semigroup/isometry, change the spectral framework, or derive additional embedded geometry that does not transform by a scalar affine law.

## 1. Additive covariance is the unitary time-operator relation

Assume

\[
V^*HV=H+dI,
\qquad d\in\mathbb R,
\]

for a unitary `V` and self-adjoint `H`, with equality of self-adjoint operators. Functional calculus gives, for every `t\in\mathbb R`,

\[
\boxed{
V^*e^{itH}V=e^{itd}e^{itH}.
}
\]

Equivalently,

\[
V e^{itH}=e^{-itd}e^{itH}V.
\]

Up to sign and normalization, this is the established strong time-operator/Weyl relation for a unitary evolution. In particular it is not an invented spectral wrapper specific to Prime Circle.

The relation can coexist with a self-adjoint discrete-spectrum operator for suitable unitaries. On `\ell^2(\mathbb Z)`, with bilateral shift `S e_k=e_{k+1}` and number operator `N e_k=k e_k`,

\[
S^*NS=N+I.
\]

This is the boundary example already recorded in PC-069. The obstruction below therefore comes from the **specific multiplicity and fixed-mode structure of the Prime-Circle solenoid dilation**, not from additive covariance in isolation.

## 2. The constant character kills the additive law on the full solenoid

On the full compatible solenoid,

\[
V_m\mathbf1=\mathbf1.
\]

Suppose `d\ne0` and a self-adjoint `H` satisfies

\[
V_m^*HV_m=H+dI.
\]

Using the bounded functional-calculus relation from Section 1,

\[
V_m e^{itH}\mathbf1
=e^{-itd}e^{itH}V_m\mathbf1
=e^{-itd}e^{itH}\mathbf1.
\]

Thus for every real `t`, the nonzero vector `e^{itH}\mathbf1` is an eigenvector of `V_m` with eigenvalue `e^{-itd}`. As `t` ranges over one interval of length `2\pi/|d|`, this produces uncountably many distinct unitary eigenvalues.

Eigenvectors of a normal operator belonging to distinct eigenvalues are orthogonal, while a separable Hilbert space cannot contain an uncountable orthogonal family of nonzero vectors. Hence

\[
\boxed{
 d\ne0
 \quad\Longrightarrow\quad
 \text{no self-adjoint }H\text{ on }L^2(\Sigma_{\mathbb Q})
 \text{ can satisfy }V_m^*HV_m=H+dI.
}
\]

No compactness hypothesis is needed for this full-space obstruction.

This is also the familiar point-spectrum warning in unitary time-operator theory: an exact strong additive conjugacy is incompatible with a unitary carrying a fixed/eigenvector sector. The Prime-Circle completion necessarily carries such a sector because the trivial character survives every power map.

## 3. Removing constants does not restore compact resolvent

A natural response is to remove the trivial character and pose the Hilbert-Pólya candidate directly on

\[
\mathcal H_0=L^2_0(\Sigma_{\mathbb Q}).
\]

Here `V_m` has no eigenvectors, so the Section 2 contradiction disappears. Nevertheless the representation is still too large.

Assume `d\ne0` and let `H` be self-adjoint with compact resolvent on `\mathcal H_0`, satisfying

\[
V_m^*HV_m=H+dI.
\]

Replacing `V_m` by `V_m^*` if necessary, take `d>0`. Compact resolvent implies that `H` has discrete real spectrum with finite-dimensional eigenspaces and only finitely many eigenvalues, counted with multiplicity, in every bounded interval.

Choose `a\in\mathbb R` so that no endpoint `a+kd`, `k\in\mathbb Z`, is an eigenvalue of `H`, and set

\[
W=\operatorname{Ran}\mathbf1_{[a,a+d)}(H).
\]

Then `W` is finite-dimensional. Additive covariance sends the spectral band `[a+kd,a+(k+1)d)` unitarily to the next band, so

\[
\boxed{
\mathcal H_0
=\bigoplus_{k\in\mathbb Z}V_m^kW.
}
\]

The subspaces are mutually orthogonal and `V_m` shifts them transitively. Therefore `V_m|_{\mathcal H_0}` would be a bilateral shift of the **finite multiplicity**

\[
r=\dim W<\infty.
\]

Now compare with the exact Pontryagin basis of the Prime-Circle solenoid. Multiplication by `m` partitions the nonzero rational characters into bilateral orbits

\[
\mathcal O_m(q)=\{m^kq:k\in\mathbb Z\},
\qquad q\ne0.
\]

Hence

\[
\boxed{
\mathcal H_0
=\bigoplus_{[q]\in\mathbb Q^\times/m^{\mathbb Z}}
\overline{\operatorname{span}}
\{\chi_{m^kq}:k\in\mathbb Z\},
}
\]

and on every summand `V_m` is the bilateral shift on `\ell^2(\mathbb Z)`.

There are infinitely many distinct orbit classes. For example, primes `\ell\nmid m` lie in pairwise distinct classes: if

\[
\ell_1=m^k\ell_2,
\]

comparison of valuations at a prime divisor of `m` forces `k=0`, hence `\ell_1=\ell_2`.

Thus

\[
\boxed{
V_m|_{\mathcal H_0}
\text{ is a bilateral shift of countably infinite multiplicity.}
}
\]

Bilateral-shift multiplicity is a unitary invariant (equivalently, after Fourier transform it is the fiber dimension in the `M_z` spectral representation). It cannot simultaneously be the finite multiplicity forced by a compact-resolvent additive time operator. Therefore

\[
\boxed{
 d\ne0
 \quad\Longrightarrow\quad
 \text{no compact-resolvent }H\text{ on }L^2_0(\Sigma_{\mathbb Q})
 \text{ satisfies }V_m^*HV_m=H+dI.
}
\]

So deleting the constant mode removes the easiest contradiction but not the actual solenoidal obstruction.

## 4. A two-dilation control gives the same boundary independently

The full compatible Prime-Circle system contains all intrinsic power maps, not just one. There is a useful independent check which avoids shift-multiplicity language.

Suppose two multiplicatively independent integers `m,n\ge2` satisfy

\[
V_m^*HV_m=H+aI,
\qquad
V_n^*HV_n=H+bI.
\]

Since the dilation unitaries commute, for all `r,s\in\mathbb Z`,

\[
(V_m^rV_n^s)^*H(V_m^rV_n^s)
=H+(ra+sb)I.
\]

If `a/b` is irrational, there are distinct nonzero values `r_ka+s_kb\to0`. Acting on any eigenvector of a compact-resolvent `H` produces distinct eigenvalues accumulating at a finite point, impossible.

If `a,b` are rationally dependent, choose `(r,s)\ne(0,0)` with `ra+sb=0`. Multiplicative independence gives

\[
\rho=m^rn^s\ne1.
\]

The resulting rational dilation `q\mapsto\rho q` commutes with `H`. On the mean-zero solenoid every nonzero rational lies in an infinite bilateral `\rho^\mathbb Z` orbit, so there is no nonzero finite-dimensional invariant subspace. But every compact-resolvent eigenspace is finite-dimensional and invariant, again impossible.

This control shows that the obstruction is not an artifact of choosing a particular fundamental spectral band in Section 3. Full additive covariance under the intrinsic refinement semigroup fails by either eigenvalue accumulation or an infinite-orbit commutant obstruction.

## 5. Prior art and novelty audit

No historical novelty is claimed for the abstract time-operator relation, Weyl functional calculus, bilateral shifts, or spectral multiplicity.

A close primary reference is Daiju Funakawa, Yasumichi Matsuzawa, Itaru Sasaki, Akito Suzuki and Noriaki Teranishi, **Time operators for quantum walks**, *Letters in Mathematical Physics* 110 (2020), 2471–2490, DOI `10.1007/s11005-020-01299-5`, arXiv:1901.10665. They study unitary time operators defined by the commutation relation `TU-UT=U` and construct self-adjoint cases with discrete real spectrum for discrete-time quantum walks. This confirms that the additive relation itself is classical and can be spectrally well behaved for finite-winding/finite-multiplicity unitary dynamics.

PC-010 already places Prime-Circle power/refinement dynamics in the Bost–Connes cyclotomic neighborhood, and PC-069 records the important control that the standard Bost–Connes representation is one-sided/isometric rather than the two-sided Haar-Koopman automorphism used here. The present no-go therefore does **not** reprove or obstruct the Bost–Connes Hamiltonian.

Targeted searches around unitary time operators, weak/strong Weyl relations, discrete-time quantum walks, and solenoidal spectral triples did not locate a source asserting this exact obstruction for multiplication by `m` on the universal arithmetic-solenoid character group `\mathbb Q`. That absence is not a novelty proof.

The durable project-specific content is narrower and exact:

\[
\boxed{
\text{Prime-Circle compatible dilation}
=\text{fixed trivial mode}\oplus
\text{infinitely many bilateral rational orbits},
}
\]

and that representation is incompatible with the finite-ladder structure forced by an ordinary compact-resolvent additive time operator.

## 6. Consequence for the affine-covariance branch

PC-069 already proves:

- pure scaling `V_m^*HV_m=cH` is incompatible with compact resolvent for every real `c`;
- every affine law `V_m^*HV_m=cH+dI` with `c\ne1` reduces by a scalar shift of `H` to pure scaling.

PC-070 supplies the missing `c=1` cases:

- `d=0` is the commuting case already covered by PC-069;
- `d\ne0` is impossible by Sections 2–3 above.

Therefore the entire scalar-affine family is closed:

\[
\boxed{
\forall m\ge2,\ \forall c,d\in\mathbb R:\qquad
V_m^*HV_m=cH+dI
\quad\Longrightarrow\quad
H\text{ is not an ordinary compact-resolvent Prime-Circle Hamiltonian.}
}
\]

For `c=1,d\ne0` on the full space, the statement is stronger: no self-adjoint solution exists at all.

This matters for the RH target because an additive `d_m\sim\log m` law is the natural way to try to retain scale/refinement while converting multiplicative dilation into an additive spectral coordinate. The compatible Prime-Circle solenoid does not permit that repair in ordinary compact-resolvent form.

## 7. Boundary of the obstruction

PC-070 does **not** rule out:

- a one-sided semigroup/isometry representation, where the inverse-dilation direction is removed and Bost–Connes-like logarithmic Hamiltonians can exist;
- a semifinite spectral triple or another framework not requiring ordinary compact resolvent;
- a non-affine conjugacy law `V_m^*HV_m=\Phi_m(H)` whose form is forced independently by Prime-Circle geometry;
- an operator on a geometrically selected finite-multiplicity dilation component, provided the selection itself is intrinsic rather than chosen to obtain discreteness;
- symmetry breaking by old/new, common-anchor, or embedded chord data before the all-level solenoid quotient;
- nonlinear determinant/transfer data that do not transform as a scalar affine function of one self-adjoint operator;
- or the global primitive-root uniformization/accessory branch of PC-017.

The surviving gate is therefore sharper than PC-069:

\[
\boxed{
\text{two-sided compatible dilation symmetry cannot be kept as any scalar affine law of an ordinary compact-resolvent }H.
}
\]

## 8. Exact audit tests

The finding has direct falsifiers.

1. Verify from PC-064/PC-069 that `V_m\chi_q=\chi_{mq}` and `V_m\mathbf1=\mathbf1`.
2. From `V_m^*HV_m=H+dI`, derive `V_m^*e^{itH}V_m=e^{itd}e^{itH}` by self-adjoint functional calculus.
3. Apply item 2 to the constant character and verify that `d\ne0` would create uncountably many distinct eigenvalues of `V_m`.
4. On `\mathbf1^\perp`, decompose `\mathbb Q^\times` into the orbits `m^\mathbb Zq` and verify that each orbit block is one bilateral shift.
5. Exhibit infinitely many orbit classes, for example using primes not dividing `m`.
6. For a hypothetical compact-resolvent additive `H`, choose a spectral interval of width `|d|` with endpoints off the spectrum and verify that its finite-dimensional spectral subspace is a wandering subspace whose `V_m` translates span the Hilbert space.
7. Conclude that item 6 forces finite bilateral-shift multiplicity, contradicting items 4–5.
8. As an independent control, combine two multiplicatively independent dilations and verify the rational-dependence/irrational-dependence dichotomy of Section 4.
9. Check the one-orbit model `S^*NS=N+I` on `\ell^2(\mathbb Z)` to confirm that the no-go depends on the Prime-Circle solenoid representation rather than on additive covariance alone.

Failure of items 1–7 would invalidate the core obstruction. Item 9 prevents overextending it beyond the representation actually forced by the compatible Prime-Circle refinement.