# VIS-259 — higher cusp-adapted moment cancellation is exactly a uniform-approximation dual problem

## Claim

Fix an integer `m>=1` and `b>0`. Let `nu` be any finite real signed Borel measure supported on `[-b,b]` satisfying

`int dnu(q)=0`,

`int |q| dnu(q)=0`,

and, when `m>=2`,

`m_(2j)(nu)=int q^(2j) dnu(q)=0`, for `j=1,...,m-1`.

The first retained even moment is

`m_(2m)(nu)=int q^(2m) dnu(q)`.

On `[0,1]`, define the finite-dimensional approximation space

`V_m = span{1, t, t^2, t^4, ..., t^(2m-2)}`,

where for `m=1` this means simply `V_1=span{1,t}`. Put

`E_m = inf_(p in V_m) ||t^(2m)-p(t)||_infinity,[0,1]`.

Then `E_m>0` and the sharp packet inequality is

`|m_(2m)(nu)| <= E_m b^(2m) ||nu||_TV`.

The constant is optimal for every `m`: there exists an admissible signed packet attaining equality. Equivalently, among all packets obeying the displayed cancellations and normalized by

`|m_(2m)(nu)|=1`,

the minimum possible total variation is exactly

`E_m^(-1) b^(-2m)`.

Thus every additional even-moment cancellation in the cusp-adapted low-frequency branch has an exact conditioning interpretation. The exponent `b^(-2m)` is not merely a generic support-capacity lower bound: after imposing zero mass, exact `|q|` cusp cancellation, and all preceding even moments, the optimal constant is precisely the reciprocal distance of `t^(2m)` from the nuisance space that those cancellations annihilate.

The previous sharp results are the first two instances:

- `m=1`: `E_1=1/8`, recovering `VIS-257` and its exact unit-quadratic cost `8 b^-2`;
- `m=2`: `E_2=E_*=0.0634615548319...`, recovering `VIS-258` and its exact unit-quartic cost `15.7575716928... b^-4`.

**Evidence/status:** `EXACT-DERIVED + FUNCTIONAL-ANALYTIC DUALITY + SHARP SIGNED-MEASURE CAPACITY + NEGATIVE/REDESIGN CONTROL + NO-NOVELTY-CLAIM`.

No formula for `E_m` at higher order, zeta-specific `2m`-th coefficient, transfer estimate, covariance theorem, Rudnick--Sarnak uniformity improvement, or RH implication is claimed.

## 1. Every admissible packet annihilates the same approximation space

Put

`t=|q|/b in [0,1]`.

For any `p in V_m`, write

`p(t)=a_0+a_1 t+sum_(j=1)^(m-1) a_(2j)t^(2j)`.

The packet constraints give

`int p(|q|/b) dnu(q)=0`.

Therefore

`m_(2m)(nu)`
` = b^(2m) int [t^(2m)-p(t)] dnu(q)`.

Taking absolute values and using total variation,

`|m_(2m)(nu)|`
` <= b^(2m) ||t^(2m)-p||_infinity ||nu||_TV`.

Since this holds for every `p in V_m`, taking the infimum yields

`|m_(2m)(nu)| <= E_m b^(2m) ||nu||_TV`.

The space `V_m` is finite-dimensional and hence closed in `C([0,1])`. Since `t^(2m)` is not in `V_m`, its distance from `V_m` is strictly positive, so `E_m>0`.

This upper bound already shows that packet shape cannot change the support exponent. What remains is to show that the approximation distance is not merely an upper-bound artifact but the exact signed-measure capacity.

## 2. Hahn--Banach and Riesz duality make the bound sharp

Let

`X=C([0,1])`

with the uniform norm, let `V=V_m`, and let `f(t)=t^(2m)`. In the quotient Banach space `X/V`, the coset `[f]` has norm

`||[f]|| = dist(f,V)=E_m`.

On the one-dimensional subspace spanned by `[f]`, define a linear functional of norm one by sending `[f]` to `E_m`. The Hahn--Banach theorem extends it to a norm-one functional on all of `X/V`. Composing with the quotient map gives a continuous real linear functional `L` on `C([0,1])` such that

`||L||=1`,

`L(p)=0` for every `p in V_m`,

and

`L(t^(2m))=E_m`.

By the Riesz--Markov representation theorem for the dual of `C([0,1])`, there is a finite real signed Borel measure `mu` on `[0,1]` with

`||mu||_TV=1`

and

`L(g)=int_0^1 g(t) dmu(t)`

for every continuous `g`.

Hence `mu` annihilates `V_m` and satisfies

`int_0^1 t^(2m) dmu(t)=E_m`.

Lift `mu` symmetrically to `[-b,b]`: for `t>0` replace a mass at `t` by the symmetric probability measure

`sigma_(bt)=(delta_(bt)+delta_(-bt))/2`,

and send `t=0` to `delta_0`. In measure-kernel notation, define `nu_b` so that for every continuous function depending only on `|q|/b`,

`int g(|q|/b) dnu_b(q)=int_0^1 g(t) dmu(t)`.

This lift satisfies all required cancellations and

`m_(2m)(nu_b)=E_m b^(2m)`.

Its total variation is at most `||mu||_TV=1`. But the upper bound already proved gives

`E_m b^(2m) <= E_m b^(2m) ||nu_b||_TV`.

Since `E_m>0`, this forces `||nu_b||_TV>=1`. Therefore in fact

`||nu_b||_TV=1`,

and equality holds in the sharp packet inequality.

Rescaling this extremizer to `|m_(2m)|=1` gives total variation exactly

`E_m^(-1)b^(-2m)`.

No assumption of finite atomic support, symmetry beyond the harmless lift, or a particular packet ansatz is needed. The result optimizes over the complete class of finite signed Borel measures allowed by the current support-edge design.

## 3. `VIS-257` and `VIS-258` are the first two exact dual problems

For `m=1`, the nuisance space is

`V_1=span{1,t}`.

The best linear approximation to `t^2` has residual

`t^2-t+1/8`,

whose alternating extrema on `[0,1]` are `+1/8,-1/8,+1/8` at `t=0,1/2,1`. Thus

`E_1=1/8`.

The general theorem becomes

`|m_2(nu)| <= (b^2/8)||nu||_TV`,

which is exactly the sharp cusp-cancelled quadratic gate in `VIS-257`.

For `m=2`,

`V_2=span{1,t,t^2}`,

so `E_2` is the best degree-two uniform approximation error for `t^4`. `VIS-258` constructed the equioscillating residual explicitly and obtained

`E_2=0.0634615548319...`.

The present result shows that these are not two unrelated optimized packets. They are consecutive instances of one dual approximation problem in which each new cancellation enlarges the nuisance space and moves the desired carrier to the next even monomial.

## 4. The exact robust error gate follows at every order

Suppose the desired source contribution on the shrinking companion band is

`S_b(q)=A_(2m) q^(2m)`

while the remaining deterministic theorem, transfer, null, or model error is known only through

`||e_b||_infinity <= epsilon_b`.

For every admissible packet,

`|int S_b(q)dnu(q)|`
` = |A_(2m)| |m_(2m)(nu)|`
` <= E_m |A_(2m)| b^(2m) ||nu||_TV`.

The worst error allowed by the stated uncertainty class is

`sup_(||e_b||_infinity<=epsilon_b) |int e_b dnu|`
` = epsilon_b ||nu||_TV`.

Therefore strict worst-case source/error separation is possible only if

`epsilon_b < E_m |A_(2m)| b^(2m)`,

and asymptotically strong separation requires

`epsilon_b/[E_m |A_(2m)| b^(2m)] -> 0`.

The extremizing packet from the previous section attains the best possible source coefficient per unit total variation. Consequently neither a different signed packet shape nor scalar amplification can improve this deterministic minimax ratio under the same support and cancellation constraints.

This sharpens the constant-one support-capacity gate in `VIS-146` for the entire cusp-adapted cancellation ladder. The only ways around it are substantive: a larger source coefficient, a slower-shrinking bandwidth, a stronger/structured error norm, covariance or sign information, a different observable, or a theorem that avoids the shrinking-companion construction.

## 5. Prior-art and novelty boundary

The functional-analytic ingredients are classical. Best uniform approximation is the distance from a function to a finite-dimensional subspace of `C([0,1])`; Hahn--Banach identifies the quotient norm with a norm-one annihilating functional; and the Riesz--Markov theorem identifies continuous linear functionals on `C([0,1])` with finite signed measures of the same total-variation norm. Standard references include:

- **Encyclopedia of Mathematics, “Best approximation”**, `https://encyclopediaofmath.org/wiki/Best_approximation`;
- **Encyclopedia of Mathematics, “Hahn–Banach theorem”**, `https://encyclopediaofmath.org/wiki/Hahn%E2%80%93Banach_theorem`;
- **Encyclopedia of Mathematics, “Riesz representation theorem”**, `https://encyclopediaofmath.org/wiki/Riesz_representation_theorem`.

`VIS-258` already records the classical Chebyshev/minimax interpretation and alternation boundary for the explicit quartic case. No novelty is claimed for approximation-space duality, Hahn--Banach, Riesz representation, or best-approximation theory in general.

The Mathia-specific durable content is the exact identification of the full support-edge packet hierarchy with that classical dual problem. It upgrades the generic exponent-only obstruction in `VIS-146` and the two explicit sharp cases in `VIS-257`--`VIS-258` into a complete optimization statement over all signed packet shapes at every cancellation order.

## 6. Boundaries and falsification

The theorem is deterministic and uses total variation as the packet norm. A stochastic covariance norm, a sign-restricted error, orthogonality to the extremal packet, or another stronger structural estimate can have a different dual optimization problem. Such an escape must be proved for the actual destination statistic.

The theorem does not say that `E_m` is monotone in `m`, give a closed form for `E_m` beyond the already solved first two cases, or claim that an optimal measure must use a particular number of radii. Those questions are classical approximation/optimization refinements and are not needed for the present research gate.

Most importantly, existence of an optimally conditioned `2m`-th-order packet does not imply that the zeta-minus-null destination supplies a nonzero `A_(2m)`. Packet existence and source-carrier existence are logically separate. The current support-edge branch has already reached the point where the latter is the scarce information.

No untouched confirmation-zero data are used.

## Research consequence

The generic packet-design branch is now closed at all cancellation orders. After zero mass and exact cusp cancellation, adding further even-moment nulls never creates a free route around shrinking-band conditioning: the exact best unit-carrier cost is always

`E_m^(-1)b^(-2m)`.

Accordingly, do **not** spend future visual invocations computing `E_3,E_4,...` or optimizing higher-order packet shapes merely because another universal Taylor term can be cancelled. Such constants can matter only after the actual zeta-minus-null destination supplies the corresponding nonzero source coefficient and an error/covariance law capable of beating

`E_m |A_(2m)| b^(2m)`.

For the accepted Montgomery support-edge residual clue, the live mathematical fork therefore remains the one already exposed by `VIS-257`--`VIS-258`: either retain the quadratic carrier and beat the sharp `E_1 b^2` error scale, or cancel it only if a genuine quartic source coefficient and an error budget below `E_2 |A_4| b^4` can be derived. Higher cancellation orders no longer need separate packet-existence investigations.