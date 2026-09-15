# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Test a frozen prime-gap residual only after exact representation-matched calibration

**Linked intuitions:** `MI-009-stable-decoding-is-a-collision-geometry-question` through `MI-024-dirichlet-gap-tent-variance-reduces-to-overlap-classes`.

VIS-237--VIS-241 progressively quotient grid-origin phase, artificial Poisson count noise, independently specified one-point intensity and endpoint-cut phase while preserving the spacing geometry that the test is supposed to measure. Symmetric Dirichlet cyclic gaps with independent rotation provide a fixed-count, exactly uniform-intensity dependence family; `alpha=1` is precisely iid-uniform circular spacing.

VIS-242 reduced the cut-averaged tent variance to low-dimensional Dirichlet expectations indexed by cyclic arc lengths and overlap cardinality. VIS-243 closes the remaining deterministic bookkeeping. Complement symmetry reduces arc lengths to `1<=r<=floor(m/2)` with the sole half-weight at `r=m/2` for even `m`; for `a=min(r,s)` and `b=max(r,s)`, the overlap multiplicities are exactly

`N_0=m-r-s+1`,  `N_a=b-a+1`,  `N_k=2` for `1<=k<a`.

Hence the general-`alpha` variance is a fully explicit finite weighted sum of the low-dimensional expectations `C_(r,s,k)`, with no complementary-arc or displacement enumeration left. At `alpha=1`, the independent audit remains the closed polynomial variance from VIS-242.

The representation-matched null calibration is therefore mathematically explicit for every **predeclared** Dirichlet parameter. The next question is genuinely confirmatory: freeze `alpha` or a stronger null independently, evaluate the deterministic calibration, and test whether the prime configuration leaves a stable residual outside that envelope.

A surviving point-process residual is still not an RH mechanism. It must be translated back through the signed prime-phase kernel and shown to survive the previously established moment-null and amplitude gates.

## Keep endpoint semantics and parameter selection outside the confirmation statistic

If interval endpoints are nuisance, use the cut average `bar T`; if physical endpoints are source-bearing, retain the separate exact endpoint channel from VIS-241. Likewise, fitting `alpha` on the same tent statistic being tested invalidates confirmation even though the variance formula is exact. These choices must be fixed by representation and null semantics rather than chosen to improve the residual.

VIS-243's half-circle quotient also depends specifically on the complement symmetry `q_u(s)=q_u(1-s)`. It must not be transferred to an oriented or endpoint-sensitive statistic without re-deriving the representation.

## Preserve the older low-frequency and fixed-clock controls

VIS-130--VIS-160 still show that finite signed moment-null packets and deterministic selector clocks can mimic broad classes of visual/mixing effects. Any confirmed spacing residual must therefore survive exact coordinate controls and connect to a source-sensitive low-frequency/destination quantity rather than remain a visually distinctive but representation-dependent statistic.