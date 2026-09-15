# MI-024 — Exact cyclotomic recovery can be algebraically lossless and analytically useless

**Evidence level:** exact cyclotomic injectivity and quantitative prime-packet conditioning boundary from [PC-306](../../findings/PC-306-prime-polygon-centroid-is-algebraically-lossless-but-topologically-unstable.md) and [PC-307](../../findings/PC-307-polylog-oriented-prime-packets-require-near-qlogq-conditioning.md), sharpening the source-reconstruction saturation results [PC-304](../../findings/PC-304-oriented-tensor-hierarchy-reaches-full-dft-and-bispectral-completeness.md) and [PC-305](../../findings/PC-305-prime-support-reconstructs-at-source-sparsity-order.md).

PC-304--PC-305 show that sufficiently many ordinary source moments reconstruct the canonical prime support. PC-306 proves that exact finite-level identifiability is actually much cheaper and therefore even less informative as a geometric resource.

For prime conductor `q`, the normalized centroid

`b_q(A)=|A|^-1 sum_(a in A) zeta_q^a`

is injective on every nonempty vertex subset `A subset Z/qZ`. The proof is the prime cyclotomic minimal polynomial: after clearing the two subset cardinalities, equality of centroids gives an integer polynomial of degree at most `q-1` vanishing at `zeta_q`; the only possible multiple of `Phi_q=1+...+X^(q-1)` has zero coefficient after evaluation at `1`, hence the subsets coincide. Thus the degree-one oriented moment already determines the complete canonical prime support if retained as an exact cyclotomic-field element.

But this is not stable information in the growing-conductor topology. For any support `A`, translation gives

`F_(A+1)(k)=zeta_q^k F_A(k)`.

PC-306 gives the representation-level estimate `O(K/q)` for the first `K` modes. PC-307 inserts the actual prime packet asymptotics instead of the trivial amplitude bound. Uniformly for polylogarithmic frequencies,

`|F_q(k)| << (1+log(2+|k|))/(|k| log q)`,

so the prime support and its one-step translate differ by only

`O((1+log(2+K))/(q log q))`

in the relevant low-frequency packet. Since the two supports are disjoint, any downstream map that separates them by a fixed output margin must have Lipschitz/conditioning cost at least

`q log q/(1+log(2+K))`.

For fixed `K` this is order `q log q`; for every polylogarithmic `K` it is still `q log q/log log q` up to constants. The PNT/Li smooth source profile therefore makes the analytic instability substantially worse than the generic translation factor alone suggests. The constructive PC-305 moment count and the exact cyclotomic injectivity threshold are not stable-resolution thresholds.

**Exact algebraic injectivity, stable analytic recoverability and zero-sensitive usefulness are three different resources.** A packet can contain the whole source in exact arithmetic while two maximally different admissible supports approach each other in the declared analytic topology faster than any bounded-condition decoder can separate them.

This changes the live Prime-Circle audit. A finite packet is not interesting because it “contains the source” in exact arithmetic. A proposed mechanism must specify the topology and precision in which its distinction survives, quantify any singular amplification needed to turn the `1/(q log q)`-scale translated-prime packet difference into an order-one output, and explain why that amplification is forced and uniformly controlled by the geometry rather than by post-hoc decoding.

**Boundary.** The prime-conductor centroid theorem is classical cyclotomic rigidity and is not an RH mechanism. PC-307 uses the actual prime packet and its one-step translate in the stated low/polylogarithmic frequency range; it does not prove that every growing-band or nonlinear operation is unstable. Substantially larger bandwidth, a singular/nonlocal weighting, Li-centered residual structure, or genuinely cross-level information may evade this particular matched pair, but then its conditioning and source-specific mechanism must be proved rather than inferred from exact reconstruction.