# AF-123 — Almost-sure fiberwise Lipschitz recovery preserves conditional information dimension

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-INGREDIENTS`, `CATEGORY-INDEXED`, `MULTISCALE-FIDELITY`, `NO-NOVELTY-CLAIM`

## Claim

AF-121 proved conditional-information-dimension monotonicity under one Lipschitz constant valid uniformly over the retained base `Y`, while AF-122 upgraded a uniform modulus to a scale-by-scale quantization-profile inequality. The uniformity requirement is stronger than necessary for the **first-order information-dimension conclusion**.

Let `Y` be arbitrary retained side information taking values in a standard Borel space, let

\[
M\in[0,1)^r,
\qquad
D\in[0,1)^q,
\]

and assume exact recovery

\[
D=R(Y,M)
\qquad\text{almost surely}.
\tag{1}
\]

Suppose there exists a measurable finite envelope

\[
L:Y\to[1,\infty)
\tag{2}
\]

such that for almost every `y`,

\[
\|R_y(m)-R_y(m')\|_\infty
\le
L(y)\,\|m-m'\|_2,
\qquad
R_y(m):=R(y,m),
\tag{3}
\]

on the relevant mark domain. No essential supremum or moment bound on `L(Y)` is assumed.

For dyadic quantization

\[
Q_k(X):=\lfloor 2^kX\rfloor
\tag{4}
\]

coordinatewise, write

\[
E_X(k\mid Y):=H_2(Q_k(X)\mid Y).
\tag{5}
\]

Define the random scale overhead

\[
A(Y):=
\left\lceil
\log_2^+\!\bigl(L(Y)\sqrt r\bigr)
\right\rceil.
\tag{6}
\]

Then two levels of fidelity follow.

### 1. Finite logarithmic Lipschitz budget gives a bounded profile defect

If

\[
\mathbb E[A(Y)]<\infty,
\tag{7}
\]

then for every `k>=0`,

\[
\boxed{
E_D(k\mid Y)
\le
E_M(k\mid Y)
+r\,\mathbb E[A(Y)]
+q.
}
\tag{8}
\]

Thus an unbounded family of fiberwise Lipschitz constants is harmless for the whole dyadic entropy profile provided its **logarithmic scale overhead is integrable**.

### 2. Almost-sure finite fiberwise Lipschitz constants already preserve information dimension

Even without `(7)`, the mere assumption

\[
A(Y)<\infty
\qquad\text{almost surely}
\tag{9}
\]

implies

\[
\boxed{
\underline d(D\mid Y)
\le
\underline d(M\mid Y),
\qquad
\overline d(D\mid Y)
\le
\overline d(M\mid Y).
}
\tag{10}
\]

Consequently, AF-121's uniform Lipschitz constant is sufficient but **not necessary** for its conditional-information-dimension lower bound. What uniformity buys is a scale-independent profile bound directly at the same quantization scale. For first-order dimension, arbitrarily large but almost-surely finite fiber constants can be discarded on a vanishing tail of retained states.

## Derivation

### Variable-depth fiber quantization

Fix `y` and abbreviate `a=A(y)`. A cell of `Q_{k+a}(M)` has Euclidean diameter at most

\[
\sqrt r\,2^{-(k+a)}.
\tag{11}
\]

By `(3)` and the definition of `a`, its image under `R_y` has `\ell_\infty` diameter at most `2^{-k}`. Therefore that image intersects at most two dyadic `D`-cells per coordinate, hence at most `2^q` cells of `Q_k(D)`. Exact recovery `(1)` gives

\[
H_2\!\left(
Q_k(D)
\mid
Y=y,Q_{k+a}(M)
\right)
\le q.
\tag{12}
\]

By the chain rule,

\[
H_2(Q_k(D)\mid Y=y)
\le
H_2(Q_{k+a}(M)\mid Y=y)+q.
\tag{13}
\]

A depth-`k+a` dyadic cell refines a depth-`k` mark cell into at most `2^{ra}` children, so

\[
H_2(Q_{k+a}(M)\mid Y=y)
\le
H_2(Q_k(M)\mid Y=y)+ra.
\tag{14}
\]

Integrating `(13)`--`(14)` over `Y` proves `(8)` whenever `E[A]<infinity`.

### Tail truncation removes every moment assumption at dimension scale

For an integer `t>=0`, split retained states into

\[
G_t=\{A\le t\},
\qquad
B_t=\{A>t\}.
\tag{15}
\]

On `G_t`, the fixed finer mark quantizer `Q_{k+t}(M)` is at least as fine as the fiber-required quantizer, so `(12)`--`(13)` give the same `q`-bit residual bound. On `B_t`, use only the trivial fact that `Q_k(D)` has at most `2^{qk}` labels. Averaging the two cases yields

\[
E_D(k\mid Y)
\le
E_M(k+t\mid Y)
+q
+qk\,\Pr(A>t).
\tag{16}
\]

Dyadic refinement of the bounded `r`-dimensional mark gives

\[
E_M(k+t\mid Y)
\le
E_M(k\mid Y)+rt,
\tag{17}
\]

hence

\[
\boxed{
E_D(k\mid Y)
\le
E_M(k\mid Y)
+rt+q
+qk\,\Pr(A>t).
}
\tag{18}
\]

Choose any integer sequence `t_k` with

\[
t_k\to\infty,
\qquad
t_k=o(k),
\tag{19}
\]

for example `t_k=floor(sqrt(k))`. Since `A<infinity` almost surely,

\[
\Pr(A>t_k)\to0.
\tag{20}
\]

After dividing `(18)` by `k`, every term except `E_M(k|Y)/k` vanishes. Taking `liminf` and `limsup` proves `(10)`.

## Sharpness and falsification controls

### Finite mean logarithmic overhead is a profile condition, not a dimension condition

The distinction between `(8)` and `(10)` is essential. If `E[A]=infinity`, one cannot infer a uniform additive profile defect from the argument: rare retained states may require arbitrarily many extra mark bits before a target scale is resolved. Nevertheless those states have probability tending to zero after any diverging truncation threshold, so they disappear after normalization by `k`.

Thus the natural hierarchy is:

- uniform Lipschitz constant: same-scale profile control with a deterministic `O(1)` defect;
- integrable random log-Lipschitz overhead: same-scale profile control with an averaged `O(1)` defect;
- almost-sure finite random Lipschitz overhead: first-order information-dimension monotonicity, with only an `o(k)` tail-controlled defect guaranteed.

### Mere measurability still fails

The digit-interleaving control from AF-121 remains decisive. With constant `Y`, a measurable almost-everywhere bijection can recover a two-dimensional uniform discriminator from one scalar uniform mark, giving `d(D)=2` and `d(M)=1`. Such a decoder has no finite Lipschitz constant on the relevant fiber. Therefore `(10)` does not restore a category-free dimension law; it identifies a strictly broader regular category than AF-121's uniformly Lipschitz one.

### Conditioning on the retained base is load-bearing

The tail argument works because the large local constant `L(y)` is indexed by information already present in `Y`, and conditional entropy averages fiberwise costs after `Y` is known. If the decoder's local scale distortion depends on hidden mark-level state rather than retained side information, it cannot be discarded by the same `Y`-tail truncation. This theorem therefore does not justify replacing an uncontrolled decoder by a random Lipschitz constant unless that constant is genuinely a retained-base-measurable envelope.

### The logarithmic budget is sufficient, not claimed necessary

`E[A]<infinity` is a clean sufficient condition for the bounded-defect profile inequality `(8)`. No converse is claimed. Special source/decoder structure may yield a bounded profile defect even when this coarse Lipschitz-envelope expectation diverges.

## Prior-art audit

The underlying monotonicity of information dimension under Lipschitz maps and its operational role in regular analog recovery are classical. **No standalone novelty claim is made for those ingredients or for the elementary truncation argument.**

- Alfréd Rényi, **“On the Dimension and Entropy of Probability Distributions,”** *Acta Mathematica Academiae Scientiarum Hungaricae* 10, 193–215 (1959), DOI `10.1007/BF02063299`. Role: foundational quantization-entropy definition of information dimension.
- Yihong Wu and Sergio Verdú, **“Rényi Information Dimension: Fundamental Limits of Almost Lossless Analog Compression,”** *IEEE Transactions on Information Theory* 56(8), 3721–3748 (2010), DOI `10.1109/TIT.2010.2050803`. Role: direct prior art for information dimension as the dimensional resource governing analog compression under regularity constraints, including Lipschitz decompression.
- Bernhard C. Geiger and Tobias Koch, **“On the Information Dimension of Stochastic Processes,”** *IEEE Transactions on Information Theory* 65(10), 6496–6518 (2019), DOI `10.1109/TIT.2019.2922186`. Role: modern information-dimension-rate and rate-distortion-dimension framework adjacent to the conditional fine-quantization viewpoint used here.
- Mohammad-Amin Charusaie, Arash Amini, and Stefano Rini, **“Compressibility Measures for Affinely Singular Random Vectors,”** *IEEE Transactions on Information Theory* 68(9), 6245–6275 (2022), DOI `10.1109/TIT.2022.3174623`. Role: modern direct evidence that Lipschitz transformations and information-dimension bounds remain an active classical compressibility framework beyond the original scalar/memoryless setting.

The specific retained-base-dependent extension `(8)`--`(10)` was not located as a named theorem in the searched literature. It should nevertheless be treated conservatively as a **derived conditional specialization of classical Lipschitz information-dimension machinery**, not as a novelty claim.

## Relationship to AF-121 and AF-122

AF-121 used a single global `L` to obtain a same-scale entropy inequality and then conditional-information-dimension monotonicity. AF-123 supplies the quantitative replacement requested by AF-121's nonuniform-fiber caveat: a retained-state-dependent Lipschitz envelope can be unbounded, and even have infinite logarithmic mean, without breaking the first-order dimension inequality.

AF-122 remains strictly stronger at the multiscale level when a common modulus exists. AF-123 shows why **profile fidelity and dimension fidelity have different regularity thresholds**. A common modulus controls every retained state at every scale; a random finite fiber constant only needs its extreme tail to vanish when one passes to the normalized asymptotic slope.

## Consequences for the research line

The admissible recovery category can now be widened without losing the AF-121 dimension obstruction. In a concrete compression problem, it is unnecessary to prove a uniform Lipschitz constant across all retained states merely to conclude that positive conditional information dimension cannot be reconstructed from a lower-dimensional mark. It is enough to exhibit a finite `Y`-measurable fiberwise Lipschitz envelope almost surely.

Conversely, applications that need **finite-scale or sublinear-profile** fidelity must continue to account for the tail of that envelope through `(18)` rather than citing information dimension alone. This separates two resources that had been conflated by the uniform hypothesis: regularity on typical retained fibers controls first-order dimension, while the distribution of rare high-distortion fibers controls finer profile fidelity.