# Weil-inertia research lines

This file holds the current mathematical questions suggested by the durable Weil-inertia intuitions. It is not a roadmap, task queue, status page, or history.

## Control the finite negative sector against the exact clipped source-tail gap

**Linked intuitions:** `MI-017-sliding-first-crossing-localization-produces-autocorrelation-symbols` through `MI-032-reserve-lifting-converts-the-frozen-essential-obstruction-into-a-finite-negative-index-problem`.

WI-304--WI-306 exactly classify the frozen-reserve tail-dropped comparison. With Liu's support and `beta_0=1/16`, the first active prime already creates an essential negative band, and the compressed-translation numerical-radius bound is sharp. No same-width reshaping of the localizer repairs that fixed comparison.

WI-307 changes the architectural conclusion. The unit-window archimedean symbol is unbounded above, so at every fixed aperture `L` the exterior reserve can be raised to any prescribed `B` by moving the Fourier cutoff. The localized comparison becomes

`D_(L,chi,B)=B I-A_(L,chi)+K_(L,chi,B)`,

with `A_(L,chi)` the finite active prime-power translation sum and `K` compact. Choosing `B>||A_(L,chi)||` moves the essential spectrum strictly positive.

WI-308 now supplies the missing source-valid remainder structure at fixed aperture. Clipping the exact unit-window source symbol at `B` decomposes the full Weil form as

`Q = D_(L,chi,B) + T_(chi,B)`,

where the omitted tail becomes, after sliding localization, a Fourier multiplier with symbol

`r_(chi,B)(xi)=(1/(2 pi)) int q_B(t)|F_chi(t-xi)|^2 dt`

and has a **strictly positive global bottom** `c_(chi,B)=inf_xi r_(chi,B)(xi)>0`. Hence `T_(chi,B)>=c_(chi,B) I`. Positivity at fixed aperture is reduced to the finite discrete inequality

`lambda_min(D_(L,chi,B)) >= -c_(chi,B)`.

Conversely, a first-crossing zero mode under an RH failure must force `lambda_min(D)<=-c<0`; it cannot hide at zero margin in this clipped comparison. The live fixed-aperture problem is therefore no longer whether the omitted source can in principle pay for the discrete sector, but whether the actual finite negative eigenvalues obey this explicit source-tail budget.

## Make the clipped tail reserve effective and uniform as the aperture grows

The positive scalar `c_(chi,B)` is qualitative in WI-308. A global argument must quantify it jointly with `B`, the localizer and the outer aperture, while also tracking the norm and multiplicity of the active arithmetic translations. The Fourier cutoff needed to realize a large reserve can become expensive, and the finite negative sector can evolve with `L`.

The next useful result should therefore either derive an effective lower bound for `c_(chi,B)` and a matching upper control on the negative discrete spectrum that survives `L->infinity`, or prove a scale incompatibility that defeats **all** admissible choices of `B` and `chi`. Reusing the frozen `beta_0=1/16` essential-band obstruction as if the reserve were intrinsic is no longer valid.

## Keep compact certificate design separate from full Weil positivity

Finite-dimensional trial-subspace optimization remains certificate design downstream of the source-valid information-retention question. WI-303 shows that the rank of a finite Loewner minorant is not structural. WI-307--WI-308 sharpen the distinction: finite negative index plus an exact positive tail reserve produces a concrete spectral inequality, but neither side may be replaced by an arbitrary finite-rank patch chosen after seeing the negative modes.

## Preserve the signed-density quotient

Even a successful reserve-lifted/tail-retaining architecture must eventually survive the exact density-one cancellation of WI-241. The RH-relevant source variable is the signed discrepancy after the universal prime main density and pole cancel. A large positive reserve or retained arithmetic mass is not yet the required sign-producing discrepancy theorem.