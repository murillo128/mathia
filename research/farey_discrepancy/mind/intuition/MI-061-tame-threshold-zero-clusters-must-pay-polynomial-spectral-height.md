# MI-061 — Tame threshold zero clusters must pay polynomial spectral height

**Evidence level:** exact RH-conditional synthesis from FD-273, FD-276 and [FD-277](../../findings/FD-277-threshold-close-zero-clusters-force-polynomial-spectral-height.md), with simple zeros inherited from the reciprocal-log cluster decomposition.

FD-276 leaves a precise trade between cluster cardinality and desingularized background conditioning. In the polynomial-depth regime `x=N^(lambda+o(1))`, write `beta=log_2(3/2)` and suppose one complete reciprocal-log cluster is itself large enough to reach the positive-capacity threshold while its collar background is `B_C(eta)<=x^(delta+o(1))`. Then with `q=1-beta-delta>0`, that component must contain at least `(q-o(1)) log x/log log x` zeros.

FD-277 shows that this cardinality cannot be packed at arbitrarily low spectral height. Reciprocal-log connectivity puts those zeros inside an interval of length `O(1/log log x)`, so Riemann--von Mangoldt turns the excess local zero count into an excursion of `S(t)`. Under RH, the sharp `|S(t)|<=(1/4+o(1)) log t/log log t` bound forces

`log Gamma/log x >= 2q/(1+2q/(pi(1+1/lambda)))-o(1)`.

Uniformly over fixed polynomial depths this is at least `2q/(1+2q/pi)-o(1)`. For subpolynomial background (`delta=0`) a threshold cluster must therefore satisfy `Gamma>=x^(0.6565900638708717-o(1))`; at balanced depth `lambda=1` the exponent is `0.7332102032858479`.

The durable interpretation is not that height itself amplifies the repair. Rather, the single-cluster escape now has a three-way tariff. If the background does not pay the missing exponent, the cluster must be large; if it is large at reciprocal-log spacing, it must also occur polynomially high enough for the ordinary zero density and the maximal allowed `S(t)` excursion to accommodate it. Source-selected phase alignment is still a separate requirement.

The remaining structurally different loophole is aggregate. FD-277 prices one component that is already threshold-sized; it does not rule out many individually subthreshold components whose grouped contributions add coherently on the physical Mertens-large horizons.

**Boundary.** The height tariff is asymptotic, assumes RH and the simple-zero setting used by FD-276, and applies to one complete reciprocal-log component at fixed polynomial depth. It does not control multiple zeros, off-line zeros, explicit-formula remainders or coherent accumulation across many subthreshold components.