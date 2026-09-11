# MI-005 — Conservative marking does not restore an L1 rigidity estimate

**Evidence level:** proved route boundary; a splice using the particular canonical boundary germ is not refuted.

The tempting endpoint extension of marked `W^{1,r}` collar rigidity (`r>1`) is false even with the usual conservative constraints. On the fixed PF-185 collar slab, [PF-194](../../findings/PF-194-hamiltonian-reflection-marked-korn-still-fails-in-L1.md) constructs, for every `K>0`, a smooth Hamiltonian reflection-equivariant field with

\[
\|\nabla u\|_1>K\|\operatorname{Def}u\|_1.
\]

Short Hamiltonian flows give exact-area, zero-flux diffeomorphisms `H`, equal to the identity near the boundary and arbitrarily `C^1`-close to it, with `||H-id||_{W^{1,1}}>K||delta_{g,H^*g}||_1`. Thus determinant one, zero flux, reflection marking, boundary identity and near-identity size together still do not imply an energy-linear strong endpoint estimate. This is a map-level obstruction, not only the earlier determinant-one laminate obstruction.

The source of failure is an interior Hamiltonian oscillation. A construction required only to match the canonical PF-179--PF-184 outer germ could discard that oscillation; the counterexample does not show that every such splice has a large cost. The unresolved distinction is therefore generic rigidity of a supplied map versus existence of a better representative matching a prescribed germ. A weak/Lorentz splice would also need an operator estimate that actually consumes its weaker norm; it is not automatically a weak-trace theorem.
