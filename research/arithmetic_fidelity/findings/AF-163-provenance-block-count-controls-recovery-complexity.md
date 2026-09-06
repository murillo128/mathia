# AF-163 — Provenance block count controls blockwise recovery complexity

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `QUANTITATIVE-FIDELITY`, `COMPOSITION-LAW`, `STRUCTURAL-RIGIDITY`, `NO-NOVELTY-CLAIM`

## Claim

AF-161 and AF-162 isolate two opposite regimes for repeated finite experiments. If the hidden alternative may be chosen independently at every coordinate, the barycentric domination radius tensorizes and grows exponentially. If one hidden alternative is shared across all coordinates, the same radius remains uniformly bounded and its convex-hull penalty vanishes asymptotically.

There is an exact interpolation between those extremes. The relevant complexity is controlled by the number of **independently recombinable provenance blocks**, not by the number of observations inside those blocks.

Let

\[
\mathcal E=(P_i)_{i=1}^m
\]

be a finite statistical experiment on a finite sample space `X`, with duplicate laws removed, so `m>=2` and the `P_i` are pairwise distinct. For `r>=1`, write

\[
\mathcal E^{\Delta r}
:=
(P_i^{\otimes r})_{i=1}^m
\]

for AF-162's shared-identity `r`-fold experiment, and denote its Shtarkov mass, barycentric domination radius, and convex-hull penalty by

\[
C_r,\qquad \Lambda_r,\qquad
G_r=\frac{\Lambda_r}{C_r}=e^{d_r}.
\tag{1}
\]

Now let `Pi={B_1,...,B_k}` be a partition of `{1,...,n}` into nonempty blocks with sizes `r_j=|B_j|`. Define the **blockwise-provenance experiment** by requiring one common alternative label inside each block while allowing labels to be chosen independently between blocks:

\[
\mathcal E^{\Pi}
:=
\left(
\bigotimes_{j=1}^k P_{i_j}^{\otimes r_j}
\right)_{(i_1,\ldots,i_k)\in[m]^k}.
\tag{2}
\]

Then

\[
\mathcal E^{\Pi}
=
\bigotimes_{j=1}^k \mathcal E^{\Delta r_j}
\tag{3}
\]

as a finite experiment, so AF-161 gives the exact factorization

\[
\boxed{
C(\mathcal E^{\Pi})=\prod_{j=1}^k C_{r_j},
\qquad
\Lambda_{\rm bar}(\mathcal E^{\Pi})=\prod_{j=1}^k\Lambda_{r_j},
}
\tag{4}
\]

and therefore

\[
\boxed{
G_{\rm hull}(\mathcal E^{\Pi})=\prod_{j=1}^kG_{r_j},
\qquad
d_{\rm hull}(\mathcal E^{\Pi})=\sum_{j=1}^k d_{r_j}.
}
\tag{5}
\]

AF-162 supplies a uniform upper bound `Lambda_r<=m` and proves `Lambda_r->m`. Since every diagonal experiment remains nontrivial, AF-161's equality criterion also gives `Lambda_r>1` for every `r`. Consequently

\[
\lambda_*(\mathcal E)
:=
\inf_{r\ge1}\Lambda_r
>1.
\tag{6}
\]

Hence every provenance partition satisfies

\[
\boxed{
\lambda_*^k
\le
\Lambda_{\rm bar}(\mathcal E^{\Pi})
\le
m^k.
}
\tag{7}
\]

This gives an exact scalability criterion for the whole class of partition-provenance models:

\[
\boxed{
\sup_N\Lambda_{\rm bar}(\mathcal E^{\Pi_N})<\infty
\iff
\sup_N |\Pi_N|<\infty.
}
\tag{8}
\]

Thus arbitrarily many observations are harmless for this recovery-calibration complexity when they are covered by only finitely many coherent provenance identities. Conversely, even very long coherent blocks cannot prevent divergence if the number of independently recombinable identities tends to infinity.

There is a second separation. Let

\[
a_*:=\max_{i<j}\sum_x\sqrt{P_i(x)P_j(x)}<1,
\qquad
q:=\frac{m-1}{2}.
\tag{9}
\]

AF-162 gives, whenever `q a_*^r<1`,

\[
0\le d_r
\le
-\log(1-q a_*^r).
\tag{10}
\]

Therefore for a sequence of partitions `Pi_N`, if

\[
\sum_{B\in\Pi_N}a_*^{|B|}\longrightarrow0,
\tag{11}
\]

then

\[
\boxed{
d_{\rm hull}(\mathcal E^{\Pi_N})\longrightarrow0,
\qquad
G_{\rm hull}(\mathcal E^{\Pi_N})\longrightarrow1.
}
\tag{12}
\]

Condition `(11)` may hold even while `|Pi_N|->infinity`. In that regime the extra convex-hull mismatch vanishes, yet `(7)` forces the total barycentric domination radius to diverge. The two source-complexity axes from AF-160 are therefore genuinely distinct at growing scale: **reference mismatch can disappear while alternative-provenance complexity still explodes**.

The endpoints recover the previous results exactly. One block gives AF-162's global shared identity; singleton blocks give AF-161's full Cartesian tensor power.

## Derivation

### A provenance partition is a tensor product of diagonal experiments

For a fixed block `B_j` of size `r_j`, the admissible laws on that block are exactly

\[
(P_i^{\otimes r_j})_{i=1}^m
=
\mathcal E^{\Delta r_j}.
\]

Independence of the labels between distinct blocks means that every tuple `(i_1,...,i_k)` is admissible. Hence the family in `(2)` is literally the full Cartesian product of the `k` diagonal block experiments, proving `(3)`.

AF-161 applies to arbitrary finite product experiments and proves exact multiplicativity of `C`, `Lambda_bar`, and `G_hull`, including against correlated barycentric mixtures of the product labels. Iterating that theorem gives `(4)` and `(5)`. No extra independence assumption is hidden in the optimization over recovery references: arbitrary mixtures over the full block-label tuple are already included in AF-161's convex hull.

### The diagonal block radius is uniformly separated from one

For every `r>=1`, pairwise distinctness of the base laws implies pairwise distinctness of their tensor powers. Thus `E^{Delta r}` is nontrivial. AF-161 proves for every finite experiment

\[
\Lambda_{\rm bar}=1
\iff
\text{all member laws coincide},
\]

so

\[
\Lambda_r>1
\qquad\forall r.
\tag{13}
\]

AF-162 further proves

\[
\Lambda_r\longrightarrow m>1.
\tag{14}
\]

Choose `R` such that `Lambda_r>(m+1)/2>1` for every `r>=R`. The finite set `Lambda_1,...,Lambda_{R-1}` has minimum strictly greater than one by `(13)`. Therefore

\[
\lambda_*
\ge
\min\left\{
\Lambda_1,\ldots,\Lambda_{R-1},\frac{m+1}{2}
\right\}>1,
\]

which proves `(6)`.

Applying `lambda_*<=Lambda_{r_j}<=m` to every factor in `(4)` proves `(7)`. If the block count is bounded by `K`, then `Lambda_bar<=m^K`; if the block count tends through an unbounded subsequence, `Lambda_bar>=lambda_*^k` diverges along that subsequence. This proves `(8)`.

### Long coherent blocks erase hull mismatch but not provenance count

AF-162 proves `(10)` for sufficiently large `r`. Under `(11)`, the largest value `a_*^{|B|}` among blocks must also tend to zero, so every block eventually lies in the positive-denominator regime of `(10)`. Since

\[
-\log(1-u)\le 2u
\]

for all sufficiently small `u>=0`, equations `(5)` and `(10)` give eventually

\[
0\le d_{\rm hull}(\mathcal E^{\Pi_N})
\le
2q\sum_{B\in\Pi_N}a_*^{|B|}
\longrightarrow0.
\tag{15}
\]

Exponentiating proves `(12)`.

This is not in tension with `(7)`. `G_hull=Lambda_bar/C` measures only the extra penalty for forcing the reference into the experiment convex hull. When every coherent block is long, repeated observations identify its fixed label well enough that its Shtarkov center approaches that hull. But if there are more and more independently chosen block labels, the source family itself still contains `m^k` combinatorial alternatives, and the total domination radius retains a block-count cost.

## Matched-control stress tests

### Same observation count, different provenance partition

Fix total length `n`. The one-block partition has

\[
\Lambda_{\rm bar}(\mathcal E^{\Delta n})\le m,
\]

whereas the singleton partition is AF-161's full Cartesian power and has

\[
\Lambda_{\rm bar}(\mathcal E^{\otimes n})
=
\Lambda_{\rm bar}(\mathcal E)^n.
\]

The local channel and total number of observations are identical. Only the admissible label-provenance relation differs. This rules out explanations based solely on sample count, local distinguishability, or repeated observation.

### Long blocks with growing recombination count

Take `k_N->infinity` blocks whose minimum block size also tends to infinity fast enough that

\[
k_N a_*^{\min_j r_{N,j}}\to0.
\]

Then `(11)` holds, hence `G_hull->1`, while `(7)` gives

\[
\Lambda_{\rm bar}\ge\lambda_*^{k_N}\to\infty.
\]

This directly falsifies the idea that asymptotic proximity of the Shtarkov center to the recoverable convex hull is by itself enough for scalable whole-family recovery calibration.

## Arithmetic/analytic stress test

AF-157--AF-162 use the two-member finite family derived from the local `p=2` Euler-factor construction,

\[
P_1=\left(\frac47,\frac27,\frac17\right),
\qquad
P_2=\left(\frac{16}{21},\frac4{21},\frac1{21}\right),
\]

with Hellinger affinity

\[
a=\frac{9+2\sqrt2}{7\sqrt3}<1.
\tag{16}
\]

For a provenance partition with block sizes `r_1,...,r_k`, AF-162 and `(4)` give

\[
\prod_{j=1}^k(2-a^{r_j})
\le
C(\mathcal E^\Pi)
\le
\Lambda_{\rm bar}(\mathcal E^\Pi)
\le
2^k.
\tag{17}
\]

Moreover `Lambda_bar` is uniformly bounded over any growing family of such partitions exactly when `k` is uniformly bounded. If `sum_j a^{r_j}->0`, then the hull penalty tends to one even if `k->infinity`; the total radius nevertheless diverges by `(7)`.

This is deliberately only a local arithmetic-derived model. It does not assert that rational primes, Euler factors, or any RH-facing construction actually carry a piecewise-constant hidden label. Its role is to make the provenance question falsifiable: a proposed global arithmetic compression must specify which local alternatives are independently recombinable and which are tied by a common source identity before importing a local recovery modulus.

## Prior-art and novelty audit

No novelty is claimed for the product, change-point, coding, or hypothesis-testing ingredients.

- Yu. M. Shtarkov, **“Universal Sequential Coding of Single Messages,”** *Problems of Information Transmission* 23(3), 175–186 (English translation, 1987), is the classical normalized-maximum-likelihood/minimax-regret source behind the Shtarkov mass used throughout AF-149--AF-162.
- Neri Merhav, **“On the Minimum Description Length Principle for Sources with Piecewise Constant Parameters,”** *IEEE Transactions on Information Theory* 39(6), 1962–1967 (1993), DOI `10.1109/18.265504`, studies universal coding when a source parameter is shared within segments and may change at finitely many transition points. It is direct prior art for treating blockwise parameter provenance/change points as a classical source-model distinction rather than a new idea of this line.
- The Bhattacharyya/Hellinger and Chernoff literature cited in AF-162 supplies the classical exponential distinguishability of fixed product alternatives used in the diagonal-block bounds.

A targeted literature check found established universal-coding/MDL work for piecewise stationary or piecewise constant parameter sources, so the partition model itself is classical. The exact formulas `(4)--(5)` are immediate applications of AF-161 to AF-162's diagonal block experiments, and `(7)--(12)` are consequences of those already-persisted bounds. The durable contribution here is therefore not a novelty claim but a **sharpened internal classification**: within this recovery-calibration framework, the number of independently recombinable provenance identities is the exact boundedness gate, while convex-hull reference mismatch is a separate quantity that can vanish independently.

## Boundaries and counterarguments

1. **A partition is only one provenance model.** Overlapping constraints, hierarchical labels, Markov label evolution, global algebraic compatibility, or non-product source laws are not represented by `(2)`. They require their own composition law rather than being forced into a partition.

2. **The criterion is for `Lambda_bar`, not every notion of recovery.** Equation `(8)` classifies the source constant used by AF-159's barycentric Pearson-to-optimal-deficiency calibration. It does not prove that another destination-relative witness class or another loss must pay the same block-count cost.

3. **Fixed finite base family is essential.** The uniform gap `lambda_*>1` uses one fixed finite nontrivial experiment. Growing, merging, or asymptotically indistinguishable alternative families require a separate analysis.

4. **Block coherence must be intrinsic.** Declaring a partition by hand does not establish arithmetic provenance. A genuine arithmetic application must derive the compatibility relation from the source construction and show that matched controls obey the same admissibility rules.

5. **Vanishing hull mismatch is weaker than bounded total complexity.** Equation `(12)` should not be interpreted as whole-family recoverability becoming trivial. It says only that the unrestricted Shtarkov center becomes asymptotically approximable by a recoverable barycentric center at the relevant directed `D_infinity` scale.

6. **No RH consequence is established.** The theorem identifies an exact local-to-global gate for one abstract recovery framework. It does not show that an RH-facing representation has bounded provenance block count or that such a bound would suffice for zero selection.

## Consequence for the line

AF-161 identified an exponential obstruction under free Cartesian recombination; AF-162 showed that one globally shared identity removes it. AF-163 closes the elementary interpolation between them: **for a fixed finite source family with blockwise shared identity, scalable whole-family calibration is equivalent to a uniform bound on the number of independently recombinable provenance blocks.**

This sharpens the next arithmetic question. Before asking whether a local fidelity estimate survives a global limit, identify the source's actual provenance relation and count its independent recombination degrees of freedom. If that relation is more structured than a partition, the next useful theorem is not another generic tensor bound but the corresponding complexity law for that intrinsic compatibility structure.