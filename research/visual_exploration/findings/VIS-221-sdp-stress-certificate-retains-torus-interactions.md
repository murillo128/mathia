# VIS-221 — semidefinite stress certificates retain the full torus interaction

## Claim

Keep the finite Hermitian zero-diagonal matrix setup of `VIS-213`--`VIS-220`. For

`G_A(z)=z^*Az`, `|z_i|=1`,

write

`M_+(A)=max_(|z_i|=1) G_A(z)`,

`M_-(A)=M_+(-A)`,

and `M_abs(A)=max(M_+(A),M_-(A))`.

Consider the standard correlation-matrix semidefinite relaxation

`U_+(A)=max Tr(A X)`

subject to

`X >= 0`, `X_ii=1`,

and put `U_-(A)=U_+(-A)`. Its dual is

`U_+(A)=min sum_i d_i`

subject to

`Diag(d)-A >= 0`, `d_i in R`.

Then:

1. `M_+(A) <= U_+(A)` and `M_-(A) <= U_-(A)`, so

   `M_abs(A) <= U_abs(A):=max(U_+(A),U_-(A))`.

2. Let `z` be a stationary torus point for `G_A`, so every

   `d_i(z)=conjugate(z_i)(Az)_i`

   is real. Define the Hermitian stress matrix

   `S_z=Diag(d(z))-A`.

   Then `S_z z=0`. If `S_z>=0`, the point `z` is a global maximizer of the original unit-modulus problem and the SDP is rank-one exact:

   `M_+(A)=U_+(A)=z^*Az`.

   Conversely, if `X=zz^*` is an optimal rank-one solution of the SDP, then necessarily `S_z>=0`. Thus positive semidefiniteness of the stationary stress is an exact a-posteriori certificate for rank-one SDP tightness.

3. The normalized magnetic certificate of `VIS-216` is already contained inside this SDP dual. Let `D=diag(deg_w(i))`, `L_+=D-A`, and on each connected support component `K` let `lambda_+(K)` be the smallest eigenvalue of `D_K^(-1/2)L_(+,K)D_K^(-1/2)`. If

   `S_+=sum_K B_K lambda_+(K)`, `B_K=sum_(i in K) deg_w(i)`,

   then the dual choice

   `d_i=(1-lambda_+(K)) deg_w(i)`, `i in K`,

   is feasible because

   `Diag(d)-A=L_(+,K)-lambda_+(K)D_K>=0`

   on every component. Hence

   `U_+(A) <= B(A)-S_+`.

   The same construction for `-A` gives `U_-(A)<=B(A)-S_-`. Therefore the correlation SDP is a genuinely stronger certificate class than the specific normalized magnetic-ground-state relaxation: the `VIS-216` bound is one explicit feasible dual point inside it.

4. Let

   `B(A)=2 sum_e w_e`,

   `R(A)=2 sum_e w_e^2`,

   `N_eff=(sum_e w_e)^2/(sum_e w_e^2)`

   as in `VIS-216`--`VIS-220`. Since every feasible correlation matrix has `|X_ij|<=1`, one has `U_+,U_-<=B`. Define SDP deficit certificates

   `Delta_+^SDP=B-U_+`,

   `Delta_-^SDP=B-U_-`.

   Then exactly

   `U_abs/sqrt(R)`
   ` = sqrt(2N_eff) [1-min(Delta_+^SDP,Delta_-^SDP)/B]`.

   Consequently this stronger relaxation proves a Haar-RMS-scale pointwise bound only if its smaller signed deficit reaches

   `B-O(sqrt(R))`,

   equivalently

   `1-min(Delta_+^SDP,Delta_-^SDP)/B=O(N_eff^(-1/2))`.

Unlike the normalized magnetic relaxation closed in `VIS-218` and the simple-cycle packing relaxation closed in `VIS-220`, no universal obstruction is established here that prevents the correlation SDP from reaching that scale. The exact fixed-modulus problem has therefore not been replaced by another already-exhausted certificate: the SDP supplies a stronger global interaction test and, when rank-one tight, an exact finite-dimensional solution certificate.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL-SDP/KKT SPECIALIZATION + STRICT CERTIFICATE-HIERARCHY CLARIFICATION + NO-NOVELTY-CLAIM`.

No polynomial-time solution of the unit-modulus quadratic problem, asymptotic SDP tightness theorem, prime-specific spectral estimate, or RH consequence is claimed.

## 1. The correlation SDP and its dual

Lift a torus vector to

`X=zz^*`.

Then `X>=0`, `X_ii=1`, `rank(X)=1`, and

`Tr(A X)=z^*Az`.

Dropping only the rank-one constraint gives the displayed SDP, so `M_+<=U_+`. The feasible set is compact, and `X=I` is strictly positive definite with the required diagonal, so ordinary SDP strong duality applies. The Lagrangian dual is

`min sum_i d_i`

subject to `Diag(d)-A>=0`.

The same construction applied to `-A` controls the negative side of the absolute torus objective.

For any feasible `X`, positive semidefiniteness and `X_ii=1` imply by the `2x2` principal minors that `|X_ij|<=1`. Therefore

`Tr(A X) <= sum_(i!=j)|A_ij|=B(A)`,

so the SDP remains inside the same coefficient envelope used throughout `VIS-214`--`VIS-220`.

## 2. A stationary torus point carries its own exact dual stress

Write `z_i=exp(i phi_i)`. Differentiating `G_A(z)` with respect to `phi_i` gives the first-order condition

`Im(conjugate(z_i)(Az)_i)=0`.

Thus at a stationary point

`d_i(z)=conjugate(z_i)(Az)_i`

is real. Since `|z_i|=1`, this is equivalent to

`(Az)_i=d_i(z)z_i`,

hence

`S_z z=[Diag(d(z))-A]z=0`.

If `S_z>=0`, then `d(z)` is dual feasible. Its dual objective is

`sum_i d_i(z)=sum_i conjugate(z_i)(Az)_i=z^*Az`.

The rank-one primal matrix `zz^*` has the same value. Weak duality therefore collapses to equality:

`z^*Az <= M_+ <= U_+ <= sum_i d_i(z)=z^*Az`.

So `z` is globally optimal and the SDP is exact.

Conversely, suppose `zz^*` is an optimal SDP solution. Strong duality gives an optimal dual diagonal `D_*` with slack `S_*=D_*-A>=0`. Complementary slackness gives

`Tr(S_*zz^*)=z^*S_*z=0`.

For a positive semidefinite matrix this forces `S_*z=0`. Therefore

`(D_*z)_i=(Az)_i`,

so, because `|z_i|=1`,

`(D_*)_ii=conjugate(z_i)(Az)_i=d_i(z)`.

Hence `S_*=S_z>=0`. This proves the stated equivalence with rank-one SDP tightness.

The certificate is global and a-posteriori: a numerical or analytic candidate phase assignment is not accepted because it looks coherent or satisfies a local fixed-point equation. It is certified only when the associated full Hermitian stress is positive semidefinite.

## 3. The magnetic ground-state bound is a restricted SDP dual ansatz

`VIS-216` defines on each connected component

`L_+=D-A`

and the normalized smallest eigenvalue `lambda_+(K)`. By the Rayleigh principle,

`L_(+,K)-lambda_+(K)D_K>=0`.

Set on that component

`Diag(d_K)=(1-lambda_+(K))D_K`.

Then

`Diag(d_K)-A_K=L_(+,K)-lambda_+(K)D_K>=0`,

so this is a feasible SDP dual point. Its objective is

`sum_(i in K)d_i=(1-lambda_+(K))B_K`.

Summing over components gives

`U_+(A)<=B-S_+`,

exactly the positive-envelope spectral certificate in `VIS-216`. Applying the same argument to `-A` gives the negative certificate.

This identifies precisely what the SDP adds. The magnetic relaxation restricts the dual diagonal on each component to be proportional to weighted degree, controlled by one scalar ground-state eigenvalue. The full SDP permits an independent real dual stress on every vertex while enforcing the complete positive-semidefinite coupling. It can therefore retain heterogeneous interactions that the componentwise spectral normalization discards.

This does not prove that the improvement is asymptotically sufficient. It proves only that the new certificate family strictly contains the old spectral ansatz and is not ruled out by `VIS-218` merely because that particular ansatz fails.

## 4. Destination-scale calibration survives unchanged

Let

`Delta_+^SDP=B-U_+`, `Delta_-^SDP=B-U_-`.

Because

`U_abs=max(B-Delta_+^SDP,B-Delta_-^SDP)`
`     =B-min(Delta_+^SDP,Delta_-^SDP)`,

and `B/sqrt(R)=sqrt(2N_eff)`, the normalized certificate is exactly

`U_abs/sqrt(R)`
` =sqrt(2N_eff)[1-min(Delta_+^SDP,Delta_-^SDP)/B]`.

Thus the lesson of `VIS-219` remains the correct gate for every stronger certificate: when `N_eff` diverges, a constant-fraction envelope improvement is not enough. The SDP must drive both signed upper bounds down to within `O(sqrt(R))` of zero, or equivalently certify a deficit from both coefficient envelopes equal to `B-O(sqrt(R))`.

There is an important asymmetry in how to interpret failure. If the SDP reaches `O(sqrt(R))`, then the exact torus optimum is automatically at most that scale. If the SDP remains much larger, this does **not** lower-bound the exact torus optimum; it may indicate only an SDP relaxation gap. Rank-one tightness, or a matching torus lower bound, is needed before a large SDP value can be interpreted as a genuine large worst start.

## 5. Prior-art and novelty boundary

Semidefinite relaxation of unit-modulus quadratic optimization and dual optimality certificates are classical. Mojtaba Soltanalian and Petre Stoica, **Designing Unimodular Codes via Quadratic Optimization**, *IEEE Transactions on Signal Processing* 62:5 (2014), 1221--1234, treats unimodular quadratic programming and semidefinite relaxation as standard tools.

Afonso S. Bandeira, Nicolas Boumal, and Amit Singer, **Tightness of the maximum likelihood semidefinite relaxation for angular synchronization**, *Mathematical Programming* 163:1--2 (2017), 145--167, DOI `10.1007/s10107-016-1059-6`, studies exactly the phase-synchronization setting where the nonconvex unit-circle problem is relaxed to an SDP and tightness is certified through optimality conditions.

The primal/dual pair, complementary-slackness argument, and stationary stress certificate above are therefore not claimed as new optimization theory. The Mathia-specific content is their placement in the live `VIS-213` worst-start problem and the exact hierarchy they expose: the normalized magnetic bound of `VIS-216` is a restricted dual stress inside the correlation SDP, while the failed simple-cycle and spectral certificates do not by themselves close this stronger global interaction route.

## Boundaries and falsification

The stress condition `S_z>=0` certifies global optimality only for a stationary candidate and the positive objective `A`; the negative side must be tested by applying the same construction to `-A`. A torus-global maximizer need not satisfy this PSD stress condition when the SDP has a genuine relaxation gap. Therefore absence of a rank-one stress certificate is not evidence that the candidate is not the true torus optimum.

Likewise, a high-rank SDP solution is not a mathematical model of independent prime phases. It is only a convex correlation relaxation used to upper-bound the deterministic fixed-modulus objective.

Falsify the main certificate by finding an error in the SDP dual, strong duality, the stationary identity `(Az)_i=d_i z_i`, complementary slackness, or the componentwise dual embedding of the `VIS-216` magnetic eigenvalue.

## Research consequence

The simple-cycle packing branch is closed, but the exact static torus problem still has a principled next certificate. For the canonical prime matrices `A_(y,H)`, determine the signed correlation-SDP values and compare

`U_abs(y,H)/sqrt(R_v(y,H))`

with the diverging envelope ratio `sqrt(2N_eff)`. If the SDP ratio stays bounded, it proves an RMS-scale static worst-start bound without solving the nonconvex torus problem. If a rank-one optimizer appears and its stationary stress is positive semidefinite, the finite torus optimum is certified exactly. If the SDP ratio itself diverges while the relaxation is high-rank, only the certificate route has failed; the exact torus optimum remains open.
