# MI-004 — Bounded CA packets have a one-sided signed interruption ledger

**Evidence level:** supported by exact bounded-packet charge/successor geometry RE-060--RE-064, the growing-depth capacity theorem RE-065, and the signed interruption theorem RE-066; no global Robin contradiction is claimed.

Inside a fixed CA support chamber, RE-059 shows that endpoint-corrected standard and reciprocal prime sources are frozen. RE-060--RE-062 identify where new source information enters and give the layer-uniform bounded-packet charge law

\[
Q=-\sum_i\frac1{j_i}+\chi_+-\chi_-+o(1).
\]

RE-063--RE-064 collapse extended bounded near-zero behavior to fringe-free `0 -> 0` packets whose higher-layer depths diverge. RE-065 then prices that escape globally: higher-layer event occurrences of growing depth have only `T^{o(1)}` capacity on polynomial windows. A polynomial-span strong-off-critical fan must therefore contain polynomially many interruptions to the quiet bounded regime unless the fan itself stretches superpolynomially.

RE-066 adds the missing **sign asymmetry**. A bounded source-bearing packet with `Q>=epsilon>0` must be a `0 -> 1` fringe transition. Its upper state is one of the base-two fringe hosts and these hosts are multiplicatively lacunary, so positive bounded charges contribute only `O(log T)` events up to scale `T`. If the next switch remains bounded and source-bearing, the same fringe persists and the successor must be `1 -> 0`, forcing

\[
Q_{\rm next}\le -1+o(1).
\]

Positive bounded charge is therefore not a scalable interruption currency: it is sparse and creates an immediate negative debt whenever the fan stays in the same bounded source-bearing category.

Combining this with RE-065 yields a polynomial-span ledger. If `H_B` counts packets that are either larger than the fixed cardinality bound or contain no higher-layer source event, and `N_B^-` counts the remaining bounded source-bearing switches with genuinely negative normalized charge, then

\[
H_B+N_B^-\ge X_B^{\delta-o(1)}.
\]

The surviving alternatives are now **structural interruption, negative signed charge, or superpolynomial physical stretch**. The sign-symmetric “many positive or negative nonquiet events” picture is no longer faithful to the source geometry.

The useful next theorem should therefore control `H_B` or the aggregate effect of the negative branch. A charge-summing argument must also control the continuous residual drift and changing normalization between consecutive exposed thresholds; the negative events cannot be telescoped for free.

**Boundary.** RE-066 assumes the bounded source-bearing charge law for the charged branch. Unbounded packets and first-layer-only packets remain in `H_B`. The successor debt applies only when the next packet remains bounded and source-bearing. The result is a signed capacity ledger, not yet a contradiction.