# PC-256 — fixed-depth multi-upper trace words are finite shifted collision correlations

**Status:** `EXACT-DERIVED` + `PRIOR-ART-CLASSICALIZATION` + `DECISIVE-NEGATIVE` for the fixed-depth nonquadratic trace-word escape left open by PC-255. Fix distinct lower primes

\[
2<p<r
\]

and let every upper level `q>r` be prime. Write

\[
D_q:=D_{p,r;q}=K_{p,q}^{*}K_{r,q}-qK_{p,r}^{T}
\]

for the PC-251 shared-upper defect. PC-255 proved that the first quadratic multi-upper contraction `tr(D_q D_s^*)` is a seven-shift correlation of scalar determinant-layer packets, while leaving nonquadratic mixed words open. The same collapse in fact persists at **every fixed word length**.

There are two finite, upper-level-independent shift kernels `kappa_p,kappa_r`, each supported on at most twelve integer shifts, such that for every fixed even word

\[
T(q_1,\ldots,q_{2m})
:=\operatorname{tr}\!\left(
D_{q_1}D_{q_2}^{*}\cdots D_{q_{2m-1}}D_{q_{2m}}^{*}
\right)
\]

one has an exact expansion as at most `12^(2m)` scalar shifted correlations of the PC-253 collision packets. In particular, for one upper level,

\[
\operatorname{tr}\bigl((D_qD_q^*)^m\bigr)
=\sum_j \sigma_j(D_q)^{2m}
\]

is a finite shifted autocorrelation for every fixed `m`. Thus neither higher fixed spectral moments nor fixed-depth noncommutative multi-upper trace words produce a new matrix-level arithmetic carrier. The only spectral escape left inside this family must use depth growing with the collision rank, the full non-polynomial spectral object, an untraced matrix-valued coupling, or an operation applied before the PC-251 rational-partition compression.

## 1. A universal determinant-layer dictionary

Put

\[
H_p:=\{h\in\mathbb Z:0<|h|<p\}.
\]

For every `h in H_p`, the Diophantine equation

\[
ri-pj=h
\]

has a unique solution with

\[
1\le i<p,\qquad 1\le j<r.
\]

Indeed,

\[
i_h=\langle r^{-1}h\rangle_p,
\qquad
j_h=\frac{ri_h-h}{p}.
\]

This dictionary depends only on the lower pair `(p,r)`, not on the upper prime. PC-253 shows that every active collision layer of every `D_q` lies in `H_p`. Extend its collision-weight packet by zero and write

\[
c_q(h)=
\begin{cases}
 w_q(i_h,j_h),& (i_h,j_h)\in\mathcal C_{p,r;q},\\
 0,&\text{otherwise},
\end{cases}
\qquad h\in H_p,
\]

and set `c_q(h)=0` outside `H_p` as well. With

\[
u_h:=\delta_{i_h}^{(p)},
\qquad
v_h:=\delta_{j_h}^{(r)},
\]

PC-251 becomes

\[
\boxed{
D_q=-\sum_{h\in H_p}c_q(h)u_hv_h^T.
}
\tag{1}
\]

Let `U` and `V` be the matrices with columns `u_h` and `v_h`, indexed by `H_p`, and let

\[
C_q:=\operatorname{diag}(c_q(h))_{h\in H_p}.
\]

Then

\[
\boxed{D_q=-UC_qV^T.}
\tag{2}
\]

The representation is deliberately redundant: different determinant layers can use the same lower path edge when one moves between different upper levels. That redundancy is useful because it puts every upper packet on one common scalar coordinate.

## 2. Pulling both path Grams back to determinant layers gives finite convolution stencils

Define

\[
A_p:=U^TU,
\qquad
A_r:=V^TV.
\]

For a path-incidence edge,

\[
\langle\delta_a,\delta_b\rangle
=\alpha_{b-a},
\qquad
\alpha_0=2,\quad
\alpha_{\pm1}=-1,\quad
\alpha_t=0\ (|t|>1).
\tag{3}
\]

The non-obvious point is that after the determinant-layer relabeling, `A_p` and `A_r` are still translation kernels. Define

\[
\kappa_p(d)=
\begin{cases}
\alpha_\varepsilon,
&d=r\varepsilon-p\eta,\quad
\varepsilon\in\{-1,0,1\},\ \eta\in\mathbb Z,\\
0,&\text{otherwise},
\end{cases}
\tag{4}
\]

and

\[
\kappa_r(d)=
\begin{cases}
\alpha_\eta,
&d=r\varepsilon-p\eta,\quad
\eta\in\{-1,0,1\},\ \varepsilon\in\mathbb Z,\\
0,&\text{otherwise}.
\end{cases}
\tag{5}
\]

Only shifts with `|d|<=2p-2` can occur between two elements of `H_p`, so the definitions may be truncated to that interval. The relevant representation in (4) or (5) is unique. For example, if two choices of `varepsilon in {-1,0,1}` represented the same `d`, coprimality would force `p` to divide their difference, impossible because `p>2`; the argument for `eta` is identical.

Now take `h,h' in H_p` and write

\[
d=h'-h
=r(i_{h'}-i_h)-p(j_{h'}-j_h).
\tag{6}
\]

If `|i_{h'}-i_h|<=1`, equation (6) puts `d` in the first case of (4), with exactly that difference as `varepsilon`. Conversely, if

\[
d=r\varepsilon-p\eta,
\qquad \varepsilon\in\{-1,0,1\},
\]

subtracting from (6) gives

\[
r(i_{h'}-i_h-\varepsilon)
=p(j_{h'}-j_h-\eta).
\]

Hence `i_{h'}-i_h-\varepsilon=pt`. But

\[
-(p-1)\le i_{h'}-i_h-\varepsilon\le p-1,
\]

so `t=0`. Therefore the path Gram coefficient is exactly `alpha_varepsilon`. The same argument on the `r` side proves

\[
\boxed{
(A_p)_{h,h'}=\kappa_p(h'-h),
\qquad
(A_r)_{h,h'}=\kappa_r(h'-h).
}
\tag{7}
\]

Thus both pulled-back lower Grams are finite Toeplitz/convolution stencils, compressed only by the missing layer `h=0` and the finite interval `H_p`.

The stencil sizes are uniformly bounded. For fixed `varepsilon` in (4), the condition

\[
|r\varepsilon-p\eta|\le2p-2
\]

restricts `eta` to an interval of length strictly less than `4`, so there are at most four possibilities. There are three choices of `varepsilon`; hence

\[
\boxed{|\operatorname{supp}\kappa_p|\le12.}
\tag{8}
\]

Likewise, for fixed `eta` in (5), the admissible `varepsilon` lie in an interval of length

\[
\frac{4p-4}{r}<4,
\]

so

\[
\boxed{|\operatorname{supp}\kappa_r|\le12.}
\tag{9}
\]

These bounds are independent of the scale and of every upper prime.

## 3. Every fixed-depth mixed trace word is a finite shifted scalar correlation

Using (2), one pair of adjacent factors gives

\[
D_{q_1}D_{q_2}^*
=UC_{q_1}A_rC_{q_2}U^T.
\]

Iterating and cyclically moving the final `U^TU=A_p` inside the trace yields the exact determinant-layer formula

\[
\boxed{
T(q_1,\ldots,q_{2m})
=\operatorname{tr}\!\left(
C_{q_1}A_rC_{q_2}A_p
\cdots
C_{q_{2m-1}}A_rC_{q_{2m}}A_p
\right).
}
\tag{10}
\]

Expand the trace using (7). Let

\[
S_r=\operatorname{supp}\kappa_r,
\qquad
S_p=\operatorname{supp}\kappa_p,
\]

and choose shifts

\[
d_1\in S_r,\ d_2\in S_p,\ \ldots,
d_{2m-1}\in S_r,\ d_{2m}\in S_p
\]

with the closed-walk constraint

\[
d_1+\cdots+d_{2m}=0.
\tag{11}
\]

Put

\[
s_1=0,
\qquad
s_t=d_1+\cdots+d_{t-1}\quad(2\le t\le2m).
\]

Then (10) becomes

\[
\boxed{
\begin{aligned}
T(q_1,\ldots,q_{2m})
={}&
\sum_{\substack{
 d_1\in S_r,d_2\in S_p,\ldots,d_{2m}\in S_p\\
 d_1+\cdots+d_{2m}=0
}}
\left(
\prod_{a=1}^{m}
\kappa_r(d_{2a-1})\kappa_p(d_{2a})
\right)\\
&\qquad\times
\sum_{h\in\mathbb Z}
\prod_{t=1}^{2m}c_{q_t}(h+s_t).
\end{aligned}
}
\tag{12}
\]

The zero extension of every `c_q` handles all boundaries automatically. Equations (8)--(9) show that for fixed `m`, (12) contains at most `12^(2m)` scalar `2m`-point correlations, regardless of how large `p,r` and the upper levels become.

This is stronger than merely saying that a finite matrix trace can be expanded entrywise. The determinant-layer change of representation forces **all intermediate indices onto one scalar coordinate with a scale-uniform finite shift alphabet**. The noncommutativity of the original rectangular matrices survives only in the ordering of the scalar packets and the alternating choice of the two fixed stencils.

## 4. PC-255 is exactly the depth-one case

For `m=1`, closure forces `d_2=-d_1`, so only shifts in the common support of the two stencils survive. A nonzero common shift must have

\[
d=r\varepsilon-p\eta,
\qquad
\varepsilon,\eta\in\{-1,0,1\}.
\]

The candidates are

\[
0,\quad \pm p,\quad \pm r,\quad
\pm(r-p),\quad \pm(r+p).
\]

But `r+p>2p-2`, so the last pair cannot connect two layers in `H_p`. Therefore the common stencil is exactly

\[
\boxed{
0,\quad \pm p,\quad \pm r,\quad \pm(r-p),
}
\tag{13}
\]

which is the seven-shift formula of PC-255. Thus PC-255 is not an isolated quadratic coincidence; it is the first member of the fixed-depth expansion (12).

## 5. Fixed spectral moments of the complete singular distribution are local correlations

Set every upper level equal to the same `q`. Then

\[
T(q,\ldots,q)
=\operatorname{tr}\bigl((D_qD_q^*)^m\bigr)
=\sum_j\sigma_j(D_q)^{2m}.
\tag{14}
\]

Equation (12) therefore gives every fixed even singular moment as a finite sum of shifted autocorrelations of the single scalar packet `c_q`. This sharpens the boundary left by PC-254. The complete nonzero singular distribution can still contain information that no *fixed* set of moments captures, but every bounded-degree polynomial spectral statistic has already collapsed to finite-range packet algebra.

Equivalently, in the collision-label representation of PC-254, the matrix

\[
W G_r W G_p
\]

whose eigenvalues are the squared nonzero singular values is pentadiagonal: each `G` is tridiagonal, so their weighted product has bandwidth two. The standard trace/closed-walk identity then says that its `m`th spectral moment is a weighted sum of closed walks of length `m` in this finite-range band operator. Equation (12) is the stronger determinant-layer version that makes those local walks explicit as scalar collision shifts.

Consequently, a proposal based on the first moment, kurtosis-like fixed moments, any fixed polynomial in `D_qD_q^*`, or a fixed-depth mixed trace word cannot claim to have recovered a new global spectral carrier merely because the matrices do not commute.

## 6. Exact control: order survives, but only through the scalar correlations

Take

\[
(p,r)=(7,11),
\qquad
q=13,
\qquad
s=17.
\]

The nonzero packets from PC-255 are

\[
c_{13}(\pm1)=12,
\quad
c_{13}(\pm2)=4,
\quad
c_{13}(\pm4)=2,
\]

and

\[
c_{17}(\pm1)=7,
\quad
c_{17}(\pm2)=6.
\]

For this lower pair the two pulled-back stencil supports are

\[
S_r=\{-11,-7,-4,0,4,7,11\},
\]

and

\[
S_p=\{-11,-10,-7,-4,-3,0,3,4,7,10,11\}.
\]

Direct exact construction of the integer defect matrices gives

\[
\operatorname{tr}(D_{13}D_{17}^*)=912,
\]

recovering PC-255, while at depth four

\[
\boxed{
\operatorname{tr}
(D_{13}D_{17}^*D_{13}D_{17}^*)
=305280.
}
\tag{15}
\]

Evaluating (12) with the same packets and stencils gives exactly `305280`.

The mixed word order is not erased. For example,

\[
\boxed{
\operatorname{tr}
(D_{13}D_{13}^*D_{17}D_{17}^*)
=322336,
}
\tag{16}
\]

which differs from (15). Thus the result does **not** claim commutativity or loss of every multi-upper relation. It identifies where that order information lives: in finitely many scalar shifted products of the already-classified determinant-layer packets.

## 7. Prior-art and novelty audit

The abstract ingredients are classical. For a finite matrix, `tr(M^m)` is the weighted closed-walk expansion of its `m`th spectral moment; in spectral graph theory this is the standard combinatorial trace method. Products and trace asymptotics of finite Toeplitz operators are likewise a classical operator-theoretic subject. No novelty is claimed for trace cyclicity, finite-range convolution, band matrices, or the closed-walk interpretation.

The arithmetic packet after the reduction is also in an established class. PC-253 gives, on the positive half,

\[
c_q(h)
=\frac{y_q(h)\bigl(r(p-y_q(h))-qh\bigr)}p
\mathbf 1_{\{qh+r y_q(h)<pr\}},
\qquad
y_q(h)=\langle -q r^{-1}h\rangle_p,
\]

with even reflection to negative `h`. Substituting this formula into any inner sum in (12) produces a finite product of modular-residue polynomials cut by finitely many rational linear inequalities. For fixed `m` this is a one-dimensional finite Fourier/rational-lattice sum of the same broad Dedekind--Rademacher/Dedekind--Carlitz type already identified in PC-253 and PC-255.

Relevant literature anchors include Matthias Beck and Sinai Robins, **Explicit and efficient formulas for the lattice point count in rational polygons using Dedekind-Rademacher sums**, *Discrete & Computational Geometry* 27 (2002), 443--459, DOI `10.1007/s00454-001-0082-3`, and Matthias Beck, Christian Haase and Asia R. Matthews, **Dedekind-Carlitz polynomials as lattice-point enumerators in rational polyhedra**, *Mathematische Annalen* 341 (2008), 945--961, DOI `10.1007/s00208-008-0220-9`. The literature search also finds the expected general trace-of-products Toeplitz theory rather than a distinct RH-specific mechanism attached to (12).

The project-local content is the exact common-coordinate factorization (7)--(12): both lower path-incidence Grams become scale-uniform finite shift kernels on the determinant-layer coordinate, so every fixed-depth mixed trace word factors through scalar collision correlations. This is an exact consequence of the Prime-Circle packet geometry, but the resulting mathematical species is classical finite-range/Fourier-lattice structure rather than a new zeta spectral construction.

## 8. Matched-control and RH-facing consequence

PC-251 already proves that the complete weighted collision matching is reproduced by the corresponding uniform rational-partition construction for pairwise-coprime non-prime labels. Equations (1)--(12) use only that matching, the two lower path incidence Grams, and finite-dimensional trace algebra. Therefore every fixed-depth trace word in this finding is reproduced by the same source-blind matched control. Taking a higher fixed moment does not restore cyclotomic or prime specificity lost at the PC-251 compression.

Nor does the construction generate the missing analytic ingredients. For fixed `m`, (12) has no free complex spectral parameter, gamma factor, `s<->1-s` symmetry, analytic continuation, or zero detector. Summing these quantities externally over prime upper levels can import ordinary prime-distribution or Dirichlet-`L` information, but that would enter through the sampling set rather than through a new intrinsic operator identity.

PC-256 therefore closes the **fixed-depth** part of the nonquadratic escape left open by PC-255:

\[
\boxed{
\text{fixed-depth multi-upper trace word}
\longrightarrow
\text{finite shifted collision correlations}.
}
\]

The qualifier is essential. This finding does not classify word lengths `m=m(p,r)` growing with collision rank, the full characteristic polynomial or resolvent, extremal singular values obtained through a high-moment limit, matrix-valued mixed products before trace compression, or a source-forced operation coupling upper levels before the rational-partition defect is formed. Those are the remaining places where genuinely nonlocal information could still survive. A future trace-based proposal must therefore explain why a depth growing with scale is intrinsic and controlled; merely moving from quadratic to cubic/quartic or another fixed polynomial statistic no longer crosses the novelty gate.
