# MI-076 — Convex critical contact is a temporal plateau gate

**Evidence level:** exact synthesis from AF-495--AF-505, with the temporal criterion proved in [AF-505](../../findings/AF-505-convex-critical-contact-is-a-temporal-plateau-gate.md).

AF-505 isolates an existence gate that compactness cannot replace. For a nonempty convex destination set `F` in a normed quotient `Q`, if `f(t)=dist_Q(tu,F)` has finite `lambda=liminf_(t->infinity) f(t)`, convexity forces `f` to decrease to `lambda`. Exact critical contact is therefore not a generic proximinality statement: `{t>=0:f(t)<=lambda}` is either empty or a terminal ray, so reaching `lambda` once is equivalent to eventual plateau.

This sits before the AF-499--AF-504 compactness questions. Pointwise nearest points answer what happens at a time `t` that already exists; the critical tail compactness test answers whether repeated critical contacts admit a compact limiting fibre. Neither manufactures the time at which the asymptotic value is reached. AF-505's two closed convex planar sets have the same `lambda`, recession cone, bounded-offset translation fibre and post-limit compactness profile, yet one plateaus at `lambda` and the other approaches it strictly from above.

For quotient-visible arithmetic fidelity the equality ledger is therefore ordered: first prove temporal attainment of the quotient distance, then ask for pointwise source/contact attainment, then ask for compactness of the retained contact fibre. If temporal attainment is unavailable, an exact-threshold argument must retain the critical-contact bit or move to controlled radii `R>lambda` rather than treating post-limit geometry as a substitute.

**Boundary.** This conclusion requires convex destination geometry and finite `lambda`. AF-505 supplies a synthetic separation example, not a claim that the natural arithmetic nuisance quotient is on the plateau or no-plateau branch, and it gives no rational-prime discriminator or RH implication.