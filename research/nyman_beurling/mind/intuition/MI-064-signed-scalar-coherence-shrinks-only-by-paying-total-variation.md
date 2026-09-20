# MI-064 — The `WV` coherence bound is worst-case, not a physical total-variation tariff

**Evidence level:** exact source-side synthesis from [NB-254](../../findings/NB-254-positive-scalar-carrier-mixtures-have-a-compulsory-coherence-window.md), [NB-255](../../findings/NB-255-signed-scalar-carriers-pay-a-total-variation-coherence-tax.md), and the representation-degeneracy refinement [NB-256](../../findings/NB-256-microscopic-dipoles-can-inflate-signed-total-variation-without-buying-carrier-cancellation.md), interpreted inside the Ford-scaled carrier framework of NB-245--NB-253.

For a signed or complex shell mixture supported in a carrier span `W`, normalize by its actual Euler return at `sigma_X=1+r/X`. After absorbing that weight, let `lambda` be the resulting complex measure with `lambda(R)=1` and total variation

`V=||lambda||_TV >= 1`.

Its Fourier--Laplace factor `B_lambda(z)=int exp(i xi z) dlambda(xi)` obeys

`|B_lambda(z)-1| <= (WV/2)|z| exp(W|Im z|/2)`.

Consequently there is an absolute `c>0` such that `B_lambda` is guaranteed to remain order-one coherent throughout `|z|<=c/(WV)`. Positivity in NB-254 is the special case `V=1`. In the Ford scaling this gives the worst-case matched population

`J_* = R/(WV)`,

so `J_*->infinity` is sufficient for the NB-255 compatibility packet to survive.

NB-256 changes how this inequality must be interpreted. Raw `V` is not an intrinsic conditioning norm of the synthesized source or carrier. Starting from a positive baseline, one can add a microscopic dipole `N delta_0-N delta_(H/N^2)`. Then `V~2N->infinity`, while the smooth shell source returns to the baseline in `L^1` and shell-scaled `L^2`, and the carrier transform returns uniformly to the baseline throughout the natural `1/W` neighborhood. The formal `1/(WV)` guarantee can therefore become arbitrarily smaller than the *actual* coherence radius without purchasing useful cancellation.

The elementary estimate already contains the missing resolution dependence. With

`M_1(lambda)=int |xi| d|lambda|(xi)`,

one has

`|B_lambda(z)-1| <= |z| exp(W|Im z|/2) M_1(lambda)`,

and `M_1<=WV/2`. For the microscopic-dipole family, however, `M_1=W/2+H/N=W/2+o(W)` even though `V->infinity`. Amplitude times separation matters; coefficient mass before quotienting near-coincident opposite terms does not.

Thus NB-255 remains a valid worst-case theorem but its condition `V \gtrsim R/W` is **not evidence that a construction has paid a real source cost or bought carrier cancellation**. Before total variation can be used as a physical tariff, the carrier dictionary must exclude unresolved positive-negative dipoles or the coefficient measure must be passed through a resolution-sensitive quotient/seminorm. `MI-065` records this stronger source-side lesson.

**Boundary.** `M_1` is not established as the final coercive invariant; higher multipoles can defeat other low-frequency seminorms. NB-256 is a control against a conditioning argument, not a successful Nyman--Beurling approximant and not a statement about actual zeta zeros. Large variation can still amplify other arithmetic error terms. The exact destination cost after legal projection remains separate.