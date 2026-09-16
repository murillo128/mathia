# Prime-lattice research lines

This file holds the current mathematical questions suggested by the durable prime-lattice intuitions. It is not a roadmap, task queue, status page, or history.

## Prove the source-amplitude gate for the actual shrinking first-prime eigenbranch

**Linked intuitions:** `MI-016-weil-form-observability-is-stronger-than-moment-observability` through `MI-025-source-amplitude-controls-first-prime-reflection`.

PL-313--PL-323 close the moving Green endpoint transfer at each fixed aperture. The exact source equation, conservative singular-kernel flux identity and positive jump-kernel maximum principle force the primitive critical coefficient and `Qm(Q)->0`; there is no remaining generic analytic task to manufacture a finite endpoint limit.

PL-324--PL-325 classify the first arithmetic activation. Positivity survives on the odd Weil sector exactly until `a=(1/2)log2`; immediately afterward the prime translation has the wrong modulus sign. In the first-prime window that translation is a two-edge flip with spectrum `{-1,0,1}` and infinite-dimensional `±1` sectors. Its operator norm jumps to one even though the coupling remains small relative to the singular endpoint form.

PL-326 shows why fixed-aperture asymptotics do not orient the first crossing: a moving antisymmetric bump on the width-`2delta` activation layer can reverse the reflected correlation while preserving the same critical endpoint germ. PL-327 identifies the generic regularity boundary: logarithmic Hölder exponent `alpha>1/2` with a vanishing normalized seminorm is sufficient, while the canonical `alpha=1/2` scale still permits sign reversal.

PL-329 now supplies the first **source-selected quantitative mechanism** that excludes exactly that critical counterfamily. Write `L_delta=log(a_delta/delta)` and let `S_delta` be the sup norm of the exact endpoint source term. The source equation selects a coefficient `C_delta` and gives the uniform tail expansion

`g_delta(Q)=C_delta Q^(-1/2) + O((1+S_delta)/Q) + O(exp(-eta Q))`.

On the shrinking first-prime layer this implies

`||r_delta||_2 << sqrt(delta) ((1+S_delta)/L_delta + exp(-eta L_delta))`.

Hence the first-prime reflection is eventually positive whenever

`(1+S_delta)/(|C_delta| sqrt(L_delta)) -> 0`.

The threshold is sharp for the PL-327 sign-reversing family: a residual of critical state amplitude `L_delta^(-1/2)` is amplified by the coercive `2Qm` term into source amplitude `S_delta asymp sqrt(L_delta)`. Thus the generic obstruction does **not** survive a sub-square-root-log source bound relative to the leading coefficient.

The live missing quantifier is now branch-specific rather than generic regularity. Prove that the **actual completed-Weil state/eigenbranch** crossing the first-prime threshold satisfies the PL-329 source-amplitude condition (or a stronger direct reflection estimate), including non-collapse of `C_delta`, across the operator-norm-discontinuous activation. If that gate is established, the known moving-layer counterexamples are excluded for a source reason rather than by imposing ad hoc smoothness.

## Keep fixed-window certificates and scalable tail geometry separate

**Linked intuition:** `MI-024-fixed-window-certification-requires-frequency-dependent-tail-control`.

PL-328 records a recent non-peer-reviewed, not independently reproduced computer-assisted source claiming full complex-test Weil coercivity at `a=17/16`, with exact active prime-power list `2,3,4,5,7,8`. Through the common-form dictionary this would imply positivity for every smaller aperture **conditional on independent validation**; it is not promoted to reproduced Mathia evidence.

The same finding contains an exact structural warning independent of trusting the certificate: beyond the `8` threshold, dropping the frequency-dependent positive tail creates a phase-locked negative high-frequency defect that no fixed bounded compact correction repairs. A scalable proof therefore has to retain frequency-dependent positive information as arithmetic channels activate.

PL-329 and PL-328 constrain different interfaces. The first gives a sharp source-amplitude criterion for orienting the **first** moving prime reflection; the second says later multi-channel positivity cannot be propagated by replacing the high-frequency reserve with a scalar floor. A global theorem must control the selected state and the retained positive tail at every moving arithmetic scale.

## Keep fixed-aperture transport, moving-threshold uniformity, source amplitude and arithmetic orientation separate

The decisive topology distinction is now fourfold. Small overlap width is not small bounded-operator norm; endpoint form control can be small while the destination sign is smaller still; canonical boundary regularity does not suppress a moving critical layer; and the exact source equation can suppress that layer only when its amplitude is `o(|C_delta| sqrt(L_delta))`. This source gate is a genuine advance, but it is not yet known for the actual eigenbranch and does not by itself extend through later prime-power activations.
