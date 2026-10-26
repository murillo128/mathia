# MI-104 — Small random-sample energy controls dispersion; fixed multiplicative bridges survive below quarter power

**Evidence level:** supported conditional recovery from [MC-537](../../findings/MC-537-small-sampled-energy-permits-quarter-power-mobius-observations.md), with the fixed-source obstruction of [MC-538](../../findings/MC-538-one-fixed-multiplicative-source-defeats-subquarter-random-observations.md). The concentration and hidden-area ingredients are classical. Neither result supplies a Möbius energy ceiling or an optimal sample count for Möbius.

For a fixed real population `u_1,...,u_X` with `|Delta u|<=A`, take `2q` independent uniform draws **with replacement**. Retain multiplicities and let `V` be their average squared deviation from their sample mean. Population pair dispersion is

`D=X^(-2) sum_(j,k)|u_j-u_k|`.

For `t>0`, with probability at least `1-3 exp(-t)`, MC-537 proves

`D <= (4+16t/sqrt(q))sqrt(V) + 8AXt^2/q^2 + 16At/q`.

Pairing the draws bounds `D` through their mean absolute difference and the fixed true range `B`; hitting neighborhoods of fixed population extrema then bounds `B` by the sample range plus the jump cost. Substitute that random range bound only after the concentration event. The sample identities are `mean_pair_difference<=2sqrt(V)` and `sample_range<=2sqrt(qV)`. This is why small observed energy improves the recovery bill from unrestricted quadrature accuracy.

For **every** complex weight vector with `sum_j w_j=0`, `|w_j|<=F`, on the same event,

`|L^(-1) sum_j w_j u_j| <= FXD/L`.

Jensen bounds mean absolute deviation about the population mean by `D`; the unknown mean then disappears from the pairing. No population second moment or fitted mean estimate is recovered, and no union over tests is needed.

For Möbius windows `u_j=M(j+L)-M(j)`, `X<=j<2X`, the jump bound is `A=2`. Put `L_1=floor(X/20)`, `L_2=floor(sqrt(2)L_1)`, `q=ceil(X^(1/4))`, and `t=4log X`. Use the product sampling law across channels and integer scales, independently of the fixed source. Summable failures give, almost surely on all sufficiently large integer scales,

`sqrt(V_1)+sqrt(V_2)+sqrt(X)(log X)^2 >= c_rho X^beta(log X)^(m-1)`

for a hypothetical zeta zero `rho=beta+i gamma`, `beta>1/2`, of multiplicity `m`. The lower signal is the existing full-multiplicity reciprocal-zeta pole test composed with the paired-box inverse; sampling only bounds its complete mean-zero pairings. Constants depend on that test and the full zero set, and onset may depend on the sample outcome.

On this probability-one event, RH is equivalent to existence of **one common unbounded integer scale set**, chosen before epsilon varies, on which both `V_i<<_epsilon X^(1+epsilon)` for every epsilon. The set may be selected after the draws because the recovery event already covers every large scale. RH supplies the converse pointwise for every sampling outcome. This is not a finite RH decision procedure.

MC-538 rules out reducing the power using just multiplicativity and exact square-free magnitudes. Fix any nonzero `phi in C_c^1((4/3,5/3);C)`, `0<=alpha<1/4`, and `3/4<kappa<1-alpha`. There exist **one deterministic** multiplicative `f:N->{-1,0,1}`, `|f|=mu^2`, and one deterministic lacunary scale sequence `X_k`, both fixed before the observations, such that

`|sum_n f(n)phi(n/X_k)| >>_phi X_k^(2kappa-1)/(log X_k)^2`,

while `2ceil(X_k^alpha)` independent uniform starts per channel give uncentered average energies `E_i(X_k)<<_epsilon X_k^(1+epsilon)` almost surely for every epsilon. Centered energies are smaller. The target has a fixed power excess over square-root size.

The mechanism is a balanced prime-sign bridge in one cell of width `X_k^kappa`: ordinary PNT plus pigeonholing supplies `m>>X_k^kappa/log X_k` primes; ordered positive then negative signs have primitive area at least `floor(m/2)^2`. A fixed derivative-phase interval makes its smooth signed response at least that area divided by `X_k`. Those primes exceed half the observation horizon, so their composites do not yet occur. The two window channels see the bridge only when a sampled endpoint enters its cell, with probability `O(X_k^(alpha+kappa-1))`.

Old prescribed primes do have composite copies. If there are `r_k` old primes, the random multiplicative background pays the finite second-moment factor `C_k=2^r_k`. Choose the next scale large enough that `C_k` is absorbed by `X_k^(1/k)` and that the background cannot cancel the bridge. A countable union bound fixes one successful global sign assignment; lacunarity makes subsequent endpoint-hit and background-energy failures summable. The observed source does not change with the scale or sample seed.

This obstruction needs neither sample-adapted signs nor a fresh nonmultiplicative tent at every scale. It does need sparse scales and permits `f(p)=+1`; it lacks Möbius's prime-sign law and reciprocal-zeta identity. It proves no dense-scale failure, no failure at exponent `1/4`, and no lower bound for actual Möbius or a different sampling design. The matching prime-source recovery and its different pole input are compared in [global MI-040](../../../mind/intuition/MI-040-paired-box-inversion-transports-trimmed-mobius-pole-tests.md).
