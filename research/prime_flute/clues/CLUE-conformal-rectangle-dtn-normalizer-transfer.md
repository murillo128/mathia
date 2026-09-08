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
  - research/prime_flute/clues/CLUE-weak-trace-reassembly-with-summable-local-mass.md
---

# Can conformal separation isolate the real boundary-normalization obstruction?

## Observation

PF-231 establishes the exact logarithmic representation of the complete neighboring-axis corridor and identifies the PF-205 inward hypercycle graphs. PF-232 then shows that straightening those graphs creates only reciprocal-prime-small relative shear in the natural thin-strip energy norm; the independent width loss remains uniformly controlled but can be order one relative to the corridor width.

PF-233 removes the next apparent obstruction without pretending that the variable width commutes with the Pöschl--Teller operator. For the exact PF-232 diagonal form with width `a(theta)`, the boundary-mass substitution `y=a(theta)^(-1/2)v` produces an exact product problem `-partial_X^2+T_a`. Its effective transverse operator satisfies `T_a asymp s^2 A` uniformly on the canonical tail, where `A=-partial_theta^2+csc^2(theta)`. Consequently the diagonal corridor's raw cross-DtN block is exactly

\[
-a^{-1/2}\,T_a^{1/2}\operatorname{csch}(T_a^{1/2})\,a^{-1/2},
\]

has `O(s^{-1})` channels on each fixed scaled band, and retains exponential high-mode decay. Thus variable-width diagonal noncommutation itself cannot destroy the PF-228/PF-231 transfer envelope.

One key normalizer issue remains unresolved. For the complete symmetric collar `|x|<f_rho(theta)` with `f_rho(theta)=arsinh(sinh(rho) sin(theta))`, define the symmetric pulled-back seam energy `Q_rho^{conf,+}` by minimizing the shifted energy with the same profile `f(theta)` on both boundary curves and dividing the minimum by two. The constant-in-`x` trial extension gives

\[
\langle f,Q_\rho^{conf,+}f\rangle
\le
\int_0^\pi f_\rho(\theta)
\left(|f'(\theta)|^2+\csc^2\theta\,|f(\theta)|^2\right)d\theta
\le
\rho\langle f,Af\rangle.
\]

This is only an upper form comparison. The seam collar degenerates at the ideal endpoints in logarithmic coordinates, so PF-233's positive-width-floor argument does not supply the missing lower bound and does not justify inversion of the normalizer.

The unresolved issue is therefore concentrated in the transfer from the exact PF-233 raw cross block to the **actual normalized local dressed block**: real seam-energy normalizers, perturbative passage from the diagonal form to the PF-232 sheared form at the off-diagonal level, physical boundary representation and `P/H` projections, and finite one-cusp-pant completion.

## Research question

Can the exact PF-233 cross-DtN factorization be combined with the actual PF-205 seam-energy forms to prove a normalized one-seam dressed transmission envelope at the PF-228 scale

\[
\frac{\sqrt{w_nw_{n+1}}}{s_n}
\]

with sufficient high-mode decay to feed PF-222's weak-trace reassembly? If not, which specific normalizer, shear-transfer, boundary-identification, projection, or pant-completion mechanism destroys that gain?

## Why it may matter

PF-228 proves that this amplitude scale makes even a pessimistic inverse-seam channel population weak-trace compatible. PF-231--PF-233 now show that the exact hyperbolic corridor has the correct channel scale and high-frequency damping through the full axis model, hypercycle straightening, and the noncommuting variable-width diagonal problem. A positive normalizer/completion transfer would therefore close most of the remaining local geometric gap before global nested-cut reassembly. A negative result would have to identify a sharply localized mechanism rather than generic corridor fanout, graph tilt, or width noncommutation.

## Decisive test

Work on the common pulled-back boundary trace space used by PF-233. Keep the actual PF-205 symmetric seam-energy forms `Q_n,Q_{n+1}` and the exact raw corridor cross block

\[
C_n=-a_n^{-1/2}F(T_n^{1/2})a_n^{-1/2},
\qquad
F(x)=x/\sinh x,
\]

rather than replacing either side by commuting scalar functions of `A`. Prove a two-sided seam-normalizer comparison or a direct factor estimate for the genuinely noncommuting normalized block `Q_{n+1}^{-1/2}C_nQ_n^{-1/2}` that yields the `sqrt(w_nw_{n+1})/s_n` low-band scale and summable high-mode tail. The displayed trial inequality is a starting upper bound, not permission to reverse order or cancel square roots.

Then quantify the passage from PF-233's diagonal form to PF-232's sheared form at the **cross-block** level; full positive-form Loewner comparison alone is insufficient. Carry the physical boundary-density unitary and `P/H` projections in their correct order. For one trimmed hypercycle its exact arclength density in the `theta` parameter is

\[
\frac{d\sigma_\rho}{d\theta}
=
\frac{\cosh\rho}
{\sin\theta\sqrt{1+\sinh^2\rho\sin^2\theta}}.
\]

These singular endpoint weights are not uniformly bounded changes of the flat `dtheta` boundary norm. Finally account explicitly for the finite cuff arcs and one-cusp-pant end completion; the complete-axis Friedrichs corridor cannot silently impose artificial conditions at the pant ends.

A useful positive outcome is the required dressed singular-value envelope for the actual local block. A useful negative outcome is an admissible boundary sequence showing precisely where the seam normalizer, shear perturbation, physical projection, or completion defeats it. Even if this succeeds, neighboring-cell extension mass and PF-222's overlapping nested-cut sum remain separate global gates.

## Evidence boundary

The conformal rectangle, Pöschl--Teller separation, exact hypercycle graphs, and fixed-domain form are established by PF-231. Reciprocal-prime smallness of graph-straightening shear and full energy-DtN form comparability are established by PF-232. PF-233 establishes an exact operator-valued factorization and uniform raw cross-block channel/high-mode envelope for the **variable-width diagonal** corridor.

None of these findings proves a two-sided theorem for the actual PF-205 seam normalizer, an off-diagonal perturbation theorem from the diagonal to the sheared DtN, physical-`L^2`/`P-H` singular-value control, finite-pant completion, or the final normalized `sqrt(w_nw_{n+1})/s_n` dressed estimate. This clue remains accepted because the route has survived successive exact reductions and now has a narrower falsifiable boundary-normalization target, not because the desired transfer or any RH consequence has been established.

## Research disposition

Continue the conformal route with one residual local target: **prove or refute the PF-228 `w/s` normalized dressed cross-block envelope after inserting the actual PF-205 seam normalizers into PF-233's exact variable-width transfer law and then controlling PF-232 shear plus physical/pant completion**. Do not reopen generic variable-fanout, graph-tilt, or diagonal-width objections unless a concrete calculation invalidates PF-231--PF-233.