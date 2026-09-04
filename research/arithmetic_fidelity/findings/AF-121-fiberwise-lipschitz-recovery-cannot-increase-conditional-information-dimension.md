# AF-121 — Fiberwise Lipschitz recovery cannot increase conditional information dimension

**Status:** `LITERATURE+DERIVED`, `EXACT-DERIVED`, `CLASSICAL-COROLLARY`, `LIPSCHITZ-FIDELITY-BOUND`, `CATEGORY-INDEXED`, `NO-NOVELTY-CLAIM`

## Claim

AF-119 and AF-120 separate two exact-recovery regimes. A coherent exact mark has finite terminal Shannon entropy only for a finite-entropy atomic retained factor, while a continuously refined source can instead carry an asymptotic innovation rate measured by Rényi information dimension. The remaining question is whether exact recoverability forces a lower bound on the fine-scale complexity of a side mark once an admissible reconstruction category is declared.

There is a sharp answer for uniformly fiberwise Lipschitz recovery.

Let `Y` be arbitrary retained side information taking values in a standard Borel space. Let

\[
M\in[0,1)^r,
\qquad
D\in[0,1)^q
\]

be respectively an auxiliary side mark and the discriminator to be recovered. Assume that

\[
D=R(Y,M)
\qquad\text{almost surely},
\tag{1}
\]

where for almost every `y` the section

\[
R_y:m\longmapsto R(y,m)
\]

is `L`-Lipschitz in the Euclidean metric, with one finite constant `L` independent of `y`.

For an integer `n>=1`, write

\[
Q_n(X):=\lfloor nX\rfloor
\]

coordinatewise for the uniform quantizer cell label. Define lower and upper conditional information dimensions by

\[
\underline d(X\mid Y)
:=
\liminf_{n\to\infty}
\frac{H(Q_n(X)\mid Y)}{\log_2 n},
\qquad
\overline d(X\mid Y)
:=
\limsup_{n\to\infty}
\frac{H(Q_n(X)\mid Y)}{\log_2 n}.
\tag{2}
\]

Then

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
\tag{3}
\]

In particular, because a bounded `r`-coordinate mark satisfies

\[
\overline d(M\mid Y)\le r,
\tag{4}
\]

any exact uniformly fiberwise Lipschitz repair obeys the coordinate lower bound

\[
\boxed{
r\ge \overline d(D\mid Y).
}
\tag{5}
\]

When the conditional information dimensions exist as limits, this reads simply

\[
\boxed{
d(D\mid Y)\le d(M\mid Y)\le r.
}
\tag{6}
\]

Thus the retained output `Y` is free: the side mark is charged only for the fine-scale discriminator complexity that remains after conditioning on what the compression already retained.

A symmetric statement gives an exact invariance class. If, in addition,

\[
M=S(Y,D)
\qquad\text{almost surely}
\tag{7}
\]

and the sections `S_y` are uniformly Lipschitz, then

\[
\boxed{
\underline d(D\mid Y)=\underline d(M\mid Y),
\qquad
\overline d(D\mid Y)=\overline d(M\mid Y).
}
\tag{8}
\]

Conditional information dimension is therefore invariant under uniformly fiberwise bi-Lipschitz changes of the side coordinate over a fixed retained base.

## Derivation

### One mark cell reaches only finitely many discriminator cells

Fix `n`. Every `Q_n(M)` cell is a half-open cube of side `1/n` in `R^r`, hence has Euclidean diameter at most

\[
\frac{\sqrt r}{n}.
\tag{9}
\]

For almost every fixed `y`, the `L`-Lipschitz property of `R_y` implies that the image of such a cell has diameter at most

\[
\frac{L\sqrt r}{n}.
\tag{10}
\]

A subset of `R^q` with Euclidean diameter at most `L sqrt(r)/n` has coordinate range at most that amount in every coordinate. Consequently it can intersect at most

\[
C_{q,r,L}
:=
\bigl(\lceil L\sqrt r\rceil+2\bigr)^q
\tag{11}
\]

uniform `D`-quantizer cubes of side `1/n`. The exact constant is immaterial; only its independence of `n`, `y`, and the particular mark cell matters.

Because `(1)` makes `D` a deterministic function of `(Y,M)`, the conditional support of `Q_n(D)` given `(Y,Q_n(M))` has cardinality at most `C_{q,r,L}` almost surely. Hence

\[
H\bigl(Q_n(D)\mid Q_n(M),Y\bigr)
\le
\log_2 C_{q,r,L}.
\tag{12}
\]

### The scale-by-scale entropy inequality

By the chain rule and monotonicity under conditioning,

\[
\begin{aligned}
H(Q_n(D)\mid Y)
&\le
H(Q_n(D),Q_n(M)\mid Y)\\
&=
H(Q_n(M)\mid Y)
+
H(Q_n(D)\mid Q_n(M),Y)\\
&\le
H(Q_n(M)\mid Y)+\log_2 C_{q,r,L}.
\end{aligned}
\tag{13}
\]

Divide by `log_2 n`. The additive term in `(13)` is scale-independent, so it disappears after normalization. Taking `liminf` and `limsup` gives `(3)`.

For bounded `M in [0,1)^r`, the quantizer has at most `n^r` labels, so

\[
H(Q_n(M)\mid Y)
\le H(Q_n(M))
\le r\log_2 n,
\tag{14}
\]

which proves `(4)` and `(5)`.

Finally, if the reverse fiberwise Lipschitz reconstruction `(7)` also exists, apply `(3)` once to `R` and once to `S`; the two opposite inequalities give `(8)`.

## Sharpness and falsification controls

### The resource inequality is sharp but tautological repair remains excluded

Take `M=D` and let `R(y,m)=m`. Then equality holds throughout `(3)`--`(6)`. Thus the dimension lower bound itself is sharp.

This does **not** make the identity mark an explanatory lift. It is exactly the unrestricted target-copying repair that the Arithmetic Fidelity mandate excludes as a false notion of minimal structure. AF-121 is a lower-bound theorem inside a declared admissible category; naturality, canonicity, and availability of a non-tautological mark remain separate gates.

### Measurable recovery destroys the dimension bound

The Lipschitz hypothesis is load-bearing. Let `Y` be constant and let

\[
D=(U,V),
\]

where `U,V` are independent uniform random variables on `[0,1)`. Outside the null set of ambiguous dyadic expansions, interleave the binary digits of `U` and `V` to obtain one scalar

\[
M\in[0,1).
\]

Digit de-interleaving is a measurable inverse almost everywhere, so `D` is exactly recoverable from the scalar `M` by a measurable decoder. The interleaved bits are again independent fair bits, hence `M` is uniform on `[0,1)`. Therefore

\[
d(M)=1,
\qquad
d(D)=2.
\tag{15}
\]

So arbitrary measurable reconstruction can increase information dimension. There is no category-free dimension lower bound for exact side information. This is the fine-scale analogue of AF-001's warning that unconstrained lifts trivialize recoverability.

### Information dimension does not price zero-dimensional ambiguity

Let `Y` again be constant and let `D` be a nondegenerate Bernoulli bit. Then

\[
d(D)=0,
\tag{16}
\]

although exact recovery clearly requires nontrivial discrete information when `Y` does not determine the bit.

Thus `(5)` is intentionally not a universal side-information cost. It measures positive-dimensional fine-scale complexity. Discrete residual ambiguity still requires the zero-error, support, cardinality, or Shannon-entropy tools developed elsewhere in this line. In particular, AF-119's finite-entropy atomic regime and AF-121's positive-dimensional regime are complementary rather than competing classifications.

### Uniformity over the retained base matters

The proof uses one Lipschitz constant `L` valid for almost every fiber. If the fiberwise constants grow without any scale-independent control, the number of target quantizer cells reachable from one mark cell need not be uniformly bounded, and the additive constant in `(13)` can become scale-dependent. Any application with nonuniform reconstruction must therefore provide a quantitative replacement before invoking the dimension inequality.

## Prior-art audit

The underlying information-dimension and Lipschitz monotonicity principles are classical. **No standalone theorem-level novelty is claimed.**

- Alfréd Rényi, **“On the dimension and entropy of probability distributions,”** *Acta Mathematica Academiae Scientiarum Hungaricae* 10, 193–215 (1959). Role: foundational definition and analysis of information dimension through fine quantization entropy.
- Yihong Wu and Sergio Verdú, **“Rényi Information Dimension: Fundamental Limits of Almost Lossless Analog Compression,”** *IEEE Transactions on Information Theory* 56(8), 3721–3748 (2010), DOI `10.1109/TIT.2010.2050803`. Role: direct prior art for information dimension as the fundamental dimensional resource in analog compression under regularity constraints, including Lipschitz decompression.
- Bernhard C. Geiger and Tobias Koch, **“On the Information Dimension of Stochastic Processes,”** *IEEE Transactions on Information Theory* 65(10), 6496–6518 (2019), DOI `10.1109/TIT.2019.2922186`. Role: modern conditional-information-dimension framework and Lipschitz/bi-Lipschitz monotonicity context; also reinforces that unrestricted transformations do not obey naive dimension-preservation rules.

AF-121's contribution is therefore organizational and category-specific rather than a claim that Lipschitz maps and information dimension have not previously been connected. It specializes the classical machinery to the Arithmetic Fidelity lift problem: condition on the already-retained compression `Y`, charge only the residual side mark `M`, expose the exact scale-by-scale entropy inequality `(13)`, and separate the positive-dimensional repair cost from both tautological target copying and zero-dimensional discrete ambiguity.

## Relationship to AF-119 and AF-120

AF-119 classifies when one coherent exactly generating refinement can have **finite terminal Shannon entropy**. Its answer is precisely the finite-entropy atomic regime. AF-120 then identifies Rényi information dimension with the Cesàro innovation rate of coherent dyadic refinement when the exact entropy budget diverges.

AF-121 closes the next gate posed there for one explicit admissible category. A target with positive conditional information dimension cannot be reconstructed through a lower-dimensional side coordinate by a uniformly fiberwise Lipschitz decoder, even when the retained base `Y` is supplied for free. Conversely, the measurable digit-interleaving control proves that the same statement is false if the category is weakened to arbitrary measurable recovery.

The resulting hierarchy is sharper than treating “information retained” as one scalar notion:

1. zero-dimensional discrete ambiguity is priced by zero-error/cardinality/Shannon resources;
2. positive-dimensional fine-scale ambiguity is priced by conditional information dimension under regular reconstruction;
3. neither resource by itself certifies that the retained mark is intrinsic, canonical, or arithmetic-specific.

## Consequences for the research line

This gives a reusable **category-indexed minimal-lift lower bound**. For a concrete compression, one may now set `Y` equal to its retained output and `D` equal to the discriminator that must survive. If the residual conditional dimension `d(D|Y)` is positive, every bounded Euclidean side mark supporting uniformly fiberwise Lipschitz recovery must have at least that many effective fine-scale dimensions.

The theorem also narrows the route toward arithmetic applications. Before information dimension can say anything about rational-prime fidelity, the line must identify a non-tautological prime discriminator, a natural retained base, and an intrinsic metric/admissible reconstruction category in which the residual discriminator has meaningful positive-dimensional structure. If the relevant prime residual is instead zero-dimensional, then information dimension is the wrong currency and the obstruction must be sought in discrete entropy, zero-error confusability, provenance, orientation, marking, or another structural invariant.
