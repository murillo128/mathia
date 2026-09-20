# MI-066 — Resolved Hilbert channels amortize isolated notches but not a full Ford band at fixed-power span

**Evidence level:** exact source-side synthesis from [NB-257](../../findings/NB-257-h-separated-signed-carriers-have-a-sharp-j-two-thirds-hilbert-cost-crossover.md) and [NB-258](../../findings/NB-258-fixed-power-resolved-carrier-spans-cannot-suppress-a-full-ford-band-at-bounded-hilbert-cost.md), refining NB-255--NB-256. The result concerns the resolved scalar source carrier before the full Hardy/Nyman destination map.

`H`-separation removes the microscopic-dipole pathology of NB-256: translated shells have disjoint physical support, so shell-scaled source `L^2` is coefficient `ell^2` up to the fixed profile factor. NB-257 nevertheless shows that one order-one Ford-scale notch can be spread over `K` resolved channels at minimum source Hilbert cost

`H^(1/2)||h||_2 ~ J/K^(3/2)`.

The sharp one-notch crossover is `K~J^(2/3)`, where the cost is only order one even though the carrier span satisfies `W/R~J^(-1/3)->0`.

NB-258 shows why that superoscillatory freedom does not extend to a whole fixed Ford interval at any fixed exponent gap below the Ford scale. If the shell-Hilbert cost stays bounded and `K<=J^(1-delta)` for fixed `delta>0`, then for some fixed `q=q(delta)` the Ford-rescaled carrier

`C_J(x)=B_lambda(x/R)`

satisfies `||C_J^(q)||_infty=o(1)`. On bounded Ford coordinates it is therefore asymptotically a polynomial of degree `<q` with `C_J(0)=1`. Evaluation at zero is coercive on that finite-dimensional polynomial space, so every fixed interval `I` of positive length has

`liminf int_I |C_J(x)|^2 dx > 0`.

At `K~J^(2/3)` one can take `q=2`: the bounded-cost family is asymptotically affine. The optimal NB-257 notch is exactly the expected linear ramp in the limit—enough to hit one point, not enough to erase an interval.

Thus **isolated interpolation constraints and full carrier-band suppression have different resolved-channel thresholds**. Bounded-cost suppression of a fixed Ford band requires leaving every fixed-power mesoscopic regime, necessarily `K=J^(1-o(1))`. For a filled dictionary this is `W/R=J^(-o(1))`.

**Boundary.** NB-258 is still source-only. It does not prove that the same positive band floor survives the legally required Hardy projection or equals the final Nyman distance, and it does not rule out near-Ford channel counts or structures outside the resolved scalar dictionary. The next obstruction must connect this source-band rigidity to the actual Hardy/Nyman destination rather than substitute an unprojected energy for it.