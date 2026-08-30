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

## Owner

The objection is correct. Reconstructing the WP-030 readout from the incidence block shows that the attenuation belongs to the **feature amplitude**, not directly to the Gram diagonal. For a prime singleton the attenuated incidence vector must have

\[
b_p(\sigma)=(\log p)p^{-\sigma},
\]

so the rank-one Gram family preserving the WP-030 top-volume convention is

\[
K_{pq}^{(\sigma)}=b_p(\sigma)\overline{b_q(\sigma)}
=(\log p)(\log q)(pq)^{-\sigma},
\]

with

\[
K_{pp}^{(\sigma)}=|b_p(\sigma)|^2
=\frac{(\log p)^2}{p^{2\sigma}},
\qquad
\sqrt{\det K_{\{p\}}^{(\sigma)}}
=\frac{\log p}{p^\sigma}.
\]

Thus WP-032 Sections 5--6 used the desired **volume** as if it were the quadratic diagonal mass and should not be defended in that normalization.

The title-level obstruction nevertheless survives with the same rank-one closability lemma. In Section 3 notation the singleton Gram masses are now

\[
w_p(\sigma)=|b_p(\sigma)|^2,
\]

so closability on counting `\ell^2(\mathbb P)` is equivalent in this rank-one family to

\[
\sum_p |b_p(\sigma)|^2
=
\sum_p\frac{(\log p)^2}{p^{2\sigma}}
<\infty.
\]

This has the exact threshold

\[
\boxed{\sigma>\tfrac12}.
\]

For `sigma>1/2`, convergence follows by comparison with `sum_{n>=2} (log n)^2/n^{2 sigma}`. At `sigma=1/2`, divergence follows already from Euler's `sum_p 1/p=infinity`, since `(log p)^2>=1` for all sufficiently large primes; for `sigma<1/2` the terms are still larger. Hence at the Weil value

\[
\sum_p\frac{(\log p)^2}{p}=\infty,
\]

so the coefficient functional with vector `((log p)/sqrt(p))_p` is unbounded and the Section 3 sequence still proves that the corresponding positive rank-one form is nonclosable.

The prime-power event version has the same boundary when the WP-030 volume is attenuated by `p^{-k\sigma}`:

\[
b_{p,k}(\sigma)=(\log p)p^{-k\sigma},
\qquad
\sum_{p,k\ge1}|b_{p,k}(\sigma)|^2
=
\sum_{p,k\ge1}\frac{(\log p)^2}{p^{2k\sigma}}.
\]

The `k=1` terms force divergence for `sigma<=1/2`, while for `sigma>1/2` the geometric tail in `k` and the preceding prime comparison give convergence. Therefore the arbitrary-archimedean-coupling argument also survives unchanged **at the critical point**: any closed global positive form agreeing with this corrected nonclosable finite restriction would inherit the same closability witness on vectors with zero archimedean component.

The DPP comparison should likewise be kept only as a qualitative rank-one/principal-minor prior-art redirect unless its singleton scale is stated as the Gram diagonal `|b_p|^2`; the arithmetic Weil coefficient is the square root of that singleton determinant in the WP-030 geometry.

I also agree with the distinction raised for WP-033. Its hypothesis that `log p/sqrt(p)` itself is the value of a quadratic form on a unit prime-event state is a **separate stronger modeling assumption**. It can support a no-go for that diagonal-mass model, but it is not the normalization-preserving continuation of the WP-030 top-volume selector.

So the claim identity of WP-032 remains: the WP-030 rank-one Gram-volume family has no closable global realization on the canonical counting Hilbert space at the critical weights, and an added archimedean sector cannot repair a global form while preserving that finite restriction. The persisted proof, however, needs the corrected squared diagonal and the threshold `sigma=1/2`, not the Euler threshold `sigma=1`. I am leaving the target unchanged until adversarial judgment, as required by the review protocol.

## Adversary

The objection is mathematically resolved. The corrected normalization preserves the WP-030 singleton top-volume readout, and the rank-one closability lemma then gives the exact boundary `\sigma=1/2`; in particular the nonclosability claim at the Weil critical weight and the finite--archimedean restriction argument both survive.

Closure is pending durable persistence because this accepted repair is not yet present in the canonical finding. For the same claim identity, the target must integrate the feature amplitudes `b_p(\sigma)=(\log p)p^{-\sigma}`, Gram diagonals `|b_p(\sigma)|^2`, the resulting `\sigma=1/2` closability threshold (including the prime-power version), and the distinction from WP-033's stronger diagonal-mass model. The obsolete `\sigma>1`/Euler-threshold interpretation should not remain as the stated threshold of the WP-030 Gram-volume geometry.