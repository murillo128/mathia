# MI-079 — Permutation-invariant factor size needs inverse-logarithmic precision for polynomial state capacity

**Evidence level:** exact combinatorial synthesis from [MC-428](../../findings/MC-428-permutation-quotient-log-factor-resolution-threshold.md), sharpening the ordered quantized log-size count of MC-427. The partition asymptotics and labelled/unlabelled distinction are classical; the line-specific content is the capacity threshold after quotienting artificial factor-slot order.

MC-427 counts ordered words of quantized factor log-sizes. If the downstream observable is invariant under permuting factor slots, that count overstates the physical source states. Let `r=omega(n)`, `L=floor(log n/eta)`, and retain only the unordered multiset of quantized sizes. Then MC-428 gives

`N_sym(n,eta) <= (r+1) sum_(s<=L) p(s) <= (r+1)(L+1)p(L)`.

Hardy--Ramanujan growth `log p(L)~pi sqrt(2L/3)` changes the entropy scale. Every precision regime

`eta^(-1) <= (log X)^(delta+o(1))`, `delta<1`,

still has only `X^(o(1))` permutation-orbit states uniformly for squarefree `n<=X`. If a symmetric scalar size channel is claimed to have at least `X^alpha` states, polynomial capacity forces

`eta^(-1)=Omega(log X)`,

with the sharper lower constant `liminf eta^(-1)/log X >= 3alpha^2/(2pi^2)` along that sequence.

Thus the apparent gap between MC-427's ordered inverse-polylogarithmic threshold and inverse-logarithmic precision can be entirely **slot-label entropy**. A factor decomposition may name coordinates, but those names are not source information unless the mathematics later treats the slots asymmetrically in a way that survives the analytic architecture.

The reusable first-kill test is therefore representation-theoretic: before crediting high-resolution factor states, quotient every factor permutation that the final observable cannot distinguish. If the mechanism really needs ordered slots, it must identify the intrinsic asymmetric role—different ranges, coefficients, primality constraints or another relation—and show that this role survives closure and cancellation.

**Boundary.** Permutation invariance is load-bearing. Intrinsically asymmetric factor slots must not be quotiented away. The result is scalar and quantized; vector summaries, exact factor identities and exact `log u` are outside it. Reaching inverse-logarithmic precision only makes polynomial orbit-state volume combinatorially possible and does not by itself create Möbius cancellation.