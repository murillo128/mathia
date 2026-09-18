# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Treat the moving lower-source branch as closed after exact gamma recentering

**Linked intuitions:** `MI-029-fixed-margin-pair-correlation-accuracy-must-outrun-packet-conditioning` through `MI-039-wang-lower-source-crossover-is-resolution-dependent`.

VIS-282--VIS-286 classify the isolated coefficient-scale profile and its two source boundaries. VIS-287--VIS-291 then move to Wang's complete pair statistic and show that on every compact power panel `x=T^beta`, `0<beta_0<=beta<=beta_1<theta`, the leading law is uniformly linear after the explicit gamma contribution is retained, with the squared-von-Mangoldt remainder controlled by the standard Korobov--Vinogradov PNT envelope. VIS-292 shows that the symmetric log-source Green filter has no exact blind frequency, and VIS-293 shows that first-half-plane holomorphy of the exact source transform is RH-equivalent rather than an independent continuation mechanism.

VIS-294--VIS-297 progressively narrowed the apparent lower moving-source boundary. They separated absolute from relative resolution, isolated the finite relative crossover, and identified its remaining order-one mean as deterministic gamma normalization rather than new arithmetic.

VIS-298 closes the entire moving lower-source branch at absolute `H` resolution under one fixed theorem ceiling. With `H=T^theta`, `L=log T`, fixed `lambda<theta`, and every `x=x(T)->infinity` satisfying `x<=T^lambda`, exact recombination of the Landau/gamma decomposition gives

`F_I(x)=(H/(2pi))[log x+(L-log(2pi))^2/x^2]+o(H)`.

The earlier `x~sqrt(L)` boundary was therefore not an intrinsic arithmetic crossover. It arose from packaging the gamma term inside a coarse remainder and then applying norm bounds before exploiting the exact frequency structure. Once the gamma term is recentered and the absolutely convergent right-half-plane zeta term is handled at its actual frequencies, no moving `x->infinity` lower-source transition remains at absolute `H` scale.

The active source questions are now different. On the **fixed-power real-axis branch**, can one improve or structurally refine the genuinely arithmetic source envelope using information strictly weaker than the RH-equivalent continuation of VIS-293? On the **upper source ceiling**, can Wang's theorem be made quantitatively uniform as the source exponent approaches `theta`, rather than keeping one fixed `lambda<theta`? A genuinely bounded source `x=O(1)` is separate and should be reopened only if it exposes information not already classified by the fixed-source findings.

## Recombine exact deterministic structure before interpreting an error wall

The current ledger separates packet total variation, support width, moving-test seminorm, source exponent, requested output scale, prime-power source measure, smoothing multiplier, theorem-uniformity range, explicit-formula remainder, deterministic gamma normalization and analytic domain of the source Dirichlet transform.

VIS-294--VIS-298 give a particularly sharp methodological warning. A nominal error boundary can disappear when terms that were split only for estimation convenience are recombined before Cauchy--Schwarz or supremum bounds are applied. The scales `sqrt(log T)` and `sqrt(log T/log log T)` were useful bookkeeping thresholds in the coarse proof, but they do not survive as moving arithmetic regimes of the exact statistic under the fixed-ceiling assumptions.

A useful next probe must therefore identify a residual that survives **after** exact deterministic normalization and recombination. Merely choosing a slower moving `x(T)->infinity`, or reinterpreting a coarse `H`-scale error term as source structure, is already ruled out. The unresolved information lies in arithmetic improvement at fixed source scale/power or in genuinely new uniformity near the upper theorem boundary.