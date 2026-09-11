# MI-004 — Nyman source information can localize far below the scale needed for geometric target repair

**Evidence level:** proved structural identities with an open bridge between them

## Core intuition

A useful Nyman compression can be well conditioned and source faithful while still hiding a target oracle. The current evidence now separates that oracle from source localization much more sharply: the Burnol-scale directional signal can be concentrated in a very small cutoff prefix, while the exact zero-loss repair is a target projection that is only approximately supplied by a recursively smaller Nyman section.

Thus “the source information is already visible at small scale” and “the target can be repaired cheaply” are different mathematical statements.

## Strongest justified claim

NB-031--NB-040 construct the weighted tail-shell quotient. It preserves the head source coordinates with polynomial conditioning, has an intrinsic `Theta(1/M)` source-only target-loss floor, and admits exact zero-loss repair by one unique target-selected line `span(P_W e)`.

NB-041--NB-044 price the obvious ambient dual route. The logarithmic repair coordinate has an explicit shrinking Möbius dual, but any fixed power decay of its full norm already gives a zero-free strip, and the optimal exponent equals the zeta zero frontier. Ambient norm improvement is therefore not a cheap route to the target.

NB-045 identifies a directional alternative: bounded step-tail discrepancies reconstruct `d_N^2` through an exact positive logarithmic average. NB-046 shows a prefix with `log M >> sqrt(log N)` already captures asymptotically all that mass. NB-047 then transfers Vinogradov--Korobov cancellation to the dual and pushes a sufficient cutoff to doubly-logarithmic scale, for example `M=exp((log log N)^(5/3+epsilon))`.

NB-048 attacks the geometric oracle from another direction. The dilated best approximant from `V_K`, `K=floor(N/M)`, lies in the weighted tail and approximates the unique repair vector with exact squared error

`L_(M,N) - (1-d_K^2)/M`.

The corresponding repaired skeleton has target-distance excess between zero and `d_K^2/M`. The oracle is therefore recursively approximable, but the approximation still consumes the smaller-section best projection.

## Synthesis of evidence

The line has exposed two exact compression mechanisms that do not yet meet. One localizes **directional source evidence** to a very small prefix. The other localizes **geometric target repair** to a smaller Nyman section. A genuinely new theorem would connect them: use the source-localized directional data to estimate the recursive repair slack or an equivalent target functional without first solving the smaller/full projection problem.

This is stronger than seeking better matrix conditioning and weaker than controlling the ambient dual at an RH-equivalent power scale. It asks for a source-selected relation between two already-identified exact objects.

## Counterevidence / boundary cases

NB-047's cutoff localization controls the aggregate directional identity, not the weighted-tail repair vector. NB-048's recursive vector is constructed from `P_(V_K)e`, so it is not source-only merely because `K<N`. No finding yet shows that the prefix discrepancies determine or tightly bound the repair slack.

The condition `d_K^2/(M d_N^2)->0` is a sufficient preservation condition, not an unconditional estimate. Choosing `M` to make the prefix small does not automatically make that ratio favorable.

## Epistemic status

**Exact separation plus open bridge:** directional Burnol-scale mass localizes unconditionally to a tiny prefix, and the target oracle admits an exact smaller-section approximation with explicit slack, but no persisted result converts the former into control of the latter.

## Novelty/prior-art status

The source identities, Vinogradov--Korobov input, projection geometry, and dilation mechanism retain their finding-level prior-art boundaries. This intuition is a synthesis of their interaction.

## Falsification criterion

Show that the NB-046/NB-047 prefix data cannot distinguish two admissible finite-section states with materially different NB-048 repair slack under the same source constraints, or prove a quantitative inequality from those directional discrepancies to the repair slack at a scale sufficient for target preservation. Either would settle the proposed bridge.
