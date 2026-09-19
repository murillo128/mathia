# Prime-lattice research lines

This file records current mathematical questions for the Prime Lattice line. It is a mutable synthesis, not a task queue or history.

## Exploit source-specific structure in the Nyman boundary defect rather than canonicalizing it away

**Linked intuition:** `MI-044-finite-prime-wold-classification-does-not-globalize-atomically`.

PL-379 shows that exact finite-prime Wold classifications need not assemble into a global atomic type. PL-380--PL-381 identify strong repairs: a generating joint wandering space or semibounded exact log-prime covariance, together with double commutativity, forces the regular countable prime multishift and leaves only a prime-independent internal sector. That result is universal for positive locally finite frequencies, so globalization alone is not arithmetic.

PL-382 identifies the sharp boundary of that normal form. The classical Nyman/Bagchi dilation operators `D_p` on `L^2(0,1)` are commuting pure isometries with the same exact positive-energy covariance and a generating joint wandering subspace, but they are not doubly commuting. The defect is an infinite-rank boundary sector. In logarithmic coordinates every `D_p` is one time `log p` of a single right-shift semigroup, so distinct prime directions overlap inside one ordered half-line rather than forming orthogonal prime-Fock coordinates.

The live question is therefore not whether the Nyman representation can be forced back into the regular multishift: PL-382 shows that doing so would exclude a classical RH-equivalent route by hypothesis. The useful target is a relation in the overlapping dilation/boundary geometry that is specific to the actual Nyman arithmetic or target vector and fails for a generic one-parameter shift semigroup. Non-double-commutativity by itself is universal and supplies no zero-sensitive mechanism.

## Keep lattice faithfulness, multidirectional operator geometry, double commutativity and arithmetic discrimination separate

Unique factorization still makes the integer dilation representation faithful: different prime exponent vectors give different dilation parameters. What collapses is the operator geometry, because the map `alpha -> sum_p alpha_p log p` places all directions on one continuous semigroup and creates overlapping boundary ranges.

Future work should therefore state which geometry is being used. The doubly commuting prime-lattice frame has an exact positive-energy Wold normal form; the Nyman dilation frame lies outside it for a concrete boundary reason. A candidate mechanism deserves arithmetic credit only if it exploits source/target relations inside that overlap which generic positive frequency samples of the same right-shift semigroup do not possess.