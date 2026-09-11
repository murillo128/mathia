# MI-013 — Adaptive Xi recovery separates depth, inverse conditioning, and acquisition visibility

**Evidence level:** proved local finite-packet geometry and linearized positive-heat visibility; global source acquisition remains open

## Core intuition

Remote atom location is not a fundamental instability of the **finite cusp inverse**. Once the packet size `m`, reference packet, and first `m` adapted cusp data are known, the atom-location inverse can be made infinitesimally isometric by using an orthogonal-polynomial basis.

Remote location does matter one stage earlier. XF-182 shows that the unrenormalized positive-heat map presents the orthogonal complexity modes with visibility `N^-1,N^-2,...,N^-m` for a remote `m`-atom Xi packet. The durable decomposition is therefore: sharp adaptive information depth, well-conditioned exact inverse coordinates, and a separate graded acquisition problem.

## Strongest justified claim

XF-177--XF-178 show that every fixed power-weighted real-axis topology can be fooled by sufficiently high-order moment-balanced remote surgery. No fixed-complexity seminorm is coercive on the full finite-surgery class.

XF-179 identifies the exact adaptive threshold. If exactly `m` positive unit-mass atom pairs are moved, the cusp jet through order `m` determines the surgery, while depth `m-1` is sharp. The obstruction is therefore tied to packet complexity.

XF-180 affinely centers and normalizes the squared atom locations. For consecutive remote Xi packets the normalized node separation is bounded below in terms of `m` alone, uniformly in the remote index. This removes absolute height from the algebraic inverse problem, although raw monomial power-moment coordinates are poorly conditioned.

XF-181 shows that this monomial conditioning is coordinate-dependent. Orthogonalize polynomials against the known reference nodes and integrate them to form adapted cusp coordinates. They are lower-triangular linear combinations of the same first `m` cusp moments, so no extra derivative depth is used. After scalar normalization their location Jacobian is orthogonal, giving condition number one and a quantitative local bi-Lipschitz neighborhood independent of the remote index for fixed `m`.

XF-182 then quantifies the missing acquisition stage. In the same orthogonal directions, the raw positive-heat Jacobi response of mode `k` is `Theta_m(N^(-(k+1)))`. The highest mode is visible only at `Theta_m(N^-m)`, while `m` samples at scales `x~N^-2` recover all modes with absolute inverse amplification `Theta_m(N^m)`. Thus orthogonalizing the cusp inverse does not equalize finite-scale heat visibility.

## Synthesis of evidence

There are now three distinct complexity costs. **Jet depth** must grow with the number of moved atoms and cannot be removed. **Coordinate conditioning** can be made benign once the packet and exact cusp data are known. **Observable acquisition** has a graded remote visibility spectrum because higher adapted modes cancel more terms of the packet heat expansion.

This redirects the source program away from better finite-dimensional inverse coordinates. The live theorem should either renormalize acquisition in a source-faithful way before absolute errors are compared, or show that the actual arithmetic/modular source cannot realize high-complexity remote packet motion.

## Counterevidence / boundary cases

XF-181 and XF-182 are local and packet-adapted. Their orthogonal polynomials depend on the reference nodes, so the construction does not solve support discovery or an infinite deformation. The nonlinear inverse neighborhood can shrink with `m` even though the linearized cusp Jacobian is perfectly conditioned.

The `N^(-(k+1))` visibility law is for the unweighted absolute positive-heat Jacobi residual. A location- and complexity-dependent renormalization can cancel those powers formally. Such a renormalization changes the topology and must be justified by an error budget; otherwise it simply moves the required `N^(k+1)` amplification into the observable definition.

The result does not contradict the fixed-topology no-go. XF-178 gives finite nonlinear packet motions invisible to every fixed power bank when packet complexity is allowed to grow; XF-182 resolves the corresponding fixed-`m` linear acquisition spectrum.

## Epistemic status

**Exact finite-packet recovery boundary:** depth `m` is information-theoretically sharp for `m` moved pairs. The exact adapted cusp inverse can be locally condition-one and remote-index uniform, but acquiring its modes from raw positive heat has sharp visibility ladder `N^-1,...,N^-m`. Remaining difficulty is source-faithful renormalized acquisition, support knowledge, nonlinear radius, and effective complexity control.

## Novelty/prior-art status

Power-moment inversion, empirical orthogonal polynomials, local preconditioning, moment cancellation, and inverse-Laplace conditioning are classical mechanisms. The persisted findings record their exact Xi/Jacobi specialization; this intuition synthesizes the separation between inverse geometry and forward visibility.

## Falsification criterion

Show that the XF-182 adapted mode response has a different power of the remote index after the full Jacobi reciprocal image is included, or construct a source-natural positive-heat normalization with uniformly bounded absolute-error amplification across all fixed packet modes. Strategically, a theorem of the latter kind would cross the current acquisition gate.

## Lean-formalizable core

For fixed distinct normalized nodes, the orthogonality identities, cancellation of the first `k` heat moments, and the resulting `a^(-(k+1))` directional bounds are finite algebra plus elementary exponential estimates. The finite-sample Vandermonde factorization giving acquisition condition `a^(m-1)` is also a finite-dimensional statement.