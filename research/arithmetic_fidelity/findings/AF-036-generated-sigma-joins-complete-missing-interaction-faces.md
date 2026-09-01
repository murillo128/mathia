# AF-036 — Generated sigma-field joins complete interaction faces beyond Hilbert joins

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-IDENTITY`, `STRUCTURAL-CLASSIFICATION`

## Claim

Let

\[
(X_i,\Sigma_i,q_i),\qquad i=1,\ldots,d,
\]

be probability spaces, let

\[
Q=\bigotimes_{i=1}^d q_i,
\]

and work in `L^2(Q)`. For every coordinate set `A\subseteq[d]`, write

\[
\mathcal F_A=\sigma(X_i:i\in A),
\qquad
V_A=L^2(\mathcal F_A),
\qquad
P_A f=\mathbb E[f\mid\mathcal F_A].
\]

Use the product-space Hoeffding decomposition from AF-034,

\[
L^2(Q)=\bigoplus_{S\subseteq[d]}\mathcal H_S,
\qquad
V_A=\bigoplus_{S\subseteq A}\mathcal H_S.
\]

Fix a finite nonempty family of coordinate sets

\[
\mathcal A=\{A_1,\ldots,A_m\},
\]

and define

\[
U=\bigcup_{i=1}^m A_i,
\qquad
\Delta=\bigcup_{i=1}^m 2^{A_i}.
\]

Thus `\Delta` is the downward-closed simplicial information state already seen in AF-033 and AF-034. There are now two different notions of joining the retained coordinate structures.

1. **The Hilbert-space join retains only the existing simplicial faces.** Let
   \[
   V_{\mathrm{lin}}
   =\overline{V_{A_1}+\cdots+V_{A_m}}.
   \]
   Then
   \[
   \boxed{
   V_{\mathrm{lin}}
   =\bigoplus_{S\in\Delta}\mathcal H_S.
   }
   \]
   Since the coordinate conditional-expectation projections commute under the product law, the orthogonal projector onto this closed sum is
   \[
   \boxed{
   P_{\Delta}
   =I-\prod_{i=1}^m(I-P_{A_i})
   =\sum_{\varnothing\ne J\subseteq[m]}
   (-1)^{|J|+1}P_{\cap_{j\in J}A_j}.
   }
   \]

2. **The generated sigma-field join fills the whole simplex on the covered coordinates.** The smallest sigma-field containing all retained coordinate fields is
   \[
   \bigvee_{i=1}^m\mathcal F_{A_i}
   =\mathcal F_U.
   \]
   Therefore
   \[
   \boxed{
   L^2\!\left(\bigvee_i\mathcal F_{A_i}\right)
   =V_U
   =\bigoplus_{S\subseteq U}\mathcal H_S.
   }
   \]
   In general this is strictly larger than the Hilbert join. Passing from the family of linear subspaces to the generated measurable structure creates access to mixed interaction faces that are not present in any individual `V_{A_i}`.

3. **The exact join defect is itself an orthogonal projection.** Define
   \[
   \mathfrak J_{\mathcal A}
   :=P_U-P_{\Delta}.
   \]
   Because `V_{\mathrm{lin}}\subseteq V_U`,
   \[
   \boxed{
   \mathfrak J_{\mathcal A}
   \text{ is the orthogonal projection onto }
   \mathcal I_{\mathcal A}
   :=\bigoplus_{\substack{S\subseteq U\\S\notin\Delta}}
   \mathcal H_S.
   }
   \]
   Equivalently,
   \[
   \boxed{
   \mathfrak J_{\mathcal A}
   =P_U-I+\prod_{i=1}^m(I-P_{A_i}).
   }
   \]
   The missing space `\mathcal I_A` consists exactly of interactions whose coordinate support is not contained in any one retained channel.

4. **The defect vanishes only when one retained channel already contains the whole covered coordinate set.** Assume every coordinate is nontrivial, meaning
   \[
   L^2_{0}(q_i)\ne\{0\}.
   \]
   Then every `\mathcal H_S` is nonzero, and
   \[
   \boxed{
   \mathfrak J_{\mathcal A}=0
   \iff
   \Delta=2^U
   \iff
   U\in\Delta
   \iff
   A_i=U\text{ for some }i.
   }
   \]
   Hence if no retained coordinate field already contains all coordinates appearing anywhere in the family, generated-sigma-field joining strictly increases the available `L^2` information. Whenever the defect is nonzero,
   \[
   \boxed{\|\mathfrak J_{\mathcal A}\|=1.}
   \]

5. **For two channels the defect is the missing mixed-interaction projector.** For `A,B\subseteq[d]`, AF-035 gives
   \[
   P_AP_B=P_{A\cap B}.
   \]
   Therefore
   \[
   \boxed{
   \mathfrak J_{A,B}
   =P_{A\cup B}-P_A-P_B+P_{A\cap B}.
   }
   \]
   Its range is
   \[
   \boxed{
   \bigoplus_{\substack{S\subseteq A\cup B\\S\not\subseteq A,\ S\not\subseteq B}}
   \mathcal H_S.
   }
   \]
   If all coordinates are nontrivial, this vanishes exactly when `A\subseteq B` or `B\subseteq A`. For incomparable channels, choose `i\in A\setminus B` and `j\in B\setminus A`; then `\mathcal H_{\{i,j\}}` is already a nonzero missing interaction.

6. **Finite product spaces give an exact dimension count.** If each `X_i` is finite with full-support law and `|X_i|=n_i`, then
   \[
   \dim\mathcal H_S=\prod_{i\in S}(n_i-1),
   \]
   so
   \[
   \boxed{
   \dim\mathcal I_{\mathcal A}
   =\sum_{\substack{S\subseteq U\\S\notin\Delta}}
   \prod_{i\in S}(n_i-1).
   }
   \]
   In the binary case every missing face contributes exactly one independent ambiguity direction.

7. **Pointwise multiplication repairs the join only while the upstream observables are still available.** Let
   \[
   \mathcal P_{\mathcal A}
   =\operatorname{span}
   \left\{
   \prod_{i=1}^m f_i:
   f_i\in L^\infty(\mathcal F_{A_i})
   \right\}.
   \]
   Then
   \[
   \boxed{
   \overline{\mathcal P_{\mathcal A}}^{\|\cdot\|_2}
   =V_U.
   }
   \]
   Thus the generated measurable join is a genuine multiplicative completion of the retained coordinate function spaces: products can synthesize precisely the cross-channel interaction faces absent from their linear Hilbert join.

8. **This multiplicative completion is not free after compression.** If the destination stores only separate marginal laws, separate expectations, or another channel-wise linear compression, one cannot infer mixed products merely because the corresponding upstream functions generate a larger algebra or sigma-field. AF-030 proves that generated-algebra density cannot replace density of the actually retained linear test span; AF-031 proves that complete separate marginals can still forget their coupling. Therefore
   \[
   \boxed{
   \text{upstream generated join}
   \ne
   \text{downstream closure of already-compressed channel values}.
   }
   \]
   Any proposed recovery that invokes products, generated sigma-fields, or algebraic closure **after** the separate-channel compression must first prove that those joint observables themselves factor through the destination.

The reusable Arithmetic Fidelity conclusion is

\[
\boxed{
\text{linear joining preserves the retained simplicial faces; measurable/algebraic joining can create the missing cross-faces.}
}
\]

This is an exact example of category-dependent fidelity. The same named upstream objects can have different joins depending on whether the destination category permits only linear superposition or still retains pointwise multiplication/measurable generation.

## Hilbert join and inclusion-exclusion

AF-034 gives

\[
V_{A_i}=\bigoplus_{S\subseteq A_i}\mathcal H_S.
\]

Because the Hoeffding interaction spaces are mutually orthogonal, the closed linear span of the `V_{A_i}` is simply the orthogonal sum over every face appearing in at least one simplex `2^{A_i}`:

\[
\overline{V_{A_1}+\cdots+V_{A_m}}
=\bigoplus_{S\in\cup_i2^{A_i}}\mathcal H_S
=\bigoplus_{S\in\Delta}\mathcal H_S.
\]

The coordinate projections are simultaneously diagonal in this decomposition. On `\mathcal H_S`,

\[
P_{A_i}|_{\mathcal H_S}
=\begin{cases}
I,&S\subseteq A_i,\\
0,&S\not\subseteq A_i.
\end{cases}
\]

Hence

\[
I-\prod_i(I-P_{A_i})
\]

acts as `1` exactly when `S` is contained in at least one `A_i`, and as `0` otherwise. It is therefore the projector `P_\Delta` onto the Hilbert join.

Since AF-035 gives the meet law

\[
\prod_{j\in J}P_{A_j}=P_{\cap_{j\in J}A_j}
\]

under the product measure, ordinary inclusion-exclusion expands the same projector as

\[
P_\Delta
=\sum_{\varnothing\ne J\subseteq[m]}
(-1)^{|J|+1}P_{\cap_{j\in J}A_j}.
\]

Thus the projection lattice generated by the retained coordinate subspaces represents the **simplicial union** of the individual faces, not the full simplex on their vertex union.

## Generated sigma-field join and the interaction gap

Every coordinate variable indexed by `U` is measurable with respect to at least one `\mathcal F_{A_i}`, so

\[
\mathcal F_U\subseteq\bigvee_i\mathcal F_{A_i}.
\]

The reverse containment is immediate because every `A_i\subseteq U`. Hence

\[
\bigvee_i\mathcal F_{A_i}=\mathcal F_U.
\]

Applying AF-034 to `U` gives

\[
V_U
=\bigoplus_{S\subseteq U}\mathcal H_S.
\]

Subtracting the orthogonal projector onto the already-retained face union leaves exactly

\[
\mathfrak J_{\mathcal A}
=P_U-P_\Delta
\]

with range

\[
\mathcal I_{\mathcal A}
=V_U\ominus V_{\mathrm{lin}}
=\bigoplus_{S\in2^U\setminus\Delta}\mathcal H_S.
\]

Because the two projections are nested and commute, their difference is itself an orthogonal projection. This proves idempotence, self-adjointness, the exact range description, and the `0/1` operator-norm dichotomy.

Under coordinate nontriviality, `\mathcal H_U\ne0`. If no `A_i` equals `U`, then `U\notin\Delta`, so `\mathcal H_U\subseteq\mathcal I_A` and the defect is nonzero. Conversely, if some `A_i=U`, then `2^U\subseteq\Delta`, hence equality holds and the defect vanishes.

For two sets, the Hilbert-join projector is the standard commuting-projection formula

\[
P_A\vee_H P_B=P_A+P_B-P_AP_B
=P_A+P_B-P_{A\cap B},
\]

while the generated coordinate field has projector `P_{A\cup B}`. Their difference is precisely the displayed `\mathfrak J_{A,B}`.

## Minimal two-coordinate control

Take two independent nontrivial coordinates `X_1,X_2`, with

\[
A=\{1\},\qquad B=\{2\}.
\]

Then

\[
V_A+V_B
=\mathcal H_\varnothing\oplus\mathcal H_{\{1\}}\oplus\mathcal H_{\{2\}},
\]

whereas

\[
V_{\{1,2\}}
=\mathcal H_\varnothing
\oplus\mathcal H_{\{1\}}
\oplus\mathcal H_{\{2\}}
\oplus\mathcal H_{\{1,2\}}.
\]

Choose bounded centered nonzero functions `u(X_1)` and `v(X_2)`. Their product

\[
u(X_1)v(X_2)\in\mathcal H_{\{1,2\}}
\]

is orthogonal to both single-coordinate spaces, yet is measurable with respect to the generated sigma-field `\mathcal F_{\{1,2\}}`. Therefore

\[
\mathfrak J_{A,B}[u(X_1)v(X_2)]
=u(X_1)v(X_2).
\]

Nothing pathological is occurring: the missing information is the ordinary second-order interaction. What changes is the closure operation. Linear addition of the two channel spaces cannot manufacture a product interaction; measurable/algebraic generation can.

## Why multiplication fills the generated join

For each coordinate, bounded square-integrable functions are dense in `L^2(q_i)`, and bounded centered functions are dense in `L^2_0(q_i)`. Fix `S\subseteq U`. An elementary Hoeffding tensor in `\mathcal H_S` can be written as a product of bounded centered single-coordinate factors.

Assign each coordinate `k\in S` to one index `i(k)` with `k\in A_{i(k)}`. Grouping the factors by their assigned channel gives

\[
h_S=\prod_{i=1}^m f_i,
\qquad
f_i\in L^\infty(\mathcal F_{A_i}).
\]

Finite linear combinations of such elementary tensors are dense in every `\mathcal H_S`, and the finite orthogonal sum over `S\subseteq U` is `V_U`. Therefore the span of cross-channel products is dense in the whole generated-join space.

This proof also identifies what is being added: multiplication does not mysteriously recover information; it explicitly creates interaction tensors whose supports combine coordinates coming from different retained channels.

## Destination-category boundary

The result must not be misread as saying that lost coupling can always be recovered by multiplying whatever remains after compression.

There are three different objects:

1. the upstream function spaces `V_{A_i}` themselves;
2. the joint algebra or sigma-field they generate before measurement;
3. the destination values produced by separately compressing each channel.

The theorem above concerns the passage from (1) to (2). If the upstream functions remain available, pointwise products genuinely are additional observable functions and can fill the missing interaction faces.

AF-030 shows why the same move is invalid for a linear-test destination. Knowing the values of `\int f\,d\mu` for retained `f` does not provide `\int fg\,d\mu` merely because `fg` lies in the algebra generated by the functions. AF-031 gives the measure-level version: even complete knowledge of every separate marginal can leave the joint coupling undetermined.

Consequently a compression pipeline cannot write

\[
\text{separate channels}
\longrightarrow
\text{generated algebra/sigma-field}
\]

as though the second object were a deterministic post-processing of the first. That arrow is valid only if the destination retains enough joint data to evaluate the newly generated observables. Otherwise the operation silently reintroduces structure erased by the compression.

This is the precise Arithmetic Fidelity warning supplied by the join defect.

## Prior art and novelty assessment

No novelty is claimed for generated sigma-fields, conditional expectation, Hilbert-space projection lattices, commuting-projection formulas, tensor-product ANOVA/Hoeffding decompositions, or the fact that products of measurable functions generate richer function classes.

- Matija Vidmar, **“Arithmetic of (independent) sigma-fields on probability spaces,”** *Modern Stochastics: Theory and Applications* 6(3), 269–284 (2019), DOI `10.15559/19-VMSTA135`. Role: direct prior art for treating intersection, generated sigma-field, complementation, and independence as genuine arithmetic/lattice operations on complete sigma-fields; prevents presenting the sigma-field join language itself as new.
- John B. Conway, ***A Course in Functional Analysis***, 2nd ed., Graduate Texts in Mathematics 96, Springer (1990). Role: standard Hilbert-space projection theory; for commuting orthogonal projections the meet is `PQ` and the closed-span join projector is `P+Q-PQ`, the operator identity specialized above to coordinate conditional expectations.
- Akimichi Takemura, **“Tensor Analysis of ANOVA Decomposition,”** *Journal of the American Statistical Association* 78(384), 894–900 (1983), DOI `10.1080/01621459.1983.10477037`. Role: classical tensor-product formulation of ANOVA decompositions in `L^2`, placing the interaction-face decomposition used here inside established multilinear/statistical theory.
- Wassily Hoeffding, **“A Class of Statistics with Asymptotically Normal Distribution,”** *The Annals of Mathematical Statistics* 19(3), 293–325 (1948), DOI `10.1214/aoms/1177730196`. Role: foundational Hoeffding/U-statistic decomposition background for orthogonal interaction components under product sampling.

The exact formulas are derived here by combining the established projection and product-decomposition facts already anchored in AF-034 and AF-035. The Arithmetic Fidelity contribution is the **boundary organization**: the map from retained coordinate sigma-fields to their `L^2` subspaces preserves the product-coordinate meet calculus but does not preserve generated joins; the discrepancy is an explicit orthogonal projector onto the missing simplicial interaction faces. This turns the informal warning that “relational information may live in products” into a computable category-change defect.

A targeted prior-art audit found mature theories for each ingredient, especially Vidmar's sigma-field arithmetic, standard commuting-projection lattices, and tensor ANOVA. No claim is made that the join-defect packaging is a historically new theorem. Its value here is as a reusable exact audit surface for later compression arguments.

## Boundaries and failure modes

- The clean orthogonal face classification uses a product reference law. For dependent inputs, AF-035 shows that the coordinate conditional-expectation projections need not obey the Boolean meet law, and dependent-input ANOVA may require oblique or otherwise modified projection systems.
- The sigma-field identity `\bigvee_i\mathcal F_{A_i}=\mathcal F_U` is coordinate-structural and does not itself require independence; independence is required for the displayed Hoeffding orthogonality and commuting-projection formulas.
- Coordinate nontriviality is required for the sharp criterion `\mathfrak J=0` iff some `A_i=U`. Degenerate coordinates can make nominally missing interaction spaces vanish.
- The product-density statement uses bounded representatives so the pointwise products remain in `L^2`. Arbitrary products of two `L^2` functions need not lie in `L^2`.
- `\mathfrak J` measures the gap between two closure categories for the declared coordinate family. It is not an entropy, mutual information, or approximate statistical-loss measure.
- A missing interaction face can be irrelevant to a particular target discriminator. As throughout Arithmetic Fidelity, ambient source fidelity and target-relative fidelity must not be conflated.
- The theorem does not license generated-algebra closure after a marginal, moment, spectral, or other compression. Such a post-processing is valid only if every newly invoked joint observable is determined by the actual destination data.
- For an infinite family of retained fields, additional topological/closure issues enter. The present statement is finite and exact.

## Consequence for the line

AF-033 classified marginal information states by downward-closed simplicial complexes. AF-034 identified those faces with exact Hoeffding interaction subspaces on product spaces. AF-035 then showed that product independence is exactly what makes coordinate conditional-expectation projections realize Boolean meets by composition.

The present result closes the complementary join question:

\[
\boxed{
\text{meet survives in the projection calculus, but generated join changes category and completes missing cross-channel interactions.}
}
\]

Future Arithmetic Fidelity work should therefore distinguish at least three closure operations whenever a proposed compression combines partial observables:

- **linear/Hilbert closure:** retains only the closed span of observables already present;
- **algebraic/measurable generation:** may create mixed relational observables by multiplication;
- **post-compression processing:** cannot exceed the actual destination fibers and does not inherit the richer upstream algebra automatically.

This gives a concrete stopping test for proposed “recovery by closure” mechanisms: identify which of these operations is actually available at the stage where recovery is claimed, then compute whether the target interaction lies in the corresponding retained space rather than silently upgrading from one closure category to another.