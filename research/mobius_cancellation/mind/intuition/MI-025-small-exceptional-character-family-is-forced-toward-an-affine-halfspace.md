# MI-025 — Near-negative exceptional characters obey dual odd-girth and entropy-rank rigidity

**Evidence level:** exact finite Fourier/information consequence of [MC-289](../../findings/MC-289-odd-moment-character-bias-from-collision-rich-shells.md), [MC-290](../../findings/MC-290-odd-moment-exception-set-near-affine-rigidity.md), [MC-291](../../findings/MC-291-near-negative-spectrum-dual-odd-girth.md), and [MC-292](../../findings/MC-292-entropy-rank-budget-beyond-union-threshold.md). These are interface theorems for the collision-rich odd shell; they supply no new character-sum estimate or bound for `M(x)`.

Let `eta=N^2/(2^r sum_s n_s^2)` be the effective occupancy and let `A_lambda` be the generated quadratic-character shell sums. When short odd relations are absent, MC-289 gives exact odd moments. MC-290 shows that if analytic input controls all but `J` characters above `-delta`, those moments force the exceptional family toward the affine endpoint: when `epsilon_m=delta^(m-2)(eta^-1-1)` is small and `log J=o(m)`, one exceptional character is `-1` on a `1-o(1)` fraction of weighted shell mass.

MC-291 adds a collective constraint that does not come from another moment estimate. Write the positive-side defect of a negative character as `d_lambda=(1+A_lambda/N)/2` and let `E_tau={lambda ne 0:d_lambda<=tau}`. If distinct `lambda_1,...,lambda_j in E_tau` have odd cardinality and sum to zero, then

`sum_i d_(lambda_i) >= 1`.

Hence `E_tau` has no odd circuit of length `j` with `j tau<1`. The near-negative spectrum itself therefore inherits a dual odd-girth gap. When `R` linearly independent near-negative modes also satisfy `R tau<1`, their common preferred-sign cell contains at least `(1-R tau)N` weighted shell mass, and Cauchy--Schwarz gives

`eta <= 2^(-R)/(1-R tau)^2`.

MC-292 shows that the loss of a common-cell guarantee at `R tau>=1` is not a loss of all rank control. For any linearly independent modes `lambda_1,...,lambda_R`, with their individual preferred-sign defects `d_i`, collision entropy and Shannon subadditivity give the exact budget

`sum_(i=1)^R [1-h_2(d_i)] <= log_2(1/eta)`.

Therefore, if all `d_i<=tau<1/2`,

`R <= log_2(1/eta)/(1-h_2(tau))`

with no `R tau<1` condition. Each independent biased direction spends a positive amount of the shell's finite entropy deficit. The common-cell and entropy mechanisms are complementary: MC-291 records actual simultaneous preferred-sign mass when total defect is small; MC-292 still bounds independent bias complexity when those defect sets can cover the whole shell.

The reusable interface is now three-level. A small analytically exceptional family is forced **toward** the affine endpoint by MC-290; MC-291 constrains the exact odd-relation/common-cell geometry of modes sufficiently close to that endpoint; MC-292 constrains the total independent bias budget even after the common-cell intersection test has failed. Future arithmetic input can attack exceptional-family size, defect profile, effective occupancy, conductor, dual rank, or the impossibility of concentrating source-generated product characters in the finite low-information alternatives left by these bounds.

**Boundary.** These conclusions depend on the exact finite Fourier identities and on `eta` not being too small. MC-292 controls rank weighted by bias, not cardinality or conductor; exponentially many biased characters may lie in a low-dimensional dual subspace. Neither entropy nor odd-girth excludes the affine endpoint, proves a lower bound on `eta`, or supplies the required arithmetic exceptional-character theorem. The common sign cell is a structural alternative, not evidence that the actual arithmetic shell realizes it.