# Weil-inertia research lines

This file holds the current mathematical questions suggested by the durable Weil-inertia intuitions. It is not a roadmap, task queue, status page, or history.

## Control the finite negative sector without mistaking tail-floor saturation for progress

**Linked intuitions:** `MI-017-sliding-first-crossing-localization-produces-autocorrelation-symbols` through `MI-032-reserve-lifting-converts-the-frozen-essential-obstruction-into-a-finite-negative-index-problem`.

WI-304--WI-306 classify the frozen-reserve tail-dropped comparison and show that its first active prime already creates an essential negative band. WI-307 changes the architecture: because the unit-window archimedean symbol is unbounded above, the exterior reserve can be lifted at every fixed aperture, moving the essential spectrum positive and leaving only a finite discrete negative sector. WI-308 restores the omitted source exactly by clipping the source symbol, producing a positive tail multiplier.

WI-309 shows that an aperture-adaptive endpoint-singular localizer can make the retained tail floor uniform. WI-310 then identifies a hidden opposite cost in the **uncapped** split: the same reserve gate forces `B_L->infinity`, and the full localized clipped excess drives fixed-test Rayleigh quotients of the complementary comparison to `-infinity`. Capping the retained excess at `1/2` repairs that representation instability while preserving a uniform lower tail floor and finite negative index.

WI-311 now proves that the endpoint singularity is not the structural source of the uniform floor. At every fixed aperture, finitely many smooth real unit-window localizers with widely separated carrier frequencies can make the capped retained-tail operator satisfy

`1/2(1-1/(2N)-epsilon) I <= That_(L,N,epsilon) <= (1/2) I`,

so `That` can approach `(1/2)I` in operator norm. The exact source split then forces

`Dhat_(L,N,epsilon) -> Q-(1/2)I`

with the same norm accuracy. Thus the largest possible scalar floor is asymptotically saturable by smooth localization, but **improving that floor alone does not simplify the RH problem**: in the saturating regime the complementary operator becomes an arbitrarily small bounded perturbation of the original unknown source shifted by `-1/2`.

The live theorem is therefore not a stronger scalar retained-tail witness. It is a genuinely independent uniform control of the finite negative sector whose proof does not become equivalent to proving `Q>=0` after a near-constant subtraction. Any successful comparison must show that the compact/discrete part is easier for source-specific reasons that survive the exact identity `Q=D+T`.

## Track compact-sector complexity across both endpoint and modulation degenerations

WI-309 placed the uniform-tail cost in endpoint singularity. WI-311 shows that smooth frequency multiplexing can move that cost elsewhere: the carrier frequencies needed to flatten the capped tail become extremely large, derivatives of the localizers grow, and the aggregate autocorrelation becomes rapidly oscillatory. The compact localization correction may therefore deteriorate even though every individual window is smooth.

Future estimates must treat **endpoint regularity and modulation scale as alternative coordinate costs**, not infer structural progress from avoiding one of them. A source-valid family needs uniform control of the compact/discrete sector under whichever degeneration produces the tail floor. No result yet bounds the negative index or negative depth uniformly along the smooth multiplexed family.

## Keep compact certificate design separate from full Weil positivity

Finite-dimensional trial-subspace optimization remains downstream of the source-valid information-retention question. The capped source-exact decomposition supplies a bounded positive margin without an unbounded subtraction artifact, but WI-311 shows that even an almost maximal margin can be representationally empty when the complement converges to `Q-cI`. An arbitrary finite-rank patch chosen after observing negative modes is still not source-valid. Any certificate must be derived from the actual localized Weil operator and survive the aperture/complexity limit.

## Preserve the signed-density quotient

Even a successful bounded-tail reserve-lifted architecture must eventually survive the exact density-one cancellation of WI-241. A large positive reserve or retained arithmetic mass is not yet the required sign-producing discrepancy theorem; the RH-relevant source variable remains the signed discrepancy after universal prime main density and pole cancellation.
