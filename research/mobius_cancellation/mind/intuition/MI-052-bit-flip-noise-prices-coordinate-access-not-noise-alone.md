# MI-052 — Aggregate noisy source-access capacity survives adaptation only by paying per access

**Evidence level:** exact information-theoretic synthesis from [MC-339](../../findings/MC-339-bounded-energy-dephasing-needs-linear-joint-source-information.md), [MC-340](../../findings/MC-340-punctured-source-total-correlation-is-only-constant.md), [MC-343](../../findings/MC-343-gaussian-noise-transcript-capacity.md), [MC-344](../../findings/MC-344-bit-flip-source-readout-capacity.md), and [MC-345](../../findings/MC-345-adaptive-source-query-feedback-capacity.md).

MC-339--MC-340 reduce bounded-energy reciprocal-endpoint dephasing to a joint-information requirement: a fixed nontrivial gain requires `I(X;Y)=Omega(R)` for the punctured reciprocal source. MC-343 shows how declared Gaussian readout prices hidden analog precision through SNR. MC-344 supplies the discrete-coordinate counterpart: if only `k` source coordinates are exposed through independent binary-symmetric channels with crossover `q`, then

`I(X;Y) <= k c(q)`,

where `c(q)=log 2-h(q)` is the one-use BSC capacity in natural units. Thus fixed gain needs `k=Omega(R)` at fixed `q`, but exposing all `R` coordinates at any fixed `q<1/2` still leaves `Theta(R)` information. Positive noise itself is not the obstruction.

MC-345 closes the obvious adaptive escape. At query time `t`, let the controller choose a source coordinate using all previous noisy answers, allow repeated coordinates, private randomness and a stopping time `tau`, and pass each queried bit through the same memoryless BSC. Because the next index is already determined by the retained history, it contributes no extra conditional information. Each fresh noisy answer contributes at most `c(q)`. Therefore

`I(X;T) <= c(q) E[tau]`

for the complete adaptive transcript, and the same bound holds after arbitrary downstream processing.

Combining this with the MC-340 endpoint requirement gives a linear expected-access lower bound for every fixed bounded-energy dephasing gain. Near the matched-filter energy floor, the Fano lower bound prices almost the full source entropy. Adaptivity can decide **where** to spend source accesses, but it cannot manufacture more capacity per access than the declared channel provides.

The zero-error boundary is consistent with the same geometry. With noiseless queries, exact source recovery needs hard depth at least `R` for even rank and `R-1` for odd rank, the latter saving exactly the one parity relation in the source support. With any fixed `0<q<1/2`, every finite transcript path has common support across source states, so an almost-surely finite protocol cannot recover the source with zero error.

The reusable audit is therefore to compute **aggregate source-access capacity at the actual downstream resolution, including every side channel used to choose what is observed**. Obstruction can come from sublinear access, per-use capacity tending to zero, low-dimensional SNR limits, or dependence that genuinely collapses total information. If an architecture has `Theta(R)` positive-capacity accesses, information theory alone has not closed the route; one still needs a structural reason why that information cannot be converted into coherent endpoint cancellation.

**Boundary.** MC-345 assumes a memoryless BSC conditional on the queried source bit and a controller whose source dependence enters only through the admitted transcript. A hidden source-dependent selector side channel, stateful/correlated noise or a different observation primitive requires its own capacity theorem. The result is a finite reciprocal-endpoint admission theorem and gives no bound for `M(x)`.