# Farey-discrepancy research lines

This file records current mathematical questions for the Farey-discrepancy line. It is a mutable synthesis, not a chronology or task list.

## Quantify the one-sided slack needed to realize a signed blind correction

**Linked intuition:** `MI-039-periodic-scale-switching-can-create-a-supercritical-floquet-blind-mode`.

FD-225--FD-227 remove switched inversion conditioning, improve prime resolution and show that smooth positive power-law capacity profiles are visible. FD-228--FD-230 then close the broader positive-cushion escape: fixed-period oscillation does not help, strict first-lag dominance rules out bounded dyadic-band cushions with macroscopic mass, and even arbitrary nonnegative within-band redistribution under the natural linear capacity envelope cannot retain a positive fraction of late-band capacity while remaining switched-subquadratic.

FD-231 identifies the exact boundary. Signed linear-capacity profiles can carry a fixed positive fraction of both positive and negative total variation on every late dyadic band while the **entire all-integer divisor response** is only first order. The obstruction is therefore not a norm lower bound for the divisor-response operator. It is the one-sided source constraint: a physical prime-flip occupancy is nonnegative.

The live capacity problem is now source-realizability of the particular signed correction required by the Mertens baseline. Given a signed switched-blind direction, how large a nonnegative reservoir offset is forced before both signs fit inside the prime-cell capacities, and can that offset itself remain compatible with the switched observation budget? A decisive result should either construct such a source-realizable correction with sufficient lower slack or prove that every realization necessarily pays a macroscopic positive-cushion cost of the kind FD-230 detects.

## Keep signed nullspace, positive occupancy and physical correction cost distinct

Exact divisor inversion means the algebraic response equations are no longer the bottleneck, and scale-adapted cells mean an avoidable prime-resolution loss is gone. FD-231 shows that large signed blind directions still exist after both cleanups. FD-230 shows that the same statement is false for nonnegative macroscopic occupancy.

Future coercive arguments must therefore remain one-sided. A lower bound in total variation, an `ell^p` norm or separate positive/negative mass cannot be true on the whole signed correction space. Conversely, the existence of a signed blind vector does not by itself produce one admissible source. The physical currency is the positive slack required to embed the signed correction into a single nonnegative reservoir profile while cancelling the actual Mertens term.