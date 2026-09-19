# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Escape the absolute-value Mellin tariff by estimating the native zeta-primitive Fourier coefficient

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale` through `MI-057-reciprocal-log-support-mass-is-the-exact-two-sided-mellin-reconstruction-currency`.

The positive-source program has progressively separated recurrence existence, source resolution, interval occupancy, atomic carrying capacity and integer-carrier discrepancy. NB-202--NB-212 derive the current log-squared corridor and show that one fixed nonnegative smooth full-von-Mangoldt barycenter already exposes it. NB-213 closes ordinary Mellin primitivization as a representation-only repair, while NB-214--NB-216 show that positivity, signs, zero mean, bounded higher shell functionals and upward shell widening all repay the apparent gain through reconstruction, conditioning, signal normalization or support width.

NB-217 removes the remaining ordinary support-geometry loophole. For an arbitrary measurable logarithmic support set `E`, any bounded source functional and `j` ordinary primitive transfers obey

`||K_j||_1/|M_psi(h)| >= 2pi / J_j(E)`, where `J_j(E)=int_E u^(-j)du`.

The exact currency of every absolute-norm reconstruction is therefore reciprocal logarithmic support mass, not connected shell width. For one primitive the tradeoff depends on the two-sided logarithmic span. For every fixed `j>=2`, any support confined to `u asymp X` retains an `Omega(X^(j-1))` tariff regardless of upward width, signs or disconnectedness. On the Vinogradov--Korobov diagonal, subpolynomial normalized absolute cost requires the lower logarithmic source scale to reach `u=Q^(o(1))=X^(o(1))`; bounded cost forces support to bounded `u`, i.e. bounded physical integers.

NB-218 now isolates where that tariff actually enters. In `Re(s)>1`, if

`P_j(t)=sum Lambda(n)/(log n)^j n^(-sigma-it)` and `K_j(v)=int u^j h(u)e^(ivu)du`, then

`sum Lambda(n)h(log n)n^(-sigma-it) = (1/2pi) int K_j(v)P_j(t+v)dv`.

The factors `(log n)^j` and `(log n)^(-j)` cancel coefficientwise inside the signed convolution. Because a genuine shell is supported away from `u=0`, `K_j` also annihilates every finite polynomial jet of `P_j(t+v)`. Hence the positive-power tariff is not an algebraic loss in exact reconstruction; it is introduced when the primitive and kernel are decoupled by absolute values. On a shell `u=X+y`, the source is exactly the carrier-frequency Fourier coefficient `int B_X(v)P_j(t+v)e^(iXv)dv`.

The live source-side escape is therefore more specific than “exploit oscillatory correlation.” One must estimate that **native carrier-frequency coefficient** without reverting to `||K_j||_1 ||P_j||_infinity`, and localize the full-line convolution to a zero-free Vinogradov--Korobov window while controlling the coupled tails and branch/pole terms. A merely better pointwise bound for `log zeta`, another finite primitive, another sign pattern, or another relative-shell geometry does not address this target. A separate destination theorem remains load-bearing: one must still show that a Nyman approximant resolving the target realizes the source condition used by this analysis.

## Keep moving-complexity uniformity, source representation, conditioning, support geometry and reconstruction explicit

The relevant currencies now include source mass, source total variation, signed conditioning `kappa`, requested return tolerance, integer-cell occupancy, moving derivative order, zero-free contour width, logarithmic support width, reciprocal support mass `J_j(E)`, the norm of the destination-visible source functional, the exact prefactor multiplying the contour saving, whether the observable is prime-only or full von Mangoldt, the reconstruction cost introduced when derivatives are moved between the arithmetic transform and Mellin carrier, and whether the final estimate preserves or destroys the carrier-frequency correlation of the zeta primitive.

NB-210--NB-212 show that several apparent representation costs were removable once the source theorem was made faithful. NB-213--NB-217 give the converse warning that smoother transforms, signs, zero mean and broader/two-sided shells can all repay the gain elsewhere once reconstruction is absolutized. NB-218 separates this absolute-norm obstruction from the exact bilinear algebra: polynomially large primitive backgrounds and finite Taylor jets are invisible to a shell kernel, so pointwise primitive size is not the native quantity that the source reads.

Any continuation should therefore measure progress only after source normalization and final reconstruction. A smaller central kernel is not an improvement if conditioning or omitted tails grow reciprocally; a large raw higher moment is not free if its normalized source functional is bounded; a nominally wide support is not an escape if its reciprocal mass remains too small; and a small pointwise primitive envelope is not enough if the proof discards the signed carrier coefficient. The next meaningful analytic currency is a cancellation-sensitive norm or direct estimate for the localized convolution itself, together with a proof that its tails and contour-shift terms remain subordinate on the coupled moving scale.
