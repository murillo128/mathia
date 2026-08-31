# AF-011 — Zero-error stochastic fidelity is support confusability

**Status:** `LITERATURE+DERIVED`, `CLASSICAL-IDENTITY`, `NEGATIVE/OBSTRUCTION`

## Claim

Let `X` and `Y` be finite sets, let

\[
K(y\mid x)\ge 0,
\qquad
\sum_{y\in Y}K(y\mid x)=1,
\]

be a stochastic compression channel, and let

\[
d:X\to D
\]

be a discriminator. Define the **discriminator-confusability graph**

\[
H(K,d)
\]

on vertex set `X` by joining distinct `x,x'` when

\[
d(x)\ne d(x')
\]

and their output supports overlap:

\[
\exists y\in Y:
K(y\mid x)>0,
\quad
K(y\mid x')>0.
\]

Then:

1. `d` is recoverable from one channel output with **zero error for every upstream state and every positive-probability channel outcome** if and only if `H(K,d)` has no edges. Equivalently, for every `y`, the set
   \[
   \{x:K(y\mid x)>0\}
   \]
   is `d`-monochromatic.
2. If `L(z\mid y)` is any downstream stochastic garbling, then
   \[
   H(K,d)\subseteq H(L\circ K,d).
   \]
   Thus a zero-error discriminator conflict created by `K` cannot be repaired by later processing that receives only the channel output.
3. If a noiseless deterministic mark
   \[
   M:X\to A
   \]
   is appended and the decoder observes `(Y,M(X))`, then zero-error recovery is possible if and only if `M` is a proper coloring of `H(K,d)`. Consequently, among arbitrary noiseless marks, the minimum alphabet size is exactly
   \[
   \chi(H(K,d)).
   \]
4. If admissible marks are restricted to a fixed observable library
   \[
   \mathcal F=\{f_1,\ldots,f_n\},
   \]
   then a subset `J` restores zero-error fidelity exactly when it separates every edge of `H(K,d)`. Writing
   \[
   \Delta(\{x,x'\})
   =\{i:f_i(x)\ne f_i(x')\},
   \]
   recovery is equivalent to
   \[
   J\cap\Delta(c)\ne\varnothing
   \qquad
   \text{for every }c\in E(H(K,d)).
   \]
   Hence the finite admissible-lift problem again reduces to the decision-relative hitting-set/reduct construction of AF-002, now with stochastic support-overlap conflicts replacing deterministic equal-fiber conflicts.
5. Zero-error failure is not controlled by a small average Bayes or `L^2` defect. There are channels whose discriminator-confusability graph contains a fixed conflict edge for every `\varepsilon>0` while both Bayes error and AF-009's conditional-variance defect tend to zero as `\varepsilon\downarrow0`.

The mathematical content is classical zero-error information theory and characteristic/confusability graph theory. The Arithmetic Fidelity consequence is a sharp separation between **average fidelity**, which is probability-weighted, and **supportwise fidelity**, which treats any positive-probability discriminator collision as fatal. Rare collisions can therefore be negligible for AF-009 while remaining decisive for exact structural recovery.

## Derivation

### Zero-error recovery is monochromatic output support

A decoder is a map

\[
r:Y\to D.
\]

Zero-error recovery means that for every `x` and every `y` with `K(y|x)>0`,

\[
r(y)=d(x).
\]

If two states `x,x'` with different discriminator values can both emit the same `y`, then the decoder would need simultaneously

\[
r(y)=d(x)
\qquad\text{and}\qquad
r(y)=d(x'),
\]

which is impossible. Thus zero-error recovery implies that every output predecessor set is `d`-monochromatic, equivalently that `H(K,d)` has no edge.

Conversely, if every predecessor set is `d`-monochromatic, define `r(y)` to be that common discriminator value whenever `y` lies in the support of some channel input; define it arbitrarily on outputs never produced. This is well defined and gives zero-error recovery.

Therefore

\[
\boxed{
\text{zero-error recovery}
\iff
E(H(K,d))=\varnothing.
}
\]

For a deterministic channel `K(y|x)=1_{y=T(x)}`, overlap of output supports is exactly equality `T(x)=T(x')`, so this reduces to AF-001's fiber criterion.

### Downstream garbling can only add confusability

Let `L: Y\rightsquigarrow Z` be another finite channel and define

\[
(L\circ K)(z\mid x)
=
\sum_y L(z\mid y)K(y\mid x).
\]

Suppose `{x,x'}` is an edge of `H(K,d)`. Choose a shared output `y` with

\[
K(y\mid x)>0,
\qquad
K(y\mid x')>0.
\]

Because `L(\cdot|y)` is a probability distribution, some `z` satisfies `L(z|y)>0`. Then

\[
(L\circ K)(z\mid x)
\ge L(z\mid y)K(y\mid x)>0
\]

and likewise

\[
(L\circ K)(z\mid x')>0.
\]

The discriminator values were already different, so `{x,x'}` remains an edge downstream. Hence

\[
\boxed{
H(K,d)\subseteq H(L\circ K,d).
}
\]

This is the supportwise analogue of the deterministic irreversibility in AF-001 and the average-risk monotonicity in AF-009. A garbling may create new conflict edges by merging previously disjoint output supports, but it cannot erase an existing one without extra upstream side information.

### Noiseless lifts are graph colorings

Append a deterministic mark `M:X\to A`. Conditional on input `x`, the decoder now observes outputs of the form

\[
(y,M(x))
\qquad
\text{with }K(y\mid x)>0.
\]

Two conflicting states `x,x'` remain confusable after the lift exactly when they share some channel output `y` and also satisfy

\[
M(x)=M(x').
\]

Thus zero-error recovery from `(Y,M)` holds if and only if every edge of `H(K,d)` receives different marks:

\[
\{x,x'\}\in E(H(K,d))
\Longrightarrow
M(x)\ne M(x').
\]

That is precisely a proper vertex coloring. Therefore

\[
\boxed{
\min_M |M(X)|=\chi(H(K,d)).
}
\]

The bound is attained by any optimal coloring. As in AF-001, this does **not** solve the natural-lift problem: the target itself is always a proper coloring because every graph edge joins unequal `d`-values. Hence

\[
\chi(H(K,d))\le |d(X)|,
\]

and unrestricted noiseless marking can still hide a copy of the answer. The graph theorem becomes structurally meaningful only after the admissible mark family is fixed independently of `d`.

### Fixed observable libraries reduce to stochastic discernibility

Let

\[
F_J(x)=(f_j(x))_{j\in J}.
\]

The previous section says that `F_J` restores zero-error recovery exactly when every conflict edge is separated by at least one selected coordinate. For an edge `c={x,x'}`, the eligible separating coordinates are

\[
\Delta(c)=\{i:f_i(x)\ne f_i(x')\}.
\]

Hence

\[
F_J\text{ recovers }d
\iff
\forall c\in E(H(K,d)),
\quad
J\cap\Delta(c)\ne\varnothing.
\]

This is the same hypergraph-transversal statement as AF-002 with a different conflict relation. Deterministic compression contributes conflicts through exact fibers; stochastic compression contributes conflicts through overlap of channel supports.

### Arbitrarily small average defect can coexist with fixed zero-error failure

Take

\[
X=D=\{0,1\},
\qquad
d(x)=x,
\]

with a full-support uniform prior on `X`. Let `Y={0,1}` and, for `0<\varepsilon<1`, define

\[
K_\varepsilon(0\mid0)=1,
\]

\[
K_\varepsilon(0\mid1)=\varepsilon,
\qquad
K_\varepsilon(1\mid1)=1-\varepsilon.
\]

For every positive `\varepsilon`, output `0` lies in the support of both inputs. Therefore

\[
H(K_\varepsilon,d)=K_2
\]

for every `\varepsilon>0`: zero-error recovery fails regardless of how small the crossover probability becomes.

The Bayes classifier, however, makes an error only on the event `X=1,Y=0`, so

\[
e_\varepsilon=\frac{\varepsilon}{2}\to0.
\]

For AF-009's binary conditional-variance defect, the only nonzero posterior variance occurs at `Y=0`. Since

\[
\mathbb P(Y=0)=\frac{1+\varepsilon}{2},
\qquad
\mathbb P(X=1\mid Y=0)=\frac{\varepsilon}{1+\varepsilon},
\]

we obtain

\[
\mathcal R_d(Y)
=
\frac{\varepsilon}{2(1+\varepsilon)}
\to0.
\]

At `\varepsilon=0` the support overlap disappears discontinuously and zero-error fidelity is restored exactly. Thus supportwise fidelity is not continuous in small probability perturbations of a channel:

\[
\boxed{
\text{arbitrarily small average loss}
\not\Rightarrow
\text{zero-error structural fidelity}.
}
\]

This is not a paradox. The two criteria answer different questions: AF-009 weights failures by probability, while the zero-error graph records whether a forbidden discriminator collision is possible at all.

## Relationship to AF-001, AF-002, and AF-009

AF-001 is the deterministic boundary case. A deterministic map has singleton output support at each input, and two states are confusable exactly when they lie in the same compression fiber.

AF-002's decision-relative discernibility hypergraph persists unchanged once the conflict relation is replaced by stochastic support overlap. This shows that fixed-observable lift selection is not a new optimization problem in the noisy case either.

AF-009 is prior-relative and average-case. For a finite channel equipped with a **full-support source prior**, zero conditional-variance defect is equivalent to absence of discriminator-confusability edges, because every support overlap then occurs with positive joint probability. If the prior assigns zero mass to some states, AF-009 may ignore conflicts involving those states while the present distribution-free audit still records them.

The distinction is therefore:

\[
\text{AF-009: what error remains under this probability law?}
\]

versus

\[
\text{AF-011: can any declared upstream state produce an ambiguous retained observation?}
\]

Both are legitimate, but they should not be substituted for one another.

## Prior art and novelty assessment

The graph mechanism is classical.

Claude Shannon's 1956 paper *The Zero Error Capacity of a Noisy Channel* introduced the channel confusability graph: two input symbols are adjacent when the noisy channel can produce a common output from either one. Shannon's concern was zero-error message transmission and graph capacity over repeated channel uses.

Witsenhausen's 1976 *The Zero-Error Side Information Problem and Chromatic Numbers* showed that one-shot zero-error transmission with decoder side information leads directly to a graph-coloring problem when the side information is unavailable at the transmitter.

Orlitsky and Roche's 2001 *Coding for Computing* develops the function-specific characteristic-graph formulation for reliably computing a function with side information. The present graph `H(K,d)` is exactly the one-shot specialization obtained when the required function is the upstream discriminator `d(X)` and the receiver's side information is the stochastic channel output.

Accordingly, no novelty is claimed for the support-overlap criterion, graph coloring, or characteristic-graph reduction. The Arithmetic Fidelity contribution is the **boundary placement** inside the developing compression taxonomy: stochastic fidelity has at least two inequivalent regimes—probability-weighted defect and supportwise zero-error confusability—and the latter survives arbitrarily small-probability perturbations that make the former negligible.

## Boundaries and failure modes

- The theorem is finite and one-shot. Infinite alphabets require measurable/topological support care, and repeated channel uses lead to graph products, graph entropy, Shannon capacity, and other established asymptotic machinery.
- Zero-error here is distribution-free over the declared state set `X`. If some upstream states are impossible by definition rather than merely low probability, they should be removed from `X` before building the graph.
- The criterion depends only on channel support, not on the positive probability values. It therefore deliberately discards quantitative reliability information.
- Conversely, AF-009's average defect can hide rare conflicts. Neither criterion dominates the other as a notion of approximate quality.
- The coloring theorem assumes the appended mark is observed noiselessly. A noisy lift requires composing its own channel and rebuilding the confusability relation.
- The arbitrary-coloring optimum does not establish naturality, locality, equivariance, or absence of target leakage. `M=d` remains an admissible trivial solution unless the lift class forbids it independently.
- The fixed-library extension uses only equality/inequality of observable values, exactly as AF-002; metric or approximate separation needs a different model.
- No claim is made that an RH-relevant arithmetic compression should use a stochastic-channel model. The result is a reusable audit when randomization, sampling, noisy measurement, probabilistic truncation, or approximate observation is genuinely part of the construction.

## Decisive audit test for zero-error stochastic compression

For a finite stochastic representation intended to preserve a discriminator exactly:

1. build the positive-support predecessor sets for every retained output;
2. construct `H(K,d)` from pairs with overlapping support and unequal discriminator values;
3. if the graph has an edge, exact supportwise recovery from the channel alone is impossible and no downstream garbling can repair it;
4. if adding noiseless marks, require the admissible marks to color the conflict graph and audit them for target leakage;
5. for a fixed observable library, use the AF-002 discernibility/hitting-set formulation on the conflict edges instead of inventing a new lift criterion;
6. separately compute AF-009's average defect when probabilities matter, but do not infer zero-error fidelity from a small Bayes or `L^2` error.

## Consequence for the line

Add **support-confusability / zero-error fidelity** as the second canonical stochastic model beside AF-009's conditional-variance/Bayes-risk model.

The line should now distinguish at least:

\[
\text{deterministic exact fidelity}
\quad\leftrightarrow\quad
\text{fiber constancy},
\]

\[
\text{stochastic average fidelity}
\quad\leftrightarrow\quad
\text{Bayes / conditional-risk defect},
\]

and

\[
\text{stochastic zero-error fidelity}
\quad\leftrightarrow\quad
\text{absence of discriminator-confusability edges}.
\]

When an arithmetic application treats a rare exceptional collision as fatal rather than merely unlikely, the supportwise graph is the correct audit object. When rare failures are genuinely tolerable, the average-risk framework is more appropriate. Future work should state which regime the intended mathematical claim requires before assigning meaning to a small numerical fidelity defect.