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

[MC-539](../../findings/MC-539-two-random-starts-detect-mobius-poles-on-fourth-power-scales.md) exchanges observations per scale for a stronger scale quantifier. For independent uniform indices `J,K` in a fixed length-`X` population with jumps at most `A`, let `p_T=Pr(|u_J-u_K|>T)`. The exact bound is

`D <= 2T + AX p_T^2 + A p_T`.

An averaged anchor leaves at most `Xp_T` entries outside its `T`-neighborhood; bounded jumps bound their total distance to the retained indices by `B(B+1)/2`. Thus a dispersion floor `D>=cX^beta`, `beta>1/2`, forces `p_(2X^gamma)>>X^(-(1-beta)/2)` for each `1/2<gamma<beta`. The complete paired-box pole test supplies that floor in at least one channel on **every** large block, without identifying the channel in advance.

Take only two starts per channel at each prescribed `X_k=k^4`, independently across scales, and put `V_i(k)=|S_(L_i)(R_1)-S_(L_i)(R_2)|^2/4`. The failure probabilities for a hypothetical zero sum to infinity because `sum_k k^(-2(1-beta))=infinity`. Independent repetition therefore produces `max_i V_i(k)>X_k^(2gamma)` infinitely often, almost surely. On one probability-one event, RH is equivalent to both ceilings `V_i(k)<<_epsilon X_k^(1+epsilon)` for every epsilon along the **whole prescribed sequence**, with an eventual onset. Any fixed increasing integer sequence with `sum_k X_k^(-d)=infinity` for every `0<d<1/4` also suffices.

This does not improve MC-537's guarantee on an arbitrary post-selected unbounded subset: a favorable subset can omit the detected scales. Nor does it estimate population energy from one pair.

[MC-540](../../findings/MC-540-one-squarefree-source-hides-every-scale-dispersion-above-fourth-power-sampling.md) realizes the faster-scale obstruction with **one fixed coefficient source**, compatible across overlapping scales and both lengths. For any `a>4`, choose `3/4<kappa<1-1/a`. Let `Q(n)=sum_(r<=n)mu(r)^2`, `B(n)=Q(n) mod 2`, and start from the alternating square-free signs `b(n)=B(n)-B(n-1)`. At centers `c_m=floor((3/2)^m)`, starting sufficiently far out, place disjoint blocks of width `w_m=floor(c_m^kappa/100)`. Let `r_m` be half the block's square-free count, rounded down. On its first `2r_m` square-free positions, replace the alternating signs by `r_m` positive followed by `r_m` negative signs; leave any last position unchanged. The replacement has zero total mass, so its single prefix `F(n)=sum_(r<=n)f(r)` returns to `B` outside the blocks, with `|f(n)|=mu(n)^2` everywhere.

The elementary count `Q(y)=y/zeta(2)+O(sqrt(y))` gives `r_m asymp c_m^kappa`. Each bridge has height `asymp X^kappa` and area at least `r_m^2 asymp X^(2kappa)`. The center ratio `3/2` puts a complete bridge inside every sufficiently large `I_X`; translating it by either `L_i` lands outside all bridge blocks. Only `O(X^kappa)` starts have an endpoint in a bridge, while their window amplitudes are `O(X^kappa)`. Consequently both compatible channels have

`D_i(X) asymp X^(2kappa-1)` for **every** large integer `X`, with jumps at most two.

At `X_k=ceil(k^a)`, the probability that any of the four queried windows has an endpoint in a bridge is `O(X_k^(kappa-1))`. Its sum converges since `a(1-kappa)>1`. Outside that event all four window values belong to `{-1,0,1}`, so `V_i(k)<=1` eventually almost surely. This direction needs only uniform marginals, not independence across draws or scales. At `a=4` the strict interval for `kappa` is empty, consistently with MC-539's detection theorem.

Thus common coefficients, exact square-free magnitudes and every-scale dispersion do not improve the generic fourth-power boundary. MC-540 does **not** retain multiplicativity or a fixed signed smooth pole certificate; MC-538 retains multiplicativity but only its lacunary signed-target conclusion. These properties cannot be combined as though one control possessed both. Neither construction retains Möbius's prime signs or reciprocal-zeta identity, supplies its arithmetic energy ceiling, or proves its optimal sampling rate.
