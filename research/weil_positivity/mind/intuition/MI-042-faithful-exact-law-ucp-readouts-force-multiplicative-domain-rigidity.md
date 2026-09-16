# MI-042 — Faithful exact-law UCP readouts are rigid, and quadratic tail energy is the exact moving-observable stability scale

**Evidence level:** exact/classical-mechanism synthesis from [WP-329](../../findings/WP-329-deterministic-amalgamated-lifts-make-operator-valued-free-divisibility-universal-before-scalarization.md) through [WP-340](../../findings/WP-340-stationary-hilbertian-transport-controls-the-ucp-defect-exactly-when-it-contains-euclidean-drift.md). Kadison--Schwarz, Stinespring/multiplicative-domain theory, transport moment control, mean ergodicity and negative-type representations are classical; the Mathia content is their sharp source-readout boundary at expanding arithmetic cutoffs.

WP-329--WP-330 show that enriched variables can be universally positive while all source specificity sits in an external scalar state or in a fluctuation sector killed by that state. WP-331--WP-332 show the opposite exact boundary: if a faithful UCP readout preserves the first and second moments of the same self-adjoint source observable, its Kadison defect vanishes and the observable enters the multiplicative domain.

WP-333--WP-337 expose why approximate preservation is nonuniform when the observable grows with the cutoff. Vanishing off-diagonal probability can travel a reciprocal distance and retain order-one variance. The sharp propagation ledger separates channel escape mass, bidirectional radii and barycentric bias.

WP-338 identifies the invariant quantity directly. For a row law `P_x` and source atom `delta_x`,

`W_2(P_x,delta_x)^2 = Q(x) + beta_x^2`,

where `Q` is the Kadison defect and `beta_x` the coordinate bias. Every `W_p` with `p<2` can vanish under rare long jumps while `Q` stays fixed; `p>=2` controls the defect, with `p=2` exact.

WP-339 shows that this is not a peculiarity of power costs. For any scalar displacement cost `c`, channel convergence plus vanishing `c`-transport controls the defect uniformly over growing supports **iff** `c(r)` eventually dominates a positive multiple of `r^2`. If `liminf c(r)/r^2=0`, an exact-barycentric three-point rare-jump family has channel norm and `c`-cost tending to zero with defect exactly one. Thus every successful universal scalar transport repair already contains the missing quadratic tail moment.

WP-340 gives the same classification inside the canonical stationary Hilbertian/negative-type category. A `Z`-cocycle satisfies

`b(n)/n -> P b(1)`

by mean ergodicity, so its squared distance has a nonzero quadratic tail exactly when the cocycle has an invariant affine drift. In Lévy--Khintchine language this is the positive quadratic coefficient. Pure spectral/jump Hilbert geometry is `o(n^2)` and fails the intrinsic dyadic rare-long-jump witness. Nonzero drift succeeds only by reproducing Euclidean squared displacement.

The reusable stability object is therefore **quadratic displacement energy**, not Wasserstein notation, an Orlicz choice or Hilbert embeddability. The propagation estimates can force it small under suitable hypotheses; `W_2` measures it directly; every universally successful scalar/Hilbertian topology must pay it asymptotically. A viable Weil route must derive this energy decay from source-specific arithmetic that matched controls cannot fake, or introduce a genuinely global/noncommutative sign mechanism outside the rowwise commutative category.

**Boundary.** These results concern one moving real source coordinate in commutative Markov/UCP readouts. They do not generate Gamma/polar terms, a source-selective sign or Weil positivity. On uniformly bounded support weaker moments can control stronger ones with diameter-dependent constants. Quadratic control should not be counted as a new mechanism when it merely restates vanishing of the defect.