# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Price height adaptation by source-resolvable motion, repertoire and approximate linear complexity

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale` through `MI-044-coordinatewise-phase-reuse-can-escape-a-jointly-hilbert-compactness-ceiling`.

NB-165--NB-167 isolate the capped Poisson transport metric actually seen by a compact signed sampler near `Re s=1`. NB-168 shows one fixed stationary template cannot produce logarithmic Euler rescue on positive density under the subcritical transport budget. NB-169--NB-171 then price ordered height adaptation by refresh count, total variation and finite `p`-variation measured at that same source resolution.

NB-172 removes temporal regularity entirely: the rescue density is controlled by the internal covering number of the template range in capped Poisson transport. NB-173 gives a different compression when the range lies **exactly** in a stationary linear span: if `m_T` normalized source directions generate every template with coefficient `ell^2` energy at most `Y_T^2`, then rescue density is bounded by `m_T Y_T^2/log^2 T` times the inherited ultra-thin factor.

NB-174 unifies those unordered compressions at the resolution the arithmetic source actually sees. Define `mathfrak L_T(epsilon)` by allowing every adaptive template to be represented by a normalized stationary dictionary plus a residual of capped-Poisson size at most `epsilon q_T`. The residual is pointwise invisible up to `C_B epsilon H_T`, while the stationary core is controlled by the NB-168 mean-square theorem. Consequently positive-density logarithmic rescue forces large **approximate** linear source complexity whenever `epsilon` stays below a fixed fraction of `log T/H_T`.

The new currency has the correct endpoints and comparison bounds:

`mathfrak L_T(0)=mathfrak L_T`,

and, at the same normalized tolerance,

`(X_T-epsilon)_+^2 <= mathfrak L_T(epsilon) <= N_T(epsilon) X_T^2`.

Thus exact rank can be enormous while the source-resolvable approximate rank is small, and small range entropy automatically bounds approximate linear complexity at the same scale. Conversely, a continuum may have huge covering entropy while remaining near a well-conditioned low-dimensional source span.

NB-175 supplies an invariant lower certificate for this currency. Choose finitely many realized templates and probe them by linear observables that share one capped-transport `ell^2` dual budget. If `A` is the resulting response matrix, then

`mathfrak L_T(epsilon) >= (||A||_* - epsilon sqrt(N min(N,K)))_+^2/N`.

NB-176 removes the arbitrary probe-design freedom in one natural direction. The actual Euler expansion of `zeta'/zeta` defines a Hilbert-valued feature map at frequencies `log n`, weighted by `Lambda(n)n^(-1-a)`, that is uniformly contractive for the same capped-Poisson metric. The corresponding Euler response Gram gives

`mathfrak L_T(epsilon) >= (tr sqrt(G^Eul)-epsilon N)_+^2/N`.

NB-177 stress-tests that canonical witness and finds an intrinsic compactness ceiling. After the capped-transport Fourier estimate is inserted, the squared Euler amplitudes have a uniformly summable tail even as `a->0`. Finite spectral truncations therefore approximate every bounded-transport Euler fingerprint uniformly, and for `N` realized templates

`tr sqrt(G^Eul) <= C X_T N^(3/4) sqrt(log(2N))`.

Hence the average singular value decays, and at the high-ordinate source resolution `epsilon_T~log log T`, if `X_T=o(sqrt(log T))` this canonical certificate is `o((log T)^2)`. This is a limit of the **jointly Hilbert witness**, not a proof that `mathfrak L_T(epsilon_T)` itself is small.

NB-178 separates that compactness ceiling from the full dual geometry. If `K` scalar probes are each individually capped-transport contractive, but need not share one joint `ell^2` budget, then

`mathfrak L_T(epsilon) >= (||A||_* - epsilon sqrt(N K min(N,K)))_+^2/(N K)`.

The larger coordinatewise witness class pays an explicit factor `K`, so duplicating probes gives no artificial gain. But when `N=K`, a dense Hadamard-scale phase code with singular values `~sqrt N` has `||A||_*~N^(3/2)` and repays that tariff completely, forcing linear source-complexity growth above tolerance. Mere separation such as `A=I_N` gives only an order-one certificate.

The post-NB-177 target is therefore exact: construct **source-natural scalar capped-Poisson probes whose coherent prime-phase response matrix has many `sqrt N` singular values**, or prove that every such arithmetic coordinatewise construction has sub-Hadamard nuclear growth. This distinguishes a witness-choice compactness ceiling from a deeper phase-complexity obstruction.

## Keep target conditioning and arithmetic-source persistence separate

NB-168--NB-178 are source-side persistence/resource theorems. They control, lower-bound or expose limits of certificates for the complexity with which compact arithmetic samplers can create logarithmic Euler rescue after the sampler family has been viewed at the source's own resolution. NB-177 shows that using the actual Euler frequencies does not make one square-summed witness complete; NB-178 shows that a coordinatewise phase-reuse architecture can in principle escape that ceiling while paying its enlarged dual budget explicitly.

None of these results turns a density obstruction into pointwise exclusion at a selected sparse sequence, removes the `a_T\lesssim T^(-1/2)` ultra-thin regime, constructs the required arithmetic Hadamard-scale response, or by itself connects surviving source response back to global Nyman approximation.