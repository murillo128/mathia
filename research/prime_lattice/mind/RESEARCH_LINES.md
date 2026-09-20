# Prime-lattice research lines

This file records current mathematical questions for the Prime Lattice line. It is a mutable synthesis, not a task queue or history.

## Preserve the distinguished Nyman semigroup/target before self-adjoint closure erases the discrete dilation lattice

**Linked intuition:** `MI-044-finite-prime-wold-classification-does-not-globalize-atomically`.

PL-379 shows that exact finite-prime Wold classifications need not assemble into a global atomic type. PL-380--PL-381 identify strong repairs: a generating joint wandering space or semibounded exact log-prime covariance, together with double commutativity, forces the regular countable prime multishift and leaves only a prime-independent internal sector. That result is universal for positive locally finite frequencies, so globalization alone is not arithmetic.

PL-382 identifies the sharp boundary of that normal form. The classical Nyman/Bagchi dilation operators `D_p` on `L^2(0,1)` are commuting pure isometries with the same exact positive-energy covariance and a generating joint wandering subspace, but they are not doubly commuting. In logarithmic coordinates every `D_p` is one sampled time `log p` of a single right-shift semigroup, so distinct prime directions overlap inside one ordered half-line rather than forming orthogonal prime-Fock coordinates.

PL-383 now shows that the obvious self-adjoint closure of this overlap is too destructive. After adjoining adjoints, `S_s^*S_t=S_(t-s)` turns differences of sampled times into genuine shifts. Because `log 2/log 3` is irrational, two prime samples already generate a dense set of nonnegative times; strong continuity recovers the full right-shift semigroup, and

`W*(D_2,D_3)=B(L^2(0,1))`.

The same conclusion holds for any two incommensurate positive times. Thus the ambient von Neumann/SOT closure forgets the discrete integer/prime sampling completely. Passing from the distinguished dilation tuple to its self-adjoint strong closure cannot be the arithmetic invariant: it produces the maximal operator algebra for generic incommensurate controls as well.

The boundary is topology- and representation-sensitive. PL-383 does **not** show that the norm-closed `C*` algebra contains all real dilations, does not collapse the positive nonselfadjoint integer semigroup, and does not identify the compressed adjoints on the Nyman step space with ambient restrictions. The RH-equivalent target/subspace problem therefore remains live precisely where the ambient self-adjoint closure no longer applies.

The useful target is now a relation in the oriented integer dilation semigroup, the distinguished Nyman invariant subspace/target vector, or another nonselfadjoint/norm-sensitive structure that distinguishes actual arithmetic sampling from a generic incommensurate pair. Non-double-commutativity by itself is universal; maximal ambient self-adjoint closure is even more universal.

## Keep lattice faithfulness, multidirectional geometry, closure topology and target-relative arithmetic separate

Unique factorization still makes the integer dilation representation faithful: different prime exponent vectors give different dilation parameters. What collapses first is multidirectional geometry, because `alpha -> sum_p alpha_p log p` puts all directions on one continuous semigroup. What collapses next, once adjoints and strong closure are admitted, is the discrete sampling itself: two irrationally related times recover the full ambient continuous shift algebra.

Future work should therefore state which structure survives the chosen closure. The doubly commuting prime-lattice frame has a universal positive-energy Wold normal form; the ambient Nyman frame lies outside it through boundary overlap; the ambient self-adjoint strong closure then becomes `B(H)` and loses arithmetic sampling. A candidate mechanism deserves arithmetic credit only if it remains sensitive to the distinguished positive semigroup, compressed target-space geometry, norm topology, Mellin/continuation data or another source-specific relation that generic sampled shifts do not reproduce.