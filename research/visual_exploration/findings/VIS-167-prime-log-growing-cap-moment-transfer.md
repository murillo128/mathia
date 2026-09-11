# VIS-167 — polynomially growing collision caps inherit Haar moment asymptotics

## Claim

Keep the fixed-support anchored held-out-prime setting of `VIS-164`--`VIS-166`. Let

`P={p_0,p_1,...,p_d}`

with `d>=1`, let `r` be a prime outside `P`, and let

`C_q = |sin(pi q beta)| / sqrt(sum_(j=1)^d sin^2(pi q alpha_j))`

be the anchored collision score from `VIS-165`. For `s>0` and `B>=1`, define the empirical and Haar capped moments

`M_(Q,s)(B) = Q^(-1) sum_(q<=Q) min(C_q,B)^s`,

`M_s(B) = E[min(C,B)^s]`,

where `C` is the matched Haar collision variable from `VIS-166`.

Let `delta=delta(P,r)>0` be any exponent admitted by `VIS-165`, and put

`a = delta/(2d+3)`,

`b = (2d+2)/(2d+3)`.

Then, for every fixed `s>0`,

`|M_(Q,s)(B)-M_s(B)| <= o_(Q->infinity)(1) + O_(P,r,d,s)(Q^(-a) B^(s+b))`

uniformly for `B>=1` along any chosen cap sequence.

Consequently, for a polynomial cap `B_Q=Q^gamma`:

1. if `0<s<d` and

   `0<gamma<delta/((2d+3)s+2d+2)`,

   then

   `M_(Q,s)(B_Q) -> E[C^s]`;

2. if `s=d` and

   `0<gamma<delta/(2d^2+5d+2)`,

   then

   `M_(Q,d)(B_Q) ~ d c_d gamma log Q`;

3. if `s>d` and the same support-scale condition

   `0<gamma<delta/(2d^2+5d+2)`

   holds, then

   `M_(Q,s)(B_Q) ~ [s c_d/(s-d)] Q^(gamma(s-d))`.

Here `c_d` is the Haar tail constant from `VIS-164`.

Thus the quantitative shrinking-target control of `VIS-165` propagates from exceedance probabilities to a nontrivial family of **jointly growing capped moments**. Below an explicit power cap, finite subcritical moments converge to the Haar population value, while critical and supercritical moments exhibit exactly the dimension-forced logarithmic or polynomial growth already present in the generic held-out-prime null.

**Evidence/status:** `EXACT-DERIVED + QUANTITATIVE-MATCHED-NULL + NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

This is not an uncapped empirical-moment theorem, an optimal cap range, a growing-support result, a source-sensitive zeta separation, or an RH consequence.

## 1. Layer cake transfers tail discrepancy to capped moments

For every nonnegative number `x`, every `s>0`, and every `B>=1`,

`min(x,B)^s = min(x,1)^s + s int_1^B t^(s-1) 1_(x>t) dt`.

Averaging over the deterministic orbit gives

`M_(Q,s)(B)`
` = M_(Q,s)(1) + s int_1^B t^(s-1) F_Q(t) dt`,

where `F_Q(t)=Q^(-1)#{q<=Q:C_q>t}`. Haar averaging gives the identical formula

`M_s(B)`
` = M_s(1) + s int_1^B t^(s-1) mu_d(t) dt`.

By the fixed-cap transfer in `VIS-166`,

`M_(Q,s)(1)-M_s(1)=o(1)`.

`VIS-165` supplies, uniformly for `t>=1`,

`|F_Q(t)-mu_d(t)|`
` <= C Q^(-a) (1+t)^b`.

Therefore

`|M_(Q,s)(B)-M_s(B)|`
` <= o(1) + C_s Q^(-a) int_1^B t^(s-1)(1+t)^b dt`
` <= o(1) + C'_s Q^(-a) B^(s+b)`.

No new discrepancy theorem is used here. This is the direct layer-cake consequence of the quantitative exceedance-set estimate already persisted in `VIS-165`.

## 2. Subcritical moments tolerate a larger cap range

Assume `0<s<d`. `VIS-166` proves that the full Haar moment is finite and

`M_s(B) -> E[C^s]`.

For `B_Q=Q^gamma`, the empirical/Haar error above tends to zero whenever

`-a + gamma(s+b) < 0`.

Since

`a/(s+b)`
` = delta/((2d+3)s+2d+2)`,

the stated subcritical cap condition gives

`M_(Q,s)(Q^gamma) - M_s(Q^gamma) -> 0`,

and hence

`M_(Q,s)(Q^gamma) -> E[C^s]`.

This is stronger than fixed-cap convergence but remains a capped statement. It does not imply convergence of the uncapped deterministic average `Q^(-1)sum C_q^s`, because the contribution above `Q^gamma` is not controlled here.

The permitted cap exponent depends on the moment order. Lower-order moments can tolerate a larger polynomial cap because layer-cake integration weights the far tail less heavily.

## 3. The critical dimension inherits logarithmic growth

At `s=d`, `VIS-166` gives

`M_d(B) ~ d c_d log B`.

For `B_Q=Q^gamma`, the empirical/Haar error is

`o(1)+O(Q^(-a+gamma(d+b)))`.

Now

`a/(d+b)=delta/(2d^2+5d+2)`.

Thus every fixed positive `gamma` strictly below this boundary makes the error `o(1)`. Since

`M_d(Q^gamma) ~ d c_d gamma log Q`,

we obtain

`M_(Q,d)(Q^gamma) ~ d c_d gamma log Q`.

The logarithmic divergence of the critical moment is therefore not merely a Haar population statement. It already appears along the deterministic prime-log orbit for a rigorously growing family of caps.

## 4. Every supercritical order has the same relative cap boundary

For fixed `s>d`, `VIS-166` gives

`M_s(B) ~ [s c_d/(s-d)] B^(s-d)`.

The absolute transfer error is still

`o(1)+O(Q^(-a)B^(s+b))`.

Relative to the Haar main term `B^(s-d)`, the quantitative part becomes

`O(Q^(-a) B^(d+b))`.

The moment order `s` cancels. Hence the relative error tends to zero for every fixed `s>d` under the single support-dependent condition

`gamma < a/(d+b)`
`      = delta/(2d^2+5d+2)`.

The fixed-cap `o(1)` term is also negligible relative to `Q^(gamma(s-d))`. Therefore

`M_(Q,s)(Q^gamma)`
` ~ [s c_d/(s-d)] Q^(gamma(s-d))`.

This cancellation is the useful structural point: once the moment order has crossed the support dimension, all higher fixed orders inherit the same conservative polynomial cap boundary from the tail-discrepancy transfer. Their different growth powers come entirely from the Haar heavy-tail law.

## 5. Relation to the shrinking-tail threshold

The supercritical/critical cap boundary

`gamma < delta/(2d^2+5d+2)`

is exactly the exponent condition appearing in `VIS-165` for relative tracking of the shrinking exceedance tail `F_Q(Q^gamma)~mu_d(Q^gamma)`.

This is not accidental. A critical or supercritical capped moment is dominated by the upper part of the admitted collision range, so its relative transfer is governed by the same competition between quantitative discrepancy error and the dimension-`d` tail. By contrast, a subcritical moment has a finite Haar target and can admit the larger order-dependent range from Section 2.

The result therefore organizes the null statistics into two regimes:

- below support dimension, polynomially growing caps can still converge to a finite population moment;
- at and above support dimension, the capped moments grow, but that growth is quantitatively forced by the same generic held-out-prime recurrence already controlling the tail.

Neither behavior is source-sensitive by itself.

## 6. Prior art and novelty boundary

No new external theorem is introduced. The two substantive inputs are already audited in the parent findings:

- `VIS-165` uses classical lower bounds for linear forms in logarithms together with Erdős--Turán--Koksma discrepancy to obtain the finite-`Q` tail-discrepancy estimate;
- `VIS-166` uses the classical layer-cake identity and Karamata/regular-variation reasoning to classify the Haar collision moments by support dimension.

The present result is their direct quantitative composition. Layer-cake integration of a tail-discrepancy bound is standard probability/analysis, and no novelty is claimed for that mechanism or for the resulting algebraic exponents. The Mathia-specific value is a sharper matched-null design rule for the persisted anchored collision observable: jointly growing moment statistics remain generic over an explicit polynomial cap range.

## 7. Boundaries and falsification

All support and primes are fixed. The exponent `delta(P,r)` can be extremely small, and the cap ranges here are deliberately conservative. Nothing is uniform in growing support or in the choice of held-out prime.

The estimate uses the non-sharp grid-transfer bound of `VIS-165`; any improvement to its discrepancy exponent or boundary approximation would improve the cap exponents here. Conversely, this finding does not establish that the displayed ranges are optimal.

It also does not control the untruncated empirical moment. Even for `s<d`, values with `C_q>Q^gamma` may contribute to the uncapped average in a way not settled by this argument. For `s>=d`, the result deliberately demonstrates generic growth rather than convergence.

Falsify the claim by finding an error in the layer-cake decomposition, the uniform tail-discrepancy estimate imported from `VIS-165`, or the Haar capped-moment asymptotics imported from `VIS-166`. No additional hidden probabilistic independence assumption is used for the deterministic orbit.

## Research consequence

Moment-based zeta-facing collision experiments now have a stronger mandatory null. Fixed caps are not the only generic regime: for every fixed support there is an explicit positive-power family of growing caps on which the deterministic held-out-prime orbit inherits the Haar moment law.

A proposed source-sensitive statistic therefore cannot use convergence of low-order capped moments, logarithmic critical growth, or polynomial high-order capped growth within these ranges as evidence. The useful target remains a predeclared relative separation from the matched omitted-prime control, or a genuinely uniform growing-support theorem that controls the deterioration of the Diophantine/discrepancy constants.