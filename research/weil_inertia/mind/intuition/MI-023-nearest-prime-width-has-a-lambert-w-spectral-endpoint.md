# MI-023 — Nearest-prime width has a Lambert-W spectral endpoint

**Evidence level:** exact for the one-signed, completely screened, symmetric two-island **nearest-prime width relaxation** through [WI-287](../../findings/WI-287-two-island-nearest-prime-width-has-a-lambert-w-endpoint.md). This is not a theorem for the full aperture-growing screening constraints, many-component supports, sign-changing modes or incomplete screening.

The growing-prime-family route has a sharp intermediate compression. If complete screening is reduced to the single consequence that the two-island half-width `b` must fit inside the nearest-prime gap, and an available prime interval theorem has length

`H(x)=sqrt(x) F(x)`,

then the bottom of Suzuki's prime-deleted gamma-plus-pole form over the resulting width-relaxed two-island class is

`lambda_width(x) = (1/2) log x - log F(x) - F(x) + O(1)`

whenever `F(x)->infinity` and `F(x)=O(log x)`.

The two competing terms have different origins and both are sharp at this level. Support of total width `O(b)` forces the gamma energy up by `log(1/b)+O(1)` through the Fourier `L^infinity` cap and a bathtub argument. On the symmetric two-island support, the pole form has an exact negative odd eigen-direction whose contribution is `-F(x)+O(1)` at the maximal allowed width. Their balance gives the transition equation

`F + log F = (1/2) log x`,

hence

`F_*(x)=W(sqrt(x))=(1/2)log x-log log x+log 2+o(1)`.

Therefore a width theorem with `F <= W(sqrt(x))-omega(1)` would force the entire width-relaxed prime-deleted form strictly positive, while `F >= W(sqrt(x))+omega(1)` still leaves explicit odd directions with Rayleigh quotient tending to `-infinity`. The square-root exponent is thus only the first-order boundary; at critical scale the decisive currency is the second-order Lambert-`W` gap.

This is a useful **compression audit** for the full WI-284 route. Nearest-prime width information alone can only prove the desired spectral contradiction if its quantitative scale crosses the Lambert-`W` endpoint. If available arithmetic input remains on the negative side, any successful complete-screening theorem must exploit information lost by the width compression: simultaneous avoidance of many prime-power lags, amplitudes from the actual null equation, multi-component restrictions, or another collective source coupling.

The open adversarial review on WI-286 concerns the exact current unconditional short-interval exponent/evidence tier, not the abstract square-root mechanism. This intuition therefore does not encode a disputed numerical best-known exponent. Its load-bearing statement is WI-287's exact conditional formula for arbitrary `F` in the stated width interface.

**Boundary.** The negative side of WI-287 constructs profiles satisfying only the scalar nearest-prime width cap; it does not construct a support that screens all active prime powers. The positive side covers only symmetric two-island completely screened supports after this compression. No unconditional prime-gap theorem is asserted here to reach the positive Lambert-`W` side, and no RH conclusion follows from the width relaxation by itself.