# MI-023 — Source information is priced by inverse distinguishability, not forward smoothness

**Evidence level:** supported cross-line synthesis from [FD-167](../../farey_discrepancy/findings/FD-167-full-field-l2-inversion-has-uniform-square-root-prefix-conditioning.md) and [MC-342](../../mobius_cancellation/findings/MC-342-forward-source-regularity-does-not-price-analog-capacity.md), with their respective exact inversion/information predecessors. No common transform theorem is claimed.

Farey Discrepancy and Möbius Cancellation now give opposite exact controls on the same information-geometric question: when does a large discrete source remain *stably distinguishable* after being represented by an analytic object?

FD-167 gives a positive inverse theorem. The complete Farey discrepancy field determines the consecutive source prefix through `floor(sqrt(H))`, and the inverse has an `H`-independent modulus in the natural unnormalized `L^2` field norm:

`max_(r<=sqrt H) |A(r)-M(r)| <= sqrt(30) ||E_H||_2`.

For integer-valued sources, field error below `1/sqrt(30)` therefore snaps the entire visible prefix exactly. A growing amount of source information can be robustly encoded because the actual observation map supplies a uniform lower distinguishability bound on those coordinates.

MC-342 gives the adversarial opposite. A scalar dyadic transcript can carry essentially `R` bits while its range, forward Hamming Lipschitz constant and every fixed positive-moment source-edge energy remain uniformly bounded. The encoding pays only through inverse geometry: minimum separation is `2^(-R)`, spread is exponential, and exact recovery requires access to linearly many precision bits.

Together these examples isolate a reusable distinction. **Forward regularity bounds how much source perturbations can move the representation; it does not say how far distinct source states remain apart. Stable source coercivity is an inverse statement.** The relevant currencies are minimum distinguishability at the declared noise scale, an inverse modulus/co-Lipschitz bound, a stable singular value, finite-precision capacity, or another representation-invariant statement that prevents exponentially fine state packing.

This changes how low-dimensional or smooth analytic representations should be audited. A bounded-range scalar statistic is not intrinsically low-information, and a small source gradient is not intrinsically stable. Conversely, a representation that visibly contains many coordinates is not necessarily ill-conditioned: the full Farey field recovers its exposed prefix with constant modulus. One must compute the native inverse geometry of the actual map rather than infer capacity from dimension, forward smoothness or exact injectivity alone.

The next line-specific questions differ. Farey must determine how the inverse modulus degrades under partial, sparse or coarsened observation. Möbius must identify a canonical metric/noise model for the genuine transcript and prove that its required linear source information cannot be hidden below the relevant resolution. Neither conclusion transfers automatically to the other line.

**Boundary.** FD-167 concerns a complete linear/Fourier field transform and MC-342 an adversarial finite scalar encoder. This synthesis does not provide a universal inverse theorem, a lower bound for every analytic representation, or an RH estimate. It supplies an audit rule: whenever source information is claimed to be analytically usable, state and prove the inverse distinguishability resource in the observation norm actually consumed downstream.