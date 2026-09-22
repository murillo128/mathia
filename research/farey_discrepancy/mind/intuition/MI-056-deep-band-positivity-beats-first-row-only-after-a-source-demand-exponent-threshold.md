# MI-056 — Deep-band positivity beats the first-row ceiling only after a source-demand exponent threshold

**Evidence level:** exact source-capacity calibration from [FD-261](../../findings/FD-261-deep-band-depletion-needs-superlinear-depth-amplification-to-beat-first-row-ceiling.md), combining the general positive depletion law of MI-054 with the first-row obstruction of MI-055.

Let `beta=log_2(3/2)`. For the scale-adapted positive cushion at divisor depth `D`, FD-260 implies a physical dyadic-band capacity

`P_N(D) << N D^(1-beta)/log N`.

Suppose a future source theorem forces negative repair demand of size `N^(theta-o(1)) D^(alpha-o(1))` on that band, with `D=N^(lambda+o(1))`. The positive-capacity ceiling can contradict that demand only when

`theta + alpha lambda > 1 + (1-beta) lambda`.

This turns the previously qualitative instruction “prove that the actual Mertens repair consumes enough positive slack” into an exponent gate. A demand merely linear in divisor depth (`alpha=1`) becomes contradictory only for `lambda>(1-theta)/beta`, which is strictly later than the independent first-row ceiling `lambda<=1-theta`. To make the general deep-band mechanism decisive no later than that first-row scale, one needs `alpha>2-beta=1.415037...` at the same arithmetic amplitude exponent.

The monotone-response cone is qualitatively different. If the extra structural condition `mu*b>=0` is actually available, FD-259 removes the depth factor from the physical capacity ceiling, leaving `O(N/log N)`. Then a linear-in-depth source demand is already exponent-critical at the first-row scale. Proving such a sign structure can therefore matter more than a small numerical improvement of the general FD-260 kernel exponent.

The durable audit is to compare a proposed source lower bound with the strongest applicable capacity law **before** treating it as progress toward a deeper obstruction. In the general positive cone, a zero-frontier-sized contribution repeated once per depth cell is not enough to beat the first switched row; the missing phenomenon is genuinely superlinear depth amplification or a structural upgrade of the admissible positive cone.

**Boundary.** FD-261 does not prove any lower bound for the canonical Mertens repair, does not show that the physical cushion has monotone divisor response, and does not obstruct the existing subpolynomial-depth construction. The exponent inequalities are necessary strength tests for future lower-bound strategies, not sufficiency or existence statements.