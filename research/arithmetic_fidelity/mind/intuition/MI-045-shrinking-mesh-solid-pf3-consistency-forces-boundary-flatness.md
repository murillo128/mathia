# MI-045 — Shrinking-mesh solid `PF_3` consistency forces infinite flatness at the `PF_2` boundary

**Evidence level:** exact synthesis from [AF-383](../../findings/AF-383-one-sided-consecutive-toeplitz-minors-generate-all-placements.md), [AF-385](../../findings/AF-385-sampled-solid-strictness-recognizes-continuum-tnk.md), [AF-387](../../findings/AF-387-connected-support-does-not-repair-nonstrict-solid-pf3-recognition.md), [AF-388](../../findings/AF-388-shrinking-solid-pf3-excludes-quadratic-boundary-contact.md), and [AF-389](../../findings/AF-389-multiscale-solid-pf3-excludes-all-finite-order-boundary-contact.md).

Fixed-lattice recognition and common-profile multiscale recognition are different information problems. AF-387 shows that on one lattice `PF_2`, connected positive support and nonnegative solid order-three minors can coexist with a negative gapped order-three minor. The failure sits on an interior lower-order degeneracy: zero order-two minors can stop the solid generators from propagating to nonlocal placements.

AF-388 shows that a quadratic version of that degeneracy cannot persist when the same smooth profile is sampled on arbitrarily fine lattices. AF-389 closes the finite-order extension. Let `f>0` be `C^infinity`, let `h_n -> 0`, and suppose all sampled solid order-two and order-three Toeplitz minors are nonnegative. With

`q = -(log f)''`,

one has `q>=0`, and every zero of `q` is infinitely flat. If the first nonzero local term were `q(x_0+y)=c y^(2m)+o(y^(2m))`, the naturally rescaled solid `3x3` determinant has a universal negative leading coefficient throughout the nearest-grid window, contradicting the sampled nonnegativity.

The mechanism is stronger than dense sampling. **Cross-scale compatibility preserves the order of contact with a compressed lower-order boundary.** One fixed lattice can hide a gapped negative minor behind a degenerate stratum; an unbounded family of compatible samples of one latent function forces every finite Taylor-order version of that stratum to disappear.

This also makes the role of regularity explicit. For positive real-analytic `f`, infinite flatness at one zero forces `q≡0`; hence either `q>0` everywhere or `f=e^(ax+b)`. In the positive integrable analytic category only the strict alternative survives. In the merely smooth category, however, infinitely-flat zeros remain a genuine unresolved endpoint.

The next recognition boundary is therefore precise: determine whether an infinitely-flat zero of `q` can satisfy the shrinking solid `PF_2/PF_3` hierarchy while some arbitrary-placement continuum order-three minor is negative. A negative answer would remove the last smooth lower-order boundary alias; a positive example would identify the exact information still lost by the multiscale solid certificate.

**Boundary.** AF-389 is source-independent recognition theory. It does not prove continuum `TN_3`, does not supply the solid-minor signs for a Riemann-associated kernel, and does not extend automatically to determinant orders above three. Infinite flatness is a necessary boundary condition under the declared hierarchy, not proof that the boundary is empty.