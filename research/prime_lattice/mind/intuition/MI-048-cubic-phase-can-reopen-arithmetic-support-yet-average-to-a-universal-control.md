# MI-048 — Cubic phase can reopen arithmetic support yet average to a universal control

**Evidence level:** exact continuation-kernel synthesis from [PL-401](../../findings/PL-401-cubic-transition-even-gap-gallagher-collapse.md), extending the subcubic phase obstruction of PL-399--PL-400. The Gallagher-averaged conclusion is for the classical pair singular-series model, not an asymptotic for the actual von Mangoldt pair sum.

The parity mismatch of PL-400 is not permanent. Retaining the next incomplete-gamma transition phase gives, for `d=o(r^(1/2))`, a cubic rotation `exp(-i pi d^3/(6r))`. At the transition scale `d~c r^(1/3)`, this rotation makes the real same-sign channel on even gaps generically order `1/d` again. The analytic phase and the parity class carrying prime-pair bulk can therefore overlap.

Reopening the support is only the first gate. Weighting this cubic channel by the Hardy--Littlewood pair singular series and averaging gaps on the natural `r^(1/3)` window uses only Gallagher's first-moment law. The leading contribution converges to a universal sine integral, with full-window value `-1/(6 sqrt(2))`. Replacing the singular series by the parity-only control `2*1_(2|d)` gives the same limit.

Thus **phase alignment can be necessary without being arithmetically discriminating**. A channel may finally live on the correct parity sector and still erase the arithmetic fluctuations that distinguish the prime source once the chosen aggregation reduces them to their mean. The matched control must therefore be applied after the mesoscopic averaging, not just to the pointwise transition coefficient.

The next meaningful quantity has to retain information beyond the first moment: fluctuations of the singular series, genuine `Lambda(r)Lambda(r+d)` correlation errors, or a coupled gap/height observable whose weighting does not collapse to parity density. Any transfer from the singular-series model to actual prime pairs also needs a uniform theorem strong enough for the `r`-dependent cubic kernel.

**Boundary.** PL-401 does not prove an averaged Hardy--Littlewood formula for the actual continuation sum, nor an RH implication. It shows exactly that the first canonical cubic-window singular-series aggregate is reproduced by a nonarithmetic parity control. Other channels, projections or fluctuation-sensitive statistics remain open.