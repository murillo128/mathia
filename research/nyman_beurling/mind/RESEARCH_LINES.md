# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Push the canonical shell discrepancy toward a near-linear scale

**Linked intuition:** `MI-002-small-shell-discrepancy-can-destroy-rooted-visibility`.

The shell decomposition still reduces the useful rooted-mixing channel to a quantitative coefficient discrepancy. The live theorem remains whether the canonical arithmetic coefficients can force a near-linear discrepancy on the relevant shell family without assuming the Nyman distance estimate one is trying to prove.

## Connect localized directional mass to recursive target repair without paying an ambient RH norm

**Linked intuitions:** `MI-001-coefficient-geometry-needs-target-coupling`, `MI-003-low-gram-spectrum-is-cheap-target-occupation-is-the-signal`, `MI-004-weighted-tail-shell-quotient-is-a-conditioned-source-skeleton`.

NB-024--NB-045 separate source-faithful compression, exact target repair, ambient-dual hardness, and directional occupation. The weighted skeleton has polynomial conditioning and a sharp `Theta(1/M)` source-only target-loss floor; one target-selected line repairs it exactly. Polynomial ambient decay of the natural logarithmic dual measures the zeta zero frontier, but the complete bounded step-tail family reconstructs the finite distance through a positive logarithmic average.

NB-046--NB-047 make that directional information much more local. The partial-flow identity shows that an initial cutoff prefix already carries `(1+o(1)) d_N^2`. Using the classical Vinogradov--Korobov Mertens estimate moves a sufficient deterministic cutoff down to

`M_N = exp((log log N)^(5/3+epsilon))`,

up to the stated flexibility. Thus the Burnol-scale source signal is concentrated in a doubly-logarithmic-size directional prefix without requiring a polynomial ambient-dual estimate.

NB-048 supplies an independent recursive geometry. Dilating the best approximant from the smaller section `V_floor(N/M)` gives an explicit vector in the weighted tail whose squared error from the unique exact repair is exactly the slack in the recursive target-loss bound, and the resulting repaired skeleton satisfies

`0 <= d_tilde_(M,N)^2-d_N^2 <= d_floor(N/M)^2/M`.

The live bridge is now precise: determine whether the localized directional prefix can control this recursive repair slack, or an equivalent one-sided target certificate, **without reconstructing the full finite-section oracle or invoking an RH-equivalent ambient norm**. The directional localization and recursive repair are both exact, but their quantitative relation is not yet established.

## Treat source localization, target repair, ambient norm, and oracle recursion as separate gates

A small directional prefix can carry the full Burnol-scale aggregate while the exact geometric repair remains target-selected. A smaller-section projection can approximate that repair with explicit error, but it is itself an oracle unless its needed data are source-accessible more cheaply. Future arguments should preserve these distinctions rather than identify “few directional witnesses” with “cheap target reconstruction.”