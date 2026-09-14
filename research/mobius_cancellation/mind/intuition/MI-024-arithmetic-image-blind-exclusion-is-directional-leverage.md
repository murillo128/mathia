# MI-024 — Arithmetic-image leverage has a parity-sensitive occupancy dichotomy

**Evidence level:** exact variational/certificate reduction from [MC-281](../../findings/MC-281-empirical-christoffel-leverage-blind-certificate.md), sharpened by [MC-282](../../findings/MC-282-separated-simplex-leverage-failure.md), [MC-284](../../findings/MC-284-page-siegel-stretched-exponential-shell-legendre-universality.md), [MC-285](../../findings/MC-285-even-shell-pairing-christoffel-support-barrier.md), [MC-286](../../findings/MC-286-odd-shell-affine-span-criterion.md), and [MC-287](../../findings/MC-287-dense-odd-shell-near-injectivity-dichotomy.md). No theorem is claimed that the required Christoffel certificate exists for the actual shell.

For feature matrix `A` on the actual arithmetic shell and blind row `v`, the endpoint-normalized energy

`C=inf_(v^*a=1)||Aa||_2^2`

satisfies `C=1/Lambda`, where `Lambda` is the minimum synthesis cost of `v` from actual rows. MC-282 shows this is directional leverage, not generic nonblindness: an arithmetic realization can have no blind direction and still have poor synthesis leverage. MC-284 further shows that moderate-conductor Legendre shadows are already Boolean-complete.

The decisive simplification is now combinatorial. For even shell weight, MC-285 shows that equal-pattern pairs create the all-positive endpoint unless projected occupancy is almost injective. For odd weight `t`, MC-286 identifies the exact support obstruction as affine-hyperplane concentration: `0 notin aff(S)`, equivalently some generated product character is `-1` on every shell prime.

MC-287 shows that this affine obstruction cannot coexist with both dense support and substantial collisions. If `K=|S|>2^(d-1)`, the support already contains an odd zero-sum nucleus of size at most three. If also `N-K>=t-1`, equal-cell pairs pad it to an exact odd `t`-row. Hence any energy-`<1` odd certificate must obey

`K<=2^(d-1)  or  N-K<=t-2`.

The second branch is near-injective. At live `t=O(log log y)`, it forces `d>=log_2 y-log_2 log y+O(1)` and the same primorial-scale conductor cost already visible in the even branch. Thus the unresolved odd obstruction is no longer “some generated character might be constant-negative” in isolation. It must arise through one of two rigid source geometries: **support compressed into at most half of the Boolean cube**, or **almost every shell prime encoded by a distinct projected pattern**.

This gives a sharper target for arithmetic input. A theorem need not realize every Boolean pattern. It is enough to exclude both branches at the support scales relevant to the Christoffel certificate. Conversely, proving only high rank, generic pattern diversity or nonblindness does not remove either branch.

**Boundary.** The density threshold `2^(d-1)` is sufficient rather than necessary for a short odd nucleus, and the collision bound is sufficient rather than necessary for padding a particular nucleus. The dichotomy is a necessary condition for the current endpoint architecture, not an RH estimate or existence theorem for the inverse.
