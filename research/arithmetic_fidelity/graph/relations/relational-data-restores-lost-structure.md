---
id: RGR-AF-RELATIONAL-001
type: research-graph-relation
scope: arithmetic_fidelity
relation: relational-recovery-examples
derived: true
---

# Relational data can restore structure lost by scalar or marginal compression

The early exact models already show that relational observables can restore information discarded by lower-order or separately scalar summaries. [[research/arithmetic_fidelity/findings/AF-004-third-order-coupling-repairs-quadratic-phase-loss|AF-004]] repairs Fourier-magnitude phase loss with third-order coupling, while [[research/arithmetic_fidelity/findings/AF-006-marked-hermitian-spectra-classified-by-eigenspace-gram-data|AF-006]] shows that per-eigenspace Gram data restore geometry lost by separately marked scalar spectral measures.

The newer measure-theoretic classification makes the coupling loss exact. [[research/arithmetic_fidelity/findings/AF-031-complete-marginals-forget-coupling-joint-tests-recover-feature-law|AF-031]] factors complete marginals through the joint feature law and identifies the quotient `ker M_Phi / ker J_Phi` as the precise coupling-defect space. Complete one-coordinate observables determine only the marginal laws; complete joint observables determine the joint pushforward, and that joint law is fully source-faithful exactly when the combined feature map is injective.

[[research/arithmetic_fidelity/findings/AF-032-k-way-marginals-retain-exactly-low-degree-walsh-interactions|AF-032]] resolves the finite Boolean model by interaction order: all marginals of order at most `k` retain exactly the Walsh sectors of degree at most `k`, while every higher interaction lies in the kernel and admits genuine probability collisions. [[research/arithmetic_fidelity/findings/AF-033-marginal-scenarios-form-a-simplicial-fidelity-lattice|AF-033]] generalizes this from uniform `k`-marginals to arbitrary coordinate-marginal scenarios, whose exact information state is the downward-closed simplicial complex of retained faces.

These findings support a precise local principle, not a universal transfer theorem: **separate channels may each be complete while their coupling remains absent, and adding relational observables is useful only when it removes an explicitly identified kernel.** No direct claim about Prime Circle, Prime Lattice, or another application line is asserted without its own source-level fiber calculation.
