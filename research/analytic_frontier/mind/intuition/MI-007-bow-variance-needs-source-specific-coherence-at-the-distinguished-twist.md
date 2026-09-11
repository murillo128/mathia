# MI-007 — Bow completion is an absolute, phase-sensitive endpoint-memory problem

**Evidence level:** supported

## Core intuition

The bow endpoint obstruction is not determined by moving-window energy, qualitative relative uniformity, coefficient quantization, or support sparsity. Target-sized completion forces a large **positive real** dyadic shifted correlation at the distinguished logarithmic twist. That signed shell can be represented exactly as a dyadic scale-slope defect of a positive endpoint Fejer family, but controlling the individual positive energies or ordinary relative correlations is not enough.

A coherent carrier-aligned drift can be implemented either by tiny amplitudes on many sites or by fixed unit amplitudes on a sparse carrier-selected set. In both cases the endpoint primitive can accumulate charge `asymp sqrt(X log X)` and remember it after charging stops. The final theorem therefore needs absolute precision in the signed/scale-difference statistic actually consumed downstream, or source information that constrains where prime/rough residual mass may occur relative to the carrier.

## Strongest justified claim

ANF-157 writes bow variance exactly as positive Fejer source energy minus an endpoint-completion square. ANF-169 proves that target-sized completion forces one endpoint and one dyadic lag shell to satisfy a positive real shifted-correlation lower bound. ANF-170 gives the positive necessary witness `|S_H|^2 <= A Q_H`, while ANF-171 shows that `Q_H` can be critical and complex Cauchy--Schwarz nearly saturated even when the real alignment and endpoint completion are negligible.

ANF-172 restores phase information without abandoning positivity. For the endpoint Fejer family `F_L>=0`, with `T_L=L F_L` and `D_L=T_L-T_{L-1}`, one has exactly

`D_{2H}-D_H = 2 Re S_H`.

Thus the decision statistic is an adjacent-scale slope defect of positive short-window residual energies, not one energy value in isolation.

ANF-173 removes the earlier upper-range artifact in exact-twist discorrelation. By choosing a sufficiently high but fixed Taylor degree, arbitrary fixed-log exact-twist cancellation extends over the full endpoint range `X^(5/8+eta) <= H <= K`. It also constructs a carrier-faithful dangerous charge using amplitudes bounded by `rho_X`, proving that bounded-test relative decorrelation and every fixed-order Gowers norm can be at most `rho_X` while completion remains target-sized whenever `sqrt(X log X)/K=o(rho_X)`.

ANF-174 shows that continuously tunable small amplitudes are not needed. Choose a coarse grid spacing `q->infinity` with `q sqrt(X log X)=o(K)`, partition the exact carrier rays on its first `O(sqrt(X log X))` sites into six sectors, and retain the sites in one populated sector. With amplitudes only in `{0,1}`, the selected rays already accumulate critical charge. The support is a subset of `q Z`, so every bounded-test relative correlation on intervals of length `H` is at most `q^{-1}+H^{-1}`, while every fixed-order Gowers norm is `O_s((q^{-1}+H^{-1})^{1/2^s})`. Taking `q=X^gamma` gives power decay for both classes of generic uniformity statistics, yet the endpoint completion and Fejer scale-slope defect remain target-sized.

Hence neither a nonzero amplitude floor, a finite alphabet, nonnegative amplitudes, nor vanishing support density closes the information gap. The surviving missing input is the **joint arithmetic placement law** of the physical residual `r_X=vartheta-Q_R` relative to the distinguished carrier, or a theorem that directly controls the equivalent signed dyadic/Fejer statistic at the required absolute scale.

## Synthesis of evidence

The sequence ANF-169--ANF-174 separates signed endpoint correlation, complex coherence, one-scale positive energy, coupled positive scale variation, relative pseudorandomness, and coefficient/occupancy rigidity. The endpoint consumes the first. The second and third can be large with the wrong phase. The fourth exactly recovers the signed statistic from positive energies. The fifth can hold over the complete endpoint horizon while a small coherent drift builds dangerous memory. The sixth still does not help abstractly, because sparse unit occupancy can emulate that drift with power-small long-interval statistics.

For the physical residual, the durable target is therefore either a source-faithful signed dyadic estimate, a coupled Fejer/Selberg scale-increment theorem at the required absolute scale, or a structural theorem forbidding carrier-sector-biased placement of prime/rough residual mass. Stronger fixed-log or fixed-order uniformity, amplitude discretization, and sparsity without that placement information are no longer plausible closure steps.

## Counterevidence / boundary cases

ANF-171, ANF-173, and ANF-174 use matched synthetic packets rather than the actual prime/rough residual. They prove that phase-blind energy, relative-uniformity hypotheses, and generic amplitude/sparsity restrictions are insufficient abstractly; they do **not** show that the physical source realizes the bad configurations.

ANF-174's sparse support is selected adversarially after inspecting the exact carrier phase. This is precisely the freedom the next source theorem is expected to remove. The result therefore sharpens the frontier toward placement arithmetic rather than arguing against such a theorem.

ANF-172 is an exact reorganization, not evidence that the positive scale-increment formulation is analytically easier. Estimating `F_H` and `F_{2H}` separately with errors large relative to their difference can still lose the endpoint signal.

The lower activation boundary of the available all-interval theorem is not removed by ANF-173; what disappears is the artificial upper `X^(2/3)` ceiling from a low Taylor degree.

## Epistemic status

**Exact information boundary through ANF-174:** bow completion is controlled by a phase-sensitive absolute endpoint-memory statistic. It is exactly recoverable as a positive Fejer scale-slope defect, while single-scale energy, full-range fixed-order relative uniformity, amplitude quantization, nonnegative unit coefficients, and vanishing support density can all miss target-sized completion. The remaining generic freedom is carrier-adapted placement; the physical source must be distinguished there.

## Novelty/prior-art status

No independent novelty claim is made here. This intuition synthesizes persisted Mathia reductions and matched controls. Fejer/autocorrelation identities, polynomial-phase approximation, Gowers norms, nilsequence discorrelation, and sparse-support estimates are treated according to the finding-level prior-art audits.

## Falsification criterion

Show that the ANF-172 scale-slope identity fails for the endpoint weights, that ANF-173's adaptive charging construction violates one of its stated relative-uniformity bounds, or that ANF-174's sparse `{0,1}` construction violates its interval-count/Gowers estimates. Strategically, a source theorem that rules out carrier-sector-biased placement for `vartheta-Q_R`, or directly proves the required absolute scale-slope bound, would not falsify the intuition; it would close its stated missing gate.