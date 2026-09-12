# MI-004 — Bounded CA packets split into negative source charge, sparse fringe charge, and charge-silent first-layer takeover

**Evidence level:** supported by exact bounded-packet charge/successor geometry RE-060--RE-064, the growing-depth capacity theorem RE-065, the signed interruption theorem RE-066, and the first-layer-only refinement RE-067; no global Robin contradiction is claimed.

Inside a fixed CA support chamber, RE-059 shows that endpoint-corrected standard and reciprocal prime sources are frozen. RE-060--RE-062 identify where new source information enters and give the layer-uniform bounded-packet charge law

\[
Q=-\sum_i\frac1{j_i}+\chi_+-\chi_-+o(1).
\]

RE-063--RE-064 collapse extended bounded near-zero behavior to fringe-free `0 -> 0` packets whose higher-layer depths diverge. RE-065 then prices that escape globally: higher-layer event occurrences of growing depth have only `T^{o(1)}` capacity on polynomial windows. A polynomial-span strong-off-critical fan must therefore contain polynomially many interruptions to the quiet bounded regime unless the fan itself stretches superpolynomially.

RE-066 adds the source-bearing sign asymmetry. A bounded source-bearing packet with `Q>=epsilon>0` must be a `0 -> 1` fringe transition. Its upper state is one of the base-two fringe hosts and these hosts are multiplicatively lacunary, so positive bounded charges contribute only `O(log T)` events up to scale `T`. If the next switch remains bounded and source-bearing, the same fringe persists and the successor must be `1 -> 0`, forcing `Q_next<=-1+o(1)`.

RE-067 now resolves the source-free bounded branch instead of leaving every first-layer-only packet in one structural bucket. If every crossed physical event has depth one, the higher-layer sum is empty and the exact packet identity becomes

\[
Q=\chi_+-\chi_-+o(1).
\]

Because bounded packets cannot have fringe at both endpoints, the only classes are

\[
0\to0:\ Q=o(1),\qquad
0\to1:\ Q=1+o(1),\qquad
1\to0:\ Q=-1+o(1).
\]

Every nonzero first-layer-only charge touches the same lacunary fringe-host set, so both signs together contribute only `O(log T)` switches. The scalable first-layer escape is therefore not an uncontrolled signed ledger: it is a **matched `0 -> 0` packet whose leading selected-residual charge cancels completely**.

Combining RE-065--RE-067 yields the sharper polynomial-span ledger

\[
U_B+F_B^{00}+N^-_{\ge2,B}\ge X_B^{\delta-o(1)}.
\]

The three terms are genuinely different currencies: `U_B` is unbounded packet complexity beyond the fixed-cardinality law, `F_B^{00}` is bounded first-layer-only charge-silent takeover, and `N^-_{\ge2,B}` is genuinely negative higher-layer source-bearing charge. Positive bounded charge and nonzero first-layer-only charge are too sparse to carry polynomial complexity.

The useful next theorem should therefore control **one of those three live currencies**. In particular, a charge-summing argument alone cannot see `F_B^{00}` at leading order; it needs another statistic or an independent rigidity theorem preventing polynomially many matched first-layer packets. Negative events also cannot be telescoped for free because the residual threshold and normalization move between exposed states.

**Boundary.** RE-067 still assumes a fixed packet-cardinality bound for the first-layer charge law and does not show that `F_B^{00}` is sparse. Unbounded packets remain separate, and the strong polynomial ledger lives only in the strong off-critical chamber inherited from RE-065. The result narrows the interruption architecture; it is not yet a contradiction.