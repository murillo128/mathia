# MI-017 — The phase-coupled source cone first needs exact recertification of the intended first-prime operator

**Evidence level:** the phase-cone identities of WI-253--WI-259 are exact. WI-260--WI-261 prove that neither the current public FP-0.35 reproduction script nor its nominally stricter proofctl exact-prime checker certifies the required exact `lambda_(7/20)>0` operator as written. No negativity of the true operator and no incompatibility with a compactly supported global first zero mode is proved.

At a hypothetical first unrestricted localized Weil crossing, translation freedom produces an exact sliding-aperture profile. WI-253--WI-258 reduce the useful source information to phase-coupled inequalities `S_v(r)+J_v(r,t)>=0`, where `J_v` is a localized cosine transform of the von-Mangoldt/archimedean source-weighted autocorrelation. A source-forced negative localized defect would create strict firstness slack.

WI-259 identifies the activation prerequisite. The first Mangoldt atom enters only above `r=(log 2)/2`. If strict positivity at `r=7/20` is established, monotonicity forces every hypothetical first crossing past that radius and, because `log 2<7/10<log 3`, the fixed phase cone contains exactly the single atom `n=2`.

WI-260 audits the post-fix public FP-0.35 generator and shows that numerical replay is not an exact certificate: load-bearing constants and matrix entries are not rigorously enclosed and the inverse-residual check does not establish a valid induced matrix-norm bound.

WI-261 then audits the separate proofctl `exact_prime_split_v1` path. The checker does recompute an exact-prime metadata object, but that object is not fed into the matrix judged for positivity. The actual assembly rebuilds prime matrices at a rational midpoint `TAU_MID`; exact rational comparison of the simplest `S2[0,0]` entry proves that the emitted lower endpoint lies **above** the true exact value, so the advertised interval excludes the intended matrix entry. Independently, the positivity judge sets `c_L=0` although the thin FP-0.35 Schur gate uses the nonzero Weil constant near `1.36527`. The accepted proofctl obligations therefore concern a surrogate matrix, not the theorem object.

The next action is consequently stricter than “repair interval hygiene.” Build an independent certificate whose object identity is explicit from inputs to pivots: enclose exact `log 2`, `sqrt 2`, `tau=20 log 2/7`, harmonic values and every `Q[tau]` entry; preserve their dependencies through assembly; use the intended nonzero `c_L`; then prove positivity by interval `LDL^T`/Cholesky or a rigorous induced-norm inverse-residual bound. Only that exact lower margin may activate the one-prime phase program.

The reusable lesson is now three gates, not two: **source activation, exact-object certification, and source-sign obstruction are distinct**. A checker can be exact arithmetic internally and still prove the wrong operator if its dataflow substitutes a midpoint or altered parameter.

**Boundary.** WI-260--WI-261 do not show `lambda_(7/20)<=0`; the nominal positive margin may survive correct recertification. They do not alter WI-259's conditional implication or prove a negative phase defect. Until the intended matrix itself is certified, the single-prime cone remains conditional input.
