# MI-004 — Bounded near-zero CA packets have subpolynomial deep-layer capacity on polynomial windows

**Evidence level:** supported by exact bounded-packet charge/successor geometry RE-060--RE-064 and the growing-depth event-capacity theorem RE-065; the remaining interruption alternatives and superpolynomial-span escape are open.

Inside a fixed CA support chamber, RE-059 shows that endpoint-corrected standard and reciprocal prime sources are frozen. RE-060--RE-062 identify where new source information enters and classify bounded packets whose normalized higher-layer charge can vanish. For higher-layer depths `j_i`, the leading charge is

\[
-\sum_i\frac1{j_i}+\chi_+-\chi_-.
\]

RE-063--RE-064 use the source geometry of nonzero fringe bits and deep base-two successors to collapse the bounded near-zero catalogue. Double-fringe bounded packets are eventually impossible, and a `0->1` Egyptian cancellation cannot recur inside a bounded near-zero run because the next bounded switch incurs an order-one negative rebound. Extended bounded near-zero behavior therefore has one surviving local architecture:

\[
\chi_- = \chi_+ =0,
\qquad \min_i j_i\to\infty.
\]

RE-065 now prices the **global capacity** of that escape. Let `M_(>=r)(T)` count higher-layer event occurrences with depth at least `r` up to event scale `T`. Uniformly in `r>=2`,

\[
M_{\ge r}(T)
\le
\log_2\!\left(\frac{T\log T}{\log2}\right)
\left(\frac{T\log T}{\log2}\right)^{1/r}.
\]

Hence every growing depth cutoff `r(T)->infinity` has only

\[
M_{\ge r(T)}(T)=T^{o(1)}
\]

capacity. A bounded source-bearing packet whose charge tends to zero is forced by RE-064 into precisely such growing depths. Therefore a consecutive bounded near-zero-charge run whose endpoint scales stay in any polynomial window `X<=Y<=X^A` has length only

\[
L_X=X^{o(1)}.
\]

This is the key splice: **vanishing charge forces deeper genuine prime-power events, but those events become subpolynomially scarce on every polynomial physical-scale window**. In the strong off-critical fan of RE-051, which requires polynomially many exposed switches, a polynomial-span fan must therefore contain polynomially many interruptions to the quiet bounded deep-layer regime. Each interruption has at least one explicit form: packet cardinality exceeds the fixed bound, the packet is first-layer-only, or its normalized charge does not vanish.

The old surviving “fringe-free deep layers” branch is thus no longer a plausible single long bounded explanation of a polynomial fan. The global escape map is now discrete: **unbounded packet complexity, first-layer takeover, nonvanishing-charge interruptions, or superpolynomial physical fan stretch**. The last escape is genuine because RE-065 does not prove the fan lives inside any fixed polynomial span.

The useful next theorem should attack one of these alternatives on the actual false-RH exposed sequence, rather than refine the bounded reciprocal-depth catalogue. In particular, a polynomial-span theorem would immediately force polynomially many nonquiet events, after which their charge/sign contribution becomes the natural target; conversely a superpolynomial-span mechanism must be reconciled with the older block-stretch geometry.

**Boundary.** RE-065 is a capacity obstruction, not a sign contradiction. It assumes bounded packet cardinality for the quiet-run estimate, does not control first-layer-only packets, and does not exclude superpolynomial span. Polynomially many interruptions need not all have large charge.