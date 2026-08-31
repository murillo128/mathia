# AF-016 — Base-model automorphism invariance is not first-order fidelity

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-IDENTITY`, `NEGATIVE/OBSTRUCTION`

## Claim

Let `M` be a countable first-order structure in a countable language and let

\[
R\subseteq M^n
\]

be a candidate structural discriminator.

There are two distinct questions:

1. is `R` invariant under every automorphism of the **particular base structure** `M`?;
2. is `R` parameter-free first-order definable from the retained language of `M`?

The second always implies the first, but the converse fails in general. Indeed, there are countable rigid structures whose automorphism group is trivial, so every relation on the underlying set is invariant, while only countably many relations are parameter-free first-order definable.

The classical Svenonius definability theorem identifies the missing closure. In a countable setting, non-definability of a relation from a retained sublanguage can be witnessed after passing to a suitable elementary extension or elementarily equivalent model by a permutation preserving the retained structure while failing to preserve the target relation. Thus a base-model automorphism test is only a **necessary** fidelity test for first-order admissibility in general; completeness requires the model-theoretic enlargement built into the Svenonius criterion.

There is, however, an important regime in which the simple automorphism test becomes complete. If `M` is countable and `omega`-categorical, then for every finite arity `n`, a relation `R subseteq M^n` is parameter-free first-order definable if and only if it is invariant under `Aut(M)`. By the Engeler--Ryll-Nardzewski--Svenonius characterization, `Aut(M)` is then oligomorphic, so it has only finitely many orbits on each `M^n`; those orbits are first-order definable, and every invariant relation is a finite union of them.

Therefore **breaking all visible symmetries of one representation is not, by itself, evidence that a discriminator has become intrinsically recoverable**. A symmetry obstruction is decisive in the negative direction, but its disappearance is positive evidence only in a category with an independent completeness theorem connecting admissible observables to those symmetries.

## Derivation

### Definability always implies automorphism invariance

Suppose `R` is defined without parameters by a formula

\[
\varphi(x_1,\ldots,x_n)
\]

in the language of `M`. Every automorphism `sigma in Aut(M)` preserves truth of first-order formulas, hence

\[
M\models\varphi(a)
\iff
M\models\varphi(\sigma a).
\]

So

\[
\sigma(R)=R
\qquad\text{for all }\sigma\in\operatorname{Aut}(M).
\]

This is the standard easy direction behind symmetry-based obstruction arguments: one automorphism of the retained structure that changes `R` proves that `R` cannot be parameter-free definable from that structure.

### Rigid structures show that the converse can fail maximally

Take

\[
M=(\mathbb N,<).
\]

Every order automorphism of `M` is the identity. The least element `0` must be fixed; then the unique immediate successor of `0` must be fixed; inductively every natural number is fixed. Hence

\[
\operatorname{Aut}(\mathbb N,<)=\{\mathrm{id}\}.
\]

Consequently **every** subset

\[
A\subseteq\mathbb N
\]

is invariant under `Aut(M)`.

But a countable first-order language has only countably many parameter-free formulas in one free variable. Therefore it defines at most countably many unary subsets of `N`, whereas

\[
|\mathcal P(\mathbb N)|=2^{\aleph_0}.
\]

So there exist continuum many `Aut(M)`-invariant unary relations that are not parameter-free first-order definable in `(N,<)`.

The gap is therefore not a small technical pathology. The base automorphism quotient can be completely discrete -- every point already has its own orbit -- while the chosen intrinsic observable language still fails to express almost all possible markings.

The same cardinality argument survives if one permits finitely many parameters: a countable structure has only countably many finite parameter tuples and formulas, hence still only countably many finitely-parameter-definable subsets. Parameter conventions must nevertheless be declared explicitly because allowing arbitrary named parameters changes the symmetry group and the intended notion of intrinsic structure.

### Svenonius supplies the correct completeness test for first-order admissibility

Svenonius' theorem addresses precisely why the base-model converse fails. In modern formulations, let `M=<A,Sigma>` be countable, let `Sigma'` be the retained sublanguage, and let `R` be an additional relation on `A`. If `R` is not first-order definable from `Sigma'`, then this failure can be witnessed in a suitable elementary extension or elementarily equivalent realization by a permutation that preserves the interpretations of the retained `Sigma'`-relations but does not preserve `R`.

Schematically,

\[
R\text{ not definable from the retained language}
\Longrightarrow
\exists M'\equiv M,\ \exists\pi:
\begin{cases}
\pi\text{ preserves the retained structure},\\
\pi\text{ does not preserve }R.
\end{cases}
\]

The exact classical formulations vary in whether the witness is presented as an elementary extension or an elementarily equivalent structure, but the fidelity point is the same: **the symmetry test must range over the model-theoretic closure appropriate to definability, not merely over automorphisms of the original realization**.

This turns a vague warning into a category-indexed maximal-admissibility principle. If the declared intrinsic observables are first-order definable from a retained language, then the relevant no-go test is not simply the orbit partition of `Aut(M)` on the base model. One must use the stronger definability criterion supplied by elementary extensions/equivalent models.

### Why `omega`-categoricity closes the gap

For a countable `omega`-categorical structure `M`, the Engeler--Ryll-Nardzewski--Svenonius theorem says that for every `n`, `Aut(M)` has only finitely many orbits on `M^n`.

Each orbit is determined by a complete `n`-type over the empty set. In an `omega`-categorical theory there are only finitely many such types, so each realized type is isolated by a first-order formula. Hence each automorphism orbit on `M^n` is parameter-free definable.

If `R subseteq M^n` is invariant under `Aut(M)`, then `R` is a union of automorphism orbits. There are only finitely many such orbits, so `R` is a finite union of definable sets and is itself parameter-free definable. Therefore

\[
\boxed{
M\text{ countable and }\omega\text{-categorical}
\Longrightarrow
R\text{ is }0\text{-definable}
\iff
R\text{ is }\operatorname{Aut}(M)\text{-invariant}.
}
\]

This is the kind of **completeness theorem** a symmetry-based Arithmetic Fidelity argument needs before it can interpret the absence of an automorphism obstruction positively.

## Relation to the existing Arithmetic Fidelity framework

AF-003 remains exact because it starts with an explicitly declared admissible observable family `A` and forms the joint evaluation map of **all** those observables. Its maximal-admissible quotient is therefore complete by construction for that observable class.

The present finding addresses a different shortcut: replacing the actual admissible observable class by the automorphism orbits of one base structure and assuming that every orbit-invariant discriminator is thereby intrinsic. The rigid example shows that this replacement can dramatically overestimate what the declared mathematical language can observe.

AF-015 likewise remains fully valid in its negative direction. The bare multiplicative monoid of positive integers admits arbitrary prime-generator permutations. Since the ordinary prime norm changes under those automorphisms, any observable required to be invariant under the bare monoid automorphism group cannot recover that norm.

But the converse inference is invalid:

> add enough structure to kill the prime permutations, therefore the rational-prime norm is intrinsically recovered.

An enrichment may make the base structure rigid while still failing to define the desired discriminator in the admitted language. Breaking the AF-015 symmetry obstruction is thus an **escape condition**, not a positive fidelity theorem.

## Why this matters for the Beurling / arithmetic-equivalence frontier

The accepted Beurling-fidelity clue asks for category-indexed enrichments that break the free prime-label symmetry and survive an exact downstream compression. AF-016 sharpens the first half of that task.

A proposed enrichment cannot be justified merely by showing

\[
\operatorname{Aut}(E)
\]

is small enough to distinguish the ordinary prime labels or weights. One must also state what observables/morphisms are intrinsically admissible in the enriched category and prove a completeness result for them, or directly characterize their maximal observable quotient as in AF-003.

For first-order structural enrichments, Svenonius gives the appropriate exact test. In an `omega`-categorical regime the simpler base automorphism criterion is complete; outside such a regime, elementary-extension witnesses are required in general.

This does not yet separate the rational primes from Beurling or arithmetic-equivalent controls. It instead prevents a false positive when searching for the required enrichment: **symmetry breaking without definability/recoverability closure is insufficient**.

## Prior art and novelty assessment

The model theory is classical. Svenonius' 1959 theorem is a foundational automorphism/permutation characterization of first-order definability once suitable elementary extensions or equivalent models are admitted. The Engeler--Ryll-Nardzewski--Svenonius characterization of `omega`-categoricity and the equivalence between parameter-free definability and automorphism invariance in the `omega`-categorical case are standard.

The rigid-structure counterexample is elementary: `(N,<)` has trivial automorphism group, while a cardinality count separates its countably many first-order definable unary relations from its continuum many subsets.

No novelty is claimed for any of these facts. The Arithmetic Fidelity contribution is the **boundary placement** they impose on admissible-lift reasoning: base-model symmetry is a powerful one-sided obstruction, but symmetry breaking is not a recovery theorem unless the mathematical category supplies an independent completeness bridge from invariance to admissible observability.

## Boundaries and failure modes

- The result concerns first-order definability as one mathematically precise admissibility class. Other categories -- continuous, measurable, analytic, operator-algebraic, functorial, local, or computational -- require their own completeness notions.
- Parameter-free definability is the clean intrinsic convention used above. Allowing parameters changes both definability and the appropriate stabilizer group and must be modeled explicitly rather than silently.
- A rigid structure need not be `omega`-categorical; `(N,<)` is deliberately a counterexample regime in which base automorphism invariance contains almost no definability information.
- `omega`-categoricity is a sufficient exact regime for the stated base-automorphism criterion, not a claim that it is the only possible regime in which invariance implies definability for a particular relation or class.
- The Svenonius witness is model-theoretic. It does not imply that every other notion of naturality or recoverability should literally be tested with elementary extensions.
- The result does not show that any concrete Mathia RH construction is naturally first-order. Such a language/category must be independently justified before applying this theorem.
- Killing all automorphisms is not itself suspicious; it simply ceases to provide a positive completeness certificate unless the admissible observable class is separately characterized.

## Decisive audit test

When a proposed enrichment is defended by saying that it removes a symmetry obstruction:

1. specify the exact retained mathematical language or observable class;
2. use base automorphisms as a one-sided falsifier: any automorphism changing the discriminator kills exact intrinsic recovery in that class;
3. before treating the absence of such an automorphism as positive evidence, prove that invariance under the tested symmetry class is **complete** for the admitted observables;
4. for first-order definability, use the Svenonius elementary-extension criterion in general, or prove a special regime such as `omega`-categoricity where base automorphism invariance is complete;
5. only then test whether the resulting retained structure survives the downstream compression and separates the rational-prime object from matched controls.

## Consequence for the line

Promote **admissibility completeness** to a separate gate between symmetry breaking and recovery.

The resulting audit chain is

\[
\text{retained structure}
\longrightarrow
\text{symmetry obstruction}
\longrightarrow
\text{admissible-observable completeness}
\longrightarrow
\text{discriminator recovery}
\longrightarrow
\text{downstream survival}.
\]

Failure at the symmetry stage gives an immediate no-go. Passing it only removes that obstruction. Positive fidelity requires either a theorem characterizing the full admitted observable quotient or another independent reconstruction result.

For the rational-prime program, this means the next category-indexed enrichment should not merely break `Sym(P)` from AF-015. It must come with a mathematically justified observable language whose completeness can be audited, and only then can its ability to retain the ordinary prime norm against Beurling/generalized-prime controls be meaningfully tested.