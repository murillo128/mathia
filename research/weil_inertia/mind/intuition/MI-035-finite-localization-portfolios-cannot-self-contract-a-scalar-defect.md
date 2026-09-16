# MI-035 — Scalar localization self-bootstrap is blocked beyond the recurrence-complexity threshold

**Evidence level:** exact synthesis from [WI-315](../../findings/WI-315-nested-weil-windows-make-vanishing-cap-diagonals-inertia-complete.md) through [WI-320](../../findings/WI-320-short-positive-witness-closes-adaptive-scalar-localization-bootstrap.md).

Once the capped comparison has been reduced to a fixed scalar defect, an exact localization identity does not automatically create a bootstrap. If the only estimate supplied for every localized source term is the same scalar bound `Q(h)>=-c||h||^2`, a uniform improvement to `c-kappa` would require the localization correction to contribute a uniformly favorable amount on **every** test vector after the localizer is chosen.

WI-317 proves that fixed finite portfolios cannot do this. WI-318 extends the recurrence obstruction to arbitrary adaptive unit-window families with uniformly bounded total `H^1`. WI-319 then finds the exact complexity boundary of that particular falsifier: on high-frequency carriers the continuous defect still vanishes when localizer second-moment energy is `o(t^2/log t)`, while an explicit resonant family at `Theta(t^2/log t)` can produce an order-one correction and defeat the recurrence witness.

The crucial correction from WI-320 is that **defeating the recurrence witness does not reopen scalar self-bootstrap**. The source-exact defect has an archimedean kernel coefficient `K(a)` that is strictly positive for `0<a<h_0`, with `h_0=log rho<log 2` and `rho^3-rho-1=0`. Choose one nonnegative smooth `f` supported in an interval of diameter `d<h_0`. Then its autocorrelation `H_f(a)` is nonnegative and vanishes for `a>=d`, so every arithmetic term at lag `log n>=log 2` disappears exactly.

For an arbitrary normalized real admissible multiwindow localizer, its aggregate autocorrelation is an inner product of a translated unit vector with itself, hence `R(a)<=1`. On the short witness,

`E_r(f)=int_0^d (1-R_r(a)) K(a) H_f(a) da >= 0`

for **every** localizer `r`, before any infimum or adaptive selection is taken. But a strict scalar contraction would require the infimum of this defect to be uniformly negative on every `f`. The same fixed short bump therefore blocks the complete admissible smooth multiwindow class with no derivative, frequency, cardinality or compactness bound.

The correct interpretation of WI-319 is now narrower: `t^2/log t` is the sharp price for escaping one high-carrier recurrence falsifier, not a complexity threshold for the architecture itself. Crossing it changes the analytic behavior of that witness but adds no new arithmetic information, and WI-320 supplies a different source-exact witness that remains fatal at arbitrary complexity.

This sharpens the information accounting. Portfolio cardinality, adaptivity and frequency budget are representation resources. **A stronger localized premise is an information resource.** Only the latter can escape the current scalar-feedback no-go without changing the exact decomposition. Viable routes include a localized arithmetic estimate genuinely stronger than the global floor, vector/matrix/mode/prime-dependent state retained between pieces, a different source-exact correction with different sign geometry, or direct coercivity/inertia control.

**Boundary.** WI-320 applies to the smooth real source-exact multiwindow identities of the current localization architecture and to bootstrapping the *same* scalar lower semibound. It does not say localization is useless, does not forbid stronger local arithmetic inputs or non-scalar state, and does not prove Weil positivity. The short witness is prime-free because `h_0<log2`; if the decomposition or source geometry changes, its sign argument must be re-audited.
