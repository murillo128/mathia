# MI-039 — Boundary Euler jets detect delayed compensation at Robin scale

**Evidence level:** exact synthesis from [RE-173](../../findings/RE-173-infinite-prime-supported-exact-mertens-compensation-survives-kv-fidelity.md), [RE-174](../../findings/RE-174-unbounded-euler-temperature-samples-restore-infinite-prime-source-rigidity.md), and [RE-175](../../findings/RE-175-euler-boundary-jets-impose-a-robin-scale-sign-change-tariff.md).

The Robin source problem now has three distinct fidelity regimes. Exact Mertens matching is one scalar conservation law and is blind to where equal signed Mertens mass is placed across prime scale; RE-173 exploits that null direction by deleting mass near `p` and repaying it only from `16p` onward, while preserving strong KV fidelity and creating an order-one transient Robin excursion. At the opposite extreme, RE-174 shows that an unbounded exact high-temperature Euler profile identifies every bounded prime multiplicity, but the first defect at `P` appears only at scale `P^(-sigma)`, so exact coefficient recovery is exponentially ill-conditioned for the Robin destination.

RE-175 isolates an intermediate family aligned with the selector scale. The right boundary jets of the logarithmic Euler discrepancy at `s=1` are

`D_Q^(j)(1+) = sum_q c_q J_j(q)`, with `J_j(q) ~ (-1)^j (log q)^j/q`.

After the coordinate change `x=log q`, these kernels form an eventual Chebyshev system of exponentially weighted polynomial moments. Matching the Mertens value and the first `K` derivatives therefore forces at least `K+1` sign changes in every sufficiently far-out nonzero multiplicity perturbation. Finite boundary information does not recover the source coefficient by coefficient; it converts the old one-dimensional compensation direction into an increasingly oscillatory/interlaced source requirement.

For the concrete RE-173 control the first derivative already has the right conditioning. Its delayed positive compensation satisfies

`|D_Q'(1+)| >= (log(16/3)-o(1)) d_p ~ 1/(sqrt(p) log p)`,

so `sqrt(p) log p |D_Q'(1+)|` stays bounded away from zero at exactly the normalization of the order-one Robin excursion. Unlike high-temperature localization, the boundary slope prices the **logarithmic displacement of equal Mertens mass**, not the exponentially small amplitude of the earliest changed prime.

The reusable distinction is therefore **destination-aligned moment detection versus full source reconstruction**. A source observable can be far weaker than an injective fingerprint and still rule out a particular dangerous compensation mechanism at the scale seen by the destination. The right question is not always how many source coefficients are recoverable, but whether the retained source moments force enough oscillation or placement cost to suppress the target excursion.

The remaining gate is source-native. Nothing in RE-175 proves that the original Robin problem automatically controls `D_Q'(1+)` or any finite boundary jet. Nor does the Chebyshev sign-count theorem yet show that sufficiently interlaced controls cannot preserve an order-one excursion. A genuine advance would either derive one or more boundary-jet bounds from independent arithmetic input, or construct matched KV-faithful controls satisfying any prescribed finite jet order while retaining the Robin-scale excursion.

**Boundary.** This is not a source-rigidity theorem, a finite-dimensional replacement for RE-174, or a proof of Robin/RH. It shows that the known RE-173 escape is visible at Robin-scale conditioning through a finite boundary observable and that additional matched jets impose a precise oscillation tariff; whether that tariff eventually becomes selector-coercive remains open.