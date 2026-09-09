# VIS-123 — the continuous-CUE support edge has a logarithmic finite-size ripple

## Claim

Let

`L_T = log(T/(2*pi))`

be the local Riemann-zero density scale and unfold a zero difference by

`x = L_T (gamma-gamma')/(2*pi)`.

For Montgomery's phase factor

`T^(i alpha (gamma-gamma'))`,

the exact Fourier coordinate in these unfolded units is

`q_T(alpha) = alpha log(T)/L_T`.

For a `CUE_N` comparison, an eigenangle difference unfolded by `x=N(theta-theta')/(2*pi)` carries the real-time trace phase `exp(2*pi i (k/N)x)`. Therefore the phase-matched full-circle dictionary is

`k/N = q_T(alpha) = alpha log(T)/L_T`.

In particular the CUE ramp/plateau edge `k/N=1` does **not** occur exactly at `alpha=1` under the local-density convention. It occurs at

`alpha_*(T) = L_T/log(T) = 1 - log(2*pi)/log(T)`.

Thus the previously proposed edge coordinate

`u = (alpha-1) log(T)`

is a valid `O(1)` coordinate but places the matched edge at

`u_* = -log(2*pi)`.

Equivalently, with

`v = u + log(2*pi) = (alpha-alpha_*) log(T)`,

one has the exact phase relation

`k-N = tau = [N/L_T] v`.

This horizontal calibration exposes a second, more consequential control. Sohail, Huang, and Wei's exact continuous-time finite-`N` CUE spectral form factor gives, for fixed real `tau` and `k=N+tau`,

`S_N(N+tau) - min(N,N+tau)`
`  = -(sin^2(pi tau)/pi^2) log(N) + O_tau(1)`

as `N -> infinity`. At integer `tau` the sine factor vanishes and the exact discrete-time identity `S_N(k)=min(N,|k|)` is recovered.

Consequently a continuous support-edge visualization centered only by the infinite-`N` ramp has a **universal finite-CUE ripple of normalized size `(log N)/N`**, not merely `1/N`. If a matched size satisfies `N(T) ~ rho L_T` for a fixed `rho>0`, this is of order

`log log(T) / log(T)`.

Therefore multiplying a ramp-centered continuous edge profile by `log(T)` before subtracting the exact finite-CUE null generically amplifies a universal CUE artifact to order `log log(T)`. The natural scale that makes this particular universal ripple `O(1)` is `N/log N` (equivalently `log(T)/log log(T)` up to the matching constant), but **no scale for the arithmetic residual after exact finite-CUE subtraction is established here**.

**Evidence/status:** `LITERATURE+DERIVED + EXACT PHASE DICTIONARY + ASYMPTOTIC NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

This finding does not assert that any specific finite-`T` zeta statistic is exactly `CUE_N`, determine the correct effective `N(T)`, transfer the full-circle formula through Montgomery's weight/window, or establish an arithmetic support-edge residual.

## 1. The phase dictionary fixes the horizontal edge before any zero inspection

Montgomery's weighted pair statistic uses the oscillatory factor

`T^(i alpha Delta_gamma) = exp(i alpha log(T) Delta_gamma)`.

Using the local Riemann-von Mangoldt unfolding

`Delta_x = L_T Delta_gamma/(2*pi)`,

this becomes

`exp(2*pi i [alpha log(T)/L_T] Delta_x)`.

For `CUE_N`, write an unfolded eigenangle difference as

`Delta_x = N Delta_theta/(2*pi)`.

Then the real-time mode `exp(i k Delta_theta)` is

`exp(2*pi i [k/N] Delta_x)`.

Matching the Fourier phases gives

`k/N = alpha log(T)/L_T`.

No random-matrix asymptotic is used in this step. It is only the coordinate dictionary between Montgomery's Fourier phase and the ordinary mean-spacing unfolding.

The support edge `k/N=1` therefore corresponds to

`alpha_*(T)=L_T/log(T)`.

Since `L_T=log(T)-log(2*pi)`, the coordinate `u=(alpha-1)log(T)` sends that edge to the fixed point

`u_*=-log(2*pi)`.

The shifted coordinate `v=u+log(2*pi)` centers it exactly. Moreover,

`k/N - 1 = v/L_T`,

so for `k=N+tau`,

`tau = (N/L_T) v`.

Hence if a chosen finite-CUE dictionary has `N/L_T -> rho`, a fixed `v` window is exactly the fixed-`tau` CUE edge regime, with `tau -> rho v`. The value of `rho` remains part of the finite-size source/null dictionary and is not selected here.

This also shows why centering at `alpha=1` without accounting for the `2*pi` density convention is not innocuous at the proposed `1/log T` horizontal scale: the displacement is itself `O(1)` in that scale.

## 2. Exact finite-`N` CUE has a continuous-time edge structure absent at integer modes

Sohail, Huang, and Wei derive an exact all-real-time formula for the CUE second-order spectral form factor `S_N(k)`. At integer `k` it collapses to the classical identity

`S_N(k)=min(N,|k|)`.

Their Corollary 3 instead resolves the continuous edge `k=N+tau` for fixed nonzero real `tau`. With

`Delta(1,tau)=S_N(N+tau)-N`,

they obtain for `tau<0`

`Delta(1,tau)`
` = tau - sin(2*pi*tau)/(2*pi)`
`   + [sin^2(pi*tau)/pi^2]`
`     [-log N + psi_0(|tau|)+|tau| psi_1(|tau|)-1+log 2 + O_tau(1/N)]`,

and for `tau>0` the same bracketed term without the leading `tau-sin(2*pi*tau)/(2*pi)` contribution.

To compare with the large-`N` ramp itself, subtract `min(N,N+tau)`, not `N` on both sides. For `tau<0` this removes the extra `tau`; for `tau>0` the baseline is already `N`. Thus in both cases

`R_N(tau) := S_N(N+tau)-min(N,N+tau)`

satisfies

`R_N(tau) = -(sin^2(pi*tau)/pi^2) log N + O_tau(1)`.

After normalization by `N`,

`R_N(tau)/N = -(sin^2(pi*tau)/pi^2) [log N/N] + O_tau(1/N)`.

The coefficient vanishes at integer `tau`, consistently with the exact discrete-time ramp/plateau identity. Therefore integer-mode sampling can hide the finite-size structure that a continuous `alpha` scan necessarily encounters. This is a representation/control issue, not an arithmetic effect.

## 3. The universal ripple fixes what may not be called an arithmetic residual

Suppose only that the finite-CUE comparison size grows proportionally to the local density scale,

`N(T) ~ rho L_T`,

with fixed `rho>0`. Then

`log N / N = Theta(log log T / log T)`.

At fixed centered edge coordinate `v`, one has `tau=(N/L_T)v`, so at generic noninteger limiting `tau` the ramp-centered continuous CUE profile already contains a deterministic oscillatory correction on that scale.

Two consequences follow.

First, the raw normalization `log(T) [S_N/N - min(1,k/N)]` is not an arithmetic-sensitive edge statistic. Its universal CUE contribution is generically of order `log log T`. A visual excess under that normalization can therefore be created by the matched null itself.

Second, `N/log N` is the scale that makes the **known universal finite-CUE edge ripple** order one. This does not mean that the zeta-minus-CUE residual should be multiplied by `N/log N`. Once the exact finite-`N` null has been subtracted, the first surviving arithmetic correction may be smaller, larger, oscillatory, or absent. Determining that residual scale requires the remaining source/null transfer rather than reusing the universal null scale as an answer.

The safe order is therefore: fix the phase/window dictionary; evaluate or derive the exact finite-CUE baseline at the same continuous coordinates; subtract that baseline; only then ask whether a source-specific residual has a stable amplitude normalization.

## 4. Prior-art and novelty assessment

H. L. Montgomery's 1973 pair-correlation paper is the classical source of the weighted Fourier statistic and its support boundary at `|alpha|=1`; no novelty is claimed for that object or for mean-spacing unfolding.

Sohail, Huang, and Wei, **Higher-order spectral form factors of circular unitary ensemble**, *Journal of Statistical Physics* 193 (2026), article 20, DOI `10.1007/s10955-026-03572-8`, derive the exact finite-`N` second-order CUE spectral form factor for real time and explicitly state both the integer identity `S_N(k)=min(N,|k|)` and the fixed-`tau` edge expansions used above. The logarithmic edge ripple is therefore direct prior art from their Corollary 3, not a Mathia discovery.

The Mathia-specific content is the control translation into the accepted Montgomery support-edge clue: combining that exact CUE edge expansion with the finite-height phase/unfolding dictionary shows that the clue's provisional `u=(alpha-1)log T` coordinate needs a fixed `-log(2*pi)` edge offset, and that a ramp-only `log T` vertical magnification is universally contaminated before exact finite-CUE subtraction.

Nearby finite-size zeta/CUE literature already recorded in `research/visual_exploration/SOURCES.md` reinforces the general warning that finite-height deviations are not automatically arithmetic-specific. This finding makes the warning quantitative for the continuous support edge, but does not claim a new CUE theorem or a new zeta pair-correlation theorem.

## Boundary and falsification

The phase dictionary assumes the ordinary local mean-spacing unfolding `L_T/(2*pi)`. Changing the precise finite-height window center or unfolding convention can move the `O(1/log T)` edge centering, so any actual experiment must freeze that convention before source inspection.

The CUE asymptotic is a full-circle continuous-time result. Montgomery's statistic has a finite height range, the weight `w(gamma-gamma')=4/(4+(gamma-gamma')^2)`, diagonal terms, and a source normalization. This finding does **not** prove that those ingredients transfer to `S_N(k)` without additional window/smoothing corrections.

The statement `N(T)~rho L_T` is a conditional scaling hypothesis for converting the CUE asymptotic into `T`-order notation. No particular `rho` is chosen or justified here. If the correct matched size has a different growth law, the `T`-scale conclusion must be recomputed, while the exact `k/N` phase dictionary and finite-`N` CUE edge formula remain valid in their own variables.

The logarithmic term vanishes at integer `tau`. Any diagnostic that samples only integer CUE modes has therefore quotiented out precisely the continuous-time ripple discussed here and cannot be used as evidence that the ripple is absent.

## Research consequence

This resolves the first calibration layer of `CLUE-zeta-montgomery-support-edge-arithmetic-residual.md` without inspecting fresh zero windows. The horizontal edge should be centered at

`v=(alpha-1)log(T)+log(2*pi)`

under the stated unfolding, with `tau=(N/L_T)v`. A ramp-only vertical residual must not be magnified by `log T` and interpreted arithmetically before the exact continuous finite-CUE baseline is removed.

The accepted clue remains live because the decisive source/null step is still missing: transfer the chosen finite-height Montgomery window, weight, diagonal convention, normalization, and effective-size rule to a matched finite-CUE statistic, then determine the scale of the **post-null** residual. Only after that derivation should any new zero confirmation window be inspected.