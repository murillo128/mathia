# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Break the matched Ford packet on the legal band, or produce a legal super-H carrier window

**Linked intuitions:** `MI-062-the-critical-ford-mark-is-a-growing-moment-observable`, `MI-063-demodulated-ford-energy-is-bandlimited-at-the-window-scale`.

NB-245--NB-249 fix the representation and order of operations. The Ford-scaled Cauchy pole must be Hardy-projected through the positive Mellin frequencies before any Hilbert-space squaring; this exactly recovers the finite depth-marked zero current and preserves its carrier phase. NB-250 then identifies the remaining second moment as a positive carrier-band form factor: after projection, the relevant Fourier variable samples physical frequencies in a band of natural width `Theta(H)=Theta(X/J)`, while pair phases still resolve ordinate differences at the finer `1/X` scale.

NB-251 sharpens what the standard matched coherent packet actually obstructs. A fixed `O(H)` carrier width leaves a positive normalized packet-energy floor, but the packet contribution tends to zero as soon as the available width satisfies `W/H -> infinity`; full `1/X`-cell orthogonality would require the much stronger `W` of order `X`. Thus the matched-packet obstruction ends already in an intermediate regime `H << W << X`.

The present source architecture, however, naturally supplies only `W=Theta(H)`. The live alternative is therefore exact: either prove zeta-specific off-diagonal cancellation for the Hardy-projected marked zero current on that legal `O(H)` band, despite the matched control packet, or exhibit a source-forced operation that legally thickens the carrier to `H << W << X` while preserving the Ford depth coefficients, selected-height localization and the projection-before-squaring order. Merely averaging farther in frequency is not admissible unless that enlarged band is produced by the source construction itself.

## Keep sufficient carrier-energy bounds separate from the actual zero theorem

The full-line carrier-band `L^2` estimate of NB-250 is a sufficient route to the hard-window bound, not an equivalence that may be assumed in reverse. NB-251 analyzes the matched packet, not arbitrary zeta-zero clustering, and therefore does not prove that super-H bandwidth is sufficient for the actual zero current. Any future argument must state which carrier interval is physically available and which pair-form-factor estimate is proved there; macroscopic averages, absolute local bounds for `zeta'/zeta`, or artificial frequency thickening lose the exact Ford interface.
