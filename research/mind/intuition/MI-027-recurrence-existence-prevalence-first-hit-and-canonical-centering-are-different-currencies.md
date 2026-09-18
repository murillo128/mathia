# MI-027 — Recurrence existence, prevalence, first hit and canonical centering are different currencies

**Evidence level:** supported cross-line synthesis from the Nyman--Beurling recurrence/acquisition chain [NB-192](../../nyman_beurling/findings/NB-192-prime-log-dimension-forces-double-exponential-bohr-return-scale.md) through [NB-200](../../nyman_beurling/findings/NB-200-atomic-phase-cell-packing-forces-a-2pi-exp-delta-endpoint-threshold.md), and the Prime-Lattice recurrence/completion chain [PL-342](../../prime_lattice/findings/PL-342-sharp-prime-block-essential-spectrum.md) through [PL-344](../../prime_lattice/findings/PL-344-bounded-modulation-pnt-edge-cancelled-by-pole.md). The two lines have different observables and conclusions; no recurrence bound is transferred between them.

Both lines use prime-log phase dynamics, but their findings separate several logically distinct questions.

**Existence** asks whether favorable returns occur at all. At fixed finite frequency set, Kronecker recurrence answers yes. In Prime Lattice that qualitative fact is already enough for PL-342: weakly-null recurrent states reproduce the sharp bounded prime edge and place it in essential spectrum. No density or first-hit estimate is needed for that topological conclusion.

**Prevalence** asks how much phase or time volume the favorable set occupies. PL-343 shows that the exact raw edge event for `H_a` has Haar and long-time density at most `exp[-Theta(e^(2a)/a)]`, even though PL-342 guarantees recurrent witnesses. Nyman--Beurling similarly finds exponentially small target volume and vanishing block density before its stronger pointwise source theorems. A favorable set can therefore be topologically unavoidable and statistically negligible at the same time.

**First-hit / return-free scale** asks how early the deterministic physical orbit can reach the favorable set as the source dimension grows. Prevalence does not answer this. PL-344 gives a concrete counterexample to the naive inference that exponential rarity forces a late first hit: the raw endpoint observable has a deterministic bounded-modulation PNT profile, and edge-sized values occur at `tau=O(1)` after phase alignment even though their long-time density is exponentially small.

Nyman--Beurling supplies the contrasting case where source-specific pointwise exclusion is genuine rather than inferred from prevalence. NB-198 uses positive source occupancy to exclude arbitrarily accurate returns throughout every fixed subunit Mellin power. NB-199 follows the shrinking phase-window scale and shows that `o(a)` positive returns cannot occur below a constant multiple of `x_a/log x_a`.

NB-200 then shows that the endpoint layer has its own **atomic first-hit capacity**. Once favorable phase cells become shorter than one integer, each cell carries at most one source atom. Counting available cells against the fixed positive mass in a top logarithmic slab proves that, for every `K<2 pi e^Delta`,

`inf_(X_a^2 <= |t| <= K x_a/X_a) A_a(t) >= c_K/X_a`.

Therefore a sequence of `o(a)` positive returns with bounded endpoint ratio must satisfy

`liminf |t|X_a/x_a >= 2 pi e^Delta`.

This is not an existence theorem above the threshold; it is a one-sided capacity obstruction. It demonstrates that first-hit analysis itself can change currency as the moving target crosses a source granularity scale: interval occupancy controls wider cells, then atom count times maximal atom mass controls sub-unit cells.

**Canonical centering** asks whether an early return survives in the destination observable at all. In PL-344 it does not: the zeta-pole quadratic form carries exactly the same leading bounded-frequency PNT response with the opposite sign. The raw early recurrence is therefore a universal background component removed by completion. The first-hit theorem relevant to coercivity must be posed for the **centered atomic-minus-PNT/pole residual**, not for the raw prime block.

The reusable rule is therefore two-dimensional: **match the recurrence theorem both to the destination's time quantifier and to the destination-surviving observable after canonical background terms are removed**. Essential-spectrum arguments may need only existence. Average statements may use prevalence. A destination that prices modulation needs a first-hit or return-free theorem in the correct source currency, including changes from continuum density to atomic capacity when the target shrinks. And none of those statements is relevant if the favorable component is canonically cancelled before the destination is evaluated.

**Boundary.** Nyman positivity/occupancy/atomic-capacity arguments do not transfer to the signed Prime-Lattice centered residual, and PL-344 supplies no theorem about that residual's recurrence. NB-200 does not construct returns above `2 pi e^Delta`. The synthesis identifies the correct quantifiers, source granularity and centering gates; it does not prove a cross-line recurrence theorem.