# MI-041 — Smooth-modulus zero-free control stops above the dyadic shell scale

**Evidence level:** literature-assisted source-specific resolution boundary from [MC-319](../../findings/MC-319-smooth-modulus-zero-free-dyadic-resolution-barrier.md).

The endpoint coding program forces a natural common radical modulus rather than an arbitrary binary matrix. In the balanced regime `2^R asymp log y`, with the source primes restricted to the natural scale `Z<=y^(1/R)`, the common modulus `q=4P` is extremely smooth: its largest prime factor is small relative to `log q`. This is enough to enter the Koukoulopoulos--Maynard--Tao/Chang smooth-modulus zero-free machinery for the whole Dirichlet-character family modulo `q`.

The resulting analytic information is genuinely arithmetic. Apart from at most one exceptional real character, the product of the Dirichlet `L`-functions modulo `q` has a zero-free strip of width on the order of `loglog q/log q`. Thus the common-radical source does satisfy a strong family rigidity that generic `[2R,R]` coding controls do not encode.

But this still does not reach the endpoint signal. The available Rodosskii-type conversion controls harmonic prime sums over broad power intervals only at scale roughly

`O((loglog q)^(-1/2))`.

The source-incidence endpoint needs resolution on one dyadic shell with signal around `1/log y`, while the relevant exponent width is itself only `Theta(1/log y)`. The existing zero-free theorem therefore proves rigidity at the wrong resolution: its prime-sum consequence is much larger than the quantity that must be separated.

The reusable lesson is precise: **a zero-free region is not a destination estimate until its conversion theorem has the spatial/scale resolution consumed by the endpoint**. Here the smooth modulus crosses the analytic zero-free gate but fails the dyadic-resolution gate. The next useful theorem would be a genuinely dyadic character-prime estimate, or another collective modulus relation, strong enough at the endpoint scale without importing a Mertens-sized conclusion.

**Boundary.** MC-319 does not prove that such a dyadic theorem is impossible. It identifies the quantitative mismatch in currently available smooth-modulus technology. The exceptional real character and the exact source-to-character reduction still have to be handled in any positive result.