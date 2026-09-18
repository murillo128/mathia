# MI-052 — Subcritical growing Euler jets make the complete real ray superlogarithmically blind

**Evidence level:** exact synthesis from [RE-186](../../findings/RE-186-subcritical-growing-euler-jet-matching-with-ordinary-primes.md), [RE-196](../../findings/RE-196-fixed-depth-euler-jet-matching-collapses-the-full-real-ray.md), [RE-197](../../findings/RE-197-subcritical-growing-jets-collapse-the-full-real-euler-ray-superlogarithmically.md), and [RE-198](../../findings/RE-198-linear-window-repair-collapses-the-full-real-euler-ray-through-every-sublinear-depth.md). The Laplace/Taylor mechanism is classical; the Mathia content is the uniform growing-order control supplied by ordinary-prime repair geometry while the Robin transient remains macroscopic.

RE-196 shows that matching any fixed number of Euler boundary jets makes the whole positive real Euler discrepancy smaller than the selector debt by the corresponding fixed power of `log p`. RE-197 then closes the growing-depth gap for the fixed-log-width repair of RE-186. With `L=log p` and `K loglog p=o(L)`, one gets

`sup_(s>=1)|D_Q(s)| <= d_p (C/L)^(K+1) + d_p p^(-1/2+o(1))`,

so if `K->infinity` the complete real ray is superlogarithmically smaller than the Robin selector debt `d_p`.

RE-198 shows that the `K loglog p=o(L)` condition was a property of the fixed-width repair, not the scalar observation itself. Letting the ordinary-prime repair window grow linearly with `K` controls the first omitted moment by the corresponding linear-width geometry and yields, for every growing `K=o(L)`,

`sup_(s>=1)|D_Q(s)| <= d_p exp(-(1-o(1)) K log(L/K))`.

Thus the **entire positive real Euler ray remains stably noncoercive through every sublinear jet depth**. The matched control preserves the relevant ordinary-prime realization and an order-one transient Robin excursion while its scalar Euler discrepancy collapses uniformly on all `s>=1`.

The geometric interpretation is now cleaner. Exact identification from the full real Laplace/Euler ray is an infinite-precision statement, but its inverse modulus on the Robin matched-control fibre is catastrophically small. Increasing boundary-jet depth does not restore stable source recovery anywhere in the continuum range `K=o(log p)`; the repair simply widens enough to absorb the extra moment constraints while the selector damping still wins.

This moves the scalar rigidity frontier to a genuine scale transition. The first unresolved continuum depth is `K` comparable to `L=log p`, where the linear repair window is no longer subcritical relative to the selector scale. At still higher orders RE-189 identifies a separate high-derivative saturation phenomenon near the log-squared regime. A stable theorem must therefore either cross the `K~log p` transition, impose a signed/source restriction that rules out these ordinary-prime repairs, or leave the scalar real-ray channel for a joint or nonlocal invariant whose response is not annihilated by moment matching.

The reusable lesson is that **wider analytic observation does not repair an unstable inverse map when the source class contains growing matched near-kernels**. One must compare the observation's precision and jet depth with the source's repair capacity, not infer stability from injectivity of the infinite continuum transform.

**Boundary.** RE-198 does not prove non-rigidity at linear or superlinear depth, include arbitrary reciprocal-variation padding, or contradict exact continuum source identification. It is a quantitative inverse-modulus theorem for the declared ordinary-prime matched-control class. The destination ambiguity remains because the Robin transient survives while the complete real Euler observation becomes superlogarithmically near-null.