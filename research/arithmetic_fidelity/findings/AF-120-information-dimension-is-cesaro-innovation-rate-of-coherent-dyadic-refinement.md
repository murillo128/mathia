# AF-120 — Rényi information dimension is the Cesàro innovation rate of coherent dyadic refinement

**Status:** `CLASSICAL-IDENTITY`, `LITERATURE+DERIVED`, `EXACT-DERIVED`, `COHERENT-MULTISCALE-ENTROPY`, `INFORMATION-DIMENSION`, `GROWTH-RATE-CLASSIFICATION`, `NO-NOVELTY-CLAIM`

## Claim

AF-119 proves a sharp zeroth-order gate for an exactly generating coherent quantizer hierarchy: uniformly bounded cumulative Shannon entropy is possible exactly for a finite-entropy atomic terminal factor. Once that cumulative entropy is unbounded, the next question is how rapidly new information must be inserted as resolution increases.

For the canonical dyadic refinement of a Euclidean-valued source, the first-order answer is classical Rényi information dimension, and it has an exact Arithmetic Fidelity interpretation as the **long-run average conditional innovation per refinement octave**.

Let

\[
X\in[0,1)^q
\]

be a Borel random vector. For `m>=0`, define the componentwise dyadic quantizer

\[
Z_m:=\lfloor 2^m X\rfloor
\in\{0,1,\ldots,2^m-1\}^q.
\tag{1}
\]

The hierarchy is coherent: `Z_{m-1}` is a deterministic function of `Z_m`. Put

\[
J_m:=H_2(Z_m\mid Z_{m-1}),\qquad m\ge1,
\tag{2}
\]

where entropy is in bits. Since `Z_0=0` almost surely,

\[
\boxed{
H_2(Z_m)=\sum_{k=1}^m J_k.
}
\tag{3}
\]

Every dyadic parent cell has at most `2^q` children, so

\[
\boxed{0\le J_m\le q.}
\tag{4}
\]

Rényi's lower and upper information dimensions may be computed on the exponential quantization subsequence `2^m`. Therefore

\[
\boxed{
\underline d(X)
=
\liminf_{m\to\infty}\frac{H_2(Z_m)}{m}
=
\liminf_{m\to\infty}\frac1m\sum_{k=1}^mJ_k,
}
\tag{5}
\]

and

\[
\boxed{
\overline d(X)
=
\limsup_{m\to\infty}\frac{H_2(Z_m)}{m}
=
\limsup_{m\to\infty}\frac1m\sum_{k=1}^mJ_k.
}
\tag{6}
\]

If the information dimension exists, `d(X)=delta`, then

\[
\boxed{
\frac1m\sum_{k=1}^mJ_k\longrightarrow\delta.
}
\tag{7}
\]

Thus `d(X)` is not merely a geometric label attached to the source. For this source-forced coherent filtration it is exactly the asymptotic **Cesàro density of new Shannon information** inserted by one more dyadic scale.

The qualification “Cesàro” is essential. Existence of `d(X)` alone does **not** imply

\[
J_m\to d(X).
\tag{8}
\]

The individual scale innovations may oscillate while their averages converge. Pointwise convergence of `J_m` requires stronger entropy-asymptotic control than information dimension by itself.

## Derivation

### Coherence turns entropy growth into accumulated innovations

Because

\[
Z_{m-1}=\left\lfloor\frac{Z_m}{2}\right\rfloor
\tag{9}
\]

componentwise, the chain rule gives

\[
H_2(Z_m)
=H_2(Z_{m-1})+H_2(Z_m\mid Z_{m-1}).
\tag{10}
\]

Iteration from `Z_0=0` proves `(3)`.

Conditional on one value of `Z_{m-1}`, the next quantizer can only select one of the `2^q` dyadic subcells. Hence its conditional entropy is at most `q` bits, proving `(4)`.

### Rényi's normalization is exactly the octave-average innovation

For a real or Euclidean random vector, Rényi information dimension is defined from the growth of fine uniform-quantization entropy divided by the logarithm of the quantization resolution. Wu and Verdú's Proposition 2 records the classical fact that the lower and upper dimensions can be computed by restricting the resolution to an exponential subsequence. With base-two entropy and resolution `2^m`, the normalization denominator is exactly `m`.

Substituting `(3)` into that exponential-subsequence characterization gives `(5)` and `(6)` directly. No additional asymptotic approximation is involved.

Wu and Verdú also identify information dimension with the entropy rate of the binary/dyadic expansion. Equations `(3)`--`(7)` are the same classical statement written in the conditional-innovation language natural for AF-119's coherent refinement tower.

## The AF-119 finite/infinite gate and information dimension are different layers

Information dimension refines AF-119, but it does not replace it.

AF-119 asks whether the total exact coherent information budget

\[
\sup_m H_2(Z_m)
\tag{11}
\]

is finite. Information dimension asks for the coefficient of its possible linear growth in the number of resolution octaves:

\[
H_2(Z_m)=\delta m+o(m)
\tag{12}
\]

when the dimension exists.

Consequently, `d(X)=0` does **not** imply a bounded exact information budget. It only says that any divergence is sublinear at first order.

A concrete matched control is a bounded countably atomic variable with infinite Shannon entropy. For example, place distinct atoms at

\[
x_j=2^{-j},\qquad j\ge2,
\tag{13}
\]

with normalized masses of order

\[
p_j\asymp \frac1{j(\log j)^2}.
\tag{14}
\]

Then

\[
H_2(p)=\infty.
\tag{15}
\]

The dyadic hierarchy eventually separates every atom, so AF-119 gives

\[
H_2(Z_m)\uparrow\infty.
\tag{16}
\]

But a discrete bounded random variable has Rényi information dimension zero, hence

\[
\frac{H_2(Z_m)}m\to0.
\tag{17}
\]

This is a decisive boundary: **zero information dimension includes both finite-total-cost exact marks and unbounded but sublinear-cost exact marks**. A single dimension number cannot distinguish them.

## Calibration regimes

The classical examples show that coherent refinement cost has several genuinely different asymptotic regimes.

### Finite-entropy atomic source

AF-119 gives

\[
H_2(Z_m)\to H_2(X)<\infty.
\tag{18}
\]

Therefore `d(X)=0`. The cumulative innovation sum is finite.

### Infinite-entropy discrete source

The preceding control has

\[
H_2(Z_m)\to\infty,
\qquad
\frac{H_2(Z_m)}m\to0.
\tag{19}
\]

The exact mark needs unbounded information, but its average cost per additional octave vanishes.

### Absolutely continuous source

For an absolutely continuous one-dimensional source satisfying the usual finiteness condition, Rényi's theorem gives

\[
d(X)=1.
\tag{20}
\]

For a full-dimensional absolutely continuous source in `R^q`, the corresponding value is `q`. Thus a fine dyadic description asymptotically inserts the full ambient number of bits per octave.

### Discrete-continuous mixture

If in one dimension

\[
\mu=(1-\rho)\mu_d+\rho\mu_c,
\qquad 0\le\rho\le1,
\tag{21}
\]

with discrete and absolutely continuous components under the standard finite coarse-entropy hypothesis, Rényi's mixture theorem gives

\[
\boxed{d(X)=\rho.}
\tag{22}
\]

Hence the coherent dyadic tower pays asymptotically `rho` new bits per octave on average. Nonatomicity therefore does not force the full ambient rate.

### Singular and scale-irregular sources

Self-similar singular measures can have fractional information dimension. More generally, lower and upper information dimensions can differ, in which case the average refinement innovation has no single asymptotic density:

\[
\liminf_m\frac1m\sum_{k\le m}J_k
<
\limsup_m\frac1m\sum_{k\le m}J_k.
\tag{23}
\]

These are important controls against interpreting “continuous”, “singular”, or “nonatomic” as a complete quantitative cost classification.

## Arithmetic Fidelity interpretation

AF-116--AF-118 separate pointwise tolerance complexity from the information cost of one coherent exact mark. AF-119 then proves that an exact coherent tower for a genuinely nonatomic terminal factor cannot have bounded cumulative entropy.

The present finding supplies the next exact layer for Euclidean multiscale provenance:

\[
\boxed{
\text{cumulative exact cost}
\quad\rightsquigarrow\quad
\text{first-order cost per refinement octave}.
}
\tag{24}
\]

The relevant invariant is not the number of coordinates in a continuous side mark and not the cardinality of its range. It is the entropy growth of the **declared coherent finite-resolution observations**. A one-real-number mark may therefore carry a nonzero asymptotic refinement rate even though its coordinate count is one.

This gives a practical audit for proposed repairs of a lossy compression. If the retained prime-specific provenance is represented by an intrinsically justified Euclidean factor and the claimed repair resolves that factor through a nested dyadic-equivalent filtration, then positive information dimension certifies an unavoidable linear-in-resolution information budget for that particular coherent representation.

This is not yet a general minimal-lift theorem. It does not prove that every admissible alternative representation must pay the same rate. Such a conclusion requires a category restriction—typically regularity, metric fidelity, Lipschitz/bi-Lipschitz admissibility, or an independent coding theorem—showing that the proposed alternative cannot hide the discriminator behind an irregular re-encoding.

## Falsification and boundary tests

### 1. The metric/coordinate structure must be intrinsic enough to matter

Information dimension is a fine-scale metric notion. An arbitrary Borel bijection can radically change geometric quantization complexity while preserving set-theoretic recoverability. Therefore `(5)`--`(7)` are not a category-free lower bound on all possible lifts.

An application must justify why the dyadic filtration, or an equivalent regular family of shrinking cells, belongs to the admissible observable category.

### 2. Independently optimized tolerance codebooks still do not qualify

The identity uses one nested filtration. A fresh optimal codebook chosen separately at every tolerance need not refine the previous one and cannot be assigned the conditional innovations `(2)` without an additional coherence theorem. AF-118's warning remains intact.

### 3. Zero dimension does not mean finite repair

The infinite-entropy discrete control `(13)`--`(17)` kills that inference exactly. Information dimension only detects the linear coefficient of fine-scale entropy growth; logarithmic, iterated-logarithmic, or other sublinear divergence can survive below it.

### 4. Dimension need not have a limit

When lower and upper information dimensions differ, there is no single asymptotic average innovation rate. Any application quoting one scalar dimension must establish existence rather than silently replacing a liminf/limsup pair by a limit.

### 5. Average innovation does not imply scale-by-scale innovation

Even when `d(X)` exists, `(7)` is a Cesàro statement. A theorem requiring every sufficiently fine scale to contribute approximately `d(X)` bits needs stronger regularity or entropy asymptotics.

### 6. Ambient continuity is not the discriminator

The correct source is the terminal factor that actually has to survive the compression. A continuous ambient carrier can contain a discrete prime-specific factor of zero information dimension, while a seemingly small continuous provenance variable can have positive information dimension. The audit must be applied to the claimed retained discriminator, not to irrelevant ambient coordinates.

## Prior art and novelty assessment

The central mathematics is classical, and **no standalone theorem-level novelty is claimed**.

- Alfréd Rényi, **“On the Dimension and Entropy of Probability Distributions,”** *Acta Mathematica Academiae Scientiarum Hungaricae* 10, 193–215 (1959), DOI `10.1007/BF02063299`. Role: original definition of lower/upper information dimension through fine quantization entropy, its Euclidean extension, and the classical discrete/continuous/mixed dimension results.
- Yihong Wu and Sergio Verdú, **“Rényi Information Dimension: Fundamental Limits of Almost Lossless Analog Compression,”** *IEEE Transactions on Information Theory* 56(8), 3721–3748 (2010), DOI `10.1109/TIT.2010.2050803`. Role: Proposition 2 permits computation on exponential quantization scales; Section III-D explicitly identifies information dimension with the entropy rate of the dyadic expansion; the paper also supplies discrete-continuous mixture and self-similar controls and an operational almost-lossless compression interpretation under regularity constraints.

The exact identity `(3)` is the ordinary Shannon chain rule on the nested dyadic partition. Combining it with the classical exponential-subsequence formula immediately yields `(5)`--`(7)`. The conditional-innovation wording is therefore an Arithmetic Fidelity reorganization of established theory, not a new theorem.

The substantive line-level consequence is the **two-tier refinement audit** that follows AF-119:

1. bounded cumulative coherent entropy is equivalent to finite-entropy atomicity of the terminal factor;
2. once cumulative entropy diverges, Rényi information dimension measures only its first-order linear density in resolution, and zero dimension still permits unbounded sublinear exact-description cost.

That second clause prevents a misleading escape from AF-119: replacing “infinite exact entropy” by “dimension zero” does not make a repair finite.

## Consequences for the research line

The immediate growth-rate frontier after AF-119 is therefore partly classicalized. For Euclidean source-forced refinements, do not invent a new scalar “multiscale fidelity rate” before checking Rényi information dimension and its rate-distortion/regular coding relatives.

The genuinely open Arithmetic Fidelity question is narrower: **under a declared admissible category of lifts, what lower bound on side-mark information dimension is forced by recoverability of a discriminator whose fine-scale structure has positive dimension?** A useful next result would have to connect a recovery map and the retained compression to a dimension inequality, or exhibit a matched control showing that no such inequality is possible without additional regularity.

For eventual prime applications, this means first identifying the exact prime-specific terminal factor and its admissible fine-scale geometry. Only then is it meaningful to ask whether a spectral, positive, quotient, or asymptotic compression can retain that factor with sublinear, linear, or bounded extra provenance cost.