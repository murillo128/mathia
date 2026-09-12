# MI-017 — First-shell reduction exposes a two-parameter Möbius amplitude gap beyond parity existence

**Evidence level:** supported by the exact CRT, Boolean-transform, smooth-inversion, and sign-population analyses MC-228--MC-234; no new square-root Möbius progression bound is claimed.

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

MC-234 calibrates what modern parity-breaking prior art actually buys on this exact family. Matomäki--Teräväinen's Linnik-scale Möbius theorem places each sign in every reduced class by `q^{2+\varepsilon}`. In every fixed interior hard pair `2\alpha+\beta<1/2`, a CRT refinement forces

\[
N_\pm(Z;q,a)\ge Z^{1/2-\eta}/q.
\]

So **existence of both signs is not the remaining obstruction**. The same progression contains `(6/\pi^2+o(1))Z/q` square-free terms, while the desired amplitude bound would require the two signs to be nearly balanced:

\[
\frac{|N_+-N_-|}{N_{\rm sf}}
\le X^{-(1/2-2\alpha-\beta)+o(1)}.
\]

The exponent deficit is therefore an amplitude/near-balance budget, not a parity-existence budget. A theorem can be qualitatively strong enough to break parity in every selected class and still be polynomially too weak for the first-shell energy.

This remains a componentwise sufficient reduction rather than an equivalence. Cancellation among smooth dilations could bypass individual near-balance estimates. The two legitimate routes are therefore precise: prove signed discrepancy on the source-selected progression family at the required deficit, or exploit coherent cancellation across the `X^{o(1)}` dilation family. Further support-mask simplification or representative-existence bounds do not pay the missing power.

**Boundary.** MC-234 uses the published Linnik-type theorem only at its stated sign-existence level and does not rule out stronger quantitative information inside its dense-model proof. Boundary scalings where `1/2-2\alpha-\beta` tends to zero need separate uniformity. No Mertens/RH consequence is proved.