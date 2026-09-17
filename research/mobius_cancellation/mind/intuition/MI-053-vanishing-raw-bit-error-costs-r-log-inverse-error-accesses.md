# MI-053 — Vanishing source-coordinate error costs `R log(1/error)` source-edge divergence

**Evidence level:** exact synthesis from [MC-340](../../findings/MC-340-source-entropy-prices-low-energy-dephasing.md), [MC-344](../../findings/MC-344-bit-flip-source-readout-capacity.md), [MC-345](../../findings/MC-345-adaptive-source-query-feedback-capacity.md), [MC-346](../../findings/MC-346-adaptive-raw-bit-reliability-overhead.md), [MC-347](../../findings/MC-347-variable-fidelity-source-query-divergence-budget.md), and [MC-348](../../findings/MC-348-channel-free-edge-kl-reliability.md).

The linear capacity budget and the cost of reliable source-coordinate reconstruction are different statements. MC-344--MC-345 show that at fixed BSC crossover `q<1/2`, even fully adaptive noisy coordinate access carries at most `c(q)` mutual information per actual query. This forces `Omega(R)` expected accesses for a fixed nontrivial source-information target, but does not make positive noise fatal.

MC-346 sharpens the regime in which the desired downstream operation requires the individual source bits to become increasingly reliable. At fixed BSC quality, if the final decoder has average coordinate error `bar p`, pairwise change-of-measure across neighboring source states forces `E[tau]=Omega_q(R log(1/bar p))`. MC-347 then removes query count as the invariant when raw-coordinate measurement fidelity varies: the same logarithmic tariff is paid in accumulated directional discrimination KL rather than in nominal events.

MC-348 removes the remaining raw-coordinate acquisition restriction. Let `P_x` be the law of the **entire admitted transcript** under source state `x`, with no assumption that the transcript factorizes into coordinate queries, has fixed dimension, or is generated nonadaptively. Put a neighboring-state graph on the reciprocal source law—single-bit edges in even rank and parity-preserving pair flips in odd rank—and charge each edge by the symmetrized transcript divergence

`b(x,x')=(D(P_x||P_x')+D(P_x'||P_x))/2`.

Averaging these edge costs gives an intrinsic budget `mathfrak J`. Bretagnolle--Huber testing on each neighboring pair plus exact source-graph counting and Jensen's inequality yield

`mathfrak J = Omega(R log(1/bar p))`

whenever average Hamming error `bar p` vanishes. The theorem applies to scalar, vector, adaptive, interactive or one-shot jointly coded transcripts. MC-347 is recovered by proving that its accumulated query divergence upper-bounds this source-edge budget.

This identifies the reusable reliability geometry more cleanly. Acquisition syntax is not the invariant. The destination demands reliable separation of neighboring admissible source states, and the complete transcript must therefore accumulate enough divergence on the source graph. Different acquisition models matter only through the theorem that converts their own resources—query count, SNR, Euclidean edge energy, total variation, or another charged quantity—into an upper bound on `mathfrak J`.

For joint Gaussian encodings this becomes a source-edge Dirichlet-energy tariff: if `Z=F(X)+N` with isotropic Gaussian noise, neighboring-state KL is controlled by `||F(x)-F(x')||^2/(2 sigma^2)`, so vanishing coordinate error forces the average squared separation of neighboring source states to grow at the same `R log(1/bar p)` scale after normalization. A low-dimensional or one-shot encoding is not free if it compresses those edge separations.

For endpoint dephasing the audit remains two-stage. Translate the target gain into the source-coordinate resolution actually required. A fixed gain may be governed only by linear mutual information/capacity. If approaching the matched-filter floor forces `bar p->0`, the additional reliability tariff is source-edge divergence, independent of how the transcript was assembled.

**Boundary.** MC-348 is intrinsic to the reciprocal finite-source law and to recovery measured by average Hamming error. It does not prove that every Möbius mechanism must recover individual source coordinates, does not price an arbitrary arithmetic destination that is insensitive to some source edges, and does not itself bound the source-edge divergence supplied by a concrete analytic architecture. Its durable content is that once the destination really requires vanishing coordinate error, arbitrary joint coding cannot remove the `R log(1/error)` discrimination burden; it can only change how that burden is paid.