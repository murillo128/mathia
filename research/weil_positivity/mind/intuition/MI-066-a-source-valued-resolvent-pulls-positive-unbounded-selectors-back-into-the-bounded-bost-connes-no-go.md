# MI-066 — A source-valued resolvent pulls positive unbounded selectors back into the bounded Bost--Connes no-go

**Evidence level:** exact operator-category synthesis from [WP-394](../../findings/WP-394-source-resolvent-visibility-collapses-positive-unbounded-mixed-prime-selectors.md), using the bounded positive-cone obstruction of WP-392.

Let `q` be a densely defined closed nonnegative form in a standard positive-energy Bost--Connes representation, with associated self-adjoint operator `T>=0`. Suppose that for one `lambda>0`,

`R_lambda=(T+lambda I)^(-1)`

belongs to the represented bounded source algebra `pi(A_BC)`. Then the canonical bounded transform

`B_lambda=T(T+lambda I)^(-1)=I-lambda R_lambda`

is a positive contraction in the same source algebra.

If every mixed-prime basis vector lies in the form domain and has `q(e_k)=0`, then `T^(1/2)e_k=0`, hence `B_lambda e_k=0` on every mixed-prime label. WP-392 applies directly to this positive bounded source element and forces `B_lambda=0`. Since `t/(t+lambda)` vanishes only at `t=0`, spectral calculus then gives `T=0` and therefore `q=0`.

The same reduction applies to a closable nonnegative form after passing to its closure, provided the mixed-prime nullity survives on the original domain and the closed operator has such a source-valued resolvent. Only one resolvent is needed; the whole functional calculus need not lie in the source algebra.

This boundary is genuinely stronger than the unital-affiliation collapse in MI-065. There are genuinely unbounded positive self-adjoint operators whose resolvent lies in `pi(A_BC)`, so source-resolvent visibility is a real unbounded category. What fails is combining that visibility with exact mixed-prime nullity.

A surviving positive unbounded selector must therefore avoid this pullback in a load-bearing way: its relevant canonical resolvent or bounded transform must leave `pi(A_BC)`, its domain/support condition must differ from exact mixed-prime nullity, the representation/correspondence must change, or prime-power support must emerge only after a larger finite--archimedean/global operation. Merely moving to a nonunital or boundary construction does not help if the represented resolvent falls back into the already-classified bounded source algebra.

**Boundary.** The argument uses nonnegativity, dense closedness (or closure of a closable form), exact mixed-prime nullity on basis vectors in the form domain, and one resolvent in the represented norm-closed Bost--Connes C-star algebra. Approximate suppression, signed forms, bicommutant-only resolvents, different modules/representations, and global assembly remain outside the obstruction.