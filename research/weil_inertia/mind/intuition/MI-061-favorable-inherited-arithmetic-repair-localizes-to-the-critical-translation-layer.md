# MI-061 — Favorable inherited arithmetic repair localizes to the critical translation layer

**Evidence level:** exact source-conditioned operator synthesis from [WI-380](../../findings/WI-380-gamma-negative-source-zero-modes-localize-favorable-arithmetic-to-critical-shifts.md), refining the unrestricted signed-translation question left by WI-379. The autocorrelation support geometry is elementary; the line-specific content is its interaction with the exact Desogus source-zero/gamma-negative modes.

For every fixed gamma depth `0<=eta<C_Gamma`, WI-380 constructs source-zero trials whose positive half is supported in a fixed-width interval centered at `A_k/2`, with `A_k=log(k+1)`, while retaining gamma energy at most `-eta||F_k||_2^2`. Odd extension produces two one-signed lobes separated across the origin.

Their autocorrelation has an exact sign/support pattern: small physical shifts `0<h<L_eta` overlap each lobe with itself and give `C_k(h)>=0`; the middle range is zero; only cross-origin shifts satisfying `|h-A_k|<=L_eta` can give `C_k(h)<=0`. Because each inherited arithmetic translation carries coefficient `-Lambda(n)/sqrt(n)`, positive repair can therefore come only from

`|log n-A_k|<=L_eta`, equivalently `|log n/A_k-1|<=L_eta/A_k -> 0`.

Thus ambient rank is not merely insufficient: on these certified negative modes, every favorable arithmetic branch is forced into the critical normalized layer `r=1+o(1)`. Fixed prime-power shifts, any fixed normalized region away from `1`, and a stationary small-shift/Toeplitz bulk symbol cannot pay the fixed gamma tariff on this family.

**Boundary.** This is a localization of where positive credit may occur, not a bound on its size. The critical annulus `n≈k` contains many prime powers and may carry large Mangoldt mass. The direct repair route is closed only if that annular contribution is quantitatively too small; alternatively the admissible domain could exclude these source-zero trials before evaluation of the old--old form.