# MI-045 — Shrinking-mesh solid `PF_3` consistency forces boundary flatness

**Evidence level:** exact synthesis from [AF-383](../../findings/AF-383-one-sided-consecutive-toeplitz-minors-generate-all-placements.md), [AF-385](../../findings/AF-385-sampled-solid-strictness-recognizes-continuum-tnk.md), [AF-387](../../findings/AF-387-connected-support-does-not-repair-nonstrict-solid-pf3-recognition.md), and [AF-388](../../findings/AF-388-shrinking-solid-pf3-excludes-quadratic-boundary-contact.md).

Fixed-lattice recognition and common-profile multiscale recognition are different information problems. AF-387 shows that on one lattice `PF_2`, connected positive support and nonnegative solid order-three minors can coexist with a negative gapped order-three minor. The failure sits on an interior lower-order degeneracy: some order-two minors vanish and stop the solid generators from propagating to nonlocal placements.

AF-388 proves that the same sort of degeneracy cannot be copied freely across arbitrarily fine samples of one smooth profile. Let `f>0` be `C^8`, sample it on meshes `h_m -> 0`, and suppose every sampled solid order-two and order-three Toeplitz minor is nonnegative. With

`q = -(log f)''`,

shrinking-mesh consistency forces the pointwise differential inequalities

`q >= 0`,

`2q^3 - q q'' + (q')^2 >= 0`.

Where `q>0`, the second inequality is `(log q)'' <= 2q`. More importantly, if `q(x_0)=0`, the next term in the solid `3x3` determinant expansion forces `q''(x_0)=0`. An ordinary nondegenerate quadratic contact with the `PF_2` boundary is therefore impossible.

The mechanism is not merely “more samples.” The same latent function must satisfy the determinant inequalities at every scale. Nearest-grid centers approach an arbitrary continuum point closely enough that the leading determinant coefficients become differential constraints, and at a boundary zero the `h^8` coefficient stays negative by a uniform margin even after the `O(h)` grid displacement is allowed. **Cross-scale compatibility converts a lossy local certificate into additional boundary information.**

This gives a precise refinement of the resource ledger. Support connectivity is still a global zero-pattern resource, lower-order interiority is still distinct from support topology, and fixed-order placement compression still does not imply full target positivity. But lower-order boundary geometry itself is now stratified by order of contact: quadratic contact is excluded by the shrinking solid `PF_3` hierarchy, while flatter contact is not yet classified.

The next recognition boundary is therefore concrete rather than qualitative. Determine whether every finite-order zero of `q` is incompatible with the same multiscale solid hierarchy, or whether some quartic-or-higher contact survives and can still hide a negative non-solid continuum `3x3` minor. An infinitely flat zero is a separate possible endpoint and should not be inferred from any finite Taylor-order calculation.

**Boundary.** AF-388 is source-independent recognition theory. It does not prove continuum `TN_3`, does not provide solid-minor signs for a Riemann-associated kernel, and does not show that strict lower-order positivity can be discarded at higher determinant orders. Its durable content is narrower: a fixed-lattice lower-order boundary obstruction may disappear once the same smooth object is required to satisfy the compressed certificate coherently on a vanishing sequence of meshes.