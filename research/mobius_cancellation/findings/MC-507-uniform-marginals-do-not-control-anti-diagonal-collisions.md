# MC-507 — Uniform marginals do not control anti-diagonal collisions

**Finding ID:** `MC-507`

**Status:** `EXACT-DERIVED` · `NEGATIVE/OBSTRUCTION` · `FRONTIER-ADVANCE` · `CLASSICAL-COUPLING+BIRKHOFF` · `PRIOR-ART-AUDITED` · `NO-GENERAL-NOVELTY-CLAIM` · `NON-RH`.

## Claim

`MC-506` reduces the varying-profile quadratic-character branch to the distribution of the physical sum coordinate

\[
t=x+j\pmod p.
\]

The next natural hope would be to control that pushforward from broad start and profile-offset marginals. This is impossible in general, even under maximally favorable marginal data.

Let \(p\) be an odd prime, let \(W>0\), and let \(\nu\) be an arbitrary probability distribution on \(\mathbf F_p\). Define the nonnegative matrix

\[
B^{\nu}_{x,j}:=\frac{W}{p}\,\nu(x+j).
\tag{1}
\]

Then all of the following hold exactly:

\[
\sum_j B^{\nu}_{x,j}=\frac Wp
\qquad\text{for every }x,
\tag{2}
\]

\[
\sum_x B^{\nu}_{x,j}=\frac Wp
\qquad\text{for every }j,
\tag{3}
\]

and the anti-diagonal pushforward from `MC-506` is

\[
\boxed{
c_t:=\sum_x B^{\nu}_{x,t-x}=W\nu(t).}
\tag{4}
\]

Thus **every** probability law on the conductor argument \(t=x+j\) is compatible with the same perfectly uniform start marginal and the same perfectly uniform profile-offset marginal. In probabilistic language, if \((X,J)\) has law \(B^{\nu}/W\), then both \(X\) and \(J\) are uniform while \(X+J\) has the arbitrarily prescribed law \(\nu\).

Consequently the collision statistic of `MC-506`,

\[
\Delta(B)
=p\sum_t\left(\frac{c_t}{W}-\frac1p\right)^2,
\tag{5}
\]

can take any value allowed by the chosen \(\nu\), from \(0\) for uniform \(\nu\) up to \(p-1\) for a point mass, while both one-dimensional marginals remain unchanged and maximally dispersed.

For every centered kernel \(F\),

\[
\mathcal C_F(B^{\nu})
=W\sum_t\nu(t)F(t),
\tag{6}
\]

so marginal equidistribution alone does not even force qualitative cancellation of the visible conductor phase.

There is a sharper isospectral obstruction. Let \(Q_{a,b}\) be the permutation matrix

\[
(Q_{a,b})_{x,j}=\mathbf1_{j=ax+b},
\qquad a\in\mathbf F_p^*,\ b\in\mathbf F_p,
\tag{7}
\]

and put

\[
B_{a,b}:=\frac Wp Q_{a,b}.
\tag{8}
\]

Every such matrix has exactly the same row and column marginals, the same number of nonzero entries, the same singular values, and the same centered nuclear and Frobenius norms. Nevertheless:

- if \(a\ne-1\), then \(t=(1+a)x+b\) is a permutation of \(\mathbf F_p\), hence \(c_t=W/p\), \(\Delta=0\), and \(\mathcal C_F(B_{a,b})=0\) for every centered \(F\);
- if \(a=-1\), then \(t=b\) identically, hence \(c_t=W\mathbf1_{t=b}\), \(\Delta=p-1\), and \(\mathcal C_F(B_{-1,b})=WF(b)\).

Therefore even the matrix summaries used as conservative certificates before `MC-506` cannot distinguish complete sum-coordinate equidistribution from maximal sum-coordinate collision when the source coupling is allowed to rotate relative to the physical sum map. The load-bearing object is the **joint coupling relative to \(x+j\)**, not either marginal and not a unitary-invariant matrix complexity statistic.

This is a representation-level no-go, not a claim that the exact first-exit source realizes these extremal couplings. The remaining arithmetic task is precisely to exploit restrictions on the physical coupling that are absent from the abstract transportation class.

## Derivation

For `(1)`, summing over one coordinate and using that translation permutes \(\mathbf F_p\) gives

\[
\sum_jB^{\nu}_{x,j}
=\frac Wp\sum_j\nu(x+j)
=\frac Wp,
\]

and similarly for the column sums. On the fibre \(x+j=t\), each of the \(p\) choices of \(x\) contributes \((W/p)\nu(t)\), proving `(4)`.

Equation `(6)` is then exactly the pushforward identity of `MC-506`.

The family `(1)` can also be written

\[
B^{\nu}
=\frac Wp\sum_{t\in\mathbf F_p}\nu(t)Q_{-1,t},
\tag{9}
\]

where \(Q_{-1,t}\) is the anti-diagonal permutation supported on \(x+j=t\). Thus arbitrary sum laws already occur inside the convex hull of scaled permutation couplings with the same uniform marginals.

For the affine permutation family `(7)`, every \(Q_{a,b}\) is unitary as a real permutation matrix. Hence

\[
\|B_{a,b}\|_*=W,
\qquad
\|B_{a,b}\|_F=\frac{W}{\sqrt p},
\qquad
\|B_{a,b}\|_{\mathrm{op}}=\frac Wp.
\tag{10}
\]

Let

\[
P=I-\frac1p\mathbf1\mathbf1^T.
\]

Because every permutation matrix fixes the constant vector and preserves its orthogonal complement,

\[
PB_{a,b}P
=\frac Wp\left(Q_{a,b}-\frac1p\mathbf1\mathbf1^T\right)
\tag{11}
\]

has singular values \(W/p\) with multiplicity \(p-1\) and zero once. Therefore

\[
\boxed{
\|PB_{a,b}P\|_*=\frac{W(p-1)}p,
\qquad
\|PB_{a,b}P\|_F=\frac{W\sqrt{p-1}}p,
}
\tag{12}
\]

independently of \(a,b\). In particular the centered nuclear interaction cost of `MC-505` is identical for the zero-collision-excess and maximal-collision-excess examples.

If \(F\not\equiv0\), choose \(b\) with \(|F(b)|=\|F\|_\infty\). Then the maximally colliding matrix has normalized bias

\[
\frac{|\mathcal C_F(B_{-1,b})|}{W}
=\|F\|_\infty
\ge
\left(\frac1p\sum_t|F(t)|^2\right)^{1/2}
=\sigma_F.
\tag{13}
\]

For the quadratic centered kernel of `MC-506`, \(\sigma_F\) is asymptotically one. Thus the abstract coupling class contains order-one-bias examples with exactly the same marginal and singular-value data as examples with identically zero bias.

## Full-support version

The obstruction is not an artifact of sparse permutation supports. For \(0<\varepsilon<1\) and any residue \(b\), take

\[
\nu_\varepsilon
=(1-\varepsilon)\delta_b+\varepsilon u,
\tag{14}
\]

where \(u\) is uniform. Then every entry of \(B^{\nu_\varepsilon}\) is strictly positive, both marginals are still uniform, and

\[
\Delta(B^{\nu_\varepsilon})
=(1-\varepsilon)^2(p-1).
\tag{15}
\]

Hence full matrix support, uniform marginal participation, and absence of empty start/profile cells still allow collision excess arbitrarily close to the maximum as \(\varepsilon\to0\).

## What this closes

This rules out a broad family of coefficient-blind continuations of the current first-exit route. None of the following can control the `MC-506` collision statistic without additional information about the **coupling** between start and offset:

- separate start equidistribution;
- separate profile-offset equidistribution;
- maximal marginal effective support;
- full support of the start-profile table;
- the singular values of the uncentered table alone;
- the centered nuclear or Frobenius norm alone.

The last point does not invalidate the bound in `MC-505`: that nuclear norm remains a valid sufficient upper-bound certificate. It shows that the certificate can be highly non-discriminating, because matrices with identical nuclear cost can have zero or maximal visible anti-diagonal collision.

The surviving question is therefore genuinely arithmetic. One must derive a restriction on how the exact first-exit source couples `x` and `j` relative to the physical map `x+j`, or directly estimate the pushforward `c_t`. Broad marginal spread is not a surrogate for that estimate.

## Prior art and novelty boundary

The general mathematics is classical. Nonnegative matrices with fixed uniform row and column marginals form the Birkhoff polytope, whose extreme points are permutation matrices by the Birkhoff--von Neumann theorem. Modern literature on copulas, dependence uncertainty, and joint mixability likewise studies how dramatically the distribution of a sum can vary while component marginals are held fixed; Wang and Wang, *Joint Mixability*, Mathematics of Operations Research 41 (2016), 808--826, DOI `10.1287/moor.2015.0755`, is a representative primary reference. The explicit finite-group construction `(1)` is elementary and no general novelty is claimed for it.

The durable line-specific contribution is the exact obstruction it creates at the `MC-506` frontier: the start and profile marginals, and even the centered singular-value data used by the previous conservative certificate, do not control the conductor argument seen by the quadratic phase. Any successful continuation must use source-derived coupling information that is destroyed by those summaries.

## Representation audit

The examples are deliberately abstract controls, not replacements for the physical first-exit source. They preserve exactly the summary statistics whose sufficiency is being tested while varying only the dependence structure relative to the kernel-visible map `x+j`.

Accordingly, the conclusion is one-way: a proof based solely on those summaries cannot establish small anti-diagonal collision excess for all admissible nonnegative tables. The finding does **not** assert that the physical Möbius source can realize an arbitrary coupling, and it does not license replacing the physical table by a convenient doubly stochastic model in the positive direction.

## Boundaries and failure modes

- **Abstract coupling control.** The extremizers need not satisfy the endpoint, sieve, quotient-fibre, or source-label constraints of the actual first-exit table.
- **No contradiction with MC-505.** The nuclear-norm estimate remains correct; identical large certificate cost can coexist with very different actual bias.
- **No sufficiency from collisions.** As in `MC-506`, excess collisions are necessary but not sufficient for large bias; the point-mass examples merely show that marginal data cannot rule them out.
- **Nonnegative coefficients.** The construction lies inside the current nonnegative branch. Signed or complex pre-aggregation coefficients have additional degrees of freedom and are not needed for this obstruction.
- **Conductor-local.** Everything is stated at one prime conductor. Outer conductor summation and global reconstruction remain separate.
- **No global Möbius conclusion.** No bound for `M(x)`, zero-free region, or RH follows.

## Consequence

`MC-506` identified the anti-diagonal pushforward as the minimal sufficient representation for the current centered conductor kernel. This finding shows why that reduction is not merely cosmetic: the discarded marginal and unitary-invariant matrix summaries are provably incapable, by themselves, of controlling the visible source law. The next useful theorem must constrain the **physical dependence of start and profile offset under addition modulo `p`**, or estimate the weighted anti-diagonal collision count directly.