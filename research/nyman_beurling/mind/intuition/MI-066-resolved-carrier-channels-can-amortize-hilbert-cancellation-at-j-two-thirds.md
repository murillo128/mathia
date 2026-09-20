# MI-066 — Resolved carrier channels can amortize Hilbert cancellation at the `J^(2/3)` scale

**Evidence level:** exact source-side synthesis from [NB-257](../../findings/NB-257-h-separated-signed-carriers-have-a-sharp-j-two-thirds-hilbert-cost-crossover.md), refining the representation obstruction of NB-255--NB-256. The result concerns one Ford-scale carrier notch before the full Hardy/Nyman destination map.

Requiring carrier centers to be separated at scale `H` successfully removes the microscopic-dipole pathology of NB-256. The translated shells then have disjoint physical support, so the shell-scaled source `L^2` norm is exactly the coefficient `ell^2` norm up to the fixed profile factor. Coefficient geometry is genuinely visible in the synthesized source.

That coercivity is nevertheless not enough to force a divergent Hilbert price. For `K` resolved channels filling an `H`-grid, the minimum source Hilbert cost of imposing an order-one carrier notch at Ford distance `Theta(1/R)` is

`H^(1/2)||h||_2 ~ J/K^(3/2)`, where `J=R/H`.

The sharp crossover is therefore `K~J^(2/3)`. Below it the required Hilbert cost diverges; at the crossover it is only order one, even though the total carrier span remains mesoscopic, `W/R~J^(-1/3)->0`.

The construction is not another unresolved cancellation artifact. Its total variation satisfies `V~J/K` and hence `WV~R`, exactly paying the NB-255 coherence tax, while the `H`-separation makes that variation physically resolvable. The difference is geometric: a Hilbert norm can amortize the required signed displacement over `K` genuinely distinct channels.

Thus **quotienting microscopic dipoles identifies physical source geometry but does not by itself make Ford-scale cancellation expensive in the Hilbert category**. The next load-bearing object must involve more than one interpolation constraint: a family of Ford-scale notches, a whole carrier-band energy, or the actual Hardy-projected destination norm. A transport or `L^1` cost may remain large, but that cannot be substituted for the Hilbert geometry of Nyman--Beurling without a theorem connecting them.

**Boundary.** NB-257 constructs and prices a single carrier notch on the source side. It does not show that the same bounded cost suppresses the positive carrier-band form factor required downstream, survives Hardy projection, or improves the Nyman distance. Conversely it does not rule those possibilities out. The exact conclusion is the `J^(2/3)` Hilbert-cost crossover for resolved scalar channels.