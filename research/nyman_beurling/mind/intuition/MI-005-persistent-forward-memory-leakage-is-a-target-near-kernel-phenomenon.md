# MI-005 — Stable tails are inner-factor continuation defects in stationary branch filters, not consequences of local flags or global conditioning

**Evidence level:** supported by NB-063--NB-072; the exact inner-factor classification is proved only for stationary scalar branch filters, and no stable-tail triviality theorem for the actual nonstationary Nyman source is proved.

NB-066--NB-067 show that a hypothetical persistent Nyman target is a global continuation problem visible through finite normalized Schur complements. NB-068--NB-071 then progressively rule out local memory, finite causal flags, exact branching, far-mass necessity, and ordinary global Gram conditioning as sufficient invariants: an exact-branching matched control can remain uniformly Riesz-conditioned while carrying an infinite-dimensional stable tail with exponentially diverging continuation cost.

NB-072 identifies the analytic mechanism behind that control. If `D_j=psi(V_m)e_j` for the pure branching isometry and `psi=theta g` is the inner--outer factorization, then

`closure Ran psi(V_m) = theta(V_m) S`

and the stable tail is `K_theta tensor ker(V_m*)`. Hence the tail is zero exactly when `psi` is outer. All finite-window trace spaces and the exact branching law are unchanged by the inner factor because the synthesis matrix remains triangular with the same nonzero diagonal.

The NB-071 family `psi(z)=1-rho z` makes the distinction concrete. For `rho>1` it has one Blaschke factor and therefore a model-space defect; its outer factor is boundedly invertible and keeps the Gram operator well conditioned. At `rho=1` the source is outer but not invertible, conditioning degenerates while the stable tail is still zero. Thus **conditioning and continuation defect can move in opposite directions because they belong to different factors**.

The reusable target is now a factorization/cyclicity statement, not a generic norm bound. To exclude the stationary matched-control mechanism for the actual arithmetic source, one must prove that its relevant branch coordinate is outer/cyclic or derive an equivalent no-inner-factor property from the exact nonstationary Gram/Mellin structure.

**Boundary.** The actual Nyman innovation system is not shown to equal `psi(V_m)` for one stationary scalar symbol. Burnol's outer half-plane multiplier lives in a different analytic variable and cannot be imported as coefficient-side Wold outerness without a source-specific dictionary. NB-072 classifies a broad obstruction mechanism; it does not settle the canonical stable tail.