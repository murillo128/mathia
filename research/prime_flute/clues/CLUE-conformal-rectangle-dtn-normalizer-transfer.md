---
id: CLUE-prime-flute-conformal-rectangle-dtn-normalizer-transfer
type: research-clue
status: accepted
origin: research-watch
target_line: prime_flute
based_on:
  - research/prime_flute/findings/PF-205-natural-width-cuff-smoothing-is-C1-uniform-and-critical-orlicz-summable.md
  - research/prime_flute/findings/PF-222-reciprocal-prime-schur-commutator-is-compact-by-one-seam-decoupling.md
  - research/prime_flute/findings/PF-228-flat-corridor-dressing-makes-inverse-seam-multiplicity-weak-trace-compatible.md
  - research/prime_flute/findings/PF-229-frozen-serial-schur-completion-preserves-flat-corridor-cut-scale.md
  - research/prime_flute/findings/PF-230-hyperbolic-corridor-has-pi-over-s-axis-inverse-width-budget.md
  - research/prime_flute/findings/PF-231-ultraparallel-corridor-is-exactly-separable-in-logarithmic-coordinates.md
  - research/prime_flute/findings/PF-232-hypercycle-straightening-shear-is-reciprocal-prime-form-small.md
  - research/prime_flute/findings/PF-233-variable-width-diagonal-corridor-has-exact-operator-valued-transfer-law.md
  - research/prime_flute/findings/PF-234-pf205-symmetric-seam-normalizer-is-quadratically-flat-comparable.md
  - research/prime_flute/findings/PF-235-hypercycle-boundary-compactification-has-only-quadratic-prime-dependent-defect.md
  - research/prime_flute/clues/CLUE-weak-trace-reassembly-with-summable-local-mass.md
---

# Can conformal separation isolate the real boundary-normalization obstruction?

## Observation

PF-231 establishes the exact logarithmic representation of the complete neighboring-axis corridor and identifies the PF-205 inward hypercycle graphs. PF-232 then shows that straightening those graphs creates only reciprocal-prime-small relative shear in the natural thin-strip energy norm; the independent width loss remains uniformly controlled but can be order one relative to the corridor width.

PF-233 removes the next apparent obstruction without pretending that the variable width commutes with the Pöschl--Teller operator. For the exact PF-232 diagonal form with width `a(theta)`, the boundary-mass substitution `y=a(theta)^(-1/2)v` produces an exact product problem `-partial_X^2+T_a`. Its effective transverse operator satisfies `T_a asymp s^2 A` uniformly on the canonical tail, where `A=-partial_theta^2+csc^2(theta)`. Consequently the diagonal corridor's raw cross-DtN block is exactly

\[
-a^{-1/2}\,T_a^{1/2}\operatorname{csch}(T_a^{1/2})\,a^{-1/2},
\]

has `O(s^{-1})` channels on each fixed scaled band, and retains exponential high-mode decay. Thus variable-width diagonal noncommutation itself cannot destroy the PF-228/PF-231 raw transfer envelope.

PF-234 removes the apparent lower-coercivity gap in the **actual seam normalizer**. In PF-205's intrinsic signed Fermi-area coordinate, the exact seam energy is two-sided comparable to the flat strip energy with factors `(1+w^2)^{+-1}`. On the symmetric branch this gives all-frequency comparison with `M_L tanh(wM_L)` and relative `1+O(P_n^{-2})` accuracy for canonical widths.

PF-235 now factors the remaining hypercycle boundary map itself. If `tau=log tan(theta/2)` is arclength on the untrimmed axis and `t` is the Fermi footpoint coordinate of the inward hypercycle at distance `rho`, `w=sinh rho`, then

\[
t=\operatorname{arsinh}\left(\frac{\sinh\tau}{\cosh\rho}\right),
\qquad
\frac{dt}{d\tau}
=\frac1{\sqrt{1+w^2\operatorname{sech}^2\tau}}.
\]

Hence the entire endpoint singularity is the **fixed** compactification `d tau=csc(theta)dtheta`; the seam-dependent part is globally `1+O(w^2)`, has coordinate shift `log cosh rho=O(w^2)`, and has exact integrable Jacobian defect `log(1+w^2)`. For canonical PF widths these defects are `O(P_n^{-2})` and summable over seams. The inward-hypercycle identification itself therefore cannot supply a first-order reciprocal-prime or nonsummable loss.

The unresolved issue is narrower still: handle the fixed but singular axis compactification in the same Hilbert trace realization as PF-233, retain genuine noncommutation, and prove the **inverse-level** two-boundary cancellation responsible for PF-228's `w/s` scale. After that, control PF-232's shear at the off-diagonal inverse/DtN level and then the physical `P/H` projections plus finite one-cusp-pant completion.

## Research question

Can PF-234/PF-235's control of the actual seam-energy forms through the axis compactification be combined with PF-233's operator-valued corridor factorization to prove that the off-diagonal block of the full normalized inverse

\[
D_n=(I+K_n)^{-1},
\qquad
K_n=Q_n^{-1/2}\Lambda_nQ_n^{-1/2},
\]

retains the PF-228 dressed scale

\[
\frac{\sqrt{w_nw_{n+1}}}{s_n}
\]

on the inverse-seam band, together with sufficient high-mode decay to feed PF-222's weak-trace reassembly? If not, which specific fixed compactification/noncommutation, shear-transfer, projection, or pant-completion mechanism destroys that inverse-level gain?

## Why it may matter

PF-228 proves that the `sqrt(w_nw_{n+1})/s_n` amplitude scale makes even a pessimistic inverse-seam channel population weak-trace compatible. PF-231--PF-233 show that the exact hyperbolic corridor has the correct raw channel scale and high-frequency damping; PF-234 shows that the real PF-205 seam branch has the correct normalizer scale; PF-235 shows that the **prime-dependent** part of the hypercycle-to-log boundary identification is only quadratic and strongly summable.

A positive compatibility/completion theorem would therefore close most of the remaining local geometric gap before global nested-cut reassembly. A negative result can no longer be attributed generically to corridor fanout, graph tilt, diagonal width variation, seam-normalizer degeneration, or a first-order hypercycle coordinate distortion. It must expose a more specific failure in the fixed axis compactification, noncommuting full inverse, off-diagonal shear response, physical projection, or finite-pant completion.

## Decisive test

Work on one neighboring-cuff edge and put **both seam forms and the PF-233 two-boundary DtN form into one scalar `theta` trace variable without discarding density factors**. Use PF-235 to factor each seam-side map as the fixed axis compactification

\[
\tau=\log\tan(\theta/2)
\]

followed by a seam-dependent diffeomorphism whose form distortion is only `1+O(w_i^2)`. Preserve that perturbation honestly; form comparability alone does not authorize commuting it through later inverse blocks.

Let

\[
Q=\operatorname{diag}(Q_1,Q_2)
\]

be the resulting actual seam-energy forms in the common trace realization and let `Lambda_diag` be PF-233's exact variable-width two-boundary DtN matrix. Form

\[
K=Q^{-1/2}\Lambda_{\rm diag}Q^{-1/2},
\qquad
D=(I+K)^{-1}.
\]

The primary target is **`D_21`**, not the raw normalized cross block `K_21=Q_2^{-1/2}C Q_1^{-1/2}`. PF-228's `w/s` factor is created by inversion of the complete positive `2x2` precision matrix: its diagonal and cross entries cancel at the relevant scale. The raw normalized cross block can be parametrically larger and therefore must not be assigned the PF-228 envelope by analogy.

Prove, without assuming commutation of `Q_i` with `A`, `T_a`, `a`, or the corridor blocks, a singular-value/counting estimate of the form

\[
s_j(D_{21})
\lesssim
\frac{\sqrt{w_1w_2}}s\,\Phi(js)
\]

for a profile `Phi` with exponential or otherwise summable high-mode decay, or construct an admissible sequence that violates such an inverse-level bound. A useful proof may use Schur complements, Robin-to-Robin transfer, form-bounded congruences, or spectral splitting, but it must preserve the full matrix inversion rather than estimate only the cross entry before inversion.

Then quantify the passage from PF-233's diagonal form to PF-232's sheared form at the **off-diagonal inverse/DtN level**; full positive-form Loewner comparison alone is insufficient. Carry the physical boundary-density unitary and `P/H` projections in their correct order. PF-235 gives

\[
\frac{d\sigma_\rho}{d\theta}
=
\frac{\cosh\rho}
{\sin\theta\sqrt{1+\sinh^2\rho\sin^2\theta}}
=\csc\theta\times(1+O(w^2))
\]

uniformly in the multiplicative seam-dependent factor, so the nonuniform endpoint weight to be treated exactly is the fixed `csc(theta)` baseline rather than a new prime-dependent singularity. Finally account explicitly for the finite cuff arcs and one-cusp-pant end completion; the complete-axis Friedrichs corridor cannot silently impose artificial conditions at the pant ends.

A useful positive outcome is the required dressed singular-value envelope for the actual local inverse block. A useful negative outcome is an admissible boundary sequence showing precisely where the fixed compactification, noncommuting inversion, shear perturbation, physical projection, or completion defeats it. Even if this succeeds, neighboring-cell extension mass and PF-222's overlapping nested-cut sum remain separate global gates.

## Evidence boundary

The conformal rectangle, Pöschl--Teller separation, exact hypercycle graphs, and fixed-domain form are established by PF-231. Reciprocal-prime smallness of graph-straightening shear and full energy-DtN form comparability are established by PF-232. PF-233 establishes an exact operator-valued factorization and uniform raw cross-block channel/high-mode envelope for the **variable-width diagonal** corridor. PF-234 establishes a two-sided all-frequency theorem for the **actual PF-205 symmetric seam normalizer** in its intrinsic marked cuff coordinate. PF-235 establishes that the seam-dependent hypercycle-to-axis boundary identification is only `1+O(P_n^{-2})` and has a summable Jacobian defect, while explicitly leaving the fixed `tau<->theta` compactification and finite-pant completion open.

None of these findings proves that the transported seam normalizer commutes with PF-233's `A`, `T_a`, multiplication by `a`, or the raw corridor blocks. More importantly, none proves that Loewner/form comparison survives as the specific **off-diagonal inverse** estimate required by PF-228. They also do not prove an off-diagonal perturbation theorem from the diagonal to the sheared problem, physical-`L^2`/`P-H` singular-value control, finite-pant completion, or the final normalized `sqrt(w_nw_{n+1})/s_n` dressed estimate. This clue remains accepted because successive exact reductions have removed several false local obstructions and left a narrower inverse/representation target, not because the desired transfer or any RH consequence has been established.

## Research disposition

Continue the conformal route with one residual local target: **put the axis-reference seam forms and PF-233 corridor matrix in the same `theta` trace realization and prove or refute the PF-228 `w/s` envelope for the off-diagonal block of `D=(I+K)^{-1}`; then control PF-232 shear plus physical/pant completion**. Do not reopen generic variable-fanout, graph-tilt, diagonal-width, seam-coercivity, or first-order hypercycle-coordinate objections unless a concrete calculation invalidates PF-231--PF-235.