# MI-001 — Farey occupation is a multiplicative-placement problem, not a growth-exponent problem

**Evidence level:** supported

## Core intuition

The projective Farey obstruction has been narrowed beyond generic regularity and beyond finite spectral complexity. The physical quotient-shell source already carries the full Mertens/zeta-zero power exponent on every fixed Jordan row, and nonsquarefree dilation forces positive average occupation along every complete multiplicative chain. A remaining failure can therefore only be **sparse in scale** and must exploit the arithmetic placement of large shell values, not a missing global exponent or ordinary short-interval roughness.

## Strongest justified claim

FD-031--FD-040 separate a universal favorable bulk from a possible low-row hyperbola-amplification escape. Terminal quotient blocks have fixed positive nonsquarefree density, while a synthetic one-Lipschitz shell profile can still concentrate enough energy on sparse low rows to drive the global occupation ratio to zero along a subsequence. Every fixed finite supercritical Mellin packet is nevertheless coercively sampled by nonsquarefree rows.

FD-041--FD-045 strengthen the physical side. Squarefree/nonsquarefree occupation is a dilation sieve of one energy curve, centering cancels the critical pole, and the weighted squarefree Euler product plus Walfisz cancellation controls growing packets through and slightly beyond the square-root frequency window. Merely increasing frequency to that scale is not an escape.

FD-046 identifies the source exponent exactly. The physical shell source `H` and the Mertens function are inverse floor transforms, so their polynomial growth exponent is the same rightmost-zero exponent `Theta`. Every fixed row, and hence both total and nonsquarefree energies, has limsup exponent `2 Theta`. No global polynomial decay of nonsquarefree occupation is possible.

FD-047 turns square-divisor self-similarity into a pointwise lower-scale injection `U_H >= w(q) E_(floor(H/q))`. Along every `q`-adic chain this yields a positive geometric-mean/average occupation and forces the set of extremely small occupation values to have small logarithmic density.

FD-048 then closes the generic smoothness response. Matomaki--Teravainen short-interval Möbius cancellation transfers to `H`, but a much smoother synthetic profile can still realize sparse occupation escape. What the control lacks is the exact multiplicative placement of the physical increments `Delta H(n)=mu(rad n) phi(rad n)/n`.

## Synthesis of evidence

The surviving difficulty is no longer “make the source regular enough” or “show nonsquarefree rows grow at the right rate.” Those are already controlled at the relevant levels. The problem is to prevent isolated horizons from arranging the physical increment pattern so that hyperbola sampling sends disproportionate energy into a few squarefree low rows while respecting all multiplicative-chain averages.

This suggests a theorem shaped around divisibility covariance, dilation consistency, or another source-specific relation coupling neighboring multiplicative scales. A successful estimate should target the exceptional-set geometry directly rather than strengthen an already-favorable limsup exponent or short-interval norm.

## Counterevidence / boundary cases

FD-047 does not give a pointwise positive occupation fraction; geometric-mean and density statements permit sparse bad horizons. FD-048's smooth countermodel is not physical and does not satisfy the exact multiplicative increment law. FD-046 controls polynomial exponents only and is compatible with ratios tending to zero slower than every power.

Thus the synthesis does not assert that the physical occupation is positive pointwise. It identifies what any counterexample must still accomplish.

## Epistemic status

**Supported source-specific narrowing:** power growth, complete-chain average occupation, finite/growing packet coercivity, and ordinary short-interval regularity are all insufficient currencies for the final pointwise statement. The unresolved information is multiplicative placement across the hyperbola samples.

## Novelty/prior-art status

No broad novelty claim is made beyond the finding-level audits. This note synthesizes the current exact Mathia boundaries.

## Falsification criterion

Construct a shell profile satisfying the exact physical increment/divisibility law and the established floor-transform relations while realizing a subsequence with `U/E -> 0`, or prove that those laws force a positive pointwise or sufficiently strong density lower bound. Either outcome would resolve the current diagnosis.
