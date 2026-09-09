# VIS-121 — deterministic CUE window triads admit exact finite Toeplitz calibration

## Claim

Let the eigenangles of Haar `CUE_N` be viewed as the determinantal point process on `[0,2 pi)` with projection kernel

`K_N(theta,phi) = (1/(2 pi)) sum_(r=0)^(N-1) exp(i r(theta-phi))`.

Fix **before source inspection** a deterministic hard arc

`W=[alpha,alpha+ell)`, `0<ell<=2 pi`,

and compactify that arc linearly by

`psi(theta)=2 pi (theta-alpha)/ell`.

For every integer frequency `q`, put

`g_q(theta)=1_W(theta) exp(i q psi(theta))`,

and let `P_N` be the orthogonal projector onto

`H_N=span{exp(i r theta)/sqrt(2 pi): 0<=r<N}`.

Define the finite compression

`A_q = P_N M_(g_q) P_N`.

For positive `a,b`, let `F_(a,b)^W` be the collision-free wrapped triad of the CUE points that fall in `W`, as defined in `VIS-120` after applying `psi`:

`F_(a,b)^W`
` = sum_(i,j,k pairwise distinct; theta_i,theta_j,theta_k in W)`
`     exp(i[a psi(theta_i)+b psi(theta_j)-(a+b)psi(theta_k)])`.

Then the **exact finite-`N` mean, Hermitian covariance, and pseudo-covariance of any finite predeclared panel of these windowed collision-free triads are deterministic finite matrix expressions in the `A_q`**. No Monte Carlo null estimate is required for this hard-window CUE model.

More precisely, for an integer list `q=(q_1,...,q_m)` define

`D_m(q_1,...,q_m)`
` = sum_(sigma in S_m) sgn(sigma)`
`     product_(cycles c=(i_1 ... i_k) of sigma)`
`       tr(A_(q_(i_1)) ... A_(q_(i_k))).`

Then `D_m` is exactly the CUE expectation of the ordered pairwise-distinct `m`-point Fourier product with labels `q_1,...,q_m`. In particular, with `c=-(a+b)`,

`mu_(a,b)^W := E_CUE[F_(a,b)^W] = D_3(a,b,c)`.

For two triads, their exact second moments are finite sums of `D_m` with `3<=m<=6`, indexed by the possible cross-identifications of the two internally distinct triples. Hence every covariance entry is computable from matrices of size only `N x N` once `N`, `ell`, the compactification, and the frequency panel are frozen.

For the arc above, the matrix entries are explicit. For `0<=r,s<N`, set

`lambda_(r,s,q)=(s-r)+2 pi q/ell`.

Then

`(A_q)_(r,s)`
` = exp(i(s-r)alpha)/(2 pi)`
`     integral_0^ell exp(i lambda_(r,s,q) t) dt`.

Thus, when `lambda_(r,s,q) != 0`,

`(A_q)_(r,s)`
` = exp(i(s-r)alpha)`
`   [exp(i lambda_(r,s,q) ell)-1]/[2 pi i lambda_(r,s,q)]`,

while for `lambda_(r,s,q)=0`,

`(A_q)_(r,s)=exp(i(s-r)alpha) ell/(2 pi)`.

Up to a common diagonal unitary conjugation these are Toeplitz matrices, so all trace-word null moments are independent of the arc origin `alpha`, as CUE rotation invariance requires.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL-DPP-MACHINERY + FINITE-WINDOW-CUE NULL + SOURCE-DICTIONARY ADVANCE + NO-NOVELTY-CLAIM`.

No zeta anomaly, finite-height arithmetic excess, Gaussian limit, independence claim, universal fixed-count calibration, or RH implication is established.

## 1. Distinct-point CUE moments reduce to cycle traces

For the CUE projection process, the `m`-point factorial correlation density is

`rho_m(theta_1,...,theta_m)=det[K_N(theta_i,theta_j)]_(i,j=1)^m`.

Therefore the ordered distinct-point moment with labels `q_1,...,q_m` is

`D_m(q_1,...,q_m)`
` = integral_(W^m) product_(j=1)^m exp(i q_j psi(theta_j))`
`     det[K_N(theta_i,theta_j)] d theta_1 ... d theta_m`.

Expand the determinant over permutations. For one cycle

`c=(i_1 ... i_k)`,

the corresponding kernel product integrates to

`tr(A_(q_(i_1)) ... A_(q_(i_k)))`.

Different cycles use disjoint variables, so their integrals multiply. Summing the signed permutation expansion gives exactly the displayed cycle-trace formula for `D_m`.

This is finite-dimensional because `K_N` is the rank-`N` projection kernel. It is also source-faithful: the random number of CUE points that happen to fall in the hard arc is already integrated over by the factorial correlations. No separate conditioning on the window count is being inserted.

## 2. The collision-free triad mean is an explicit `D_3`

For

`q=(a,b,-a-b)`,

`VIS-120`'s collision-free statistic is precisely the ordered distinct three-point product represented by `D_3`. Expanding the six permutations gives

`mu_(a,b)^W`
` = tr(A_a) tr(A_b) tr(A_(-a-b))`
`   - tr(A_a A_b) tr(A_(-a-b))`
`   - tr(A_a A_(-a-b)) tr(A_b)`
`   - tr(A_b A_(-a-b)) tr(A_a)`
`   + tr(A_a A_b A_(-a-b))`
`   + tr(A_a A_(-a-b) A_b)`.

This is the exact finite-CUE centering for the statistic **after** hard-window selection and linear rewrapping. It is not obtained by transferring the full-circle Haar trace mean from `VIS-118`, and it does not assume that the selected CUE points are independent or uniformly distributed conditional on their count.

The formula also makes the window dependence inspectable. Changing `ell` changes the compressed multiplication matrices and therefore changes the null mean even though the underlying full CUE ensemble is unchanged.

## 3. The arc matrices are explicit Toeplitz compressions

With basis

`e_r(theta)=exp(i r theta)/sqrt(2 pi)`, `0<=r<N`,

the compression entries are

`(A_q)_(r,s)=<e_r,g_q e_s>`.

Substituting `theta=alpha+t` yields exactly the integral in the claim. The only `alpha` dependence is the factor `exp(i(s-r)alpha)`. Hence there is one diagonal unitary `U_alpha` such that every `A_q(alpha)` is obtained from `A_q(0)` by the same unitary conjugation.

Every quantity appearing in `D_m` is a product of traces of words in the `A_q`, so the complete deterministic-arc null is independent of `alpha`. The nontrivial window parameter is the arc length and, more generally, the chosen selection/compactification rule rather than the arbitrary angular origin.

The matrices are Toeplitz before the common diagonal conjugation because their entries depend on `s-r` and `q`. This gives a compact exact computational representation of the finite-window null without replacing the CUE dependence by an independent-phase approximation.

## 4. Full-circle consistency recovers `VIS-120`

Take `ell=2 pi`. Then

`(A_q)_(r,s)=1` exactly when `r=s+q` lies in `{0,...,N-1}`, and is zero otherwise. Thus `A_q` is the corresponding truncated shift.

For positive `a,b` with `a+b<=N`, all one-cycle and two-cycle terms in the `D_3(a,b,-a-b)` expansion vanish. The two three-cycle traces are each

`N-a-b`.

Consequently

`D_3(a,b,-a-b)=2(N-a-b)`,

which is exactly the full-circle collision-free CUE mean derived independently in `VIS-120` from the classical Haar trace moments.

This recovery is an internal falsification control on the window formula. The deterministic-arc calibration agrees with the already established full-circle boundary when the window becomes the entire circle.

## 5. Exact covariance uses only 34 cross-identification patterns

Let the first internally distinct triad carry frequency labels

`q=(a,b,-a-b)`

and the conjugate of a second triad carry

`r=(-c,-d,c+d)`.

When the product `F_(a,b)^W overline(F_(c,d)^W)` is expanded, each triple is internally pairwise distinct. Therefore equalities between the two triples can only form a **partial matching** between their three labelled positions: a point in the first triple can coincide with at most one point in the second and conversely.

There are

`sum_(k=0)^3 binom(3,k)^2 k! = 1+9+18+6 = 34`

such partial matchings.

For a particular partial matching `P` of size `k`, merge every matched pair of labels by addition. Because this is a unit-weight hard window,

`g_u(theta) g_v(theta)=g_(u+v)(theta)`

on a shared selected point. Leave every unmatched label unchanged, and call the resulting list of `6-k` frequency labels `L(P)`.

The equality pattern represented by `P` then contributes exactly

`D_(6-k)(L(P))`.

Hence

`E[F_(a,b)^W overline(F_(c,d)^W)]`
` = sum_(P partial matching) D_(6-|P|)(L(P))`,

and therefore

`Cov(F_(a,b)^W,F_(c,d)^W)`
` = sum_P D_(6-|P|)(L(P))`
`   - mu_(a,b)^W overline(mu_(c,d)^W)`.

The pseudo-covariance is obtained by the same formula using second-triad labels

`(c,d,-c-d)`

instead of the conjugated labels `(-c,-d,c+d)`, followed by subtraction of `mu_(a,b)^W mu_(c,d)^W`.

Every term is a `D_m` with `m<=6`, hence a finite sum of traces of products of the same explicit `N x N` matrices. The complete second-order panel calibration is therefore exact and deterministic for a frozen hard arc and frequency panel.

## 6. A predeclared panel can be whitened without a simulated CUE covariance

For a finite panel of unordered frequency pairs, compute the exact complex mean vector, Hermitian covariance, and pseudo-covariance from the formulas above. These determine the covariance of the real vector formed by stacking all real and imaginary parts.

If that real covariance is nonsingular, apply its inverse square root to obtain an exactly centered, identity-covariance finite-CUE panel. If it is singular, restrict to its support or use the corresponding pseudoinverse whitening while retaining the exact rank.

This is only a **second-order** calibration. Exact whitening does not imply that panel coordinates are independent, Gaussian, or free of higher-order CUE structure. Any combined decision statistic that uses more than its second moments still needs its own null law or a valid finite-CUE simulation under the already frozen transformation.

The useful change from `VIS-119`--`VIS-120` is narrower: mean and covariance no longer need to be guessed, imported from the full-circle trace vector, or estimated from a noisy Monte Carlo covariance matrix for this deterministic hard-window model.

## 7. Prior art and novelty assessment

The mathematical machinery is classical. Determinantal correlation functions and factorial moment measures are standard point-process tools; `VIS-120` already records this boundary through Daley--Vere-Jones and through J. Ben Hough, Manjunath Krishnapur, Yuval Peres, and Balint Virag, **Determinantal Processes and Independence**, *Probability Surveys* 3 (2006), 206--229, DOI `10.1214/154957806000000078`.

Alexander Soshnikov, **Determinantal random point fields**, *Russian Mathematical Surveys* 55:5 (2000), 923--975, DOI `10.1070/RM2000v055n05ABEH000321`, is another standard reference for determinantal point fields and their correlation-kernel formalism.

The CUE determinantal kernel and finite-rank projection description are standard random-matrix facts. The permutation-cycle trace expansion above is elementary once the determinant correlation formula is inserted. The 34-pattern covariance bookkeeping is ordinary overlap classification for two ordered distinct triples.

No DPP theorem, Toeplitz theorem, CUE correlation theorem, or general factorial-moment identity is claimed as new. The Mathia-specific delta is the exact specialization to the current `VIS-120` collision-free wrapped triad: it closes the deterministic-hard-window mean/covariance calibration gap that had prevented a source-faithful CUE comparison.

## Boundary and falsification

The explicit Toeplitz formulas above assume Haar `CUE_N`, a deterministic **hard arc**, unit weights, and the stated linear compactification. A taper changes shared-point collision factors because weights multiply; it can still be treated by the same general DPP cycle-trace method, but the simple frequency-label merge `g_u g_v=g_(u+v)` no longer holds unchanged.

A data-dependent or fixed-count selection rule is also different. If, for example, one selects the next exactly `M` eigenangles rather than all points in a deterministic arc, the simple restricted factorial-correlation integral does not automatically describe the conditioned sample. The matched null must reproduce the same conditional/Janossy/Palm selection law or be simulated under the identical rule.

The finding does not identify which effective `N`, arc length, unfolding, height window, or frequency panel is appropriate for zeta zeros. Those are part of the source dictionary and must be frozen before confirmation data are inspected.

The finding is falsified by any finite-`N` CUE configuration law for which the stated DPP factorial-density formula fails, by an error in the permutation-cycle trace expansion, by failure of the 34 partial matchings to partition the cross-equality patterns of two internally distinct triples, or by failure to recover `2(N-a-b)` in the full-circle corridor.

## Visual consequence

No canonical PNG is retained. The substantive result is an exact null-calibration mechanism, not an empirical pattern. A future heatmap or phase portrait of the collision-free panel should be centered and scaled using this **matched windowed CUE calibration** rather than the full-circle trace baseline or an independent-phase visual control.

In particular, apparent ridges caused by deterministic window leakage or covariance should be removed in the same coordinates before visual interpretation. Any residual worth retaining must still pass the predeclared panel, fresh-confirmation, and finite-height arithmetic-correction gates already recorded in the accepted multiscale clue.

## Research consequence

`VIS-119` showed that wrapping a finite source block does not justify importing the full Haar trace null. `VIS-120` removed repeated-index contamination and reduced the desired comparison to the third factorial channel. This finding resolves the next **deterministic hard-window** subproblem: once a CUE matrix size, arc, linear compactification, and finite frequency panel are fixed, the collision-free panel's finite-`N` mean and complete second-order covariance are exact finite matrix quantities.

The next separate thread is now source-side rather than null-side. Before inspecting untouched zeta confirmation material, predeclare the zeta height windows/unfolding, the corresponding effective finite-CUE rule, the frequency panel and combined statistic, then use the exact matched CUE calibration above (or the appropriate conditioned variant if fixed-count selection is chosen). Only after those choices are frozen should any zeta residual be inspected, and any departure must still be audited against known finite-height arithmetic corrections.
