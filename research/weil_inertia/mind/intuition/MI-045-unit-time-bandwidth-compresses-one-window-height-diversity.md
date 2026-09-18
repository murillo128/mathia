# MI-045 — Unit time--bandwidth compresses one-window height diversity

**Evidence level:** exact synthesis from [WI-328](../../findings/WI-328-bow-ordinates-are-twist-frozen-on-cubic-source-blocks.md) through [WI-343](../../findings/WI-343-natural-gallagher-window-has-bounded-height-carrier-dimension.md). The general time--bandwidth principle is classical; the Mathia content is its exact quantitative realization on the WI-195 Gallagher window.

A bow can contain a power-growing number of zero ordinates without providing a comparable number of independent linear arithmetic probes. On the natural multiplicative Gallagher window, the source log-coordinate has width `delta=1/H` while the selected heights occupy a span at most `H`. The carrier family `c_U(n)=n^(iU)` therefore has exact time--bandwidth product one.

This yields two source-independent compression statements. Any two normalized carriers from the same bow satisfy

`|<c_U,c_V>| >= cos(1/2)`

for arbitrary nonnegative source weights. More strongly, after removing one fixed carrier, Taylor expansion in the local log coordinate puts every height carrier within relative distance `1/(d+1)!` of a fixed `(d+1)`-dimensional span. At `d=6`, an arbitrarily large portfolio is within `1/5040` of a seven-dimensional carrier space, and its Gram spectral tail beyond rank seven is at most `m/5040^2`.

The relevant resource is therefore **effective carrier dimension at the physical source aperture**, not the number of available spectral heights. WI-328 already showed that on a shorter cubic source block the bow is asymptotically twist-frozen; WI-329 showed that the natural-window arithmetic theorem has one common phase-uniform exceptional set; WI-330 showed that sub-square-root height diversity does not create many Riemann--Siegel source cells. WI-343 now shows that even at the first order-one dephasing window, the linear height portfolio remains bounded-dimensional in a quantitative approximation sense.

This closes any amplification argument that treats many bow ordinates on one fixed Gallagher window as independent linear samples merely because their phases differ. Separate estimates at many heights would still need additional arithmetic decorrelation; independence is not supplied by the carrier geometry itself.

Height diversity can become a new resource only by changing something that increases or bypasses the one-window time--bandwidth budget: use genuinely different source starts/windows, widen the logarithmic aperture so `H delta` grows, introduce cross-window covariance, make the observable depend nonlinearly on the source/carrier pair, or prove the distinguished signed covariance directly. Counting more nearby ordinates without one of these changes is representational multiplicity, not new information.

**Boundary.** The bounded approximate dimension is a statement about the linear carriers on one natural Gallagher window. It does not bound the exact algebraic rank, rule out arithmetic coefficient-dependent decorrelation, classify nonlinear or cross-window observables, control off-critical zero equations, remove the exceptional source starts, or prove the WI-195 covariance target or RH.
