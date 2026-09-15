# MI-035 — Exact finite cross-gap Pick positivity is a universal resolvent Gram

**Evidence level:** exact finite-section classification from [WP-322](../../findings/WP-322-multipoint-boundary-pick-positivity-is-universal-across-exact-gap-nodes.md), strengthening the weak-topology matched-control obstruction WP-321. The Pick/Loewner and Schur-complement facts are classical; the arithmetic-selectivity conclusion is the line-specific synthesis.

WP-321 leaves open a discontinuous escape: perhaps exact simultaneous values at several arithmetic gap nodes satisfy a positive cross-gap relation that atomwise smoothing cannot preserve. WP-322 classifies the canonical scalar version of that idea.

For any scalar Herglotz function with positive representing measure and any finite set of regular real nodes `t_i`, the boundary Loewner matrix satisfies

`L_ij = a + int dmu(x)/[(x-t_i)(x-t_j)]`.

Thus `L` is exactly the Gram matrix of the resolvent vectors `(sqrt(a),(x-t_i)^-1)` and is positive semidefinite for **every** positive scalar Herglotz source. With infinite support it is generically strictly positive definite. Exact arithmetic locations can change the matrix entries, but they do not change the reason for positivity.

Boundary Julia--Nevanlinna reductions do not escape this cone. Their finite-node effect is Schur complementation of the same Pick matrix, equivalently orthogonal projection of the resolvent vectors. Every resulting finite positivity statement is therefore inherited from universal Hilbert-space Gram geometry rather than from Mangoldt arithmetic.

This closes a stronger route than WP-321. The obstruction no longer depends on smoothing, weak convergence or a specially engineered matched source: **finite exact multipoint Pick positivity itself is source-independent**. Adding more exact gap nodes, principal minors or finite Julia reductions cannot turn that sign theorem into the missing arithmetic positivity mechanism.

The scalar frontier is narrower. A surviving exact invariant must use support/mass arithmetic in a way that is not equivalent to positivity of a scalar Pick kernel, or the construction must leave the scalar Herglotz category for genuinely matrix/operator-valued, indefinite-to-positive, infinite-domain or finite--archimedean structure with an independent sign theorem.

**Boundary.** WP-322 is finite-section. It does not classify boundedness/closability of an infinite gap-node operator, genuinely matrix-valued Herglotz functions, or arbitrary support-sensitive invariants. It also does not say the exact matrix entries are non-arithmetic; only their positivity is universal.