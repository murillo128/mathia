# VIS-273 — fixed-`q` Wang probes sit exactly at the present derivative-budget boundary

## Claim

Let `L=log T` and use the logarithmic source coordinate from `VIS-272`,

`q = alpha L/(2*pi)`.

A smooth probe with **fixed nonzero width in `q`** necessarily pulls back to an `alpha`-test of width `Theta(1/L)`. Under the quantitative moving-test estimate extracted from Biao Wang's proof in `VIS-266`, that pullback sits exactly at the first-derivative boundary: the certified normalized remainder is only `O(1)`, not `o(1)`.

More precisely, fix a nonconstant `h in C_c^infinity((-B,B))` and a fixed source location `q_0>B>0`. Define

`g_T(alpha)=c_T h(alpha L/(2*pi)-q_0)`.

For all sufficiently large `T`, `g_T` is supported inside any fixed Wang margin `[-lambda,lambda]` with `0<lambda<theta`. Its seminorms are exactly

`||g_T||_infinity = |c_T| ||h||_infinity`,

`||g_T'||_infinity = |c_T| L/(2*pi) ||h'||_infinity`.

Substituting into the normalized family bound of `VIS-266` gives the proof-level majorant

`O_(lambda,theta)( |c_T| ||h'||_infinity/(2*pi)`
` + |c_T| ||h||_infinity [1/L + L^(-3/2) + T^(lambda-theta)L + 1/(T^theta L)] ).`

Hence for a fixed-amplitude source probe, `c_T -> c != 0`, the available bound does not tend to zero. The obstruction is already the derivative term: converting fixed `q` resolution to the Wang `alpha` coordinate costs exactly one factor of `L`, which cancels the `1/L` gain in the theorem interface.

Amplitude damping does not recover a normalized fixed-`q` observable. Taking `c_T -> 0` makes the displayed proof error vanish, but dividing the statistic by `c_T` to restore the original fixed-`q` functional restores the same order-one derivative majorant.

Thus the Green-kernel source dictionary of `VIS-272` is **not yet theorem-accessible by direct fixed-`q` localization through Wang's current moving-test bound**. Any successful transfer needs an improvement that exploits additional structure beyond the `||g'||_infinity/L` estimate, an integrated identity whose error avoids this derivative loss, or a different theorem interface.

**Evidence/status:** `EXACT-DERIVED + LITERATURE-TRANSFER COROLLARY + THEOREM-INTERFACE OBSTRUCTION + NO-NOVELTY-CLAIM`.

This is not a lower bound on the true pair-correlation error and does not prove that a fixed-`q` asymptotic is false. It proves only that the presently audited Wang proof estimate does not certify such localization with vanishing normalized error.

## 1. Fixed source resolution becomes `1/L` frequency resolution

The source coordinate in `VIS-272` is

`q=log x/(2*pi)`.

Inside Wang's pair-correlation parameterization `x=T^alpha`, this becomes

`q=alpha L/(2*pi)`.

Therefore the fixed source window

`q in [q_0-B,q_0+B]`

pulls back to

`alpha in [2*pi(q_0-B)/L, 2*pi(q_0+B)/L]`.

Its center and width are both `Theta(1/L)`. This is the precise shrinking regime that `VIS-271` identified qualitatively when it observed that a fixed prime source corresponds to `alpha_T=log p/L`.

The point is independent of the particular bump shape. Any fixed smooth profile in `q` acquires one factor of `L` in its first `alpha` derivative by the chain rule.

## 2. Wang's current seminorm estimate loses exactly that factor

`VIS-266` extracted from Wang's proof, for fixed `0<lambda<theta<1`, the normalized family estimate

`Err_T(g_T)`
` = O_(lambda,theta)( ||g_T'||_infinity/L`
` + ||g_T||_infinity [1/L + L^(-3/2) + T^(lambda-theta)L + 1/(T^theta L)] ).`

For

`g_T(alpha)=c_T h(alpha L/(2*pi)-q_0)`,

one has

`g_T'(alpha)=c_T L/(2*pi) h'(alpha L/(2*pi)-q_0)`.

Hence

`||g_T'||_infinity/L = |c_T| ||h'||_infinity/(2*pi)`.

Every other displayed term tends to zero relative to fixed `|c_T|` because `lambda<theta` gives a fixed power saving. The derivative contribution is therefore the unique critical term in this pullback.

For `c_T=1`, the proof supplies only an order-one remainder majorant. It does not establish

`Err_T(g_T)=o(1)`.

This is exactly the amplitude-bounded endpoint of the scaling discussion already implicit in `VIS-266`: a bump of width `b=L^(-1)` has derivative scale `b^(-1)=L`, so the theorem's `1/L` derivative budget is fully consumed.

## 3. Damping the test does not solve normalized recovery

One may try

`c_T -> 0`.

Then the theorem majorant is `O(|c_T|)` and does vanish. But this merely attenuates the entire observable. If the desired source functional is the one associated with the undamped profile `h`, one must divide the measured quantity by `c_T`. The resulting certified error majorant is again

`O_(lambda,theta)( ||h'||_infinity/(2*pi) + o(1) ).`

Thus scalar amplitude damping cannot buy fixed-`q` resolution after normalization. A genuine improvement must come from cancellation or structure in the error itself, not from shrinking the whole test.

The same conclusion is stronger for mass-normalized or moment-normalized packets. Those require amplitudes growing with the shrinking `alpha` width, so their `||g_T||_infinity` and `||g_T'||_infinity` costs are larger. `VIS-267` quantifies that phenomenon for unit even-moment carriers; the present result isolates the simpler obstruction that already appears before any such carrier normalization.

## 4. Consequence for the Green bridge

`VIS-272` showed that Wang's source diagonal energy

`A(q)=int exp(-4*pi|q-xi|) dmu(xi)`

contains exactly the Rodgers weighted prime-power measure and that

`mu=(16*pi^2-d_q^2)A/(8*pi)`

distributionally. For a fixed smooth `q`-test `psi`, the corresponding integrated source functional is a fixed-width pairing against `A(q)` or, after adjoint Green inversion, against derivatives of `psi`.

Pulling any such fixed `q` profile directly into Wang's `alpha` variable produces the same `Theta(1/L)` support scale and `Theta(L)` first derivative. Therefore the existing pair-correlation proof estimate does not by itself provide the vanishing error needed to evaluate that fixed-source functional asymptotically.

This sharpens the theorem-level bottleneck left open in `VIS-272`. The missing ingredient is not merely a vague form of "uniformity as alpha tends to zero." The required source resolution lies at a concrete critical scale where the current first-derivative error bookkeeping loses its asymptotic gain.

## 5. Prior-art and novelty boundary

The external analytic input is Biao Wang, **Simple critical zeros and distinct zeros of the Riemann zeta-function in short intervals**, arXiv:2609.07918v1 (2026), through the proof-level family estimate already audited and persisted in `VIS-266`.

The source-coordinate relation `q=alpha log T/(2*pi)` and the Wang-to-Rodgers Green dictionary are persisted in `VIS-271` and `VIS-272`. The present finding is their direct composition with the `||g'||_infinity/L` theorem interface.

The chain-rule scaling and the conclusion that an `O(1/L)` derivative budget is exhausted by a width-`1/L` pullback are elementary. No novelty is claimed for that analytic observation, for moving-test rescaling, or for the general principle that localization costs derivative norms. The durable content is the exact Mathia transfer boundary for the currently active Wang/Rodgers bridge.

A targeted check of Wang's current arXiv source confirms that the paper establishes the short-interval pair-correlation theorem used by this branch; this finding does not claim that the paper states the fixed-`q` obstruction in this form.

## 6. Boundaries and falsification

The result concerns the **present audited proof estimate**, not the optimal truth. It would be evaded by a stronger estimate whose error depends on a norm invariant under the `q` pullback, by cancellation showing that the derivative contribution is absent for the exact source-functional class, or by an integrated explicit-formula argument that accesses the Green pairing without localizing through `g_T` in this way.

The fixed outer support condition is harmless here: the pulled-back support shrinks toward `alpha=0`, so it lies deep inside every fixed `[-lambda,lambda]` for large `T`. The obstruction is therefore distinct from the moving support-edge problem of `VIS-265`.

The claim would need correction if the quantitative family estimate in `VIS-266` is strengthened or found to overstate the derivative loss for this special class. Such a refinement should replace this interface obstruction rather than be hidden inside it.

No untouched confirmation-zero data are used.

## Research consequence

The direct route "use Wang's existing moving-test estimate on a fixed-width `q` window and then apply the `VIS-272` Green dictionary" is now sharply closed at the level of currently certified error: fixed source resolution consumes the full derivative budget.

The next useful theorem question is correspondingly specific. One must either derive a **structure-sensitive integrated Wang estimate** for the fixed-`q` Green-adjoint functional with `o(1)` normalized error, or improve the local moving-test bound so that a width-`Theta(1/L)` pullback gains more than the present `1/L` derivative factor. Merely changing bump amplitude, adding another coordinate reformulation, or invoking the existing fixed-margin theorem does not cross this boundary.
