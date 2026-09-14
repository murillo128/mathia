# MI-010 — The complete cumulative Farey discrepancy field is a reversible Mertens representation

**Evidence level:** exact representation classification from [FD-116](../../findings/FD-116-fixed-rational-anchor-horizon-dynamics-is-a-periodic-mobius-transform.md) and [FD-117](../../findings/FD-117-full-farey-discrepancy-field-is-invertibly-equivalent-to-the-quotient-mertens-staircase.md), using the denominator-shell/Fourier identities already canonical in the line. This is not a new Mertens bound and does not prove RH.

FD-116 showed that every fixed rational anchor history is only a periodic Möbius filter. FD-117 removes the apparent moving-anchor escape. For every horizon `N`, the entire cumulative discrepancy function satisfies

`D_N(x)=x-floor(x)+sum_(m<=N) (floor(mx)-mx) M(floor(N/m))`.

Thus arbitrary moving endpoints, growing denominators, growing endpoint families, or same-field adaptive selectors are all functionals of the same quotient-Mertens staircase. The converse is exact as well: for `1<=k<=N` the Fourier coefficients obey

`1+2 pi i k \hat D_N(k)=sum_(d|k) d M(floor(N/d))`,

and divisor Möbius inversion recovers every quotient value `M(floor(N/k))`. The complete discrepancy field therefore has exactly the same arithmetic information as that quotient-Mertens state, up to explicit finite transforms.

Across horizons the conclusion becomes stronger rather than weaker: `(D_2,...,D_N)` and `(M(1),...,M(N))` are mutually reconstructible. Moving the observation rule can change the geometry of the representation, but it cannot create a second source channel.

The remaining value of a Farey/geometric reorganization is therefore **proof-theoretic, not informational**. An ordered refinement, exterior coordinate, moving selector, or nonlinear transform can still expose positivity, locality, coercivity, or cancellation that is difficult to see in Mertens coordinates. To count as progress it must yield a quantitatively stronger theorem for the same source, not merely a higher-dimensional or moving representation.

**Boundary.** Information equivalence does not imply equal proof difficulty. FD-117 rules out source independence, not the possibility that a reversible geometric transform makes an RH-critical estimate easier to prove.
