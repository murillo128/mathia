# VIS-135 — bounded CUE cumulants force a Gaussian terminal tent packet and a nonzero intensity-noise floor

## Claim

Continue the bounded-source CUE construction of `VIS-130`--`VIS-134`. Let `P_N` be the rank-`N` CUE projection kernel on the unit circle and, with the notation of `VIS-133`, write

`Z_(N,v)=sum_j a_(alpha_N)(theta_j) exp(i t_(N,v) theta_j)`,

where `alpha_N=M/N -> alpha in (0,1)`, `t_(N,v)=N+rho_N v`, `rho_N=N/L -> rho>0`, and the tent satisfies `0<=a_(alpha_N)<=1` on a fixed non-wrapping chart. Put

`X_(N,v)=[Z_(N,v)-E Z_(N,v)]/sqrt(H_2)`,  `H_2=M/3=Theta(N)`.

For every fixed cumulant order `p>=3`, every fixed finite set of scaled edge coordinates, and every mixed choice of `X_(N,v)` and its complex conjugate, the joint cumulant is

`O(N^(1-p/2))`.

In particular,

`cum(X_(N,v), overline{X_(N,v)}, X_(N,w), overline{X_(N,w)}) = O(N^-1)`

uniformly for fixed `v,w`. Combined with `VIS-133` and `VIS-134`, whose second-order limits are

`E[X_(N,v) overline{X_(N,w)}] -> R_(alpha,rho)(v-w)`

and

`E[X_(N,v) X_(N,w)] -> 0`,

the terminal bounded-tent amplitude packet has finite-dimensional limits given by a centered proper complex Gaussian field with covariance kernel `R_(alpha,rho)`.

Consequently the connected fourth cumulant cannot cancel the Wick term isolated in `VIS-134`. For

`I_N(v)=|X_(N,v)|^2-E|X_(N,v)|^2`,

one has

`Cov(I_N(v),I_N(w)) -> |R_(alpha,rho)(v-w)|^2`.

After the fixed Montgomery/Laplace smoothing

`J_N(v)=integral_R exp(-2|u|) I_N(v+u) du`,

one likewise has

`Cov(J_N(v),J_N(w)) -> G_(alpha,rho)(v-w)`,

where `G_(alpha,rho)` is the strictly positive-definite smoothed Wick kernel already defined in `VIS-134`.

Thus every nonzero fixed finite contrast of the smoothed support-edge field retains a strictly positive asymptotic CUE variance. Samplewise diagonal subtraction, zero-sum coordinate projection, the bounded source taper, and the fixed Montgomery smoothing do **not** make a single matched CUE source window self-average.

**Evidence/status:** `LITERATURE+DERIVED + ASYMPTOTIC GAUSSIAN SPECIALIZATION + DECISIVE NEGATIVE STOCHASTIC CONTROL + NO-NOVELTY-CLAIM`.

This closes the specific fourth-cumulant cancellation loophole left open by `VIS-134`. It does not establish a zeta-to-CUE transfer theorem, independence of distinct height windows, an arithmetic support-edge residual, or any implication toward RH.

## 1. Rank-`N` projection DPPs give an `O(N)` fixed-order cumulant bound

The CUE eigenangles form a determinantal point process whose correlation operator `P_N` is an orthogonal projection of rank `N`. For a bounded test function `f`, write

`L_f=sum_j f(theta_j)`.

The standard determinantal cumulant expansion expresses each fixed-order cumulant `kappa_p(L_f)` as a finite linear combination, depending only on `p`, of traces of the form

`Tr(M_(f^p1) P_N M_(f^p2) P_N ... M_(f^pm) P_N)`,

where `p_1+...+p_m=p` and `M_g` denotes multiplication by `g`.

Every such term has the elementary trace-norm bound

`|Tr(M_(f^p1) P_N ... M_(f^pm) P_N)| <= N ||f||_infinity^p`.

Indeed one projection may be taken in trace norm, `||P_N||_1=N`, while every remaining projection has operator norm one and every multiplication operator contributes its sup norm. Since only finitely many compositions occur at fixed `p`, there is a constant `C_p`, independent of `N` and of the oscillation frequency of `f`, such that

`|kappa_p(L_f)| <= C_p N ||f||_infinity^p`.

The mixed version follows either from the corresponding mixed determinantal expansion or by polarization of the homogeneous polynomial `f -> kappa_p(L_f)`. Hence for any fixed bounded family `f_1,...,f_p`,

`|kappa(L_(f_1),...,L_(f_p))| = O_p(N)`.

The important point for the present thread is that this estimate is **frequency-blind**. It does not require the high powers in the Fourier expansion to be separated by at least `N`, so the failure of the simple Soshnikov--Wu separated-high-trace vanishing criterion noted in `VIS-134` is not an obstruction to controlling the whole bounded tent statistic.

## 2. The terminal tent normalization kills every higher joint cumulant

For each scaled edge coordinate `v`, the CUE test function is

`f_(N,v)(theta)=a_(alpha_N)(theta) exp(i t_(N,v) theta)`.

It satisfies `||f_(N,v)||_infinity<=1` uniformly in `N` and `v`. Complex conjugation merely replaces the test function by its conjugate, which has the same bound. Cumulants of order at least two are unchanged by subtracting deterministic means, so for every fixed `p>=3`,

`kappa(X_(N,v_1)^(epsilon_1),...,X_(N,v_p)^(epsilon_p))`
` = O(N) / H_2^(p/2)`
` = O(N^(1-p/2))`,

where each `epsilon_j` denotes either the variable or its complex conjugate.

Thus all fixed higher joint cumulants vanish. At order two, `VIS-133` gives the nondegenerate conjugate covariance kernel `R_(alpha,rho)`, while `VIS-134` gives vanishing pseudocovariance. For any fixed real linear combination of real and imaginary parts of finitely many edge amplitudes, the higher cumulants therefore vanish and the variance converges. The moment-cumulant relations, tightness from the bounded second moments, and Gaussian moment determinacy give the finite-dimensional proper-complex-Gaussian limit.

This is stronger than merely bounding the one fourth cumulant required by `VIS-134`: the whole fixed-dimensional terminal packet is asymptotically Gaussian under the bounded-tent normalization.

## 3. The connected fourth cumulant is too small to cancel the Wick kernel

For the fourth-order combination relevant to the intensity covariance, Section 2 gives

`Kappa_N(v,w)`
` = cum(X_(N,v),overline{X_(N,v)},X_(N,w),overline{X_(N,w)})`
` = O(N^-1)`.

`VIS-134` proved the exact identity

`Cov(I_N(v),I_N(w))`
` = |C_N(v,w)|^2 + |P_N(v,w)|^2 + Kappa_N(v,w)`,

with `C_N(v,w)->R_(alpha,rho)(v-w)` and `P_N(v,w)->0`. Therefore

`Cov(I_N(v),I_N(w)) -> W_(alpha,rho)(v-w)`

with

`W_(alpha,rho)(d)=|R_(alpha,rho)(d)|^2`.

The possible order-one negative connected term left open in `VIS-134` cannot occur: the bounded-projection cumulant estimate forces it to zero at least as `O(1/N)` after the natural `sqrt(H_2)` normalization.

Since `VIS-134` already proves that `W_(alpha,rho)` is strictly positive definite on every finite set of distinct coordinates, every nonzero fixed finite intensity contrast has a positive limiting variance.

## 4. Fixed Montgomery smoothing preserves the full variance floor

The same cumulant estimate is uniform in the scaled coordinate because changing `v` changes only the unit-modulus oscillatory factor in `f_(N,v)`. Hence

`sup_(v,w) |Kappa_N(v,w)| = O(N^-1)`

within the fixed-ratio, non-wrapping tent family.

With `K(u)=exp(-2|u|)` and `integral K=1`, the connected fourth-order contribution to the smoothed covariance is therefore bounded by

`integral integral K(u)K(s) |Kappa_N(v+u,w+s)| du ds = O(N^-1)`.

For the second-order Wick terms, the normalized amplitude covariance is uniformly bounded by the same rank-`N` second-cumulant estimate. Together with the fixed-coordinate limits from `VIS-133`--`VIS-134`, dominated convergence propagates the covariance through the integrable Laplace kernel. Thus

`Cov(J_N(v),J_N(w)) -> G_(alpha,rho)(v-w)`.

`VIS-134` proves that `G_(alpha,rho)` is strictly positive definite. Therefore a predeclared nonzero finite contrast `sum_i c_i J_N(v_i)` has

`lim Var(sum_i c_i J_N(v_i))`
` = sum_(i,j) c_i overline(c_j) G_(alpha,rho)(v_i-v_j) > 0`.

The support-edge statistic has an order-one stochastic floor per matched CUE source window even after the exact common-mode and smoothing controls.

## 5. Immediate measurement consequence

The active clue targets a candidate arithmetic mean displacement of order `1/L`. If `m` matched source windows were genuinely independent and each carried a fixed nonzero contrast with limiting variance `sigma_c^2>0`, averaging the windows would give standard deviation asymptotic to `sigma_c/sqrt(m)`.

Thus fixed signal-to-noise against an `a/L` mean displacement requires `m=Theta(L^2)` independent effective windows, while making the stochastic error `o(1/L)` requires `m/L^2 -> infinity`. This is only an **independence-model corollary**, not a claim that zeta height windows supply that many independent samples. Correlation between windows can only be assessed after an explicit source-window dependence model or theorem is fixed.

The next live gate is therefore no longer the single-window CUE fourth cumulant. It is whether the zeta/CUE transfer, finite-height unfolding/counting errors, and dependence between admissible source windows permit an effective averaging budget capable of resolving the proposed arithmetic scale.

## Prior-art and novelty assessment

Alexander Soshnikov, **Gaussian Limit for Determinantal Random Point Fields**, *The Annals of Probability* 30:1 (2002), 171--187, DOI `10.1214/aop/1020107764`, develops the determinantal cumulant method and Gaussian limits for linear statistics. Alexander Soshnikov and Chutong Wu, **A Note on Cumulant Technique in Random Matrix Theory**, *Entropy* 25:5 (2023), 725, DOI `10.3390/e25050725`, reviews the determinantal cumulant formula and studies high-trace cumulants of Haar unitary matrices. Diaconis--Evans trace-moment/covariance machinery remains the second-order source already used in `VIS-132`--`VIS-133`.

Accordingly, neither the `O(N)` bounded-linear-statistic cumulant estimate nor the resulting Gaussian mechanism is claimed as a new random-matrix theorem. The Mathia-specific contribution is the specialization to the exact terminal-frequency bounded-tent triangular array fixed by `VIS-130`--`VIS-134`: it shows that the unresolved connected fourth cumulant is automatically lower order despite nearby `N+O(1)` Fourier modes, closes the only remaining CUE-side cancellation loophole in the frozen support-edge null, and transfers that conclusion through the fixed Montgomery/Laplace smoothing.

A literature search found the general determinantal cumulant/CLT machinery and modern high-trace formulations above; no novelty is claimed for the general probabilistic ingredients.

## Boundary and falsification

The argument uses a bounded source taper and `H_2=Theta(N)` with `alpha_N->alpha in (0,1)`. If the taper amplitude grows with `N`, the source fraction degenerates, the normalization is subextensive, or a different observable is not a bounded linear statistic before squaring, the rank-`N` cumulant estimate may no longer imply vanishing normalized higher cumulants at the stated rate.

The Gaussian statement is finite-dimensional for fixed scaled coordinates. A coordinate family whose size grows with `N`, a shrinking feature scale, or a process-level functional limit requires additional uniform control. The smoothed covariance statement uses the fixed integrable Laplace kernel of `VIS-133`; an `N`-dependent smoothing bandwidth requires a fresh argument.

Most importantly, this is a **matched finite-CUE null** result. It does not prove that high zeta zeros obey this finite-CUE law at the `1/L` lower-order scale, that separated height windows are independent, or that an arithmetic residual exists. The result instead raises the evidentiary bar: any claimed support-edge residual must beat a null with a rigorously non-self-averaging single-window quadratic fluctuation and must supply its own transfer and effective-sample-size control.

## Research consequence

The support-edge fourth-order null is now closed. `VIS-131` fixes the bounded-tent mean, `VIS-132` removes the realized diagonal common mode, `VIS-133` fixes the terminal amplitude covariance, `VIS-134` isolates the only possible Wick-cancelling connected term, and this finding forces that connected term to vanish after normalization.

The next coherent investigation should leave the CUE fourth cumulant behind and quantify **effective source-window averaging plus finite-height zeta-to-CUE transfer at the target `1/L` scale**. Only if that gate is favorable should an arithmetic lower-order amplitude and untouched zeta confirmation be brought into the test.