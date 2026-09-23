# NB-308 — Möbius shell inversion forces a reciprocal floor for canonical Nyman pivots

- **Date:** 2026-09-23
- **Status:** proved
- **Research line:** `nyman_beurling`
- **Depends on:** NB-014, NB-290, NB-301, NB-307
- **Classification:** `EXACT-DERIVED + CANONICAL-NYMAN-SOURCE + RECIPROCAL-SHELLS + MOBIUS-INVERSION + COEFFICIENT-FUNCTIONAL + GRAM-SCHMIDT-PIVOTS + EXPLICIT-LOWER-BOUND + POST-CORE-GAP + TARGET-RATE-NOT-CLAIMED + PRIOR-ART-AUDITED`

## Claim

Let

\[
U_N:=\operatorname{span}\{g_2,\ldots,g_N\},
\qquad
g_j(x)=\left\{\frac1{jx}\right\}-\frac1j\left\{\frac1x\right\},
\]

and let

\[
w_n=(I-P_{U_{n-1}})g_n,
\qquad
\sigma_n=\|w_n\|_2
\]

be the canonical Gram--Schmidt innovation and pivot. Finite linear independence from `NB-014` gives `sigma_n>0`.

The reciprocal-shell representation contains enough arithmetic information to recover the coefficient of every generator by a finite Möbius transform. This gives the explicit universal pivot floor

\[
\boxed{
\sigma_n\ge \frac{\sqrt{3/2}}{\pi n},
\qquad n\ge2.
}
\tag{1}
\]

More precisely, if

\[
D_n
:=
\sum_{k=1}^{n}
k(k+1)
\left|
-\mathbf 1_{k\mid n}\mu(n/k)
+\mathbf 1_{k+1\mid n}\mu(n/(k+1))
\right|^2,
\tag{2}
\]

then

\[
\boxed{
\sigma_n\ge D_n^{-1/2},
\qquad
D_n\le4\sum_{d\mid n}d^2
\le\frac{2\pi^2}{3}n^2.
}
\tag{3}
\]

Consequently the multiplicative pivot-survival coefficients of `NB-290`,

\[
c_{m,j}:=rac{\sqrt m\,\sigma_{mj}}{\sigma_j},
\qquad 0<c_{m,j}\le1,
\]

also have the explicit lower bound

\[
\boxed{
c_{m,j}^2\ge\frac{3}{2\pi^2m j^2}.}
\tag{4}
\]

Combining (4) with the determinant certificate of `NB-307`, for

\[
2\le m\le N,
\qquad
q=\left\lfloor\frac Nm\right\rfloor,
\]

gives

\[
\boxed{
1-s_{\rm post}(N,m)^2
\ge
\left(\frac{3}{2\pi^2m}\right)^{N-q}
\left(\frac{q!}{N!}\right)^2.
}
\tag{5}
\]

In the first post-core strip `N/2<m<=N`, where `q=1` and `s_post(N,m)=beta_(N+1)(m)`, this becomes

\[
\boxed{
1-\beta_{N+1}(m)^2
\ge
\left(\frac{3}{2\pi^2m}\right)^{N-1}
\frac1{(N!)^2}.
}
\tag{6}
\]

The bound is deliberately interpreted only as a quantitative strictness certificate. It is factorially/exponentially tiny in the moving regime and does **not** give a useful asymptotic decay rate for `beta`, a target-aware gain, a finite-section Nyman-distance rate, or the Riemann hypothesis.

## 1. Reciprocal shells recover the generator coefficients

For

\[
I_k=\left(\frac1{k+1},\frac1k\right],
\qquad k\ge1,
\]

`NB-301`--`NB-304` use the exact shell values

\[
g_j|_{I_k}=r_j(k),
\qquad
r_j(k)=\frac{k\bmod j}{j}.
\tag{7}
\]

Take

\[
u=\sum_{j=2}^{N}a_jg_j\in U_N
\]

and denote its shell value by

\[
u_k=\sum_{j=2}^{N}a_jr_j(k),
\qquad u_0:=0.
\tag{8}
\]

The first difference of one shell sequence is

\[
\begin{aligned}
\Delta r_j(k)
&:=r_j(k)-r_j(k-1)\\
&=\frac1j-\mathbf 1_{j\mid k}.
\end{aligned}
\tag{9}
\]

Indeed the residue rises by one at every step except when `k` is a multiple of `j`, where it wraps from `(j-1)/j` to zero.

Let

\[
C:=\sum_{j=2}^{N}\frac{a_j}{j}.
\]

Summing (9) with coefficients `a_j` gives

\[
\boxed{
\Delta u(k)
=C-
\sum_{\substack{j\mid k\\j\ge2}}a_j.
}
\tag{10}
\]

At `k=1` the divisor sum is empty, so `Delta u(1)=C`. For every `n>=2`, Möbius inversion of (10) therefore yields

\[
\begin{aligned}
a_n
&=
\sum_{d\mid n}\mu(n/d)\bigl(C-\Delta u(d)\bigr)\\
&=-\sum_{d\mid n}\mu(n/d)\Delta u(d),
\end{aligned}
\tag{11}
\]

because

\[
\sum_{d\mid n}\mu(n/d)=0.
\]

Thus the coefficient functional

\[
L_n(u):=a_n
\]

has the exact shell formula

\[
\boxed{
L_n(u)
=-\sum_{d\mid n}\mu(n/d)(u_d-u_{d-1}).
}
\tag{12}
\]

This is the key point: the coefficient of `g_n` is visible from only the first `n` reciprocal shells, with completely explicit integer weights.

## 2. The coefficient functional has norm `O(n)`

Collecting the coefficient of each `u_k` in (12), define

\[
\lambda_{n,k}
:=-\mathbf 1_{k\mid n}\mu(n/k)
+\mathbf 1_{k+1\mid n}\mu(n/(k+1)).
\tag{13}
\]

Then

\[
L_n(u)=\sum_{k=1}^{n}\lambda_{n,k}u_k.
\tag{14}
\]

The exact Hilbert norm in shell coordinates is

\[
\|u\|_2^2
=
\sum_{k\ge1}\frac{|u_k|^2}{k(k+1)},
\tag{15}
\]

because `|I_k|=1/[k(k+1)]`. Weighted Cauchy--Schwarz therefore gives

\[
|L_n(u)|^2
\le
D_n\,\|u\|_2^2,
\tag{16}
\]

with `D_n` as in (2).

To estimate it uniformly, use

\[
|x+y|^2\le2(|x|^2+|y|^2)
\]

in (13). The first term contributes, after writing `d=k`, at most

\[
2\sum_{d\mid n}d(d+1),
\]

and the second, after writing `d=k+1`, contributes at most

\[
2\sum_{d\mid n}(d-1)d.
\]

Hence

\[
\begin{aligned}
D_n
&\le
2\sum_{d\mid n}\bigl(d(d+1)+(d-1)d\bigr)\\
&=4\sum_{d\mid n}d^2\\
&=4n^2\sum_{e\mid n}\frac1{e^2}\\
&\le4\zeta(2)n^2
=\frac{2\pi^2}{3}n^2.
\end{aligned}
\tag{17}
\]

The first inequality deliberately drops the factors `mu^2`, so (17) is safe but not intended to be sharp. The exact arithmetic constant `D_n` in (2) can be substantially smaller.

## 3. Applying the coefficient functional to the canonical innovation

By definition,

\[
w_n=g_n-P_{U_{n-1}}g_n.
\tag{18}
\]

The second term is a linear combination of `g_2,...,g_(n-1)`, so the coefficient of `g_n` in `w_n` is exactly one. Therefore

\[
L_n(w_n)=1.
\tag{19}
\]

Equations (16) and (19) give

\[
1
\le
\sqrt{D_n}\,\|w_n\|_2
=
\sqrt{D_n}\,\sigma_n,
\]

hence the exact lower bound

\[
\boxed{
\sigma_n\ge D_n^{-1/2}.
}
\tag{20}
\]

Combining (20) with (17) proves (1).

This also supplies a global determinant floor for the canonical Gram matrix `G_N=(<g_i,g_j>)_(i,j=2)^N`. Gram--Schmidt factorization gives

\[
\det G_N=\prod_{n=2}^{N}\sigma_n^2,
\]

and hence

\[
\boxed{
\det G_N
\ge
\left(\frac{3}{2\pi^2}\right)^{N-1}
\frac1{(N!)^2}.
}
\tag{21}
\]

Again, (21) is a nondegeneracy floor, not a useful conditioning estimate: a determinant may be extremely small while every finite section remains independent.

## 4. Explicit lower survival for multiplicative pivots

For every shell `I_k`, equation (7) gives

\[
0\le g_j(x)<1.
\]

Consequently

\[
\|g_j\|_2\le1,
\qquad
\sigma_j\le\|g_j\|_2\le1.
\tag{22}
\]

The survival coefficient from `NB-290` therefore satisfies

\[
\begin{aligned}
c_{m,j}
&=\frac{\sqrt m\,\sigma_{mj}}{\sigma_j}\\
&\ge \sqrt m\,\sigma_{mj}\\
&\ge
\frac{\sqrt{3/2}}{\pi j\sqrt m}.
\end{aligned}
\tag{23}
\]

Squaring gives (4).

The logarithmic form is also useful. For `q=floor(N/m)`,

\[
\boxed{
\sum_{j=q+1}^{N}-\log c_{m,j}
\le
\frac{N-q}{2}\log\frac{2\pi^2m}{3}
+
\log\frac{N!}{q!}.
}
\tag{24}
\]

Thus `NB-307`'s pivot-survival entropy cannot diverge arbitrarily fast: the reciprocal-shell arithmetic imposes a completely explicit ceiling. The ceiling is, however, still of order `N log N` in the principal moving regimes, far too large to force a macroscopic post-core gap.

## 5. Consequence for the post-core projected-dilation gap

`NB-307` proves that for

\[
2\le m\le N,
\qquad
q=\left\lfloor\frac Nm\right\rfloor,
\]

one has

\[
1-s_{\rm post}(N,m)^2
\ge
\prod_{j=q+1}^{N}c_{m,j}^2.
\tag{25}
\]

Substituting (4),

\[
\begin{aligned}
1-s_{\rm post}(N,m)^2
&\ge
\prod_{j=q+1}^{N}
\frac{3}{2\pi^2m j^2}\\
&=
\left(\frac{3}{2\pi^2m}\right)^{N-q}
\left(\frac{q!}{N!}\right)^2,
\end{aligned}
\tag{26}
\]

which is (5).

For `N/2<m<=N`, `NB-306` gives `q=1`, the exact unit core has disappeared, and `s_post(N,m)=beta_(N+1)(m)`. Equation (26) then reduces to (6).

This closes one narrow logical gap left by `NB-307`: the determinant certificate there was only formally positive because `c_(m,j)>0`; now its positivity has an explicit arithmetic size. In particular, after the exact core disappears, the projected-dilation norm is not merely strictly below one in finite dimension. Its separation from one has a fully explicit, unconditional lower bound depending only on `N` and `m`.

The bound is nevertheless much too small to settle the moving transition. For `m` comparable with `N`, the right-hand side of (6) behaves on a logarithmic scale like `-Theta(N log N)`. It therefore allows `beta_(N+1)(m)` to be extraordinarily close to one. A useful transition theorem still needs either substantially stronger collective lower survival than (4), or direct information on the generalized residual-Gram pencil `(mR,S)` from `NB-307`.

## 6. Checks and failure modes

Several indexing and inequality directions matter here.

First, equation (9) has a negative divisor indicator because the sawtooth `r_j(k)` jumps downward at multiples of `j`. Testing `n=2` and `n=3` in (12) recovers the corresponding coefficients with the stated sign.

Second, the coefficient of `u_k` in (12) receives contributions from `d=k` and `d=k+1`, which is why (13) contains both divisibility conditions. The support ends at `k=n`; no shell beyond `n` enters `L_n`.

Third, the weighted factor in (16) is exactly `k(k+1)`, the reciprocal of the shell length. Replacing it by an unweighted Euclidean coefficient norm would give the wrong functional estimate.

Fourth, the lower bound in (23) uses `sigma_j<=1`. The division direction is important: because `0<sigma_j<=1`, dividing by `sigma_j` can only increase `sqrt(m) sigma_(mj)`.

Finally, neither (1) nor (21) controls a condition number. The reciprocal pivot floor is compatible with very poor finite-section conditioning, and the determinant product in (26) can be far below the true least defect eigenvalue. No inference from this source-side nondegeneracy to target occupation is made.

## 7. Relationship to prior work

The exact reciprocal-shell formula (7) and its weighted Hilbert norm were already part of the internal development in `NB-301`--`NB-305`; `NB-014` supplies finite independence, `NB-290` supplies the multiplicative pivot coefficients, and `NB-307` supplies the post-core determinant bridge. The new step here is to invert the shell first-difference divisor relation by Möbius inversion and use the resulting coefficient functional to lower-bound each canonical pivot.

A fresh prior-art search on 2026-09-23 surfaced the standard arithmetic Nyman--Beurling literature of Báez-Duarte, work on Gram structures for generalized Nyman--Beurling criteria by Alouges--Darses--Hillion, and recent Gram-decay work of Carvill. The reviewed material confirms that Möbius arithmetic, coefficient control, and Gram geometry are natural in this setting, but the search did not identify this specific reciprocal-shell coefficient functional or the resulting `sigma_n >= const/n` canonical-pivot floor. This is an audit statement, not a claim of bibliographic novelty.

No external source is load-bearing for the proof above, so `SOURCES.md` does not require an update.

## 8. Consequences and next step

The main quantitative question created by `NB-307` was whether the product

\[
\prod_{j=q+1}^{N}c_{m,j}^2
\]

could be lower-controlled at all. `NB-308` answers that at the most basic unconditional level: yes, the shell arithmetic prevents arbitrarily catastrophic collapse and gives an explicit factorial-scale floor.

At the same time, the size of (26) shows why this alone is not the missing moving-rate theorem. The universal `1/n` pivot floor loses roughly one logarithmic unit per index, so multiplying it across an `O(N)` post-core band produces an `exp(-Theta(N log N))` certificate. Improving constants cannot change that qualitative conclusion.

The next useful source-side question is therefore sharper: determine whether the *actual collective* survival coefficients in the relevant multiplicative band are much larger than the pointwise reciprocal floor, perhaps through correlations between adjacent pivots or direct structure of the residual pencil `(mR,S)`. If no such collective improvement exists, the determinant route is quantitatively exhausted even though it is now fully explicit.

This remains separate from the target-aware bottleneck recorded in `CLUE-visible-semigroup-defect-controls-section-enrichment.md`; that clue is not resolved or consumed by the present finding.
