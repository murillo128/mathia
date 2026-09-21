# MC-438 — Consecutive-block Möbius projection collapses to boundary-spanning motifs

**Evidence:** `EXACT-DERIVED · NEGATIVE/OBSTRUCTION · FRONTIER-ADVANCE · CLASSICAL-MECHANISM · PRIOR-ART-AUDITED · NO-NOVELTY-CLAIM · NON-RH`

## Claim

`MC-437` shows that Möbius convolution at a squarefree source extracts the full Boolean interaction of the divisor statistic. A possible escape from its bounded-degree obstruction is that **adjacency itself depends on the selected divisor**: removing one prime makes previously separated primes adjacent, so even a sum of local chain motifs can have arbitrarily high Boolean degree.

That escape is real at the degree level, but its top interaction has an exact boundary collapse.

Let

\[
n=p_1\cdots p_r,\qquad p_1<\cdots<p_r,
\]

be squarefree. Fix `k>=2` and any scalar- or vector-valued kernel `W(q_1,...,q_k)` on strictly increasing `k`-tuples of primes. For a squarefree integer

\[
m=q_1\cdots q_s,\qquad q_1<\cdots<q_s,
\]

define the consecutive-`k`-block observable

\[
A_{W,k}(m)
:=
\sum_{a=1}^{s-k+1}W(q_a,\ldots,q_{a+k-1}),
\tag{1}
\]

with `A_{W,k}(m)=0` when `s<k`. Then for every `r>=k`,

\[
\boxed{
(\mu*A_{W,k})(n)
=
(-1)^{r-k}
\sum_{1=i_1<i_2<\cdots<i_{k-1}<i_k=r}
W(p_{i_1},\ldots,p_{i_k}).
}
\tag{2}
\]

Thus Möbius convolution annihilates every consecutive-block contribution whose selected block does **not** span both global endpoint primes `p_1` and `p_r`. Selection-dependent adjacency can generate full Boolean interaction, but only the boundary-spanning part survives.

For `k=2`, `(2)` becomes the particularly sharp identity

\[
\boxed{
(\mu*A_{W,2})(n)=(-1)^{r-2}W(p_1,p_r).
}
\tag{3}
\]

Every interior adjacent-pair contribution disappears. In particular, if

\[
W(q_1,q_2)=\phi(q_2-q_1),
\]

then the Möbius projection of the sum of `phi` applied to the adjacent selected-prime gaps is

\[
(\mu*A_{W,2})(n)=(-1)^{r-2}\phi(p_r-p_1).
\tag{4}
\]

For `phi(x)=x`, the entire chain-gap sum collapses to the outer range `p_r-p_1` with the alternating sign in `(4)`.

This is an exact obstruction for a broad natural attempt to turn the factorial gap-order source capacity of `MC-436` into a Möbius-facing observable: **any fixed-size additive motif sum along the selected-prime chain forgets all motifs that fail to touch both endpoints at the top Möbius interaction.** No estimate for `M(x)` follows.

## 1. Exact coefficient calculation

For `T\subseteq[r]`, write its elements in increasing order as

\[
T=\{t_1<\cdots<t_m\}
\]

and set

\[
G_{n,k}(T)
:=
A_{W,k}\!\left(\prod_{i\in T}p_i\right)
=
\sum_{a=1}^{m-k+1}
W(p_{t_a},\ldots,p_{t_{a+k-1}}).
\tag{5}
\]

By `MC-437`,

\[
(\mu*A_{W,k})(n)
=
\sum_{T\subseteq[r]}(-1)^{r-|T|}G_{n,k}(T).
\tag{6}
\]

Fix one increasing `k`-tuple

\[
B=(i_1<\cdots<i_k).
\]

The term `W(p_{i_1},...,p_{i_k})` appears in `G_{n,k}(T)` exactly when the indices in `B` form a consecutive block of the ordered set `T`. Hence:

- every index of `B` must lie in `T`;
- every index strictly between two consecutive elements of `B` but not in `B` must be absent from `T`;
- indices to the left of `i_1` and to the right of `i_k` are unrestricted.

Let

\[
O_B:=\{1,\ldots,i_1-1\}\cup\{i_k+1,\ldots,r\}.
\]

The allowed subsets contributing this fixed motif are precisely

\[
T=B\cup U,\qquad U\subseteq O_B.
\]

Its coefficient in `(6)` is therefore

\[
\sum_{U\subseteq O_B}(-1)^{r-k-|U|}
=
(-1)^{r-k}(1-1)^{|O_B|}.
\tag{7}
\]

This vanishes unless `O_B` is empty, which is equivalent to

\[
i_1=1,\qquad i_k=r.
\]

When those endpoint conditions hold, the coefficient is exactly `(-1)^{r-k}`. Summing the surviving motifs proves `(2)`.

No asymptotics, prime-distribution theorem, analytic continuation, or probabilistic model enters the argument.

## 2. Why this is stronger than the bounded-degree test in MC-437

A fixed local kernel does **not** make `G_{n,k}` a degree-`k` Boolean polynomial. Whether `p_i` and `p_j` are adjacent among the primes selected by `T` depends on the absence of every selected prime between them. Expanding that absence condition introduces arbitrarily high-order products as the gap `j-i` grows.

For example, at `k=2` the contribution of a pair `i<j` contains the indicator

\[
\mathbf 1_{\{i,j\}\subseteq T}
\prod_{i<\ell<j}\mathbf 1_{\ell\notin T},
\]

whose multilinear expansion has degree `j-i+1`. Thus the simple fixed-degree vanishing criterion of `MC-437` does not apply.

Equation `(3)` closes precisely this loophole. The induced high interaction is not generic interior information: inclusion-exclusion cancels every pair that leaves at least one freely selectable prime outside its span. Only the pair spanning the complete ordered source survives.

The same mechanism gives `(2)` for arbitrary fixed block size. At fixed `k`, there are only

\[
\binom{r-2}{k-2}
\]

boundary-spanning `k`-tuples in the surviving formula. This count should not be confused with an information bound on their numerical values; a single kernel value can itself carry substantial arithmetic information. The exact conclusion is structural: **all non-boundary-spanning motif terms are erased.**

## 3. Consequence for the gap-order branch

`MC-436` established that the full ordinal pattern of the `r-1` adjacent prime-divisor gaps realizes all `(r-1)!` permutations. `MC-437` then required an exact divisor statistic before that capacity could be credited as Möbius-relevant.

The most immediate statistics one might build from a chain are additive local-motif sums: total adjacent-gap weight, sums of a nonlinear function of each adjacent gap, fixed-window scores, or vector coordinates obtained by summing a fixed tuple kernel over consecutive selected primes. Equation `(2)` shows that this entire family cannot transport its interior chain structure through Möbius convolution. Its full interaction is determined only by motifs spanning the two extreme prime factors.

For raw gap lengths the collapse is especially severe. Because

\[
\sum_{a=1}^{s-1}(q_{a+1}-q_a)=q_s-q_1,
\]

the full-chain observable already telescopes before convolution; `(4)` shows that the divisor-lattice projection preserves exactly the same endpoint character.

For nonlinear pair kernels the chain sum need not telescope pointwise, yet `(3)` proves that its Möbius interaction still does. This is the substantive new boundary: **nonlinearity of each local gap score does not prevent endpoint collapse.**

The factorial permutation escape therefore has to use structure outside `(1)` if it is to survive Möbius convolution. Possibilities not ruled out here include a genuinely global nonadditive functional of the whole gap permutation, a kernel whose effective block size grows with `r`, or a different arithmetic operation whose survival map is not the Boolean top coefficient.

## 4. Prior art and novelty boundary

The algebraic engine is the classical Boolean-lattice Möbius/Harsanyi transform already audited in `MC-437`: the top interaction is an alternating sum over all subsets, and free subset coordinates cancel by `(1-1)^m`. The literature on set-function Möbius transforms and Harsanyi dividends treats this inversion framework as standard, while graph-restricted and network-cost cooperative games provide adjacent examples where coalition values are built from graph structure.

The present identity is derived directly from that classical mechanism. The prior-art search did not reveal any external theorem needed to obtain `(2)`, and **no novelty claim is made** for the ordered-block specialization itself. Its durable value here is as a frontier-specific exact calculation: it determines what the first natural family of adjacency-dependent divisor statistics from `MC-436` actually becomes under the `MC-437` survival map.

## Boundaries and falsification tests

- **Additivity over consecutive blocks is load-bearing.** A global rank statistic, determinant, extremal score, nonlinear function of the entire motif collection, or other nonadditive observable is not covered merely because it is computed from adjacent gaps.
- **The kernel is intrinsic to the selected tuple.** If an edge label is defined using its rank among all gaps of the current divisor, then that label depends on the surrounding selected set and cannot be inserted into `(1)` as a fixed pair kernel without a separate derivation.
- **Fixed `k` is not required for the identity.** Equation `(2)` holds for every `2<=k<=r`; however, the interpretation as a bounded local motif family concerns `k` not growing comparably to `r`.
- **Boundary collapse is not a state-count theorem.** The surviving endpoint-spanning kernel values can have large or continuous alphabets. Any capacity conclusion needs an additional justified resolution/counting argument.
- **Nonzero top interaction is not cancellation.** Even a large surviving endpoint term supplies no signed average estimate over `n` by itself.
- **The result concerns Möbius divisor convolution.** Another bilinear, spectral, or averaging operation may retain interior chain data and must be audited separately.
- **No RH-scale information is imported.** The proof is finite inclusion-exclusion on a squarefree divisor lattice.

## Consequence for the research line

The first concrete survival test requested by `MC-437` is now resolved for additive consecutive-block statistics. Selection-dependent adjacency does evade the naive bounded-Boolean-degree test, but it does not preserve interior local-motif information: the top Möbius interaction is forced onto blocks spanning the two extreme prime factors.

The live gap-order branch should therefore not spend further effort on fixed-size additive chain scores. The next meaningful test is a **genuinely global nonadditive statistic of the induced gap-order permutation** whose value on every divisor subset is defined intrinsically and whose full Boolean interaction can be computed or sharply constrained before any analytic estimate is attempted.