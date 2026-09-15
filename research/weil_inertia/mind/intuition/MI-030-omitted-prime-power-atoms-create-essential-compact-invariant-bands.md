# MI-030 — Omitted prime-power atoms create compact-invariant bands, and the first prime already beats the reserve

**Evidence level:** exact-derived operator obstruction from [WI-304](../../findings/WI-304-omitted-prime-power-atoms-create-essential-obstruction-bands.md), sharpened to the exact first-prime threshold by [WI-305](../../findings/WI-305-first-prime-activation-already-obstructs-compact-repair.md).

Consider a tail-dropped localized comparison whose high-frequency modulations have Rayleigh quotient tending to `beta>0`. If an active prime-power atom `q` at `a=log q` is geometrically isolatable, phase modulation yields a weakly-null family with limiting Rayleigh quotients

`beta-w_q cos(theta)`,  `w_q=(Lambda(q)/sqrt(q))(1-rho_chi(log q))`.

Hence the whole interval `[beta-w_q,beta+w_q]` lies in the essential numerical range. Since compact perturbations leave that set invariant, `w_q>beta` implies that no fixed compact self-adjoint correction can make the tail-dropped comparison positive.

WI-305 shows that, for Liu's normalized real localizers `chi in C_c^infty((-1,1))`, this obstruction is already unavoidable at `q=2`. Let `S_a` be translation by `a` compressed to `L^2(-1,1)`. If `S_a^m=0`, the Haagerup--de la Harpe inequality gives

`|rho_chi(a)| <= cos(pi/(m+1))`.

At `a=log 2`, `S_a^3=0`, so `rho_chi(log 2)<=1/sqrt(2)`. With the comparison reserve `beta_0=1/16`,

`w_2 >= (log 2/sqrt(2))(1-1/sqrt(2)) > 1/16`.

The atom `q=2` is active exactly when `L>log(2)/2`; below that aperture no prime-power atom is active. Thus, within this localization/tail-dropping architecture, the essential compact-repair obstruction begins at the **first arithmetically possible threshold**. The earlier `q=8` witness is not the structural onset; it is only the first shift where support makes the autocorrelation vanish without a sharper operator bound.

The design consequence is stronger than a generic “noncompact tail matters” statement. Once the first prime channel enters, any successful comparison must alter something that survives the same weakly-null sequence: retain source-exact noncompact information, increase the positive reserve, reduce the defect through a genuinely stronger localizer mechanism, or add another noncompact contribution. A compact/finitely ranked patch is invisible to the obstruction.

**Boundary.** The result concerns the specified bounded tail-dropped comparison plus fixed compact correction. It is not a negative test for the full Weil form, does not validate or refute the unreplayed finite certificate, and does not prove that every prime-power channel must be retained individually. The full source-exact remainder can supply noncompact compensation absent from the reduced comparison.