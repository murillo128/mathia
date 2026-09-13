# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable Farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Uniformize projective transport to the logarithmic source budget

**Linked intuitions:** `MI-001-cumulative-farey-discrepancy-is-mertens-energy`, `MI-002-odd-prime-square-reembedding-localizes-recursive-failure-to-dyadic-channel`, `MI-003-normalized-record-defect-is-the-composition-loss`, `MI-004-multiplicative-horizon-descent-can-preserve-the-source-quotient`, `MI-005-source-neutral-carrier-descent-spends-a-strict-finite-row-potential`.

FD-094--FD-098 close one-step representation, projective composition loss and the strongest current uniform short-interval regularity gain. FD-099 gives the matched obstruction: a fixed source record can support arbitrarily long multiplicative horizon descent while its sampled source quotient remains unchanged. FD-100 and FD-101 then show that a fixed tagged carrier cannot do this forever: its row inventory is finite and floor/ceiling errors can change its source shell at most once.

FD-102 removes carrier identity from the remaining retagging issue. Every current non-head physical predecessor satisfies `H' <= ceil(H/2)`. For a non-head tag with source `x=floor(H/r)`, the carrier-free potential

\[
\mathfrak A(H,x)=\log_2\frac{H-1}{8x-1}
\]

is nonnegative, and an arbitrary child retag from source `x` to source `y` obeys

\[
\mathfrak A(H',y)
\le
\mathfrak A(H,x)-1
+
\log_2\frac{8x-1}{8y-1}.
\]

Thus a carrier switch can replenish source-neutral inventory only by paying actual logarithmic source descent. Along any `m` consecutive non-head predecessors, regardless of row reselection,

\[
8x_m-1\le\frac{H_0-1}{2^m}.
\]

On the frontier core, `x_0 >= H_0^{Theta-delta+o(1)}`, so a path that remains at or above its starting source scale has length at most

\[
(1-\Theta+\delta+o(1))\log_2 H_0.
\]

The live theorem is therefore no longer a genealogical carrier-switch theorem. It is a **logarithmic-depth uniformization theorem**: make the projective predecessor transport, including the shrinking certificate and all asymptotic transport errors, valid for `m` proportional to `(1-Theta) log H`. At that depth the deterministic geometry already forces source-scale movement even under completely adaptive retagging.

## Price logarithmic-depth source progress against projective quality

FD-097 gives the projective certificate

\[
\mathcal Q_\sigma(H_j)\gtrsim \mathcal Q_\sigma(H_0)b_\sigma^j
\]

at every fixed depth and allows a diagonal sequence of depths tending to infinity, but it does not relate available depth effectively to the starting horizon. FD-102 identifies the missing scale: unspecified growing depth is not enough; the non-head geometry needs depth of order `(1-Theta) log H` to force the source below a frontier-scale starting quotient.

If the FD-097 transport could be uniformized to that depth without changing its branch factor, the quality loss would be polynomial,

\[
b_\sigma^m
=H^{-(1-\Theta+\delta)\log_2(1/b_\sigma)+o(1)},
\]

rather than subpower. The next analytic question is therefore whether the transported nonsquarefree packet remains strong enough after this polynomial loss, whether the per-step projective coefficient can be improved, or whether head/source-descending events occur earlier and supply source motion before the full logarithmic budget is spent.

This is now the useful coupling problem: **projective quality versus logarithmic source progress**, not projective quality versus carrier identity.

## Keep non-head contraction, head progress and source retags distinct

Source-record slowdown supplies the entry family. FD-094--FD-095 supply exact one-step closure; FD-097 supplies projective multistep accounting; FD-098 prices the current source-head regularity gain; FD-099 separates physical horizon descent from source descent; FD-100--FD-101 prove finite tagged inventory and one-shell rigidity; FD-102 amortizes arbitrary non-head retagging directly against source scale.

The remaining escape mechanisms are now sharply separated. A long non-head segment must lower the source quotient by the exact FD-102 budget. A source-descending retag already pays in the desired currency and should be quantified by how much mass/quality survives at the lower source. A head step avoids dyadic horizon contraction but is precisely the additive source-moving branch of FD-095/FD-098. A final descent argument must combine these two kinds of source progress with a certificate that remains valid for logarithmic depth.

In particular, do not spend another cycle looking for a carrier label whose identity survives retagging: FD-102 makes that unnecessary. The strongest next target is uniform control of the existing predecessor inequalities at `c log H` depth, or a proof that the head/source-retag alternatives accumulate enough source movement before that depth is reached.