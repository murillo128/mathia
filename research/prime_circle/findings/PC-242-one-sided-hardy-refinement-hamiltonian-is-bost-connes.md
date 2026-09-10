# PC-242 — one-sided Hardy refinement Hamiltonian is the Bost–Connes Gibbs representation

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `CLASSICAL-STRUCTURE` + `DECISIVE-NEGATIVE` for obtaining a new Prime-Circle/RH mechanism from the canonical one-sided Hardy realization of power refinement with its intrinsic positive-frequency generator. The one-sided passage does evade the two-sided compact-resolvent obstruction of PC-070: the positive Hardy sector carries a natural self-adjoint compact-resolvent Hamiltonian with exact additive refinement covariance. But the resulting representation, Hamiltonian, and Gibbs trace are exactly the canonical Bost–Connes representation. The escape works analytically only by landing in established cyclotomic thermodynamic structure; it does not turn Riemann zeros into eigenvalues or derive the critical line.

The result is deliberately narrow. It classifies the **canonical bare Hardy/power-map realization**, not every shell-dependent, chord-dependent, nonseparable, or domain-sensitive one-sided operator that could be built from additional embedded Prime-Circle data.

## 1. The intrinsic one-sided Hardy model

The interior harmonic/holomorphic side of the unit circle gives a canonical one-sided frequency space. Let

\[
\mathcal H_+=zH^2(S^1)
\]

with orthonormal basis

\[
e_k(z)=z^k,\qquad k\ge1.
\]

For each integer `n>=1`, the power refinement of the circle acts by composition

\[
(V_nf)(z)=f(z^n),
\qquad
V_ne_k=e_{nk}.
\tag{1}
\]

Hence `V_n` is an isometry and

\[
V_mV_n=V_{mn}.
\tag{2}
\]

Its range is exactly the closed span of modes whose index is divisible by `n`, so

\[
V_nV_n^*e_k=
\begin{cases}
e_k,&n\mid k,\\
0,&n\nmid k.
\end{cases}
\tag{3}
\]

The roots-of-unity action is equally intrinsic on this Hardy boundary space. For `y in Q/Z`, define the rational rotation

\[
(R_yf)(z)=f(e^{2\pi i y}z).
\]

Then

\[
R_ye_k=e^{2\pi i k y}e_k.
\tag{4}
\]

Equations (1)--(4) already contain the one-sided power-semigroup action and cyclotomic phases before any primitive-shell mask, chord kernel, old/new projection, resultant, or anchored potential is inserted.

This is exactly the kind of one-sided semigroup/isometry escape left open by PC-070 after two-sided solenoid automorphisms were shown incompatible with compact-resolvent affine covariance.

## 2. Positive angular frequency gives a compact-resolvent Hamiltonian

On `\mathcal H_+`, the positive angular number operator

\[
N=-i\partial_\theta,
\qquad
Ne_k=k e_k,
\tag{5}
\]

is positive self-adjoint on

\[
\mathcal D(N)=
\left\{
\sum_{k\ge1}a_ke_k:
\sum_{k\ge1}k^2|a_k|^2<\infty
\right\}.
\]

It satisfies the exact refinement covariance

\[
\boxed{NV_n=nV_nN.}
\tag{6}
\]

The logarithm is therefore available without a zero-mode ambiguity:

\[
H=\log N,
\qquad
He_k=(\log k)e_k,
\tag{7}
\]

with

\[
\mathcal D(H)=
\left\{
\sum_{k\ge1}a_ke_k:
\sum_{k\ge1}(\log k)^2|a_k|^2<\infty
\right\}.
\tag{8}
\]

Every `V_n` preserves this domain because `log(nk)=log n+log k`. Applying functional calculus to (6), or simply checking on the basis, gives

\[
\boxed{
HV_n=V_nH+(\log n)V_n.
}
\tag{9}
\]

Equivalently,

\[
\boxed{
e^{itH}V_ne^{-itH}=n^{it}V_n.}
\tag{10}
\]

The spectrum is

\[
\operatorname{Spec}(H)=\{\log k:k\ge1\},
\tag{11}
\]

with multiplicity one and no finite accumulation point. Consequently `(H+i)^{-1}` is compact. Thus the one-sided Hardy model genuinely evades the bilateral-shift multiplicity obstruction from PC-070: there is an ordinary self-adjoint compact-resolvent operator with exact additive refinement covariance.

The important question is therefore not existence but provenance: does this Hamiltonian arise as new embedded Prime-Circle structure, or is it already the standard arithmetic semigroup representation?

## 3. Exact unitary identification with the canonical Bost–Connes representation

Let `\ell^2(\mathbb N^*)` have its standard basis `\varepsilon_k`, and define

\[
W:\mathcal H_+\to\ell^2(\mathbb N^*),
\qquad
We_k=\varepsilon_k.
\tag{12}
\]

Under this unitary,

\[
WV_nW^*\varepsilon_k=\varepsilon_{nk},
\tag{13}
\]

\[
WR_yW^*\varepsilon_k=e^{2\pi i k y}\varepsilon_k,
\tag{14}
\]

and

\[
WHW^*\varepsilon_k=(\log k)\varepsilon_k.
\tag{15}
\]

These are not merely analogous to the Bost–Connes system. They are the canonical representation used by Bost and Connes: their isometries `\mu_n` act by `\varepsilon_k\mapsto\varepsilon_{nk}`, their cyclotomic generators `e(y)` act by the phase `\exp(2\pi i k y)`, and the implementing Hamiltonian is

\[
H_{BC}\varepsilon_k=(\log k)\varepsilon_k.
\tag{16}
\]

Therefore

\[
\boxed{
(\mathcal H_+,\{R_y\},\{V_n\},H)
\simeq
(\ell^2(\mathbb N^*),\{\pi_1(e(y))\},\{\pi_1(\mu_n)\},H_{BC}).
}
\tag{17}
\]

This strengthens the prior-art boundary in PC-010 and PC-241 in a specific direction. PC-010 identifies the abstract roots-of-unity/refinement tower with Bost–Connes data, while PC-241 identifies the bounded addition-dilation operator algebra with Cuntz's classical `ax+b` system. The present one-sided Hardy construction supplies the natural unbounded additive-covariance Hamiltonian left open by those bounded/algebraic classifications, but that Hamiltonian is again exactly the established Bost–Connes one.

## 4. The Gibbs trace is zeta because the energy is log conductor

For real `beta>1`,

\[
e^{-\beta H}e_k=k^{-\beta}e_k,
\]

so the Gibbs trace is

\[
\boxed{
\operatorname{Tr}(e^{-\beta H})
=
\sum_{k\ge1}k^{-\beta}
=
\zeta(\beta).
}
\tag{18}
\]

This is precisely the Bost–Connes partition function. The additive shift in (9) is the same arithmetic energy law:

\[
\log n=\sum_p v_p(n)\log p.
\tag{19}
\]

Thus the prime logarithms appear through unique factorization of the semigroup index, not through a new chord, shell, harmonic-potential, or common-anchor observable.

Equation (18) is a genuine operator trace only in its trace-class half-plane `beta>1`. Meromorphic continuation of the scalar function `zeta(beta)` beyond that region does not turn its nontrivial zeros into eigenvalues of `H`. The self-adjoint spectrum in (11) remains the elementary set `{log k}`. In particular, the construction derives neither a critical-line localization, a gamma factor, nor the `s <-> 1-s` functional equation.

This distinguishes a thermodynamic occurrence of zeta from a Hilbert–Pólya mechanism. The operator is mathematically natural and compact-resolvent, but its spectral levels are positive logarithms of integers rather than ordinates of Riemann zeros.

## 5. Matched control removes all Prime-Circle shell geometry

A decisive control is obtained by erasing every feature that distinguishes the Prime-Circle birth geometry:

- no primitive/new-vertex projector;
- no cyclotomic polynomial `Phi_n` or logarithmic potential `U_n`;
- no anchored von Mangoldt evaluation;
- no chord length or old/new incidence;
- no cross-shell resultant or mask.

Retain only the ordinary Hardy space of the disk, rational rotations of its boundary, and the power maps `z -> z^n`. Equations (1)--(18) are unchanged. The same compact-resolvent Hamiltonian, additive covariance, and zeta Gibbs trace survive exactly.

Hence the appearance of `zeta(beta)` cannot be attributed to the embedded Prime-Circle structure that the line is trying to exploit. It is already present in the bare one-sided semigroup representation. Any arithmetic information obtained solely from `(R_y,V_n,H)` factors through this control and therefore fails the line-specific requirement that a new mechanism use information beyond the abstract cyclotomic/refinement tower.

## 6. Relation to neighboring Prime-Circle obstructions

This result closes a precise gap rather than repeating the earlier no-go results.

PC-070 studies the **two-sided compatible solenoid**, where the power map is a unitary automorphism with infinitely many bilateral orbits; additive covariance then conflicts with compact resolvent. Passing to `\mathcal H_+` removes the negative-frequency half and changes the refinement maps from unitaries to proper isometries, so that obstruction no longer applies. PC-242 shows what the canonical successful repair becomes: Bost–Connes.

PC-171 classifies a fixed self-adjoint first-order boundary operator satisfying the stronger relation `A C_n=n C_n A` under all circle power maps. Its surviving positive-frequency `|D|`/`D` channel is consistent with (5). Taking the logarithm changes the multiplicative first-order covariance into the additive law (9), but does not reveal new arithmetic because the resulting logarithmic generator is determined entirely by the bare Fourier index.

PC-241 shows that retaining the original coordinate shift together with refinement yields the classical Cuntz `ax+b` algebra. PC-242 adds the thermodynamic generator to the canonical one-sided representation and finds no escape from that classicalization: the unbounded generator and its partition function are already part of the original Bost–Connes construction.

Thus the chain

\[
\boxed{
\text{one-sided Hardy frequencies}
\to
\text{power-refinement isometries}
\to
\log(-i\partial_\theta)
\to
\text{compact-resolvent additive Hamiltonian}
\to
\zeta\text{ partition function}
}
\]

is mathematically valid but not a new Prime-Circle/RH bridge.

## 7. Prior-art and novelty audit

The decisive source is J.-B. Bost and A. Connes, *Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory*, Selecta Mathematica (N.S.) 1:3 (1995), 411–457, DOI `10.1007/BF01589495`. In the canonical `\ell^2(\mathbb N^*)` representation they write exactly the multiplication isometries and cyclotomic phases in (13)--(14), identify the Hamiltonian by `H\varepsilon_n=(\log n)\varepsilon_n`, and obtain `Tr(e^{-\beta H})=\zeta(\beta)` for `beta>1`.

The operator-algebraic neighborhood is already reinforced inside this line by PC-010 and by Cuntz's `ax+b` semigroup algebra recorded for PC-241. Targeted comparison against Bost–Connes thermodynamic dynamics, Cuntz semigroup algebras, and the already stored Prime-Circle dilation/operator results finds no additional shell-derived datum in (17). The unitary equivalence is exact, so this is stronger than a generic literature resemblance and does not rely on absence of a matching phrase in searches.

No novelty is claimed for the Hardy-space number operator, composition isometries, logarithmic generator, Bost–Connes representation, or zeta partition function. The durable contribution is the **Prime-Circle-specific boundary statement**: the most canonical one-sided compact-resolvent repair of the additive refinement problem is not an uncovered spectral mechanism; it is an exact analytic realization of established Bost–Connes dynamics.

## 8. Boundary of the obstruction and falsification tests

The assumptions carrying the negative conclusion are explicit. The Hilbert space is the bare positive Hardy sector; refinements act by unweighted composition `f(z)->f(z^n)`; the Hamiltonian is the intrinsic positive-frequency logarithmic generator; and no shell-dependent or embedded geometric coefficient is added before diagonalization. Under those hypotheses, the unitary equivalence (17) is complete.

The result does **not** rule out a one-sided operator whose entries are forced by primitive-shell masks, chord geometry, old/new incidence, off-circle harmonic fields, or another embedded Prime-Circle observable and which is not reducible to a scalar function of the Fourier number operator. It also does not classify level-dependent/nonseparable source operators, nonlinear cross-level constructions, or the global uniformization/accessory-parameter branch. Those require independent derivation and novelty audits.

The exact claim has direct audit tests:

1. verify `V_ne_k=e_{nk}` and that `V_nV_n^*` is the divisibility projector;
2. verify `NV_n=nV_nN` on the finite Fourier core;
3. verify that `V_n` preserves `D(log N)` and gives (9)--(10);
4. verify compactness of `(log N+i)^{-1}` from `log k -> infinity`;
5. apply `W e_k=epsilon_k` and compare (13)--(16) with the canonical Bost–Connes representation;
6. verify the Gibbs trace (18) for `beta>1`.

Failure of any of these identities would invalidate the exact classicalization. A future one-sided Prime-Circle Hamiltonian evades PC-242 only if its additional operator data are **derived from the original embedded geometry and survive the matched control**, rather than being chosen because their trace or determinant has a desired zeta factor.
