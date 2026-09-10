# MI-007 — Bow completion is an endpoint-local arithmetic correlation problem

**Evidence level:** exact Fejer-minus-completion identity, Selberg-calibrated localization, all-interval source controls, matched endpoint-charge/carrier obstructions through ANF-168, and exact endpoint shifted-correlation reduction in ANF-169

## Core intuition

The bow endpoint problem is no longer primarily about finding stronger relative cancellation on long intervals. The strongest current source estimates already push dangerous completion beyond every fixed polylogarithmic enlargement of the cubic total-variation scale, while deterministic matched controls show that those increment bounds, local activity, exact centering, and even the exact logarithmic carrier can coexist with target-sized endpoint energy.

ANF-169 identifies what a persistent endpoint charge means in source variables: after removing a target-negligible diagonal edge term, the endpoint square is exactly a triangular sum of shifted products. A macroscopic completion therefore forces positive endpoint-local bilinear correlation at some dyadic lag scale. The decisive currency is now not merely the size of an absolute prefix, but the **arithmetic shifted correlation that can sustain that prefix memory**.

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

For `r_X=vartheta-Q_R`, each product in this block is exactly `r_X(n)r_X(n+h)((n+h)/n)^(-iU)` up to reversal at the right endpoint. This is the concrete source statistic that a charge-and-hold mechanism must realize.

## Program consequence

Target a dyadic endpoint correlation theorem for the fixed prime-minus-Ramanujan residual at the distinguished twist. Preserve the four signed terms in `(vartheta-Q_R)(n)(vartheta-Q_R)(n+h)` until their common local structure has had a chance to cancel. A uniform `o(X log X/log K)` bound for every normalized endpoint/dyadic block is sufficient to make the whole endpoint completion negligible.

An absolute prefix bound, a lower activation length, or a direct primitive-square theorem remains useful if it implies the same conclusion, but the shifted-correlation ledger is the most source-faithful current formulation. Do not treat another logarithmic improvement of one-point all-interval discrepancy as progress unless it crosses the old product gate or yields this bilinear bound.

## Counterevidence / boundary

ANF-169 does not prove that the actual endpoint correlation is small. It only proves that large completion must leave a positive dyadic bilinear witness. A single positive dyadic block is not by itself sufficient for large completion because other lag blocks may contribute negatively. The useful exclusion statement controls all dyadic blocks.

Nor does the reduction invoke a prime-pair conjecture. The prime/Ramanujan decomposition is exact, the endpoint weights are finite and explicit, and the distinguished high-frequency phase is retained without Taylor replacement. Existing coefficient-generic controls can still realize the witness by adapting their real amplitudes; the unresolved question is whether the fixed arithmetic source can.

The positive Fejer term may also dominate completion through a coupled inequality that bypasses separate endpoint control, but any argument proceeding through the ANF-157 completion identity now has a precise arithmetic target.

## Epistemic status

**Exact information boundary: target-sized endpoint completion forces a positive endpoint-local dyadic shifted correlation in the actual source variables; after ANF-168, controlling that arithmetic bilinear statistic is the cleanest surviving route to eliminate persistent endpoint charge.**

## Falsification criterion

Construct the actual residual `r_X=vartheta-Q_R` at the distinguished bow twist with a dyadic endpoint block of size `gg X log X/log K` while the endpoint square nevertheless remains negligible for structural reasons, or show that the ANF-169 correlation ledger omits a target-scale diagonal/boundary contribution. Either would invalidate the present identification of the bilinear witness as the correct endpoint currency.
