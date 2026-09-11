# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Push the canonical shell discrepancy toward a near-linear scale

**Linked intuition:** `MI-002-small-shell-discrepancy-can-destroy-rooted-visibility`.

The shell decomposition still reduces the rooted-mixing channel to a quantitative coefficient discrepancy. The live theorem remains whether the canonical arithmetic coefficients can force near-linear discrepancy on the relevant shell family without assuming the Nyman distance estimate one is trying to prove.

## Relate localized source direction to the continuous-versus-natural target gap

**Linked intuitions:** `MI-001-coefficient-geometry-needs-target-coupling`, `MI-003-low-gram-spectrum-is-cheap-target-occupation-is-the-signal`, `MI-004-weighted-tail-shell-quotient-is-a-conditioned-source-skeleton`.

NB-024--NB-048 separate source-faithful compression, exact target repair, ambient-dual hardness, and directional occupation. The Burnol-scale directional signal localizes to a small prefix while the exact weighted-tail repair is a target projection.

NB-049 shows ambient-norm localization turns on only when `M d_N^2 -> infinity`, exactly where the unrepaired weighted skeleton is already relatively lossless. In the critical corridor, any bridge must exploit orientation/cancellation rather than an ambient norm product.

NB-050 identifies the recursive repair slack exactly as the finite enrichment gap between the reciprocal-integer section `V_K` and the denser grid `C_(M,N)=span{rho_(M/n)}`:

`widetilde d_(M,N)^2-d_N^2=(d_K^2-delta_(M,N)^2)/M`.

NB-051 shows this is not generically a vanishing mesh error. In the two-scale regime `M->infinity`, `N/M->infinity`, the numerator converges to the fixed global target-projection gap

`Delta_* = d_nat^2-d_cont^2`,

between the natural Báez-Duarte closure and the full continuous Nyman closure; at fixed aspect ratio the enrichment can stay uniformly nontrivial. The first-order `1/M` repair slack therefore carries a genuine target component, not merely discretization noise.

The live bridge is now sharper: determine whether the localized source-direction data constrain `Delta_*` or its finite approximants in a target-useful way, without solving the target projection problem or importing an RH-equivalent norm estimate.

## Treat source localization, ambient norm, finite-grid enrichment, and closure-level target gap as separate gates

A tiny source witness does not make the target oracle cheap. The denser weighted-tail grid can contain a stable extra target direction even as its mesh refines. Future work should explain that direction from source structure rather than assume it disappears by discretization.