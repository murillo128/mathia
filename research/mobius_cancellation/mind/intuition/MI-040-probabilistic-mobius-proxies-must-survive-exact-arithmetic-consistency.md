# MI-040 — Probabilistic Möbius proxies must survive exact arithmetic consistency before asymptotics can carry new information

**Evidence level:** exact/literature-derived obstruction from [MC-318](../../findings/MC-318-schmidt-independence-q1n-consistency-obstruction.md), auditing the stated Schmidt 2026 probabilistic route.

Two elementary identities give a hard pre-asymptotic gate. First, the stratum `Omega(n)=1` consists of primes, so squarefreeness is deterministic there:

`P(mu^2(n) != 0 | Omega(n)=1)=1`,

not the unconditional limiting density `6/pi^2`. Any independence hypothesis quantified over that stratum is false as stated.

Second, if

`Q_(1,n)(x)=sum_(j<=x) lambda(nj) mu^2(j)`,

then complete multiplicativity and `lambda(j)mu^2(j)=mu(j)` give exactly

`Q_(1,n)(x)=lambda(n) M(x)`.

So the auxiliary object is not an independently noisy proxy for the Mertens sum: it is the target itself up to a known sign. In particular an `n`-independent nonzero leading asymptotic cannot hold simultaneously for `n=1` and `n=2`.

The reusable gate is specific. Before invoking probabilistic independence, test conditioned strata where arithmetic support becomes deterministic; before estimating a proxy, simplify it under exact multiplicative identities. A probabilistic model only adds information if the surviving observable is not already algebraically equivalent to the target and the conditioning law is compatible with forced arithmetic events.

A possible repaired route must therefore change at least one load-bearing object: restrict the independence statement to a defensible central/growing-`Omega` regime and/or replace `Q_(1,n)` by an auxiliary statistic that does not collapse to `lambda(n)M(x)`. Whether such a replacement retains enough quantitative leverage is open.

**Boundary.** MC-318 audits the stated manuscript version; it is not a rejection of probabilistic number theory and yields no new bound on `M(x)`. A later corrected version must be rechecked. The durable content is the exact consistency gate, not a claim that every probabilistic Möbius approach must fail.