# MC-145 — Fixed rational Bost–Connes matrix bands are exactly profinite-continuous

**Status:** `EXACT-DERIVED`, `NEGATIVE/OBSTRUCTION`, `PRIOR-ART-AUDITED`, `NO-NOVELTY-CLAIM`.

## Claim

Work in the canonical number-state representation of the Bost–Connes algebra `A_BC` on

\[
\ell^2(\mathbb N)=\overline{\operatorname{span}}\{\varepsilon_k:k\ge1\},
\]

with

\[
\pi(e(r))\varepsilon_k=e^{2\pi i k r}\varepsilon_k,
\qquad
\pi(\mu_n)\varepsilon_k=\varepsilon_{nk}.
\tag{1}
\]

Fix coprime positive integers `a,b`. For a bounded observable `A\in A_{BC}`, define the matrix-band readout along the fixed rational ray `a/b` by

\[
R_{a,b}(A)(k)
:=\langle\varepsilon_{ak},\pi(A)\varepsilon_{bk}\rangle,
\qquad k\ge1.
\tag{2}
\]

Then this apparently off-diagonal readout contains **exactly** the same class of scalar profinite information as the canonical diagonal classified in `MC-144`:

\[
\boxed{
R_{a,b}(A)(k)
=
\left\langle\varepsilon_k,
\pi(\mu_a^*A\mu_b)\varepsilon_k
\right\rangle.
}
\tag{3}
\]

Consequently there is a unique continuous function

\[
\widetilde R_{a,b}(A)\in C(\widehat{\mathbb Z})
\cong C^*(\mathbb Q/\mathbb Z)
\tag{4}
\]

whose restriction to the positive integers is `(2)`, and

\[
\boxed{
\widetilde R_{a,b}(A)
=
E_{\mathrm{diag}}(\mu_a^*A\mu_b),
}
\tag{5}
\]

where `E_diag` is the diagonal conditional expectation of `MC-144`.

The map

\[
R_{a,b}:A_{BC}\longrightarrow C(\widehat{\mathbb Z})
\tag{6}
\]

is contractive and **surjective**. Thus allowing one fixed off-diagonal multiplicative transport ratio does not enlarge the scalar readout class at all.

Combining surjectivity with the exact profinite Möbius obstruction in `MC-143` gives

\[
\boxed{
\inf_{A\in A_{BC}}
\sup_{\substack{k\ge1\\ \mu(k)\ne0}}
\left|
\langle\varepsilon_{ak},\pi(A)\varepsilon_{bk}\rangle
-\mu(k)
\right|
=1.
}
\tag{7}
\]

The same obstruction survives any **finite family** of fixed rational bands followed by a continuous finite-dimensional scalar decoder: every such decoded sequence is again the restriction of a continuous function on `\widehat{\mathbb Z}` and therefore cannot uniformly approximate the square-free Möbius sign with error below `1`.

This closes a concrete part of the off-diagonal escape left open by `MC-144`. A surviving bounded Bost–Connes route cannot obtain new Möbius orientation merely by moving from the diagonal to one fixed rational matrix band, or to finitely many such bands with continuous scalarization. It must use structure that is genuinely relational across **varying** ratios/scales, an infinite or non-continuously decoded family, a different state/readout geometry, or another mechanism outside this theorem's hypotheses.

## 1. Every fixed rational band is a shifted diagonal

From `(1)`,

\[
\pi(\mu_b)\varepsilon_k=\varepsilon_{bk},
\qquad
\pi(\mu_a)\varepsilon_k=\varepsilon_{ak}.
\]

Therefore, for every `A\in A_{BC}`,

\[
\begin{aligned}
\left\langle\varepsilon_k,
\pi(\mu_a^*A\mu_b)\varepsilon_k\right\rangle
&=
\left\langle
\pi(\mu_a)\varepsilon_k,
\pi(A)\pi(\mu_b)\varepsilon_k
\right\rangle\\
&=
\langle\varepsilon_{ak},\pi(A)\varepsilon_{bk}\rangle.
\end{aligned}
\tag{8}
\]

Because `A_BC` is a `C^*`-algebra, `\mu_a^*A\mu_b\in A_{BC}`. `MC-144` applies directly to this element and says its canonical number-state diagonal is the restriction of a unique member of `C(\widehat{\mathbb Z})`. This proves `(4)`–`(5)` without any approximation or spectral hypothesis.

Contractivity is immediate:

\[
\|\widetilde R_{a,b}(A)\|_\infty
=
\sup_{k\ge1}|R_{a,b}(A)(k)|
\le \|A\|.
\tag{9}
\]

The equality between the supremum over positive integers and the profinite sup norm uses density of `\mathbb N` in `\widehat{\mathbb Z}`, exactly as in `MC-144`.

Surjectivity is equally exact. Let `c\in C^*(\mathbb Q/\mathbb Z)` be arbitrary and choose

\[
A=\mu_a c\mu_b^*.
\tag{10}
\]

Since each `\mu_n` is an isometry,

\[
\mu_a^*A\mu_b
=\mu_a^*\mu_a\,c\,\mu_b^*\mu_b
=c.
\tag{11}
\]

Thus `(5)` returns exactly the continuous profinite function represented by `c`. Hence the range in `(6)` is neither smaller nor larger than the coefficient algebra.

For `a=b=1`, this reduces to the diagonal map of `MC-144`. For a general positive rational ratio, dividing numerator and denominator by their gcd reduces to the coprime case without changing the ray.

## 2. Algebraic monomials make the ratio selection explicit

The standard algebraic span consists of monomials

\[
\mu_m c\mu_n^*,
\qquad
m,n\ge1,
\quad
c\in C^*(\mathbb Q/\mathbb Z).
\tag{12}
\]

Let `g\in C(\widehat{\mathbb Z})` denote the coefficient function represented by `c`. Then

\[
\mu_n^*\varepsilon_{bk}
=
\begin{cases}
\varepsilon_{bk/n},&n\mid bk,\\
0,&n\nmid bk.
\end{cases}
\tag{13}
\]

After applying `c` and then `\mu_m`, the resulting basis vector is `\varepsilon_{mbk/n}`. Its inner product with `\varepsilon_{ak}` can be nonzero only when

\[
mb=an.
\tag{14}
\]

Because `\gcd(a,b)=1`, `(14)` is equivalent to

\[
m=ad,
\qquad
n=bd
\tag{15}
\]

for some integer `d\ge1`. In that case `n\mid bk` is equivalent to `d\mid k`, and therefore

\[
\boxed{
R_{a,b}(\mu_m c\mu_n^*)(k)
=
\begin{cases}
\mathbf 1_{d\mid k}\,g(k/d),
& m=ad,\ n=bd,\\
0,& mb\ne an.
\end{cases}
}
\tag{16}
\]

The nonzero expression in `(16)` is exactly the diagonal coefficient of `\mu_d c\mu_d^*`, hence a coefficient-algebra/profinite-continuous function. Thus a fixed rational band simply selects one positive-rational homogeneous direction and then forgets the remaining crossed-product transport through the same diagonal projection already classified in `MC-144`.

Equation `(16)` is useful as a falsification check on `(3)`: no hidden summation over unrelated ratios is present. Only monomials with the selected ratio `m/n=a/b` survive.

## 3. The Möbius uniform-distance floor is still exactly one

`MC-143` proves the exact approximation barrier

\[
\inf_{f\in C(\widehat{\mathbb Z})}
\sup_{\mu(k)\ne0}|f(k)-\mu(k)|=1.
\tag{17}
\]

The lower bound comes from a profinite collision: one can choose primes and products of two primes converging to the same point of `\widehat{\mathbb Z}` while their Möbius signs remain `-1` and `+1`. A continuous scalar observable cannot separate those two limiting sign requirements with uniform error below `1`.

By surjectivity of `(6)`, the collection of sequences in `(2)` as `A` varies over `A_BC` is exactly the restriction of `C(\widehat{\mathbb Z})`. Substituting this equality of classes into `(17)` proves the lower bound in `(7)`. The zero observable gives error exactly `1`, so equality follows.

This is stronger than saying that one convenient off-diagonal observable fails. It classifies **every bounded observable read along one fixed rational multiplicative ray**.

It is also deliberately weaker than a statement about all off-diagonal information. The full two-index kernel

\[
(j,k)\longmapsto
\langle\varepsilon_j,\pi(A)\varepsilon_k\rangle
\]

contains relations among many ratios simultaneously; `(7)` does not collapse that two-dimensional object to one profinite coordinate.

## 4. Finite fixed-band scalarization cannot repair the collision

Fix finitely many coprime pairs

\[
(a_1,b_1),\ldots,(a_r,b_r)
\]

and bounded observables `A_1,\ldots,A_r`. Each band gives a continuous function

\[
f_i=\widetilde R_{a_i,b_i}(A_i)
\in C(\widehat{\mathbb Z}).
\tag{18}
\]

Hence the joint readout

\[
x\longmapsto(f_1(x),\ldots,f_r(x))
\tag{19}
\]

is a continuous map from `\widehat{\mathbb Z}` to `\mathbb C^r`. For any continuous decoder `F:\mathbb C^r\to\mathbb C`, the scalar sequence

\[
k\longmapsto F(f_1(k),\ldots,f_r(k))
\tag{20}
\]

again extends continuously to `\widehat{\mathbb Z}`. The same prime/semiprime collision used in `(17)` therefore gives

\[
\sup_{\mu(k)\ne0}
|F(f_1(k),\ldots,f_r(k))-\mu(k)|\ge1.
\tag{21}
\]

Thus finitely many fixed homogeneous bands do not evade the obstruction merely by being combined nonlinearly, provided the final scalarization is continuous.

This corollary is intentionally finite-dimensional. It does not classify an infinite family of ratios equipped with a topology strong enough to retain new relational information, nor a decoder that becomes singular/discontinuous in a scale-dependent limit.

## 5. Prior art and novelty audit

The operator-algebraic framework is standard.

- Jean-Benoît Bost and Alain Connes, *Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory*, Selecta Mathematica (N.S.) **1** (1995), 411–457, introduced the arithmetic `C^*`-dynamical system, its canonical representations, and the semigroup isometries used in `(1)`.
- Marcelo Laca and Iain Raeburn, *A Semigroup Crossed Product Arising in Number Theory*, Journal of the London Mathematical Society **59** (1999), 330–344, DOI `10.1112/S0024610798006620`, realize the Bost–Connes algebra as a semigroup crossed product. This is the natural established language for the monomials `(12)` and their multiplicative ratio structure.
- Marcelo Laca, *From Endomorphisms to Automorphisms and Back: Dilations and Full Corners*, Journal of the London Mathematical Society **61** (2000), 893–904, DOI `10.1112/S0024610799008492`, constructs the dilation of the Bost–Connes system as a crossed product by `\mathbb Q_+^*`, making the positive-rational homogeneous viewpoint explicit at the ambient crossed-product level.

A targeted search of Bost–Connes semigroup-crossed-product, conditional-expectation, and positive-rational grading literature confirms that homogeneous/rational crossed-product decomposition is established operator-algebraic structure. No novelty is claimed for that structure, for the matrix-coefficient identity `(3)`, or for the fact that a fixed homogeneous coefficient can be shifted to degree zero.

The line-specific contribution here is only the **combination** of those standard identities with the already persisted exact profinite obstruction `MC-143` and diagonal classification `MC-144`: every bounded fixed-rational matrix band, and every finite continuously scalarized family of such bands, lands in the same profinite-continuous information quotient that is uniformly one unit away from the square-free Möbius sign.

No absence of a literature search hit is used as novelty evidence.

## Boundaries and falsification tests

- **Fixed ratio is essential.** If the ratio `a/b` changes with `k` or with the observation scale, `(3)` no longer reduces the entire sequence to the diagonal of one fixed algebra element.
- **Finite-band scalarization is only continuous.** A growing/infinite family or a singular scale-dependent decoder may retain information not represented by one continuous function on `\widehat{\mathbb Z}`.
- **The observables are bounded elements of `A_BC`.** Unbounded affiliated or measurable operators can fall outside the norm-completion argument inherited from `MC-144`.
- **The theorem concerns scalar matrix coefficients in the canonical number-state representation.** Coherent superpositions, operator-valued kernels, families of states, or other representations are not classified here.
- **Pointwise Möbius recovery is stronger than an aggregate transfer.** A fixed-band statistic might still enter a weighted or collective estimate without approximating `\mu(k)` pointwise; such a proposal needs an independent source-to-Mertens theorem and is not excluded by `(7)`.
- **The finite-band corollary does not collapse the full two-index kernel.** It rules out only a finite set of fixed rays followed by continuous scalar decoding.
- **No RH implication or Mertens improvement is obtained.** This is an exact information/readout obstruction.

The decisive escape test is therefore explicit: a future bounded off-diagonal candidate must identify what relation among changing ratios, scales, or states survives the reduction `(3)` and why that relation cannot be continuously represented by finitely many profinite coefficient functions. Merely choosing a nonzero off-diagonal matrix coefficient is no longer enough.

## Consequence for the line

`MC-144` left off-diagonal matrix coefficients as one of the principal bounded crossed-product escape surfaces. The present result shows that **off-diagonalness by itself is not the missing ingredient**. Every fixed positive-rational band can be conjugated back to the canonical diagonal before readout, and its scalar information class is exactly `C(\widehat{\mathbb Z})`.

Together with `MC-143`–`MC-144`, this narrows the Bost–Connes branch to genuinely multi-ratio or scale-varying relations, non-continuous/infinite-dimensional decoding, alternative state geometry, unbounded observables, or aggregate transfer mechanisms that do not require pointwise Möbius orientation recovery. Any such continuation must still meet the line's harder source-to-excursion requirement: it must yield a quantitatively cheaper route to Mertens amplitude rather than merely storing the Möbius sign in a more elaborate representation.