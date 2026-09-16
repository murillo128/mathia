# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable Farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Quantify source information in anchor geometries that actually give coercivity

**Linked intuitions:** `MI-001-cumulative-farey-discrepancy-is-mertens-energy` through `MI-021-finite-lq-ancestry-coercivity-needs-quantitative-anchor-exposure`.

FD-145--FD-147 reduce finite-`L^q` binary ancestry recovery to anchored cut exposure. FD-148--FD-153 price rank-aligned anchors: sparse anchors pay parent distortion, central-rank anchors buy bounded parent load with macroscopic source information but retain a `sqrt(log log T)` child window, and bounded residual depth requires orienting almost all coefficients.

FD-154 shows that this rank-depth law is not universal. A fixed finite-prime avoidance face is divisor-closed, has positive asymptotic mass, and gives bounded ancestry depth and `T`-uniform endpoint distortion. FD-155 then prices thinning that face: reducing anchored exposure to `alpha` needs `s_alpha=exp(alpha^(-1+o(1)))` prime coordinates and the direct parent load becomes double exponential in `alpha^(-1+o(1))`.

FD-156--FD-160 successively remove one-parent, multi-parent, finite auxiliary vocabulary, divisor-downward support and static sparse-hole escapes. For an arbitrary sparse active-core family, taking divisor closure of the depth-`r` cores internalizes hole inflow and restores the exponential pressure `P+L/|D_r(C)|>=h(2^r-1)`.

FD-161 prices terminal-core migration for the initial-prime anchor by recovering a growing Boolean face inside every active principal divisor closure. FD-162 strengthens and generalizes the mechanism. For an arbitrary finite prime anchor `S`, let `ell_S` be its first omitted prime and `m(S)` the length of its initial-prime prefix. Every nontrivial active `S`-free core `c` has

`bar f_(S,D(c))(T) >= (Q_sf(ell_S-1)-1)/2`,

so the anchored cut law forces

`P_(S,T) + L_(S,D(c),T)/2^(omega(c)) >= (h_(S,T)/2)(Q_sf(ell_S-1)-1)`.

If `m(S)->infinity`, then `ell_S=p_(m+1)` and the guaranteed average fibre grows as `(1/(2 zeta(2))+o(1)) m log m`. Thus merely perturbing an initial-prime anchor at moving high primes does not reopen terminal migration: **every anchor family that eventually contains each fixed prime regenerates growing squarefree-volume pressure after principal closure**.

The surviving alternative-anchor escape is therefore sharper. With bounded architecture resources and persistent nontrivial auxiliary cores, `m(S)` must stay bounded along an infinite subsequence; after refinement, one fixed small prime is omitted throughout that subsequence. Otherwise anchored expansion, parent distortion, normalized outer leakage, or another hypothesis must deteriorate. A persistent low-prime hole is not ruled out by FD-162 and is now the concrete anchor-side structural alternative to test.

## Apply the information-budget gate only after cut exposure survives

FD-144 remains a later lower bound: even after anchoring and quantitative cut exposure are solved, `o(r_T)` arbitrary source-independent normalized ancestry tests can still be fooled along a subsequence. Neither a large cross-core recipient population, fresh-prime migration nor growing squarefree principal-closure volume is by itself an information lower bound; a deterministic rule may generate many recipients from little description. Any epistemic claim still needs a theorem connecting geometric leakage to independent source information and then to the Franel--Landau destination.

Audit future ancestry proposals in the order **anchor geometry and mass -> first omitted prime/initial coverage -> source justification -> parent distortion -> hole/cross-core/outer leakage -> divisor/principal-ideal closure -> closure fibre volume -> anchored expansion -> child distortion/recipient population -> information and precision budget -> destination relevance**.

## Keep coefficient coercivity and nonlocal destination coercivity separate

FD-147--FD-162 concern binary Möbius orientations, finite `L^q` and positive divisibility-ancestry observations. They show exactly how excellent coefficient-side coercivity can be purchased and why extra parents, finite auxiliary vocabularies, sparse holes, terminal-core presentation and high-prime perturbations of an exhausting anchor do not remove the hidden-fibre cut once intrinsic divisor closure is taken. None proves that Farey discrepancy supplies the orientation or that the resulting norm controls the RH-equivalent destination. Any surviving route must state which source hypothesis or geometry changes and why it does not simply reconstruct the source.