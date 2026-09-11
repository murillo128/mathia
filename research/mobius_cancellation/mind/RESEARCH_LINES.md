# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Prove source-forced cross-degree cancellation in the lifted square-defect channel

**Linked intuitions:** `MI-013-bost-connes-regularity-needs-an-intermediate-transverse-category`, `MI-014-centered-parity-and-zero-mode-are-separate-currencies`, `MI-015-sign-support-covariance-gives-a-conditioned-quadratic-bridge`, `MI-016-source-aligned-shifts-face-a-defect-or-mertens-dichotomy`.

MC-188--MC-215 show that canonical equivariant, CRT, character, support-shift, completion, and high-moment routes either stay sector-diagonal, collapse to sparse defects, reconstruct a principal mode at Mertens strength, or expose phases removable by residue relabeling.

MC-216 closes the cross-modulus version of the phase escape. The selected residues `-q mod d^2` form one coherent inverse-limit point, so a single compatible unit translation gauges all selected-character phases away simultaneously. Canonical reduction/CRT/push-pull structure does not restore the lost arithmetic sign.

MC-217 shows that the desired raw square-defect energy scale is not intrinsically impossible: a matched random multiplicative source with the same square-free support and lifted incidences has diagonal-scale shell energy in expectation and almost surely at dyadic scales.

MC-218 identifies why that comparator is too favorable. Actual Möbius has a coherent degree-one prime layer whose first-shell energy is polynomially larger than the target, whereas random prime signs cancel inside that layer. Reaching diagonal deterministic energy therefore requires the higher square-free degrees to cancel the coherent prime vector with relative weighted `L^2` error `X^(-1/2+o(1))`.

The live theorem is thus more precise than generic principal/transverse covariance: prove a **gauge-invariant, lifted cross-Hamming-degree cancellation law** forced by the actual Möbius source, and show that it is cheaper than reconstructing the principal Mertens mode.

## Treat residue gauge, random multiplicative calibration, and actual prime-layer coherence as separate controls

Cross-modulus character phases are still gauge. Generic random multiplicativity reaches the target scale for the wrong reason because it randomizes the coherent prime layer. A useful source theorem must preserve the lift `n+q=d^2m`, interval order, and deterministic all-prime sign while explaining cancellation between source degrees.