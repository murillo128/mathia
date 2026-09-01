# WI-075 — Ambient scalar-lcm projection does not transfer incidence sparsity without a weighted-support theorem

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + PRIOR-ART-REDIRECTION`. This finding does **not** certify the Yang--Yang one-sided fourth-moment candidate and does not change Mathia's current unconditional simple-critical proportion.

The exact Yang common-lock geometry gives

\[
(h_1,h_2)=(rk,qk),\qquad (r,q)=1,
\qquad
L:=\operatorname{lcm}(|h_1|,|h_2|)=rq|k|.
\]

WI-071 showed that the resulting two-dimensional **ambient incidence family** is lcm-sparse: after aggregating all slopes it lies in an `O(X(log X)^2)` set inside an ambient shift square of area `\asymp X^2`. A tempting next step is to project each incidence to the scalar `L` and invoke a sparse-moduli large sieve.

The exact conclusion available from the algebra is narrower. On a fixed low reduced slope, the set of **candidate** scalar moduli can be dense: for `(b_1,b_2)=(2,4)` one has `(r,q)=(1,2)` and therefore candidate values `L=2|k|`; for equal reduced legs one has candidate values `L=|k|`. But the public Yang source does not attach nonzero weight to every algebraically allowed `k`. The `S1` swap requires nonzero von-Mangoldt weight on `m`, `m'=m-rk`, `n`, and `n'=n-qk`, together with the source-window constraints. Hence the effective weighted scalar support is only a subset of those progressions.

Therefore the ambient projection proves an **interface warning**, not a density theorem:

\[
\boxed{
\text{two-dimensional incidence sparsity alone does not imply}
\quad
\text{sparse effective scalar-modulus support}.
}
\]

Nor does it imply the opposite. A scalar sparse-large-sieve route remains live if one can prove that the actual nonzero weighted `L`-support (or its additive energy / weighted analogue) is sparse enough for the theorem being used. Conversely, one cannot justify such a route merely by reinterpreting the pair-count `O(X(log X)^2)` as a count of distinct scalar moduli. The missing mathematical input is a theorem about the **weighted support after projection**, not the identity `L=rq|k|` itself.

## 1. Exact source geometry and the effective support

The pinned public Yang reproduction source is

`JoshuaHKU/zeta-0.7947-reproduction@d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8`, especially `scripts/t2_swaps.py`.

For fixed prime-power legs `b_1,b_2`, write

\[
g=(b_1,b_2),\qquad r=b_1/g,\qquad q=b_2/g.
\tag{1}
\]

Then `(r,q)=1`, and the equal-lock change of variables is

\[
m'=m-rk,\qquad n'=n-qk.
\tag{2}
\]

Thus

\[
\boxed{
 h_1=rk,\qquad h_2=qk,
 \qquad
 \gcd(|h_1|,|h_2|)=|k|,
 \qquad
 L=rq|k|.
}
\tag{3}
\]

However, the `S1` loop in the pinned source skips `m` unless `Lambda(m)\ne0`, skips `m'` unless `Lambda(m')\ne0`, builds the inner `n`-window only from `Lambda(n)\ne0`, and contributes only when `Lambda(n')\ne0`. Ignoring harmless positive logarithmic weights, the support condition is therefore of the form

\[
\Lambda(m)\Lambda(m-rk)\Lambda(n)\Lambda(n-qk)\ne0
\tag{4}
\]

plus the moving-window and nonzero-offset restrictions.

For a fixed reduced slope `(r,q)`, define the effective index set abstractly by

\[
\mathcal K_{r,q}^{\rm eff}
=
\{k:\text{there exist admissible }m,n\text{ satisfying (4) and the source windows}\}.
\tag{5}
\]

The corresponding scalar support is

\[
\mathcal L_{r,q}^{\rm eff}
=
\{rq|k|:k\in\mathcal K_{r,q}^{\rm eff}\}.
\tag{6}
\]

Equation (3) gives only

\[
\boxed{
\mathcal L_{r,q}^{\rm eff}
\subseteq rq\,\mathbf N
}
\tag{7}
\]

with the appropriate finite range. It does **not** give a lower bound for the density or cardinality of `\mathcal K_{r,q}^{\rm eff}`.

That distinction is material for any sparse-modulus theorem, because zero-weight moduli may normally be omitted from the scalar modulus family before applying the inequality.

## 2. What the low-slope algebra does prove

For the explicit off-diagonal leg pair

\[
(b_1,b_2)=(2,4),
\]

one has `g=2`, `(r,q)=(1,2)`, and therefore

\[
(h_1,h_2)=(k,2k),\qquad L=2|k|.
\tag{8}
\]

If one forgets the von-Mangoldt/source weights and keeps every algebraically admissible integer `k`, the scalar projection is the even progression in the relevant interval. Likewise, for `r=q=1`, the ambient candidate projection is the full integer interval.

These examples establish a precise set-theoretic fact: **the projection map itself need not preserve the ambient sparsity of the two-dimensional incidence set.** A set of slope incidences can be thin in a two-dimensional box while its unlabelled scalar image is a positive-density arithmetic progression.

What they do not establish is

\[
\#\mathcal L_{1,2}^{\rm eff}\gg K
\quad\text{or}\quad
\#\mathcal L_{1,1}^{\rm eff}\gg K
\tag{9}
\]

for a source index range of length `K`. Any such statement would require additional arithmetic control of the four von-Mangoldt factors and the actual source windows. The algebraic parametrization is insufficient.

Thus the safe implication is

\[
\boxed{
\text{pair-incidence sparsity}
\not\Rightarrow
\text{scalar sparsity by projection alone},
}
\tag{10}
\]

not a claim that the effective weighted scalar support is dense.

## 3. Consequence for sparse scalar-modulus large sieves

Roger C. Baker, Marc Munsch and Igor E. Shparlinski, *Additive energy and a large sieve inequality for sparse sequences*, Mathematika 68 (2022), 362--399, DOI `10.1112/mtk.12140`, arXiv:2103.12659, prove large-sieve estimates for one-dimensional sparse scalar modulus sequences, with bounds driven by the arithmetic/additive-energy structure of the scalar sequence.

Karin Halupczok and Marc Munsch, *Large sieve estimate for multivariate polynomial moduli and applications*, Monatshefte fuer Mathematik 197 (2022), 463--478, arXiv:2110.13257, use several variables to generate scalar polynomial moduli. Neither theorem is, as printed, a black-box estimate for Yang's weighted two-dimensional common-`k` covariance.

The present source audit therefore leaves two logically distinct tasks.

First, the `O(X(log X)^2)` count from WI-071 cannot simply be substituted for the number of distinct scalar `L` values: it counts **incidences `(h_1,h_2)`**, and many incidences can project to the same scalar modulus while a fixed candidate slope can project onto a dense arithmetic progression.

Second, this does not rule out a sparse scalar route on the **effective weighted family**. To use one, an argument must establish an interface such as:

\[
\#\mathcal L^{\rm eff}(Z)\ll Z^{1-\delta}
\quad\text{or a suitable weighted/additive-energy substitute},
\tag{11}
\]

with the exact Yang weights and source windows, or prove an exact transform in which factorization/direction labels `(r,q)` remain visible and are handled at acceptable total cost.

The scalar large-sieve escape is therefore neither automatically available from WI-071 nor closed by the ambient low-slope examples. Its status depends on a new weighted-support or weighted-energy theorem.

## 4. Factorization labels remain a possible asset

For a fixed scalar value `L`, every reduced representation satisfies

\[
rq\mid L,\qquad k=L/(rq),
\tag{12}
\]

with `(r,q)=1` and, in the Yang source, each reduced factor equal to `1` or a prime power. Hence the number of reduced slope labels is at most polylogarithmic:

\[
\#\{(r,q):rq\mid L,\ (r,q)=1,\ r,q\text{ prime-power-or-1}\}
\le (1+\Omega(L))^2
=O((\log L)^2).
\tag{13}
\]

This is not a sparsity theorem for `\mathcal L^{\rm eff}`. It only shows why a scalar reorganization that **retains** the labels may still be analytically reasonable: the loss from reduced-slope multiplicity is not automatically power-sized. Common factors, coefficient weights, overlap geometry, prime-power multiplicities and cell restrictions remain additional bookkeeping.

## 5. Relation to the existing obstruction chain

WI-071 remains unchanged: it concerns the geometry/cardinality of the aggregated two-dimensional ambient shift family and proves lcm-sparsity there. WI-072 and WI-073 likewise address source-agnostic ambient localization losses and Cartesian pruning.

The present result fixes the exact boundary between those geometric statements and a scalar-modulus theorem:

\[
\boxed{
\begin{array}{ccl}
(h_1,h_2)\text{ incidence family} &:& \text{provably lcm-sparse in 2-D},\\
L=\operatorname{lcm}(|h_1|,|h_2|)\text{ candidate image} &:& \text{can be dense},\\
L\text{ with nonzero Yang weight} &:& \text{density presently unproved either way}.
\end{array}}
\tag{14}
\]

Accordingly, the live large-sieve targets are: a source-weighted two-dimensional incidence inequality; a scalar inequality for the actual effective weighted `L` family; or a labelled scalar transform that exploits (13). No one of these follows from ambient support counting alone.

## 6. Prior-art and novelty boundary

No novelty is claimed for gcd/lcm identities, divisor counting, sparse-modulus large-sieve theory, or the cited Baker--Munsch--Shparlinski and Halupczok--Munsch theorems. The exact Yang support condition is read directly from the pinned public source.

The durable Mathia deduction is the source-interface distinction in (14): the current exact geometry controls ambient incidences and their candidate scalar projection, but **does not determine the scalar support after the von-Mangoldt/source weights are imposed**. A structure-level audit of the existing `weil_inertia` corpus shows that WI-071--WI-073 do not supply that missing weighted-support theorem.

Primary references:

- Yang reproduction source: `JoshuaHKU/zeta-0.7947-reproduction@d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8`, especially `scripts/t2_swaps.py`.
- Roger C. Baker, Marc Munsch and Igor E. Shparlinski, *Additive energy and a large sieve inequality for sparse sequences*, Mathematika 68:2 (2022), 362--399, DOI `10.1112/mtk.12140`, arXiv:2103.12659.
- Karin Halupczok and Marc Munsch, *Large sieve estimate for multivariate polynomial moduli and applications*, Monatshefte fuer Mathematik 197 (2022), 463--478, arXiv:2110.13257.

## 7. Boundary conditions and decisive tests

1. **Recovering a positive-density obstruction requires arithmetic input.** To strengthen (8) into a statement about effective support, prove a lower bound such as (9) with the actual source windows and all four nonzero von-Mangoldt conditions. A first-moment count is not enough if many configurations concentrate on few `k`; distinct-index density needs an appropriate second-moment or multiplicity control.
2. **A sparse scalar route is falsifiable.** Specify the exact weighted scalar family produced by the Yang covariance and verify the hypotheses of the intended sparse-modulus theorem on that family. If its effective support/additive energy is sufficiently sparse, the scalar route survives despite the dense ambient candidate image.
3. **Labelled scalar transforms remain outside the obstruction.** An exact reorganization by `L` retaining `(r,q)` and source weights could exploit the polylogarithmic representation bound (13).
4. **Two-dimensional source-adapted large sieves remain outside the obstruction.** They may use incidence/directional sparsity directly without projecting to unlabelled scalar `L`.
5. **Cancellation can supersede support questions.** Exact cancellation in `S1-2S2+S3`, coefficient-cell cancellation, or another identity may make support cardinality irrelevant.

The decisive next question is therefore not whether the ambient formula `L=rq|k|` looks sparse or dense. It is whether the **effective Yang covariance after all source weights and windows are imposed** admits a scalar modulus description with a provably favorable support/energy bound, or whether retaining direction information is essential.