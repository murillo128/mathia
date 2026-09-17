# Prime-lattice research lines

This file holds the current mathematical questions suggested by the durable prime-lattice intuitions. It is not a roadmap, task queue, status page, or history.

## Move from local activation birth signs to global branch and compensation control

**Linked intuitions:** `MI-016-weil-form-observability-is-stronger-than-moment-observability` through `MI-030-pnt-endpoint-modes-cap-jump-only-coercivity-before-completion`.

The moving endpoint problem is no longer blocked by a generic concentration estimate. The source equation, norm-resolvent branch transport, the odd reflected Hopf mechanism and the jump-form `L^infty` estimate together control the first-prime threshold on the selected odd branch.

PL-338 extends the local mechanism to every finite prime-power activation `q=p^k`. Norm-resolvent continuity survives the jump, the newly active reflected correlation is universally first-order flat, `P_q=O(delta/L_delta)`, and whenever the transported boundary coefficient has nonzero limit,

`P_q ~ 4 Lambda(q)/sqrt(q) C_0^2 delta/L_delta > 0`.

Thus later activation births do not introduce a new local concentration obstruction. Each finite channel is born favorably provided its branch trace does not collapse.

PL-339 closes a separate many-channel concern. The zero-exterior compressed translation has the exact path-chain gap

`D_h=2I-S_h-S_h* >= [2-2 cos(pi/(ceil(2/h)+1))] I`.

Every source in the outer logarithmic half-window `1<=h<2` has unit gap, and that shell carries asymptotically all weighted von-Mangoldt mass. Consequently the positive jump sector satisfies `J_a >= (1-o(1))W_a I`. Accumulating more active prime powers therefore does not dilute the favorable atomic sector relative to total source mass.

PL-340 shows that this positive bulk cannot reach the `2W_a` scalar-cancellation threshold by compatibility alone. PL-341 sharpens that ceiling to the full leading PNT spectrum. If `K_a` is the weighted compressed-shift sum, then

`sup sigma(K_a)=e^a(1+o(1))`, `inf sigma(K_a)=-e^a(1+o(1))`,

while `W_a=2e^a(1+o(1))`. Hence the isolated prime block `P_a=-K_a` has normalized edges `-1/2` and `+1/2`, and the positive jump sector `J_a=2W_aI-K_a` has normalized edges `3/2` and `5/2`. The favorable jump edge therefore remains exactly `W_a/2` below the scalar compensation scale.

What remains is global but narrower: prove persistence/ordering and trace noncollapse for the relevant branch, and control the scalar compensation plus completion strongly enough to convert the sharp universal prime-block spectrum into a destination sign. No refinement confined to the same PNT-scale jump geometry can close the fixed half-mass deficit.

## Keep universal bulk coercivity distinct from rational-prime selectivity

The computer-assisted fixed-window claim recorded earlier remains non-peer-reviewed and not independently reproduced. Its structural warning remains useful: after enough channels are active, frequency-dependent signed structure can matter even when a large positive bulk is present.

PL-339 shows that scalable **positive-tail coercivity itself is not the missing resource**. PL-340 shows that joint compatibility cannot push that coercivity to the scalar-cancellation threshold. PL-341 completes the leading picture: the isolated PNT prime block occupies asymptotically the half-source-mass spectral interval `[-W_a/2,W_a/2]`, while the jump block occupies `[3W_a/2,5W_a/2]` at leading order.

Those constants use only the positive PNT mass law and the compressed-shift geometry. A matched generalized-prime source with the same PNT-scale weight reproduces them. The sharp spectrum is therefore PNT-universal rather than rational-prime-specific.

A successful continuation must use structure beyond this universal block: cancellation/control of `-2W_aI` against the completion, a rational-prime-specific mesoscopic or correlation constraint on the selected low branch, or a theorem propagating noncollapse/order through the activation sequence. Re-proving nonnegativity, coercivity, or a better universal constant for the accumulated jump term would no longer address the live frontier.

## Keep transport, state bounds, sign orientation and destination positivity distinct

Norm-resolvent continuity transports eigenbranches; uniform jump-form boundedness controls the moving state and endpoint source; the antisymmetric Hopf argument fixes the threshold trace sign on the lowest odd branch; PL-338 converts that trace into favorable local activation signs; PL-339 keeps the positive accumulated jump sector coercive at total-mass scale; PL-340--PL-341 show exactly how far that isolated block can go before completion.

None of these alone gives a globally positivity-preserving completed semigroup or proves the final Weil destination. The next theorem must connect branch persistence and the signed compensation/completion geometry to a rational-prime-specific discriminator rather than reopen already-closed local or PNT-universal bulk gates.
