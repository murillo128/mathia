# MI-043 — Support-scale interaction components bound effective relational arity

**Evidence level:** exact synthesis from [AF-372](../../findings/AF-372-finite-order-total-positivity-does-not-determine-laguerre-polya.md), [AF-376](../../findings/AF-376-uniform-separation-defeats-e-polya-frequency-determination.md) through [AF-379](../../findings/AF-379-vanishing-row-mesh-determines-continuous-translation-total-positivity.md), and the generator refinements [AF-381](../../findings/AF-381-prime-ratio-minors-determine-translation-total-nonnegativity.md) through [AF-385](../../findings/AF-385-sampled-solid-minor-hierarchy-certifies-continuum-fixed-order-total-nonnegativity.md).

Nominal access to determinants of every order does not imply genuinely unbounded relational information. For a compact/local translation kernel with support width `w`, the intrinsic graph `G_w(E)` joins sampled rows only when their translates can interact. If its connected components have size at most `r`, every sampled Toeplitz determinant factors into blocks of order at most `r`; AF-377 makes this obstruction survive even when the minimum spacing of `E` vanishes.

The converse resource is finite-pattern closure. AF-379 shows that density of normalized sampled row patterns determines every continuous one-sided translation minor. AF-381 strengthens this to joint normalized row/column patterns: if arbitrary finite row and column configurations can be approximated after one common translation, fully sampled `E x E` minors determine the entire real translation target. Vanishing tail mesh is a sufficient condition, and `E={log p}` has it.

Placement complexity is a different axis from determinant order. AF-382 gives the strongest order-two collapse: for strictly positive profiles, logarithms convert adjacent `2x2` inequalities into mixed differences whose rectangle sums generate every sampled order-two inequality, so successor-prime rectangles already determine global `TN_2` on a vanishing mesh.

AF-383 gives the unrestricted higher-order baseline. At fixed order `k`, every lattice Toeplitz minor is a nonnegative integer combination of minors with one consecutive row stencil and arbitrary columns. AF-384 then shows that strict lower-order total positivity collapses the remaining placement axis: solid order-`k` minors suffice.

AF-385 sharpens the hidden side-information cost. The lower-order strictness consumed by finite `k`-positivity recognition does **not** have to be known on the continuum or on arbitrary placements. On any mesh sequence `h_m -> 0`, it is enough to have the solid one-parameter determinants

`C_(j,h_m)(d)=det(f((d+a-b)h_m))_(a,b=0)^(j-1)`

strictly positive for every `j<k` and nonnegative for `j=k`. The finite recognition theorem reconstructs every lattice minor through order `k`; continuity then gives continuum `TN_k`. Strict sampled margins may vanish in the limit, so this is genuinely weaker than assuming continuum strict total positivity below `k`.

The resource ledger is therefore:

- **relational arity:** unrestricted `PF_infinity` still needs unbounded determinant order by AF-372;
- **placement generators:** one-axis placement suffices without strictness by AF-383, while the full fixed-order placement family collapses to solid relative-offset generators under the sampled strict-interior hierarchy of AF-385;
- **interiority hierarchy:** compression at order `k` consumes strict signs at every lower order on the sampled solid family, not an independent continuum strictness theorem;
- **continuum resolution:** a shrinking mesh is still needed, and each mesh retains infinitely many relative offsets.

This prevents two opposite mistakes. Raw inequality count is not information: recognition theorems can make most placements redundant. But a small generator family is not a finite or source-selective certificate merely because it has low geometric dimension. Its completeness may still consume unbounded determinant order, infinitely many offsets, shrinking spatial scales and strict lower-order signs.

For prime logs, arithmetic specificity is therefore pushed almost entirely into provenance of the generator signs. A target-complete grid and a triangular solid-minor hierarchy do not make the final positivity arithmetic. A source-selective route must explain why the RH-facing source forces the required sampled strict/nonnegative hierarchy across growing order, rather than assume the target certificate itself.

**Boundary.** AF-383--AF-385 are source-independent target-recognition statements. They do not provide any solid-minor sign for the Riemann-associated kernel and do not weaken AF-372's all-order requirement for unrestricted `PF_infinity`. AF-385 also does not imply continuum strict positivity from sampled strictness; only continuum nonnegativity is obtained by closure.
