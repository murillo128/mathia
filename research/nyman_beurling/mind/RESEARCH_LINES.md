# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Break the matched Ford packet on the legal band, or create bandwidth that is super-H without renormalizing H

**Linked intuitions:** `MI-062-the-critical-ford-mark-is-a-growing-moment-observable`, `MI-063-demodulated-ford-energy-is-bandlimited-at-the-window-scale`.

NB-245--NB-249 fix the representation and order of operations. The Ford-scaled Cauchy pole must be Hardy-projected through the positive Mellin frequencies before any Hilbert-space squaring; this exactly recovers the finite depth-marked zero current and preserves its carrier phase. NB-250 then identifies the remaining second moment as a positive carrier-band form factor: after projection, the relevant Fourier variable samples physical frequencies in a band of natural width `Theta(H)=Theta(X/J)`, while pair phases still resolve ordinate differences at the finer `1/X` scale.

NB-251 sharpens what the standard matched coherent packet actually obstructs. A fixed `O(H)` carrier width leaves a positive normalized packet-energy floor, but the packet contribution tends to zero as soon as the available width satisfies `W/H -> infinity`; full `1/X`-cell orthogonality would require the much stronger `W` of order `X`. Thus the matched-packet obstruction ends already in an intermediate regime `H << W << X`.

NB-252 closes the literal single-shell dilation as a way to reach that regime. Replacing the shell width by `H_B=B_J H` also changes the source parameter to `J_B=R/H_B=J/B_J`. For `1<<B_J<<J`, the new legal carrier still has width only `Theta(H_B)` relative to its own scale, contains a matched packet with `Theta(J_B)` points, and retains a positive normalized energy floor. The Ford depth coordinate merely shifts by `log B_J`; the critical layer is transported rather than removed. Single-shell dilation is therefore scale-covariant, not a source-forced super-`H` bandwidth gain.

The live alternative is now narrower: either prove zeta-specific off-diagonal cancellation for the Hardy-projected marked zero current on the legal `O(H)` band, despite the matched control packet, or construct a genuinely different source operation—such as a multi-carrier or multi-shell architecture—whose support width grows superlinearly relative to a fixed underlying `H,J` normalization while preserving the Ford depth coefficients, selected-height localization and projection-before-squaring order. Merely redefining the shell scale does not qualify.

## Keep sufficient carrier-energy bounds separate from the actual zero theorem

The full-line carrier-band `L^2` estimate of NB-250 is a sufficient route to the hard-window bound, not an equivalence that may be assumed in reverse. NB-251 analyzes the matched packet, not arbitrary zeta-zero clustering, and NB-252 only proves scale covariance of a particular dilation. A future argument must state which carrier interval is physically generated, which shell normalization remains fixed, and which pair-form-factor estimate is proved there; macroscopic averages, absolute local bounds for `zeta'/zeta`, artificial frequency thickening, or a relabeling of `H` lose the exact Ford interface.
