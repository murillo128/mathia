# Arithmetic-fidelity research lines

This file records the current mathematical questions that survive the Arithmetic-Fidelity evidence. It is not a roadmap, task queue, status page, or history.

## Which source relations remain observable after matched controls, nuisance closure and the actual representation map?

AF-523--AF-528 show that leading scalar boundary-curvature data can be matched while an exact relational carrier still retains hidden source shape. For power-separated anchors, the projective logarithmic derivative of the exact carrier recovers the anchor exponent, but the signal is infinitesimal and therefore does not by itself give a stable finite-resolution observable.

AF-533--AF-538 identify the correct nuisance-relative geometry. In Gaussian and regular semiparametric models the retained target information is the component of the efficient score transverse to the **closed** downstream nuisance-plus-invisible space. For finite-dimensional targets this becomes a positive-semidefinite efficient-information matrix: the fidelity subspace is the kernel of the stagewise information loss, and the end-to-end fidelity spectrum records which target combinations survive compression. Algebraic injectivity, raw sample count or an unprojected carrier norm is not the relevant stability notion.

AF-539--AF-541 then isolate a genuine exact-carrier shape coordinate for the prime-prefix model with scalar tail-multiplier nuisance. The first projective log-slope can be cancelled only when the multiplier reaches its explicit logarithmic threshold, while every fixed higher log-jet annihilates the unbounded affine multiplier direction. More importantly, the two-point contrast

`Q_(A,h)=log R_A(h)-(1+h)log R_A(0)`

removes that unbounded multiplier exactly and, at `h=A^(-1)`, recovers `1-theta` after the normalization `log log A/(h log A)`.

AF-542 shows why this exact-carrier theorem cannot simply be transported through raw normalized curvature: the first nonlinear carrier-to-curvature correction is small at value level but becomes dominant after the shrinking two-point discriminator is applied. The correct transfer criterion is therefore error control in the **seminorm induced by the downstream discriminator**, not a pointwise `1+o(1)` approximation.

AF-543 supplies the first successful curvature-native repair for this model. Writing the normalized curvature defect in terms of the source carrier `D` and the canonical prime reference coordinate

`r(t)=M_1(t)^2/[M_0(t)M_2(t)]`,

the exact map `D -> g_r(D)` is locally invertible in the physical small-`D` regime. Inverting it before taking the relational contrast reconstructs a calibrated carrier `D^sharp` and restores the AF-541 anchor-scale limit. This is a genuine representation-level result: the nonlinear curvature defect can be removed without access to the hidden cutoff carrier itself, but only after retaining the additional reference coordinate `r(t)`.

AF-544 makes the calibration burden quantitative. At the physical endpoint, the leading approximation `r(t)~1/log(1/t)` is not accurate enough after the transverse discriminator; the finite-part constant in the prime-zeta expansion becomes load-bearing. Using

`r(t)=1/[log(1/t)+beta_P]+O(t/log(1/t))`

crosses the common-calibration accuracy threshold in the AF-543 regime, whereas omitting `beta_P` produces a downstream error larger than the target signal. The finding also separates common-mode calibration error from differential error: common errors enjoy cancellation in the relational ratio, while independently varying errors must be controlled at a much finer scale.

AF-545 identifies the exact general mechanism behind that common-mode cancellation. For a locally invertible observation `y=G(z,u)` and readout `q`, the inverse-calibration field

`K_q(z,u)=-q'(z) G_u(z,u)/G_z(z,u)`

satisfies `d q(Phi_u(z))/du=K_q(Phi_u(z),u)`. A shared-calibration contrast between two decoded sources therefore differentiates to the **difference** of their inverse sensitivities, not to either absolute sensitivity. All pairwise contrasts are exactly calibration-invariant iff `K_q` is independent of the source coordinate, equivalently the calibration flow acts as a translation in the readout coordinate. Away from that exact quotient, the relevant error budget is the variation of `K_q` across the compared branches; differential calibration instead couples to their average sensitivity. This criterion is invariant under smooth reparameterization of the latent coordinate and is general inverse-problem geometry, not prime-specific evidence.

AF-546 extends this from translation nuisance to an exact low-degree hierarchy. In the readout coordinate `Q=q(z)`, every decoded branch obeys the common scalar flow `partial_u Q=V(Q,u)`. Two-point differences remove the nuisance exactly iff `V` is constant in `Q`; three-point ratios of differences are invariant iff `V` is affine; four-point cross-ratios are invariant iff `V` is quadratic, equivalently the common flow is locally Riccati/projective. The converse statements hold on connected local intervals under the stated regularity. Thus one extra matched branch can enlarge the exactly quotiented nuisance class without first reconstructing `u`, while departures from these classes are measured by the corresponding `Q`-derivatives of `V`. This is a structural inverse-problem theorem, not evidence that the prime-prefix nuisance actually lies in one of the larger classes.

The live question is therefore no longer whether **some** nonlinear curvature correction exists for the exact prime-prefix model. It is to classify the smallest source-natural relational lift that removes the nuisance class actually induced after the physical representation map, and to prove its stability in the destination-induced seminorm. AF-545--AF-546 sharpen the test from branchwise reconstruction error to the geometry of the common calibration field: translation, affine and projective nuisance require respectively two, three and four matched branches for exact low-arity invariants. A successful arithmetic extension must show that the required matched branches and shared calibration are genuinely available from the source, distinguish common from differential nuisance directions, and survive matched generalized sources. AF-543--AF-546 establish a calibrated normal form, its precision threshold and the general relational quotient hierarchy; they do not yet produce an arithmetic discriminator or an RH mechanism.

## Classify quotient-visible contact through admission and no-contact accessibility rates

AF-495--AF-508 isolate a separate fidelity mechanism in critical translated-distance problems. Closed quotient geometry determines the asymptotic threshold, membership of the nearest transverse point in the actual quotient image determines whether finite-time contact occurs, and the admission height determines when a plateau begins. In the no-contact branch the exact carrier is the accessibility profile: with `rho(r)=dist(0,C_r)^2-lambda^2`, the distance excess is the one-sided quadratic envelope `inf_r [rho(r)+(r-t)_+^2]`.

The unresolved step is arithmetic realization rather than abstract convex geometry. Identify a natural arithmetic nuisance quotient and admission rule, determine whether its critical transverse point is admitted, and in the no-contact case prove a source-derived law for `rho` (or its inverse admission profile) strong enough to survive the quadratic envelope. Only after actual contact exists do pointwise source attainment and compactness of the retained contact fibre become relevant.
