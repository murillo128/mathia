# MI-007 — Bow completion is a phase-sensitive endpoint-local correlation problem

**Evidence level:** supported

## Core intuition

The bow endpoint obstruction is not determined by moving-window energy alone. Target-sized completion forces a large **positive real** dyadic shifted correlation at the distinguished logarithmic twist. A positive moving-window square function is a useful necessary witness, but it discards the angular alignment between the current coefficient and its preceding block sum.

At the exact target scale this loss can be decisive: a packet may have maximal complex coherence and large square energy while its real endpoint correlation vanishes because the two factors are almost in quadrature. The source theorem must therefore preserve phase-sensitive alignment, not only local energy.

## Strongest justified claim

ANF-157 writes bow variance exactly as positive Fejer source energy minus an endpoint-completion square. ANF-158--ANF-168 show that increasingly strong coefficient-generic interval, activity, centering, and carrier controls still allow target-sized endpoint completion. ANF-169 then proves that such completion forces one endpoint and one dyadic lag shell to satisfy a positive real shifted-correlation lower bound.

ANF-170 rewrites the shell as

`S_H = sum_m (1-m/K) b_m overline(B_H(m))`

with moving-window sum `B_H(m)`, and Cauchy--Schwarz yields `|S_H|^2 <= A Q_H`. This makes `Q_H` a positive necessary witness. ANF-171 shows the implication cannot be reversed even at the danger scale: a constant-modulus geometric packet can satisfy `|S_H|^2/(A Q_H) -> 1` while `Re S_H/sqrt(A Q_H) -> 0`, with negligible endpoint completion. Defining

`alpha_H = Re S_H / sqrt(A Q_H)`

isolates the missing currency. Danger is carried by `alpha_H sqrt(A Q_H)`, not by `Q_H` alone.

## Synthesis of evidence

The sequence ANF-169--ANF-171 separates three levels that must not be conflated: signed endpoint correlation, complex coherence, and positive moving-window energy. The first is the decision statistic entering completion; the second can be large with the wrong phase; the third forgets phase completely. The exact quarter-turn stress control in ANF-171 therefore weakens the earlier idea that a square-function theorem is the cleanest standalone destination.

For the physical residual `r_X=vartheta-Q_R`, the durable target is a source-faithful estimate on the real dyadic correlation at the distinguished twist, or a theorem that controls both the energy factor and the alignment factor. A positive second-moment estimate remains sufficient when it is genuinely small, but it is no longer justified as the uniquely natural or necessary source currency.

## Counterevidence / boundary cases

ANF-171 is a matched synthetic packet, not the actual prime/rough residual. It proves that phase-blind energy can be misleading, not that the physical source has small alignment. Conversely, a theorem forcing `A Q_H` below the ANF-170 threshold would still rule out completion regardless of phase; the point is that large `Q_H` cannot be interpreted as evidence of danger without controlling `alpha_H`.

The reduction remains dyadic and endpoint-local. Cancellation between dyadic shells or between the two endpoints can only make completion smaller, so any direct signed bound must preserve the exact real-part convention used by ANF-169.

## Epistemic status

**Exact information boundary through ANF-171:** target-sized completion forces a phase-sensitive positive dyadic correlation; positive moving-window energy is only a necessary relaxation, and its loss of angular alignment can be target-scale sharp.

## Novelty/prior-art status

No independent novelty claim is made here. This intuition synthesizes the exact persisted Mathia reductions and stress controls.

## Falsification criterion

Show that ANF-171's quarter-turn packet cannot satisfy the same normalization and bow-scale hypotheses consumed by ANF-170, or derive an identity for the actual residual forcing `|alpha_H|` uniformly away from zero whenever `A Q_H` is at the danger scale. Either result would restore the positive square function as a substantially sharper proxy than the current evidence supports.
