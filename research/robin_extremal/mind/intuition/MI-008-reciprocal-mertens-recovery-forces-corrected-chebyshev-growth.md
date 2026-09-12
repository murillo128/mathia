# MI-008 — Robin's two late Lyapunov coordinates are one transport measure, and long fans force its two moments onto complementary power fronts

**Evidence level:** exact on sufficiently late common positive rightmost CA fans through RE-080 under the stated false-RH/long-same-block hypotheses. No contradiction with false RH, exclusion of long fans, or source-specific impossibility of the forced transport profile is proved.

RE-076 makes corrected Chebyshev `Hhat(C,b)=Z_b(C)-log rad(C)` strictly increasing along the late positive rightmost fan. RE-078 makes fringe-corrected logarithmic Mertens `Ehat(C,b)=E_l(Z_b(C))-delta_l(Z_b(C))` strictly decreasing.

RE-079 identifies the dependence hidden behind those opposite monotonicities. For any ordered selected fan segment there is one canonical positive finite measure `mu` supported on the selector interval such that

`Delta Hhat = int 1 dmu`

and

`-Delta Ehat + B_1 = int (1/(s log s)) dmu`.

The first-layer birth correction `B_1` is the sole structural mismatch and has summable late tail. On bounded selector dilation the two corrected increments are therefore equivalent after the natural `Z log Z` scaling; they are not independent source capacities.

RE-080 asks what happens when the same selected block persists across a threshold interval while its selected logarithmic sizes stretch by `r=Y_1/Y_0->infinity`. The convex-envelope inequalities force the endpoint height ratio, and the pointwise shadows of the two RE-079 moments then force

`W/M` between the power scales `r^(b_0-1)/(Y_0 log Y_1)` and `r^(b_1-1)/(Y_0 log Y_1)`.

Equivalently the unique effective selector defined by `1/(Z_eff log Z_eff)=W/M` must lie in the intermediate window

`Z_0 r^(1-b_1-o(1)) <= Z_eff <= Z_0 r^(1-b_0+o(1))`.

The result is stronger than a barycenter location. For every fixed small `epsilon>0`, the fraction of **unweighted** transport mass below `Z_0 r^(1-b_1-epsilon)` tends to zero at a power rate, while the fraction of the **kernel-weighted** moment remaining above `Z_0 r^(1-b_0+epsilon)` also tends to zero. A long false-RH same-block fan therefore requires complementary moving transport fronts at the exponent `1-b`.

This turns “control the scale distribution of `mu`” into a concrete source test. An abstract positive measure can satisfy these inequalities, so positivity and moment matching alone are exhausted. The next leverage must show that actual ordinary-prime event geometry cannot realize the required front motion, or must independently rule out the long-stretch same-block branch. Bounded-stretch fans remain a separate regime.

**Boundary.** RE-080 assumes an infinite long-same-block family with `r->infinity`; it does not prove such a family must occur under false RH. It does not contradict the existence of an abstract positive `mu`, control event counts/ranks, or make the first-layer correction vanish locally. Its gain is a quantitative localization theorem for the one transport ledger left by RE-079.
