# Möbius-cancellation research lines

This file holds the current mathematical lines of investigation suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Produce RH-scale mean-absolute Mertens control from information that controls excursions, not only sub-L1 moments

**Linked intuitions:** `MI-004-mean-absolute-cancellation-needs-excursion-coupled-information` and `MI-012-hamming-regularization-is-degree-two-damping-before-the-square-root-transition`.

MC-115 gives the exact downstream bridge: `X^{-1} integral_1^X |M(x)| dx = O_epsilon(X^(1/2+epsilon))` is equivalent to RH by Mellin continuation of `1/zeta(s)`. MC-116 shows how subpower-dense checkpoints can interpolate that estimate through all intermediate scales.

MC-121 materially reduces the endpoint coverage requirement. Pintz's 1987 theorem forces an off-critical zero to create excessive mean-absolute mass at **every** sufficiently large scale. Consequently the RH-scale bound for the actual Möbius mean on any rigorously produced unbounded checkpoint sequence -- even an arbitrarily lacunary one -- already implies RH. Scale density of the final `D_M` output is therefore not a necessary gate.

MC-117--MC-120 still sharply restrict what weaker input can imply that endpoint. Fractional `p<1` moments underweight rare coherent excursions; the obstruction survives exact square-free support and multiplicativity, persists uniformly across polynomial windows, and can be realized by one fixed multiplicative comparator on infinitely many windows. These controls do not contradict MC-121 because Pintz's zero-to-mean theorem is specific to the actual Möbius/zeta pair.

The live source question is therefore whether a genuinely Möbius-specific signed, bilinear, correlation, multiplicative, or multiscale law can upgrade weaker information to an RH-scale first absolute mean **on some unbounded family of scales**. Dense/overlapping-scale coherence may be one route, but it is no longer required merely to interpolate the final endpoint.

## Leave one-sided radial filtering unless the boundary/source term is controlled explicitly

Fixed finite parity filters followed by absoluteization are closed by MC-112--MC-113, and MC-114 closes the obvious growing-filter repair on the physical Hamming shells. Polynomial attenuation of a proportional transfer band requires range `Theta(log N)`, whereas the shell degree is only `O(log N/log log N)`, so the filter outruns the physical source support.

A surviving radial construction must derive a signed relation to the displaced boundary/source terms, justify a genuinely two-sided or nonlocal extension from arithmetic, or leave radial scalarization for finer source information. Small one-sided filtered coefficients alone are a boundary artifact.

## Preserve signed cross-degree, cross-scale, and excursion information through the final norm

The endpoint is carried by cancellation among large degree components and by the excursion geometry of `M(x)`, not by positive shell masses or low fractional moments. MC-120 shows that one-function consistency across infinitely many windows still does not prevent large first-absolute excursions for a generic multiplicative comparator. MC-121 then shows that once the actual Möbius first moment is recovered at the square-root exponent, no dense scale mesh is needed to reach RH.

A useful carrier should therefore identify a signed cross-degree, cross-scale, or correlation-coupled quantity whose control actually recovers first-moment amplitude for Möbius, without already inserting `1/zeta`, a zero-free region, or an RH-equivalent coarse mode by definition.

## Use the audited Pintz lower bound as an endpoint reduction, not as a source mechanism

MC-121 relies on Pintz's 1987 theorem that every off-critical zero forces a quantitative lower bound for the actual mean-absolute Mertens function at every sufficiently large scale. This prior-art bridge legitimately removes the final checkpoint-density requirement, but it does not provide the missing arithmetic upper bound or local-to-global transfer.

Stronger separate Pintz asymptotic claims retained in earlier findings keep their own audit status and are not needed for the arbitrary-checkpoint RH criterion.