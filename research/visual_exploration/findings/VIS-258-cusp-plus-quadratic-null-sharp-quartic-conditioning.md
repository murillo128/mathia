# VIS-258 — cusp-plus-quadratic cancellation has a sharp quartic conditioning constant

## Claim

Let `0<b<=1` and let `nu` be any finite real signed Borel measure supported on `[-b,b]` satisfying

`int dnu(q)=0`,

`int |q| dnu(q)=0`,

and

`m_2(nu)=int q^2 dnu(q)=0`.

Write

`m_4(nu)=int q^4 dnu(q)`.

Define

`u = [1 + sqrt(10 + 6 sqrt(3))]/[9 + 6 sqrt(3)]`,

`v = (1 + sqrt(3))u`,

and

`E_* = (9/2 + 3 sqrt(3)) u^4`.

Numerically,

`u = 0.284431583143...`,

`v = 0.777081536424...`,

and

`E_* = 0.0634615548319...`.

Then the sharp inequality

`|m_4(nu)| <= E_* b^4 ||nu||_TV`

holds for every such `nu`. The constant `E_*` is optimal.

Equivalently, among all packets with the three cancellations above and normalized by `|m_4(nu)|=1`, the minimum possible total variation is exactly

`K_* b^(-4)`,

where

`K_* = 1/E_* = 15.7575716928...`.

Thus the cusp-adapted branch left open by `VIS-257` has a fully sharp quartic conditioning floor: killing mass, the limiting sine-kernel cusp, and the finite-window quadratic mode while retaining an order-one quartic carrier costs at least `15.7575... b^-4` in total variation.

An extremizer exists on exactly four radii `0`, `ub`, `vb`, and `b`. It can be taken symmetric in `q`, so the sharp constant is attained without using angular/asymmetric freedom.

**Evidence/status:** `EXACT-DERIVED + SHARP MINIMAX/SIGNED-MEASURE BOUND + NEGATIVE/REDESIGN CONTROL + NO-NOVELTY-CLAIM`.

No zeta-specific quartic coefficient, finite-height transfer estimate, Rudnick--Sarnak uniformity theorem, cross-height covariance law, or RH implication is claimed.

## 1. The problem is a degree-two uniform approximation problem

Put `t=|q|/b` on `[0,1]`. Because `nu` annihilates `1`, `|q|`, and `q^2`, every quadratic polynomial

`p_2(t)=a_0+a_1 t+a_2 t^2`

may be subtracted from `t^4` without changing the quartic packet moment:

`m_4(nu)`
` = b^4 int [t^4-p_2(t)] dnu(q)`.

Therefore any uniform bound

`sup_(0<=t<=1) |t^4-p_2(t)| <= E`

implies

`|m_4(nu)| <= E b^4 ||nu||_TV`.

The sharp packet constant is consequently the best uniform approximation error of `t^4` by polynomials of degree at most two. The argument below constructs the optimizer and an extremizing signed measure directly, so no approximation-theory theorem is load-bearing.

## 2. Explicit equioscillating residual

Let

`rho=1+sqrt(3)`,

`v=rho u`,

with `u` as above. These numbers satisfy

`v^2-2uv-2u^2=0`

and

`u^2-2uv+2u-2v^2+1=0`.

Equivalently, the second identity reduces to

`(9+6sqrt(3))u^2-2u-1=0`,

whose positive root is the displayed `u`. In particular,

`0<u<v<1`.

Define

`D(t)=4(t-u)(t-v)(t+u+v)`.

Its only critical zeros on `[0,1]` are `u` and `v`; its sign is positive on `(0,u)`, negative on `(u,v)`, and positive on `(v,1)`.

Now put

`E_* = (1/2) int_0^u D(t) dt`.

Direct integration gives

`E_*=(9/2+3sqrt(3))u^4`.

Define the residual by

`R(t)=-E_* + int_0^t D(s) ds`.

The two algebraic identities above give

`int_0^v D(t)dt = v^2(2u^2+2uv-v^2)=0`

and

`int_u^1 D(t)dt = (1-u)^2(u^2-2uv+2u-2v^2+1)=0`.

Hence

`R(0)=-E_*`,

`R(u)=+E_*`,

`R(v)=-E_*`,

and

`R(1)=+E_*`.

Because the derivative changes sign only at `u` and `v`, these are the alternating extrema on `[0,1]`, so

`||R||_infinity=E_*`.

Also `D` is a cubic with no quadratic term. Therefore its antiderivative has no cubic term and

`R(t)=t^4-p_2^*(t)`

for a quadratic polynomial. More explicitly, if

`B=-4uv(u+v)`

and

`C=2(u^2+uv+v^2)`,

then

`p_2^*(t)=E_*+Bt+Ct^2`.

Thus every admissible packet satisfies

`|m_4(nu)| <= E_* b^4 ||nu||_TV`.

## 3. A four-radius signed packet attains equality

Let the four normalized radii be

`t_0=0`, `t_1=u`, `t_2=v`, `t_3=1`,

and define the barycentric weights

`lambda_i = [product_(j != i)(t_i-t_j)]^(-1)`.

For every polynomial `p` of degree at most two,

`sum_i lambda_i p(t_i)=0`.

A self-contained way to see this is to write the Lagrange interpolation formula for `p` on the four nodes. Its cubic coefficient is zero, while the cubic coefficient of the `i`-th Lagrange basis polynomial is exactly `lambda_i`.

The ordered nodes give the alternating signs

`lambda_0<0`, `lambda_1>0`, `lambda_2<0`, `lambda_3>0`,

which match the signs of `R(t_i)`.

For `x>0`, let

`sigma_x=(delta_x+delta_(-x))/2`,

and let `sigma_0=delta_0`. Define

`nu_b^* = sum_(i=0)^3 lambda_i sigma_(b t_i)`.

The interpolation identities imply exactly

`int dnu_b^*=0`,

`int |q| dnu_b^*=0`,

and

`m_2(nu_b^*)=0`.

The supports are distinct, so

`||nu_b^*||_TV = sum_i |lambda_i|`.

Since the quadratic approximant is annihilated,

`m_4(nu_b^*)`
` = b^4 sum_i lambda_i t_i^4`
` = b^4 sum_i lambda_i R(t_i)`
` = E_* b^4 sum_i |lambda_i|`.

Therefore equality holds in the bound. Rescaling `nu_b^*` to `|m_4|=1` gives total variation exactly

`1/(E_* b^4)=K_* b^-4`.

This proves both sharpness and attainability.

## 4. Relation to the previous conditioning gates

`VIS-146` gave the universal support-capacity estimate

`|m_4(nu)| <= b^4 ||nu||_TV`

after quadratic cancellation, and showed that the exponent `b^-4` is unavoidable and attainable up to a fixed factor. It did not include exact cusp cancellation and did not determine the optimal constant.

`VIS-257` then supplied the complementary sharp result one order lower: after zero mass and exact cusp cancellation,

`|m_2(nu)| <= (b^2/8)||nu||_TV`,

so a unit quadratic carrier costs exactly `8b^-2` total variation.

The present result closes the next fork. If the redesign also imposes `m_2=0`, the optimal quartic carrier is not merely `Theta(b^-4)`; its exact best conditioning is

`K_* b^-4 = 15.7575716928... b^-4`.

The additional cusp constraint therefore makes the robust quartic capacity strictly smaller than the generic support bound of `VIS-146` by the factor `E_*=0.06346...`.

## 5. Finite-window consequence

For the smooth centered-cosine channel of `VIS-146`, after imposing `m_2=0`,

`int Delta_H(q)dnu(q)`
` = -(2/3)pi^4 mu_4(H)m_4(nu) + R_6`,

with

`|R_6| <= (4/45)pi^6 M_6(H)b^6 ||nu||_TV`.

Normalize the sharp cusp-plus-quadratic packet by `m_4=1`. Its total variation is `K_*b^-4`, hence

`|R_6| <= (4/45)pi^6 K_* M_6(H)b^2`.

So the explicit optimal packet kills the limiting `|q|` cusp and the finite-window quadratic term exactly, retains the quartic coefficient at order one, and pays only the expected `O(M_6 b^2)` Taylor remainder after normalization. The cost has not disappeared; it has been concentrated into the exact `K_*b^-4` conditioning factor.

More generally, if a desired quartic source term is `A_4 q^4` while an unknown deterministic transfer/theorem error is controlled only by

`||e_b||_infinity <= epsilon_b`,

then every packet satisfying the three cancellations obeys

`|A_4 m_4(nu)| <= E_* |A_4| b^4 ||nu||_TV`,

while the worst admissible error is `epsilon_b ||nu||_TV`. Therefore strict worst-case separation requires

`epsilon_b < E_* |A_4| b^4`,

and asymptotically strong separation requires

`epsilon_b/[E_* |A_4| b^4] -> 0`.

The extremizing packet attains the sharp signal-to-total-variation constant. Scalar amplification cannot improve it.

This strengthens the constant-one necessary gate in `VIS-146` for the cusp-adapted quartic branch. Exact cusp cancellation is mathematically possible, but it makes the quartic error budget about `1/E_*=15.76` times tighter than the unconstrained support-capacity envelope.

## 6. Prior art and novelty boundary

The abstract approximation problem is classical Chebyshev/minimax approximation: best uniform approximation is characterized by alternating extrema, and the present four-point residual is exactly the degree-two minimax geometry for `t^4` on `[0,1]`. A bounded prior-art check against the standard Chebyshev alternation theorem confirms that no general approximation-theory novelty should be claimed. See, for example, **Encyclopedia of Mathematics, “Chebyshev theorem”**, `https://encyclopediaofmath.org/wiki/Chebyshev_theorem`.

The proof here is nevertheless self-contained: the explicit residual gives the upper bound, and the four-radius barycentric signed measure gives equality. No external theorem is required for correctness.

The Mathia-specific durable content is the composition with the support-edge design constraints from `VIS-141`--`VIS-146`, `VIS-256`, and `VIS-257`: once a low-frequency companion is required to cancel both the universal sine-kernel cusp and the finite-window quadratic mode, its best possible quartic carrier has the exact conditioning constant above.

No claim is made that this particular constant or extremal polynomial is new within approximation theory.

## 7. Boundaries and falsification

The theorem concerns finite real signed measures and total variation. A redesign using a different observable, a stronger norm, positivity, covariance orthogonality, theorem-specific oscillation, or another structured error model can face a different optimization problem. Such structure must be established in the exact destination statistic rather than inferred from this bound.

The cusp cancellation is exact because the limiting sine-kernel support-edge profile is `|q|` on `[-b,b]`. The result does not by itself show that a zeta-specific source term has a quartic Taylor coefficient, or that such a coefficient survives finite-height transfer and cross-window dependence.

The finite-window remainder statement inherits the moment assumptions and Taylor regime of `VIS-146`. If the relevant source moments grow so quickly that `M_6(H)b^2` is not controlled relative to `|mu_4(H)|`, the quartic truncation need not be useful.

No untouched confirmation-zero data are used.

## Research consequence

The accepted support-edge residual clue can now replace the qualitative “cusp-adapted quartic-or-higher” branch by a sharp quantitative gate.

If the redesign retains `m_2`, `VIS-257` says that unit quadratic sensitivity costs exactly `8b^-2`. If it also cancels `m_2`, the best possible unit quartic carrier costs exactly `K_*b^-4` with `K_*=15.7575716928...`, and any total-variation-linear transfer uncertainty must beat `E_*|A_4|b^4` rather than merely the generic `|A_4|b^4` scale.

The next mathematical question is therefore no longer packet existence or normalization. It is whether the actual zeta-minus-null destination has a source-specific quartic coefficient and a theorem/transfer/covariance error budget small enough to survive this sharp conditioning gate. Until that coefficient and error law are derived, adding further moment cancellations would only move the carrier to a more expensive order without evidence that the destination supplies it.