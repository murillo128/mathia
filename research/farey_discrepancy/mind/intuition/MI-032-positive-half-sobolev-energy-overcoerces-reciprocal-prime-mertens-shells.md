# MI-032 — Half-Sobolev is the centering threshold for positive Farey energy

**Evidence level:** exact synthesis from [FD-196](../../findings/FD-196-weighted-fourier-duality-phase-diagram.md) through [FD-201](../../findings/FD-201-fixed-mode-cross-horizon-positive-energy-still-overcoerces-multiplicative-mertens-shells.md).

A positive quadratic observation can be simultaneously **too weak for one inverse direction and too strong as a global source requirement**. Farey Discrepancy shows that the half-Sobolev index is the exact transition where a reciprocal-prime shell can be centered against the common base row at bounded positive-energy cost, and FD-201 shows that the same overcoercion survives even when cross-horizon differencing genuinely adds source-sensitive information.

Write `K=floor(sqrt(H))` and

`B_H(k)=sum_(d|k) d M(floor(H/d))`.

For primes `K/2<p<=K`,

`B_H(p)-B_H(1)=p M(floor(H/p))`.

For the weighted positive energies `E_(H,sigma)(K)=sum_(k<=K)|B_H(k)|^2/k^(2sigma)`, FD-199 proves that the centering map on this shell has exact measurement-space squared norm

`1+S_sigma(K)`, where `S_sigma(K)=sum_(K/2<p<=K) p^(-2sigma)`.

By PNT, `S_sigma(K)->0` exactly for `sigma>=1/2`; at the endpoint it is `~log(2)/log K`, while below one half it grows like `K^(1-2sigma)/log K`. Thus `sigma=1/2` is the precise point where subtracting the common row from `Theta(K/log K)` prime coordinates stops carrying a growing rank-one tariff.

FD-198--FD-199 show that on the RH-facing energy line, every `sigma>=1/2` then forces subpower RMS across the whole reciprocal-prime Mertens shell. FD-200 rules out one apparent cross-horizon escape because matched horizon-mode dilation is universal divisor transport. FD-201 tests the complementary fixed-mode direction and finds a real information gain:

`D_(r,H)(p)-D_(r,H)(1)=p[M(floor(rH/p))-M(floor(H/p))]`.

The increment is a genuine Möbius sum over a fixed-ratio multiplicative interval; it is not algebraic replication of `M(H)`. But if these source-sensitive rows are immediately compressed into the positive half-Sobolev energy, the same shellwide tariff returns. An `O(H^(1+epsilon))` budget forces subpower RMS for `Theta(K/log K)` multiplicative Mertens increments, while a squarefree Rademacher multiplicative control already contributes `H^(3/2+o(1))` on the prime shell.

The reusable diagnostic is therefore three-stage. First remove or price common modes. Second verify that a proposed cross-horizon transformation creates genuinely new source information rather than divisor transport. Third audit the **destination compression**: a source-sensitive family can still lose the needed sign/correlation structure when it is squared diagonally into a positive norm.

A more economical Farey route needs signed cross-mode or cross-horizon covariance, a source-forced projection, or another destination statistic that preserves the correlations in the fixed-mode increments before positive compression. More horizons are useful only if their new information survives the norm that consumes them.

**Boundary.** The sharp centering norm is a measurement-coordinate statement, not a source-realizability lower bound. FD-201 proves source sensitivity of fixed-mode horizon differencing and overcoercion of one positive compression; it does not rule out signed/correlated cross-horizon statistics and does not prove any critical Farey energy false.