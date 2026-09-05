# AF-140 — Location Fisher geometry is a full-law affine-natural source metric

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-MECHANISM`, `GAUGE-REPAIR`, `FULL-LAW`, `CATEGORY-GATE`, `NO-NOVELTY-CLAIM`

## Claim

AF-139 proves that if a source metric is allowed to depend only on a positive-definite covariance matrix and must transform naturally under every invertible generator reparameterization, then it is forced to be a scalar multiple of the inverse covariance. That repair is therefore intrinsically second-order.

The second-order ceiling is not forced by full affine naturality itself. If the independently specified source object is a sufficiently regular probability law with a canonical translation structure, its location Fisher information gives another metric with exactly the transport law required by AF-138, while depending on the full density rather than only on covariance.

Let `X` be an `R^m`-valued random vector with a strictly positive `C^1` density `p`, mean zero, positive-definite covariance

\[
C=\mathbb E[XX^T]>0,
\tag{1}
\]

and score

\[
\rho(x)=\nabla\log p(x).
\tag{2}
\]

Assume `\rho(X)\in L^2`, the coordinatewise integration-by-parts boundary terms vanish, and define the location Fisher matrix

\[
J=\mathbb E[\rho(X)\rho(X)^T].
\tag{3}
\]

Then:

1. **`J` has the same full-`GL_m` metric transport law as the source metric in AF-138.** For any `R\in GL_m(\mathbb R)`, represent the same source in new coordinates by
   \[
   X_R=R^{-1}X.
   \tag{4}
   \]
   Its density and score are
   \[
   p_R(y)=|\det R|\,p(Ry),
   \qquad
   \rho_R(y)=R^T\rho(Ry),
   \tag{5}
   \]
   so
   \[
   \boxed{J_R=R^TJR.}
   \tag{6}
   \]
   Thus `M=J` is a legitimate coefficient metric under the generator gauge of AF-138 whenever the source translation law is intrinsic.

2. **Fisher geometry refines the covariance-only metric.** Integration by parts gives
   \[
   \mathbb E[X\rho(X)^T]=-I.
   \tag{7}
   \]
   Positivity of the joint second-moment matrix of `(X,\rho(X))` yields
   \[
   \begin{pmatrix}
   C&-I\\
   -I&J
   \end{pmatrix}\ge0,
   \tag{8}
   \]
   hence by the Schur complement
   \[
   \boxed{J\ge C^{-1}.}
   \tag{9}
   \]
   Equality holds exactly when
   \[
   \rho(X)=-C^{-1}X
   \quad\text{a.s.},
   \tag{10}
   \]
   which, under the stated positive-density regularity, is exactly the centered Gaussian law with covariance `C`.

3. **AF-138 therefore produces an affine-invariant full-law spectral geometry.** Let `H` be a real Hilbert space, `A:\mathbb R^m\to H`, `G=A^*A`, and fix `k\in H`. With `M=J`, the generalized source spectrum is the spectrum of
   \[
   \widehat G_J=J^{-1/2}GJ^{-1/2}.
   \tag{11}
   \]
   Its nonzero eigenvalues equal those of the source-induced output operator
   \[
   \boxed{Q_J=AJ^{-1}A^*.}
   \tag{12}
   \]
   If `F_B^J` is the spectral projector of `Q_J` for `B\subset(0,\infty)`, then AF-138's target-relative measure becomes
   \[
   \boxed{\mu_{J;A,k}(B)=\|F_B^Jk\|^2.}
   \tag{13}
   \]
   Consequently a Fisher-generalized spectral cutoff loses exactly the target energy carried by the discarded eigenspaces of `Q_J`.

4. **The covariance geometry is an exact Loewner upper envelope.** From `(9)`, inversion reverses the positive-definite order:
   \[
   J^{-1}\le C.
   \tag{14}
   \]
   Hence
   \[
   \boxed{Q_J\le Q_C:=ACA^*.}
   \tag{15}
   \]
   AF-139's covariance-natural output covariance `Q_C` is therefore the Gaussian/extremal envelope of the Fisher-natural full-law operator at fixed covariance. Equality for every synthesis map `A` is equivalent to Gaussianity. For one fixed noninjective `A`, equality may still occur because `A` can annihilate the positive defect `C-J^{-1}`.

5. **Equal covariance no longer forces a collision.** In one dimension, a standard Gaussian has variance `1` and location Fisher information `J_G=1`. A centered logistic law with scale
   \[
   s=\frac{\sqrt3}{\pi}
   \tag{16}
   \]
   also has variance `1`, but
   \[
   J_L=\frac{1}{3s^2}=\frac{\pi^2}{9}>1.
   \tag{17}
   \]
   Thus the two laws collide under the covariance-only metric of AF-139 but are separated by the Fisher metric. For `A=1`, their Fisher output scales are respectively `1` and `9/\pi^2`.

The reusable Arithmetic Fidelity conclusion is therefore:

\[
\boxed{
\begin{array}{c}
\text{full affine naturality does not force a second-order fidelity ceiling;}\\
\text{covariance-only input does.}\\
\text{A canonical smooth translation law supplies the full-law Fisher metric }J,\\
\text{but importing that metric into a discrete arithmetic carrier requires a source-natural}\\
\text{statistical/translation structure rather than arbitrary smoothing.}
\end{array}}
\tag{18}
\]

## Derivation

### Affine reparameterization transports Fisher information as a coefficient metric

For `Y=X_R=R^{-1}X`, the change-of-variables formula gives `(5)`. Differentiating in `y`,

\[
\nabla_y\log p_R(y)
=R^T\nabla\log p(Ry).
\tag{19}
\]

Therefore

\[
J_R
=\mathbb E[\rho_R(Y)\rho_R(Y)^T]
=R^T\mathbb E[\rho(X)\rho(X)^T]R
=R^TJR,
\]

which is `(6)`.

This is precisely the tensorial law demanded by AF-138 when generators are changed by `A_R=AR`: the same source quadratic form is represented by `J_R=R^TJR`. After Fisher whitening, arbitrary invertible coordinate changes again reduce to a right orthogonal gauge, exactly as a general source metric does in AF-138.

The score in `(2)` is the negative of the parameter score for the translation family `p_\theta(x)=p(x-\theta)` at `\theta=0`; the sign disappears in `(3)`. Thus `J` is the ordinary Fisher information for location, not a newly defined metric tailored to the Gram problem.

### The information inequality identifies the Gaussian boundary

For coordinates `i,j`, integration by parts gives

\[
\mathbb E[X_i\rho_j(X)]
=\int x_i\,\partial_jp(x)\,dx
=-\delta_{ij},
\tag{20}
\]

under the stated boundary hypothesis. This proves `(7)`.

Now for arbitrary `u,v\in\mathbb R^m`,

\[
\mathbb E[(u^TX+v^T\rho(X))^2]\ge0,
\]

so the block matrix `(8)` is positive semidefinite. Since `C>0`, its Schur complement is

\[
J-C^{-1}\ge0,
\]

proving `(9)`. Equivalently, completing the square gives the more diagnostic identity

\[
\mathbb E[(\rho(X)+C^{-1}X)(\rho(X)+C^{-1}X)^T]
=J-C^{-1}.
\tag{21}
\]

Hence equality in `(9)` is equivalent to `(10)`. With positive differentiable density, `(10)` says

\[
\nabla\log p(x)=-C^{-1}x
\]

almost everywhere; integration yields

\[
p(x)=Z^{-1}\exp\!\left(-\tfrac12x^TC^{-1}x\right),
\]

so the law is Gaussian. Conversely the Gaussian score is `-C^{-1}x`, giving equality.

Thus the difference

\[
J-C^{-1}
\tag{22}
\]

is itself an exact positive-semidefinite full-law defect beyond the covariance-only geometry. It vanishes precisely at the Gaussian boundary in this regular location class.

### The Fisher generalized spectrum is an output information geometry

Apply AF-138 with `M=J`. Because `J\ge C^{-1}>0`, the Fisher metric is positive definite. Set

\[
B=AJ^{-1/2}.
\tag{23}
\]

Then

\[
B^*B=J^{-1/2}GJ^{-1/2}=\widehat G_J,
\qquad
BB^*=AJ^{-1}A^*=Q_J.
\tag{24}
\]

The two operators have the same nonzero eigenvalues with multiplicity. For a singular system

\[
Bv_j=s_ju_j,
\qquad s_j>0,
\]

AF-138's whitened target vector is

\[
\widehat b_J=J^{-1/2}A^*k=B^*k.
\]

Therefore

\[
\langle v_j,\widehat b_J\rangle
=s_j\langle u_j,k\rangle,
\]

and the `1/s_j^2` weight in the generalized Picard measure cancels the singular value exactly. Summing over a Borel spectral set gives `(13)`.

Equation `(15)` follows directly from `(14)` by congruence with `A`. It must not be overinterpreted as a monotone statement about every spectral projector or target tail: Loewner order compares quadratic forms and ordered eigenvalues, but spectral subspaces can rotate. The exact target-relative object remains the measure `(13)`.

## Exact matched control: Gaussian versus equal-variance logistic law

Let the centered logistic density with scale `s>0` be

\[
p_s(x)=\frac{e^{-x/s}}{s(1+e^{-x/s})^2}.
\tag{25}
\]

Its variance is

\[
\operatorname{Var}(X)=\frac{\pi^2s^2}{3}.
\tag{26}
\]

Its CDF is `F_s(x)=1/(1+e^{-x/s})`, and direct differentiation gives

\[
\rho_s(x)
=\frac{d}{dx}\log p_s(x)
=\frac{1-2F_s(x)}{s}.
\tag{27}
\]

Since `U=F_s(X)` is uniform on `(0,1)`,

\[
J_L
=\mathbb E[\rho_s(X)^2]
=\frac{1}{s^2}\int_0^1(1-2u)^2du
=\frac{1}{3s^2}.
\tag{28}
\]

Taking `s=\sqrt3/\pi` makes `(26)` equal to `1` and gives `(17)`. The standard Gaussian has the same covariance but score `\rho_G(x)=-x`, hence `J_G=1`.

This control is stronger than merely observing that higher moments differ. Both source laws inhabit the same smooth location category, have the same first two moments, and obey the same full affine transformation rule, yet the full-law metric separates them. Therefore the AF-139 collision is caused by its declared covariance-only input, not by the `GL` gauge.

## Boundary conditions and falsification tests

1. **The translation/statistical structure must be part of the source.** Fisher information is defined here from the location family generated by translating `p`. A bare measure space or an arbitrary collection of generator weights does not canonically supply that family.

2. **Smooth absolute continuity is a real category gate.** The score proof uses a density, differentiability, square-integrability, and integration by parts. Singular or discrete laws require a different statistical model or a different notion of information; `(2)` cannot simply be copied to them.

3. **Arbitrary smoothing is not a repair.** For a discrete arithmetic carrier, convolution with a chosen kernel or insertion of a bandwidth may produce a smooth Fisher matrix, but unless that smoothing is forced independently by the source mathematics, the kernel/bandwidth is new gauge data. The construction has then relocated rather than solved the canonicity problem.

4. **Fisher information remains model-relative.** A different intrinsic parametric family can produce a different Fisher metric. The present theorem certifies naturality for the location structure; it does not claim a universal canonical metric for every probability law.

5. **Output equality is weaker than source equality for one fixed synthesis.** From `(15)`,
   \[
   Q_C-Q_J=A(C-J^{-1})A^*.
   \tag{29}
   \]
   A non-Gaussian source can still satisfy `Q_C=Q_J` for a particular `A` if `\operatorname{ran}A^*` misses the defect directions. Gaussianity follows from equality of the full source metrics, or from output equality for a sufficiently separating family of synthesis maps, not from one arbitrary compressed output.

6. **The result does not say that Fisher geometry preserves the desired arithmetic discriminator.** It only proves that a full-law source metric can survive the same affine gauge while retaining information that covariance necessarily discards. An RH-facing use still needs a source-natural probability/statistical structure and a proof that its retained Fisher-relative spectral data distinguish the rational-prime target from admissible controls.

A decisive matched-control test for any Fisher-based arithmetic proposal is therefore: hold fixed the declared source category and all canonical statistical structure, then construct controls matching the retained Fisher metric or Fisher-relative target profile while differing in the claimed arithmetic discriminator. If such controls exist, the discriminator has already been lost at that layer.

## Prior art and novelty assessment

No novelty claim is made for Fisher information, its transformation as a Riemannian/statistical metric, the Cramér–Rao information inequality, the Gaussian equality case, or the Fisher-information inequalities surrounding them.

- C. R. Rao, **“Information and the Accuracy Attainable in the Estimation of Statistical Parameters,”** *Bulletin of the Calcutta Mathematical Society* 37 (1945), 81–91. Role: primary classical source for the information bound and the geometric role of Fisher information in multiparameter estimation.
- A. J. Stam, **“Some Inequalities Satisfied by the Quantities of Information of Fisher and Shannon,”** *Information and Control* 2(2) (1959), 101–112, DOI `10.1016/S0019-9958(59)90348-1`. Role: classical Fisher-information inequality and Gaussian-extremality context.
- Shun-ichi Amari and Hiroshi Nagaoka, ***Methods of Information Geometry***, Translations of Mathematical Monographs 191, American Mathematical Society / Oxford University Press (2000), DOI `10.1090/MMONO/191`. Role: authoritative information-geometric treatment of Fisher information as the natural Riemannian metric on statistical manifolds and of coordinate invariance.

The affine score transformation `(19)`, block-matrix information inequality `(8)`--`(9)`, Gaussian equality characterization, and logistic control are derived directly here from standard formulas. They are not asserted as new theorems.

The new-to-this-line content is the diagnostic synthesis with AF-138 and AF-139: **the same generator-gauge law that forces inverse covariance when only second-order source data are admitted also accepts a genuinely full-law Fisher metric once a smooth translation structure is independently part of the source.** This identifies the exact location of the earlier ceiling and turns the possible escape into a falsifiable category requirement rather than a generic instruction to “use more information.”

## Consequence for the current frontier

AF-139 closes the covariance-only branch: full affine naturality leaves one metric, `C^{-1}`, and no covariance-only construction can recover a higher-order discriminator. AF-140 opens and simultaneously constrains the next branch. A full source law can carry extra information through the same generator gauge, but only through additional source structure that has its own mathematical justification.

For smooth translation models, the Fisher metric supplies one exact positive answer and the defect `J-C^{-1}` measures how far that metric lies beyond covariance geometry. For rational-prime applications, however, the immediate task is not to smooth a prime-derived sequence and compute Fisher information. It is to determine whether the arithmetic construction itself supplies a canonical statistical/translation family, or another comparably natural full-law geometry, before any such metric is admitted.

This gives a stopping rule: if the only route to a full-law metric requires a freely chosen smoothing kernel, bandwidth, parametric family, or target-dependent law, then the proposed repair fails the same source-canonicity gate as an arbitrary coefficient metric. If a canonical family is forced by the source, AF-138 applies to its metric and the next substantive burden is an exact matched-control test of the resulting target-relative spectral profile.