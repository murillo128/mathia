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

[MC-541](../../findings/MC-541-optimal-prescribed-prime-moments-still-force-lacunarity.md) identifies the sharp replacement for that crude factor. Let `A` be the prescribed primes with signs `b_p`, `Z` the disjoint zeroed primes, and all other prime signs independent Rademachers. Extend multiplicatively on square-free integers and set nonsquare-free values to zero. Write `Q_A=product_(p in A)p`, `b(d)=product_(p|d)b_p`, `D_A(t)=#{d|Q_A:d<=t}`, and let `q_0` be the smallest prime outside `A union Z`. For deterministic complex weights on `1,...,N`, allowed to depend on the prescribed signs but not the free signs, put `T_v=sum_(n<=N)v_ng(n)`. Then

`sup_(v!=0) E|T_v|^2 / sum|v_n|^2 = D_A(N)`,

`sup_(v!=0) E|T_v-E T_v|^2 / sum|v_n|^2 = D_A(N/q_0)`.

The decomposition `n=dm` into prescribed divisor and free square-free part gives

`E|T_v|^2 = sum_m |sum_(d|Q_A, d<=N/m)b(d)v_(dm)|^2`.

Each free part is one orthogonal signed rank-one block of size `D_A(N/m)`. Ensemble centering deletes only `m=1`; the `m=q_0` block remains, attained by `v_(q_0 d)=b(d)`. This is not centering over sampled window starts. Balanced signs cannot improve the uniform weighted norm: the weights can align with them. With `Z` empty, even balanced sets `A subset (Y,2Y]` with `|A| asymp Y^kappa` have `sum_(p in A)1/p ->0` but both norms `1+|A|` at `N=4Y` for large `Y`, since `q_0=2` and products of two prescribed primes exceed the horizon.

In MC-538, `A=A_(<k)`, `Z=P_k`, `q_0=2`, and the preceding block contributes `|P_(k-1)| >> X_(k-1)^kappa/log X_(k-1)` single-prime divisors below `N_k/2`. Requiring even the optimal factor to be at most `X_k^eta_k`, `eta_k ->0`, forces

`log X_k / log X_(k-1) >= (kappa-o(1))/eta_k -> infinity`.

Thus optimizing the uniform moment constant or removing just the expectation cannot densify this construction. MC-541's extremizers are sign-aligned divisor fibres, generally not interval or fixed smooth weights. Its worst-case norm alone supplies no lower bound on actual background window energy.

[MC-542](../../findings/MC-542-balanced-prime-replicas-force-centered-window-energy.md)
adds the interval-specific constraint, including overlapping selected blocks.
Let `Y>=100` be integral, prescribe balanced signs `b_p` on a nonempty
finite prime set `P subset (4Y/3,5Y/3)`, and set

\[
B(n)=\sum_{p\in P,\ p\le n}b_p,\quad
w=\max P-\min P,\quad \mathcal B_2=\sum_n|B(n)|^2.
\]

Take integers `3Y<=X<=floor(13Y/4)`, `I_X={X,...,2X-1}`,
`H=floor(X/20)`, `K=floor(sqrt(2)H)`. For `L=H` or `K`, the replica test is
`a_L(j)=C(j+L)-C(j)`, where `C(j)=B(floor(j/3))`. Both translated supports
lie completely inside `I_X`, so `sum_j a_L(j)=0`. With

\[
R=\left\lceil\frac{3w}{\lfloor3Y/20\rfloor}\right\rceil\le8,
\qquad E_L=\sum_j|a_L(j)|^2,
\]

compact-support telescoping gives `E_L>=3 mathcal B_2/R^2` and
`|supp a_L|<=6w`, even when `3w>L`. The separated-pulse identity
`E_L=6 mathcal B_2` cannot be used in that regime.

For any square-free-supported multiplicative `g:N->{-1,0,1}` with these
prime values and `|g(3)|=1`, zero all primes of `P` to obtain `g_0` and put
`A=max_(t<=7Y)|sum_(n<=t)g_0(n)|`. On the test support, the only nonzero
selected-prime multiples in the windows are `3p`: multiplier four is
nonsquare-free and all other multipliers are outside. Hence exactly

\[
S_L(j)-\sum_{j<n\le j+L}g_0(n)=g(3)a_L(j).
\]

Pair this identity with `a_L`. Its zero mean removes any fitted constant,
and Cauchy--Schwarz gives, for the complete empirical energy
`V_L=X^(-1)sum_(j in I_X)|S_L(j)-mean_(I_X) S_L|^2`,

\[
\sqrt{XV_L}\ge
\left(\frac{\sqrt{3\mathcal B_2}}R-2A\sqrt{6w}\right)_+.
\]

For fixed `phi in C^1([4/3,5/3];C)`, `D=||phi'||_infinity>0`, write
`T_B(Y)=sum_(p in P)b_p phi(p/Y)`. Summation by parts bounds this
**selected-prime target** by `D sqrt(w mathcal B_2)/Y`, so

\[
|T_B(Y)|\le\frac{RD}{Y}\sqrt{\frac{Xw}{3}}\sqrt{V_L}
             +\frac{2\sqrt2RDw}{Y}A
\ll D(\sqrt{V_L}+A).
\]

Thus retaining `|T_B(Y)|>=Y^(1/2+delta)` with `V_L=Y^(1+o(1))`
requires `A>>_phi Y^(1/2+delta)`, for fixed `delta>0`. Overlapping
prescriptions within this band cannot erase their combined smooth target's
replica without a large prefix in the background after those primes are
removed. This deterministic alternative has no old-prime-product assumption.

The stronger typical-energy conclusion has additional hypotheses: the old
prescribed set `A_0` excludes three and has `product_(p in A_0)p<Y`, three
is free, and apart from a disjoint finite zeroed set, remaining prime signs
are independent Rademachers.
The one maximal-prefix estimate `E A^2<=2^(|A_0|)(7Y)(ceil(log_2(7Y))+1)^2`
then yields, conditional on the target size above, `V_H,V_K>>_phi |T_B(Y)|^2`
throughout the band with probability `1-O_phi(Y^(-2delta+o(1)))`.
It does not follow from expectation alone. These are finite-ensemble
statements about complete energies, not all realizations, sparse sampled
energies, actual Möbius sums, or one dense infinite multiplicative control.
The remaining escape needs backgrounds paying the displayed deterministic
cost, removal of the replica, or geometry outside its isolated multiplier
band; no impossibility of such a construction has been established.

[MC-543](../../findings/MC-543-independent-block-orientations-cannot-suppress-every-prime-replica.md)
excludes independent block orientations as a way to pay that cancellation
cost at every scale. Keep a balanced template `b_p` on `P` as above, fix
arbitrary signs at all other primes, and set `f_sigma(p)=sigma b_p` for
`sigma=+1,-1`. Extend multiplicatively on square-free integers and set the
other values to zero. On the same replica test support,

\[
S_{+,L}(j)-S_{-,L}(j)=2f(3)a_L(j),\qquad
Z_+-Z_-=2f(3)E_L,\quad Z_\sigma=\sum_j a_L(j)S_{\sigma,L}(j).
\]

The background cancels in this **difference** even if its prefixes are
large. Since `sum a_L=0` and `|f(3)|=1`,

\[
\max(|Z_+|,|Z_-|)\ge E_L,\qquad
\max_\sigma V_{\sigma,L}\ge E_L/X
\ge3\mathcal B_2/(R_L^2X),\quad R_L=\lceil3w/L\rceil\le8.
\]

Thus a fair orientation has conditional probability at least `1/2` of
energy `E_L/X`, for each fixed length and scale separately. The successful
orientation need not be the same for the two lengths or across scales.
This is a two-point inequality, not a free-prime moment estimate.

For one infinite source, fix in advance `Y_k->infinity`, pairwise disjoint
prime sets `P_k subset (4Y_k/3,5Y_k/3)`, balanced templates, and all
complementary prime signs. Give the blocks independent fair orientations.
At `X_k=3Y_k`, almost surely each channel has infinitely many indices with

\[
V_{i,k}\ge\mathcal B_{2,k}/(64Y_k).
\]

To justify the dependence across scales, select a deterministic subsequence
`Y_(k_(r+1))>6Y_(k_r)` and condition on every off-subsequence orientation,
without deleting its block. The windows involve only integers below
`7Y_(k_r)`; later retained primes exceed that horizon. Each next failure
has conditional probability at most `1/2`, so `n` consecutive failures
have probability at most `2^(-n)`. The original block family needs no
lacunarity or old-prime-product bound, and its containing bands may overlap.

For the fixed smooth weight above, `|T_k|^2<=w_k D^2 mathcal B_(2,k)/Y_k^2`
and `w_k<Y_k/3`. Hence an eventual selected-block target
`|T_k|>=Y_k^(1/2+delta)` forces, almost surely for each channel,
`V_(i,k)>=3|T_k|^2/(64D^2)` infinitely often. An eventual complete-energy
ceiling `X_k^(1+o(1))` has probability zero in this ensemble. Exceptional
deterministic orientations and complements coordinated with them remain
possible; independence is a new hypothesis, not a property of Möbius.
Neither full smooth-target size nor sparse sampled energy follows from
this selected-block target and complete-energy bound.

MC-538's sampling obstruction needs neither sample-adapted signs nor a fresh nonmultiplicative tent at every scale. It does need sparse scales and permits `f(p)=+1`; it lacks Möbius's prime-sign law and reciprocal-zeta identity. It proves no dense-scale failure, no failure at exponent `1/4`, and no lower bound for actual Möbius or a different sampling design. The matching prime-source recovery and its different pole input are compared in [global MI-040](../../../mind/intuition/MI-040-paired-box-inversion-transports-trimmed-mobius-pole-tests.md).

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
