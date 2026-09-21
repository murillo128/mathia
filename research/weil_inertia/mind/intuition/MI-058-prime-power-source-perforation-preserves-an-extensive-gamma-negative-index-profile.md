# MI-058 — Prime-power source perforation preserves an extensive gamma negative-index profile

**Evidence level:** exact source-conditioned spectral synthesis from [WI-377](../../findings/WI-377-source-perforation-preserves-digamma-negative-index-density.md), strengthening the bottom-of-spectrum obstruction WI-376. The statement concerns the corrected archimedean block on the true source-zero subspace; it does not classify the full coupled rooted operator.

Let `A_k=log(k+1)` and impose exact zero values on all true prime-power source slots. For every fixed depth `0<=eta<C_Gamma`, if `q_eta` is defined by the corrected whole-line symbol through `m(q_eta)=-eta`, WI-377 proves

`liminf iota^(src)_(eta,k)/A_k >= q_eta/pi`.

At depth zero the certified density is `q_0/pi = 2.0021169777...`. Thus source conditioning does not merely leave one bad bulk quasimode: it leaves linearly many negative directions at every fixed depth below the gamma floor.

The geometric reason is stronger than the measure estimate in WI-376. On any fixed macroscopic interior, only prime powers up to `k^(1-delta+o(1))` can create holes, and their aggregate screened jump-capacity tends to zero. A linear Dirichlet band can therefore be masked to vanish on every source slot with `o(1)` relative energy cost, preserving its dimension and the digamma spectral profile in the limit.

Consequently, if a repair acts **additively** on this source-zero block and makes it nonnegative, it cannot be finite-rank or `o(A_k)`-rank. At every fixed level `0<t<C_Gamma`, it must supply at least `(q_t/pi+o(1))A_k` positive spectral directions above level `t`. The missing resource is extensive coercivity on the inherited bulk, not merely a corrected sign at the bottom eigenvalue.

**Boundary.** The rank statement is conditional on an additive bounded self-adjoint repair of the corrected source-zero archimedean block. A fully coupled inherited-core/source/polar network may provide extensive coercivity in another category, and WI-377 neither proves that such a channel cannot exist nor establishes or refutes RH.