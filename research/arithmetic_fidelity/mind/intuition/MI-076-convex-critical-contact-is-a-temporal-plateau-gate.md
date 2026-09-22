# MI-076 — Convex critical contact is a quotient-boundary, admission-height and accessibility-rate gate

**Evidence level:** exact synthesis from AF-495--AF-508, with the contact criterion proved in [AF-505](../../findings/AF-505-convex-critical-contact-is-a-temporal-plateau-gate.md), the quotient-membership refinement in [AF-506](../../findings/AF-506-ray-quotient-turns-temporal-contact-into-boundary-membership.md), the admission-height refinement in [AF-507](../../findings/AF-507-admission-height-refines-quotient-contact-into-exact-plateau-onset.md), and the no-contact rate carrier in [AF-508](../../findings/AF-508-sublevel-distance-profile-is-exact-no-contact-rate-carrier.md).

AF-505 isolates a temporal existence gate that compactness cannot replace. For a nonempty closed convex destination set `F` and `f(t)=dist(tu,F)` with finite asymptotic value `lambda`, convexity forces `f` to decrease to `lambda`; the critical equality set is either empty or a terminal ray. Reaching `lambda` once is therefore equivalent to eventual plateau.

AF-506 identifies what that gate becomes after quotienting by the observation direction `L=span(u)`. Bounded asymptotic distance forces `u` into the recession cone and

`lambda = dist_(Q/L)(0,q(F)) = dist_Q(F,L)`.

Under the relevant proximinality hypotheses, plateau occurs exactly when the minimum-norm point of the closed quotient image actually belongs to the possibly nonclosed image `q(F)`. Passing from `q(F)` to its closure preserves the critical scalar value while potentially deleting the one boundary-membership bit that decides exact contact.

AF-507 sharpens the same mechanism in finite-dimensional Hilbert geometry. Writing `Q=u^perp direct_sum R u`, every one-sided ray-invariant closed convex `F` is the epigraph of a proper closed convex admission height `a_F`; the quotient image is `dom(a_F)`. If `z_*` is the nearest point to `closure(dom a_F)`, then the equality set is exactly `[tau_F,infinity)` when `a_F(z_*)<infinity`, with `tau_F=max(0,a_F(z_*))`, and is empty otherwise. Thus quotient closure fixes the asymptotic threshold, finiteness of `a_F(z_*)` fixes whether contact exists, and its scalar value fixes exactly when the plateau begins.

AF-508 identifies the exact quantitative datum when contact never occurs. For the admission sublevels `C_r={z:a_F(z)<=r}` define

`rho(r)=dist(0,C_r)^2-lambda^2`.

Then `rho(r)>0` at every finite budget, `rho(r)` decreases to zero, and

`f(t)^2-lambda^2 = inf_r [rho(r)+(r-t)_+^2]`.

Equivalently, only values of `rho` in the intrinsic forward window `0<=h<=sqrt(rho(t))` can improve on the current budget. The inverse admission-divergence profile `A(eta)` is the generalized inverse of `rho`, so no additional rate information is hidden in the height description. Under the local stability condition that `rho(t+h)/rho(t)->1` uniformly on that intrinsic window, the final quadratic envelope preserves the profile asymptotically. Power-law divergence transfers exactly: `A(eta)~c eta^(-beta)` gives `rho(t)~c^(1/beta)t^(-1/beta)`, followed by the expected positive-threshold or zero-threshold square-root conversion for `f(t)-lambda` or `f(t)`.

The equality/rate ledger is therefore ordered more finely than contact alone: closed quotient geometry fixes the limiting threshold; quotient-image membership decides whether contact exists; finite admission height determines plateau onset; and, if the critical point is missing, the nested sublevel accessibility profile determines the rate at which the scalar distance approaches its unattained limit after a universal one-sided quadratic smoothing. Compactness and proximinality belong only after the relevant contact or near-contact state has survived these earlier gates.

**Boundary.** The sharp admission and rate formulas are finite-dimensional Hilbert convex geometry with one-sided recession. They do not identify a natural arithmetic nuisance quotient, prove its boundary point is admitted, derive an arithmetic accessibility profile, or supply a rational-prime discriminator or RH implication. The asymptotic replacement of the exact quadratic envelope by `rho(t)` also requires the explicit intrinsic-window regularity hypothesis; it is not automatic for an arbitrary decreasing profile.