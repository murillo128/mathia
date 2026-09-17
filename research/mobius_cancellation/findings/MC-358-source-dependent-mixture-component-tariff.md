# MC-358 — Source-dependent mixtures split exactly into latent and component discrimination tariffs

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `CLASSICAL-MECHANISM` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-357` closes the fixed-component mixture loophole: when the source changes only the mixing law and the component kernel is fixed, data processing forces the latent mixing law itself to pay the source-edge divergence tariff. The remaining mixture escape identified there is that the **components themselves may move with the source**.

That escape is not free either. For a concrete latent-variable architecture, the lifted joint law gives an exact non-double-counting split between latent-law motion and source-dependent component motion.

Let `X` be the reciprocal source state, let `Theta` be a latent variable in a common measurable state space, and let `Y` be the admitted transcript. Under source state `x`, suppose the architecture factors as

\[
\Theta\sim\nu_x,
\qquad
Y\mid\Theta=\theta\sim K_x(\cdot\mid\theta),
\tag{1}
\]

where now both the mixing law `nu_x` and the component kernel `K_x` may depend on the source. Write the lifted joint law and output marginal as

\[
Q_x(d\theta,dy)
:=\nu_x(d\theta)K_x(dy\mid\theta),
\qquad
P_x:=Q_x\circ\pi_Y^{-1}.
\tag{2}
\]

For a natural source edge `e={x,x'}`, retain the half-Jeffreys output cost

\[
b_e(Y)
:=\frac12\left(D(P_x\|P_{x'})+D(P_{x'}\|P_x)\right),
\tag{3}
\]

and define

\[
b_e(\Theta)
:=\frac12\left(D(\nu_x\|\nu_{x'})+D(\nu_{x'}\|\nu_x)\right).
\tag{4}
\]

The conditional component tariff is

\[
\begin{aligned}
c_e(K)
:=\frac12\Bigg[&
\int D\!\left(K_x(\cdot\mid\theta)\|K_{x'}(\cdot\mid\theta)\right)\,\nu_x(d\theta)\\
&+\int D\!\left(K_{x'}(\cdot\mid\theta)\|K_x(\cdot\mid\theta)\right)\,\nu_{x'}(d\theta)
\Bigg].
\end{aligned}
\tag{5}
\]

Whenever the directed divergences are finite, the relative-entropy chain rule gives the exact lifted decompositions

\[
D(Q_x\|Q_{x'})
=
D(\nu_x\|\nu_{x'})
+
\int D(K_x(\cdot\mid\theta)\|K_{x'}(\cdot\mid\theta))\,\nu_x(d\theta),
\tag{6}
\]

and the reverse identity with `x,x'` exchanged. If an absolute-continuity requirement fails, interpret the corresponding divergence as `+infinity`; the upper bounds below then hold in the extended sense.

Marginalization `(Theta,Y) -> Y` is a Markov kernel, so relative entropy contracts. Therefore

\[
\boxed{
 b_e(Y)
 \le
 \frac12\left(D(Q_x\|Q_{x'})+D(Q_{x'}\|Q_x)\right)
 =
 b_e(\Theta)+c_e(K).
}
\tag{7}
\]

The right side is the exact half-Jeffreys divergence of the **actual lifted architecture**. Thus latent-law discrimination and conditional component discrimination are additive at the joint level rather than being combined by a loose triangle inequality.

Combining `(7)` with the source-edge lower tariff of `MC-353`, under the same bounded-energy reciprocal dephasing hypotheses

\[
\mathcal E(W)\le C,
\qquad
\delta(W)\le1-\eta,
\qquad C<\infty,
\quad \eta>0,
\tag{8}
\]

gives

\[
\boxed{
\mathbf E_e\bigl[b_e(\Theta)+c_e(K)\bigr]
\ge
\frac{\eta^2}{C}-o(1).
}
\tag{9}
\]

Hence a source-dependent mixture architecture cannot evade the reciprocal endpoint tariff by shifting source dependence from weights into components. It may choose **where** to pay, but if both the adjacent latent-law divergence and adjacent conditional-component divergence vanish on average, fixed nontrivial bounded-energy dephasing is impossible.

No estimate for `M(x)` follows. The theorem is a finite reciprocal-endpoint admission result. Its value is that the mixture frontier left open by `MC-357` now has an exact accounting identity: any surviving architecture must place nonvanishing source discrimination either in the latent law, in the conditional component family, or in an additional source path not represented by `(1)`.

## 1. The KL chain rule gives the split without double counting

Assume first that `nu_x << nu_x'` and that the conditional law `K_x(.|theta)` is absolutely continuous with respect to `K_x'(.|theta)` for `nu_x`-almost every `theta`. On standard Borel spaces, the Radon-Nikodym derivative of the lifted law factors as

\[
\frac{dQ_x}{dQ_{x'}}(\theta,y)
=
\frac{d\nu_x}{d\nu_{x'}}(\theta)
\frac{dK_x(\cdot\mid\theta)}{dK_{x'}(\cdot\mid\theta)}(y)
\tag{10}
\]

for compatible conditional versions. Taking the `Q_x` expectation of the logarithm gives `(6)`. The same argument in the reverse direction gives

\[
\frac12 J(Q_x,Q_{x'})
=
b_e(\Theta)+c_e(K),
\tag{11}
\]

where `J` is Jeffreys divergence.

Equation `(11)` is the key architectural statement. The component term is conditional on the **same realized latent coordinate**, so information already carried by the change in `nu_x` is not charged again as component motion. Conversely, source dependence that remains after conditioning on `Theta` is visible precisely in `c_e(K)`.

Now project away `Theta`. Data processing gives

\[
D(P_x\|P_{x'})\le D(Q_x\|Q_{x'}),
\tag{12}
\]

and likewise in reverse, proving `(7)`.

This is only an upper resource bound: a large lifted tariff need not survive marginalization to `Y`. But the direction is exactly what the admission problem needs. Since `MC-353` independently forces a positive output tariff, every architecture realizing that output must have at least as much lifted latent-plus-component tariff.

## 2. Finite categorical mixtures expose the two resources explicitly

Let the latent variable be a finite architectural label `J in {1,...,m}`. Under source states `x,x'`, write

\[
w=(w_1,\ldots,w_m),
\qquad
v=(v_1,\ldots,v_m),
\tag{13}
\]

and source-dependent component laws

\[
K_{x,j},\qquad K_{x',j}.
\tag{14}
\]

When the two weight vectors have common positive support and the paired component divergences are finite, `(7)` becomes

\[
\boxed{
\begin{aligned}
b_e(Y)
\le &\;\frac12\sum_{j=1}^m
(w_j-v_j)\log\frac{w_j}{v_j}\\
&+\frac12\sum_{j=1}^m
\left[
 w_jD(K_{x,j}\|K_{x',j})
 +v_jD(K_{x',j}\|K_{x,j})
\right].
\end{aligned}
}
\tag{15}
\]

The first line is exactly the latent categorical half-Jeffreys cost from `MC-357`; the second is the conditional component tariff.

Two limiting cases recover the expected boundaries:

- if `K_{x,j}=K_{x',j}` for every `j`, the component term vanishes and `(15)` reduces to the fixed-component theorem `MC-357`;
- if `w=v` is source-independent, all source discrimination must come from component motion:

\[
\boxed{
 b_e(Y)
 \le
 \frac12\sum_j w_j
 \left[D(K_{x,j}\|K_{x',j})+D(K_{x',j}\|K_{x,j})\right].
}
\tag{16}
\]

Thus changing components instead of weights is a genuine architectural alternative, but it is not an unpriced one.

## 3. Exact dephasing forces singularity somewhere on every shared latent fiber

The exact reciprocal endpoint requires neighboring complete-transcript laws to be mutually singular. If

\[
P_x\perp P_{x'},
\tag{17}
\]

then total-variation contraction under marginalization implies

\[
Q_x\perp Q_{x'}.
\tag{18}
\]

For the finite categorical architecture above, the label coordinates are disjoint fibers. Therefore `(18)` has a precise consequence: for every label `j` with

\[
w_j>0,
\qquad
v_j>0,
\tag{19}
\]

the paired component laws must themselves be singular,

\[
\boxed{
K_{x,j}\perp K_{x',j}.
}
\tag{20}
\]

Indeed, if `A subset {1,...,m} x Y` separates the two joint laws and `A_j={y:(j,y) in A}`, then `w_j>0` forces `K_{x,j}(A_j)=1`, while `v_j>0` forces `K_{x',j}(A_j)=0`.

This sharpens the support statement from `MC-357`. With fixed components, exact output singularity forces the **weight supports** to be disjoint. With moving components, shared positive-weight labels are allowed, but every such shared fiber must itself become singular. An all-interior finite mixture whose corresponding source-dependent components remain mutually absolutely continuous cannot realize the exact endpoint.

The conclusion is architectural, not a claim that the marginal mixture components are canonically identifiable from `Y` alone.

## 4. The split is meaningful only for a real common latent architecture

There is an important invariance boundary. Equations `(6)`--`(16)` price a **specified generative factorization** with one common latent coordinate system across source states. A common source-independent measurable relabeling of `Theta` changes no divergence and is harmless.

A source-dependent relabeling is different: it changes the coupling of component fibers across the two source states and can move apparent cost between the latent and conditional terms. Likewise, an arbitrary post-hoc mixture decomposition of the same marginal `P_x` is not evidence that the system actually paid the corresponding tariff.

Therefore the invariant object is the lifted half-Jeffreys cost

\[
\frac12J(Q_x,Q_{x'}),
\tag{21}
\]

of the admitted architecture. The decomposition `b_e(Theta)+c_e(K)` is exact relative to that architecture. For finite mixtures, the pairing `j <-> j` in `(15)` must come from the actual latent label semantics, not from an after-the-fact permutation chosen to make the bound small or large.

This also identifies the next falsification target. To obstruct a concrete Möbius endpoint architecture, it is not enough to assert that its visible output “looks like a mixture.” One must expose a genuine source-indexed latent/component factorization and prove an arithmetic upper bound on the corresponding joint tariff or on both terms of `(9)`.

## Prior art and novelty boundary

No novelty is claimed for the relative-entropy chain rule, KL data processing, conditional relative entropy, or latent-variable lifting. Cover and Thomas, *Elements of Information Theory*, 2nd ed. (Wiley, 2006), §2.5, states the chain rule

\[
D(P_{XY}\|Q_{XY})
=
D(P_X\|Q_X)
+D(P_{Y|X}\|Q_{Y|X}\mid P_X),
\]

which is exactly the classical identity underlying `(6)`. The same chapter derives relative-entropy contraction under a common Markov transition.

Polyanskiy and Wu, *Strong Data-Processing Inequalities for Channels and Bayesian Networks*, in *Convexity and Concentration* (2017), arXiv:1508.06025, surveys data-processing and its channel/network strengthenings. This is the general information-theoretic background for `(12)`; no strong contraction coefficient is needed here.

Nielsen and Nock, *On w-mixtures: Finite convex combinations of prescribed component distributions*, arXiv:1708.00568, studies the information geometry of finite mixtures with a **fixed prescribed component bank**. That is adjacent to the fixed-component regime closed in `MC-357`; it does not make source-dependent component motion free and does not replace the joint-law chain-rule accounting above.

A targeted prior-art audit on 17 September 2026 found the decomposition and contraction mechanisms to be classical. No novelty is claimed for `(6)`, `(7)`, `(15)`, or the general fact that a latent-variable joint distribution upper-bounds the divergence of its marginal. The durable Mathia-specific delta is their composition with the independently derived reciprocal source-edge lower tariff of `MC-353`, together with the exact categorical singularity boundary `(20)`. This closes the generic “source-dependent components” escape left explicit in `MC-357` at the level of architecture admission.

## Boundaries and falsification tests

- **The latent factorization must be architectural.** A convenient mathematical decomposition of `P_x` chosen after observing the marginal is not a source resource theorem.
- **The same latent coordinate must have the same architectural meaning across source states.** Source-dependent relabeling can move divergence between the two terms and must itself be represented as source dependence rather than treated as gauge.
- **Extended-valued divergences are allowed.** A support change in `nu_x` or a singular conditional component gives infinite directed KL; the theorem then identifies a large tariff rather than producing a finite quantitative bound.
- **A large lifted tariff is not sufficient for dephasing.** Marginalization can discard most latent/component discrimination. The result is a necessary-resource statement only.
- **Exact singularity is stronger than large finite KL.** Equation `(20)` applies to the exact endpoint; approximate dephasing requires quantitative near-singularity or divergence control rather than literal disjoint support.
- **Hidden side channels must be included.** If an adaptive branch, random seed, component selector, metadata field, or additional observation depends on the source outside `(1)`, enlarge the lifted transcript before applying the tariff.
- **Component pairing cannot be optimized post hoc.** In `(15)`, `K_{x,j}` and `K_{x',j}` are paired because the architecture uses the same latent label `j`. An unlabeled mixture representation needs a separately justified coupling or quotient formulation.
- **No arithmetic upper bound has been proved.** The live Möbius task remains to show that an actual reciprocal endpoint construction has small adjacent lifted divergence, or to exhibit a mathematically forced singular/high-divergence channel that survives the arithmetic constraints.

## Research consequence

The mixture loophole is now structurally exhausted at the generic latent-variable level. Fixed components are priced by latent-law motion (`MC-357`); moving components are priced by the exact joint chain rule here. A future mixture-based endpoint mechanism must therefore do one of three concrete things: exhibit nonvanishing adjacent latent-law divergence, exhibit nonvanishing/singular adjacent component motion, or reveal an additional source-bearing path omitted from the proposed latent graph.

The next productive step is no longer to classify ever broader statistical mixture families. It is to take a **specific Möbius-derived endpoint architecture** and prove a source-edge upper theorem for its actual lifted joint law. Without that arithmetic upper bridge, the information-theoretic tariff remains an admission constraint rather than a bound on `M(x)`.