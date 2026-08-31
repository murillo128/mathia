# AF-015 — Abstract multiplication forgets rational-prime norms

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-IDENTITY`, `NEGATIVE/OBSTRUCTION`

## Claim

Let

\[
M=\mathbb N_{>0}
\]

be viewed **only as a commutative monoid under multiplication**, with no addition, order, embedding in `\mathbb R`, or numerical norm retained. By unique factorization, `M` is the free commutative monoid on the set `\mathcal P` of rational primes.

Then:

1. every monoid automorphism of `M` permutes the prime generators, and every permutation of `\mathcal P` extends uniquely to a monoid automorphism. Hence
   \[
   \operatorname{Aut}(M)\cong \operatorname{Sym}(\mathcal P);
   \]
2. if
   \[
   n=\prod_{j=1}^r p_j^{a_j},\qquad a_j>0,
   \]
   the `Aut(M)`-orbit of `n` is determined exactly by the unordered multiset of positive exponents
   \[
   \lambda(n)=\{a_1,\ldots,a_r\};
   \]
   equivalently, the orbit quotient remembers the **factorization shape** but not which prime generator carries which exponent;
3. primality survives this quotient: the primes are exactly the elements with shape `{1}`. More generally, properties determined only by exponent shape, such as being square-free or the total number of prime factors counted with multiplicity, survive;
4. no individual rational-prime identity survives. All primes lie in one automorphism orbit, so any observable invariant under every abstract multiplicative automorphism takes the same value on every prime;
5. in particular, the ordinary numerical norm
   \[
   \nu(n)=n
   \]
   and its logarithm are **not** intrinsic to the bare multiplicative monoid: on primes, `\nu(p)=p` is not constant on the unique prime orbit. Neither the order of the primes nor the distinguished weights `\log p` can be recovered from automorphism-invariant data of the unweighted monoid alone.

Thus there is an exact fidelity boundary between **prime type** and **rational-prime specificity**. Abstract multiplication and unique factorization retain the notion “is an irreducible/prime generator” but erase the numerical identity and Archimedean size that distinguish `2`, `3`, `5`, and the rest.

This boundary is already built into classical abstract analytic number theory. Knopfmacher's arithmetical semigroup formalism takes a uniquely factorizing commutative semigroup/monoid of abstract primes together with an additional multiplicative norm (or additive degree) map. The norm is not redundant decoration: it is precisely extra structure beyond the free multiplicative monoid. Consequently, a proposed rational-prime discriminator that is invariant under arbitrary prime-generator permutations cannot obtain the ordinary prime norm from multiplication alone.

## Derivation

### The prime generators are intrinsic as atoms

Call a non-unit `a in M` an atom if

\[
a=bc\Longrightarrow b=1\text{ or }c=1.
\]

For positive integers under multiplication, the atoms are exactly the ordinary primes. Atomicity is defined purely in the monoid language, so every automorphism sends atoms to atoms. Therefore every

\[
\phi\in\operatorname{Aut}(M)
\]

induces a permutation of `\mathcal P`.

Conversely, let

\[
\sigma:\mathcal P\to\mathcal P
\]

be any permutation. Unique factorization gives a unique map

\[
\phi_\sigma\!\left(\prod_p p^{v_p(n)}\right)
=
\prod_p \sigma(p)^{v_p(n)}.
\]

It is multiplicative, has inverse `\phi_{\sigma^{-1}}`, and is therefore a monoid automorphism. This proves

\[
\boxed{\operatorname{Aut}(\mathbb N_{>0},\times)\cong\operatorname{Sym}(\mathcal P).}
\]

No analytic number theory is involved: this is the universal property of a free commutative monoid together with the fundamental theorem of arithmetic.

### The exact automorphism quotient is factorization shape

Write

\[
n=\prod_{j=1}^r p_j^{a_j}
\]

with distinct `p_j` and positive `a_j`. An automorphism can rename the support primes arbitrarily but cannot change the exponents attached to them. Hence `\lambda(n)`, the multiset of positive exponents, is invariant.

Conversely, suppose

\[
m=\prod_{j=1}^r q_j^{b_j}
\]

has the same exponent multiset. After reindexing, take `a_j=b_j`. Choose a permutation of the prime set carrying every `p_j` to `q_j` and extend it arbitrarily to the remaining primes. Its induced monoid automorphism carries `n` to `m`.

Therefore

\[
\boxed{
n\sim_{\operatorname{Aut}(M)}m
\iff
\lambda(n)=\lambda(m).
}
\]

So the orbit space of the bare multiplicative monoid is not a quotient that forgets all arithmetic. It retains exactly the unlabeled factorization pattern.

For example,

\[
12=2^2\cdot3
\quad\text{and}\quad
75=3\cdot5^2
\]

have the same shape `{2,1}` and lie in the same orbit, while `12` and `18=2\cdot3^2` also lie in the same orbit. But `12` and `36=2^2\cdot3^2` do not, because `{2,1}` and `{2,2}` differ.

### Prime type survives while prime identity does not

An element is prime exactly when its factorization shape is `{1}`. Hence primality itself is invariant under all automorphisms. The same is true for every property that factors through `\lambda`.

But the action on the set of atoms is transitive: for any rational primes `p,q`, a generator permutation exists with `\phi(p)=q`. Therefore every fully automorphism-invariant observable `F:M\to A` satisfies

\[
F(p)=F(q)
\qquad\text{for all primes }p,q.
\]

In particular, the ordinary embedding/norm `n\mapsto n` fails this test because `p\ne q` gives different values. So do `\log p`, the natural order of primes, residue information requiring addition, and any other datum whose definition distinguishes one abstract prime generator from another.

This is an instance of AF-003's maximal-admissible-quotient rule. Here the admissibility principle is invariance under every automorphism of the bare multiplicative monoid, and its exact orbit quotient is `\lambda`. If a discriminator varies inside one `\lambda`-fiber, no observable constrained to that symmetry class can recover it.

## Normed arithmetical semigroups make the missing structure explicit

Classical abstract analytic number theory already separates these layers. An arithmetical semigroup has a countable prime set with unique factorization together with a multiplicative norm

\[
|ab|=|a||b|,
\qquad |p|>1,
\]

plus a finiteness condition on bounded norm. In additive form one uses a degree

\[
\partial(ab)=\partial(a)+\partial(b).
\]

The ordinary positive integers are the prototype, with `|n|=n`. Thus classical theory does not regard the free multiplicative structure as sufficient to recover ordinary prime sizes; the norm/degree is specified as additional data.

This supplies a cleaner prior-art boundary than treating “generalized primes” only as an adversarial analogy. Once the category has forgotten the norm, the prime-permutation symmetry above proves an exact no-go. Restoring a norm breaks that symmetry according to the weight assignment on generators, but **an arbitrary norm is not yet rational-prime specificity**: many weight systems on the same formal free prime monoid are possible. Beurling generalized-prime systems and abstract arithmetical semigroups are established frameworks for studying precisely such variation of prime-like multiplicative systems and their size data.

Therefore the meaningful downstream question is not

> does multiplication remember primality?

—it does—but rather

> which independently justified extra structure singles out the ordinary rational-prime norm strongly enough to survive the later compression being studied?

## Why this matters for Arithmetic Fidelity

The finding separates three levels that otherwise risk being conflated:

1. **unique-factorization fidelity:** the bare monoid remembers atomhood and exponent shape;
2. **weighted-prime fidelity:** a chosen norm/degree distinguishes generators according to externally supplied weights;
3. **rational-prime fidelity:** the specific ordinary assignment `p\mapsto p` (or `p\mapsto\log p`) must remain distinguishable from matched alternative weight systems after the destination map.

This makes “the construction still contains primes” an insufficient audit. A representation can perfectly preserve the abstract prime-generator structure while having already forgotten every feature that makes the generator set the **ordinary rational primes with their actual norm**.

It also narrows the Beurling/arithmetic-equivalence clue. A category-independent minimal-lift theory is already too weak by AF-001, and the bare multiplicative category has a complete classical answer: the maximal symmetry quotient is factorization shape. Any residual capable of supporting a rational-prime-specific RH mechanism must therefore be **category-indexed** and must retain structure that breaks arbitrary prime permutation for an independently mathematical reason.

## Prior art and novelty assessment

The mathematical ingredients are classical. The fundamental theorem of arithmetic identifies positive integers under multiplication with the free commutative monoid on the rational primes. The automorphism and orbit statements above follow immediately from that free-object description.

Knopfmacher's *Abstract Analytic Number Theory* treats arithmetical semigroups as uniquely factorizing commutative semigroups equipped with a norm, with the positive integers as the prototype. Cohen's formulation of additive arithmetical semigroups states the same separation particularly explicitly: a free commutative semigroup with identity is generated by abstract primes and is additionally equipped with an additive degree map satisfying finiteness conditions.

No novelty is claimed for free commutative monoids, generator permutations, factorization shape, or normed arithmetical semigroups. The Arithmetic Fidelity contribution is the exact placement of the boundary: **multiplicative structure alone is faithful to prime type but not to rational-prime norm identity**, and the obstruction is the full symmetric group on the prime generators. This gives a decisive matched-control test before a downstream spectral, positive, averaged, or asymptotic object is interpreted as retaining specifically rational-prime information.

## Boundaries and falsification tests

- The theorem intentionally forgets addition, order, and the standard embedding in the real numbers. Any of those can break prime-permutation symmetry and must be audited as genuinely additional retained structure.
- The classification is for automorphisms of the **bare** multiplicative monoid. If the admissible morphisms are required to preserve a chosen norm, order, topology, measure, or other marking, the automorphism group can shrink drastically.
- Preserving atomhood is not the same as preserving a named prime. A mechanism whose target discriminator is only “prime versus composite” is not killed by this finding.
- A norm attached to the free monoid is additional structure, but merely choosing the ordinary norm by hand does not explain why a later compression preserves it or why it defeats matched generalized-prime controls.
- Beurling generalized-number systems can have multiplicative coincidences in their numerical realization and count generalized integers with multiplicity. The exact free-monoid theorem here is therefore applied to the formal uniquely-factorizing prime-label layer / Knopfmacher arithmetical-semigroup setting, not asserted as a theorem that every numerical Beurling realization is literally the same free submonoid of `\mathbb R_{>0}`.
- The result has no direct RH consequence. A concrete RH line must identify its exact destination map and show that the rational-prime norm or another prime-specific discriminator survives there against controls in the same category.

## Decisive audit test

For a proposed prime-derived representation, strip away every structure the destination actually forgets and determine the automorphism group of what remains. If arbitrary prime-generator permutations still act, then any destination observable invariant under those automorphisms can preserve at most unlabeled prime-factorization type. It cannot certify the ordinary prime norm.

A candidate escapes this obstruction only by identifying additional structure that:

1. is present independently of the desired RH conclusion;
2. breaks the relevant prime-permutation equivalences before they are compressed away; and
3. remains visible after the exact downstream transformation under study.

## Consequence for the line

Use **prime-generator permutation symmetry** as the baseline control for multiplicative constructions. Before invoking Beurling systems, spectra, positivity, or asymptotics, ask whether the current representation has retained anything beyond the free prime-label monoid. If not, the exact surviving information is only factorization shape and no rational-prime-specific norm information can be reconstructed downstream.

The next nonclassical target is therefore narrower: classify, category by category, the weakest independently defined enrichments—norm, additive coupling, order, Archimedean embedding, local/global marking, operator structure, or another relation—whose maximal admissible quotient genuinely breaks the prime-permutation barrier and then test whether that enrichment still separates the ordinary primes from matched alternative norm systems after compression.