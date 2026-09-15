# MI-031 — Positive Euler-product Poisson sampling is sharp off the line but has a self-dual boundary jump

**Evidence level:** exact source-specific occupancy theorem from [NB-144](../../findings/NB-144-euler-product-poisson-mass-forces-logarithmic-confluence-away-from-the-one-line.md), with corrected minimax classification from [NB-146](../../findings/NB-146-separated-right-half-poisson-optimality-has-a-factor-two-self-dual-boundary-jump.md). NB-146 supersedes the withdrawn NB-145.

For exterior samples `s=1+delta+iv`, the explicit formula and the absolutely convergent Euler product give one positive budget: the zero Poisson mass is bounded by `(1/2)log G` plus the `delta^(-1)` Euler-side cost. The useful charge per counted zero depends on its functional-equation reflection orbit.

For a packet centered at `beta_G=1-epsilon_G>1/2` and separated from the critical line by more than its horizontal width, each counted zero has a **distinct reflected partner outside the packet**. Using only zero-side positivity and the pointwise absolute majorant for `zeta'/zeta`, arbitrary positive superpositions of exterior samples have sharp leading floor

`(1/2) epsilon_G(1-epsilon_G) log G`.

The one-point sampler of NB-144 attains this floor when `epsilon_G log G -> infinity`. Thus more positive samples do not buy more arithmetic information in the separated right-half regime.

At a symmetric packet centered on `Re s=1/2`, the counting changes. A line zero is fixed by reflection, and an off-line reflected pair inside the symmetric packet already contributes two counted occurrences. The usable Poisson charge per counted occurrence is therefore half the formal off-line pair charge. The exact minimax coefficient becomes

`(1/4) log G`,

whereas `lim_(epsilon->1/2-) (1/2)epsilon(1-epsilon) log G = (1/8)log G`.

The factor-two jump is not a discontinuity of the Poisson kernel. It is an **orbit-counting discontinuity**: off the line, a distinct uncounted partner contributes positive mass for free; at the self-dual boundary it does not.

The reusable conclusion has two parts. First, within the positive exterior-sampling architecture the off-line coefficient is already optimized, so the fixed-interior gap requires a new mathematical resource rather than denser sampling. Second, any argument moving the packet toward the critical line must track whether reflection remains a distinct outside occurrence; one cannot pass to the endpoint by continuity in `epsilon` alone.

**Boundary.** This is a method-optimality theorem for positive weights, Poisson positivity and the pointwise absolute Euler-product bound. Signed combinations, prime correlations, higher moments and target-projection information remain outside the classification.