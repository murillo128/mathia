---
type: adversarial-review
target: research/weil_positivity/findings/WP-032-global-determinantal-gram-completion-is-nonclosable-at-critical-weights.md
---

# Adversarial review

## Adversary

The central **nonclosability at the critical exponent** survives, but Sections 5--6 appear to criticalize the WP-030 Gram selector with the wrong power and therefore overstate the location of the global closability threshold.

WP-030 does not read the singleton arithmetic coefficient from the Gram diagonal itself. For a singleton `S={p}` it has

\[
G_{pp}=(\log p)^2,
\qquad
\sqrt{\det G_S}=\log p.
\]

After half-energy attenuation, the desired singleton **top volume** is

\[
\frac{\log p}{\sqrt p}.
\]

Therefore, if the attenuation is to be built *into the same rank-one Gram feature* while preserving the WP-030 volume readout, the criticalized feature amplitude should be

\[
b_p=\frac{\log p}{\sqrt p},
\]

and the corresponding rank-one Gram kernel should have

\[
K_{pq}=b_pb_q,
\qquad
K_{pp}=b_p^2=\frac{(\log p)^2}{p}.
\]

By contrast, WP-032 equation (14) sets the **diagonal** itself equal to `log p/sqrt(p)`, and equation (15) therefore uses coefficient vector

\[
\sqrt{\frac{\log p}{\sqrt p}},
\]

whose singleton top volume is `sqrt(log p/sqrt(p))`, not the WP-030/Weil coefficient `log p/sqrt(p)`.

This normalization matters beyond notation. With the WP-030 volume convention, the `sigma`-attenuated amplitude is

\[
b_p(\sigma)=(\log p)p^{-\sigma},
\]

so closability of the rank-one form on counting `\ell^2(\mathbb P)` is governed by

\[
\sum_p |b_p(\sigma)|^2
=\sum_p \frac{(\log p)^2}{p^{2\sigma}}.
\]

That series diverges at `sigma=1/2` and converges for every `sigma>1/2`. Thus the exact threshold for the **criticalized WP-030 Gram-volume realization** is `sigma=1/2`, not the Euler-product threshold `sigma=1` claimed in Section 6 from `sum_p (log p)p^{-sigma}`. The full prime-power version has the same threshold because the `k=1` subfamily is decisive.

So the title-level claim remains supportable: at the critical value `sigma=1/2`, the correct coefficient vector `(log p)/sqrt(p)` is not in `\ell^2`, since `sum_p (log p)^2/p` diverges, and the rank-one positive form is indeed nonclosable. The objection is to the stronger persisted identification of equations (14)--(20) with the WP-030 selector and to the asserted `sigma>1` closability boundary.

This is also relevant to WP-033: treating `log p/sqrt(p)` as a **quadratic diagonal mass** is a legitimate different model, but it is not automatically the same geometric normalization as WP-030, whose arithmetic coefficient is a square root of a singleton Gram determinant. Any downstream no-go using the diagonal-mass convention should distinguish that extra requirement from preservation of the original top-volume selector.

A repair can keep the decisive critical no-go while replacing the criticalized kernel by

\[
K_{pq}^{(\sigma)}
=(\log p)(\log q)(pq)^{-\sigma},
\]

and changing the threshold discussion accordingly. Alternatively, if the intention is deliberately to promote the Weil coefficient itself to a Gram diagonal rather than preserve the WP-030 top-volume normalization, the finding should state that as an additional modeling assumption and should not call the resulting `sigma>1` boundary the exact threshold of the WP-030 Gram geometry.
