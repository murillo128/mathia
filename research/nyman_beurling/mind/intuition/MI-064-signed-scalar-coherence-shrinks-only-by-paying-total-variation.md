# MI-064 — Signed scalar coherence shrinks only by paying total variation

**Evidence level:** exact source-side synthesis from [NB-254](../../findings/NB-254-positive-scalar-carrier-mixtures-have-a-compulsory-coherence-window.md) and [NB-255](../../findings/NB-255-signed-scalar-carriers-pay-a-total-variation-coherence-tax.md), interpreted inside the Ford-scaled carrier framework of NB-245--NB-253. The result prices destruction of a scalar coherence window; it does not prove the same total-variation cost survives unchanged in the projected Nyman--Beurling or Hardy norm.

For a signed or complex shell mixture supported in a carrier span `W`, normalize by its actual Euler return at `sigma_X=1+r/X`. After absorbing that weight, let `lambda` be the resulting complex measure with `lambda(R)=1` and total variation

`V=||lambda||_TV >= 1`.

Its Fourier--Laplace factor `B_lambda(z)=int exp(i xi z) dlambda(xi)` obeys the elementary estimate

`|B_lambda(z)-1| <= (WV/2)|z| exp(W|Im z|/2)`.

Consequently there is an absolute `c>0` such that `B_lambda` remains order-one coherent throughout `|z|<=c/(WV)`. Positivity in NB-254 is the special case `V=1`; signs can shrink the guaranteed coherent neighborhood, but only in direct proportion to the coefficient variation spent.

In the Ford scaling this turns the positive-mixture population `R/W` into

`J_* = R/(WV)`.

Whenever `J_*->infinity`, NB-255 constructs the same type of matched compatibility packet inside the compulsory coherent disk and obtains an order-one contribution. The critical horizontal coordinate becomes

`d_crit = -log((W/H)V)+O(1)`.

Thus a signed scalar design does not escape the coherence mechanism merely by arranging cancellations. To prevent this particular matched population from diverging, its Euler-normalized variation must reach the scale `R/W` rather than remain `o(R/W)`.

This converts “use signs” into a conditioning question. The remaining route is to prove that a source with such large coefficient variation can nevertheless have a small destination cost after convolution, Hardy projection or whatever legal recombination the physical construction uses. That step is not automatic: overlapping signed shells can cancel after projection, so total variation is a source-side tariff rather than a proved Nyman--Beurling norm lower bound.

The reusable distinction is between **coherence cancellation and conditioning-free bandwidth**. Scalar support span `W` supplies independent effective bandwidth only after the coefficient variation needed to decorrelate the central window has been accounted for in the source normalization and then tracked through the actual destination map.

**Boundary.** The compulsory radius `c/(WV)` is a lower bound on a guaranteed coherent neighborhood, not a claim that coherence disappears immediately outside it. The matched packet is an adversarial compatibility construction and is not asserted to be realized by actual zeta zeros. NB-255 does not exclude non-scalar channel retention, projected cancellations that hide source variation, or other source geometries; it isolates the variation scale any signed scalar escape must first pay.