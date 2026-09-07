# Möbius-cancellation research lines

This file holds the current mathematical lines of investigation suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Produce RH-scale mean-absolute Mertens control from information that controls excursions, not only sub-L1 moments

**Linked intuitions:** `MI-004-mean-absolute-cancellation-needs-excursion-coupled-information` and `MI-012-hamming-regularization-is-degree-two-damping-before-the-square-root-transition`.

MC-115 gives the exact downstream bridge: `X^{-1} integral_1^X |M(x)| dx = O_epsilon(X^(1/2+epsilon))` is equivalent to RH by Mellin continuation of `1/zeta(s)`. MC-116 shows it is enough to prove the exponent on a deterministic subpower-dense checkpoint sequence.

MC-117--MC-120 sharply restrict what weaker input can imply that endpoint. Fractional `p<1` moments underweight rare coherent excursions; the obstruction survives exact square-free support and multiplicativity, persists uniformly across polynomial windows, and can be realized by one fixed multiplicative comparator on infinitely many windows. The remaining escape in that construction is deliberate lacunarity: it does not satisfy the subpower-dense checkpoint geometry of MC-116 and does not reproduce Möbius-specific correlation laws.

The live source question is therefore whether dense/overlapping-scale coherence, a genuinely joint multiplicativity-correlation theorem, or another Möbius-specific constraint forbids the coherent excursion blocks that all sub-`L1` controls above permit.

## Leave one-sided radial filtering unless the boundary/source term is controlled explicitly

Fixed finite parity filters followed by absoluteization are closed by MC-112--MC-113, and MC-114 closes the obvious growing-filter repair on the physical Hamming shells. Polynomial attenuation of a proportional transfer band requires range `Theta(log N)`, whereas the shell degree is only `O(log N/log log N)`, so the filter outruns the physical source support.

A surviving radial construction must derive a signed relation to the displaced boundary/source terms, justify a genuinely two-sided or nonlocal extension from arithmetic, or leave radial scalarization for finer source information. Small one-sided filtered coefficients alone are a boundary artifact.

## Preserve signed cross-degree, cross-scale, and excursion information through the final norm

The endpoint is carried by cancellation among large degree components and by the excursion geometry of `M(x)`, not by positive shell masses or low fractional moments. MC-120 adds a cross-scale warning: even one-function consistency across infinitely many lacunary windows does not prevent large first-absolute excursions.

A useful carrier should therefore identify a signed cross-degree, cross-scale, or correlation-coupled quantity whose control implies the RH-scale mean-absolute bound without already inserting `1/zeta`, a zero-free region, or an RH-equivalent coarse mode by definition.

## Treat stronger Pintz asymptotics as optional refinement, not a prerequisite

MC-009 remains `NEEDS-AUDIT` for the claimed stronger excursion profile. It must not be used as the evidentiary basis for the bare mean-absolute RH equivalence, which is independently established by MC-115.