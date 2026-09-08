# VIS-099 — finite quantization turns local-block reassembly into an exact Markov-type null

## Claim

Let `a=(a_1,...,a_N)` be a finite real sequence, let `Q:R->A` be a fixed quantizer into a finite alphabet `A`, and write `b_i=Q(a_i)`. Fix a memory length `m<N`, the initial context

`u_0=(b_1,...,b_m)`,

and for each `u in A^m`, `c in A` define the transition count

`n(u,c)=#{1<=i<=N-m : (b_i,...,b_(i+m-1))=u, b_(i+m)=c}`.

Let `T_Q(a)` be the set of all length-`N` symbol sequences with the same initial context `u_0` and the same complete table `{n(u,c)}`.

Then:

1. `T_Q(a)` is exactly the order-`m` Markov type class determined by the initial context and transition counts. Equivalently, after lifting `m`-symbol contexts to vertices, its elements are exactly the compatible Eulerian reassemblies of the directed context multigraph with `n(u,c)` edges from `u` to `shift(u,c)`.
2. For every homogeneous order-`m` Markov chain with transition probabilities `p(c|u)` that assigns positive probability to the observed type, every sequence in `T_Q(a)` has the same conditional probability. Hence

`P(B=b' | B_1^m=u_0, {n(u,c)}) = 1/|T_Q(a)|`

for every `b' in T_Q(a)`.
3. Therefore uniform sampling from `T_Q(a)` is an **exact, parameter-free conditional null** for the whole family of homogeneous order-`m` Markov chains on the quantized alphabet. Its nondegeneracy is the concrete combinatorial condition `|T_Q(a)|>1`.

For the active three-delay branch, `m=3`: fixing quantized length-four block counts gives an exact third-order Markov type class. A fourth-level path/log-signature statistic evaluated on a fixed numerical embedding of the quantized symbols can therefore be compared against a mathematically exact local-memory null, provided the type class is non-singleton.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL-MARKOV-TYPE IDENTIFICATION + EXACT CONDITIONAL-NULL CONSTRUCTION + NO-NOVELTY-CLAIM`.

The result does not claim a zeta effect, an arithmetic-specific statistic, or a new Markov-type theorem. Its role is to replace an underspecified “coarsened local-block control” by a precise conditional experiment with an exact null law.

## 1. Quantized blocks are a finite context graph

A quantized length-`(m+1)` word

`(x_1,...,x_m,c)`

is exactly the transition from context

`u=(x_1,...,x_m)`

to

`shift(u,c)=(x_2,...,x_m,c)`.

Thus the table `{n(u,c)}` is the edge-multiplicity table of a finite directed multigraph on the observed `m`-word contexts. Starting at `u_0`, any symbol sequence with this table traverses every edge occurrence with the prescribed multiplicity and therefore gives an Eulerian reassembly of the graph. Conversely, every compatible Eulerian traversal beginning at `u_0` spells a unique symbol sequence with exactly those transition counts.

This is the finite-alphabet analogue of the exact local-block graph in `VIS-094` and `VIS-098`, but quantization deliberately identifies nearby real-valued windows. It can therefore create repeated context states and genuine reassembly freedom even when the exact real-valued graph is a simple path.

The relevant admission test is not merely whether the graph has a repeated vertex. As in `VIS-098`, repetitions need not imply multiple compatible traversals. The null is useful only when the resulting type class contains more than one symbol sequence, and preferably enough alternatives for the intended conditional comparison.

## 2. Conditioning removes the Markov parameters exactly

For a homogeneous order-`m` Markov chain and a fixed initial context `u_0`, the probability of any symbol sequence `b'` is

`P(b' | u_0) = product_(u,c) p(c|u)^(n_(b')(u,c))`.

Every member of `T_Q(a)` has the same transition-count table, so this product is identical over the entire type class. Whenever the conditioning event has positive probability, division by the sum over the class gives the uniform conditional law

`P(b' | u_0, {n(u,c)}) = 1/|T_Q(a)|`.

No transition-probability estimate is required. The conditioning has removed the nuisance parameters exactly rather than approximately matching fitted moments or simulating from a chosen estimator.

The same statement can be viewed as first-order Markov conditioning on the lifted state space `A^m`. Classical Markov-type/Whittle counting machinery can count the compatible sequences from the transition table and the associated Eulerian graph; for this finding only the equal-probability identity and the resulting conditional-uniform law are needed.

## 3. What this buys the level-four chronology test

`VIS-097` proves that a three-delay signature can contain order information at level four that is absent from the unordered exact local-four-block inventory. `VIS-098` then shows why the obvious exact real-valued reassembly null is generically unusable: distinct continuous delay windows make the exact type class a singleton.

A fixed finite quantization supplies a principled next quotient. Choose in advance:

- the unfolding/source representation;
- a finite quantizer `Q`;
- a fixed numerical embedding `e:A->R` when a geometric/path statistic needs numerical coordinates;
- the three-delay construction and finite observation window;
- one direction-sensitive fourth-level or log-signature observable.

The source statistic is then computed on the quantized embedded path `e(Q(a_i))`, and the matched controls are uniform members of the exact `m=3` type class. Every control preserves the initial quantized triple and every quantized length-four block count exactly, while alternative Eulerian assembly is the only remaining degree of freedom inside that conditional model.

If a pre-registered level-four statistic separates the source from this null, the correct conclusion is narrow: the quantized sequence is inconsistent with the corresponding homogeneous order-three Markov conditional model at that statistic. The separation is beyond the admitted quantized local-four-block table, but it is not automatically arithmetic-specific.

## 4. The exactness stops at the quantized quotient

The conditional-uniform theorem is exact for the symbol sequence, and therefore for any statistic that is a deterministic function of the quantized sequence (including a path statistic after a fixed symbol embedding). It does **not** provide an exact null for a statistic evaluated on the original real-valued ordinates or gaps.

To return from a reassembled symbol path to continuous values one must choose some within-cell reconstruction, resampling, or generative law. That extra choice introduces new nuisance structure and can change lower signature levels as well as the level-four residual. The parameter-free conditional guarantee is then lost unless a separate theorem establishes it.

This distinction gives a clean leakage audit. The quantized experiment asks whether chronology survives after a particular finite local quotient. A later continuous-valued experiment must separately measure what information the quotient discarded and what freedom any dequantization model injected.

Likewise, the quantizer itself is part of the representation. Thresholds, alphabet size, normalization, and symbol embedding must be fixed before confirmation data are inspected. Searching them until a level-four separation appears would convert representation choice into the signal.

## 5. Prior art and novelty assessment

The type-class interpretation is classical. P. Whittle, **Some Distribution and Moment Formulae for the Markov Chain**, *Journal of the Royal Statistical Society: Series B* 17:2 (1955), 235–242, DOI `10.1111/j.2517-6161.1955.tb00197.x`, develops formulae for realizations with fixed Markov transition totals. Richard Cowan, **Expected frequencies of DNA patterns using Whittle's formula**, *Journal of Applied Probability* 28:4 (1991), 886–892, DOI `10.2307/3214691`, explicitly uses the fact that realizations with the prescribed transition counts are equally likely under the conditioned Markov model. Philippe Jacquet, Charles Knessl, and Wojciech Szpankowski, **Counting Markov Types, Balanced Matrices, and Eulerian Graphs**, *IEEE Transactions on Information Theory* 58:7 (2012), 4261–4272, DOI `10.1109/TIT.2012.2191476`, develops the Markov-type/Eulerian-graph counting correspondence.

No novelty is claimed for Markov types, Whittle counting, Eulerian reconstruction, or the conditional-uniform identity. The Mathia-specific contribution is the control selection: after the exact continuous local-block null in `VIS-098` was shown to be generically singleton, finite pre-registered quantization yields a mathematically exact and testable replacement **on the quotient representation**, while making explicit where continuous-value leakage re-enters.

## Boundary and falsification

This finding does not establish that any particular quantizer is informative, nondegenerate, or statistically powerful on Riemann-zero data. A coarse quantizer may create abundant reassemblies while destroying the very chronology one hoped to test; a fine quantizer may leave a singleton or tiny type class. Either outcome is a legitimate failure of that representation.

It also does not establish stationarity or finite-order Markov structure for zeta gaps. The homogeneous order-`m` Markov family is the null being conditioned away, not a model asserted to be true.

Falsify the main conditional-null claim by giving two symbol sequences with the same initial `m`-context and the same complete transition-count table but different probabilities under one homogeneous order-`m` Markov chain assigning positive probability to both. The factorization above would then fail.

The theorem remains true even when `|T_Q(a)|=1`; in that case it is simply a degenerate conditional experiment and cannot test chronology. Nondegeneracy must therefore be verified for the actual pre-registered representation before the level-four statistic is interpreted.

## Visual consequence

No canonical PNG is retained. The useful object is the exact quotient graph and its conditional sample space; a rendered graph would not add evidence beyond the transition-count theorem.

## Research consequence

The accepted critical-strip multiscale clue now has a concrete first replacement for the singleton exact-real-valued null: **pre-register a finite quantized representation, require a nondegenerate third-order Markov type class, and test one pre-registered level-four statistic against the uniform conditional type-class law**.

A positive result at this stage would establish chronology beyond quantized four-block counts, not arithmetic specificity. Before any stronger interpretation, it must survive quantizer/embedding controls fixed independently of confirmation data and then be compared with suitably matched higher-order spectral controls rather than only with the conditioned Markov family.