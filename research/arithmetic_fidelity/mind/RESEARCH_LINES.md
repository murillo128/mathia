# Arithmetic-fidelity research lines

This file holds the current mathematical questions suggested by the durable arithmetic-fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Preserve exact shell provenance through a joint carrier with auditable conditioning

**Linked intuition:** `MI-055-derivative-depth-is-a-second-left-tail-scaling-coordinate`.

AF-416--AF-432 isolate the full left-tail determinant hierarchy. Fixed derivative shifts close to a positive Cauchy limit, moving depth introduces `s_n/n`, the complete partition family detects the critical value `2`, and the effective coordinate is `b_n(a)=a n^(s_n/n-2)`. Exact square fibres retain finer rectangle, packet and derivative-offset obstructions that continuous saddle matching misses.

AF-433--AF-435 separate source realization, source selection and transport. Coefficient-root neutrality canonically selects the Taylor radius, hence `c=2pi` and `a=1` for the Bernoulli source, but the current determinant aggregates shell labels before packet geometry and the selected square fibre fails the present adjacent-packet cancellation.

AF-436 shows that this loss is **not intrinsic to the exact coefficient sequence**. The normalized even coefficients are `s_k=zeta(2k)=sum_(m>=1)m^(-2k)`, so the complete exact moment sequence determines the shell ladder. AF-437 then prices the triangular way of exposing it: recursive peeling of shell `m` amplifies earlier shell-`j` errors at the target scale by roughly `(m/j)^(2k)`, so exact recoverability and stable recoverability are different resources.

AF-438 resolves the next exact representation question. The generating transform

`F(z)=sum_(k>=1) zeta(2k) z^(k-1)=sum_(m>=1) 1/(m^2-z)`

is a classical Stieltjes/Markov transform with meromorphic continuation

`F(z)=(1-pi sqrt(z) cot(pi sqrt(z)))/(2z)`.

Its poles are exactly `z=m^2`, all with residue `-1`. Thus every shell label is present **simultaneously** in one exact carrier; exposing shell `m` no longer requires subtracting shells `1,...,m-1`. The exponential cascade of AF-437 is therefore a property of sequential peeling, not an information-theoretic loss of the exact Euler sequence.

The live question has moved to **stable joint recovery**. Given only a finite/noisy moment prefix, can Stieltjes continued fractions, Padé, Hankel/Prony or another joint inverse recover the first `M` poles/residues with conditioning materially better than the AF-437 peeling benchmark? A negative result is equally useful if it proves that analytic continuation/rational reconstruction recreates an equivalent instability. Exact pole transport by itself does not answer that finite-data question.

## Keep selection, exact carrier, inverse conditioning, downstream transport and target cancellation as separate currencies

A source-selected parameter can fail downstream; exact source information can be present but badly conditioned; and a representation can preserve aggregate moments while deleting provenance needed by the target. AF-438 now adds the converse lesson: changing representation can remove an **artificial sequential inverse** while leaving the genuine stability problem unresolved.

A continuation should therefore change something substantive: quantify the finite/noisy conditioning of the joint Stieltjes carrier, construct a shell-resolved destination that consumes those poles without re-aggregating them, justify a different source-native selector independently of target success, or use a destination mechanism that does not require the adjacent-packet cancellation excluded at the selected scale. Metric largeness of favorable amplitudes, exact analytic continuation with infinite data, or downstream optimization cannot substitute for these obligations.