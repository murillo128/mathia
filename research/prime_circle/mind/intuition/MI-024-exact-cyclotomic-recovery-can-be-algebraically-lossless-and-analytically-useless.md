# MI-024 — Exact cyclotomic recovery can be algebraically lossless and analytically useless

**Evidence level:** exact cyclotomic injectivity and conditioning boundary from [PC-306](../../findings/PC-306-prime-polygon-centroid-is-algebraically-lossless-but-topologically-unstable.md), sharpening the source-reconstruction saturation results [PC-304](../../findings/PC-304-oriented-tensor-hierarchy-reaches-full-dft-and-bispectral-completeness.md) and [PC-305](../../findings/PC-305-prime-support-reconstructs-at-source-sparsity-order.md).

PC-304--PC-305 show that sufficiently many ordinary source moments reconstruct the canonical prime support. PC-306 proves that exact finite-level identifiability is actually much cheaper and therefore even less informative as a geometric resource.

For prime conductor `q`, the normalized centroid

`b_q(A)=|A|^-1 sum_(a in A) zeta_q^a`

is injective on every nonempty vertex subset `A subset Z/qZ`. The proof is the prime cyclotomic minimal polynomial: after clearing the two subset cardinalities, equality of centroids gives an integer polynomial of degree at most `q-1` vanishing at `zeta_q`; the only possible multiple of `Phi_q=1+...+X^(q-1)` has zero coefficient after evaluation at `1`, hence the subsets coincide. Thus the degree-one oriented moment already determines the complete canonical prime support if retained as an exact cyclotomic-field element.

But this is not stable information in the growing-conductor topology. For any support `A`, translation gives

`F_(A+1)(k)=zeta_q^k F_A(k)`,

so the first `K` Fourier coefficients of `A` and `A+1` differ by at most `2 pi K/q` in sup norm. For the actual prime support, `P_q` and `P_q+1` are disjoint and hence maximally separated in total variation, yet every packet with `K=o(q)` converges to the same analytic observation. Even at the constructive PC-305 scale `K=L_q=O(q/log q)`, the packet distance is only `O(1/log q)`.

Therefore a downstream map that separates this matched pair by a fixed margin must have conditioning at least order `q/K`; at `K=L_q` this already diverges logarithmically. **Exact algebraic injectivity, stable analytic recoverability and zero-sensitive usefulness are three different resources.** Counting exact moments can overestimate information just as severely as counting coordinates can underestimate it.

This changes the live Prime-Circle audit. A finite packet is not interesting because it “contains the source” in exact arithmetic. A proposed mechanism must specify the topology and precision in which its distinction survives, quantify any singular amplification needed to turn a shrinking packet difference into an order-one output, and explain why that amplification is forced by the geometry rather than by post-hoc decoding.

**Boundary.** The prime-conductor centroid theorem is classical cyclotomic rigidity and is not an RH mechanism. The translated-support estimate proves instability for one canonical disjoint matched pair; it does not show that every growing-order operation is unstable. A singular or renormalized operator may amplify the difference, but then that amplification and its uniform control become the mathematical mechanism that needs proof.