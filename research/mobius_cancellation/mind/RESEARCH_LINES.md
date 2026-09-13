# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Resolve the support-resolved signed Krawtchouk hierarchy or the surviving blind source mode

**Linked intuitions:** `MI-013-bost-connes-regularity-needs-an-intermediate-transverse-category`, `MI-014-centered-parity-and-zero-mode-are-separate-currencies`, `MI-015-sign-support-covariance-gives-a-conditioned-quadratic-bridge`, `MI-016-source-aligned-shifts-face-a-defect-or-mertens-dichotomy`, `MI-017-first-shell-crt-common-mode-is-a-source-coupled-energy-coordinate`, `MI-018-nonnegative-transference-does-not-create-fixed-power-sign-balance`, `MI-019-shell-square-blindness-is-a-cross-prime-common-quotient-problem`, `MI-020-explicit-large-sieve-uniformity-stops-before-blind-support-scale`, `MI-021-support-matched-high-moments-cross-the-single-blind-shell-threshold`.

The conductor and fixed-order algebraic escapes are largely exhausted. Full shell generation would require an all-class smooth-representative theorem near the logarithmic generator cutoff, while the growing-order quadratic-large-sieve route loses its saving before the first possible blind support.

[MC-264](../findings/MC-264-support-matched-high-moment-blind-threshold.md) identifies the viable amplification scale: at the first unresolved support `t~(1/log 2)log log y`, moment order `2(t+1)` crosses the single-blind-atom threshold with large slack. [MC-265](../findings/MC-265-even-support-central-krawtchouk-balance-obstruction.md) rules out the first-order-balance shortcut: even perfect Hamming balance leaves a central even Krawtchouk coefficient far above the pointwise scale required by a triangle-inequality proof.

[MC-266](../findings/MC-266-tensor-pair-krawtchouk-radial-source-walk-collapse.md) now removes the apparent two-source complexity. The tensor coefficients are convolution powers on the lower-prime Boolean cube, so

`sum_u c_m(u)c_m(uq)=c_(2m)(q)`

exactly. Hence the full moment is the one-source mixture

`S_(2m,y)(t)=sum_q c_(2m,y)(q) K_t(d_y(q);N_y)`.

Because `c_(2m,y)(q)` depends only on the source support `s=omega(q)`, this reduces further to the finite radial hierarchy

`S_(2m,y)(t)=sum_(s even, 0<=s<=2m) C_(2m,k_y)(s) H_(s,y)(t)`,

where `H_(s,y)(t)` is the signed shell Krawtchouk aggregate over products of exactly `s` lower primes. The nontrivial radial layers have raw coefficient masses of higher polynomial degree than the diagonal, so absolute-value control still cannot close the estimate.

The live theorem is therefore narrower: prove enough signed cancellation in the support-resolved aggregates `H_2,H_4,...,H_(2m)`, exploit a recurrence coupling neighboring support layers before absolute values are taken, or estimate their exact weighted mixture directly. The alternative exits remain logarithmic all-class generation or direct source-scale control of the surviving blind character.

## Keep support order, radial source mass and signed shell cancellation separate

MC-266 shows that arbitrary tensor-pair geometry is not an independent resource: multiplication in the exponent-two Boolean group collapses it to a single `2m`-step source walk. But radiality does not make the arithmetic kernel radial—`d_y(q)` still varies inside a fixed support layer—and the raw mass of the nontrivial layers is much larger than the diagonal. The missing resource is specifically **signed arithmetic cancellation inside or across the source-support layers at `m=t+1`**, not another generic pairwise pseudorandomness estimate.
