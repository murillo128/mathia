# MI-048 — The physical bow path saturates the square-root resolution tariff

**Evidence level:** exact synthesis from [WI-348](../../findings/WI-348-global-phase-sensitivity-still-needs-resolution-collapse.md) and [WI-349](../../findings/WI-349-physical-bow-carrier-saturates-the-quadratic-resolution-cost.md), using classical packing geometry and Kirszbraun extension as audited in WI-349.

WI-348 bounds the phase-saturated fixed-aperture carrier by `O(rho^-2)` states at ordinary Hilbert resolution `rho`, leading to the generic feature tariff `L/mu >> sqrt(r_tau)`. A natural objection is that the phase-saturated cylinder is two-dimensional while the actual height carrier is a one-parameter path.

WI-349 shows that the objection does not improve the uniform exponent. For a two-coordinate physical carrier with aperture `H Delta=1` and center-frequency ratio `R=x_c/Delta`, the actual one-dimensional orbit contains `Theta(R^2)` points separated at scale `1/R`. Thus at the family-dependent carrier resolution `rho=1/R`, its covering number is already `Omega(rho^-2)`.

This does not contradict one-dimensional Minkowski behavior for a **fixed** curve. The curve family itself changes: its length and winding frequency grow like `R`, while the requested resolution shrinks like `1/R`. Parameter dimension alone therefore does not control uniform metric entropy in a coupled high-frequency/small-resolution limit.

The sharpness is operational, not just combinatorial. Mapping the packed points to orthogonal target vectors and extending by Kirszbraun gives a height-independent Lipschitz feature with `L=O(R)`, nonvanishing transmission, and effective normalized Gram rank `Theta(R^2)`. Hence `L/mu=O(sqrt(r_tau))`, matching WI-348 in exponent.

The reusable lesson is: **low-dimensional parameterization does not imply cheap uniform compression when the geometric variation scale grows with the family.** Any entropy argument must track curve length/frequency, physical resolution and output rank together. A one-dimensional source can carry quadratically many distinguishable states at the resolution forced by its own growing winding scale.

For Weil Inertia this closes the generic route from “physical path is one-dimensional” to a linear sensitivity tariff. Stronger compression must use information absent from arbitrary Lipschitz geometry: arithmetic covariance, feature-algebra restrictions, gauge equivariance, source-specific norms, or another exact identity.

**Boundary.** The matching example is generic and deliberately uses a small source support plus an arbitrary Kirszbraun-extended feature. It does not show that the actual `Lambda-Lambda^sharp` source realizes that feature or that the distinguished covariance sign is inaccessible. Projective compression remains stronger because quotienting global phase removes the fast winding responsible for the quadratic ordinary packing.