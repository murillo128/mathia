# VIS-138 — exact CUE marginals do not determine cross-window averaging without a uniform mixing law

## Claim

Let `mu_N` be Haar measure on `U(N)` and let `F_N:U(N)->R` be any square-integrable centered scalar statistic with

`E_mu F_N = 0`,  `Var_mu(F_N)=sigma_N^2>0`.

For the frozen support-edge program, `F_N` may be the already predeclared single-window contrast after its within-window taper, effective-size convention, diagonal subtraction, edge coordinates, and fixed smoothing have been applied.

For any `q in [0,1]`, define a stationary CUE-valued refresh chain by the transition kernel

`P_q(U,dV)=q delta_U(dV)+(1-q) mu_N(dV)`.

Thus at each step the chain either keeps the current CUE matrix with probability `q` or refreshes it from an independent CUE draw with probability `1-q`. If `U_0~mu_N`, then every `U_j` is **exactly CUE(N)**. Nevertheless, for every lag `h>=0`,

`Cov(F_N(U_0),F_N(U_h)) = q^h sigma_N^2`.

For `q<1` the chain is reversible and geometrically mixing, with mean-zero transition operator exactly `q I` and spectral gap `1-q`. Its long-run variance is

`tau_N(q)=sigma_N^2 (1+q)/(1-q)`.

Consequently the same exact one-window CUE law supports radically different averaging behavior. `q=0` gives independent windows and the ordinary `Theta(L^2)` count for detecting an `a/L` mean shift. Fixed `q>0` preserves the exponent but inflates the required count by `(1+q)/(1-q)`. If

`q_L = 1-c L^(-alpha)+o(L^(-alpha))`,  `c>0`, `alpha>0`,

and `sigma_N^2` stays bounded away from zero and infinity, then

`tau_N(q_L) ~ (2 sigma_N^2/c) L^alpha`,

so fixed signal-to-noise against an `a/L` shift requires

`m = Theta(L^(2+alpha))`.

At `q=1` the same CUE matrix is reused forever, `Cov(F_0,F_h)=sigma_N^2`, and averaging does not reduce the variance at all.

Therefore **exact single-window CUE calibration — even together with exact finite-`N` means, variances, cumulants, and within-window edge covariance — places no useful bound on the cross-window averaging law by itself**. To infer the feasibility exponent for actual zeta height windows one needs a genuinely cross-height statement: a direct covariance law, a uniform mixing/spectral-gap estimate in the `L`-dependent regime, or another dependence theorem strong enough to control the zero-frequency mass.

**Evidence/status:** `EXACT-DERIVED + MATCHED-MARGINAL MARKOV CONTROL + NEGATIVE IDENTIFIABILITY RESULT + CLASSICAL MARKOV-CHAIN INGREDIENTS + NO-NOVELTY-CLAIM`.

This finding does not assert that separated Riemann-zero windows form a Markov chain, satisfy CUE marginals exactly, or exhibit any particular value of `q_L`. The refresh family is a falsification control showing what one-window random-matrix agreement cannot identify.

## 1. Exact CUE marginal preservation

For any measurable set `A subset U(N)`,

`int P_q(U,A) mu_N(dU)`
` = q mu_N(A) + (1-q) mu_N(A)`
` = mu_N(A)`.

Hence `mu_N` is invariant. Starting the chain from `mu_N` makes it stationary and gives the exact CUE marginal at every source-window index.

The stationary two-point measure is

`mu_N(dU) P_q(U,dV)`
` = q mu_N(dU) delta_U(dV) + (1-q) mu_N(dU) mu_N(dV)`,

which is symmetric in `U,V`. Thus the chain is reversible.

For `q<1`, iterating the kernel gives the exact identity

`P_q^h(U,dV)=q^h delta_U(dV)+(1-q^h) mu_N(dV)`.

So the dependence dies geometrically for every fixed `q<1`; this is not a pathological non-mixing counterexample.

## 2. The covariance sequence is exact

For any centered `F_N`,

`P_q F_N(U)`
` = q F_N(U) + (1-q) E_mu F_N`
` = q F_N(U)`.

Therefore `P_q^h F_N=q^h F_N`, and stationarity gives

`gamma_N(h)`
` = E[F_N(U_0)F_N(U_h)]`
` = <F_N,P_q^h F_N>_(L^2(mu_N))`
` = q^h sigma_N^2`.

Substitution into the exact averaging identity of `VIS-136` yields

`Var(bar F_m)`
` = (sigma_N^2/m) [1+2 sum_(h=1)^(m-1) (1-h/m)q^h]`.

For fixed `q<1`, dominated convergence of the geometric series gives

`Var(bar F_m) ~ [sigma_N^2/m] (1+q)/(1-q)`.

Thus a surrogate can be perfectly calibrated to the complete one-window CUE distribution and still carry an arbitrarily large short-memory variance inflation.

## 3. Uniform mixing, not pointwise mixing, controls the `L`-dependent experiment

The support-edge residual target shrinks like `1/L`, while the matched finite-CUE null itself changes with the effective size. It is therefore insufficient to know merely that each fixed-`L` surrogate is geometrically mixing.

Take

`q_L=1-cL^(-alpha)+o(L^(-alpha))`.

Then

`1-q_L ~ cL^(-alpha)`

and the exact relaxation/mixing scale of the refresh chain is order `L^alpha`. Also

`(1+q_L)/(1-q_L) ~ (2/c)L^alpha`.

Using `VIS-136`, a mean shift `a/L` has asymptotic squared signal-to-noise of order

`m / L^(2+alpha)`

up to nonzero constants when `sigma_N^2` is order one. Hence fixed signal-to-noise requires `m=Theta(L^(2+alpha))`, while making stochastic error `o(1/L)` requires `m/L^(2+alpha)->infinity`.

This gives a concrete failure mode for an argument that says only "the null is mixing". The needed hypothesis must control the dependence **uniformly along the same asymptotic sequence in which the residual shrinks**.

## 4. Why single-window finite-CUE calculations cannot close the source-height gate

`VIS-131`--`VIS-135` determine increasingly detailed properties of one bounded-tent finite-CUE window: the edge mean, the removable realized diagonal mode, the terminal amplitude covariance, and the Gaussian/Wick covariance floor after fixed smoothing. `VIS-137` additionally shows that one fixed-ratio CUE circle cannot manufacture a growing pool of pairwise-disjoint translated source windows.

The refresh family proves a complementary limitation. Even if every admissible source window were assigned the **exact same complete CUE marginal law** used in those one-window calculations, the coupling between windows remains free enough to realize independent averaging, arbitrarily slow uniformly degrading short memory, or a persistent common mode without changing that marginal law at all.

Therefore a multi-CUE simulation in which matrices are sampled independently is a valid calculation **conditional on that coupling**, but it is not evidence for the coupling of separated zeta height windows. Conversely, observing excellent one-window finite-CUE agreement cannot justify an `L^2` source-window budget unless cross-height dependence is controlled separately.

## 5. Prior-art audit

The refresh kernel and its spectral calculation are standard Markov-chain/probability constructions; no novelty is claimed for the general mechanism. The operator viewpoint, reversibility, spectral gap, and geometric mixing language are standard material in David A. Levin, Yuval Peres, and Elizabeth L. Wilmer, *Markov Chains and Mixing Times*, 2nd ed. The familiar variance inflation factor `(1+lambda)/(1-lambda)` associated with a Markov-chain absolute spectral parameter also appears in general concentration bounds, for example Jianqing Fan, Bai Jiang, and Qiang Sun, *Hoeffding's lemma for Markov Chains and its applications to statistical learning*, arXiv:1802.00211.

The Mathia-specific content is the use of this exact matched-marginal family as a **negative identifiability control** for the already frozen Montgomery support-edge experiment. It shows that the next unresolved quantity in the accepted clue cannot be supplied by stronger one-window CUE calibration alone.

## Consequence for the accepted support-edge clue

The source-window gate can now be stated more sharply. A proposed zeta-to-random-matrix transfer adequate for a `1/L` residual must include not only a one-window finite-CUE approximation but enough **joint** information to bound the low-frequency covariance mass uniformly in `L`.

For a Markov or approximately Markov surrogate, a uniform lower bound on the relevant spectral gap would preserve the quadratic exponent; a gap shrinking like `L^-alpha` permits an `L^(2+alpha)` requirement even though every fixed-`L` model is geometrically mixing. More generally, the direct covariance regimes in `VIS-136` remain the authoritative formulation when no Markov structure is justified.

This does not yet provide the actual zeta cross-height covariance law or the finite-height transfer estimate. It closes only the inference route from **single-window CUE agreement to effective source-window independence/mixing**.

## Boundaries

No untouched confirmation-zero dataset is inspected. No arithmetic residual amplitude is fitted or assumed. No claim is made that CUE refresh chains model Riemann zeros physically or arithmetically.

The finding is a control theorem: exact CUE marginals and even pointwise-in-`L` geometric mixing are insufficient unless the dependence estimate is uniform at the shrinking `1/L` signal scale.