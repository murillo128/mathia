# MI-075 — Vertical localization conserves a linear defect-area budget

**Evidence level:** exact translated-Blaschke identity and sharp finite-total-variation coverage theorem from [WI-411](../../findings/WI-411-vertical-translations-obey-height-area-budget.md), continuing the classical half-plane factorization ledger of WI-409--WI-410.

For an off-critical zero `rho=1/2+d+i gamma`, `0<d<1/2`, and a translated half-plane probe `s=1/2+a+ib`, the single-zero Blaschke charge is

`q_(a,b)(gamma,d) = (1/2) log(((gamma-b)^2+(a+d)^2)/((gamma-b)^2+(a-d)^2)) >= 0`.

Vertical translation can make this charge locally `O(d)` by choosing `b` near the target ordinate, apparently avoiding the `d/gamma` pointwise attenuation of the best real-axis scale in WI-410. WI-411 shows that the gain is localization, not free amplification. The exact area law is

`int_R q_(a,b)(gamma,d) dgamma = 2 pi min(a,d) <= 2 pi d`,

and is independent of `b`. Moving the center only transports a fixed amount of single-defect sensitivity along the height axis.

This conserved area immediately prices arbitrary finite signed or complex mixtures. If `nu` is a measure on `(a,b)` with total variation `M`, then

`int_R |Q_nu(gamma,d)| dgamma <= 2 pi d M`.

Therefore `|Q_nu(gamma,d)|>=c d` on a set of height measure `L` forces `M>=cL/(2 pi)`. In particular, covering a dyadic interval `[T,2T]` with a height-uniform linear-depth response costs `Omega(T)` coefficient mass. WI-411 also gives a matching `O(T)` construction, so the required order is exactly `Theta(T)` inside this linear mixture architecture.

The useful distinction is between **local defect sensitivity** and **coverage budget**. A translated probe can be excellent at one chosen ordinate, yet a source-independent family that must be ready for an unknown defect anywhere in an expanding interval has to pay linearly for the interval it covers. This is the height analogue of a localization resource whose integral mass, rather than its peak value, is the invariant currency.

The remaining escape is correspondingly narrower. A growing translated family matters only if its actual source-side norm can afford the `Theta(T)` coefficient budget; a sparse adaptive family matters only if its target ordinates can be selected non-circularly from source information; and a count-coercive mechanism must still address arbitrarily shallow depths, since every charge remains proportional to `d`. Infinite-total-variation limits, nonlinear functionals and different explicit-formula observables are outside this budget theorem.

**Boundary.** The area identity is an exact statement for the Burnol--Kunik/Blaschke translated half-plane family, and the coverage theorem uses finite coefficient total variation and Lebesgue-measure height coverage. It does not bound an arbitrary discrete measure-zero target set, identify coefficient TV with every possible arithmetic source norm, prove that a `Theta(T)` budget is unaffordable in all zeta applications, or rule out Carleman/distributional limits or nonlinear constructions. No RH conclusion is obtained.