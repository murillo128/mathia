# MI-052 — Growing Euler jets leave the complete real ray exponentially blind into linear depth

**Evidence level:** exact synthesis from [RE-186](../../findings/RE-186-subcritical-growing-euler-jet-matching-with-ordinary-primes.md), [RE-196](../../findings/RE-196-fixed-depth-euler-jet-matching-collapses-the-full-real-ray.md), [RE-197](../../findings/RE-197-subcritical-growing-jets-collapse-the-full-real-euler-ray-superlogarithmically.md), [RE-198](../../findings/RE-198-linear-window-repair-collapses-the-full-real-euler-ray-through-every-sublinear-depth.md), and [RE-199](../../findings/RE-199-full-real-euler-collapse-persists-through-sub-quarter-linear-depth.md). The Laplace/Taylor mechanism is classical; the Mathia content is the uniform growing-order control supplied by the ordinary-prime repair geometry while the Robin transient remains macroscopic.

RE-196 shows that matching any fixed number of Euler boundary jets makes the whole positive real Euler discrepancy smaller than the selector debt by the corresponding fixed power of `log p`. RE-197 closes the growing-depth gap for the fixed-log-width repair. With `L=log p` and `K loglog p=o(L)`, the complete real ray is superlogarithmically smaller than the Robin selector debt `d_p`.

RE-198 shows that this condition was a property of the repair frame, not the scalar observation itself. Letting the ordinary-prime repair window grow linearly with `K` controls the first omitted centered moment and yields, for every growing `K=o(L)`,

`sup_(s>=1)|D_Q(s)| <= d_p exp(-(1-o(1))K log(L/K))`.

Thus the complete positive real Euler ray remains stably noncoercive through every sublinear jet depth.

RE-199 penetrates the nominal linear transition. The key is to retain the exact RE-188 repair radius `W=4K` instead of hiding it in an unspecified `CK`. After selector-centering, exact vanishing of the first `K+1` Laplace moments gives

`sup_(s>=1)|D_Q(s)| << d_p e^(C sqrt(K)) K ((4K+O(1))/L)^(K+1) + d_p p^(-1+o(1))`

uniformly for `K<=eta L`, every fixed `eta<1/4`. Therefore, if `K->infinity` in that wedge,

`sup_(s>=1)|D_Q(s)| <= d_p e^(-c_eta K)`.

If `K/L->kappa<1/4`, the sharper relative exponent is

`exp(-(1-o(1))K log(1/(4 kappa)))`.

The prime-power terms do not spoil the estimate. Keeping their exact centered rate shows that all harmonics `m>=2` retain an extra factor `p^-1` throughout this linear wedge. The first harmonic and the spatial repair radius are the load-bearing terms.

The geometric interpretation is stronger than the sublinear result. Exact identification from the full real Euler/Laplace ray is an infinite-precision theorem, but its inverse modulus on the Robin matched-control fibre can remain exponentially small even when the number of exactly matched boundary jets is a fixed positive fraction of `log p`. Increasing jet depth into the linear regime does not by itself restore stable source recovery; selector damping still beats the exact `4K` repair radius below the quarter-linear boundary.

The constant `1/4` is not claimed intrinsic. It is the threshold where the present absolute first-moment factor `(4K/L)^(K+1)` stops decaying. The exact source construction is valid much deeper than this, and RE-199 does not prove scalar rigidity at or above `K=L/4`. Signed cancellation in the first omitted moment, a narrower/nonuniform repair frame, or another scalar representation could move the boundary.

The reusable lesson is that **the relevant transition is set by repair radius versus selector damping, not by jet depth alone**. A scalar rigidity theorem must price the effective centered radius of every admissible matched repair, or control a signed source quantity that the absolute-moment bound throws away. Merely observing `K~log p` constraints is insufficient while a positive linear wedge remains continuum-near-null.

**Boundary.** RE-199 is a quantitative inverse-modulus theorem for the declared ordinary-prime `{0,1,2}` repair class with its `W=4K` geometry. It neither proves non-rigidity beyond the quarter-linear wedge nor contradicts exact continuum source identification. The destination ambiguity remains because the pre-repair Robin excursion stays order one while the complete real Euler observation becomes exponentially small at selector scale.