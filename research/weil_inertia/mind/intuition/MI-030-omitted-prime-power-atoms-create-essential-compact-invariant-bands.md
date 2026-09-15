# MI-030 — Omitted prime-power atoms create compact-invariant essential obstruction bands

**Evidence level:** exact-derived operator obstruction from [WI-304](../../findings/WI-304-omitted-prime-power-atoms-create-essential-obstruction-bands.md), generalizing the source-exact `q=8` construction recorded around WI-302--WI-303.

Consider a tail-dropped localized comparison whose high-frequency modulations of a fixed compact test have Rayleigh quotient tending to `beta>0`. If an active prime-power atom `q` at `a=log q` is geometrically isolatable by a two-bump test, phase-modulating that test yields weakly-null unit vectors with limiting Rayleigh quotients

`beta - w_q cos(theta)`,

where

`w_q=(Lambda(q)/sqrt(q))(1-rho_chi(log q))`.

Varying `theta` therefore places the whole interval

`[beta-w_q,beta+w_q]`

inside the essential numerical range of the tail-dropped comparison. Since essential numerical range is invariant under compact perturbations, the criterion

`w_q>beta`

implies that **no fixed compact self-adjoint correction can make the comparison positive**.

This turns a qualitative “noncompact tail matters” statement into a channel-by-channel design invariant. An omitted arithmetic atom is dangerous when its localization defect weight exceeds the comparison's high-frequency positive reserve. A successful architecture must retain noncompact information for that channel, raise the reserve, reduce the atom's defect through the localizer, or add another noncompact mechanism that survives the same weakly-null sequence.

The criterion does not require retaining every prime power. For a fixed positive reserve and a localizer with `rho_chi(log q)=0` eventually, `Lambda(q)/sqrt(q)->0`, so only finitely many channels can violate the inequality. What is structurally forbidden is replacing a dangerous omitted channel by any fixed compact/finitely ranked patch.

**Boundary.** The interval theorem concerns the bounded tail-dropped comparison and individually isolatable atoms. It is a necessary obstruction, not a sufficient positivity test after all dangerous channels are treated, and it does not validate the unreplayed `17/16` certificate or claim negativity of the full Weil form retaining its source-exact positive remainder.