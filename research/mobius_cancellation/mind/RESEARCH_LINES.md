# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Prove full quadratic generation or signed rough-Möbius cancellation on the exact blind affine cell

**Linked intuitions:** `MI-013-bost-connes-regularity-needs-an-intermediate-transverse-category`, `MI-014-centered-parity-and-zero-mode-are-separate-currencies`, `MI-015-sign-support-covariance-gives-a-conditioned-quadratic-bridge`, `MI-016-source-aligned-shifts-face-a-defect-or-mertens-dichotomy`, `MI-017-first-shell-crt-common-mode-is-a-source-coupled-energy-coordinate`, `MI-018-nonnegative-transference-does-not-create-fixed-power-sign-balance`, `MI-019-shell-square-blindness-is-a-cross-prime-common-quotient-problem`.

MC-238--MC-243 identify smooth-dilation blindness with a Legendre-symbol kernel, force growing support, convert that into a coding-scale rank lower bound, and show why minimum support alone cannot determine blind-sector dimension.

MC-244 then inverts the entire quadratic blind family to one affine Legendre-sign source projector. The factor `2^kappa` from the number of blind characters cancels exactly against the `2^-kappa` density of their annihilator fiber, so every positive blind dimension has the same worst-case support exponent. Only full rank is qualitatively different.

MC-245 removes one more apparent source complication exactly. The smooth weight `Psi(T/m,y)` in the MC-244 projector is just the old smooth-inverse convolution coordinate: because every `y`-smooth multiplier has trivial charge in the Legendre quotient,

`mu * s_y = g_y`

regroups the complete blind contribution into a **single logarithmically rough Möbius partial sum on one affine Legendre cell**. The support count gains the expected rough-density factor `1/log log X`, but no new power; the `alpha=1/4` absolute-support boundary remains.

Character by character, the rough twist has Dirichlet series `L(s,chi_v)^(-1)` times only a finite small-prime Euler correction. Thus roughing does not regularize the reciprocal-Dirichlet-`L` obstruction. At the aggregate-cell level, however, cross-character cancellation remains logically possible and is not equivalent to bounding every blind character separately.

The live theorem has therefore become very concrete. Either prove `kappa=0` and eliminate the nonprincipal quadratic blind sector, or prove fixed-power signed cancellation for the one source-selected rough Möbius affine cell. Another support floor, positive-dimension estimate, or analysis of the auxiliary smooth `Psi` weight no longer reaches the frontier.

## Keep minimum support, blind dimension, affine-cell density, arithmetic rank, rough support, cross-character cancellation, and signed amplitude separate

MC-244 shows why positive dimension does not buy support power after source inversion; MC-245 shows why the all-powers smooth weight also disappears under exact inversion. The remaining source object is the rough Möbius mass in one quotient charge. Full rank and signed affine-cell cancellation are the two genuinely different exits.