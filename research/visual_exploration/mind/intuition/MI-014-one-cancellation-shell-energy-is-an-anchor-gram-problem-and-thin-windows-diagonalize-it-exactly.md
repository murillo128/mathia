# MI-014 — One-cancellation shell energy is a coupled positive anchor-Gram problem

**Evidence level:** supported by VIS-204 and [VIS-209](../../findings/VIS-209-one-cancellation-shell-anchor-gram-kernel.md). The former VIS-210 thin-window diagonalization is withdrawn and supplies no current evidence. No uniform spectral-concentration estimate is claimed.

After the noncancelling determinant band is removed in start-averaged energy, VIS-209 identifies the first surviving one-cancellation layer with one positive semidefinite anchor Gram kernel. If `G` is the Gram matrix of the prime-anchor profiles, then

`E_1 = 4[tr(G^2)-sum_u G_(u,u)^2]`.

This is the durable structural reduction. Raw shell multiplicity is not the correct object; the endpoint is the off-diagonal concentration of the actual prime-ratio kernel. Any useful bound must retain the real anchor couplings rather than replace them by an unsupported finite-support picture.

The previously stored claim that a thin-window cone makes distinct shell supports exactly disjoint depended on VIS-210. That finding has been withdrawn, so exact diagonalization, the six-anchor support model and its claimed `6/5` resonance are no longer part of the current mind. They cannot be used to reduce `||G||_op` to its largest diagonal entry.

The current exact kernel remains sufficiently structured to support narrower questions. For the autocorrelation taper, the positive symmetric anchor matrix has entries of the form

`Psi_(u,t)=Q_y^(-1)(ut)^(-alpha) rho(H log(u/t))`.

VIS-209 makes its operator concentration the relevant quantity. A proposed weighted-Schur reduction in the local clue inbox gives one possible route, but its required uniform prime-window estimate is not established and therefore is not promoted here.

The live theorem is to control the coupled anchor kernel itself—by a valid Schur estimate, spectral spreading, sparse-window analysis, or a counterexample showing concentration at a particular anchor scale—while preserving the actual prime-ratio geometry and the start-averaged sinc weighting already proved upstream.

**Boundary.** This note records the surviving exact Gram reduction after the VIS-210 withdrawal. It does not assert the proposed Schur asymptotic, effective rank, diagonal dominance, or uniform-in-start control.