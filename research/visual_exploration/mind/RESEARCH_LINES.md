# Visual-exploration research lines

This file records the current mathematical questions that survive the Visual-Exploration evidence. It is not a roadmap, task queue, status page, or history.

## Derive a Wang/source-packet capacity bound before testing the qutrit residual

VIS-367--VIS-389 reduce the intrinsic centered source-subspace problem to a scale-free commutator-Laplacian observable. In the minimal generic qutrit rank-one case, after source conjugacy and the scalar defect rate are fixed, the normalized positive spectrum has one residual shape coordinate. VIS-390--VIS-402 then calibrate that coordinate under progressively broader independently specified Gaussian/Gamma packet, exclusive-allocation, signed sector and finite common-factor nuisance mechanisms.

VIS-403--VIS-404 show why unrestricted latent language does not sharpen the null. Conditional independence given some finite latent is vacuous, and even a fixed scalar prior `U~Uniform(0,1)` plus an unrestricted monotone quantile decoder realizes every Borel residual law. Qualitative monotonicity or smoothness is therefore not a capacity restriction when the decoder or its constants are chosen after seeing the target.

VIS-405 identifies the first exact quantitative boundary for that transport escape. If the monotone decoder is required **in advance** to have `Lip(Q)<=L` on a residual interval `I` of length `ell`, then this is equivalent to the observable mass-floor condition

`nu((x,y]) >= (y-x)/L`

for every residual interval, or equivalently

`nu = (1/L) Leb_I + (1-ell/L) eta`, with `L>=ell`.

At `L=ell` the only admissible law is uniform; for larger fixed `L` the remaining excess law `eta` is arbitrary. Thus a numerical Lipschitz budget is genuinely falsifiable, but its mathematical content is exactly a uniform mass floor and nothing stronger.

VIS-406 closes the generic representation-to-capacity bridge. A fixed differentiable basis with coefficient budget `||c||_p<=B` gives `Lip(Q)<=B M_q` and hence a forced uniform component of mass at least `ell/(B M_q)`. A monotone polynomial decoder of degree at most `n` has the universal Markov bound `Lip(Q)<=n^2 ell`, forcing uniform mass at least `1/n^2`. In the ordered Bernstein subclass, the coefficient-gap geometry improves this to the exact floor `ell/(n Delta)`, and in particular to at least `1/n` when only degree and ordered endpoints are retained. These are source-free capacity consequences: they show exactly how a representation budget becomes a target-law restriction, but they do not derive any such budget from Wang arithmetic.

The live question is therefore narrower: **can the actual Wang/source-packet construction derive, before the candidate residual is inspected, a fixed basis, degree, coefficient norm, Bernstein-gap, interaction or comparable complexity budget?** Once such a bound is source-derived, VIS-405--VIS-406 turn it immediately into a falsifiable residual mass floor. Choosing a convenient decoder family or its constants after seeing the residual remains circular and collapses back toward the VIS-404 universal transport.

The accepted clue `CLUE-wang-fixed-source-packet-localization` already records this handoff and does not need a Mind-owned status change. No new proposed clue is warranted by VIS-406: the precise fertile direction is established and already persisted as an accepted research question.

## Quotient universal compact geometry before crediting a Wang gain

Any positive-Hilbert improvement still has to survive the earlier representation gates: remove exact commutant directions, freeze the ambient Hilbert metric and numerical-rank rule, calibrate source-subspace and tangent-orientation nulls, and condition on the minimal source invariants before interpreting nonlinear low modes. A source-side residual anomaly is not yet a destination gain; its effect must propagate through the Wang map after metric scale, Gram-gap/cluster width, coefficient norm, normalization, rank selection and source-information costs are charged.

Higher dimension or rank may introduce additional shape coordinates, but nominal dimensionality is not evidence. The next genuine escape is a pre-specified nuisance/decoder class that excludes some residual laws for a source-derived reason and whose excluded direction remains resolvable at the destination.