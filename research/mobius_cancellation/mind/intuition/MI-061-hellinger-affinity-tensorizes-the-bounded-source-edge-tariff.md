# MI-061 — Hellinger affinity tensorizes the bounded source-edge tariff and remains endpoint-sharp after TV transfer

**Evidence level:** exact synthesis from [MC-340](../../findings/MC-340-bounded-energy-dephasing-forces-linear-joint-source-information.md), [MC-359](../../findings/MC-359-total-variation-source-edge-tariff.md), [MC-360](../../findings/MC-360-hellinger-product-component-edge-tariff.md), [MC-361](../../findings/MC-361-binary-entropy-sharpens-reciprocal-endpoint-information-floor.md), and [MC-362](../../findings/MC-362-tv-to-hellinger-near-endpoint-transfer.md). The TV--Hellinger comparison, Jensen--Shannon/Hellinger comparison, Hellinger data processing, joint convexity and product affinity are classical; the Mathia content is their composition with the reciprocal-endpoint information floor and source-edge geometry.

Total variation solves the singular-endpoint problem but does not provide a canonical additive accounting rule for conditionally independent transcript components. Squared Hellinger distance supplies both boundedness and product structure. For neighboring source states `e={x,x'}` let

`h_e^2=H^2(P_x,P_x')`

and normalize

`H_1=(2/m) sum_e h_e^2`.

MC-360 proves

`I(X;Y) <= H_1 + 2(R-1)/m`.

This already forces an extensive average Hellinger boundary under bounded-energy nontrivial dephasing. Its additional value is compositional. Suppose an edge is represented by a genuine common latent coordinate `Theta` and, conditional on `Theta`, a product transcript `Y=(Y_1,...,Y_k)`. If the latent laws are `nu_x,nu_x'` and `h_(e,j)^2(theta)` is the conditional component Hellinger cost, then MC-360 proves

`H^2(P_x,P_x') <= H^2(nu_x,nu_x') + sum_j int sqrt(r_x r_x') h_(e,j)^2 d kappa`.

Thus source dependence may move between the latent law and the conditionally independent components, but it cannot disappear. Unlike a post-hoc TV coupling, the Hellinger accounting is intrinsic to the product architecture because affinity factorizes.

The direct MC-360 route through `JS<=H^2` is not endpoint-sharp: mutually singular edge laws have Jensen--Shannon divergence `log 2` but squared Hellinger distance `1`, so that comparison leaves a permanent `log 2` fraction even as dephasing becomes exact. MC-361 and MC-362 show that this slack is avoidable without abandoning Hellinger composition.

Let `T_1=(2/m)sum_e TV(P_x,P_x')` and `q_R=(m-1)/m`. MC-362 proves the aggregate metric transfer

`T_1/(R q_R) <= sqrt((H_1/(R q_R))(2-H_1/(R q_R)))`.

Hence if `T_1/(R q_R)>=s`, then

`H_1/R >= q_R Psi(s)`,  where  `Psi(s)=1-sqrt(1-s^2)`.

MC-361 first turns near-endpoint dephasing into an almost-full transcript-information requirement. MC-359 then converts that information floor into a nearly maximal TV boundary using the endpoint-sharp inequality `JS<=(log 2)TV`. Only after that global TV floor is established does MC-362 transfer it to Hellinger. For normalized energy at most one and dephasing error at most `epsilon`, the asymptotic lower bound becomes

`liminf H_1/R >= 1-sqrt(1-(1-h(epsilon/2)/log 2)^2)`,

which tends to `1` as `epsilon->0`. Thus near-exact dephasing forces an **almost-maximal** Hellinger source boundary rather than merely a positive fraction of one.

When the latent law is source-independent and component `j` depends only on source coordinates `A_j`, the same lower bound transfers through MC-360 to the total affinity-weighted source-coordinate incidence. Splitting a source-sensitive transcript into many individually weak components therefore does not evade the endpoint demand; near exactness drives the aggregate compositional tariff toward its maximal per-direction scale.

The reusable distinction is between **bounded distinguishability and compositional bounded distinguishability**, together with the order in which metric conversions are applied. TV is natural when a genuine common-seed representation turns source flips into change probabilities and is endpoint-sharp for binary discrimination. Hellinger is natural when the transcript has a genuine latent/product factorization. MC-362 shows that one can obtain the sharp endpoint requirement in TV first and only then transfer it to Hellinger, retaining product tensorization without paying the direct Jensen--Shannon/Hellinger endpoint slack. Jeffreys/Fisher remain sharper in regular smooth channels.

**Boundary.** MC-362 is still a necessary admission theorem, not an arithmetic upper bound and not an estimate for `M(x)`. The TV and Hellinger budgets must refer to the same complete conditional transcript laws. Conditional independence and the latent representation must be genuine properties of the architecture rather than an artificial refactorization. The next useful result remains architecture-specific: prove a subextensive TV/common-seed or Hellinger latent/component budget for the actual Möbius-derived transcript, or identify the real source-dependent component that pays the almost-maximal near-endpoint tariff.
