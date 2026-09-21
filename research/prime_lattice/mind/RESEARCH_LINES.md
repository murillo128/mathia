# Prime-lattice research lines

This file holds the current mathematical questions suggested by the durable prime-lattice intuitions. It is not a roadmap, task queue, status page, or history.

## Transfer the regulated zero-sensitive cubic layer to the exact continuation statistic

**Linked intuitions:** `MI-044-finite-prime-wold-classification-does-not-globalize-atomically`, `MI-045-fixed-gap-meet-join-data-collapse-to-finite-congruence-decoration`, `MI-046-growing-gap-arithmetic-complexity-pays-a-reciprocal-continuation-tariff`, `MI-047-mesoscopic-continuation-phase-can-miss-the-prime-pair-parity-sector`, `MI-048-cubic-phase-can-reopen-arithmetic-support-yet-average-to-a-universal-control`, `MI-049-abel-cubic-singular-series-asymptotics-isolate-an-rh-equivalent-zero-layer-at-model-level`.

PL-391--PL-401 separate frozen multiplicative geometry from the continuation-faithful transition layer, price growing-gap information by a reciprocal `1/d` tail, and show that the cubic scale `d~r^(1/3)` restores the even-gap sector while its leading singular-series average is still reproduced by a parity-only control.

PL-402 identifies the hidden arithmetic layer in that same classical singular series. Its Mellin continuation contains poles at `s_rho=rho/2-1`, and the ideal cubic kernel has nonzero Mellin transform at every such location. The leading Gallagher collapse is therefore not a proof of zero-blindness; it only says the zero information is subleading.

PL-403 resolves the model-level regularization problem. With fixed Abel damping `w_eta(u)=exp(-eta u^3) sin(pi u^3/6)/u`, Mellin inversion has exponential vertical decay, the deterministic `H^-1` term is explicit, and the zeta-zero layer is preserved. For every fixed `eta>0`, the asymptotic

`A_eta(H)=phi_eta/3 - c_eta/(2H) + O_(eta,epsilon)(H^(-7/4+epsilon))`

for every `epsilon>0` is equivalent to RH. A parity control retains the leading constant but has neither the `H^-1` singular-series term nor the zero layer, so the subleading hierarchy is genuinely arithmetic.

The live obstruction is now the transfer step, not Mellin regularization of the model. Can the exact incomplete-gamma continuation statistic be compared with this Abel-regularized singular-series average with aggregate error `o(H^-7/4+epsilon)` after every larger deterministic contribution is removed? Until that bridge is proved, PL-403 is an RH-equivalent asymptotic for the classical source model rather than for the Prime-Lattice observable itself.

## Keep model-level RH equivalence and actual prime-pair transfer separate

PL-403 materially strengthens PL-402: at the singular-series level the cubic zero layer is no longer only visible in a formal contour picture; it admits a well-behaved regulator and a precise RH-equivalent remainder exponent. That does not erase the distinction between the model and actual `Lambda(r)Lambda(r+d)` correlations.

A viable continuation argument must retain the Abel-regulated cubic phase, subtract the explicit deterministic layers, prove a uniform transition comparison below `H^-7/4`, and justify replacing singular-series local densities by the exact arithmetic statistic. The remaining theorem is therefore a quantitative transfer theorem at the zero-sensitive scale, not another search for a regulator or another leading-average calculation.