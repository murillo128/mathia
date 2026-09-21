# MI-059 — Polynomially vanishing cluster masses are additive shifts in the Hermite cost spectrum

**Evidence level:** exact fixed-depth weighted-Hermite synthesis from [VIS-363](../../findings/VIS-363-polynomial-mass-decay-hermite-order-statistic.md), extending the equal-mass one-inner-scale law of VIS-362.

Vanishing positive cluster masses do not create a new compact Wang cancellation mechanism when they decay polynomially in the same inner scale and each local weighted cloud remains uniformly nondegenerate. If the mass fraction of outer cluster `ell` satisfies

`pi_ell asymp epsilon^(2 a_ell)`,

then its Hermite jet of derivative order `d` carries the single asymptotic cost

`a_ell+d`.

Form the multiset of all such costs `a_ell+d`, `0<=d<=q-1`, and let `tau_q` be the `q`-th smallest value. VIS-363 proves the sharp global laws

`lambda_min(M^(-1) S_epsilon^* W S_epsilon) asymp epsilon^(2 tau_q)`

and

`s_q(A_w) asymp sqrt(M) rho^(q-1) epsilon^tau_q`.

The lower bound comes from the `q` cheapest Hermite jets: because their derivative orders can be taken as initial segments at each separated center, they form a uniformly invertible confluent interpolation problem. The matching upper bound is a polynomial whose zero multiplicities remove every jet cheaper than `tau_q`. The exponent is therefore an order statistic of a finite jet filtration, not a loose estimate.

VIS-362 is exactly the equal-mass case `a_ell=0`, where `tau_q=floor((q-1)/L)`. VIS-363 shows that making some positive clusters polynomially light merely delays all of their jets by the additive valuation `a_ell`; it does not add an unpriced source-free degree of freedom.

The remaining compact positive-diagonal escape must therefore leave this one-scale valuation model: a local normalized weighted Gram must degenerate after rescaling, a genuinely deeper nested scale must appear, the mass asymptotics must require another noncomparable rescaling, or the coefficient geometry/source information must leave the positive diagonal setting.

**Boundary.** The result assumes one common inner scale, polynomially comparable mass fractions, separated outer centers and uniformly healthy local positive weighted clouds. It does not classify recursive cluster trees, non-polynomial or incomparable mass scales, growing depth, noncompact geometry, non-diagonal/indefinite coefficient metrics, or signed arithmetic source gains.