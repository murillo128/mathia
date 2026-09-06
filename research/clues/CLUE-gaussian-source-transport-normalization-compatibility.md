---
id: CLUE-global-gaussian-source-transport-normalization-compatibility
type: research-clue
status: proposed
origin: independent-review
target_line: global
based_on:
  - research/xi_flow/clues/CLUE-gaussian-reference-quotient-localizes-heat-without-zero-seams.md
  - research/analytic_frontier/clues/CLUE-gaussian-xi-source-periodization-relative-error.md
  - research/xi_flow/findings/XF-071-guarded-log-vieta-quotient-blocks-ultra-infrared-repopulation.md
  - research/xi_flow/findings/XF-072-period-dilation-trades-interface-suppression-for-local-frame-dilution.md
---

# Is there one compatible source-to-transition scale regime for a reference-divided Gaussian heat localization?

## Observation

The proposed construction has two separate destination-local handoffs. Analytic Frontier receives a candidate relative comparison of the actual time-zero Xi function with its Gaussian periodization, justified by Euler-product bounds and the Gamma factor on a reflected half-plane. Xi Flow receives an exact Gaussian heat symmetry and a known-reference quotient whose interior non-affine drift is exponentially small. Neither handoff alone closes the source-to-transition implication.

The source candidate, for fixed reflected real part greater than one, has a relative image error bounded by a polynomial times `exp(-L^2/(8 w_ref^2))` when `L>=pi w_ref^2`. The known Gaussian-reference logarithmic drift has an explicit bound of order `(L/(w_ref^2 h)) exp(-L^2/(4 w_ref^2 h))`, where `h=1-2t/w_ref^2>0`. A Gaussian **selector** window separately has prime leakage bounded by a prefactor times `exp(-w_sel^2 d^2/2)`, where `d` is its distance from the first prime frequency. The reference width `w_ref` and the measurement width `w_sel` are different choices; equating them without checking the frame can destroy the original destination resolution.

Arbitrary zero-block periodization does not have these source-dependent comparisons. Conversely, the new function construction creates artificial non-real seam zeros even from a zero-free Gaussian. Known-reference division and an interior domain are indispensable, and the divided state no longer has the unforced finite-degree Vieta evolution automatically.

## Research question

Can the two lines establish a **single compatible parameter regime and norm** in which source error, reference drift, Fourier/analytic truncation, and frame conditioning are all dominated by the same destination signal?

For a fixed positive heat interval, define all errors in explicitly compatible norms. If `K_T` is the proved transport amplification, `D_T` the required state/derivative control, and `b_T` the actual local frame lower constant at the norm level, the relevant test has the form

\[
\frac{K_T}{b_T}\left(E_{\rm source}(T)
+\int D_T(t)E_{\rm drift}(T,t)\,dt
+E_{\rm truncation}(T)\right)\longrightarrow0.
\]

This is a proposed admission inequality, not an assertion that those stability quantities exist or are polynomially bounded. The norm, operator domains, contour, and time dependence must be part of the theorem.

## Why it may matter

The central opportunity is not another isolated identity. It is the possibility that an actual arithmetic relative estimate pays for a local heat construction without the seam/frame cancellation in XF-072. A starting scale experiment is `w_ref ~ log T`, `L ~ (log T)^3`, while preserving the destination's required selector width independently. The reference image error then has an exponent of order `-(log T)^4` at the fixed source line, but no conclusion follows before the moving-line constants and the full normalized stability cost have been compared with that exponent.

This test is genuinely cross-line: Analytic Frontier can establish source admissibility but not the nonlinear transition coercivity; Xi Flow can establish the dynamical comparison but cannot assume an Euler product at positive heat time.

## Decisive test

Require one complete source-to-destination inequality rather than separate vanishing-error claims with incompatible widths or normalizations. Independently reconstruct the local clue calculations, then determine the first uncontrolled factor in the displayed admission inequality. A useful negative result is a concrete incompatible exponent, unavoidable reference pole, or conditioning loss that consumes the gain. A useful positive result is one normalized, source-faithful transport theorem on compatible scales.

Even after that positive result, require a separate theorem that a hypothetical `Lambda>0` Xi transition forces a nonvanishing retained destination state. A collision hidden in the discarded sector, a zero-density defect, or a vanishing normalized signal cannot be ruled out by source smallness alone. Do not identify high zero density, universal simplicity, or auxiliary surrogate roots with RH.

## Evidence boundary

The local handoffs are `proposed`, not accepted findings. The Gaussian/Appell symmetry and Euler-product/Gamma ingredients are classical; the new candidate is their source-faithful, reference-divided assembly and its quantitative compatibility test. No source-to-transition theorem or bound on Lambda has been proved by creating this clue. The existing destination-local copies carry the information needed by the isolated research watches; this global clue is for evaluating their mathematical compatibility, not evidence that either watch has executed or accepted them.
