# MI-059 — Generic strip analyticity is sharp, while zeta-specific localization trades source width for Ford-scale reach

**Evidence level:** exact synthesis from [NB-221](../../findings/NB-221-flat-soft-primitive-windows-factor-through-local-log-derivative-contour.md) through [NB-224](../../findings/NB-224-log-wide-shell-converts-local-zero-counts-into-exact-ford-gap.md), building on the exact source/kernel coupling of NB-218--NB-220.

NB-221 removes the artificial costs of fixed-depth primitivization, global vertical acquisition and remote-zero transport. After faithful localization and a safe finite contour shift, every fixed primitive depth has the same leading term: a carrier-frequency convolution of the local logarithmic derivative `-zeta'/zeta`.

NB-222 asks whether the carrier itself can force more cancellation from nothing beyond holomorphy and boundedness in a zero-free strip. For the exact moving-shell transform the answer is no. If `F` is bounded by `M` in a strip of height `eta`, the carrier functional has operator norm

`Theta(M e^(-X eta))`,

and a carrier-matched entire exponential attains the lower bound. Generic strip regularity, even with the full Cauchy derivative envelope, is therefore exhausted.

NB-223 shows that the actual zeta carrier has additional spectral structure. Moving the contour across the nontrivial zeros produces the weighted sum

`sum_rho m(rho) e^(-X(1-beta)) (1+|gamma-t|)^(-A)`.

Bellotti's near-one density theorem controls the population in layers `1-beta~K/R`, where

`R=(log |t|)^(2/3)(log log |t|)^(1/3)`.

For a fixed-width logarithmic shell, every fixed positive power in `X/R` beats those layer counts, yielding an order-one positive Euler gap throughout every fixed `log^epsilon` margin below Ford height. At exact Ford scale `X/R=Theta(1)`, that argument stalls because a carrier of vertical width `Theta(1)` still sees too many zeros in the final near-edge layer.

NB-224 shows that this is not a universal endpoint obstruction; it is coupled to source resolution. Take a nonnegative shell of logarithmic width `H=theta X`, normalized by `1/H`. Its source mass stays order one, but its Fourier carrier becomes `e^(iXv)F(Hv)` and narrows to vertical scale `1/H=Theta(1/X)`. Bellotti's local disk bound then prices the shallow zero population by the horizontal depth `K` itself. At fixed sufficiently large `Y=X/R`, the resulting residue sum is exponentially small in `Y`, so a constant positive-return gap survives all the way to

`log |t| <= kappa_0 X^(3/2)/(log X)^(1/2)`

for a sufficiently small fixed `kappa_0>0`.

The price is equally structural. A shell of width `theta X` occupies an integer range roughly `[e^X,e^((1+theta)X)]`. Exact-Ford reach has been purchased by sacrificing multiplicative localization. NB-224 therefore does not settle the fixed-width endpoint from NB-223; it reveals a **source-width/carrier-width tradeoff**.

The reusable lesson is three-layered. Generic strip analyticity is genuinely sharp. Source-specific singularity population can beat that ambient extremizer. And once zero information is local in the vertical coordinate, physical source width becomes a controllable localization resource: wider source support creates a narrower carrier that can convert local zero counts into stronger height reach. Any claimed gain must price the resulting loss of destination resolution.

The next meaningful question is not another contour refinement. It is whether the exact Ford gap can be retained with fixed or sublinear logarithmic source width, or whether one can prove an optimal width-versus-Ford-constant law. If fixed width is intrinsically insufficient for population-only arguments, the remaining source-side option is phase cancellation in the weighted zero sum rather than further absolute counting.

**Boundary.** NB-224 is still source-side. It reaches the exact Ford denominator only for a proportional log-width shell and sufficiently small fixed Ford constant. It does not solve the fixed-width endpoint, give a Nyman--Beurling distance bound, or show that every good approximant realizes the positive Euler-return observable.