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

PF-234 now removes the apparent lower-coercivity gap in the **actual seam normalizer**. In PF-205's intrinsic signed Fermi-area coordinate, the exact seam metric is

\[
g=\frac{dx^2}{1+x^2}+(1+x^2)ds^2,
\qquad |x|<w,
\]

so the full shifted seam energy is two-sided comparable to the flat energy on the same strip with factors `(1+w^2)^{+-1}`. Minimizing with equal data on the two seam boundaries gives

\[
(1+w^2)^{-1}M_L\tanh(wM_L)
\le_{\rm form}
Q_{L,w}^{\rm hyp,+}
\le_{\rm form}
(1+w^2)M_L\tanh(wM_L),
\]

where `M_L=(1-partial_s^2)^{1/2}`. For the canonical widths `w_n=O(P_n^{-1})`, the actual symmetric seam branch is therefore the PF-228 flat normalizer up to relative `1+O(P_n^{-2})` factors at **all** tangential frequencies. The vanishing logarithmic-coordinate collar width at `theta=0,pi` is coordinate compression of the complete Fermi direction, not loss of intrinsic seam coercivity.

The unresolved issue is now narrower: transport this controlled intrinsic seam normalizer into the **same boundary representation** as PF-233's exact variable-width corridor block and prove the required singular-value estimate without commuting the resulting operators. After that, control PF-232's shear at the off-diagonal DtN level and then the physical `P/H` projections plus finite one-cusp-pant completion.

## Research question

Can PF-234's all-frequency two-sided control of the actual PF-205 seam-energy forms be combined, through the exact boundary reparameterization, with PF-233's operator-valued corridor factorization to prove a normalized one-seam dressed transmission envelope at the PF-228 scale

\[
\frac{\sqrt{w_nw_{n+1}}}{s_n}
\]

with sufficient high-mode decay to feed PF-222's weak-trace reassembly? If not, which specific noncommuting boundary-identification, shear-transfer, projection, or pant-completion mechanism destroys that gain?

## Why it may matter

PF-228 proves that the `sqrt(w_nw_{n+1})/s_n` amplitude scale makes even a pessimistic inverse-seam channel population weak-trace compatible. PF-231--PF-233 show that the exact hyperbolic corridor has the correct channel scale and high-frequency damping through the full-axis conformal model, small graph shear, and the noncommuting variable-width diagonal problem. PF-234 now shows that the real PF-205 seam branch itself has the same all-frequency normalizer scale as PF-228's flat calibration, with only quadratic reciprocal-prime relative error.

A positive compatibility/completion theorem would therefore close most of the remaining local geometric gap before global nested-cut reassembly. A negative result must now identify a sharply localized mechanism in the change of boundary representation, off-diagonal shear response, physical projection, or pant completion rather than generic corridor fanout, graph tilt, diagonal width variation, or seam-normalizer degeneration.

## Decisive test

Start in the intrinsic marked cuff coordinate where PF-234 gives bounded comparison maps between the actual symmetric seam form and

\[
Q_{L,w}^{0,+}=M_L\tanh(wM_L).
\]

Transport those forms by the **exact** hypercycle/cuff boundary identification into the pulled-back trace space used by PF-233. Keep the exact raw diagonal corridor block

\[
C_n=-a_n^{-1/2}F(T_n^{1/2})a_n^{-1/2},
\qquad
F(x)=x/\sinh x,
\]

and estimate the genuinely noncommuting normalized block `Q_{n+1}^{-1/2}C_nQ_n^{-1/2}`. The target is the `sqrt(w_nw_{n+1})/s_n` low-band amplitude together with an exponentially or otherwise summably decaying high-mode envelope. PF-234 permits bounded-ideal insertion of the real seam normalization **once all factors live on the same trace space**; it does not permit replacing the transported normalizer by a scalar function of `A` or `T_n`.

Then quantify the passage from PF-233's diagonal form to PF-232's sheared form at the **cross-block** level; full positive-form Loewner comparison alone is insufficient. Carry the physical boundary-density unitary and `P/H` projections in their correct order. For one trimmed hypercycle its exact arclength density in the `theta` parameter is

\[
\frac{d\sigma_\rho}{d\theta}
=
\frac{\cosh\rho}
{\sin\theta\sqrt{1+\sinh^2\rho\sin^2\theta}}.
\]

The singular endpoint weight is now understood as a representation issue, but it is still not a uniformly bounded multiplication on flat `dtheta` and therefore must be conjugated exactly rather than discarded. Finally account explicitly for the finite cuff arcs and one-cusp-pant end completion; the complete-axis Friedrichs corridor cannot silently impose artificial conditions at the pant ends.

A useful positive outcome is the required dressed singular-value envelope for the actual local block. A useful negative outcome is an admissible boundary sequence showing precisely where the boundary reparameterization, shear perturbation, physical projection, or completion defeats it. Even if this succeeds, neighboring-cell extension mass and PF-222's overlapping nested-cut sum remain separate global gates.

## Evidence boundary

The conformal rectangle, Pöschl--Teller separation, exact hypercycle graphs, and fixed-domain form are established by PF-231. Reciprocal-prime smallness of graph-straightening shear and full energy-DtN form comparability are established by PF-232. PF-233 establishes an exact operator-valued factorization and uniform raw cross-block channel/high-mode envelope for the **variable-width diagonal** corridor. PF-234 establishes a two-sided all-frequency theorem for the **actual PF-205 symmetric seam normalizer** in its intrinsic marked cuff coordinate and shows that the flat PF-228 normalizer is accurate up to relative `1+O(P_n^{-2})` factors.

None of these findings proves that the transported seam normalizer commutes with PF-233's `A`, `T_a`, multiplication by `a`, or raw corridor cross block. They also do not prove an off-diagonal perturbation theorem from the diagonal to the sheared DtN, physical-`L^2`/`P-H` singular-value control, finite-pant completion, or the final normalized `sqrt(w_nw_{n+1})/s_n` dressed estimate. This clue remains accepted because successive exact reductions have removed the seam-coercivity uncertainty and left a narrower representation/compatibility target, not because the desired transfer or any RH consequence has been established.

## Research disposition

Continue the conformal route with one residual local target: **transport PF-234's real seam normalizers into PF-233's boundary space and prove or refute the PF-228 `w/s` normalized dressed cross-block envelope, then control PF-232 shear plus physical/pant completion**. Do not reopen generic variable-fanout, graph-tilt, diagonal-width, or seam-coercivity objections unless a concrete calculation invalidates PF-231--PF-234.