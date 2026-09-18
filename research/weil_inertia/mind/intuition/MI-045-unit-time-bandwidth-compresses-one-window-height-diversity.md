# MI-045 — Bounded source aperture compresses linear height diversity

**Evidence level:** exact synthesis from [WI-328](../../findings/WI-328-bow-ordinates-are-twist-frozen-on-cubic-source-blocks.md) through [WI-344](../../findings/WI-344-fixed-source-aperture-compresses-all-linear-height-windows.md). The general time--bandwidth/Taylor approximation principle is classical; the Mathia content is its exact quantitative realization on the WI-195 source geometry and its stability under bounded height-independent linear preprocessing.

A bow can contain a power-growing number of zero ordinates without providing a comparable number of independent linear arithmetic probes. More generally, if the physical source lies in a log-coordinate interval of width `Delta` and the selected heights occupy a span `H`, the carrier family `c_U(n)=n^(iU)` has effective linear complexity controlled by the time--bandwidth product `H Delta`, not by the number of sampled heights.

WI-344 gives the quantitative form. After centering the source interval, degree-`d` Taylor expansion puts every carrier in a common `(d+1)`-dimensional subspace up to relative error

`epsilon_d=(H Delta/4)^(d+1)/(d+1)!`.

This statement holds for arbitrary finite nonnegative source weights and survives any bounded height-independent linear map applied to the source coordinates. If the resulting outputs are normalized and the map transmits each carrier at relative scale at least `eta`, the normalized Gram spectral tail beyond rank `d+1` is at most `m(epsilon_d/eta)^2`. A linear preprocessing step can expose the tiny residual directions only by paying for them in transmission scale.

The natural Gallagher window is the sharp fixed-aperture example: `H Delta=1`. Centering improves the earlier left-endpoint bound dramatically; at `d=6`, every carrier is within `1/82575360` of a seven-dimensional common span before normalization. Thus even a power-growing height portfolio cannot produce extensive scale-preserving linear diversity from one fixed physical aperture.

The relevant resource is therefore **effective carrier dimension together with transmitted amplitude at the physical source aperture**. Counting spectral parameters is misleading when all their source-side carriers lie in the same low-dimensional approximation tube. A badly conditioned linear map that amplifies the residual does not evade the obstruction unless the destination still receives that residual at a useful scale after normalization.

Height diversity can become a genuinely new resource only by changing a hypothesis that enlarges or bypasses this budget: make total `H Delta` grow, couple different apertures or scales, let the coefficient bank depend essentially on height or arithmetic source structure, use a nonlinear observable that is not a fixed linear image of the carrier family, or prove the distinguished signed covariance directly.

**Boundary.** The result concerns linear carrier families on bounded logarithmic source aperture and bounded height-independent linear preprocessing. It does not bound exact algebraic rank, rule out height-dependent or arithmetic coefficient banks, classify nonlinear/cross-scale observables, control off-critical zero equations, remove exceptional source starts, or prove the WI-195 covariance target or RH. A growing aperture with `H Delta->infinity` remains outside the fixed-budget obstruction.
