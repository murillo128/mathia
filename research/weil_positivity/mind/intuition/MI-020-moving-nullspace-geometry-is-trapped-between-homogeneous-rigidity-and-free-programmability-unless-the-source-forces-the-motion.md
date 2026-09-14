# MI-020 — Moving-nullspace geometry is trapped between homogeneous rigidity and free programmability unless the source forces the motion

**Evidence level:** exact for the finite-dimensional homogeneous/projector models in [WP-302](../../findings/WP-302-homogeneous-moving-nullspaces-are-archimedean-rigid-while-free-projector-paths-are-programmable.md), building on the fixed-kernel obstruction in [WP-301](../../findings/WP-301-frustration-free-holonomy-zero-modes-are-universal-kernel-intersections.md). This does not rule out infinite-dimensional, singular, nonlocal, nonunitary or source-forced nonhomogeneous mechanisms and does not prove Weil positivity.

WP-301 shows that a fixed positive frustration-free completion cannot recover nonzero archimedean spectrum through its zero-mode projector. Allowing the kernel to move is therefore a genuine escape, but WP-302 puts two opposite exact controls around it.

For a finite-dimensional homogeneous motion

`P(t)=e^(itA) P_0 e^(-itA)`,

every finite jet `P^(k)(t)` is a simultaneous unitary conjugate of a fixed jet. Any conjugation-invariant local scalar of that jet is therefore constant. If fixed bounded finite-prime/source operators are added as a reference frame, trace-polynomial local readouts become finite exponential polynomials in `t`, and every continuous readout of the compact orbit data remains bounded.

The completed-zeta archimedean digamma symbol does not have that behavior: its real part grows like `log|t|`. Hence a finite-dimensional fixed-generator moving kernel with a regular local readout has the wrong global analytic profile even when it moves nontrivially relative to a fixed arithmetic frame.

At the opposite extreme, a freely chosen rank-one projector path is too flexible to explain anything. For `v(t)=(cos theta(t), sin theta(t))` and `P_theta=vv*`, the Grassmann/Fubini--Study metric density is exactly

`(1/2) Tr(P_theta'(t)^2)=theta'(t)^2`.

Thus any prescribed smooth positive profile `h(t)` can be realized by choosing `theta'(t)=sqrt(h(t))`. Agreement with the desired archimedean density is then programmed into the path rather than forced by arithmetic.

The reusable gate is therefore not merely “make the kernel move.” A useful moving-nullspace mechanism must sit between **homogeneous rigidity** and **free programmability**: the source must force enough nonhomogeneous, infinite-dimensional, singular or nonlocal structure to produce the required archimedean behavior, while leaving too little freedom to fit that behavior by construction. The source law has to be specified before comparison with the target.

This adds a fifth distinction to the curvature/readout ledger: reachability, source specificity and readout fidelity are still insufficient if the surviving geometric motion is either too homogeneous to carry the target profile or so unconstrained that the target can be encoded directly into it.

**Boundary.** Boundedness uses finite-dimensional compact homogeneous orbit data and regular continuous local readouts. Singular determinants/resolvents, nonlocal kernels, unbounded/infinite-dimensional representations, semigroup/nonunitary evolution and genuinely coupled finite--archimedean operators remain open. Any such escape must identify the independently source-forced structure that prevents the same programmability objection.