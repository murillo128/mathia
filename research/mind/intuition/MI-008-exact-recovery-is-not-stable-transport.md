# MI-008 — Inverse separation, channel coupling, cadence, horizon, and operator order are different quantitative losses

**Evidence level:** supported by the specified inverse, sampling, and propagation models; no common universal condition number is claimed.

For a finite simple Blaschke product, AF-178 gives a local inverse constant proportional to the reciprocal zero-separation product. Exact recovery survives while conditioning diverges as zeros collide. This is a metric/local-degree statement, not a generic source-recovery law.

Dirichlet recovery has several different acquisition losses. AF-278 shows that continuous vertical averaging at fixed real part recovers each declared coefficient by paying phase-time breadth and noise amplification. AF-279 shows that regular vertical sampling first quotients frequencies through `lambda -> e^{-ih lambda}`: rational resonance can create exact aliases even with the full bilateral lattice, while a nonresonant cadence restores infinite-data injectivity without giving a uniform finite-window inverse modulus.

AF-280 adds a distinct **channel-coupling** gate. A finite family of regular lattices is injective on the unrestricted weighted `ell^1` ordinary-Dirichlet source class iff at least one cadence is already nonresonant. If every cadence has a rational alias, an explicit finite group-algebra interaction lies in the common kernel. Even when the tuple of phase labels is injective, keeping the complete one-coordinate lattice sequences separately can lose a mixed interaction that a genuinely joint phase observable would retain.

Finite cadence diversity also does not cure finite-horizon instability: simultaneous torus recurrence makes a remote logarithmic frequency approach the target phase in every fixed cadence window while the target coefficient changes by order one. Therefore exact separation, retention of joint coupling, and finite-acquisition stability are genuinely different properties.

Prime Flute supplies a separate composition lesson. Exponential far propagation can change the frequency window in which a leakage estimate is needed; one cannot simply multiply local condition numbers. PF-297 adds that a finite-section contraction can itself be a truncation artifact: the canonical Robin factors are strict `ell^1(q)` contractions at finite depth but their norms tend to one, while the complete map preserves positive `q`-mass.

Keep the relevant separation metric, source category, channel coupling, cadence fibers, observation horizon, forcing/escape balance, and composed frequency window explicit. None is supplied merely by exact uniqueness or strictness at an earlier finite stage, and there is no established theorem identifying their condition numbers across these models.