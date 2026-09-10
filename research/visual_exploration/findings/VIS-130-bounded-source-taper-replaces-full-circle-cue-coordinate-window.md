# VIS-130 — a bounded source taper must replace, not compound, the full-circle CUE coordinate window

## Claim

Let

`D_N(x) = sin(pi x)/(N sin(pi x/N))`,

with the removable value `D_N(0)=1`. In mean-spacing coordinates `x=N(theta-phi)/(2*pi)`, the exact connected two-point kernel of `CUE_N` is the diagonal delta minus `D_N(x)^2`.

The all-real-time full-circle spectral form factor used in `VIS-123` is not the Fourier transform of this stationary kernel with unit weight on the real line. Because Sohail--Huang--Wei define it by integrating both eigenangles over the fixed coordinate interval `[0,2*pi]`, changing variables to the raw difference introduces the exact rectangular-overlap factor

`R_N(x) = (1-|x|/N)_+`.

Consequently, with `q=k/N`,

`S_N(Nq)/N`
` = 1 - integral_(-N)^N R_N(x) D_N(x)^2 exp(2*pi*i*q*x) dx`.

Thus the continuous noninteger-time structure of `S_N` already contains a source-coordinate window: the autocorrelation of the full-circle rectangular chart.

Now let the intended source window instead be the bounded tent from `VIS-128`,

`h_M(y)=h(y/M)`,  `h(t)=(1-2|t|)_+`,

supported on one connected CUE arc of unfolded length `M<N`, and normalize by

`integral h_M(y)^2 dy = M/3`.

Its normalized pair-overlap function is

`A_M(x)=A(|x|/M)`,

where

`A(s)=1-6s^2+6s^3` for `0<=s<=1/2`,

`A(s)=2(1-s)^3` for `1/2<=s<=1`,

and `A(s)=0` for `s>=1`.

With Montgomery's difference weight

`W_L(x)=1/(1+(pi*x/L)^2)`,

the exact connected, tent-windowed, weight-matched finite-CUE expectation under this arc convention is therefore

`C_(N,L,M)(q)`
` = 1 - integral_(-M)^M A_M(x) W_L(x) D_N(x)^2 exp(2*pi*i*q*x) dx`.

Equivalently, by evenness,

`C_(N,L,M)(q)`
` = 1 - 2 integral_0^M A_M(x) W_L(x) D_N(x)^2 cos(2*pi*q*x) dx`.

The diagonal contribution is the leading `1`; a diagonal-subtracted convention removes exactly that term.

This formula is the direct finite-`N` source-window replacement required by the accepted Montgomery support-edge clue. In contrast,

`P_L * Q_M^tent * [S_N(N·)/N]`

corresponds in difference space to multiplying by

`W_L(x) A_M(x) R_N(x)`.

It therefore **compounds the tent overlap with the full-circle rectangular overlap already built into the continuous-time `S_N`**, rather than replacing that coordinate window. The convolution is mathematically valid as an additional multiplier, but it is not the intended bounded-source CUE null unless the extra `R_N` factor is explicitly part of the source definition or is proved negligible for the statistic being used.

**Evidence/status:** `EXACT-DERIVED + LITERATURE KERNEL + WINDOW-TRANSFER CORRECTION + NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

No arithmetic residual, new CUE theorem, new pair-correlation theorem, effective-size transfer theorem, covariance formula, or implication toward RH is claimed.

## 1. Continuous real-time `S_N` contains a rectangular coordinate-overlap factor

Sohail, Huang, and Wei define the second-order CUE spectral form factor for real `k` as

`S_N(k)=integral_0^(2*pi) integral_0^(2*pi)`
`        exp(i*k*(theta-phi)) N_(2)(theta,phi) dtheta dphi`,

where their connected two-point function is

`N_(2)(theta,phi)`
` = delta(theta-phi) K_N(theta,phi)`
`   - K_N(theta,phi)K_N(phi,theta)`.

For CUE,

`K_N(theta,phi)`
` = [1/(2*pi)] sin(N(theta-phi)/2)/sin((theta-phi)/2)`

up to an irrelevant phase convention, so its squared modulus depends only on the difference.

For any function `f(theta-phi)`, the elementary square-to-difference identity is

`integral_0^(2*pi) integral_0^(2*pi) f(theta-phi) dtheta dphi`
` = integral_(-2*pi)^(2*pi) (2*pi-|delta|) f(delta) ddelta`.

Put `x=N delta/(2*pi)` and `q=k/N`. Dividing the connected statistic by `N` gives exactly

`S_N(Nq)/N`
` = 1 - integral_(-N)^N (1-|x|/N)`
`       D_N(x)^2 exp(2*pi*i*q*x) dx`.

This identity reproduces the exact all-real-time formula of Sohail--Huang--Wei after evaluating the integral. It also explains why noninteger time is sensitive to the chosen coordinate cut: `exp(i k theta)` is not a periodic function of the eigenangle when `k` is not an integer. At integer `k`, the standard periodic Fourier modes recover the familiar exact ramp/plateau values.

The factor `R_N` is therefore not an arithmetic ingredient and not an intrinsic modification of the local CUE two-point kernel. It is the overlap of two copies of the coordinate interval used in the full-circle real-time definition.

## 2. The tent source window has an exact compact cubic pair overlap

For the scaled tent `h_M(y)=h(y/M)`, define

`A_M(x)`
` = [integral_R h_M(y) h_M(y+x) dy] / [M ||h||_2^2]`.

`VIS-128` already gives `||h||_2^2=1/3` and the Fourier transform of this normalized autocorrelation,

`hat A_M(r)=Q_M^tent(r)=(3M/4)sinc^4(Mr/2)`.

The real-space form is equally explicit. By symmetry it is enough to put `s=|x|/M`. Direct integration over the overlap of the two tents gives

`integral h(t)h(t+s)dt`
` = 1/3 - 2s^2 + 2s^3`,  `0<=s<=1/2`,

and

`integral h(t)h(t+s)dt`
` = (2/3)(1-s)^3`,  `1/2<=s<=1`.

Dividing by `1/3` yields the stated `A(s)`. The two pieces agree at `s=1/2`, with value `1/4`; `A(0)=1` and `A(1)=0`.

This pair-overlap is what a source taper contributes before any Fourier transform. It is not an additional copy of the full-circle triangle `R_N`.

## 3. Direct determinantal integration gives the exact bounded-arc null

Choose one CUE coordinate chart and place the tent support inside it with unfolded length `M<N`. In unfolded coordinates the one-point density is exactly one, so normalizing the pair statistic by `M||h||_2^2=M/3` makes the diagonal term equal to one.

For distinct points, the exact scaled CUE two-point density is generated by `D_N(x)^2`. Multiplying the connected pair measure by the source overlap `A_M(x)`, Montgomery weight `W_L(x)`, and phase `exp(2*pi*i*q*x)`, then integrating the center coordinate, gives

`C_(N,L,M)(q)`
` = 1 - integral_(-M)^M A_M(x) W_L(x) D_N(x)^2`
`       exp(2*pi*i*q*x) dx`.

No large-`N`, fixed-`tau`, or stationary-sine-kernel approximation enters this identity. It is a one-dimensional exact finite-`N` quadrature once `N`, `L`, `M`, and the coordinate convention are frozen.

The formula also keeps the source taper and the circle geometry visibly separate. The periodic finite-CUE kernel remains exact at differences comparable with `N`, while `A_M` describes only which pairs the source window admits. A nonvanishing capacity margin `M/N<1` prevents the support itself from crossing the coordinate cut; any desired stronger condition against endpoint/complement interactions can now be tested directly in the same integral rather than hidden in a convolution convention.

## 4. Why convolving the full-circle real-time SFF double-counts window geometry

Fourier multiplication/convolution itself is not the problem. `VIS-124` is exact when it says that multiplying a specified difference measure by `W_L` convolves its form factor with `P_L`, and `VIS-128` is exact for a specified stationary measure when it adds the tent overlap through `Q_M^tent`.

The issue is the starting measure. The full-circle continuous-time quantity `S_N(Nq)/N` is already the transform of

`delta_0 - R_N(x)D_N(x)^2 dx`,

not of the bare stationary connected kernel

`delta_0 - D_N(x)^2 dx`.

Convolving that full-circle transform with `P_L` and `Q_M^tent` therefore gives the transform of

`delta_0 - W_L(x)A_M(x)R_N(x)D_N(x)^2 dx`.

The intended bounded-tent source statistic instead has

`delta_0 - W_L(x)A_M(x)D_N(x)^2 dx`.

These are different finite-`N` nulls. For `M/N` tending to a nonzero constant, `R_N(x)` differs from one by order one across a nonzero fraction of the admitted source-difference range, so there is no uniform small-error argument that permits the extra factor to be discarded. Whether the support-edge asymptotic happens to localize strongly enough that the difference becomes lower order is a separate derivation, not something supplied by the full-circle SFF formula.

This is precisely the kind of representation-induced false positive the visual line is meant to remove: a mathematically legitimate continuous-time CUE feature can cease to be the right null after the source window is changed.

## Prior-art and novelty assessment

The CUE determinantal kernel and its exact two-point correlation are classical. Peter Forrester and Bo-Jian Shen, **Finite size corrections in the bulk for circular beta ensembles**, *Forum of Mathematics, Sigma* 14 (2026), e105, DOI `10.1017/fms.2026.10240`, records the CUE kernel explicitly and its mean-spacing-scaled two-point form.

Sohail, Youyi Huang, and Lu Wei, **Higher-order spectral form factors of circular unitary ensemble**, *Journal of Statistical Physics* 193 (2026), article 20, DOI `10.1007/s10955-026-03572-8`, define the all-real-time second-order SFF as the double integral over `[0,2*pi]^2` used above and derive its exact closed form. Their result is the prior-art source for `VIS-123`; no novelty is claimed for it.

Triangular/Bartlett windows, autocorrelation windowing, and the `sinc^4` spectral kernel are classical harmonic-analysis and signal-processing material; `VIS-128` already anchors this prior-art boundary through Harris's standard windowing reference.

The Mathia-specific result is the control composition: writing the real-time SFF and the intended bounded source taper in the same difference coordinate shows that the full-circle rectangular overlap and the bounded tent overlap are alternative source-window geometries, not two factors that should automatically be multiplied. The cubic formula and the direct finite-`N` arc integral are elementary consequences of those standard ingredients and are stored to correct the active null construction, not as new random-matrix theory.

## Boundary and falsification

The exact formula is for the connected CUE two-point statistic normalized by the tent's `L^2` mass. A zeta-side statistic using a different centering, mean subtraction, diagonal convention, or normalization must reproduce those choices explicitly before comparison.

The result does not yet derive the covariance of several edge coordinates, the correct finite-height effective size, the effect of stochastic counting-function fluctuations, or the asymptotic support-edge profile of the bounded-tent integral. In particular, it does **not** prove that the logarithmic ripple in `VIS-123` disappears. It proves that its coefficient and `rho`-sensitivity cannot simply be imported from the full-circle `S_N` after replacing the source window.

Accordingly, the `VIS-129` `delta_rho=Theta(1/log L_T)` resolution warning remains an exact warning for the full-circle `VIS-123` edge term, but its quantitative threshold for the actual bounded-tent null is now conditional on re-deriving the `rho` dependence of `C_(N,L,M)`.

If a later derivation shows that `R_N(x)=1+o(1)` on every difference scale that contributes to the frozen support-edge statistic, then the simpler convolution may become asymptotically valid in that narrower regime. That must be proved from the exact integral, not assumed from window terminology.

## Research consequence

The accepted Montgomery support-edge clue should no longer ask for `P_L*Q_M^tent*K_N` with `K_N(q)=S_N(Nq)/N` as though that were the exact finite-`N` bounded-source null. The next coherent calculation is instead the exact arc-window integral `C_(N,L,M)` above, using the predeclared effective-size candidate and a capacity-compatible tent width.

Before any fresh zero confirmation, derive the support-edge asymptotic and joint covariance from this window-replacement null, then recompute its sensitivity to the effective-size rule. Only after that step is it meaningful to decide whether the full-circle logarithmic ripple, the `VIS-129` calibration-resolution threshold, or a smaller arithmetic residual survives the actual bounded-source representation.
