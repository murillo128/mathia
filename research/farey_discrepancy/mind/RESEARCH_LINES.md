# Farey-discrepancy research lines

This file holds the current mathematical questions suggested by the durable Farey-discrepancy intuitions. It is not a roadmap, task queue, status page, or history.

## Measure the affine distance from the physical correction to the positive cone modulo switched blind directions

**Linked intuition:** `MI-039-periodic-scale-switching-can-create-a-supercritical-floquet-blind-mode`.

FD-231 establishes that signed switched-blind directions can have macroscopic mass while keeping the all-integer response only first order. FD-232 then shows that this freedom cannot automatically be realized by a nonnegative occupancy. If a signed blind correction has a fixed positive fraction of negative aggregate capacity on late dyadic blocks, every positive lift `a=b+s` whose occupancy and switched response are both subquadratic would require too much nonnegative slack.

For the explicit FD-231 blind profile, the negative-capacity fraction stays bounded away from zero, so that particular blind direction cannot be hidden inside a subquadratic positive reservoir. The unresolved physical question is narrower: start from the correction forced by the actual Farey/Mertens inversion and allow addition of any signed switched-blind direction. Can its negative part be made aggregate-capacity sparse on late blocks?

A positive lower bound for that best possible negative-capacity fraction would give an intrinsic one-sided obstruction. A sequence of blind representatives whose negative fraction tends to zero would reopen the construction, but would still need a separate response/capacity estimate. The relevant quotient is therefore the affine class of the physical correction modulo the switched blind space, measured against the positive cone rather than by a symmetric nullspace norm.

## Keep signed invisibility and positive realizability distinct

Signed kernel vectors describe what the switched operator cannot see. A physical occupancy must also satisfy positivity and capacity constraints. FD-232 proves that these are independent requirements: a large signed null direction can be analytically invisible yet physically unaffordable. Future constructions should price the negative part after the best admissible blind adjustment before attributing any gain to switched cancellation.
