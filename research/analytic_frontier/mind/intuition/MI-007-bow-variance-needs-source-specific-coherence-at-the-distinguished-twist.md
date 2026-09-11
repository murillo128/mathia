# MI-007 — Bow completion is an absolute, phase-sensitive endpoint-memory problem

**Evidence level:** supported

## Core intuition

The bow endpoint obstruction is not determined by moving-window energy, qualitative relative uniformity, coefficient quantization, support sparsity, or an activation exponent considered in isolation. Target-sized completion forces a large **positive real** dyadic shifted correlation at the distinguished logarithmic twist. That signed shell can be represented exactly as a dyadic scale-slope defect of a positive endpoint Fejer family, but controlling the individual positive energies or ordinary relative correlations is not enough.

A coherent carrier-aligned drift can be implemented by tiny amplitudes on many sites, by unit amplitudes on a sparse carrier-selected set, or by prime-sized `log X` atoms at prime-scale density. In the last form the critical charge `asymp sqrt(X log X)` is assembled on the sharp physical scale `asymp sqrt(X log X)` and the whole dangerous packet has only that much total absolute mass. The final theorem therefore needs absolute precision in the signed/scale-difference statistic actually consumed downstream, or source information that constrains where prime/rough residual mass may occur relative to the carrier.

## Strongest justified claim

ANF-157 writes bow variance exactly as positive Fejer source energy minus an endpoint-completion square. ANF-169 proves that target-sized completion forces one endpoint and one dyadic lag shell to satisfy a positive real shifted-correlation lower bound. ANF-170 gives the positive necessary witness `|S_H|^2 <= A Q_H`, while ANF-171 shows that `Q_H` can be critical and complex Cauchy--Schwarz nearly saturated even when the real alignment and endpoint completion are negligible.

ANF-172 restores phase information without abandoning positivity. For the endpoint Fejer family `F_L>=0`, with `T_L=L F_L` and `D_L=T_L-T_{L-1}`, one has exactly

`D_{2H}-D_H = 2 Re S_H`.

Thus the decision statistic is an adjacent-scale slope defect of positive short-window residual energies, not one energy value in isolation.

ANF-173 removes the earlier upper-range artifact in exact-twist discorrelation. By choosing a sufficiently high but fixed Taylor degree, arbitrary fixed-log exact-twist cancellation extends over the full endpoint range `X^(5/8+eta) <= H <= K`. It also constructs a carrier-faithful dangerous charge using amplitudes bounded by `rho_X`, proving that bounded-test relative decorrelation and every fixed-order Gowers norm can be at most `rho_X` while completion remains target-sized whenever `sqrt(X log X)/K=o(rho_X)`.

ANF-174 shows that continuously tunable small amplitudes are not needed. A carrier-selected sparse packet with amplitudes only in `{0,1}` can accumulate critical charge while every bounded-test relative correlation and every fixed-order Gowers norm is power-small on long intervals. ANF-175 then removes the sparse one-point-scale mismatch: atoms of magnitude `log X` at candidate spacing `log X` obey the local envelope `O(H+log X)`, which both forces and permits the critical charge to be assembled at physical length `Theta(sqrt(X log X))`. The packet's total `l^1` mass is only `O(sqrt(X log X))`, yet holding that charge for `Theta(K)` prefixes creates target-sized completion and the Fejer defect.

ANF-176 converts that observation into a general activation-saving boundary. If a theorem activates at `H_0=X^(theta+o(1))` and its admissible error at that scale is `H_0 X^(-sigma+o(1))`, then the ANF-175 packet is invisible whenever `theta-sigma>1/2`. The exact criterion is whether the first controlled absolute error is above or below `sqrt(X log X)`; slowly varying factors decide the critical line. Hence arbitrary fixed-log savings cannot compensate for any fixed power activation gap above one half. At `5/8`, roughly an `X^(-1/8)` relative power saving is needed to cross the packet scale; at the actual `sqrt(X log X)` loading scale any genuine `o(1)` relative saving does.

Hence neither a nonzero amplitude floor, a finite alphabet, nonnegative amplitudes, prime-sized one-point marginals, vanishing support density, nor exponent-only progress above one half closes the information gap. The surviving missing input is the **joint arithmetic placement law** of the physical residual `r_X=vartheta-Q_R` relative to the distinguished carrier, or a theorem whose absolute error / Fejer slope control crosses the critical memory scale.

## Synthesis of evidence

The sequence ANF-169--ANF-176 separates signed endpoint correlation, complex coherence, one-scale positive energy, coupled positive scale variation, relative pseudorandomness, coefficient/occupancy rigidity, prime-scale marginals, and activation-error strength. The endpoint consumes the first. Complex coherence and one-scale energy can be large with the wrong phase. Coupled positive scale variation exactly recovers the signed statistic. Relative pseudorandomness, amplitude quantization, sparsity, and even prime-scale magnitude/density can all coexist with target-sized stored memory. ANF-176 shows why: once the dangerous packet's entire mass is `asymp sqrt(X log X)`, any theorem whose smallest allowed absolute error remains larger than that cannot see it regardless of how sophisticated the bounded test class is.

For the physical residual, the durable target is therefore either a source-faithful signed dyadic estimate, a coupled Fejer/Selberg scale-increment theorem at the required absolute scale, or a structural theorem forbidding carrier-sector-biased placement of prime/rough residual mass. Activation and saving should be evaluated jointly through `rho_X H_0` rather than separately.

## Counterevidence / boundary cases

ANF-171 and ANF-173--ANF-176 use matched synthetic packets rather than the actual prime/rough residual. They prove that phase-blind energy, relative-uniformity hypotheses, generic amplitude/sparsity restrictions, prime-sized marginals, and certain activation-error profiles are insufficient abstractly; they do **not** show that the physical source realizes the bad configurations.

The carrier-selected packets are adversarially placed after inspecting the exact logarithmic phase. This is precisely the freedom the next source theorem is expected to remove. The results therefore sharpen the frontier toward placement arithmetic rather than arguing against such a theorem.

ANF-176 is one-way. An error allowance `o(sqrt(X log X))` rules out the persisted ANF-175 packet at controlled scales, but by itself does not prove the full bow estimate; uncontrolled shorter prefixes and the exact signed scale-difference statistic still need accounting.

ANF-172 is an exact reorganization, not evidence that the positive scale-increment formulation is analytically easier. Estimating `F_H` and `F_{2H}` separately with errors large relative to their difference can still lose the endpoint signal.

## Epistemic status

**Exact information boundary through ANF-176:** bow completion is controlled by a phase-sensitive absolute endpoint-memory statistic. It is exactly recoverable as a positive Fejer scale-slope defect. Matched controls with prime-sized atoms and density can load the critical memory `sqrt(X log X)` on the sharp near-square-root scale while passing every bounded-test estimate whose first allowed absolute error is asymptotically larger. In power coordinates `(theta,sigma)`, this blind region is `theta-sigma>1/2`, with subpower factors deciding the boundary. The remaining generic freedom is carrier-adapted placement; the physical source must be distinguished there.

## Novelty/prior-art status

No independent novelty claim is made here. This intuition synthesizes persisted Mathia reductions and matched controls. Fejer/autocorrelation identities, polynomial-phase approximation, Gowers norms, nilsequence discorrelation, short-interval prime exponents, and sparse-support estimates are treated according to the finding-level prior-art audits.

## Falsification criterion

Show that the ANF-172 scale-slope identity fails for the endpoint weights, that the ANF-175 prime-scale packet violates its local marginal or total-mass estimates, or that the ANF-176 comparison `B_X(H_0)` versus `sqrt(X log X)` fails for that packet. Strategically, a source theorem that rules out carrier-sector-biased placement for `vartheta-Q_R`, or directly proves the required absolute scale-slope bound, would not falsify the intuition; it would close its stated missing gate.