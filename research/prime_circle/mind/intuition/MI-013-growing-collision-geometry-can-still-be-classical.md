# MI-013 — Growing collision geometry can still be classical

**Evidence level:** proved

## Core intuition

Escaping a fixed finite residue packet by letting the collision carrier grow is necessary but not sufficient. A growing state can still be completely organized by classical arithmetic geometry. In the shared-upper Prime-Circle construction, the first comparable-scale carrier retains orientation and growing rank, yet its support is exactly a rank-one congruence lattice inside a rational triangle, and its determinant-like spectral volume reduces to collision weights and one-dimensional path-run combinatorics.

The useful discriminator is therefore not “does the dimension grow?” but “does the growing observable retain information outside a classical modular-discrepancy/path factorization?”

## Strongest justified claim

PC-253 proves for distinct primes `p<r<q` that the rank of the shared-upper defect is twice the number of points of an oriented congruence lattice `Lambda_ell` inside one rational triangle. The orientation can make the defect vanish or become macroscopic, so it is genuine information not visible in the earlier centered singular packets. But the support/counting law itself is classical rational-lattice geometry.

PC-254 keeps the ordered matching and computes the product of all nonzero singular values exactly. After ordering the collisions, the matching is monotone; the defect factors as `-U W V^T`, and the relevant Gram matrices are selected path-edge Grams. Their determinants split over consecutive runs, yielding a pseudodeterminant equal to the product of squared collision weights times elementary factors `|R|+1` for the path runs.

Thus neither growing rank nor determinant/log-volume compression supplies a new global zero-sensitive invariant in this branch.

## Synthesis of evidence

PC-249 closes fixed lower-prime cross-Grams beyond the Frobenius threshold. PC-251--PC-253 show how a new carrier reappears when all prime scales are comparable, while PC-254 demonstrates that one natural global compression of that carrier still classicalizes. This gives a stronger boundary than fixed-finite closure: growth can preserve new orientation without escaping classical modular organization.

The surviving candidates are the complete singular-value distribution, higher-order relations among collision cells before Gram contraction, several independent upper variables, or another growing source-defined statistic that cannot be recovered from the oriented lattice packet plus path incidence.

## Counterevidence / boundary cases

PC-254 does not classify the full singular spectrum of `W G_r W G_p`, arbitrary nonlinear functions of that spectrum, or higher-order/multi-upper observables. The classicalization of rank and pseudodeterminant therefore cannot be promoted to a no-go for all growing carriers.

A growing family of classical modular discrepancies can itself encode substantial arithmetic information. The claim is only that growth and orientation alone do not establish a new RH mechanism.

## Epistemic status

**Exact growing-carrier boundary:** the comparable-scale shared-upper defect has genuinely growing oriented support, but its rank is a classical modular-triangle count and its pseudodeterminant is an elementary weighted path-run product.

## Novelty/prior-art status

PC-253--PC-254 explicitly classify the surrounding lattice/path ingredients as classical or elementary and make no broad novelty claim. This intuition preserves that boundary.

## Falsification criterion

Show that the PC-253 rank is not determined by the stated oriented triangle lattice, or that PC-254's pseudodeterminant factorization fails for an admissible ordered collision matching. More strategically, exhibit a determinant-like or other low-complexity invariant of the same matching that provably contains information not determined by the current modular-lattice/path data; that would narrow the claimed classicalization boundary.

## Lean-formalizable core

The finite statement that a monotone selected-edge matching has Gram determinants equal to products of `(run length + 1)` and hence the PC-254 pseudodeterminant factorization is a natural finite combinatorial linear-algebra target.
