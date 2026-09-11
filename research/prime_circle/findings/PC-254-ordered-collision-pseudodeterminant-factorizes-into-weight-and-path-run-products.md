# PC-254 — ordered collision pseudodeterminant factorizes into weight and path-run products

**Status:** `EXACT-DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-NEGATIVE` for determinant/log-volume compression of the ordered shared-upper collision carrier left open by PC-253. Let `2<p<r<q` be distinct primes and let

\[
D_{p,r;q}=K_{p,q}^{*}K_{r,q}-qK_{p,r}^{T}
\]

be the PC-251 shared-upper defect. PC-251 writes this defect as a weighted matching of lower-grid path incidences. Keeping the full ordering of that matching does retain more information than the scalar rank and unordered weight packet classicalized in PC-253, but its natural pseudodeterminant does not create a new global spectral invariant. If the `k` collision pairs are ordered increasingly as

\[
(i_1,j_1),\ldots,(i_k,j_k),
\qquad i_1<\cdots<i_k,
\]

then automatically `j_1<\cdots<j_k`. Writing `w_a>0` for the integral PC-251 weight of the `a`th collision, the product of the nonzero singular values of `D_{p,r;q}` is exactly

\[
\boxed{
\prod_{a=1}^{k}\sigma_a(D_{p,r;q})
=
\left(\prod_{a=1}^{k}w_a\right)
\sqrt{
\prod_{R\in\mathcal R_p}(|R|+1)
\prod_{S\in\mathcal R_r}(|S|+1)
},
}
\tag{1}
\]

where `mathcal R_p` is the set of maximal runs of consecutive indices among `i_1,...,i_k`, and `mathcal R_r` is the analogous run decomposition of `j_1,...,j_k`. Equivalently,

\[
\boxed{
\operatorname{pdet}(D_{p,r;q}D_{p,r;q}^{*})
=
\left(\prod_{a=1}^{k}w_a^2\right)
\prod_{R\in\mathcal R_p}(|R|+1)
\prod_{S\in\mathcal R_r}(|S|+1).
}
\tag{2}
\]

Thus the determinant-style compression of the remaining ordered matching contains only the product of the already-classical collision weights and elementary path-run factors. It has no cancellation, phase, complex parameter, or hidden zero divisor. This does **not** classify the complete singular-value distribution or arbitrary nonlinear/multi-upper-scale observables; it closes the specific determinant/log-volume escape.

## 1. The PC-251 collision matching is order preserving

PC-251 gives the exact factorization

\[
D_{p,r;q}
=-\sum_{a=1}^{k}
 w_a\,\delta_{i_a}^{(p)}\bigl(\delta_{j_a}^{(r)}\bigr)^T,
\qquad
\delta_i^{(p)}=e_{i-1}-e_i,
\tag{3}
\]

with

\[
w_a
=pr\,G\!\left(\frac{a_{i_a}}p,\frac{b_{j_a}}r\right)
\in\mathbb Z_{>0}.
\tag{4}
\]

A collision means

\[
\left\lfloor\frac{qi_a}{p}\right\rfloor
=
\left\lfloor\frac{qj_a}{r}\right\rfloor.
\tag{5}
\]

If `i<i'`, then

\[
\frac{q(i'-i)}p>1
\]

because `q>p`. Hence

\[
\left\lfloor\frac{qi'}p\right\rfloor
>
\left\lfloor\frac{qi}p\right\rfloor.
\tag{6}
\]

The same strict monotonicity holds for `j -> floor(qj/r)` because `q>r`. Therefore two collision pairs satisfy

\[
i<i'\quad\Longleftrightarrow\quad j<j'.
\tag{7}
\]

The PC-251 matching is consequently a **monotone matching** between selected edges of the length-`p` and length-`r` paths. No crossing permutation remains after the collision cells are ordered.

## 2. The complete nonzero singular spectrum lives in two selected-path Gram matrices

Collect the selected incidence columns into

\[
U=
\begin{bmatrix}
\delta_{i_1}^{(p)}&\cdots&\delta_{i_k}^{(p)}
\end{bmatrix}
\in\mathbb R^{p\times k},
\]

\[
V=
\begin{bmatrix}
\delta_{j_1}^{(r)}&\cdots&\delta_{j_k}^{(r)}
\end{bmatrix}
\in\mathbb R^{r\times k},
\qquad
W=\operatorname{diag}(w_1,\ldots,w_k).
\tag{8}
\]

Then (3) is simply

\[
\boxed{D_{p,r;q}=-UWV^T.}
\tag{9}
\]

Define the two collision Gram matrices

\[
G_p:=U^TU,
\qquad
G_r:=V^TV.
\tag{10}
\]

Because distinct edge-incidence columns of a path are linearly independent, both matrices are positive definite. Their entries are completely explicit:

\[
(G_p)_{ab}
=
\begin{cases}
2,&a=b,\\
-1,&|i_a-i_b|=1,\\
0,&\text{otherwise},
\end{cases}
\tag{11}
\]

and the identical formula with `i` replaced by `j` holds for `G_r`. Order preservation (7) means any nonzero off-diagonal entry occurs between neighboring collision labels. Hence both `G_p` and `G_r` are tridiagonal with breaks.

Now

\[
D_{p,r;q}D_{p,r;q}^{*}
=
UWG_rWU^T.
\tag{12}
\]

Using the standard fact that `AB` and `BA` have the same nonzero eigenvalues, the `k` positive squared singular values of `D_{p,r;q}` are exactly the eigenvalues of

\[
\boxed{WG_rWG_p.}
\tag{13}
\]

Although (13) is not symmetric as written, it is similar to the positive-definite matrix

\[
G_p^{1/2}WG_rWG_p^{1/2}.
\tag{14}
\]

Thus even the **complete** singular spectrum has already collapsed from the original `p x r` defect to a `k x k` product of two selected-path Gram matrices and the positive diagonal collision weights. Equation (13) does not by itself classicalize all of those eigenvalues, but it makes the exact one-dimensional carrier explicit.

## 3. Path runs make the pseudodeterminant elementary

Let

\[
I=\{i_1,\ldots,i_k\}\subset\{1,\ldots,p-1\}.
\]

Split `I` into maximal runs of consecutive integers. If one run has length `L`, its block in `G_p` is

\[
T_L=
\begin{pmatrix}
2&-1&&\\
-1&2&\ddots&\\
&\ddots&\ddots&-1\\
&&-1&2
\end{pmatrix}.
\tag{15}
\]

The elementary determinant recurrence

\[
d_L=2d_{L-1}-d_{L-2},
\qquad d_0=1,\quad d_1=2,
\tag{16}
\]

gives

\[
\det T_L=L+1.
\tag{17}
\]

Therefore

\[
\boxed{
\det G_p
=
\prod_{R\in\mathcal R_p}(|R|+1),
\qquad
\det G_r
=
\prod_{S\in\mathcal R_r}(|S|+1).
}
\tag{18}
\]

Taking determinants in (13),

\[
\prod_{a=1}^{k}\sigma_a(D_{p,r;q})^2
=
\det(WG_rWG_p)
=
(\det W)^2\det G_p\det G_r.
\tag{19}
\]

Since every collision weight is strictly positive, equations (18)--(19) prove (1)--(2). No sign choice or square-root ambiguity enters: all factors on the right are positive.

For the native normalization of PC-251,

\[
\Delta_{p,r;q}
=\frac{D_{p,r;q}}{q\sqrt{pr}},
\tag{20}
\]

one obtains the equally explicit formula

\[
\boxed{
\operatorname{pdet}(\Delta_{p,r;q}\Delta_{p,r;q}^{*})
=
(q^2pr)^{-k}
\left(\prod_{a=1}^{k}w_a^2\right)
\prod_{R\in\mathcal R_p}(|R|+1)
\prod_{S\in\mathcal R_r}(|S|+1).
}
\tag{21}
\]

Consequently the logarithmic volume is additive:

\[
\log\operatorname{pdet}(\Delta\Delta^*)
=
2\sum_a\log w_a
+
\sum_R\log(|R|+1)
+
\sum_S\log(|S|+1)
-k\log(q^2pr).
\tag{22}
\]

Any determinant or log-determinant proposal based only on the nonzero collision volume therefore discards the remaining ordered matching down to local weights, two run-length multisets, and the rank `k`.

## 4. Exact control: `(p,r,q)=(7,11,13)`

The collision pairs are

\[
(1,1),(2,3),(3,5),(4,6),(5,8),(6,10),
\tag{23}
\]

with weights

\[
2,12,4,4,12,2.
\tag{24}
\]

The `p`-indices form one run of length `6`, while the `r`-indices have run lengths

\[
1,1,2,1,1.
\tag{25}
\]

Hence

\[
\det G_p=7,
\qquad
\det G_r=2\cdot2\cdot3\cdot2\cdot2=48,
\qquad
\prod_a w_a=9216.
\tag{26}
\]

Equations (1)--(2) give

\[
\prod_a\sigma_a(D)
=9216\sqrt{7\cdot48}
=36864\sqrt{21},
\tag{27}
\]

and

\[
\operatorname{pdet}(DD^*)
=28\,538\,044\,416.
\tag{28}
\]

Direct construction from the six `2 x 2` incidence outer products in (3) gives the same value. The example also shows why the run factors are real information beyond the unordered weights: one side is one long selected-edge run while the other has four isolated edges and one two-edge run. Nevertheless their determinant contribution is only the elementary factor `7 x 48`.

## 5. Prior-art and novelty audit

The ambient linear algebra is classical. For an oriented graph incidence matrix, incidence Gram matrices and graph Laplacians are standard objects; selected edges of a path produce the tridiagonal Dirichlet path matrix (15), and its determinant `L+1` is elementary spectral-graph theory. Standard references include Chris Godsil and Gordon Royle, **Algebraic Graph Theory**, Graduate Texts in Mathematics 207, Springer (2001), especially the Laplacian/incidence-matrix framework, and Fan Chung, **Spectral Graph Theory**, CBMS 92, AMS (1997). Gram determinants and the identity between nonzero spectra of `AB` and `BA` are ordinary matrix theory. No novelty is claimed for any of those ingredients.

The project-local content is the exact consequence for the PC-251/PC-253 carrier: once the source-forced shared-upper defect has reduced to its monotone weighted collision matching, the natural determinant of its nonzero spectral sector is forced to factor as (2). A targeted search for incidence-matrix pseudodeterminants, path Laplacians, Gram determinants, and weighted matching factorizations found the expected classical graph/matrix machinery, not a distinct zeta or RH-specific determinant attached to this Prime-Circle packet. The conclusion therefore does not rely on an absence-of-literature claim.

The matched-control test remains negative for prime specificity. PC-251 already shows that the complete weighted matching (3) is reproduced by the corresponding uniform rational-partition construction for admissible pairwise-coprime non-prime labels. Equations (7)--(22) use only that matching, path incidences, positive weights, and finite-dimensional linear algebra. The pseudodeterminant factorization is consequently reproduced by the same source-blind controls.

## 6. RH-facing consequence and remaining boundary

PC-253 left the **ordered weighted matching** as a narrower survivor after scalar collision rank and unordered weight statistics had classicalized to moving rational-lattice data. PC-254 now rules out the most natural determinant compression of that survivor. The positive spectral volume has no cancellation mechanism: after normalization it is exactly (21), and its logarithm is the additive local expression (22). Introducing a complex variable by replacing these positive factors with an arbitrary Mellin or resolvent wrapper would add external analytic structure rather than derive a zeta zero detector from the collision geometry.

This is deliberately not a no-go for the complete ordered matching. The individual singular values in (13) still depend on the interleaving of the two selected-path adjacency patterns with `W`; the characteristic polynomial `det(lambda I-WG_rWG_p)`, resolvent data, nonlinear combinations of several independent upper scales, and operators that retain more than one pairwise shared-upper defect are not classified by (2). A future positive mechanism would therefore have to use such information before determinant/log-volume compression and still pass the matched-control and prior-art gates of the Prime-Circle mandate.

The decisive audit is finite and exact: reconstruct the PC-251 collision set and weights, order the collision pairs, form `U`, `V`, and `W`, verify (9), compute `G_p=U^TU` and `G_r=V^TV`, identify their consecutive-index runs, and compare the positive eigenvalue product of `DD^*` against (2). Any counterexample to (7), (18), or (19) falsifies the finding; otherwise the determinant/log-volume route is completely reduced as stated.
