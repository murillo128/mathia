# MI-009 — Passive Gamma scalarization is either too rigid or too flexible unless a new coercive class is source-forced

**Evidence level:** exact/literature-backed passive, Fredholm, modified-determinant, and dissipative controls through WP-180

## Core intuition

The real-place Gamma obstruction is no longer merely a closure theorem for ordinary Schur scalarization. The regular passive hierarchy now has a sharp two-sided boundary. Lossless passivity is **too rigid** in the determinant channels that inherit its order: ordinary determinant and `det_2` have one-sided boundary phase motion and cannot reproduce the sign-changing Gamma phase. Higher modified determinants and genuinely dissipative Schur systems are **flexible enough** to change phase orientation, but exactly for that reason passivity no longer supplies the sign theorem.

A viable escape must therefore define a smaller source-derived class and prove a replacement coercivity/order theorem after the category change. Matching the Gamma phase is not itself evidence of positivity.

## Strongest justified principle

WP-171--WP-177 close regular matrix-Schur readouts, finite negative index, regular `J`-contractive/passive-Hilbert termination, common-domain singular limits, weak boundary convergence, ordinary Nevanlinna relations, and analytic trace-class Fredholm scalarization. None creates a hidden Gamma-compatible passive scalar class.

WP-178 identifies the first modified-determinant boundary. `det_2` can leave the scalar Schur modulus, but on a regular lossless Hilbert--Schmidt unitary path its boundary phase derivative is `Tr((I-Re U)Q_U)>=0`. The Gamma phase changes orientation, so escaping the modulus does not escape the passive phase sign.

WP-179 classifies all higher modified determinants. For `det_m`, the phase derivative contains the functional-calculus factor `Re[(-1)^{m-1}(U-I)^{m-1}]`. It is positive for `m=1,2`, but its scalar symbol changes sign on the unit circle for every `m>=3`. A pure-delay inner function with constant positive delay therefore already produces both phase orientations after higher regularization. The counterterm, not new arithmetic geometry, manufactures the sign freedom.

WP-180 tests the other obvious category change before any determinant is taken. The elementary passive one-port `S(s)=(s+a)/(s+b)`, `0<a<b`, is strictly Schur and has a positive-real resistor--inductor realization, yet its boundary phase derivative changes sign at `|omega|=sqrt(ab)`. That crossover can be placed arbitrarily by varying `a,b`. Dissipative passivity is therefore not a one-sided phase-order theorem.

The durable category boundary is: **ordinary/lossless passive scalarization preserves an order incompatible with Gamma, while higher regularization or dissipation removes that order without replacing it.**

## What remains possible

A source-forced spectral-sector restriction could make a higher-determinant factor one-sided on the actual admissible spectrum. A dissipative construction could carry a positive kernel, storage inequality, Herglotz measure, de Branges-type norm, or coupled finite--archimedean quadratic form whose sign survives scalarization. Singular/domain-changing or indefinite/infinite-index constructions remain outside the tested classes.

Each possibility needs an independent theorem fixing the admissible class **before** the Gamma target is fitted. A counterterm, dissipation profile, reference, or spectral sector chosen because it reproduces the desired sign is a representation, not an explanation of Weil positivity.

## Status / novelty

Schur/Nevanlinna theory, Fredholm and modified determinants, positive-real/passive realization, and phase behavior of inner/dissipative systems are classical. The durable Mathia synthesis is the two-sided coercivity boundary: **category escape either retains too much passive order or loses the order entirely; a successful route must introduce a new source-native positive structure.**

## Falsification criterion

Produce a lossless passive `det_m`, `m=1` or `2`, whose phase violates the established one-sided law; prove a universal one-sided phase theorem for `det_m`, `m>=3`, despite the pure-delay controls; or prove that ordinary dissipative Schur passivity forces one phase orientation despite WP-180's positive-real counterexample. Any such result would change this category boundary.