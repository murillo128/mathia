# VIS-128 — a bounded tent taper gives an explicit composed Montgomery edge profile

## Claim

Let

`h(t)=(1-2|t|)_+`

be the centered unit-support tent taper, supported on `[-1/2,1/2]`, and scale it to unfolded source length `M>0` by

`h_M(x)=h(x/M)`.

Use the Fourier convention

`hat f(r)=integral_R f(x) exp(-2*pi*i*r*x) dx`

and `sinc(y)=sin(pi*y)/(pi*y)`. Then

`hat h(z)=(1/2)sinc^2(z/2)`,

`||h||_2^2=1/3`,

so the normalized source-window kernel from `VIS-125` is exactly

`Q_M^tent(r)=(3M/4)sinc^4(Mr/2)`.

It is even, nonnegative, and has unit mass. Its normalized spectral first moment is finite and explicit:

`C_tent = [integral_R |z| |hat h(z)|^2 dz]/||h||_2^2`
`       = 6 log(2)/pi^2`.

Consequently the tent-only smoothing of the infinite-CUE ramp

`K_infty(q)=min(|q|,1)`

has positive-edge deficit

`1-(Q_M^tent*K_infty)(1)`
` = [3 log(2)]/[pi^2 M] + O(M^-3)`.

Thus the tent taper removes the rectangular-window `log M/M` enhancement from `VIS-125`, but it does **not** make the source window invisible at the first `1/M` scale.

More importantly, combine this taper with Montgomery's pair weight from `VIS-124`. Write

`P_L(r)=L exp(-2L|r|)`

and suppose `M/L -> lambda` with fixed `lambda>0`. Define the fixed scaled densities

`p(s)=exp(-2|s|)`,

`q_lambda(s)=(3 lambda/4)sinc^4(lambda s/2)`.

Then

`P_L(r)=L p(Lr)`,

`Q_M^tent(r)=L q_lambda(Lr)`

when `M=lambda L`, and the exact stationary weighted+tapered null for any form factor `K` is

`P_L*Q_M^tent*K`.

At the positive infinite-CUE support edge, for every fixed real `v`,

`L[(P_L*Q_M^tent*K_infty)(1+v/L)-1] -> G_lambda(v)`,

where

`G_lambda = q_lambda * H`

and `H` is the exact Montgomery-weight edge profile from `VIS-124`:

`H(v)=v-(1/4)exp(2v)` for `v<=0`,

`H(v)=-(1/4)exp(-2v)` for `v>=0`.

In particular,

`1-(P_L*Q_M^tent*K_infty)(1)`
` = A(lambda)/L + o(1/L)`,

with

`A(lambda)`
` = 3 log(2)/(pi^2 lambda)`
`   + (1/4) integral_R exp(-2|s|) q_lambda(s) ds`.

The two universal edge effects therefore interact at leading order. The correct coefficient is **not** obtained by simply adding the separate Montgomery value `1/4` and the tent-only value `3 log(2)/(pi^2 lambda)`.

For a physical source support of fixed height `H_src` in the local zeta scaling,

`M=H_src L_T/(2*pi)`,

`L=L_T=log(T/(2*pi))`,

so

`lambda=H_src/(2*pi)`.

If a finite-CUE model has `N/L_T -> rho in (0,infinity)`, then the tent support fits inside one connected non-wrapping CUE arc whenever

`H_src < 2*pi*rho`

with asymptotic margin. This bounded-taper regime therefore avoids the growing-hard-window capacity obstruction in `VIS-127`, while leaving an explicit universal source-window correction at the same `1/L_T` scale on which a candidate arithmetic edge residual would naturally be sought.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL WINDOW/FOURIER CONTROL + DESIGN-CORRIDOR + NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

This finding does not determine the correct effective `N(T)`, the finite-`N` composed edge profile, the finite-height covariance, counting-function fluctuations beyond the smooth Riemann--von Mangoldt term, an arithmetic lower-order amplitude, or any residual in zero data.

## 1. The tent taper has a squared-sinc-squared spectral kernel

Let

`Lambda(u)=(1-|u|)_+`.

The standard triangular function satisfies

`hat Lambda(z)=sinc^2(z)`

under the stated Fourier convention. Since

`h(t)=Lambda(2t)`,

Fourier scaling gives

`hat h(z)=(1/2)sinc^2(z/2)`.

Direct integration also gives

`||h||_2^2`
` = 2 integral_0^(1/2) (1-2t)^2 dt`
` = 1/3`.

The normalized taper kernel from `VIS-125` is therefore

`Q_M^tent(r)`
` = M |hat h(Mr)|^2 / ||h||_2^2`
` = (3M/4)sinc^4(Mr/2)`.

The general autocorrelation/Fourier argument in `VIS-125` already gives nonnegativity and unit mass. Unlike the rectangular squared-sinc kernel, this kernel has `r^-4` tails at fixed `M`, so its first absolute moment is finite.

## 2. The spectral first moment is exactly `6 log(2)/pi^2`

From the formula above,

`integral_R |z| |hat h(z)|^2 dz`
` = (1/4) integral_R |z| sinc^4(z/2) dz`.

Putting `z=2u` yields

`integral_R |u| sinc^4(u) du`.

To evaluate it, write

`J=integral_0^infinity sin^4(x)/x^3 dx`.

Two integrations by parts are justified after the usual finite-endpoint truncation and passage to the limit. The boundary terms vanish because `sin^4(x)=O(x^4)` at zero and is bounded at infinity. First,

`J=2 integral_0^infinity sin^3(x)cos(x)/x^2 dx`.

Using

`sin^3(x)cos(x)=(1/4)sin(2x)-(1/8)sin(4x)`

and integrating by parts once more gives

`J=integral_0^infinity [cos(2x)-cos(4x)]/x dx`
` = log 2`,

by the classical cosine-difference/Frullani integral.

Rescaling from `x=pi u` therefore gives

`integral_R |u| sinc^4(u) du = 2 log(2)/pi^2`.

Dividing by `||h||_2^2=1/3` yields

`C_tent=6 log(2)/pi^2`.

For the scaled kernel,

`integral_R |r| Q_M^tent(r) dr = C_tent/M`.

This supplies an explicit instance of the finite-first-moment criterion in `VIS-125` rather than merely assuming a sufficiently regular taper exists.

## 3. The tent-only ramp edge has an exact first-order coefficient

At the positive edge of `K_infty`, the same decomposition used in `VIS-125` gives

`D_M^tent = 1-(Q_M^tent*K_infty)(1)`
` = integral_0^1 r Q_M^tent(r) dr`
`   + integral_1^2 (2-r) Q_M^tent(r) dr`.

Because `Q_M^tent` is even,

`integral_0^infinity r Q_M^tent(r) dr`
` = (1/2) integral_R |r| Q_M^tent(r) dr`
` = 3 log(2)/(pi^2 M)`.

For `r>=1`,

`Q_M^tent(r) <= 12/(pi^4 M^3 r^4)`.

Hence replacing the first integral's upper endpoint `1` by infinity costs `O(M^-3)`, and the second integral is also `O(M^-3)`. Therefore

`D_M^tent = 3 log(2)/(pi^2 M) + O(M^-3)`.

For a fixed physical source support `H_src`, where

`M=H_src L_T/(2*pi)`,

this becomes

`D_M^tent`
` = [6 log(2)]/[pi H_src L_T] + O((H_src L_T)^-3)`.

The key control is qualitative as well as quantitative: smoothing removes the hard-window logarithm, but for fixed `H_src` the source-window effect remains exactly on the `1/L_T` scale. A comparison against an unwindowed CUE ramp would therefore manufacture a universal same-scale residual even with this smooth taper.

## 4. Pair-weight smoothing and taper smoothing must be composed before subtraction

`VIS-124` gives

`P_L(r)=L p(Lr)`,

`p(s)=exp(-2|s|)`.

When `M=lambda L`, the tent kernel can be written

`Q_M^tent(r)=L q_lambda(Lr)`,

`q_lambda(s)=(3lambda/4)sinc^4(lambda s/2)`.

Their convolution therefore has the exact one-scale form

`(P_L*Q_M^tent)(r)=L (p*q_lambda)(Lr)`.

Now set

`g(v)=min(v,0)`.

Since the ramp is globally 1-Lipschitz,

`|L[K_infty(1+a/L)-1]| <= |a|`,

and `p*q_lambda` has finite first moment. Dominated convergence then gives

`L[(P_L*Q_M^tent*K_infty)(1+v/L)-1]`
` -> [(p*q_lambda)*g](v)`.

Associativity and `p*g=H` from `VIS-124` yield

`G_lambda(v)=q_lambda*H(v)`.

Thus the full leading universal edge shape is already forced by the two admitted smoothing mechanisms. The taper does not contribute an independent scalar correction that can simply be added after the Montgomery correction; it broadens the entire Montgomery edge profile.

At `v=0`, let independent random variables `X,Y` have densities `p` and `q_lambda`. Both are symmetric. Then

`-G_lambda(0)=(1/2) E|X+Y|`.

For the Laplace density `p(x)=exp(-2|x|)`, direct integration gives

`E[|X+y|] = |y| + (1/2)exp(-2|y|)`.

Averaging over `Y` and using

`E|Y|=C_tent/lambda=6 log(2)/(pi^2 lambda)`

gives

`A(lambda)=-G_lambda(0)`
` = 3 log(2)/(pi^2 lambda)`
`   + (1/4) E[exp(-2|Y|)]`,

which is the coefficient stated above.

Because `Y` is nondegenerate for finite `lambda`,

`0 < E[exp(-2|Y|)] < 1`.

Hence the true composed coefficient is strictly smaller than the naive sum

`3 log(2)/(pi^2 lambda) + 1/4`.

This interaction is not an arithmetic effect; it is forced by applying two universal difference-space multipliers before Fourier transformation.

## 5. The bounded taper opens a capacity-compatible single-CUE corridor

`VIS-127` showed that a source interval with unfolded length `M` can fit as one connected non-wrapping arc of `CUE_N` only if

`M<=N`.

For fixed physical support `H_src`,

`M/L_T=H_src/(2*pi)=lambda`.

If

`N/L_T -> rho`,

then

`M/N -> lambda/rho`.

Any predeclared `H_src<2*pi rho`, equivalently `lambda<rho`, therefore fits with asymptotic margin. Unlike the growing rectangular window used to suppress the `log M/M` leakage in `VIS-125`, this source support does not force `M/N` to diverge and does not by itself drive the finite-CUE edge coordinate out of the fixed-ratio regime.

This is only a compatibility corridor. The correct `rho`, the exact arc implementation, and the finite-`N` covariance still have to be derived rather than chosen to make the residual look favorable.

## Prior-art and novelty assessment

Triangular/Bartlett-type tapers, their squared-sinc Fourier transforms, and the tradeoff between compact source support and spectral leakage are classical harmonic-analysis and signal-processing material. Fredric J. Harris, **On the use of windows for harmonic analysis with the discrete Fourier transform**, *Proceedings of the IEEE* 66:1 (1978), 51--83, DOI `10.1109/PROC.1978.10837`, is a standard windowing reference already used as the prior-art boundary in `VIS-125`.

No novelty is claimed for the tent window, the Fourier transform `sinc^2`, the autocorrelation kernel, the cosine-difference integral, or the general principle that smoother source windows have faster spectral decay.

The Mathia-specific value of this finding is narrower: it instantiates the abstract taper escape left open by `VIS-125`, checks it against the single-circle capacity obstruction in `VIS-127`, and computes the exact leading support-edge control after composing the taper with Montgomery's already-fixed Laplace smoother. This converts “choose a sufficiently regular taper” into one explicit, auditable null family without claiming a new window theorem.

## Boundary and falsification

The composed profile above uses the infinite-CUE ramp as the underlying form factor. A finite `CUE_N` null must use the exact finite-`N` `K_N` from the adopted convention and evaluate

`P_L*Q_M^tent*K_N`

rather than replacing it by the limiting profile `G_lambda`.

The stationary source-window identity assumes one frozen unfolding scale. `VIS-126` controls only the smooth Riemann--von Mangoldt density linearization in an asymptotic corridor; stochastic counting fluctuations and any exact finite-height weighting remain separate.

The capacity condition uses the literal support of the tent taper. Other tapers with infinite support require a different effective-support or periodization analysis and are not covered by the simple `M<=N` criterion.

The physical width `H_src`, the effective-size ratio `rho`, and any edge coordinates used in a confirmation statistic must be fixed independently of fresh zero data. Choosing them after looking at the residual would reintroduce the representation-selection failure that this line is designed to control.

No conclusion about arithmetic structure follows from the coefficient `A(lambda)`. It is a universal null term. If a future calculation reproduces the entire candidate residual by the exact finite-`N` weighted+tapered control, the arithmetic interpretation is killed.

## Research consequence

The accepted Montgomery support-edge thread now has an explicit bounded source window that avoids the particular growing-hard-window/single-CUE incompatibility of `VIS-127`. But the same calculation closes a tempting shortcut: **a smooth taper cannot simply be declared negligible because it removes the logarithmic leakage penalty**. At fixed physical width it still changes the support edge at order `1/L_T`, and its leading effect interacts with Montgomery's pair-weight smoothing.

The next coherent question is therefore no longer which generic window class to choose. It is to fix an independently justified finite-CUE effective-size ratio and one admissible bounded taper width, then derive the exact finite-`N` composed null `P_L*Q_M^tent*K_N` together with the matching covariance/diagonal/arc conventions. Counting-function fluctuations beyond smooth density remain part of that transfer. Only after those controls are frozen should an arithmetic lower-order amplitude or fresh-zero confirmation be considered.
