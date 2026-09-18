# Visual-exploration research lines

This file holds the current mathematical questions suggested by the durable visual-exploration intuitions. It is not a roadmap, task queue, status page, or history.

## Determine what survives when the packet leaves the fixed-interior bounded-projection regime

**Linked intuitions:** `MI-029-fixed-margin-pair-correlation-accuracy-must-outrun-packet-conditioning` through `MI-037-laplace-null-localization-pays-an-inverse-width-conditioning-cost`, with corrected moving-test synthesis in `MI-031-wang-transfer-allows-moving-tests-only-inside-a-seminorm-and-support-budget`.

The fixed-source representation audit has removed the apparent generic `L^-3/2` frontier from every direct sector inspected so far. VIS-271--VIS-278 identify the theorem/source coordinate mismatch, reconstruct the gamma-normalized source and show that its invariant residual has positive prime-power energy `C_Lambda` entering only at `L^-2`. VIS-279--VIS-281 then show that the direct `D_x--E_x` envelope, the `D_x--B_x` cross and the zero-window localization loss all fall to `L^-2` or below after specializing to compact physical source before rescaling.

VIS-282 resolves the formerly anonymous `O(H)` Dirichlet mean square. At fixed source,

`int_I |D_x(t)|^2 dt = H S_D(x)+O_K(1)`,

where

`S_D(x)=x^(-2) sum_(n<=x)n Lambda(n)^2 + x^2 sum_(n>x) Lambda(n)^2/n^3`.

The profile has explicit derivative jumps `-4 Lambda(m)^2/m^2` at prime powers, so the coefficient-scale `L^-2` term contains deterministic arithmetic structure rather than merely theorem error.

VIS-283 closes the signed recombination question. The arithmetic residual `zeta'/zeta(3/2-it)` has the wrong temporal-frequency orientation to resonate with `D_x`: product frequencies are `-log(mn)`, not differences, so there is no zero-frequency diagonal. Consequently the signed prime/source cross is power-small after fixed-source normalization, while the field energy separates through constant order as

`(1/H) int_I |A(x,t)|^2 dt = S_D(x) + x^(-2)[log(T/(2*pi))^2 + C_Lambda] + o_K(1)`.

Keeping the exact gamma baseline intact leaves the positive coefficient-scale arithmetic profile

`Q_gamma(x)=S_D(x)+C_Lambda/x^2`.

VIS-284 now closes the **fixed-interior packet projection** itself. For every uniformly `L^1`-bounded packet family supported in one fixed compact physical-source interval, Wang's exact inversion gives the coefficient-scale contribution as a bounded linear functional of `Q_gamma(e^(2*pi q))`. If the packet annihilates the universal Laplace mode `e^(-4*pi q)`, then support localization has a sharp conditioning cost: for support diameter `b`,

`|<h,Q_gamma(e^(2*pi q))>| <= C_K b ||h||_1`.

Thus a Laplace-null packet with bounded total variation loses arithmetic response as its support shrinks. Keeping a nonzero localized response requires `||h||_1` to grow at least like `1/b`, and that same growth amplifies the unresolved remainder. Narrowing inside the fixed compact regime therefore does not create free source resolution.

The live question has moved to the boundary of that theorem. A new mechanism must arise when packet support approaches a source boundary, escapes every fixed compact physical-source interval, or uses a singular normalization with enough quantitative control to survive its own norm amplification. Any claimed gain must first subtract the established `Q_gamma` projection and universal Laplace mode, then show a residual term absent from the compact-source model whose error budget remains controlled under the moving family.

## Keep packet conditioning, arithmetic selectivity, theorem coordinates and parameter-uniformity separate

The current ledger separates moving-test seminorm cost, prime-power support, normalization gauge, physical source scale, sign/covariance retention, temporal-frequency orientation and now **packet total variation versus support width**. VIS-284 adds a precise distinction: localization can improve spatial resolution only by paying in operator norm, and a gain bought entirely by that norm is not new arithmetic information. A future probe should preserve exact source structure through the physical pullback, quantify the moving-family remainder before amplification, and only then interpret any surviving boundary signal.
