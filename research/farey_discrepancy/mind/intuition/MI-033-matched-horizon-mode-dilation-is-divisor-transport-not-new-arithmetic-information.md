# MI-033 — Matched horizon-mode dilation is divisor transport, not new arithmetic information

**Evidence level:** exact synthesis from [FD-200](../../findings/FD-200-matched-horizon-mode-dilations-are-a-universal-divisor-cocycle.md), with the earlier cross-horizon context of FD-121 and the square-root Fourier frontier FD-198--FD-199.

The simplest way to combine horizon and mode growth in the Farey Fourier coordinates is algebraically redundant before any Möbius-specific input enters. For an arbitrary cumulative source `A`, define

`B_H(k)=sum_(d|k) d A(floor(H/d))`.

For every prime `p`, FD-200 proves the exact transport law

`B_(pH)(pk)=B_(pH)(k)+p B_H(k)-p 1_(p|k) B_H(k/p)`.

Equivalently, along a `p`-adic mode tower the first differences satisfy `D_(a+1)(pH;m)=p D_a(H;m)`. Repeated-prime collisions therefore create only lower-triangular leakage into already existing modes; they do not expose a new source residual.

The same statement tensorizes on coprime composite dilations. When `(q,k)=1`, the matched coordinate `B_(qH)(qk)` is the divisor convolution `sum_(a|q) a B_((q/a)H)(k)`, and ordinary Dirichlet inversion recovers the fixed-mode horizon coordinates from a divisor-closed matched family. Thus multiplying horizon and mode together does not increase deterministic information in that family. At the prime-shell endpoint the redundancy is especially sharp:

`(B_(pH)(p)-B_(pH)(1))/p = B_H(1)=A(H)`.

For the physical source `A=M`, every matched ridge observation `(pH,p)` is exactly the same Mertens value `M(H)`. Replicating that witness across primes or matched horizons cannot supply the independent cancellation missing from the positive square-root-band energies.

This narrows the post-FD-199 cross-horizon escape. A useful construction must break the universal matched divisor transport: compare fixed modes across horizons, use unmatched mode/horizon ratios, retain an order-sensitive or nonlinear coupling before norm compression, or exploit a source-specific relation between distinct quotient coordinates. Cross-horizon structure can still matter through incompatibility of several universal identities with one common source, as in FD-121; what fails is treating the matched-dilation residual itself as arithmetic signal.

**Boundary.** The composite inversion requires the relevant divisor-closed intermediate horizons. A sparse composite sensor may omit enough terms that the explicit inversion is unavailable internally, although the prime-step identity has no such caveat. FD-200 is a universal algebraic redundancy theorem, not a claim that every cross-horizon observable is redundant and not an RH-critical cancellation estimate.