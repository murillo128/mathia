# MI-013 — Compactification-critical low packets survive away from the cuff seam

**Evidence level:** exact for the unprojected compactified cuff-cell form through [PF-322](../../findings/PF-322-physical-low-packets-retain-critical-compactified-transverse-energy.md), with the seam-artifact loophole removed by [PF-323](../../findings/PF-323-interior-critical-low-packets-avoid-the-cuff-seam.md). This is still not a lower bound for the completed shear-deleted intrinsic `L/H` angle; the pant quotient, seam-energy normalization, physical projections and common completion may cancel the exhibited component.

The seam scale `s_n` tends to zero, and PF-233 writes the compactified transverse form schematically as `T_(a_n)=s_n^2 T_tilde_n`. PF-322 shows that `s_n` is not a uniform small parameter on the full fixed physical-low sector: a zero-mean Dirichlet packet can follow the receding high-weight region and retain order-one scaled energy.

PF-323 shows this is not caused by centering the packet at the quotient seam. Fix `0<lambda<1` and choose the unique interior point

`s_n cosh tau_(n,lambda)=lambda`.

Its distance from the positive cuff seam is strictly larger than `log(1/lambda)`. Hence any fixed window `|x|<=R<log(1/lambda)`, with `x=tau-tau_(n,lambda)`, lies strictly inside the cell for all sufficiently large `n`. Translation preserves the packet's norm, zero mean and fixed physical frequency band.

On that interior coordinate there is an exact scale normalization

`s_n cosh(tau_(n,lambda)+x) = lambda cosh x + sqrt(lambda^2-s_n^2) sinh x -> lambda e^x`

uniformly on bounded `x`. The potential part alone therefore has the positive limit

`lambda^2 integral_(-R)^R e^(2x) sin^2(kappa x)/(pi kappa x^2) dx > 0`.

So **moving away from the seam does not restore uniform pre-projection Taylor smallness**. The obstruction is a genuine compactification scale collision inside the growing cuff: fixed-band packets can sit where the shrinking geometric scale and the expanding compactification weight balance exactly.

This sharper witness changes the downstream test. Instead of asking whether seam identification removes the PF-322 packet, propagate the recentered critical-level packet through the actual one-cusp-pant quotient, PF-205 seam-energy normalization, physical `L/H` projections and PF-320 common completion. Any successful PF-321 estimate must show that those destination operations eliminate or sufficiently dilute the interior critical component, or else pay its surviving singular-value/Hilbert--Schmidt leakage in the PF-318 budget.

**Boundary.** The packet is globally defined on the cuff; PF-323 proves that a fixed interior window already contributes positive critical energy, not that the packet is compactly supported there. The result remains at the unprojected cell-form stage and does not constrain the independent conditional channel `T_H`.
