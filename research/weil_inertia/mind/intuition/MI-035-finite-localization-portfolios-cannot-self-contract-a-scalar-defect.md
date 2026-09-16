# MI-035 — Scalar localization self-bootstrap survives neither complexity nor finite channel enrichment

**Evidence level:** exact synthesis from [WI-315](../../findings/WI-315-nested-weil-windows-make-vanishing-cap-diagonals-inertia-complete.md) through [WI-321](../../findings/WI-321-hilbert-valued-channelization-cannot-contract-scalar-weil-semibound.md).

Once the capped comparison has been reduced to a scalar defect, an exact localization identity does not automatically create a bootstrap. If every localized source term receives only the same premise `Q(h)>=-c||h||^2`, a uniform improvement to `c-kappa` would require the localization correction to contribute a uniformly favorable amount on **every** test vector after the localizer is chosen.

WI-317 proves that fixed finite portfolios cannot do this. WI-318 extends the recurrence obstruction to arbitrary adaptive unit-window families with uniformly bounded total `H^1`. WI-319 then finds the exact complexity boundary of that particular falsifier: on high-frequency carriers the continuous defect still vanishes when localizer second-moment energy is `o(t^2/log t)`, while resonant families at `Theta(t^2/log t)` can defeat the recurrence witness.

WI-320 shows that defeating that witness does not reopen the architecture. The source-exact defect has an archimedean coefficient `K(a)>0` for `0<a<h_0`, where `h_0=log rho<log2`. Choose one nonnegative smooth `f` with support diameter below `h_0`. Its autocorrelation is nonnegative and vanishes before the first arithmetic lag, so every prime-power term disappears exactly. For every normalized real multiwindow localizer, its aggregate autocorrelation satisfies `R(a)<=1`, hence the defect on this same `f` is nonnegative. No derivative, frequency, cardinality or compactness budget remains to tune.

WI-321 removes the next representational escape. Let `G` be a normalized finite-dimensional complex Hilbert-valued window and `R_G(a)` its autocorrelation. The exact source identity becomes

`E_G(f)=continuous/arithmetic sums of Re((1-R_G(a)) h_f(a))`.

On the same short real nonnegative witness, `h_f(a)` is real nonnegative and all arithmetic lags vanish. Translation Cauchy--Schwarz gives `|R_G(a)|<=1`, so

`Re((1-R_G(a))h_f(a)) = (1-Re R_G(a)) h_f(a) >= 0`.

Thus complex phases, any finite number of auxiliary channels and arbitrary unitary mixing do not help if the localized form is only the diagonal Hilbert-space amplification of the scalar Weil form and the same scalar semibound is applied componentwise.

The reusable distinction is now sharper: **representation dimension and information dimension are different resources**. A vector of scalar copies has more coordinates but the admissible set is still a Cartesian product of the same scalar premise. The short prime-free witness is insensitive to how those copies are mixed, so no strictly stronger scalar constant can emerge.

A genuine non-scalar escape has to change the propagated constraint itself: a matrix lower bound with cross-channel terms, a prime- or mode-dependent state, a source relation coupling channels, or another exact decomposition whose correction has different sign geometry. Localization may organize such information, but it cannot manufacture it from repeated scalar copies.

The interpretation of WI-319 remains local to its witness: `t^2/log t` is the price for defeating one recurrence argument, not a threshold beyond which scalar self-bootstrap becomes possible. WI-320--WI-321 block the architecture at arbitrary real-window complexity and after finite complex Hilbert-valued enrichment.

**Boundary.** WI-321 covers finite-dimensional complex channelizations whose form is the diagonal amplification of `Q` and whose only lower input is the same scalar semibound on each component. It does not rule out genuinely coupled matrix estimates, prime-dependent admissible sets, source-breaking localizations or a different coercivity/inertia mechanism. None of these no-go results proves Weil positivity.
