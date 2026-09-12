# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Prove signed near-balance on the reduced progressions exposed by the first-shell lift

**Linked intuitions:** `MI-013-bost-connes-regularity-needs-an-intermediate-transverse-category`, `MI-014-centered-parity-and-zero-mode-are-separate-currencies`, `MI-015-sign-support-covariance-gives-a-conditioned-quadratic-bridge`, `MI-016-source-aligned-shifts-face-a-defect-or-mertens-dichotomy`, `MI-017-first-shell-crt-common-mode-is-a-source-coupled-energy-coordinate`.

MC-188--MC-227 show that residue phases are gauge, fixed square-free Hamming degrees form an alternating cascade, and GRH-strength progression bounds are sufficient but too strong; sparse exceptions, generic large-sieve/BDH estimates, and fiberwise control lose the source-selected coupling.

MC-228--MC-233 localize and simplify the first-shell obstruction. High incidence is support-harmless, Boolean inversion removes exact-cell conditioning at `X^{o(1)}` cost, and logarithmic smooth inversion removes the primorial roughness mask at `X^{o(1)}` multiplicity. The hard object is a sparse, source-coupled family of ordinary reduced-residue Möbius progression sums

\[
M_\mu(Z;q,a),
\qquad q=X^{2\alpha+o(1)},
\qquad Z=X^{1-\beta+o(1)}.
\]

Support closes `2\alpha+\beta\ge1/2`. In the strict hard region `2\alpha+\beta<1/2`, the componentwise sufficient target needs fixed-power cancellation `1/2-2\alpha-\beta`.

MC-234 removes qualitative parity existence. MC-235 removes polynomial sign scarcity as well. Retaining the quantitative mass in the Matomäki--Teräväinen dense-model proof and amplifying by CRT gives, for every fixed `\eta>0` and each sign,

\[
N_\pm(Z;q,a)\ge \frac Zq X^{-\eta}
\]

through every fixed interior hard pair. Both signs therefore occupy the progression at the full exponent, while the target still requires relative discrepancy

\[
\frac{|N_+-N_-|}{N_{\rm sf}}
\le X^{-(1/2-2\alpha-\beta)+o(1)}.
\]

The live theorem is now unambiguously **signed comparison/near-balance**, not existence or abundance. A useful use of the dense-model architecture must preserve information comparing the positive and negative masses, rather than merely strengthen separate positive lower bounds. The other surviving route is coherent cancellation across the subpower family of smooth dilations before triangle inequality.

## Treat gauge, support, Boolean conditioning, smooth inversion, sign abundance, and signed amplitude as separate gates

High incidence is cheap by support. Exact-cell membership and the Boolean transform cost only `X^{o(1)}`. At logarithmic smoothness, the primorial coprimality mask unfolds into only `X^{o(1)}` ordinary progression sums. MC-235 further shows that each Möbius sign already has essentially full-exponent abundance in every fixed strict hard component.

None of these reductions supplies the near-balance demanded by the source-selected amplitude. Separate lower bounds on `N_+` and `N_-` can both be almost maximal while their difference stays at trivial power. MC-233 also remains only a sufficient componentwise reduction: triangle inequality can discard cancellation between smooth dilations, and the `d=1` term keeps the low-incidence source problem genuinely hard.

Future progress must therefore be credited to a quantitative **signed** estimate for the selected progression family or to controlled aggregate cancellation, not to further removal of subpower masks, stronger representative-existence theorems, or higher unsigned sign counts.