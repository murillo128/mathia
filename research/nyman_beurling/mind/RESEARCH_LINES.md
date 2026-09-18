# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Escape the absolute-value Mellin tariff rather than merely changing source representation

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale` through `MI-056-bounded-shell-signals-make-zero-mean-and-support-width-explicit-mellin-currencies`.

The positive-source program has progressively separated recurrence existence, source resolution, interval occupancy, atomic carrying capacity and integer-carrier discrepancy. NB-202--NB-205 push an `o(1/X_a)` positive Euler return from quadratic shell height through the Vinogradov--Korobov acquisition regime. NB-206 shows why fixed-complexity estimates cannot be used blindly on a moving diagonal, while NB-207 removes an avoidable harmonic-window logarithm.

NB-208--NB-212 derive the current log-squared corridor and show that one fixed nonnegative smooth full-von-Mangoldt barycenter already exposes it. NB-213 then closes ordinary Mellin primitivization as a representation-only repair: replacing `-zeta'/zeta` by `log zeta` and estimating the transferred contour absolutely differentiates the shell carrier and restores a factor `X`.

NB-214 closes the larger positive fixed-shell preconditioning escape. For every nonzero nonnegative profile supported in one fixed logarithmic shell `[0,Delta]`, the source-normalized primitive reconstruction kernel has `L1` norm at least `c_Delta X`, and positivity preserves the same order on a fixed central frequency neighborhood.

NB-215 removes the tempting conclusion that signs alone repair this. For every signed/complex fixed-shell profile with nonzero mean `m`, Fourier inversion gives the sign-blind global lower bound

`||K_X||_1/|m| >= 2pi/log(1+Delta/X) >= (2pi/Delta)X`.

After `j` primitive transfers the same argument costs at least `(2pi/Delta)X^j`. A signed profile can suppress the central lobe only by exporting reconstruction mass to other frequencies or by becoming badly conditioned as a source functional. If `kappa=||h||_1/|m|` and the contour contains a fixed central neighborhood, NB-215 proves

`kappa max{1,C_X(I)} >= X/(5Delta)`,

so at least one of source conditioning or central reconstruction costs `Omega(sqrt(X))`. On the Vinogradov--Korobov diagonal `X=Q^(2/3+o(1))`, bare absolute-norm closure therefore still pays a positive power `Q^(1/3+o(1))` somewhere and remains in the same log-squared method class.

NB-216 prices the two explicit representation escapes left by NB-215. For any bounded shell reference pattern `||psi||_infinity<=1` with nonzero normalized signal `M_psi(h)`, the `j`-primitive kernel satisfies

`||K_(X,j)||_1/|M_psi(h)| >= 2pi / int_0^Delta (X+y)^(-j)dy`.

Thus zero mean does not help merely by replacing the barycenter with a bounded higher moment: the same reciprocal-multiplier tariff applies. A growing shell creates a genuine tradeoff only for `j=1`, where reducing the cost to a subpolynomial class requires `Delta >= X Q^(-o(1))` and bounded cost requires `Delta=Omega(X)`. For every `j>=2`, widening the shell arbitrarily still leaves an irreducible `Omega(X^(j-1))` tariff. The escape therefore has to spend real logarithmic support width or leave the bounded-shell-functional class altogether.

The live escape is now more specific than “use signs”, “use zero mean” or “widen the shell.” One must exploit the **actual oscillatory correlation between the zeta primitive and the reconstruction kernel before absolute values**, identify a destination-visible source functional whose natural normalization genuinely lies outside bounded shell duality and price that norm, or change the physical support geometry so radically that it is a different observable. A separate destination theorem remains load-bearing: one must still show that a Nyman approximant resolving the target realizes the source condition used by this analysis.

## Keep moving-complexity uniformity, source representation, conditioning, support width and reconstruction explicit

The relevant currencies now include source mass, source total variation, signed conditioning `kappa`, requested return tolerance, integer-cell occupancy, moving derivative order, zero-free contour width, logarithmic support width `Delta`, the norm of the destination-visible source functional, the exact prefactor multiplying the contour saving, whether the observable is prime-only or full von Mangoldt, and the reconstruction cost introduced when derivatives are moved between the arithmetic transform and Mellin carrier.

NB-210--NB-212 show that several apparent representation costs were removable once the source theorem was made faithful. NB-213--NB-216 give the converse warning: a smoother arithmetic transform, a positive profile, a signed profile, zero-mean recentering or a wider shell can all repay the apparent gain through carrier reconstruction, source conditioning, functional normalization or physical support width. After two or more primitives, upward widening does not even remove the residual polynomial tariff.

Any continuation should therefore measure progress only after source normalization and final reconstruction. A smaller central kernel is not an improvement if `kappa` or the omitted frequency tails grow by the reciprocal amount; a large raw higher moment is not free if its normalized source functional is bounded; and a broader shell is not local preconditioning once `Delta` approaches the carrier scale. Only a source-specific correlation theorem, a genuinely different normalized signal, or a changed support geometry can move the method into a new asymptotic class.