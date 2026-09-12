# MI-006 — First-layer timing is macroscopic before readout but summable in the Robin metric

**Evidence level:** proved for the first CA layer and exact Robin workload in RE-069; no conclusion is transferred to higher layers or nonlinear selector geometry.

RE-068 shows that a matched first-layer packet contains the same ordinary prime set on the selector and physical-event sides. The remaining first-layer datum is positional: the event for `p` occurs at `eta_p>p`, not at `p`.

RE-069 writes this difference exactly as delay pulses,

\[
B_1(x)
=
\sum_p(\log p)\mathbf 1_{[p,\eta_p)}(x).
\]

For a late complete matched packet these pulses have large raw transport:

\[
\int B_1(x)\,dx
=
\left(\frac12+o(1)\right)
\sum_{p\in\mathcal E}\log p.
\]

So the positional information is real and can accumulate macroscopically even when the packet cardinality is unbounded.

The exact Robin readout sees a very different geometry. With `g(x)=1/(x log x)`, one complete delay contributes

\[
-\int_p^{\eta_p}(\log p)g'(x)\,dx
=
\frac1p-\log(1+1/p)
=:\kappa_p,
\]

and `0<kappa_p<1/(2p^2)`. Therefore the total contribution of **all future first-layer delays** after scale `X` is only `O(1/X)`.

The reusable distinction is between information present in a representation and information visible to the requested functional. A source coordinate can have macroscopic mass in one metric while the destination kernel projects it into an absolutely summable tail. Counting more such coordinates cannot repair a summable readout.

**Boundary.** First-layer timing can still affect support chambers, selector positions, and nonlinear packet interactions before integration, and no bound here applies to higher-layer event geometry. The result rules out only the direct linear timing contribution to the exact Robin workload.
