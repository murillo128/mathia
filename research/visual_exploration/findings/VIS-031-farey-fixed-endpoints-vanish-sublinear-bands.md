# VIS-031 — every fixed Farey endpoint hierarchy vanishes from sublinear Dirichlet bands

## Claim

Let

`0=x_0<x_1<...<x_N=1`

be the Farey sequence of order `n`, with `N=sum_(q<=n) phi(q)` gaps and discrepancy

`D_k=x_k-k/N`, `1<=k<=N-1`.

Fix `Y>1`. Define the reflected fixed-endpoint component `D^(Y)` by retaining `D_k` only at Farey ranks with `x_k<=Y/n` or `x_k>=1-Y/n`, and setting the interior to zero. For the orthonormal Dirichlet sine basis from `VIS-027`,

`v_m(k)=sqrt(2/N) sin(pi m k/N)`,

write `d_m^(Y)=<D^(Y),v_m>`.

Then, for fixed `Y`, uniformly in positive integers `r`,

`|d_(2r)^(Y)| = O_Y(r/n^2)`.

Consequently, for every integer cutoff `q=q(n)` within the available even modes,

`n sum_(1<=r<=q) |d_(2r)^(Y)|^2 = O_Y((q/n)^3)`.

In particular, for every sublinear band `q_n=o(n)`,

`n sum_(1<=r<=q_n) |d_(2r)^(Y)|^2 -> 0`.

For `q_n=floor(n^alpha)` with any fixed `0<alpha<1`, the bound is

`O_Y(n^(-3(1-alpha)))`.

Thus the deterministic fixed-`nx` endpoint hierarchy identified in `VIS-028` and `VIS-029` can generate the natural `r=Theta(n)` modal scale while contributing asymptotically nothing, at the same `n`-scaled energy normalization, to every even Dirichlet band whose mode cutoff grows strictly slower than `n`.

**Evidence/status:** `EXACT-DERIVED SPECTRAL LOCALIZATION + ENDPOINT-NULL CONTROL + FINITE NUMERICAL VALIDATION + NO-NOVELTY-CLAIM`.

No nonzero asymptotic for the full Farey low-mode spectrum, stronger Franel–Landau criterion, or RH implication is claimed.

## Derivation

`VIS-029` gives, for every fixed `Y`,

`R_n(Y)=#{x_k:0<x_k<=Y/n}=nK(Y)+O_Y(1)=O_Y(n)`

and uniformly on that endpoint window

`D_k=O_Y(1/n)`.

Farey reflection gives the identical right endpoint with opposite discrepancy, so odd Dirichlet modes vanish exactly as in `VIS-027`. For an even mode `m=2r`, pairing the two endpoints yields

`d_(2r)^(Y) = 2 sqrt(2/N) sum_(k<=R_n(Y)) D_k sin(2 pi r k/N)`.

Using `|sin theta|<=|theta|`,

`|d_(2r)^(Y)|`
` <= 4 pi r sqrt(2/N) N^(-1) sum_(k<=R_n(Y)) k |D_k|`.

Because `R_n(Y)=O_Y(n)` and `|D_k|=O_Y(1/n)`,

`sum_(k<=R_n(Y)) k|D_k| = O_Y(n)`.

The classical summatory-totient asymptotic gives `N=Theta(n^2)`, hence `sqrt(N)=Theta(n)`. Substitution gives

`|d_(2r)^(Y)|=O_Y(r/n^2)`.

Squaring and summing through `q` gives

`n sum_(r<=q)|d_(2r)^(Y)|^2`
` <= O_Y(n/n^4) sum_(r<=q) r^2`
` = O_Y(q^3/n^3)`.

This proves the stated sublinear-band vanishing without subtracting, fitting, or numerically estimating the endpoint profile.

## Relation to the `r=Theta(n)` endpoint scale

There is no contradiction with `VIS-028` or `VIS-029`. Those findings show that a fixed endpoint window has rank width `Theta(n)` inside a sequence with `N=Theta(n^2)` gaps, and therefore places nontrivial energy on modes `r=Theta(n)`. The present estimate describes the opposite edge of the same scale separation: when `r/n->0`, the sine kernel varies too slowly across a `Theta(n)`-rank endpoint layer to see more than its first small-angle moment.

Equivalently, the continuum transform in `VIS-029` is forced to vanish at the origin at least linearly. The `r/n` collapse and the sublinear-band null are therefore complementary consequences of endpoint localization rather than competing interpretations.

This gives a non-circular control that `VIS-030` makes especially useful. One need not remove an ever-growing number of endpoint layers, which would progressively subtract a normalized-totient Riesz/Möbius channel. A pre-registered sublinear band automatically suppresses **every fixed** endpoint hierarchy asymptotically while leaving the full Farey discrepancy untouched.

## Finite validation and visual check

The paired visualization `../visualizations/farey-endpoint-sublinear-band-decoupling.md` evaluates the exact Farey discrepancy rather than a fitted continuum profile. It fixes the explicit sublinear choice `q=floor(sqrt(n))` and shows both cutoff robustness across `Y=2,4,10` and the finite separation between the `Y=10` endpoint component and the complete Farey discrepancy.

At that square-root cutoff, the endpoint values for `Y=10` are approximately

`0.08723, 0.09495, 0.05201, 0.02531, 0.01045`

for `n=100,200,400,800,1600`. The corresponding full-Farey band values are approximately

`0.09800, 0.15173, 0.09568, 0.06603, 0.05507`.

These full-Farey values are finite diagnostics only; no nonzero limit, exponent, or monotonic law is inferred from them.

The endpoint decay is not specific to `Y=10`. At `q=floor(sqrt(n))` and `n=200,400,800,1600`, the scaled endpoint energies are approximately

`0.00429, 0.00154, 0.000527, 0.000190` for `Y=2`,

`0.02882, 0.01120, 0.00411, 0.00152` for `Y=4`, and

`0.09495, 0.05201, 0.02531, 0.01045` for `Y=10`.

The theorem, not this finite trend, establishes the fixed-`Y` asymptotic null.

## Prior art and novelty assessment

The ingredients are classical. Farey endpoint discrepancy and the summatory-totient normalization are already anchored in `SOURCES.md` through Dress and the endpoint/rank literature used in `VIS-028` and `VIS-029`; the Dirichlet sine decomposition is the standard path-Laplacian basis classified in `VIS-027`. Broader Fourier treatments of Farey structures also exist.

No novelty is claimed for the inequality or for localization implying low-frequency suppression. The durable Mathia contribution is its use as an exact **control boundary** for the active Farey multiscale question: fixed endpoint layers can be excluded from a whole asymptotic spectral regime without subtracting arithmetic-bearing endpoint data.

## Boundary conditions and falsification

The result requires `Y` to be fixed while `n->infinity`. It does not cover `Y=Y(n)` growing with Farey order. `VIS-030` shows why that distinction is substantive: enlarging the endpoint window progressively exposes a normalized-totient Riesz mean with an explicit Möbius decomposition and zeta-ratio Dirichlet series.

The result also does not say that the **full** Farey discrepancy has nontrivial sublinear-band energy. The full band may itself decay, may be controlled by the classical Franel–Landau/Möbius scalar channel, or may be reproduced by stronger matched nulls. This finding removes only the entire family of fixed-`nx` endpoint hierarchies as a possible source of a surviving sublinear-band effect.

Odd modes remain exactly zero from Farey reflection and therefore carry no discriminating information. Any useful next test should use the surviving even modes and still compare against reflection-preserving same-gap or stronger controls.

A material falsification would require failure of the fixed-`Y` rank/amplitude bounds from `VIS-029`, the reflection pairing from `VIS-027`, or the small-angle sine bound used above.

## Research consequence

The proposed Farey handoff

`research/farey_discrepancy/clues/CLUE-farey-gap-order-bridge-suppression.md`

can now use a cleaner endpoint-safe test. Pre-register one or more sublinear cutoffs such as `q_n=floor(sqrt(n))` or `q_n=floor(n^(2/3))` and analyze the full Farey even-mode energy or a cross-band statistic without subtracting endpoint layers. Any effect that remains non-negligible at the corresponding normalization cannot be generated by any fixed-`Y` endpoint hierarchy.

That would still not identify an arithmetic mechanism. A surviving signal must separately defeat reflection-preserving same-gap controls, stronger local-order controls, and collapse to the known Franel–Landau/Möbius scalar channel before it can be interpreted as genuinely interior Farey organization.
