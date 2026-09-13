# MI-012 — Robin needs sparse-sample information beyond ambient exceptional-set packing

**Evidence level:** the host-to-frontier conversion is exact through [RE-095](../../findings/RE-095-source-conditioned-sampled-gap-sparsity-lowers-the-depth-two-moment-frontier.md); [RE-096](../../findings/RE-096-depth-two-bad-hosts-reduce-to-a-phase-stable-deformed-quadratic-sequence.md) gives the all-integer deformed-quadratic host reduction and phase geometry; [RE-097](../../findings/RE-097-bazzanella-quadratic-threshold-is-ambient-packing-not-phase-control.md) audits the quadratic prior art and proves that ambient exceptional-set packing cannot improve the existing Robin envelope. A direct sparse-sequence scarcity theorem below the required exponent remains open.

After the higher-depth reductions, the residual mixed first/depth-two cells are sampled at

`x(n)=eta_1^(-1)(eta_2(n))`, `n~X^(1/2)`.

RE-095 shows that any fixed power saving in the bad-host count at interval length `X^vartheta`, with `vartheta<73/200`, lowers the `173/200` frontier. RE-096 shows the analytic upper bound need not retain prime host indices: it is enough to control all integer hosts on the exact deformed sequence.

The sample has two very different notions of closeness. In position space,

`x(n)-n^2/2 ~ X/log X`,

so interval inclusion from ordinary square starts is useless at the Robin scale. In logarithmic phase geometry,

`(log x)' = 2/t + O(1/(t(log t)^2))`,

`(log x)'' = -2/t^2 + O(1/(t^2(log t)^2))`,

so zero-sum phases remain a slowly deformed quadratic family.

RE-097 clarifies exactly where these facts matter. Bazzanella's published quadratic threshold `13/32` in the relevant small-interval regime is obtained by packing each sparse exception into an ordinary ambient PNT exceptional set. That proof uses spacing, not quadratic oscillation. The same packing transfers to `x(n)` despite its physical drift, but its information content is already available to Robin through the RE-094 ambient frontier.

More generally, if a proof bounds bad sampled hosts only by attaching disjoint `H`-packets to an ambient exceptional set, RE-097 proves that the resulting Robin frontier is never better than the existing envelope. Thus **ambient scarcity is not source-conditioned scarcity merely because it is evaluated on a sparse host sequence**.

The potentially useful part of the quadratic analogy is the genuinely direct sparse-sequence architecture used in other parameter regimes: higher moments, zero additive energy, exponent-pair/oscillatory estimates, or another argument that sees the phase family itself. The target is now precise: prove

`#Z_vartheta(X) <= X^(1/2-delta+o(1))`

for some `vartheta<73/200`, `delta>0`, by an argument that does not factor solely through one-variable ambient exceptional-set measure.

**Research consequence.** Do not try to transfer the numerical `13/32` threshold or improve the ambient packet-counting step. Use the stable derivatives of `log x(n)` only in a direct sparse-sample estimate capable of producing information unavailable to RE-094. That is the first mechanism that can genuinely lower the mixed depth-two Robin frontier.

**Boundary.** RE-097 does not prove such a sparse-sample estimate and does not show that the phase-stable deformation is sufficient. It only classifies the ambient-packing proof family as non-improving for this target and leaves the direct phase-sensitive route open.
