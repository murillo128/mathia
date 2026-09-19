# Arithmetic-fidelity research lines

This file holds the current mathematical questions suggested by the durable arithmetic-fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Preserve exact shell provenance through the representation, not merely at the source

**Linked intuition:** `MI-055-derivative-depth-is-a-second-left-tail-scaling-coordinate`.

AF-416--AF-432 isolate the full left-tail determinant hierarchy. Fixed derivative shifts close to a positive Cauchy limit, moving depth introduces `s_n/n`, the complete partition family detects the critical value `2`, and the effective coordinate is `b_n(a)=a n^(s_n/n-2)`. Exact square fibres retain finer rectangle, packet and derivative-offset obstructions that continuous saddle matching misses.

AF-433--AF-435 separate source realization, source selection and transport. Coefficient-root neutrality canonically selects the Taylor radius, hence `c=2pi` and `a=1` for the Bernoulli source, but the current determinant aggregates shell labels before packet geometry and the selected square fibre fails the present adjacent-packet cancellation.

AF-436 shows that this loss is **not intrinsic to the exact coefficient sequence**. The normalized even coefficients are `zeta(2k)`; after exact peeling of earlier shells, the residual beginning at shell `m` is asymptotic to `m^(-2k)`. The full shell ladder is therefore recoverable in exact arithmetic.

AF-437 adds the conditioning boundary hidden by exact peeling. For sequential recovery of shell `m`, coefficient noise and errors in every earlier shell are amplified at the target scale by

`m^(2k)|e_k| + sum_(j<m) (m/j)^(2k)(|omega_(j,k)| + k|eta_(j,k)|)`.

Hence an earlier weight error must be `o((j/m)^(2k))` and a relative location error must be `o(k^(-1)(j/m)^(2k))` for that peeling route; estimating the common radius itself requires error `o(m^(-2k)/k)`. Exact symbolic normalization avoids that particular estimation cost.

The live question is no longer whether the source contains canonical shell data. It does. The question is whether a destination representation can transport the shell ladder **without first paying this sequential exponential error cascade**. A serious carrier must either preserve shell labels before recursive subtraction, prove a joint inverse whose conditioning beats the peeling benchmark, or use exact symbolic shell structure so that the earlier layers are not re-estimated from noisy downstream data.

## Keep selection, carrier resolution, conditioning, transport and target cancellation as separate currencies

A source-selected parameter can fail downstream; exact source information can be present but exponentially ill-conditioned; and a representation can preserve aggregate moments while deleting provenance needed by the target. AF-437 makes the distinction between exact recoverability and stable recoverability explicit rather than leaving it inside a generic precision warning.

A continuation should therefore change something substantive: construct a shell-resolved carrier with auditable conditioning, justify a different source-native selector independently of target success, or use a destination mechanism that does not require the adjacent-packet cancellation excluded at the selected scale. Metric largeness of favorable amplitudes or downstream optimization cannot substitute for those source-side obligations.