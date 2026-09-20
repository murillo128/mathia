# MI-046 — Growing-gap arithmetic complexity pays a reciprocal continuation tariff

**Evidence level:** exact continuation-aware synthesis from [PL-396](../../findings/PL-396-fixed-gap-transition-survives-exact-continuation.md), [PL-398](../../findings/PL-398-fixed-gap-meet-join-finite-congruence-collapse.md), and [PL-399](../../findings/PL-399-growing-gap-transition-tail-suppression.md). The `1/d` law is for the larger-mode incomplete-gamma coefficient at the nominal pair saddle in the mesoscopic regime `d->infinity`, `d=o(r)`; it is not a theorem about every completed bilinear observable.

Fixed additive gaps and growing gaps pay opposite prices. At fixed `d`, the completed transition overlap remains order one, but `gcd(r,r+d)=gcd(r,d)` confines meet/join information to the finite divisor alphabet of `d`. Letting `d` grow can enlarge the arithmetic support of the gap, but PL-399 shows that at `T=2 pi r(r+d)` the larger continuation coefficient satisfies

`|Q_(r+d)(T)|=(1+o(1))/(sqrt(2) pi d)`,

while `Q_r(T)=1+O(1/d)`.

Thus the most direct way to buy more gap-supported prime coordinates simultaneously weakens the continuation channel by a reciprocal factor. The fixed-gap order-one kernel of PL-397 cannot simply be carried into a slowly growing-gap regime: the larger mode has moved `Theta(d)` transition widths into the complex complementary-error-function tail.

The durable resource question is therefore quantitative. Any arithmetic weight whose extra information is obtained by increasing the gap support must produce enough controlled amplification, aggregation or signed cancellation to survive the `1/d` continuation tariff. Merely observing that `d` has more prime factors does not create a free high-dimensional channel.

This does not penalize arithmetic information that is retained separately in `r` and `r+d` rather than purchased through `v(d)`, and it does not rule out integrating over a moving height window where the saddle/transition geometry changes. Those mechanisms require their own completed analysis.

**Boundary.** The asymptotic assumes `1<<d<<r` and the nominal pair saddle. It is algebraic rather than Gaussian suppression, does not assert a total pair contribution, and leaves open source weights such as `mu(r)mu(r+d)` or `Lambda(r)Lambda(r+d)` if their fully completed contribution can overcome the tariff.