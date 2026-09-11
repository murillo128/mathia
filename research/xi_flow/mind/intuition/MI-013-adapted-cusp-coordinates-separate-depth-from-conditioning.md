# MI-013 — Adaptive Xi recovery separates depth, inverse conditioning, and the acquisition category

**Evidence level:** proved local finite-packet geometry and holomorphic linearized acquisition; global source coercivity remains open

## Core intuition

Remote packet location is not a fundamental instability of the finite Xi inverse. For fixed packet complexity, adapted cusp coordinates make the exact local inverse well conditioned. Positive-real heat acquisition does have a sharp graded visibility loss, and relative normalization removes it only at exponential absolute cost. But the holomorphic Jacobi source has another degree of freedom: complex phase can resolve the packet without attenuating its remote carrier.

The durable separation is now fourfold: **adaptive depth, inverse coordinates, acquisition category, and global source control**.

## Strongest justified claim

XF-177--XF-182 show that fixed real-axis topologies can miss sufficiently complex remote surgery, that `m` moved atom pairs require exactly cusp depth `m`, and that orthogonal packet-adapted coordinates remove remote-index conditioning from the exact inverse. On raw positive heat, however, the adapted modes appear with visibility `N^-1,...,N^-m`.

XF-183 proves this ladder belongs to the acquisition normalization rather than the packet inverse. At packet-width real scale, division by the positive reference packet heat mass cancels the common remote factor and leaves a uniformly conditioned relative map. The price is explicit: the reference mass itself is `exp(-Theta(N))`, so an additive absolute estimate would need exponentially small error to recover the relative observable.

XF-184 changes the information model instead of renormalizing. Choose complex samples with `Re x~N^-2` and `Im x~N^-1`. The real part keeps the Gaussian carrier at fixed modulus while the imaginary part gives order-one relative phases across the packet. A boundedly normalized finite acquisition bank converges to the DFT and has condition number tending to one, uniformly in the remote index; the reciprocal Jacobi image is exponentially negligible.

Thus the positive-real polynomial/exponential tradeoff is not an information-theoretic obstruction for the holomorphic Jacobi source.

## Synthesis of evidence

For fixed `m`, local linear acquisition of a known remote packet is now essentially solved in the complex domain. The next theorem should not seek another preconditioner. It should transport this local mechanism into the actual infinite/source problem: unknown support, nonlinear displacement, growing packet complexity, and the analytic bounds needed to sample the physical Xi/Jacobi object at the required mesoscopic complex points.

A future obstruction must also be category-aware. Showing instability on the positive real axis no longer rules out the holomorphic source. Conversely, complex samples are useful only if the downstream theorem can control them without importing zero information equivalent to the target.

## Counterevidence / boundary cases

XF-184 is linearized, finite-packet, and packet-adapted. The sampling bank depends on the packet scale and does not solve support discovery or a global infinite deformation. Nonlinear neighborhoods may shrink with complexity, and uniformity as `m` grows is not established.

Allowing complex Jacobi samples may make analytic control substantially harder. Uniform conditioning of the finite acquisition matrix does not itself supply bounds for the true source at those points.

## Epistemic status

**Exact local acquisition boundary:** depth `m` remains sharp, the exact inverse can be well conditioned, positive-real acquisition has a graded/exponential tradeoff, and mesoscopic complex Jacobi phase removes that remote packet loss for fixed complexity. The remaining problem is global source coercivity and complexity growth.

## Novelty/prior-art status

Moment inversion, orthogonal preconditioning, Fourier/DFT resolution, and holomorphic heat kernels are classical mechanisms. The persisted findings record their exact Xi/Jacobi specialization; this intuition synthesizes the category boundary.

## Falsification criterion

Invalidate the XF-184 uniform singular-value bounds or show that the reciprocal Jacobi image reintroduces a remote loss at the stated complex samples. Strategically, prove a nonlinear growing-complexity source theorem using the complex acquisition bank; that would cross the current gate.

## Lean-formalizable core

For fixed finite packets, the adapted-coordinate identities and the asymptotic DFT acquisition matrix reduce to finite linear algebra plus elementary exponential estimates.