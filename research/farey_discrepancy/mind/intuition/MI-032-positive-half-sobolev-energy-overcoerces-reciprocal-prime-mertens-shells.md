# MI-032 — Half-Sobolev is the centering threshold for positive Farey energy

**Evidence level:** exact synthesis from [FD-196](../../findings/FD-196-weighted-fourier-duality-phase-diagram.md), [FD-197](../../findings/FD-197-random-squarefree-multiplicative-source-saturates-noncritical-fourier-energy-line.md), [FD-198](../../findings/FD-198-prime-square-root-fourier-shell-forces-subpower-mertens-rms.md), and [FD-199](../../findings/FD-199-half-sobolev-is-the-prime-shell-centering-threshold.md).

A positive quadratic observation can be simultaneously **too weak for one inverse direction and too strong as a global source requirement**. Farey Discrepancy now shows that the half-Sobolev index is the exact transition where a whole reciprocal-prime shell can be centered against the common base row at bounded positive-energy cost.

Write `K=floor(sqrt(H))` and

`B_H(k)=sum_(d|k) d M(floor(H/d))`.

For primes `K/2<p<=K`,

`B_H(p)-B_H(1)=p M(floor(H/p))`.

For the weighted positive energies `E_(H,sigma)(K)=sum_(k<=K)|B_H(k)|^2/k^(2sigma)`, FD-199 proves that the centering map on this shell has exact measurement-space squared norm

`1+S_sigma(K)`, where `S_sigma(K)=sum_(K/2<p<=K) p^(-2sigma)`.

By PNT, `S_sigma(K)->0` exactly for `sigma>=1/2`; at the endpoint it is `~log(2)/log K`, while below one half it grows like `K^(1-2sigma)/log K`. Thus `sigma=1/2` is not just a convenient weight. It is the precise point where subtracting the common row `B_H(1)` from `Theta(K/log K)` prime coordinates stops carrying a growing rank-one tariff in the uncentered positive norm.

This sharpens the overcoercion audit from FD-198. On the FD-196 RH-facing line `gamma+sigma=3/2`, every `sigma>=1/2` forces subpower RMS across the whole reciprocal-prime Mertens shell. Below `1/2`, the direct positive-energy transfer weakens by exactly the growing common-row centering cost. The transition belongs to the **observation norm**, not to a change in the exact prime-shell identity.

The reusable diagnostic is two-stage. First remove or price common modes before interpreting a weighted positive energy. Then audit the strongest simultaneous source consequence of the remaining positive budget. Explicit centering can eliminate the low-`sigma` rank-one tariff, but it does not cure the upper-half overcoercion: a positive RH-facing energy still demands much more collective suppression than the pointwise RH target.

A more economical Farey route therefore needs genuinely signed/projected cross-mode structure, cross-horizon coherence, or another destination norm that removes nuisance common rows **without** replacing them by uniform positive suppression of the centered shell.

**Boundary.** The sharp norm statement is at the measurement-coordinate level; it is not a source-realizability lower bound. FD-199 does not prove the critical positive energy false, does not transfer the threshold to arbitrary observation norms, and does not show that explicit signed centering solves the RH problem. It identifies exactly which loss is a common-mode artifact and which simultaneous-amplitude demand survives after that artifact is removed.