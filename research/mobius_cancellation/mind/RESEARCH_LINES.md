# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Exploit the remaining tame squarefree shell quotient, or cancel the exact rough Möbius coset directly

**Linked intuitions:** `MI-013-bost-connes-regularity-needs-an-intermediate-transverse-category`, `MI-014-centered-parity-and-zero-mode-are-separate-currencies`, `MI-015-sign-support-covariance-gives-a-conditioned-quadratic-bridge`, `MI-016-source-aligned-shifts-face-a-defect-or-mertens-dichotomy`, `MI-017-first-shell-crt-common-mode-is-a-source-coupled-energy-coordinate`, `MI-018-nonnegative-transference-does-not-create-fixed-power-sign-balance`, `MI-019-shell-square-blindness-is-a-cross-prime-common-quotient-problem`.

MC-238--MC-246 reduce complete blindness to one rough Möbius coset and the localized lower-prime/shell-prime quotient. MC-252--MC-256 then eliminate generic fixed-order residue rank as a source of rigidity once localization is removed: quadratic matrices, completed `2`-class towers, and every fixed tame prime residue order admit controls with arbitrary compatible cross-prime behavior.

MC-257 closes the remaining wild prime-square escape in the actual factor-of-two shell. For every shell prime `r`, some lower prime has nonzero Fermat quotient mod `r`; CRT/Sylow isolation then forces the whole wild subgroup `U_r=1+rZ/r^2Z` into the lower-prime-generated subgroup `H`. Hence the full wild kernel lies in `H`, every blind character factors through the squarefree shell modulus `R`, and the exact quotient `G/H` is already tame.

The surviving algebraic problem is therefore narrower: determine whether **moving-shell localization couples the tame squarefree cross-prime matrix strongly enough** to constrain the remaining quotient, or whether the conductor descent from `R^2` to `R` materially strengthens an exact localized character-sum/projector estimate. Fixed-order nonlocalized universality remains the control. The alternative is still to bypass quotient generation and prove signed cancellation directly for the exact rough Möbius coset.

## Keep localization, conductor size, tame cross-prime structure and signed cancellation separate

MC-257 is an exact structural reduction, not an analytic cancellation theorem. Lowering the natural blind conductor from the shell-square modulus to a divisor of the squarefree shell removes every wild Sylow direction but does not imply that `H=G`, impose rank rigidity on the tame matrix, or improve a character-sum bound automatically.

A useful next theorem must re-enter the exact localized analytic estimates with the squarefree conductor, or prove a new shell-specific constraint on the tame bipartite residue data. Growing-order/wild prime-square structure is no longer an independent escape route for this shell construction.