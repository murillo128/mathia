# FD-261 — Deep-band depletion needs superlinear depth amplification to beat the first-row ceiling

- **Date:** 2026-09-22
- **Status:** proved
- **Task:** Farey discrepancy
- **Research line:** `farey_discrepancy`
- **Kind:** source-side positivity / deep-band slack demand / exponent phase boundary / first-row comparison / reservoir capacity
- **Depends on:** FD-226, FD-258, FD-259, FD-260
- **Classification:** `EXACT-DERIVED + SOURCE-DEMAND-CALIBRATION + POSITIVE-LIFT-OBSTRUCTION + EXPONENT-PHASE-BOUNDARY + FIRST-ROW-DOMINANCE`

## Claim

FD-260 strengthens the general nonnegative switched-cushion ceiling to relative dyadic capacity `x^(-beta)`, with

\[
\beta=\log_2\frac32=0.5849625007\ldots .
\]

The live source-side question is whether the actual signed Mertens repair requires enough positive slack to violate that ceiling. The following comparison shows quantitatively what a lower bound of that kind would have to accomplish before it could improve the independent first-row obstruction of FD-258.

Use the scale-adapted FD-226 reservoirs at divisor depth `D`, with natural occupancy scale

\[
L_N=\frac{N}{D\log N}.
\]

Let `p_N(d)>=0` be a positive cushion satisfying the physical linear capacity envelope

\[
0\le p_N(d)\le C L_N d,
\qquad 1\le d\le D,
\]

and suppose its normalized switched rows are uniformly bounded: after writing

\[
b_N(d)=\frac{p_N(d)}{L_N},
\]

all complete period-three switched rows used by FD-260 are bounded by one fixed constant `B`.

Let `x=x_N` be the largest dyadic number with `2x<=D`. Then `D/4<x<=D/2`, so FD-260 gives

\[
\boxed{
P_N(x):=\sum_{x\le d<2x}p_N(d)
\ll_{C,B}
L_N x^{2-\beta}
\ll
\frac{N D^{1-\beta}}{\log N}.
}
\tag{1}
\]

Now let `c_N` be any signed repair that has to be lifted by `p_N`, in the pointwise sense

\[
c_N(d)+p_N(d)\ge0.
\]

Its unavoidable positive-slack demand on the same band is

\[
R_N(x):=
\sum_{x\le d<2x}(-c_N(d))_+.
\]

Necessarily `R_N(x)<=P_N(x)`. Suppose that on an unbounded family one can prove the source-specific lower bound

\[
\boxed{
R_N(x)
\ge
N^{\theta-o(1)}D^{\alpha-o(1)},
}
\tag{2}
\]

for fixed `0<=theta<1` and fixed `alpha>=0`, while

\[
D=N^{\lambda+o(1)}.
\]

Then the FD-260 ceiling can contradict (2) at exponent level only when

\[
\boxed{
\theta+\alpha\lambda
>
1+(1-\beta)\lambda.
}
\tag{3}
\]

If `alpha<=1-beta`, no polynomial depth can satisfy (3). If `alpha>1-beta`, the threshold is

\[
\boxed{
\lambda>
\frac{1-\theta}{\alpha-1+\beta}.
}
\tag{4}
\]

In particular, a lower bound only **linear in divisor depth**, `alpha=1`, becomes contradictory only for

\[
\boxed{
\lambda>
\frac{1-\theta}{\beta}.
}
\tag{5}
\]

Since `beta<1`, this lies strictly beyond the corresponding first-row scale `lambda=1-theta`. To make the general FD-260 deep-band mechanism become decisive at or before that scale, one needs

\[
\boxed{
\alpha>2-\beta
=1.4150374992\ldots .
}
\tag{6}
\]

Thus a source lower bound that merely supplies one zero-frontier-sized unit of negative repair per divisor cell cannot improve the polynomial-depth obstruction already visible in the first switched row. A genuinely stronger result must exhibit **superlinear amplification in divisor depth**, or else add structure strong enough to replace the FD-260 exponent by the inverse-linear FD-259 regime.

## 1. Convert the FD-260 normalized ceiling back to physical occupancy

The choice of `x` ensures that the entire band `[x,2x)` lies inside the finite divisor depth. FD-260's finite-block form therefore applies to `b_N=p_N/L_N` and gives

\[
\frac{\sum_{x\le d<2x}b_N(d)}
     {\sum_{x\le d<2x}d}
\ll_{C,B}
x^{-\beta}.
\tag{7}
\]

Since

\[
\sum_{x\le d<2x}d\asymp x^2,
\]

we obtain

\[
\sum_{x\le d<2x}b_N(d)
\ll_{C,B}x^{2-\beta}.
\tag{8}
\]

Multiplying by the physical occupancy scale `L_N` proves the first inequality in (1). Because `x` is within a fixed factor of `D`,

\[
L_Nx^{2-\beta}
\asymp
\frac{N}{D\log N}D^{2-\beta}
=
\frac{ND^{1-\beta}}{\log N},
\tag{9}
\]

which proves the second.

No information about the internal placement of the positive cushion is being discarded here. FD-260 inherits the cellwise-positive reduction of FD-230 and permits arbitrary redistribution inside the band. Equation (1) is therefore an aggregate physical slot ceiling for every positive lift whose normalized switched contribution remains bounded.

The statement also covers the stronger physical target in which the cushion's unnormalized switched contribution is `O(1)`: whenever `L_N` tends to infinity, its normalized row bound even tends to zero. Keeping a fixed `B` above is deliberately weaker.

## 2. The repair-demand exponent has an exact phase boundary

Pointwise nonnegativity of the lifted occupancy gives

\[
p_N(d)\ge(-c_N(d))_+,
\]

hence

\[
R_N(x)\le P_N(x).
\tag{10}
\]

At polynomial depth `D=N^(lambda+o(1))`, equation (1) has exponent

\[
1+(1-\beta)\lambda,
\tag{11}
\]

up to logarithmic and subpower factors, whereas (2) has exponent

\[
\theta+\alpha\lambda.
\tag{12}
\]

A strict exponent contradiction therefore requires (3). Rearranging gives

\[
(\alpha-1+\beta)\lambda>1-\theta.
\tag{13}
\]

Because the right side is positive, `alpha<=1-beta` can never work. For `alpha>1-beta`, division gives (4).

This is only a **necessary strength test for a lower-bound strategy**. It does not assert the existence of a positive lift when (3) fails, and it does not claim that the actual canonical repair obeys (2) for any `theta,alpha`. Its role is to say exactly when a future lower bound of the form (2) would be strong enough for the already-proved FD-260 ceiling to turn it into an obstruction.

The current subpolynomial construction is also correctly left untouched. When `D=N^{o(1)}`, the right side of (1) is `N^{1+o(1)}` up to the logarithm, while every lower bound of the form (2) with fixed `theta<1` remains `N^{theta+o(1)}`. The exponent comparison cannot contradict the existing FD-225--FD-226 block.

## 3. Linear-in-depth demand loses to the first switched row

FD-258 supplies an independent source-side obstruction before any deep-band positivity estimate is used. On a subsequence where the physical first-row Mertens forcing has size at least `N^(theta-o(1))`, its exact first-two-cell identity forces

\[
D\le N^{1-\theta+o(1)}
\tag{14}
\]

for subpower switched tolerance. Let us compare a hypothetical deep-band lower bound using the **same arithmetic amplitude exponent** `theta`.

If the negative repair demand grows only linearly with the number of divisor cells, so `alpha=1`, equation (4) becomes

\[
\lambda>
\frac{1-\theta}{\beta}.
\tag{15}
\]

But `1/beta=1.709511...>1`. Hence the deep-band contradiction begins strictly after the scale already excluded by (14). At the square-root calibration `theta=1/2`, for example,

\[
\lambda>
\frac{1/2}{\beta}
=0.8547556456\ldots,
\tag{16}
\]

whereas the first-row square-root ceiling is `lambda<=1/2`.

More generally, ask what depth exponent `alpha` in (2) would make the deep-band threshold no later than `lambda=1-theta`. Substituting into (3) and cancelling `1-theta>0` gives

\[
\alpha-1+\beta>1,
\]

or exactly the strict condition (6). At equality `alpha=2-beta`, the polynomial exponents only tie and logarithmic information becomes decisive.

This is the main strategic consequence. A theorem saying roughly “there are `D` deep cells and each needs Mertens-sized slack” is not strong enough to improve the present source boundary. To make general nonnegative depletion beat the first row, the physical repair must force its negative part to accumulate faster than

\[
D^{2-\beta}
=D^{1.415037\ldots}
\tag{17}
\]

at fixed arithmetic amplitude exponent. That identifies the missing phenomenon much more sharply than the generic instruction to obtain a lower bound on positive slack.

For comparison, a capacity-shaped demand with `alpha=2` would clear this threshold. In that regime (4) becomes

\[
\lambda>
\frac{1-\theta}{1+\beta},
\tag{18}
\]

which is strictly earlier than `1-theta`. The distinction between linear and nearly quadratic depth accumulation is therefore structural, not a small numerical refinement of the FD-260 constant.

## 4. Why the FD-259 monotone cone changes the comparison qualitatively

FD-259 proves a different ceiling when the positive cushion has nonnegative Möbius increments,

\[
\mu*b_N\ge0.
\tag{19}
\]

Then its aggregate normalized mass on a dyadic band is only `O(x)`, not `O(x^(2-beta))`. Returning to physical units at `x\asymp D`,

\[
\boxed{
P_N(x)
\ll
L_ND
\asymp
\frac{N}{\log N}.
}
\tag{20}
\]

The divisor depth disappears from the upper bound. Against the same demand (2), a strict polynomial contradiction now requires

\[
\boxed{
\theta+\alpha\lambda>1.
}
\tag{21}
\]

For `alpha>0`, the threshold is

\[
\lambda>
\frac{1-\theta}{\alpha}.
\tag{22}
\]

In particular `alpha=1` now meets the first-row exponent `1-theta` exactly. Logarithmic strength decides the boundary case, but there is no longer the factor `1/beta` postponing the deep-band obstruction.

This explains why proving a structural sign condition such as `mu*b_N>=0`, if it were genuinely available for the physical positive lift, would be much more consequential than improving the general FD-260 kernel exponent from `0.58496...` toward its present method ceiling near `0.62`. In the unrestricted signed-increment cone, even a linear source-demand theorem arrives too late. In the monotone-response cone, the same depth law is already exponent-critical.

The sign condition is not known for the actual repair and must not be assumed. Equation (20) is included to identify a qualitatively different route, not to claim that the canonical Mertens correction lies in that cone.

## 5. Boundary, prior art, and verdict

A targeted literature audit around Farey discrepancy, Mertens divisor sums, positive Volterra recurrences and source-capacity inequalities found the expected classical Mertens/Dirichlet-convolution background but no external theorem matching this reservoir-specific exponent comparison. No external result is load-bearing here. Equations (1)--(6) are direct consequences of the already-established physical capacity scale of FD-226, the general nonnegative depletion theorem FD-260, the first-row obstruction FD-258, and the monotone-response theorem FD-259. No update to `SOURCES.md` is required.

The result does not provide the missing lower bound on `R_N(x)`. In particular it does not prove any `theta` or `alpha` for the canonical block-Mertens repair, and it does not strengthen the Mertens function. It instead narrows what such a theorem must look like if the goal is to improve the polynomial-depth source obstruction rather than merely establish some nonzero slack consumption.

There are now two quantitatively distinct targets. In the general nonnegative cushion class, a deep-band lower bound must exhibit depth amplification stronger than `D^(2-beta)=D^1.415...` before it can beat the same-amplitude first-row ceiling. In the extra monotone-response cone, linear depth accumulation is already exponent-critical. This makes further small optimizations of the FD-260 positive kernel secondary unless they are accompanied by a source theorem strong enough to move `alpha` across the corresponding phase boundary.

**Verdict.** The live source-side problem is not merely to prove that the Mertens repair consumes positive slack. A lower bound linear in divisor depth, even at square-root arithmetic amplitude, cannot improve the first-row polynomial ceiling when combined with the strongest current general nonnegative depletion theorem. To make deep-band positivity genuinely decisive before the first row, the repair must force superlinear depth accumulation beyond exponent `2-log_2(3/2)=1.415037...`, or one must prove additional structure such as monotone divisor response that upgrades the available positive-cushion ceiling to inverse-linear capacity depletion.
