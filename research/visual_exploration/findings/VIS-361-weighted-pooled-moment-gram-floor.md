# VIS-361 — positive Wang coefficient weights reduce to a weighted moment Gram

## Claim

Fix a finite Wang asymptotic depth `q>=1`, an invertible diagonal tail matrix

`D_beta=diag(beta_1,...,beta_q)`,

a compact positive center range `0<r<=c<=R`, and a fixed normalized radius bound `T>=1`.

For `N>=q`, choose nodes

`x_j=c+rho t_j`, `1<=j<=N`,

with `|t_j|<=T` and `0<rho<=rho_0`, where `rho_0 T<=r/2`. Let

`V=(x_j^k)_(1<=k<=q,1<=j<=N)`.

Now give the coefficient coordinates positive weights `w_j>0`. Write

`W=diag(w_1,...,w_N)`,
`M=sum_j w_j`,

and measure a bank coefficient vector `a` in the diagonal Hilbert norm

`||a||_(w^-1)^2 = sum_j |a_j|^2/w_j`.

Equivalently, writing `a=W^(1/2) z`, the weighted Wang moment map on Euclidean coordinates is

`A_w=D_beta V W^(1/2)`.

Let `S` be the normalized polynomial-sampling matrix

`S=(t_j^d)_(1<=j<=N,0<=d<=q-1)`.

Assume the normalized **weighted** degree-`q-1` moment Gram has a uniform floor:

`lambda_min(M^(-1) S^* W S) >= gamma > 0`.

Then there are constants `C_1,C_2>0`, depending only on `q,r,R,T,D_beta,gamma`, such that

`C_1 sqrt(M) rho^(q-1) <= s_q(A_w) <= C_2 sqrt(M) rho^(q-1)`.

Thus arbitrary positive nonuniform coefficient weights do not constitute an additional compact Wang cancellation resource once their total mass and weighted polynomial-sampling Gram are charged. The raw occupancy `N` in `VIS-360` is simply replaced by the effective positive mass `M`; the geometric invariant is the weighted discrete measure, not whether its atoms have equal weights.

In particular, if the normalized weighted empirical measures

`mu_N = M^(-1) sum_j w_j delta_(t_j)`

converge weakly on `[-T,T]` to a probability measure `mu` whose support contains at least `q` distinct points, then the weighted moment Gram is eventually uniformly positive definite and the same `sqrt(M) rho^(q-1)` law follows.

Therefore **nonuniform positive weights matter only through degeneration of the normalized weighted moment measure**. Weight concentration becomes a genuinely new compact regime only when `lambda_min(M^(-1)S^*WS)->0`, so fewer than `q` polynomial modes remain stably visible after the correct geometric rescaling.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL WEIGHTED-LEAST-SQUARES/MOMENT-GRAM GEOMETRY + STRUCTURAL NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

This result concerns positive diagonal coefficient metrics at fixed asymptotic depth. It does not classify signed or indefinite metrics, non-diagonal coefficient norms, a hierarchy in which the weighted Gram keeps degenerating after further rescaling, growing `q`, scale escape, infinite-dimensional topologies, or source-dependent signed arithmetic estimates.

## 1. Positive coefficient weights are a diagonal change of Hilbert coordinates

The unweighted Wang tail map from `VIS-354` is

`a -> D_beta V a`.

If the coefficient space carries

`||a||_(w^-1)^2=sum_j |a_j|^2/w_j`,

set `a=W^(1/2) z`. Then

`||a||_(w^-1)=||z||_2`

and the map becomes

`z -> A_w z = D_beta V W^(1/2) z`.

So positive diagonal weighting does not introduce a new nonlinear operation. It replaces ordinary polynomial sampling by sampling in the positive discrete measure with masses `w_j`.

This distinction is useful for the Wang clue. Signed cancellation remains in the coefficient vector itself. The positive `w_j` only specify how coefficient size is measured or how strongly each column is represented in the Hilbert geometry.

## 2. Weighted outer rescaling gives the lower bound

For `y in C^q`, write as in `VIS-360`

`p_y(x)=sum_(k=1)^q conjugate(y_k) beta_k x^k = x Q_y(x)`,

with `deg Q_y<=q-1`.

Expand around the pooled center:

`Q_y(c+rho t)=sum_(d=0)^(q-1) b_d t^d`.

If

`a(c)=(Q_y^(d)(c)/d!)_(d=0)^(q-1)`,

then

`b=D_rho a(c)`,
`D_rho=diag(1,rho,...,rho^(q-1))`.

Uniform invertibility of translation on this fixed polynomial space and invertibility of `D_beta` give

`||b||_2 >= c_0 rho^(q-1) ||y||_2`.

Because `x_j>=r/2`,

`||A_w^* y||_2^2`
` = sum_j w_j |p_y(x_j)|^2`
` >= (r/2)^2 sum_j w_j |Q_y(x_j)|^2`
` = (r/2)^2 b^* S^* W S b`.

The weighted Gram hypothesis therefore yields

`||A_w^* y||_2^2 >= C M rho^(2(q-1)) ||y||_2^2`.

Taking the infimum over unit `y` proves

`s_q(A_w) >= C_1 sqrt(M) rho^(q-1)`.

No pointwise lower or upper bound on an individual `w_j` is needed. All positive weight imbalance is already visible in the normalized matrix `M^(-1)S^*WS`.

## 3. The weighted mass exponent is sharp

Take

`Q_0(x)=(x-c)^(q-1)`,
`p_0(x)=x Q_0(x)`.

After normalizing the corresponding fixed coefficient direction in the Wang row space,

`|p_0(x_j)| <= C rho^(q-1) |t_j|^(q-1)`.

Hence

`||A_w^* y_0||_2^2`
` <= C rho^(2(q-1)) sum_j w_j |t_j|^(2(q-1))`
` <= C M rho^(2(q-1))`.

Therefore

`s_q(A_w) <= C_2 sqrt(M) rho^(q-1)`.

The only effect of a positive diagonal coefficient metric in the nondegenerate regime is thus the square root of total weighted mass. Unequal weights do not create an extra singular exponent.

## 4. Weak weighted limits identify exactly when the Gram stays healthy

The normalized weighted Gram is the degree-`q-1` moment matrix of

`mu_N=M^(-1) sum_j w_j delta_(t_j)`:

`G_(mu_N)=(int t^(a+b) dmu_N(t))_(0<=a,b<=q-1)`.

If `mu_N -> mu` weakly on the compact interval `[-T,T]`, all moments through degree `2q-2` converge. Thus

`M^(-1)S^*WS -> G_mu`.

For any coefficient vector `u`,

`u^*G_mu u = int |P_u(t)|^2 dmu(t)`

with `deg P_u<=q-1`. If `supp(mu)` contains at least `q` distinct points, no nonzero polynomial of degree at most `q-1` can vanish on the whole support. Hence `G_mu` is positive definite and the weighted Gram floor follows for all sufficiently large `N`.

This gives the correct interpretation of extreme but harmless nonuniformity. Some weights may vanish relative to `M` and others may dominate, yet there is no new compact escape provided the limiting weighted measure still retains at least `q` stably visible support points. Conversely, a weight pattern that asymptotically concentrates the normalized mass onto fewer than `q` points necessarily makes the degree-`q-1` Gram singular.

## 5. What remains after positive diagonal weights are priced

`VIS-360` left nonuniform weights as a nominal separate compact mechanism. The present result removes that ambiguity for positive diagonal coefficient metrics.

A claimed weighted escape must now exhibit one of the following genuinely different resources:

- the normalized positive weighted moment Gram itself tends to singularity, requiring finer rescaling of its deficient polynomial modes;
- the coefficient geometry is non-diagonal or indefinite rather than a positive diagonal Hilbert metric;
- the effective asymptotic depth grows;
- the scale range escapes the compact positive regime;
- the representation becomes infinite-dimensional;
- or the coefficients/metric encode signed arithmetic information whose gain must be proved directly at the source and survive the Wang destination audit.

Merely assigning unequal positive masses to an otherwise nondegenerate rescaled cloud is not enough.

## Prior-art audit

No novelty is claimed for weighted polynomial sampling or the weighted Gram matrix. Positive weighted least squares classically replaces the ordinary normal matrix by a weighted polynomial-sampling Gram. Akil Narayan, John D. Jakeman, and Tao Zhou, **A Christoffel function weighted least squares algorithm for collocation approximations**, *Mathematics of Computation* 86 (2017), 1913–1947, DOI `10.1090/mcom/3192`, is an explicit modern polynomial-approximation reference using weighted least-squares geometry.

Rectangular Vandermonde conditioning is also classical. Mykhailo Kuian, Lothar Reichel, and Sergij Shiyanovskii, **Optimally Conditioned Vandermonde-Like Matrices**, *SIAM Journal on Matrix Analysis and Applications* 40:4 (2019), 1399–1424, DOI `10.1137/19M1237272`, treats rectangular Vandermonde-like conditioning in orthogonal-polynomial coordinates. The clustered-node boundary remains the Batenkov--Demanet--Goldman--Yomdin and Batenkov--Diederichs--Goldman--Yomdin literature already cited in `VIS-358`--`VIS-360`.

The Mathia-specific delta is only the Wang bookkeeping: after the coefficient norm is expressed as a positive diagonal metric, the supposed weight resource is exactly a weighted discrete moment measure. If that measure retains `q` stable polynomial modes, the fixed-depth Wang quotient has the ordinary `sqrt(M) rho^(q-1)` floor.

## Dependencies

- `VIS-354`: fixed-depth Wang tail coefficients form a truncated inverse-scale Vandermonde map.
- `VIS-355`: source-adaptive choice cannot evade a uniformly conditioned compact quotient floor.
- `VIS-358`: regular unweighted one-cluster occupancy has scale `sqrt(N) epsilon^(q-1)`.
- `VIS-360`: a pooled unweighted colliding cloud with nondegenerate normalized moment Gram has scale `sqrt(N) rho^(q-1)`.
- `CLUE-wang-fixed-source-packet-localization`: accepted clue narrowed by this result.

## Research consequence

The compact fixed-depth Wang frontier can be narrowed again. **Positive nonuniform coefficient weights are completely priced by the total mass and the normalized weighted moment Gram.** When that Gram stays uniformly positive definite, the quotient floor is exactly of order `sqrt(M) rho^(q-1)`, regardless of how unequal the individual weights are.

Future compact-bank work should therefore not cite positive weight imbalance by itself as a new conditioning mechanism. A surviving weighted route must make the normalized weighted Gram genuinely degenerate and then explain what survives after the deficient modes are rescaled, or must leave the positive diagonal Hilbert setting altogether.