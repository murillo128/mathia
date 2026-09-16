# MI-044 — Finite sampling fidelity is controlled by target margin, covering radius, regularity, and determinant sensitivity

**Evidence level:** exact/literature-backed synthesis from [AF-379](../../findings/AF-379-vanishing-row-mesh-determines-continuous-translation-total-positivity.md) and [AF-380](../../findings/AF-380-prime-gap-bounds-give-finite-prime-log-negativity-witnesses.md). The prime-log covering rate uses the Baker--Harman--Pintz short-interval prime theorem already audited in AF-380. No uniform finite RH test is claimed.

AF-379 separates exact determining power from arithmetic provenance. For continuous translation kernels, density of normalized finite row patterns modulo common translation makes sampled total nonnegativity determine every real-row minor. Vanishing tail mesh is sufficient, so the intrinsic prime-log set `E={log p}` is already determining: if every prime-log row minor is nonnegative, continuity propagates the certificate to all row patterns. At that exact Boolean level, prime labels no longer supply an additional discriminator.

AF-380 identifies the quantitative currency hidden by that closure argument. Suppose a fixed target `k x k` minor has determinant `-eta<0`. If a sampled row pattern is within radius `r` after the common translation, and the kernel has local modulus of continuity `omega`, then the transported determinant obeys

`|det B-det A| <= k k! M^(k-1) omega(r)`.

The sign is therefore preserved once this perturbation is smaller than the target margin `eta`. A determining sample set can consequently be exact while the finite height at which a particular violation becomes visible depends on four separate resources: the target's distance from the zero-determinant boundary, the row-pattern covering radius, the kernel regularity on the relevant neighborhood, and the determinant sensitivity that converts entrywise error into sign error.

For prime-log rows, Baker--Harman--Pintz gives the unconditional one-sided covering modulus `r_T <= exp(-19T/40)` on every fixed finite pattern after a sufficiently large common translation. Hence every fixed strict negative minor has a finite prime-log witness. If the kernel is locally Hölder with exponent `alpha`, a sufficient witness scale is polynomial in the inverse margin,

`q_max = O(eta^(-40/(19 alpha)))`,

up to constants depending on the fixed target geometry, local regularity data, and the short-interval threshold. In the Lipschitz case the exponent is `40/19`.

The reusable distinction is **exact determining fidelity versus finite witness conditioning**. Pattern closure answers whether all sampled inequalities imply the target theorem. It does not say how far one must sample to see a strict target violation. A finite or stable claim must therefore expose the target margin and the continuity/conditioning map through which sampling error reaches the decision boundary; sampling density by itself is not a quantitative certificate.

This also sharpens the source/destination split. Prime-gap theory removes the geometry of prime-log row coverage as an obstruction for any fixed Hölder-regular strict violation, but it does not create prime-specific positivity. The live arithmetic problem remains upstream: derive or control the sampled sign inequalities intrinsically from prime data, or retain a richer observable in which provenance survives the passage to the RH-equivalent destination.

**Boundary.** The witness bound is target-relative. AF-380 supplies no uniform lower bound on the first negative determinant margin, no uniform bound on determinant order or target location, and no algorithmic cutoff for an unknown RH counterexample. For merely continuous kernels each fixed violation still has a finite witness through its actual modulus `omega`, but no power-law rate follows without quantitative regularity. The result concerns arbitrary real columns as in AF-379; sampling the column variable as well is a separate fidelity problem.