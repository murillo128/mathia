# MI-021 — Finite-`L^q` ancestry coercivity is anchored cut exposure, and principal closure prices anchor exhaustion

**Evidence level:** exact/proved synthesis from [FD-147](../../findings/FD-147-finite-seed-ancestry-coercivity-is-exactly-an-anchored-cut-problem.md) through [FD-162](../../findings/FD-162-first-omitted-anchor-prime-forces-squarefree-volume-closure-pressure.md).

For binary orientations anchored on `D`, finite-`L^q` recovery is controlled by anchored boundary exposure: `C^(bin)_(q,D)=h_D(nu,eta)^(-1/q)`. Connectivity only excludes zero boundary; stable recovery requires every admissible macroscopic flip to carry uniformly positive observed boundary mass.

FD-154 gives a qualitatively different anchor from rank cuts. For a finite prime set `S`, the prime-avoidance face is divisor-closed and every unanchored squarefree integer has an `S`-free core in the anchor at depth at most `|S|`. The cost appears when that face is thinned: FD-155--FD-157 show that low anchor exposure plus bounded load forces exponentially large cross-core leakage.

FD-158 proves that a finite completed auxiliary vocabulary does not terminate the process. FD-159 then replaces complete auxiliary cubes by arbitrary finite **divisor-downward** active core sets. If `f(c)` is the occupied primary `S`-fibre size and `bar f` its average, the exact cut pressure is

`P_(S,T) + L_(S,C,T)/|C| >= h_(S,T) bar f`.

FD-160 removes the downward-closure assumption. Arbitrary sparse holes contribute an explicit incoming bill, and taking the divisor closure of every depth-`r` subfamily internalizes that bill without losing primary depth. Static non-downward holes therefore do not weaken the exponential obstruction; they only move its boundary outward in the divisor poset.

FD-161 first closes terminal presentation for the initial-prime anchor: a nontrivial terminal `S_s`-free core can have bounded visible primary depth while its principal divisor ideal regenerates a growing Boolean face. FD-162 shows that the Boolean face was only a sparse lower bound and removes the exact initial-segment requirement.

Let `ell_S` be the smallest prime not in a finite anchor `S`, and let `m(S)` be the number of initial primes contained in `S`. For every nontrivial active `S`-free core `c`, choose any prime `r|c`. Since `r>=ell_S`, every squarefree primary product `q<ell_S` fits in the fibres above the half of `D(c)` omitting `r`. Therefore

`bar f_(S,D(c))(T) >= (Q_sf(ell_S-1)-1)/2`.

The exact cut law becomes

`P_(S,T) + L_(S,D(c),T)/2^(omega(c)) >= (h_(S,T)/2)(Q_sf(ell_S-1)-1)`.

If `m=m(S)->infinity`, then `ell_S=p_(m+1)~m log m` and squarefree density gives

`bar f >= (1/(2 zeta(2))+o(1)) m log m`.

So terminal migration is obstructed not only for literal initial-prime anchors but for **every anchor family that asymptotically exhausts the fixed primes**. Moving high-prime holes do not help: principal closure sees all squarefree primary products below the first omitted prime. With bounded expansion/distortion/leakage budgets, persistence of a nontrivial auxiliary core forces `m(S)` to remain bounded along a subsequence, hence one fixed small prime is omitted along a further subsequence.

The conceptual correction is stronger than “terminality is not stable under closure.” **Anchor exhaustion has a quantitative closure volume measured by the first omitted prime.** The closure does not need to contain a complete high-dimensional Boolean face to become expensive; FD-159 prices the cardinality of occupied primary states, and all low squarefree products already supply `Theta(m log m)` pressure.

The information-budget caveat remains separate. A large outer-recipient population or growing principal-closure fibre need not contain proportionally many independent source bits; a deterministic rule can generate many recipients from a short description. FD-144 still requires a later theorem connecting whatever geometric resource survives the cut analysis to independent source information and then to the Franel--Landau destination.

**Boundary.** FD-162 applies to finite prime-avoidance anchors and positive divisibility-edge coercivity. It deliberately becomes weak when a small prime hole persists: bounded `m(S)` gives only bounded universal squarefree-volume pressure. It does not rule out such low-prime-hole anchors, signed/nonpositive couplings, unbounded distortion, closure escaping the controlled truncation, or source constraints changing the admissible cuts. The closure-volume bound is geometric, not an information lower bound.