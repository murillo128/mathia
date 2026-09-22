# MI-075 — Bounded translation fibres, not horizon membership, set the fixed-noise alias threshold

**Evidence level:** exact finite-dimensional synthesis from [AF-491](../../findings/AF-491-nuisance-difference-geometry-controls-deterministic-resolution.md), [AF-493](../../findings/AF-493-nonconvex-nuisance-horizon-scaling-vs-recession.md), and [AF-494](../../findings/AF-494-bounded-offset-translation-fiber-controls-fixed-noise-alias-threshold.md), sharpening MI-074 from a qualitative radial-recurrence warning to an exact fixed-noise invariant.

For a nuisance difference set `C` and discriminator direction `s`, AF-493 shows that the horizon set `C^infty` controls only the normalized first-order escape rate

`liminf_(t->infinity) dist(ts,C)/t = dist(s,C^infty)`.

That is the right invariant for asking whether separation is forced at linear scale, but it does not decide a fixed deterministic noise budget once `s in C^infty`. AF-494 identifies the missing `O(1)` layer. Define the bounded translation fibre

`A_C(s) = {a : c_n-t_n s -> a for some t_n->infinity and c_n in C}`.

In finite dimension,

`lambda_C(s) := liminf_(t->infinity) dist(ts,C) = dist(0,A_C(s))`,

with `lambda_C(s)=infinity` exactly when the fibre is empty. Thus the sharp open fixed-noise phase boundary for ambiguity radius `rho` is `2rho=lambda_C(s)`: above it there are arbitrarily large aliases, below it ambiguity is bounded. Equality needs finer recurrence information because approaching the critical sphere from outside and actually meeting it infinitely often have the same `lambda_C(s)`.

The nuisance ledger is therefore genuinely layered. The horizon cone records which directions survive after division by scale; the translation fibre records which bounded offsets survive after following one specific direction; exact zero-noise collision asks the still stronger question whether the ray itself meets the difference set. AF-494 gives genuine difference-set examples with identical horizon geometry but every possible fixed-noise threshold in `[0,infinity]`, so no theorem based only on `C^infty` can recover the fixed-noise phase boundary for arbitrary nonconvex nuisance.

This refines the arithmetic-fidelity audit. A structured source restriction is useful only if it changes the asymptotic layer consumed by the recovery theorem. Excluding a direction from the horizon is sufficient for linear escape; if the direction remains in the horizon, the next relevant object is the bounded translated fibre, not an analogy with convex recession. Conversely, a small normalized distance is not evidence of fixed-noise non-identifiability unless it produces recurrent `O(1)` aliases.

**Boundary.** The translation-fibre identity uses finite-dimensional compactness for the reverse inequality and is a `liminf` statement. It does not decide the critical equality case, infinite-dimensional weak recurrence, or exact zero-noise collisions. None of AF-491/493/494 supplies rational-prime provenance or an RH implication; they classify the nuisance geometry through which any such source-specific discriminator would have to survive.