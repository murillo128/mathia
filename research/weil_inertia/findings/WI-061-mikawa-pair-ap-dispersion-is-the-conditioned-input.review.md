---
type: adversarial-review
target: research/weil_inertia/findings/WI-061-mikawa-pair-ap-dispersion-is-the-conditioned-input.md
---

# Adversarial review

## Adversary

Equation (18) is not justified by the displayed pointwise estimate (15). After (13) is relaxed to

\[
|C_d(k)|^2\le B_d(h_1(k))d^2\max_a |E_d(a,h_2(k))|^2,
\]

summing over an injective shift family yields a term proportional to

\[
\sum_{h_2}\max_a |E_d(a,h_2)|^2,
\]

whereas the Mikawa square-function input quoted in (8) controls

\[
\max_a\sum_{h_2}|E_d(a,h_2)|^2.
\]

The first quantity cannot in general be bounded by the second, so the stated transition from (15) to (18) interchanges `sum` and `max` in the wrong direction.

The intended per-conductor estimate appears repairable, but only by retaining exact Parseval before taking the residue-class maximum. Cauchy with (10) and the equality in (13) gives

\[
|C_d(k)|^2
\le B_d(h_1(k))\,d\sum_a |E_d(a,h_2(k))|^2.
\]

Using the uniform bound `dB_d(h_1)\le 6^{\omega(d)}`, then summing over the injective `h_2` family, gives

\[
\sum_k|C_d(k)|^2
\le 6^{\omega(d)}\sum_a\sum_{h_2}|E_d(a,h_2)|^2,
\]

which can be compared to Mikawa only after the exact admissible residue set is checked; for the coprime residue classes in the quoted theorem one would use at most `\varphi(d)` copies of `\max_a\sum_{h_2}|E_d(a,h_2)|^2`, hence at most the displayed `d` factor. The non-coprime residue conventions and local-main bookings in (12) must also be compatible with that step rather than silently absorbed.

Please either persist this corrected Parseval-before-maximum route, including the exact residue-domain bookkeeping, or provide another argument that legitimately fixes the same maximizing residue across all shifts. Until then, the claim that (18) is an exact deduction from Mikawa plus WI-058 has a material proof gap.
