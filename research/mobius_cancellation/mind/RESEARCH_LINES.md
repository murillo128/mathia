# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history. Lines should survive only while they separate genuinely different mechanisms.

## Identify the signed or multiscale datum that beats the polynomial information-budget barrier

**Linked intuitions:** `MI-001-local-cancellation-needs-a-polynomial-information-budget`.

MC-001 gives an exact black-box local-to-global transfer bound, while MC-004--MC-006 show that the same quantitative barrier survives much stronger-looking inputs. Exact square-free support plus full qualitative fixed-shift Chowla allows `X/log X` anchored bias when multiplicativity is absent; exact support plus multiplicativity and vanishing normalized mean still allows `x/(log x)^beta`; and the currently proved averaged two-point Chowla estimate yields only logarithmic global saving through van der Corput.

A surviving cancellation mechanism must identify the additional datum that rules out all of these controls at polynomial strength. Natural candidates are signed correlations between overlapping windows, multiscale compatibility of exceptional sets, quantitative prime-local constraints, bilinear/Type-I-II structure, or higher correlations uniform over polynomial ranges. A decisive result must state the transfer inequality and produce a fixed polynomial gain after every exceptional-set, scale-transition, and correlation-range loss.

## Separate prime-power fidelity from a genuinely useful comparator theorem

**Linked intuitions:** `MI-002-single-scale-pretentiousness-has-a-prime-harmonic-ceiling` and `MI-003-analytic-nonmasking-is-weaker-than-absolute-convolution-inversion`.

MC-002 proves that the standard prime-only pretentious scalar has only `O(log log x)` information. MC-003 shows that the natural prime-power enrichment does distinguish Möbius from Liouville, but its exact threshold is the square layer `1/2`, matching the elementary square-divisor convolution; with current Liouville bounds it gives no unconditional power bootstrap.

MC-007--MC-008 sharpen the comparator question. Same-prime multiplicative comparators differ from Möbius through a squarefull kernel, so forward power transfer above `1/2` is automatic, while absolute reverse inversion can be obstructed by finitely many small-prime factors. Yet the explicit `2`-adic comparator of MC-008 remains RH-sensitive even when its absolute inverse only converges for `Re s>1`: what matters analytically is that its auxiliary transfer factor is zero-free on the open right critical half-strip.

The live problem is therefore to find an independently controlled comparator together with a **nonmasking** transfer factor whose zero-free property is proved without importing the zeta divisor. A decisive positive gives a new comparator estimate and a non-circular analytic bridge. A decisive negative shows that every available nonmasking comparator is already as hard to bound as Möbius or that the proposed transfer merely re-encodes `1/zeta`.

## Require every global-cancellation statistic to expose its information budget and matched controls

**Linked intuitions:** `MI-001-local-cancellation-needs-a-polynomial-information-budget`, `MI-002-single-scale-pretentiousness-has-a-prime-harmonic-ceiling`, and `MI-003-analytic-nonmasking-is-weaker-than-absolute-convolution-inversion`.

Local pseudorandomness, logarithmic averages, correlation bounds, pretentious distances, prime-power enrichments, and comparator Dirichlet series should be evaluated by the quantitative information they retain about the **uniform anchored** summatory target. Qualitative fixed-shift cancellation, exact support, multiplicativity, or a rich prime-power statistic can all be diagnostic without supplying a polynomial transfer.

A decisive candidate must state both the information budget and the strongest matched control. At minimum it should survive the MC-004 qualitative-Chowla control, the MC-005 multiplicative exact-support control, the Möbius/Liouville square kernel, and same-prime squarefull comparators. Using `1/zeta`, Perron shifting, or an explicit formula is admissible only when the zero-free information needed by the argument has been derived upstream rather than imported through the target analytic continuation.
