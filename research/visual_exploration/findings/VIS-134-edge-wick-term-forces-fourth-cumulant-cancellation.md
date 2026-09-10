# VIS-134 — the bounded-tent edge Wick term forces a fourth-cumulant cancellation

## Claim

Continue the bounded-source CUE construction of `VIS-130`--`VIS-133`. Use the centered normalized edge amplitudes

`X_(N,v) = [Z_(N,v)-E Z_(N,v)] / sqrt(H_2)`

from `VIS-133`, with `N/L -> rho>0`, `M/N -> alpha in (0,1)`, and fixed non-wrapping source margin. Write

`C_N(v,w)=E[X_(N,v) overline{X_(N,w)}]`

and

`P_N(v,w)=E[X_(N,v) X_(N,w)]`.

Then for every fixed `v,w`,

`C_N(v,w) -> R_(alpha,rho)(v-w)`

as in `VIS-133`, while

`P_N(v,w)=O(N^-2)`.

For the centered intensity field

`I_N(v)=|X_(N,v)|^2-E|X_(N,v)|^2`,

define the connected fourth cumulant

`Kappa_N(v,w)=cum(X_(N,v), overline{X_(N,v)}, X_(N,w), overline{X_(N,w)})`.

The exact moment-cumulant identity gives

`Cov(I_N(v),I_N(w))`
` = |C_N(v,w)|^2 + |P_N(v,w)|^2 + Kappa_N(v,w)`

and therefore

`Cov(I_N(v),I_N(w))`
` = |R_(alpha,rho)(v-w)|^2 + Kappa_N(v,w) + o(1)`.

The kernel

`W_(alpha,rho)(d)=|R_(alpha,rho)(d)|^2`

is strictly positive definite on every finite set of distinct edge coordinates. Thus no nonzero finite linear contrast — including a zero-sum contrast that exactly removes the realized diagonal common mode of `VIS-132` — can remove the order-one **Wick contribution**. Any asymptotic self-averaging of the full projected intensity contrast requires a compensating order-one connected fourth cumulant.

The same remains true after the Montgomery/Laplace smoothing from `VIS-133`. With

`K(u)=exp(-2|u|)`, `integral_R K(u) du = 1`

and

`J_N(v)=integral_R K(u) I_N(v+u) du`,

the Wick part of the limiting covariance is

`G_(alpha,rho)(d)`
` = integral_R integral_R K(u)K(s) W_(alpha,rho)(d+u-s) du ds`.

`G_(alpha,rho)` is again strictly positive definite. Hence the fixed-width Montgomery smoothing does not remove the Wick contribution either.

**Evidence/status:** `EXACT-DERIVED + MOMENT-CUMULANT REDUCTION + NECESSARY FOURTH-CUMULANT CANCELLATION + NEGATIVE STOCHASTIC CONTROL + NO-NOVELTY-CLAIM`.

This finding does **not** prove that the complete projected pair statistic has an order-one variance floor. The connected fourth cumulant may in principle cancel the positive Wick term. The next unresolved mathematical object is precisely whether that cancellation occurs for the terminal-frequency bounded-tent CUE packet.

## 1. The edge pseudocovariance vanishes

Use the fixed-ratio tent notation of `VIS-133`,

`a_alpha(theta)=(1-|theta|/(pi alpha))_+`

with Fourier coefficient

`b_alpha(xi)=(1/(2 pi)) integral a_alpha(theta) exp(-i xi theta) dtheta`.

The explicit triangular transform gives the uniform decay

`b_alpha(xi)=O((1+|xi|)^-2)`.

For

`t_(N,v)=N+rho_N v`, `rho_N=N/L`,

the CUE linear-statistic covariance formula applied without complex conjugating the second statistic gives

`Cov(Z_(N,v), Z_(N,w))`
` = sum_(k in Z, k!=0) min(N,|k|)`
`     b_alpha(k-t_(N,v)) b_alpha(-k-t_(N,w))`

up to the convergent `alpha_N=M/N -> alpha` parameter perturbation.

The two coefficient packets are centered near `+N` and `-N`. Their separation is `2N+O(1)`. The convolution bound for two `(1+|x|)^-2` tails gives

`sum_k |b_alpha(k-t_(N,v)) b_alpha(-k-t_(N,w))| = O(N^-2)`.

Since `min(N,|k|)<=N`,

`Cov(Z_(N,v),Z_(N,w))=O(N^-1)`.

Because `H_2=M/3=Theta(N)`,

`P_N(v,w)=H_2^-1 Cov(Z_(N,v),Z_(N,w))=O(N^-2)`.

Thus the limiting edge field is asymptotically circular at second order even though its conjugate covariance remains the nontrivial kernel `R_(alpha,rho)`.

## 2. Intensity covariance separates into Wick and connected parts

For arbitrary centered complex random variables `A,B`, the fourth moment decomposes exactly as

`E[A overline A B overline B]`
` = E[A overline A] E[B overline B]`
`   + E[A overline B] E[overline A B]`
`   + E[A B] E[overline A overline B]`
`   + cum(A,overline A,B,overline B)`.

Subtracting the product of the two intensity means and taking `A=X_(N,v)`, `B=X_(N,w)` yields

`Cov(I_N(v),I_N(w))`
` = |C_N(v,w)|^2 + |P_N(v,w)|^2 + Kappa_N(v,w)`.

`VIS-133` supplies `C_N(v,w)->R_(alpha,rho)(v-w)`, while Section 1 gives `P_N(v,w)->0`. Hence only one genuinely new stochastic term remains:

`Cov(I_N(v),I_N(w))`
` = W_(alpha,rho)(v-w) + Kappa_N(v,w) + o(1)`.

A Gaussian/Wick replacement would set the connected fourth cumulant to zero and would therefore predict the nonvanishing covariance kernel `W`. Such a replacement is **not assumed here**.

In particular, because `R_(alpha,rho)(0)=1`,

`Var(I_N(v)) = 1 + Kappa_N(v,v) + o(1)`.

Therefore `Var(I_N(v))->0` is possible only if

`Kappa_N(v,v)->-1`.

More generally, for a fixed coefficient vector `c` on distinct coordinates `v_1,...,v_r`,

`Var(sum_i c_i I_N(v_i))`
` = sum_(i,j) c_i overline(c_j) W_(alpha,rho)(v_i-v_j)`
`   + sum_(i,j) c_i overline(c_j) Kappa_N(v_i,v_j)`
`   + o(1)`.

If the variance of such a nonzero contrast tends to zero, the connected fourth-cumulant quadratic form must asymptotically cancel the full positive Wick quadratic form.

## 3. The Wick kernel is strictly positive definite

`VIS-133` writes `R` as the Fourier transform of the nonnegative tent-square density. Explicitly,

`R_(alpha,rho)(d)`
` = (3/(2 pi alpha)) integral_(-pi alpha)^(pi alpha)`
`     a_alpha(theta)^2 exp(i rho d theta) dtheta`.

After the change of variable `lambda=rho theta`, this is the characteristic/Fourier transform of a positive density supported on an interval and positive in its interior.

Therefore

`W(d)=|R(d)|^2`

is the Fourier transform of the convolution of that density with its reflection. The resulting spectral density is positive on an interval around zero.

For distinct `v_1,...,v_r` and nonzero coefficients `c_i`,

`sum_(i,j) c_i overline(c_j) W(v_i-v_j)`

is the integral of

`|sum_i c_i exp(i lambda v_i)|^2`

against that positive spectral density. A nonzero finite exponential polynomial cannot vanish on an interval, so the integral is strictly positive.

This includes every nonzero zero-sum coefficient vector. Consequently the coordinate contrast used to eliminate the `VIS-132` realized diagonal common mode does not eliminate the Wick contribution generated by the correlated terminal edge amplitudes.

## 4. Fixed Montgomery smoothing preserves the same obstruction

`VIS-133` shows that the Montgomery weight converts the support-edge pair statistic into a fixed scaled Laplace average with

`K(u)=exp(-2|u|)`.

For the centered intensity field, the Wick contribution to

`Cov(J_N(v),J_N(w))`

converges formally by the integrable kernel and the bounded second-order edge covariance to

`G(d)=integral integral K(u)K(s) W(d+u-s) du ds`.

Equivalently, in Fourier space the spectral measure of `G` is the spectral measure of `W` multiplied by

`|hat K(lambda)|^2`.

With the ordinary Fourier convention,

`hat K(lambda)=4/(4+lambda^2)`,

which is strictly positive for every real `lambda`. Since the spectral density of `W` is positive on an interval, the spectral density of `G` is also positive there. The same exponential-polynomial argument proves strict positive definiteness of `G`.

Thus a fixed Laplace smoothing window cannot create self-averaging by projecting away the Wick kernel. For any nonzero finite contrast of the smoothed field, including zero-sum contrasts, a vanishing asymptotic variance would again require the smoothed connected fourth cumulant to cancel a strictly positive order-one Wick quadratic form.

## Prior-art and novelty assessment

The CUE trace covariance used in `VIS-133` and Section 1 is classical; Diaconis and Evans, **Linear functionals of eigenvalues of random matrices**, *Transactions of the American Mathematical Society* 353:7 (2001), 2615--2633, is the existing source anchor used by the preceding findings.

The moment-cumulant decomposition above is standard probability. Soshnikov and Wu, **A Note on Cumulant Technique in Random Matrix Theory**, *Entropy* 25:5 (2023), 725, DOI `10.3390/e25050725`, explicitly develop joint cumulants of high traces of Haar unitary matrices and use them for pair-counting fluctuations. Their high-trace results make the connected fourth cumulant the natural next object here, but they do not justify deleting it in the present packet.

In particular, their simple cumulant-vanishing criterion for several distinct high powers requires every admitted nonzero integer combination of those powers to have magnitude at least `N`. The terminal packet relevant here contains nearby powers `N+n`; taking the difference of two neighboring packet frequencies gives `O(1)`, so that sufficient separation condition fails. Therefore the Gaussian/Wick shortcut is not licensed by that result.

The strict-positive-definiteness arguments for Fourier transforms of positive interval-supported densities and the Laplace smoothing identity are elementary harmonic analysis. The contribution of this finding is only the exact control reduction for Mathia's frozen bounded-tent support-edge construction: common-mode projection and fixed Montgomery smoothing cannot remove the positive Wick part; any self-averaging must come from a specific connected fourth-order cancellation. No new general random-matrix theorem is claimed.

## Boundary and falsification

The result inherits the fixed-ratio, fixed-coordinate, non-wrapping assumptions of `VIS-133`. If `alpha`, `rho`, the taper, the coordinate family, or the smoothing scale varies with `N`, the covariance and positivity arguments must be redone in that regime.

Strict positivity of the Wick kernel is **not** strict positivity of the full covariance kernel. Connected fourth cumulants can be negative and can cancel Wick contractions. This finding therefore does not establish a stochastic floor for the complete CUE pair statistic, a Gaussian limit, independence or dependence of separated zeta height windows, or a required number of confirmation windows.

The `P_N=O(N^-2)` estimate uses the fixed tent's quadratic Fourier decay and the `2N+O(1)` separation of positive and negative terminal packets. A different taper with materially slower Fourier decay needs its own pseudocovariance estimate.

No fresh Riemann-zero confirmation data are used. Nothing here establishes an arithmetic lower-order residual, Montgomery's full pair-correlation conjecture, a zeta-to-CUE transfer theorem, or an implication toward RH.

## Research consequence

The support-edge covariance gate is now narrower than in `VIS-133`. The second-order amplitude kernel is known, the anomalous pseudocovariance vanishes, and both zero-sum common-mode projection and fixed Montgomery smoothing leave a strictly positive Wick covariance contribution.

The next coherent mathematical target is therefore the connected fourth-cumulant kernel of the **terminal-frequency bounded-tent CUE packet**, propagated through the fixed Laplace average. One must determine whether it cancels the Wick kernel, partially cancels it, or leaves a positive residual quadratic form. This should be attacked with the exact high-trace cumulant/determinantal machinery rather than assuming a Gaussian field.

Only after that fourth-order CUE question and the finite-height zeta-to-CUE transfer uncertainty are controlled does it make sense to freeze an independent-window averaging budget or inspect untouched zeta confirmation data.
