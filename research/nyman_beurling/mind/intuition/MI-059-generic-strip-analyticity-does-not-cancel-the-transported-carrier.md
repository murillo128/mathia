# MI-059 — Generic strip analyticity is sharp, but near-one zero density beats it on the actual zeta carrier

**Evidence level:** exact synthesis from [NB-221](../../findings/NB-221-flat-soft-primitive-windows-factor-through-local-log-derivative-contour.md), [NB-222](../../findings/NB-222-strip-analyticity-alone-cannot-improve-carrier-contour-gain.md), and [NB-223](../../findings/NB-223-near-edge-zero-density-gives-constant-euler-gap-within-every-log-epsilon-of-ford-scale.md), building on the exact source/kernel coupling of NB-218--NB-220.

NB-221 removes the artificial costs of fixed-depth primitivization, global vertical acquisition and remote-zero transport. After faithful localization and a safe finite contour shift, every fixed primitive depth has the same leading term: a carrier-frequency convolution of the local logarithmic derivative `-zeta'/zeta`. The remaining pointwise proof pays the Vinogradov--Korobov envelope after the contour factor has already been gained.

NB-222 asks whether the rapid carrier itself can force more cancellation from nothing beyond holomorphy and boundedness in that zero-free strip. For the exact moving-shell transform and the same flat windows, the answer is no. If `F` is bounded by `M` in a strip of height `eta`, the carrier functional has operator norm

`Theta(M e^(-X eta))`.

A bounded entire exponential with frequency matched to the source shell attains the lower bound. The same extremizer also satisfies the whole Cauchy derivative envelope `|F^(m)| <= m! M eta^(-m)`, so repeated integration by parts cannot extract an additional uniform factor from generic strip regularity.

NB-223 demonstrates that this method boundary is sharp in the useful sense: the **actual zeta carrier has additional spectral structure that does improve the theorem**. Shift the smooth carrier globally across the nontrivial zeros instead of bounding it pointwise inside the zero-free strip. The resulting main term is controlled by

`sum_rho m(rho) e^(-X(1-beta)) (1+|gamma-t|)^(-A)`.

The shell supplies the exponential distance weight; Bellotti's near-one zero-density theorem supplies the missing arithmetic restriction on how many zeros can lie in layers `1-beta~K/R`, where

`R=(log |t|)^(2/3)(log log |t|)^(1/3)`.

A finite layer decomposition shows that every fixed positive power in the ratio `X/R` beats the allowed near-one zero population. Thus for any fixed `d>0`,

`X/R >= (log log |t|)^d`

forces the twisted smooth Euler barycenter to be `o(1)`. Equivalently, for every fixed `epsilon>0` and `kappa>0`, one gets uniform decay throughout

`log |t| <= kappa X^(3/2)/(log X)^(1/2+epsilon)`.

For a nonnegative shell this converts into an order-one positive-return gap on the same range. The previous log-squared corridor was therefore not a source barrier: it was the cost of replacing a discrete arithmetic zero spectrum by the generic pointwise strip envelope.

The endpoint also becomes clearer. At the formal Ford scale `log |t| ~ X^(3/2)/(log X)^(1/2)`, one has only `X/R=Theta(1)`. Bellotti controls every near-one layer depth `(log log T)^alpha` with fixed `alpha<1`, but the final untreated population lives at depth comparable with `log log T`. Absolute counting can no longer be beaten by the fixed exponential weight. Reaching the endpoint requires either stronger control of that last layer or cancellation among the weighted zero phases themselves.

The reusable lesson is now two-sided. **Generic strip analyticity is genuinely exhausted**, so more contour manipulation using only the same bounded analytic class is futile. But that does not mean the transported carrier is exhausted: once the proof retains the actual singularity distribution of `-zeta'/zeta`, zeta-specific density information can beat the matched analytic extremizer and materially extend the source theorem.

**Boundary.** NB-223 is still a source-side theorem. It does not prove the exact Ford endpoint, a quantitative Nyman--Beurling distance bound, or that every good Nyman approximant realizes the positive Euler-return observable. Its gain uses zero population rather than zero-phase cancellation, and the final `log log T`-deep layer remains unresolved.
