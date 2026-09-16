# MI-021 — Finite-`L^q` ancestry coercivity is anchored cut exposure, and divisor closure prices terminal migration

**Evidence level:** exact/proved synthesis from [FD-147](../../findings/FD-147-finite-seed-ancestry-coercivity-is-exactly-an-anchored-cut-problem.md) through [FD-161](../../findings/FD-161-terminal-auxiliary-cores-force-growing-primorial-closure-pressure.md).

For binary orientations anchored on `D`, finite-`L^q` recovery is controlled by anchored boundary exposure: `C^(bin)_(q,D)=h_D(nu,eta)^(-1/q)`. Connectivity only excludes zero boundary; stable recovery requires every admissible macroscopic flip to carry uniformly positive observed boundary mass.

FD-154 gives a qualitatively different anchor from rank cuts. For a finite prime set `S`, the prime-avoidance face is divisor-closed and every unanchored squarefree integer has an `S`-free core in the anchor at depth at most `|S|`. The cost appears when that face is thinned: FD-155--FD-157 show that low anchor exposure plus bounded load forces exponentially large cross-core leakage.

FD-158 proves that a finite completed auxiliary vocabulary does not terminate the process. FD-159 then replaces complete auxiliary cubes by arbitrary finite **divisor-downward** active core sets. If `f(c)` is the occupied primary `S`-fibre size and `bar f` its average, the exact cut pressure is

`P_(S,T) + L_(S,C,T)/|C| >= h_(S,T) bar f`.

FD-160 removes the downward-closure assumption. Arbitrary sparse holes contribute an explicit incoming bill, and taking the divisor closure of every depth-`r` subfamily internalizes that bill without losing primary depth. Static non-downward holes therefore do not weaken the exponential obstruction; they only move its boundary outward in the divisor poset.

FD-161 closes the remaining apparent escape in which the active auxiliary cores themselves are terminal and carry only bounded primary depth. For the initial-prime anchor `S_s={p_1,...,p_s}`, every nontrivial `S_s`-free terminal core `c` with `2c<=T` has a principal divisor ideal containing a full primary Boolean face through depth

`b_s=max{j<=s: P_j<=p_(s+1)}`,

where `P_j=p_1...p_j`. Averaging over that closure gives at least `(2^(b_s)-1)/2` occupied primary states, hence the same anchored cut law forces a bill of order `2^(b_s)`. Since `b_s~log s/log log s`, this pressure still diverges:

`2^(b_s)=exp((log 2+o(1)) log s/log log s)`.

The important correction is conceptual. **Terminality of the presented core is not terminality under the closure intrinsic to divisibility.** A core can sit at bounded visible primary depth while its principal divisor ideal regenerates a growing initial-prime face. The surviving escape is no longer “move the complexity into terminal auxiliary support”; it must make the relevant closure leave the controlled regime, allow the distortion/expansion/leakage budgets to deteriorate, change the anchor/cut geometry, trivialize the root, or impose a source-native coefficient restriction that removes the tested flips.

The information-budget caveat remains separate. A large outer-recipient population or growing primorial closure need not contain proportionally many independent source bits; a deterministic rule can generate many recipients from a short description. FD-144 still requires a later theorem connecting whatever geometric resource survives the cut analysis to independent source information and then to the Franel--Landau destination.

**Boundary.** FD-161 is tied to the initial-prime avoidance architecture and positive divisibility-edge coercivity. The primorial depth is a closure-pressure lower bound, not an information lower bound, and it is weaker than the direct double-exponential thinning bill. It does not rule out different anchors, signed/nonpositive couplings, unbounded distortion, closure that escapes the controlled truncation, or source constraints that change the admissible cuts.