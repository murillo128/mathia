# MI-043 — Low-degree endpoint weighting cannot see the half-loaded source band

**Evidence level:** exact source-specific synthesis from [MC-327](../../findings/MC-327-quartic-saturation-forces-half-loaded-source-mass.md) and [MC-328](../../findings/MC-328-low-degree-endpoint-reweighting-half-loading-blindness.md), using classical Walsh--Fourier/Krawtchouk structure on the Hamming cube. No estimate for `M(x)` or RH consequence is claimed.

At quartic saturation the actual common source package is already forced into the central Hamming region: MC-327 gives `B_R->0`, so asymptotically all logarithmic source mass lies on columns whose occupancy is `R/2+o(R)`. The remaining hope was that the endpoint coefficient itself might provide a nonnegative mode weighting that preferentially avoids those arithmetic columns.

MC-328 identifies the exact obstruction. With

`x(a)=(-1)^|a|(1-2|a|/R)`,

any polynomial weight `w(a)=F_R(x(a))` of degree `d_R` has Walsh support only at source characters of Hamming weight at most `d_R` or at least `R-d_R`. Therefore every source column with

`d_R < |s| < R-d_R`

is invisible to the nonconstant Fourier content of the weight and has exact loading

`ell_w(s)=1/2+w_0/(2W) >= 1/2`.

When `d_R=o(R)`, MC-327 places `1-o(1)` of the actual logarithmic source mass precisely in this blind band. Hence positive low-degree endpoint reweighting cannot improve the half-loading constant. Fixed even moments are especially sharp controls: they can concentrate almost all mode weight on near-quadratic-conductor directions while still producing aggregate source loading `1/2+o(1)`, so the conductor accounting returns exponent four and no more.

The surviving resource is not another smooth or fixed-order function of the endpoint coefficient. To distinguish the economical arithmetic source inside the central band, a weighting must carry Fourier degree comparable to the central Hamming scale, or use arithmetic information not expressible through the endpoint scalar alone. Equivalently, one needs a genuinely joint/signed conductor law, a stronger individual conductor horizon, or a different source representation.

**Falsification criterion.** A proposed endpoint-only positive reweighting beats the quartic source floor only if its Fourier support reaches the source columns that carry asymptotic logarithmic mass, or if the actual source is proved to avoid that band. MC-327 rules out the second option at quartic saturation, and MC-328 rules out the first for degree `o(R)` endpoint polynomials.
