# Möbius-cancellation research lines

This file holds the current mathematical questions suggested by the durable Möbius-cancellation intuitions. It is not a roadmap, task queue, status page, or history.

## Prove the graded reduced-progression Möbius bounds exposed by the first-shell lift

**Linked intuitions:** `MI-013-bost-connes-regularity-needs-an-intermediate-transverse-category`, `MI-014-centered-parity-and-zero-mode-are-separate-currencies`, `MI-015-sign-support-covariance-gives-a-conditioned-quadratic-bridge`, `MI-016-source-aligned-shifts-face-a-defect-or-mertens-dichotomy`, `MI-017-first-shell-crt-common-mode-is-a-source-coupled-energy-coordinate`.

MC-188--MC-227 show that residue phases are gauge, fixed square-free Hamming degrees form an alternating cascade, and GRH-strength progression bounds are sufficient but too strong; sparse exceptions, generic large-sieve/BDH estimates, and fiberwise control lose the source-selected coupling.

MC-228--MC-231 localize the first-shell obstruction to low/mesoscopic incidence. High incidence is support-harmless, exact-cell diagonalization is sufficient at fixed-power resolution, and singleton cells already carry near-full unsigned mass. Naive same-cell divisibility pairing reaches only a vanishing part of that singleton support.

MC-232 removes exact-incidence exclusions at only `X^{o(1)}` condition cost by Boolean Möbius inversion. MC-233 removes the remaining primorial roughness mask at the same fixed-power resolution. With `Q_S=prod_(r in S)r^2`, the partial-intersection coordinate has the exact decomposition

\[
B_S(X)=
\sum_{\substack{d\le T\\P^+(d)\le y}}
M_\mu\!\left(T/d;Q_S,-Pd^{-1}\bmod Q_S\right),
\]

and at the logarithmic cutoff `y=c log X` there are only `X^{o(1)}` smooth dilation parameters. The hard object is therefore a sparse, source-coupled family of **ordinary reduced-residue Möbius progression sums**, not an exact-cell or roughness mask.

At incidence depth

\[
|S|=(\alpha+o(1))\frac{\log X}{\log\log X}
\]

and smooth dilation scale `d=X^{\beta+o(1)}`, the progression occupancy is `X^{1-2\alpha-\beta+o(1)}` while the sufficient amplitude target remains `X^{1/2+o(1)}`. The fixed-power deficit is therefore

\[
\max(0,\tfrac12-2\alpha-\beta).
\]

Support alone closes the region `2\alpha+\beta\ge1/2`; genuine cancellation is needed only below that boundary, with the hardest corner at simultaneously small incidence and small smooth dilation. The next theorem should attack this two-parameter surface directly, uniformly or in the weighted aggregate. A generic logarithmic saving cannot cross the bottom-left fixed-power gap, while square-root cancellation in every component is stronger than necessary.

## Treat gauge, support, Boolean conditioning, smooth inversion, and source cancellation as separate gates

High incidence is cheap by support. Exact-cell membership and the Boolean transform cost only `X^{o(1)}`. At logarithmic smoothness, the primorial coprimality mask also unfolds into only `X^{o(1)}` ordinary progression sums. None of these representation reductions supplies the missing cancellation.

MC-233 is deliberately only a sufficient componentwise reduction: triangle inequality can discard cancellation between smooth dilations, and the `d=1` term keeps the low-incidence source problem genuinely hard. Future progress must therefore be credited to an actual estimate for the source-selected progression family or to controlled cancellation across its smooth-dilation components, not to further removal of already-subpower masks.