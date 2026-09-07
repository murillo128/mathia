# Möbius-cancellation research lines

This file holds the current mathematical lines of investigation suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Produce RH-scale mean-absolute Mertens control from information beyond fixed local feedback

**Linked intuitions:** `MI-004-mean-absolute-cancellation-needs-excursion-coupled-information` and `MI-012-hamming-regularization-is-degree-two-damping-before-the-square-root-transition`.

MC-115 gives the exact downstream bridge: `X^{-1} integral_1^X |M(x)| dx = O_epsilon(X^(1/2+epsilon))` is equivalent to RH by Mellin continuation of `1/zeta(s)`. MC-121 materially reduces the endpoint coverage requirement: Pintz's 1987 theorem forces an off-critical zero to create excessive mean-absolute mass at every sufficiently large scale, so the RH-scale bound for the actual Möbius mean on any rigorously produced unbounded checkpoint sequence already implies RH.

MC-117--MC-120 still show that sub-`L^1` information can miss rare coherent excursions even under exact square-free support, multiplicativity, polynomial windows, and one fixed multiplicative comparator. MC-122--MC-124 now close another large class of apparent source enrichments. Deterministically weighted amplitude feedback is exactly quadratic path energy after its square-free correction; every scalar state-local one-step feedback splits into a path potential plus unoriented occupation; and every fixed finite-memory observable odd under global Möbius sign reversal is a finite combination of fixed-shift `mu/mu^2` correlations that is logarithmically negligible by existing theory.

The live source question is therefore sharper: derive a **quantitative Möbius-specific mechanism outside fixed local cylinder information** that recovers first-absolute excursion amplitude on some unbounded family of scales. Candidate escapes include growing/state-coupled memory, multiscale or nonlocal correlations, quantitatively controlled occupation statistics, or another source law with an explicit polynomial information budget. Merely adding deterministic weights or a bounded amount of local history is no longer a new carrier.

## Kill fixed state-local and fixed-memory feedback before treating it as new signed information

MC-122 gives the amplitude test: arbitrary deterministic weights on `mu_n M_{n-1}` reduce by summation by parts to weighted `M_n^2` energy plus the explicit square-free diagonal. MC-123 gives the structural reason on the scalar Mertens state graph: every reversal-odd one-step edge field is a potential, and all non-potential residue is unoriented edge/loop occupation.

MC-124 shows that finite memory does create genuine cycle topology, but not a new logarithmic information class. Every fixed-window sign-odd cylinder observable expands into finitely many shifted products of `mu` and `mu^2`; the Tao--Teräväinen product criterion makes all such terms logarithmically invisible. A memory proposal should therefore identify exactly where it leaves the fixed-cylinder regime and why the resulting estimate is quantitatively stronger than qualitative fixed-shift correlation cancellation.

## Leave one-sided radial filtering unless the boundary/source term is controlled explicitly

Fixed finite parity filters followed by absoluteization are closed by MC-112--MC-113, and MC-114 closes the obvious growing-filter repair on the physical Hamming shells. Polynomial attenuation of a proportional transfer band requires range `Theta(log N)`, whereas the shell degree is only `O(log N/log log N)`, so the filter outruns the physical source support.

A surviving radial construction must derive a signed relation to the displaced boundary/source terms, justify a genuinely two-sided or nonlocal extension from arithmetic, or leave radial scalarization for finer source information. Small one-sided filtered coefficients alone are a boundary artifact.

## Preserve signed cross-degree, cross-scale, occupation, and excursion information through the final norm

The endpoint is carried by cancellation among large degree components and by the excursion geometry of `M(x)`, not by positive shell masses, low fractional moments, or a fixed local feedback vocabulary. MC-121 shows that once the actual Möbius first moment is recovered at the square-root exponent, no dense scale mesh is needed to reach RH; MC-122--MC-124 show that several tempting local mechanisms either repackage path energy or fall inside qualitative fixed-correlation theory.

A useful carrier should therefore identify information that survives those reductions and actually controls first-moment amplitude for Möbius, without inserting `1/zeta`, a zero-free region, or an RH-equivalent coarse mode by definition.

## Use the audited Pintz lower bound as an endpoint reduction, not as a source mechanism

MC-121 relies on Pintz's 1987 theorem that every off-critical zero forces a quantitative lower bound for the actual mean-absolute Mertens function at every sufficiently large scale. This prior-art bridge legitimately removes the final checkpoint-density requirement, but it does not provide the missing arithmetic upper bound or local-to-global transfer.

Stronger separate Pintz asymptotic claims retained in earlier findings keep their own audit status and are not needed for the arbitrary-checkpoint RH criterion.