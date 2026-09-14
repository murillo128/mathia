# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Find arithmetic rigidity or collective capacity beyond bounded overlap and the enlarged Page band

**Linked intuitions:** `MI-013-bost-connes-regularity-needs-an-intermediate-transverse-category` through `MI-027-bounded-overlap-order-cannot-determine-page-parity`.

MC-293--MC-297 move the problem from individual character cost to the selected subset spectrum. In the disjoint endpoint model almost all noncentral subset sums are Page-high-cost; with overlap, a cheap upper-half mode must spend enough parity-folding overlap to cancel the disjoint-profile bias.

MC-298 closes a generic repair by adding finitely many higher intersection statistics. If `K` is endpoint-defect multiplicity, symmetric `j`-fold overlaps through order `r` are exactly the factorial moments `E[(K)_j]`, while Page sign is the full parity character `(-1)^K`. For every fixed `r<m`, explicit moment-matched finite models have identical overlap data through order `r` but different Page parity. No bounded hierarchy of overlap marginals can therefore control high-cardinality Page modes by itself.

MC-299 adds an arithmetic feedback in the exceptional branch. If the unique possible Page exception is actually near-negative with defect `O(1/log log y)`, its Landau--Siegel zero is close enough that Deuring--Heilbronn repulsion forces every other shell mode with source cost

`Q(lambda) <= E_y = exp(kappa_A log(y) log log log(y) / log log(y))`

to be smaller than any prescribed power of `1/log y`. Relative to the original Page band `D_y=exp(kappa_0 log(y)/log log(y))`, the logarithmic source-cost threshold expands by an unbounded `log log log y` factor. Thus a surviving multi-mode near-negative obstruction must, apart from the single exceptional direction, live beyond this larger band.

The live arithmetic gate is therefore two-sided. Either actual Möbius/Legendre geometry collapses high-order parity to accessible structure, interaction information grows with selected cardinality, or a collective source-capacity theorem rules out realizing the required family of characters once almost all modes are forced beyond `E_y`. MC-299 moves the admission threshold; it does not solve collective realizability beyond it.

## Keep parity, overlap order, exceptional-zero repulsion and collective realizability separate

MC-298 shows that replacing pair overlap by any fixed finite order still leaves a generic parity-null direction. MC-299 is different: it does not reconstruct parity from overlaps, but conditionally enlarges the arithmetic source-cost band whenever the one allowed Page exception is strong enough to matter.

Even perfect pricing of individual modes would still leave the collective-realizability question. Conversely, a source-capacity theorem could close the branch without reconstructing parity from overlaps. These are distinct resources.

## Preserve matched controls and classical arithmetic feedback as falsifiers

The exchangeable moment-matched controls of MC-298 join MC-295 as explicit warnings: generic finite set systems can satisfy rich low-order data while retaining the forbidden high-order behavior. Geelen thresholds, entropy bounds and Hamming/Sperner arguments remain controls, while Landau--Page and Deuring--Heilbronn now provide genuine arithmetic restrictions on the source-cost spectrum. None alone closes the high-cost quotient escape.
