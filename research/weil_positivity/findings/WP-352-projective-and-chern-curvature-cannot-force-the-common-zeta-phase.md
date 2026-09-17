---
id: WP-352
title: Projective and Chern curvature cannot force the common zeta phase
branch: weil_positivity
status: supported
kind: cross-parameter-scalar-curvature-no-go
claim_strength: exact geometric and complex-analytic derivation with a zero-free reciprocal matched control and targeted prior-art audit
created: 2026-09-17
related: [WP-165, WP-166, WP-241, WP-348, WP-350, WP-351]
clues: [CLUE-maass-selberg-remainder-sign-interface]
prior_art:
  - Barry Simon, Holonomy, the Quantum Adiabatic Theorem, and Berry's Phase, Phys. Rev. Lett. 51 (1983), 2167-2170, DOI 10.1103/PhysRevLett.51.2167
  - classical Berry/Grassmann projector connection and curvature
  - classical Maurer--Cartan flatness for a globally defined unitary frame
  - classical Poincare--Lelong formula for meromorphic functions/sections
  - Jean-Pierre Demailly, Complex Analytic and Differential Geometry, Chapter III section 13, Lelong--Poincare equation and first Chern class
---

# WP-352 — Projective and Chern curvature cannot force the common zeta phase

## Claim

`WP-351` leaves one natural phase-sensitive escape open: replace pointwise contraction-defect positivity by a genuinely **cross-parameter connection**, and hope that Berry/Chern curvature or holonomy detects the scalar global scattering phase that pointwise positive geometry loses.

For the squarefree scattering factorization

\[
U(s)=g(s)R(s),
\qquad
 g(s)=\frac{\zeta^\star(2s-1)}{\zeta^\star(2s)},
\tag{1}
\]

this direct escape also fails in two complementary ways.

First, every projective/eigenbundle geometry is blind to `g`: multiplying an operator by a nonzero scalar changes its eigenvalues but not its eigenspaces or spectral projectors. Hence Berry/Grassmann connections, their curvature, quantum metrics, Chern forms, and projector holonomies are unchanged by

\[
U\longmapsto cU
\tag{2}
\]

whenever the selected bundle is defined projectively rather than by an externally fixed absolute eigenphase window.

Second, if one instead regards the scalar factor `g` itself as a line-bundle section, its ordinary smooth connection is locally pure gauge. On the complex parameter surface the only canonical singular curvature supplied by the scalar meromorphic function is, by Poincare--Lelong, its **divisor current**. Away from zeros and poles that curvature vanishes; at the singularities it is exactly the zero-minus-pole data one was trying not to insert.

There is a decisive analytic matched control. For every real `a`, put

\[
c_a(s):=e^{a(s-1/2)},
\qquad
\widetilde g_a(s):=c_a(s)g(s).
\tag{3}
\]

Then `c_a` is entire and nowhere zero,

\[
c_a(1-s)=c_a(s)^{-1},
\qquad
|c_a(1/2+it)|=1,
\tag{4}
\]

so it preserves the reciprocal scattering symmetry, critical-line unitarity, every zero and pole, and every divisor/Chern current of `g`. It also leaves all projective eigenspace geometry of `U` unchanged. Nevertheless, for

\[
q_g(t):=-i\frac{d}{dt}g(1/2+it)\,g(1/2+it)^{-1},
\tag{5}
\]

one has

\[
\boxed{q_{\widetilde g_a}(t)=q_g(t)+a.}
\tag{6}
\]

Thus neither gauge-invariant projective curvature nor scalar divisor curvature determines even the additive normalization of the critical-line logarithmic derivative. Any successful cross-parameter construction must contain an additional, independently forced **phase anchor or noncentral coupling**. If that anchor is obtained from the meromorphic divisor, it has reverted to zero data; if it is obtained from a chosen trivialization/metric/absolute eigenphase, that extra structure itself carries the arithmetic burden.

This closes the direct Berry/Chern-curvature interpretation of the cross-parameter loophole in `WP-351`. It does not rule out a genuinely noncentral adelic/cohomological bundle whose connection is forced before scalarization and whose positivity theorem simultaneously couples finite and archimedean terms.

**Classification:** `EXACT-DERIVED + CROSS-PARAMETER-CONNECTION-TESTED + PROJECTIVE-SCALAR-BLINDNESS + MAURER-CARTAN-PURE-GAUGE + POINCARE-LELONG-DIVISOR-REDIRECT + ZERO-FREE-RECIPROCAL-MATCHED-CONTROL + DECISIVE-NARROWING + PRIOR-ART-CLASSICALIZATION + NOT-A-WEIL-BRIDGE`.

## 1. Scalar multiplication leaves projector geometry unchanged

Let `M` be a smooth real parameter manifold and let

\[
U(x)=g(x)R(x),
\qquad g(x)\in\mathbb C^*,
\tag{7}
\]

be a smooth family of matrices or bounded operators for which a finite-rank spectral/eigenbundle `E -> M` is well defined. At every `x`, `U(x)` and `R(x)` have exactly the same invariant eigenspaces: scalar multiplication moves the eigenvalues but not the eigenvectors.

Therefore any spectral projector `P(x)` selected by continuation of an eigenspace or cluster satisfies

\[
\boxed{P_U(x)=P_R(x).}
\tag{8}
\]

The standard Grassmann/Berry curvature can be written directly in projector form, for example

\[
\Omega_P=P\,(dP\wedge dP)\,P,
\tag{9}
\]

with scalar Chern/Berry forms obtained by traces of this expression. Since (8) is exact, all such forms are identical for `U` and `R`. The same is true for the usual projector quantum metric and for parallel transport intrinsic to the subbundle `Ran P`.

Consequently a scalar rephasing

\[
U\mapsto e^{i\phi(x)}U
\tag{10}
\]

can change the scattering phase generator while leaving the entire projective bundle geometry fixed.

There is one important qualification. A rule such as "take the eigenvalues lying in this fixed arc of the unit circle" is not projective: a common scalar rephasing moves the spectrum relative to that externally fixed arc and can change the selected subspace. Such a construction is phase-sensitive precisely because the fixed arc supplies an **absolute phase anchor**. The positivity of the resulting bundle cannot by itself explain why that anchor is the arithmetic one; canonicality of the selection rule becomes the new theorem to prove.

This is distinct from `WP-350`. There the moving frame could contribute Berry terms before a unitary compression, but those terms cancelled from the trace and same-sign ramification survived. Here the statement is stronger for genuinely projective cross-parameter geometry: the common scalar factor never enters the projector in the first place.

## 2. The full Maurer--Cartan connection contains the scalar phase only as an exact central one-form

Suppose now that `U:M -> U(m)` is a smooth critical-line/unitary family. Its right or left Maurer--Cartan form contains all first-order phase information. With

\[
\mathcal A_U:=-iU^{-1}dU,
\tag{11}
\]

and `U=gR`, one obtains

\[
\boxed{
\mathcal A_U
=-ig^{-1}dg\,I+\mathcal A_R.
}
\tag{12}
\]

Under the rephasing `g -> e^{i\phi}g`,

\[
\mathcal A_U\longmapsto \mathcal A_U+d\phi\,I.
\tag{13}
\]

Thus the scalar phase is present at the **connection-potential** level. But it enters as an exact central one-form. The Maurer--Cartan identity gives

\[
\boxed{
\mathcal F_U:=d\mathcal A_U+i\mathcal A_U\wedge\mathcal A_U=0
}
\tag{14}
\]

for a globally defined unitary frame. More generally, any curvature built after quotienting to the projective/eigenbundle geometry loses the central exact term in (13).

Closed-loop gauge invariants do not restore the missing local density. If `\phi` is a globally defined real function, then

\[
\oint_\gamma d\phi=0
\tag{15}
\]

for every closed loop `\gamma`, while its directional derivative can be changed arbitrarily inside a coordinate patch. Hence a local critical-line phase velocity such as (5) cannot be forced by curvature or closed holonomy that is invariant under (13).

This is the higher-dimensional analogue of the pure-gauge obstruction in `WP-165`--`WP-166`, but now applied to the **common scalar scattering phase** and to the specific cross-parameter escape left open after `WP-351`. Adding parameter directions creates room for nonzero projective curvature, but that curvature still cannot see a central scalar rephasing.

## 3. Complexifying the parameter does not help unless the divisor is used

A natural objection is that the scattering scalar is meromorphic in the complex spectral parameter `s`, so one should use complex/Chern rather than purely real Berry geometry.

Let `D` be a complex domain and let `g` be meromorphic. On any simply connected open set avoiding the divisor, `g` is holomorphic and nonvanishing, so locally `g=e^h` for a holomorphic function `h`. Therefore

\[
\log|g|=\operatorname{Re}h
\tag{16}
\]

is harmonic and

\[
\boxed{dd^c\log|g|=0}
\tag{17}
\]

there. Thus the scalar line is flat on the divisor complement.

Distributionally, the Poincare--Lelong formula says, up to the conventional normalization of `d^c`,

\[
\boxed{dd^c\log|g|=[\operatorname{div}(g)].}
\tag{18}
\]

For a meromorphic function the right-hand side is the signed zero-minus-pole current. Applied to (1), it is literally the divisor of the completed-zeta scattering normalizer. Hence the only singular curvature canonically generated by the scalar meromorphic function is not an independent geometric explanation of its zero data: it **is that divisor data in current form**.

Taking only the positive part of the current does not solve the circularity. It explicitly selects the zero divisor from the signed meromorphic divisor. Conversely, adding a nonflat Hermitian metric can add smooth Chern curvature, but then the metric is extra structure. Unless Mathia forces that metric independently and its sign theorem couples the finite and archimedean terms before the divisor is read, the positivity has merely been put into the metric choice.

## 4. A zero-free reciprocal matched control preserves all curvature/divisor data but moves the phase generator

The family (3) makes the selectivity failure exact inside the analytic scattering category rather than only at the level of an arbitrary critical-line phase perturbation.

Because `c_a` is entire and nowhere zero,

\[
\operatorname{div}(\widetilde g_a)=\operatorname{div}(g).
\tag{19}
\]

Equation (4) also gives the same reciprocal functional-equation symmetry as a scattering scalar and unit modulus on the critical line. Therefore all of the following are unchanged when `g` is replaced by `\widetilde g_a`:

\[
\begin{array}{c}
\text{zeros and poles with multiplicity},\\
\text{Poincare--Lelong divisor current},\\
\text{critical-line unitarity},\\
\text{reciprocal symmetry }s\leftrightarrow1-s,\\
\text{eigenspaces and all projector/Berry geometry of }gR.
\end{array}
\tag{20}
\]

On the critical line,

\[
c_a(1/2+it)=e^{iat},
\tag{21}
\]

so direct differentiation gives (6).

This control is deliberately stronger than a generic gauge perturbation. It does **not** change the divisor, does **not** break critical-line unitarity, and does **not** break the reciprocal scattering symmetry. The only standard scattering datum it can violate is an additional normalization/asymptotic condition. Therefore any derivation of the physical `q_g` from geometry must use such a normalization or another phase anchor somewhere. Curvature/divisor data alone do not contain it.

The parameter `a` need not imitate an actual automorphic scattering matrix. It is a matched control for the proposed implication "curvature/divisor geometry + reciprocal unitary scattering structure forces the physical scalar phase." Since all hypotheses visible to that geometry survive while the target changes, that implication is false without an additional normalization hypothesis.

## 5. Prior-art and novelty audit

The underlying geometric facts are classical. Simon's 1983 holonomy formulation identifies Berry phase with the natural connection on the eigenline bundle, and the projector formulation of Berry/Grassmann curvature makes its dependence on eigenspaces rather than a common scalar eigenvalue phase explicit. Maurer--Cartan flatness for a global unitary frame is standard differential geometry. Poincare--Lelong is the classical statement that the curvature/current of the logarithm of a meromorphic section records its divisor.

None of those ingredients is claimed as new mathematics.

The Mathia-specific contribution is their combined use against the exact scattering factorization isolated in `WP-348`--`WP-351`, together with the control (3). It sharpens the remaining `cross-parameter connection` loophole into a precise trilemma:

1. projective/Berry geometry is exactly blind to the scalar `g`;
2. ordinary scalar connection curvature is flat/pure gauge and cannot determine `q_g`;
3. singular complex curvature sees `g` only through its divisor, while a zero-free reciprocal factor changes `q_g` without changing that divisor.

Thus a cross-parameter route survives only if it introduces a **noncentral coupling or canonical phase normalization not reducible to the scalar line itself**. That surviving requirement is stronger than the pointwise defect failure in `WP-351` and is not merely a restatement of `WP-165`, which concerned the one-dimensional cyclotomic radial flux rather than the common automorphic scattering normalizer.

A targeted literature audit found no additional positivity theorem in Berry/Chern geometry that changes this conclusion: the standard gauge-invariant objects are projective/curvature data, while divisor curvature is classical Poincare--Lelong data.

## 6. Boundary of the no-go and consequence for the research line

This finding does **not** exclude every connection or cohomological construction. It excludes the direct idea that the common zeta scalar acquires an independent sign theorem merely by being promoted from a phase to a Berry/Chern connection.

A surviving candidate must violate at least one hypothesis used above in a mathematically productive way. In particular, it could use a noncentral operator-valued connection in which the scalar normalizer is coupled to finite-place directions before projection; a genuinely nontrivial global bundle whose transition data are not generated by the scalar function `g`; or an independently forced metric/phase normalization whose curvature theorem already contains the finite--archimedean local-to-global structure required by the README.

But those are new structures, not consequences of the scalar scattering phase. They must survive the same matched control and must prove their sign without RH or inserted zero data.

## Representation audit

The primary objects are the operator family `U=gR`, its spectral projectors, the Maurer--Cartan connection, and the meromorphic scalar line defined by `g`. No basis or scalar statistic is used to create the obstruction. The matched control is analytic, zero-free, reciprocal, and unitary on the critical line.

The finding does not use RH, a zero-defined self-adjoint spectrum, a hand-picked Weil kernel, or a sign-forcing regularization. Poincare--Lelong appears only as a **negative prior-art redirect**: once singular curvature is used to recover the scalar divisor, the proposed geometry has become a representation of already-known zero/pole data rather than an independent positivity mechanism.

## Verdict

**Supported exact negative.** Cross-parameter geometry does not rescue the common scalar scattering phase in its direct Berry/Chern forms. Projector geometry cannot see a common scalar factor; the full scalar connection contributes only an exact central one-form; and complex singular curvature is exactly the meromorphic divisor. The zero-free reciprocal family `e^{a(s-1/2)}g(s)` preserves all of those geometric/divisor data while shifting the critical-line phase generator by the arbitrary constant `a`.

The surviving frontier is therefore narrower: any genuine Weil-positivity bridge must introduce an independently forced noncentral/global coupling or phase normalization **before** the scalar zeta factor is reduced to projective curvature, defect positivity, or divisor data.