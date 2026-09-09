# VIS-126 — smooth zero-density drift admits a mesoscopic support-edge corridor

## Claim

Let

`L_T = log(T/(2*pi))`

and let the smooth Riemann--von Mangoldt counting main term be

`Nbar(t) = [t/(2*pi)] log(t/(2*pi)) - t/(2*pi) + C`,

where the constant `C` is irrelevant below. Then

`Nbar'(t)=log(t/(2*pi))/(2*pi)`.

For offsets `a,b` in a symmetric physical window `|a|,|b|<=H<T`, compare the exact smooth unfolding across the window with the center-linearized unfolding:

`D_T(a,b)`
` := [Nbar(T+a)-Nbar(T+b)] - [L_T/(2*pi)](a-b)`.

There is the exact identity

`D_T(a,b) = (1/(2*pi)) integral_b^a log(1+s/T) ds`,

and therefore the uniform bound

`|D_T(a,b)| <= H^2/[pi(T-H)]`.

If `H=o(T)`, uniformly on the window,

`D_T(a,b) = (a^2-b^2)/(4*pi*T) + O(H^3/T^2)`.

Thus, in any bounded support-edge Fourier coordinate `|q|<=Q`, replacing exact smooth Riemann--von Mangoldt unfolding by the frozen center density changes each pair phase by at most

`O_Q(H^2/T)`.

For a Montgomery-weighted local pair statistic normalized per zero/window length, standard local zero counting and the summability of `w(u)=4/(4+u^2)` give normalized absolute weighted pair mass `O(L_T)`. Hence the corresponding normalized form-factor error from **smooth density linearization alone** is bounded by

`O_Q(L_T H^2/T)`.

Consequently a sufficient condition for smooth-density drift to be negligible at a proposed `1/L_T` support-edge residual scale is

`H^2 L_T^2 / T -> 0`.

Combining this with the hard-window leakage condition from `VIS-125`,

`H/log(H L_T) -> infinity`,

produces a broad common mesoscopic corridor. For example, every fixed power

`H = L_T^A`, `A>0`,

simultaneously makes the rectangular-window leakage and the smooth-density linearization error `o(1/L_T)` as `T->infinity`. With a smooth taper satisfying the finite spectral first-moment condition of `VIS-125`, the window requirement weakens to `H->infinity`, and the same density-drift corridor remains available.

Therefore the classical smooth variation of zero density across a local window is **not by itself an asymptotic obstruction** to resolving a support-edge residual on the `1/log T` scale. The remaining transfer problem lies elsewhere: exact finite-CUE effective-size/arc matching, diagonal and compactification conventions, covariance, counting-function fluctuations beyond the smooth main term, and any genuinely arithmetic lower-order contribution.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL RIEMANN--VON MANGOLDT CONTROL + NEGATIVE OBSTRUCTION TEST + NO-NOVELTY-CLAIM`.

No arithmetic support-edge residual, effective matrix size, CUE covariance transfer, new zero-density theorem, or RH implication is claimed.

## 1. Smooth unfolding and center-linearization differ by one explicit integral

Differentiate the smooth counting main term:

`Nbar'(t)=log(t/(2*pi))/(2*pi)`.

Hence

`Nbar(T+a)-Nbar(T+b)`
` = (1/(2*pi)) integral_b^a log((T+s)/(2*pi)) ds`.

Subtracting the frozen center-density contribution gives

`D_T(a,b)`
` = (1/(2*pi)) integral_b^a [log((T+s)/(2*pi))-L_T] ds`
` = (1/(2*pi)) integral_b^a log(1+s/T) ds`.

For `|s|<=H<T`,

`|log(1+s/T)| <= |s|/(T-H) <= H/(T-H)`.

Since `|a-b|<=2H`,

`|D_T(a,b)| <= [1/(2*pi)](2H)[H/(T-H)]`
`              = H^2/[pi(T-H)]`.

This is a deterministic coordinate error. It does not use zero statistics, random matrices, RH, or a cancellation hypothesis.

Expanding `log(1+s/T)` uniformly for `H=o(T)` yields

`log(1+s/T)=s/T+O(H^2/T^2)`.

After integration,

`D_T(a,b)=(a^2-b^2)/(4*pi*T)+O(H^3/T^2)`.

The first correction is therefore a quadratic shear across the physical source window, rather than an independent oscillatory arithmetic term.

## 2. The support-edge phase error is `O(H^2/T)` pointwise

Use the exact smooth-unfolded pair coordinate

`x_exact = Nbar(T+a)-Nbar(T+b)`

and the frozen local coordinate

`x_lin = [L_T/(2*pi)](a-b)`.

For a Fourier coordinate `q`, their phases differ by

`exp(2*pi*i*q*x_exact)-exp(2*pi*i*q*x_lin)`.

The elementary bound `|exp(iu)-exp(iv)|<=|u-v|` gives

`|phase_exact-phase_lin| <= 2*pi |q| |D_T(a,b)|`.

Thus for `|q|<=Q`,

`|phase_exact-phase_lin| <= 2Q H^2/(T-H)`.

The support-edge regime of `VIS-123` has `q=1+O(1/L_T)`, so it lies inside such a fixed bounded `Q` range. Smooth density variation therefore does not create a hidden order-one phase distortion on that edge whenever `H^2/T -> 0`.

## 3. A conservative weighted-statistic bound costs one factor of `L_T`

A local Montgomery statistic contains the pair weight

`w(u)=4/(4+u^2)`.

For heights in a window `T+O(H)` with `H<=T/2`, standard Riemann--von Mangoldt zero counting gives `O(L_T)` zeros in each unit-height interval. Since

`sum_(m in Z) sup_(u in [m,m+1]) w(u) < infinity`,

one obtains, uniformly for each zero `gamma` in the source window,

`sum_(gamma') w(gamma-gamma') = O(L_T)`

over zeros in the same local height regime. A window containing `O(H L_T+L_T)` zeros therefore has total absolute weighted pair mass `O(H L_T^2+L_T^2)`.

After the natural per-zero/window normalization of order `H L_T` for `H>=1`, the absolute weighted mass is `O(L_T)`. Multiplying by the pointwise phase error above gives the conservative form-factor bound

`|F_exact(q)-F_lin(q)| = O_Q(L_T H^2/T)`

for the smooth-unfolding replacement.

This is deliberately an absolute-mass estimate. It does not borrow cancellation from the source or from CUE and therefore is safe as a null-design gate. A sharper covariance calculation may improve it, but no such improvement is needed to exhibit a viable corridor.

To make this error `o(1/L_T)`, it is sufficient that

`H^2 L_T^2/T -> 0`.

Equivalently, the physical half-window may grow substantially faster than any logarithm while remaining far below the square-root scale `sqrt(T)/L_T`.

## 4. The source-window and smooth-density gates are simultaneously satisfiable

`VIS-125` showed that a hard local source window of physical width `H` has unfolded length

`M = H L_T/(2*pi)`

and creates a universal ramp-edge leakage of order

`log M/(H L_T)`.

For that leakage to be `o(1/L_T)`, it suffices that

`H/log(H L_T) -> infinity`.

The new smooth-density gate is

`H^2 L_T^2/T -> 0`.

These conditions are not in tension. Set, for any fixed `A>0`,

`H=L_T^A`.

Then

`H/log(H L_T) = L_T^A/[(A+1)log L_T] -> infinity`,

while

`H^2 L_T^2/T = L_T^(2A+2)/T -> 0`.

Thus the hard-window problem can be pushed below the `1/L_T` target scale **without** making smooth density variation large enough to re-enter at that scale.

If a smooth taper with finite spectral first moment is used instead, `VIS-125` reduces the generic stationary window error to `O(1/(H L_T))`; then merely taking `H->infinity` suppresses that term, subject again to `H^2 L_T^2/T->0`. The taper route therefore has an even larger admissible design region.

## 5. What this removes — and what it does not

This finding removes one specific objection to the accepted support-edge clue: the need to enlarge the source window enough to suppress window leakage does **not** force the smooth Riemann--von Mangoldt density to vary so much that center unfolding becomes invalid on the same `1/L_T` scale.

It does not replace the remaining null construction. In particular:

- the exact zero-counting function contains the fluctuating term customarily denoted `S(t)` in addition to the smooth main term; no claim here bounds its induced covariance contribution by the deterministic calculation above;
- a finite CUE control still needs an effective size `N(T)` and an exact arc/window or matched-ensemble convention;
- `VIS-123`'s continuous finite-`N` ripple, `VIS-124`'s Laplace weight smoothing, and `VIS-125`'s source-window kernel must still be applied in the same representation rather than added piecemeal;
- the covariance of the final low-dimensional support-edge coordinates remains to be derived or simulated under the frozen null;
- no arithmetic lower-order formula has yet selected the amplitude scale of the post-null residual.

The practical consequence is a narrowing, not a positive signal: **smooth density drift can be designed away asymptotically, so the next useful work should concentrate on the genuinely unresolved finite-CUE/covariance and arithmetic terms rather than treating density nonstationarity as an unavoidable blocker.**

## Prior-art and novelty assessment

The Riemann--von Mangoldt zero-counting law and its smooth density are classical. NIST DLMF §25.10 gives the standard zero-distribution/counting context and points to E. C. Titchmarsh, revised by D. R. Heath-Brown, *The Theory of the Riemann Zeta-function*, 2nd ed. (Oxford, 1986), §4.17. No novelty is claimed for the counting main term, its derivative, Taylor expansion, or local density interpretation.

The Mathia-specific content is only the control calculation obtained by combining that classical smooth density with the already persisted support-edge/window scales of `VIS-123`--`VIS-125`: the two previously separate requirements have a large explicit common asymptotic corridor. This is stored because it closes a concrete calibration ambiguity in the active visual experiment, not as a new theorem about zero distribution.

## Boundary and falsification

The bound uses the smooth Riemann--von Mangoldt main term `Nbar`, not the exact staircase `N(t)`. Any later statistic whose unfolding explicitly includes empirical counting fluctuations requires a separate analysis.

The weighted-mass estimate uses only standard local zero-counting magnitude and absolute values. Different normalizations must recompute the final factor of `L_T`; the pointwise coordinate bound `H^2/[pi(T-H)]` itself is normalization-free.

The corridor is asymptotic. At a concrete finite height, the exact chosen `H`, taper, density convention, finite-CUE size, and covariance must be frozen and checked numerically or analytically before source inspection. A formal asymptotic `o(1/L_T)` statement does not certify that a finite window is already in that regime.

If the eventual matched null uses a nonlocal unfolding, adaptive window, or effective-size rule depending on the observed zeros, this calculation no longer certifies the transfer and the corresponding representation must be audited separately.

## Research consequence

`VIS-123` calibrated the support-edge coordinate and continuous finite-CUE ripple, `VIS-124` calibrated Montgomery-weight smoothing, and `VIS-125` calibrated source-window leakage. `VIS-126` now shows that suppressing the source-window artifact need not conflict with freezing the smooth zero density at the window center: a broad mesoscopic height corridor makes both errors smaller than `1/L_T`.

The accepted clue should therefore stop treating smooth Riemann--von Mangoldt density drift as an undifferentiated remaining blocker. The live pre-data gates are now the exact finite-CUE effective-size/arc dictionary, diagonal and compactification conventions, the contribution of counting-function fluctuations beyond the smooth main term, and the joint covariance of the frozen support-edge statistic. Only after those are fixed should arithmetic lower-order terms choose the residual scale and untouched high-zero data be inspected.