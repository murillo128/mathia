# MI-017 — The regular CA staircase itself samples the finite-edge stable profile densely

**Evidence level:** exact attained-edge reduction through RE-112--RE-118, sharpened globally over regular CA states by [RE-119](../../findings/RE-119-regular-ca-heights-sample-the-finite-edge-profile-on-an-exponentially-fine-phase-mesh.md). No contradiction with false RH, lower-order selector theorem, nonattained-edge result or `Theta=1` result is claimed.

Let `Theta` be an attained finite off-critical edge, `c=1-Theta`, and `J=F_Theta+G_Theta`. RE-114--RE-118 show that endpoint criticality, first recovery and rightmost block maximality all collapse to compatibility conditions on the same weighted almost-periodic state `J`.

RE-119 removes the remaining possibility that the **actual arithmetic CA sequence is too sparse in phase** for those compatible spectral states to matter. For every sufficiently large regular CA state `C`, with `Y=log C` and `nu=log Y`, one has uniformly

`Y^c nu h(C)=J(nu)+o(1)`.

Moreover consecutive regular-state phases satisfy

`Delta nu = O(e^(-nu/2) nu^(3/2))`,

so the CA phase mesh is finer than every inverse power of `nu`. On every fixed phase interval the sampled supremum and infimum of the normalized Robin height converge to those of `J` itself.

Since `J` is nonzero, real, uniformly almost periodic and has zero Bohr mean, the actual regular CA staircase therefore samples both positive and negative sign-margin lobes with bounded phase gaps. Under an attained off-critical edge, two-sided CA excursions occur at the natural edge scale

`(log C)^(Theta-1)/log log C`.

The missing datum is no longer leading-order arithmetic placement. **The full regular CA sequence already reads out the same stable profile at that resolution.** A surviving contradiction must live in the lower-order remainder of the pointwise projection, in a source coordinate not encoded by `J`, or in a selector property visible at a scale finer than the current `o(1)` edge-normalized error.

This also prevents overinterpreting the earlier moving-ray/block-record conditions. They can still matter at finer resolution, but at leading order they do not select a rare subset of compatible phases: the whole regular staircase is an exponentially fine sampling of the same profile.

**Boundary.** RE-119 gives a uniform `o(1)` normalized asymptotic, not an expansion through `1/nu`. The unknown remainder may dominate the deterministic inverse-log drift used in finer maximum-selection arguments. It does not locate a block maximizer at subleading scale or address the nonattained-edge and `Theta=1` regimes.
