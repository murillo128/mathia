# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Force target-bearing geometry with an arithmetic local source law

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale` through `MI-031-euler-product-poisson-mass-is-a-local-confluence-budget`.

NB-123--NB-140 separate recurrence visibility, raw conditioning, coordinate choice and target occupation. Near-confluent simple-zero packets can remain target-poor even when recurrence information is visible and the state span is described in stable confluent coordinates.

NB-141 shows that strong global zero-density rarity does not eliminate a sparse sequence of dangerous logarithmic-rank cells. NB-142 identifies their scalar source bill: on polynomially short intervals a cell with `c log G` zeros forces an order-`log G` positive increment of the zero-count remainder. NB-143 then shows that generic xi-type analytic realizability, the functional equation and the imported coarse zero laws still permit such target-poor packets.

NB-144 supplies the first quantitative local discriminator from the actual arithmetic half-plane source. For a polynomially small right-half cell centered at `beta_0=1-epsilon`, positivity of the zero Poisson kernel together with the absolutely convergent Euler product on `Re s>1` gives

`d_G <= (epsilon(1-epsilon)/2+o(1)) log G`.

If the center approaches the one-line with `epsilon_G log G -> infinity`, the same argument gives `d_G <= (1/2+o(1)) epsilon_G(1-epsilon_G) log G`, hence `d_G=o(log G)` when `epsilon_G->0`. The Vinogradov--Korobov region supplies the required lower scale for actual zeta zeros. NB-144 also gives explicit parameters for which the NB-143 xi-type control admits a logarithmic packet that the actual Euler-product source forbids.

This is genuine progress but not closure. At every fixed interior `epsilon>0` the Poisson budget still allows a positive multiple of `log G`, so the target-poor geometry survives in a nonempty fixed-interior regime. The live theorem is now sharper: improve the one-point Euler-product budget to `o(log G)` at fixed interior location, extract a stronger multi-point/source relation, or prove directly that any crowded actual cell surviving the Poisson budget must carry non-negligible Nyman-target projection.

## Push the canonical shell discrepancy toward a near-linear scale

**Linked intuition:** `MI-002-small-shell-discrepancy-can-destroy-rooted-visibility`.

The shell decomposition still reduces the rooted-mixing channel to a quantitative coefficient discrepancy. The live theorem is whether the canonical arithmetic coefficients can force near-linear discrepancy on the relevant shell family without assuming the Nyman distance estimate one is trying to prove.

## Keep recurrence order, conditioning, subspace geometry, target occupation and source realizability separate

Visibility of a packet, stable coordinates for its state span, xi-type entire realizability and realizability by the actual zeta source are different resources. NB-144 proves that the last distinction is quantitatively visible: the Euler product imposes a positive local Poisson-mass budget not shared by the synthetic xi-type control. But source realizability still does not equal target occupation; the fixed-interior budget leaves logarithmic-rank packets possible. Any closing argument must state which additional arithmetic property either removes those packets or forces them to become target-bearing.