# MI-041 — Smooth common-modulus rigidity and ordinary interval cancellation both stop before the dyadic prime-shell gate

**Evidence level:** literature-assisted source-specific resolution boundary from [MC-319](../../findings/MC-319-smooth-modulus-zero-free-dyadic-resolution-barrier.md), sharpened by the exact matched obstruction [MC-320](../../findings/MC-320-smooth-modulus-interval-cancellation-prime-shell-conductor-inflation.md).

The endpoint coding program forces a natural common radical modulus rather than an arbitrary binary matrix. In the balanced regime `2^R asymp log y`, with the source primes restricted to the natural scale `Z<=y^(1/R)`, the common modulus `q=4P` is extremely smooth: its largest prime factor is small relative to `log q`. This is enough to enter the Koukoulopoulos--Maynard--Tao/Chang smooth-modulus zero-free machinery for the whole Dirichlet-character family modulo `q`.

The resulting analytic information is genuinely arithmetic. Apart from at most one exceptional real character, the product of the Dirichlet `L`-functions modulo `q` has a strong zero-free strip. But MC-319 shows that the known Rodosskii-type conversion controls harmonic prime sums only over broad power intervals at scale roughly `O((loglog q)^(-1/2))`, whereas the endpoint needs one-dyadic-shell resolution with signal around `1/log y` and exponent width `Theta(1/log y)`.

MC-320 removes the most tempting workaround. There are source-scale-matched smooth moduli `q=4P` and characters induced from the primitive conductor-`4` character such that

`sup_(M,H>=y^alpha) |sum_(M<n<=M+H) chi(n)| / H -> 0`

for every fixed `alpha>0`—indeed the raw interval sums are only polylogarithmic at the critical rank—while on primes `y<p<=2y`, `p=1 mod 4`, the same character is identically `+1`. Its weighted prime sum is `y/2+o(y)` and its harmonic shell signal is `(log 2)/(2 log y)+o(1/log y)`, exactly the scale the endpoint must distinguish.

So the missing information is not generic “more cancellation.” **Ordinary interval discrepancy can be almost perfect while the prime-restricted destination remains maximally biased.** The MC-320 control differs from the actual endpoint family in the primitive arithmetic source: its large modulus is conductor inflation around a primitive conductor of `4`, whereas the endpoint characters are primitive quadratic characters assembled from lower-prime source products and forced source-cost profiles.

The next useful theorem must therefore be prime-sensitive and provenance-sensitive. It could combine primitive conductor size/factorization, the multiquadratic family relation and common-modulus smoothness to obtain a dyadic `Lambda`/prime-shell estimate for an endpoint-biased nonexceptional mode. A result depending only on the inflated common modulus, its zero-free region, or unweighted sums `sum chi(n)` cannot distinguish the matched control.

The reusable lesson is precise: **analytic rigidity must be converted in the exact observation category consumed by the endpoint**. Zero-free control is not a destination estimate; neither is strong cancellation on integers when the destination samples primes. Preserve primitive source provenance until after the prime-weighted shell estimate is obtained.

**Boundary.** MC-319--MC-320 do not prove that the required primitive-conductor dyadic theorem is impossible. MC-320 is deliberately imprimitive and therefore does not model the load-bearing source feature. The possible exceptional real character and the exact distribution of primitive conductors across endpoint-biased modes remain part of any positive argument.