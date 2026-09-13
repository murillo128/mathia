# MI-012 — Robin's direct sparse-host route is now a shifted four-zero/phase-kernel problem

**Evidence level:** the host-to-frontier conversion is exact through [RE-095](../../findings/RE-095-source-conditioned-sampled-gap-sparsity-lowers-the-depth-two-moment-frontier.md); [RE-096](../../findings/RE-096-depth-two-bad-hosts-reduce-to-a-phase-stable-deformed-quadratic-sequence.md) gives the all-integer deformed-quadratic host reduction and phase geometry; [RE-097](../../findings/RE-097-bazzanella-quadratic-threshold-is-ambient-packing-not-phase-control.md) proves that ambient exceptional-set packing cannot improve the Robin envelope; and [RE-098](../../findings/RE-098-resonant-four-zero-energy-already-clears-the-robin-host-window.md) shows that known near-resonant four-zero additive energy already crosses the required Robin exponent window. The shifted/nonresonant fourth-moment term remains open.

After the higher-depth reductions, the residual mixed first/depth-two cells are sampled at

`x(n)=eta_1^(-1)(eta_2(n))`, `n~X^(1/2)`.

RE-095 shows that any fixed power saving in the bad-host count at interval length `X^vartheta`, with `vartheta<73/200`, lowers the `173/200` frontier. RE-096 shows that the analytic upper bound may enlarge to all integer hosts and that the logarithmic phase remains quadratically stable even though the physical displacement from `n^2/2` is large.

RE-097 separates ambient packing from genuine sparse-sample information. Bazzanella's published quadratic `13/32` threshold in the relevant range comes from embedding sparse exceptions into an ordinary ambient PNT exceptional set. That mechanism transfers to the CA sample by spacing but cannot improve Robin beyond the existing ambient frontier. The useful quadratic analogy must therefore enter through a direct phase-sensitive estimate.

RE-098 tests the natural fourth-moment route and finds that its **near-resonant zero energy is already strong enough**. If

`N^*(sigma,T)=#{|gamma_1+gamma_2-gamma_3-gamma_4|<=1}`,

then the known Heath-Brown/Bazzanella bound gives a power saving on the resonant contribution whenever

`vartheta > vartheta_res = (69-16 sqrt(3))/121 = 0.3412164221...`,

which lies strictly below `73/200=0.365`. Thus there is a nonempty exponent window in which the resonant quartets are not the bottleneck.

The unresolved term is shifted. Writing `Omega=gamma_1+gamma_2-gamma_3-gamma_4` and

`S_X(Omega)=sum_(n~X^(1/2)) exp(i Omega log x(n))`,

the nonresonant fourth moment reduces dyadically to weighted shifted energies of the form

`X^(4sigma-4) sum_U K_X(U) N^*_sh(sigma,T;U)`,

where `K_X(U)=sup_(U<|omega|<=2U)|S_X(omega)|`. Ordinary unshifted additive energy plus a generic count of possible shifts loses the entire gain and reproduces the square-root barrier `vartheta>1/2`.

So the live resource is the **coupling between shifted zero-additive energy and the deformed-quadratic oscillatory kernel**, not a better estimate for the near-resonant energy alone. RE-096's stable derivatives of `log x(n)` now have a precise place to enter: they must produce cancellation in `K_X(U)`, support a stronger shifted-energy estimate, or combine both strongly enough to yield a power-saving bad-host count for some `vartheta` in `(vartheta_res,73/200)`.

**Research consequence.** Do not spend the next step improving ambient exceptional-set packing or ordinary `N^*(sigma,T)` unless the improvement is explicitly coupled to the shifted kernel. The resonant exponent budget already clears the Robin window. The target is the weighted nonresonant sum, and any claimed fourth-moment advance should be measured directly against it.

**Boundary.** RE-098 does not prove sparse-host scarcity, does not show that the CA deformation itself creates cancellation, and does not control `|Omega|>1`. Its resonant calculation is equally valid for exact quadratic starts. The remaining theorem is source/sample-specific precisely because the shifted phase kernel is where the deformed sequence first matters.
