---
id: CLUE-prime-flute-conformal-rectangle-dtn-normalizer-transfer
type: research-clue
status: proposed
origin: research-watch
target_line: prime_flute
based_on:
  - research/prime_flute/findings/PF-230-hyperbolic-corridor-has-pi-over-s-axis-inverse-width-budget.md
  - research/prime_flute/findings/PF-205-natural-width-cuff-smoothing-is-C1-uniform-and-critical-orlicz-summable.md
  - research/prime_flute/findings/PF-228-flat-corridor-dressing-makes-inverse-seam-multiplicity-weak-trace-compatible.md
  - research/prime_flute/findings/PF-229-frozen-serial-schur-completion-preserves-flat-corridor-cut-scale.md
  - research/prime_flute/findings/PF-222-reciprocal-prime-schur-commutator-is-compact-by-one-seam-decoupling.md
  - research/prime_flute/clues/CLUE-weak-trace-reassembly-with-summable-local-mass.md
---

# Can conformal separation isolate the real boundary-normalization obstruction?

## Observation

PF-230 proves that the axis corridor has the leading Fermi width `s cosh(t)`, even after natural-width trimming. This rules out calling that physical geometry an asymptotically constant-width strip. It does not rule out a different representation that separates the shifted energy exactly. The following explicit upper-half-plane calculation supplies a candidate reference operator; it does not identify that reference with the actual normalized pant cut.

Map the two complete ultraparallel cuff axes by a hyperbolic isometry to the concentric semicircles `|z|=1` and `|z|=exp(s)`, where `s` is their common-perpendicular distance. In logarithmic polar coordinates

\[
z=e^{q+i\theta},\qquad 0<q<s,\quad 0<\theta<\pi,
\]

the hyperbolic metric and positive-shift energy are exactly

\[
g=\frac{dq^2+d\theta^2}{\sin^2\theta},\qquad
\mathcal E[u]=\int_0^s\!\int_0^\pi
\left(|u_q|^2+|u_\theta|^2+\csc^2\theta\,|u|^2\right)d\theta\,dq.
\]

Here the nonnegative hyperbolic Laplacian is `-div grad`, so its `+1` equation becomes

\[
(-\partial_q^2+A)u=0,\qquad
A=-\partial_\theta^2+\csc^2\theta.
\]

Take the Friedrichs realization of `A` in `L^2((0,pi),dtheta)`, initially on compactly supported smooth functions, and put `B=A^{1/2}`. The complete-axis strip's two-boundary **energy** DtN form in the `dtheta` trace representation is

\[
\boxed{\Lambda_s^{\rm conf}=
\begin{pmatrix}
B\coth(sB)&-B\operatorname{csch}(sB)\\
-B\operatorname{csch}(sB)&B\coth(sB)
\end{pmatrix}.}
\]

This follows by solving the scalar boundary problem in each `A`-eigenfunction; it is an exact separation of the bulk equation, not a flat-metric approximation. The reference modes are explicit: with `alpha=(1+sqrt(5))/2`, so `alpha(alpha-1)=1`,

\[
A\psi_n=(n+\alpha)^2\psi_n,\qquad
\psi_n(\theta)=\sin^\alpha\theta\,C_n^\alpha(\cos\theta),\quad n\ge0,
\]

up to normalization. This is the classical symmetric trigonometric Pöschl–Teller/Gegenbauer problem. A precise literature anchor is A. Smirnov, *View on N-dimensional spherical harmonics from the quantum mechanical Pöschl-Teller potential well*, arXiv `1901.06711v1`, section 4, equations (4.4)–(4.9). Substitution into the Gegenbauer equation independently verifies the spectral formula; no novelty or arithmetic significance is claimed for it.

Along the first axis, signed arclength can be chosen as `t=log tan(theta/2)`. Then `dt=dtheta/sin(theta)` and `sin(theta)=sech(t)`. The angular interval of length `pi` is compatible with PF-230's leading integral `integral sech(t) dt=pi`; it does not convert that geometric calibration into the physical operator's singular-value count.

The actual constant-distance seam trimming also has an exact representation. Signed distance `d` from `q=0` satisfies `sinh d=sinh q/sin theta`. Define

\[
a_\rho(\theta)=\operatorname{arsinh}(\sinh\rho\,\sin\theta).
\]

The two pant-facing equidistant curves at distances `rho_1,rho_2` therefore become

\[
q=a_{\rho_1}(\theta),\qquad
q=s-a_{\rho_2}(\theta),
\]

with conformal-coordinate width

\[
\boxed{s-a_{\rho_1}(\theta)-a_{\rho_2}(\theta)}.
\]

Since `0<=a_rho<=rho`, this width lies between `s-rho_1-rho_2` and `s`. PF-230's natural-width bound `(rho_1+rho_2)/s<=kappa+o(1)<1` thus gives a nondegenerate conformal rectangle perturbation. Smallness is governed by the offset-to-separation ratio, not by the false assertion `cosh(t)=1+o(1)` on a fixed Fermi window.

There is a concrete seam-normalizer comparison to investigate rather than declaring it diagonal in `A`. For the complete symmetric collar `|q|<a_rho(theta)`, define `Q_rho^{conf,+}` by minimizing the shifted energy with equal pulled-back profiles `f(theta)` on its two boundaries and dividing that minimum by two. The admissible trial extension `u(q,theta)=f(theta)` yields, for `f` compactly supported in `(0,pi)`,

\[
\boxed{\langle f,Q_\rho^{\rm conf,+}f\rangle
\le\int_0^\pi a_\rho(\theta)
\left(|f'|^2+\csc^2\theta\,|f|^2\right)d\theta
\le\rho\langle f,Af\rangle.}
\]

The factor of two is essential: this is one symmetric boundary branch, not the summed energy of two copies. This trial-form inequality supplies only an upper comparison; it does not establish a two-sided normalizer theorem or a dressed cross-block bound.

## Research question

Can this conformal energy representation, together with the exact offset curves and seam comparison, supply a faithful local dressed DtN/Poisson estimate at the PF-228 `sqrt(w_1 w_2)/s` scale for the real PF-205 trimmed pant? More precisely, can one localize the obstruction to the actual boundary-energy normalizer, end completion, and physical frequency projections, instead of attributing it to irreducible bulk mode mixing merely because the Fermi width varies?

The natural comparison object is the operator-function DtN matrix above with the **actual pulled-back seam forms**, not an invented commuting normalizer `B tanh(wB)`. Seek a same-Hilbert-space factorization or controlled form-transfer theorem, with a spectral-band estimate strong enough to bound the dressed singular-value population. If it fails, identify the exact boundary/domain/completion term causing failure.

## Why it may matter

The exact bulk reference is fully separable and its mode scale is explicit, so a comparison need not start with an uncontrolled variable-width flat-strip approximation. A successful transfer could provide both inverse-seam damping and the high-mode decay needed before PF-222's global cut assembly. The elementary trial-form comparison also identifies a concrete starting inequality whose missing lower/domain information can be tested.

This is different from the already accepted umbrella question: it proposes a specific coordinate map, transverse operator, boundary deformation, and variational normalizer bound. It is compatible with PF-230, which explicitly allows a transformation that makes its nonconstant physical profile harmless. None of the logarithmic-polar change, separation-of-variables formula, or classical transverse spectrum is presented as a new general theorem.

## Decisive test

First verify the full representation on the complete-axis control, including domains at `theta=0,pi`. For the untrimmed axes, physical arclength is `dt=dtheta/sin(theta)`. The unitary `U:L^2(dt)->L^2(dtheta)` is `Uf=sin(theta)^{-1/2}f`; accordingly

\[
U\Lambda_s^{\rm phys}U^{-1}
=\sin(\theta)^{1/2}\Lambda_s^{\rm conf}\sin(\theta)^{1/2}
\]

in the corresponding form sense, with the multiplier on both boundary copies. These singular-endpoint multipliers are not uniformly bounded invertible changes of the unweighted trace norm. Pull back the seam form through the same transformation and, if useful, prove the correct polar/unitary equivalence of the energy-normalized operators. Do not cancel square roots of noncommuting forms by inspection.

For a trimmed curve `q=a_rho(theta)`, use its exact arclength density

\[
\frac{\sqrt{1+(a_\rho')^2}}{\sin\theta}
=\frac{\cosh\rho}{\sin\theta\sqrt{1+\sinh^2\rho\sin^2\theta}}.
\]

Flatten the two offset graphs only at the level of the full shifted form, keeping the transformed potential and boundary trace maps. Establish which constants are uniform as `s` tends to zero with the PF-205 offset ratios. The trial inequality above is a starting test, not permission to infer that off-diagonal blocks of inverses are monotone under form ordering. Check the symmetric and antisymmetric seam branches separately before reconstructing the full physical module.

Then distinguish the complete-axis covering strip from the finite cuff arcs and the remaining one-cusp pant. Identify the end/cusp boundary conditions and the exact extension or Schur elimination used to complete the central region. A complete-axis Friedrichs control cannot silently replace the pant or impose artificial vanishing on its ends. Carry the physical `P/H` projections in their correct transformed order. A useful positive result is a bound for the actual normalized local dressed block with the required amplitude and high-mode envelope; a useful negative result identifies an admissible sequence on which the boundary normalization or end completion defeats that bound.

A constructive transfer argument and an endpoint-localized counterexample search are complementary uses of the same representation. Even if local transfer succeeds, variable neighboring-cell extension mass and PF-222's overlapping nested-cut sum remain separate gates; PF-229's frozen-chain comparison does not settle either.

## Evidence boundary

These explicit calculations describe reference energy forms and proposed comparison ingredients, not an accepted Mathia finding or a formal verification. No operator equality between the full pant and the complete-axis rectangle has been established. The discrete spectrum of `A` in `L^2(dtheta)` is not by itself a discrete physical boundary spectrum or an `O(1/s)` singular-value upper count: the original boundaries have infinite arclength, singular weights, different seam forms, and nontrivial completion. The normalizer upper bound alone gives neither an inverse comparison in the required off-diagonal norm nor a weak-Schatten theorem. No global mixed cut estimate, nested reassembly, prime/clone separation, or RH implication is claimed.
