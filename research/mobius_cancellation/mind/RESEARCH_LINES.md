# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Prove moving-degree parity balance on the first square-defect shell

**Linked intuitions:** `MI-013-bost-connes-regularity-needs-an-intermediate-transverse-category`, `MI-014-centered-parity-and-zero-mode-are-separate-currencies`, `MI-015-sign-support-covariance-gives-a-conditioned-quadratic-bridge`, `MI-016-source-aligned-shifts-face-a-defect-or-mertens-dichotomy`.

MC-188--MC-218 show that canonical residue/character structure is gauge or principal-mode information and that random multiplicativity reaches the desired shell scale for the wrong reason: it randomizes the coherent prime layer.

MC-219--MC-220 show that no fixed collection of square-free Hamming degrees repairs actual Möbius. Degree two overcompensates degree one by `~loglog X`, and every fixed degree is eventually overrun by the next; each fixed signed truncation is asymptotically dominated by its last term.

MC-221 identifies the full burden. The selected shell contains unsigned square-free energy `X^(2-o(1))`, whereas the desired signed energy is only `X^(1+o(1))`. The live theorem is therefore a **moving-degree parity-balance law** for `omega(n)` in the source-selected congruence classes, preserving `n+q=d^2m` and interval order, strong enough to produce square-root-scale cancellation.

## Treat residue gauge, fixed-degree asymptotics, and moving-degree parity as separate gates

Residue phases are gauge; low Hamming degrees form an alternating cascade rather than a cancellation mechanism; and the target lives in the parity balance of the complete square-free population. A useful source theorem must be uniform through the moving degree range where that population concentrates.
