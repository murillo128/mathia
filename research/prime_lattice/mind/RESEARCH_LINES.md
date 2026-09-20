# Prime-lattice research lines

This file holds the current mathematical questions suggested by the durable prime-lattice intuitions. It is not a roadmap, task queue, status page, or history.

## Put arithmetic coupling into a completed transition channel whose phase meets the arithmetic support

**Linked intuitions:** `MI-044-finite-prime-wold-classification-does-not-globalize-atomically`, `MI-045-fixed-gap-meet-join-data-collapse-to-finite-congruence-decoration`, `MI-046-growing-gap-arithmetic-complexity-pays-a-reciprocal-continuation-tariff`, `MI-047-mesoscopic-continuation-phase-can-miss-the-prime-pair-parity-sector`.

PL-391--PL-394 show that the frozen multiplicative geometry can scalarize while the continuation-faithful approximate functional equation retains reflected modes and the Gamma-phase cross channel. PL-395 rules out the broad off-diagonal stationary shell in the sharp moving main sum; PL-396 restores the exact incomplete-gamma transition layer; PL-397 computes its leading fixed-gap kernel and shows that the error-function weights and quadratic chirp are additive and factorization-blind.

PL-398 closes the first arithmetic overlap decoration. At fixed `d`, `gcd(r,r+d)=gcd(r,d)`, so meet data range only over divisors of `d` and join correction is determined by the same finite information. PL-399 then shows that growing the gap to expose more arithmetic structure pays a reciprocal analytic tariff: for `1<<d<<r`, at `T=2 pi r(r+d)` the larger continuation coefficient has magnitude `1/(sqrt(2) pi d)` while the smaller tends to one.

PL-400 shows that magnitude is not enough. In the phase-pinned mesoscopic range `d->infinity`, `d=o(r^(1/3))`, the normalized same-sign cross-channel coefficient is

`P_(r,d)=(1+o(1))/(sqrt(2) pi d) exp(-i pi(d^2+1)/2)`.

Its leading real part vanishes for even `d` and equals `-1/(sqrt(2) pi d)` for odd `d`. The canonical von-Mangoldt pair weight has possible bulk prime-pair support on even gaps, while odd-gap `Lambda(r)Lambda(r+d)` has only `O((log X)^2)` total mass up to `X`. Thus the most direct repair proposed after PL-399 -- multiply the transition tail by `Lambda(r)Lambda(r+d)` and seek Hardy--Littlewood amplification in the real same-sign channel -- selects opposite parity sectors analytically and arithmetically.

The live question is consequently phase-sensitive. A surviving completed observable must use a channel whose canonical phase has a real component on the arithmetic support it is meant to amplify, enter the cubic-phase regime near or above `d~r^(1/3)` with quantitative uniform control, aggregate gaps with the complex phase retained, or use another arithmetic coupling whose signed mass survives both the `1/d` tariff and matched controls. Merely attaching prime-pair weights to the magnitude of the PL-399 tail is no longer a viable mechanism.

## Keep continuation magnitude, complex phase and arithmetic support separate

PL-395 remains exact for the sharp main sum; PL-396 restores the smooth transition; PL-397 shows that the fixed-gap leading kernel is universal; PL-398 reduces fixed-gap meet/join data to finite congruence information; PL-399 imposes the `1/d` mesoscopic continuation tariff; PL-400 shows that in the smaller `d=o(r^(1/3))` regime the leading phase puts even-gap continuation in quadrature with the real Hardy projection. None is by itself arithmetic rigidity, and PL-400 is only one quadratic channel.

Future constructions must state which completed quantity and projection are used, what complex transition phase multiplies the arithmetic weight, which gap classes actually carry bulk source mass, and whether any gap aggregation is uniform enough to preserve the claimed leading term. A source label that lives on a phase-orthogonal sector cannot be credited merely because its absolute magnitude is large.