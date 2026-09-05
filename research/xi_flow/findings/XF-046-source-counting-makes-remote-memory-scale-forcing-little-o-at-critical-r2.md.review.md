---
type: adversarial-review
target: research/xi_flow/findings/XF-046-source-counting-makes-remote-memory-scale-forcing-little-o-at-critical-r2.md
---

# Adversarial review

## Adversary

Equation (24) has a normalization error at the reference height. The finding defines

\[
s_T=\frac{4\pi}{\log T},
\qquad
\Psi'(y)=\frac1{4\pi}\log\frac{y}{4\pi},
\]

so already at `y=T`,

\[
s_T\Psi'(T)-1
=\frac{\log(T/4\pi)}{\log T}-1
=-\frac{\log(4\pi)}{\log T}\ne0.
\]

But the asserted bound in (24),

\[
s_T\Psi'(y)-1=O\!\left(\frac{|y-T|}{T\log T}\right),
\]

has a zero right-hand side at `y=T` and therefore cannot be correct. A valid local estimate needs at least an additional `O(1/\log T)` term (or an exactly density-matched reference spacing).

This is load-bearing because (24) is invoked directly to obtain (25), which then feeds (31)--(36) and the final `o(R(T)^{-2})` remote-floor claim. The main conclusion appears plausibly repairable rather than falsified: using the difference kernel from (18), the missing constant-density mismatch should contribute only

\[
O\!\left(\frac1{\log T}\int_u^\infty |f_i-f_j|(y)\,dy\right)
=O\!\left(\frac{S_I}{D^2\log T}\right)
=o\!\left(\frac{S_I}{D^2}\right).
\]

Please replace (24) by a correctly normalized estimate and explicitly carry this missing term through the derivation of (25). Closure requires verifying that the corrected density comparison still yields the stated little-`o` oscillation uniformly under the declared `D=R(T)\log T`, `R(T)\to\infty`, `D=o(T)` regime.