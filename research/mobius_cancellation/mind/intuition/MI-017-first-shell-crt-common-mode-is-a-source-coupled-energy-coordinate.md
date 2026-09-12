# MI-017 — First-shell reduction leaves a signed near-balance gap even after full-exponent sign abundance

**Evidence level:** supported by the exact CRT, Boolean-transform, smooth-inversion, and dense-model sign-population analyses MC-228--MC-235; no square-root Möbius progression bound is claimed.

For the first square-defect shell, MC-228--MC-231 localize the difficult diagonalized target to low/mesoscopic incidence. MC-232 replaces exact incidence cells by their upper Boolean zeta transform at only subpower condition cost. MC-233 then removes the primorial roughness mask algebraically. At logarithmic smoothness,

\[
B_S(X)=
\sum_{\substack{d\le T\\P^+(d)\le y}}
M_\mu\!\left(T/d;Q_S,-Pd^{-1}\bmod Q_S\right),
\qquad Q_S=\prod_{r\in S}r^2,
\]

with only `X^{o(1)}` smooth dilations. Thus neither exact-cell exclusions nor roughness are fixed-power obstructions.

If

\[
|S|=(\alpha+o(1))\frac{\log X}{\log\log X},
\qquad d=X^{\beta+o(1)},
\]

then `Q_S=X^{2\alpha+o(1)}`, `Z=T/d=X^{1-\beta+o(1)}`, and the progression occupancy is `X^{1-2\alpha-\beta+o(1)}`. The sufficient componentwise target remains `X^{1/2+o(1)}`, so the missing fixed-power gain is

\[
\boxed{\max(0,\tfrac12-2\alpha-\beta)}.
\]

MC-234 already showed that parity existence is not the obstruction. MC-235 strengthens this decisively by retaining the quantitative mass in the 2026 Matomäki--Teräväinen Linnik dense-model proof. In every fixed interior hard pair `2\alpha+\beta<1/2` and for each sign,

\[
\boxed{
N_\pm(Z;q,a)\ge \frac Zq X^{-\eta}
}
\]

for every fixed `\eta>0` and all sufficiently large `X`. Each sign therefore has the **full progression occupancy exponent**. No fixed negative-power sparsity of one sign remains available as an explanation of the amplitude gap.

This still gives essentially no signed cancellation. The square-free population is `(6/\pi^2+o(1))Z/q`, and lower bounds of size `(Z/q)X^{-o(1)}` for both signs allow one sign to dominate by almost the entire support. The target instead requires

\[
\frac{|N_+-N_-|}{N_{\rm sf}}
\le X^{-(1/2-2\alpha-\beta)+o(1)}.
\]

Thus **representative abundance and signed balance are different currencies even at the exponent level**. The dense-model proof already spends enough information to populate both signs at full exponent; extracting still more representatives from the same positive lower-bound architecture cannot by itself pay the amplitude deficit. Any useful strengthening must preserve a comparison between the two sign masses, or exploit cancellation when the `X^{o(1)}` smooth-dilation components of MC-233 are recombined before triangle inequality.

The two surviving routes are therefore precise: prove signed discrepancy on the source-selected progression family at the required deficit, or prove coherent aggregate cancellation across the smooth dilations. Support-mask simplification, parity existence, and separate lower bounds for `N_+` and `N_-` are now exhausted as explanations of the missing power.

**Boundary.** MC-235 derives its counting statement from the quantitative lower bound inside the published dense-model proof and is fixed-parameter/interior; moving boundary scalings require renewed uniformity. The reduction remains componentwise sufficient rather than necessary, so aggregate cancellation can still bypass individual near-balance. No Mertens/RH consequence is proved.