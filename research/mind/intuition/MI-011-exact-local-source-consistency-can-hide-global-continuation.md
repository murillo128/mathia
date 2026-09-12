# MI-011 — Exact finite-window source consistency can coexist with divergent or invisible global continuation

**Evidence level:** supported by the exact stable-tail/extension theorem NB-066 and exact first-layer prime-set conservation RE-068 on their stated models; no operator, source, or contradiction is transferred between the two lines.

Nyman--Beurling and Robin Extremal now give two mathematically different examples of the same information boundary: **perfect local source consistency does not imply that the missing global object is controlled or even visible in the same coordinates**.

In Nyman--Beurling, NB-066 characterizes the stable-tail space by

\[
\mathcal T_\infty
=\{t\in\mathcal D:J_Rt\in\mathcal G_R\text{ for every }R\}.
\]

A nonzero stable-tail vector is globally orthogonal to the natural space while every finite Paley--Wiener truncation is exactly a natural trace. This finite compatibility is not approximate: the local synthesis problem is solved at every scale. Yet if `E_R(t)` is the least unseen-future norm of a genuine natural extension with the same finite trace, then

\[
\mathfrak E_R(t)\,\|(I-J_R)t\|
\ge\|J_Rt\|^2,
\]

so `E_R(t)->infinity`. The obstruction is therefore **global continuation cost**, not failure of local representability. The canonical persistent branch, if it exists, converges to one such fixed locally natural mode.

In Robin Extremal, RE-068 gives an exact endpoint consistency law of a different kind. For every complete first-layer-only fan packet, the ordinary primes crossed by the adaptive selector interval and the physical event primes satisfy

\[
\mathcal S\uplus\chi_-\{r_-\}
=\mathcal E\uplus\chi_+\{r_+\}.
\]

In the matched fringe-free branch, `S=E` exactly. Hence every additive endpoint prime statistic agrees automatically, for **any** prime weight `w`. A packet may therefore be physically nontrivial while the entire additive endpoint source algebra is blind to it. Increasing packet cardinality does not change that conclusion for a pure first-layer packet.

The cross-line relation is not that these mechanisms are the same. NB-066 is an inverse-limit/extension-norm obstruction in a Hilbert space; RE-068 is unique-factorization rigidity of a finite prime multiset. The reusable distinction is between three levels that must not be conflated:

1. exact agreement on every finite/local source interface;
2. bounded or stable global continuation of that compatible data;
3. existence of a readout that sees information not already fixed by the local interface.

NB-066 shows that level 1 can hold while level 2 fails catastrophically. RE-068 shows that level 1 can make a whole class of level-3 additive readouts identically uninformative. In both cases, asking for a more accurate version of the same local statistic attacks the wrong resource.

This gives a concrete diagnostic for new constructions. When finite/local source matching is exact, first identify what information is **not determined** by that match. In NB the surviving variable is the norm cost of the unseen global continuation. In RE it is delayed event geometry, packet ordering, higher-layer history, or a non-additive relation. A useful theorem must control one of those residual variables rather than remeasure the already-matched local data.

**Boundary.** No Nyman extension estimate transfers to Robin packets, and no prime-set conservation law transfers to Nyman traces. The common statement is only the information-theoretic separation above, grounded in the two exact project-specific theorems. Neither result by itself proves or disproves RH.