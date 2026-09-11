# MI-010 — Weighted collision nulls have separate concentration and shape dimensions

**Evidence level:** supported by the exact weighted-Haar calculation and classical Lindeberg--Feller specialization in VIS-173; deterministic growing-dimensional prime-log transfer remains open.

For positive weights `w_j`, define

\[
W=\sum_jw_j,\qquad Q=\sum_jw_j^2,\qquad R=\sum_jw_j^4,
\]

and the two effective dimensions

\[
D_2=\frac{W^2}{Q},\qquad D_4=\frac{Q^2}{R}.
\]

They control different parts of the matched Haar collision null. If `D_2->infinity`, the weighted denominator concentrates around its mean and the leading collision score has the universal `W^{-1/2}` bulk scaling. But the first normalized relative correction is a weighted centered sum whose standardized excess kurtosis is

\[
-\frac{3}{2D_4}+o(1).
\]

Moreover `D_4->infinity` is exactly the maximal-weight negligibility condition `max_j w_j/sqrt(Q)->0`, hence the Lindeberg boundary for the bounded Haar coordinates. The first correction is Gaussian when `D_4->infinity`; if `D_4` stays bounded, a Gaussian limit is impossible along that subsequence.

So a large effective support in the variance sense does not imply a universal shape. One can have `D_2->infinity` while `D_4` remains finite: the bulk concentrates sharply, yet a finite collection of heavy coordinates retains a non-Gaussian fingerprint in standardized fluctuations.

The prime-power taper `w_p=p^{-alpha}` makes the split explicit. For `0<=alpha<=1/2`, both dimensions diverge and the first correction is Gaussian. For `1/2<alpha<=1`, `D_2` diverges but `D_4` tends a finite prime-zeta ratio, so leading concentration coexists with persistent low-prime non-Gaussian shape. For `alpha>1`, even `W` converges and the concentrated-bulk regime itself disappears.

The practical null gate is therefore two-dimensional. Before interpreting a weighted residual as source-sensitive, match the leading concentration scale through `D_2` and the first-correction shape through `D_4`, or use the exact non-Gaussian weighted null. Matching only variance/effective size can manufacture an apparent structural residual from a change in weight concentration.

**Boundary.** This is a theorem for independent Haar phases. It does not show that a deterministic prime-log orbit has the same growing-support law, and it does not calibrate rare collision tails or decoder approximation error. Those remain separate population and discrepancy gates.
