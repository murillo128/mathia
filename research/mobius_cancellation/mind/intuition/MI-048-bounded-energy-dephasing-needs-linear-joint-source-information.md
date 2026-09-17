# MI-048 — Bounded-energy dephasing needs linear joint source information

**Evidence level:** exact finite-endpoint synthesis from [MC-338](../../findings/MC-338-observation-energy-tradeoff.md), [MC-339](../../findings/MC-339-maximal-correlation-information-budget.md), [MC-340](../../findings/MC-340-global-transcript-information-capacity.md), and [MC-361](../../findings/MC-361-binary-entropy-transcript-capacity-curve.md).

MC-338--MC-339 turn endpoint dephasing into a source-relative information problem. Each coefficient can cancel its own binary phase cheaply only to the extent that its admitted observation predicts that phase, and the exact projection/energy inequality prices any remaining blindness. HGR maximal correlation and mutual information make that predictability invariant under reparameterization and explicit information channels.

MC-340 shows that the per-coordinate view is not enough. Let `X=(X_1,...,X_R)` be the complete reciprocal source vector and `Y` the complete admitted transcript. If `rho^2` is the average squared own-phase predictability, then

`rho^2 <= m^(-2) + (2/R)(I(X;Y)+TC(X))`.

The total-correlation term is the exact price of intrinsic dependence among the source phases. For the punctured character law it remains only `O(1)` nats: it tends to `0` at even rank and `log 2` at odd rank. The odd parity relation is therefore a real decoder but only a constant information surcharge; it cannot account for order-`R` average predictability.

MC-361 replaces the earlier Pinsker/Fano conversion by the sharp binary posterior-entropy curve. If `b_i=E[X_i|Y]`, `rho_i^2=E b_i^2`, `rho^2=R^(-1)sum_i rho_i^2`, and `h` is binary entropy in nats, concavity gives

`H(X|Y) <= R h((1+rho)/2)`

and hence

`I(X;Y) >= H(X)-R h((1+rho)/2)`.

Combining this with the MC-338 energy/dephasing inequality makes the endpoint capacity threshold quantitative at every fixed margin, not merely asymptotic. At normalized coefficient energy at most one and dephasing error at most `epsilon`,

`I(X;Y) >= H(X)-R h(epsilon/2)`.

As `epsilon->0`, the transcript therefore carries asymptotically the full source entropy; at exact zero error it determines the source. For a discrete transcript the same inequality immediately yields the corresponding state-count lower bound through `I(X;Y)<=log|Y|`.

This closes an important loophole in local information accounting. Many observations can each reveal little about their own target coordinate while collectively encoding the whole source vector, after which a joint decoder can reconstruct every needed phase. A useful analytic restriction must therefore bound the **joint transcript information**, not just average `I(X_i;Y_i)`, low rank, low Walsh degree, variable exclusion or the apparent number of output coordinates.

The state-count corollary should not be mistaken for the invariant statement. One real or complex statistic can encode exponentially many discrete source states. What matters is actual `I(X;Y)` under the declared source law and the energy needed to exploit it. Conversely, large syntactic transcripts need not be informative if they factor through a large exact source kernel.

The live arithmetic task is to identify a source-natural transcript for a genuine Möbius coefficient architecture and prove a quantitative joint-information upper bound that survives all exact source relations, while controlling coefficient energy/conditioning. MC-361 sharpens the compulsory destination-side amount but does not supply that arithmetic upper theorem. A separate possible route is to prove that acquiring the required linear source information necessarily forces an analytic energy cost that destroys endpoint gain.

**Boundary.** MC-340--MC-361 are finite reciprocal-endpoint theorems for the declared binary character source law. They do not provide a canonical probability model for actual Möbius coefficients, do not bound the mutual information of an existing analytic construction, and do not estimate `M(x)` or prove RH. The posterior-entropy curve is an exact capacity obstruction, not an arithmetic cancellation theorem.