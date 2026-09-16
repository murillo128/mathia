# Prime-lattice research lines

This file holds the current mathematical questions suggested by the durable prime-lattice intuitions. It is not a roadmap, task queue, status page, or history.

## Prove the source-amplitude gate for the actual shrinking first-prime eigenbranch

**Linked intuitions:** `MI-016-weil-form-observability-is-stronger-than-moment-observability` through `MI-025-source-amplitude-controls-first-prime-reflection`.

PL-313--PL-323 close the moving Green endpoint transfer at each fixed aperture. The exact source equation, conservative singular-kernel flux identity and positive jump-kernel maximum principle force the primitive critical coefficient and `Qm(Q)->0`; there is no remaining generic analytic task to manufacture a finite endpoint limit.

PL-324--PL-325 classify the first arithmetic activation. Positivity survives on the odd Weil sector exactly until `a=(1/2)log2`; immediately afterward the prime translation has the wrong modulus sign. In the first-prime window that translation is a two-edge flip with spectrum `{-1,0,1}` and infinite-dimensional `±1` sectors. Its bounded-operator norm jumps to one even though the coupling remains small relative to the singular endpoint form.

PL-326 shows why fixed-aperture asymptotics do not orient the first crossing: a moving antisymmetric bump on the width-`2delta` activation layer can reverse the reflected correlation while preserving the same critical endpoint germ. PL-327 identifies the generic regularity boundary: logarithmic Hölder exponent `alpha>1/2` with a vanishing normalized seminorm is sufficient, while the canonical `alpha=1/2` scale still permits sign reversal.

PL-329 supplies the first **source-selected quantitative mechanism** that excludes exactly that critical counterfamily. Write `L_delta=log(a_delta/delta)` and let `S_delta` be the sup norm of the exact endpoint source term. The source equation selects a coefficient `C_delta` and gives

`g_delta(Q)=C_delta Q^(-1/2) + O((1+S_delta)/Q) + O(exp(-eta Q))`.

Hence the first-prime reflection is eventually positive whenever

`(1+S_delta)/(|C_delta| sqrt(L_delta)) -> 0`.

The threshold is sharp for the PL-327 sign-reversing family: its critical residual is magnified by the coercive source equation into `S_delta asymp sqrt(L_delta)`.

PL-330 removes a different apparent obstruction without weakening this gate. The newly active edge-flip channel converges strongly but not in bounded-operator norm as `a -> (1/2)log2`. Because the threshold localized-Weil operator has compact resolvent, the full self-adjoint family is nevertheless **norm-resolvent continuous** across the first-prime activation; isolated spectral projections are norm-continuous, and simple eigenvectors can be transported continuously even in the fixed logarithmic graph norm.

But the PL-327 sign-reversing perturbation can itself be chosen to tend to zero in that graph norm while still reversing the shrinking reflected correlation. Thus the topology hierarchy is now sharp: bounded-operator norm is too strong and reports a fake source jump; norm-resolvent and logarithmic graph continuity are available but still too weak for the sign; the source-amplitude ratio of PL-329 measures the moving layer at the scale the destination actually consumes.

The live missing quantifier is therefore branch-specific rather than topological. Prove that the **actual completed-Weil eigenbranch** crossing the first-prime threshold satisfies the PL-329 source-amplitude condition, including non-collapse of `C_delta`. PL-330 means spectral transport through the activation is not the blocker, but continuity of the branch alone cannot supply the sign.

## Keep fixed-window certificates and scalable tail geometry separate

**Linked intuition:** `MI-024-fixed-window-certification-requires-frequency-dependent-tail-control`.

PL-328 records a recent non-peer-reviewed, not independently reproduced computer-assisted source claiming full complex-test Weil coercivity at `a=17/16`, with exact active prime-power list `2,3,4,5,7,8`. Through the common-form dictionary this would imply positivity for every smaller aperture **conditional on independent validation**; it is not promoted to reproduced Mathia evidence.

The same finding contains an exact structural warning independent of trusting the certificate: beyond the `8` threshold, dropping the frequency-dependent positive tail creates a phase-locked negative high-frequency defect that no fixed bounded compact correction repairs. A scalable proof therefore has to retain frequency-dependent positive information as arithmetic channels activate.

PL-329--PL-330 and PL-328 constrain different interfaces. The first pair says the initial eigenbranch can be transported spectrally across the first activation but still needs source-amplitude control to orient the shrinking reflection; the second says later multi-channel positivity cannot be propagated by replacing the high-frequency reserve with a scalar floor. A global theorem must control the selected state and the retained positive tail at every moving arithmetic scale.

## Keep fixed-aperture transport, moving-threshold uniformity, spectral topology, source amplitude and arithmetic orientation separate

The decisive topology distinction is now fivefold. Small overlap width is not small bounded-operator norm; strong convergence plus compact resolvent is enough for norm-resolvent spectral transport; graph-small perturbations can still dominate a much smaller moving sign reserve; canonical boundary regularity does not suppress the critical antisymmetric layer; and the exact source equation suppresses that layer only when its forcing amplitude is `o(|C_delta| sqrt(L_delta))`. The source gate is therefore genuinely finer than the natural spectral continuity available across the activation.
