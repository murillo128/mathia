# MI-052 — Bit-flip noise prices coordinate access, not noise alone

**Evidence level:** exact information-theoretic synthesis from [MC-339](../../findings/MC-339-bounded-energy-dephasing-needs-linear-joint-source-information.md), [MC-340](../../findings/MC-340-punctured-source-total-correlation-is-only-constant.md), [MC-343](../../findings/MC-343-gaussian-noise-transcript-capacity.md), and [MC-344](../../findings/MC-344-bit-flip-source-readout-capacity.md).

MC-339--MC-340 reduce bounded-energy reciprocal-endpoint dephasing to a joint-information requirement: a fixed nontrivial gain requires `I(X;Y)=Omega(R)` for the punctured reciprocal source. MC-343 shows how a declared Gaussian readout prices hidden analog precision through SNR. MC-344 supplies the discrete-coordinate counterpart and clarifies an important boundary: **positive noise is not itself the obstruction; insufficient aggregate channel capacity is.**

Suppose a readout exposes only `k` source coordinates and each is passed independently through a binary symmetric channel with crossover probability `q<1/2`. If `Z_J` is the noisy coordinate vector and `Y` is any downstream processing, data processing gives

`I(X;Y) <= I(X;Z_J) <= k c(q)`,

where `c(q)=log 2-h(q)` is the one-bit channel capacity in natural units. Combining this with the MC-340 lower bound implies that any fixed bounded-energy dephasing gain requires `k=Omega(R)` at fixed `q`.

This gives a clean coordinate-access theorem: an architecture that reads only `o(R)` independently noisy source coordinates cannot supply the linear joint information demanded by the endpoint, no matter how nonlinear the downstream processing is. Equivalently, if the coefficient-energy budget is bounded by `C` and the desired gain is fixed at `eta`, the accessed fraction has a positive lower bound proportional to `eta^2/(C c(q))` up to the punctured-source `o(1)` correction.

But the converse stress test matters just as much. If all `R` source coordinates are exposed through the same fixed-noise channel, then the punctured source still satisfies

`I(X;Z)=R c(q)-o(R)`.

So every fixed `q<1/2` leaves extensive information. Even though exact recovery is impossible and each coordinate is noisy, the channel remains large enough in principle to meet an `Omega(R)` information demand. A proof that says only “there is positive readout noise” therefore cannot exclude bounded-energy dephasing.

The reusable audit is to compute **aggregate source-access capacity at the actual downstream resolution**. Obstruction can come from sublinear access, per-coordinate capacity tending to zero, low-dimensional SNR limits, or source/readout dependence that destroys joint capacity. If the admitted observation has `Theta(R)` surviving capacity, information theory alone has not closed the route; one still needs to ask whether the arithmetic architecture can exploit that capacity coherently at the endpoint.

**Boundary.** MC-344 studies coordinatewise binary-symmetric access to the reciprocal finite source and does not claim that this is the canonical observation model for Möbius cancellation. It gives an exact capacity benchmark. A different readout may obey a different law, but any claimed information obstruction must control its total channel capacity rather than appeal to noise, dimension, or coordinate syntax in isolation.