# MI-079 — Fixed-order moment convergence removes density defect, not every negative direction

**Evidence level:** supported conditional synthesis of [WI-456](../../findings/WI-456-retracted-moment-transport-leaves-only-a-conditional-density-capstone.md). Its persisted primary-source correction withdraws the Yang--Yang unconditional higher-moment transport from the fourth-moment tier onward. Model algebra and finite certificates do not establish that missing arithmetic input. The surviving implication below is a classical abstract moment argument, not a zeta moment theorem or an RH result.

Let `A_T` be Hermitian of dimension `d_T`, with `d_T/N_T -> 1` and `N_T -> infinity`. Suppose the empirical spectral measures `mu_T=d_T^(-1)sum_j delta_(lambda_j(A_T))` converge in every fixed moment to a probability measure `nu` with all moments finite, which is **Hamburger determinate** and has `nu((-infinity,0])=0`. Suppose separately that the actual source gives

`n_+(A_T) <= (N_T+S_T)/2 + o(N_T)`, `0<=S_T<=N_T`.

Then `n_(<=0)(A_T)=o(N_T)` and `S_T/N_T -> 1`.

The bounded second moment gives tightness. For each fixed `r`, a bounded even moment of order `2s>r` gives the tail control

`int_(|x|>R)|x|^r dmu_T <= C_s R^(r-2s)`.

Every weak subsequential limit therefore has all the prescribed moments. Hamburger determinacy identifies it with `nu`; the closed-set inequality for `(-infinity,0]` removes the entire nonpositive spectral mass. A zero-atom estimate alone would not remove negative eigenvalues, and Stieltjes uniqueness alone is not the stated uniqueness hypothesis for these indefinite matrices.

For an exact zero-block form, a simple critical zero supplies at most one positive direction, a multiple critical point at most one, and a mirror pair at most one. Counting multiplicity yields the displayed positive-index budget. Applying it to a truncated arithmetic matrix still needs its actual tail/counting estimate: a small operator-norm perturbation does not preserve inertia near zero.

No uniform rate in moment order is needed. Likewise, if independently justified fixed-order certificates give `liminf_T S_T/N_T >= 1-2lambda_k` for every fixed `k`, with `lambda_k -> 0`, taking the supremum of these bounds on a single liminf proves density one. The missing step is arithmetic transport, not an interchange of the two limits.

Individual exceptions remain invisible: `A_d=diag(-1,1,...,1)`, `N_d=d`, `S_d=d-2` has limiting measure `delta_1`, obeys the counting budget with equality, and retains one negative direction for every `d>=2`. Thus even a valid complete fixed-order moment tower would require an additional individual-block detector to exclude every exceptional zero. This finite-matrix control is not an asserted zeta-zero configuration.
