# Prime-lattice research lines

This file records current mathematical questions for the Prime Lattice line. It is a mutable synthesis, not a task queue or history.

## Preserve numerical prime weights or the distinguished Nyman target beyond universal ambient operator algebras

**Linked intuition:** `MI-044-finite-prime-wold-classification-does-not-globalize-atomically`.

PL-379--PL-381 show that a generating joint wandering space plus semibounded exact log-prime covariance and double commutativity forces a universal regular multishift normal form. PL-382 identifies the sharp boundary: the classical Nyman/Bagchi dilations satisfy the positive-energy covariance and have a generating wandering subspace but are not doubly commuting. In logarithmic coordinates every `D_p` is one sampled time `log p` of the same right-shift semigroup, so the prime lattice overlaps inside one ordered half-line.

PL-383 shows that adjoining adjoints and taking ambient strong closure is too destructive: two incommensurate prime times already recover the full continuous right-shift semigroup and generate `B(L^2(0,1))`. PL-384 moves the loss earlier. Without adjoining adjoints, the joint commutant of two irrationally related sampled shifts already equals the commutant of the full continuous flow; the same is therefore true of bicommutant and hyperinvariant-subspace data.

PL-385 now closes the obvious norm-topology escape at the level of the **unweighted ambient generated algebra**. Norm closure does preserve the oriented discrete positive semigroup sharply: `S_t` has distance `1` from the prime-generated norm algebra whenever `t` is not `log n`. But for every finite rationally independent time tuple the generated norm algebra is isometric to the corresponding polydisk algebra, and the countable prime algebra is the uniform closure of analytic cylinder polynomials on `T^infinity`. Replacing `(log p)` by any positive `Q`-linearly independent frequency sequence gives the same generator-preserving abstract norm algebra. Thus norm topology retains discreteness while still forgetting the **numerical prime geometry**.

The surviving route must therefore add structure not determined by the ambient commutant, self-adjoint closure or unweighted norm algebra. Natural live candidates are the positive-energy generator/covariance relation `[H,S_(log p)]=(log p)S_(log p)`, Mellin or analytic-continuation data, the distinguished Nyman invariant subspace/target, or another weight-sensitive relation coupling the actual `log p` values to arithmetic information. PL-385 does not show that any such enrichment succeeds; it shows that the ambient algebra alone cannot distinguish primes from a generic rationally independent frequency basis.

## Keep faithfulness, closure topology, abstract algebra type, numerical weights and target compression separate

Unique factorization still makes the integer dilation action faithful, and the norm algebra still distinguishes `log N` from nonsampled real times. Those facts are weaker than arithmetic rigidity: the same free positive-monoid/polydisk algebra occurs for generic rationally independent frequencies. At the opposite extreme, commutant and self-adjoint strong closure erase even more and recover continuous-flow invariants or all of `B(H)`.

Future work should therefore state exactly which extra structure remembers the values `log p` rather than only the abstract coordinate labels. A candidate receives arithmetic credit only if it survives a matched generic-frequency control and remains visible after restriction/compression to the RH-relevant Nyman target.