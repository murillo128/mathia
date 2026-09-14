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

`X>=0`, `X_ii=1`,

and put `U_-(A)=U_+(-A)`. Its dual is

`U_+(A)=min sum_i d_i`

subject to

`Diag(d)-A>=0`, `d_i in R`.

Then:

1. `M_+(A)<=U_+(A)` and `M_-(A)<=U_-(A)`, so

   `M_abs(A)<=U_abs(A):=max(U_+(A),U_-(A))`.

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

   `U_+(A)<=B(A)-S_+`.

   The same construction for `-A` gives `U_-(A)<=B(A)-S_-`. Therefore the correlation SDP is a genuinely stronger certificate class than the specific normalized magnetic-ground-state relaxation: the `VIS-216` bound is one explicit feasible dual point inside it.

4. Let

   `B(A)=2 sum_e w_e`,

   `R(A)=2 sum_e w_e^2`,

   `N_eff=(sum_e w_e)^2/(sum_e w_e^2)`

   as in `VIS-216`--`VIS-220`. Since every feasible correlation matrix has `|X_ij|<=1`, one has `U_+,U_-<=B`. Define

   `Delta_+^SDP=B-U_+`,

   `Delta_-^SDP=B-U_-`.

   Then exactly

   `U_abs/sqrt(R)`
   ` = sqrt(2N_eff) [1-min(Delta_+^SDP,Delta_-^SDP)/B]`.

   Consequently this relaxation reaches Haar-RMS scale only if its smaller signed deficit reaches

   `B-O(sqrt(R))`.

5. `VIS-222` supplies the missing converse comparison using the classical complex symmetric Grothendieck inequality:

   `U_abs(A) <= K_gamma^C M_abs(A)`,

   with `K_gamma^C<=8/pi-1`. Hence the full correlation SDP and exact torus optimum are universally constant-factor equivalent in objective value. A large high-rank SDP optimum may fail to recover the exact optimizer, but it cannot be an arbitrarily loose multiplicative upper bound.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL-SDP/KKT SPECIALIZATION + STRICT CERTIFICATE-HIERARCHY CLARIFICATION + LATER CONSTANT-FACTOR CLOSURE VIA VIS-222 + NO-NOVELTY-CLAIM`.

No polynomial-time exact solution of the unit-modulus quadratic problem, asymptotic prime-specific SDP estimate, exact universal relaxation constant, or RH consequence is claimed.

## 1. The correlation SDP and its dual

Lift a torus vector to

`X=zz^*`.

Then `X>=0`, `X_ii=1`, `rank(X)=1`, and

`Tr(A X)=z^*Az`.

Dropping only the rank-one constraint gives the displayed SDP, so `M_+<=U_+`. The feasible set is compact, and `X=I` is strictly positive definite with the required diagonal, so standard SDP strong duality applies. The Lagrangian dual is

`min sum_i d_i`

subject to `Diag(d)-A>=0`.

The same construction applied to `-A` controls the negative side of the absolute torus objective.

For any feasible `X`, positive semidefiniteness and `X_ii=1` imply from the `2x2` principal minors that `|X_ij|<=1`. Therefore

`Tr(A X)<=sum_(i!=j)|A_ij|=B(A)`,

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

`z^*Az<=M_+<=U_+<=sum_i d_i(z)=z^*Az`.

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

## 4. Destination-scale calibration and the later two-sided closure

Let

`Delta_+^SDP=B-U_+`, `Delta_-^SDP=B-U_-`.

Because

`U_abs=max(B-Delta_+^SDP,B-Delta_-^SDP)`
`     =B-min(Delta_+^SDP,Delta_-^SDP)`,

and `B/sqrt(R)=sqrt(2N_eff)`, the normalized certificate is exactly

`U_abs/sqrt(R)`
` =sqrt(2N_eff)[1-min(Delta_+^SDP,Delta_-^SDP)/B]`.

Thus when `N_eff` diverges, a constant-fraction envelope improvement is not enough. Reaching RMS scale requires both signed upper bounds to be `O(sqrt(R))`, equivalently a deficit from both coefficient envelopes equal to `B-O(sqrt(R))`.

The original version of this finding left open the possibility that `U_abs` might remain parametrically large only because the correlation relaxation is high rank. `VIS-222` removes that ambiguity by identifying `U_abs` and `M_abs` with the `gamma` and `theta` seminorms in the complex symmetric Grothendieck inequality. It proves

`M_abs<=U_abs<=K_gamma^C M_abs`,

`K_gamma^C<=8/pi-1`.

Accordingly, rank affects optimizer recovery but not asymptotic objective scale beyond a universal factor. A bounded `U_abs/sqrt(R)` gives a bounded exact torus ratio, while a divergent `U_abs/sqrt(R)` also forces the exact torus ratio to diverge.

## 5. Prior art and novelty boundary

Semidefinite relaxation of unit-modulus quadratic optimization and dual optimality certificates are classical. Mojtaba Soltanalian and Petre Stoica, **Designing Unimodular Codes via Quadratic Optimization**, *IEEE Transactions on Signal Processing* 62:5 (2014), 1221--1234, treats unimodular quadratic programming and semidefinite relaxation as standard tools.

Afonso S. Bandeira, Nicolas Boumal, and Amit Singer, **Tightness of the maximum likelihood semidefinite relaxation for angular synchronization**, *Mathematical Programming* 163:1--2 (2017), 145--167, DOI `10.1007/s10107-016-1059-6`, studies the phase-synchronization setting where the nonconvex unit-circle problem is relaxed to an SDP and tightness is certified through optimality conditions.

The later constant-factor comparison is classical symmetric-Grothendieck prior art and is recorded separately in `VIS-222`. No novelty is claimed for the primal/dual pair, complementary slackness, stress certificate, Grothendieck inequality, or approximation factor.

The Mathia-specific contribution of this finding is the placement of the correlation SDP in the live `VIS-213` worst-start problem and the exact hierarchy it exposes: the normalized magnetic bound of `VIS-216` is a restricted dual stress inside the full correlation SDP, while `VIS-222` subsequently shows that the full SDP itself is a universal constant-factor surrogate for the exact torus objective.

## Boundaries and falsification

The stress condition `S_z>=0` certifies global optimality only for a stationary candidate and the positive objective `A`; the negative side must be tested by applying the same construction to `-A`. A torus-global maximizer need not satisfy this PSD stress condition when the SDP has a genuine relaxation gap. Therefore absence of a rank-one stress certificate is not evidence that a candidate is not the true torus optimum.

A high-rank SDP solution is not a mathematical model of independent prime phases. It is a convex correlation relaxation. By `VIS-222`, however, its **optimal value** cannot exceed the exact unit-modulus optimum by more than the universal complex symmetric-Grothendieck factor.

Falsify the main certificate by finding an error in the SDP dual, strong duality, the stationary identity `(Az)_i=d_i z_i`, complementary slackness, or the componentwise dual embedding of the `VIS-216` magnetic eigenvalue. The two-sided objective comparison is independently falsifiable through the dictionary audited in `VIS-222`.

## Research consequence

The simple-cycle packing branch is closed, but the full correlation SDP remains a principled route to the static torus scale. For the canonical prime matrices `A_(y,H)`, determine

`U_abs(y,H)/sqrt(R_v(y,H))`.

`VIS-222` means this is no longer merely a certificate-quality diagnostic: it determines the exact fixed-modulus worst-start scale within a universal factor. If the ratio stays bounded, the exact torus optimum is at RMS scale. If it diverges, the exact torus optimum also diverges relative to RMS. Rank-one stress remains valuable for exact finite optimizers, and one-parameter orbit access time remains a separate problem.