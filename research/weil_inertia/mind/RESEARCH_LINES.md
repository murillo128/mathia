# Weil-inertia research lines

This file holds the current mathematical questions suggested by the durable Weil-inertia intuitions. It is not a roadmap, task queue, status page, or history.

## Control the recombined deep negative sector rather than total comparison inertia

**Linked intuitions:** `MI-017-sliding-first-crossing-localization-produces-autocorrelation-symbols` through `MI-032-reserve-lifting-converts-the-frozen-essential-obstruction-into-a-finite-negative-index-problem`.

WI-304--WI-306 classify the frozen-reserve tail-dropped comparison and show that its first active prime already creates an essential negative band. WI-307 changes the architecture: because the unit-window archimedean symbol is unbounded above, the exterior reserve can be lifted at every fixed aperture, moving the essential spectrum positive and leaving only a finite discrete negative sector. WI-308 restores the omitted source exactly by clipping the source symbol, producing a positive tail multiplier.

WI-309 shows that an aperture-adaptive endpoint-singular localizer can make the retained tail floor uniform. WI-310 then identifies a hidden opposite cost in the **uncapped** split: the same reserve gate forces the retained excess to diverge, and the complementary comparison develops arbitrarily deep discrete negative modes independently of RH. Capping the retained excess at `1/2` repairs that representation instability while preserving a uniform lower tail floor and finite negative index.

WI-311 proves that endpoint singularity is not the structural source of the uniform floor. At every fixed aperture, finitely many smooth real unit-window localizers with widely separated carrier frequencies can make the bounded retained-tail operator arbitrarily close to `(1/2)I`. But the exact split simultaneously makes the complementary comparison arbitrarily close to `Q-(1/2)I`. Thus **improving the scalar floor alone does not simplify the RH problem**: in the saturating regime the finite-sector question tracks the original unknown source after scalar subtraction.

WI-312 quantifies the compact-sector cost of that smooth flattening. Let `mu` be the aggregate frequency-energy law of the localizers and suppose its concentration function satisfies `Q_mu(h)<=eta`. For the continuous archimedean correction `C_R`, anti-concentration forces `||C_R||_HS^2` to grow at least on the scale `eta^(-1)`. Hence any smooth multiplexed family whose frequency law becomes sufficiently spread out to flatten the capped tail loses uniform componentwise Hilbert--Schmidt control.

WI-313 identifies the **correct inertia statistic** carried by the saturated split. If the retained tail satisfies `(1/2-delta)I <= T_hat <= (1/2)I` and `D_hat=Q-T_hat`, then variational min--max gives, for every source level `s`,

`N_Q(s-delta) <= N_(D_hat)(s-1/2) <= N_Q(s)`.

In particular total comparison inertia `n_-(D_hat)` tracks source spectrum below `1/2`, so positive source modes in `(0,1/2)` become false negative comparison modes. Source sign is instead encoded at the **deep compensation threshold** `c=1/2-delta`:

`N_Q(0) <= N_(D_hat)(-c) <= N_Q(delta)`.

The only false positives then come from the source window `[0,delta)`. Shrinking that sign-resolution window in the WI-311 smooth construction simultaneously costs `||C_R||_HS^2=Omega(delta^(-1))` for the continuous archimedean component.

The live theorem is therefore narrower and more source-aligned than “control the compact sector” or “make the negative index small.” A successful comparison must control the **recombined sector below the full compensation depth**, with spectral resolution tending to zero, through source-specific cancellation or another invariant that survives the aperture/complexity limit. Uniform componentwise `S_2` control is not required and is incompatible with the known smooth saturation mechanism; ordinary total negative index is not the RH-relevant statistic in that regime.

## Track sign resolution, compact complexity and recombination across endpoint, modulation and anti-concentration degenerations

WI-309 placed the uniform-tail cost in endpoint singularity. WI-311 shows that smooth frequency multiplexing can move that cost into high carrier frequencies. WI-312 proves that sufficiently strong frequency anti-concentration forces Hilbert--Schmidt blow-up quantitatively. WI-313 shows what that complexity is buying: a comparison sublevel that resolves source sign only within a `delta` spectral window.

Future estimates must therefore treat **endpoint regularity, modulation scale, frequency concentration, sign-resolution width and recombination** as separate resources. A source-valid family needs a uniform theorem for the final deep negative sector under whichever degeneration produces the tail floor; it cannot infer structural progress merely because individual windows remain smooth or because total comparison inertia is finite. Any claimed compact bound should state whether it is componentwise, after exact recombination, in operator norm, in a Schatten norm, or directly on the deep negative count.

## Keep compact certificate design separate from full Weil positivity

Finite-dimensional trial-subspace optimization remains downstream of the source-valid information-retention question. The capped source-exact decomposition supplies a bounded positive margin without an unbounded subtraction artifact, but WI-311 shows that even an almost maximal margin can be representationally empty, WI-312 shows that achieving it can force large componentwise compact complexity, and WI-313 shows that the relevant source-sign statistic is the comparison spectrum below the compensation threshold rather than the whole negative spectrum. An arbitrary finite-rank patch chosen after observing negative modes is still not source-valid.

## Preserve the signed-density quotient

Even a successful bounded-tail reserve-lifted architecture must eventually survive the exact density-one cancellation of WI-241. A large positive reserve or retained arithmetic mass is not yet the required sign-producing discrepancy theorem; the RH-relevant source variable remains the signed discrepancy after universal prime main density and pole cancellation.
