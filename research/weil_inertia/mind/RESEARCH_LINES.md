# Weil-inertia research lines

This file records the current mathematical questions that survive the Weil-Inertia evidence. It is not a roadmap, task queue, status page, or history.

## Keep source regularity separate from regularity of the canonical defect measure

WI-417--WI-422 identify sharp coercive source-space phenomena for translated-Blaschke probes. With an independently fixed planar density cap, one-target cost has the expected shallow-depth blow-up and critically separated target families converge to a Poisson-capacity problem. Generic TV/Carleson control is too weak because target-adaptive atoms remain cheap. For the bare translated-Blaschke response, ordinary global `L^p` control is bounded exactly for `1<p<2`, with a Lorentz endpoint and different behavior once a finite-TV budget is added.

WI-423 shows why these useful auxiliary spaces cannot simply be imposed on the canonical exact zeta source. The Riesz identity `-Delta U = 2 pi mu_off` makes that source the atomic counting measure of off-critical zeros; exact absolute continuity of the same source would already force the defect measure to vanish. A nontrivial route must therefore generate an auxiliary probe/coefficient source independently and prove an exact or quantitatively controlled coupling from its potential back to the canonical defect measure.

The live question is to derive such an auxiliary source and a target-independent concentration-and-tail budget from accessible prime-side, boundary or explicit-formula data. The norm must be fixed without inspecting hypothetical zero locations and must control the actual Poisson-capacity geometry consumed by the destination.

## Escape fixed-safe-strip cubic blindness without hiding the defect in a singular operator budget

WI-424 identifies the boundary logarithmic derivative of the Kunik Blaschke factor as a canonical positive Poisson defect counter. WI-425 shows that any fixed interior safe line is cubically blind to sufficiently shallow defects. WI-426 gives the same blind-or-singular obstruction for positive multiscale `L^2` line energy, and WI-427 closes every finite-cost positive diagonal `L^p` portfolio below the local pole threshold.

WI-428 closes the two most immediate nonpositive escapes on a fixed safe strip. For the one-defect response, the exact cross-scale kernel is

`K_d(a,b)=16 pi d^2 / [(a+b)((a+b)^2-4d^2)]`.

Any signed or complex cross-scale charge with finite depth-independent weighted variation `int int (a+b)^(-3) d|nu|` therefore produces only `Q_nu(d)=O(d^2)`, while the canonical boundary energy is `2 pi/d`. The relative response is still `O(d^3)`. The same obstruction holds for bounded non-diagonal quadratic forms and for bounded cancellation before taking a Hilbert norm. To retain a fixed fraction of the boundary energy as `d->0`, a quadratic-form operator must have norm at least order `d^(-3)`, or a preprocessing map before squaring must have norm at least order `d^(-3/2)`.

Signs, cross-scale mixing and cancellation-before-norm are therefore not independent repairs when their budget remains bounded and the safe strip stays a fixed distance from the boundary. The live question is to identify a **source-forced reason for any required singularity or category change**: for example a depth-dependent operator/renormalization whose growth is derived without inspecting the hypothetical defect, a controlled approach of the probing strip toward the boundary with its cost fully priced, or arithmetic structure that couples directly to the canonical boundary flux outside the bounded safe-strip model. Merely allowing negative coefficients or non-diagonal kernels is now excluded.
