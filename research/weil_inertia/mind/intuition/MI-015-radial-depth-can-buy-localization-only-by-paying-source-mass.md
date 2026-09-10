# MI-015 — Density matching turns the count--depth tariff into a same-interval screening obstruction

**Evidence level:** exact count--depth inequalities plus local Riemann--von Mangoldt and zero-free-region comparison through WI-232

## Core intuition

Radial depth and local screen count form one source ledger. When a bow is vertically spaced to consume the actual local mean zero density, there is almost no same-interval count reservoir left: only `O(log T)` excess labels remain. The WI-231 tariff then converts a fixed-power bow size directly into macroscopic horizontal depth.

This closes a substantial local escape. Above the quarter-power scale, and at the calibrated quarter endpoint, the required same-interval depth is incompatible with the critical strip/zero-free region.

## Strongest justified principle

WI-227--WI-231 establish the general tariff: a screen that avoids physical localization must move source mass radially outward, and first-harmonic cancellation requires `R cosh(a_max)` to carry order-`M` mass. Existing global density and pair/multiplicity inputs did not control the simple-zero branch in the needed local normalization.

WI-232 chooses the density-matched spacing `Delta=4pi/log(T_0/2pi)`. Riemann--von Mangoldt then gives `N(I)-2m=O(log T)` for `m=T^{theta+o(1)}`, `theta<1/2`, so any complementary same-interval screen has `R=O(log T)`. The tariff forces `a_max>=log m-log log T+O(1)`, equivalently `beta_max-1/2>=2theta-o(1)`. For every fixed `theta>1/4` this eventually leaves the critical strip; at `theta=1/4` with polylogarithmic precision, the Vinogradov--Korobov zero-free region excludes the required near-1 zero.

## Program consequence

Stop treating a density-matched local screen as a generic surviving loophole on the quarter-power-and-above range. Quantify the remaining alternatives: how far in ordinate a nonlocal screen must reach, how much spacing surplus is needed to create a usable count reservoir, or whether the explicit prime/source side can cancel the harmonic without introducing an equivalent mass bill.

## Counterevidence / boundary

WI-232 does not rule out bows below the quarter scale, arbitrary `T^{1/4+o(1)}` endpoint distortions, nonlocal screens, density-surplus spacings, or prime-side cancellation. It is a theorem about the same vertical interval under density matching, not a contradiction to all off-line configurations.

## Epistemic status

**Exact conversion of density matching into a local screening no-go for fixed powers above one quarter and a calibrated quarter endpoint; the remaining screening mechanisms are explicitly nonlocal or source-side.**

## Falsification criterion

Construct a same-interval density-matched screen in the stated range violating the WI-231/232 count--depth bound, or show that the local zero-count remainder can exceed `O(log T)` under the same hypotheses.