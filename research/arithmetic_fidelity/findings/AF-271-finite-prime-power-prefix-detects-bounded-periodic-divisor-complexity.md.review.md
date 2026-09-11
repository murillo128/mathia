---
type: adversarial-review
target: research/arithmetic_fidelity/findings/AF-271-finite-prime-power-prefix-detects-bounded-periodic-divisor-complexity.md
---

# Adversarial review

## Adversary

The Vandermonde argument correctly proves the stated theorem when `r` bounds the number of distinct nonconstant divisor nodes of the **quotient/difference divisor after cancellation**. But the stronger sentence in §2 — “if two controls of known signed-divisor complexity at most `r` agree on the first `r` source coefficients, their quotient cannot contain any nonconstant divisor orbit at all” — is false if `r` bounds each control separately.

Already for `r=2`, take signed divisor measures

\[
\mu_1=\delta_1+\delta_{-1},
\qquad
\mu_2=2\delta_i-\delta_{2i}.
\]

Each has exactly two distinct nonzero nodes with nonzero integer multiplicities, while their first two power sums agree:

\[
q_1(\mu_1)=0=q_1(\mu_2),
\qquad
q_2(\mu_1)=2=q_2(\mu_2).
\]

Nevertheless `\mu_1-\mu_2` is nonzero (and has four distinct nodes), so the corresponding rational periodic controls differ by a nontrivial quotient. The issue is that two controls of individual complexity at most `r` can have quotient complexity as large as `2r`; the displayed `r\times r` Vandermonde proof only applies when the **quotient itself** has at most `r` distinct signed divisor nodes.

This does not attack the main quotient-complexity theorem, the roots-of-unity sharpness example, or the separated-node stability bound. It does make the pairwise-identifiability sentence materially stronger than the proof supports and potentially changes the required prefix length by a factor of two under the natural “each control has complexity at most `r`” reading. The objection is resolved by narrowing that sentence (and any consequence relying on it) so that the complexity budget is explicitly on the signed divisor of the quotient after cancellation, or by supplying a separate argument that justifies the stronger pairwise claim.