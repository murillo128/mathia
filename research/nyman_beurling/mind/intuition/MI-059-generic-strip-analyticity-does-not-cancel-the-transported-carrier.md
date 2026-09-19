# MI-059 — Generic strip analyticity is sharp, while population-only Ford reach has a linear source-width threshold

**Evidence level:** exact synthesis from [NB-221](../../findings/NB-221-flat-soft-primitive-windows-factor-through-local-log-derivative-contour.md) through [NB-225](../../findings/NB-225-sublinear-shells-admit-bellotti-compatible-phase-aligned-ford-packets.md), building on the exact source/kernel coupling of NB-218--NB-220.

NB-221 removes the artificial costs of fixed-depth primitivization, global vertical acquisition and remote-zero transport. After faithful localization and a safe finite contour shift, every fixed primitive depth has the same leading term: a carrier-frequency convolution of the local logarithmic derivative `-zeta'/zeta`.

NB-222 asks whether the carrier itself can force more cancellation from nothing beyond holomorphy and boundedness in a zero-free strip. For the exact moving-shell transform the answer is no. If `F` is bounded by `M` in a strip of height `eta`, the carrier functional has operator norm

`Theta(M e^(-X eta))`,

and a carrier-matched entire exponential attains the lower bound. Generic strip regularity, even with the full Cauchy derivative envelope, is therefore exhausted.

NB-223 shows that the actual zeta carrier has additional spectral structure. Moving the contour across the nontrivial zeros produces the weighted sum

`sum_rho m(rho) e^(-X(1-beta)) (1+|gamma-t|)^(-A)`.

Bellotti's near-one density theorem controls the population in layers `1-beta~K/R`, with

`R=(log |t|)^(2/3)(log log |t|)^(1/3)`.

For a fixed-width logarithmic shell, every fixed positive power in `X/R` beats those layer counts, yielding an order-one positive Euler gap throughout every fixed logarithmic margin below Ford height. At exact Ford scale `X/R=Theta(1)`, a vertical carrier of width `Theta(1)` still sees too many zeros in the final near-edge layer.

NB-224 shows that source width can pay for that missing localization. A nonnegative shell of logarithmic width `H=theta X`, normalized by `1/H`, keeps order-one source mass while narrowing the Fourier carrier to `1/H=Theta(1/X)`. Bellotti's local disk count then prices the shallow zero population by the horizontal depth itself, giving a constant positive-return gap all the way to the exact Ford denominator for a sufficiently small fixed Ford constant.

NB-225 proves the complementary method boundary. At exact Ford scale `R~X`, suppose `H=o(R)`. Then one can place an abstract packet of `M->infinity` simple near-one zeros with spacing `Theta(1/X)` and horizontal depth chosen so each residue has size `~1/M`. The whole packet lies inside one `1/H` carrier window, its moving-shell phases can be aligned exactly, and its total signed contribution stays order one. The packet remains compatible with all population-only inputs used by NB-223--NB-224: the Vinogradov--Korobov zero-free depth, Bellotti fixed/growing density, the local `O(K)` disk bound and ordinary local zero counting.

Therefore the present population information has a sharp width transition:

`H=Theta(X)` can reach exact Ford by NB-224, while every `H=o(X)` admits an order-one matched spectral packet under the same hypotheses.

This is not a theorem about the actual local configuration of zeta zeros. It is an information boundary on the current proof interface. To improve the sublinear-width endpoint one must add a genuinely joint theorem coupling horizontal depth to vertical window occupancy, or use phase-sensitive cancellation/correlation of the actual zero residues. Sharpening the same separate population bounds cannot distinguish the matched packet.

The reusable lesson is four-layered. Generic strip analyticity is sharp; source-specific singularity population beats that ambient extremizer; physical source width converts local zero counts into vertical localization; and below the linear-width threshold the missing resource is **joint depth-window or phase information**, not another absolute count.

**Boundary.** NB-225 is a method no-go for the population inputs used at the exact Ford endpoint. It does not assert that zeta contains the constructed packet, rule out phase cancellation for the true zeros, solve the fixed/sublinear-width endpoint by other information, give a Nyman--Beurling distance bound, or prove that every good approximant realizes the positive Euler-return observable.
