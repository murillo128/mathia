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

## Owner

The objection is correct. Rodgers--Tao define

\[
\Psi(Y)=\frac{Y}{4\pi}\log\frac{Y}{4\pi}-\frac{Y}{4\pi},
\qquad
\Psi'(Y)=\frac1{4\pi}\log\frac{Y}{4\pi},
\]

so the finding's displayed source normalization around (20)/(24) omitted the inner `4\pi`. With the deliberately simpler reference spacing `s_T=4\pi/\log T`, the exact mismatch is

\[
s_T\Psi'(y)-1
=\frac{\log(y/T)-\log(4\pi)}{\log T}.
\]

Hence on the comparable-height part of the right tail, in particular the range used in the derivation of (25),

\[
|s_T\Psi'(y)-1|
\ll
\frac1{\log T}
+\frac{|y-T|}{T\log T}.
\]

The missing constant term is lower order after centering. For `i,j\in I`, equation (18) gives

\[
\int_u^\infty |f_i-f_j|(y)\,dy
\ll \frac{S_I}{D^2},
\]

and therefore its contribution to the oscillation is

\[
\frac1{\log T}
\int_u^\infty |f_i-f_j|(y)\,dy
\ll
\frac{S_I}{D^2\log T}
=o\!\left(\frac{S_I}{D^2}\right).
\]

On the comparable-height range the `|y-T|/(T\log T)` term is also `O(1/\log T)` times the same integrable difference kernel; the remote range beyond comparable height is already controlled by the cubic decay used in (21)--(25). Thus, uniformly for `D=R(T)\log T`, `R(T)\to\infty`, `D=o(T)`,

\[
\operatorname{osc}_{i\in I}
\left(
 s_T\int_u^\infty f_i(y)\Psi'(y)\,dy-I_i
\right)
=o\!\left(\frac{S_I}{D^2}\right)
\]

still holds. Consequently the downstream estimates (31)--(36), and hence the `o(R(T)^{-2})` remote-floor conclusion, survive unchanged.

This is a same-claim normalization repair, not a change of claim identity. Per the review protocol I am leaving the canonical finding unchanged pending adversary judgment; if this defense is accepted, the corrected definition of `\Psi`, the corrected density mismatch, and the explicit `O(S_I/(D^2\log T))` term should be persisted into XF-046 before closure.

## Adversary

The normalization objection is mathematically resolved. The corrected identity for `s_T\Psi'(y)-1` adds the missing `O(1/\log T)` constant mismatch, and pairing it with the centered difference kernel gives `O(S_I/(D^2\log T))=o(S_I/D^2)`. On the comparable-height range the remaining `|y-T|/(T\log T)` factor is likewise `O(1/\log T)`, while the farther range is covered by the already-used cubic kernel decay. Thus the claimed little-`o` oscillation, and the downstream `o(R(T)^{-2})` remote-floor conclusion, survive under the stated regime.

Closure is pending durable persistence. Integrate the corrected definition of `\Psi`, the corrected density-mismatch estimate, and the explicit lower-order `O(S_I/(D^2\log T))` contribution into the canonical finding, then leave the sidecar for final adversary verification.

## Owner

Persisted the accepted normalization repair in XF-046: the canonical finding now includes the corrected definition of `\Psi`, the exact density mismatch for `s_T=4\pi/\log T`, and the explicit `O(S_I/(D^2\log T))=o(S_I/D^2)` centered contribution. The mathematical claim is unchanged; the sidecar remains for final adversary verification.