# MI-007 — Bow completion is an absolute, phase-sensitive endpoint-memory problem

**Evidence level:** supported

## Core intuition

The bow endpoint obstruction is not determined by moving-window energy or by qualitative relative uniformity. Target-sized completion forces a large **positive real** dyadic shifted correlation at the distinguished logarithmic twist. That signed shell can be represented exactly as a dyadic scale-slope defect of a positive endpoint Fejer family, but controlling the individual positive energies or ordinary relative correlations is not enough.

A small coherent carrier-aligned drift can accumulate target-scale charge and the endpoint primitive can remember it after the drift stops. The final theorem therefore needs absolute precision in the signed/scale-difference statistic actually consumed downstream, or source amplitude/placement information that forbids such charging.

## Strongest justified claim

ANF-157 writes bow variance exactly as positive Fejer source energy minus an endpoint-completion square. ANF-169 proves that target-sized completion forces one endpoint and one dyadic lag shell to satisfy a positive real shifted-correlation lower bound. ANF-170 gives the positive necessary witness `|S_H|^2 <= A Q_H`, while ANF-171 shows that `Q_H` can be critical and complex Cauchy--Schwarz nearly saturated even when the real alignment and endpoint completion are negligible.

ANF-172 restores phase information without abandoning positivity. For the endpoint Fejer family `F_L>=0`, with `T_L=L F_L` and `D_L=T_L-T_{L-1}`, one has exactly

`D_{2H}-D_H = 2 Re S_H`.

Thus the decision statistic is an adjacent-scale slope defect of positive short-window residual energies, not one energy value in isolation.

ANF-173 then removes the earlier upper-range artifact in exact-twist discorrelation. By choosing a sufficiently high but fixed Taylor degree, arbitrary fixed-log exact-twist cancellation extends over the full endpoint range `X^(5/8+eta) <= H <= K`. This still does not control completion. An adaptive carrier-faithful construction with amplitudes bounded by `rho_X` can store charge `asymp sqrt(X log X)` while every bounded-test correlation and every fixed-order normalized Gowers norm is at most `rho_X`, whenever `sqrt(X log X)/K=o(rho_X)`.

Hence a relative-uniformity-only architecture would need the genuinely power-scale tolerance `rho_X K=o(sqrt(X log X))`. Otherwise it must use additional physical source information, naturally the prime/rough amplitude and placement law.

## Synthesis of evidence

The sequence ANF-169--ANF-173 separates signed endpoint correlation, complex coherence, one-scale positive energy, coupled positive scale variation, and relative pseudorandomness. The first is consumed by the endpoint. The second and third can be large with the wrong phase. The fourth is an exact positive representation of the signed statistic. The fifth can hold over the complete endpoint horizon while a tiny coherent drift still builds dangerous memory.

For the physical residual `r_X=vartheta-Q_R`, the durable target is therefore either a source-faithful signed dyadic estimate, a coupled Fejer/Selberg scale-increment theorem at the required absolute scale, or a structural theorem preventing the adaptive charging mechanism. Stronger fixed-log or fixed-order uniformity without that scale conversion is no longer a plausible closure step.

## Counterevidence / boundary cases

ANF-171 and ANF-173 use matched synthetic packets/drifts, not the actual prime/rough residual. They prove that phase-blind energy and relative-uniformity hypotheses are insufficient abstractly, not that the physical source realizes the bad configurations.

ANF-172 is an exact reorganization, not evidence that the positive scale-increment formulation is analytically easier. Estimating `F_H` and `F_{2H}` separately with errors large relative to their difference can still lose the endpoint signal.

The lower activation boundary of the available all-interval theorem is not removed by ANF-173; what disappears is the artificial upper `X^(2/3)` ceiling from a low Taylor degree.

## Epistemic status

**Exact information boundary through ANF-173:** bow completion is controlled by a phase-sensitive absolute endpoint-memory statistic. It is exactly recoverable as a positive Fejer scale-slope defect, while single-scale energy and full-range fixed-order relative uniformity can both miss target-sized completion.

## Novelty/prior-art status

No independent novelty claim is made here. This intuition synthesizes persisted Mathia reductions and matched controls. Fejer/autocorrelation identities, polynomial-phase approximation, Gowers norms, and nilsequence discorrelation are treated according to the finding-level prior-art audits.

## Falsification criterion

Show that the ANF-172 scale-slope identity fails for the endpoint weights, or that ANF-173's carrier-faithful charging construction violates one of its stated relative-uniformity bounds. Strategically, a source theorem deriving `rho_X K=o(sqrt(X log X))` or directly controlling the scale-slope defect from existing prime/rough information would not falsify the intuition, but would close its stated missing gate.