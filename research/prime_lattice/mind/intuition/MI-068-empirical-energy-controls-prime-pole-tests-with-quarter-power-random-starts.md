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

Neither empirical centering nor fewer observations supplies the arithmetic ceiling. [PL-483](../../findings/PL-483-fixed-prime-supported-sources-evade-subquarter-uniform-observations.md) does put the hidden-area mechanism on actual prime support. For any fixed nonzero `phi in C_c^1((4/3,5/3);C)`, `0<=alpha<1/4` and `3/4<kappa<1-alpha`, there are two deterministic infinite sources, fixed before sampling, with

`a_n/2 <= b_n^+ , b_n^- <= 3a_n/2`,

equal to `a_n` except at primes `n=1 mod 5`, and with cumulative sums `psi(x;5,1)+O(x^kappa)=x/4+o(x)`. At scales `X_k=4^k`, couple their `2ceil(X_k^alpha)` uniform starts per channel with those of `a`. Almost surely all sampled window values eventually coincide exactly, but

`|sum_n (b_n^+-b_n^-)phi(n/X_k)| asymp X_k^(2kappa-1) > X_k^(1/2)`

in the sense of a strict exponent gap. The construction may also use a mean-zero `phi`.

The primitive is one balanced packet per scale. PNT and pigeonholing select a cell of width `B=floor(X^kappa)` with prime capacity `W asymp B`; a sieve upper bound prevents that capacity from concentrating at one point. For cumulative capacity `C_j`, set `F_j=min(C_j,W-C_j)`, zero outside the cell. Its exact median identity gives `sum_j F_j=min_z sum_n c_n|n-z| asymp B^2`, with `c_p=(log p)/2`. Set `b_n^+-a_n=a_n-b_n^-=F_n-F_(n-1)`. A fixed derivative-phase interval turns this area into signed target separation `asymp B^2/X`. Windows see only `F_(j+L)-F_j`, so the two channels miss the packet unless a start enters one of three translated cells. The hit probability is `O(X^(alpha+kappa-1))`, summable on `4^k`. Completed packets have zero mass, allowing a single fixed source pair with the stated PNT.

This rules out square-root signed recovery from those samples uniformly over positive bounded reweightings of the prime source. Their common empirical energy is exactly the baseline's, **with no proved ceiling**. The result neither proves a necessary sample exponent for the exact Mangoldt sequence nor covers adaptive or accumulated cross-scale observations. Its coefficients also need not retain canonical Euler factors or the noncancelling pole formula. The signed multiplicative control in [Möbius MI-104](../../../mobius_cancellation/mind/intuition/MI-104-small-random-sample-energy-controls-dispersion-but-subquarter-multiplicative-bridges-survive.md) does supply small energy in its own different source class. [Global MI-040](../../../mind/intuition/MI-040-paired-box-inversion-transports-trimmed-mobius-pole-tests.md) keeps this distinction and the scale-coverage alternative explicit.
