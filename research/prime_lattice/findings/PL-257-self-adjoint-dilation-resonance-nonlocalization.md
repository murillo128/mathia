# PL-257 — Self-adjoint dilation of a full-divisor scattering generator does not localize its resonances

## Claim

`PL-033` gives an unconditional automorphic Lax--Phillips operator whose eigenvalues, with algebraic multiplicity, are exactly the nontrivial zeros of the Riemann zeta function. After `PL-254`--`PL-256`, a natural apparent escape is to keep that divisor-complete non-self-adjoint generator but place it inside a larger self-adjoint system, hoping that self-adjoint spectral reality will then force the zero divisor onto the critical axis.

For the Lax--Phillips realization this move is already present from the start and does **not** localize the resonances. The ambient scattering evolution is a unitary group `U(t)` on a Hilbert space. By Stone's theorem it has a self-adjoint generator `L`. The zero-bearing interaction semigroup is instead a compression

\[
Z(t)=P_K U(t)|_K,\qquad t\ge 0,
\]

onto the Lax--Phillips interaction space `K`, and Uetake's `A_c` is its infinitesimal generator. The zeta zeros are eigenvalues of `-2A_c`, not eigenvalues of the ambient self-adjoint `L`.

Consequently the package

\[
\text{one self-adjoint/unitary ambient dynamics}
+\text{one canonical compression}
+\text{full zeta divisor as compression spectrum}
\]

already exists unconditionally. Hypothetical off-critical zeros are perfectly compatible with it: they appear as complex eigenvalues/resonances of the compressed generator while the dilation generator remains self-adjoint with real spectrum. Thus **self-adjoint dilation is not the missing Hilbert--Pólya step**. What is missing is a theorem that makes the zero-bearing operator itself self-adjoint/normal in the relevant centered variable, or otherwise transfers ambient positivity to the resonance divisor.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + DECISIVE-NEGATIVE` for the route "take a divisor-complete dissipative/scattering realization and recover RH from the self-adjointness of its unitary dilation." The Lax--Phillips unitary scattering framework and Uetake's exact zero/eigenvalue theorem are literature already anchored in `SOURCES.md` items 43--44. The compression-versus-dilation distinction is an exact operator-theoretic consequence of that framework. No new scattering theorem, dilation theorem, or result about zeta zeros is claimed.

## 1. The self-adjoint ambient operator is already built into Lax--Phillips scattering

The starting datum of Lax--Phillips scattering is not a non-self-adjoint evolution. It is a strongly continuous **unitary group**

\[
\{U(t):t\in\mathbb R\}
\]

on a Hilbert space together with incoming and outgoing subspaces `D_-` and `D_+`. In the standard orthogonal setup one defines

\[
K=\mathcal H\ominus(D_-\oplus D_+)
\]

and obtains the interaction semigroup by compression of the future evolution to `K`.

By Stone's theorem there is a self-adjoint operator `L=L*` such that, up to the sign convention for the Fourier/time variable,

\[
U(t)=e^{-itL}.
\]

Thus the automorphic scattering construction used in `PL-033` is already embedded in bona fide self-adjoint Hilbert-space dynamics before the zeta-sensitive interaction generator is extracted.

Uetake then studies the infinitesimal generator `A_c` of the Lax--Phillips semigroup for the modular automorphic scattering system. His theorem identifies the poles of its resolvent with the poles of the relevant scattering factor and proves, after the explicit affine normalization recorded in `PL-033`,

\[
\rho\text{ nontrivial zeta zero of multiplicity }m
\quad\Longleftrightarrow\quad
\rho\in\sigma_p(-2A_c)
\]

with algebraic multiplicity `m`.

The important structural point is therefore not merely that the zero operator is non-self-adjoint. It is that **the zero operator is already the compression/resonance part of an ambient unitary system**. Enlarging the Hilbert space to recover self-adjoint dynamics does not add a new constraint; it reconstructs the standard scattering architecture from which `A_c` came.

## 2. Compression eigenvalues are not dilation eigenvalues

The distinction can be seen directly without any zeta-specific input. Suppose `f in K` is an eigenvector of the interaction generator,

\[
A_c f=\lambda f.
\]

Then, in the semigroup normalization,

\[
Z(t)f=e^{t\lambda}f.
\]

Since `Z(t)=P_KU(t)|_K`, this means only

\[
P_KU(t)f=e^{t\lambda}f.
\]

It does **not** imply

\[
U(t)f=e^{t\lambda}f.
\]

Indeed one may write

\[
U(t)f=e^{t\lambda}f+h_t,
\qquad h_t\in K^\perp,
\]

with the escaping component `h_t` carrying precisely the information discarded by the compression. Therefore `f` need not be an eigenvector of the self-adjoint generator `L`, and `\lambda` need not belong to `\sigma(L)`.

This is exactly how complex resonances coexist with a self-adjoint scattering Hamiltonian. Self-adjointness controls the spectrum of the ambient generator; poles of a compressed/continued resolvent or eigenvalues of the Lax--Phillips interaction generator are a different spectral object. There is no contradiction between

\[
\sigma(L)\subset\mathbb R
\]

and complex resonance parameters for `A_c`.

For the zeta specialization, a hypothetical zero `\rho=\beta+i\gamma` with `\beta\ne 1/2` would therefore give an off-axis eigenvalue of the centered/scaled interaction generator exactly as Uetake's theorem says, while the ambient `L` remains self-adjoint. The unitary dilation does not reject the hypothetical zero; it simply represents it as a resonance of a conservative system.

## 3. Making the interaction space reducing would be a new and much stronger condition

The only elementary way for ambient self-adjointness to descend automatically to the interaction dynamics is for `K` to be reducing for `U(t)`. If

\[
U(t)K\subset K\qquad\text{for all }t\in\mathbb R,
\]

then the compression is actually a restriction of a unitary group, and its generator is skew-adjoint in the time convention. After the affine centering used in `PL-033`, its spectrum would lie on the corresponding symmetry axis.

But this property is not furnished by Lax--Phillips scattering; nontrivial leakage between `K` and the incoming/outgoing channels is the point of the scattering construction. Demanding reducingness would therefore insert a new structural theorem rather than extracting a consequence of the existing self-adjoint dilation.

It would also be stronger than the bare zero-location statement in another direction. A unitary or normal restriction cannot support nontrivial Jordan blocks. Uetake's theorem matches **algebraic** multiplicities through generalized eigenspaces, while RH itself does not assert simplicity of the zeta zeros. Hence any proposal that tries to make the complete Uetake interaction generator literally unitary/normal must separately address possible multiple zeros and semisimplicity. The present negative should not be replaced by the stronger but unjustified claim that RH is equivalent to reducingness of `K`.

## 4. General dilation theory makes the obstruction non-arithmetic

The same issue is not special to the modular surface. Generators of strongly continuous contraction semigroups are maximal dissipative after the standard choice of sign, and maximal dissipative operators admit self-adjoint dilations. In functional-model language, their characteristic functions/scattering matrices encode the non-self-adjoint spectral data while the larger dilation evolves unitarily.

This genericity is an important matched control. If the implication

\[
\text{non-self-adjoint divisor model has a self-adjoint dilation}
\Longrightarrow
\text{its poles/eigenvalues lie on the real or unitary axis}
\]

were valid, it would incorrectly localize the resonances of ordinary dissipative scattering systems as well. The dilation theorem preserves the open-system dynamics by compression; it does not turn compression resonances into eigenvalues of the conservative generator.

Accordingly, attaching a self-adjoint dilation to an arbitrary characteristic-function or boundary model is subject to the same programmability warning as `PL-256`. The arithmetic burden is not existence of a conservative dilation. It is an additional identity that constrains the characteristic function or transfers a positive form from the ambient system to **all poles of the continued compressed resolvent**.

## 5. Relation to the current prime-lattice frontier

This finding completes a useful four-way separation around the current spectral frontier.

`PL-033` supplies **divisor completeness without self-adjointness**: every nontrivial zeta zero is an eigenvalue of one Lax--Phillips interaction generator. `PL-254` supplies **self-adjointness with a selector**: designed pseudo-Laplacians force the critical axis for admitted L-zeros but do not admit the full divisor. `PL-255` shows that taking a literal self-adjoint square root of that selected operator cannot recover the missing zeros. `PL-256` shows that abstract boundary/Weyl machinery can manufacture alternative self-adjoint domains, but the zeta-specific Herglotz positivity needed to force the axis is already RH-level.

The present result rules out a remaining hybrid shortcut: keep the divisor-complete non-self-adjoint generator of `PL-033` and declare victory because it has an ambient self-adjoint dilation. That hybrid already exists in the original Lax--Phillips setup and permits complex resonances.

For `prime_lattice`, this reinforces the canonical mandate's distinction between an operator that merely **stores** the analytically continued divisor and a mechanism that **constrains** it. The prime-power axes and `log p` weights enter the modular scattering factor through the genuine global automorphic completion, but the self-adjoint ambient wave dynamics does not propagate a critical-line constraint back to the zero-bearing compression.

A surviving route must therefore do at least one of the following in a source-determined way: make the full zero-bearing operator itself self-adjoint/normal after the correct centering; prove that every zeta resonance of a self-adjoint scattering system is forced onto the symmetry axis by an arithmetic positivity law; or produce a two-way determinant/trace relation in which no off-axis zero can hide as a non-real resonance while the ambient operator remains self-adjoint. Merely exhibiting a unitary dilation, conservative colligation, or self-adjoint ambient Hamiltonian is no longer evidence of localization.

## 6. Prior art and novelty audit

The arithmetic spectral input is the same primary source already recorded in `SOURCES.md` item 43:

- **Yoichi Uetake**, “The Lax--Phillips infinitesimal generator and the scattering matrix for automorphic functions,” *Annales Polonici Mathematici* **92**(2) (2007), 99--122, DOI `10.4064/ap92-2-1`. Uetake proves that the interaction-generator spectrum coincides with the scattering poles and, after normalization, with the nontrivial zeta-zero divisor including algebraic multiplicity.

The ambient unitary architecture is classical Lax--Phillips theory, already recorded in `SOURCES.md` item 44:

- **Peter D. Lax, Ralph S. Phillips**, *Scattering Theory for Automorphic Functions*, Annals of Mathematics Studies **87**, Princeton University Press, 1976. The scattering system is built from a unitary evolution with incoming/outgoing subspaces, while the interaction semigroup is obtained by compression.

A current literature audit around maximal dissipative functional models and self-adjoint dilations confirms that this compression/dilation structure remains standard operator theory: characteristic functions of dissipative operators are realized as scattering matrices of self-adjoint dilations, rather than their complex poles being converted into real eigenvalues of the dilation. This search is used only to bound novelty; the mathematical conclusion above already follows from the classical Lax--Phillips/Uetake setup.

Internal duplication was checked against the live local frontier, especially `PL-033`, `PL-042`, `PL-119`, `PL-254`, `PL-255`, and `PL-256`. `PL-033` establishes the full zero/eigenvalue correspondence but does not isolate the failure of **ambient** self-adjointness as a localization mechanism. `PL-042` concerns universal Clark unitary boundary perturbations of model spaces, `PL-119` separates adelic zero spectrality from Weil positivity, and `PL-254`--`PL-256` concern self-adjoint selectors, operator squares, and programmable boundary/Weyl data. The present finding records the complementary dilation obstruction and does not claim a new theorem of dilation theory.

## 7. Adversarial boundaries

1. **Not a no-go theorem for Hilbert--Pólya.** It rules out only the inference from a self-adjoint ambient dilation to localization of a non-self-adjoint compression/resonance spectrum. A self-adjoint operator whose own eigenvalues are the full zero divisor would be qualitatively stronger.
2. **The zeros are not claimed to be ambient eigenvalues.** That distinction is the point. Uetake places them in the spectrum of the interaction generator; Stone's theorem places the ambient unitary generator's spectrum on the real axis.
3. **Reducingness is sufficient, not known or RH-equivalent.** If the interaction space reduced the ambient unitary group, the compressed dynamics would be unitary, but RH alone does not imply this stronger operator statement and does not imply simplicity of the zeros.
4. **A different self-adjoint coupling can still matter.** A construction in which the arithmetic boundary/source changes the operator so that the full zeta divisor becomes its actual self-adjoint point spectrum is not covered by this negative. Such a route must prove divisor completeness rather than rely on dilation.
5. **No formal Euler continuation is used.** The zeta divisor in the scattering coefficient is supplied by meromorphic Eisenstein/automorphic continuation as audited in `PL-033`; the present argument begins after that continued operator model is established.
6. **Not intrinsic prime-lattice geometry.** The decisive continuation and scattering structure remain global/automorphic. The result is a falsification control for operator mechanisms allowed by the line mandate, not evidence that the bare exponent monoid itself has a self-adjoint dilation carrying the zeros.

## Research implication

The current spectral target should distinguish three notions that are easy to conflate: self-adjointness of an **ambient conservative dynamics**, self-adjointness of the **zero-bearing operator**, and reality of **resonance poles of a compression/continuation**. Only the latter two can directly constrain the Riemann divisor, and neither follows from the first.

Therefore future source-determined constructions should be rejected as localization mechanisms if their final step is only

\[
\text{full zeta divisor in a dissipative/compressed generator}
\longrightarrow
\text{that generator has a self-adjoint/unitary dilation}.
\]

The correct load-bearing question is instead: **what arithmetic theorem prevents a hypothetical off-line zero from remaining a perfectly legitimate complex resonance of the self-adjoint global system?** Without such a theorem, the construction has reproduced classical Lax--Phillips dilation geometry rather than advanced the RH mechanism.