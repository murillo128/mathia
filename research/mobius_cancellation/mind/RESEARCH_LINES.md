# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Exploit analytic cancellation at squarefree conductor, or constrain the localized tame quotient

**Linked intuitions:** `MI-013-bost-connes-regularity-needs-an-intermediate-transverse-category`, `MI-014-centered-parity-and-zero-mode-are-separate-currencies`, `MI-015-sign-support-covariance-gives-a-conditioned-quadratic-bridge`, `MI-016-source-aligned-shifts-face-a-defect-or-mertens-dichotomy`, `MI-017-first-shell-crt-common-mode-is-a-source-coupled-energy-coordinate`, `MI-018-nonnegative-transference-does-not-create-fixed-power-sign-balance`, `MI-019-shell-square-blindness-is-a-cross-prime-common-quotient-problem`.

MC-238--MC-246 reduce complete blindness to one rough Möbius coset and the localized lower-prime/shell-prime quotient. MC-252--MC-256 eliminate generic fixed-order residue rank as a source of rigidity once localization is removed. MC-257 then closes the wild prime-square escape in the actual factor-of-two shell: the full wild kernel lies in the lower-prime-generated subgroup, so every blind character factors through the squarefree shell modulus `R`.

MC-258 now resolves the simplest hoped-for payoff from that descent. Although `q=R^2` descends exactly to `R`, the source projector carries an exterior factor `1/R`: `B_S^(A)=R^(-1) P_R(g_y;T,-1)`. This normalization exactly compensates the larger squarefree residue support in the main term. At `R=X^(alpha+o(1))`, support-only control still reaches the square-root scale only at `alpha>=1/4`; the descent improves the elementary error but not the support exponent.

The surviving problem is therefore genuinely analytic/localized. Prove cancellation for the exact rough Möbius coset using the now-squarefree blind conductors, or show that moving-shell localization constrains the tame cross-prime quotient in a way absent from fixed-order nonlocalized controls. Recounting support at the smaller conductor is closed.

## Keep conductor descent, projector normalization, tame quotient size and signed cancellation separate

MC-257 is an exact structural reduction; MC-258 is an exact normalization audit. Together they remove the wild conductor layer without shrinking the support exponent. A smaller conductor is useful only if an analytic theorem actually exploits it.

A useful next theorem must therefore enter squarefree-conductor twisted Möbius cancellation or prove new shell-specific tame coupling. It must not infer a gain merely from replacing `R^2` by `R`, and it must keep the exterior `1/R` projector normalization visible.