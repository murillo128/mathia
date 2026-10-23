# MI-066 — RH Mellin variance excludes balanced near-capacity despite the endpoint barrier

**Evidence level:** supported RH-conditional consequence of [FD-311](../../findings/FD-311-a-quarter-power-sliding-variance-saving-would-close-balanced-capacity.md), [FD-312](../../findings/FD-312-pointwise-mertens-envelopes-cannot-close-sliding-variance-below-source-ceiling.md), and [MC-520](../../../mobius_cancellation/findings/MC-520-rh-mellin-variance-closes-conditional-farey-window-target.md). This concerns the specified balanced block-Mertens branch, not a proof of RH or a closure of every Farey route.

Put `M(t)=sum_(n<=t)mu(n)`, `c=1-log_2(3/2)`, `G_N(d)=sum_(q|d)[M(Nq)-M(N(q-1))]`, and `L_N(x)=sum_(x<d<=2x)|G_N(d)|`. At balanced depth `x=N^(1+o(1))`, near-capacity `L_N(x)>=N^(1/2)x^(1+c-o(1))` forces a carrying shell with integer `X=NQ` and

`J_mu(X,N)=sum_(X<=y<2X)|M(y+N)-M(y)|^2 >= X N^(1/2+3c-o(1))`.

Under RH the shell lies in `N=X^(beta+o(1))`, `1/2<=beta<=1/(1+2c)`. MC-520 supplies, uniformly on all these windows,

`J_mu(X,N) <<_epsilon X^(1+epsilon)N <= X N^(1+2epsilon+o(1))`.

Any fixed `0<epsilon<(3c-1/2)/2` creates a strict power contradiction. For example `epsilon=1/8` leaves exponent gap `3c-3/4=0.495112...`. The exact correspondence is the *same discrete sliding moment on the same selected shell*, with no exceptional-window transfer. The [Möbius mechanism](../../../mobius_cancellation/mind/intuition/MI-100-mellin-differences-retain-the-rh-short-window-variance-gain.md) retains the difference before Mellin Plancherel; it is not a sharper pointwise endpoint envelope.

FD-312's no-go remains intact: writing the shell depth as `Q=x^(rho+o(1))`, RH gives `2c<=rho<=1`. Separate endpoint bounds give at best the balanced saving `eta=1-rho<=1-2c`, below the required `eta>3/2-3c` by `1/2-c`. That is a limitation of the proof operation, while the retained-difference estimate succeeds under the same RH assumption. RH is now used both for shell localization and for the analytic variance bound; it is not merely a geometric localization hypothesis.

FD-311/312's frontier descriptions do not establish that a new variance theorem is needed under RH; MC-520 supplies the explicit derivation and corrects FD-312's weaker Gao report. Their source-reduction and endpoint-barrier formulas survive. No unpublished Gao proof is needed for this implication. The remaining independent question is an unconditional or explicitly weaker-hypothesis estimate on a separately justified shell range; using MC-520 to prove RH would be circular.
