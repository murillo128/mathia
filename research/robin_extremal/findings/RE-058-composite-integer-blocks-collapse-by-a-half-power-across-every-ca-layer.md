# RE-058 — composite integer blocks collapse by a half-power across every CA layer

**Status:** `EXACT-DERIVED + NEGATIVE/OBSTRUCTION + ALL-LAYER-DIVISOR-SUM-REALIZATION-GATE + COMPOSITE-HALF-POWER-PENALTY + PRIME-SQUARE-SHARPNESS + GENERALIZED-CONTROL-BOUNDARY + PRIOR-ART-CLASSIFIED`.

`RE-057` shows that a composite integer label cannot realize the formal first-layer CA gain `log(1+1/q)` under the ordinary divisor-sum function: its internal divisors contribute at square-root scale and move the corresponding tangent event from scale `q` down to `O(sqrt(q))`. The all-layer matched controls of `RE-055`--`RE-056`, however, assign the same prime-form tower to every label,

\[
\lambda_j(q)
:=
\log\!\left(
1+\frac1{q+q^2+\cdots+q^j}
\right),
\qquad j\ge1.
\tag{1}
\]

The first-layer obstruction is not exceptional. If a composite integer `q` is treated as one new coprime block coordinate and its block exponent is raised from `j-1` to `j`, then **every fixed layer pays the same missing half-power**.

Put

\[
f(n):=\frac{\sigma(n)}n
\tag{2}
\]

and define the actual ordinary-divisor-sum block increment

\[
\boxed{
\Lambda_j^\sigma(q)
:=
\log\frac{f(q^j)}{f(q^{j-1})}
\qquad(j\ge1).
}
\tag{3}
\]

For a prime `q=p`, this is exactly the genuine CA layer increment:

\[
\boxed{
\Lambda_j^\sigma(p)=\lambda_j(p).
}
\tag{4}
\]

For every composite `q` and every fixed `j>=1`, by contrast,

\[
\boxed{
\Lambda_j^\sigma(q)
\ge
\frac14\,q^{-j+1/2}.
}
\tag{5}
\]

Since

\[
\lambda_j(q)=q^{-j}(1+O_j(q^{-1})),
\tag{6}
\]

the true composite block gain is uniformly larger than the prime-form gain by at least a factor of order `sqrt(q)`.

Transport this through the same CA tangent map

\[
g(x)=\frac1{x\log x}.
\tag{7}
\]

Define the actual block event coordinate `\zeta_{\sigma,j}(q)>1` by

\[
\boxed{
g(\zeta_{\sigma,j}(q))
=\frac{\Lambda_j^\sigma(q)}{\log q}.}
\tag{8}
\]

Then every composite `q` satisfies the explicit all-layer collapse

\[
\boxed{
\zeta_{\sigma,j}(q)
<8q^{j-1/2}.
}
\tag{9}
\]

The prime-form event coordinate of `RE-054`--`RE-056`, defined by

\[
g(\eta_j(q))
=\frac{\lambda_j(q)}{\log q},
\tag{10}
\]

obeys

\[
\eta_j(q)
=\frac{q^j}{j}
\left(1+O_j\!\left(\frac1{\log q}\right)\right).
\tag{11}
\]

Consequently, for every fixed layer,

\[
\boxed{
\frac{\zeta_{\sigma,j}(q)}{\eta_j(q)}
=O_j(q^{-1/2})
\longrightarrow0
\qquad(q\to\infty,\ q\text{ composite}).
}
\tag{12}
\]

The half-power loss is sharp in every layer. For prime squares `q=p^2`,

\[
\boxed{
\zeta_{\sigma,j}(p^2)
=
\left(\frac{2}{2j-1}+o_j(1)\right)
q^{j-1/2}.
}
\tag{13}
\]

Thus the generalized integer controls do not merely fail ordinary arithmetic at their first transition. Their **entire formal CA tower is incompatible with ordinary `sigma` on every composite block**: the synthetic layer event is placed at scale `q^j`, while the true divisor-sum block event occurs no later than scale `q^(j-1/2)`. Prime squares show that no uniform improvement of that exponent is possible.

This is still a boundary theorem, not a contradiction to false RH. It closes one natural escape from `RE-057`: a composite label cannot agree with ordinary divisor-sum arithmetic in the higher layers after failing only at layer one. Once the ordinary `sigma` response is required throughout the tower, the all-layer matched controls of `RE-055`--`RE-056` cannot use composite integers as substitute prime atoms at any fixed depth. The remaining RH-facing problem is global: actual prime atoms may still realize the required adaptive fan, and the present result supplies no new distribution theorem for them.

## 1. The true block increment factors over the internal prime coordinates

Write

\[
q=\prod_{r\mid q}r^{a_r},
\tag{14}
\]

where the product is over the distinct prime divisors of `q`. The normalized divisor-sum factor is

\[
f(q^j)
=
\prod_{r\mid q}
\frac{1-r^{-(a_rj+1)}}{1-r^{-1}}.
\tag{15}
\]

Therefore

\[
\boxed{
\frac{f(q^j)}{f(q^{j-1})}
=
\prod_{r\mid q}
\frac{1-r^{-(a_rj+1)}}
{1-r^{-(a_r(j-1)+1)}}.
}
\tag{16}
\]

For one internal prime power `r^a || q`, its factor can be written exactly as

\[
\frac{1-r^{-(aj+1)}}
{1-r^{-(a(j-1)+1)}}
=
1+x_{r,a,j},
\tag{17}
\]

with

\[
\boxed{
x_{r,a,j}
=
\frac{r^{-[a(j-1)+1]}(1-r^{-a})}
{1-r^{-[a(j-1)+1]}}.
}
\tag{18}
\]

If `q=p` is prime, equations (16)--(18) reduce to

\[
\frac{f(p^j)}{f(p^{j-1})}
=
\frac{1-p^{-(j+1)}}{1-p^{-j}}
=
1+\frac1{p+p^2+\cdots+p^j},
\tag{19}
\]

which proves (4). Thus (3) is exactly the ordinary-integer analogue of the formal layer law used in the matched controls; no asymptotic identification is involved at prime labels.

For composite `q`, equation (16) exposes what the formal single-label model suppresses. Raising the block exponent activates **every prime coordinate inside `q` simultaneously**. The excess is therefore internal to the label and cannot be removed by making distinct labels pairwise coprime.

## 2. One small internal prime already forces a half-power gain penalty

Let `q` be composite. Choose a prime divisor `p|q` with

\[
p\le\sqrt q,
\tag{20}
\]

and write `p^a || q`, `a>=1`. From (18),

\[
x_{p,a,j}
\ge
\frac12 p^{-[a(j-1)+1]},
\tag{21}
\]

because `1-p^{-a}>=1/2` and the denominator in (18) is less than one. Also

\[
p^{a(j-1)+1}
=(p^a)^{j-1}p
\le q^{j-1}\sqrt q
=q^{j-1/2}.
\tag{22}
\]

Hence

\[
\boxed{
x_{p,a,j}
\ge\frac12q^{-j+1/2}.}
\tag{23}
\]

For completeness, `0<x_{p,a,j}<=1`: the numerator in (18) is at most `1/2`, while its denominator is at least `1/2`. Therefore

\[
\log(1+x_{p,a,j})
\ge\frac{x_{p,a,j}}2.
\tag{24}
\]

All factors in (16) are greater than one, so

\[
\Lambda_j^\sigma(q)
=
\sum_{r\mid q}\log(1+x_{r,a_r,j})
\ge
\log(1+x_{p,a,j})
\ge
\frac14q^{-j+1/2},
\tag{25}
\]

which proves (5).

On the other hand,

\[
q+q^2+\cdots+q^j
=q^j(1+O_j(q^{-1})),
\tag{26}
\]

so (1) gives (6). Combining (5) and (6),

\[
\boxed{
\frac{\Lambda_j^\sigma(q)}{\lambda_j(q)}
\gg_j\sqrt q
\qquad(q\text{ composite}).
}
\tag{27}
\]

The important point is the exponent. The same square-root separation found at `j=1` in `RE-057` persists at **every fixed block depth**: both gains acquire the expected factor `q^{-(j-1)}`, but the composite block retains one extra internal divisor at scale at most `sqrt(q)`.

## 3. The gain penalty becomes an all-layer event-coordinate collapse

Equation (5) implies

\[
g(\zeta_{\sigma,j}(q))
\ge
\frac1{4q^{j-1/2}\log q}.
\tag{28}
\]

Put `alpha=j-1/2>=1/2`. At the explicit comparison point `8q^alpha`,

\[
g(8q^\alpha)
=
\frac1{8q^\alpha(\alpha\log q+\log8)}
<
\frac1{4q^\alpha\log q}.
\tag{29}
\]

Since `g` is strictly decreasing on `(1,infinity)`, equations (28)--(29) give

\[
\zeta_{\sigma,j}(q)<8q^{j-1/2},
\tag{30}
\]

proving (9). Combining this with (11) proves (12).

This comparison is stronger than saying that the composite layer gain is numerically different. The formal all-layer geometry of `RE-054`--`RE-056` puts layer `j` near

\[
\eta_j(q)\asymp_j q^j,
\tag{31}
\]

while ordinary divisor-sum arithmetic puts the same composite block transition no later than

\[
\zeta_{\sigma,j}(q)=O(q^{j-1/2}).
\tag{32}
\]

Thus every fixed layer loses the same relative half-power in physical event scale.

## 4. Prime squares make the half-power exponent sharp in every layer

Let `q=p^2` with `p` prime. There is only one internal prime coordinate, with exponent `a=2`, so (16) becomes

\[
\frac{f(q^j)}{f(q^{j-1})}
=
\frac{1-p^{-(2j+1)}}
{1-p^{-(2j-1)}}.
\tag{33}
\]

Equivalently,

\[
\frac{f(q^j)}{f(q^{j-1})}
=
1+
\frac{p^{-(2j-1)}(1-p^{-2})}
{1-p^{-(2j-1)}}.
\tag{34}
\]

For fixed `j`, therefore,

\[
\Lambda_j^\sigma(p^2)
=(1+o_j(1))p^{-(2j-1)}
=(1+o_j(1))q^{-j+1/2}.
\tag{35}
\]

After division by `log q`,

\[
g(\zeta_{\sigma,j}(p^2))
=
\frac{1+o_j(1)}{q^{j-1/2}\log q}.
\tag{36}
\]

Writing `alpha=j-1/2`, monotone inversion of `g` gives

\[
\zeta_{\sigma,j}(p^2)
=
\left(\frac1\alpha+o_j(1)\right)q^\alpha
=
\left(\frac{2}{2j-1}+o_j(1)\right)q^{j-1/2},
\tag{37}
\]

which proves (13). At `j=1`, this is exactly the sharp `2sqrt(q)` scale of `RE-057`.

Hence neither the gain exponent in (5) nor the event-coordinate exponent in (9) can be improved uniformly over composite labels. Prime squares are the least disruptive composites at every fixed layer, and they still miss the prime-form tower by a factor `sqrt(q)`.

## 5. Consequence for the all-layer generalized controls

`RE-055` and `RE-056` deliberately assign each label `q` the prime-form tower (1), then arrange one PNT-dense common label source whose resulting events avoid a chosen adaptive support chamber simultaneously in every layer. `RE-057` showed that a composite integer label cannot realize the first member of that tower under ordinary `sigma`.

The present result rules out a possible repair in which the discrepancy is treated as a first-layer artifact while the deeper formal events remain meaningful approximations to a composite block. They do not. If `q` is composite, every fixed actual block transition `q^(j-1)->q^j` lands at the wrong physical scale by a relative factor `O_j(q^-1/2)` compared with the assigned prime-form layer event.

Therefore a matched control that is required to preserve the ordinary normalized divisor-sum response **through the full fixed-depth event tower** cannot retain composite integer labels as substitute atoms. Pairwise coprimality between labels does not repair the model, because equations (16)--(25) arise from the internal factorization of each label separately. Declaring a composite label to be a free generator repairs the formal tower only by changing the arithmetic object away from ordinary integers and ordinary `sigma`.

This narrows the common-source frontier left after `RE-054`--`RE-057`:

\[
\text{all-layer event synchronization}
+\text{PNT density}
+\text{integer labels}
\]

can be faked, but

\[
\text{all-layer event synchronization}
+\text{the ordinary }\sigma\text{ response of each integer block}
\]

cannot be faked by composite atoms. The exact ordinary-prime category is already visible locally at every fixed layer, not only at the first one.

## 6. Prior-art boundary, limitations, and next obstruction

The arithmetic ingredients are classical: multiplicativity of `sigma`, the prime-power formula for `sigma(p^a)`, and the prime-coordinate organization of colossally abundant integers. Alaoglu--Erdos and the modern CA event formulation already organize genuine states through prime-power coordinates. A targeted literature check found these standard ingredients and the recent prime-layer workload framework, but no prior statement transporting the internal composite block factorization through the CA tangent map to obtain the uniform half-power tower collapse (9)--(13). No new external theorem is load-bearing, so `SOURCES.md` is unchanged.

The theorem is intentionally **fixed-layer**. Constants and the asymptotic inversion in (11)--(13) are not asserted uniformly for `j` growing with `q`. It also concerns an independent block coordinate. If a multiplier `q` shares prime factors with an ambient state `N`, the move must be decomposed into the genuine active prime-exponent coordinates before comparison; it is not one new block atom. Likewise, the theorem does not say that a quotient of consecutive genuine CA integers must be prime: simultaneous transitions may produce composite quotients as products of several genuine prime-coordinate events.

Most importantly, the result does not constrain the distribution of the surviving actual prime labels. Once ordinary `sigma` is imposed, the synthetic composite-label escape simply collapses back to the ordinary prime source. A useful continuation must now exploit a **global relation among those genuine prime coordinates** that the local primality gate does not already encode. The strongest candidates already present in this line are the accumulated closure `Y=Phi(Z)`, the exact Euler-product height, and the same-label standard/reciprocal prime-race coupling of the compact adaptive fan. Any next matched control must preserve those source-coupled quantities while also respecting the ordinary prime-coordinate divisor-sum tower.