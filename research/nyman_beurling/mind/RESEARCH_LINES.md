# Nyman--Beurling research lines

This file holds the current mathematical questions suggested by the durable Nyman--Beurling intuitions. It is not a roadmap, task queue, status page, or history.

## Price height adaptation by source-resolvable motion, repertoire and approximate linear complexity

**Linked intuitions:** `MI-001-target-aware-gram-geometry-must-carry-absolute-scale` through `MI-042-euler-fourier-fingerprints-give-a-source-native-complexity-certificate`.

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

The certificate is representation-invariant but NB-175 leaves the probe family abstract.

NB-176 removes that remaining probe-design freedom in one natural direction. The actual Euler expansion of `zeta'/zeta` defines a Hilbert-valued feature map with coordinates weighted by `Lambda(n)n^(-1-a)` at frequencies `log n`; after an order-one normalization `Z_a`, the full infinite map is `1`-Lipschitz for the same capped Poisson metric uniformly for `0<a<=1`. For realized templates the corresponding Euler response Gram

`G^Eul_(ij) = (q^2 Z_a^2)^(-1) sum_(n>=2) Lambda(n)^2 n^(-2-2a) Re(hat nu_i(log n) overline(hat nu_j(log n)))`

therefore gives the explicit source-native lower certificate

`mathfrak L_T(epsilon) >= (tr sqrt(G^Eul)-epsilon N)_+^2/N`.

If `G^Eul >= alpha^2 I_N`, this becomes `mathfrak L_T(epsilon) >= N(alpha-epsilon)_+^2`. The witness uses the actual Euler frequencies and amplitudes rather than an optimized arbitrary Lipschitz family.

The surviving adaptive escape is therefore sharper than “large range”, “high exact rank”, or “perhaps some dual witness exists.” A positive-density rescue must remain complicated after quotienting sub-Poisson-resolution motion, and NB-176 now gives a canonical sufficient test for that complexity. The next structural question is whether source-natural adaptive Nyman templates can realize arbitrarily many Euler fingerprints whose singular values stay above `epsilon_T=Theta(log T/H_T)`. Even a positive answer would still leave a separate arithmetic gate: the Hilbert geometry of many Euler modes need not make their scalar phases `n^(-it)` align coherently enough to produce logarithmic rescue.

## Keep target conditioning and arithmetic-source persistence separate

NB-168--NB-176 are source-side persistence/resource theorems. They control or certify the complexity with which compact arithmetic samplers can create logarithmic Euler rescue after the sampler family has been viewed at the source's own resolution. NB-176 is source-native because its coordinates are exactly the Euler modes of `zeta'/zeta`, but its Gram certificate measures their `ell^2` geometry rather than the coherent scalar sum itself. None of these results turns a density obstruction into pointwise exclusion at a selected sparse sequence, removes the `a_T\lesssim T^(-1/2)` ultra-thin regime, or by itself connects surviving source response back to global Nyman approximation.