# MI-017 — A finite zero edge forces a phase-locked Robin corridor, but even the self-consistent moving endpoint ray is syndetically realizable

**Evidence level:** exact consequence of [RE-112](../../findings/RE-112-finite-zero-edge-forces-power-scale-robin-recovery-corridors.md)--[RE-116](../../findings/RE-116-self-consistent-moving-endpoint-ray-is-syndetically-realized.md). No contradiction with false RH or density theorem for actual selected CA blocks is claimed.

Let `Theta=sup Re(rho)` and suppose `1/2<Theta<1` is attained; write `c=1-Theta`. RE-112--RE-113 replace the scalar recovery envelope by the actual edge phase

`F_Theta(u)=sum_(Re rho=Theta) exp(i Im(rho)u)/rho`.

A genuinely sublinear selected recovery is strictly super-minimal. Any unbounded fixed-constant near-minimal family under `V-Y<=Y` must instead live at the full edge amplitude `h(C) asy Y^(Theta-1)/log Y` and carry an order-one favorable edge phase.

RE-114 adds the reciprocal coordinate

`G_Theta(u)=sum_(Re rho=Theta) exp(i Im(rho)u)/(1-rho)`

and shows that the full attained edge face realizes every fixed admissible mixed ray `bG=(1-b)F` with positive amplitude at bounded logarithmic gaps. Leading-edge Chebyshev/Mertens compatibility is therefore not a spectral obstruction.

RE-115 retunes the adaptive block functional to the exact edge scale. Maximizing

`B_Theta(C)=Y^c log Y (e^(h(C))-1)`

produces a genuine CA tangent with the **moving exponent**

`b_Y=c+1/log Y`.

Along any nondegenerate near-minimal family, the normalized maximum `q` is order one and the edge projections satisfy

`F_Theta(log Y)=c q+o(1)`, `G_Theta(log Y)=Theta q+o(1)`.

At first sight the drifting exponent could still evade the fixed-`b` syndeticity theorem. RE-116 closes exactly that diagonal loophole. Put `J=F+G`. The edge coefficients satisfy `J'=cJ-F`, so at phase `u=log Y`

`K_(c+1/u)(u) = (c+1/u)G(u) - (1-c-1/u)F(u) = J'(u)+J(u)/u = (uJ(u))'/u`.

Thus the self-consistent moving ray is realized precisely at weighted critical points `(uJ(u))'=0`. Uniform almost periodicity and a fixed transverse sign-change cell imply that positive such critical points with `J(u)>=m_0` occur **syndetically** for all sufficiently large `u`. The `1/u` drift is too small to destroy the fixed transversality margin.

The attained-edge frontier has therefore moved beyond ray existence in every natural sense tested so far: scalar edge amplitude, two-coordinate fixed rays, edge-normalized adaptive maxima, and the exact self-consistent moving ray are all spectrally compatible. A closing theorem must control **where the arithmetic CA selector actually lands inside these bounded-gap compatibility windows**, introduce a lower-order source coordinate finer than the leading edge face, or couple recovery geometry to selector placement in a way uniform almost periodicity does not preserve.

**Boundary.** Syndetic spectral compatibility does not show that actual CA selectors hit those phases. The extreme `Theta=1` branch remains the separate unconditional RE-109--RE-111 problem.