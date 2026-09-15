# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Test a frozen prime-gap residual only after exact representation-matched calibration

**Linked intuitions:** `MI-009-stable-decoding-is-a-collision-geometry-question` through `MI-024-dirichlet-gap-tent-variance-reduces-to-overlap-classes`.

VIS-237--VIS-241 progressively quotient grid-origin phase, artificial Poisson count noise, independently specified one-point intensity and endpoint-cut phase while preserving the spacing geometry that the test is supposed to measure. Symmetric Dirichlet cyclic gaps with independent rotation provide a fixed-count, exactly uniform-intensity dependence family; `alpha=1` is precisely iid-uniform circular spacing.

VIS-242 closes the remaining variance-calibration gap for the cut-averaged tent statistic. Writing the statistic as one half of the sum over oriented cyclic arcs, the covariance of two terms depends only on the two arc lengths and their overlap cardinality. Dirichlet aggregation reduces every covariance to an expectation under at most four aggregated Dirichlet components. Thus `Var_G(bar T)` is an exact finite overlap-class sum rather than a high-dimensional Monte Carlo problem.

At `alpha=1`, the statistic is a translation-invariant degree-two U-statistic whose distinct pair terms are pairwise uncorrelated, giving the closed audit formula

`Var(bar T)=binom(m,2)[2u/3-4u^2/3+11u^3/15-u^4/9]`,

with `E[bar T]=binom(m,2)(u-u^2/3)`.

The immediate null-calibration problem is therefore mathematically closed for every **predeclared** Dirichlet parameter: the general variance is a deterministic low-dimensional integral/sum and the iid member has a polynomial benchmark. The next question is genuinely confirmatory: freeze `alpha` or a stronger null independently, compute the exact calibration, and test whether the prime configuration has a residual outside that envelope.

A surviving point-process residual is still not an RH mechanism. It must be translated back through the signed prime-phase kernel and shown to survive the previously established moment-null and amplitude gates.

## Keep endpoint semantics and parameter selection outside the confirmation statistic

If interval endpoints are nuisance, use the cut average `bar T`; if physical endpoints are source-bearing, retain the separate exact `E[V_cut]` channel from VIS-241. Likewise, fitting `alpha` on the same tent statistic being tested invalidates confirmation even though the variance formula itself is exact. These choices must be fixed by the representation and null semantics rather than chosen to improve the residual.

## Preserve the older low-frequency and fixed-clock controls

VIS-130--VIS-160 still show that finite signed moment-null packets and deterministic selector clocks can mimic broad classes of visual/mixing effects. Any confirmed spacing residual must therefore survive exact coordinate controls and connect to a source-sensitive low-frequency/destination quantity rather than remain a visually distinctive but representation-dependent statistic.