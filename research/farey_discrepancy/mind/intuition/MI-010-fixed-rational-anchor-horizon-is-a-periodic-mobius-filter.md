# MI-010 — The complete cumulative Farey discrepancy field is a reversible Mertens representation

**Evidence level:** exact representation classification from [FD-116](../../findings/FD-116-fixed-rational-anchor-horizon-dynamics-is-a-periodic-mobius-transform.md), [FD-117](../../findings/FD-117-full-farey-discrepancy-field-is-invertibly-equivalent-to-the-quotient-mertens-staircase.md), and [FD-118](../../findings/FD-118-floor-quotient-frequencies-form-a-minimal-linear-fourier-skeleton.md), using the denominator-shell/Fourier identities already canonical in the line. This is not a new Mertens bound and does not prove RH.

FD-116 showed that every fixed rational anchor history is only a periodic Möbius filter. FD-117 removes the apparent moving-anchor escape. For every horizon `N`, the entire cumulative discrepancy function satisfies

`D_N(x)=x-floor(x)+sum_(m<=N) (floor(mx)-mx) M(floor(N/m))`.

Thus arbitrary moving endpoints, growing denominators, growing endpoint families, or same-field adaptive selectors are all functionals of the same quotient-Mertens staircase. The converse is exact as well: for `1<=k<=N` the Fourier coefficients obey

`1+2 pi i k \hat D_N(k)=sum_(d|k) d M(floor(N/d))`,

and divisor Möbius inversion recovers every quotient value `M(floor(N/k))`. The complete discrepancy field therefore has exactly the same arithmetic information as that quotient-Mertens state, up to explicit finite transforms.

FD-118 sharpens the spectral side of this equivalence. The distinct quotient set `Q_N={floor(N/m):1<=m<=N}` is closed under divisors and the map `k -> floor(N/k)` is an involution on it. Therefore the Fourier coordinates indexed by `Q_N` form a square Möbius-invertible skeleton for the entire quotient-Mertens state. Only `2 sqrt(N)+O(1)` positive frequencies are needed; every other Fourier mode is algebraically redundant. This is minimal only in the formal real-linear sense for an arbitrary source vector indexed by `Q_N`, not an information-theoretic claim about the actual Mertens sequence.

Across horizons the conclusion becomes stronger rather than weaker: `(D_2,...,D_N)` and `(M(1),...,M(N))` are mutually reconstructible. Moving the observation rule or adding Fourier bandwidth can change the geometry of the representation, but neither can create a second source channel.

The remaining value of a Farey/geometric reorganization is therefore **proof-theoretic, not informational**. An ordered refinement, exterior coordinate, moving selector, nonlinear transform, or redundant spectral family can still expose positivity, locality, coercivity, or cancellation that is difficult to see in Mertens coordinates. To count as progress it must yield a quantitatively stronger theorem for the same source, not merely a higher-dimensional, moving, or wider-band representation.

**Boundary.** Information equivalence does not imply equal proof difficulty. FD-117--FD-118 rule out source independence and extra spectral bandwidth, not the possibility that a reversible or redundant geometric transform makes an RH-critical estimate easier to prove.
