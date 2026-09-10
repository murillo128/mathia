# VIS-143 — finite source windows force an ultra-low-frequency quadratic CUE companion regime

## Claim

Use the exact bounded-arc finite-CUE null and notation of `VIS-142`:

`D_N(x)=sin(pi x)/(N sin(pi x/N))`,

`W_L(x)=1/(1+(pi x/L)^2)`,

`0<M<=alpha N` with fixed `0<alpha<1`, and

`Delta_(N,L,M)(q)=integral_(-M)^M A_M(x)W_L(x)D_N(x)^2[1-cos(2*pi*q*x)]dx`.

Put

`kappa_alpha=(pi alpha)/sin(pi alpha)`

and

`J(M)=integral_(-M)^M sin(pi x)^2 dx = M-sin(2*pi*M)/(2*pi)`.

Then for every real `q`,

`0 <= Delta_(N,L,M)(q) <= 2 kappa_alpha^2 J(M) q^2`.

Combining this with the uniform linear estimate of `VIS-142` gives

`0 <= Delta_(N,L,M)(q) <= kappa_alpha^2 min(min(|q|,1), 2 J(M) q^2)`.

Consequently, for any finite signed measure `nu_b` supported in `|q|<=b<1`,

`|integral Delta_(N,L,M)(q) dnu_b(q)|`
` <= kappa_alpha^2 ||nu_b||_TV min(b, 2 J(M)b^2)`.

Thus the shrinking low-frequency companion has two distinct null-side regimes. The linear `O(b)` bound of `VIS-142` is the robust bound when the source-difference window is allowed to grow without relation to `b`. But once

`2 J(M)b << 1`,

the finite source window resolves the sine-kernel cusp and the centered CUE mean is instead at most `O(J(M)b^2)`. For large `M`, `J(M)=M+O(1)`, so the crossover is at frequency scale `b asymp 1/M`; in particular, if `M b -> 0`, bounded-normalization packets have amplitude `O(M b^2)`.

If one demands an order-one **CUE-centered mean contribution** from such an ultra-low-frequency packet solely by scalar/total-variation amplification, the exact necessary pressure is

`||nu_b||_TV >= c_0 / [2 kappa_alpha^2 J(M)b^2]`

along any subsequence where the packet contribution is required to have magnitude at least `c_0>0` and the quadratic branch is the active upper bound. When `M->infinity` with `M b->0`, this is of order at least `1/(M b^2)`, which is stronger than the `1/b` pressure recorded in `VIS-142`.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL ELEMENTARY FOURIER BOUND + NEGATIVE DESIGN CONTROL + NO-NOVELTY-CLAIM`.

No zeta arithmetic signal, covariance law, four-level theorem, variance estimate, or lower bound on `Delta` is claimed.

## 1. Exact finite-window quadratic bound

`VIS-142` proves on `|x|<=M<=alpha N` that

`0 <= A_M(x)W_L(x)D_N(x)^2 <= kappa_alpha^2 sinc(x)^2`,

where `sinc(x)=sin(pi x)/(pi x)`.

Use the elementary inequality

`1-cos u <= u^2/2`.

With `u=2*pi*q*x`,

`Delta(q)`
` <= 2*pi^2 kappa_alpha^2 q^2 integral_(-M)^M x^2 sinc(x)^2 dx`.

Since

`x^2 sinc(x)^2 = sin(pi x)^2/pi^2`,

this becomes

`Delta(q) <= 2 kappa_alpha^2 q^2 integral_(-M)^M sin(pi x)^2 dx`.

The remaining integral is elementary:

`integral_(-M)^M sin(pi x)^2 dx = M-sin(2*pi*M)/(2*pi)=J(M)`.

Hence

`Delta(q) <= 2 kappa_alpha^2 J(M)q^2`.

No asymptotic replacement has been used; the bound holds for every admissible finite `N,L,M` and every real `q` under the same fixed capacity margin as `VIS-142`.

## 2. Why this does not contradict the linear sine-kernel cusp

`VIS-142` deliberately extended the positive kernel from `[-M,M]` to the full real line and used

`integral_R sinc(x)^2[1-cos(2*pi*q*x)]dx=min(|q|,1)`.

That infinite-window profile has a linear cusp at zero because the second moment of `sinc^2` diverges. The present estimate keeps the actual finite source-difference support. Its second moment is finite, so the zero-centered Fourier profile is quadratically flat at sufficiently small frequency.

The two statements therefore control different uniformity regimes rather than conflict. At fixed nonzero `q`, letting `M` grow sends the quadratic upper bound upward and leaves the uniform linear bound useful. At fixed finite `M`, taking `q->0` activates the quadratic bound. For large `M`, the transition occurs when `J(M)|q|` is order one, equivalently at the inverse source-window scale up to constants.

This is also a representation check. The quadratic flattening is a property of the exact Fourier-frequency response of the declared finite pair-difference kernel; it is not inferred from a plotted slope, display coordinate, or visual smoothing artifact.

## 3. Consequence for a support-safe companion packet

Let `nu_b` be any finite signed measure supported on `[-b,b]`, with `b<1`. Total variation gives

`|integral Delta(q)dnu_b(q)|`
` <= ||nu_b||_TV sup_(|q|<=b) Delta(q)`
` <= kappa_alpha^2 ||nu_b||_TV min(b,2J(M)b^2)`.

The support constraint from `VIS-141` only says that the companion bandwidth must collapse as the first factor approaches the Montgomery edge. `VIS-142` showed that this already costs at least a linear normalization pressure under a bound uniform in the source-window size. The new finite-window estimate says that a design which pushes the companion still farther toward DC, into `J(M)b<<1`, enters a more expensive analytic regime rather than finding a free nearly-constant mode.

For a proposed family `(M_L,b_L)`, the normalization audit must therefore state which dimensionless regime applies. If `J(M_L)b_L` is not small, retain the `O(b_L)` control from `VIS-142`. If `J(M_L)b_L->0`, use the sharper `O(J(M_L)b_L^2)` bound. An argument that silently changes the relation between source-window width and companion bandwidth changes the null-side amplitude scale and cannot reuse a normalization estimate from the other regime.

The necessary total-variation growth above concerns only a demand for order-one **finite-CUE centered mean** produced by this packet. It is not a statement that a zeta-specific arithmetic correction must have the same scaling, nor that such amplification is sufficient to reveal one.

## 4. Stress tests and boundaries

The estimate passes the exact `q=0` check and remains nonnegative because the original kernel and `1-cos` factor are nonnegative. For integer `M`, the coefficient simplifies to `J(M)=M`, so the quadratic bound is exactly

`Delta(q) <= 2 kappa_alpha^2 M q^2`.

For noninteger `M`, the oscillatory endpoint correction is retained rather than hidden in an asymptotic. Since `J(M)` is itself the integral of a nonnegative function, no sign issue is introduced by that correction.

The bound deliberately uses only `A_M<=1` and `W_L<=1`; it may therefore be loose. Additional taper or Montgomery-weight cancellation can make the actual profile smaller, never invalidate the upper bound. Likewise, signed cancellation inside `nu_b` can reduce the packet amplitude but cannot evade the total-variation estimate.

The fixed-capacity assumption remains essential for the uniform constant `kappa_alpha`. If `M/N->1`, the current domination of `D_N` by `sinc` loses uniformity and the finite-circle coordinate boundary must be analyzed directly.

Most importantly, this is a mean-profile control. It does not determine stochastic variance, cross-height dependence, the zeta-to-CUE transfer error, the Rudnick–Sarnak remainder for an `L`-dependent test family, or the arithmetic lower-order term. Any normalization growing like `1/[J(M)b^2]` must still be propagated through those channels before a shrinking-band redesign can become a viable experiment.

## 5. Prior-art and novelty audit

The mathematical ingredients are classical and already bounded by the current line's source anchors. The finite-CUE kernel and capacity-margin domination are inherited from `VIS-130` and `VIS-142`; the full-line `sinc^2`/triangle identity and restricted-support context are already treated there and in `VIS-140`--`VIS-142`. The new step uses only the elementary inequality `1-cos u<=u^2/2` and the exact finite integral of `sin^2(pi x)`.

Compactly supported integrable kernels having a quadratically flat centered cosine transform when their second moment is finite is standard Fourier analysis, so no general harmonic-analysis or random-matrix novelty is claimed. A bounded literature check found only the expected classical Fejer/windowing context, not a reason to reinterpret this elementary estimate as a new theorem. The Mathia-specific value is the explicit crossover and normalization accounting for the exact support-edge CUE null already frozen by this research thread.

No new external source is needed beyond the anchors already recorded in `research/visual_exploration/SOURCES.md`.

## Research consequence

The accepted support-edge clue now has a sharper design fork. Any asymmetric edge–low-frequency proposal should freeze not only the support margin and packet normalization but also the relation between companion bandwidth `b_L` and the finite source-difference width `M_L`.

If `J(M_L)b_L` stays order one or larger, the robust `VIS-142` linear pressure remains the useful null-side gate. If `J(M_L)b_L->0`, the finite-CUE companion becomes quadratically flat and an order-one centered mean obtained by scalar amplification requires total variation at least on the scale `1/[J(M_L)b_L^2]`. That stronger amplification must be carried through the same theorem-uniformity, finite-height transfer, stochastic-noise, and cross-window covariance obligations already identified by the clue.

This narrows the restricted-support escape without touching untouched confirmation-zero data. The original edge-edge route remains unaffected: genuinely wider-support four-level information or a direct covariance/mixing theorem would bypass the shrinking companion entirely.
