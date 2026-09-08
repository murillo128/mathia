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
  - research/prime_flute/clues/CLUE-weak-trace-reassembly-with-summable-local-mass.md
---

# Can conformal separation isolate the real boundary-normalization obstruction?

## Observation

PF-231 establishes the exact logarithmic representation of the complete neighboring-axis corridor: after an isometry and `z=exp(x+i theta)`, the shifted energy is separable on `(0,s) x (0,pi)` with transverse operator `A=-partial_theta^2+csc^2(theta)` and exact two-axis energy DtN matrix `A^(1/2)[[coth(sA^(1/2)),-csch(sA^(1/2))],[-csch(sA^(1/2)),coth(sA^(1/2))]]`. It also gives the exact PF-205 inward hypercycle graphs and their fixed-domain form after straightening.

PF-232 removes a further apparent obstruction. Although the straightened differential expression contains `b/a=O(1)`, the natural thin-strip energy normalization turns the gradient part into `|P|^2+|Q-bP|^2`, where `|b|<=max(sinh rho_1,sinh rho_2)=max(w_1,w_2)`. For the canonical PF-205 supports this is `O(P_n^-1)`. Thus graph tilt is reciprocal-prime form-small; the independent width loss `(rho_1+rho_2)/s` remains uniformly controlled but can be order one relative to the corridor width.

One useful variational handle from the original proposal remains unresolved rather than superseded. For the complete symmetric collar `|x|<f_rho(theta)` with `f_rho(theta)=arsinh(sinh(rho) sin(theta))`, define the symmetric pulled-back seam energy `Q_rho^{conf,+}` by minimizing the shifted energy with the same profile `f(theta)` on both boundary curves and dividing the minimum by two. The constant-in-`x` trial extension gives

\[
\langle f,Q_\rho^{conf,+}f\rangle
\le
\int_0^\pi f_\rho(\theta)
\left(|f'(\theta)|^2+\csc^2\theta\,|f(\theta)|^2\right)d\theta
\le
\rho\langle f,Af\rangle.
\]

This is only an upper form comparison; it neither supplies the missing lower bound nor controls a normalized inverse cross block.

The unresolved issue is therefore no longer generic bulk mode mixing from the variable Fermi profile. It is the transfer from this exact energy model to the **actual normalized local dressed block**, including the variable-width diagonal problem, real seam-energy normalizers, physical boundary representation and `P/H` projections, and finite one-cusp-pant completion.

## Research question

Can the PF-231/PF-232 conformal form comparison be upgraded to a faithful estimate for the actual PF-205 normalized one-seam dressed transmission with the PF-228 scale

\[
\frac{\sqrt{w_nw_{n+1}}}{s_n}
\]

and sufficient high-mode decay to feed PF-222's weak-trace reassembly?

Equivalently, after separating the now-controlled graph shear from the width coefficient, can one prove a same-boundary-space estimate for the real energy-normalized Schur cross block, or identify a specific normalizer/completion/projection mechanism that destroys the `w/s` gain?

## Why it may matter

PF-228 proves that exactly this amplitude scale makes even a pessimistic inverse-seam channel population weak-trace compatible. PF-231 supplies an exact hyperbolic bulk reference rather than a fictitious constant-width geometric approximation, and PF-232 shows that straightening its actual hypercycle boundaries introduces only reciprocal-prime relative form shear. A positive transfer would therefore close the main remaining local geometric gap before global nested-cut reassembly; a negative result would have to identify a much more specific obstruction than variable corridor fanout.

## Decisive test

Work on the common pulled-back boundary trace space of the PF-231 fixed strip. Keep the exact variable-width diagonal form and the actual PF-205 seam-energy forms rather than replacing them by commuting functions of the Pöschl--Teller operator. Prove a two-sided normalizer comparison or a direct Schur-factor estimate strong enough to control the normalized cross block on the `s_n A^(1/2)=O(1)` population and to obtain exponential or otherwise summable decay above that band. The displayed trial inequality is a starting upper bound, not permission to invert the ordering.

Carry the physical boundary-density unitary and the `P/H` projections in their correct order. For one trimmed hypercycle its exact arclength density in the `theta` parameter is

\[
\frac{d\sigma_\rho}{d\theta}
=
\frac{\cosh\rho}
{\sin\theta\sqrt{1+\sinh^2\rho\sin^2\theta}}.
\]

These singular endpoint weights are not uniformly bounded changes of the flat `dtheta` boundary norm. Loewner comparison of the full positive DtN form is likewise not enough: the decisive estimate must survive the boundary identification, normalization, and extraction of the cross block. Do not cancel square roots of noncommuting seam forms or infer inverse/off-diagonal monotonicity from PF-232's form inequalities.

Then account explicitly for the finite cuff arcs and the one-cusp-pant end completion. The complete-axis Friedrichs corridor may be used as a reference, but it cannot silently impose artificial boundary conditions at the pant ends. A useful positive outcome is the required dressed singular-value envelope for the actual local block; a useful negative outcome is an admissible boundary sequence showing precisely where the normalizer, width coefficient, projection, or completion defeats it.

Even if this local transfer succeeds, neighboring-cell extension mass and PF-222's overlapping nested-cut sum remain separate global gates.

## Evidence boundary

The conformal rectangle, Pöschl--Teller separation, exact hypercycle graphs, and fixed-domain form are established by PF-231. The reciprocal-prime smallness of graph-straightening shear and the resulting **full energy-DtN form comparability** are established by PF-232. Neither finding proves an off-diagonal dressed block estimate, a two-sided theorem for the actual PF-205 seam normalizer, physical-`L^2` singular-value control, finite-pant completion, or weak `S_1` reassembly.

The proposed `sqrt(w_nw_{n+1})/s_n` transfer for the real pant therefore remains unproved. This clue is accepted because the route is now exact enough to justify continued investigation, not because the desired transfer or any RH consequence has been established.

## Research disposition

The conformal route survives initial derivation, adversarial form scaling, and prior-art audit. Continue it with one precise residual target: **prove or refute the PF-228 `w/s` normalized cross-block envelope for the real PF-205 variable-width pant boundary problem after the PF-232 shear reduction**. Do not reopen generic variable-fanout or graph-tilt objections unless a concrete calculation invalidates PF-231 or PF-232.