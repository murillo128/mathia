# MI-075 — Logarithmic Ford mesh mass does not force diagonal quadratic energy

**Evidence level:** exact/asymptotic synthesis from [NB-268](../../findings/NB-268-logarithmic-ford-mesh-mass-can-coexist-with-vanishing-diagonal-quadratic-energy.md), interpreted against the logarithmic aggregate coercivity of NB-267.

NB-267 forces `ell^1` mesh response `sum |D_n| >= c m` on an `O(log K)` resolved window containing `N asymp m log K` mesh sites. That statement alone cannot yield an order-one damped quadratic quantity: the sharp generic conversion gives only

`e^(-2u) ||D||_2^2 >= const/(m log K)`

at the live depth `e^(-u) asymp 1/m`.

NB-268 shows this loss is realizable by a legal bounded-cost carrier, not just an artifact of Cauchy--Schwarz. For the uniform positive carrier `c_j=1/K`, the mesh profile converges to the sinc-type transform

`G_0(s)=exp(is/2) 2 sin(s/2)/s`,

whose squared modulus is integrable. Since the mesh spacing is `asymp 1/m`, one has `sum |D_n|^2 asymp m` on the logarithmic window, and therefore

`e^(-2u) sum |D_n|^2 asymp 1/m -> 0`,

while the same family still satisfies the `Omega(m)` aggregate linear response required by NB-267.

Thus logarithmic Ford-mesh `ell^1` coercivity and target-side quadratic coercivity are different mechanisms. A bridge to the Hardy/Nyman distance cannot be obtained merely by converting aggregate amplitude to diagonal sample energy. It must use structure absent from that diagnostic: the actual Gram kernel/off-diagonal terms, projection-forced concentration, or arithmetic information about the true zero set.

The decisive next calculation is the exact Hardy/Nyman projected quadratic form on this uniform carrier. If it also tends to zero, the carrier is a genuine escape candidate from the source-side obstruction; if it stays bounded below, the responsible off-diagonal Gram contribution identifies the missing target-side coercivity mechanism.

**Boundary.** NB-268 does not show that the true Hardy/Nyman norm of the uniform carrier vanishes and does not place zeta zeros on the matched mesh. It separates diagonal quadratic energy from the established linear aggregate obstruction; it does not refute NB-267.