# MI-021 — Finite-`L^q` ancestry coercivity is anchored cut exposure, and sparse holes only move the boundary bill

**Evidence level:** exact/proved synthesis from [FD-147](../../findings/FD-147-finite-seed-ancestry-coercivity-is-exactly-an-anchored-cut-problem.md) through [FD-160](../../findings/FD-160-sparse-auxiliary-holes-only-move-cheeger-pressure-to-divisor-closure.md).

For binary orientations anchored on `D`, finite-`L^q` recovery is controlled by anchored boundary exposure: `C^(bin)_(q,D)=h_D(nu,eta)^(-1/q)`. Connectivity only excludes zero boundary; stable recovery requires every admissible macroscopic flip to carry uniformly positive observed boundary mass.

FD-154 gives a qualitatively different anchor from rank cuts. For a finite prime set `S`, the prime-avoidance face is divisor-closed and every unanchored squarefree integer has an `S`-free core in the anchor at depth at most `|S|`. The cost appears when that face is thinned: FD-155--FD-157 show that low anchor exposure plus bounded load forces exponentially large cross-core leakage.

FD-158 proves that a finite completed auxiliary vocabulary does not terminate the process. FD-159 then replaces complete auxiliary cubes by arbitrary finite **divisor-downward** active core sets. If `f(c)` is the occupied primary `S`-fibre size and `bar f` its average, the exact cut pressure is

`P_(S,T) + L_(S,C,T)/|C| >= h_(S,T) bar f`.

The remaining loophole after FD-159 was non-downward sparsity: deleted lower cores could supply additional incoming boundary. FD-160 identifies that bill exactly. For an arbitrary sparse family `C`, let `J_(S,C,T)` be incoming mass whose `S`-free parent core lies in the hole set `(downarrow C)\C`. Then

`P_(S,T) + (J_(S,C,T)+L_(S,C,T))/|C| >= h_(S,T) bar f`.

So holes are not free; they exchange occupied-fibre pressure for explicit incoming source flux.

More importantly, the hole bill can be eliminated from the accounting by changing the test cut, not the architecture. For the depth-`r` occupied cores `C_(>=r)`, take their divisor closure `D_r(C)`. Divisibility closure preserves primary depth, makes the former hole inflow internal, and gives

`P_(S,T) + L_(S,D_r(C),T)/|D_r(C)| >= h_(S,T)(2^r-1)`.

Under bounded child distortion the same excess forces exponentially many genuinely outer recipients. Even a single deep sparse core triggers the law after taking its principal divisor ideal. Therefore **static non-downward holes do not weaken the exponential prime-depth obstruction; they only move its boundary outward in the divisor poset**.

This changes the surviving architecture question. A genuinely different route must use support that is terminal or migrates with scale so that the relevant divisor closure itself leaves the controlled regime, allow the normalized parent/leakage or child-distortion budgets to grow, change the anchor/cut geometry, or impose a source identity that removes the corresponding coefficient flips from the admissible class. Merely using incomplete boxes, truncated down-sets, or sparse holes no longer changes the coercivity mechanism.

The information-budget caveat remains separate. A large outer-recipient population or migrating prime vocabulary need not contain proportionally many independent source bits; a deterministic rule can generate many recipients from a short description. FD-144 still requires a later theorem connecting whatever geometric resource survives the cut analysis to independent source information and then to the Franel--Landau destination.

**Boundary.** FD-160 remains inside the declared positive divisibility-edge architecture with global anchored expansion. It does not rule out different anchors, signed/nonpositive couplings, unbounded distortion, genuinely migrating/terminal support, or source constraints that change the admissible cuts. The result is coefficient-side and does not itself produce Möbius orientation or an RH-equivalent discrepancy bound.
