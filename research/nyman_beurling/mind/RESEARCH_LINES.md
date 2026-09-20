# Nyman--Beurling research lines

This file records current mathematical questions for the Nyman--Beurling line. It is a mutable synthesis, not a task queue or history.

## Control the carrier-resonant Ford current of the R-normalized logarithmic derivative

**Linked intuition:** `MI-062-the-critical-ford-mark-is-a-growing-moment-observable`.

NB-230--NB-233 show that population-only control, global pair statistics and unweighted local phase equidistribution do not determine the carrier-width Ford transition. NB-234 identifies the exact nonlinear depth mark and shows that a slowly growing hierarchy of profiled depth--phase moments reconstructs it with factorial accuracy, while every fixed finite hierarchy remains blind in a matched Bellotti-compatible packet.

NB-235 changes representation from abstract growing moments to a classical zeta object. On the critical layer, the unresolved coefficient is a horizontally marked microlocal Landau--Gonek remainder; the shell profile kills the ordinary prime-power diagonal, while black-box smoothing of the global cumulative formula loses the microscopic scale.

NB-236 removes the horizontal-localization tariff itself. Inserting a smooth Ford-depth cutoff into the holomorphic carrier and applying Poincare--Lelong turns the marked zero sum into a signed pairing with `log|zeta|` whose two-edge kernel has bounded `L^1` mass and annihilates harmonic backgrounds.

NB-237 now gives the first-order dual form through `zeta'/zeta`. Distributional Cauchy--Pompeiu/logarithmic-derivative calculus yields the exact Ford-layer pairing with kernel mass `O(1/R)`. After the Ford change of variables, the natural source observable is therefore a microlocal signed average of

`R^(-1) zeta'(s)/zeta(s)`.

This sharper normalization is not free decay. The matched critical packets of NB-231 are exactly resonant with the carrier: pole spacing `asymp 1/R` becomes an integer number of carrier periods, so `M asymp J` pole residues can arrive with the same phase and produce order-one contribution. Generic high-frequency/Riemann--Lebesgue reasoning therefore cannot make the first-order pairing small.

The load-bearing theorem is now more explicit than a generic signed-potential estimate. One needs a deterministic microlocal cancellation statement for the `R`-normalized logarithmic derivative, or an equivalent zero-statistical theorem, that excludes carrier-locked Ford-depth/phase packets while preserving the poles rather than deleting or absolutely estimating them. Averaging over height, removing pole neighborhoods, or forgetting the depth mark changes the problem.

## Keep source resolution, localization tariff, first-order normalization and pole resonance distinct

NB-234--NB-237 separate four currencies that previously appeared entangled. Growing depth--phase moments are one sufficient way to identify the missing source mark. The exact zeta representation is a horizontally marked local zero sum. Poincare--Lelong shows that smooth horizontal localization itself has bounded cost. The logarithmic-derivative representation then shows that the same observable has an `O(1/R)` first-order kernel but can still be order one because the moving pole configuration may resonate at exactly the carrier scale.

Thus **small kernel norm is not cancellation when the source singularities move with the oscillation scale**. The next theorem must control joint pole geometry/sign phase in the particular Ford window, not only the absolute local size of `log|zeta|` or `zeta'/zeta`. Conversely, a successful first-order estimate would attack the exact coefficient without reconstructing the full growing moment hierarchy.

Future work should preserve the coupled Ford geometry explicitly: horizontal depth, microscopic ordinate scale, carrier phase, `R` normalization, pole residues and the final `o(1)` destination. The remaining bottleneck is source-specific decorrelation from the carrier, not the cost of localizing the source.