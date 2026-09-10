# PC-250 — three-prime transfer defect is full-rank but collapses to pairwise residue data

**Status:** `EXACT-DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-BOUNDARY` for the several-independent-upper-level escape left open by PC-248/PC-249. Let `p<q<r` be distinct primes and let `K_{a,b}` denote the native prime-prime transfer packets of PC-245/PC-246. The normalized two-step-versus-direct transfer defect

\[
E_{p,q,r}
:=\frac{K_{q,r}}{\sqrt{qr}}\frac{K_{p,q}}{\sqrt{pq}}
-\frac{K_{p,r}}{\sqrt{pr}}
\tag{1}
\]

has the maximal possible rank on the nonconstant lower-shell sector:

\[
\boxed{\operatorname{rank}E_{p,q,r}=p-1.}
\tag{2}
\]

Thus coupling two independent upper levels before contraction does produce genuine finite-scale relational information that is absent from one pairwise Gram packet. However, with `p,q` fixed and `r\to\infty`, its complete fixed-domain Gram matrix converges in operator norm to exactly the PC-246 weighted-path residue packet:

\[
\boxed{
E_{p,q,r}^{*}E_{p,q,r}
\longrightarrow
\frac{1}{pq}L_{p,h},
\qquad h\equiv q\pmod p.
}
\tag{3}
\]

Moreover the convergence is one-sided and admits the explicit bound

\[
0\le \frac{1}{pq}L_{p,h}-E_{p,q,r}^{*}E_{p,q,r},
\qquad
\left\|\frac{1}{pq}L_{p,h}-E_{p,q,r}^{*}E_{p,q,r}\right\|
\le \frac{16p(p-1)}{r}.
\tag{4}
\]

Consequently the extra `r`-dependence is a real finite-mesh effect but not a durable new all-scale carrier in the fixed-`(p,q)` limit. After the third level resolves the circle, the surviving singular spectrum is determined by the same signed residue `q mod p` already classicalized in PC-246/PC-247, apart from the elementary scale `pq`.

## 1. Native prime packets are cross-projections between uniform partitions

Work in `L^2([0,1])`. Let `U_n` be the `n`-dimensional subspace of functions constant on the uniform cells

\[
I_t^{(n)}=[t/n,(t+1)/n),
\qquad 0\le t<n,
\tag{5}
\]

and let `P_n` be the orthogonal projection onto `U_n`. The canonical orthonormal cell basis is

\[
e_t^{(n)}=\sqrt n\,1_{I_t^{(n)}}.
\tag{6}
\]

For primes `a<b`, PC-246 proves that the native transfer packet is the integer overlap matrix of the `a`- and `b`-block partitions of an `ab`-point interval. After scaling that interval to `[0,1]`,

\[
K_{a,b}(u,t)=ab\,|I_u^{(b)}\cap I_t^{(a)}|.
\tag{7}
\]

Hence its normalized form

\[
S_{a,b}:=\frac{K_{a,b}}{\sqrt{ab}}
\tag{8}
\]

has entries

\[
S_{a,b}(u,t)
=\langle e_u^{(b)},e_t^{(a)}\rangle.
\tag{9}
\]

Therefore `S_{a,b}` is exactly the coordinate matrix of

\[
P_b|_{U_a}:U_a\longrightarrow U_b.
\tag{10}
\]

This representation is source-forced by the prime all-one cyclotomic masks; no new operator has been inserted.

## 2. The three-level composition defect is a projection defect

For `p<q<r`, matrix multiplication in the canonical cell bases gives

\[
S_{q,r}S_{p,q}
\longleftrightarrow
P_rP_q|_{U_p},
\tag{11}
\]

while the direct packet gives

\[
S_{p,r}
\longleftrightarrow
P_r|_{U_p}.
\tag{12}
\]

Thus (1) has the exact operator form

\[
\boxed{
E_{p,q,r}
\longleftrightarrow
-P_r(I-P_q)|_{U_p}.
}
\tag{13}
\]

Equivalently, in integer packet coordinates define

\[
C_{p,q,r}:=K_{q,r}K_{p,q}-qK_{p,r}.
\tag{14}
\]

Then

\[
\boxed{
E_{p,q,r}=\frac{C_{p,q,r}}{q\sqrt{pr}}.
}
\tag{15}
\]

The direct and two-step native transfers therefore fail to compose transitively precisely by the component lost when the intermediate uniform conditional-expectation/projection `P_q` is imposed and then sampled at level `r`.

## 3. Exact maximal-rank theorem

The constants lie in the kernel of (13), so `rank E<=p-1`. The point is that there is no further kernel.

Take `f\in U_p`, with constant values `x_0,...,x_{p-1}` on the `p` cells, and put

\[
h:=(I-P_q)f.
\tag{16}
\]

Because `q>p`, a `q`-cell contains at most one interior `p`-boundary. Because `(p,q)=1`, no interior `p`-boundary `k/p` lies on the `q`-grid. Hence the `p-1` boundaries `k/p`, `1<=k<p`, lie in `p-1` distinct active `q`-cells. On every other `q`-cell, `f` is already constant and `h=0`.

In the active `q`-cell containing `k/p`, the function `h` is a two-step mean-zero wavelet. Its amplitude is proportional to the jump

\[
\Delta_k:=x_k-x_{k-1}.
\tag{17}
\]

Let

\[
H(x):=\int_0^x h(t)\,dt.
\tag{18}
\]

Since each active wavelet has mean zero on its whole `q`-cell, `H` vanishes at every `q`-grid endpoint. Inside an active cell, if `\Delta_k\ne0`, `H` is a nonzero triangular tent: it is linear from zero to a nonzero extremum at `k/p`, then linear back to zero, and therefore has no zero in the open cell.

Assume now that `P_rh=0`. The average of `h` on every `r`-cell then vanishes. Starting from `H(0)=0`, this implies

\[
H(v/r)=0,
\qquad 0\le v\le r.
\tag{19}
\]

But `r>q`, so the spacing `1/r` is strictly smaller than the length `1/q` of every active `q`-cell. Every open active `q`-cell therefore contains an interior `r`-grid point. Equation (19) is incompatible with a nonzero triangular tent. Hence every `\Delta_k=0`, so `f` is constant.

Thus

\[
\ker\bigl(P_r(I-P_q)|_{U_p}\bigr)
=\operatorname{span}\{1\},
\tag{20}
\]

and (2) follows. This is an exact finite-level statement: the two-step relational defect is not low rank, not a single boundary scalar, and not annihilated by retaining the intermediate upper level.

The proof actually needs only `(p,q)=1`, `p<q<r`, and uniform all-one masks. Hence for arbitrary coprime integers `p<q` with the same artificial uniform masks and any integer `r>q`, the same rank `p-1` holds. This matched control shows that maximal rank itself is partition geometry, not a prime discriminator.

## 4. The third level disappears in the fixed-`(p,q)` continuum limit

Although the finite defect has full mean-zero rank, its normalized spectral content simplifies when the final mesh is refined. Set

\[
A_{p,q}:=(I-P_q)|_{U_p}.
\tag{21}
\]

Equation (13) gives

\[
E_{p,q,r}^{*}E_{p,q,r}
=A_{p,q}^{*}P_rA_{p,q}.
\tag{22}
\]

The uniform-cell projections satisfy `P_r g\to g` in `L^2([0,1])` for every fixed `g` as `r\to\infty`. Since `U_p` is finite dimensional, the convergence is uniform on its unit sphere after applying the fixed map `A_{p,q}`. Therefore

\[
E_{p,q,r}^{*}E_{p,q,r}
\longrightarrow
A_{p,q}^{*}A_{p,q}
=P_p(I-P_q)P_p
\tag{23}
\]

in operator norm on `U_p`.

Now invoke the exact PC-246 pairwise Gram identity

\[
K_{p,q}^{*}K_{p,q}
=pqI_p-L_{p,h},
\qquad h\equiv q\pmod p.
\tag{24}
\]

Using `S_{p,q}=K_{p,q}/sqrt(pq)`, the matrix of `P_pP_qP_p` on `U_p` is

\[
S_{p,q}^{*}S_{p,q}
=I_p-\frac{1}{pq}L_{p,h}.
\tag{25}
\]

Substituting into (23) proves (3):

\[
\boxed{
A_{p,q}^{*}A_{p,q}
=\frac{1}{pq}L_{p,h}.
}
\tag{26}
\]

Thus every limiting squared singular value of the three-level defect is

\[
\frac{\lambda_j(L_{p,h})}{pq},
\qquad 0\le j<p,
\tag{27}
\]

with exactly one zero mode. PC-246 already proves that the complete centered spectral data of `L_{p,h}` are equivalent to `h=q mod p` up to `h<->p-h`. The final prime `r` supplies no additional limiting arithmetic variable.

## 5. Quantitative one-sided convergence

The convergence above is not merely qualitative. On an active `q`-cell the local two-step wavelet in (16) has total variation exactly `2|Delta_k|`; summing over the active cells gives

\[
\operatorname{Var}(h)
\le2\sum_{k=1}^{p-1}|\Delta_k|.
\tag{28}
\]

By Cauchy-Schwarz and the elementary path-difference estimate,

\[
\sum_{k=1}^{p-1}|\Delta_k|
\le\sqrt{p-1}\left(\sum_k|\Delta_k|^2\right)^{1/2},
\qquad
\sum_k|\Delta_k|^2
\le4\sum_{t=0}^{p-1}|x_t|^2.
\tag{29}
\]

Since `||f||_2^2=p^{-1}sum_t|x_t|^2`,

\[
\operatorname{Var}((I-P_q)f)
\le4\sqrt{p(p-1)}\,\|f\|_2.
\tag{30}
\]

For any bounded-variation function `g`, cellwise averaging on the uniform `r`-partition satisfies

\[
\|(I-P_r)g\|_2^2
\le\frac{\operatorname{Var}(g)^2}{r}.
\tag{31}
\]

Indeed, on each cell the squared deviation from its mean is at most the cell length times the squared oscillation, while the sum of cell oscillations is at most the total variation. Applying (31) to (30) yields

\[
\|(I-P_r)A_{p,q}\|^2
\le\frac{16p(p-1)}r.
\tag{32}
\]

Finally,

\[
\begin{aligned}
A_{p,q}^{*}A_{p,q}-E_{p,q,r}^{*}E_{p,q,r}
&=A_{p,q}^{*}(I-P_r)A_{p,q}\\
&=((I-P_r)A_{p,q})^{*}((I-P_r)A_{p,q})\ge0.
\end{aligned}
\tag{33}
\]

Equations (26), (32), and (33) prove (4). Each finite-`r` Gram lies below its PC-246 limiting Gram in Loewner order, even though the projections `P_r` are not nested as `r` varies.

## 6. Exact finite controls

For `(p,q,r)=(3,5,7)`, direct integer overlap arithmetic gives

\[
C_{3,5,7}
=
\begin{pmatrix}
0&0&0\\
-3&3&0\\
3&-3&0\\
0&0&0\\
0&-3&3\\
0&3&-3\\
0&0&0
\end{pmatrix},
\tag{34}
\]

which has rank `2=p-1`. The exact limiting Gram from (26) has eigenvalues

\[
\left\{0,\frac{2}{15},\frac25\right\}.
\tag{35}
\]

At `r=7`, the finite Gram has eigenvalues

\[
\left\{0,\frac{6}{175},\frac{18}{175}\right\},
\tag{36}
\]

all below the corresponding limiting eigenvalues as required by (33). The rank remains maximal even though the finite spectrum has not yet approached its limit closely.

The matched nonarithmetic control is stronger than a numerical surrogate: replace the prime masks by all-one masks at arbitrary coprime integers `p<q` and any `r>q`. The entire projection representation, kernel argument, and limit remain valid. Thus neither the full-rank defect nor its convergence is caused by primality. Prime cyclotomy makes this uniform-partition system canonical at prime levels; the arithmetic dependence that survives the limit is exactly the pairwise modular residue already identified in PC-246.

## 7. Prior-art and novelty audit

The ambient functional analysis is classical. Conditional expectation with respect to a finite partition is the orthogonal `L^2` projection onto the corresponding step-function subspace. Products, relative positions, and spectra of pairs of orthogonal projections belong to the classical two-subspace theory initiated by P. R. Halmos, **Two subspaces**, *Transactions of the American Mathematical Society* 144 (1969), 381-389, DOI `10.1090/S0002-9947-1969-0251519-5`. A modern projection/principal-angle treatment is A. Galantai, **Subspaces, angles and pairs of orthogonal projections**, *Linear and Multilinear Algebra* 56:3 (2008), 227-260, DOI `10.1080/03081080600743338`.

No novelty is claimed for orthogonal projections, conditional expectations, principal-angle/product-of-projection geometry, uniform step-function approximation, or the bounded-variation estimate. The all-one polyphase/interval-overlap representation is already established locally by PC-245/PC-246.

The project-local delta is narrower. The first source-forced **three-prime native transfer composition** that retains two upper levels before contraction has a sharp and somewhat deceptive information profile: its finite defect has maximal possible rank `(p-1)`, but after canonical normalization and final-mesh refinement its entire fixed-domain Gram converges to the same one-residue weighted path `L_{p,h}` that controls the pairwise packet. The negative RH consequence therefore does not rest on a literature-absence claim; it follows from the exact projection identity (13), the kernel theorem (20), and the limit identity (26).

## 8. Research consequence and strict boundary

This finding closes the most direct fixed-`(p,q)` version of the PC-249 escape

\[
\text{prime }p
\to q
\to r
\quad\text{versus}\quad
p\to r,
\tag{37}
\]

when the observable is the canonically normalized two-step transfer defect and the final upper prime alone tends to infinity. Merely observing that the three-level defect is nonzero or even full-rank would have been misleading: the extra finite-scale relation is progressively resolved away by `P_r`, and the limiting singular spectrum returns exactly to pairwise signed-residue data.

The theorem deliberately does **not** close joint growth such as `p=p(r)` or `q=q(r)`, where the domain dimension and intermediate mesh change and the bound (4) may fail to vanish after normalization. It also does not close networks with several upper levels coupled in a non-chain graph before contraction, native composite cyclotomic masks, row-coordinate-sensitive observables whose coordinate dependence is proved intrinsic, or infinite-dimensional/source-forced limits taken before fixing the lower spaces. Those are materially different from the fixed-`(p,q)` continuum limit proved here.

There is no new bridge to the Riemann zeros in this three-prime chain. The useful result is the exact separation between **finite relational information gain** and **durable all-scale information gain**: maximal finite rank is insufficient, and the next survivor must keep a genuinely growing relational variable alive in the limiting topology rather than allowing the last mesh projection to converge to the identity.

## Falsification checks

The result can be audited without numerical fitting. First verify the PC-246 overlap normalization (7)-(10). Then multiply the normalized packet matrices and check (13)-(15). For the rank theorem, any nonconstant kernel vector would produce at least one nonzero jump `Delta_k`; its active `q`-cell gives a triangular primitive `H` with no interior zero, while `P_rh=0` forces zeros at every `r`-grid point. Since `1/r<1/q`, this is impossible.

For the limiting statement, compute `E^*E` as in (22), use strong convergence of uniform cell-average projections on `L^2` plus finite dimensionality of `U_p`, and substitute the exact PC-246 identity (24). For the quantitative bound, verify the local variation `2|Delta_k|`, the path estimate (29), and the cellwise oscillation inequality (31). Any failure of (13), kernel equality (20), or Gram limit (26) changes the conclusion; otherwise the fixed-lower three-prime chain is exactly classified as above.