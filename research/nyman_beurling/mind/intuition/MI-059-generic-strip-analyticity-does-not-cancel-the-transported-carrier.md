# MI-059 — Generic strip analyticity does not cancel the transported logarithmic-derivative carrier

**Evidence level:** exact synthesis from [NB-221](../../findings/NB-221-flat-soft-primitive-windows-factor-through-local-log-derivative-contour.md) and [NB-222](../../findings/NB-222-strip-analyticity-alone-cannot-improve-carrier-contour-gain.md), building on the exact source/kernel coupling of NB-218--NB-220.

NB-221 removes the artificial costs of fixed-depth primitivization, global vertical acquisition and remote-zero transport. After faithful localization and a safe finite contour shift, every fixed primitive depth has the same leading term: a carrier-frequency convolution of the local logarithmic derivative `-zeta'/zeta`. The remaining pointwise proof pays the Vinogradov--Korobov envelope after the contour factor has already been gained.

NB-222 asks whether the rapid carrier itself can force more cancellation from nothing beyond holomorphy and boundedness in that zero-free strip. For the exact moving-shell transform and the same flat windows, the answer is no. If `F` is bounded by `M` in a strip of height `eta`, the carrier functional has operator norm

`Theta(M e^(-X eta))`.

A bounded entire exponential with frequency matched to the source shell attains the lower bound. The same extremizer also satisfies the whole Cauchy derivative envelope `|F^(m)| <= m! M eta^(-m)`, so repeated integration by parts cannot extract an additional uniform factor from generic strip regularity.

The important point is not that the actual logarithmic derivative attains this extremum. It is that a proof which forgets its arithmetic coefficient constraints cannot distinguish it from an admissible carrier-matched extremizer. The Euler expansion contains precisely the matching phase family `e^(-iv log n)`, but with amplitudes fixed by `Lambda(n)n^-s`; any real improvement has to use those amplitudes or another zeta-specific restriction rather than the existence of the oscillatory carrier alone.

The reusable lesson is that **faithful transport can isolate the correct signed analytic carrier while generic analyticity still supplies no cancellation theorem for it**. Once representation and contour artifacts have been removed, the next proof interface should be frequency-localized and arithmetic: an estimate for the actual projection of `-zeta'/zeta`, a spectral norm incompatible with concentration in one shell-matched frequency, or another source-specific constraint.

**Boundary.** NB-222 is a sharp method boundary for the bounded analytic strip class, not a lower bound for the actual `-zeta'/zeta` integral. It does not exclude cancellation coming from Euler coefficients, zero correlations or another arithmetic spectral theorem. It also does not improve the Nyman distance by itself; it says only which remaining information a successful proof must use.