# AF-533 — Gaussian nuisance quotients are governed by transverse precision energy

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `ARITHMETIC-FIDELITY` · `STOCHASTIC-NOISE` · `CORRELATED-GAUSSIAN` · `NUISANCE-QUOTIENT` · `GENERALIZED-LEAST-SQUARES` · `EFFICIENT-FISHER-INFORMATION` · `MINIMAX` · `RECOVERY-BOUNDARY` · `NO-NOVELTY-CLAIM`

## Claim

AF-490 showed in a deterministic norm-bounded channel that an unrestricted linear nuisance removes exactly the discriminator component lying in the nuisance subspace: raw sensitivity is replaced by a quotient norm. AF-532 showed in a correlated Gaussian channel with no nuisance that raw carrier energy is replaced by precision-weighted energy. These are not separate corrections. In the Gaussian linear setting they compose exactly into one invariant: **distance from the carrier to the nuisance subspace in the precision geometry of the noise**.

Let

\[
Y_A
=
\delta_A\bigl((1-\theta)\mathbf u_A+\mathbf r_{A,\theta}\bigr)
+B_A\gamma_A
+\varepsilon_A,
\qquad
\varepsilon_A\sim N(0,\Sigma_A),
\tag{1}
\]

where:

- \(\theta\in K=[\theta_-,\theta_+]\Subset(0,1)\) is the target;
- \(\gamma_A\in\mathbb R^{k_A}\) is an unrestricted nuisance;
- \(B_A\in\mathbb R^{n_A\times k_A}\) has full column rank;
- \(\Sigma_A\) is known, positive definite, and independent of \((\theta,\gamma_A)\);
- \(\mathbf u_A\) is the sampled AF-530 carrier; and
- \(\mathbf r_{A,\theta}\) is the sampled AF-530 remainder.

Write \(W_A=\Sigma_A^{-1}\) and define the residual precision operator

\[
P_A
:=
W_A
-W_AB_A(B_A^TW_AB_A)^{-1}B_A^TW_A.
\tag{2}
\]

Then

\[
P_AB_A=0,
\qquad
P_A\Sigma_AP_A=P_A,
\tag{3}
\]

and

\[
\boxed{
\mathbf u_A^TP_A\mathbf u_A
=
\inf_{b\in\operatorname{col}(B_A)}
\|\mathbf u_A-b\|_{W_A}^2.
}
\tag{4}
\]

The correct nuisance-invariant information scale is therefore

\[
\boxed{
J_A^\perp
:=
\delta_A^2\mathbf u_A^TP_A\mathbf u_A
=
\delta_A^2
\operatorname{dist}_{W_A}
\bigl(\mathbf u_A,\operatorname{col}(B_A)\bigr)^2.
}
\tag{5}
\]

For the exact rank-one mean family \(\mathbf r_{A,\theta}=0\), equation (5) is simultaneously:

1. the squared norm of the carrier surviving the nuisance quotient after whitening;
2. the minimum Mahalanobis separation between two target values after optimally adjusting their nuisance parameters;
3. the efficient Fisher information for \(\theta\), obtained as the Schur complement of the nuisance block; and
4. the inverse variance of the optimal nuisance-annihilating scalar Gaussian coordinate.

Moreover, if \(\mathbf u_A\in\operatorname{col}(B_A)\), then \(J_A^\perp=0\) and the rank-one target is **exactly non-identifiable**: every target change can be absorbed by the nuisance.

For the perturbed AF-530 family, suppose \(\mathbf u_A^TP_A\mathbf u_A>0\) eventually and define

\[
\beta_A^\perp
:=
\sup_{\theta\in K}
\frac{
\sqrt{\mathbf r_{A,\theta}^TP_A\mathbf r_{A,\theta}}
}{
\sqrt{\mathbf u_A^TP_A\mathbf u_A}
}.
\tag{6}
\]

If

\[
\boxed{\beta_A^\perp\to0,}
\tag{7}
\]

then uniform consistent recovery of \(\theta\), uniformly over the unrestricted nuisance \(\gamma_A\), is possible **if and only if**

\[
\boxed{J_A^\perp\to\infty.}
\tag{8}
\]

Thus AF-490 and AF-532 combine into a single rule:

> **first measure the discriminator in the observation channel's precision geometry, then quotient the directions that the nuisance can imitate. Only the transverse precision energy is recoverable.**

The loss relative to AF-532 is exact. With

\[
J_A
=
\delta_A^2\mathbf u_A^TW_A\mathbf u_A,
\tag{9}
\]

one has

\[
\boxed{
J_A-J_A^\perp
=
\delta_A^2
(B_A^TW_A\mathbf u_A)^T
(B_A^TW_AB_A)^{-1}
(B_A^TW_A\mathbf u_A)
\ge0.
}
\tag{10}
\]

Hence a nuisance does not impose a generic scalar penalty such as “lose \(k_A\) samples.” It removes precisely the component of the carrier lying in the nuisance span under the metric selected by the noise channel.

## Representation declaration

The source event for this finding is the AF-530 boundary-profile family together with a declared Gaussian observation channel and an unrestricted linear nuisance action.

- **Source object \(X_A\):** \((\theta,\gamma_A)\) together with the mean profile \(\delta_A((1-\theta)\mathbf u_A+\mathbf r_{A,\theta})+B_A\gamma_A\).
- **Forward map \(T_A\):** addition of \(N(0,\Sigma_A)\) noise, followed conceptually by quotienting observations under translations by \(\operatorname{col}(B_A)\).
- **Represented object:** the nuisance-invariant Gaussian experiment obtained after whitening and projecting away the whitened nuisance subspace.
- **Target observable:** \(\theta\), under absolute-error loss uniformly over \(\gamma_A\).
- **Equivalence:** observations differing by a nuisance translation \(B_Ah\) carry the same admissible target information because \(\gamma_A\) is unrestricted.

The theorem is representation-relative: changing the nuisance class, bounding \(\gamma_A\), changing the covariance model, or allowing the covariance to depend on the target changes the quotient experiment. No source-level arithmetic conclusion is inferred from the Gaussian representation itself.

## Exact Gaussian quotient geometry

### Whitening turns the problem into an ordinary orthogonal quotient

Let

\[
C_A=\Sigma_A^{-1/2}B_A,
\qquad
x_A=\Sigma_A^{-1/2}\mathbf u_A.
\tag{11}
\]

Let \(\Pi_{C_A}\) be the Euclidean orthogonal projector onto \(\operatorname{col}(C_A)\). Direct calculation gives

\[
P_A
=
\Sigma_A^{-1/2}
(I-\Pi_{C_A})
\Sigma_A^{-1/2}.
\tag{12}
\]

Therefore

\[
\mathbf u_A^TP_A\mathbf u_A
=
\|(I-\Pi_{C_A})x_A\|_2^2.
\tag{13}
\]

This proves (4): the statistically visible carrier is exactly the whitened carrier after orthogonal removal of the whitened nuisance span.

The order matters conceptually. A naive Euclidean projection of \(\mathbf u_A\) away from \(\operatorname{col}(B_A)\) is generally not the efficient quotient when \(\Sigma_A\) is nonspherical. The correct projection is defined by the precision metric, equivalently by whitening first.

### Pairwise separation after nuisance optimization

For the exact rank-one family, two target-nuisance states have mean difference

\[
\Delta\mu
=
\delta_A(\eta-\theta)\mathbf u_A
+B_Ah,
\tag{14}
\]

where \(h\) is the difference between nuisance vectors. Minimizing its squared Mahalanobis norm gives

\[
\begin{aligned}
\inf_h\|\Delta\mu\|_{W_A}^2
&=
\delta_A^2(\theta-\eta)^2
\mathbf u_A^TP_A\mathbf u_A\\
&=
(\theta-\eta)^2J_A^\perp.
\end{aligned}
\tag{15}
\]

Indeed, the minimizer solves

\[
(B_A^TW_AB_A)h
=-\delta_A(\eta-\theta)B_A^TW_A\mathbf u_A,
\tag{16}
\]

and substitution gives (15).

Since equal-covariance Gaussian KL divergence is one half of squared Mahalanobis separation, the smallest KL divergence between the two composite target fibres is exactly

\[
\boxed{
\inf_{\gamma,\gamma'}
D_{\mathrm{KL}}
\bigl(P_{A,\theta,\gamma}\|P_{A,\eta,\gamma'}\bigr)
=
\frac12(\theta-\eta)^2J_A^\perp.
}
\tag{17}
\]

This is the stochastic analogue of AF-490's deterministic statement that target separation must be measured only after quotienting nuisance directions.

### The nuisance-annihilating coordinate

Assume \(Q_A:=\mathbf u_A^TP_A\mathbf u_A>0\). Define

\[
T_A
:=
1-
\frac{\mathbf u_A^TP_AY_A}
{\delta_AQ_A}.
\tag{18}
\]

Because \(P_AB_A=0\), the statistic is exactly independent of the nuisance mean. In the rank-one family,

\[
\boxed{
T_A\sim N\!\left(\theta,(J_A^\perp)^{-1}\right)
}
\tag{19}
\]

for every \(\gamma_A\). The variance identity follows from

\[
P_A\Sigma_AP_A=P_A.
\tag{20}
\]

After whitening, all residual coordinates orthogonal to \((I-\Pi_{C_A})x_A\) are parameter-free. Thus the nuisance-invariant rank-one experiment contains exactly one target-bearing Gaussian coordinate, and its information is (5).

### Efficient Fisher information is the same quantity

For the exact mean family, the joint Fisher matrix for \((\theta,\gamma_A)\) is

\[
\mathcal I_A
=
\begin{pmatrix}
\delta_A^2\mathbf u_A^TW_A\mathbf u_A
&
-\delta_A\mathbf u_A^TW_AB_A\\
-\delta_AB_A^TW_A\mathbf u_A
&
B_A^TW_AB_A
\end{pmatrix}.
\tag{21}
\]

The Schur complement of the nuisance block is

\[
\mathcal I_{A,\mathrm{eff}}(\theta)
=
\delta_A^2\mathbf u_A^TP_A\mathbf u_A
=
J_A^\perp.
\tag{22}
\]

Equation (10) is therefore also the exact Fisher-information loss caused by making \(\gamma_A\) unknown rather than known. This is the finite-dimensional Gaussian nuisance-score projection mechanism behind the quotient norm.

## Perturbed AF-530 profile: sharp recovery boundary

Return to (1) and assume (7). The statistic (18) now satisfies

\[
\mathbb E_{\theta,\gamma_A}T_A-\theta
=
-
\frac{
\mathbf u_A^TP_A\mathbf r_{A,\theta}
}{Q_A}.
\tag{23}
\]

Cauchy-Schwarz in the seminorm induced by \(P_A\) gives

\[
\sup_{\theta,\gamma_A}
|\mathbb E T_A-\theta|
\le
\beta_A^\perp.
\tag{24}
\]

The variance remains exactly

\[
\operatorname{Var}(T_A)
=
(J_A^\perp)^{-1}.
\tag{25}
\]

Projecting \(T_A\) to \(K\) cannot increase its distance from the true \(\theta\). Hence

\[
\boxed{
\sup_{\theta\in K}\sup_{\gamma_A\in\mathbb R^{k_A}}
\mathbb E_{\theta,\gamma_A}
|\widehat\theta_A-\theta|
\le
\beta_A^\perp
+
\sqrt{\frac2\pi}\,(J_A^\perp)^{-1/2}.
}
\tag{26}
\]

Thus (7) and \(J_A^\perp\to\infty\) imply uniform consistency.

For necessity, define the quotient pairwise divergence

\[
D_A^\perp(\theta,\eta)
:=
\inf_{\gamma,\gamma'}
D_{\mathrm{KL}}
\bigl(P_{A,\theta,\gamma}\|P_{A,\eta,\gamma'}\bigr).
\tag{27}
\]

The same nuisance minimization as above gives exactly

\[
D_A^\perp(\theta,\eta)
=
\frac{\delta_A^2}{2}
\left\|
(\eta-\theta)\mathbf u_A
+\mathbf r_{A,\theta}-\mathbf r_{A,\eta}
\right\|_{P_A}^2,
\tag{28}
\]

where \(\|x\|_{P_A}^2=x^TP_Ax\). For every fixed distinct \(\theta,\eta\), condition (7) yields

\[
\boxed{
D_A^\perp(\theta,\eta)
=
\frac12(\theta-\eta)^2J_A^\perp(1+o(1)).
}
\tag{29}
\]

If \(J_A^\perp\) does not diverge, pass to a subsequence with \(J_A^\perp\le M\). Choose two fixed interior target values separated by a sufficiently small \(d>0\). Equation (29) then keeps the KL divergence between suitably chosen nuisance states below a fixed testing constant. Pinsker's inequality and the standard two-point testing bound give a positive lower bound on worst-case absolute-error risk along that subsequence. No estimator can therefore be uniformly consistent over \(K\times\mathbb R^{k_A}\).

This proves (8). If \(J_A^\perp\to0\), every fixed target pair has nuisance representatives whose total-variation distance tends to zero.

At bounded \(J_A^\perp\), condition (7) also makes the projected remainder negligible in the nuisance-invariant experiment: its whitened transverse norm is at most \(\sqrt{J_A^\perp}\,\beta_A^\perp\). Hence the quotient experiment reduces asymptotically to the scalar Gaussian coordinate (19), exactly as AF-532 reduces the no-nuisance experiment after whitening.

## Compound symmetry with an unknown common offset

The interaction with AF-532 becomes explicit for

\[
\Sigma_A
=
\sigma^2\bigl((1-\varrho_A)I_{n_A}
+\varrho_A\mathbf1\mathbf1^T\bigr),
\qquad
0\le\varrho_A<1,
\tag{30}
\]

and an unrestricted common-offset nuisance

\[
B_A=\mathbf1.
\tag{31}
\]

Let

\[
m_A=\frac1{n_A}\sum_i u_{A,i},
\qquad
v_A=\frac1{n_A}\sum_i(u_{A,i}-m_A)^2.
\tag{32}
\]

Because the constant vector is a covariance eigendirection, precision-weighted nuisance removal is ordinary centering on the contrast subspace, and

\[
P_A
=
\frac1{\sigma^2(1-\varrho_A)}
\left(I-\frac1{n_A}\mathbf1\mathbf1^T\right).
\tag{33}
\]

Therefore

\[
\boxed{
J_A^\perp
=
\frac{\delta_A^2}{\sigma^2}
\frac{n_Av_A}{1-\varrho_A}.
}
\tag{34}
\]

Compare this with AF-532's known-offset information

\[
J_A
=
\frac{\delta_A^2}{\sigma^2}
\left[
\frac{n_Av_A}{1-\varrho_A}
+
\frac{n_Am_A^2}{1-\varrho_A+n_A\varrho_A}
\right].
\tag{35}
\]

The nuisance quotient deletes the second term **exactly**. Common-mode carrier energy is not merely noisy; it is inadmissible evidence about \(\theta\) because an unrestricted offset can reproduce it.

Two consequences are sharp.

**Repeated-point design.** If all \(u_{A,i}=u_0\), then \(v_A=0\) and \(J_A^\perp=0\). In fact the entire mean in (1), including the AF-530 remainder, is a constant vector because all samples use the same location. Every target-dependent mean can therefore be absorbed into the unknown offset. Repeating the same point arbitrarily many times gives exact non-identifiability, not merely the information saturation found in AF-532 when the offset is known.

**Spread design.** If \(v_A\ge v_0>0\) and \(\varrho_A\le\varrho_*<1\), then the AF-530 uniform remainder \(\rho_A\to0\) implies

\[
\beta_A^\perp
\le
\frac{\rho_A}{\sqrt{v_A}}
\to0,
\tag{36}
\]

and

\[
J_A^\perp\asymp n_A\delta_A^2.
\tag{37}
\]

Thus the inverse-square sampling threshold from AF-531 survives in order only through **transverse design spread**. Absolute mean level contributes nothing once the common offset is nuisance.

This example separates two effects that a scalar “effective sample size” would conflate. Correlation determines the metric in which contrasts are measured; nuisance symmetry determines which directions are admissible at all.

## Composition law for fidelity resources

Equations (12) and (13) expose a useful composition principle for linear Gaussian compression.

Start with the carrier \(\mathbf u_A\). The Gaussian channel applies the whitening map

\[
\mathbf u_A
\longmapsto
\Sigma_A^{-1/2}\mathbf u_A.
\tag{38}
\]

The nuisance quotient then applies the orthogonal projection

\[
\Sigma_A^{-1/2}\mathbf u_A
\longmapsto
(I-\Pi_{\Sigma_A^{-1/2}B_A})
\Sigma_A^{-1/2}\mathbf u_A.
\tag{39}
\]

The squared norm of the result, multiplied by \(\delta_A^2\), is exactly \(J_A^\perp\). Hence two apparently different forms of information loss—correlated observational noise and nuisance non-identifiability—compose as ordinary Hilbert-space geometry after the representation has selected its natural metric.

This is stronger than saying “project out the nuisance.” The metric used to define “out” is itself part of the channel. The same algebra explains why Euclidean residualization can be inefficient under nonspherical errors and why the generalized least-squares residualization is the correct invariant operation.

Equation (10) also gives an exact local lift criterion. If additional side information removes some nuisance directions or turns them into known quantities, the recovered information is precisely the corresponding reduction of the projection defect. A lift need not reconstruct the whole source; it must restore enough of the carrier component currently lying in the nuisance tangent space.

## Prior art and novelty audit

The statistical and linear-algebraic ingredients are classical. No theorem-level novelty is claimed for generalized least squares, nuisance-score projection, Schur complements, or the weighted Frisch-Waugh mechanism.

- Abram Kagan and C. R. Rao, **“Some properties and applications of the efficient Fisher score,”** *Journal of Statistical Planning and Inference* 116(2), 343–352 (2003), DOI `10.1016/S0378-3758(02)00351-8`. This is direct prior art for efficient Fisher scores and information matrices in the presence of nuisance parameters, including normal linear-regression structure.
- Denzil G. Fiebig and Robert Bartels, **“The Frisch-Waugh theorem and generalized least squares,”** *Econometric Reviews* 15(4), 431–443 (1996), DOI `10.1080/07474939608800365`. This is direct prior art for correct residualization in nonspherical linear regression and for the distinction between naive residualization and efficient GLS residualization.
- R. M. Fewster and P. E. Jupp, **“Information on parameters of interest decreases under transformations,”** *Journal of Multivariate Analysis* 120, 34–39 (2013), DOI `10.1016/j.jmva.2013.05.010`. This treats Fisher information for parameters of interest with nuisance parameters through partitioned information matrices and Schur complements.
- David L. Donoho, **“Statistical Estimation and Optimal Recovery,”** *Annals of Statistics* 22(1), 238–270 (1994), DOI `10.1214/aos/1176325367`. This supplies the broader minimax/indistinguishability viewpoint already used in AF-490 and the surrounding recovery line.

The new value inside Arithmetic Fidelity is therefore not a new regression theorem. It is the exact synthesis of two previously separate line-local resource laws. AF-490's quotient norm and AF-532's precision energy are the same construction at different layers: after Gaussian noise chooses the precision metric, nuisance symmetry replaces the carrier norm by its quotient norm in that metric. This closes AF-532's explicit “no nuisance” boundary and turns the interaction into a reusable fidelity rule.

## Falsification and boundary audit

1. **The nuisance must be genuinely unrestricted for exact quotienting.** Bounds, priors, penalties, repeated experiments sharing structured nuisance, or side information can make nuisance-parallel carrier components informative again.

2. **The covariance is known and parameter-independent.** If \(\Sigma_A\) is unknown, estimated, singular, nuisance-dependent, or target-dependent, whitening is no longer a fixed lossless coordinate change and additional information/uncertainty enters.

3. **The nuisance enters linearly in the mean.** Nonlinear nuisance manifolds require tangent-space projection only locally; the global quotient may have curvature, multiple fibres, or non-identifiability not captured by one matrix \(B_A\).

4. **Condition (7) is load-bearing.** AF-530 gives a small remainder in sup norm, but a badly conditioned precision/nuisance geometry can amplify its transverse component. The remainder must be negligible in the same quotient geometry used by the theorem.

5. **The exact non-identifiability claim concerns the rank-one carrier, unless the full remainder is also nuisance-valued.** A remainder can in principle contain extra target information transverse to \(B_A\). The repeated-point/common-offset example is stronger because its full sampled remainder is also constant and is therefore absorbed exactly.

6. **Gaussianity makes KL, whitening, and the scalar quotient coordinate exact.** Elliptical or non-Gaussian noise may retain the same linear quotient intuition but need not have information determined solely by covariance or by (5).

7. **Efficient Fisher information is local statistical fidelity, not arithmetic provenance.** A large \(J_A^\perp\) only says that the AF-530 anchor parameter survives the declared Gaussian+nuisance observation model. It does not show that rational-prime identity, ordering, or another arithmetic discriminator survives the earlier construction.

8. **No sample-count heuristic replaces (5).** Increasing \(n_A\) can add zero information when new carrier coordinates lie in the nuisance span, can add ordinary order-\(n_A\) contrast information, or can behave differently under changing covariance geometry.

## Relationship to AF-490, AF-532, and the line mandate

AF-490 proved the deterministic quotient principle: under norm-bounded error, the recoverable discriminator is measured by distance to the nuisance subspace. AF-532 proved the correlated-Gaussian precision principle: without nuisance, the recoverable carrier is measured by its Mahalanobis norm. AF-533 shows that the common generalization is not an ad hoc compromise but the canonical weighted quotient norm (5).

This supplies a concrete answer to one of the line's central questions about composition of compressions. A first transformation can change the geometry in which distinguishability is measured; a second quotient can then erase directions relative to that geometry. What survives the chain is computed by applying both operations to the carrier, not by multiplying two scalar retention factors.

For later arithmetic applications, the operational test is therefore sharper: before assigning value to a prime-derived carrier direction, identify the observation metric and every nuisance symmetry at that layer, whiten in the declared channel geometry, quotient the nuisance directions, and only then ask whether the rational-prime discriminator still has nonzero—and sufficiently growing—transverse energy.