# MC-435 — Bounded local decorations cannot supply polynomial source-type diversity

**Evidence:** `EXACT-DERIVED · NEGATIVE/OBSTRUCTION · FRONTIER-ADVANCE · CLASSICAL-INGREDIENTS · PRIOR-ART-AUDITED · NO-NOVELTY-CLAIM · NON-RH`

## Claim

`MC-434` separates two resources that the previous relational-capacity audit had conflated. The canonical successor order on the prime divisors of a squarefree integer is internally rigid, so it can address every factor partition, yet its bare isomorphism type has zero variation once `r=omega(n)` is fixed. The immediate escape is to decorate that canonical order by source-dependent arithmetic data such as residue labels, gap bins, ratio bins, local character values, or other local marks.

There is a simple exact budget law for this escape.

Let

\[
n=p_1\cdots p_r,\qquad p_1<\cdots<p_r,
\]

be squarefree, and retain the directed successor chain

\[
p_1\to p_2\to\cdots\to p_r.
\]

For each `r`, choose `m_r` canonically positioned decoration sites on this chain. A site may be a vertex, an edge, or any other position determined solely by rank; no independence between sites is assumed. At site `j`, the decoration takes values in a finite alphabet `A_{r,j}`. Write

\[
B_r:=\sum_{j=1}^{m_r}\log |A_{r,j}|.
\tag{1}
\]

Let `T_r` be the number of isomorphism types of decorated successor structures that are actually realized as `n` ranges over squarefree integers with `omega(n)=r`. Then

\[
\boxed{T_r\le \prod_{j=1}^{m_r}|A_{r,j}|=e^{B_r}.}
\tag{2}
\]

The bound is exact at the representation level: because the directed successor chain has a unique rank-preserving isomorphism, two decorated chains are isomorphic only if their corresponding rank-position labels agree. Arithmetic constraints may make many label words unrealizable, but they can never create more types than the product alphabet permits.

Calibrate this against the squarefree primorial

\[
N_r:=\prod_{j\le r}p_j,
\qquad
\log N_r=(1+o(1))r\log r.
\tag{3}
\]

Then

\[
\boxed{B_r=o(r\log r)\quad\Longrightarrow\quad T_r=N_r^{o(1)}.}
\tag{4}
\]

Conversely, if a decorated-order mechanism requires conditional source-type diversity

\[
T_r\ge N_r^{\alpha-o(1)}
\]

for some fixed `alpha>0`, then necessarily

\[
\boxed{B_r\ge (\alpha-o(1))r\log r.}
\tag{5}
\]

Thus a source-varying decoration of the canonical prime order does not escape `MC-434` merely by being arithmetic, local, or canonical. To retain a fixed polynomial fraction of the primorial-scale source diversity, it must carry an **identity-scale total label budget** of order `r log r` natural-information units.

A useful uniform specialization is immediate. If `m_r<=Cr` and every site uses at most `K_r` labels, then

\[
T_r\le K_r^{Cr}.
\tag{6}
\]

Hence

\[
K_r=r^{o(1)}
\quad\Longrightarrow\quad
T_r=N_r^{o(1)}.
\tag{7}
\]

For edge-only decoration, where `m_r=r-1`, retaining `N_r^{\alpha-o(1)}` source types forces

\[
K_r\ge r^{\alpha-o(1)}.
\tag{8}
\]

This is a **source-diversity obstruction**, not a cancellation estimate. It does not bound `M(x)` and gives no RH consequence.

## 1. Exact type-count proof

The directed path on `r` vertices has a unique isomorphism to every other directed path on `r` vertices: the first vertex must map to the first, its successor to the second, and so on. Therefore a decorated successor chain has no residual coordinate permutation after the rank scaffold is fixed.

Associate to a source `n` its decoration word

\[
w(n)=(a_1(n),\ldots,a_{m_r}(n))
\in
\prod_{j=1}^{m_r}A_{r,j}.
\tag{9}
\]

If two sources have isomorphic decorated successor structures, their words agree coordinatewise. Conversely, for the representation defined here, equal words give the same decorated isomorphism type. Thus the realized types inject into the Cartesian product in `(9)`, proving `(2)`.

No stochastic independence, equidistribution, prime-number theorem in progressions, gap theorem, or other arithmetic input enters this finite count. Correlations among the labels only shrink the realized image.

Now divide `log T_r<=B_r` by `(3)`. If `B_r=o(r log r)`, then

\[
\frac{\log T_r}{\log N_r}\to0,
\]

which is `(4)`. If instead `T_r>=N_r^{\alpha-o(1)}`, the same comparison reverses to give `(5)`. Equation `(6)` follows from `B_r<=Cr log K_r`, and `(7)`--`(8)` are its primorial-scale consequences.

The theorem is deliberately phrased in terms of the **realized decoration word** rather than the algorithm that computes it. A complicated arithmetic rule cannot beat the count if its final retained output still lives in the same finite product alphabet.

## 2. What this rules out

The result immediately kills a broad family of tempting repairs to the universal-order obstruction in `MC-434` when the downstream representation keeps only bounded-resolution local marks.

For example, any fixed modulus `q` may label each prime divisor by its residue class, each adjacent pair by a residue transition, or each edge by whether its prime gap lies in one of finitely many bins. A fixed finite collection of finite-order characters, finitely many sign tests, bounded-depth local predicates, or any fixed finite tuple of such labels still gives `K_r=O(1)` per `O(r)` sites. Their total conditional source-type count is at most

\[
\exp(O(r))=N_r^{o(1)}.
\tag{10}
\]

The same conclusion holds for a slowly growing menu of labels. If each local site has only `r^{o(1)}` possible retained values and only `O(r)` sites are kept, then `(7)` applies regardless of how arithmetically sophisticated the rule producing those labels is.

This does **not** say such coarse data are mathematically useless. Residues, characters, or coarse gap statistics can support strong analytic theorems. The statement is narrower: they cannot be credited with carrying a polynomial number of distinct equal-`omega` source types through the decorated-order representation unless their aggregate retained alphabet grows to the `r log r` information scale.

## 3. Why this is distinct from `MC-432`

`MC-432` studies a different quotient. There the prime coordinates are colored and one asks how many **factor-partition states** survive after permutations inside color classes. The load-bearing quantity is the multinomial distinguishability budget

\[
D=\log\frac{r!}{\prod_a r_a!}.
\]

`MC-434` then shows that factor-state addressability and arithmetic source variation are not the same thing: the bare successor chain is rigid enough to keep all Bell factor states distinct while contributing only one source isomorphism type at fixed `r`.

The present result prices the missing second resource directly. It does not count factor partitions at all. It asks how many different **decorated source structures** can occur after the universal rank scaffold has been factored out. The answer is controlled by the total retained label budget `B_r`.

So the two resource tests are complementary:

- `MC-432` asks how much prime distinguishability is needed to preserve factor-incidence state capacity under a color quotient;
- `MC-435` asks how much source-varying decoration is needed to create polynomially many non-isomorphic ordered-prime sources once the canonical rank frame itself is recognized as universal.

A proposal can pass one test and fail the other.

## 4. Global ordinal relations expose the exact escape

The theorem also clarifies what a genuine escape must pay.

Suppose the `r-1` consecutive prime-divisor gaps are retained only through their **global rank order**: which gap is smallest, second-smallest, and so on, ignoring the actual magnitudes when ties are absent. Superficially this uses no high-precision real values. But the resulting ordinal pattern can take up to

\[
(r-1)!
\]

values, whose logarithm is

\[
(1+o(1))r\log r.
\tag{11}
\]

Equivalently, if one writes the global ranks back onto the `r-1` edge positions, the effective edge alphabet already has size about `r`. The representation has therefore paid exactly the scale required by `(5)`.

This is an important boundary. **Low numerical precision is not the same as low source information.** A globally coupled comparison pattern can encode `Theta(r log r)` bits of ordering information even though every comparison is qualitative.

Equation `(11)` does not establish that all gap-order permutations are realizable by prime-divisor sets under any useful size constraint, nor that their ordinal pattern survives a Möbius-facing analytic operation. It only shows why a global ordering relation is outside the bounded-local-decoration obstruction: its combinatorial alphabet is already identity-scale.

## 5. Consequence for the decorated-order frontier

After `MC-434`, it was natural to try canonical decorations of the prime-successor chain. The present result supplies the first resource gate for that search.

A candidate should first expose the exact retained source-varying datum and compute its finite type budget after conditioning on `omega(n)=r`. If the datum consists of only `O(r)` bounded or `r^{o(1)}`-valued local labels, then it has only `N_r^{o(1)}` possible source types and cannot be the polynomial-capacity escape sought after `MC-430`--`MC-434`.

To escape, the candidate must use at least one of the following kinds of resources:

- polynomially growing effective local alphabets;
- superlinear numbers of retained local sites;
- genuinely global relational patterns whose number of possible types is `exp(Theta(r log r))` or larger;
- continuous/high-resolution values whose justified discretization carries the same aggregate information budget.

Passing this source-diversity gate is still only a representation condition. The line-specific Möbius test remains harder: the source-varying information must survive coefficient formation, averaging, sign projection, or the intended bilinear/Dirichlet-polynomial operation and create a signed analytic gain. A high-capacity decoration that is subsequently forgotten is no better than the rigid universal scaffold in `MC-434`.

## Prior art and novelty boundary

The combinatorial core is elementary finite-word counting. If positions `j` take values in alphabets `A_{r,j}`, there are at most `prod_j |A_{r,j}|` words, and the logarithm of that count is the additive description budget in `(1)`. The information-theoretic language is classical; Claude E. Shannon, *A Mathematical Theory of Communication*, Bell System Technical Journal **27** (1948), 379--423 and 623--656, DOI `10.1002/j.1538-7305.1948.tb01338.x` / `10.1002/j.1538-7305.1948.tb00917.x`, is the foundational source for logarithmic information and finite-alphabet capacity. Finite-alphabet word growth is also standard symbolic-dynamics language; Lind and Marcus, *An Introduction to Symbolic Dynamics and Coding* (Cambridge University Press, 1995), treats entropy as the growth rate of admissible finite words.

No novelty is claimed for word counting, Shannon information, symbolic-dynamics entropy, labeled paths, Stirling's formula, or primorial asymptotics. The durable Mathia contribution is the **frontier specialization**: once `MC-434` exposes canonical prime order as a rigid but source-universal scaffold, `(2)`--`(8)` give an exact cost law for adding source-varying local arithmetic decoration. This prevents bounded residues, character tags, gap bins, or other finite local marks from being mistaken for a polynomial-capacity source discriminator merely because they are canonically derived from the primes.

A literature search across finite graph labelings, symbolic dynamics, and information-capacity language found the expected general theories but no need for a stronger external theorem: the arithmetic statement here is a direct finite counting consequence, and it is intentionally classified as classical-ingredients/no-novelty-claim rather than a new combinatorial theorem.

## Boundaries and falsification tests

- **Finite retained alphabets are load-bearing.** Real-valued gaps, ratios, or phases are not covered until a justified finite resolution is specified. Hidden infinite precision must not be assigned zero cost.
- **Canonical rank positions are load-bearing.** The theorem prices decorations of the successor scaffold. A different relation with superlinear incidence structure or global constraints needs its own type count.
- **`O(r)` sites are needed for the simple corollary `(7)`, not for the master bound `(2)`.** Equation `(2)` applies to arbitrary `m_r`; a superlinear number of sites simply contributes proportionally to `B_r`.
- **The count is an upper bound on realizable arithmetic types.** Arithmetic restrictions, correlations, forbidden words, and prime-distribution constraints can only reduce `T_r`; no equidistribution assumption is made.
- **Conditional source diversity is not cancellation.** Even `T_r=N_r^{1-o(1)}` would not imply orthogonality, a mean-value theorem, or any bound for `M(x)`.
- **Low numerical precision can still hide high combinatorial cost.** Global rank/order patterns such as `(11)` are not counterexamples because their effective alphabet/word count already has `Theta(r log r)` logarithmic size.
- **A source label may be redundant with `omega(n)`.** Conditioning on fixed `r` deliberately removes the trivial information already present in the length of the chain.
- **Post-projection survival remains mandatory.** If a downstream Möbius observable depends only on block sizes, parity, or another coarse quotient, the relevant information budget is that of the surviving datum, not the upstream decoration.

The next first-kill test is therefore concrete: for any weighted/decorated successor-chain proposal, discretize only at the resolution actually used by the downstream analytic operation and compute `B_r`. If `B_r=o(r log r)`, the source-varying representation has subpolynomial primorial-scale diversity. If `B_r` reaches `Theta(r log r)`, the capacity obstruction has been escaped, but the proposal must then justify why that much retained source information is canonical, non-near-lossless, and Möbius-relevant.