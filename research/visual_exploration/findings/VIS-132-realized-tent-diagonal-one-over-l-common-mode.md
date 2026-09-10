# VIS-132 — the realized tent diagonal carries an exact `1/L` common-mode fluctuation

## Claim

Continue the bounded-source finite-CUE statistic of `VIS-130` and `VIS-131`. Let `U_N` be Haar distributed in `U(N)`, write its eigenangles in one non-wrapping chart as `theta_j in (-pi,pi]`, and unfold them by

`y_j = N theta_j/(2 pi)`.

Fix a tent-support ratio

`alpha = M/N in (0,1)`

and use the source taper

`h_M(y) = (1-2|y|/M)_+`,

whose squared mass is

`H_2 = integral_R h_M(y)^2 dy = M/3`.

For any realized connected pair statistic with the `VIS-130` source convention, the diagonal pairs `j=k` contribute the random quantity

`D_(N,M) = H_2^(-1) sum_j h_M(y_j)^2`
`          = (3/M) sum_j h_M(y_j)^2`.

This term is independent of the support-edge coordinate `q`, because the Montgomery weight and oscillatory phase both equal one at zero difference.

Put

`f_alpha(theta) = (1-|theta|/(pi alpha))_+^2`.

Then `D_(N,M)=(3/(alpha N)) sum_j f_alpha(theta_j)`, and its Fourier coefficients are

`hat f_alpha(0)=alpha/3`,

`hat f_alpha(k)`
` = 2(pi alpha k - sin(pi alpha k))/(pi^3 alpha^2 k^3)`,  `k>=1`,

with `hat f_alpha(-k)=hat f_alpha(k)`. The exact CUE trace covariance therefore gives

`E[D_(N,M)] = 1`

and

`Var(D_(N,M))`
` = [18/(alpha^2 N^2)] sum_(k>=1) min(N,k) |hat f_alpha(k)|^2`.

For every fixed `alpha in (0,1)`, define

`Sigma_diag^2(alpha)`
` = [18/alpha^2] sum_(k>=1) k |hat f_alpha(k)|^2`.

The series is finite and strictly positive. Since `hat f_alpha(k)=O(k^-2)`,

`Var(D_(N,M)) = Sigma_diag^2(alpha)/N^2 + O(N^-4)`,

and the CUE linear-statistic central limit theorem gives

`N(D_(N,M)-1)  ->  Normal(0,Sigma_diag^2(alpha))`.

Consequently, in the support-edge scaling `N/L -> rho>0`, `M/L -> kappa>0`, with fixed `alpha=kappa/rho<1`, the **realized diagonal alone has a nondegenerate stochastic fluctuation of order `1/L`**.

This is exactly the same scale on which `VIS-131` leaves open a candidate arithmetic mean residual. However, the nuisance is structurally simple: it is the same scalar in every `q` coordinate. A samplewise realized-diagonal subtraction removes it exactly, and any linear contrast `sum_r c_r C(q_r)` with `sum_r c_r=0` cancels it identically. Subtracting only the ensemble mean diagonal `1` does **not** remove the random `D_(N,M)-1` term.

**Evidence/status:** `EXACT-DERIVED + LITERATURE CUE TRACE COVARIANCE/CLT + STOCHASTIC NUISANCE CONTROL + NO-NOVELTY-CLAIM`.

No formula for the off-diagonal covariance, no total variance estimate for the bounded-tent statistic, no zeta-to-CUE transfer theorem, no arithmetic residual, and no implication toward RH is claimed.

## 1. The random diagonal hidden behind the deterministic mean `1`

`VIS-130` writes the exact connected bounded-tent CUE expectation as

`C_(N,L,M)(q)`
` = 1 - integral_(-M)^M A_M(x) W_L(x) D_N(x)^2 exp(2 pi i q x) dx`.

The leading `1` is the **ensemble mean** of the diagonal contribution. To expose the realized quantity, consider the natural source-windowed pair estimator before ensemble averaging,

`C_hat(q)`
` = H_2^(-1) { sum_(j,k) h_M(y_j) h_M(y_k)`
`       W_L(y_j-y_k) exp(2 pi i q(y_j-y_k)) - B(q) }`,

where `B(q)` is the deterministic independent-density background integral with the same taper, weight and phase. The CUE distinct-pair density is `1-D_N(x)^2`, so the deterministic background removes its `1` part and `E[C_hat(q)]=C_(N,L,M)(q)`.

For `j=k`, the difference is zero. Hence `W_L(0)=1`, the phase is one, and the diagonal part of `C_hat(q)` is exactly

`D_(N,M)=H_2^(-1) sum_j h_M(y_j)^2`,

independent of `q`. Its mean is one, but a single matrix realization does not replace it by its mean.

This distinction matters for the accepted support-edge clue: a convention described only as “include the diagonal and subtract `1`” still leaves a random common mode. A convention that subtracts the **realized** diagonal source mass does not.

## 2. Exact CUE variance from the tent-square Fourier coefficients

In eigenangle coordinates,

`h_M(N theta/(2 pi))^2 = f_alpha(theta)`

with `alpha=M/N`. Uniform one-point density gives

`E[sum_j f_alpha(theta_j)] = N hat f_alpha(0)`.

Direct integration yields

`hat f_alpha(0)`
` = (1/pi) integral_0^(pi alpha) (1-theta/(pi alpha))^2 dtheta`
` = alpha/3`,

which proves `E[D_(N,M)]=1`.

For `k>=1`, the same elementary integral gives

`hat f_alpha(k)`
` = (1/pi) integral_0^(pi alpha)`
`     (1-theta/(pi alpha))^2 cos(k theta) dtheta`
` = 2(pi alpha k - sin(pi alpha k))/(pi^3 alpha^2 k^3)`.

Expanding the real linear statistic in CUE traces,

`sum_j f_alpha(theta_j) - N hat f_alpha(0)`
` = sum_(k>=1) hat f_alpha(k) Tr(U_N^k)`
`   + sum_(k>=1) hat f_alpha(k) Tr(U_N^(-k))`.

Diaconis and Evans record the exact Haar-unitary covariance

`E[Tr(U_N^j) Tr(U_N^(-k))] = delta_(jk) min(N,k)`.

All same-sign second moments vanish. Therefore

`Var(sum_j f_alpha(theta_j))`
` = 2 sum_(k>=1) min(N,k) |hat f_alpha(k)|^2`,

which gives the displayed exact variance of `D_(N,M)` after multiplying by `9/(alpha^2 N^2)`.

## 3. The diagonal noise is genuinely on the support-edge `1/L` scale

The tent-square has a derivative cusp at the chart center, so its Fourier coefficients decay as `O(k^-2)`. Thus

`sum_(k>=1) k |hat f_alpha(k)|^2 < infinity`.

Replacing `min(N,k)` by `k` changes the variance of the unnormalized linear statistic by

`2 sum_(k>N) (k-N)|hat f_alpha(k)|^2 = O(N^-2)`.

It follows that

`Var(D_(N,M))`
` = Sigma_diag^2(alpha)/N^2 + O(N^-4)`.

The same weighted Fourier summability is the standard hypothesis for the CUE linear-statistic central limit theorem of Diaconis--Evans/Johansson. Therefore the centered unnormalized tent-square statistic converges without normalization to a nondegenerate Gaussian, and multiplying by `3/(alpha N)` yields

`N(D_(N,M)-1) -> Normal(0,Sigma_diag^2(alpha))`.

Under `N=rho L+o(L)` and `M=kappa L+o(L)` with `alpha=kappa/rho` fixed,

`L(D_(N,M)-1)`

has a nonzero limiting fluctuation scale. The stochastic diagonal cannot therefore be discarded merely because its ensemble expectation is exactly one.

## 4. A zero-sum edge contrast kills this nuisance exactly

Let `C_hat(q_1),...,C_hat(q_R)` use the same realized CUE spectrum and source taper. Their diagonal vector is

`D_(N,M) (1,1,...,1)`.

For any deterministic coefficients with

`sum_(r=1)^R c_r = 0`,

the diagonal contribution to

`sum_r c_r C_hat(q_r)`

is exactly zero for every realization, every `N`, and every admissible `M`; this is not an asymptotic cancellation. Equivalently, define a samplewise diagonal-subtracted statistic by removing `D_(N,M)` before forming the edge residual. The common-mode fluctuation disappears identically.

By contrast, replacing `D_(N,M)` by its ensemble mean `1` leaves `D_(N,M)-1`, whose standard deviation is `Theta(1/L)` in the fixed-ratio support-edge regime. A proposed arithmetic mean displacement at that same scale can therefore be confused with source-count fluctuation unless the diagonal convention is fixed at the realized-statistic level or the decision statistic annihilates the common mode.

This exact cancellation is useful because it removes one nuisance direction without fitting any coefficient to zeta zeros and without consuming source confirmation data.

## Prior-art and novelty assessment

Persi Diaconis and Steven N. Evans, **Linear functionals of eigenvalues of random matrices**, *Transactions of the American Mathematical Society* 353:7 (2001), 2615–2633, DOI `10.1090/S0002-9947-01-02800-8`, record the exact CUE trace covariance in Theorem 2.1(b) and develop the Fourier linear-statistic CLT used above. The trace covariance originates in the Diaconis--Shahshahani moment calculation. No novelty is claimed for either theorem or for the Fourier analysis of a compact tent-square test function.

Alex Altland, Francisco Divi, Tobias Micklitz, Silvia Pappalardi, and Maedeh Rezaei, **Statistics of the random matrix spectral form factor**, *Physical Review Research* 7 (2025), 033138, DOI `10.1103/n7rj-gwwj`, emphasize that the ordinary random-matrix spectral form factor is non-self-averaging: its fluctuations can remain comparable to its mean at large matrix size. That result is a **boundary on interpretation**, not an input to the proof here. The bounded-tent off-diagonal statistic is different and its covariance must still be derived rather than imported from the full-circle SFF.

The Mathia-specific contribution is only the control specialization: the deterministic diagonal `1` in the `VIS-130` mean corresponds, in a single realization, to a tent-square CUE linear statistic with an exact `1/L` common-mode fluctuation. Identifying its scale and its exact samplewise cancellation narrows the active covariance gate; it is not a new CUE theorem.

## Boundary and falsification

The finite-`N` expectation and variance formula above are exact for the non-wrapping fixed-ratio tent chart. The stated CLT is for fixed `alpha in (0,1)` as `N->infinity`. A taper whose support ratio shrinks, grows toward the circle capacity, or changes shape with `N` requires a separate triangular-array analysis.

This finding controls only the `j=k` component. It does **not** imply that the total bounded-tent covariance is `Theta(L^-2)`. The off-diagonal quadratic statistic can have larger fluctuations and can be correlated with the diagonal linear statistic, so their variances must not be added as though independent. In particular, the non-self-averaging of the ordinary full-circle SFF is a warning that an `O(1)` off-diagonal stochastic floor is possible in related observables, not evidence that the same floor occurs here.

The result is CUE-side only. It says nothing yet about stochastic Riemann--von Mangoldt counting error, local unfolding error, independence between distinct zeta height windows, or an exact finite-height transfer from Riemann zeros to this CUE observable. No fresh zeta confirmation data are inspected or required.

## Research consequence

The accepted Montgomery support-edge clue can sharpen its covariance requirement immediately. Before deriving or simulating the remaining joint null, define the frozen edge statistic with either **samplewise realized-diagonal subtraction** or an explicitly zero-sum coordinate contrast. This removes an otherwise unavoidable `Theta(1/L)` common-mode nuisance without fitting to the source.

After that exact projection, the genuinely unresolved object is the joint covariance of the **off-diagonal** bounded-tent CUE statistic, together with finite-height zeta-to-CUE transfer and unfolding/counting uncertainty. If the off-diagonal covariance retains an `O(1)` floor, many effectively independent source windows would be needed to resolve a `1/L` mean residual; if it decays, its actual rate determines the confirmation budget. `VIS-132` does not decide between those possibilities.