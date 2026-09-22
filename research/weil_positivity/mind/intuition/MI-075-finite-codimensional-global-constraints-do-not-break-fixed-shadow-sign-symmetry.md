# MI-075 — Finite-codimensional global constraints do not break fixed-shadow sign symmetry

**Evidence level:** exact RH-independent extension from [WP-403](../../findings/WP-403-finite-codimensional-source-constraints-cannot-create-fixed-shadow-orientation.md), removing the cutoff-stability hypothesis from MI-074/WP-402 for closed finite-codimensional source slices.

Let `V_d` be the centered self-adjoint hereditary fixed-shadow tangent space and let `P_d` denote the order-bounded tangent core: directions `h` for which `-Md<=h<=Md` for some finite `M`. Continuous hereditary cutoffs make `P_d` norm dense in `V_d`.

Now let `F subset V_d` be a closed real linear subspace of finite codimension. The individual cutoffs need not preserve `F`. Finite codimension is nevertheless enough to repair them: the image of the dense linear space `P_d` in the finite-dimensional quotient `V_d/F` is automatically all of that quotient. Choosing finitely many order-bounded quotient representatives lets every approximant be corrected back into `F` with vanishing norm cost. Hence

`closure(F intersect P_d)=F`.

Every direction in `F intersect P_d` has both sufficiently small signs inside the positive fibre `d+h>=0`. Therefore any linear response `T:F->Y` into a Banach space with pointed cone that is oriented solely by fixed-shadow positivity vanishes on this dense core. If `T` is closable, the graph criterion then forces `T=0` on all of `F`.

The source-nonlocality requirement left by MI-074 is thus stronger than literal cutoff instability. Imposing finitely many continuous global moments, matching equations, normalization conditions or balance laws can make every canonical cutoff leave the constraint surface, yet those finite quotient errors can still be repaired inside the two-sided tangent core. **Finite-dimensional global memory is not enough to create a linear orientation.**

A surviving linear escape must therefore exhibit structure that prevents this finite-dimensional repair: for example an infinite-codimensional source relation whose intersection with the order-bounded core is no longer dense, a singular/nonclosed operator domain, a genuinely nonclosable response, or a one-sided admissible set. Nonlinear/quadratic geometry or a finite--archimedean completion in which sectors transform together also lies outside the theorem.

**Boundary.** Finite codimension is a sufficient no-go criterion, not a characterization of all global relations. WP-403 does not show that an infinite-codimensional restriction escapes, does not rule out proper dense operator domains or nonlinear energies, and supplies no Weil positivity by itself. The reusable test is whether the proposed source relation actually destroys dense two-sided order-bounded tangency, not merely whether a cutoff violates a finite list of constraints.