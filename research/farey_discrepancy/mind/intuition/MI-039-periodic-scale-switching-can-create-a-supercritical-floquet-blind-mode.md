# MI-039 — Switched blind directions matter only through their distance to a realizable positive occupancy

**Evidence level:** exact synthesis from FD-230--[FD-232](../../findings/FD-232-macroscopic-negative-capacity-forbids-switched-null-positive-lifts.md). No Mertens or RH conclusion is claimed.

The switched divisor geometry has a genuine signed blind space. FD-231 constructs profiles with macroscopic signed mass whose all-integer switched response remains only first order, so one-sided coercivity on nonnegative occupancies does not extend to arbitrary signed inputs.

FD-232 identifies the missing physical constraint. Writing a candidate occupancy as a signed blind profile plus nonnegative slack is possible at subquadratic scale only if the negative part of the signed representative is itself sparse relative to aggregate late-block capacity. A profile with a fixed negative-capacity fraction forces comparable slack and therefore cannot be hidden inside a subquadratic positive lift. The explicit FD-231 blind family has such a fixed negative fraction and is ruled out as a direct physical escape.

The reusable object is thus not the size of the signed kernel but the **distance of the required physical correction to the positive cone modulo that kernel**. Given a source-forced correction `c`, one may replace it by `c+h` with `h` switched-blind; the first necessary test is whether the negative part of some such representative becomes aggregate-capacity sparse. Only after that one-sided feasibility test is passed is it meaningful to ask whether the resulting positive realization retains the desired small switched response.

This moves the obstruction from “does a large blind mode exist?” to “can the source-forced affine class approach positivity cheaply?” It also prevents a signed nullspace construction from being credited as a physical occupancy before its reservoir cost is quantified.

**Boundary.** FD-232 gives a necessary condition, not a sufficient positive construction. It does not prove that the actual Mertens-derived correction has macroscopic negative distance from the blind quotient, nor that a vanishing negative fraction would by itself give the desired discrepancy bound.
