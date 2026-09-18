# MI-038 — Wang source continuation is RH-equivalent in the first half-plane

**Evidence level:** exact synthesis from [VIS-292](../../findings/VIS-292-wang-symmetric-source-smoothing-is-an-invertible-green-resolvent.md) and [VIS-293](../../findings/VIS-293-wang-source-dirichlet-rh-half-plane.md). The prime-zeta Möbius inversion identities are classical; the Mathia content is the exact pole bookkeeping for Wang's weighted prime-power source and its nonvanishing Green multiplier.

Wang's symmetric source profile is not hiding an arithmetic frequency behind a smoothing zero. VIS-292 identifies its log-scale Green kernel and shows that the Mellin multiplier `4/(4-w^2)` is nonzero in the relevant strip. VIS-293 then identifies the analytic content of the unsmoothed weighted prime-power source itself.

For

`D(s)=sum_(n>=1) Lambda(n)^2 n^(-s)`,

prime-zeta inversion gives

`D(s)=sum_(r>=1) c(r)(log zeta)''(rs)=(log zeta)''(s)+A(s)`,

where `c(r)=prod_(p|r)(1-p)` and `A` is holomorphic throughout `Re(s)>1/2`. Thus every nontrivial zeta zero in that half-plane appears as a pole of the source transform, and no term from `r>=2` can cancel it there.

After removing the elementary pole at `s=1`, holomorphy of `D(s)` on `Re(s)>1/2` is therefore equivalent to the absence of zeta zeros there, hence to RH by the functional equation. Multiplying by Wang's nonvanishing Green resolvent does not change this pole set. The exact source transform certainly retains the zero divisor, but obtaining the desired first-half-plane analytic continuation is **the target statement itself**, not an independent source theorem.

This separates two notions that exact transform identities can blur. Source recoverability says that the weighted prime-power data are still present after smoothing. Proof leverage requires a real-axis or source-side estimate whose continuation consequence is derived without assuming the zero-free half-plane. Simply rewriting the source as a Dirichlet/Mellin transform and asking it to be holomorphic past `1/2` has returned to RH in different coordinates.

**Boundary.** The result does not rule out useful real-axis estimates for `D`, moving-source asymptotics, boundary regimes, Tauberian implications or source-specific inequalities strong enough to imply a zero-free region. It rules out treating first-half-plane holomorphy of the exact Wang source transform as an independent input or new mechanism.
