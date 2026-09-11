# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Beat the first square-defect shell through source-coupled signed family cancellation

**Linked intuitions:** `MI-013-bost-connes-regularity-needs-an-intermediate-transverse-category`, `MI-014-centered-parity-and-zero-mode-are-separate-currencies`, `MI-015-sign-support-covariance-gives-a-conditioned-quadratic-bridge`, `MI-016-source-aligned-shifts-face-a-defect-or-mertens-dichotomy`, `MI-017-first-shell-crt-common-mode-is-a-source-coupled-energy-coordinate`.

MC-188--MC-221 show that residue phases are gauge, fixed square-free Hamming degrees form an alternating cascade, and the first shell ultimately needs square-root-scale parity balance across the moving degree range of a nearly quadratic unsigned population.

MC-222 gives the conditional benchmark: Dirichlet-GRH-quality cancellation for each selected progression closes the first shell, while the primorial roughness itself costs only subpower after the exact semigroup reduction. MC-223--MC-227 close weaker replacements: sparse exceptional sectors, coefficient-uniform large-sieve/BDH bounds, and fiberwise estimates do not recover the missing power because they discard the source-selected coupling.

MC-228 now identifies one such coupling exactly. All selected square-modulus supports share the same CRT progression `n=kQ_y-P`; its cardinality is `X^(1-2c+o(1))/log y`, and for `c<1/4` almost all common points are square-free. Writing `A_d=C_y+B_d` exposes one signed scalar `C_y` copied into every shell coordinate. Estimating that common block independently is target-scale harmless only for `c>=1/4`; below `1/4`, support bounds alone lose a fixed power.

The live theorem below `c=1/4` must therefore exploit the deterministic parity of the common CRT block or its coherent interference with the residual vectors. The matched independent prime-sign control already has sub-target expected common energy, so common incidence itself is not the obstruction. A useful estimate must distinguish the actual all-minus Möbius source from that control without reverting to GRH-strength bounds for every character.

## Treat gauge, family averaging, common-mode parity, and common/residual interference as separate gates

Residue phases are gauge; fixed-degree asymptotics do not control the moving population; GRH-strength characterwise bounds are sufficient but too strong for an RH-directed proof; sparse-exception and generic large-sieve averaging are quantitatively insufficient. MC-228 adds a sharper split: the shell contains an exact source-forced common coordinate, but controlling it separately can itself be too expensive. The remaining currency is a signed source theorem that acts before the decomposition is made phase-blind or orthogonal.
