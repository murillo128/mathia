# MC-470 — Empty-vector residual is a nonnegative sieve-boundary count

**Status:** `EXACT-DERIVED` · `LITERATURE+DERIVED` · `CLASSICAL-IDENTITY` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `PRIOR-ART-AUDITED` · `NO-NOVELTY-CLAIM` · `NON-RH`.

## Claim

The `r=0` empty-vector component isolated in `MC-469` has more structure than the generic residual divisor sum of `MC-458`. In Lichtman's finite linear-sieve decomposition, its residual factor is exactly the standard **upper** linear-sieve weight on the smooth block. Consequently its divisor-sum amplitude is not an oscillatory coefficient sum: it is a nonnegative integer-valued upper-sieve boundary count.

Use Lichtman's notation from (5.15). Put

\[
Q:=D^\varepsilon,
\qquad
z:=D^{\varepsilon^2}=Q^\varepsilon,
\]

and for the empty-vector component write

\[
\beta_d=\lambda^{(0)}(d)
       =\mu(d)\,\mathbf 1_{d\in\mathcal D^+(Q)}\,\mathbf 1_{d\mid P(z)},
\qquad
P(z):=\prod_{p<z}p.
\tag{1}
\]

For a positive integer `y`, define its small-prime squarefree kernel

\[
m_z(y):=\prod_{\substack{p<z\\p\mid y}}p.
\tag{2}
\]

Then

\[
B_\beta(y):=\sum_{d\mid y}\beta_d
=
\sum_{\substack{d\mid m_z(y)\\d\in\mathcal D^+(Q)}}\mu(d)
\in \mathbf Z_{\ge 0},
\tag{3}
\]

and in particular

\[
\boxed{\quad B_\beta(y)\ge \mathbf 1_{(y,P(z))=1}.\quad}
\tag{4}
\]

There is an exact boundary-count formula behind `(3)`. For a squarefree `m\mid P(z)`, let an excluded divisor be written

\[
d=p_1\cdots p_r,
\qquad
p_1>\cdots>p_r,
\]

and let `\ell` be the first index at which the upper-sieve support condition fails. For the standard support

\[
\mathcal D^+(Q)=
\left\{
 p_1\cdots p_r:
 Q^{1/2}>p_1>\cdots>p_r,
\quad
 p_1\cdots p_{j-1}p_j^3\le Q
\text{ for every odd }j\le r
\right\},
\tag{5}
\]

that first failing index is odd. Writing `a_j=p_1\cdots p_j`, finite inclusion-exclusion gives

\[
\boxed{
B_\beta(y)
=
\mathbf 1_{m=1}
+
\sum_{\substack{
\ell\ \mathrm{odd}\\
p_\ell<\cdots<p_1<z\\
a_{\ell-1}\in\mathcal D^+(Q),\ a_\ell\notin\mathcal D^+(Q)\\
a_\ell\mid m
}}
\mathbf 1_{(m,P(p_\ell))=1},
\qquad m=m_z(y).
}
\tag{6}
\]

Because `p_\ell\mid m`, the last indicator in `(6)` simply says that `p_\ell` is the least small prime divisor of `m`. Thus, away from the genuinely `z`-rough case `m=1`, `B_\beta(y)` counts odd first-exit prefixes from the Rosser--Iwaniec upper support whose final prime is the least small prime factor of `y`. Multiple such prefixes can occur, so the amplitude need not be `0` or `1`; what is exact is its nonnegativity and boundary-count interpretation.

The special relation `z=Q^\varepsilon` also gives a finite-rank exclusion. If `m=m_z(y)>1` has `k=\omega(m)` distinct prime factors and

\[
\varepsilon(k+2)\le1,
\tag{7}
\]

then every divisor `d\mid m` lies in `\mathcal D^+(Q)`, hence

\[
\boxed{\quad B_\beta(y)=0.\quad}
\tag{8}
\]

Equivalently, a non-rough value with positive residual amplitude must satisfy

\[
B_\beta(y)>0,\ m_z(y)>1
\quad\Longrightarrow\quad
\varepsilon\bigl(\omega(m_z(y))+2\bigr)>1.
\tag{9}
\]

This does **not** make the residual amplitude power-sparse. All `z`-rough values remain with weight exactly `1`, while the false-positive part is a nonnegative high-rank sieve-boundary correction. It does, however, remove one possible source of hidden oscillation from the live base-component route: any conductor-power gain in the `MC-469` empty-vector branch cannot come from sign cancellation internal to `B_{\lambda^{(0)}}` itself.

## 1. Identification of the empty-vector residual

Lichtman's decomposition first separates an integer into a rough block `p_1\cdots p_r` and a smooth block `b`. Equation (5.15) defines

\[
\lambda^{(r)}_{(D_1,\ldots,D_r)}
=
\lambda_{(D_1,\ldots,D_r)}*\lambda^{(r)},
\]

where `\lambda^{(r)}=\lambda^+` for even `r` and `\lambda^{(r)}=\lambda^-` for odd `r`, with the smooth variable restricted by

\[
b\in\mathcal D^{(r)}(D^\varepsilon),
\qquad
b\mid P(D^{\varepsilon^2}).
\tag{10}
\]

For `r=0`, the rough vector is empty and its block weight is `\delta_1`, as used in `MC-469`. Hence `(10)` becomes precisely `(1)`: the surviving residual is the standard upper linear-sieve weight `\lambda^+` at level `Q=D^\varepsilon`, restricted to primes below `z=D^{\varepsilon^2}`.

This is more specific than the generic `|\beta_s|\le1` hypothesis in `MC-458`. The generic residual divisor sum may be complex or signed; the concrete empty-vector residual is an upper-sieve majorant.

## 2. Exact first-exit decomposition

Let `m=m_z(y)`. Since `\beta_d` is squarefree and supported on `P(z)`, equation `(3)` is immediate. If `m=1`, only `d=1` contributes and `B_\beta(y)=1`.

Assume now `m>1`. Full Möbius inversion gives

\[
\sum_{d\mid m}\mu(d)=0,
\]

so

\[
B_\beta(y)
=-\sum_{\substack{d\mid m\\d\notin\mathcal D^+(Q)}}\mu(d).
\tag{11}
\]

For each excluded squarefree divisor `d=p_1\cdots p_r`, choose the first failed support index `\ell`. By `(5)`, `\ell` is odd, `a_{\ell-1}\in\mathcal D^+(Q)`, and `a_\ell\notin\mathcal D^+(Q)`. Write

\[
d=a_\ell b,
\qquad
b\mid P(p_\ell).
\]

Since `\ell` is odd,

\[
-\mu(d)=\mu(b).
\tag{12}
\]

For a fixed first-exit prefix `a_\ell`, summing all admissible tails `b` that also divide `m` gives

\[
\sum_{b\mid(m,P(p_\ell))}\mu(b)
=
\prod_{\substack{q<p_\ell\\q\mid m}}(1-1)
=
\mathbf 1_{(m,P(p_\ell))=1}.
\tag{13}
\]

Substituting `(13)` into `(11)` proves `(6)`, hence `(3)` and `(4)`. This is the same parity-tail mechanism used in Lichtman's Lemma 4.3 to prove the upper-sieve inequality for the modified support `\mathcal D^*`; here it is specialized directly to the standard `\mathcal D^+` residual that appears in the empty-vector component.

The formula also explains why positivity is compatible with multiplicities greater than one. Once `p_\ell` is forced to be the least small prime factor of `m`, several different choices of larger prime factors can form distinct first-exit prefixes, and each contributes `+1`.

## 3. Low-rank false positives vanish exactly

Suppose `m>1` has `k` distinct prime factors below `z` and `(7)` holds. For any divisor

\[
d=p_1\cdots p_r\mid m,
\qquad
p_1>\cdots>p_r,
\]

we have `r\le k`, and for every odd `j\le r`, because each `p_i<z=Q^\varepsilon`,

\[
p_1\cdots p_{j-1}p_j^3
< z^{j+2}
=Q^{\varepsilon(j+2)}
\le Q.
\tag{14}
\]

Also `p_1<z<Q^{1/2}` for the small `\varepsilon` regime used by the construction. Thus every divisor `d\mid m` belongs to `\mathcal D^+(Q)`. Equation `(3)` reduces to the complete Möbius divisor sum and vanishes, proving `(8)` and `(9)`.

The rank gate is only structural. Since `1/\varepsilon` is fixed once the sieve parameters are fixed, `(9)` is not by itself an asymptotic density estimate, and it must not be promoted to a conductor-power saving. In particular, no claim is made that the high-rank false-positive set is negligible in the affine families of the live kernel.

## 4. Consequence for the live base-component kernel

The unresolved base family in the accepted clue contains

\[
\sum_j
F_{s_0}(j)\,
B_{\lambda^{(0)}}(C_{s_0}+s_0j),
\qquad
F_{s_0}(j)
=
\chi(j+U_{s_0})
\overline{\chi(j+U_{s_0}-D_{s_0})}.
\tag{15}
\]

`MC-458` had to treat `B_\beta` as a general residual divisor-sum amplitude. For the empty-vector component, `(6)` sharpens the object: the second factor in `(15)` is a **positive sieve-boundary weight**. It supplies no internal sign cancellation that could be harvested before positive closure.

Therefore the base branch has only three remaining ways to obtain a strict conductor-power gain:

1. prove cancellation of the translated-character phase `F_{s_0}` **against** the positive rough/boundary weight in the actual affine family;
2. exploit signed cancellation in the outer aggregated coefficients `\widetilde\beta(s_0)` before taking absolute values; or
3. retain the signed finite decomposition and obtain genuine cross-component interference, as already separated in the accepted clue.

A proof that merely invokes alternating signs of the upper-sieve coefficients inside `B_{\lambda^{(0)}}` as an additional oscillatory resource is invalid after `(6)`: those signs have already recombined pointwise into a nonnegative boundary count. Conversely, `(6)` does **not** justify replacing the amplitude by `1`, by the roughness indicator, or by a density heuristic. The high-rank boundary correction is real and can have multiplicity, and its correlation with `F_{s_0}` remains an open quantitative problem.

This is a genuine narrowing of the empty-vector branch, not a closure of it.

## 5. Prior art and novelty boundary

The upper linear-sieve support `(5)`, the weights `\lambda^\pm(d)=\mu(d)\mathbf 1_{d\in\mathcal D^\pm}`, and the decomposition `(10)` are classical/standard sieve structures as presented explicitly in Jared Duker Lichtman, *A modification of the linear sieve, and the count of twin primes*, Algebra & Number Theory 19 (2025), no. 1, 1--38, DOI `10.2140/ant.2025.19.1`, arXiv `2109.02851`. In that paper, equation (3.1) gives `\mathcal D^+`, equation (5.15) gives the smooth residual `\lambda^{(r)}`, and Lemma 4.3 proves the same minimal-excluded-index parity mechanism for the modified upper support `\mathcal D^*`. Equation (4.4) records the corresponding standard `\mathcal D^+` first-exit decomposition at the sieve main-term level.

Accordingly, no novelty is claimed for upper-sieve positivity, Rosser--Iwaniec first-exit combinatorics, or the fact that the divisor sum majorizes roughness. The Mathia delta is narrower: `MC-469` exposed the unavoidable `r=0` cell in the live staged character kernel, and `(3)`--`(9)` identify exactly what its previously unresolved residual amplitude is allowed to do. The amplitude is a nonnegative least-small-prime boundary count with an exact low-rank vanishing rule, not a generic signed divisor sum.

A fresh literature search on 22 September 2026 found the expected general upper-sieve/linear-sieve treatments and character-sum literature, but no theorem that directly estimates the specific translated rational-character phase in `(15)` against this affine upper-sieve boundary weight. That absence is not a novelty claim; the quantitative joint estimate remains to be derived or falsified.

## Boundaries and falsification tests

- **No character-sum gain is proved.** Positivity classifies the residual amplitude; it does not estimate `(15)`.
- **Nonnegative does not mean constant.** `B_{\lambda^{(0)}}` can exceed `1`; distinct first-exit prefixes can contribute to the same `y`.
- **Rough values survive.** If `(y,P(z))=1`, then `B_{\lambda^{(0)}}(y)=1`. Support pruning cannot remove the entire base channel.
- **The high-rank gate is not a density theorem.** Condition `(9)` is necessary for non-rough false positives but does not say they are rare enough for a power saving.
- **Affine concentration remains load-bearing.** Divisibility conditions in `(6)` can correlate with the step `s_0` and offset `C_{s_0}`. Unrestricted sieve densities or the global `L^2` bound from `MC-458` do not transfer automatically.
- **Expanding the boundary count too early reopens the old product variables.** Formula `(6)` is a structural audit, not permission to triangle-bound each prefix and then claim a factor-specific gain; the `MC-458`/`MC-467` tariffs still apply after such an expansion.
- **Outer and cross-component signs remain live.** The result removes only sign cancellation internal to the base residual amplitude. It does not remove cancellation in `\widetilde\beta(s_0)` or between signed finite components retained before positive closure.

## Consequence for the research line

The accepted staged-sieve clue should no longer ask whether the empty-vector residual has useful *coefficient-sign* cancellation. It does not: pointwise recombination turns the upper-sieve coefficients into the nonnegative boundary count `(6)`.

The next decisive base-component test is therefore more specific: estimate the translated-character phase against the positive `z`-rough plus high-rank first-exit boundary weight on the exact affine trajectories, while separately accounting for outer `s_0` signs and the near-complete endpoint. A conductor-power saving must come from that joint arithmetic interaction or from cross-component interference, not from hidden oscillation of `B_{\lambda^{(0)}}` itself.

No improved bound for `M(x)`, no zero-free region, and no RH consequence follows.