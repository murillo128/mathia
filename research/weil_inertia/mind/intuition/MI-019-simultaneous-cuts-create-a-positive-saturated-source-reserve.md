# MI-019 — Hilbert cut orientation strengthens the reserve, but current scalar profile data still cannot cross the archimedean budget

**Evidence level:** exact at a hypothetical attained first unrestricted Suzuki crossing through [WI-274](../../findings/WI-274-simultaneous-cuts-create-a-positive-saturated-source-reserve.md), [WI-275](../../findings/WI-275-a-harmonic-minimax-reserve-is-the-sharp-mass-only-cut-bound.md), [WI-276](../../findings/WI-276-cross-cut-energy-obeys-a-sharp-nilpotent-shift-reserve.md), [WI-277](../../findings/WI-277-commensurate-cross-cut-shifts-obey-a-sharp-finite-toeplitz-reserve.md), the scalar-profile countermodeled barrier [WI-278](../../findings/WI-278-certified-profile-data-do-not-force-the-source-reserve-past-the-archimedean-budget.md), and the oriented-cut refinement [WI-279](../../findings/WI-279-hilbert-cut-covariance-yields-a-bottom-toeplitz-reserve-but-does-not-break-the-scalar-profile-wall.md). Prime-overlap remains conditional on a one-signed null mode.

WI-275 exhausts complementary mass information through the sharp harmonic reserve. WI-276 retains one cross-cut correlation. WI-277 consumes several commensurate shifts jointly after scalarizing the cut path to the norm profile `sqrt(Q_s)`, obtaining a finite Toeplitz reserve from the top eigenvalue of

`H_N(alpha)=1/2 sum_k alpha_k (J_N^k+(J_N^*)^k)`.

WI-279 shows that this scalarization was a genuine information loss. Keep the oriented cut vectors `G_s` in the Hilbert quotient of the first-crossing PSD form. Their signed covariance satisfies the exact identity

`F_v(kh/2)=S_v-C_k(h)`.

For the same commensurate weights, the joint covariance is bounded below by the **bottom** eigenvalue `eta_N(alpha)=lambda_min(H_N(alpha))`, giving

`S_v >= (sum_k alpha_k k r lambda_(kr))/(sum_k alpha_k-eta_N(alpha))`.

This is always at least as strong as the WI-277 top-spectrum reserve and can be strictly stronger. For `N=3` and `alpha_1=alpha_2=1`, the denominator improves from `3` to `5/2`. So the orientation of the common Hilbert cut path is real information that disappears when one keeps only `sqrt(Q)`.

The gain is also sharp for **abstract PSD cut geometry**: a bottom-eigenvector can be realized by a rank-one null partition, so no universal improvement of that coefficient follows from positivity/null-partition structure alone. More importantly, WI-278 still blocks the RH-facing step. Its admissible scalar profile has `sup_r r lambda_r < K_+`, and because `eta_N<=0`, every bottom-spectrum reserve remains bounded by the same scalar profile ceiling. Restoring cut orientation improves the coefficient for an actual profile but does not create stronger numerator information about `lambda_r`.

The correct exhaustion statement is therefore subtler than “support-only geometry is finished.” **Scalar profile data are finished; Hilbert orientation is not algebraically useless, but it still cannot cross the budget while the numerator is controlled only by the current `lambda_r` information.** The next theorem must use a source/eigenfunction constraint absent from the counterprofile: the exact Suzuki signed-source multiplier equation, source-specific noncommensurate cut compatibility, null-mode nodal/shape information, or archimedean sign geometry.

This also keeps the sign gate separate. The reserve inequalities are sign-independent, while the prime-overlap tariff is currently one-signed. A stronger source-specific reserve does not by itself control a sign-changing first mode.

**Boundary.** WI-278 is a logical scalar-profile countermodel, not an alternative Weil operator. WI-279 proves no source-specific noncommensurate compatibility and no nodal theorem. The bottom-Toeplitz coefficient is sharp only for generic PSD null-partition geometry; the actual Suzuki null mode may satisfy additional constraints capable of further gain.
