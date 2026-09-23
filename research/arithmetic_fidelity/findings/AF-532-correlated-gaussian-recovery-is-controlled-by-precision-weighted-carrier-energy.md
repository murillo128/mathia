# AF-532 — Correlated Gaussian recovery is controlled by precision-weighted carrier energy

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `ARITHMETIC-FIDELITY` · `STOCHASTIC-NOISE` · `CORRELATED-GAUSSIAN` · `GENERALIZED-LEAST-SQUARES` · `CARRIER-SHAPE` · `FINITE-RESOLUTION` · `MINIMAX` · `EXPERIMENT-EQUIVALENCE` · `RECOVERY-BOUNDARY` · `NO-NOVELTY-CLAIM`

## Claim

AF-530 gives the compact-uniform rank-one boundary-profile expansion

\[
F_{A,\theta}(u)
=
\delta_A\bigl(u(1-\theta)+r_{A,\theta}(u)\bigr),
\qquad
\delta_A:=\frac{\log A}{A\log\log A},
\tag{1}
\]

for \(\theta\) in a fixed nondegenerate compact interval

\[
K=[\theta_-,\theta_+]\Subset(0,1),
\tag{2}
\]

with

\[
\rho_A:=
\sup_{\theta\in K}\sup_{0\le u\le1}|r_{A,\theta}(u)|
\longrightarrow0.
\tag{3}
\]

AF-531 proved the sharp stochastic recovery law when the sampled errors are independent with common variance. The independence assumption can be removed exactly, but raw sample count is then replaced by the geometry of the noise covariance.

Choose deterministic sample locations

\[
u_{A,1},\ldots,u_{A,n_A}\in[0,1]
\tag{4}
\]

such that the carrier vector

\[
\mathbf u_A=(u_{A,1},\ldots,u_{A,n_A})^T
\tag{5}
\]

is nonzero. Put

\[
\mathbf r_{A,\theta}
=
\bigl(r_{A,\theta}(u_{A,1}),\ldots,r_{A,\theta}(u_{A,n_A})\bigr)^T.
\tag{6}
\]

Observe

\[
Y_A
=
\delta_A\bigl((1-\theta)\mathbf u_A+\mathbf r_{A,\theta}\bigr)
+\varepsilon_A,
\qquad
\varepsilon_A\sim N(0,\Sigma_A),
\tag{7}
\]

where \(\Sigma_A\) is known, positive definite, and independent of \(\theta\).

Write

\[
\|x\|_{\Sigma_A^{-1}}^2:=x^T\Sigma_A^{-1}x
\tag{8}
\]

and define the **precision-weighted carrier information**

\[
\boxed{
J_A
:=
\delta_A^2\|\mathbf u_A\|_{\Sigma_A^{-1}}^2
=
\delta_A^2\mathbf u_A^T\Sigma_A^{-1}\mathbf u_A.
}
\tag{9}
\]

The AF-530 remainder must be small in the same observation geometry. Define

\[
\beta_A
:=
\sup_{\theta\in K}
\frac{\|\mathbf r_{A,\theta}\|_{\Sigma_A^{-1}}}
{\|\mathbf u_A\|_{\Sigma_A^{-1}}}
\tag{10}
\]

and assume

\[
\boxed{\beta_A\to0.}
\tag{11}
\]

Then:

1. for every fixed distinct \(\theta,\eta\in K\),

\[
\boxed{
D_{\mathrm{KL}}(P_{A,\theta}\|P_{A,\eta})
=
\frac12(\theta-\eta)^2J_A(1+o(1));
}
\tag{12}
\]

2. uniform consistent recovery of \(\theta\) under absolute-error loss is possible **if and only if**

\[
\boxed{J_A\to\infty;}
\tag{13}
\]

3. if \(J_A\to j\in(0,\infty)\), the full correlated Gaussian experiment is asymptotically equivalent, uniformly over \(\theta\in K\), to the scalar Gaussian location experiment

\[
\boxed{
Z=\theta+j^{-1/2}G,
\qquad G\sim N(0,1);
}
\tag{14}
\]

4. if \(J_A\to0\), every fixed pair of parameter values becomes asymptotically indistinguishable in total variation.

Thus the correct stochastic fidelity resource is not \(n_A\), and not independence as a binary property. It is the squared carrier amplitude measured in the **precision geometry** of the observation channel.

A compound-symmetric covariance makes the distinction explicit. Let

\[
\Sigma_A
=
\sigma^2\bigl((1-\varrho_A)I_{n_A}+\varrho_A\mathbf1\mathbf1^T\bigr),
\qquad
0\le\varrho_A<1,
\tag{15}
\]

with fixed \(\sigma>0\). Define the empirical design mean and variance

\[
m_A=\frac1{n_A}\sum_i u_{A,i},
\qquad
v_A=\frac1{n_A}\sum_i(u_{A,i}-m_A)^2.
\tag{16}
\]

Then exactly

\[
\boxed{
J_A
=
\frac{\delta_A^2}{\sigma^2}
\left[
\frac{n_Av_A}{1-\varrho_A}
+
\frac{n_Am_A^2}{1-\varrho_A+n_A\varrho_A}
\right].
}
\tag{17}
\]

This produces two opposite regimes.

**Repeated-point design.** If all samples are taken at the same fixed \(u_0>0\), then \(v_A=0\), \(m_A=u_0\), condition (11) follows directly from (3), and

\[
\boxed{
J_A
=
\frac{\delta_A^2u_0^2}{\sigma^2}
\frac{n_A}{1+(n_A-1)\varrho_A}.
}
\tag{18}
\]

For any fixed positive correlation floor \(\varrho_A\ge\varrho_0>0\),

\[
J_A\le
\frac{\delta_A^2u_0^2}{\sigma^2\varrho_0}
\longrightarrow0,
\tag{19}
\]

no matter how quickly \(n_A\to\infty\). Arbitrarily many repeated measurements then fail to recover \(\theta\). More generally, repeated-point recovery is possible exactly when

\[
\boxed{
\frac{\delta_A^2 n_A}
{1+(n_A-1)\varrho_A}
\to\infty.
}
\tag{20}
\]

In the correlation-dominated regime \(n_A\varrho_A\to\infty\), this requires \(\varrho_A=o(\delta_A^2)\).

**Spread design.** If instead

\[
v_A\ge v_0>0,
\qquad
\varrho_A\le\varrho_*<1,
\tag{21}
\]

then the AF-530 sup-norm remainder already implies (11), and

\[
J_A\asymp n_A\delta_A^2.
\tag{22}
\]

Hence the AF-531 inverse-square sample threshold survives in order even under a fixed common-mode correlation. The varying sample locations create a contrast component of the carrier that the common mode cannot mimic.

Correlation therefore does not have a monotone interpretation such as “fewer effective samples” independent of design. What matters is the alignment between the retained carrier direction and the noisy covariance eigenspaces.

## Derivation

### 1. Pairwise distinguishability is the Mahalanobis carrier norm

For fixed \(\theta,\eta\in K\), equation (7) gives

\[
\mu_{A,\theta}-\mu_{A,\eta}
=
\delta_A\left((\eta-\theta)\mathbf u_A
+\mathbf r_{A,\theta}-\mathbf r_{A,\eta}\right).
\tag{23}
\]

By (10),

\[
\|\mathbf r_{A,\theta}-\mathbf r_{A,\eta}\|_{\Sigma_A^{-1}}
\le
2\beta_A\|\mathbf u_A\|_{\Sigma_A^{-1}}.
\tag{24}
\]

For every fixed separation \(d=|\theta-\eta|>0\), the triangle inequality therefore yields

\[
\frac{
\|\mu_{A,\theta}-\mu_{A,\eta}\|_{\Sigma_A^{-1}}
}{
\delta_A d\|\mathbf u_A\|_{\Sigma_A^{-1}}
}
=1+o(1).
\tag{25}
\]

Two Gaussian laws with the same covariance satisfy

\[
D_{\mathrm{KL}}
\bigl(N(\mu_0,\Sigma)\|N(\mu_1,\Sigma)\bigr)
=
\frac12(\mu_0-\mu_1)^T\Sigma^{-1}(\mu_0-\mu_1).
\tag{26}
\]

Equations (9), (25), and (26) prove (12).

### 2. Generalized least squares gives the recovery upper bound

Define

\[
T_A
:=
1-
\frac{
\mathbf u_A^T\Sigma_A^{-1}Y_A
}{
\delta_A\mathbf u_A^T\Sigma_A^{-1}\mathbf u_A
}
\tag{27}
\]

and project onto the parameter interval,

\[
\widehat\theta_A=\Pi_K(T_A).
\tag{28}
\]

The bias satisfies, uniformly in \(\theta\),

\[
|\mathbb E_\theta T_A-\theta|
=
\left|
\frac{
\mathbf u_A^T\Sigma_A^{-1}\mathbf r_{A,\theta}
}{
\mathbf u_A^T\Sigma_A^{-1}\mathbf u_A
}
\right|
\le\beta_A
\tag{29}
\]

by Cauchy-Schwarz in the \(\Sigma_A^{-1}\) inner product.

The noise variance is exactly

\[
\operatorname{Var}_\theta(T_A)
=
\frac1{J_A}.
\tag{30}
\]

Projection onto an interval cannot increase distance to \(\theta\in K\), so

\[
\boxed{
\sup_{\theta\in K}
\mathbb E_\theta|\widehat\theta_A-\theta|
\le
\beta_A
+
\sqrt{\frac2\pi}\,J_A^{-1/2}.
}
\tag{31}
\]

Thus \(J_A\to\infty\), together with (11), implies uniform consistency.

### 3. Bounded precision-weighted information prevents consistency

Suppose \(J_A\) does not diverge. Along some subsequence,

\[
J_A\le M<\infty.
\tag{32}
\]

Choose fixed interior \(\theta_0,\theta_1\in K\) with separation \(d>0\) small enough that \(d^2M/2\) is below a fixed testing constant. By (12), their KL divergence remains uniformly small along that subsequence. Pinsker's inequality then keeps the corresponding total-variation distance bounded strictly below one.

The standard two-point testing bound gives a fixed positive lower bound on worst-case absolute-error risk over \(\{\theta_0,\theta_1\}\). Hence no estimator can be uniformly consistent on \(K\) unless \(J_A\to\infty\). Together with (31), this proves (13).

If \(J_A\to0\), (12) and Pinsker immediately imply pairwise total-variation collapse, proving statement 4.

### 4. At bounded information the whole experiment becomes one scalar Gaussian coordinate

Remove the AF-530 remainder and consider

\[
\widetilde P_{A,\theta}
=
N\!\left(\delta_A(1-\theta)\mathbf u_A,\Sigma_A\right).
\tag{33}
\]

The Mahalanobis size of the omitted mean term is bounded uniformly by

\[
\delta_A
\|\mathbf r_{A,\theta}\|_{\Sigma_A^{-1}}
\le
\sqrt{J_A}\,\beta_A.
\tag{34}
\]

Therefore, whenever \(J_A\) is bounded, (11) implies

\[
\sup_{\theta\in K}
\|P_{A,\theta}-\widetilde P_{A,\theta}\|_{\mathrm{TV}}
\to0.
\tag{35}
\]

Whiten the rank-one experiment by \(\Sigma_A^{-1/2}\). Its mean lies entirely in the one-dimensional span of

\[
\Sigma_A^{-1/2}\mathbf u_A.
\tag{36}
\]

Every orthogonal Gaussian coordinate is parameter-free. Equivalently, the scalar generalized-least-squares statistic

\[
Z_A
:=
1-
\frac{
\mathbf u_A^T\Sigma_A^{-1}Y_A
}{
\delta_A\mathbf u_A^T\Sigma_A^{-1}\mathbf u_A
}
\tag{37}
\]

is, in the rank-one comparison experiment, exactly

\[
Z_A\sim N(\theta,J_A^{-1}).
\tag{38}
\]

If \(J_A\to j\in(0,\infty)\), equations (35)--(38) prove the experiment limit (14).

### 5. Compound symmetry separates common-mode and contrast information

For (15), the inverse covariance is

\[
\Sigma_A^{-1}
=
\frac1{\sigma^2(1-\varrho_A)}
\left[
I
-
\frac{\varrho_A}
{1-\varrho_A+n_A\varrho_A}
\mathbf1\mathbf1^T
\right].
\tag{39}
\]

Because

\[
\|\mathbf u_A\|_2^2=n_A(v_A+m_A^2),
\qquad
(\mathbf1^T\mathbf u_A)^2=n_A^2m_A^2,
\tag{40}
\]

substitution into (9) gives

\[
\mathbf u_A^T\Sigma_A^{-1}\mathbf u_A
=
\frac1{\sigma^2}
\left[
\frac{n_Av_A}{1-\varrho_A}
+
\frac{n_Am_A^2}{1-\varrho_A+n_A\varrho_A}
\right],
\tag{41}
\]

which proves (17).

For repeated sampling at \(u_0\), the carrier and the remainder are both constant-coordinate vectors. Hence

\[
\beta_A
=
\sup_{\theta\in K}
\frac{|r_{A,\theta}(u_0)|}{u_0}
\le\frac{\rho_A}{u_0}
\to0,
\tag{42}
\]

and (18)--(20) follow from (17).

For the spread design (21), positive semidefiniteness of the removed common-mode term in (39) gives

\[
\|\mathbf r_{A,\theta}\|_{\Sigma_A^{-1}}^2
\le
\frac{n_A\rho_A^2}{\sigma^2(1-\varrho_A)},
\tag{43}
\]

whereas (41) gives

\[
\|\mathbf u_A\|_{\Sigma_A^{-1}}^2
\ge
\frac{n_Av_0}{\sigma^2(1-\varrho_A)}.
\tag{44}
\]

Thus

\[
\beta_A\le\rho_A/\sqrt{v_0}\to0.
\tag{45}
\]

Since \(u_{A,i}\in[0,1]\) and \(\varrho_A\le\varrho_*<1\), equation (17) also yields constants \(0<c<C<\infty\), independent of \(A\), such that

\[
c\,n_A\delta_A^2
\le J_A\le
C\,n_A\delta_A^2,
\tag{46}
\]

proving (22).

## Prior-art / novelty audit

The covariance-weighted estimation machinery is classical.

A. C. Aitken, **“On Least Squares and Linear Combination of Observations,”** *Proceedings of the Royal Society of Edinburgh* 55, 42–48 (1936), DOI `10.1017/S0370164600014346`, is foundational prior art for inverse-covariance weighting and least squares with correlated observations.

George Zyskind and Frank B. Martin, **“On Best Linear Estimation and General Gauss-Markov Theorem in Linear Models with Arbitrary Nonnegative Covariance Structure,”** *SIAM Journal on Applied Mathematics* 17(6), 1190–1202 (1969), DOI `10.1137/0117110`, treats general known covariance structure and records that, in the multivariate-normal case, the generalized least-squares estimator is also maximum likelihood.

David L. Donoho, **“Statistical Estimation and Optimal Recovery,”** *The Annals of Statistics* 22(1), 238–270 (1994), DOI `10.1214/aos/1176325367`, is the same optimal-recovery background used in AF-531 for statistical estimation from indirect data under Gaussian noise.

The equal-covariance Gaussian KL identity, whitening reduction, rank-one sufficiency, compound-symmetry inverse, and generalized-least-squares estimator used here are standard finite-dimensional calculations. No novelty is claimed for them.

The durable Arithmetic Fidelity content is their exact specialization to the AF-530 carrier collapse. AF-531's independent-noise quantity

\[
S_A^2
=
\frac{\delta_A^2}{\sigma_A^2}\sum_i u_{A,i}^2
\]

is not the fundamental invariant; it is the diagonal-covariance specialization of (9). Equation (17) then exhibits a source-specific design/correlation dichotomy: common-mode correlation can completely destroy the gain from infinitely many repeated observations while leaving the inverse-square threshold intact for designs whose carrier has a nonvanishing contrast component.

## Boundaries and falsification audit

1. **The covariance is known and parameter-independent.** If \(\Sigma_A\) is unknown, must be estimated, or depends on \(\theta\), the covariance itself may carry or obscure parameter information. None of those experiments is classified here.

2. **The precision geometry must also see the AF-530 remainder as negligible.** Sup-norm smallness (3) alone does not imply (11) for an arbitrary ill-conditioned \(\Sigma_A\). A covariance whose precision explodes along a remainder direction can promote nominally lower-order shape into leading information. Condition (11) is therefore a genuine compatibility gate, not a technical decoration.

3. **Correlation is not intrinsically information loss.** Equation (17) shows that the same positive common-mode correlation that saturates repeated-point information can be rejected by a spread design through contrasts. More generally, covariance eigenvalues matter only through their alignment with the carrier and remainder directions.

4. **Singular covariance is excluded.** Generalized inverses can extend the algebra, but a zero-noise direction can change the experiment qualitatively and requires a separate support-level classification.

5. **Gaussianity remains load bearing for the exact KL and scalar-experiment statements.** Broader regular correlated-noise families may have analogous local information laws, but they are not proved here.

6. **No rational-prime discriminator is recovered.** The theorem classifies how one already-retained AF-530 anchor parameter survives a correlated observation channel. It does not show that the carrier distinguishes rational primes from matched generalized-prime or other admissible arithmetic controls.

For this concrete carrier the lesson is exact: stochastic sample accumulation is a geometric resource. The recoverability threshold is determined by \(\delta_A^2\mathbf u_A^T\Sigma_A^{-1}\mathbf u_A\), and sample count is informative only insofar as the added observations enlarge that precision-weighted carrier energy.