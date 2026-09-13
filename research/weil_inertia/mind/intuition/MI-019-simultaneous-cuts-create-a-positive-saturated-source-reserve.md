# MI-019 — Simultaneous cuts have a sharp harmonic mass-only reserve

**Evidence level:** exact at a hypothetical attained first unrestricted Suzuki crossing through [WI-274](../../findings/WI-274-simultaneous-cuts-create-a-positive-saturated-source-reserve.md) and [WI-275](../../findings/WI-275-a-harmonic-minimax-reserve-is-the-sharp-mass-only-cut-bound.md). The total reserve is sign-independent. The prime-overlap corollary remains conditional on a one-signed null mode, and no theorem yet forces the harmonic reserve above the positive archimedean budget.

Single-cut localization prices each cut separately and hits a sharp Carleman wall as an internal gap closes. WI-274 changes the order of operations: impose firstness for all sharp cuts and integrate the family before estimating the source. A source pair at lag `h` crosses a set of cuts of length exactly `h`, so the lag weight regularizes the short-range archimedean singularity and leaves a positive saturated source reserve even though the endpoint eigenvalue is zero.

WI-275 shows that averaging the two complementary inequalities is not optimal. For each cut,

`Q_t >= A_t M_L(t)`, `Q_t >= B_t M_R(t)`, `M_L+M_R=1`,

with `A_t=lambda_((a+t)/2)` and `B_t=lambda_((a-t)/2)`. Therefore

`Q_t >= A_t B_t/(A_t+B_t)`

pointwise. Integrating gives the exact harmonic reserve

`S_v >= R_harm(a) := 2 integral_0^a lambda_r lambda_(a-r)/(lambda_r+lambda_(a-r)) dr`.

This dominates the WI-274 area reserve, with the explicit gain

`R_harm(a) - 2 integral_(a/2)^a lambda_s ds`
`= 2 integral_0^(a/2) lambda_(a-r)(lambda_r-lambda_(a-r))/(lambda_r+lambda_(a-r)) dr >= 0`.

The improvement is also a sharpness theorem for the available information. The minimax equality mass profile

`M_L^*(t)=B_t/(A_t+B_t)`

is monotone in `t`, so monotonicity of the left-mass CDF alone cannot strengthen the envelope. Any additional reserve must use information discarded by the two scalar cut bounds: regularity/differential constraints of the actual mass profile, relations among different `Q_t`, the Suzuki null equation, the PSD signed-source multiplier family, or nodal/source geometry.

On a one-signed branch the weighted prime overlap satisfies

`P_v >= R_harm(a)-K_+`.

Thus the immediate scalar test is no longer the old spectral area but the paired-radius harmonic functional. If rigorous constraints on `r -> lambda_r` force `R_harm(a)>K_+`, complete prime screening is impossible on that branch. If an admissible spectral profile can keep `R_harm(a)<=K_+`, the mass-only spectral route is exhausted and the next theorem must couple cuts through genuinely source-specific structure.

**Boundary.** The harmonic reserve does not prove that the first null mode is one-signed, does not force prime overlap on a sign-changing branch, and does not assert that the minimax equality profile is realized by an actual Suzuki eigenfunction. Its role is to mark the exact boundary of the complementary-mass relaxation.
