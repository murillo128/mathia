# VIS-216 — normalized magnetic ground states give a scale-free torus-frustration certificate

## Claim

Keep the finite Hermitian zero-diagonal matrix setup of `VIS-213`--`VIS-215`. On an oriented support edge `e=u->v`, write

`A_(u,v)=w_e exp(i theta_e)`, with `w_e>0`,

and let

`d_u=sum_(v: {u,v} in E) w_(u,v)`

be the weighted support degree. Discard isolated vertices, which contribute neither to `G(z)=z^*Az` nor to the coefficient envelope, and write `D=diag(d_u)`.

Define the two magnetic/connection Laplacians

`L_+ = D-A`,

`L_- = D+A = D-(-A)`

and their normalized forms

`calL_+ = D^(-1/2) L_+ D^(-1/2)`,

`calL_- = D^(-1/2) L_- D^(-1/2)`.

For each connected support component `K`, let `B_K=sum_(u in K)d_u=2 sum_(e in K)w_e`, and let `lambda_+(K)` and `lambda_-(K)` be the smallest eigenvalues of the restrictions of `calL_+` and `calL_-` to that component. Put

`S_+ = sum_K B_K lambda_+(K)`,

`S_- = sum_K B_K lambda_-(K)`.

Then every torus point `|z_u|=1` satisfies

`B(A)-G(z) >= S_+`,

`B(A)+G(z) >= S_-`,

where `B(A)=sum_u d_u=2 sum_e w_e`. Hence

`max_(|z_u|=1) |z^*Az| <= B(A)-min(S_+,S_-)`.

Equivalently, with the coefficient-mass-weighted normalized ground-state averages

`bar_lambda_+ = S_+/B(A)`,

`bar_lambda_- = S_-/B(A)`,

one has the scale-free envelope bound

`max |z^*Az| / B(A) <= 1-min(bar_lambda_+,bar_lambda_-)`.

This recovers the exact balance boundary of `VIS-214`: on a connected component, `lambda_+=0` exactly when the original gain is balanced, and `lambda_-=0` exactly when the shifted gain `-g` is balanced. The spectral quantity is therefore a quantitative relaxation of the same gauge-invariant obstruction, not a new phase statistic.

The certificate also combines monotonically with the fractional cycle-packing bound of `VIS-215`. If `P_+` and `P_-` are the two optimal packing rewards there, then

`max |z^*Az|`
` <= B(A)-min(max(S_+,P_+), max(S_-,P_-))`.

Finally, the Haar variance of the torus quadratic form is

`R(A)=int |z^*Az|^2 dz = 2 sum_e w_e^2`.

Let

`N_eff = (sum_e w_e)^2 / sum_e w_e^2`.

Then

`B(A)/sqrt(R(A)) = sqrt(2 N_eff)`.

Therefore this normalized spectral certificate can prove an RMS-scale bound

`max |z^*Az| = O(sqrt(R(A)))`

only if

`1-min(bar_lambda_+,bar_lambda_-) = O(N_eff^(-1/2))`.

A magnetic ground-state gap merely bounded away from zero gives only a constant-fraction improvement over the absolute coefficient envelope. When `N_eff -> infinity`, matching the Haar RMS scale through this route requires the relevant normalized ground states to approach the maximal scale `1` at the much sharper `N_eff^(-1/2)` rate.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL-CONNECTION-LAPLACIAN SPECTRAL SPECIALIZATION + SCALE-DIAGNOSTIC + NO-NOVELTY-CLAIM`.

No new Cheeger inequality, synchronization theorem, magnetic-Laplacian theorem, prime asymptotic, or RH consequence is claimed.

## 1. The torus deficits are exactly magnetic Dirichlet energies

For `z_u=exp(i phi_u)`, `VIS-215` writes

`G(z)=2 sum_e w_e cos(theta_e+phi_v-phi_u)`

and

`E_+(z)=B(A)-G(z)`,

`E_-(z)=B(A)+G(z)`.

Expanding one edge gives

`w_e |z_u-exp(i theta_e)z_v|^2`
` = 2w_e-2w_e Re(conjugate(z_u) exp(i theta_e) z_v)`.

Summing over support edges therefore gives exactly

`E_+(z)=z^* L_+ z`.

Replacing every edge gain by its negative gives

`E_-(z)=z^* L_- z`.

Thus the positive and negative coefficient-envelope deficits are not merely analogous to synchronization energies: they are the two connection-Laplacian quadratic forms restricted to the unit-modulus torus.

## 2. Degree normalization turns the ground-state eigenvalue into a coefficient-mass fraction

Fix one connected support component `K`. Set

`y=D_K^(1/2) z_K`.

Then

`z_K^* L_(+,K) z_K = y^* calL_(+,K) y`.

Because every torus coordinate has modulus one,

`||y||^2 = z_K^* D_K z_K = sum_(u in K) d_u = B_K`.

The Rayleigh principle therefore gives

`E_(+,K)(z) >= lambda_+(K) B_K`.

The same argument for `L_-` gives

`E_(-,K)(z) >= lambda_-(K) B_K`.

Summing over components proves the displayed `S_+` and `S_-` bounds.

Using components rather than the smallest eigenvalue of the full disconnected graph is essential. One balanced component would otherwise force the global smallest eigenvalue to zero even though other components can carry unavoidable frustration. The coefficient-mass-weighted sum preserves every component's contribution.

For a connected component, the normalized magnetic Laplacian is positive semidefinite. Its smallest eigenvalue is zero precisely when the gain can be switched to the trivial gain; for `L_-` this is the same statement applied to the shifted gain `-g`. This is the standard spectral form of balance and matches the cycle-holonomy criterion in `VIS-214`.

## 3. Spectral and cycle-packing certificates are complementary lower bounds on the same energy

Let

`eta_+ = B(A)^(-1) min_(|z_u|=1) E_+(z)`,

`eta_- = B(A)^(-1) min_(|z_u|=1) E_-(z)`.

These are the exact normalized positive/negative torus-frustration energies. The connection-Laplacian relaxation gives

`eta_+ >= S_+/B(A)=bar_lambda_+`,

`eta_- >= S_-/B(A)=bar_lambda_-`.

`VIS-215` independently gives

`eta_+ >= P_+/B(A)`,

`eta_- >= P_-/B(A)`.

Neither lower bound is asserted to dominate the other on every weighted gain graph. The spectral bound relaxes the fixed-modulus condition and captures global geometry through an eigenvalue; the packing bound keeps explicit cycle holonomies but relaxes their interaction through edge capacities. Taking the larger certificate separately for each sign is therefore always valid and can only sharpen the envelope bound.

This also clarifies what the spectral route forgets. A ground-state eigenvector of `calL_+` or `calL_-` may have highly nonuniform amplitudes, whereas the actual torus optimization fixes every vertex amplitude to one. The spectral gap is consequently a safe lower bound on unit-modulus frustration, not an exact formula for the torus optimum.

## 4. Haar RMS exposes how strong the static certificate must become

Under Haar measure on the vertex torus, distinct character frequencies are orthogonal. Since `A` is Hermitian with zero diagonal,

`int |z^*Az|^2 dz = sum_(u != v) |A_(u,v)|^2 = 2 sum_e w_e^2`.

This is the abstract form of the variance identity used for the prime matrix in `VIS-213`.

Write

`W_1=sum_e w_e`,

`W_2=sum_e w_e^2`.

Then

`B(A)=2W_1`,

`R(A)=2W_2`,

and hence

`B(A)/sqrt(R(A)) = sqrt(2) W_1/sqrt(W_2) = sqrt(2N_eff)`.

The quantity `N_eff=W_1^2/W_2` is the usual inverse-concentration/effective-count scale of the edge weights. It equals the number of edges when all nonzero weights are equal and becomes much smaller when the coefficient mass is concentrated on a few edges.

The spectral envelope bound reads

`max |G| <= B(A)[1-min(bar_lambda_+,bar_lambda_-)]`.

Consequently a proof of `max |G| <= C sqrt(R(A))` from this certificate alone requires

`1-min(bar_lambda_+,bar_lambda_-) <= C / sqrt(2N_eff)`.

This is a useful negative calibration. Showing only `bar_lambda_± >= delta>0` leaves an upper bound of order `B(A)`, which can still exceed the RMS scale by `Theta(sqrt(N_eff))`. Static frustration must therefore be almost maximally spectral, not merely nonzero or uniformly positive, before this particular relaxation can collapse the worst-start envelope to the Haar scale.

The same calibration applies to any lower-bound certificate inserted in place of `S_±`: to prove RMS-scale suppression through `VIS-215`, one needs `min(P_+,P_-)=B(A)-O(sqrt(R(A)))`. A visually dense collection of frustrated cycles is not enough unless its certified weight is nearly the full coefficient mass on the effective-edge scale.

## 5. Prior-art boundary

The connection-Laplacian and magnetic-Laplacian framework is classical. Afonso S. Bandeira, Amit Singer, and Daniel A. Spielman, **A Cheeger Inequality for the Graph Connection Laplacian**, *SIAM Journal on Matrix Analysis and Applications* 34:4 (2013), 1611--1630, DOI `10.1137/120875338`, relates synchronization quality to the spectrum of the graph connection Laplacian.

Carsten Lange, Shiping Liu, Norbert Peyerimhoff, and Olaf Post, **Frustration index and Cheeger inequalities for discrete and continuous magnetic Laplacians**, *Calculus of Variations and Partial Differential Equations* 54 (2015), 4165--4196, DOI `10.1007/s00526-015-0935-x`, treats weighted `U(1)` signatures, switching/gauge invariance, frustration, magnetic Laplacians, and first-eigenvalue Cheeger inequalities.

These sources rule out novelty claims based on using a connection/magnetic ground-state eigenvalue as a frustration measure or on the equivalence between zero ground-state energy and balance. The inequalities in this finding are direct Rayleigh-quotient specializations to the exact `VIS-213` torus objective.

The Mathia-specific value is the normalization: the unit-modulus objective has `z^*Dz=B(A)` exactly, so the normalized magnetic ground state measures a literal fraction of coefficient-envelope deficit. Combining that with the exact Haar variance yields the `N_eff^(-1/2)` near-one requirement for this spectral route to reach RMS scale.

## 6. Prime-phase consequence and remaining gate

For the prime coefficient matrix `A_(y,H)` of `VIS-213`, the static worst-start problem now has three nested deterministic descriptions:

- `VIS-214`: cycle holonomy decides exact coefficient-envelope attainability;
- `VIS-215`: fractional weighted cycle packing lower-bounds unavoidable torus frustration;
- this finding: the normalized magnetic ground state supplies a global spectral lower bound and reveals the strength required to reach the Haar RMS scale.

The immediate arithmetic target is therefore not merely to prove a positive magnetic spectral gap. If the effective edge count of `A_(y,H)` grows, a constant gap still permits an envelope-scale worst start. To make this relaxation alone prove RMS-scale pointwise suppression, one needs

`min(bar_lambda_+(y,H),bar_lambda_-(y,H))`
` = 1-O(N_eff(y,H)^(-1/2))`.

That may be too strong, in which case the spectral route is primarily a diagnostic or a component of a sharper certificate rather than the final pointwise theorem. Determining the actual asymptotic ground-state behavior of the prime-weighted magnetic graph, comparing it with the cycle-packing reward, and understanding whether the fixed-modulus torus minimum is substantially larger than the relaxed spectral minimum are separate later questions.

The one-parameter access-time problem remains untouched. Even a sharp static torus bound says nothing about how quickly the prime-log orbit approaches extremal torus regions as dimension grows.