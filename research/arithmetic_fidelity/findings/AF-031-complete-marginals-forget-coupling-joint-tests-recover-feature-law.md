# AF-031 — Complete marginals can forget coupling; joint tests recover the feature law

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-IDENTITY`, `NEGATIVE/OBSTRUCTION`

## Claim

Let `X` be a compact Hausdorff space, let

\[
\phi_i:X\to Y_i,
\qquad i=1,\ldots,d,
\]

be continuous maps into compact Hausdorff spaces, and write

\[
\Phi=(\phi_1,\ldots,\phi_d):X\to Y_1\times\cdots\times Y_d.
\]

For a finite signed regular Borel measure `\mu` on `X`, there are two different exact compression levels.

The **joint feature law** is

\[
J_\Phi(\mu)=\Phi_*\mu,
\]

while the **complete marginal law** is

\[
M_\Phi(\mu)=\bigl((\phi_1)_*\mu,\ldots,(\phi_d)_*\mu\bigr).
\]

Then:

1. **Marginalization is a genuine downstream compression.** There is a canonical linear map
   \[
   \operatorname{Marg}:M(\Phi(X))\to\prod_{i=1}^d M(Y_i)
   \]
   obtained by coordinate pushforward such that
   \[
   \boxed{M_\Phi=\operatorname{Marg}\circ J_\Phi.}
   \]
   Consequently
   \[
   \boxed{\ker J_\Phi\subseteq\ker M_\Phi.}
   \]
   The quotient
   \[
   \boxed{\mathcal C_\Phi:=\ker M_\Phi/\ker J_\Phi}
   \]
   is the exact linear **coupling-defect space**: source perturbations invisible to every separate feature channel but still visible in the joint relation among those channels.

2. **Complete separate observables determine only the marginals.** Equality of
   \[
   \int_X f_i(\phi_i(x))\,d\mu(x)
   \]
   for every `i` and every `f_i\in C(Y_i)` is equivalent to
   \[
   M_\Phi(\mu)=M_\Phi(\nu).
   \]
   No amount of additional processing that factors only through these separate marginal laws can recover a nonzero class in `\mathcal C_\Phi`.

3. **Complete joint observables determine exactly the joint feature law.** Equality of
   \[
   \int_X g(\Phi(x))\,d\mu(x)
   \]
   for every `g\in C(\Phi(X))` is equivalent to
   \[
   \boxed{J_\Phi(\mu)=J_\Phi(\nu).}
   \]
   Hence the correct retained object for relational fidelity is the joint pushforward, not the tuple of complete marginals.

4. **Joint features are fully source-faithful exactly when the feature map is injective.** On all finite signed measures,
   \[
   \boxed{J_\Phi\text{ is injective}\iff \Phi\text{ is injective}.}
   \]
   Thus a feature tuple may jointly contain enough information to recover the source while its separately retained channels still lose the coupling that makes the tuple informative.

5. **Compact real features give a moment realization of the same distinction.** If each `Y_i` is a compact subset of `\mathbb R`, then retaining every one-variable polynomial moment
   \[
   \int \phi_i(x)^n\,d\mu(x)
   \qquad(i=1,\ldots,d,\ n\ge0)
   \]
   determines exactly the complete marginal law `M_\Phi(\mu)`. Retaining every mixed monomial moment
   \[
   \boxed{
   \int_X \phi_1(x)^{\alpha_1}\cdots\phi_d(x)^{\alpha_d}\,d\mu(x),
   \qquad \alpha\in\mathbb N^d,
   }
   \]
   determines exactly the joint feature law `J_\Phi(\mu)`.

6. **Complete marginals can fail even when the joint feature map is injective.** On
   \[
   X=\{0,1\}^2
   \]
   with coordinate maps `x,y`, let
   \[
   P=\tfrac12\delta_{(0,0)}+\tfrac12\delta_{(1,1)},
   \qquad
   Q=\tfrac12\delta_{(0,1)}+\tfrac12\delta_{(1,0)}.
   \]
   Then both coordinate marginals are the same Bernoulli distribution, so **all** separate moments of `x` and `y` agree. But
   \[
   \int xy\,dP=\tfrac12,
   \qquad
   \int xy\,dQ=0.
   \]
   The joint map `(x,y)` is the identity and therefore injective; the loss is entirely the subsequent marginalization step.

7. **Restricted source classes have an exact gate.** For `\mathcal S\subset M(X)`, separate-channel fidelity and joint-feature fidelity are respectively
   \[
   \boxed{
   (\mathcal S-\mathcal S)\cap\ker M_\Phi=\{0\}
   }
   \]
   and
   \[
   \boxed{
   (\mathcal S-\mathcal S)\cap\ker J_\Phi=\{0\}.
   }
   \]
   Thus source-specific constraints can make marginals sufficient, but this must be proved from the admissible source class rather than inferred from completeness of each channel separately.

The reusable Arithmetic Fidelity conclusion is

\[
\boxed{
\text{complete channel-wise information}
\not\Rightarrow
\text{complete relational information}.
}
\]

The missing object is not necessarily another scalar statistic. It is the coupling class left in `\mathcal C_\Phi` after the joint law has been compressed to its marginals.

## Exact factorization and kernel hierarchy

Let

\[
K=\Phi(X)\subseteq Y_1\times\cdots\times Y_d.
\]

For each coordinate projection `\pi_i:K\to Y_i`,

\[
(\phi_i)_*\mu
=(\pi_i)_*(\Phi_*\mu).
\]

Therefore

\[
M_\Phi(\mu)
=
\bigl((\pi_1)_*J_\Phi(\mu),\ldots,(\pi_d)_*J_\Phi(\mu)\bigr),
\]

which proves the canonical factorization

\[
M_\Phi=\operatorname{Marg}\circ J_\Phi.
\]

Any signed measure killed by `J_\Phi` is necessarily killed by every coordinate pushforward, so

\[
\ker J_\Phi\subseteq\ker M_\Phi.
\]

This inclusion identifies two logically different losses.

- `\ker J_\Phi` consists of source differences already invisible to the entire joint feature tuple.
- `\ker M_\Phi/\ker J_\Phi` consists of differences that the tuple still sees jointly but that disappear only when the destination forgets the dependence among channels.

The latter quotient is therefore a precise realization of relational or provenance loss under a second compression stage. It is not captured by asking whether every individual channel is itself measured completely.

## Why complete separate tests stop at the marginals

For one coordinate,

\[
\int_X f_i(\phi_i(x))\,d\mu(x)
=
\int_{Y_i}f_i(y)\,d((\phi_i)_*\mu)(y).
\]

Equality for all `f_i\in C(Y_i)` determines the pushforward measure uniquely by the Riesz representation theorem. Repeating this independently for every coordinate gives exactly the tuple

\[
M_\Phi(\mu).
\]

But a test of the form

\[
f_1(\phi_1)+\cdots+f_d(\phi_d)
\]

still integrates using only those separate marginals. Arbitrary downstream nonlinear manipulation of the already-compressed marginal measures cannot distinguish two sources with the same `M_\Phi`, because such manipulation factors through the same destination fiber.

This is the measurement-level analogue of AF-030's generated-algebra warning. Rich mathematics that can be formed **after** a compression does not become retained source information unless its value is determined by the destination. In particular, knowing every function of each channel separately does not give the value of a genuinely joint function such as

\[
g(\phi_1,\phi_2).
\]

## Mixed moments recover the compact joint feature law

Assume now that each feature is real-valued with compact image. Then

\[
K=\Phi(X)\subset\mathbb R^d
\]

is compact.

If all mixed monomial moments agree for `\mu` and `\nu`, then the pushforward difference

\[
\rho=\Phi_*(\mu-\nu)
\]

annihilates every polynomial on `K`:

\[
\int_K p(z)\,d\rho(z)=0.
\]

The restrictions of real polynomials to `K` form a unital subalgebra of `C(K)` that separates points. Stone-Weierstrass therefore gives uniform density in `C(K)`. Since integration against `\rho` is continuous in the uniform norm,

\[
\int_K g\,d\rho=0
\qquad\forall g\in C(K),
\]

and hence `\rho=0`. Therefore

\[
\boxed{
\text{all mixed moments agree}
\iff
\Phi_*\mu=\Phi_*\nu.
}
\]

By contrast, all one-variable moments of each coordinate determine only the individual pushforwards `(\phi_i)_*\mu`, because the corresponding measured linear space contains no mixed monomials unless they are explicitly retained or exactly reducible to the separate destination.

This also clarifies what “adding products” means after AF-030. If the destination actually stores the integrals of all mixed products, those products are genuine retained observables and their polynomial span can be dense on the joint feature image. If it stores only the original separate integrals, algebraically generating products on the source side still creates no new destination information.

## Binary coupling counterexample

Take the four-point compact space

\[
X=\{(0,0),(0,1),(1,0),(1,1)\}
\]

with `\Phi(x,y)=(x,y)`. The map `\Phi` is injective, so the complete joint feature law is identical to the source probability measure.

Now define

\[
P=\tfrac12\delta_{(0,0)}+\tfrac12\delta_{(1,1)},
\qquad
Q=\tfrac12\delta_{(0,1)}+\tfrac12\delta_{(1,0)}.
\]

For either measure, both coordinates are Bernoulli with mass `1/2` at `0` and `1/2` at `1`. Hence

\[
(x)_*P=(x)_*Q,
\qquad
(y)_*P=(y)_*Q,
\]

and therefore

\[
M_\Phi(P)=M_\Phi(Q).
\]

Because `0^n=0` and `1^n=1` for every `n\ge1`, every separate polynomial moment agrees as well.

The mixed product detects the dependence immediately:

\[
\mathbb E_P[xy]=\tfrac12,
\qquad
\mathbb E_Q[xy]=0.
\]

Thus the same complete marginal information is compatible with positive correlation and negative correlation while the joint feature tuple itself is perfectly source-faithful. The difference

\[
\eta=P-Q
\]

is an explicit nonzero element of

\[
\ker M_\Phi\setminus\ker J_\Phi,
\]

so the coupling-defect quotient is genuinely nontrivial.

## Full source fidelity of the joint feature map

If `\Phi` is injective, compactness of `X` and Hausdorffness of the product imply that

\[
\Phi:X\to K
\]

is a homeomorphism. Hence `\Phi_*\mu=\Phi_*\nu` implies `\mu=\nu` by pushing back through `\Phi^{-1}`.

Conversely, if `\Phi` is not injective, choose distinct `x,x'\in X` with

\[
\Phi(x)=\Phi(x').
\]

Then

\[
\Phi_*\delta_x=\Phi_*\delta_{x'},
\]

so `J_\Phi` is not injective even on positive probability measures.

Therefore

\[
\boxed{
J_\Phi\text{ faithful on all finite measures}
\iff
\Phi\text{ injective}.
}
\]

The marginal compression has no analogous pointwise criterion in terms of injectivity of the tuple, because it deliberately discards the tuple's joint law after that law has been formed.

## Restricted classes and admissible relational lifts

For an admissible source class `\mathcal S`, ambient coupling ambiguity matters only when an admissible difference direction realizes it. Exact marginal fidelity is

\[
M_\Phi|_{\mathcal S}\text{ injective}
\iff
(\mathcal S-\mathcal S)\cap\ker M_\Phi=\{0\},
\]

while exact joint-feature fidelity is

\[
J_\Phi|_{\mathcal S}\text{ injective}
\iff
(\mathcal S-\mathcal S)\cap\ker J_\Phi=\{0\}.
\]

This prevents an overstatement of the binary example. Independence, deterministic relations, monotone couplings, algebraic source constraints, or another model-specific theorem can make the marginals determine the joint law on a restricted family. But such a theorem is **additional retained structure**; it cannot be inferred merely from complete marginal measurement.

The same distinction applies to a proposed lift. Suppose a new feature `\psi` is added. Retaining its complete marginal law supplies more separate information, but it need not determine how `\psi` couples to the previously retained features. To certify relational fidelity one must show either:

- the enlarged destination contains enough genuinely joint observables to determine the relevant joint pushforward; or
- the admissible source class forces the coupling uniquely from the retained marginals.

Without one of those mechanisms, “every component is known exactly” is not a recovery theorem for the whole structured object.

## Prior art and novelty assessment

The mathematical ingredients and the dependence-versus-marginals distinction are classical.

- Marshall H. Stone, **“The Generalized Weierstrass Approximation Theorem,”** *Mathematics Magazine* 21(4) (1948), 167–184, and 21(5), 237–254. Role: polynomial restrictions on a compact subset of `\mathbb R^d` form a unital point-separating algebra, so complete mixed polynomial moments determine the compactly supported joint pushforward measure.
- Abe Sklar, **“Fonctions de répartition à n dimensions et leurs marges,”** *Publications de l'Institut de Statistique de l'Université de Paris* 8 (1959), 229–231. Role: foundational copula theorem; a multivariate distribution consists of its marginals together with a dependence/coupling object, directly delimiting any novelty claim for the observation that complete marginals need not determine the joint law.
- Harald Cramér and Herman Wold, **“Some Theorems on Distribution Functions,”** *Journal of the London Mathematical Society* s1-11(4) (1936), 290–294, DOI `10.1112/jlms/s1-11.4.290`. Role: classical Cramér-Wold recovery theorem; the full joint distribution can be recovered from all one-dimensional linear projections, showing that mixed monomials are one convenient complete relational family, not a uniquely necessary encoding.
- Mihai Putinar and Konrad Schmüdgen, **“Multivariate Determinateness,”** arXiv:`0810.0840` (2008). Role: broad multivariate moment-problem prior art and determinacy criteria; prevents treating multivariate moment recovery itself as an Arithmetic Fidelity novelty.

No novelty is claimed for pushforward measures, marginal distributions, copulas, compact moment determinacy, Stone-Weierstrass, or Cramér-Wold. The reusable Arithmetic Fidelity contribution is the exact **two-stage kernel audit**

\[
\boxed{
\mu
\longmapsto
\Phi_*\mu
\longmapsto
\bigl((\phi_i)_*\mu\bigr)_i,
}
\]

which separates source-to-feature loss from subsequent relation-to-marginals loss and makes the latter measurable as

\[
\ker M_\Phi/\ker J_\Phi.
\]

This is the abstract version of a pattern already visible in AF-004 and AF-006: individually rich channels can still forget the cross-channel relation that carries the discriminator.

## Boundaries and failure modes

- Compactness is essential to the simple polynomial-density argument. On unbounded support, equality of all moments need not determine a measure without additional determinacy hypotheses.
- Complete mixed monomials are sufficient to recover the compact joint feature law but are not asserted to be a minimal observable family. Cramér-Wold gives a different complete family, and other categories can have more economical determining classes.
- The theorem distinguishes marginals from the joint law; it does not claim that every useful discriminator depends on coupling. A target constant on marginal fibers is already recoverable from the marginal destination.
- The quotient `\mathcal C_\Phi` is linear because it is defined on signed measures. For a nonlinear positive/probability source class, the operational collision set is the intersection of those fibers with the admissible class rather than the whole quotient vector space.
- If one coordinate `\phi_i` is already injective on `X`, its complete pushforward alone determines the source measure; the coupling defect can then vanish. The nontrivial phenomenon requires source directions invisible to all separate coordinate pushforwards but visible jointly.
- “Adding a feature” and “adding its relation to existing features” are different operations. A separate new channel may leave the old coupling ambiguity untouched.
- No arithmetic-specific conclusion follows automatically. A prime, spectral, positivity, or explicit-formula application must identify the concrete channels, the actual admissible joint observables, and a matched source class before invoking this theorem.

## Consequences for the research line

AF-030 identified the closed linear hull of the **actually retained** scalar tests as the exact information object for linear measurements. AF-031 adds a complementary warning for multi-channel representations: even when every channel is individually retained completely, compressing the joint law to separate marginals can erase a whole dependence sector.

This sharpens several recurring candidate-lift questions into one audit:

\[
\boxed{
\text{Are we adding more complete channels,
 or are we retaining the relations among them?}
}
\]

A proposed marked, boundary, transverse, phase, sign, or multi-component lift should therefore be tested at the destination level. If the compression keeps only channel-wise summaries, its exact coupling fiber must be computed before the lift is credited with structural fidelity. If the relevant relation is retained through mixed tests, matrix-valued measures, joint projections, or a source-specific uniqueness theorem, that mechanism should be stated explicitly.

For later rational-prime applications this gives a concrete stopping rule: separate completeness of several arithmetic or analytic summaries is not evidence that prime-specific provenance survives their aggregation. The surviving claim must either factor through the marginal destination or use an independently justified relational carrier that kills the relevant coupling defect.