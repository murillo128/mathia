# MI-073 — Continuous source cutoffs make hereditary fixed-shadow sign symmetry norm dense

**Evidence level:** exact RH-independent C-star synthesis from [WP-401](../../findings/WP-401-hereditary-cstar-source-fibres-have-norm-dense-sign-symmetric-tangents.md), strengthening the fixed-shadow localization obstructions of MI-071 and MI-072.

Let `A` be a C-star algebra, `E:A->B` a conditional expectation, `d in B_+`, and

`H_d=Her_A(d)=closure(dAd)`,

`V_d={k in (H_d)_sa : E(k)=0}`.

The absence of discontinuous spectral projections from the source C-star algebra does not protect a linear positivity orientation. Continuous functional calculus already supplies source-internal cutoffs

`c_n=f_n(d)`, with `f_n(t)=min(1,nt)`,

and for every `k in V_d`,

`k_n=c_n k c_n -> k` in norm,

`E(k_n)=0`,

`-n||k|| d <= k_n <= n||k|| d`.

Thus for sufficiently small `epsilon>0`, both `d+epsilon k_n` and `d-epsilon k_n` remain positive with the same conditional-expectation shadow. Two-sided admissible tangents are therefore norm dense in the entire centered hereditary source space.

The topological upgrade matters. WP-399/400 used spectral cutoffs in a von Neumann completion and obtained strong/ultraweak density, enough to kill normal linear orientations. WP-401 keeps every cutoff inside `C*(d)` and obtains norm density, so **every bounded real linear functional** whose sign is supposed to follow from positivity on the fixed-shadow fibre must vanish on `V_d`. The same conclusion holds on any linear source subspace stable under the continuous compressions `k -> c_n k c_n`.

A surviving bounded linear source relation must therefore be genuinely nonlocal across the spectral scales of `d`: continuous source localization must destroy a specific part of the relation, and that destroyed cross-scale quantity must carry the destination-relevant orientation. Merely saying that the original C-star algebra lacks the von Neumann spectral projections used in WP-400 does not provide such a mechanism.

**Boundary.** The theorem is conditional on the hereditary/source-local setting and cutoff stability of any restricted linear subspace. It does not rule out nonlinear or global readouts, singular or unbounded functionals, non-cutoff-stable domains, one-sided correspondences, nonunital boundary categories, or finite--archimedean couplings. It supplies no Weil sign; it identifies the precise locality property that a bounded linear source relation must violate to have any chance of orienting one.