# MI-035 — Jordan transport must be measured in Poisson widths near the boundary

**Evidence level:** exact synthesis from [NB-160](../../findings/NB-160-continuous-separated-jordan-samplers-still-export-an-adverse-zero-reservoir.md), [NB-161](../../findings/NB-161-collapsing-jordan-transport-forces-conditioning-blowup.md), and [NB-162](../../findings/NB-162-poisson-width-transport-controls-target-and-signed-euler-leakage.md), using Lipschitz/optimal-transport bounds for the exterior Poisson kernel and the absolutely convergent Euler series on `Re s>1`.

After zero total mass removes the universal Hadamard background, opposite signs cannot be collapsed for free. For a zero-mass signed height measure `nu=nu^+-nu^-`, let `M=nu^+(R)=nu^-(R)`, `V=||nu||_TV=2M`, and define the mean optimal Jordan transport length

`ell(nu)=W_1(nu^+,nu^-)/M`.

NB-161 showed at fixed horizontal offset that target response is bounded by total variation times `ell`, so transport collapse forces conditioning blowup. NB-162 identifies the correct invariant when the exterior sampler itself approaches `Re s=1`. If `a` is the boundary gap, `c` the positive reference mass and `C=V/c`, define

`Theta = C ell/a`.

For every actual zero, whose Poisson width `x` satisfies `x>=a`, the normalized target response is `O(Theta)`. More importantly, the same `Theta` controls the signed Euler-product response relative to its natural boundary scale `c/a`, because `|hat nu(u)|<=|u|W_1` and the derivative of `zeta'/zeta` grows like `1/a^2`. Thus sub-Poisson transport `Theta=o(1)` suppresses **both** the nuisance Euler leakage and the target signal.

This corrects the absolute-scale reading of NB-161. If `a_G->0`, it is harmless for `ell_G->0` in absolute units provided the Jordan transport remains comparable to the narrowing Poisson width after conditioning. What is fatal is `C_G ell_G/a_G->0`. A bounded-conditioning sampler retaining a fixed fraction of natural target gain must transport opposite signs across at least a constant fraction of a Poisson width.

Combined with NB-160, the unresolved geometry is now narrower. Many-width sign separation exports an `Omega(log G)` adverse-zero reservoir; sub-Poisson transport becomes target-invisible. The surviving bounded-cost regime is **one-Poisson-width interlacing**, `Theta_G=Theta(1)`, where the same local zeros can see both signs but the Jordan transport has not collapsed relative to the kernel.

The next useful theorem should decide whether one-width interlacing can cancel the routine local zero population while preserving target gain, and whether any prime-side cancellation stronger than the generic transport estimate can be obtained without simultaneously shrinking the target. The relevant coordinate is dimensionless transport relative to the kernel width, not absolute support distance or transport length separately.

**Boundary.** NB-162 does not close `Theta_G=Theta(1)`, nor does it prove that an interlaced sampler in that regime exports an adverse zero reservoir. It also permits fine absolute transport when the Poisson width shrinks at the same rate. Its content is the exact coupling between boundary scale, conditioning, target visibility and signed Euler leakage.
