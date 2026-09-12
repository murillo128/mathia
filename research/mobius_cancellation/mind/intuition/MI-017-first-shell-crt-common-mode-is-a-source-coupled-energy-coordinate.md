# MI-017 — First-shell exact cells and roughness masks reduce to a two-parameter family of ordinary Möbius progressions

**Evidence level:** supported by the exact CRT, Boolean-transform, and smooth-inversion reductions MC-228--MC-233; no new Möbius cancellation estimate is claimed.

For the first square-defect shell, MC-228--MC-231 localize the difficult diagonalized target to low/mesoscopic incidence. MC-232 then replaces exact incidence cells by their upper Boolean zeta transform at only subpower condition cost. If

\[
B_S=\sum_{U\supseteq S}C_U,
\]

then the exact-cell and partial-intersection energies are equivalent at fixed-power resolution, and each `B_S` is a single source-selected CRT progression carrying the roughness condition `(n,P)=1`.

MC-233 removes that final support mask algebraically. The logarithmic smooth inverse `g_y=\mu*s_y` gives

\[
B_S(X)=
\sum_{\substack{d\le T\\P^+(d)\le y}}
M_\mu\!\left(T/d;Q_S,-Pd^{-1}\bmod Q_S\right),
\qquad Q_S=\prod_{r\in S}r^2.
\]

Because the smooth primes and shell primes are disjoint, every inner sum is an ordinary reduced-residue Möbius progression at the same modulus `Q_S`. At `y=c\log X`, the number of smooth dilations is only `X^{o(1)}`. Thus neither exact-incidence exclusions nor primorial roughness are fixed-power obstructions for this stronger diagonal route.

The cancellation bill becomes two-dimensional. If

\[
|S|=(\alpha+o(1))\frac{\log X}{\log\log X},
\qquad d=X^{\beta+o(1)},
\]

then `Q_S=X^{2\alpha+o(1)}` and the corresponding progression has natural occupancy `X^{1-2\alpha-\beta+o(1)}`. The sufficient target is still `X^{1/2+o(1)}`, so the missing fixed-power gain is

\[
\boxed{\max(0,\tfrac12-2\alpha-\beta)}.
\]

Support alone handles `2\alpha+\beta\ge1/2`; genuine cancellation is needed below that line. Increasing incidence and increasing smooth dilation are therefore interchangeable only in the **trivial support budget**, not as sources of cancellation. The bottom-left corner `\alpha=\beta=0`, including the `d=1` component, remains a square-root-in-`X` source problem.

This is a representation reduction, not an equivalence component by component. The smooth-dilation decomposition is exact, but bounding it by absolute values can lose cancellation across `d`. A future theorem may control individual source-selected progressions or exploit coherent cancellation among the subpower family; either way it must cross the explicit deficit above rather than merely manipulate support masks.

**Boundary.** The reduction concerns the stronger diagonalized first-shell target, not the original shell energy itself. It proves no estimate for the deterministic Möbius progression family and no Mertens/RH consequence.