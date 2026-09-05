# AF-141 — Fisher information loss is the conditional score-projection defect

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-IDENTITY`, `FIDELITY-BRIDGE`, `CATEGORY-GATE`, `NO-NOVELTY-CLAIM`

## Claim

AF-140 shows that a source-natural smooth translation law can supply a full-law Fisher metric that obeys the generator-gauge transport required by AF-138. That resolves a canonicity problem but not a compression-fidelity problem: a canonical Fisher metric can itself contract when the statistical source is replaced by a statistic or a noisy observation.

Let `Theta` be an open subset of `R^d`, and let `{P_theta}` be a regular dominated statistical model on a sample space `X`, with density `p_theta(x)` and square-integrable score

\[
S_\theta(X)=\nabla_\theta\log p_\theta(X),
\qquad
\mathbb E_\theta S_\theta=0.
\tag{1}
\]

Let `Y` be obtained from `X` through a Markov kernel `K(dy|x)` that is independent of `theta`. Assume the induced model `{Q_theta}` on `Y` is dominated and differentiation may be interchanged with the kernel integral. Write

\[
I_X(\theta)=\mathbb E_\theta[S_\theta S_\theta^T]
\tag{2}
\]

for the upstream Fisher matrix and `I_Y(theta)` for the Fisher matrix after compression.

Then:

1. **The retained score is the conditional expectation of the upstream score.** If `S^Y_theta(Y)` denotes the score of the induced model on `Y`, then
   \[
   \boxed{
   S^Y_\theta(Y)=\mathbb E_\theta[S_\theta(X)\mid Y]
   }
   \quad\text{a.s.}
   \tag{3}
   \]

2. **Fisher information loss is exactly an `L^2` projection defect.** Consequently
   \[
   \boxed{
   I_X(\theta)-I_Y(\theta)
   =
   \mathbb E_\theta\!\left[
   (S_\theta-S^Y_\theta)(S_\theta-S^Y_\theta)^T
   \right]
   =
   \mathbb E_\theta[\operatorname{Cov}_\theta(S_\theta\mid Y)]
   \succeq0.
   }
   \tag{4}
   \]
   Thus the Fisher monotonicity inequality is not merely an order relation: the lost metric is the exact conditional-variance defect of the score.

3. **The surviving parameter directions are characterized exactly.** For any `a in R^d`,
   \[
   a^T(I_X-I_Y)a
   =
   \mathbb E_\theta\!\left[
   \bigl(a^TS_\theta-\mathbb E_\theta[a^TS_\theta\mid Y]\bigr)^2
   \right].
   \tag{5}
   \]
   Hence
   \[
   \boxed{
   a\in\ker(I_X-I_Y)
   \iff
   a^TS_\theta(X)\text{ is }\sigma(Y)\text{-measurable a.s.}
   }
   \tag{6}
   \]
   Full equality `I_X(theta)=I_Y(theta)` holds exactly when the whole score vector is retained by `Y` at that parameter value.

4. **The defect adds exactly along a Markov compression chain.** If
   \[
   X\longrightarrow Y\longrightarrow Z
   \tag{7}
   \]
   is a chain of `theta`-independent Markov kernels satisfying the same regularity conditions, then
   \[
   \boxed{
   I_X-I_Z=(I_X-I_Y)+(I_Y-I_Z).
   }
   \tag{8}
   \]
   Equivalently, the score projections form the nested conditional-expectation chain
   \[
   S^Z_\theta
   =\mathbb E_\theta[S^Y_\theta\mid Z]
   =\mathbb E_\theta[S_\theta\mid Z].
   \tag{9}
   \]
   Once a parameter direction has acquired positive score-projection defect at one stage, later garbling cannot restore it without extra parameter-dependent or upstream side information.

5. **For the location Fisher metric of AF-140, the exact retained object is the conditional score.** For the translation family
   \[
   p_\theta(x)=p(x-\theta),
   \tag{10}
   \]
   the parameter score at `theta=0` is `-rho(X)`, where `rho=grad log p` is AF-140's location score. Therefore its source metric `J` obeys
   \[
   \boxed{
   J_Y
   =
   \mathbb E\!\left[
   \mathbb E[\rho(X)\mid Y]
   \mathbb E[\rho(X)\mid Y]^T
   \right],
   }
   \tag{11}
   \]
   and
   \[
   \boxed{
   J-J_Y
   =
   \mathbb E[\operatorname{Cov}(\rho(X)\mid Y)].
   }
   \tag{12}
   \]
   Thus a full-law Fisher repair survives a downstream observation exactly in the score directions that the observation retains.

The reusable Arithmetic Fidelity conclusion is:

\[
\boxed{
\begin{array}{c}
\text{statistical canonicity and compression fidelity are different obligations;}\\
\text{Fisher geometry may be canonical for the declared statistical source,}\\
\text{yet a compression preserves it only to the extent that it preserves the score.}
\end{array}}
\tag{13}
\]

## Derivation

### The induced score is a conditional expectation

For clarity first suppose the Markov kernel has a density `k(y|x)` with respect to a fixed measure `nu`; the same statement follows in the general dominated-kernel formulation by Radon-Nikodym differentiation. The induced density is

\[
q_\theta(y)=\int k(y\mid x)p_\theta(x)\,d\mu(x).
\tag{14}
\]

Because `K` is independent of `theta` and differentiation is permitted under the integral,

\[
\nabla_\theta q_\theta(y)
=
\int k(y\mid x)\nabla_\theta p_\theta(x)\,d\mu(x)
=
\int k(y\mid x)p_\theta(x)S_\theta(x)\,d\mu(x).
\tag{15}
\]

Dividing by `q_theta(y)` on its positive support gives

\[
\nabla_\theta\log q_\theta(y)
=
\frac{\int k(y\mid x)p_\theta(x)S_\theta(x)\,d\mu(x)}
{\int k(y\mid x)p_\theta(x)\,d\mu(x)}
=
\mathbb E_\theta[S_\theta(X)\mid Y=y],
\tag{16}
\]

which is `(3)`.

This identity is the key category gate. It uses a genuine statistical channel that does not itself depend on the unknown parameter. A parameter-dependent kernel can inject score terms of its own and is not merely a compression of the original experiment.

### Fisher contraction is exactly AF-009 applied to the score

Set

\[
m_Y=\mathbb E_\theta[S_\theta\mid Y]=S^Y_\theta.
\tag{17}
\]

Conditional expectation is the orthogonal projection in `L^2(P_theta)`. Therefore

\[
S_\theta=m_Y+(S_\theta-m_Y),
\qquad
\mathbb E_\theta[(S_\theta-m_Y)m_Y^T]=0.
\tag{18}
\]

Taking second moments yields

\[
I_X
=
\mathbb E_\theta[m_Ym_Y^T]
+
\mathbb E_\theta[(S_\theta-m_Y)(S_\theta-m_Y)^T].
\tag{19}
\]

By `(3)`, the first term is exactly `I_Y`. This proves `(4)`.

Mathematically, the Pythagorean step is precisely AF-009 with discriminator `D=S_theta(X)`. The additional nontrivial bridge is `(3)`: after statistical compression, the optimal `L^2` predictor of the upstream score is not merely an auxiliary statistic but is exactly the score of the induced experiment. This identifies AF-009's discriminator defect with the classical Fisher-information loss.

Equation `(6)` follows by applying `(4)` to the scalar score direction `a^TS_theta`. It is intentionally a **pointwise-in-parameter local statement**. Score measurability at one `theta` must not be promoted automatically to global Fisher-Neyman sufficiency for the whole family.

### Composition is an exact orthogonal decomposition

For a `theta`-independent Markov chain `X -> Y -> Z`, the induced score identities give

\[
S^Y_\theta=\mathbb E[S_\theta\mid Y],
\qquad
S^Z_\theta=\mathbb E[S^Y_\theta\mid Z].
\tag{20}
\]

Now decompose

\[
S_\theta-S^Z_\theta
=
(S_\theta-S^Y_\theta)+(S^Y_\theta-S^Z_\theta).
\tag{21}
\]

The first term is orthogonal to every square-integrable function of `Y`, and hence to the second term. Taking covariance matrices gives `(8)`. The defect therefore localizes exactly where score geometry is lost in a compression chain instead of assigning all failure to the final representation.

## Exact matched control: a Gaussian translation direction erased by projection

Let

\[
X=(X_1,X_2)\sim N(\theta,I_2),
\qquad
\theta=(\theta_1,\theta_2).
\tag{22}
\]

The full-data score is

\[
S_\theta(X)=X-\theta,
\qquad
I_X=I_2.
\tag{23}
\]

Compress to the deterministic statistic

\[
Y=X_1.
\tag{24}
\]

Then

\[
\mathbb E[S_\theta(X)\mid Y]
=(X_1-\theta_1,0)^T,
\tag{25}
\]

so

\[
I_Y=
\begin{pmatrix}
1&0\\
0&0
\end{pmatrix},
\qquad
I_X-I_Y=
\begin{pmatrix}
0&0\\
0&1
\end{pmatrix}.
\tag{26}
\]

The compression is perfectly faithful to the first translation direction and completely blind to the second. Nothing about the canonicity of the Fisher metric prevents this collapse. The kernel in `(6)` identifies the surviving parameter direction exactly.

A second compression that is only a function or garbling of `Y` cannot restore `theta_2`; doing so requires adding information not present in the retained experiment.

## Prior art and novelty assessment

The core mathematics is classical and no theorem-level novelty is claimed.

- Thomas A. Louis, **“Finding the Observed Information Matrix When Using the EM Algorithm,”** *Journal of the Royal Statistical Society: Series B (Methodological)* 44(2), 226–233 (1982), DOI `10.1111/j.2517-6161.1982.tb01203.x`. Role: classical missing-information / incomplete-data information decomposition using complete-data scores and conditional expectations; direct prior art for interpreting observed Fisher information as what remains after latent-data compression.
- Nihat Ay, Jürgen Jost, Hông Vân Lê, and Lorenz J. Schwachhöfer, **“Information geometry and sufficient statistics,”** *Probability Theory and Related Fields* 162(1–2), 327–364 (2015), DOI `10.1007/s00440-014-0574-8`, arXiv:`1207.6736`. Role: general parametrized-measure-model treatment of Fisher monotonicity under Markov morphisms, preservation under sufficient statistics, and the Chentsov-type characterization of Fisher geometry by invariance under sufficient statistics.
- Kaori Yamaguchi and Hiraku Nozawa, **“On statistics which are almost sufficient from the viewpoint of the Fisher metrics,”** *Information Geometry* 7, 543–553 (2024), DOI `10.1007/s41884-024-00160-1`, arXiv:`2305.04199`. Role: direct quantitative prior art treating a statistic's Fisher-metric contraction as information loss and studying bi-Lipschitz / almost-sufficient retention.
- Shun-ichi Amari and Hiroshi Nagaoka, ***Methods of Information Geometry***, Translations of Mathematical Monographs 191, American Mathematical Society / Oxford University Press (2000), DOI `10.1090/MMONO/191`. Role: standard information-geometric source for Fisher monotonicity, sufficient statistics, and the distinction between statistical models and their induced models.

Thus Fisher monotonicity, score conditioning, missing-information decompositions, and sufficient-statistic invariance are established statistics/information-geometry results. The Arithmetic Fidelity contribution is the **bridge and audit rule** created by placing them after AF-009 and AF-140:

- AF-009 already identifies conditional variance as the exact `L^2` defect for an arbitrary declared discriminator;
- AF-140 shows that a full-law Fisher matrix can be an independently natural source metric;
- AF-141 identifies the Fisher metric's own downstream loss with AF-009 applied to the score and therefore separates **source-metric canonicity** from **compression fidelity**.

Chentsov-type uniqueness does not remove this distinction. Uniqueness/invariance under sufficient or congruent transformations says why Fisher geometry is canonical in a statistical category; it does not say that an arbitrary lossy statistic or Markov channel preserves that geometry. Equation `(4)` gives the exact obstruction.

## Boundary conditions and falsification tests

1. **Regular dominated model.** The score identity requires enough differentiability and domination to interchange parameter differentiation with the kernel integral. Singular models, moving supports, nondominated families, or nonsquare-integrable scores need separate treatment.

2. **Parameter-independent channel.** If `K` depends on `theta`, the output score contains a channel-score contribution. Such a map can introduce new parameter information and is not a pure downstream compression.

3. **Local versus global sufficiency.** Equality `I_X(theta)=I_Y(theta)` at one parameter value means local score preservation there. It does not by itself imply a globally sufficient statistic. Global sufficiency requires the appropriate whole-family hypotheses and factorization/conditional-law condition.

4. **Fisher retains only infinitesimal statistical discrimination.** Two globally distinct experiments can agree in Fisher geometry at a point or even along a restricted tangent family. Exact experiment equivalence is a stronger object, addressed by likelihood-ratio/Blackwell-type criteria such as AF-012 and AF-013.

5. **A metric may survive while the desired arithmetic discriminator does not.** Preserving all Fisher directions of a chosen statistical model only preserves the model's tangent score geometry. If the chosen model or smoothing has already forgotten rational-prime provenance, zero Fisher defect cannot recover it.

6. **Arbitrary probabilization remains arbitrary.** AF-140's source-category warning remains binding. Inventing a probability law, translation family, noise kernel, or smoothing scale solely to obtain a Fisher metric does not make that metric intrinsic to an arithmetic carrier.

7. **Approximate retention needs a declared geometry.** Small `I_X-I_Y` in one coordinate system is not automatically a coordinate-free scalar guarantee. The meaningful statement is quadratic-form control relative to the source Fisher metric, for example a lower bound `I_Y >= delta^2 I_X` on the relevant tangent subspace, as in almost-sufficiency frameworks.

## Consequence for the current frontier

AF-140 opened a full-law escape from the covariance-only ceiling. AF-141 closes the next possible shortcut: **using Fisher geometry does not itself solve the information-survival problem.** The exact retained carrier under a statistical observation is the conditional score, and its lost directions are the positive eigenspace of the score-projection defect `(4)`.

For any future Fisher-based or statistically regularized Mathia carrier, the required gate is now explicit:

1. derive the statistical/translation model intrinsically from the source rather than choosing it for convenience;
2. identify the observation/compression as a parameter-independent channel;
3. compute or bound the score-projection defect `I_X-I_Y` in the parameter directions that encode the claimed discriminator;
4. if a later spectral or target-relative construction uses the retained Fisher metric, propagate only those directions that survive this gate;
5. test matched arithmetic controls at the same retained-score layer, because zero Fisher loss inside a chosen model is not evidence that the model itself distinguishes rational primes.

The next useful advance is therefore not a more canonical generic Fisher metric. It is a **source-natural statistical model plus a non-escape theorem for the specific score directions needed by the downstream arithmetic target**, or a matched-control construction proving that those directions already collide.