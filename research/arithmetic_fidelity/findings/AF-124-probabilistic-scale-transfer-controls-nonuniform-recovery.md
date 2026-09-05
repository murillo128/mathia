# AF-124 — Probabilistic scale transfer controls nonuniform recovery

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `CLASSICAL-INGREDIENTS`, `CATEGORY-INDEXED`, `MULTISCALE-FIDELITY`, `NO-NOVELTY-CLAIM`

## Claim

AF-122 gives a full quantization-profile inequality when every retained fiber shares one deterministic modulus of continuity. AF-123 shows that, for first-order information dimension, a common Lipschitz constant is unnecessary: arbitrarily large retained-state-dependent Lipschitz constants are harmless as long as they are finite almost surely.

The common mechanism is more general. What matters is not a uniform modulus itself but the **input resolution depth required, on a retained fiber, to resolve one target scale**.

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

For dyadic depth `k>=0`, write

\[
Q_k(X):=\lfloor 2^kX\rfloor
\tag{2}
\]

coordinatewise and

\[
E_X(k\mid Y):=H_2(Q_k(X)\mid Y).
\tag{3}
\]

Suppose that for every `k` there is a measurable fiber-resolution depth

\[
\Phi_k:Y\to\mathbb N\cup\{\infty\}
\tag{4}
\]

with the following property: for almost every retained state `y`, whenever `\Phi_k(y)<\infty` and

\[
Q_{\Phi_k(y)}(m)=Q_{\Phi_k(y)}(m'),
\tag{5}
\]

then

\[
\|R_y(m)-R_y(m')\|_\infty\le 2^{-k},
\qquad
R_y(m):=R(y,m),
\tag{6}
\]

on the relevant mark domain.

Thus `\Phi_k(y)` is any certified dyadic input depth sufficient to determine the target to scale `2^{-k}` on fiber `y`. It need not arise from a Lipschitz or Hölder modulus, and it need not be uniformly bounded over `y`.

Then for every deterministic integer `m>=0`, with

\[
\delta_{k,m}:=\Pr\{\Phi_k(Y)>m\},
\tag{7}
\]

one has the exact profile bound

\[
\boxed{
E_D(k\mid Y)
\le
E_M(m\mid Y)
+q
+qk\,\delta_{k,m}.
}
\tag{8}
\]

Equivalently, if `m_k(\delta)` is any deterministic `\delta`-upper quantile of the random resolution depth,

\[
\Pr\{\Phi_k(Y)>m_k(\delta)\}\le\delta,
\tag{9}
\]

then

\[
\boxed{
E_D(k\mid Y)
\le
E_M(m_k(\delta)\mid Y)
+q+qk\delta.
}
\tag{10}
\]

This gives a nonuniform analogue of AF-122: instead of one worst-case modulus, the target profile is controlled by a **high-probability scale-transfer envelope**.

Define the probabilistic resolution exponent

\[
c_R
:=
\operatorname{p\!\!-limsup}_{k\to\infty}
\frac{\Phi_k(Y)}{k}
=
\inf\left\{
c\ge0:
\forall\varepsilon>0,
\Pr\!\left(
\Phi_k(Y)>(c+\varepsilon)k
\right)\to0
\right\}.
\tag{11}
\]

If `c_R<\infty`, then the lower and upper conditional information dimensions satisfy

\[
\boxed{
\underline d(D\mid Y)
\le
c_R\,\underline d(M\mid Y),
\qquad
\overline d(D\mid Y)
\le
c_R\,\overline d(M\mid Y).
}
\tag{12}
\]

The convention is that the right-hand side is zero when `c_R=0`. Equation `(12)` is therefore a scale-complexity data-processing law: an exact decoder may increase information dimension only by paying the corresponding asymptotic input-resolution expansion.

## Derivation

### Good retained fibers need only constantly many target cells

Fix `k` and a deterministic mark depth `m`. Let

\[
G_{k,m}:=\{y:\Phi_k(y)\le m\},
\qquad
B_{k,m}:=\{y:\Phi_k(y)>m\}.
\tag{13}
\]

Because dyadic partitions are nested, on `G_{k,m}` equality of `Q_m(m_1)` and `Q_m(m_2)` implies equality at the coarser depth `\Phi_k(y)`. By `(6)`, the image of one `Q_m(M)` cell under `R_y` has `\ell_\infty` diameter at most `2^{-k}`.

Such an image intersects at most two depth-`k` dyadic target intervals in each coordinate and hence at most

\[
2^q
\tag{14}
\]

cells of `Q_k(D)`. Therefore

\[
H_2(Q_k(D)\mid Y=y,Q_m(M))\le q
\tag{15}
\]

for almost every `y\in G_{k,m}`.

On `B_{k,m}` no regularity is assumed. Since `D\in[0,1)^q`, however, `Q_k(D)` has at most `2^{qk}` possible labels, so always

\[
H_2(Q_k(D)\mid Y=y,Q_m(M))\le qk.
\tag{16}
\]

The good/bad event is already determined by `Y`, so no extra binary-event entropy is needed. Averaging `(15)` and `(16)` over `Y` gives

\[
H_2(Q_k(D)\mid Y,Q_m(M))
\le
q(1-\delta_{k,m})+qk\delta_{k,m}
\le q+qk\delta_{k,m}.
\tag{17}
\]

The chain rule now yields

\[
\begin{aligned}
E_D(k\mid Y)
&\le
H_2(Q_m(M),Q_k(D)\mid Y)\\
&=
E_M(m\mid Y)
+H_2(Q_k(D)\mid Y,Q_m(M))\\
&\le
E_M(m\mid Y)+q+qk\delta_{k,m},
\end{aligned}
\tag{18}
\]

which proves `(8)` and `(10)`.

### Probabilistic scale growth gives the upper-dimension bound

Fix `\varepsilon>0` and set

\[
m_k:=\lceil(c_R+\varepsilon)k\rceil.
\tag{19}
\]

By `(11)`,

\[
\delta_k:=\Pr\{\Phi_k(Y)>m_k\}\to0.
\tag{20}
\]

Applying `(8)` gives

\[
\frac{E_D(k\mid Y)}k
\le
\frac{E_M(m_k\mid Y)}{m_k}
\frac{m_k}{k}
+\frac qk+q\delta_k.
\tag{21}
\]

If `c_R+\varepsilon>0`, then `m_k\to\infty` and `m_k/k\to c_R+\varepsilon`. The limsup of `E_M(m_k|Y)/m_k` along this subsequence is at most the global upper conditional information dimension. Hence

\[
\overline d(D\mid Y)
\le
(c_R+\varepsilon)\overline d(M\mid Y).
\tag{22}
\]

Letting `\varepsilon\downarrow0` proves the upper inequality in `(12)`. The same argument with arbitrarily small positive `\varepsilon` also covers `c_R=0`.

### The lower-dimension bound needs an inverse-scale subsequence

A direct liminf of `(21)` is insufficient because a subsequence of the mark profile can have a larger liminf than the full profile. Instead choose integers `n_j\to\infty` such that

\[
\frac{E_M(n_j\mid Y)}{n_j}
\to
\underline d(M\mid Y).
\tag{23}
\]

Again fix `\varepsilon>0` and put `a=c_R+\varepsilon>0`. Choose

\[
k_j:=\left\lfloor\frac{n_j-1}{a}\right\rfloor.
\tag{24}
\]

Then `k_j\to\infty`, `n_j/k_j\to a`, and for all large `j`,

\[
\lceil ak_j\rceil\le n_j.
\tag{25}
\]

Apply `(8)` at target depth `k_j` and mark depth `m_j=\lceil ak_j\rceil`. By monotonicity of dyadic entropy under refinement,

\[
E_M(m_j\mid Y)\le E_M(n_j\mid Y).
\tag{26}
\]

The bad-fiber probability at `k_j` tends to zero by `(11)`, so

\[
\begin{aligned}
\underline d(D\mid Y)
&\le
\liminf_j\frac{E_D(k_j\mid Y)}{k_j}\\
&\le
\lim_j
\frac{E_M(n_j\mid Y)}{n_j}
\frac{n_j}{k_j}\\
&=
(c_R+\varepsilon)\underline d(M\mid Y).
\end{aligned}
\tag{27}
\]

Letting `\varepsilon\downarrow0` proves the lower inequality in `(12)`.

## Exact specializations

### AF-123 is the unit scale-exponent case

Under AF-123's retained-state-dependent fiberwise Lipschitz envelope,

\[
\|R_y(m)-R_y(m')\|_\infty
\le
L(y)\|m-m'\|_2,
\tag{28}
\]

one may take

\[
\Phi_k(Y)
\le
k+
\left\lceil
\log_2^+\!\bigl(L(Y)\sqrt r\bigr)
\right\rceil.
\tag{29}
\]

The random additive term is finite almost surely, so divided by `k` it converges to zero in probability without any moment assumption. Therefore `c_R\le1`, and `(12)` reproduces AF-123's information-dimension monotonicity.

This explains exactly why the tail-truncation proof there works: first-order dimension ignores an `o_p(k)` random scale overhead.

### AF-122's Hölder factor is a deterministic resolution exponent

If every fiber is uniformly `(L,\alpha)`-Hölder,

\[
\|R_y(m)-R_y(m')\|_\infty
\le
L\|m-m'\|_2^\alpha,
\qquad 0<\alpha\le1,
\tag{30}
\]

then

\[
\Phi_k(Y)
\le
\frac{k}{\alpha}+O(1)
\tag{31}
\]

uniformly, so

\[
c_R\le\frac1\alpha.
\tag{32}
\]

Equation `(12)` recovers AF-122's Hölder dimension factor.

### Prefix-local measurable decoding can be dimension-expanding but still scale-controlled

The digit-interleaving example from AF-121 and AF-123 is not Lipschitz: one scalar uniform mark `M` can measurably encode two independent uniform coordinates `D=(U,V)`, so `d(M)=1` while `d(D)=2`.

Nevertheless the decoder is **prefix local**. Knowing the first `2k` binary digits of `M` determines the first `k` digits of both `U` and `V` away from the usual null set of ambiguous binary expansions. Thus one may take

\[
\Phi_k\le2k+O(1),
\tag{33}
\]

and hence `c_R\le2`. Equation `(12)` gives

\[
d(D)\le2d(M)=2,
\tag{34}
\]

which is attained.

So AF-124 does not pretend that measurable recovery is dimension-monotone. It prices the failure by its input/output resolution expansion. This is strictly broader than a continuity-class statement.

## Sharpness and falsification controls

### A vanishing bad-fiber probability is enough; a small mean is not required

Equation `(8)` shows that a rare set of arbitrarily irregular retained fibers contributes at most `qk` bits times its probability. For dimension fidelity, the tail need only vanish at every linear scale threshold above `c_R k`. No expectation of `\Phi_k`, no moment of a Lipschitz constant, and no uniform modulus is required.

This is an information-spectrum-style statement: first-order asymptotic fidelity is governed by a probabilistic upper envelope, not by a mean regularity cost.

### Positive-probability rough fibers cannot be discarded by this theorem

If for some `c` there is a fixed positive probability that `\Phi_k(Y)>ck` along infinitely many scales, then that rough stratum does not disappear after conditioning and averaging. The definition `(11)` correctly refuses to ignore it.

The resulting `c_R` can therefore be pessimistic when different retained strata have very different mark dimensions or probabilities. AF-124 makes no claim that the single scalar `c_R` is the sharpest possible stratified bound. A finer theorem would need to couple fiberwise resolution exponents to fiberwise entropy growth before averaging.

### The resolution certificate is category data, not a free optimization variable

One can always choose a larger `\Phi_k`; doing so only weakens the bound. A meaningful application must derive a small resolution depth from an independently justified decoder, metric, filtration, symbolic locality rule, or other admissible structure. The theorem does not make an arbitrary encoding canonical.

Similarly, changing the source metric or dyadic filtration can change `\Phi_k` drastically. As in AF-122, the refinement geometry is part of the declared category.

### Finite `\Phi_k` is not automatic for arbitrary measurable maps

A measurable decoder can oscillate on every dyadic cell at every depth. For such a map, a finite fiber-resolution certificate of type `(4)`--`(6)` may not exist at a given target scale. AF-124 therefore does not turn unrestricted measurable recovery into a regularity theorem; it isolates the exact additional property needed for scale-local recoverability.

### Bounded target support is used quantitatively

The bad-fiber term `qk\delta_{k,m}` uses only that `D\in[0,1)^q`, so the target depth-`k` partition has at most `2^{qk}` atoms. For unbounded targets or other refinement systems, `(8)` requires the corresponding deterministic or conditional entropy bound on the bad fibers.

## Prior-art audit

All core ingredients are classical, and **no standalone novelty claim is made for the entropy inequality or the probabilistic-limsup formulation**.

- Alfréd Rényi, **“On the Dimension and Entropy of Probability Distributions,”** *Acta Mathematica Academiae Scientiarum Hungaricae* 10, 193–215 (1959). Role: foundational quantization-entropy definition of information dimension.
- Yihong Wu and Sergio Verdú, **“Rényi Information Dimension: Fundamental Limits of Almost Lossless Analog Compression,”** *IEEE Transactions on Information Theory* 56(8), 3721–3748 (2010), DOI `10.1109/TIT.2010.2050803`. Role: direct prior art for information dimension as the dimensional resource governing analog compression under regularity constraints, especially Lipschitz decompression.
- Tsutomu Kawabata and Amir Dembo, **“The Rate-Distortion Dimension of Sets and Measures,”** *IEEE Transactions on Information Theory* 40(5), 1564–1572 (1994), DOI `10.1109/18.333868`. Role: classical bridge between fine-scale information growth and rate-distortion scaling.
- Te Sun Han, ***Information-Spectrum Methods in Information Theory***, Springer (2003), and the information-spectrum literature built around probabilistic limsup/liminf quantities. Role: established language for asymptotic thresholds controlled by limit superior in probability rather than expectations or almost-sure uniform bounds.

Targeted literature searches for combinations of conditional information dimension, nonuniform/random moduli, random Lipschitz constants, and fiberwise Hölder recovery located the classical information-dimension and analog-compression frameworks above but did not identify this exact retained-base resolution-depth inequality as a named theorem. That absence is not treated as evidence of novelty: `(8)` is an elementary conditional-entropy argument once the resolution certificate is stated, and `(12)` is its direct information-spectrum normalization.

The durable value for Arithmetic Fidelity is organizational and structural. AF-124 identifies a common invariant underlying AF-122 and AF-123 and extends it beyond topological regularity classes: **the scale-transfer law itself** is the fidelity resource.

## Consequences for Arithmetic Fidelity

The recent multiscale branch can now be stated without overcommitting to Lipschitz or Hölder categories. For a proposed compression with retained output `Y`, discriminator `D`, and side mark `M`, the relevant question is:

> how many bits of mark resolution are required, on all but a vanishing fraction of retained states, to resolve `k` bits of the discriminator?

The answer is the random depth `\Phi_k(Y)`. Its high-probability quantiles control the full finite-scale entropy profile through `(10)`, while its probabilistic linear growth rate controls information dimension through `(12)`.

This gives a sharper audit for future arithmetic applications. A prime-specific residual need not have a globally Lipschitz reconstruction to be meaningfully faithful. It may instead have a source-forced symbolic, boundary, transverse, spectral, or multiscale decoder whose resolution demand is quantifiable. Conversely, any proposal that claims to recover a richer prime discriminator from a poorer retained mark must exhibit the required scale-transfer budget explicitly; downstream spectralization, positivity, determinant formation, or asymptotic limiting cannot erase that cost.

The next unresolved level is **stratified scale fidelity**: when retained fibers have genuinely different resolution exponents and different conditional entropy profiles, the worst-case-in-probability scalar `c_R` may be too coarse. A sharper theorem would have to couple the fiberwise scale-transfer profile to fiberwise discriminator/mark entropy before averaging, rather than summarize regularity and information content separately.