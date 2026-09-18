# MI-027 — Recurrence existence, prevalence, first hit and canonical centering are different currencies

**Evidence level:** supported cross-line synthesis from the Nyman--Beurling recurrence/acquisition chain [NB-192](../../nyman_beurling/findings/NB-192-prime-log-dimension-forces-double-exponential-bohr-return-scale.md) through [NB-199](../../nyman_beurling/findings/NB-199-diagonal-brun-titchmarsh-localizes-vanishing-positive-euler-returns-to-the-logarithmic-mellin-endpoint.md), and the Prime-Lattice recurrence/completion chain [PL-342](../../prime_lattice/findings/PL-342-sharp-prime-block-essential-spectrum.md) through [PL-344](../../prime_lattice/findings/PL-344-bounded-modulation-pnt-edge-cancelled-by-pole.md). The two lines have different observables and conclusions; no recurrence bound is transferred between them.

Both lines use prime-log phase dynamics, but their recent findings separate four logically distinct questions.

**Existence** asks whether favorable returns occur at all. At fixed finite frequency set, Kronecker recurrence answers yes. In Prime Lattice that qualitative fact is already enough for PL-342: weakly-null recurrent states reproduce the sharp bounded prime edge and place it in essential spectrum. No density or first-hit estimate is needed for that topological conclusion.

**Prevalence** asks how much phase or time volume the favorable set occupies. PL-343 shows that the exact raw edge event for `H_a` has Haar and long-time density at most `exp[-Theta(e^(2a)/a)]`, even though PL-342 guarantees recurrent witnesses. Nyman--Beurling similarly finds exponentially small target volume and vanishing block density before its stronger pointwise source theorems. A favorable set can therefore be topologically unavoidable and statistically negligible at the same time.

**First-hit time** asks how early the deterministic physical orbit reaches the favorable set as the source dimension grows. Prevalence does not answer this. PL-344 gives a concrete counterexample to the naive inference that exponential rarity forces a late first hit: the raw endpoint observable has a deterministic bounded-modulation PNT profile, and edge-sized values occur at `tau=O(1)` after phase alignment even though their long-time density is exponentially small.

**Canonical centering** asks whether that early return survives in the destination observable at all. In PL-344 it does not: the zeta-pole quadratic form carries exactly the same leading bounded-frequency PNT response with the opposite sign. The raw early recurrence is therefore a universal background component removed by completion. The first-hit theorem relevant to coercivity must be posed for the **centered atomic-minus-PNT/pole residual**, not for the raw prime block.

Nyman--Beurling supplies the contrasting case where source-specific pointwise exclusion is genuine rather than inferred from prevalence. NB-198 uses positive source occupancy to exclude arbitrarily accurate returns throughout every fixed subunit Mellin power. NB-199 retains the variable phase-window scale and proves that a return of tolerance `eta` forces

`|t| >= x_a^(1-C eta)/log x_a`,

so vanishing positive tolerances `eta_a=o(1/log x_a)` cannot occur below the final logarithmic Mellin layer. This is a direct acquisition theorem about the physical source orbit, not a conversion from small target measure to first-return time.

The reusable rule is therefore two-dimensional: **match the recurrence theorem both to the destination's time quantifier and to the destination-surviving observable after canonical background terms are removed**. Essential-spectrum arguments may need only existence. Average statements may use prevalence. A destination that prices modulation needs a first-hit or return-free theorem. And none of those statements is relevant if the favorable component is canonically cancelled before the destination is evaluated.

**Boundary.** Nyman positivity/occupancy does not transfer to the signed Prime-Lattice centered residual, and PL-344 supplies no theorem about that residual's recurrence. The synthesis identifies the correct quantifiers and centering gate; it does not prove a cross-line recurrence theorem.