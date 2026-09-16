# MI-043 — Support-scale interaction components bound effective relational arity

**Evidence level:** exact synthesis from [AF-372](../../findings/AF-372-finite-order-total-positivity-does-not-determine-laguerre-polya.md), [AF-376](../../findings/AF-376-uniform-separation-defeats-e-polya-frequency-determination.md) through [AF-379](../../findings/AF-379-vanishing-row-mesh-determines-continuous-translation-total-positivity.md), and the generator refinements [AF-381](../../findings/AF-381-prime-ratio-minors-determine-translation-total-nonnegativity.md) through [AF-384](../../findings/AF-384-strict-lower-order-positivity-collapses-order-k-to-solid-toeplitz-minors.md).

Nominal access to determinants of every order does not imply genuinely unbounded relational information. For a compact/local translation kernel with support width `w`, the intrinsic graph `G_w(E)` joins sampled rows only when their translates can interact. If its connected components have size at most `r`, every sampled Toeplitz determinant factors into blocks of order at most `r`; AF-377 makes this obstruction survive even when the minimum spacing of `E` vanishes.

The converse resource is finite-pattern closure. AF-379 shows that density of normalized sampled row patterns determines every continuous one-sided translation minor. AF-381 strengthens this to joint normalized row/column patterns: if arbitrary finite row and column configurations can be approximated after one common translation, fully sampled `E x E` minors determine the entire real translation target. Vanishing tail mesh is a sufficient condition, and `E={log p}` has it.

Placement complexity is a different axis from determinant order. AF-382 gives the strongest order-two collapse: for strictly positive profiles, logarithms convert adjacent `2x2` inequalities into mixed differences whose rectangle sums generate every sampled order-two inequality, so successor-prime rectangles already determine global `TN_2` on a vanishing mesh.

AF-383 gives the robust higher-order baseline. For every fixed order `k` and every lattice mesh `h`, every order-`k` Toeplitz minor is a nonnegative integer combination of minors whose rows are one consecutive `k`-block while the columns remain arbitrary. Translation invariance removes the starting row index, and shrinking mesh plus continuity closes the lattice certificate to continuum `TN_k`.

AF-384 shows exactly when the remaining column family also collapses. If the kernel is strictly totally positive through every order below `k`, classical finite `k`-positivity recognition turns nonnegative **solid consecutive** order-`k` minors into all order-`k` lattice minors. Hence, on shrinking lattices, one relative-offset family determines continuum `TN_k`. The compression is real but conditional: lower-order strict positivity is itself a strong resource.

The useful resource ledger is therefore:

- **relational arity:** unrestricted `PF_infinity` still needs unbounded determinant order by AF-372;
- **placement generators:** AF-383 removes one spatial tuple at every fixed order without strictness;
- **lower-order interiority:** AF-384 removes the other placement tuple at fixed order when strict positivity below `k` is already known;
- **continuum resolution:** a vanishing mesh is still needed to recover unsampled placements.

This prevents two opposite mistakes. Raw inequality count is not information: exact positive-generation/recognition theorems can make most placements redundant. But a compact generator family is only as cheap as the hypotheses that make it complete. In particular, importing solid-minor recognition into an RH-facing nonnegative kernel is illegitimate unless the source independently supplies the lower-order strictness needed by AF-384.

For prime logs, arithmetic specificity is pushed into provenance. A target-complete grid and a tiny generator family do not make the final positivity arithmetic. A source-selective route must explain why the arithmetic source forces the solid-generator signs and any required lower-order strictness, or else work in a boundary regime where the general AF-383 arbitrary-column family remains load-bearing.

**Boundary.** AF-383 is source-independent and does not reduce determinant order. AF-384 is also a target-side recognition theorem: it does not prove lower-order strict positivity for the RH-facing source and does not provide the sign of any solid generator. AF-382 uses a different order-two logarithmic/Monge mechanism. None of these placement compressions weakens the all-order requirement for unrestricted `PF_infinity`.
