# MI-018 — Source complexity matters only when the destination transports it

**Evidence level:** supported by AF-217--AF-220 and sharpened by [AF-338](../../findings/AF-338-harmonic-collision-count-reduces-euler-sign-depth-to-linear-order.md), [AF-341](../../findings/AF-341-prime-layer-retains-rh-pole-discriminator-and-leading-sign-complexity.md)--[AF-347](../../findings/AF-347-finite-riesz-smoothing-erases-power-background-locality.md). The observation theorem remains fixed-finite-order in the absolutely convergent half-plane; no growing-order critical-line transport theorem is claimed.

AF-338 identifies a genuine observation currency: finite source sign variation transfers through a finite sign-regular observation order. But AF-344--AF-346 show that the source side can be recoded cheaply. Prime-independent weighted `k`-th-power backgrounds preserve the right-half-plane RH pole discriminator while reducing ordered sign variation to `O(P^(1/k))`; sign variation is exactly prime-gap occupancy, and the same family saturates the forced occupancy/mass-moment trade.

AF-347 adds a separate transport obstruction. The same background has extremely sparse support, large gaps and large amplitudes, so replacing sign count by a stronger raw locality profile looks promising. Yet after polynomial Riesz smoothing of order `r`, its mass on `X=M^k` obeys

`R_(k,r)(X)=X/(r+1)+O(X^max(1-(r+1)/k,0))`,

and for `r>=k-1` it is only `O(1)` away from the corresponding dense unit background. Finite differences in the smoothing annihilate the polynomial-scale Faulhaber corrections. The raw locality distinction is real, but the chosen destination can stop seeing it.

The durable lesson is therefore stronger than “use a richer source statistic.” A source certificate is useful only together with a **transport theorem for the exact destination operation**. One must show either that the destination consumes the certificate before averaging, or that the certificate survives the averaging with a quantitative margin that reaches the final endpoint. Otherwise source complexity can be genuine and still be mathematically unavailable downstream.

This separates three questions that should not be collapsed: what the arithmetic source contains, what the observation map preserves, and what the endpoint theorem charges. A growing-order sign-regular theorem could couple these currencies if its constants price the full source geometry; alternatively a different normalized source functional could work if it is provably stable under the required smoothing/compression.

**Boundary.** AF-347 is stated on exact-power cutoffs and for one family of polynomial Riesz means; it does not prove that every locality functional is erased or that no critical-line transport can use the perfect-power geometry. The supported conclusion is only that raw locality, like sign count and one mass moment, cannot be promoted to a source certificate without proving its survival through the destination map.
