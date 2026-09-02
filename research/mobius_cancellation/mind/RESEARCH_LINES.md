# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history. Lines should survive only while they separate genuinely different mechanisms.

## Identify the signed or multiscale datum that beats the polynomial information-budget barrier

**Linked intuitions:** `MI-001-local-cancellation-needs-a-polynomial-information-budget`.

MC-001 gives an exact black-box local-to-global transfer bound, while MC-004--MC-006 show that the same quantitative barrier survives much stronger-looking inputs. A surviving cancellation mechanism must identify additional source-natural data that rule out these controls at polynomial strength. Natural candidates are signed correlations between overlapping windows, multiscale compatibility of exceptional sets, quantitative prime-local constraints, bilinear structure, or higher correlations uniform over polynomial ranges.

A decisive result must state the transfer inequality and produce a fixed polynomial gain after every exceptional-set, scale-transition, and correlation-range loss.

## Preserve cancellation while targeting mean-absolute Mertens size

**Linked intuitions:** `MI-004-mean-absolute-cancellation-needs-excursion-coupled-information`.

MC-013 gives an exact Tanaka interface for `D_M`, but MC-014 proves that separately bounding its signed-feedback and local-time pieces is the wrong generic target: for the character modulo `3` both pieces are quadratic and cancel almost completely. The first surviving pathwise carrier is the excursion-square budget `E_2(N)=sum ell_j^2`, which controls total absolute area and can be `N^(3/2)` even when pointwise height reaches `N^(3/4)`.

The live arithmetic question is whether Möbius structure yields `E_2(N)=O_epsilon(N^(3/2+epsilon))`, or a comparably strong multiscale excursion-tail bound, without importing the desired Mertens estimate. The connection from RH-scale `D_M` back to RH currently uses the fresh Pintz theorem recorded in MC-009 and remains subject to its incomplete audit in MC-010--MC-012; that conditional endpoint must not be used as upstream evidence.

## Separate prime-power fidelity from a genuinely useful comparator theorem

**Linked intuitions:** `MI-002-single-scale-pretentiousness-has-a-prime-harmonic-ceiling` and `MI-003-analytic-nonmasking-is-weaker-than-absolute-convolution-inversion`.

MC-002 proves that the standard prime-only pretentious scalar has only `O(log log x)` information. MC-003 shows that prime-power enrichment distinguishes Möbius from Liouville, but its exact threshold is the square layer `1/2`, matching the elementary square-divisor convolution. MC-007--MC-008 show that absolute reverse inversion can fail even when a comparator remains analytically RH-sensitive.

The live problem is to find an independently controlled comparator together with a nonmasking transfer factor whose zero-free property is proved without importing the zeta divisor.

## Require every global-cancellation statistic to expose its information budget and matched controls

**Linked intuitions:** `MI-001-local-cancellation-needs-a-polynomial-information-budget`, `MI-002-single-scale-pretentiousness-has-a-prime-harmonic-ceiling`, `MI-003-analytic-nonmasking-is-weaker-than-absolute-convolution-inversion`, and `MI-004-mean-absolute-cancellation-needs-excursion-coupled-information`.

Local pseudorandomness, logarithmic averages, correlation bounds, pretentious distances, prime-power enrichments, comparator Dirichlet series, and excursion statistics should be evaluated by the quantitative information they retain about the anchored summatory target. MC-014 adds a new matched-control rule: **do not turn an internally cancelling identity into separate absolute budgets** unless the source theorem genuinely controls those pieces.

A decisive candidate must state both the information budget and the strongest matched control. Using `1/zeta`, Perron shifting, an explicit formula, or the still-audited mean-absolute zero theorem is admissible only when the zero information needed by the argument has been derived upstream rather than imported through the target continuation.
