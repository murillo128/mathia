# AF-141 — Fisher information loss is the conditional score-projection defect

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-IDENTITY`, `FIDELITY-BRIDGE`, `CATEGORY-GATE`, `NO-NOVELTY-CLAIM`

## Claim

AF-140 shows that a source-natural smooth translation law can supply a full-law Fisher metric with the generator-gauge transport required by AF-138. That resolves a canonicity problem but not a compression-fidelity problem: a canonical Fisher metric can itself contract when the statistical source is replaced by a statistic or noisy observation.

Let `Theta` be an open subset of `R^d`, and let `{P_theta}` be a regular dominated statistical model on a sample space `X`, with density `p_theta(x)`, square-integrable score

\[
S_\theta(X)=\nabla_\theta\log p_\theta(X),
\qquad
\mathbb E_\theta S_\theta=0,
\tag{1}
\]

and Fisher matrix

\[
I_X(\theta)=\mathbb E_\theta[S_\theta S_\theta^T].
\tag{2}
\]

Let `Y` be obtained from `X` through a Markov kernel `K(dy|x)` independent of `theta`. Assume the induced model on `Y` is dominated and that differentiation may be interchanged with the kernel integral. If `S^Y_theta(Y)` and `I_Y(theta)` are the induced score and Fisher matrix, then:

1. **The retained score is the conditional expectation of the upstream score:**
   \[
   \boxed{S^Y_\theta(Y)=\mathbb E_\theta[S_\theta(X)\mid Y]}
   \quad\text{a.s.}
   \tag{3}
   \]

2. **Fisher information loss is exactly an `L^2` projection defect:**
   \[
   \boxed{
   I_X(\theta)-I_Y(\theta)
   =\mathbb E_\theta[(S_\theta-S^Y_\theta)(S_\theta-S^Y_\theta)^T]
   =\mathbb E_\theta[\operatorname{Cov}_\theta(S_\theta\mid Y)]
   \succeq0.
   }
   \tag{4}
   \]

3. **Surviving parameter directions are exact score-measurability directions.** For `a in R^d`,
   \[
   a^T(I_X-I_Y)a
   =\mathbb E_\theta\left[
   \bigl(a^TS_\theta-\mathbb E_\theta[a^TS_\theta\mid Y]\bigr)^2
   \right],
   \tag{5}
   \]
   so
   \[
   \boxed{
   a\in\ker(I_X-I_Y)
   \iff
   a^TS_\theta(X)\text{ is }\sigma(Y)\text{-measurable a.s.}
   }
   \tag{6}
   \]
   Full equality at a fixed parameter value holds exactly when the whole score vector is retained there.

4. **The defect adds exactly along a Markov compression chain.** If
   \[
   X\longrightarrow Y\longrightarrow Z
   \tag{7}
   \]
   is a chain of `theta`-independent Markov kernels satisfying the same regularity assumptions, then
   \[
   \boxed{I_X-I_Z=(I_X-I_Y)+(I_Y-I_Z).}
   \tag{8}
   \]
   In particular,
   \[
   S^Z_\theta
   =\mathbb E_\theta[S^Y_\theta\mid Z]
   =\mathbb E_\theta[S_\theta\mid Z].
   \tag{9}
   \]

5. **For AF-140's location Fisher metric, the retained metric is the conditional-score metric.** For
   \[
   p_\theta(x)=p(x-\theta),
   \tag{10}
   \]
   the parameter score at `theta=0` is `-rho(X)`, where `rho=grad log p`. Hence
   \[
   \boxed{
   J_Y=
   \mathbb E\!\left[
   \mathbb E[\rho(X)\mid Y]
   \mathbb E[\rho(X)\mid Y]^T
   \right],
   }
   \tag{11}
   \]
   and
   \[
   \boxed{J-J_Y=\mathbb E[\operatorname{Cov}(\rho(X)\mid Y)].}
   \tag{12}
   \]

Thus **statistical canonicity and compression fidelity are separate obligations**. Fisher geometry may be canonical for the declared statistical source, yet a compression preserves it only to the extent that it preserves the score.

## Derivation

### The induced score is a conditional expectation

Suppose first that the kernel has density `k(y|x)` with respect to a fixed measure `nu`. The induced density is

\[
q_\theta(y)=\int k(y\mid x)p_\theta(x)\,d\mu(x).
\tag{13}
\]

Because the kernel is parameter-independent,

\[
\nabla_\theta q_\theta(y)
=\int k(y\mid x)p_\theta(x)S_\theta(x)\,d\mu(x).
\tag{14}
\]

On the positive support of `q_theta`, division by `(13)` gives

\[
\nabla_\theta\log q_\theta(y)
=\mathbb E_\theta[S_\theta(X)\mid Y=y],
\tag{15}
\]

proving `(3)`. The general dominated-kernel version is the same Radon-Nikodym calculation.

The parameter-independence assumption is structural. If the channel itself depends on `theta`, its score contributes new terms; such a map can inject parameter information and is not merely a downstream compression of the original experiment.

### Fisher contraction is AF-009 applied to the score

Set

\[
m_Y=\mathbb E_\theta[S_\theta\mid Y]=S^Y_\theta.
\tag{16}
\]

Conditional expectation is the orthogonal projection in `L^2(P_theta)`, so

\[
S_\theta=m_Y+(S_\theta-m_Y),
\qquad
\mathbb E_\theta[(S_\theta-m_Y)m_Y^T]=0.
\tag{17}
\]

Taking second moments gives

\[
I_X
=\mathbb E_\theta[m_Ym_Y^T]
+\mathbb E_\theta[(S_\theta-m_Y)(S_\theta-m_Y)^T].
\tag{18}
\]

The first term is `I_Y` by `(3)`, proving `(4)`. The Pythagorean step is exactly AF-009 with discriminator `D=S_theta(X)`; the additional bridge is that the optimal predictor of the upstream score is itself the score of the induced statistical experiment.

Equation `(6)` follows by applying `(4)` to the scalar direction `a^TS_theta`. It is deliberately pointwise in `theta`: score measurability at one parameter value must not be promoted automatically to global Fisher-Neyman sufficiency for the full family.

### Composition requires the Markov conditional-independence step

For a parameter-independent Markov chain `X -> Y -> Z`,

\[
S^Y_\theta=\mathbb E[S_\theta\mid Y],
\qquad
S^Z_\theta=\mathbb E[S^Y_\theta\mid Z].
\tag{19}
\]

The second identity follows because the Markov property gives

\[
\mathbb E[S_\theta\mid Y,Z]=\mathbb E[S_\theta\mid Y]=S^Y_\theta,
\tag{20}
\]

and then conditioning on `Z` yields `(19)`. Decompose

\[
S_\theta-S^Z_\theta
=(S_\theta-S^Y_\theta)+(S^Y_\theta-S^Z_\theta).
\tag{21}
\]

The cross term vanishes because

\[
\mathbb E[S_\theta-S^Y_\theta\mid Y,Z]=0,
\tag{22}
\]

while `S^Y_theta-S^Z_theta` is measurable with respect to `(Y,Z)`. Taking second moments gives `(8)`. Thus the exact score defect localizes the stage at which Fisher geometry is lost.

## Exact matched control: a translation direction erased by projection

Let

\[
X=(X_1,X_2)\sim N(\theta,I_2),
\qquad
\theta=(\theta_1,\theta_2).
\tag{23}
\]

The full score is `S_theta(X)=X-theta`, hence `I_X=I_2`. Compress to the deterministic statistic `Y=X_1`. Then

\[
\mathbb E[S_\theta(X)\mid Y]=(X_1-\theta_1,0)^T,
\tag{24}
\]

and therefore

\[
I_Y=
\begin{pmatrix}1&0\\0&0\end{pmatrix},
\qquad
I_X-I_Y=
\begin{pmatrix}0&0\\0&1\end{pmatrix}.
\tag{25}
\]

The same canonical Fisher geometry is perfectly retained in the first translation direction and completely erased in the second. A later garbling of `Y` cannot recover `theta_2` without extra side information.

## Prior art and novelty assessment

The core mathematics is classical and no theorem-level novelty is claimed.

- Thomas A. Louis, **“Finding the Observed Information Matrix When Using the EM Algorithm,”** *Journal of the Royal Statistical Society: Series B (Methodological)* 44(2), 226–233 (1982), DOI `10.1111/j.2517-6161.1982.tb01203.x`. Role: classical missing-information / incomplete-data decomposition using complete-data scores and conditional expectations.
- Nihat Ay, Jürgen Jost, Hông Vân Lê, and Lorenz J. Schwachhöfer, **“Information geometry and sufficient statistics,”** *Probability Theory and Related Fields* 162(1–2), 327–364 (2015), DOI `10.1007/s00440-014-0574-8`, arXiv:`1207.6736`. Role: general parametrized-measure-model treatment of Fisher monotonicity under Markov morphisms, preservation under sufficient statistics, and Chentsov-type characterization by invariance under sufficient statistics.
- Kaori Yamaguchi and Hiraku Nozawa, **“On statistics which are almost sufficient from the viewpoint of the Fisher metrics,”** *Information Geometry* 7, 543–553 (2024), DOI `10.1007/s41884-024-00160-1`, arXiv:`2305.04199`. Role: direct quantitative prior art treating Fisher-metric contraction as information loss and studying almost-sufficient retention.
- Shun-ichi Amari and Hiroshi Nagaoka, ***Methods of Information Geometry***, Translations of Mathematical Monographs 191, American Mathematical Society / Oxford University Press (2000), DOI `10.1090/MMONO/191`. Role: standard information-geometric source for Fisher monotonicity and sufficient statistics.

Fisher monotonicity, score conditioning, missing-information decompositions, and sufficient-statistic invariance are therefore established mathematics. The Arithmetic Fidelity contribution is the bridge and audit rule obtained by placing them after AF-009 and AF-140: AF-009 supplies the generic conditional-variance fidelity defect; AF-140 supplies a full-law source-natural Fisher metric; AF-141 identifies that metric's own downstream loss with the score instance of AF-009.

Chentsov-type uniqueness does not erase this distinction. It explains why Fisher geometry is canonical within the relevant statistical category; it does not imply that an arbitrary lossy statistic or Markov channel preserves that geometry. Equation `(4)` is the exact obstruction.

## Boundary conditions and falsification tests

1. **Regularity is real.** The score identity needs domination, differentiability and enough integrability to exchange differentiation and kernel integration. Moving supports, singular models, nondominated families or nonsquare-integrable scores need separate treatment.

2. **The channel must be parameter-independent.** A parameter-dependent kernel can carry its own score and is not a pure compression.

3. **Local Fisher equality is weaker than global sufficiency.** Equality at one `theta` means local score preservation there. Whole-family sufficiency requires the appropriate global conditional-law or factorization hypotheses.

4. **Fisher geometry is only infinitesimal statistical discrimination.** Two globally distinct experiments can share Fisher geometry at a point or along a tangent family. Exact experiment equivalence is stronger and is addressed by likelihood-ratio/Blackwell criteria such as AF-012 and AF-013.

5. **Zero Fisher loss does not prove arithmetic fidelity.** It only says that the chosen statistical model's score directions survive. If the model or smoothing already forgot rational-prime provenance, no downstream Fisher calculation repairs that earlier loss.

6. **Arbitrary probabilization remains arbitrary.** AF-140's source-category warning remains binding: a probability law, translation family, noise kernel or smoothing scale chosen solely to obtain Fisher geometry is new gauge data unless independently forced by the source mathematics.

7. **Approximate retention must be metric-relative.** A meaningful coordinate-invariant quantitative guarantee compares quadratic forms, e.g. `I_Y >= delta^2 I_X` on a declared tangent subspace, rather than treating a raw matrix norm of `I_X-I_Y` as canonical.

## Consequence for the current frontier

AF-140 opened a full-law escape from the covariance-only ceiling. AF-141 closes the next shortcut: **using Fisher geometry does not itself solve information survival.** Under a statistical observation, the retained carrier is the conditional score and the lost directions are exactly the positive directions of the score-projection defect `(4)`.

A future Fisher-based Mathia carrier must therefore pass four separate gates: the statistical model must be source-natural; the observation must be an honest parameter-independent compression; the arithmetic-relevant score directions must have zero or quantitatively controlled defect; and matched controls must still be tested at the retained-score layer. The next useful advance is consequently a source-natural statistical model plus a non-escape theorem for the specific score directions needed downstream, or a matched-control construction showing that those directions already collide.