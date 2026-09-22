# MI-057 — Signed band drift is a positive Mertens scale average, not a block-population observable

**Evidence level:** exact signed-band identity and Abel-summation reduction from [FD-264](../../findings/FD-264-signed-band-drift-collapses-block-population-to-a-positive-mertens-scale-average.md), refining the amplitude-density frontier of MI-056/FD-263.

For the canonical full-grid inverse, the divisor-band replication count

`m_x(q)=floor(2x/q)-floor(x/q)`

has the exact nearest-integer form

`m_x(q)=floor(x/q+1/2)`.

Hence the jumps `w_x(q)=m_x(q)-m_x(q+1)` are nonnegative and sum to `x`. After summation by parts, the signed repair drift over `x<d<=2x` is therefore

`sum c_d = (x/2)(P_x R_N - P_x[M(N·)])`,

where `P_x` is the probability average with weights `w_x(q)/x`. For rounded full-grid flattening, `|R_N(q)|<=1`, so the signed band total is controlled by a normalized positive average of Mertens prefix values.

This destroys the block-population resource that survives in the absolute ledger of FD-263. In particular `w_x(q)=0` for `x<=q<2x` and `w_x(2x)=1`: the entire deepest interval telescopes in the signed aggregate. Many same-amplitude deep blocks can therefore create large `l^1` repair mass while contributing only their net endpoint drift to the band mean.

At divisor depth `D`, if `max_(q<=2D)|M(qN)| <= A_N D^(delta+o(1))`, the signed drift is at most `A_N D^(1+delta+o(1))+O(D)`. It can reach the FD-261 general positive-capacity threshold only if `delta>1-beta`, where `beta=log_2(3/2)`. **Block density alone cannot supply the missing exponent.**

The remaining full-grid arithmetic route is therefore intrinsically one-sided or variation-sensitive. To exploit the FD-263 population mechanism one must force `sum(-c_d)_+` or comparable within-band `l^1` mass to be much larger than the negative part of the signed band sum. A theorem about a negative band mean, even one produced by many large consecutive Mertens blocks, is structurally too compressed unless the amplitude itself crosses the stronger power threshold.

This is a useful audit distinction: the replication ledger is the correct observable before sign cancellation, while the signed mean is a probability-normalized quotient of that ledger. Any proposed source theorem must state which of those two currencies it actually controls.

**Boundary.** FD-264 does not bound the one-sided repair mass from above, does not refute the FD-263 amplitude-density escape, and does not prove a new Mertens estimate. It only shows that population information is lost after signed aggregation; the surviving one-sided/`l^1` source theorem remains open.