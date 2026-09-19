# MC-389 — Endpoint affine rank forces an explicit excess over the Welch exception budget

## Status

`EXACT-DERIVED` · `PRIOR-ART-AUDITED` · `FRONTIER-ADVANCE` · `STRUCTURAL-OBSTRUCTION` · `NON-RH`.

The endpoint-support affine-rank identity of MC-388 has a direct finite-field consequence that makes the previous inverse-theorem argument unnecessary. For a finite set in a binary vector space, large affine dimension limits every nonzero translate overlap. Summing that overlap bound gives an explicit additive-energy deficit for the projected endpoint simplex, hence an explicit fourth-moment contraction and an explicit multiplicative gap above the generic `H/R` exceptional-mode threshold of MC-386.

## Precise claim

Let `W <= F_2^R` have dimension `d`, let `H=|W|=2^d`, and consider the endpoint Bochner kernel from MC-388

\[
g(K)=\sum_\xi p(\xi)(-1)^{\langle\xi,K\rangle},
\qquad
p=\sum_z d_z\,\delta_{\pi(\mathbf 1+e_z)},
\]

where `p` is a probability measure and its distinct support is

\[
S=\{\pi(\mathbf1+e_z):1\le z\le R\},
\qquad r=|S|\le R.
\]

Assume the high-rank endpoint branch

\[
d\ge \frac{3R}{4}.
\]

Then, for all sufficiently large `R`, the support has the explicit energy bound

\[
\boxed{E(S)\le \frac34 r^3.}
\tag{1}
\]

Consequently, if `B subset W\setminus\{0\}` is an exceptional set and every good nonzero mode satisfies

\[
|g(K)|\le\varepsilon_R,
\qquad
K\in W\setminus(B\cup\{0\}),
\qquad
\varepsilon_R=o(R^{-1/2}),
\]

then, for all sufficiently large `R`,

\[
\boxed{|B|\ge\left(1+\frac1{4096}\right)\frac HR.}
\tag{2}
\]

The constant `1/4096` is deliberately non-optimized. The result remains conditional on the stated good-mode estimate; it does not supply that analytic estimate and does not imply an RH-scale bound for `M(x)`.

## Derivation

### 1. Affine dimension bounds every nonzero translate overlap

Let `A` be any finite subset of a vector space over `F_2`, with

\[
|A|=r,
\qquad
k=\dim\operatorname{aff}(A).
\]

For nonzero `t`, put

\[
m_t:=|A\cap(A+t)|.
\]

Translation by `t` acts without fixed points on `A\cap(A+t)`, so those `m_t` points split into `m_t/2` disjoint pairs `{a,a+t}`. Choose one representative from each pair and keep the `r-m_t` points of `A` outside the overlap. The whole of `A` lies in the affine span of these

\[
\frac{m_t}{2}+(r-m_t)=r-\frac{m_t}{2}
\]

representatives together with the one direction `t`. Therefore

\[
k\le r-\frac{m_t}{2},
\]

and hence

\[
\boxed{m_t\le 2(r-k)\qquad(t\ne0).}
\tag{3}
\]

This estimate is sharp in the affinely independent extreme: if `k=r-1`, every nonzero pair sum has at most the two ordered representations obtained by swapping the pair.

### 2. Translate overlap gives an explicit energy deficit

In characteristic two the additive representation number is exactly

\[
r_A(t)=|A\cap(A+t)|=m_t,
\]

with `m_0=r`, and

\[
\sum_t m_t=r^2.
\]

Thus

\[
E(A)=\sum_t m_t^2
\le r^2+2(r-k)\sum_{t\ne0}m_t
=r^2+2(r-k)(r^2-r).
\tag{4}
\]

This is a general explicit affine-rank/energy inequality for finite subsets of binary vector spaces.

For the endpoint support, MC-388 gives

\[
k=\dim\operatorname{aff}(S)
=d-\dim(W\cap\langle\mathbf1\rangle)
\ge d-1
\ge\frac{3R}{4}-1.
\]

Since `r<=R`,

\[
r-k\le\frac r4+1.
\]

Substituting into `(4)` gives

\[
E(S)
\le r^2+\left(\frac r2+2\right)(r^2-r)
=\frac12r^3+\frac52r^2-2r.
\tag{5}
\]

The affine-rank lower bound also implies `r>=3R/4`, so `r` tends to infinity with `R`. In particular, for `r>=10`, the right side of `(5)` is at most `3r^3/4`, proving `(1)`.

The important point is that the fixed energy gap is now elementary and explicit. No additive inverse theorem or ineffective stability modulus is required.

### 3. Near-Welch endpoint weights inherit an explicit fourth-moment contraction

Let

\[
Q:=\sum_{K\in W}|g(K)|^2=H\|p\|_2^2.
\]

Set

\[
\alpha:=\frac1{1024}.
\]

Suppose first that

\[
Q\le(1+\alpha)\frac HR.
\tag{6}
\]

Because `p` is supported on `r` points,

\[
\|p\|_2^2\ge\frac1r,
\]

so `(6)` implies `r>=R/(1+alpha)`. If `u_S` denotes the uniform probability measure on `S`, then

\[
\|p-u_S\|_2^2
=\|p\|_2^2-\frac1r
\le\frac\alpha R.
\tag{7}
\]

From `(1)`,

\[
\|u_S*u_S\|_2^2
=\frac{E(S)}{r^4}
\le\frac{3}{4r}.
\tag{8}
\]

Young's inequality gives

\[
\|p*p-u_S*u_S\|_2
\le2\|p-u_S\|_2.
\]

Using `(7)`, `(8)`, `r<=R`, and `\|p\|_2>=r^{-1/2}`,

\[
\frac{\|p*p\|_2}{\|p\|_2}
\le \frac{\sqrt3}{2}+2\sqrt\alpha
=\frac{\sqrt3}{2}+\frac1{16}.
\tag{9}
\]

The square of the last quantity is strictly below `7/8`. Finite-group Plancherel therefore yields the explicit contraction

\[
\boxed{
\sum_{K\in W}|g(K)|^4
=H\|p*p\|_2^2
\le\frac78 Q
}
\tag{10}
\]

whenever `(6)` holds and `R` is sufficiently large for `(1)`.

### 4. Fewer than `(1+1/4096)H/R` exceptions force the near-Welch regime and contradict `(10)`

Let `E=|B|`. On the good modes,

\[
\sum_{K\notin B\cup\{0\}}|g(K)|^2
\le H\varepsilon_R^2
=o(H/R).
\tag{11}
\]

Also `Q>=H/r>=H/R`. Suppose toward contradiction that

\[
E<\left(1+\frac1{4096}\right)\frac HR.
\tag{12}
\]

Since `|g(K)|<=1`, `(11)` and `(12)` give

\[
Q\le1+E+o(H/R)
\le\left(1+\frac1{4096}+o(1)\right)\frac HR.
\]

Because `d>=3R/4`, one has `H/R -> infinity`; hence, for sufficiently large `R`, this is strictly below `(1+1/1024)H/R`. Thus `(10)` applies.

Let

\[
U:=\sum_{K\in B\cup\{0\}}|g(K)|^2.
\]

By `(11)`, `U=(1-o(1))Q`. Cauchy--Schwarz and `(10)` give

\[
U^2
\le(E+1)\sum_{K\in B\cup\{0\}}|g(K)|^4
\le(E+1)\frac78Q.
\]

Therefore

\[
E+1
\ge\left(\frac87-o(1)\right)Q
\ge\left(\frac87-o(1)\right)\frac HR.
\tag{13}
\]

For large `R`, `(13)` contradicts `(12)` because `1=o(H/R)`. This proves `(2)`.

## Relevance

MC-386 showed that generic PSD/rank information alone cannot force more than approximately `H/R` exceptional modes because annihilator kernels attain that scale. MC-387 identified the near-extremal subgroup geometry, and MC-388 showed that the actual endpoint support has too much affine rank to approach it. The previous form of MC-389 converted that qualitative obstruction into an existential fixed gap by invoking robust restricted-sumset stability.

The direct overlap argument `(3)` is stronger for the actual high-rank endpoint regime. It turns affine rank immediately into an explicit energy deficit of at least one quarter, removes the inverse-theorem modulus, and gives a concrete endpoint exception gap. The structural frontier is therefore no longer effectiveness of the additive-energy constant. The remaining bottleneck is analytic: obtain a good-mode estimate at the `o(R^{-1/2})` frame scale with an exceptional family smaller than the explicit endpoint budget.

## Prior-art audit

Additive energy and the representation identity `E(A)=sum_t r_A(t)^2` are classical. Xuancheng Shao, *Additive energies of subsets of discrete cubes*, Proceedings of the Royal Society of Edinburgh Section A: Mathematics **156** (2026), 944–965, DOI `10.1017/prm.2024.126`, studies near-maximal additive energy and provides the robust restricted-sumset stability previously used here. The related paper by de Dios Pont, Greenfeld, Ivanisvili and Madrid, *Additive energies on discrete cubes*, Discrete Analysis (2023), studies sharp energy inequalities for subsets of discrete cubes.

A targeted literature search by the mathematical ingredients `affine dimension`, `translate overlap`, `binary vector space`, and `additive energy` did not identify a source for the exact inequality `(4)`. That absence is not evidence of novelty. Inequality `(3)` is an elementary affine-span count, and `(4)` is its immediate energy consequence, so no novelty claim is made for either. The line-specific result is their application to the exact projected endpoint simplex and the resulting explicit frame threshold.

## Boundaries and failure modes

- The binary-field hypothesis is load-bearing for the pairing argument: for `t!=0`, translation by `t` is a fixed-point-free involution. The displayed constants are not asserted over general groups.
- The high-rank endpoint branch `d>=3R/4` is load-bearing for the `3/4` energy factor. Equation `(4)` itself holds for every finite set in a binary vector space.
- The exact endpoint support identity of MC-388 is load-bearing. A generic rank-`R` PSD Cayley kernel need not have high-affine-rank Fourier support and still admits the annihilator sharpness example of MC-386.
- The constant `1/4096` is not optimized. It is chosen only to sit comfortably inside the explicit near-Welch admission window used in `(6)`--`(10)`.
- The good-mode hypothesis `epsilon_R=o(R^{-1/2})` remains essential. This finding supplies no character-sum theorem capable of proving it.
- The result does not upgrade averaged, logarithmic, short-interval, or exceptional-set Möbius cancellation to uniform global cancellation.
- No RH or direct `M(x)` estimate follows.

## Consequences

1. The endpoint branch now has an **effective structural exception threshold**: `(1+1/4096)H/R`, rather than an unspecified `(1+c_endpoint)H/R`.
2. The additive inverse-theorem modulus is no longer a frontier issue for this step; the elementary translate-overlap bound already gives a much larger explicit energy deficit.
3. Any analytic good/bad decomposition intended to close the high-rank source-frame branch must now beat the explicit threshold `(2)` while reaching `o(R^{-1/2})` on the good modes.
4. Improving the structural constant further is secondary unless it changes that analytic comparison; the immediate live question is the good-mode character-sum estimate at frame scale.
