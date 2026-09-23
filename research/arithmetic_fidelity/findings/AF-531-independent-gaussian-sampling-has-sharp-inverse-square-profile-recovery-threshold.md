# AF-531 — Independent Gaussian sampling has a sharp inverse-square profile-recovery threshold

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `ARITHMETIC-FIDELITY` · `STOCHASTIC-NOISE` · `GAUSSIAN-SHIFT` · `CARRIER-SHAPE` · `FINITE-RESOLUTION` · `MINIMAX` · `SAMPLE-COMPLEXITY` · `RECOVERY-BOUNDARY` · `NO-NOVELTY-CLAIM`

## Claim

AF-530 proves that the anchored boundary profile in the AF-527 co-tuned control family has the compact-uniform rank-one expansion

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

where

\[
\rho_A
:=
\sup_{\theta\in K}\sup_{0\le u\le1}
|r_{A,\theta}(u)|
\longrightarrow0.
\tag{3}
\]

AF-530 then shows that under deterministic adversarial sup-norm error, denser access to the same profile does not improve the recovery scale \(\delta_A\).

For **independent Gaussian sample noise**, the answer is different and admits a sharp criterion.

Choose any deterministic design

\[
u_{A,1},\ldots,u_{A,n_A}\in[0,1]
\tag{4}
\]

satisfying the nondegeneracy condition

\[
q_A
:=
\frac1{n_A}\sum_{i=1}^{n_A}u_{A,i}^2
\ge q_0>0.
\tag{5}
\]

Observe

\[
Y_{A,i}
=
F_{A,\theta}(u_{A,i})
+
\sigma_A\xi_{A,i},
\qquad
\xi_{A,i}\stackrel{\mathrm{iid}}\sim N(0,1),
\tag{6}
\]

with known \(\sigma_A>0\). Define the effective stochastic signal

\[
\boxed{
S_A^2
:=
\frac{\delta_A^2}{\sigma_A^2}
\sum_{i=1}^{n_A}u_{A,i}^2.
}
\tag{7}
\]

Then:

1. for every fixed distinct \(\theta,\eta\in K\),

\[
\boxed{
D_{\mathrm{KL}}
(P_{A,\theta}\|P_{A,\eta})
=
\frac12(\theta-\eta)^2S_A^2(1+o(1));
}
\tag{8}
\]

2. uniform consistent recovery of \(\theta\) under absolute-error loss is possible **if and only if**

\[
\boxed{S_A\longrightarrow\infty;}
\tag{9}
\]

3. if \(S_A\to s\in(0,\infty)\), the full sampled experiment is asymptotically equivalent, uniformly over \(\theta\in K\), to the one-dimensional Gaussian location experiment

\[
\boxed{
Z=\theta+s^{-1}G,
\qquad G\sim N(0,1);
}
\tag{10}
\]

4. if \(S_A\to0\), every fixed pair of parameter values becomes asymptotically indistinguishable in total variation;

5. for fixed per-sample noise \(\sigma_A\equiv\sigma>0\) and any design with \(q_A\to q>0\), the phase boundary is

\[
\boxed{
n_A\delta_A^2.}
\tag{11}
\]

More explicitly,

\[
\begin{array}{lll}
n_A\delta_A^2\to0
&\Longrightarrow&
\text{collapse of fixed parameter distinctions},\\[3pt]
n_A\delta_A^2\to\lambda\in(0,\infty)
&\Longrightarrow&
\text{finite-information Gaussian location limit},\\[3pt]
n_A\delta_A^2\to\infty
&\Longrightarrow&
\text{uniformly consistent recovery}.
\end{array}
\tag{12}
\]

Since

\[
\delta_A^{-2}
=
\left(\frac{A\log\log A}{\log A}\right)^2,
\tag{13}
\]

fixed-variance independent sampling needs

\[
\boxed{
n_A\gg
\left(\frac{A\log\log A}{\log A}\right)^2
}
\tag{14}
\]

for consistent recovery of the anchor exponent from this profile channel.

Thus AF-530's rank-one collapse does **not** mean that arbitrarily many stochastic samples are useless. It means that all parameter information is asymptotically concentrated in one profile direction. Independent noise permits repeated measurements to accumulate information along that direction at the usual square-root rate; adversarial sup-norm noise does not.

## Derivation

### 1. Representation declaration

The source-side object remains exactly AF-530's anchored carrier profile

\[
F_{A,\theta}\in C([0,1]).
\]

The representation in this finding is not the continuum profile itself but the Gaussian observation channel

\[
\mathcal E_A
=
\left\{
N\!\left(
\mu_{A,\theta},
\sigma_A^2 I_{n_A}
\right):
\theta\in K
\right\},
\tag{15}
\]

where

\[
\mu_{A,\theta,i}
=
F_{A,\theta}(u_{A,i}).
\tag{16}
\]

The compression inherited from AF-530 has already reduced the normalized source family to the leading direction \(u\mapsto u\). The new resource is the observation geometry: each sampled coordinate receives an independent Gaussian error rather than one adversarial perturbation constrained in sup norm.

This distinction is load bearing. Sample cardinality is not, by itself, a fidelity resource; it becomes one here because the noise law makes repeated coordinates statistically independent.

### 2. Pairwise information is exactly controlled by \(S_A\)

Write

\[
\mathbf u_A
=(u_{A,1},\ldots,u_{A,n_A}),
\qquad
\mathbf r_{A,\theta}
=(r_{A,\theta}(u_{A,1}),\ldots,r_{A,\theta}(u_{A,n_A})).
\tag{17}
\]

Equation (1) gives

\[
\mu_{A,\theta}-\mu_{A,\eta}
=
\delta_A
\left(
(\eta-\theta)\mathbf u_A
+
\mathbf r_{A,\theta}-\mathbf r_{A,\eta}
\right).
\tag{18}
\]

The residual obeys

\[
\|\mathbf r_{A,\theta}-\mathbf r_{A,\eta}\|_2
\le2\rho_A\sqrt{n_A}.
\tag{19}
\]

By (5),

\[
\|\mathbf u_A\|_2
\ge\sqrt{q_0n_A}.
\tag{20}
\]

Hence for every fixed separation \(d=|\theta-\eta|>0\),

\[
\frac{
\|\mathbf r_{A,\theta}-\mathbf r_{A,\eta}\|_2
}{
d\|\mathbf u_A\|_2
}
\le
\frac{2\rho_A}{d\sqrt{q_0}}
\longrightarrow0.
\tag{21}
\]

Two Gaussians with common covariance \(\sigma_A^2I\) satisfy

\[
D_{\mathrm{KL}}
(P_{A,\theta}\|P_{A,\eta})
=
\frac{
\|\mu_{A,\theta}-\mu_{A,\eta}\|_2^2
}{2\sigma_A^2}.
\tag{22}
\]

Combining (18)--(22) with (7) proves (8).

In particular, when \(S_A\to0\), Pinsker's inequality gives

\[
\|P_{A,\theta}-P_{A,\eta}\|_{\mathrm{TV}}
\longrightarrow0
\tag{23}
\]

for every fixed pair \(\theta,\eta\in K\).

### 3. An explicit projection estimator gives the upper recovery bound

Define

\[
T_A
:=
1-
\frac{
\sum_{i=1}^{n_A}u_{A,i}Y_{A,i}
}{
\delta_A\sum_{i=1}^{n_A}u_{A,i}^2
},
\tag{24}
\]

and let

\[
\widehat\theta_A=\Pi_K(T_A),
\tag{25}
\]

where \(\Pi_K\) is metric projection onto \(K\).

From (1),

\[
\mathbb E_\theta T_A-\theta
=
-
\frac{
\sum_i u_{A,i}r_{A,\theta}(u_{A,i})
}{
\sum_i u_{A,i}^2
}.
\tag{26}
\]

Since \(0\le u_{A,i}\le1\),

\[
\left|
\mathbb E_\theta T_A-\theta
\right|
\le
\frac{\rho_A n_A}{q_0n_A}
=
\frac{\rho_A}{q_0}.
\tag{27}
\]

The noise term is Gaussian with

\[
\operatorname{Var}_\theta(T_A)
=
\frac{\sigma_A^2}
{\delta_A^2\sum_i u_{A,i}^2}
=
\frac1{S_A^2}.
\tag{28}
\]

Projection cannot increase distance to a point in \(K\), so

\[
\boxed{
\sup_{\theta\in K}
\mathbb E_\theta
|\widehat\theta_A-\theta|
\le
\frac{\rho_A}{q_0}
+
\sqrt{\frac2\pi}\frac1{S_A}.
}
\tag{29}
\]

Therefore \(S_A\to\infty\) implies uniform consistency.

### 4. Bounded \(S_A\) prevents uniform consistency

Suppose \(S_A\not\to\infty\). Then along some subsequence

\[
S_A\le M<\infty.
\tag{30}
\]

Choose two fixed interior parameter values \(\theta_0,\theta_1\in K\) with separation \(d>0\) sufficiently small that

\[
\frac12d^2M^2<\frac18.
\tag{31}
\]

If \(M=0\), any sufficiently small fixed \(d\) works. By (8), after shrinking along the same subsequence if needed,

\[
D_{\mathrm{KL}}(P_{A,\theta_0}\|P_{A,\theta_1})
<\frac14
\tag{32}
\]

for all large \(A\). Pinsker therefore gives a total-variation distance strictly below one by a fixed margin.

The elementary two-point testing bound then implies that every estimator has a fixed positive worst-case absolute-error risk on \(\{\theta_0,\theta_1\}\). Concretely,

\[
\inf_{\widehat\theta}
\max_{j=0,1}
\mathbb E_{\theta_j}
|\widehat\theta-\theta_j|
\ge
\frac d4
\left(
1-
\|P_{A,\theta_0}-P_{A,\theta_1}\|_{\mathrm{TV}}
\right),
\tag{33}
\]

whose right-hand side has positive liminf. Uniform consistency on \(K\) is therefore impossible whenever \(S_A\) fails to diverge. Together with (29), this proves (9).

### 5. At critical scaling the whole experiment reduces to one Gaussian coordinate

Let the rank-one comparison experiment be

\[
\widetilde P_{A,\theta}
=
N\!\left(
\delta_A(1-\theta)\mathbf u_A,
\sigma_A^2I_{n_A}
\right).
\tag{34}
\]

The Mahalanobis norm of the omitted remainder is bounded by

\[
\frac{
\|\mu_{A,\theta}-\delta_A(1-\theta)\mathbf u_A\|_2
}{\sigma_A}
\le
\frac{\delta_A\rho_A\sqrt{n_A}}{\sigma_A}
\le
\frac{S_A\rho_A}{\sqrt{q_0}}.
\tag{35}
\]

If \(S_A\to s<\infty\), the right-hand side tends to zero uniformly in \(\theta\). Equal-covariance Gaussian laws whose standardized mean displacement tends to zero have total-variation distance tending to zero, so

\[
\sup_{\theta\in K}
\|P_{A,\theta}-\widetilde P_{A,\theta}\|_{\mathrm{TV}}
\longrightarrow0.
\tag{36}
\]

In \(\widetilde P_{A,\theta}\), decompose \(\mathbb R^{n_A}\) into the span of \(\mathbf u_A\) and its orthogonal complement. Every orthogonal coordinate is pure \(N(0,\sigma_A^2)\) noise independent of \(\theta\). The projection onto \(\mathbf u_A\) contains all parameter dependence.

Equivalently, the scalar statistic

\[
Z_A
:=
1-
\frac{\langle\mathbf u_A,Y_A\rangle}
{\delta_A\|\mathbf u_A\|_2^2}
\tag{37}
\]

under the rank-one experiment is exactly

\[
Z_A\sim N(\theta,S_A^{-2}).
\tag{38}
\]

Equations (36)--(38) prove the critical limit (10) when \(S_A\to s\in(0,\infty)\). No nonparametric equivalence theorem is needed: the reduction is finite-dimensional and exact after the vanishing mean perturbation is removed.

### 6. Fixed-noise sampling has the inverse-square signal threshold

If \(\sigma_A\equiv\sigma>0\) and \(q_A\to q>0\), then

\[
S_A^2
=
\frac{q_A}{\sigma^2}
\,n_A\delta_A^2.
\tag{39}
\]

Therefore (12) follows directly from the three regimes of \(S_A\). Substituting AF-530's

\[
\delta_A
=
\frac{\log A}{A\log\log A}
\tag{40}
\]

gives (13)--(14).

This is the exact statistical price of changing AF-530's observation geometry from one adversarial sup-norm perturbation to independent equal-variance Gaussian errors at the sampled coordinates.

## Prior-art / novelty audit

All statistical machinery used above is classical.

David L. Donoho, **“Statistical Estimation and Optimal Recovery,”** *The Annals of Statistics* 22(1), 238–270 (1994), DOI `10.1214/aos/1176325367`, studies estimation from indirect data contaminated by random Gaussian noise and relates minimax statistical difficulty to optimal recovery and moduli of continuity. Author copy: https://web.stanford.edu/dept/statistics/cgi-bin/donoho/wp-content/uploads/2018/08/SEOR.pdf

Lucien Le Cam and Grace Lo Yang, ***Asymptotics in Statistics: Some Basic Concepts***, 2nd ed., Springer (2000), DOI `10.1007/978-1-4612-1166-2`, develops comparison of statistical experiments, Gaussian experiments, likelihood limits, and asymptotic decision theory. The experiment-comparison language used around (36) is standard in that framework.

Lawrence D. Brown and Mark G. Low, **“Asymptotic Equivalence of Nonparametric Regression and White Noise,”** *The Annals of Statistics* 24(6), 2384–2398 (1996), DOI `10.1214/aos/1032181159`, is neighboring classical prior art showing how independent Gaussian regression observations can be compared with Gaussian white-noise experiments. Their theorem is substantially more general than anything needed here; AF-531 uses only the elementary finite-dimensional rank-one Gaussian reduction in (34)--(38).

No novelty is claimed for the Gaussian KL formula, Pinsker inequality, two-point minimax testing, weighted least squares, Fisher-information accumulation, Gaussian location experiments, or square-root averaging under independent noise.

The durable Arithmetic Fidelity content is the specialization to AF-530's exact compression geometry. AF-530 identifies a source-derived profile whose entire normalized parameter family becomes asymptotically rank one at the vanishing amplitude \(\delta_A\). AF-531 shows that the recovery fate of that retained direction depends sharply on the **observation channel**: deterministic sup-norm access has threshold \(\varepsilon_A=o(\delta_A)\), whereas independent Gaussian samples accumulate effective information \(S_A^2\) and restore consistency precisely beyond \(n_A\asymp\delta_A^{-2}\) at fixed variance.

## Boundaries and falsification audit

1. **Independence is the new resource.** Repeated samples do not improve fidelity merely because there are many of them. Equation (7) uses the covariance \(\sigma_A^2I\). Strongly correlated noise can reduce or eliminate the \(n_A\) gain, and adversarial pointwise noise returns to an AF-530-type geometry.

2. **The design must see the retained direction.** Condition (5) excludes designs collapsing toward \(u=0\). More generally the relevant quantity is exactly \(\sum_i u_{A,i}^2\), not sample count alone.

3. **Gaussianity is convenient, not proved universal.** The exact KL and experiment-reduction statements use Gaussian noise. Analogous thresholds may hold for broader regular noise families through local asymptotic normality or direct concentration/testing arguments, but that is not established here.

4. **Known noise scale.** The estimator and experiment are stated with known \(\sigma_A\). Joint estimation of an unknown or heterogeneous covariance is a different channel.

5. **Anchored shape only.** As in AF-530, the observation is the baseline-differenced profile \(F_{A,\theta}\), not raw unquotiented carrier amplitude. Extra information in the zero-jet amplitude is outside this theorem.

6. **Compact exponent family.** The uniform remainder (3) is inherited from AF-530 and requires \(K\Subset(0,1)\). Drifting endpoint regimes need separate asymptotics.

7. **Critical experiment, not exact finite-\(A\) sufficiency.** The actual AF-530 profile contains the remainder \(r_{A,\theta}\), which can carry finite-\(A\) parameter dependence outside the leading direction. At bounded \(S_A\), equation (36) proves that this extra dependence vanishes statistically. At \(S_A\to\infty\), no claim is made that the rank-one projection is asymptotically sufficient at arbitrary growth rates; the remainder may become statistically visible even though the explicit projection estimator is already consistent.

8. **No rational-prime discriminator is created.** The recovered parameter is the coarse anchor exponent \(\theta\). As in AF-530, the leading profile law follows from Mertens-type moment behavior and may be reproducible by matched generalized-prime systems. Independent sampling repairs statistical conditioning of the retained direction; it does not establish arithmetic specificity.

9. **No contradiction with the older stochastic-fidelity findings.** AF-229/AF-230 study stochastic marking and rate-distortion of a discrete prime-tail localization source. AF-531 studies repeated noisy observation of AF-530's continuous boundary-profile carrier. The information-theory language overlaps, but the source object, compression, and decision experiment are different.

## Consequence

AF-530's deterministic conclusion must be read together with its noise geometry. The full profile has only one leading parameter direction, so denser deterministic access cannot create a second discriminator. But under independent Gaussian noise, denser sampling can repeatedly measure that same direction and increase its effective signal-to-noise ratio as \(S_A\asymp\delta_A\sqrt{n_A}/\sigma_A\).

The resulting Arithmetic Fidelity principle is:

> **A compression can preserve a discriminator in low rank while the observation channel decides whether repeated access can recover it. Fidelity therefore depends not only on what the representation retains, but also on the geometry and dependence structure of the noise applied after compression.**

For this concrete carrier, the distinction is sharp: adversarial sup-norm noise requires per-observation accuracy \(o(\delta_A)\), while independent fixed-variance Gaussian access requires sample count asymptotically larger than \(\delta_A^{-2}\).