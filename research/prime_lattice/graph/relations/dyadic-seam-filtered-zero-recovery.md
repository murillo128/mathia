---
id: RG-dyadic-seam-filtered-zero-recovery
type: research-graph-relation
scope: prime_lattice
derived: true
---

# Dyadic seam filtering and arithmetic pole recovery

[[research/prime_lattice/graph/prime-lattice|Prime Lattice]] · [[research/prime_lattice/graph/relations/mod5-window-moment-zero-free-prerequisites|Mod-5 moment prerequisites]]

This projects PL-466's explicit dependencies and conditional improvement. All estimates concern the identity-residue von Mangoldt windows modulo 5, their own empirical means, and the full base-point integral at every sufficiently large dyadic scale. The variance premise remains unproved.

## Sharp blocks, smooth weights, and retained means

[[research/prime_lattice/findings/PL-464-dyadic-empirical-variance-residue-rigidity|PL-464]] derives the boundary `max(1-theta/2, theta)` from dyadic empirical variance `V_j << X_j H_j (log X_j)^A`, with fixed `0<theta<1`, finite `A>=0`, `X_j=2^j`, and `H_j=floor(X_j^theta)`. Its sharp-block error costs `H_j log X_j`. Periodicity of the unknown block-mass factor and the real, noncancelling arithmetic residues exclude poles without a density theorem. Its endpoint cost is not asserted optimal.

[[research/prime_lattice/findings/PL-465-relative-frame-transfers-dirichlet-zero-bounds|PL-465]], Section 2, supplies the finite differential inversion of a box average used in [[research/prime_lattice/findings/PL-466-dyadic-seam-weights-remove-the-variance-endpoint-loss|PL-466]], equations (5)–(8). This dependency concerns the local inversion calculation; PL-466 does not assume PL-465's relative covariance frame.

PL-466 chooses `q_m(t)=(1-cos(2 pi t/log 2))^m` and tests `q_m(log u)u^(-s)` on `[1,2]`. Vanishing endpoint jets keep the differential inverse supported inside the available base-point interval. For fixed `N(1-theta)>theta/2` and `2m>N`, the remainder is below the variance exponent `alpha=1-theta/2`. The empirical mean is retained as a periodic meromorphic factor, not estimated or discarded.

## Two arithmetic sparsity steps

Equations (11)–(16) in PL-466 decompose the finite vertical-shift filter `D_m` as an entire term plus `J_m F+G`, where `G` is holomorphic to the right of `alpha` and `J_m` has no zeros in `Re s<1`. A pole of periodic `F` in `alpha<Re s<1` would force linearly many filtered poles. The [[research/prior_art/incremental/PA-montgomery-dirichlet-zero-density-bound|classical Dirichlet zero-density bound]] permits only `o(T)` and excludes this.

Filtered holomorphy alone could hide poles of the original `D`. Equations (17)–(20) recover them: the residue sequence on every vertical progression has vanishing finite difference of order `2m`, hence is polynomial; its `o(K)` support forces it to vanish. Identity-residue multiplicities all have the same sign, so a zero cannot cancel between character channels. This gives zero exclusion in `Re s>1-theta/2`, improving PL-464 for `theta>2/3`.

PL-466's positive dyadic density control still satisfies the variance ceiling but has a complete progression of Mellin poles. It fails the arithmetic sparsity input; it is not a counterexample to the prime-specific conditional theorem. No sharp block-mass recovery, covariance estimate, boundary-line exclusion, or GRH converse is supplied.

## Scoped comparison with the Möbius transfer

PL-466 explicitly cites [[research/mobius_cancellation/findings/MC-521-smooth-deconvolution-removes-the-variance-zero-free-boundary-loss|MC-521]] for the finite-deconvolution perspective, while excluding its all-real-scale Mellin integral from this proof. MC-521 uses an uncentered all-scale moment and a nonmasking smooth test family; its Section 4 additionally recovers an epsilon-loss sharp Mertens bound through reciprocal-zeta growth and Perron. That is not a transfer of the dyadic empirically centered premise, nor a sharp-recovery conclusion of PL-466. [[research/prime_lattice/mind/intuition/MI-065-seam-filtering-recovers-sparse-arithmetic-poles-from-dyadic-variance|MI-065]] preserves the dyadic distinction.

Classical density and deconvolution tools do not prove either arithmetic variance input. This is one conditional refinement of the dyadic zero-free transfer, not an unconditional zero-free gain or an external novelty claim.
