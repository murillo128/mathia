# MI-045 — Reciprocity closure is abelian-trivial and low-rank first, but all-depth faithfulness is still only source recovery

**Evidence level:** exact synthesis from [PC-347](../../findings/PC-347-full-radial-chen-signature-is-faithful-to-mangoldt-shell-path.md), [PC-349](../../findings/PC-349-reciprocity-closed-signature-has-rank-two-first-lie-defect.md), and [PC-350](../../findings/PC-350-full-inversion-defect-is-faithful-via-two-by-two-fourier-decoder.md). The signature/Fourier-uniqueness ingredients are classical; the source/destination interpretation is specific to the Prime-Circle construction.

Reciprocity closure has two very different information scales. At low degree it destroys almost everything; at all depths it can recover almost everything again. Neither fact by itself supplies zero selection.

PC-349 shows that closing the radial path by its forced exterior reciprocity ray kills the entire abelian signature. The first nonzero Lie term is the rank-two antisymmetric area

`A_mn = zeta(2) phi(m) phi(n) (g_n-g_m)`.

Thus commutative characters, determinants and first-order nonabelian summaries see only a universal low-rank defect.

PC-350 shows that this low-rank first layer is not an information ceiling. Use shell `2` as the canonical calibration coordinate and center

`W_n(r)=X_n(r)-phi(n)X_2(r)`.

Reciprocity gives `W_n(r)=W_n(1/r)`. A `2x2` solvable evaluation of the complete regularized defect isolates

`V_n(lambda)=int_0^infinity (1+r)^lambda dW_n(r)`.

For `lambda=i tau`, inversion rewrites this as the Fourier transform of a finite signed measure whose two pieces occupy disjoint intervals below and above `log 2`. Fourier uniqueness recovers `dW_n`, hence `W_n` and the original radial profile. In fact the repeated-shell-`2`/one-transverse subsector already suffices. The rank-two quantity from PC-349 is exactly the first derivative `V_n'(0)`; higher derivatives restore the transverse source information invisible at first order.

The matched-control audit is decisive. The same decoder works for any sufficiently regular reciprocal path family with one canonical calibration direction. All-depth faithfulness is therefore kinematic: it proves that the signature is a powerful source code, not that cyclotomic arithmetic has produced a Riemann-zero selector.

The reusable lesson is that **low-degree collapse and all-depth faithfulness can coexist**. One cannot infer source poverty from a small first Lie layer, but one also cannot infer arithmetic selectivity from eventual source reconstruction. The mathematically interesting regime lies between them: a strict quotient/invariant or growing-depth law that forgets generic reciprocal source freedom while retaining a destination-relevant arithmetic relation.

For Prime Circle, every future noncommutative proposal should identify that quotient before crediting additional depth. If the proposed observable is faithful on the matched reciprocal control class, it has merely encoded the path more accurately. If it collapses to the abelian or first-Lie data, it is already classified. The open space is a proper intermediate invariant with an independent zero-sensitive theorem.

**Boundary.** PC-350 proves injectivity for the complete regularized inversion defect under the stated reciprocity/calibration setup. It does not classify every quotient of that defect, every conductor-coupled depth regime, or every nonlinear destination map. Those remain possible only after matched-control selectivity is established.