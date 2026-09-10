# VIS-142 — a Rudnick–Sarnak-safe low-frequency CUE companion has at most linear centered amplitude

## Claim

Use the exact bounded-arc finite-CUE null from `VIS-130`. Let

`D_N(x)=sin(pi x)/(N sin(pi x/N))`,

let `A_M(x)` be the normalized tent-overlap factor, let

`W_L(x)=1/(1+(pi x/L)^2)`,

and assume a fixed capacity margin

`0 < M <= alpha N`, with `0<alpha<1`.

Define the CUE mean profile

`C_(N,L,M)(q)=1-integral_(-M)^M A_M(x) W_L(x) D_N(x)^2 cos(2*pi*q*x) dx`

and its zero-frequency-centered increment

`Delta_(N,L,M)(q)=C_(N,L,M)(q)-C_(N,L,M)(0)`.

Then for every real `q`,

`0 <= Delta_(N,L,M)(q) <= kappa_alpha^2 min(|q|,1)`,

where

`kappa_alpha = (pi alpha)/sin(pi alpha)`.

Consequently, if a support-safe low-frequency companion is any signed superposition of these centered modes with a finite signed measure `nu_b` supported in `|q|<=b<1`, then

`| integral Delta_(N,L,M)(q) d nu_b(q) | <= kappa_alpha^2 b ||nu_b||_TV`.

Thus the companion forced by `VIS-141` toward bandwidth `b_L->0` has **vanishing finite-CUE centered mean amplitude whenever its total-variation normalization stays bounded**. To keep an order-one CUE-scale centered companion by linear rescaling alone requires normalization growing at least on the order of `1/b_L`.

This does not prove that a zeta-specific arithmetic term vanishes. It sharpens the redesign gate: an edge–low-frequency statistic must now justify not only why the low-frequency factor is arithmetic-specific, but also which normalization keeps that signal visible and why the corresponding `L`-dependent test family remains inside the quantitative range of the theorem used to control it.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL FOURIER IDENTITY + NEGATIVE DESIGN CONTROL + NO-NOVELTY-CLAIM`.

No new CUE theorem, zeta pair-correlation theorem, four-level theorem, covariance estimate, or arithmetic residual is claimed.

## 1. Finite-CUE kernel is uniformly dominated by the sine kernel away from the circle boundary

Write

`sinc(x)=sin(pi x)/(pi x)`

with the removable value `sinc(0)=1`. Then

`D_N(x)=sinc(x) * [(pi x/N)/sin(pi x/N)]`.

For `|x|<=M<=alpha N`, put `u=pi |x|/N`. The function `u/sin u` is increasing on `(0,pi)` because

`d/du [u/sin u] = [sin u-u cos u]/sin(u)^2`

and `sin u-u cos u` has derivative `u sin u>0` and vanishes at zero. Hence

`|D_N(x)| <= kappa_alpha |sinc(x)|`,

where `kappa_alpha=(pi alpha)/sin(pi alpha)`.

The tent overlap and Montgomery weight satisfy

`0<=A_M(x)<=1`, `0<W_L(x)<=1`.

Therefore on the full source-difference support,

`0 <= A_M(x)W_L(x)D_N(x)^2 <= kappa_alpha^2 sinc(x)^2`.

The constant depends only on the declared capacity margin `alpha`; it is independent of `N`, `L`, `M`, and the low frequency `q`. Its divergence as `alpha->1` is consistent with the coordinate-boundary warning in `VIS-130`.

## 2. The classical sinc-squared triangle identity gives the linear bound

Because the kernel is nonnegative and even,

`Delta(q)`
` = integral_(-M)^M A_M(x)W_L(x)D_N(x)^2 [1-cos(2*pi*q*x)] dx`

is nonnegative.

Using the domination above and extending the nonnegative integral to the real line gives

`Delta(q)`
` <= kappa_alpha^2 integral_R sinc(x)^2 [1-cos(2*pi*q*x)] dx`.

With the Fourier convention used throughout this thread, the classical transform identity is

`integral_R sinc(x)^2 exp(2*pi*i*q*x) dx = (1-|q|)_+`.

Since `integral_R sinc(x)^2 dx=1`,

`integral_R sinc(x)^2 [1-cos(2*pi*q*x)] dx = min(|q|,1)`.

This proves

`0<=Delta(q)<=kappa_alpha^2 min(|q|,1)`.

The linear cusp is important. A naive Taylor expansion of `cos(2*pi*q*x)` would suggest a quadratic small-`q` law, but the infinite sine-kernel second moment is not integrable. Finite source windows smooth that cusp at extremely small `q`, yet the uniform bound over all admissible `M,N,L` remains linear. The correct robust statement for a shrinking companion band is therefore `O(b)`, not an assumed `O(b^2)` or an order-one DC mode.

## 3. Any bounded-normalization low-frequency packet collapses in centered CUE mean

Let `nu_b` be a finite signed measure supported on `[-b,b]`, `b<1`. By total variation,

`| integral Delta(q) dnu_b(q) |`
` <= sup_(|q|<=b) Delta(q) ||nu_b||_TV`
` <= kappa_alpha^2 b ||nu_b||_TV`.

So any family with uniformly bounded `||nu_b||_TV` vanishes at least linearly as `b->0`.

This applies in particular to a probability-weighted average of low-frequency companion modes, to a fixed-shape compact packet whose `L1` normalization is held constant, or to any signed packet whose total variation is uniformly bounded. Oscillatory cancellation can make the result smaller, but cannot evade this upper bound.

Conversely, if one wants the **CUE-centered mean contribution itself** to remain order one solely by multiplying such a packet by a scalar, the packet's total-variation norm must grow at least like `1/b` along any subsequence on which an order-one lower bound is demanded. This is only a necessary normalization pressure, not a sufficiency theorem: a `1/b` rescaling can amplify noise, finite-size error, and transfer error together with any desired signal.

## 4. Interaction with the Rudnick–Sarnak support budget

`VIS-141` shows that a tensor-product pair test whose first factor reaches `a_L=1-epsilon_L` can lie inside the classical Rudnick–Sarnak support diamond only if the independent companion support obeys

`b_L<epsilon_L`.

Combining that exact support inequality with the present bound gives, for bounded companion normalization,

`|B_L| <= kappa_alpha^2 b_L ||nu_(b_L)||_TV < kappa_alpha^2 epsilon_L ||nu_(b_L)||_TV`.

Therefore the simple restricted-support escape has a second cost beyond frequency collapse: **the zero-mode-centered finite-CUE mean scale of the companion also collapses** unless its normalization grows.

Growing normalization does not violate Fourier support by itself, but it creates a quantitative-uniformity obligation. Rudnick–Sarnak's support theorem, as used in `VIS-140`, supplies an asymptotic for admissible smooth tests; it does not by itself supply the error estimate needed for an `L`-dependent family whose amplitude/seminorms diverge like `1/b_L` while its support margin may simultaneously approach the boundary. Any such use must prove the relevant uniformity rather than multiplying a fixed-test `o(1)` remainder by an unbounded factor and assuming it remains negligible.

This is independent of the already-recorded localization issue: the actual source windows are bounded physical windows with an `L`-dependent geometry, so support admissibility alone was never a complete cross-height covariance theorem.

## 5. Prior-art and novelty audit

The ingredients are classical or already anchored in the current line:

- `VIS-130` derives the exact finite-CUE bounded-tent kernel from the standard CUE determinantal two-point function and records the capacity-margin issue.
- The Fourier transform `sinc^2 <-> triangle` is the classical Fejer/Bartlett kernel identity underlying ordinary spectral windowing; no novelty is claimed for it.
- `VIS-140` and `VIS-141` record the Rudnick–Sarnak restricted-support theorem and its exact pullback to the pair-pair plane.

The present contribution is the Mathia-specific composition of those controls. It turns the qualitative phrase “the companion collapses toward DC” into a quantitative bound for the exact finite-CUE null used by the support-edge thread and exposes the normalization/uniformity price of trying to keep that companion macroscopically visible.

A bounded literature recheck did not reveal any need to reinterpret this elementary estimate as a new random-matrix or harmonic-analysis theorem. The result is stored as a design obstruction for the active experiment, not as a novelty claim.

## 6. Boundary and falsification

The inequality controls the **finite-CUE mean profile after centering at `q=0`**. It does not control zeta's arithmetic correction, the variance of the companion, its cross-height covariance, or a non-factorized four-level statistic. In particular, it does not prove that a zeta-specific term inside `|q|<=b_L` must be `O(b_L)`.

A viable edge–low-frequency redesign can therefore escape this obstruction in a substantive way: derive an arithmetic contribution whose declared normalization remains informative as `b_L->0`, and simultaneously prove that CUE noise, finite-height transfer, source-window dependence, and the higher-correlation theorem error remain below that contribution under the same normalization.

The estimate also assumes a fixed capacity margin `M/N<=alpha<1`. If a proposed construction lets `M/N->1`, the constant `kappa_alpha` ceases to be uniform and the full-circle coordinate boundary must be handled directly rather than hidden inside this bound.

Finally, the result does not rule out the original edge-edge route. A direct covariance/mixing theorem or genuinely wider-support four-level information bypasses the shrinking-companion design entirely.

## Research consequence

The accepted support-edge clue should treat the asymmetric Rudnick–Sarnak-safe route as a **renormalized shrinking-channel problem**, not merely a support-placement problem. Before constructing confirmation statistics, specify the companion packet `nu_(b_L)`, its total-variation/amplitude normalization, and the relation of `b_L` to the edge margin `epsilon_L`.

If the normalization stays bounded, its finite-CUE zero-mode-centered mean is at most `O(b_L)` and therefore vanishes. If it is amplified by `1/b_L` or more to keep an order-one scale, the same amplification must be propagated through theorem errors, finite-height transfer, stochastic variance, and cross-window covariance. An arithmetic residual is useful only if it survives that full accounting.

No untouched confirmation-zero evidence is used.