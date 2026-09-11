# MI-013 — Adaptive Xi recovery separates required depth from coordinate conditioning

**Evidence level:** proved local finite-packet geometry; global source acquisition remains open

## Core intuition

Remote atom location is not the fundamental instability in finite Xi source surgery, and even the exponential conditioning seen in monomial moment coordinates is not intrinsic. Once the packet size `m` and reference packet are known, the first `m` Jacobi cusp derivatives contain exactly enough information, and an adapted orthogonal-polynomial basis can make the local inverse infinitesimally isometric.

The irreducible cost is therefore **adaptive complexity depth and acquisition**, not a fixed remote-index penalty or unavoidable local Vandermonde condition number.

## Strongest justified claim

XF-177--XF-178 show that every fixed power-weighted real-axis topology can be fooled by sufficiently high-order moment-balanced remote surgery. No fixed-complexity seminorm is coercive on the full finite-surgery class.

XF-179 identifies the exact adaptive threshold. If exactly `m` positive unit-mass atom pairs are moved, the cusp jet through order `m` determines the surgery, while depth `m-1` is sharp. The obstruction is therefore tied to packet complexity.

XF-180 affinely centers and normalizes the squared atom locations. For consecutive remote Xi packets the node separation is bounded below in terms of `m` alone, uniformly in the remote index. This removes the absolute height from the inverse problem, although monomial power-moment coordinates still have an inverse norm at least of exponential order in `m`.

XF-181 changes that conditioning conclusion. Orthogonalize polynomials against the known reference nodes and integrate them to form adapted cusp coordinates. They are lower-triangular linear combinations of the same first `m` cusp moments, so no extra derivative depth is used. After scalar normalization their Jacobian at the reference packet is orthogonal, giving condition number one and a quantitative local bi-Lipschitz neighborhood independent of the remote index for fixed `m`.

## Synthesis of evidence

There are now three distinct complexity costs. **Jet depth** must grow with the number of moved atoms and cannot be removed. **Coordinate conditioning** can be dramatically improved once the packet is known. **Observable acquisition** asks whether those adapted linear combinations of cusp derivatives can actually be estimated from the positive heat/source data with sufficient accuracy before the zero-sensitive transition amplifies errors.

This redirects the source program. Searching for a better finite-dimensional inverse coordinate is no longer the main issue. The live theorem should bound effective packet complexity or transport the necessary adapted depth from source data into transition control.

## Counterevidence / boundary cases

XF-181 is local and packet-adapted. Its orthogonal polynomials depend on the reference nodes, so the construction does not solve support discovery. The nonlinear neighborhood may shrink with `m`, and derivative/observable coefficients may become expensive even though the Jacobian is perfectly conditioned.

The result does not contradict the fixed-topology no-go: the required coordinate family changes with packet complexity. A source allowing unbounded balanced surgery can still evade every fixed finite bank.

## Epistemic status

**Exact finite-packet recovery boundary:** depth `m` is information-theoretically sharp for `m` moved pairs; remote index can be normalized away; monomial exponential conditioning is coordinate-dependent and admits a locally isometric adapted replacement. Remaining difficulty is adaptive depth, support knowledge, nonlinear radius, and source-to-cusp acquisition.

## Novelty/prior-art status

Power-moment inversion, empirical orthogonal polynomials, and local preconditioning are classical mechanisms. The persisted findings record their exact specialization; this intuition synthesizes the source-complexity consequence.

## Falsification criterion

Show that the XF-181 adapted coordinates require cusp information beyond order `m`, or that their normalized Jacobian is not orthogonal under the stated empirical inner product. Strategically, prove a source theorem giving uniformly accurate adapted depth-`m` observables for an unbounded but controlled complexity class; that would cross the current acquisition gate.

## Lean-formalizable core

For fixed distinct nodes, the lower-triangular equivalence between power moments and integrated orthogonal-polynomial coordinates, plus the orthogonality of the Jacobian, is a finite algebraic statement well suited to formalization.
