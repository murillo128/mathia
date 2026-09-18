# MI-061 — Hellinger affinity tensorizes the bounded source-edge tariff and has a sharp direct endpoint envelope

**Evidence level:** exact synthesis from [MC-340](../../findings/MC-340-bounded-energy-dephasing-forces-linear-joint-source-information.md), [MC-359](../../findings/MC-359-total-variation-source-edge-tariff.md), [MC-360](../../findings/MC-360-hellinger-product-component-edge-tariff.md), [MC-361](../../findings/MC-361-binary-entropy-sharpens-reciprocal-endpoint-information-floor.md), [MC-362](../../findings/MC-362-tv-to-hellinger-near-endpoint-transfer.md), and [MC-363](../../findings/MC-363-sharp-js-hellinger-endpoint-envelope.md). The statistical inequalities and binary-channel extremality are classical; the Mathia content is their composition with the reciprocal-endpoint information floor and source-edge geometry.

Total variation solves the singular-endpoint problem but does not provide a canonical additive accounting rule for conditionally independent transcript components. Squared Hellinger distance supplies both boundedness and product structure. For neighboring source states `e={x,x'}` let

`h_e^2=H^2(P_x,P_x')`

and normalize

`H_1=(2/m) sum_e h_e^2`.

MC-360 proves

`I(X;Y) <= H_1 + 2(R-1)/m`.

This already forces an extensive average Hellinger boundary under bounded-energy nontrivial dephasing. Its additional value is compositional. Suppose an edge is represented by a genuine common latent coordinate `Theta` and, conditional on `Theta`, a product transcript `Y=(Y_1,...,Y_k)`. If the latent laws are `nu_x,nu_x'` and `h_(e,j)^2(theta)` is the conditional component Hellinger cost, then MC-360 proves

`H^2(P_x,P_x') <= H^2(nu_x,nu_x') + sum_j int sqrt(r_x r_x') h_(e,j)^2 d kappa`.

Thus source dependence may move between the latent law and the conditionally independent components, but it cannot disappear. Unlike a post-hoc TV coupling, the Hellinger accounting is intrinsic to the product architecture because affinity factorizes.

The first direct route in MC-360 used `JS<=H^2`. It is qualitatively correct but not endpoint-sharp: mutually singular edge laws have Jensen--Shannon divergence `log 2` and squared Hellinger distance `1`, so that linear comparison leaves a permanent `log 2` fraction. MC-361 and MC-362 showed that the architectural conclusion could be made endpoint-sharp by first forcing a nearly maximal TV boundary and only then transferring TV to Hellinger. That detour proved `H_1/R -> 1` as dephasing error tends to zero, but its quantitative deficit was `O(sqrt(epsilon log(1/epsilon)))`.

MC-363 identifies the sharp direct one-dimensional conversion. For probability laws `P,Q`, put `z=H^2(P,Q)` and

`Phi(z)=log 2-h((1-sqrt(1-(1-z)^2))/2)`.

Then

`JS(P,Q) <= Phi(z)`,

with equality for the binary-symmetric experiment. `Phi` is increasing and concave. The concavity matters because the envelope can be inserted after the source-edge reduction and averaged over the punctured cube without abandoning the Hellinger coordinate. If `q_R=(m-1)/m`, MC-363 gives

`I(X;Y) <= R q_R Phi(H_1/(R q_R)) + 2(R-1)log 2/m`.

For normalized energy at most one and dephasing error at most `epsilon`, inversion of this sharp envelope yields

`liminf H_1/R >= 1-sqrt(2 epsilon-epsilon^2)`

along the even-rank endpoint sequence. Hence the deficit from maximal Hellinger separation is asymptotically at most `sqrt(2 epsilon)`. This strictly improves the TV-mediated `sqrt(epsilon log(1/epsilon))` scale while preserving the same compositional Hellinger ledger.

When the latent law is source-independent and component `j` depends only on source coordinates `A_j`, the MC-360 product bound transfers the same lower requirement to the total affinity-weighted source-coordinate incidence. Splitting a source-sensitive transcript into many individually weak components therefore does not evade the endpoint demand, and MC-363 removes the remaining possibility of hiding inside a loose metric conversion.

The reusable distinction is between **bounded distinguishability, compositional bounded distinguishability, and sharp conversion into the compositional currency**. TV remains natural when a genuine common-seed representation turns source flips into change probabilities. Hellinger is natural when the transcript has a genuine latent/product factorization. MC-363 shows that one need not choose between endpoint sharpness and Hellinger tensorization: the sharp Jensen--Shannon/affinity envelope supplies both directly. Jeffreys/Fisher remain sharper in regular smooth channels.

**Boundary.** MC-363 is still a necessary admission theorem, not an arithmetic upper bound and not an estimate for `M(x)`. The Hellinger budgets must refer to the same complete conditional transcript laws. Conditional independence and the latent representation must be genuine properties of the architecture rather than an artificial refactorization. The next useful result remains architecture-specific: prove a subextensive TV/common-seed or Hellinger latent/component budget for the actual Möbius-derived transcript, or identify the real source-dependent component that pays the almost-maximal near-endpoint tariff.
