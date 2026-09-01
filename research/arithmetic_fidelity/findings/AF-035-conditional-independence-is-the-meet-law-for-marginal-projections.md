# AF-035 — Conditional independence is exactly the meet law for conditional-expectation projections

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-IDENTITY`, `STRUCTURAL-CLASSIFICATION`

## Claim

Let `(\Omega,\mathcal F,\mathbb P)` be a probability space and let

\[
\mathcal C\subseteq \mathcal G\cap\mathcal H
\]

be completed sub-`\sigma`-fields, with equality of measurable objects understood modulo `\mathbb P`-null sets. Write

\[
P_{\mathcal A}f=\mathbb E[f\mid\mathcal A]
\]

for the orthogonal projection of `L^2(\Omega)` onto `L^2(\mathcal A)`.

Then the following are equivalent:

1. `\mathcal G` and `\mathcal H` are conditionally independent given `\mathcal C`;
2. every `u\in L^2(\mathcal G)` satisfies
   \[
   P_{\mathcal H}u=P_{\mathcal C}u;
   \]
3. the conditional-expectation projections obey
   \[
   \boxed{P_{\mathcal H}P_{\mathcal G}=P_{\mathcal C};}
   \]
4. equivalently, by adjoint symmetry,
   \[
   \boxed{P_{\mathcal G}P_{\mathcal H}=P_{\mathcal C}.}
   \]

Whenever these conditions hold,

\[
\boxed{L^2(\mathcal G)\cap L^2(\mathcal H)=L^2(\mathcal C),}
\]

so conditional independence over `\mathcal C` removes not only probabilistic dependence outside `\mathcal C` but also any extra common measurable information beyond `\mathcal C`.

Define the **conditional-expectation meet defect**

\[
\mathfrak D_{\mathcal G,\mathcal H\mid\mathcal C}
:=P_{\mathcal H}P_{\mathcal G}-P_{\mathcal C}.
\]

Because `\mathcal C\subseteq\mathcal G,\mathcal H`, this factors exactly as

\[
\boxed{
\mathfrak D_{\mathcal G,\mathcal H\mid\mathcal C}
=(P_{\mathcal H}-P_{\mathcal C})(P_{\mathcal G}-P_{\mathcal C}).
}
\]

Hence

\[
\boxed{
\mathfrak D_{\mathcal G,\mathcal H\mid\mathcal C}=0
\iff
\mathcal G\perp\!\!\!\perp\mathcal H\mid\mathcal C.
}
\]

The defect is generally not self-adjoint, but its adjoint is the reversed defect and its operator norm lies in `[0,1]`. In the unconditional case where `\mathcal C` is the trivial `\sigma`-field, this operator norm is exactly the Hirschfeld--Gebelein--Rényi maximal correlation between `\mathcal G` and `\mathcal H`.

Now let `X=(X_1,\ldots,X_d)` be a finite random vector and, for every `A\subseteq[d]`, set

\[
\mathcal F_A=\sigma(X_i:i\in A),
\qquad
P_A=P_{\mathcal F_A},
\]

again completed modulo null sets. Then for every pair `A,B`,

\[
\boxed{
P_A P_B=P_{A\cap B}
\iff
\mathcal F_A\perp\!\!\!\perp\mathcal F_B
\mid \mathcal F_{A\cap B}.
}
\]

Equivalently, the coordinates in `A\setminus B` and `B\setminus A` carry no residual dependence once the overlap coordinates are retained.

Most importantly, the entire Boolean meet law is rigid:

\[
\boxed{
P_A P_B=P_{A\cap B}
\quad\text{for every }A,B\subseteq[d]
\iff
X_1,\ldots,X_d\text{ are mutually independent}.
}
\]

Thus the product-space projection calculus of AF-034 is not merely one convenient setting in which coordinate conditional expectations happen to select interaction faces. **Mutual independence is exactly the condition under which the full family of raw coordinate conditional-expectation projections represents the Boolean meet operation by composition.**

For dependent inputs, selected pairs may still satisfy the meet law; those exact identities are precisely selected conditional-independence statements. What is lost in general is the global Boolean projection representation, not necessarily every useful decomposition.

## Derivation

### Conditional independence gives the projection product

A standard conditional-independence characterization says that if

\[
\mathcal G\perp\!\!\!\perp\mathcal H\mid\mathcal C,
\]

then conditioning a `\mathcal G`-measurable integrable random variable on `\mathcal H` reveals nothing beyond `\mathcal C`:

\[
\mathbb E[u\mid\mathcal H]
=
\mathbb E[u\mid\mathcal C]
\qquad
(u\in L^2(\mathcal G)).
\]

For arbitrary `f\in L^2`, take `u=P_{\mathcal G}f`. Then

\[
P_{\mathcal H}P_{\mathcal G}f
=P_{\mathcal C}P_{\mathcal G}f.
\]

Since `\mathcal C\subseteq\mathcal G`, the tower property gives

\[
P_{\mathcal C}P_{\mathcal G}=P_{\mathcal C},
\]

and therefore

\[
P_{\mathcal H}P_{\mathcal G}=P_{\mathcal C}.
\]

Conversely, if this operator identity holds and `u\in L^2(\mathcal G)`, then `P_{\mathcal G}u=u`, so

\[
P_{\mathcal H}u
=P_{\mathcal H}P_{\mathcal G}u
=P_{\mathcal C}u.
\]

Testing first on bounded `\mathcal G`-measurable indicators and extending by the monotone-class/conditional-expectation characterization recovers conditional independence. Hence the operator identity is not a weaker second-moment proxy: it is exactly the full conditional-independence statement for the two retained `\sigma`-fields.

Each `P_{\mathcal A}` is self-adjoint on `L^2`. Taking adjoints yields

\[
(P_{\mathcal H}P_{\mathcal G})^*
=P_{\mathcal G}P_{\mathcal H}
=P_{\mathcal C},
\]

so the two orders agree exactly in the conditionally independent case.

### The common-information intersection is forced

Suppose `u\in L^2(\mathcal G)\cap L^2(\mathcal H)`. Then

\[
P_{\mathcal G}u=u,
\qquad
P_{\mathcal H}u=u.
\]

Under the meet identity,

\[
u=P_{\mathcal H}P_{\mathcal G}u=P_{\mathcal C}u,
\]

so `u\in L^2(\mathcal C)`. The reverse containment is immediate from `\mathcal C\subseteq\mathcal G\cap\mathcal H`. Therefore the common `L^2` information is exactly the conditioning field.

This matters for fidelity because a proposed `\mathcal C` cannot be called the complete retained overlap merely because it is visibly shared syntactically. If `\mathcal G` and `\mathcal H` possess an additional common random variable outside `\mathcal C`, the meet law must fail.

### Exact dependence defect

Using the nesting identities

\[
P_{\mathcal H}P_{\mathcal C}=P_{\mathcal C},
\qquad
P_{\mathcal C}P_{\mathcal G}=P_{\mathcal C},
\qquad
P_{\mathcal C}^2=P_{\mathcal C},
\]

we obtain

\[
\begin{aligned}
(P_{\mathcal H}-P_{\mathcal C})(P_{\mathcal G}-P_{\mathcal C})
&=P_{\mathcal H}P_{\mathcal G}
-P_{\mathcal H}P_{\mathcal C}
-P_{\mathcal C}P_{\mathcal G}
+P_{\mathcal C}\\
&=P_{\mathcal H}P_{\mathcal G}-P_{\mathcal C}.
\end{aligned}
\]

So the failure of the expected meet is itself the cross-action between the two residual subspaces after removing the declared common information.

When `\mathcal C` is trivial, let

\[
L^2_0(\mathcal G)=\{u\in L^2(\mathcal G):\mathbb E u=0\}
\]

and similarly for `\mathcal H`. Then

\[
\|\mathfrak D\|
=
\sup_{\substack{u\in L^2_0(\mathcal G)\\\|u\|_2=1}}
\|P_{\mathcal H}u\|_2
=
\sup_{\substack{u\in L^2_0(\mathcal G),\ v\in L^2_0(\mathcal H)\\
\|u\|_2=\|v\|_2=1}}
|\mathbb E[uv]|,
\]

which is the classical maximal-correlation coefficient. Thus the same operator has an exact zero set given by independence and a standard quantitative dependence interpretation away from zero.

## Coordinate meet law and product rigidity

For coordinate fields `\mathcal F_A,\mathcal F_B`, their visible overlap field `\mathcal F_{A\cap B}` is contained in both. Applying the theorem above immediately gives

\[
P_A P_B=P_{A\cap B}
\iff
\mathcal F_A\perp\!\!\!\perp\mathcal F_B
\mid\mathcal F_{A\cap B}.
\]

If `X_1,\ldots,X_d` are mutually independent, disjoint coordinate blocks are independent and remain conditionally independent after exposing their shared overlap coordinates. Hence the meet identity holds for every `A,B`.

Conversely, if it holds for every pair, then in particular for every pair of disjoint coordinate sets,

\[
P_A P_B=P_\varnothing.
\]

The two corresponding coordinate `\sigma`-fields are therefore independent. Taking, for example,

\[
A=\{1,\ldots,k-1\},
\qquad
B=\{k\}
\]

for `k=2,\ldots,d` shows inductively that each next coordinate is independent of all previous coordinates. The joint law therefore factors as the product of the marginal laws.

This proves the global rigidity statement.

## Full-support dependent control

The failure is not confined to deterministic dependence or duplicated coordinates. Let

\[
X_1,X_2\in\{-1,+1\}
\]

have joint law

\[
\mathbb P(X_1=x,X_2=y)
=\frac14(1+\rho xy),
\qquad 0<|\rho|<1.
\]

All four atoms have positive probability and both marginals are fair. Directly,

\[
\mathbb E[X_1\mid X_2]=\rho X_2,
\qquad
\mathbb E[X_2\mid X_1]=\rho X_1.
\]

With `P_1,P_2` the two coordinate projections and `P_\varnothing` expectation,

\[
P_2P_1X_1
=P_2X_1
=\rho X_2
\ne0
=P_\varnothing X_1.
\]

Therefore the Boolean meet law already fails for the two singleton coordinates. Since each centered coordinate subspace is one-dimensional, the defect norm here is exactly

\[
\|P_2P_1-P_\varnothing\|=|\rho|.
\]

The obstruction is genuine stochastic dependence, not a singular-support artifact.

## Relation to AF-030 and AF-034

AF-030 gives the category-independent linear-test rule: retained exact scalar tests carry precisely the closed linear span that they actually measure. AF-034 makes that span completely explicit under a product reference law by the orthogonal Hoeffding decomposition

\[
L^2(Q)=\bigoplus_{S\subseteq[d]}\mathcal H_S
\]

and proves that coordinate marginalization selects the downward-closed collection of interaction faces.

The present result identifies the exact boundary behind that simplicity. Under product independence,

\[
\boxed{P_A P_B=P_{A\cap B}}
\]

for the entire coordinate family, and AF-034's face selectors form an orthogonal Boolean meet calculus. Conversely, if the raw coordinate conditional-expectation projections satisfy this calculus for every pair, the source law must be product.

Therefore the next dependent-input theory cannot honestly preserve the entire AF-034 mechanism unchanged. It has three legitimate possibilities:

1. retain only the **partial meet identities** corresponding to conditional independences actually present in the dependent law;
2. return to the generic AF-030 closed-span/annihilator geometry without pretending that the span has canonical orthogonal faces; or
3. introduce a genuinely different dependent-input decomposition, typically with hierarchical or oblique projections, and audit that new projection family on its own terms.

Recent dependent-input Hoeffding/functional-ANOVA work explicitly follows the third route: the classical mutually independent decomposition does not simply carry over, and generalized summands are characterized using oblique projections under additional dependence conditions.

The reusable Arithmetic Fidelity principle is therefore

\[
\boxed{
\text{a clean projection lattice is itself retained structure, not neutral notation.}
}
\]

Before using a product-style interaction calculus after compression, one must prove the projection multiplication law in the actual source category. If the law fails, the missing interaction geometry cannot be inferred from product formulas merely because the same coordinate labels remain available.

## Prior art and novelty assessment

No novelty is claimed for conditional independence, its conditional-expectation characterization, products of conditional-expectation operators, maximal correlation, or dependent-input Hoeffding decompositions.

- A. P. Dawid, **“Conditional Independence in Statistical Theory,”** *Journal of the Royal Statistical Society: Series B (Methodological)* 41(1), 1–15 (1979), DOI `10.1111/j.2517-6161.1979.tb01052.x`. Role: foundational systematic treatment of conditional independence as an irrelevance relation in statistical theory; supplies the classical conditional-expectation semantics used in the equivalence above.
- D. L. Burkholder and Y. S. Chow, **“Iterates of Conditional Expectation Operators,”** *Proceedings of the American Mathematical Society* 12(3), 490–495 (1961), DOI `10.2307/2034224`. Role: classical operator-theoretic prior art showing that products and iterates of nonnested conditional-expectation projections are substantive objects rather than automatically reducible by the tower property.
- A. Rényi, **“On Measures of Dependence,”** *Acta Mathematica Academiae Scientiarum Hungaricae* 10(3–4), 441–451 (1959), DOI `10.1007/BF02024507`. Role: classical maximal-correlation/dependence framework based on conditional means; anchors the unconditional operator-norm interpretation of the meet defect.
- Matija Vidmar, **“Arithmetic of (independent) sigma-fields on probability spaces,”** *VMSTA* 6(3), 269–284 (2019), DOI `10.15559/19-VMSTA135`. Role: direct modern study of intersection, generated `\sigma`-fields, complementation, and independence for complete `\sigma`-fields; prevents treating the lattice language itself as new.
- Marouane Il Idrissi, Nicolas Bousquet, Fabrice Gamboa, Bertrand Iooss, and Jean-Michel Loubes, **“Hoeffding decomposition of black-box models with dependent inputs,”** arXiv:`2310.06567` (2023). Role: close current prior art for the exact boundary exposed by AF-034: classical Hoeffding decomposition is tied to mutually independent inputs, while dependent-input generalization requires a different framework and uses oblique projections under explicit dependence assumptions.

The Arithmetic Fidelity contribution is the **boundary theorem organization** relative to AF-034: the whole raw coordinate projection family realizes Boolean meet by operator composition if and only if the source law is product. This converts AF-034's warning that product structure is essential into an exact iff test, identifies each surviving pairwise meet identity with a conditional-independence statement, and supplies an operator defect whose zero set is exactly the desired local lattice relation. It is a structural classification assembled from classical probability/operator facts, not a claim to a new theorem of probability theory.

## Boundaries and failure modes

- **All equalities are modulo null sets.** Completed `\sigma`-fields are the correct objects for the `L^2` projection statement.
- **The conditioning field must be retained by both sides.** The theorem assumes `\mathcal C\subseteq\mathcal G\cap\mathcal H`; arbitrary third `\sigma`-fields require the usual formulation with the relevant joins.
- **Pairwise selected meet identities are not global product structure.** A dependent system can have many exact conditional independences. Product rigidity requires the full coordinate family, or another generating collection strong enough to imply mutual independence.
- **Failure of the meet law does not rule out dependent ANOVA.** It rules out the unchanged raw orthogonal face-selector calculus. Oblique, hierarchical, or model-specific decompositions may still be exact and must be audited separately.
- **The defect norm is category-specific.** It quantifies `L^2` dependence of the two retained `\sigma`-fields; it is not automatically a total-variation, Bayes-risk, zero-error, or nonlinear reconstruction metric.
- **Coordinate meaning must be intrinsic.** As in AF-034, a nonlinear reparameterization mixing coordinates changes the coordinate `\sigma`-fields and therefore changes the meet table. An application must justify why these channels are mathematically forced.
- **No rational-prime conclusion follows.** A future arithmetic application would first need a justified family of retained substructures whose conditional-expectation or analogous projection algebra has intrinsic meaning.

## Consequences for the research line

AF-034 identified the product/orthogonal versus dependent/non-orthogonal boundary but left it qualitative. AF-035 makes that boundary exact:

\[
\boxed{
\text{global coordinate meet law}
\iff
\text{product independence}.
}
\]

This supplies a general audit for future relational lifts. When an argument depends on intersections of retained channels behaving like combinatorial faces, the multiplication table of the actual conditional-expectation projections must be checked first. Exact pairwise failures are not bookkeeping defects; they are witnesses that the purported face lattice has forgotten the source's dependence geometry.

Conversely, selected identities

\[
P_A P_B=P_{A\cap B}
\]

are useful positive structure even in a globally dependent system: they expose the precise partial meet relations that remain valid. The next non-product question is therefore sharper than “generalize Hoeffding under dependence.” It is to determine which partial conditional-independence/commuting-square geometry is intrinsic enough to support an exact fidelity calculus, and which additional oblique structure is genuinely required when that partial lattice is insufficient.