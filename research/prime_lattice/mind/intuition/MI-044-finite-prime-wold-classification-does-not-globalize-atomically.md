# MI-044 — Positive-energy Wold regularity and ambient self-adjoint closure both have sharp information-loss boundaries for Nyman dilations

**Evidence level:** literature-backed and exact-derived synthesis from [PL-379](../../findings/PL-379-infinite-prime-wold-globalization-failure.md)--[PL-383](../../findings/PL-383-two-prime-adjoint-closure-erases-discrete-dilation-lattice.md), interpreted against the scalarization boundaries of PL-377--PL-378.

PL-379 shows that finite-coordinate Wold classifications do not by themselves assemble into one global atomic type. PL-380 proves that a generating joint wandering space recovers the regular multishift when the coordinate sectors are orthogonal, and PL-381 gives an intrinsic sufficient condition: semibounded exact log-prime covariance plus double commutativity forces the global wandering space to generate and yields

`A ~= N_log tensor I + I tensor B`.

Because the same proof works for arbitrary positive locally finite frequency families, this positive-energy globalization is a universal coercivity mechanism rather than rational-prime arithmetic.

PL-382 shows that **double commutativity is the load-bearing boundary, not a technical convenience**. The Nyman/Bagchi normalized dilations `D_p` on `L^2(0,1)` are commuting pure isometries, satisfy the same semibounded exact covariance, and have a generating joint wandering subspace. Nevertheless they fail double commutativity through an infinite-rank boundary operator. In logarithmic coordinates `D_p` is the right translation `S_(log p)` on `L^2(R_+)`: the representation remains faithful on integers, but its multidirectional geometry has collapsed to one ordered half-line.

PL-383 identifies a second, opposite information-loss boundary. Once adjoints are adjoined, `S_s^*S_t=S_(t-s)` turns sampled-time differences into actual positive shifts. For two irrationally related times, such as `log 2` and `log 3`, those differences are dense; strong continuity recovers every `S_t`. The resulting von Neumann algebra is

`W*(D_2,D_3)=B(L^2(0,1))`.

Thus self-adjoint strong closure does not repair the non-double-commuting geometry into something arithmetic. It erases the discrete dilation lattice completely, and it does so for any generic incommensurate pair. The two tempting canonicalizations therefore fail in opposite ways: imposing double commutativity excludes the classical Nyman representation, while taking the full ambient self-adjoint strong closure keeps it but forgets the arithmetic sampling.

The reusable audit is to preserve the **distinguished generators, topology and target space** until one knows they are dispensable. Faithfulness of the positive integer semigroup can coexist with a universal one-parameter ambient model; adjoining adjoints plus SOT closure can then universalize that model all the way to `B(H)`. A useful operator invariant must live before that forgetful closure or on a target/invariant subspace where the ambient adjoint identity no longer descends unchanged.

For the Nyman route, surviving categories include the oriented nonselfadjoint integer semigroup, norm-sensitive `C*` structure, the compressed tuple on the Nyman step space, the distinguished target vector and Mellin/continuation relations. Each must still pass a generic-frequency control: merely retaining non-double-commutativity, incommensurability or ambient shift geometry is not arithmetic.

**Boundary.** PL-379 remains the general globalization obstruction without extra hypotheses. PL-381 remains exact for doubly commuting isometries. PL-382 locates Nyman outside that class. PL-383 is only an ambient von Neumann/SOT-closure theorem: it does not identify the norm-closed `C*` algebra, collapse the positive nonselfadjoint semigroup, or prove `W*(T_2,T_3)=B(M)` for compressed dilations on the Nyman step space. None of these results proves RH.