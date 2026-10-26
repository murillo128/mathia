# MI-068 — Empirical energy controls prime pole tests with quarter-power random starts

**Evidence level:** supported conditional synthesis of [PL-482](../../findings/PL-482-small-empirical-energy-permits-quarter-power-prime-observations.md). The finite concentration lemma is classical and inherited from MC-537; no prime energy estimate, full second-moment recovery or external novelty is asserted.

Fix `a_n=Lambda(n)1_(n=1 mod 5)`, `S_L(j)=sum_(j<n<=j+L)a_n`, integer `X>=40`, `L_1=floor(X/20)` and `L_2=floor(sqrt(2)L_1)`. In each channel take `2q`, `q=ceil(X^(1/4))`, independent uniform starts from `{X,...,2X-1}`, with replacement and retained multiplicities. Let `V_i` be the average squared deviation from that channel's own sample mean. Use the product sampling law across channels and integer scales, independently of the fixed source.

The transferable statistic is population mean absolute dispersion,

`D_i=X^(-2)sum_(j,k)|S_(L_i)(j)-S_(L_i)(k)|`,

rather than the population variance. Nonnegative coefficients give the exact jump bound `|Delta S_L|<=log(3X)`, including prime powers and windows crossing `2X`. PL-482's finite bound for a population with jump bound `A` is

`D <= (4+16t/sqrt(q))sqrt(V)+8AXt^2/q^2+16At/q`

outside probability `3 exp(-t)`. With `t=4log X`, both channels therefore satisfy

`D_i << sqrt(V_i)+sqrt(X)(log X)^3`

on one probability-one event at every sufficiently large integer scale. The extra prime logarithm enters through `A`; it changes no sample-count exponent. This is an event for the fixed source, not one uniform over sources chosen after sampling.

Every bounded mean-zero cell-weight vector satisfies `|L_i^(-1)sum_j w_j S_(L_i)(j)|<=||w||_infinity XD_i/L_i`. Thus the event simultaneously controls the paired-box pole tests from [MI-067](MI-067-two-box-lengths-recover-smooth-pole-tests-at-macroscopic-scale.md), with no union over zeros or test choices. A zero `rho=beta+i gamma`, `beta>1/2`, of zeta or one of the three primitive nonprincipal mod-5 functions forces

`sqrt(V_1)+sqrt(V_2)+sqrt(X)(log X)^3 >= c_rho X^beta`.

The isolated prime signal is `-w_rho X^rho+O(X^sigma_0)`, `sigma_0<beta`, `w_rho=(1/4)sum_chi m_chi(rho)>0`; coincident zeros add their weights. Multiple zeros still produce simple logarithmic-derivative poles. The reciprocal-zeta multiplicity logarithm must not be imported from Möbius. Integer rounding of the second length costs `O(log X)` in the complete pairing, already dominated here.

On the probability-one event, existence of one unbounded integer scale set, common to both channels and fixed before epsilon, with `V_i<<_epsilon X^(1+epsilon)` for every epsilon is equivalent to joint GRH for these four functions. The set can depend on the observations. The separate converse uses `psi(x;5,1)=x/4+O(sqrt(x)log^2(3x))`: center at `L_i/4` to bound every sampled value, then minimize over centers. It holds for every sample outcome and does not infer a sparse estimate from a full mean square.

Neither empirical centering nor fewer observations weakens the arithmetic ceiling. A generic fixed tent is missed below the quarter-power exponent, but it need not be a prime-window source. The stronger fixed square-free multiplicative control in [Möbius MI-104](../../../mobius_cancellation/mind/intuition/MI-104-small-random-sample-energy-controls-dispersion-but-subquarter-multiplicative-bridges-survive.md) has signed coefficients and likewise is not a positive prime-source lower bound. The exact transferable recovery and the source-class boundary are retained in [global MI-040](../../../mind/intuition/MI-040-paired-box-inversion-transports-trimmed-mobius-pole-tests.md).
