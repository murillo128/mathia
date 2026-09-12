# MI-017 — First-shell exact cells can be replaced by graded CRT progression sums at subpower cost

**Evidence level:** supported by the exact CRT, incidence-cell, and Boolean-transform reductions MC-228--MC-232; no new Möbius cancellation estimate is claimed.

For the first square-defect shell, MC-228--MC-229 show that high incidence is cheap by support. MC-230 then gives a sufficient diagonal target in terms of exact incidence cells `C_S`, while MC-231 shows that the difficult sign geometry is already present at incidence one and cannot be removed by a cheap same-cell divisibility involution.

MC-232 changes the useful representation of that target. Define the upper Boolean zeta transform

\[
B_S=\sum_{U\supseteq S}C_U.
\]

After decomposing the weighted energies coordinatewise, the Boolean transform and its inverse have squared `ell^2` condition factor

\[
\kappa^{m_y-1},\qquad \kappa=\frac{3+\sqrt5}{2},
\]

where `m_y=O(log X/loglog X)`. Hence `\kappa^{m_y}=X^{o(1)}`: at fixed-power resolution the exact-cell energy and the partial-intersection energy are equivalent. The exclusions defining “exactly this incidence set” are therefore not power-essential inside the diagonal route.

The arithmetic payoff is exact. For `Q_S=prod_(d in S)d^2`, each partial intersection is the single source-selected affine sum

\[
B_S(X)=
\sum_{\substack{P/Q_S<k\le X/Q_S\\(k,P)=1}}
\mu(kQ_S-P).
\]

Thus the hard object is no longer an exact-cell combinatorial mask. It is a sparse family of Möbius sums with moving coefficient `Q_S`, common primorial source `P`, and roughness condition `(k,P)=1`.

The cancellation bill is graded by incidence depth. If

\[
|S|=(\alpha+o(1))\frac{\log X}{\log\log X},
\qquad 0\le\alpha<\frac14,
\]

then `Q_S=X^{2\alpha+o(1)}` and the lifted interval length is `L_S=X^{1-2\alpha+o(1)}`. A sufficient uniform target is still

\[
|B_S(X)|\le X^{1/2+o(1)},
\]

so the missing gain over trivial support is `X^{1/2-2\alpha+o(1)}`. The bottom levels are genuine square-root-in-`X` problems; the required cancellation weakens continuously and becomes support-trivial at `\alpha=1/4`.

This refines the MC-231 obstruction rather than contradicting it. Same-cell multiplicative pairing is ineffective, but Boolean inversion shows that the stronger diagonalized route can be attacked through additive/bilinear/harmonic structure of the clean CRT lifts without preserving exact-cell membership pointwise.

**Boundary.** The Boolean equivalence is between two sufficient diagonal energies, not between either of them and the original shell energy `W_y`. Cross-cell cancellation may still help the original problem. MC-232 also proves no bound for deterministic Möbius on the affine family; it only identifies the exponent-resolved target that a source theorem must cross.