# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Push the canonical shell discrepancy toward a near-linear scale

**Linked intuition:** `MI-002-small-shell-discrepancy-can-destroy-rooted-visibility`.

The shell decomposition still reduces the useful rooted-mixing channel to a quantitative coefficient discrepancy. The live theorem remains whether the canonical arithmetic coefficients can force a near-linear discrepancy on the relevant shell family without assuming the Nyman distance estimate one is trying to prove.

## Use directional tail identities without paying the ambient RH-equivalent norm price

**Linked intuitions:** `MI-001-coefficient-geometry-needs-target-coupling`, `MI-003-low-gram-spectrum-is-cheap-target-occupation-is-the-signal`, `MI-004-weighted-tail-shell-quotient-is-a-conditioned-source-skeleton`.

NB-024--NB-040 construct a source-faithful weighted tail quotient with polynomial conditioning and a sharp `Theta(1/M)` target-loss floor. One target-selected retained direction removes that loss exactly, showing that compression and exact target repair are distinct gates.

NB-041--NB-044 make the ambient-dual boundary exact. The logarithmic tail scalar has an explicit Möbius dual, but any polynomial norm decay already forces a fixed zero-free strip, and the optimal power exponent equals `1-Theta_zeta`, the zeta zero frontier. Near-square-root decay is therefore not merely difficult; ambient norm improvement directly measures the zero problem one is trying to solve.

NB-045 supplies a different kind of source information. The complete family of bounded step-tail discrepancies satisfies the exact logarithmic identity

`sum_(L<N) log((L+1)/L) D_(L,N) = d_N^2 - Theta(N)`.

Burnol's lower bound and the classical Möbius remainder force a positive discrepancy of order at least `1/log^2 N`, with a nontrivial logarithmic occupation lower bound across cutoffs. Thus the finite Nyman distance already decomposes into many explicit **directional** source-selected witnesses even though the ambient dual norm remains RH-hard.

The live theorem is to convert this multiscale directional occupation into the projected repair geometry, a one-sided target certificate, or the near-linear shell discrepancy at the required scale without reconstructing `d_N` through an RH-equivalent norm estimate. A materially different quotient remains possible, but simply improving the same ambient dual is now fully priced.

## Treat compression, exact repair, ambient dual decay, and multiscale directional occupation as separate gates

The weighted skeleton is conditioned but loses target energy; rank-one target repair is exact but target-selected; ambient dual power decay measures the zero frontier; and step-tail discrepancies nevertheless reconstruct the finite distance through a positive logarithmic average. Future arguments should exploit the last directional structure without silently upgrading it into an ambient norm theorem.