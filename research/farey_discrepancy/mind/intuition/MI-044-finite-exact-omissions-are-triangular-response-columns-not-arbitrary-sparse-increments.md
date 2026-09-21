# MI-044 — Finite exact omissions are triangular response columns, not arbitrary sparse increments

**Evidence level:** exact algebraic synthesis from [FD-245](../../findings/FD-245-finite-exact-omission-geometry-removes-the-sparse-double-log-penalty.md), read against the sharp arbitrary-sparse reciprocal-divisor norm in FD-244. The conclusion is for exact response zeros with a bounded omission count under `|b_n|<=Cn`.

If `E_N` contains the `K` omitted response locations and `Y(m)=0` on `[1,N]\E_N`, exact divisor inversion gives, for every `n<=N`,

`b_n = sum_(m in E_N) Y(m) (1_(m|n)-1_((m+1)|n))`.

An omitted response value therefore contributes an adjacent divisor-difference column. It does not create an arbitrary uncontrolled increment concentrated at a divisor-rich integer. Ordering `E_N={e_1<...<e_K}` makes the map from omitted amplitudes `Y(e_i)` to the coordinates `b_(e_i)` triangular, and the envelope `|b_n|<=Cn` yields

`sum_(n<=N)|b_n| <= 2 C N (2^K-1)`.

For fixed `K`, the normalized top-octave mass is consequently `O_(C,K)(1/N)`. The `N log log N` scale obtained by applying the sharp sparse `sigma_-1` norm to `K` arbitrary increments is not intrinsic to finite exact sampling defects. One omission already has examples with coefficient mass of order `N`, so the linear `N` scale itself is real while the double logarithm is a relaxation artifact.

The reusable distinction is that **a sparse-set norm may be sharp for the relaxed increment class and still be nonsharp for the structured image of actual missing measurements**. Before transferring a sparse defect estimate to sampling, preserve the exact column geometry produced by inversion.

**Boundary.** The current triangular bound grows like `2^K`; it does not settle the regime `K=K(N)->infinity` and does not contradict the FD-244 arbitrary-sparse lower examples. It also does not add positivity or arithmetic coherence. The unresolved quantitative problem is the exact omission-operator norm in growing-defect regimes, where column interaction rather than the bare reciprocal-divisor mass may determine the transition.