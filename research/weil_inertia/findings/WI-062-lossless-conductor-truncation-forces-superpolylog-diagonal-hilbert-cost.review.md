---
type: adversarial-review
target: research/weil_inertia/findings/WI-062-lossless-conductor-truncation-forces-superpolylog-diagonal-hilbert-cost.md
---

# Adversarial review

## Adversary

The abstract Hilbert-space lemma is sound, but the claimed “exact identification” of its coefficient with `a_d=dB_d(h_1)` drops a shift dependence that is still present in the imported WI-061 estimate. Equation (10) uses `\widehat G_{h_1(k)}` and (11) correctly has `B_d(h_1(k))`, while the booked-family hypothesis used in (12) only says that `k -> h_2(k)` is injective. Nothing displayed makes `h_1(k)` constant on that family. Therefore (12) does not by itself imply

\[
\|C_d\|_{\ell^2(k)}^2\le d^2 B_d(h_1)M_d,
\]

because the varying weights `B_d(h_1(k))` cannot simply be factored out of the `k`-sum as one unspecified `B_d(h_1)`.

This matters to the finding's strongest formulation: equations (1)--(4) call `\sum_d dB_d(h_1)` the sharp norm-only conductor cost inherited from the actual arithmetic family. WI-061 avoided exactly this issue by replacing `dB_d(h_1(k))` uniformly with `6^{\omega(d)}` before summing over shifts. A likely repair is to define

\[
B_d^*:=\sup_{k\ \mathrm{in\ the\ booked\ family}} B_d(h_1(k)),
\]

which would give `\|C_d\|_2^2\le d^2B_d^*M_d` and hence `a_d=dB_d^*`. Since the local formula still gives `dB_d(h)\ge1` for every active conductor and every shift, the combinatorial super-polylogarithmic lower bound appears likely to survive with `B_d^*`; alternatively the owner could prove that the relevant booking actually fixes `h_1` or supply a weighted Mikawa argument that retains the varying factors.

Please make that quantifier explicit and re-derive the conductor coefficient before treating (3) as the exact sharp interface for the Yang family. The negative conclusion may well remain unchanged, but as written the key specialization (11)--(14) does not follow from the stated hypotheses.