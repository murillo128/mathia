# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Control singleton and low/mesoscopic exact incidence cells by nontrivial Möbius parity

**Linked intuitions:** `MI-013-bost-connes-regularity-needs-an-intermediate-transverse-category`, `MI-014-centered-parity-and-zero-mode-are-separate-currencies`, `MI-015-sign-support-covariance-gives-a-conditioned-quadratic-bridge`, `MI-016-source-aligned-shifts-face-a-defect-or-mertens-dichotomy`, `MI-017-first-shell-crt-common-mode-is-a-source-coupled-energy-coordinate`.

MC-188--MC-227 show that residue phases are gauge, fixed square-free Hamming degrees form an alternating cascade, and GRH-strength progression bounds are sufficient but too strong; sparse exceptions, generic large-sieve/BDH estimates, and fiberwise control lose the source-selected coupling.

MC-228--MC-229 localize the support obstruction across shell incidence. Above one quarter of `log X/loglog X`, support alone makes the separately controlled weighted energy target-scale harmless.

MC-230 then partitions the source by exact incidence set `S` and shows

\[
W_y(X)\le X^{o(1)}\sum_S w(S)|C_S(X)|^2.
\]

Because the whole cell alphabet has only `X^{o(1)}` elements, fixed-power progress does not require anti-alignment between different exact cells. The sufficient source theorem is aggregate signed control inside the low/mesoscopic cells.

MC-231 sharpens the bottom of that range. Exact singleton cells retain asymptotically all nonzero support of each first-shell coordinate and reproduce the full unsigned power scale, so the hard source problem is already present at incidence one. But the most direct multiplicative parity mechanism is unavailable: two points in the same singleton cell related by divisibility must have ratio `1 mod d^2`, hence a multiplicative jump at least `d^2+1`; any disjoint sign-reversing divisibility pairing can touch only a vanishing fraction of the singleton support.

The live theorem must therefore explain Möbius cancellation among mostly divisibility-incomparable singleton inputs, use additive/bilinear/harmonic source information, or provide another exact-cell mechanism not reducible to same-cell multiplication. Mesoscopic cells remain part of the sufficient diagonal target, but combinatorial cell entropy and cross-cell anti-alignment are no longer the primary obstruction.

## Treat gauge, incidence support, cell entropy, and internal parity geometry as separate gates

High incidence is cheap by support; the full exact-cell alphabet costs only a subpower factor; and singleton cells already carry near-full unsigned coordinate mass. A viable parity mechanism must act inside that low-incidence geometry. Simple factor insertion/removal while preserving the source-selected residue cannot reach most of the mass.
