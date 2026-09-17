# MI-045 — Shrinking-mesh solid `PF_3` consistency leaves curvature-component topology as the final smooth boundary resource

**Evidence level:** exact synthesis from [AF-383](../../findings/AF-383-one-sided-consecutive-toeplitz-minors-generate-all-placements.md), [AF-385](../../findings/AF-385-sampled-solid-minor-hierarchy-certifies-continuum-fixed-order-total-nonnegativity.md), [AF-387](../../findings/AF-387-connected-support-does-not-repair-nonstrict-solid-pf3-recognition.md), [AF-388](../../findings/AF-388-shrinking-solid-pf3-excludes-quadratic-boundary-contact.md), [AF-389](../../findings/AF-389-multiscale-solid-pf3-excludes-all-finite-order-boundary-contact.md), and [AF-394](../../findings/AF-394-connected-curvature-support-completes-smooth-pf3-fidelity.md).

Fixed-lattice recognition and common-profile multiscale recognition are different information problems. AF-387 shows that on one lattice `PF_2`, connected positive support and nonnegative solid order-three minors can coexist with a negative gapped order-three minor. The failure sits on an interior lower-order degeneracy: zero order-two minors can stop the solid generators from propagating to nonlocal placements.

AF-388 shows that a quadratic version of that degeneracy cannot persist when the same smooth profile is sampled on arbitrarily fine lattices. AF-389 closes the finite-order extension. Let `f>0` be `C^infinity`, let `h_n -> 0`, and suppose all sampled solid order-two and order-three Toeplitz minors are nonnegative. With

`q = -(log f)''`,

one has `q>=0`, and every zero of `q` is infinitely flat. If the first nonzero local term were `q(x_0+y)=c y^(2m)+o(y^(2m))`, the naturally rescaled solid `3x3` determinant has a universal negative leading coefficient throughout the nearest-grid window, contradicting the sampled nonnegativity.

The mechanism is stronger than dense sampling. **Cross-scale compatibility preserves the order of contact with a compressed lower-order boundary.** One fixed lattice can hide a gapped negative minor behind a degenerate stratum; an unbounded family of compatible samples of one latent function forces every finite Taylor-order version of that stratum to disappear.

AF-394 then resolves the smooth endpoint that AF-389 left open. The same shrinking hierarchy already forces the local analytic conditions needed for continuum `TN_3`; the exact remaining condition is

`{q>0} is an interval`.

An infinitely-flat zero is therefore not intrinsically bad. It is admissible when it lies on the boundary of one connected positive-curvature region, but it is fatal when it separates two positive-curvature components. In the latter case nonlocal placement data detect a negative order-three orientation even though every local finite jet at the separating zero can be flat.

This isolates a sharp information hierarchy. Shrinking local certificates recover the full finite-jet boundary geometry and the positive-curvature differential cone, but they do not encode **component membership**. The final smooth order-three resource is global topology, not another derivative, another finite window, or stronger pointwise flatness.

Quasianalytic continuation and log-concavity remain useful sufficient closures because they force the allowed component geometry, but AF-394 shows they are stronger than necessary. The unrestricted smooth target is already characterized once connectedness of positive curvature is supplied.

**Boundary.** This is source-independent recognition theory. It does not derive the sampled solid signs or curvature connectivity from arithmetic data, does not imply RH, and does not establish an analogous component-topology criterion for determinant orders above three. Its durable content is the separation between multiscale recovery of local boundary jets and the global topology still invisible to those local certificates.