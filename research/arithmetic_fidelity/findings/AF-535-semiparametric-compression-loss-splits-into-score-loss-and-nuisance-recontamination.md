# AF-535 — Semiparametric compression loss splits into score loss and nuisance recontamination

## Status

`EXACT-DERIVED` · `LITERATURE+DERIVED` · `CLASSICAL-INGREDIENTS` · `ARITHMETIC-FIDELITY` · `SEMIPARAMETRIC` · `EFFICIENT-SCORE` · `NUISANCE-TANGENT` · `DATA-PROCESSING` · `MINIMAL-LIFT` · `NO-NOVELTY-CLAIM`

## Claim

AF-141 identifies ordinary Fisher-information loss under a parameter-independent statistic or Markov channel with the conditional-projection defect of the score. AF-533 and AF-534 then show, in finite- and infinite-dimensional Gaussian nuisance models, that the relevant target carrier is not the raw score but the component transverse to the nuisance space. These two operations do not commute trivially in a general semiparametric model: after compression, a component that was orthogonal to nuisance upstream can become nuisance-like downstream.

At a fixed baseline distribution `P_0`, let

\[
H_X=L_0^2(P_0)
\]

and let `Lambda subset H_X` be the closed nuisance tangent space. Let `s in H_X` be the score for a scalar parameter of interest and define the full-observation efficient score

\[
 e=(I-\Pi_\Lambda)s,
 \qquad
 I_X^{\rm eff}=\|e\|_{H_X}^2.
\tag{1}
\]

Let a parameter-independent Markov kernel send `X` to `Y`, and under the baseline joint law define the conditional-expectation contraction

\[
 C:H_X\to H_Y:=L_0^2(Q_0),
 \qquad
 Cf=\mathbb E_0[f(X)\mid Y].
\tag{2}
\]

Assume the pushed-forward model is differentiable in quadratic mean and that its nuisance tangent space is

\[
 M=\overline{C\Lambda}\subset H_Y.
\tag{3}
\]

Then its target score is `Cs`, its efficient score is

\[
\boxed{
 e_Y=(I-\Pi_M)Ce,
}
\tag{4}
\]

and its efficient Fisher information satisfies the exact decomposition

\[
\boxed{
 I_X^{\rm eff}-I_Y^{\rm eff}
 =
 \underbrace{\bigl(\|e\|^2-\|Ce\|^2\bigr)}_{\text{direct efficient-score loss}}
 +
 \underbrace{\|\Pi_M Ce\|^2}_{\text{nuisance recontamination}}.
}
\tag{5}
\]

For a deterministic statistic, and more generally under the joint realization of the Markov kernel, the first term is

\[
\|e\|^2-\|Ce\|^2
=
\mathbb E_0\!\left[\operatorname{Var}_0(e(X)\mid Y)\right].
\tag{6}
\]

Thus a compression can destroy nuisance-robust target information in **two distinct ways**:

1. it can erase part of the full efficient score itself; and
2. even among the surviving conditional-score component, it can destroy the upstream target/nuisance separation by moving that component into the compressed nuisance tangent space.

The equality boundary is especially rigid:

\[
\boxed{
 I_Y^{\rm eff}=I_X^{\rm eff}
 \iff
 e(X)\text{ is }\sigma(Y)\text{-measurable under the baseline joint law.}
}
\tag{7}
\]

Consequently, among sigma-field lifts that retain the original observation `Y`, adjoining the full efficient score gives the smallest first-order repair in the ordinary information order:

\[
\boxed{
 \mathcal G_{\min}=\sigma(Y,e(X)).
}
\tag{8}
\]

More precisely, if `G` is any observation sigma-field with `sigma(Y) subset G subset sigma(X,Y)` and the induced nuisance tangent space is the closure of the corresponding conditional images of `Lambda`, then full efficient-information preservation forces `e` to be `G`-measurable. Hence every such full-fidelity lift contains `sigma(Y,e)`, while `sigma(Y,e)` itself preserves the full first-order efficient information.

This is a local, target-relative minimal lift. It does **not** say that the efficient score is a source-natural observable, globally sufficient statistic, or parameter-free object available to an implementation.

## Representation declaration

The source object is a local regular statistical experiment at a fixed baseline, with a declared scalar target direction and a declared nuisance tangent space.

- **Source representation:** the Hilbert tangent experiment `(H_X,s,Lambda)` at `P_0`.
- **Forward map:** a parameter-independent Markov kernel `K:X rightsquigarrow Y`, represented infinitesimally by conditional expectation `C`.
- **Represented downstream object:** the pushed-forward tangent experiment `(H_Y,Cs,M)` with `M=closure(C Lambda)`.
- **Target observable:** nuisance-robust first-order information about the scalar target parameter, measured by the squared efficient-score norm.
- **Equivalence:** target scores differing by nuisance tangent directions represent the same first-order target direction before taking the orthogonal representative.

Nothing here asserts that a statistical tangent representation is intrinsic to a particular arithmetic construction. An arithmetic application must independently justify the statistical source, target direction, nuisance class, and observation channel.

## Derivation

### Compression acts on both target and nuisance scores

Write

\[
 v=\Pi_\Lambda s,
 \qquad
 s=v+e,
 \qquad
 v\in\Lambda,
 \qquad
 e\perp\Lambda.
\tag{9}
\]

By the score-conditioning identity of AF-141, the target score after the parameter-independent Markov channel is

\[
 s_Y=Cs.
\tag{10}
\]

The same differentiation-under-the-kernel calculation applies to every regular nuisance path: if `lambda in Lambda` is a nuisance score upstream, its pushed-forward score is `C lambda`. After closure, the downstream nuisance tangent space is therefore `M` as declared in (3).

Since `Cv in C Lambda subset M`,

\[
\begin{aligned}
 e_Y
 &= (I-\Pi_M)Cs\\
 &= (I-\Pi_M)(Cv+Ce)\\
 &= (I-\Pi_M)Ce,
\end{aligned}
\tag{11}
\]

which proves (4).

This identity is the key distinction from simply applying AF-141 to the raw target score. The upstream efficient score is already nuisance-orthogonal, but conditional expectation need not preserve that orthogonality.

### Exact two-term information loss

Because `Pi_M` is an orthogonal projection,

\[
 I_Y^{\rm eff}
 =\|(I-\Pi_M)Ce\|^2
 =\|Ce\|^2-\|\Pi_MCe\|^2.
\tag{12}
\]

Subtracting from `I_X^{eff}=||e||^2` gives (5).

Both terms are nonnegative. The first is the ordinary Hilbert contraction defect of the efficient score. The second is a genuinely nuisance-relative penalty: it measures the portion of the surviving score that is statistically indistinguishable, to first order, from compressed nuisance variation.

When `C` is conditional expectation, its `L^2` Pythagorean identity gives

\[
\|e\|^2
=
\|Ce\|^2
+
\mathbb E_0[(e-Ce)^2],
\tag{13}
\]

and the last term is the expected conditional variance in (6).

### Equality is exact efficient-score recoverability

Suppose first that `I_Y^{eff}=I_X^{eff}`. Equation (5) is a sum of two nonnegative terms, so in particular

\[
\|Ce\|=\|e\|.
\tag{14}
\]

Conditional expectation is an orthogonal projection in the baseline joint `L^2` space. Equality of norms therefore holds exactly when

\[
 e=Ce,
\tag{15}
\]

that is, when `e(X)` is measurable with respect to `sigma(Y)`.

Conversely, assume `e` is `Y`-measurable. Then `Ce=e`. For every `lambda in Lambda`,

\[
\langle e,C\lambda\rangle_{H_Y}
=
\mathbb E_0[e(Y)\,\mathbb E_0(\lambda(X)\mid Y)]
=
\mathbb E_0[e(X)\lambda(X)]
=0.
\tag{16}
\]

Hence `e` is orthogonal to `C Lambda` and therefore to `M=closure(C Lambda)`. Equation (4) gives `e_Y=e`, so the efficient information is exactly preserved. This proves (7).

The argument also explains why the second term in (5) vanishes automatically at the equality boundary. If the whole efficient score survives as an output statistic, its upstream nuisance orthogonality transfers exactly to every compressed nuisance score.

### Minimal first-order lift

Let `G` be a sigma-field containing `sigma(Y)` and obtainable by retaining additional source information. Replace `C` by conditional expectation onto `G`. The same theorem applies.

If the lifted observation preserves `I_X^{eff}`, equation (7) forces `e` to be `G`-measurable. Therefore

\[
\sigma(Y,e)\subseteq G.
\tag{17}
\]

On the other hand, for `G=sigma(Y,e)`, the efficient score is measurable by construction, so (7) gives exact first-order preservation. This proves (8) in the lattice of observation sigma-fields containing `sigma(Y)`.

The result is deliberately target-relative. A different target parameter has a different efficient score and can require a different minimal lift. For a vector target the corresponding object is the sigma-field generated by the efficient-score vector, subject to the usual matrix/operator version of the same projection argument.

## Matched control: raw target score preserved, all nuisance-robust information lost

A two-dimensional Gaussian model shows why AF-141 alone is insufficient once nuisance is present. Let

\[
X=(X_1,X_2)\sim
N\!\left(
\theta\begin{pmatrix}1\\0\end{pmatrix}
+
\eta\begin{pmatrix}1\\1\end{pmatrix},
I_2
\right),
\tag{18}
\]

where `theta` is the target and `eta` is nuisance. At `(theta,eta)=(0,0)`,

\[
 s=X_1,
 \qquad
 \lambda=X_1+X_2.
\tag{19}
\]

The full efficient score is

\[
 e
 =X_1-\frac{\langle X_1,X_1+X_2\rangle}{\|X_1+X_2\|^2}(X_1+X_2)
 =\frac12(X_1-X_2),
\tag{20}
\]

so

\[
 I_X^{\rm eff}=\|e\|^2=\frac12.
\tag{21}
\]

Now compress to

\[
Y=X_1.
\tag{22}
\]

The raw target score is retained perfectly:

\[
Cs=\mathbb E[X_1\mid X_1]=X_1=s,
\tag{23}
\]

so if the nuisance were known, the target Fisher information would suffer no loss at all. But the compressed nuisance score is

\[
C\lambda
=
\mathbb E[X_1+X_2\mid X_1]
=X_1,
\tag{24}
\]

which coincides with the compressed target score. Thus

\[
M=\operatorname{span}\{X_1\},
\qquad
 e_Y=0,
\qquad
 I_Y^{\rm eff}=0.
\tag{25}
\]

The two terms of (5) are both visible:

\[
Ce=\frac12X_1,
\qquad
\|e\|^2-\|Ce\|^2
=\frac12-\frac14
=\frac14,
\tag{26}
\]

and

\[
\|\Pi_MCe\|^2=\frac14.
\tag{27}
\]

Half of the original efficient information is lost because part of the efficient score is erased; the other half is lost because the surviving component becomes entirely nuisance-like. Globally the output law is `Y~N(theta+eta,1)`, so this local collapse has an exact identifiability interpretation in the control as well.

This matched control isolates the new audit point: **preserving the raw target score or its ordinary Fisher information is not enough. A compression must preserve the target/nuisance separation encoded by the efficient score.**

## Prior art and novelty assessment

The statistical ingredients are classical, and no theorem-level novelty is claimed.

- Janet M. Begun, W. J. Hall, Wei-Min Huang, and Jon A. Wellner, **“Information and Asymptotic Efficiency in Parametric-Nonparametric Models,”** *The Annals of Statistics* 11(2), 432–452 (1983). DOI `10.1214/aos/1176346151`. Role: foundational semiparametric information/efficiency theory and the nuisance-tangent projection viewpoint.
- Peter J. Bickel, Chris A. J. Klaassen, Ya'acov Ritov, and Jon A. Wellner, ***Efficient and Adaptive Estimation for Semiparametric Models***, Johns Hopkins University Press (1993; Springer reprint 1998). Role: standard tangent-space and efficient-score framework for parameters of interest in the presence of infinite-dimensional nuisance.
- A. W. van der Vaart, ***Asymptotic Statistics***, Cambridge University Press (1998), Chapter 25. Role: standard modern source for tangent spaces, efficient scores/influence functions, information bounds, and regular semiparametric estimation.
- Abram Kagan and C. Radhakrishna Rao, **“Some properties and applications of the efficient Fisher score,”** *Journal of Statistical Planning and Inference* 116(2), 343–352 (2003). DOI `10.1016/S0378-3758(02)00351-8`. Role: direct prior art for monotonicity properties of efficient Fisher information in the presence of nuisance parameters.
- Rachel M. Fewster and Peter E. Jupp, **“Information on parameters of interest decreases under transformations,”** *Journal of Multivariate Analysis* 120, 34–39 (2013). DOI `10.1016/j.jmva.2013.05.010`. Role: direct prior art that information for parameters of interest decreases under transformations, explicitly building on efficient-score monotonicity with nuisance.

AF-141 already contains the no-nuisance score-conditioning identity and exact score-measurability equality criterion. AF-533 contains the finite-dimensional Gaussian Schur-complement/precision projection, and AF-534 contains the infinite-dimensional Gaussian nuisance-closure boundary. AF-535 does not claim a new semiparametric information theorem. Its line-local contribution is the exact **two-mechanism fidelity decomposition** (5), the corresponding efficient-score equality/minimal-lift criterion, and the explicit control showing that perfect preservation of the raw target score can coexist with total destruction of nuisance-robust target information.

## Boundary conditions and falsification tests

1. **This is first-order/local information.** Equality of efficient Fisher information at a baseline does not imply global Blackwell sufficiency, global identifiability, or recovery of the full parameterized law. AF-012, AF-013, and AF-126 address stronger experiment-level notions.

2. **The pushed nuisance space matters.** Equation (4) assumes that the downstream nuisance tangent space is exactly `closure(C Lambda)`. If the reduced model introduces additional nuisance directions not generated by pushing forward the source nuisance paths, the downstream efficient information can only be smaller and the formula must use the actual larger nuisance tangent space.

3. **The channel must be parameter-independent.** If the observation mechanism depends on the target or nuisance parameter, its own score terms enter and conditional expectation alone is not the correct tangent map.

4. **Zero efficient information is not global non-identifiability.** If `s in closure(Lambda)`, then `e=0` and no downstream parameter-independent compression can create positive first-order nuisance-robust Fisher information. Irregular or slower-rate identification can nevertheless remain, exactly as AF-534 separates algebraic identifiability from stable Gaussian fidelity.

5. **The minimal lift is mathematical, not automatically admissible.** `e` can depend on the baseline law, nuisance model, unknown parameters, or choices not intrinsic to the source problem. Adjoining it is a lower-bound witness for what must be retained, not permission to import it into an arithmetic construction.

6. **Orthogonality is representation-dependent.** The tangent Hilbert structure comes from the declared statistical experiment. A different observation law or nuisance class changes `Lambda`, `e`, and the fidelity boundary.

7. **Vector targets require the operator/matrix version.** The scalar statement avoids conflating Loewner-order information preservation with preservation of individual target directions. Directionwise application is valid, but a canonical multivariate minimal lift should be stated with the full efficient-score vector.

A decisive falsification of the finding would be a regular parameter-independent pushforward satisfying (3) for which the induced efficient score is not `(I-Pi_M)Ce`, or a full-information equality case in which `e` is not measurable from the output. Both would contradict the Hilbert projection identities above.

## Consequence for the current frontier

AF-533 and AF-534 identified nuisance quotient geometry as the correct carrier in Gaussian channels. AF-535 removes the Gaussian restriction at the local regular-experiment level and exposes an additional failure mode that is easy to miss: **compression does not merely shorten the transverse carrier; it can re-entangle the surviving carrier with nuisance.**

For Arithmetic Fidelity this gives a sharper transformation audit. A proposed compression must be tested not only for how much of the discriminator survives as an observable, but also for whether the surviving component remains transverse to the transformed control/nuisance family. In the statistical tangent category, the exact object that must survive is the efficient score itself. If it does not, the lost first-order information splits canonically into direct erasure and nuisance recontamination, and the smallest unrestricted first-order repair is to retain that efficient score alongside the compressed observation.