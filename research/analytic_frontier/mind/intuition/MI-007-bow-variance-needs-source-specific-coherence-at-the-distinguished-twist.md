# MI-007 — Bow completion is a phase-sensitive endpoint-local correlation problem

**Evidence level:** supported

## Core intuition

The bow endpoint obstruction is not determined by moving-window energy alone. Target-sized completion forces a large **positive real** dyadic shifted correlation at the distinguished logarithmic twist. A single positive moving-window square function is a useful necessary witness, but it discards the angular alignment between the current coefficient and its preceding block sum.

At the exact target scale this loss can be decisive: a packet may have maximal complex coherence and large square energy while its real endpoint correlation vanishes because the two factors are almost in quadrature. However, phase sensitivity is not incompatible with positivity itself. The signed shell can be recovered exactly from the **scale variation of a positive Fejer family**. What fails is a standalone phase-blind positive statistic, not every positive-energy representation.

## Strongest justified claim

ANF-157 writes bow variance exactly as positive Fejer source energy minus an endpoint-completion square. ANF-158--ANF-168 show that increasingly strong coefficient-generic interval, activity, centering, and carrier controls still allow target-sized endpoint completion. ANF-169 then proves that such completion forces one endpoint and one dyadic lag shell to satisfy a positive real shifted-correlation lower bound.

ANF-170 rewrites the shell as

`S_H = sum_m (1-m/K) b_m overline(B_H(m))`

with moving-window sum `B_H(m)`, and Cauchy--Schwarz yields `|S_H|^2 <= A Q_H`. This makes `Q_H` a positive necessary witness. ANF-171 shows the implication cannot be reversed even at the danger scale: a constant-modulus geometric packet can satisfy `|S_H|^2/(A Q_H) -> 1` while `Re S_H/sqrt(A Q_H) -> 0`, with negligible endpoint completion. Defining

`alpha_H = Re S_H / sqrt(A Q_H)`

isolates the datum lost by the single-scale relaxation.

ANF-172 supplies a phase-faithful positive representation. For the endpoint lag ledger define

`F_L = A + 2 sum_{h<L} (1-h/L) Re G_h >= 0`

and `T_L=L F_L`, `D_L=T_L-T_{L-1}`. Then exactly

`D_{2H}-D_H = 2 Re S_H`.

Moreover `F_L` is a positive average of squared coefficient sums over intersections of endpoint prefixes with ordinary length-`L` intervals. For the physical source these are exact twisted sums of `r_X=vartheta-Q_R`; the prime-minus-Ramanujan cancellation remains coupled inside each square.

## Synthesis of evidence

The sequence ANF-169--ANF-172 separates four levels that must not be conflated: signed endpoint correlation, complex coherence, single-scale positive moving-window energy, and a coupled positive scale family. The first is the decision statistic entering completion; the second can be large with the wrong phase; the third forgets phase completely; the fourth retains it through a discrete scale-slope defect.

This changes the source-side interface without changing the information boundary. A theorem making `A Q_H` subcritical is still sufficient, but stronger than necessary. A direct estimate of `Re S_H` is exact but expands naturally into a signed shifted correlation. ANF-172 gives an equivalent phase-faithful option in which the arithmetic residual remains inside positive short-interval squares, at the price of requiring **adjacent-scale precision** rather than a bound at one scale.

For the physical residual `r_X=vartheta-Q_R`, the durable target is therefore either a source-faithful signed dyadic estimate or a coupled Fejer/Selberg scale-increment theorem. A positive second-moment estimate is useful only if it is coupled across scales strongly enough to control `D_{2H}-D_H`; separate coarse asymptotics for `F_H` and `F_{2H}` can lose the small slope defect.

## Counterevidence / boundary cases

ANF-171 is a matched synthetic packet, not the actual prime/rough residual. It proves that phase-blind energy can be misleading, not that the physical source has small alignment. Conversely, ANF-172 does not prove that the coupled scale increment is analytically easier than the signed correlation; the identities are exact reorganizations of the same endpoint information.

The positive representation also does not license subtraction of two independently estimated large quantities. Since `T_L` contains a large affine diagonal component, an error term acceptable for `T_L` itself may be far too large after adjacent-scale differencing. Any claimed Selberg-integral route must be checked at the `o(X log X/log K)` slope-defect scale forced by ANF-169.

The reduction remains dyadic and endpoint-local. Cancellation between dyadic shells or between the two endpoints can only make completion smaller, so any direct signed bound or scale-increment bound must preserve the exact real-part convention used by ANF-169.

## Epistemic status

**Exact information boundary through ANF-172:** target-sized completion forces a phase-sensitive positive dyadic correlation. Single-scale moving-window energy is only a necessary relaxation, but the same signed shell is exactly the dyadic slope defect of a positive endpoint Fejer family. Positivity can therefore be retained only by preserving coupled scale variation.

## Novelty/prior-art status

No independent novelty claim is made here. This intuition synthesizes the exact persisted Mathia reductions and stress controls. The underlying Fejer/autocorrelation relation is classical; the relevant new internal interface is its endpoint-weighted scale-slope form tied to the surviving bow shell.

## Falsification criterion

Show that the positive representation in ANF-172 fails for the endpoint weights of ANF-169, or produce a target-scale control with large `Re S_H` but `D_{2H}-D_H=o(X log X/log K)`. Either would break the claimed exact scale-slope interface. Alternatively, prove that available source theorems control `A Q_H` sharply enough that the coupled scale family never improves the analytic cost; that would leave ANF-172 correct but strategically redundant.
