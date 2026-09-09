# VIS-127 — a growing hard zeta window cannot fit one finite-CUE circle at logarithmic matrix size

## Claim

Let

`L_T = log(T/(2*pi))`

and use the local unfolding from `VIS-123`--`VIS-126`. A physical zero window of length `H=H(T)` then has unfolded length

`M = H L_T/(2*pi)`.

For `CUE_N`, the ordinary unfolded eigenangle coordinate

`x = N theta/(2*pi)`

makes the **entire circle** have unfolded circumference `N`. Therefore a connected, non-wrapping CUE arc that is meant to represent the same source window must satisfy the exact capacity condition

`M <= N`,

or equivalently

`H <= 2*pi*N/L_T`.

Consequently, any finite-CUE matching with

`N/L_T -> rho in (0,infinity)`

can represent only physical windows with asymptotic length at most `2*pi*rho` as a single non-wrapping arc. In particular it is incompatible with the hard-window leakage regime from `VIS-125`,

`H/log M -> infinity`,

because that condition forces `H -> infinity` and hence

`M/N = H L_T/(2*pi N) -> infinity`.

Trying to repair the capacity failure by increasing the CUE dimension does not preserve the edge asymptotic already used in `VIS-123`. To fit the growing hard window one needs

`N/L_T >= H/(2*pi) -> infinity`,

whereas the fixed centered support-edge coordinate `v` in `VIS-123` satisfies

`tau = (N/L_T) v`.

For fixed nonzero `v`, the required enlarged-circle regime therefore sends `|tau| -> infinity`; it leaves the fixed-`tau` finite-CUE edge asymptotic that produced the logarithmic ripple control.

Thus the three requirements

1. one connected non-wrapping arc of a single `CUE_N` circle;
2. a growing hard source window strong enough to make the rectangular leakage `o(1/L_T)` by `H/log M -> infinity`;
3. the logarithmic-size/fixed-`tau` edge regime `N/L_T -> rho in (0,infinity)` used by the current support-edge calibration;

cannot hold simultaneously.

**Evidence/status:** `EXACT-DERIVED + MODEL-COMPATIBILITY OBSTRUCTION + NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

This does not rule out finite-CUE local statistics, a smooth bounded window/taper, a stationary sine-kernel/CUE bulk null, a multi-window ensemble, or a separately derived large-`tau`/large-`N` transfer. It rules out only the literal single-circle growing-hard-arc implementation of the currently calibrated null.

## 1. The unfolded CUE circle has finite capacity

For a unitary matrix of dimension `N`, eigenangles live modulo `2*pi`. Under the standard mean-spacing unfolding

`x=N theta/(2*pi)`,

a full turn changes `x` by exactly `N`. Hence a connected arc without wrap has unfolded length at most `N`.

The zeta-side local unfolding uses density `L_T/(2*pi)`. A physical interval of length `H` therefore contains unfolded length

`M=H L_T/(2*pi)`

in the stationary approximation of `VIS-125`. Matching that interval to one literal CUE arc forces `M<=N`. No probabilistic or asymptotic input is needed for this inequality; it is only the compatibility of the two coordinate dictionaries.

If `N/L_T -> rho`, then

`M/N -> H/(2*pi*rho)`

whenever `H` has a finite limit, and the ratio diverges whenever `H->infinity`. Thus a fixed-ratio logarithmic CUE dimension supplies only a bounded physical arc length.

The effective finite-matrix models used in the Riemann-zero finite-size literature provide concrete examples of precisely this logarithmic regime. Bogomolny, Bohigas, Leboeuf, and Monastra (2006) derive for nearest-neighbor spacing corrections

`N_eff = log(E/(2*pi))/sqrt(12 Lambda)`

with a fixed positive constant `Lambda`. That particular effective size is not asserted to be the correct one for the present Montgomery statistic; it simply confirms that `N=Theta(L_T)` is a standard finite-CUE scaling rather than an artificial assumption introduced by this finding.

## 2. The hard-window leakage gate forces the capacity ratio to diverge

`VIS-125` showed that a rectangular source window has support-edge leakage

`(log M)/(pi H L_T) + O(1/(H L_T))`.

To make this contribution `o(1/L_T)` by increasing the hard physical window, its stated sufficient regime is

`H/log M -> infinity`.

Because `M=H L_T/(2*pi)` and `L_T->infinity`, a bounded `H` would make `H/log M -> 0`. Hence the leakage gate necessarily has `H->infinity`.

If simultaneously `N/L_T -> rho` with finite positive `rho`, then

`M/N = [H/(2*pi)] [L_T/N] -> infinity`.

Eventually `M>N`, contradicting the single-arc capacity condition. This is not a small boundary correction: the desired source window eventually contains arbitrarily many CUE circumferences in unfolded units.

Periodically wrapping that interval around the same circle is not an equivalent fix. It identifies differences separated by integer multiples of the CUE circumference and changes the pair-overlap geometry that produced the `Q_M` window kernel in `VIS-125`. Any such periodized model needs a new derivation rather than being called the same matched source window.

## 3. Enlarging the circle changes the support-edge regime

One could instead choose `N` large enough that `M<=N` even while `H->infinity`. But then necessarily

`N/L_T >= H/(2*pi) -> infinity`.

`VIS-123` relates the centered zeta support-edge coordinate

`v=(alpha-1)log(T)+log(2*pi)`

to the continuous CUE edge variable by

`tau=(N/L_T)v`,

where `k=N+tau`. Its quoted finite-CUE logarithmic ripple is a fixed-real-`tau` asymptotic.

Therefore an enlarged circle that tracks the growing hard source window sends `tau` out of that regime for every fixed nonzero `v`. The previously calibrated edge formula cannot simply be reused after changing `N` this way. One would need either a new joint asymptotic in which `tau` grows with `N/L_T`, or a different source/null representation.

This is the second half of the obstruction: increasing `N` repairs circle capacity only by invalidating the fixed-`tau` finite-size edge approximation that motivated the current low-dimensional edge control.

## 4. Prior-art and novelty assessment

The circular geometry of `CUE_N`, its mean-spacing unfolding, and finite-size CUE models for Riemann-zero statistics are standard. The relevant finite-size literature already anchored in `research/visual_exploration/SOURCES.md` includes Forrester--Mays (2015) and Bornemann--Forrester--Mays (2017). Bogomolny, Bohigas, Leboeuf, and Monastra, **On the spacing distribution of the Riemann zeros: corrections to the asymptotic result**, *Journal of Physics A* 39 (2006), 10743--10754, DOI `10.1088/0305-4470/39/34/010`, gives the explicit logarithmic effective dimension above.

No novelty is claimed for any of those ingredients, for the fact that one circle has circumference `N` after unfolding, or for ordinary window/periodization effects. The Mathia-specific result is the compatibility check between three already-adopted control requirements: the `VIS-125` hard-window leakage corridor, the `VIS-123` fixed-`tau` support-edge scaling, and a literal one-circle arc null. Their conjunction is empty.

A targeted literature search found the standard finite-size CUE/Riemann-zero program and explicit `N_eff=Theta(log T)` models, but no need for a new general theorem: the obstruction itself is an elementary consequence of the coordinate dictionaries. It should therefore be treated as a negative design control, not as a new random-matrix result.

## Boundary and falsification

The capacity statement concerns a **single connected non-wrapping CUE arc**. It does not say that a finite-CUE kernel cannot model local zero correlations when the source window is larger than one effective circumference; local statistics may be assembled through a stationary limit, multiple samples, or another ensemble construction if that construction is derived consistently.

The argument also does not choose the correct `N(T)` for Montgomery's weighted finite-height statistic. If a future source/null derivation yields `N/L_T -> infinity`, the first capacity contradiction disappears, but the `VIS-123` fixed-`tau` edge asymptotic must then be replaced or rescaled as shown above. If it yields `N/L_T -> 0`, the capacity problem is stronger.

A compactly supported smooth taper of bounded physical width is not excluded. For such a design, the single-circle geometric gate is simply that its effective support fit within `2*pi N/L_T`; `VIS-125` already shows that a suitable taper can remove the logarithmic rectangular-window penalty without forcing `H->infinity`.

## Research consequence

The accepted Montgomery support-edge clue should no longer treat “grow a hard local window and match it to one finite CUE arc” as a neutral implementation option in the `N=Theta(L_T)` edge regime. That route is geometrically inconsistent before any zero data are inspected.

The cleanest remaining design is to freeze a sufficiently regular bounded physical taper whose support fits the chosen finite-CUE geometry, then derive its exact finite-CUE/window covariance and effective-size transfer. If a growing window is scientifically necessary, the null should instead be formulated as a stationary/local bulk process or another explicitly derived multi-sample construction; it cannot be obtained by wrapping the growing source interval around one logarithmic-size CUE circle while retaining the current fixed-`tau` edge calibration.

This finding stops at that compatibility boundary. Choosing the taper or constructing the alternative stationary/multi-sample null is the next mathematical question rather than an extension of the same result.