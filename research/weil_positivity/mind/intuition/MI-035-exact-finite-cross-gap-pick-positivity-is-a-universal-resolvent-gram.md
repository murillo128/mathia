# MI-035 — Exact finite and confluent cross-gap Pick positivity is a universal higher-resolvent Gram

**Evidence level:** exact finite-section classification from [WP-322](../../findings/WP-322-multipoint-boundary-pick-positivity-is-universal-across-exact-gap-nodes.md), extended to arbitrary fixed finite boundary jets by [WP-323](../../findings/WP-323-finite-confluent-pick-jets-are-universal-resolvent-gram.md). The Pick/Loewner, Carathéodory--Fejér and Schur-complement facts are classical; the arithmetic-selectivity conclusion is the line-specific synthesis.

WP-321 leaves open a discontinuous escape: perhaps exact simultaneous values at several arithmetic gap nodes satisfy a positive cross-gap relation that atomwise smoothing cannot preserve. WP-322 classifies the canonical scalar first-order version. For any scalar Herglotz function with positive representing measure and any finite set of regular real nodes `t_i`, the boundary Loewner matrix is exactly the Gram matrix of resolvent vectors `(sqrt(a),(x-t_i)^-1)`. Exact arithmetic locations can change entries, but not the universal reason for positivity.

WP-323 shows that taking more exact local information at those nodes does not change this conclusion. For finite jet orders `R_i`, normalized derivatives of the Pick kernel satisfy

`C_(i,r),(j,s) = a delta_(r0)delta_(s0) + int dmu(x)/[(x-t_i)^(r+1)(x-t_j)^(s+1)]`.

Thus the confluent matrix is the Gram matrix of the higher resolvent vectors

`(sqrt(a) delta_(r0), (x-t_i)^(-r-1))`.

Every finite confluent Pick matrix is positive semidefinite for **every** positive scalar Herglotz source satisfying the required moments, and with infinite support it is generically strictly positive definite. The reflected Mangoldt source has all fixed finite gap-node jet moments needed here, so this is not a regularity dodge: arbitrary fixed-order exact arithmetic derivatives exist but their Pick positivity remains universal.

Boundary Julia--Nevanlinna reductions, principal minors and Schur-complement consequences stay inside the same cone. Raising the finite jet order therefore adds numerical source fingerprints without adding a source-selective sign theorem. Finite boundary Carathéodory--Fejér positivity is another representation of the same obstruction when it is generated solely by the scalar Pick kernel.

The scalar frontier is narrower: a surviving exact invariant must use support/mass/multiplicative arithmetic in a way not equivalent to positivity of finitely many scalar Pick-kernel jets, or the construction must leave the scalar Herglotz finite-section category for genuinely matrix/operator-valued, indefinite-to-positive, infinite-node/domain or finite--archimedean structure with an independent sign theorem.

**Boundary.** WP-322--WP-323 are finite-section statements. They do not classify arbitrary nonlinear functions of the exact support/masses, infinite-order jets, infinite-node operator domains, genuinely matrix-valued Herglotz functions, or direct archimedean coupling. They also do not say the exact matrix entries are non-arithmetic; only the positivity mechanism is universal.