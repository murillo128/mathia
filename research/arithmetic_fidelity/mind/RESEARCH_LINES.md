# Arithmetic-fidelity research lines

This file records the current mathematical questions that survive the Arithmetic-Fidelity evidence. It is not a roadmap, task queue, status page, or history.

## Separate finite-sample recoverability from rational-prime provenance

AF-483--AF-484 show that nonintegral Beurling-prime controls can preserve prime density, free numerical factorization, the square mass, the sharp Gibbs boundary law, and any prescribed finite family of exact prime-zeta samples. AF-485--AF-487 identify a genuinely different exact-fidelity regime: samples escaping to the right determine a discrete Dirichlet source, and a positive depth-`J` source observed at its critical scale has sharp local generator resolution `Theta(1/t)`. AF-488--AF-490 then price the observation channel itself. Under coherent pointwise critical noise, accumulated history inside a horizon does not beat the `Theta(1/H)` barrier; a fixed global finite-`p` noise budget can make sample accumulation useful; and nuisance directions must be quotiented before raw depth or cardinality is credited as sensitivity.

AF-509--AF-510 close the exact whole-profile question for simple unit-weight positive sources. Equality of the log-Dirichlet curvature `kappa_Q=(log P_Q)''` classifies sources exactly up to common dilation, and the quotient inverse is canonical: double tail integration recovers `log(q_1^s P_Q(s))`, exponentiation recovers the normalized positive Laplace sum, and successive tail peeling recovers every ratio `q_n/q_1`. The first nontrivial ratio is already the exponential decay rate of `kappa_Q`. Thus exact quotient fidelity is no longer the issue for this carrier; deeper atoms instead expose an inverse-conditioning problem because they live in exponentially smaller residuals.

AF-511 shows that this conditioning issue persists even when the observation is the entire right half-line and the dilation gauge has already been fixed arithmetically. Replacing one remote prime `p_n` by the composite `p_n+1` preserves primitive integer support, the least generators and the AF-509 scale anchor, while for every fixed `sigma>1` the relative curvature-profile distance `sup_(s>=sigma)|log kappa_R(s)-log kappa_P(s)|` tends to zero as `p_n` tends to infinity. AF-512 removes the apparent convergence-boundary escape. The same neighboring replacement satisfies

`sup_(s>1) |log kappa_R(s)-log kappa_P(s)| -> 0`.

Near `s=1+t`, prime-zeta curvature grows like `1/(t^2 log(1/t))`, whereas the neighboring remote replacement changes the underlying Dirichlet sum and its first two derivatives only at `O(p_n^(-2)(1+log^2 p_n))` on a fixed boundary neighborhood. The singular boundary therefore dilutes the relative perturbation instead of amplifying it.

AF-513--AF-514 show that this is not a one-atom pathology. If every prime above a cutoff `A` is shifted by one, the entire moved tail is composite and the full-domain relative-curvature error is `O((1+log^2 A)/A)`. More generally, for distinct outward transports `q_p=p+h_p` with `0<=h_p<=p`, the sufficient weighted transport budget

`B_A=sum_(p>A) h_p(1+log^2 p)/p^2`

controls the full profile: `sup_(s>1)|kappa_R(s)-kappa_P(s)|/kappa_P(s) <= C B_A` whenever `B_A->0`. In particular, displacements `h_p asymp p^alpha` with any fixed `0<alpha<1` can send every remote prime to an even composite at unbounded distance while the complete relative-curvature and log-curvature profiles still converge uniformly to the prime profiles. Exact equality still identifies the source, but rational-prime provenance has zero positive isolation margin along a quantitatively large cofinite transport class.

The quantitative frontier is consequently to state both the target source property and the observation topology before asking for stability. For exact normalized-source recovery, quantify growing-depth conditioning under finite windows, discrete sampling and explicit noise/correlation laws. For robust rational-prime provenance, merely extending the same relative-curvature observation toward `s=1` or requiring adversarial atoms to move an unbounded sublinear distance is now closed. A successful repair must use a topology that prices remote generator transport more strongly than the `B_A` budget, retain independent arithmetic incidence such as parity/factorization/additive or congruence structure, or weaken the target to a coarser RH-relevant invariant with a provable positive margin. Source-pullback or atom-indexed observations and other source-aware norms remain open. Candidate snapping after localization and externally imposed scale restrictions remain side information, not provenance supplied by the curvature map.

## Classify quotient-visible contact through admission, boundary membership and no-contact accessibility rates

AF-495 exposes a fidelity issue invisible in the scalar inverse-modulus story: a task-truncated critical bit can depend on whether bounded translated residuals recur at equality before an outer asymptotic limit is taken. AF-496--AF-504 then separate distance attainment, quotient-visible compactness, source saturation and nuisance-fibre lifting. In a Hilbert quotient, the infinite-dimensional nuisance contribution collapses exactly at the critical truncation `R=lambda` but reappears immediately above it; compactness therefore has to be tested in the quotient and at the correct radius rather than inferred from raw representatives.

AF-505 isolates a logically earlier gate. For `f(t)=dist_Q(tu,F)` with nonempty closed convex `F` and finite `lambda=liminf_(t->infinity)f(t)`, convexity forces monotone approach to `lambda`, and exact critical contact occurs if and only if the profile eventually plateaus. Proximinality at already-existing times and critical-tail compactness do not manufacture that temporal witness.

AF-506 identifies the static quotient datum behind this plateau test. Quotienting by `L=span(u)` gives `lambda=dist_(Q/L)(0,q(F))`; under the relevant proximinality hypotheses, finite-time contact is equivalent to the minimum-norm point of `closure(q(F))` belonging to the possibly nonclosed image `q(F)`. Replacing the quotient image by its closure therefore preserves the asymptotic scalar threshold while potentially deleting exactly the boundary-membership bit that decides equality.

AF-507 refines this further in finite-dimensional Hilbert geometry. A one-sided ray-invariant closed convex set is the epigraph of an extended-real convex admission height `a_F` on `u^perp`, with `q(F)=dom(a_F)`. If `z_*` is the nearest point to `closure(dom a_F)`, then the critical equality set is `[tau_F,infinity)` with `tau_F=max(0,a_F(z_*))` when that value is finite, and is empty otherwise. Thus closed quotient geometry determines the limiting threshold, membership of `z_*` in the quotient image determines whether a plateau exists, and the admission height at `z_*` determines exactly when it begins.

AF-508 closes the corresponding quantitative geometry in the no-contact branch. With sublevel sets `C_r={z:a_F(z)<=r}` and

`rho(r)=dist(0,C_r)^2-lambda^2`,

the squared distance excess is exactly the one-sided quadratic envelope

`f(t)^2-lambda^2 = inf_r [rho(r)+(r-t)_+^2]`.

The inverse admission-divergence profile `A(eta)` and `rho` are generalized inverses, so they carry the same accessibility information in different coordinates. If `rho` varies negligibly on its intrinsic window of width `sqrt(rho(t))`, then the distance excess is asymptotic to `rho(t)`. In particular, `A(eta)~c eta^(-beta)` gives `rho(t)~c^(1/beta)t^(-1/beta)`; for positive `lambda` this yields `f(t)-lambda~c^(1/beta)/(2lambda)t^(-1/beta)`, while for `lambda=0` the distance itself has exponent `1/(2beta)`.

The live question is therefore no longer which abstract divergence profiles can produce approach rates: the exact carrier is known. The unresolved step is arithmetic realization. Identify a natural arithmetic nuisance quotient and legitimate admission rule; determine whether its critical transverse point is admitted; and, in the no-contact case, prove a source-derived law or regularity statement for `rho` (equivalently `A`) strong enough to survive the final quadratic envelope. Only after actual contact exists do pointwise source attainment and compactness of the retained contact fibre become relevant. Any claimed discriminator must still state the nuisance quotient, admission rule, representative/lift class, truncation radius, compactness test, and whether it uses actual contacts, a post-limit fibre, or only an accessibility-rate profile.