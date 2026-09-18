# Prime-lattice research lines

This file holds the current mathematical questions suggested by the durable prime-lattice intuitions. It is not a roadmap, task queue, status page, or history.

## Move from local activation birth signs to the full completed low-state frequency balance

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

while `W_a=2e^a(1+o(1))`. Hence the isolated prime block `P_a=-K_a` has normalized edges `-1/2` and `+1/2`, and the positive jump sector `J_a=2W_aI-K_a` has normalized edges `3/2` and `5/2` at leading order.

PL-342 now proves that the sharp `+/-e^a` prime-block edges are not isolated smooth endpoint modes: they are already the **essential spectral edges** of `K_a`. Multiplying the PL-341 endpoint vectors by high common oscillations and using Kronecker recurrence on the finitely many active prime logarithms reproduces the same Rayleigh values on weakly-null sequences. Therefore

`sup sigma_ess(K_a)=e^a(1+o(1))`, `inf sigma_ess(K_a)=-e^a(1+o(1))`.

The zeta-pole completion term has rank at most two, and the bounded continuous completion remainder is compact at fixed aperture, so neither can lower this sharp prime-block scale in the Calkin quotient. This reconciles rather than contradicts the smooth pole cancellation of PL-059: the pole cancels the fixed smooth PNT boundary mode, while weakly-null recurrent copies make compact corrections asymptotically invisible.

The surviving obstruction is now precisely the part that is **not** compact. The full localized completed-Weil operator contains the unbounded logarithmic principal operator and has compact resolvent. The high oscillation frequencies used to realize the essential prime edge pay an increasing archimedean/logarithmic energy cost. Thus the RH-facing question is whether that unbounded frequency penalty, together with source-selected branch information and scalar compensation, suppresses the recurrent prime edge on the same relevant low states. No statement confined to the bounded PNT block or compact completion sector can decide that balance.

## Keep universal bulk coercivity distinct from rational-prime selectivity

The computer-assisted fixed-window claim recorded earlier remains non-peer-reviewed and not independently reproduced. Its structural warning remains useful: after enough channels are active, frequency-dependent signed structure can matter even when a large positive bulk is present.

PL-339 shows that scalable **positive-tail coercivity itself is not the missing resource**. PL-340 shows that joint compatibility cannot push that coercivity to the scalar-cancellation threshold. PL-341 completes the leading ordinary spectral picture, and PL-342 shows that the same half-source-mass edges survive modulo every bounded compact correction.

Those constants use only the positive PNT mass law, compressed-shift geometry, and finite rational independence of the active logarithmic frequencies. A matched generalized-prime source with the same PNT-scale weight and corresponding independent frequencies reproduces the mechanism. The sharp ordinary and essential prime-block spectra are therefore PNT-universal rather than rational-prime-specific.

A successful continuation must use structure beyond this universal bounded block: a same-state comparison between the logarithmic principal frequency cost and recurrent prime translation gain, rational-prime-specific mesoscopic/correlation constraints on the selected low branch, or a theorem propagating noncollapse/order through the activation sequence into the completed operator. Re-proving nonnegativity, coercivity, a better universal constant, or compact completion control would no longer address the live frontier.

## Keep transport, bounded-block spectrum and completed-state energy distinct

Norm-resolvent continuity transports eigenbranches; uniform jump-form boundedness controls the moving state and endpoint source; the antisymmetric Hopf argument fixes the threshold trace sign on the lowest odd branch; PL-338 converts that trace into favorable local activation signs; PL-339 keeps the accumulated jump sector coercive at total-mass scale; PL-340--PL-341 determine exactly how far the isolated block can go; PL-342 shows that this sharp block edge survives in essential spectrum and through compact completion.

None of these alone controls the full completed low spectrum. The recurrence witnesses of PL-342 leave the bounded prime sector unchanged at leading order precisely by moving to arbitrarily high frequency, where the unbounded logarithmic principal operator becomes expensive. The next theorem must therefore compare these two effects on the same moving states and connect that balance to the source-selected branch. Essential-spectrum survival of the bounded block is a stronger obstruction, but it is not a negative direction for the compact-resolvent completed operator.
