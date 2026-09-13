# MI-019 — Simultaneous cuts have complementary sharp mass and cross-cut shift reserves

**Evidence level:** exact at a hypothetical attained first unrestricted Suzuki crossing through [WI-274](../../findings/WI-274-simultaneous-cuts-create-a-positive-saturated-source-reserve.md), [WI-275](../../findings/WI-275-a-harmonic-minimax-reserve-is-the-sharp-mass-only-cut-bound.md), and [WI-276](../../findings/WI-276-cross-cut-energy-obeys-a-sharp-nilpotent-shift-reserve.md). The total reserves are sign-independent. The prime-overlap corollary remains conditional on a one-signed null mode, and no theorem yet forces the combined reserve above the positive archimedean budget.

Single-cut localization prices each cut separately and hits a sharp Carleman wall as an internal gap closes. WI-274 changes the order of operations: impose firstness for all sharp cuts and integrate the family before estimating the source. A source pair at lag `h` crosses a set of cuts of length exactly `h`, leaving a positive saturated source reserve even though the endpoint eigenvalue is zero.

WI-275 computes the sharp envelope of the complementary **mass-only** information. With

`Q_t >= A_t M_L(t)`, `Q_t >= B_t M_R(t)`, `M_L+M_R=1`,

where `A_t=lambda_((a+t)/2)` and `B_t=lambda_((a-t)/2)`, one gets

`Q_t >= A_t B_t/(A_t+B_t)`

and hence

`S_v >= R_harm(a) := 2 integral_0^a lambda_r lambda_(a-r)/(lambda_r+lambda_(a-r)) dr`.

The equality mass profile is monotone, so CDF monotonicity cannot improve this envelope. The complementary-mass relaxation is exhausted.

WI-276 then retains information that WI-275 discards: the same null vector couples **different cuts**. Put `f(t)=sqrt(Q_t)`. Splitting the null mode at `t` and `t+2r` gives

`|F_v(r)-S_v| <= integral f(t) f(t+2r) dt`.

Because `f` is supported in `[-a,a]`, translation by `2r` is a nilpotent contraction of order `N=ceil(a/r)`. The sharp Haagerup--de la Harpe numerical-radius inequality yields

`S_v >= R_shift(r) := r lambda_r/(1+cos(pi/(ceil(a/r)+1)))`.

Therefore the current sign-free reserve is

`S_v >= max(R_harm(a), sup_(0<r<a) R_shift(r))`.

The shift coefficient is itself sharp if one retains only `Q>=0` and compact support. This is a second relaxation boundary: generic one-shift decorrelation cannot improve WI-276. Any further reserve must exploit information absent from both sharp relaxations, such as the exact Weil-source shape of `Q_t`, compatibility among several shifts, regularity/nodal constraints of the actual first null mode, or a finite compression of the PSD signed-source multiplier family.

On a one-signed branch the weighted prime overlap obeys `P_v >= S_v-K_+`. The immediate scalar test is therefore the **maximum** of the harmonic and shift reserves against `K_+`, not either bound in isolation. If rigorous constraints on `r -> lambda_r` force this maximum above `K_+`, complete prime screening is impossible on that branch. If an admissible profile keeps both below the budget, the next theorem must use source/eigenfunction shape rather than another universal relaxation.

**Boundary.** Neither reserve proves that the first null mode is one-signed or forces prime overlap on a sign-changing branch. Their abstract sharpness extremizers need not be simultaneously compatible with Suzuki's exact null equation; that possible incompatibility is now one of the main remaining sources of quantitative gain.
