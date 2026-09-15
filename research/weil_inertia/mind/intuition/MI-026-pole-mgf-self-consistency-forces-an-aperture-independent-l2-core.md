# MI-026 — Pole MGF self-consistency forces an aperture-independent L2 core

**Evidence level:** exact one-signed complete-screening rigidity from [WI-297](../../findings/WI-297-pole-mgf-tightness-forces-a-bounded-l2-core.md), sharpening the global `L^1` mass floor in [WI-296](../../findings/WI-296-gamma-pole-self-consistency-forces-an-l1-mass-floor.md)

For a normalized one-signed completely screened first-crossing null mode `v>=0`, put `M=||v||_1`, `s=M^2` and normalize the positive measure

`dnu(x)=v(x)dx/M`.

WI-296 uses the exact gamma bathtub `H(s)` and the pole lower bound only to obtain `H(s)+2s<0`. WI-297 retains the full pole factorization

`P_a(v)=2 L_-(v)L_+(v)`

and divides by the same mass `s`. If `X~nu`, then

`E exp(X/2) E exp(-X/2) < kappa_*`,

where

`kappa_*=max_(u in S) [-H(u)/(2u)]`

on the exact candidate-admissible set `S={u in (0,log 2]: H(u)+2u<=0}`.

For independent `X,Y~nu`, the product is

`E cosh((X-Y)/2)`.

Since `cosh t >= 1+t^2/2`, this gives the aperture-independent variance bound

`Var_nu(X) < 4(kappa_*-1)`.

Chebyshev and the WI-296 mass floor then force a fixed interval of radius

`R_*=sqrt(8(kappa_*-1))`

to carry more than half of the `L^1` mass and a universal positive fraction `q_*>0` of the normalized `L^2` mass. After a natural exponential-moment recentering, the same MGF identity gives two-sided `L^1` tails bounded by `sqrt(kappa_*) exp(-R/2)`.

Thus the earlier sparse-satellite escape is much narrower than a global mass floor suggests. The exact null identity forces an **aperture-independent nonvanishing core**, while any remote support used to maintain full essential span can carry only exponentially small normalized `L^1` mass after recentering.

The remaining gate is local-to-global propagation. To close the branch one needs a source/null-equation theorem saying that a full-span screened first mode must transport a fixed positive amount of `L^1` or `L^2` mass across successive distant cuts; such propagation would collide directly with the exponential pole-tail budget. Another global uncertainty inequality is not the missing resource.

**Boundary.** The probability normalization uses `v>=0`, and complete screening is load-bearing in the prime-deleted null identity. The theorem does not cover sign-changing first modes or incomplete screening, does not rule out arbitrarily weak satellites, and does not itself prove the required propagation from the forced core to remote support.