# AF-534 — Cameron–Martin nuisance closure separates identifiability from stable fidelity

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `ARITHMETIC-FIDELITY` · `INFINITE-DIMENSIONAL-GAUSSIAN` · `CAMERON-MARTIN` · `NUISANCE-CLOSURE` · `MINIMAX` · `RECOVERY-BOUNDARY` · `NO-NOVELTY-CLAIM`

## Claim

AF-533 identifies the exact nuisance-invariant information in a finite-dimensional Gaussian linear experiment as the squared precision distance from the target carrier to the nuisance span. In infinite-dimensional Gaussian experiments the same geometry survives, but one new distinction becomes unavoidable: **exact algebraic aliasing is controlled by the nuisance subspace itself, whereas stable uniform recoverability is controlled by its Cameron–Martin closure**.

Let \((E,H,\mu)\) be an abstract Wiener space: \(E\) is a separable Banach space, \(\mu\) is a centered Gaussian measure on \(E\), and \(H\) is its Cameron–Martin Hilbert space. Let \(N\subset H\) be a linear nuisance subspace, not assumed closed, let \(u\in H\) be a target carrier, and let \(\delta>0\). For target \(\theta\in K\subset\mathbb R\) and nuisance \(n\in N\), observe the Gaussian shift experiment

\[
P_{\theta,n}:=(\tau_{\delta\theta u+n})_\#\mu,
\qquad
\tau_h(x)=x+h.
\tag{1}
\]

Write

\[
\bar N:=\overline N^{\,H},
\qquad
u:=P_{\bar N^\perp}u,
\qquad
d:=\|\nu\|_H=\operatorname{dist}_H(u,\bar N),
\qquad
J:=\delta^2d^2.
\tag{2}
\]

Then:

1. **Exact target aliasing uses \(N\), not \(\bar N\).** For distinct \(\theta,\eta\), there exist nuisances \(n,m\in N\) with
   \[
   P_{\theta,n}=P_{\eta,m}
   \]
   if and only if \(u\in N\). Thus \(u\notin N\) gives exact target identifiability even when \(u\in\bar N\).

2. **Stable pairwise distinguishability uses the closure.** For any \(\theta,\eta\),
   \[
   \boxed{
   \inf_{n,m\in N}
   D_{\mathrm{KL}}(P_{\theta,n}\|P_{\eta,m})
   =\frac12\delta^2(\theta-\eta)^2d^2
   =\frac12(\theta-\eta)^2J.
   }
   \tag{3}
   \]
   The infimum need not be attained when \(N\) is not closed.

3. **The surviving scalar coordinate is exactly the orthogonal Cameron–Martin component.** If \(d>0\), let \(W(\nu)\) denote the first-chaos/Paley–Wiener Gaussian coordinate associated with \(\nu\). Under every \(P_{\theta,n}\),
   \[
   W(\nu)\sim N(\delta\theta d^2,d^2),
   \tag{4}
   \]
   independently of the nuisance value in the sense that its law contains no \(n\)-term. Hence
   \[
   \widehat\theta=\frac{W(\nu)}{\delta d^2}
   \tag{5}
   \]
   is nuisance-invariant with
   \[
   \operatorname{Var}(\widehat\theta)=J^{-1}.
   \tag{6}
   \]

4. **Dense nuisance can destroy stable fidelity without creating an exact alias.** If
   \[
   u\in\bar N\setminus N,
   \tag{7}
   \]
   then the target is algebraically identifiable, but \(d=J=0\) and for every distinct target pair
   \[
   \inf_{n,m\in N}
   \|P_{\theta,n}-P_{\eta,m}\|_{\mathrm{TV}}=0.
   \tag{8}
   \]
   Thus no estimator can recover \(\theta\) uniformly over unrestricted nuisance values, despite the absence of an exactly equal-law target alias.

For a sequence of experiments \((E_A,H_A,\mu_A,N_A,u_A,\delta_A)\), define

\[
d_A=\operatorname{dist}_{H_A}(u_A,\overline{N_A}^{H_A}),
\qquad
J_A=\delta_A^2d_A^2.
\tag{9}
\]

If \(K\) is a fixed compact interval with nonempty interior, then there exist estimators \(\widehat\theta_A\) satisfying

\[
\sup_{\theta\in K}\sup_{n\in N_A}
P_{A,\theta,n}(|\widehat\theta_A-\theta|>\varepsilon)
\longrightarrow0
\quad\text{for every }\varepsilon>0
\tag{10}
\]

**if and only if**

\[
\boxed{J_A\to\infty.}
\tag{11}
\]

So the finite-dimensional AF-533 rule extends exactly after one essential replacement:

> in an infinite-dimensional Gaussian nuisance problem, quotient by the **closed** nuisance geometry selected by the Cameron–Martin norm. Algebraic non-membership in the raw nuisance span is not enough for stable fidelity.

This gives a concrete infinite-system answer to the line mandate. Completion is not a technical afterthought: it is the boundary between exact identifiability and robust recoverability.

## Representation declaration

The source event here is an infinite-dimensional Gaussian shift family with a declared linear nuisance action.

- **Source object:** \((\theta,n)\in K\times N\) with shift vector \(\delta\theta u+n\in H\).
- **Forward map:** translation of the fixed centered Gaussian law \(\mu\) by that shift.
- **Represented object:** the family of probability laws \(\{P_{\theta,n}\}\) on \(E\).
- **Target observable:** \(\theta\), uniformly over unrestricted \(n\in N\).
- **Equivalence relevant to target fidelity:** nuisance translations are admissible changes of representation, so target distinguishability is measured after optimizing over \(N\).
- **Natural metric:** the Cameron–Martin norm, forced by Gaussian likelihood ratios rather than chosen as an external Euclidean geometry.

The result is representation-relative. A different nuisance class, a bounded or probabilistic nuisance, target-dependent covariance, or shifts outside the Cameron–Martin space define different experiments and can change the recovery boundary.

## Exact derivation

### Cameron–Martin likelihood geometry

For \(h,k\in H\), the Cameron–Martin theorem gives equivalence of the shifted Gaussian laws and the exponential likelihood-ratio formula. Applied to the shift difference \(h-k\), it yields

\[
D_{\mathrm{KL}}(\mu_h\|\mu_k)
=\frac12\|h-k\|_H^2.
\tag{12}
\]

For two target/nuisance states in (1),

\[
(\delta\theta u+n)-(\delta\eta u+m)
=\delta(\theta-\eta)u+(n-m).
\tag{13}
\]

Because \(N\) is linear, \(n-m\) ranges over \(N\). Therefore

\[
\begin{aligned}
\inf_{n,m\in N}
D_{\mathrm{KL}}(P_{\theta,n}\|P_{\eta,m})
&=
\frac12
\inf_{v\in N}
\|\delta(\theta-\eta)u+v\|_H^2\\
&=
\frac12\delta^2(\theta-\eta)^2
\operatorname{dist}_H(u,N)^2.
\end{aligned}
\tag{14}
\]

Distance to a set equals distance to its closure, so

\[
\operatorname{dist}_H(u,N)
=\operatorname{dist}_H(u,\bar N)
=\|P_{\bar N^\perp}u\|_H,
\tag{15}
\]

which proves (3).

This is the first place where infinite dimension changes the logical structure. In finite dimensions every linear subspace is closed, so \(u\notin N\) automatically implies positive distance from \(N\). In an infinite-dimensional Hilbert space one may have \(u\notin N\) but \(\operatorname{dist}(u,N)=0\).

### Exact aliases and approximate aliases are different

Two translates of the same Gaussian measure are equal only when their translation vectors are equal. Hence a target alias with \(\theta\ne\eta\) exists exactly when

\[
\delta(\theta-\eta)u=m-n\in N.
\tag{16}
\]

Since \(N\) is linear and \(\delta(\theta-\eta)\ne0\), this is equivalent to \(u\in N\). That proves statement 1.

Now suppose \(u\in\bar N\setminus N\). Exact equality (16) is impossible, yet for every \(\epsilon>0\) there is \(v_\epsilon\in N\) such that

\[
\|\delta(\theta-\eta)u+v_\epsilon\|_H<\epsilon.
\tag{17}
\]

The corresponding Gaussian laws have KL divergence below \(\epsilon^2/2\). Pinsker's inequality then gives total variation below \(\epsilon/2\) after an inessential rescaling of \(\epsilon\), proving (8).

Thus the raw nuisance span controls **exact collision**, while its Hilbert closure controls **arbitrarily accurate imitation**.

### The nuisance-free first-chaos coordinate

For each \(h\in H\), abstract Wiener space theory provides an isonormal first-chaos coordinate \(W(h)\in L^2(\mu)\) satisfying

\[
W(h)\sim N(0,\|h\|_H^2)
\tag{18}
\]

under \(\mu\). Under translation by \(g\in H\), its mean becomes \(\langle h,g\rangle_H\) while its variance is unchanged.

Set \(h=\nu=P_{\bar N^\perp}u\). Since \(\nu\perp N\), under shift \(\delta\theta u+n\),

\[
\mathbb E_{\theta,n}W(\nu)
=\delta\theta\langle\nu,u\rangle_H+\langle\nu,n\rangle_H
=\delta\theta\|\nu\|_H^2.
\tag{19}
\]

Together with (18), this proves (4)–(6). For compact \(K\), projecting (5) back to \(K\) cannot increase absolute error. Therefore \(J_A\to\infty\) implies the uniform consistency in (10).

### Bounded transverse Cameron–Martin energy prevents uniform recovery

For necessity, suppose (11) fails. Along some subsequence,

\[
J_A\le C<\infty.
\tag{20}
\]

Choose two fixed target values \(\theta_0,\theta_1\in\operatorname{int}K\) with separation \(a=|\theta_1-\theta_0|>0\). By (14), for every \(A\) and every \(\epsilon>0\) one can choose nuisance states whose shift difference has Cameron–Martin norm at most

\[
a\sqrt{J_A}+\epsilon
\le a\sqrt C+\epsilon.
\tag{21}
\]

For two Gaussian shifts separated by Cameron–Martin norm \(r\), the likelihood ratio is a one-dimensional Gaussian statistic and the equal-prior optimal testing error is

\[
\Phi(-r/2)>0
\tag{22}
\]

for every finite \(r\). Hence (21) gives a positive lower bound, depending only on \(a\) and \(C\), on the testing error between suitable nuisance representatives of the two fixed target values. Any estimator that were uniformly consistent would induce a test with error tending to zero by thresholding between \(\theta_0\) and \(\theta_1\), a contradiction. This proves necessity.

When \(J_A=0\), the stronger conclusion (8) holds: nuisance representatives can make the two target laws arbitrarily close in total variation, even if no exact alias exists.

## Matched control: a dense proper nuisance subspace

Let

\[
H=\ell^2(\mathbb N),
\qquad
N=c_{00},
\tag{23}
\]

where \(c_{00}\) is the subspace of finitely supported sequences. Then \(N\) is a proper dense linear subspace of \(H\). Choose, for example,

\[
u=(2^{-1},2^{-2},2^{-3},\ldots)\in\ell^2\setminus c_{00}.
\tag{24}
\]

For the Gaussian shift experiment generated by this Cameron–Martin geometry,

\[
u\notin N,
\qquad
\nu\in\overline N^H=H.
\tag{25}
\]

So no nonzero target change is exactly absorbed by a finitely supported nuisance, but

\[
\operatorname{dist}_H(u,N)=0.
\tag{26}
\]

Truncations of \(-\delta(\theta-\eta)u\) lie in \(c_{00}\) and converge to it in \(\ell^2\), producing nuisance representatives whose Gaussian laws become arbitrarily close. This is a direct matched control against the false inference

\[
\text{“no exact alias”}\quad\Longrightarrow\quad\text{“stable recovery.”}
\]

The implication fails solely because completion adds approximate nuisance directions.

## Prior art and novelty audit

The underlying mathematics is classical, and no theorem-level novelty is claimed for the Cameron–Martin theorem, Gaussian-shift likelihoods, semiparametric nuisance closure, or orthogonal efficient-score projection.

- Hui-Hsiung Kuo, ***Gaussian Measures in Banach Spaces***, Lecture Notes in Mathematics 463, Springer (1975), DOI `10.1007/BFb0082007`. Role: classical Gaussian-measure reference for abstract Wiener spaces, equivalence/orthogonality of Gaussian translates, and Cameron–Martin geometry.
- Masoumeh Dashti and Andrew M. Stuart, **“The Bayesian Approach to Inverse Problems,”** in *Handbook of Uncertainty Quantification*, Springer (2017), pp. 311–428, DOI `10.1007/978-3-319-12385-1_7`. Role: modern infinite-dimensional inverse-problem treatment using Cameron–Martin spaces and Gaussian change-of-measure formulas.
- A. W. van der Vaart, ***Asymptotic Statistics***, Chapter 25 “Semiparametric Models,” Cambridge University Press (1998), DOI `10.1017/CBO9780511802256.026`. Role: standard semiparametric efficiency framework for infinite-dimensional nuisance parameters and tangent-space projection.
- Peter J. Bickel, Chris A. J. Klaassen, Ya'acov Ritov, and Jon A. Wellner, ***Efficient and Adaptive Estimation for Semiparametric Models***, Johns Hopkins University Press (1993). Role: classical nuisance-tangent-space and efficient-score projection framework.

AF-141 already records the finite/statistical principle that Fisher information retained after a compression is an orthogonal score projection. AF-490 records the deterministic finite-dimensional quotient norm, and AF-533 records the finite-dimensional Gaussian precision quotient. The additional line-local value here is narrower: it identifies **closure of the nuisance space as the exact stable-fidelity boundary** for an infinite-dimensional Gaussian shift and records the resulting separation between exact identifiability and uniform recoverability. This is an application/synthesis of classical Hilbert and Gaussian theory, not a claim of a new Gaussian-statistics theorem.

## Falsification and boundary audit

1. **All target and nuisance shifts are assumed to lie in the Cameron–Martin space.** If a target shift leaves \(H\), the corresponding Gaussian translates can become mutually singular. That is a different, potentially perfectly distinguishable regime and is not covered by (3)–(11).

2. **The nuisance is linear and unrestricted.** A bounded nuisance set, nonlinear nuisance manifold, prior, penalty, or repeated structure shared across experiments need not reduce to a closed linear quotient. In nonlinear semiparametric problems the closure rule normally applies first to tangent spaces and is local rather than an exact global quotient.

3. **Closure controls stable minimax fidelity, not exact parameter equality.** Replacing \(N\) by \(\bar N\) in the exact-alias statement would be wrong when \(N\) is nonclosed. The distinction in (7) is the substantive new boundary exposed by infinite dimension.

4. **The Gaussian covariance structure is fixed.** Target- or nuisance-dependent covariance introduces additional score directions and can carry information not represented by the mean-shift Cameron–Martin quotient.

5. **The first-chaos coordinate is a measurable Gaussian coordinate, not necessarily a continuous linear functional on all of \(E\).** The abstract Wiener formulation therefore uses the canonical Paley–Wiener/isonormal realization rather than assuming every Cameron–Martin vector belongs to \(E^*\).

6. **Large \(J\) is fidelity only for the declared target in the declared experiment.** It does not show that a prior arithmetic construction preserved rational-prime provenance before entering the Gaussian channel.

7. **Pointwise identifiability is too weak for noisy infinite systems.** The matched control (23)–(26) shows that checking only whether the target carrier belongs algebraically to the nuisance span can miss complete collapse of uniform recovery.

## Relationship to AF-141, AF-490, AF-533, and the line mandate

AF-141 explains statistical information loss through Hilbert projection of scores. AF-490 makes nuisance quotient distance the exact deterministic recovery resource. AF-533 combines nuisance quotienting with the precision metric of a finite-dimensional Gaussian channel. AF-534 extends that chain to infinite-dimensional Gaussian shifts and shows where finite-dimensional intuition breaks: the operative nuisance object is the **closed** nuisance subspace in Cameron–Martin geometry.

This directly addresses the README's request to separate exact injectivity from stable recoverability in infinite systems. A transformation may preserve target identity set-theoretically while making every target difference arbitrarily well reproducible by nuisance directions. For later arithmetic instantiations, the correct audit is therefore not merely “is the prime discriminator outside the nuisance span?” but the stronger question “does it remain a positive—and eventually growing—distance away from the completed nuisance class in the natural observation metric?”