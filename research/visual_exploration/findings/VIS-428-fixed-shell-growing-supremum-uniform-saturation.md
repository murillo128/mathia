# VIS-428 — fixed-shell growing-window suprema uniformly saturate under the prime-log flow

## Claim

Continue the fixed-shell prime-torus representation of `VIS-419`. Let

`Phi_N : T^(P_N) -> C`

be a nonzero finite Laurent polynomial for one fixed Wang shell, let

`S_N = max_z |Phi_N(z)| > 0`,

and write

`A_N(z)=|Phi_N(z)|/S_N in [0,1]`.

Let the vertical prime-log flow be

`tau_N(u)=(p^(-iu))_(p in P_N)`

and define the path supremum

`Q_(N,rho)(z)=sup_(|u|<=rho) A_N(z tau_N(u))`.

For every fixed threshold `t in (0,1)`, define the open superlevel target

`E_(N,t)={z : A_N(z)>t}`

and the two-sided hitting time

`H_(N,t)(z)=inf{|u| : z tau_N(u) in E_(N,t)}`.

Then:

1. `E_(N,t)` is nonempty and open;
2. `H_(N,t)(z)<infinity` for every torus phase `z`;
3. the shell-specific cover radius

`R_N(t)=sup_z H_(N,t)(z)`

is finite; and
4. for every `rho>=0`,

`Q_(N,rho)(z)<=t  iff  H_(N,t)(z)>rho`.

Consequently, for every fixed shell,

`Q_(N,rho)(z) -> 1`

**uniformly in the starting phase `z` as `rho->infinity`**. Equivalently, for every `epsilon in (0,1)` there is a finite `R_N(1-epsilon)` such that

`Q_(N,rho)(z)>1-epsilon`

for every `z` whenever `rho>=R_N(1-epsilon)`.

For any changing-shell family and any fixed threshold `t<1`, if a chosen radius law satisfies

`rho_N >= R_N(t)`

eventually, then the low-supremum event `Q_(N,rho_N)<=t` is identically empty for **every** starting phase, including both Gram-selected phases and Haar-random phases. Thus a nontrivial growing-window supremum test can only live in the pre-saturation regime controlled by the changing-shell hitting/cover scale `R_N(t)` (or by a threshold `t=t_N` tending to one), not in unqualified growth of `rho_N` by itself.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL KRONECKER/MINIMAL-FLOW SPECIALIZATION + NEGATIVE/BOUNDARY + NO-NOVELTY-CLAIM`.

No quantitative bound on `R_N(t)`, no uniform theorem in the growing shell, no Gram anomaly, and no RH consequence is claimed.

## 1. The high-amplitude target is a nonempty open set

Because `Phi_N` is continuous on the compact torus, it attains its positive maximum `S_N`. If `z_*` is a maximizer, then

`A_N(z_*)=1>t`.

Hence `E_(N,t)` is nonempty. Continuity of `A_N` makes it open.

This step uses the **exact torus supremum normalization** already fixed in `VIS-419`--`VIS-425`; no visual threshold or numerical maximizer is being promoted to evidence.

## 2. Minimality gives a hit from every starting phase

`VIS-419` proves that the base-prime logarithms have no nontrivial integer relation: an identity

`sum_(p in P_N) m_p log p=0`

would exponentiate to `prod_p p^(m_p)=1`, and unique factorization forces every `m_p=0`.

Therefore the continuous Kronecker flow

`u -> z tau_N(u)`

is dense in the full finite prime torus for every starting phase `z`. Since `E_(N,t)` is nonempty and open, every orbit intersects it. Thus

`H_(N,t)(z)<infinity`

for every `z`.

This is exactly the fixed-shell minimality already underlying the Haar/translation equivalence of `VIS-419`; no stronger number-theoretic input has been introduced.

## 3. Compactness upgrades pointwise recurrence to a uniform cover radius

For each phase `z`, choose one time `u_z` such that

`z tau_N(u_z) in E_(N,t)`.

Because multiplication by `tau_N(u_z)` is continuous and `E_(N,t)` is open, the set

`U_z={y : y tau_N(u_z) in E_(N,t)}`

is an open neighborhood of `z`.

The collection `{U_z}` covers the compact torus. Choose a finite subcover

`U_(z_1),...,U_(z_J)`

and set

`R=max_(1<=j<=J) |u_(z_j)|`.

Every starting phase belongs to some `U_(z_j)` and therefore reaches `E_(N,t)` at a time of magnitude at most `R`. Hence

`R_N(t)=sup_z H_(N,t)(z) <= R < infinity`.

This is the continuous-time version of the standard syndetic-return consequence of minimal compact dynamics. The proof above is included so that the Wang specialization does not depend on an unstated recurrence theorem.

## 4. A growing-window supremum is exactly a hitting-time tail

By definition,

`Q_(N,rho)(z)>t`

if and only if there exists `|u|<=rho` with `A_N(z tau_N(u))>t`, which is equivalent to

`H_(N,t)(z)<=rho`.

Taking complements gives the exact identity

`Q_(N,rho)(z)<=t  iff  H_(N,t)(z)>rho`.

Thus the Haar self-null for a low growing-window supremum is not a new amplitude distribution. It is the hitting-time tail

`m_H{z : H_(N,t)(z)>rho}`

for the prime-log flow entering the shell's exact superlevel set.

Likewise, evaluating the same statistic at an arithmetic selector phase `z(T_*)` asks whether that source-selected phase has an unusually long avoidance time of `E_(N,t)` relative to this exact Haar hitting-time law.

The fixed-shell limit follows immediately. Since `R_N(t)<infinity`, the tail above is exactly zero for every `rho>=R_N(t)`. Taking `t=1-epsilon` for arbitrary `epsilon>0` gives uniform convergence `Q_(N,rho)->1`.

## 5. What remains in a growing family

The conclusion is deliberately fixed-shell. The compactness argument gives no useful control on how

`R_N(t)`

grows when the prime support, coefficient geometry, arithmetic shell height, or superlevel target changes with `N`.

That missing rate is precisely the remaining resource. A changing family can show nontrivial growing-window behavior only before universal saturation: for example when `rho_N` remains below the relevant cover scale, when only a small Haar fraction has hit the target by time `rho_N`, or when `t_N->1` makes the target itself shrink.

This separates two very different statements that were previously grouped under "growing-window supremum":

- `rho_N->infinity` alone is not a mechanism; each fixed shell eventually saturates for every phase;
- a genuinely nontrivial test requires quantitative **shrinking-target / cover-time competition** between the chosen radius and the changing shell.

For the phase-anchored clue, the useful scalar object is therefore the hitting profile `H_(N,t)` (or its Haar tail), not merely the fact that a window radius grows.

## 6. Prior art, representation audit, and falsification

The dynamical input is classical. `VIS-419` already records the Kronecker-Weyl/Bohr prime-torus correspondence and cites Hedenmalm--Lindqvist--Seip (1997) and Defant--Garcia--Maestre--Sevilla-Peris (2019) for that viewpoint. Minimal compact systems have syndetic return times to nonempty open sets; a standard monograph background is Joseph Auslander, **Minimal Flows and Their Extensions**, North-Holland Mathematics Studies 153, Elsevier (1988), especially the opening chapters on flows, minimal sets, and equicontinuous flows. No novelty is claimed for minimality, recurrence, syndeticity, or compactness.

The representation is intrinsic to the fixed Wang shell: changing prime-coordinate labels or translating the starting torus phase does not alter the target's cover property. The threshold target is defined from normalized shell amplitude itself, not from an arbitrary visual embedding. The result is therefore a representation-certified boundary statement rather than a visual pattern claim.

The nonzero-shell and fixed-threshold assumptions matter. At `t=1`, the exact maximizing set need not be hit by a given orbit even though it is approached densely. For `t_N->1`, the open target can shrink and its cover radius can diverge. For a changing shell there is no uniform rate without additional Diophantine/target-geometry information.

Falsify the argument by finding a participating base-prime relation that destroys minimality, a threshold `t<1` for which the superlevel set is empty or non-open, a starting phase whose orbit avoids that open set, or a fixed shell for which no finite collection of translated target preimages covers the compact torus.

## Dependencies

- `VIS-419`: finite Wang shells are Laurent polynomials on the base-prime torus and the vertical prime-log flow is Haar-equidistributed/dense.
- `VIS-425`: fixed-radius path suprema are the persistence observable currently used by the Wang selector clue.
- `VIS-427`: normalized fixed-power path averages remain controlled even for arbitrary growing radius, leaving localized/supremum behavior as a residual route.

## Research consequence

The surviving growing-window supremum branch in `CLUE-wang-phase-anchored-small-values` should be reformulated as a **quantitative hitting-time problem**. For each fixed shell it is eventually trivial: every phase reaches every fixed sub-maximal amplitude level within a finite shell-specific radius.

A source-sensitive effect can therefore survive only if the transported Wang family places the arithmetic selector atypically in the pre-saturation hitting-time tail, or if the shell-specific cover radius / shrinking-target scale grows fast enough that the prescribed `rho_N` does not reach universal saturation. The next substantive test is to quantify that competition for the actual changing Wang shells rather than treating `rho_N->infinity` itself as an escape mechanism.