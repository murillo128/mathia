# VIS-125 — hard source windows force logarithmic support-edge leakage

## Claim

Let `nu` be a translation-invariant unfolded pair-difference measure whose normalized form factor is

`K(q)=integral_R exp(2*pi*i*q*x) dnu(x)`.

Restrict both points to a hard interval of unfolded length `M>0` and normalize by the interval length. Translation invariance inserts the exact overlap factor

`A_M(x)=(1-|x|/M)_+`.

With the normalized convention

`sinc(y)=sin(pi*y)/(pi*y)`,

one has

`hat A_M(r)=Q_M(r)=M sinc^2(Mr)`,

`Q_M(r)>=0`, and `integral_R Q_M(r)dr=1`. Therefore the hard-window form factor is exactly

`K_M = Q_M * K`.

If Montgomery's pair weight from `VIS-124` is applied at unfolded density scale `L`, then multiplication by

`W_L(x)=1/(1+(pi*x/L)^2)`

and by `A_M(x)` gives the combined stationary null

`K_M^(w) = P_L * Q_M * K`,

where `P_L(r)=L exp(-2L|r|)`. Thus a hard source window is a second, independent Fourier smoother of the support edge; it cannot be represented by the pointwise weighted full-circle null alone.

For the infinite-CUE/GUE ramp

`K_infty(q)=min(|q|,1)`,

the effect at the positive support edge is quantitatively larger than the naive `1/M` window scale:

`1-(Q_M*K_infty)(1)`
` = (log M)/(2*pi^2*M) + O(1/M)`

as `M -> infinity`.

The logarithm is the spectral-leakage cost of the rectangular cutoff. More generally, for a scaled taper `h_M(t)=h(t/M)` with normalized pair-overlap transform

`Q_(M,h)(r)= M |hat h(Mr)|^2 / ||h||_2^2`,

if

`C_h = [integral_R |z| |hat h(z)|^2 dz]/||h||_2^2 < infinity`,

then the 1-Lipschitz ramp satisfies the uniform bound

`|(Q_(M,h)*K_infty)(q)-K_infty(q)| <= C_h/M`.

Hence the logarithmic enhancement is not an unavoidable finite-window phenomenon: it is caused by the slow `sinc^2` spectral tail of the hard rectangular window. A sufficiently regular taper with finite spectral first moment removes that logarithmic loss.

For a local zero window of physical height `H` at density scale

`L=L_T=log(T/(2*pi))`,

its stationary unfolded length is

`M=H L_T/(2*pi)`.

Under this local-stationary idealization the hard-window edge deficit is therefore

`(log M)/(pi*H*L_T) + O(1/(H*L_T))`.

A fixed-height hard window is **not neutral at a proposed `1/L_T` arithmetic residual scale**: after multiplication by `L_T`, its universal edge leakage grows like `log M/(pi H)`. To make this hard-window contribution `o(1/L_T)`, one needs at least

`H/log M -> infinity`

within a regime where the local-stationary approximation itself remains valid, or one must replace the rectangular cutoff by a taper whose spectral first moment is finite.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL WINDOW/FOURIER CONTROL + ASYMPTOTIC NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

This finding does not transfer the full nonstationary finite-height zeta statistic to finite CUE, choose the effective matrix size `N(T)`, determine the covariance of the eventual residual statistic, inspect fresh zero data, or establish an arithmetic support-edge term.

## 1. A hard interval inserts triangular pair overlap

Consider a stationary pair intensity in unfolded coordinates and restrict both coordinates `u,v` to an interval `I` of length `M`. For a fixed difference `x=u-v`, the set of admissible translates has length

`|I intersect (I+x)| = (M-|x|)_+`.

After the same division by `M` used to obtain a per-unit-length pair statistic, the difference measure is multiplied by

`A_M(x)=(1-|x|/M)_+`.

This is purely source-window geometry. It occurs before any arithmetic interpretation and is independent of the detailed pair process as long as the null is translation invariant at the scale being modeled.

The Fourier transform of a triangular overlap is the squared transform of the underlying rectangle. With the convention

`hat f(r)=integral_R f(x) exp(-2*pi*i*r*x) dx`,

one obtains

`Q_M(r)=hat A_M(r)=M sinc^2(Mr)`.

Since `A_M(0)=1`, Fourier inversion gives

`integral_R Q_M(r)dr=1`.

For any pair form factor `K`, multiplication of the difference measure by `A_M` therefore becomes convolution:

`K_M(q)=(Q_M*K)(q)`.

This is the continuous Fejer/squared-sinc form of ordinary rectangular-window spectral leakage. No zeta or random-matrix input is required for the identity.

## 2. The window and Montgomery weight compose as two exact smoothers

`VIS-124` showed that Montgomery's difference weight has Fourier kernel

`P_L(r)=L exp(-2L|r|)`

and that weighting a stationary pair measure sends `K` to `P_L*K`.

Applying the hard source window as well multiplies the same difference measure by `W_L(x)A_M(x)`. The Fourier transform of that product is the convolution `P_L*Q_M`, so

`K_M^(w)=(P_L*Q_M*K)`.

The two effects are conceptually distinct. `P_L` is fixed by Montgomery's classical pair weight and has exponential Fourier tails. `Q_M` is fixed by the source-window geometry and has the much slower squared-sinc tail. Subtracting the exact weighted full-circle CUE curve but omitting `Q_M` therefore leaves a deterministic window residual.

The diagonal convention remains visible but is not altered by either multiplier at difference zero: `W_L(0)=A_M(0)=1`. If the source statistic subtracts the diagonal, the null must subtract it by the same convention.

## 3. Rectangular leakage is logarithmically enhanced exactly at the ramp edge

At the positive support edge of

`K_infty(q)=min(|q|,1)`,

the deficit after hard-window smoothing is

`D_M = 1-(Q_M*K_infty)(1)`.

Because `Q_M` is even and has unit mass, only shifts for which `|1-r|<1` contribute to the deficit. Hence exactly

`D_M`
` = integral_0^1 r Q_M(r) dr`
`   + integral_1^2 (2-r) Q_M(r) dr`.

For the first integral substitute `y=Mr`:

`integral_0^1 r Q_M(r)dr`
` = (1/(pi^2*M)) integral_0^M [sin^2(pi*y)/y] dy`.

Since

`sin^2(pi*y)=(1-cos(2*pi*y))/2`,

the standard oscillatory-integral estimate gives

`integral_0^M sin^2(pi*y)/y dy = (1/2)log M + O(1)`.

Therefore

`integral_0^1 r Q_M(r)dr = (log M)/(2*pi^2*M)+O(1/M)`.

On `1<=r<=2`, the factor `r` is bounded away from zero and

`Q_M(r) <= 1/(pi^2*M*r^2)`,

so the second integral is `O(1/M)`. Combining the two terms proves

`D_M=(log M)/(2*pi^2*M)+O(1/M)`.

The logarithm comes from integrating the first moment of the `1/(M r^2)` squared-sinc tail over the scale range `1/M << r << 1`. It is therefore exactly the kind of window artifact that a visually sharpened support edge could mistake for a lower-order source correction.

## 4. Smooth tapers remove the logarithmic first-moment divergence

Let `h` be a square-integrable taper and scale it by `h_M(t)=h(t/M)`. Normalize its autocorrelation so that the pair-overlap multiplier equals one at zero difference. Wiener-Khinchin then gives the unit-mass Fourier kernel

`Q_(M,h)(r)=M |hat h(Mr)|^2/||h||_2^2`.

For any 1-Lipschitz function `K`,

`|(Q_(M,h)*K)(q)-K(q)|`
` <= integral_R Q_(M,h)(r)|r|dr`
` = C_h/M`,

provided the spectral first moment `C_h` is finite.

The infinite-CUE ramp is 1-Lipschitz, so the same bound holds at and around its support edge. Rectangular `h` has `|hat h(z)|^2` proportional to `sinc^2(z)`, whose weighted first moment diverges logarithmically; that is precisely why the hard-window calculation acquires `log M/M`. A taper with faster spectral decay turns the universal window error back into `O(1/M)`.

This does not prove that any particular taper is optimal for the eventual zeta statistic. It gives a falsifiable design criterion: the chosen source window should have a controlled spectral first moment at the scale on which an arithmetic residual is to be tested.

## 5. Consequence for local finite-height support-edge tests

For a local height window of width `H`, freezing the mean zero density at its central scale gives unfolded length

`M=H L_T/(2*pi)`.

Substituting this into the hard-window asymptotic yields

`D_M = [log M]/[pi H L_T] + O(1/(H L_T))`.

Thus a fixed physical-height rectangular window has a universal support-edge error larger than a constant multiple of `1/L_T` by the slowly growing factor `log M/H`. A candidate arithmetic profile expected at `1/L_T` cannot be tested against a pointwise/full-circle null under that window without first removing this contribution.

There are two clean escapes. One may let `H` grow so that `H/log M -> infinity`, subject to separately controlling density variation across the expanding source window. Or one may use a predeclared smooth taper with finite `C_h`, for which the stationary window error is `O(1/(H L_T))`; then fixed `H` can at least avoid the logarithmic enhancement, though nonstationarity, effective-size matching, and covariance remain separate gates.

This finding intentionally stops there. Choosing the actual taper, deriving the nonstationary source-to-CUE transfer, and freezing the final covariance-aware statistic are the next mathematical question rather than extensions of the same result.

## Prior-art and novelty assessment

Triangular overlap from a rectangular observation window, the squared-sinc/Fejer spectral kernel, and the general tradeoff between window sharpness and spectral leakage are classical Fourier-analysis and signal-processing facts. F. J. Harris, **On the use of windows for harmonic analysis with the discrete Fourier transform**, *Proceedings of the IEEE* 66:1 (1978), 51-83, DOI `10.1109/PROC.1978.10837`, is a standard windowing reference. No novelty is claimed for those ingredients or for Wiener-Khinchin.

`VIS-123` and `VIS-124` already anchor the Montgomery/CUE-specific phase, finite-size, and pair-weight controls. The Mathia-specific content here is the exact transfer of ordinary source-window geometry into that support-edge null and the resulting quantitative warning: a rectangular local window produces a universal `(log M)/M` edge deficit, while finite-first-moment tapers reduce the generic ramp error to `O(1/M)`.

No external source is claimed to omit this elementary consequence, and no new harmonic-analysis theorem is asserted. The result is persisted because it closes another calibration ambiguity in the accepted Montgomery support-edge clue.

## Boundary and falsification

The exact triangular-overlap identity assumes a translation-invariant pair-difference null with one fixed unfolding scale. Actual Riemann zeros over a finite height range have slowly varying density, and a finite-CUE model has its own circular/arc geometry. Those effects are deliberately **not** collapsed into this stationary calculation.

The formula `M=H L_T/(2*pi)` is therefore a local-stationary dictionary, not an assertion that Montgomery's original global `0<gamma<=T` statistic is literally a rectangular stationary sample. A later finite-height null must integrate the varying density/window convention or reproduce it in a matched ensemble.

The asymptotic at `q=1` uses the infinite-CUE ramp. At finite `N`, the exact real-time correction from `VIS-123` must be convolved with both `P_L` and the chosen window kernel rather than added independently by analogy. Cross-terms are automatically included by evaluating the full convolution.

The smooth-taper bound is an upper bound from Lipschitz continuity. It does not determine the exact signed finite-CUE edge profile, the correct source covariance, or the scale of an arithmetic remainder after all null components are removed.

No zero data, confirmation window, or residual amplitude normalization was selected or inspected in deriving this finding.

## Research consequence

The accepted Montgomery support-edge clue now has three non-arithmetic calibration layers: phase/continuous finite-CUE centering (`VIS-123`), Montgomery-weight convolution (`VIS-124`), and source-window spectral leakage (`VIS-125`).

Before any fresh zero confirmation test, freeze a source window whose spectral leakage is demonstrably below the intended residual scale. A hard local window requires a growing-height condition such as `H/log(H L_T) -> infinity` for an `o(1/L_T)` window error; a sufficiently regular taper can remove the logarithmic penalty but still needs an exact nonstationary/effective-`N` transfer.

The remaining live step is therefore narrower: after fixing such a window/taper, derive the density variation, finite-CUE effective-size dictionary, diagonal normalization, and joint covariance in the same representation. Only then can an arithmetic lower-order formula choose the post-null amplitude scale and only after that may fresh high-zero material be inspected.