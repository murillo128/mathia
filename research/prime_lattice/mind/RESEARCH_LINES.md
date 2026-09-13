# Prime-lattice research lines

This file holds the current mathematical questions suggested by the durable prime-lattice intuitions. It is not a roadmap, task queue, status page, or history.

## Extract positive-order transport or a sign theorem special to the actual low Weil eigenbranch

**Linked intuition:** `MI-016-weil-form-observability-is-stronger-than-moment-observability`.

PL-280--PL-284 give the aperture ledger, terminating fixed-aperture positivity certificate, and a conditional positive endpoint at `a=0.8` with a simple isolated ground state and tiny explicit margin.

PL-285--PL-291 separate ambient form regularity, graph-domain regularity and actual eigenbranch regularity. Generic form and graph balls have only inverse-log and inverse-squared-log transport, while the source-static eigen-equation places actual eigenstates in every finite logarithmic Fourier scale.

PL-292 quantifies that all-log hierarchy. On compact source-static aperture intervals the logarithmic moments can be bounded by `exp(C m^2 log(m+2))`; optimizing over `m` gives a subpower modulus faster than every fixed inverse-log power but still slower than every Hölder modulus. The same finding shows that generic physical cutoffs have at least `(c m)^m` cost, so tightening the all-log bootstrap cannot by itself create a positive Sobolev exponent.

PL-293 identifies the sharp universal boundary obstruction to the most direct upgrade. The optimal zero-exterior Dirichlet logarithmic-Laplacian boundary amplitude is `ell(t)^(1/2)`, and a one-dimensional Gagliardo calculation shows that a nonvanishing channel at that scale excludes `H^s` for every `s>=1/2`. The canonical torsion solution is a matched positive control that attains the bad scale. Thus the principal operator and Dirichlet boundary law cannot generically supply the `H^(1/2)` first-frequency moment needed for routine differentiation of moving prime-shift autocorrelations.

PL-294 closes the generic semigroup-positivity escape as well. For Suzuki's localized Weil form the standard Beurling--Deny absolute-value criterion holds exactly only for

`0<a<=a_BD=(1/2) log(rho_pl)=0.140599787...`,

where `rho_pl^3-rho_pl-1=0`. This threshold occurs **before** the first prime-power translation at `(1/2)log 2`. Above it, a two-bump test avoiding the discrete prime lags makes the criterion fail, so ordinary positivity-preserving/Perron--Frobenius continuation cannot prove that the certified `a=0.8` ground state has fixed sign. This is a method obstruction, not a sign-change theorem for the actual eigenfunction.

The live theorem must therefore exploit the **actual rational-prime Weil eigen-equation twice over**: either suppress the universal `ell^(1/2)` boundary channel enough to gain some `H^s`, `0<s<1/2`, derive a non-absolute translation derivative, prove a source-specific fixed-sign property of the selected eigenbranch at the aperture of interest, or bypass the regularity/Hopf route entirely. Generic principal-operator regularity and generic semigroup positivity are both exhausted.

## Separate ambient topology, graph-domain sharpness, optimized all-log transport, universal boundary amplitude, semigroup positivity and source-specific eigenbranch structure

The regularity/order ladder is now quantitative. Ambient form control gives inverse-log transport; graph-domain control gives inverse-squared-log transport; actual eigenstates have optimized all-log subpower transport. The generic cutoff architecture cannot upgrade this to Hölder, and the sharp principal-operator boundary law supplies explicit positive states outside `H^(1/2)`. Independently, the exact Beurling--Deny window ends at the archimedean pre-prime aperture `a_BD`, so the standard positivity-improving theorem cannot be propagated to `a=0.8`.

Neither obstruction is a theorem about the sign or Sobolev regularity of the actual Weil ground state. A further improvement must therefore visibly use the selected eigenstate/source equation rather than repeat generic cutoff estimates, generic logarithmic-Laplacian regularity, or generic Dirichlet-form positivity.