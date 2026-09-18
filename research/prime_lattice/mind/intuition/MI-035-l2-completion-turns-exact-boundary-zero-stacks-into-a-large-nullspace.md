# MI-035 — ℓ² completion turns exact boundary-zero stacks into a large nullspace

**Evidence level:** supported synthesis from [PL-354](../../findings/PL-354-real-dirichlet-evaluation-stack-dense-or-zero.md), [PL-355](../../findings/PL-355-prime-l2-boundary-zero-stacks.md), and [PL-356](../../findings/PL-356-boundary-zero-stacks-finite-constraint-robustness.md). The zero-set theorem is classical Seip prior art; the Mathia content is the topology comparison and its consequence for the current Prime-Lattice escape.

PL-354 gives a sharp finite-support statement: finitely many exact positive-real Dirichlet evaluations remove no closed directions in the local completed form topology, while an infinite distinct exact stack annihilates every nonzero finite Dirichlet polynomial. That rigidity might suggest using infinitely many real evaluations as an intermediate source constraint.

PL-355 shows that the conclusion changes abruptly after completing the degree-one prime sector to

`P^2_0={sum_p c_p p^(-s): c in l2(P)}`.

Point evaluation is continuous exactly for `Re s>1/2`. A nonzero element cannot have real zeros accumulating in the interior or escaping to `+infinity`, so an infinite real zero stack can accumulate only at the boundary `1/2`. Classical Seip zero-set theory then shows that this escape is genuine: bounded real Blaschke stacks such as `1/2+2^(-j)` are zero sets of nontrivial pure-prime `l2` Dirichlet series.

The failure is not one-dimensional. PL-356 uses Seip's arbitrarily far tail-supported construction to produce infinitely many linearly independent vectors vanishing on the **same** stack. Therefore the common vanishing space remains infinite-dimensional after imposing any finite family of bounded homogeneous coefficient functionals. Finite low-prime exclusions, finitely many `l2` moments or finite orthogonality conditions cannot restore the finite-support stack rigidity.

The reproducing kernel of this completion is `K(s,w)=sum_p p^(-s-bar(w))`. On the logarithmic boundary scale `sigma_u=1/2+e^(-u)`, it has leading form `min(u,v)+O(1)`, the Brownian covariance kernel. This identifies the critical boundary as natural Hilbert geometry, but that geometry is already classical and permits arbitrary boundary interpolation; it is not zero selection.

The reusable lesson is that **exact constraint strength is topology-relative**. An infinite family can annihilate the algebraic finite-support class and still leave a huge nullspace in a natural completion. A viable Prime-Lattice repair must therefore specify the source topology and add a canonical coupling that Seip interpolation does not preserve: an infinite closed arithmetic relation, nonlinear/positivity structure, cross-degree Euler compatibility, target-relative coupling, or another constraint whose nontriviality is proved in the completed space.

**Boundary.** PL-355--PL-356 concern bounded real Blaschke stacks and the prime-supported `l2` first chaos. They do not classify arbitrary complex zero sets, affine or nonlinear constraints, or stronger source topologies. No relation between these freely interpolated zeros and the Riemann zero divisor is implied.