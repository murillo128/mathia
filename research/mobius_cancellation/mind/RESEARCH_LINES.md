# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Find arithmetic rigidity or collective capacity beyond bounded overlap and the enlarged Page band

**Linked intuitions:** `MI-013-bost-connes-regularity-needs-an-intermediate-transverse-category` through `MI-028-deuring-heilbronn-source-bandwidth-has-a-lambert-w-certificate-ceiling`.

MC-293--MC-297 move the problem from individual character cost to the selected subset spectrum. In the disjoint endpoint model almost all noncentral subset sums are Page-high-cost; with overlap, a cheap upper-half mode must spend enough parity-folding overlap to cancel the disjoint-profile bias.

MC-298 closes a generic repair by adding finitely many higher intersection statistics. If `K` is endpoint-defect multiplicity, symmetric `j`-fold overlaps through order `r` are exactly the factorial moments `E[(K)_j]`, while Page sign is the full parity character `(-1)^K`. For every fixed `r<m`, explicit moment-matched finite models have identical overlap data through order `r` but different Page parity. No bounded hierarchy of overlap marginals can therefore control high-cardinality Page modes by itself.

MC-299 adds arithmetic feedback in the exceptional branch. If the unique possible Page exception is actually near-negative with defect `O(1/log log y)`, its Landau--Siegel zero is close enough that Deuring--Heilbronn repulsion forces every other shell mode with source cost

`Q(lambda) <= E_y = exp(kappa_A log(y) log log log(y) / log log(y))`

to be smaller than any prescribed power of `1/log y`. Relative to the original Page band `D_y=exp(kappa_0 log(y)/log log(y))`, the logarithmic source-cost threshold expands by an unbounded `log log log y` factor.

MC-300 identifies the information ceiling of that same black-box route. Writing `delta_*` for the exceptional zero distance and `v=log q`, fixed inverse-log accuracy is certified only in the Lambert-W envelope

`v ≲_A (log y/log log y) W(c_A log log y/(delta_* log y))`.

With only the coarse input `delta_* ≲ 1/(log y log log y)`, the worst admissible case gives exactly `v=O_A(log y log log log y/log log y)`. The MC-299 enlargement is therefore not a loose parameter choice: a parametrically super-`log log log y` uniform band requires stronger exceptional-zero information, a collective family theorem, or a different carrier.

The live arithmetic gate is two-sided. Either actual Möbius/Legendre geometry collapses high-order parity to accessible structure, interaction information grows with selected cardinality, or a collective source-capacity theorem rules out realizing the required family once almost all modes are forced beyond the Lambert-W band. Individual-mode repulsion has now been priced to its present input limit; the unresolved problem is collective realizability or genuinely stronger arithmetic input.

## Keep parity, overlap order, exceptional-zero repulsion and collective realizability separate

MC-298 shows that replacing pair overlap by any fixed finite order still leaves a generic parity-null direction. MC-299 is different: it conditionally enlarges the arithmetic source-cost band whenever the one allowed Page exception is strong enough to matter. MC-300 is different again: it computes the **certificate ceiling** of that single-exception route from the available exceptional-zero accuracy.

A ceiling of the present proof channel is not a theorem that wider bands are impossible. Even perfect pricing of individual modes would still leave the collective-realizability question, while stronger information about `delta_*` would widen the Lambert-W envelope without changing the overlap obstruction. These are distinct resources.

## Preserve matched controls and classical arithmetic feedback as falsifiers

The exchangeable moment-matched controls of MC-298 join MC-295 as explicit warnings: generic finite set systems can satisfy rich low-order data while retaining the forbidden high-order behavior. Geelen thresholds, entropy bounds and Hamming/Sperner arguments remain controls, while Landau--Page and Deuring--Heilbronn provide genuine arithmetic restrictions on the source-cost spectrum. MC-300 prevents constant optimization inside the same zero-repulsion inequality from being mistaken for new arithmetic information. None of these ingredients alone closes the high-cost quotient escape.
