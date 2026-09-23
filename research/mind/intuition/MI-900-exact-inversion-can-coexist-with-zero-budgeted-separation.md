# MI-900 — Exact inversion, source separation and budgeted destination separation are distinct gates

**Evidence level:** supported cross-line synthesis from [AF-509](../../arithmetic_fidelity/findings/AF-509-log-prime-sum-curvature-classifies-simple-sources-up-to-dilation.md)--[AF-514](../../arithmetic_fidelity/findings/AF-514-weighted-tail-transport-destroys-curvature-provenance-margin.md), [NB-298](../../nyman_beurling/findings/NB-298-projected-dilation-is-a-subblock-of-the-existing-future-tail.md)--[NB-301](../../nyman_beurling/findings/NB-301-early-shell-mobius-inversion-gives-cubic-moving-cutoff-source-compression.md), and [WI-412](../../weil_inertia/findings/WI-412-haar-scale-blaschke-mixing-buys-a-count-quantum-only-at-infinite-budget.md)--[WI-413](../../weil_inertia/findings/WI-413-centered-blaschke-scale-convolution-is-invertible.md). The correspondence below is a synthesis of different operators, not a theorem identifying them.

Three recent exact calculations separate gates that can look interchangeable if only injectivity or source geometry is inspected.

For Arithmetic Fidelity, the complete curvature map `Q -> kappa_Q=(log P_Q)''` is exactly and constructively invertible modulo dilation on the simple unit-weight source class. Nevertheless AF-513--AF-514 move an entire cofinite prime tail, even by unbounded sublinear distances to composites, while the full-domain relative-curvature profile converges uniformly back to the prime profile. The relevant sufficient perturbation cost is

`B_A=sum_(p>A) h_p(1+log^2 p)/p^2 -> 0`.

Thus exact inverse existence does not imply a positive decision margin in the chosen observation topology.

For Weil Inertia, the centered log-scale Blaschke convolution is itself an automorphism of tempered distributions because

`Khat(xi)=pi/xi tanh(pi xi/2)`

has no real zero and has a slowly increasing reciprocal. Yet the target profile that would be most useful for defect counting, an exact nonzero constant at every log-depth, has a unique tempered preimage: Haar density `2q/pi^2 ds`. WI-412 already shows that this preimage has infinite total variation across scale and induces a nonintegrable height tail. Exact invertibility therefore does not imply that a desired destination profile has a preimage inside the source-budget class needed by the proof.

For Nyman--Beurling, the canonical source geometry behaves in the opposite direction. Early-shell Möbius inversion gives the moving-section overlap bound

`||P_(V_(n-1)) S_m|_(V_(n-1))||^2 <= min(1,6(n-1)^3/m)`.

Thus the old source section and its dilation become asymptotically separated already when `m/(n-1)^3 -> infinity`, without invoking the much larger common reciprocal-cell period. But off-critical sampling simultaneously contracts by `m^(-delta_Z)`. NB-298--NB-301 then force the normalized projected-dilation destination block to vanish whenever `m/(n-1)^3 -> infinity` and `delta_Z log m -> infinity`, subject to the stated first-free factorization. Strong source-space separation can therefore become sample-null rather than destination-visible.

The common ledger is consequently three-stage rather than one-stage: **(1) source identifiability or geometric separation, (2) a source-norm/budget for the preimage or perturbation class, and (3) a destination topology in which the target classes remain positively separated.** The three lines fail at different stages. Arithmetic Fidelity has exact identification but no margin in its natural relative profile; Weil Inertia has an invertible response operator but the desired flat profile lies outside finite scale budget; Nyman--Beurling can have asymptotically separated source sections while the sampling map erases the projected escape.

This correspondence does not transfer constants, source classes or norms between the lines. In particular `B_A`, total variation in log-scale, and the Nyman `L^2`/sample Gram norms are different objects. What transfers is the exact logical separation: proving any one of injectivity, source orthogonality or response invertibility cannot substitute for proving a bounded source-side realization **and** a positive margin after the actual destination map.