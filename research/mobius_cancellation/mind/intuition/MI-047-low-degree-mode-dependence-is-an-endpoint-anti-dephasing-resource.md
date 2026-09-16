# MI-047 — Low-degree endpoint mode dependence is anti-dephasing only when own-source phase is expensive to recover

**Evidence level:** exact finite-endpoint synthesis from [MC-332](../../findings/MC-332-arbitrary-mode-dependent-prime-rows-exactly-dephase-the-reciprocal-endpoint.md) through [MC-337](../../findings/MC-337-odd-source-parity-all-or-nothing-self-phase-barrier.md).

MC-332 shows that arbitrary dependence of prime coefficients on the endpoint mode is too expressive: the conjugate-character matched filter erases the phase exactly, even though its evaluation matrix has rank only `R`. MC-333--MC-334 then show that rank, total Frobenius energy and centered variation are separate currencies.

MC-335 adds Fourier degree in the **standard endpoint mode bits**. If every prime-coordinate function extends to a Walsh polynomial of degree at most `d`, multiplication by the one-defect character geometry restricts the reachable output frequencies. For low `d` the best approximation error to uniform all-mode dephasing stays at the full target scale; near-maximal degree restores exact programmability. In those coordinates, genuinely low degree is a real anti-programmability resource.

MC-336 identifies the hidden coordinate dependence. Reparameterize the mode by the source phases `x_i(a)=(-1)^(a·s_i)`. The matched filter is then degree one: a coefficient at source cell `i` can simply read `x_i` and cancel that same phase locally. Low polynomial degree by itself is therefore not an invariant complexity bound. A nonlinear coordinate change that exposes the target phase can turn an apparently hard matched filter into a linear observable.

For even source rank, MC-336 repairs this by **self-phase exclusion**. If coefficient `i` may depend on the other source phases but not on `x_i`, with source-coordinate degree at most `d`, the reachable output space misses a high-degree character tail. The resulting exact projection formula leaves asymptotically full RMS dephasing error for `d=o(R)` and exact dephasing first appears at `d=R-1`.

MC-337 shows that literal variable exclusion is still not the invariant notion when the source coordinates satisfy relations. For odd `R`,

`prod_(i=1)^R x_i=1`,

so the source-phase map has kernel `{0,1}` and image the even-parity subgroup `H`. The forbidden own phase is algebraically recoverable from the others:

`x_i=prod_(j!=i) x_j` on `H`.

The key point is the **cost** of that reconstruction. For `d<=R-2`, reachable outputs are exactly the nonconstant characters of `H` whose subset/complement class has minimal weight at most `d+1`. With `L=2^(R-1)`, `N=2^R` and `q_d` the missing nonconstant quotient characters, the exact error is

`E_d = N (L+q_d)/(L+q_d+1)`.

Hence the normalized error tends to one uniformly throughout the entire submaximal-degree range. Once `d>=(R-3)/2`, all nonconstant quotient characters are already reachable and the error nevertheless remains on the plateau `NL/(L+1)`. Only at `d=R-1` does the parity relation make the excluded phase cheap enough to reconstruct exactly, at which point the constant target enters and dephasing becomes exact.

The durable resource is therefore **source-relative reconstruction complexity**, not low degree or syntactic self-phase exclusion separately. A useful information-flow restriction must prevent each output coefficient from observing *or cheaply reconstructing* the phase it is meant to cancel after all exact source relations and quotient identifications are taken into account.

Rank, energy, variation, degree and own-phase reconstructibility remain independent. A class can be low rank but contain the matched filter; low degree in a target-exposing coordinate can be fully programmable; and an excluded variable can still be determined globally by the admitted variables while remaining inaccessible below a degree threshold. Any analytic theorem must charge restrictions in the same source-relative quotient representation in which programmability is tested.

**Boundary.** MC-336--MC-337 are exact for the finite reciprocal endpoint and its source-phase character geometry. They do not show that a useful arithmetic coefficient family satisfies the required information-flow restriction. The odd-rank result depends on the precise parity relation and proves an all-or-nothing degree threshold there; different algebraic relations, mode sets, nonlinear output statistics or analytic norms require their own reconstruction-capacity calculation. Nothing here bounds `M(x)` or proves RH.