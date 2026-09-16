# MI-048 — Bounded-energy dephasing needs linear joint source information

**Evidence level:** exact finite-endpoint synthesis from [MC-338](../../findings/MC-338-observation-energy-tradeoff.md), [MC-339](../../findings/MC-339-maximal-correlation-information-budget.md), and [MC-340](../../findings/MC-340-global-transcript-information-capacity.md).

MC-338--MC-339 turn endpoint dephasing into a source-relative information problem. Each coefficient can cancel its own binary phase cheaply only to the extent that its admitted observation predicts that phase, and the exact projection/energy inequality prices any remaining blindness. HGR maximal correlation and mutual information make that predictability invariant under reparameterization and explicit information channels.

MC-340 shows that the per-coordinate view is not enough. Let `X=(X_1,...,X_R)` be the complete reciprocal source vector and `Y=(Y_1,...,Y_R)` the complete admitted transcript. If `rho^2` is the average squared own-phase predictability, then

`rho^2 <= m^(-2) + (2/R)(I(X;Y)+TC(X))`.

The total-correlation term is the exact price of intrinsic dependence among the source phases. For the punctured character law it remains only `O(1)` nats: it tends to `0` at even rank and `log 2` at odd rank. The odd parity relation is therefore a real decoder but only a constant information surcharge; it cannot account for order-`R` average predictability.

Combining this with the MC-338 energy inequality gives a global capacity threshold. At bounded normalized coefficient energy, any constant improvement over full dephasing error requires `I(X;Y)=Omega(R)`. If `Y` has only `K_R` states, then `log K_R=o(R)` is insufficient. Near the matched-filter energy floor the statement is sharper: if `E<=1` and the dephasing error tends to zero, then the transcript carries asymptotically the full entropy of `X`; at exact zero error it determines `X` completely.

This closes an important loophole in local information accounting. Many observations can each reveal little about their own target coordinate while collectively encoding the whole source vector, after which a joint decoder can reconstruct every needed phase. A useful analytic restriction must therefore bound the **joint transcript information**, not just average `I(X_i;Y_i)`, low rank, low Walsh degree, variable exclusion or the apparent number of output coordinates.

The state-count corollary should not be mistaken for the invariant statement. One real or complex statistic can encode exponentially many discrete source states. What matters is actual `I(X;Y)` under the declared source law and the energy needed to exploit it. Conversely, large syntactic transcripts need not be informative if they factor through a large exact source kernel.

The live arithmetic task is to identify a source-natural transcript for a genuine Möbius coefficient architecture and prove a quantitative joint-information bound that survives all exact source relations, while controlling coefficient energy/conditioning. A separate possible route is to prove that acquiring the required linear source information necessarily forces an analytic energy cost that destroys endpoint gain.

**Boundary.** MC-340 is a finite reciprocal-endpoint theorem for the declared binary character source law. It does not provide a canonical probability model for actual Möbius coefficients, does not bound the mutual information of an existing analytic construction, and does not estimate `M(x)` or prove RH. The cross-coordinate entropy inequalities are a capacity obstruction, not an arithmetic cancellation theorem.