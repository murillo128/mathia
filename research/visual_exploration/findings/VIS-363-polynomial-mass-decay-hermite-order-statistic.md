# VIS-363 — polynomially vanishing cluster masses are priced by weighted Hermite order statistics

## Claim

Fix a finite Wang asymptotic depth `q>=2`, an invertible diagonal tail matrix

`D_beta=diag(beta_1,...,beta_q)`,

a compact positive center range `0<r<=c<=R`, and fixed bounds for the normalized coordinates below.

Let `z_1,...,z_L` be distinct outer normalized centers in a fixed compact interval, with pairwise separation bounded below by a positive constant. For cluster `ell`, choose bounded inner nodes `u_(ell,j)`, positive weights `w_(ell,j)>0`, cluster mass

`M_ell=sum_j w_(ell,j)`,

total mass

`M=sum_ell M_ell`,

and mass fraction

`pi_ell=M_ell/M`.

At one common inner scale `epsilon in (0,1]`, put

`t_(ell,j)=z_ell+epsilon u_(ell,j)`,
`x_(ell,j)=c+rho t_(ell,j)`.

Assume each local normalized weighted polynomial cloud is uniformly healthy: if `U_ell` has columns `1,u,...,u^(q-1)` and `W_ell=diag(w_(ell,j))`, then

`lambda_min(M_ell^(-1) U_ell^* W_ell U_ell) >= gamma > 0`.

Assume also that the cluster mass fractions have fixed polynomial orders in the same inner scale: for some exponents `a_ell>=0` and constants `0<c_0<=C_0<infinity`,

`c_0 epsilon^(2a_ell) <= pi_ell <= C_0 epsilon^(2a_ell)`

for all sufficiently small `epsilon`. Necessarily `min_ell a_ell=0`.

Form the multiset of weighted Hermite costs

`H={a_ell+d : 1<=ell<=L, 0<=d<=q-1}`

and let `tau_q` be its `q`-th smallest element, counting multiplicity.

Let `S_epsilon` be the global degree-`q-1` polynomial-sampling matrix in the outer normalized coordinate `t`, and let `W` be the diagonal matrix of all sample weights. Then

`lambda_min(M^(-1) S_epsilon^* W S_epsilon) asymp epsilon^(2 tau_q)`.

If `V` is the `q x N` Wang monomial matrix with column `(x,x^2,...,x^q)^T` at each sample and

`A_w=D_beta V W^(1/2)`,

then, uniformly for sufficiently small `epsilon` and `rho` while the samples stay in the fixed positive compact range,

`s_q(A_w) asymp sqrt(M) rho^(q-1) epsilon^tau_q`.

Thus polynomially vanishing positive cluster masses do not create an unpriced compact cancellation resource. They simply delay the Hermite jets of a light cluster by the additive cost `a_ell`; the smallest singular-value exponent is the `q`-th order statistic of the jet costs `a_ell+d`.

`VIS-362` is the equal-mass special case. If all `a_ell=0`, the `q`-th smallest value among `L` copies of `0,1,2,...` is

`tau_q=floor((q-1)/L)`,

recovering its support-count exponent exactly.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL WEIGHTED HERMITE/CONFLUENT-VANDERMONDE GEOMETRY + STRUCTURAL NEGATIVE CONTROL + NO-NOVELTY-CLAIM`.

This result is source-free. It proves no new estimate for `theta`, the normalized remainder `G`, the zeta zero set, or RH.

## 1. The weighted cloud is a filtered Hermite system

For a polynomial

`P(t)=sum_(d=0)^(q-1) b_d t^d`,

write its normalized global sampling energy as

`E_epsilon(P)=M^(-1) sum_(ell,j) w_(ell,j) |P(z_ell+epsilon u_(ell,j))|^2`.

Taylor expansion at `z_ell` gives

`P(z_ell+epsilon u)=sum_(d=0)^(q-1) epsilon^d P^(d)(z_ell) u^d/d!`.

The local Gram hypothesis and boundedness of the inner coordinates give two-sided constants, uniform in `epsilon`,

`M_ell^(-1) sum_j w_(ell,j) |P(z_ell+epsilon u_(ell,j))|^2`
` asymp sum_(d=0)^(q-1) epsilon^(2d) |P^(d)(z_ell)/d!|^2`.

Multiplying by `pi_ell asymp epsilon^(2a_ell)` and summing over clusters,

`E_epsilon(P)`
` asymp sum_ell sum_(d=0)^(q-1)`
` epsilon^(2(a_ell+d)) |P^(d)(z_ell)/d!|^2`.

So every Hermite jet `(ell,d)` has one explicit asymptotic cost `a_ell+d`. Vanishing mass and derivative depth enter additively in the exponent.

## 2. The `q` cheapest jets give the lower bound

Let `tau_q` be the `q`-th smallest cost. Select `q` pairs `(ell,d)` with cost at most `tau_q`, breaking ties so that the selected derivatives at each center form an initial segment

`d=0,1,...,m_ell-1`.

This is always possible because the costs at a fixed center increase strictly with `d`. The selected `q` jet functionals are therefore an ordinary Hermite interpolation map with multiplicities `m_ell` satisfying

`sum_ell m_ell=q`.

Since the centers are distinct and uniformly separated, the associated confluent Vandermonde matrix is invertible with a fixed inverse bound. Hence

`sum_ell sum_(d<m_ell) |P^(d)(z_ell)|^2 >= C ||b||_2^2`.

Every selected cost is at most `tau_q`, so for `0<epsilon<=1` its weight is at least `epsilon^(2 tau_q)`. The filtered-energy identity then gives

`E_epsilon(P) >= C' epsilon^(2 tau_q) ||b||_2^2`.

Therefore

`lambda_min(M^(-1) S_epsilon^* W S_epsilon) >= C' epsilon^(2 tau_q)`.

The lower bound has a simple interpretation: a degree-`q-1` polynomial is determined by any `q` Hermite jets, and the cheapest `q` available jets determine the first asymptotic scale at which the full polynomial space becomes visible.

## 3. A vanishing polynomial makes the order statistic sharp

For each center define

`r_ell^-=#{d in {0,...,q-1}: a_ell+d<tau_q}`.

Because `tau_q` is the `q`-th smallest cost,

`sum_ell r_ell^- <= q-1`.

Enlarge these multiplicities, if necessary, to integers `r_ell>=r_ell^-` with

`sum_ell r_ell=q-1`.

Define

`P_0(t)=prod_ell (t-z_ell)^(r_ell)`.

This has degree exactly `q-1`. At center `ell`,

`P_0(z_ell+epsilon u)=O(epsilon^(r_ell))`

uniformly for bounded `u`. By the definition of `r_ell^-`, the first unforced jet obeys

`a_ell+r_ell^- >= tau_q`,

and therefore also

`a_ell+r_ell >= tau_q`.

After normalizing the coefficient vector of `P_0`, the cluster contribution is bounded by

`pi_ell O(epsilon^(2r_ell))`
` = O(epsilon^(2(a_ell+r_ell)))`
` = O(epsilon^(2 tau_q))`.

Summing over the finitely many clusters gives

`E_epsilon(P_0) <= C epsilon^(2 tau_q)`,

hence

`lambda_min(M^(-1) S_epsilon^* W S_epsilon) <= C epsilon^(2 tau_q)`.

Together with the lower bound,

`lambda_min(M^(-1) S_epsilon^* W S_epsilon) asymp epsilon^(2 tau_q)`.

This witness also shows why a light cluster is not free information: its low-order jets are shifted to later positions in the same Hermite filtration.

## 4. Transfer to the Wang bank

As in `VIS-360`--`VIS-362`, for a row direction `y in C^q` write

`p_y(x)=sum_(k=1)^q conjugate(y_k) beta_k x^k=x Q_y(x)`,

with `deg Q_y<=q-1`. In the outer coordinate `x=c+rho t`, write

`Q_y(c+rho t)=sum_(d=0)^(q-1) b_d t^d`.

The fixed-depth translation/rescaling map and invertibility of `D_beta` give

`||b||_2 >= C rho^(q-1) ||y||_2`.

Because `x` stays uniformly away from zero, the weighted Gram estimate implies

`||A_w^* y||_2^2`
` >= C M rho^(2(q-1)) epsilon^(2 tau_q) ||y||_2^2`.

Thus

`s_q(A_w) >= C sqrt(M) rho^(q-1) epsilon^tau_q`.

For the matching upper bound, use the degree-`q-1` witness in the original variable

`Q_rho(x)=rho^(q-1) P_0((x-c)/rho)`
` = prod_ell (x-c-rho z_ell)^(r_ell)`.

It is monic of fixed degree and its coefficient norm stays bounded above and below as `rho->0`. On cluster `ell`,

`Q_rho(c+rho(z_ell+epsilon u))`
` = rho^(q-1) P_0(z_ell+epsilon u)`
` = O(rho^(q-1) epsilon^(r_ell))`.

After normalizing the corresponding Wang row direction,

`||A_w^* y_0||_2^2`
` <= C M rho^(2(q-1)) epsilon^(2 tau_q)`.

Therefore

`s_q(A_w) asymp sqrt(M) rho^(q-1) epsilon^tau_q`.

## 5. What this closes and what remains

`VIS-362` required every outer support point to retain a positive fraction of the total mass. That hypothesis is no longer needed when the mass loss is polynomial in the same inner scale and the local weighted clouds remain uniformly nondegenerate.

The entire one-scale positive weighted problem is then encoded by the finite jet-cost spectrum

`a_ell, a_ell+1, ..., a_ell+q-1`.

The first `q` costs are enough to recover the whole polynomial space, and `tau_q` is the exact singular exponent. In particular, making some positive clusters asymptotically light does not by itself escape the source-free conditioning ledger.

Still-unpriced compact geometry now requires at least one genuinely new scale or topology:

- a local normalized weighted Gram that itself degenerates rather than remaining healthy after the common inner rescaling;
- nested inner scales that cannot be represented by one exponent list `a_ell+d`;
- cluster masses whose relevant asymptotics are not controlled by a fixed common-scale valuation and require another rescaling;
- a non-diagonal or indefinite coefficient geometry;
- source-dependent signed information whose gain must be proved at the arithmetic source.

Growing asymptotic depth, noncompact scale escape, global phase complexity, shrinking windows, infinite-dimensional limits, and nonlinear source dependence remain separate exits already identified by the accepted clue.

## Prior-art audit

No novelty is claimed for the underlying Hermite interpolation or clustered-Vandermonde mechanism. Confluent Vandermonde matrices are the classical linear algebra of value-and-derivative interpolation; Hao Lu, **Fast Solution of Confluent Vandermonde Linear Systems**, *SIAM Journal on Matrix Analysis and Applications* 15:4 (1994), 1277–1289, DOI `10.1137/S089547989324416X`, is an established reference.

The modern clustered-Vandermonde literature likewise makes local cluster multiplicity and geometry the controlling singular scales. Dmitry Batenkov, Laurent Demanet, Gil Goldman, and Yosef Yomdin, **Conditioning of Partial Nonuniform Fourier Matrices with Clustered Nodes**, *SIAM Journal on Matrix Analysis and Applications* 41:1 (2020), 199–220, DOI `10.1137/18M1212197`, and Dmitry Batenkov, Benedikt Diederichs, Gil Goldman, and Yosef Yomdin, **The spectral properties of Vandermonde matrices with clustered nodes**, *Linear Algebra and Its Applications* 609 (2021), 37–72, DOI `10.1016/j.laa.2020.08.034`, provide the relevant cluster-controlled spectral prior-art boundary.

The present order-statistic formula is recorded only as Mathia-specific fixed-depth bookkeeping for positive diagonal Wang weights with polynomially vanishing cluster masses. It is an elementary consequence of the weighted Hermite filtration above, and no claim of a new general Vandermonde or interpolation theorem is made.

## Dependencies

- `VIS-354`: the fixed-depth Wang tail coefficient map is a truncated inverse-scale Vandermonde map.
- `VIS-360`: after pooling at the outer width, the normalized polynomial-sampling Gram is the correct compact invariant.
- `VIS-361`: positive diagonal coefficient weights reduce to a normalized weighted moment Gram.
- `VIS-362`: equal-order positive support masses give the one-inner-scale exponent `floor((q-1)/L)`.
- `CLUE-wang-fixed-source-packet-localization`: accepted clue narrowed by this result.

## Research consequence

For one common inner scale with healthy local positive weighted clouds, **vanishing cluster masses are fully priced by the `q`-th smallest weighted Hermite cost `a_ell+d`**. The compact source-free branch cannot claim a new cancellation mechanism merely because some support masses vanish polynomially.

A further compact escape must make the local weighted geometry itself degenerate after rescaling, introduce a genuinely deeper scale hierarchy, or change the coefficient topology/source information. The remaining positive diagonal problem is therefore no longer “unequal or vanishing weights” in general; it is recursive degeneration beyond a single weighted Hermite filtration.
