# MI-017 — Sliding first-crossing localization produces autocorrelation symbols

**Evidence level:** supported by the exact unrestricted first-crossing sliding-window identity WI-253; the proposed incompatibility across radii remains unproved.

At the first unrestricted localized Weil crossing `a_*`, translation freedom changes the localization geometry. For a normalized zero mode `v`, averaging all translated interval cutoffs of half-width `r<a_*` removes the window center and depends only on the ordinary real autocorrelation

\[
C_v(h)=\operatorname{Re}\int v(x+h)\overline{v(x)}\,dx.
\]

WI-253 proves the exact necessary family

\[
\mathcal F_v(r)
=\int_0^{2a_*}\min(h,2r)C_v(h)\,d\nu_{a_*}(h)
+\int_0^{2a_*}\min(h,2r)\kappa(h)C_v(h)\,dh
\ge r\lambda_r>0
\]

for every `0<r<a_*`. Since

\[
C_v(h)=\frac1{2\pi}\int\cos(zh)|\widehat v(z)|^2\,dz,
\]

this is equivalently

\[
\frac1{2\pi}\int\Sigma_r(z)|\widehat v(z)|^2\,dz\ge r\lambda_r,
\]

where `Sigma_r` is an explicit prime-plus-archimedean cosine symbol. The spectral weight is nonnegative, so the first-crossing constraint has been converted from an odd reflected-Hankel problem into a continuum of ordinary spectral averages.

The important structural gain is **simultaneity in the aperture parameter**. The kernel `min(h,2r)` changes slope at the prime-power thresholds `r=(log n)/2`, so the family `{Sigma_r}` carries more information than any one localized inequality. A useful continuation should exploit relations between radii—one-sided derivatives, convexity/monotonicity failures, or incompatible moment demands—rather than bound one symbol uniformly.

This does not make the route automatically positive. A nonnegative spectral density can average a sign-changing symbol positively, and WI-253 does not prove that the family is inconsistent with compact support or with the zero-mode equation. The exact next question is whether the **same** compactly supported spectral density can satisfy every source-dependent inequality and `Q_W(v)=0` simultaneously.

**Boundary.** This intuition concerns the unrestricted first crossing, not the odd first crossing. It proves no pointwise positivity of `Sigma_r`, no phase/nodal theorem, and no RH consequence. The proposed clue `CLUE-first-global-crossing-sliding-autocorrelation-symbol` remains a research question until an incompatibility or a matched countermodel is derived.