# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Prevent physical hyperbola-sampling amplification with source-specific energy regularity or coercivity

**Linked intuition:** `MI-001-cumulative-farey-discrepancy-is-mertens-energy`.

FD-024--FD-040 show that terminal nonsquarefree occupation is universally positive and every fixed finite supercritical Mellin packet is coercively sampled, while generic bounded-increment shell profiles can still evade by concentrating energy on sparse low rows. FD-041 then makes the scalar split exact: squarefree versus nonsquarefree occupation is a powerful-number dilation sieve of one total-energy curve, so regular multiplicative scaling already forces a positive nonsquarefree fraction.

FD-042--FD-044 sharpen the critical spectral side. Centering by the natural density cancels the critical pole, and the centered finite Jordan kernel factors through zeta with only the classical zero-free-region logarithmic cost. Well-conditioned growing packets remain controlled through frequency diameter below the square-root scale; close frequencies by themselves do not create an inverse-gap escape.

FD-045 pushes the source control farther. The weighted squarefree coefficient has the classical `zeta(s)/zeta(2s)` factorization, and Walfisz cancellation carries the centered kernel estimate through frequencies of size `R^(1/2) exp(c Lambda(R))`. Thus merely reaching the square-root frequency window is not a physical escape either.

The live theorem must now explain how the actual quotient-shell source could evade all three controls at once: regular scalar scaling, centered Euler-product cancellation, and finite/growing packet coercivity. A viable escape needs genuinely larger effective complexity, bad coefficient conditioning, a non-negligible truncation/remainder, or source-specific multiplicative irregularity; another generic density, Lipschitz, or square-root-frequency argument is below the frontier.

## Treat terminal density, scalar scaling, centered Euler cancellation, and packet coercivity as matched controls

Terminal Jordan blocks, regular multiplicative total-energy growth, fixed critical packets, and well-conditioned growing packets through and slightly beyond the square-root window all force positive nonsquarefree occupation. Generic shell regularity alone does not. Any proposed physical escape or proof must identify which exact source mechanism defeats or enforces these controls rather than infer pointwise rigidity from one proxy in isolation.