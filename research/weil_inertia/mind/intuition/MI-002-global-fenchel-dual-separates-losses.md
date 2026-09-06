# MI-002 — Realizability helps, but the fixed single-profile linear-pressure assembly has a matched ceiling

**Evidence level:** supported by exact duality, source-specific realizability gains, formally checked local surplus, interval bounds, and explicit periodic countermodels through WI-175

## Core intuition

The Weil-inertia program separates optimization loss, realizability loss, and representation/assembly loss. Global optimization and actual source geometry can recover information discarded by a coarse scalar envelope, and WI-172 proves that this can yield a strict source-specific gain. But once the complete represented data are matched by a periodic countermodel, retuning constants or redistributing a linear pressure cannot create new information.

## Strongest justified principle

WI-012 establishes the global Fenchel improvement over fixed-window pinching. WI-020--WI-024 and WI-036 then show that abstract spectral envelopes omit translation-Gram realizability constraints, so span/packing geometry can improve the local scalar bound. WI-172 confirms the point on the actual Montgomery--Taylor source: the kernel/placement coupling gives a strict formally checked improvement beyond the sharp arbitrary-positive relaxation.

WI-174 quantifies how little remains in the most literal continuation. The exact fixed-`p=2500` four-point constant lies below `2343/10^6`, so sharpening only that local constant can improve the certified bridge by less than `8.65e-6` after optimal block-size bookkeeping.

WI-175 closes the broader linear-pressure retuning class under the same single-profile shifted assembly. On the period-33 witness, averaging over starting phase sends every nonnegative linear gap-pressure vector to the same scalar total `A/r`; the local pressure credit is then cancelled exactly by the global pressure tax. The resulting ceiling is independent of how the coefficients are distributed. Hence “better coefficients” inside this architecture are not a new mechanism.

## Consequence

A further gain must change a load-bearing interface: nonlinear/source-dependent pressure, another or multiple independent profiles, a global assembly not reducible to the same scalar tax, the uncollapsed exceptional block, or new arithmetic information that excludes the periodic witness. The order remains: optimize globally, impose source realizability, then test the complete represented architecture against matched controls.

## Evidence against overgeneralization

WI-174--WI-175 are route-specific. They do not bound every support-one argument, every Gram matrix, or every pressure concept. A changed profile, nonlinear pressure, multiple channels, different assembly, or stronger source theorem is genuinely outside the matched witness class.

## Status / novelty

Fenchel duality, translation-Gram realizability, interval optimization, and periodic averaging are classical/persisted ingredients. The durable synthesis is: **source realizability can beat a universal scalar relaxation, but once a matched periodic model sees the same single-profile linear-pressure data, further scalar retuning is information-neutral**.

## Falsification criterion

Exceed the WI-175 ceiling using exactly the same single Montgomery--Taylor profile, a nonnegative linear gap pressure, and the same scalar shifted-block accounting, without any additional observable or hypothesis. An improvement using new represented data would instead confirm the stated boundary.

## Lean-formalizable core

- Exact Fenchel and realizability inclusions.
- Monotonic propagation of a local-constant cap through the fixed bridge.
- Phase averaging of an arbitrary linear pressure and cancellation of local credit against global tax.
