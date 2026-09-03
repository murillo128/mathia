# Monotone Grosswald–Schnitzer integer rigidity profile

![Log-log plot of the exact one-step phase-slope threshold and its asymptotic](grosswald-schnitzer-rigidity-profile.png)

## Question

`PL-127` turns the critical-line reflection phase into an additive rigidity diagnostic for Grosswald–Schnitzer deformations. For integer generators it defines the low-scale certificate through

`delta(X) = min_{p prime, p<=X} [g(p)-g(p+1)]`,

where `g(x)=log(x)/(sqrt(x)-1)`.

The visual question was whether this minimum hides irregular prime-scale dips, or whether the individual one-step thresholds lie on a simple monotone resolution profile that can be formalized.

## Construction

Define

`h(x)=g(x)-g(x+1)`.

The figure plots the exact values `h(p)` at every prime `11<=p<=100000` on logarithmic axes. It also plots the large-`p` asymptotic from `PL-127`,

`((1/2)log p - 1) p^(-3/2)`.

The first few primes are omitted from the asymptotic overlay because its leading coefficient changes sign below the range where it is a useful approximation; the exact `h(p)` remains positive there. Prime sampling is used only to display the integer-deformation thresholds. No smoothing or fitted envelope is applied.

The render was produced at `1800 x 1080` and palette-quantized after plotting to reduce repository size without changing coordinates or sampled values.

## Observation

The exact prime thresholds form a smooth, strictly descending curve. No local prime-gap-induced dips or reversals appear. The asymptotic approaches the exact profile rapidly as the prime scale grows.

This suggests that the minimization in `delta(X)` may be artificial: the weakest detectable one-step integer deformation below a cutoff appears always to occur at the largest prime below that cutoff.

## Robustness

The visual impression is replaced by an exact control in [[research/visual_exploration/findings/VIS-007-grosswald-schnitzer-rigidity-profile-monotone.md]]. That finding proves `g''(x)>0` for every `x>1`. Since `g` is also strictly decreasing, `h(x)>0` and

`h'(x)=g'(x)-g'(x+1)<0`.

Thus monotonicity holds on the entire real interval, not just on the displayed primes. As a numerical audit, `h(p)` was additionally evaluated at every prime through `200000` and was strictly decreasing throughout.

The final PNG passed a complete Pillow decode check using `Image.verify()`, followed by reopen and `Image.load()` after quantization.

## Research consequence

The image led to the exact refinement [[research/visual_exploration/findings/VIS-007-grosswald-schnitzer-rigidity-profile-monotone.md]]: if `P_X` is the largest prime not exceeding `X`, then the `PL-127` cutoff is exactly `delta(X)=g(P_X)-g(P_X+1)`.

The scalar threshold still does not recover the complete deformation pattern. That residual question is handed to Prime Lattice in [[research/prime_lattice/clues/CLUE-grosswald-schnitzer-phase-fingerprint.md]].