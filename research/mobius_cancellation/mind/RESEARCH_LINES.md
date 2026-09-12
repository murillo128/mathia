# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Prove quantitative near-balance on the reduced progressions exposed by the first-shell lift

**Linked intuitions:** `MI-013-bost-connes-regularity-needs-an-intermediate-transverse-category`, `MI-014-centered-parity-and-zero-mode-are-separate-currencies`, `MI-015-sign-support-covariance-gives-a-conditioned-quadratic-bridge`, `MI-016-source-aligned-shifts-face-a-defect-or-mertens-dichotomy`, `MI-017-first-shell-crt-common-mode-is-a-source-coupled-energy-coordinate`.

MC-188--MC-227 show that residue phases are gauge, fixed square-free Hamming degrees form an alternating cascade, and GRH-strength progression bounds are sufficient but too strong; sparse exceptions, generic large-sieve/BDH estimates, and fiberwise control lose the source-selected coupling.

MC-228--MC-233 localize and simplify the first-shell obstruction. High incidence is support-harmless, Boolean inversion removes exact-cell conditioning at `X^{o(1)}` cost, and logarithmic smooth inversion removes the primorial roughness mask at `X^{o(1)}` multiplicity. The hard object is a sparse, source-coupled family of ordinary reduced-residue Möbius progression sums

\[
M_\mu(Z;q,a),
\qquad q=X^{2\alpha+o(1)},
\qquad Z=X^{1-\beta+o(1)}.
\]

Support closes `2\alpha+\beta\ge1/2`. In the strict hard region `2\alpha+\beta<1/2`, the componentwise sufficient target still needs fixed-power cancellation `1/2-2\alpha-\beta`.

MC-234 removes a weaker apparent bottleneck. The 2026 Matomäki--Teräväinen Linnik theorem for multiplicative functions gives both Möbius signs in every reduced class by `q^{2+\varepsilon}`. A CRT amplification yields, for each sign and every fixed interior hard scaling pair,

\[
N_\pm(Z;q,a)\ge \frac{Z^{1/2-\eta}}q.
\]

But the square-free support has size `(6/\pi^2+o(1))Z/q`, so this guaranteed sign population is still a vanishing fraction. The target `|M_\mu(Z;q,a)|\le X^{1/2+o(1)}` requires near-balance with relative sign bias at most

\[
X^{-(1/2-2\alpha-\beta)+o(1)}.
\]

The live problem is therefore **amplitude balance, not parity existence**. A promising use of the recent prior art must extract a quantitative signed-count/discrepancy statement from the multiplicative dense-model proof before its final existence corollary, or exploit cancellation across the subpower family of smooth dilations. Reusing only the `q^{2+o(1)}` representative bound cannot change the fixed-power ledger.

## Treat gauge, support, Boolean conditioning, smooth inversion, parity existence, and source amplitude as separate gates

High incidence is cheap by support. Exact-cell membership and the Boolean transform cost only `X^{o(1)}`. At logarithmic smoothness, the primorial coprimality mask also unfolds into only `X^{o(1)}` ordinary progression sums. MC-234 further shows that both Möbius signs already occur abundantly enough to cross the qualitative parity barrier throughout the strict hard region.

None of these reductions supplies the near-balance demanded by the source-selected amplitude. MC-233 remains only a sufficient componentwise reduction: triangle inequality can discard cancellation between smooth dilations, and the `d=1` term keeps the low-incidence source problem genuinely hard. Future progress must therefore be credited to a quantitative signed estimate for the selected progression family or to controlled aggregate cancellation, not to further removal of subpower masks or additional sign-existence theorems.