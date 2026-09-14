# MI-018 — Source complexity matters only when the destination transports it

**Evidence level:** supported by AF-217--AF-220 and sharpened by [AF-338](../../findings/AF-338-harmonic-collision-count-reduces-euler-sign-depth-to-linear-order.md), [AF-341](../../findings/AF-341-prime-layer-retains-rh-pole-discriminator-and-leading-sign-complexity.md)--[AF-348](../../findings/AF-348-uniform-riesz-smoothing-erases-power-background-locality.md). The observation theorem remains fixed-finite-order in the absolutely convergent half-plane; no growing-order critical-line transport theorem is claimed.

AF-338 identifies a genuine observation currency: finite source sign variation transfers through a finite sign-regular observation order. But AF-344--AF-346 show that the source side can be recoded cheaply. Prime-independent weighted `k`-th-power backgrounds preserve the right-half-plane RH pole discriminator while reducing ordered sign variation to `O(P^(1/k))`; sign variation is exactly prime-gap occupancy, and the same family saturates the forced occupancy/mass-moment trade.

AF-347 added a separate transport obstruction on exact-power cutoffs. AF-348 shows that restriction was not load-bearing. For every fixed `k,r`, uniformly over all real cutoffs,

`R_(k,r)(X)=X/(r+1)+O_(k,r)(X^max(1-(r+1)/k,0))`.

Thus for `r>=k-1` the sparse weighted perfect-power source and dense unit mass differ by only `O_(k,r)(1)` under the Riesz observable everywhere along the cutoff axis, despite radically different support cardinality, gaps and amplitudes. The terminal fractional cell does not recover the lost source geometry.

The durable lesson is stronger than “use a richer source statistic.” A source certificate is useful only together with a **transport theorem for the exact destination operation**. One must show either that the destination consumes the certificate before averaging or that the certificate survives the averaging with a quantitative margin that reaches the final endpoint. Otherwise source complexity can be genuine and still be mathematically unavailable downstream.

This separates three questions that should not be collapsed: what the arithmetic source contains, what the observation map preserves, and what the endpoint theorem charges. A growing-order sign-regular theorem could couple these currencies if its constants price the full source geometry; alternatively a different normalized source functional could work if it is provably stable under the required smoothing/compression.

**Boundary.** AF-348 concerns one scalar family of polynomial Riesz means with fixed `k,r`; the constants are not uniform in growing order/degree, bounded error is not exact equality, and other operators can still see the raw power-source geometry. The supported conclusion is only that raw locality, like sign count and one mass moment, cannot be promoted to a source certificate without proving its survival through the destination map.
