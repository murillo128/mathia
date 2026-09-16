# Weil-inertia research lines

This file holds the current mathematical questions suggested by the durable Weil-inertia intuitions. It is not a roadmap, task queue, status page, or history.

## Control the source-aligned deep sector with the correct order of limits

**Linked intuitions:** `MI-017-sliding-first-crossing-localization-produces-autocorrelation-symbols` through `MI-033-fixed-cap-threshold-recovers-inertia-only-after-cofinal-saturation`.

WI-304--WI-306 classify the frozen-reserve tail-dropped comparison and show that its first active prime already creates an essential negative band. WI-307 changes the architecture: because the unit-window archimedean symbol is unbounded above, the exterior reserve can be lifted at every fixed aperture, moving the essential spectrum positive and leaving only a finite discrete negative sector. WI-308 restores the omitted source exactly by clipping the source symbol, producing a positive tail multiplier.

WI-309 shows that an aperture-adaptive endpoint-singular localizer can make the retained tail floor uniform. WI-310 then identifies the opposite cost in the uncapped split: the same reserve gate forces retained excess to diverge and the complementary comparison develops arbitrarily deep negative modes independently of RH. Capping the retained excess at `1/2` removes that representation artifact.

WI-311 proves that endpoint singularity is not the structural source of the uniform floor. At every fixed aperture, finitely many smooth real unit-window localizers with widely separated carrier frequencies can make the bounded retained-tail operator arbitrarily close to `(1/2)I`; the exact split simultaneously makes the complement arbitrarily close to `Q-(1/2)I`. WI-312 quantifies the compact-sector price: strong frequency anti-concentration forces Hilbert--Schmidt growth of the continuous archimedean correction.

WI-313 identifies the moving-floor sign statistic. If `(1/2-delta)I <= T_hat <= (1/2)I` and `D_hat=Q-T_hat`, then

`N_Q(0) <= N_D_hat(-1/2+delta) <= N_Q(delta)`.

This has no false negatives for source-negative directions but may count source spectrum in `[0,delta)`.

WI-314 supplies the complementary fixed-cap statistic:

`N_Q(-delta) <= N_D_hat(-1/2) <= N_Q(0)`.

It has **no false positives** and can only miss source-negative directions of depth at most `delta`. For any cofinal saturation `delta_j->0` at one fixed aperture,

`N_Q(0)=sup_j N_(D_j)(-1/2)`, 

and finite source negative index is eventually recovered exactly. Thus positive source spectrum near zero is not the fundamental obstruction once the fixed cap is used.

The remaining obstruction is the **changing-source limit**. A single diagonal choice `delta_L->0` while the aperture changes to `Q_L` need not detect negativity: the source-negative margin can collapse faster than the cap defect. The live theorem must therefore control source-tail alignment across aperture—through a uniform negative-depth bound, a vectorwise cap-defect estimate on the negative sector, or cofinal saturation at each fixed aperture before the source changes. Scalar floor improvement alone is insufficient.

## Track sign resolution, compact complexity and recombination across endpoint, modulation and aperture limits

WI-309 placed the uniform-tail cost in endpoint singularity. WI-311 moves it into high carrier frequencies, WI-312 proves an anti-concentration/compact-complexity tradeoff, and WI-313--WI-314 identify what that complexity buys: two complementary comparison thresholds bracketing strict source negative index from opposite sides.

Future estimates must keep **endpoint regularity, modulation scale, frequency concentration, sign-resolution width, source-negative margin, aperture, saturation order and exact recombination** as separate resources. Uniform componentwise `S_2` control is not required and is incompatible with the known smooth saturation mechanism; ordinary total negative index is not the RH-relevant statistic; and a diagonal saturation schedule is not a substitute for controlling the source margin as the aperture changes.

## Keep compact certificate design separate from full Weil positivity

Finite-dimensional trial-subspace optimization remains downstream of the source-valid information-retention question. The capped source-exact decomposition supplies bounded positive margin without an unbounded subtraction artifact, while WI-314 gives an exact fixed-aperture inertia recovery law. Neither fact solves the finite-to-global passage: a certificate must remain source-valid under the aperture/saturation limit rather than infer global positivity from one chosen comparison scale.

## Preserve the signed-density quotient

Even a successful bounded-tail reserve-lifted architecture must eventually survive the exact density-one cancellation of WI-241. A large positive reserve or retained arithmetic mass is not yet the required sign-producing discrepancy theorem; the RH-relevant source variable remains the signed discrepancy after universal prime main density and pole cancellation.
