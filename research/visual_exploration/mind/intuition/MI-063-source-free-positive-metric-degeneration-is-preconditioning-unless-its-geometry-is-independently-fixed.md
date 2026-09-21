# MI-063 — Source-free positive metric degeneration is preconditioning unless its geometry is independently fixed

**Evidence level:** exact/classical matrix-analysis synthesis from [VIS-369](../../findings/VIS-369-source-free-degenerate-positive-metric-prescribes-singular-spectrum.md) and [VIS-370](../../findings/VIS-370-source-free-commuting-positive-metrics-are-spectral-filters.md), extending the bounded-metric comparison of MI-062.

VIS-368 shows that a positive coefficient metric uniformly comparable to an already priced baseline can change Wang singular values only by bounded factors. Letting the relative metric degenerate genuinely leaves that theorem, but VIS-369 shows that unconstrained degeneration is too expressive to count as arithmetic structure. If

`A_W = U Sigma V^*`

is the baseline Wang map, choosing a positive relative metric

`C = V D^2 V^*`

with `d_i=tau_i/sigma_i` on the active right-singular directions makes the new active singular values exactly any prescribed positive multiset `{tau_i}`. The metric eigenvalue `d_i^2` pays exactly for the factor applied to that singular channel. Rank is unchanged while `C>0`; exact new nullity appears only in a singular semidefinite limit.

The negative control does not disappear merely because the metric is chosen by a canonical or pre-registered rule. VIS-370 classifies every positive relative metric `C` commuting with the baseline Gram `G=A_W^*A_W`: in a common eigenbasis,

`G=diag(lambda_i)`, `C=diag(c_i)`,

so the new squared singular values are exactly `lambda_i c_i`. If `C=f(G)`, the singular spectrum is the scalar filter

`tau_i = sigma_i sqrt(f(sigma_i^2))`.

Inverse-Gram whitening, fractional powers and ridge rules can therefore flatten or change the apparent singular scale while introducing no source information and no new singular directions. A collapsing baseline direction rescued to order one by whitening imports the reciprocal-square conditioning scale into the coefficient metric.

The reusable distinction is between **metric degeneration** and **independently justified geometry**. A positive metric is not a new arithmetic resource merely because it is unboundedly ill-conditioned, canonical, regularized, fixed before inspection of the final plot, or generated from the Wang operator itself. Its full eigenvalue-and-orientation geometry must be fixed by a physical topology or arithmetic source law external to the already priced source-free coefficient map, and its cost must be propagated through the destination.

This also sharpens the noncommuting case. Free alignment with the right-singular basis is already programmable by VIS-369; commuting source-free rules are exactly spectral filters by VIS-370. A noncommuting positive metric can count only if the reason for its orientation is independently source- or destination-forced and survives comparison with the freely engineered control.

**Boundary.** VIS-369--VIS-370 are finite-dimensional positive-Hilbert statements about relative coefficient metrics for the source-free Wang map. They do not classify independently mandated physical norms, source-dependent metric rules whose selection itself contains arithmetic information, genuinely indefinite/non-Hilbert forms, nonlinear coupling, noncompact/global geometry, or controlled infinite-dimensional limits. They prove no improvement for the Chebyshev-theta remainder, zeta zeros or RH; they identify when a spectral improvement is only a transfer of conditioning into the metric.
