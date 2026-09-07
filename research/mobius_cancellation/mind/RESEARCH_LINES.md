# Möbius-cancellation research lines

This file holds the current mathematical lines of investigation suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Produce RH-scale mean-absolute Mertens control on a source-faithful set of scales

**Linked intuitions:** `MI-004-mean-absolute-cancellation-needs-excursion-coupled-information` and `MI-012-hamming-regularization-is-degree-two-damping-before-the-square-root-transition`.

MC-115 gives the clean downstream bridge: the bound

`X^{-1} integral_1^X |M(x)| dx = O_epsilon(X^(1/2+epsilon))`

is equivalent to RH by an elementary Mellin continuation argument for `1/zeta(s)`. The endpoint relevance no longer depends on the still-audited Pintz preprint. Pintz would strengthen the profile if verified, but it is not needed for the RH equivalence.

MC-116 also shows that the bound need not be proved at every real scale. Because the cumulative absolute mass is monotone, any deterministic checkpoint sequence with `log X_(j+1)/log X_j -> 1` interpolates without exponent loss. The live burden is therefore **cancellation strength**, not dense scale coverage: derive the square-root mean-absolute estimate on a subpower-dense family from source information genuinely weaker than the conclusion.

## Leave one-sided radial filtering unless the boundary/source term is controlled explicitly

Fixed finite parity filters followed by absoluteization were already closed by MC-112--MC-113. MC-114 now closes the obvious growing-filter repair on the physical Hamming shells. Polynomial attenuation of a proportional transfer band requires filter range `Theta(log N)`, whereas the physical shell degree is only `O(log N/log log N)`. The filter therefore runs beyond the entire source support.

Exact Laurent bookkeeping shows what happens: parity survives only if the negative-index boundary terms are retained. With zero extension, tiny filtered values on the physical shells can be manufactured for every input because most of the filter lies outside the source. This is a finite-support boundary artifact, not Möbius cancellation.

A surviving radial construction must derive a signed relation between the physical shell and the displaced boundary/source terms, justify a genuinely two-sided or nonlocal extension from arithmetic, or leave radial scalarization for finer source information. Small one-sided filtered coefficients alone are no longer an admissible endpoint signal.

## Preserve signed cross-degree and excursion information through the final norm

The endpoint is carried by cancellation among large degree components and by the excursion structure of `M(x)`, not by positive shell masses. Positive norms, absoluteization, and local filtering can preserve labels while erasing the interaction that MC-115 ultimately needs.

A useful carrier should therefore identify a signed cross-degree, cross-scale, or excursion-coupled quantity whose control implies the RH-scale mean-absolute bound without already inserting `1/zeta`, a zero-free region, or an RH-equivalent coarse mode by definition.

## Treat stronger Pintz asymptotics as optional refinement, not a prerequisite

MC-009 remains `NEEDS-AUDIT` for the claimed full logarithmic-order asymptotic and terminal-window maximum equivalence. If that audit succeeds it may sharpen the geometry of large excursions. It must not be used as the evidentiary basis for the bare mean-absolute RH equivalence, which is independently established by MC-115.