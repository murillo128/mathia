# VIS-124 — Montgomery's pair weight is an exact Laplace smoother of the CUE support edge

## Claim

Let

`L > 0`

and write an unfolded pair difference as

`x = L Delta/(2*pi)`.

Montgomery's classical pair weight

`w(Delta)=4/(4+Delta^2)`

then becomes

`W_L(x)=w(2*pi*x/L)=1/(1+(pi*x/L)^2)`.

With Fourier convention

`hat f(r)=integral_R f(x) exp(-2*pi*i*r*x) dx`,

one has the exact transform

`hat W_L(r)=P_L(r)=L exp(-2 L |r|)`

and

`integral_R P_L(r) dr = 1`.

Thus the pair weight is a unit-mass Laplace smoother in the Fourier/support-edge coordinate.

More generally, let `mu` be any finite pair-difference measure and define its unweighted form factor

`K(q)=integral_R exp(2*pi*i*q*x) dmu(x)`.

The same measure with Montgomery's weight has form factor

`K^(w)(q)=integral_R W_L(x) exp(2*pi*i*q*x) dmu(x)`

and exactly

`K^(w)=P_L * K`.

In particular, if a phase-matched full-circle `CUE_N` pair measure is normalized so that

`K_N(q)=S_N(N q)/N`,

where `S_N` is its real-time second-order spectral form factor under the same eigenangle-difference convention, then the correctly weight-matched full-circle null is

`K_N^(w)(q) = (P_L * K_N)(q)`,

not the pointwise value `S_N(N q)/N`.

For the infinite-CUE/GUE ramp

`K_infty(q)=min(|q|,1)`,

center the positive support edge by

`q=1+v/L`.

For every fixed real `v`, as `L -> infinity`,

`L[(P_L*K_infty)(1+v/L)-1] = H(v) + O_v(exp(-2L))`,

where

`H(v) = v - (1/4) exp(2v)` for `v<=0`,

`H(v) = -(1/4) exp(-2v)` for `v>=0`.

Since

`L[K_infty(1+v/L)-1]=min(v,0)`,

the weight alone contributes the universal edge-rounding residual

`L[(P_L*K_infty)(1+v/L)-K_infty(1+v/L)]`
`  = -(1/4) exp(-2|v|) + O_v(exp(-2L))`.

Equivalently, before any finite-`N` correction or arithmetic term is considered, Montgomery's pair weight creates a negative support-edge bump of height `1/(4L)` and width `O(1/L)` in `q`.

For the finite-height zeta normalization in `VIS-123`,

`L=L_T=log(T/(2*pi))`,

`q=alpha log(T)/L_T`,

so the centered coordinate is exactly

`v=L_T(q-1)=(alpha-1)log(T)+log(2*pi)`.

The weight-induced bump therefore lives on the same `1/log T` horizontal and vertical scale that a raw ramp-centered support-edge visualization would naturally magnify. It is universal smoothing, not evidence of arithmetic structure.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL FOURIER/PAIR-CORRELATION CONTROL + NO-NOVELTY-CLAIM`.

This finding does not determine the correct effective `N(T)`, transfer the hard finite-height zero window to CUE, establish a source-specific residual scale, inspect fresh zero data, or claim a new pair-correlation or random-matrix theorem.

## 1. The Montgomery weight becomes a unit-mass Laplace kernel

Put

`a=L/pi`.

Then

`W_L(x)=a^2/(a^2+x^2)`.

The standard Cauchy-kernel Fourier transform gives

`integral_R [a^2/(a^2+x^2)] exp(-2*pi*i*r*x) dx`
`  = pi*a exp(-2*pi*a|r|)`
`  = L exp(-2L|r|)`.

Hence

`P_L(r)=L exp(-2L|r|)`.

Its mass is

`integral_R P_L(r) dr`
`  = 2L integral_0^infinity exp(-2Lr) dr`
`  = 1`.

The scale is therefore intrinsic: the original difference weight has physical width `Delta=O(1)`, which becomes `x=O(L)` after unfolding, while its Fourier dual has width `q=O(1/L)`.

For `L=L_T`, this is precisely the support-edge resolution identified in `VIS-123`. The smoothing scale is not an arbitrary plotting bandwidth.

## 2. Weighting a pair-difference measure is convolution in support-edge frequency

Fourier inversion gives

`W_L(x)=integral_R P_L(r) exp(2*pi*i*r*x) dr`.

Therefore, for a finite pair-difference measure `mu`,

`K^(w)(q)`
` = integral_R W_L(x) exp(2*pi*i*q*x) dmu(x)`
` = integral_R P_L(r) K(q+r) dr`.

Because `P_L` is even, this is the usual convolution

`K^(w)(q)=(P_L*K)(q)`.

This identity is exact and does not use a large-`N`, large-`T`, or random-matrix approximation. It also keeps the diagonal automatically: at zero difference `W_L(0)=1`, so whatever diagonal convention is present in `mu` passes through unchanged at the measure level.

For a full-circle finite-CUE control, define the normalized pair measure and its real-time form factor using one fixed eigenangle-difference convention. If its unweighted transform is written as

`K_N(q)=S_N(Nq)/N`,

then the Montgomery-weight-matched null is exactly

`K_N^(w)=P_L*K_N`.

Thus `VIS-123`'s exact all-real-time finite-`N` CUE baseline is an input to the null, but it must be convolved with `P_L` before comparison with Montgomery's weighted statistic. Pointwise evaluation of the unweighted finite-CUE curve leaves a deterministic weight mismatch.

## 3. The universal ramp has an explicit rounded-edge profile

Take

`K_infty(q)=min(|q|,1)`

and focus on the positive edge. Set

`q=1+v/L`, `s=1+y/L`.

Then

`P_L(q-s) ds = exp(-2|v-y|) dy`.

At fixed `v`, the part of the integral near `s=1` sees

`K_infty(1+y/L)=1+y/L` for `y<0`,

`K_infty(1+y/L)=1` for `y>0`.

The distant cusp at zero and the opposite support edge are `O_v(exp(-2L))` under this kernel. Hence

`L[(P_L*K_infty)(1+v/L)-1]`
` = integral_(-infinity)^0 y exp(-2|v-y|) dy + O_v(exp(-2L))`.

For `v>=0`, the absolute value never changes sign on `y<=0`, giving

`H(v)=exp(-2v) integral_(-infinity)^0 y exp(2y) dy`
`    = -(1/4)exp(-2v)`.

For `v<=0`, split the integral at `y=v`:

`H(v)`
` = integral_(-infinity)^v y exp(-2(v-y)) dy`
`   + integral_v^0 y exp(-2(y-v)) dy`
` = v-(1/4)exp(2v)`.

Subtracting the unsmoothed ramp leaves in both cases

`H(v)-min(v,0)=-(1/4)exp(-2|v|)`.

The shape is therefore fixed before any zeta-zero data are inspected: a symmetric exponential deficit around the correctly centered edge. A visualization that subtracts only `min(|q|,1)` will display this bump even for the universal infinite-CUE null.

The finite-`N` situation contains two distinct universal controls on the same edge: `VIS-123`'s continuous-time CUE finite-size ripple and the exact Laplace convolution established here. They must be combined before a residual is assigned arithmetic meaning.

## 4. Prior-art and novelty assessment

Montgomery's weighted pair-correlation statistic and the weight `w(u)=4/(4+u^2)` are classical. Goldston--Gonek--Özlük--Snyder is a standard precise reference for the weighted transform and its support/continuation problem. No novelty is claimed for the statistic, the weight, the Cauchy/Laplace Fourier pair, or the general fact that multiplication in the difference variable becomes convolution in Fourier frequency.

Languasco--Perelli--Zaccagnini's explicit pair-correlation/short-interval relations use exponential smoothing in the Abelian--Tauberian machinery. That literature is a prior-art warning against presenting exponential smoothing itself as a new arithmetic mechanism; this finding does not claim their kernel is identical to the finite-CUE convolution used here.

Sohail--Huang--Wei's 2026 exact all-real-time finite-`N` CUE spectral form factor remains the authoritative finite-CUE input used by `VIS-123`. The Mathia-specific content here is only the control translation required by the accepted support-edge clue: once Montgomery's weight is written in the same unfolded coordinate as `VIS-123`, the matched full-circle null is forced to be a Laplace convolution, and the limiting ramp's resulting edge-rounding profile can be evaluated explicitly.

No external source found in the line's current prior-art surface is being claimed to omit this elementary transform. The result is stored because it closes a concrete null-calibration ambiguity for the active visual experiment, not because the Fourier identity is novel mathematics.

## Boundary and falsification

The derivation assumes the fixed local unfolding scale `L` across the pair-difference measure. The actual Montgomery statistic on zeros up to height `T` has hard finite-height geometry and a density that varies across the source window. Replacing that source by one stationary unfolded measure is an additional transfer step not proved here.

The finite-CUE statement is exact only after a precise full-circle pair measure, eigenangle-difference convention, and normalization have been fixed. For noninteger real time, branch/arc conventions must match the `S_N` definition used in the chosen exact CUE formula. This finding does not choose the effective size `N(T)`.

The diagonal is not removed by the weight, since `W_L(0)=1`; a source statistic that subtracts or renormalizes diagonal mass must apply the identical convention to its CUE null.

The explicit profile is for the infinite-CUE ramp. It must not be substituted for the exact finite-`N` weighted null. At the finite sizes relevant to a source comparison, compute or evaluate `P_L*K_N` itself so that the real-time finite-`N` ripple and the pair-weight smoothing are not double-counted or omitted.

No statement here determines whether an arithmetic residual survives after those controls. If the eventual source-window transfer changes the effective Fourier kernel, the matched null must use that exact kernel instead of reusing the full-circle formula by analogy.

## Research consequence

`VIS-123` fixed the phase coordinate and exposed a continuous-time finite-CUE support-edge correction. `VIS-124` closes the next calibration layer: Montgomery's pair weight is not a nuisance parameter to tune but an exact unit-mass Laplace convolution in the same edge coordinate, with a universal `-(4L_T)^(-1) exp(-2|v|)` ramp-rounding profile.

The accepted support-edge clue therefore remains live but narrower. Before any fresh zero confirmation window is inspected, the remaining null problem is to transfer the actual finite-height source window and nonstationary unfolding, fix the effective `N(T)` and diagonal normalization, and evaluate the resulting weighted finite-CUE covariance/statistic under those same choices. Only after that matched null is frozen is it meaningful to search for or scale a post-null arithmetic residual.