# MI-052 — Subcritical growing Euler jets make the complete real ray superlogarithmically blind

**Evidence level:** exact synthesis from [RE-186](../../findings/RE-186-subcritical-growing-euler-jet-matching-with-ordinary-primes.md), [RE-196](../../findings/RE-196-fixed-depth-euler-jet-matching-collapses-the-full-real-ray.md), and [RE-197](../../findings/RE-197-subcritical-growing-jets-collapse-the-full-real-euler-ray-superlogarithmically.md). The Laplace/Taylor mechanism is classical; the Mathia content is the uniform growing-order control supplied by the fixed-log-width ordinary-prime repair geometry while the Robin transient remains macroscopic.

RE-196 shows that matching any fixed number of Euler boundary jets makes the whole positive real Euler discrepancy smaller than the selector debt by the corresponding fixed power of `log p`. Its deliberate gap was growing jet depth: the first uncontrolled centered transport moment had not been bounded uniformly in `K`.

RE-197 closes that gap throughout the fixed-window subcritical regime already constructed by RE-186. Let `L=log p` and let the ordinary-prime `{0,1,2}` matched control match jets through order `K`, with

`K loglog p=o(log p)`.

Then for some absolute `C>1`,

`sup_(s>=1)|D_Q(s)| <= d_p (C/log p)^(K+1) + d_p p^(-1/2+o(1))`,

where `d_p~1/(sqrt(p)log p)` is the Robin selector debt. If `K->infinity`, this becomes

`sup_(s>=1)|D_Q(s)| <= d_p exp(-(1-o(1))K loglog p)`.

Thus increasing the exact jet depth buys essentially one further factor `1/log p` per matched derivative **uniformly on the entire positive real Euler axis**, not merely near `s=1`.

The reason is geometric. RE-186 performs the repair in a fixed centered logarithmic window and advances by exponentially small microsteps while the residual mass contracts geometrically. The first omitted normalized transport moment therefore grows only like `C^K`, not `(CK)^K`. After factoring the common selector decay, Taylor's remainder contributes `C^K/(log p)^(K+1)`. The quantization tail and higher prime-power modes stay below a `p^-1/2+o(1)` relative floor throughout the same subcritical condition.

This sharpens the distinction between exact identification and stable destination information. The scalar Euler channel is analytically injective at infinite precision, yet one can preserve exact growing jets, every fixed KV source envelope, ordinary-prime bounded multiplicities and an order-one transient Robin excursion while making the **complete real spectral ray** superlogarithmically smaller than the selector debt.

The surviving scalar rigidity frontier is therefore not “observe a wider real interval” and not “let the number of boundary derivatives grow slowly.” Any stable scalar theorem must cross the fixed-window depth `K loglog p=o(log p)`, impose a genuinely coercive signed source restriction that excludes the RE-186 repair, or use a joint/nonlocal invariant whose response cannot be annihilated by this moment geometry.

The theorem does not reach the larger constructive region of RE-188, whose repair width grows with `K`, nor the log-squared high-order saturation regime of RE-189. Those are genuinely different scales: widening the source window changes the first omitted moment, while normalized high derivatives eventually collapse for a separate reason.

**Boundary.** RE-197 does not include arbitrary growing reciprocal-variation padding, prove non-rigidity beyond `K loglog p=o(log p)`, or contradict exact continuum source identification. It is a quantitative inverse-modulus result for the current matched-control class. The destination ambiguity remains only because the Robin transient survives while the scalar Euler observation becomes superlogarithmically near-null.