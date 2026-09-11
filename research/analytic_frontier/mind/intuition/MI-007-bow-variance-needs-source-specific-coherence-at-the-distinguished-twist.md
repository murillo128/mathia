# MI-007 — Bow completion is an endpoint-local arithmetic correlation problem

**Evidence level:** exact Fejer-minus-completion identity, Selberg-calibrated localization, all-interval source controls, matched endpoint-charge/carrier obstructions through ANF-168, exact endpoint shifted-correlation reduction in ANF-169, and positive moving-window square-function reduction in ANF-170

## Core intuition

The bow endpoint problem is no longer primarily about finding stronger relative cancellation on long intervals. The strongest current source estimates already push dangerous completion beyond every fixed polylogarithmic enlargement of the cubic total-variation scale, while deterministic matched controls show that those increment bounds, local activity, exact centering, and even the exact logarithmic carrier can coexist with target-sized endpoint energy.

ANF-169 identifies what a persistent endpoint charge means in source variables: after removing a target-negligible diagonal edge term, the endpoint square is exactly a triangular sum of shifted products, so macroscopic completion forces positive endpoint-local bilinear correlation at some dyadic lag scale. ANF-170 sharpens that witness without adding a source assumption: each dyadic correlation shell is exactly a current coefficient paired with a preceding dyadic moving-window sum, and Cauchy--Schwarz forces a positive second moment of those moving sums. The decisive currency can therefore be taken to be **source-faithful endpoint moving-window energy at the distinguished twist**.

## Strongest justified principle

ANF-157 writes bow variance exactly as positive Fejer source energy minus an endpoint-completion square. ANF-158--ANF-165 progressively sharpen localization and show that target-sized completion cannot occur inside any fixed polylogarithmic multiple of `R_TV=(X K log X)^(1/3)` under the available all-interval decorrelation and Cramer--Granville normalization.

ANF-166 constructs source-budget-matched data whose discrepancy is stronger than every fixed logarithmic saving above `H_0`, but whose prefix/suffix primitive reaches `asymp sqrt(X log X)` and stays there for a macroscopic fraction of the endpoint horizon. ANF-167 keeps two-sided local `L^1/L^2` activity, and ANF-168 additionally keeps real amplitudes on the exact distinguished logarithmic carrier. These controls isolate the fixed arithmetic amplitude law as the remaining source information.

ANF-169 expands the endpoint square as

\[
E_\partial
=
\Delta_\partial
+2K\operatorname{Re}
\sum_{\sigma\in\{-,+\}}
\sum_{h<K}G_h^\sigma,
\]

where `Delta_partial=o(XK log X)` for the actual source and `G_h^sigma` is a triangularly weighted endpoint shifted correlation. Consequently, if `E_partial>=delta X K log X`, then one endpoint and one dyadic lag block satisfy

\[
\operatorname{Re}
\sum_{h\sim H}G_h^\sigma
\gg_\delta
\frac{X\log X}{\log K}.
\]

ANF-170 writes that dyadic sum exactly as

\[
S_H^\sigma
=
\sum_m
\left(1-\frac mK\right)
 b_m^\sigma\overline{B_H^\sigma(m)},
\qquad
B_H^\sigma(m)
=
\sum_{\substack{h\sim H\\h<m}}b_{m-h}^\sigma.
\]

With

\[
A_\sigma
=
\sum_m\left(1-\frac mK\right)|b_m^\sigma|^2,
\qquad
Q_H^\sigma
=
\sum_m\left(1-\frac mK\right)|B_H^\sigma(m)|^2,
\]

Cauchy--Schwarz gives `|S_H^sigma|^2<=A_sigma Q_H^sigma`. Hence target-sized completion forces

\[
Q_H^\sigma
\gg_\delta
\frac{X^2\log^2X}{A_\sigma\log^2K}.
\]

For `r_X=vartheta-Q_R`, `Q_H^sigma` is a positive moving-window second moment of exact sums of `r_X(n)n^(-iU)`. This is the same source obstruction as ANF-169, but in a positive square-function currency.

## Program consequence

Target a uniform endpoint moving-window estimate

\[
A_\sigma Q_H^\sigma
=o\left(\frac{X^2\log^2X}{\log^2K}\right)
\]

for both endpoints and every dyadic `H` relevant to the bow. By ANF-170 and the sufficient dyadic criterion of ANF-169, this implies `E_partial=o(XK log X)`. Preserve the prime/rough subtraction inside the moving sums for as long as possible; expanding into the four signed shifted-correlation pieces is optional rather than mandatory.

A direct positive short-interval second moment, a large-sieve estimate adapted to the multiplicative carrier, or a Type-I/II argument may therefore be more natural than proving cancellation separately in every signed prime/Ramanujan component. An absolute prefix bound or direct primitive-square theorem remains useful if it implies the same conclusion. Do not treat another logarithmic improvement of one-point all-interval discrepancy as progress unless it crosses the old product gate or yields this moving-window bound.

## Counterevidence / boundary

ANF-170 does not prove that the actual moving-window energy is small. It only proves that the positive dyadic correlation witness of ANF-169 cannot be large unless the corresponding square function is large. Large `Q_H` is not sufficient for large completion because the current coefficient can be nearly orthogonal to its preceding block sum, and different signed lag shells can still cancel.

Nor does the reduction invoke a prime-pair conjecture. The prime/Ramanujan residual is exact, the endpoint weights are finite and explicit, and the distinguished high-frequency phase is retained without Taylor replacement. Existing coefficient-generic controls can still realize the required square-function energy; the unresolved question is whether the fixed arithmetic source can do so at the quantitative scale forced by ANF-170.

The positive Fejer term may also dominate completion through a coupled inequality that bypasses separate endpoint control, but any argument proceeding through the ANF-157 completion identity now has both a signed bilinear target and a positive square-function target.

## Epistemic status

**Exact information boundary: target-sized endpoint completion forces a positive endpoint-local dyadic shifted correlation, which in turn forces a positive moving-window square-function witness for the actual twisted residual. Controlling that source-faithful second moment is the cleanest current route to eliminate persistent endpoint charge.**

## Falsification criterion

Show that the reindexing/Cauchy bridge in ANF-170 loses a target-scale factor that makes the resulting square-function condition unattainable even when the signed ANF-169 block is small, or construct the actual residual `r_X=vartheta-Q_R` with moving-window energy at the forced scale while proving by an independent structural mechanism that all endpoint completion is negligible. Either would show that the positive square function is only a weak necessary shadow rather than a useful theorem currency.
