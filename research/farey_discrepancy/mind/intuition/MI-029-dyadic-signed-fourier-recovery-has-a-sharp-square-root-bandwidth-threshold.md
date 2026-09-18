# MI-029 — Dyadic signed Fourier recovery has a sharp square-root bandwidth threshold

**Evidence level:** proved synthesis from [FD-117](../../findings/FD-117-farey-fourier-data-is-exactly-mobius-quotient-data.md) and [FD-189](../../findings/FD-189-dyadic-fourier-bands-have-a-sharp-square-root-tail-recovery-threshold.md).

For a formal arithmetic source `a` with cumulative sum `A`, the signed Farey Fourier coordinate at horizon `H` is equivalent, after divisor Möbius inversion, to the quotient sample `A(floor(H/k))`. Along dyadic horizons `H=2^m`, retaining every signed mode `1<=k<=H^alpha` therefore asks which source indices can occur as `floor(2^m/k)`.

FD-189 identifies the exact transition. If `alpha>1/2`, every sufficiently large index occurs, so the dyadic band recovers the complete source tail and a finite prefix fixes the rest. If `alpha<=1/2`, infinitely many Mersenne indices `2^r-1` are never sampled; paired perturbations at consecutive unsampled coordinates give a genuine formal-source kernel. The endpoint `alpha=1/2` is therefore noninjective, while every super-square-root bandwidth is tail-injective.

The useful lesson is not that Fourier data are intrinsically stronger than quotient samples: at each fixed horizon they are exactly the same information in different coordinates. The gain comes from how a growing observation family sweeps the source lattice across scales. For recovery through source depth `X`, horizons of order `X^2` are enough, and a band `H^(1/2+epsilon)` uses only `X^(1+2epsilon)` signed coordinates.

This sharpens the observation-side frontier. Any genuinely sparser Farey bridge must exploit structure absent from the unrestricted formal source class—such as physical squarefree/multiplicative admissibility—or accept a lossy statistic such as scalar spectral energy. Merely repackaging the same signed band cannot beat the square-root threshold.

**Boundary.** The subcritical Mersenne perturbations are formal sources and need not preserve the Möbius/squarefree constraints. The theorem concerns the full signed coefficient vector, not band energy or another scalarization. It is a recovery threshold, not a Franel--Landau estimate and not an RH implication.