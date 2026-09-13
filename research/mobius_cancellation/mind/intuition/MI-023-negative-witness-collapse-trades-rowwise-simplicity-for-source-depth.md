# MI-023 — Negative witnesses aggregate cheaply; normalization is an OR barrier

**Evidence level:** proved for the flat Christoffel source by [MC-273](../../findings/MC-273-christoffel-negative-witness-homogeneous-collapse.md), [MC-274](../../findings/MC-274-negative-witness-conditioning-fourier-depth-tax.md) and [MC-275](../../findings/MC-275-witness-normalization-approximate-degree-barrier.md). No low-degree theorem on the actual localized Legendre-shell image or endpoint cancellation estimate is claimed.

MC-273 gives an exact rowwise simplification. If a target sign vector has a negative lower-prime coordinate `i`, then

`g_m(x)=sum_(|S|<=m)x_S=e_m(x_hat_i)`.

MC-274 shows that selecting such witnesses atom by atom can be expensive: conditioning through query depth `J` raises the Walsh/source degree of the energy from `2m` to `2m+J`, and resolving an atom-scale family naturally asks for `J` much larger than the original `m=Theta(log log y)`.

MC-275 corrects the over-broad reading of that obstruction. Witness **aggregation itself is cheap**. Writing `b(x)` for the number of negative coordinates,

`U_m(x)=sum_i n_i(x)e_m(x_hat_i)=b(x)g_m(x)`

and

`U_m=1/2[(k-m)e_m-(m+1)e_(m+1)]`.

Thus all negative witnesses can be retained simultaneously with only one extra source degree. No decision tree or first-witness choice is required.

The hard operation is dividing away the multiplicity `b`. An exact normalized decomposition must sum to the nonblind selector `NB=1_(b>0)`, whose multilinear representation is

`NB(x)=1-2^(-k) prod_i(1+x_i)`.

Hence exact polynomial normalization has degree `k`. The symmetric `1/b` normalization has the same endpoint cost: polynomial interpolation on `b=1,...,k` needs degree at least `k-1`. Even approximate normalization is generically expensive because `NB` is OR: uniform error `epsilon` needs degree `Theta(sqrt(k log(1/epsilon)))`. Constant error already exceeds the live Christoffel depth, while atom-sensitive error is parametrically worse.

So the endpoint distinction is now three-way: **rowwise collapse is cheap, overlapping witness use is cheap, generic normalization/classification is expensive**. A useful continuation must avoid reconstructing OR on the full cube. It can instead exploit the tightly localized Legendre-shell image, prove a distributional surrogate only on that arithmetic image, or use the signed aggregate `b g_m` directly without division.

MC-252 is the matched control. Once the upper primes are allowed to separate from the moving shell, genuine Legendre-symbol configurations realize the full Boolean cube. Therefore a low-depth escape cannot follow merely from quadratic reciprocity or primality; it must use the tight source-size coupling that the separated-prime control destroys.

**Boundary.** The approximate-degree theorem is a worst-case full-cube obstruction, not a lower bound on the actual localized arithmetic image. MC-275 does not rule out distributional approximation or signed identities that never normalize witness multiplicity. Nothing here excludes blind support or improves `M(X)`.
