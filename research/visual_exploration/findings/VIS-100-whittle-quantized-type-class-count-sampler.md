# VIS-100 — Whittle cardinality makes the quantized Markov-type null exactly countable and sampleable

## Claim

Continue with the finite-alphabet quotient from `VIS-099`. Let `b=(b_1,...,b_N)` be a symbol sequence, fix memory length `m<N`, and lift it to context states

`u_i=(b_i,...,b_(i+m-1))`, `1<=i<=N-m+1`.

Let `s=u_1` and `t=u_(N-m+1)` be the initial and terminal contexts. For context states `u,v`, let

`F_(uv)=#{1<=i<=N-m : u_i=u, u_(i+1)=v}`

and let

`r_u=sum_v F_(uv)`.

Restrict to the finite set `V` of context states that occur in the path. Define the matrix `B` on `V` by

`B_(uv)=delta_(uv)-F_(uv)/r_u`

when `r_u>0`, and `B_(uv)=delta_(uv)` when `r_u=0`. Let `C_(t,s)(B)` denote the ordinary signed cofactor obtained by deleting row `t` and column `s`.

Then the exact cardinality of the Markov type class with the same initial context and transition table is

`W(s,t;F) = |T_Q(b)|`
` = [prod_u r_u! / prod_(u,v) F_(uv)!] C_(t,s)(B)`.

This is Whittle's classical transition-count formula applied to the lifted context chain. In particular, the exact admission gate from `VIS-099` is computable without enumerating all reassemblies:

`the quantized conditional null is nondegenerate iff W(s,t;F)>1`.

Moreover the same cardinality gives an exact sequential uniform sampler. Suppose the current context is `x` and the remaining transition table is `F`. For each allowed next context `y` with `F_(xy)>0`, put

`F' = F - E_(xy)`

and compute the number of compatible completions

`W(y,t;F')`.

Choose `y` with probability

`W(y,t;F') / W(x,t;F)`,

assigning zero probability to transitions whose residual table has no compatible completion. Repeating this rule generates every member of the type class with probability exactly `1/W(s,t;F)`.

For the active `m=3` quantized three-delay branch, this turns the null in `VIS-099` into a completely specified finite conditional experiment: its support size and exact sampling law are both determined by the quantized length-four block counts.

**Evidence/status:** `LITERATURE+DERIVED + CLASSICAL-WHITTLE COUNT + EXACT CONDITIONAL SAMPLER + NO-NOVELTY-CLAIM`.

No zeta effect, arithmetic specificity, statistical power guarantee, new Euler-trail enumeration theorem, or new Markov-type theorem is claimed.

## 1. The lifted delay path is an ordinary finite-state transition-count problem

For fixed `m`, each length-`m` context is a state and each observed length-`(m+1)` block is a directed transition between contexts. Thus the complete quantized block-count table from `VIS-099` is exactly a transition-count matrix `F` for a first-order chain on the lifted state space.

The start state is the initial `m`-block `s`; the terminal state `t` is determined by the final `m`-block. For a feasible observed path the degree balances satisfy

`out(u)-in(u)=1_(u=s)-1_(u=t)`

with the balanced Euler-circuit case `s=t` included. Keeping `F` and `s` fixed therefore also fixes the compatible terminal state.

Whittle's formula counts state sequences with precisely these transition totals and endpoints. Because a lifted context sequence is in one-to-one correspondence with its underlying symbol sequence once the initial context is fixed, the same formula counts `T_Q(b)` itself.

The factorial term

`prod_u r_u! / prod_(u,v) F_(uv)!`

accounts for repeated outgoing transition types, while the cofactor `C_(t,s)(B)` supplies the global connectivity/Euler-trail compatibility that a local multiplicity count alone misses. This is exactly why repeated contexts are not sufficient for nondegeneracy: the cofactor can collapse the apparent local branching into one globally compatible assembly.

## 2. Exact nondegeneracy is a count, not a visual graph judgment

`VIS-098` showed that repeated states are necessary but not sufficient for multiple exact real-valued reassemblies. `VIS-099` then replaced the generically singleton real-valued graph by a finite quantized Markov type, but left its admission condition as the abstract requirement `|T_Q(b)|>1`.

The Whittle count closes that gap. Once the quantizer and observation window are frozen, `W(s,t;F)` is an exact integer determined by the observed quantized block table. No graph drawing, heuristic cycle count, MCMC exploration, or finite sampling failure is needed to decide whether the conditional sample space is a singleton.

This does **not** supply a universal lower threshold for statistical usefulness. `W=1` is a hard rejection of the chronology test, while `W>1` only certifies that counterfactual assemblies exist. Whether the support is large and diverse enough for a chosen level-four statistic is a separate power/design question and must be fixed without tuning on confirmation residuals.

## 3. Completion counts give an exact uniform sampler

Let `W(x,t;F)` denote the number of valid remaining symbol sequences when the current context is `x`, the terminal context must be `t`, and the remaining transition multiset is `F`.

Every valid completion begins with exactly one outgoing transition `x->y`. Removing that transition partitions the type class disjointly, so

`W(x,t;F)=sum_(y:F_(xy)>0) W(y,t;F-E_(xy))`,

where incompatible residual tables contribute zero.

Therefore choosing the first transition with probability proportional to its number of completions is exactly the conditional distribution of the first step under the uniform type-class law. After that choice the same argument applies recursively.

For a completed sequence with residual counts

`W_0, W_1, ..., W_(N-m)=1`,

the generated probability telescopes:

`(W_1/W_0)(W_2/W_1)...(1/W_(N-m-1)) = 1/W_0`.

Thus the sampler is exact and needs neither burn-in nor an asymptotic mixing argument. The only substantive implementation requirement is to evaluate the completion counts correctly; large factorials and cofactors may require exact-integer/rational arithmetic or numerically stable equivalent calculations.

## 4. Prior art and novelty assessment

The counting theorem is classical. P. Whittle, **Some Distribution and Moment Formulae for the Markov Chain**, *Journal of the Royal Statistical Society: Series B* 17:2 (1955), 235–242, DOI `10.1111/j.2517-6161.1955.tb00197.x`, derives the exact transition-total distribution and the determinant/cofactor formula underlying the cardinality above.

Richard Cowan, **Expected frequencies of DNA patterns using Whittle's formula**, *Journal of Applied Probability* 28:4 (1991), 886–892, DOI `10.2307/3214691`, explicitly states the sequence-counting interpretation, equal conditional probabilities, and the sequential construction that chooses the next symbol in proportion to the number of remaining compatible sequences.

Philippe Jacquet, Charles Knessl, and Wojciech Szpankowski, **Counting Markov Types, Balanced Matrices, and Eulerian Graphs**, *IEEE Transactions on Information Theory* 58:7 (2012), 4261–4272, DOI `10.1109/TIT.2012.2191476`, gives the modern Markov-type/balanced-matrix/Eulerian-graph context.

No novelty is claimed for any of this combinatorics. The Mathia-specific result is the exact specialization to the quantized local-block null selected in `VIS-099`: the same fixed length-four block table that conditions away homogeneous third-order Markov parameters also supplies an exact support-size admission gate and an exact uniform reassembly sampler.

## Boundary and falsification

The formula and sampler live entirely on the fixed finite-alphabet quotient. They do not justify evaluating the null on the original continuous-valued zeta-gap path, and they do not repair information discarded by the quantizer.

They also do not make data-dependent representation search safe. A quantizer, symbol embedding, window, and level-four statistic must still be fixed independently of confirmation residuals. Choosing among quantizers after seeing the target separation would turn representation search into part of the test.

Falsify the specialized counting claim by exhibiting a feasible quantized context path for which direct enumeration of all symbol sequences with the same start context and transition table disagrees with the Whittle cardinality above. Falsify the sampler claim by showing that its completion-count recursion assigns unequal probabilities to two members of the same admitted type class.

## Visual consequence

No canonical PNG is retained. The useful object is the exact finite conditional sample space; a graph rendering would add no mathematical evidence to the cofactor-factorial count.

## Research consequence

The accepted critical-strip multiscale clue no longer needs an unspecified enumeration or approximate reassembly procedure at its first admission gate. For any pre-registered quantized three-delay representation, compute `W(s,t;F)` exactly; reject the local-memory chronology experiment if `W=1`, and otherwise sample its conditioned homogeneous-order-three Markov null exactly by recursive Whittle completion counts.

This closes the null-construction mechanics. The next independent step is no longer another reassembly theorem: it is the pre-registered source-specific experiment itself, with representation and level-four statistic frozen before confirmation.
