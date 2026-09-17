# MI-041 — Dual nuclear response certifies source-resolved linear complexity

**Evidence level:** exact source-side synthesis from [NB-167](../../findings/NB-167-capped-poisson-transport-is-the-source-resolution.md), [NB-174](../../findings/NB-174-poisson-resolution-approximate-source-complexity-suppresses-adaptive-rescue.md), and [NB-175](../../findings/NB-175-dual-nuclear-response-certifies-approximate-source-complexity.md).

NB-174 isolates `mathfrak L_T(epsilon)` as the stationary linear repertoire that remains after all template motion below the capped-Poisson source resolution has been quotiented out. That makes the currency invariant to sub-resolution adaptive decoration, but by itself it is defined through an infimum over dictionaries and is difficult to lower-bound from a concrete nonlinear sampler family.

NB-175 supplies a dual certificate that depends only on realized source geometry. Choose realized templates `nu_1,...,nu_N` and linear probes `ell_1,...,ell_K` sharing one `ell_2` dual budget for the normalized capped-Poisson norm. If `A_ik=ell_k(nu_i)` and `r=min(N,K)`, then

`mathfrak L_T(epsilon) >= (||A||_* - epsilon sqrt(Nr))_+^2/N`.

The shared contraction is the essential invariant. It prevents artificial inflation by duplicating one observable, while vector-valued `1`-Lipschitz maps for the same truncated Poisson metric generate admissible probe families directly. The witness therefore measures simultaneous source-resolvable directions rather than syntactic coordinates of the sampler.

A particularly useful regime is near-orthogonal response. If `A=alpha I_N+R` with `||R||_*<=N delta`, then `mathfrak L_T(epsilon)>=N(alpha-delta-epsilon)_+^2`. Many templates carrying distinct source-visible responses consequently force linear approximate complexity even when they are produced by a concise nonlinear rule or have tiny parameter count.

The reusable lesson is that **approximate source complexity can be certified from the dual geometry of the same observation norm that defines source resolution**. One need not choose a stationary dictionary first and then argue that its rank is large; it is enough to exhibit many realized states and one jointly budgeted family of source-native observables with a large singular-value/nuclear response.

The certificate is deliberately one-sided. Failure to find a large nuclear witness does not prove that `mathfrak L_T(epsilon)` is small, and large approximate source complexity remains only a necessary resource for arithmetic rescue, not evidence that the available stationary directions couple effectively to the target. The next task is therefore constructive: build or rule out such capped-Lipschitz witnesses for natural adaptive Nyman--Beurling families at `epsilon_T=Theta(log T/H_T)`.

**Boundary.** Nuclear/Frobenius factorization and Lipschitz duality are generic analytic tools. The arithmetic content is the use of the NB-167 capped-Poisson norm and the NB-174 tolerance at exactly the source resolution consumed by `zeta'/zeta`. No converse duality or RH consequence is claimed.