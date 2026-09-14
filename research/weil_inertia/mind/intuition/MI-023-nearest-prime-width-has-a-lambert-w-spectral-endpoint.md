# MI-023 — Nearest-prime width has a Lambert-W spectral endpoint

**Evidence level:** exact for the one-signed, completely screened, symmetric two-island **nearest-prime width relaxation** through [WI-287](../../findings/WI-287-two-island-nearest-prime-width-has-a-lambert-w-endpoint.md), with the growing-family width input of [WI-286](../../findings/WI-286-growing-prime-screening-hits-a-square-root-gap-threshold.md). The peer-reviewed Baker--Harman--Pintz exponent `0.525` and Runbo Li's stronger `0.52` preprint claim both remain on the negative side of the square-root transition. This is not a theorem for full screening, many-component supports, sign-changing modes or incomplete screening.

The growing-prime-family route has a sharp intermediate compression. If complete screening is reduced to the single consequence that the two-island half-width `b` must fit inside the nearest-prime gap, and an available prime interval theorem has length

`H(x)=sqrt(x) F(x)`,

then the bottom of Suzuki's prime-deleted gamma-plus-pole form over the resulting width-relaxed two-island class is

`lambda_width(x) = (1/2) log x - log F(x) - F(x) + O(1)`

whenever `F(x)->infinity` and `F(x)=O(log x)`.

The two competing terms have different origins and are sharp at this compression level. Support of total width `O(b)` forces gamma energy up by `log(1/b)+O(1)` through Fourier uncertainty; on the symmetric two-island support the pole form has an exact negative odd direction whose contribution is `-F(x)+O(1)` at maximal allowed width. Their balance gives

`F + log F = (1/2) log x`,

hence

`F_*(x)=W(sqrt(x))=(1/2)log x-log log x+log 2+o(1)`.

Therefore a width theorem with `F <= W(sqrt(x))-omega(1)` forces the entire width-relaxed prime-deleted form strictly positive, while `F >= W(sqrt(x))+omega(1)` still leaves explicit odd directions with Rayleigh quotient tending to `-infinity`. The square-root exponent is only the first-order boundary; at critical scale the decisive currency is the second-order Lambert-`W` gap.

WI-286 supplies the current concrete arithmetic calibration. Baker--Harman--Pintz gives the peer-reviewed interval exponent `theta=0.525`, hence width decay exponent `0.475`. Li's current preprint claim `theta=0.52` improves that decay to `0.48`. Both leave a positive exponential pole-growth allowance (`0.025` and `0.02` respectively) and therefore do not cross even the strict square-root threshold through the nearest-prime interface. The preprint improves the numerical miss; it does not alter the qualitative endpoint.

This is a **compression audit** for the full WI-284 route. Nearest-prime width information alone can only prove the desired spectral contradiction if its quantitative scale crosses the Lambert-`W` endpoint. If available arithmetic input remains on the negative side, any successful complete-screening theorem must exploit information lost by the compression: simultaneous avoidance of many prime-power lags, amplitudes from the actual null equation, multi-component restrictions, or another collective source coupling.

**Boundary.** The negative side constructs profiles satisfying only the scalar nearest-prime width cap; it does not construct a support that screens all active prime powers. The positive side covers only symmetric two-island supports after this compression. No current unconditional prime-gap theorem is asserted to reach the positive Lambert-`W` side, and no RH conclusion follows from the width relaxation by itself.