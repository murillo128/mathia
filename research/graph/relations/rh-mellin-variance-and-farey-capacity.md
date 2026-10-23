---
id: RG-rh-mellin-variance-and-farey-capacity
type: research-graph-relation
scope: mobius_cancellation-farey_discrepancy
derived: true
---

# RH Mellin variance and balanced Farey capacity

This projects the explicit bridge in MC-520 and the variance-to-zero-free refinement in MC-521, retaining their hypotheses and the method-level scope of the earlier obstructions. It adds no cancellation theorem.

## Same moment, same selected shell

[[research/farey_discrepancy/findings/FD-311-a-quarter-power-sliding-variance-saving-would-close-balanced-capacity|FD-311]], equations (6), (9) and (24), records the balanced near-capacity lower bound
\(J_\mu(X,N)\ge XN^{1/2+3c-o(1)}\), with \(c=1-\log_2(3/2)\), and RH-localized shells \(N=X^{\beta+o(1)}\), \(1/2\le\beta\le1/(1+2c)\). Its upper-bound target concerns this complete discrete sliding moment, not unrelated scales or typical starts.

[[research/mobius_cancellation/findings/MC-520-rh-mellin-variance-closes-conditional-farey-window-target|MC-520]], equations (1)–(13), derives under RH the uniform bound \(J_\mu(X,N)\ll_\varepsilon X^{1+\varepsilon}N\) for integer windows. Section 4 applies it to that exact packet: \(X\le N^{2+o(1)}\), and any fixed \(0<\varepsilon<(3c-1/2)/2\) gives a strict power contradiction. Its conclusion excludes the specified **RH-conditional balanced near-capacity branch**. RH is used both for shell localization and for the variance theorem. MC-520 takes the upstream Farey reduction as its authorized input; this projection does not independently re-audit that chain.

## Why the endpoint and smooth-sector barriers survive

[[research/farey_discrepancy/findings/FD-312-pointwise-mertens-envelopes-cannot-close-sliding-variance-below-source-ceiling|FD-312]], equations (38)–(40), limits the operation that separately majorizes the two Mertens endpoints: the best balanced saving is \(1-2c\), below the required \(3/2-3c\). MC-520 retains the difference in the Mellin multiplier, so it does not refute that no-go. It corrects the broader suggestion that a new variance theorem is needed under RH, and section 5 corrects FD-312's weaker report of Gao's unpublished estimate. The unpublished proof is not a load-bearing input.

[[research/mobius_cancellation/findings/MC-178-chinis-polynomial-window-smooth-number-ceiling|MC-178]], prior-art and boundary sections, likewise confines its polynomial-window ceiling to Chinis's large-prime-factor/block-extension method. Its updated text explicitly points to MC-520 as a different RH method. Neither finding supplies the unconditional source input sought by [[research/mobius_cancellation/findings/MC-176-gallagher-critical-shell-good-churchhouse-variance|MC-176]] and [[research/mobius_cancellation/findings/MC-177-gallagher-diagonal-energy-direct-mertens-power|MC-177]]. Those references express MC-520's circularity boundary, not a new transfer.

## Classical inputs and durable synthesis

The [[research/prior_art/incremental/PA-rh-reciprocal-zeta-subpower-bound|RH reciprocal-zeta bound]] controls frequencies after Mellin Plancherel; [[research/prior_art/incremental/PA-saffari-vaughan-averaging|Saffari–Vaughan averaging]] converts multiplicative to additive windows. These are separate documented dependencies, not a new prior-art theorem proving the Farey consequence by itself.

[[research/mobius_cancellation/mind/intuition/MI-100-mellin-differences-retain-the-rh-short-window-variance-gain|MC MI-100]] records the retained-difference mechanism; [[research/farey_discrepancy/mind/intuition/MI-066-rh-mellin-variance-excludes-balanced-near-capacity|FD MI-066]] records the matching shell and surviving endpoint barrier. Their synthesis does not increase the evidence level. Unconditional cancellation, logarithmic-loss variance, and general Farey-route closure are not established here.

## Reverse direction without sharp endpoints

[[research/mobius_cancellation/findings/MC-521-smooth-deconvolution-removes-the-variance-zero-free-boundary-loss|MC-521]], equations (1)–(14), assumes the complete uncentered moment bound \(J(X,X^\theta)\ll_\varepsilon X^{1+\varepsilon}(X^\theta)^{2-\eta}\), for every \(\varepsilon>0\) and every sufficiently large real \(X\), with fixed \(0<\theta<1\), \(0<\eta\le1\). It derives zero exclusion in \(\Re s>\alpha=1-\theta\eta/2\). Its multiplicative-window version has the same analytic consequence. In contrast, [[research/mobius_cancellation/findings/MC-177-gallagher-diagonal-energy-direct-mertens-power|MC-177]], equation (14), recovers sharp Mertens endpoints only with exponent \(\max(\alpha,\theta)\) by its direct boundary method.

MC-521 applies [[research/prior_art/incremental/PA-van-cittert-approximate-deconvolution|finite van Cittert deconvolution]] to the smooth test weight, with fixed depth satisfying \(K(1-\theta)>\theta\eta/2\). The resulting Mellin test family excludes a putative zero without a uniform inverse estimate at growing height. This improves the analytic conclusion when \(\theta>2/(2+\eta)\); it neither refutes MC-177's method-specific optimum nor supplies the corresponding sharp unsmoothed Mertens bound or removes its weighted Gallagher Gaussian-removal cost.

Section 5 of MC-521 explicitly combines its implication with MC-520's RH converse: diagonal variance at each of a sequence of fixed \(\theta_j\uparrow1\), with the complete all-scale quantifiers, is RH-equivalent. Constants may depend on \(j\). A selected shell, uncontrolled exceptional starts, or centering by an uncontrolled mean cannot replace the premise. At the balanced \(\theta=1/2\) scale, MC-521 states that this gives no stronger Farey-window estimate. [[research/mobius_cancellation/mind/intuition/MI-101-smooth-deconvolution-separates-zero-exclusion-from-endpoint-recovery|MC MI-101]] preserves these distinctions. The uniform arithmetic variance input remains unproved unconditionally; no new unconditional zero-free region or novelty claim follows.
