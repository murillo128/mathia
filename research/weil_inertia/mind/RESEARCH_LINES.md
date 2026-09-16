# Weil-inertia research lines

This file holds the current mathematical questions suggested by the durable Weil-inertia intuitions. It is not a roadmap, task queue, status page, or history.

## Control the finite negative sector for a bounded retained-tail comparison

**Linked intuitions:** `MI-017-sliding-first-crossing-localization-produces-autocorrelation-symbols` through `MI-032-reserve-lifting-converts-the-frozen-essential-obstruction-into-a-finite-negative-index-problem`.

WI-304--WI-306 classify the frozen-reserve tail-dropped comparison and show that its first active prime already creates an essential negative band. WI-307 changes the architecture: because the unit-window archimedean symbol is unbounded above, the exterior reserve can be lifted at every fixed aperture, moving the essential spectrum positive and leaving only a finite discrete negative sector. WI-308 restores the omitted source exactly by clipping the source symbol, producing a positive tail multiplier.

WI-309 shows that an aperture-adaptive endpoint-singular localizer can make the retained tail floor uniform while the essential spectrum stays positive. However WI-310 identifies a hidden opposite cost in the **uncapped** split. The same reserve gate forces `B_L->infinity`, and the full localized clipped excess grows like `1/eta_B` on every fixed bounded frequency window. Therefore

`Q=D_(L,chi_B,B)+T_(chi_B,B)`

with the full unbounded retained tail necessarily drives fixed-test Rayleigh quotients of `D` to `-infinity` along the adaptive family. The uncapped comparison manufactures arbitrarily deep discrete negative modes regardless of RH, so a uniform bound on that `D` is the wrong endgame.

WI-310 gives an exact repair. Replace the retained excess by

`qhat_B=min((sigma_1-B)_+,1/2)`.

The source identity remains exact,

`Q=Dhat_(L,chi_B,B)+That_(chi_B,B)`,

while the retained-tail operator now satisfies the uniform two-sided bound

`1/(64 pi e) I <= That <= (1/2) I`.

The lower edge from WI-309 survives because the cap equals `1/2` on the exterior region used in that argument, but the upper bound prevents the representation itself from injecting unbounded negative depth into `Dhat`. Moreover `Dhat>=D`, so the reserve gate still leaves only a finite negative sector at each aperture.

The live theorem is therefore **uniform control of the finite negative spectrum of the capped comparison**, not a stronger tail floor and not a lower bound for the uncapped `D`. Under an RH failure the first-crossing mode still forces a negative direction of depth at least `1/(64 pi e)`; a positive strategy must rule out such a direction for the source-valid capped family, while an impossibility result must show that the compact/discrete sector defeats every admissible bounded-tail reserve/localizer architecture.

## Track localizer singularity and compact-sector complexity without retained-tail overcharge

Endpoint-singular localization remains the mechanism that keeps a uniform source-tail witness, and its compact correction can still lose regularity as the singularity approaches the `L^2` boundary. But WI-310 separates that genuine compact-sector difficulty from a coordinate artifact: letting the retained positive tail grow without bound automatically forces the complementary comparison negative.

Future estimates should therefore use a bounded retained-tail split (or prove an equivalent representation-stability property) before interpreting negative eigenvalue depth/multiplicity. A representation whose positive summand diverges while the source form stays fixed is not evidence of an arithmetic obstruction in the complementary summand.

## Keep compact certificate design separate from full Weil positivity

Finite-dimensional trial-subspace optimization remains downstream of the source-valid information-retention question. The capped source-exact decomposition supplies a fixed positive margin without an unbounded subtraction artifact, but an arbitrary finite-rank patch chosen after observing negative modes is still not source-valid. Any certificate must be derived from the actual adaptive localized Weil operator and survive the aperture limit.

## Preserve the signed-density quotient

Even a successful bounded-tail reserve-lifted architecture must eventually survive the exact density-one cancellation of WI-241. A large positive reserve or retained arithmetic mass is not yet the required sign-producing discrepancy theorem; the RH-relevant source variable remains the signed discrepancy after universal prime main density and pole cancellation.
