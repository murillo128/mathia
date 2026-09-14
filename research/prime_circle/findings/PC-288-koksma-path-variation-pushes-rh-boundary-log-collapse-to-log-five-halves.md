# PC-288 — Koksma path variation pushes RH boundary-log collapse to a log-five-halves gap

**Status:** `DERIVED` + `CONDITIONAL-RH-COROLLARY` + `DECISIVE-BOUNDARY` for the exact one-profile boundary-log finite-section frontier left by PC-287.

PC-287 sharpened the exact Prime-Circle boundary-log comparison by flat-clipping the logarithmic singularity. Its remaining source-transport term still used a global Lipschitz estimate,

\[
\frac{B}{\varepsilon}W_1(\nu_q,\widetilde\lambda_q),
\]

which charges the worst derivative `O(1/epsilon)` at every source position. The clipped log-sine profile has a substantially smaller **integrated squared derivative**: its `L^2` derivative cost is only `O(epsilon^{-1/2})`. Because the source is one-dimensional before taking the product law, the relevant prime-versus-Li error can be paired with total variation through the classical one-dimensional Koksma / integration-by-parts inequality rather than with a global Lipschitz constant.

This yields a strictly sharper deterministic transport estimate for the **same exact matrix, same flat clipping, same source laws, and same normalized ordered singular-value observable as PC-287**. Put `L=log q` and define the one-dimensional Kolmogorov discrepancy

\[
\Delta_q
:=
\sup_{0\le t\le1}
\left|
\nu_q([0,t])-\widetilde\lambda_q([0,t])
\right|.
\tag{1}
\]

For `1/q<=epsilon<=1/4`, the clipped singular-spectrum laws satisfy

\[
\boxed{
W_1^{(\ell^\infty)}\!\left(
\widehat\rho^{prime,(\varepsilon)}_{q,B},
\widehat\rho^{Li,(\varepsilon)}_{q,B}
\right)
\ll
\frac{B}{\sqrt\varepsilon}\,\Delta_q.
}
\tag{2}
\]

Combining (2) with the unchanged flat-clipping estimate of PC-287 gives

\[
\boxed{
W_1^{(\ell^\infty)}\!\left(
\rho^{prime,log}_{q,B},
\rho^{Li,log}_{q,B}
\right)
\ll
\sqrt{\varepsilon L+\frac{L^3}{q}}
+\frac{B}{\sqrt\varepsilon}\Delta_q
+\frac{L^2}{q}.
}
\tag{3}
\]

Under RH, Schoenfeld's prime-counting estimate implies

\[
\boxed{
\Delta_q
\ll
q^{-1/2}L^2+\frac{L}{q}.
}
\tag{4}
\]

Choosing

\[
\boxed{
\varepsilon_q
:=Bq^{-1/2}L^{3/2}
}
\tag{5}
\]

then yields

\[
\boxed{
W_1^{(\ell^\infty)}\!\left(
\rho^{prime,log}_{q,B},
\rho^{Li,log}_{q,B}
\right)
\ll
B^{1/2}q^{-1/4}L^{5/4}
+B^{1/2}q^{-3/4}L^{1/4}
+\frac{L^{3/2}}{\sqrt q}
+\frac{L^2}{q}.
}
\tag{6}
\]

Consequently,

\[
\boxed{
\mathrm{RH}
\quad\Longrightarrow\quad
B=o\!\left(\frac{\sqrt q}{(\log q)^{5/2}}\right)
\Longrightarrow
W_1^{(\ell^\infty)}\!\left(
\rho^{prime,log}_{q,B},
\rho^{Li,log}_{q,B}
\right)\to0.
}
\tag{7}
\]

This improves PC-287's `sqrt(q)/log^3(q)` conditional classicalization frontier by half a logarithmic power. It is still a one-way RH consequence, not an RH criterion and not a new zeta mechanism.

## 1. The clipped spectral path has variation `O(B/sqrt(epsilon))`

Use exactly the PC-287 flat-clipped matrix

\[
\widehat K^{(\varepsilon)}_{q,B}(x,y)(h,k)
=
\begin{cases}
-\log q,&(h,k)=(0,0),\\
g_\varepsilon(hx+ky),&(h,k)\ne(0,0),
\end{cases}
\tag{8}
\]

on `H_B={-B,...,B}`, with `N=2B+1`, and normalize by `N`. The clipped profile is constant on `||u||<=epsilon` and elsewhere has derivative

\[
g_\varepsilon'(u)=\pi\cot(\pi u)
\]

up to the even-periodic sign convention. Hence

\[
\boxed{
I_\varepsilon
:=\int_0^1|g_\varepsilon'(u)|^2\,du
\ll \varepsilon^{-1}.
}
\tag{9}
\]

Indeed this is the elementary integral of `cot^2(pi u)` from `epsilon` to `1/2`; the clipping removes the non-integrable endpoint.

Fix `y`. For every nonzero integer `h`, periodicity gives exactly

\[
\int_0^1
|g_\varepsilon'(hx+ky)|^2\,dx
=I_\varepsilon,
\tag{10}
\]

independently of `k` and `y`. The `h=0` rows have zero `x`-derivative. Therefore

\[
\begin{aligned}
\int_0^1
\left\|
\partial_x\frac{\widehat K^{(\varepsilon)}_{q,B}(x,y)}{N}
\right\|_F^2dx
&=
\frac1{N^2}
\sum_{h,k}h^2
\int_0^1|g_\varepsilon'(hx+ky)|^2dx\\
&\ll
\frac{I_\varepsilon}{N}
\sum_{|h|\le B}h^2\\
&\ll
\frac{B^2}{\varepsilon}.
\end{aligned}
\tag{11}
\]

By Cauchy-Schwarz on the unit interval,

\[
\boxed{
\int_0^1
\left\|
\partial_x\frac{\widehat K^{(\varepsilon)}_{q,B}(x,y)}{N}
\right\|_{op}dx
\le
\int_0^1\|\cdot\|_Fdx
\ll
\frac{B}{\sqrt\varepsilon}.
}
\tag{12}
\]

The same bound holds with `x` and `y` interchanged.

Let `widehat Sigma(x,y)` be the ordered singular-value vector of the normalized matrix and let `Phi` be any real `1`-Lipschitz test on that vector space for the `ell^infinity` metric. Singular-value perturbation gives

\[
\|s(A)-s(A')\|_\infty\le\|A-A'\|_{op}.
\tag{13}
\]

Thus, for fixed `y`, the scalar path

\[
F_y(x):=\Phi(\widehat\Sigma(x,y))
\]

is absolutely continuous and has total variation

\[
\boxed{
\operatorname{Var}(F_y)
\ll B\varepsilon^{-1/2},
}
\tag{14}
\]

uniformly in `y`. Possible singular-value crossings cause no problem: (13) controls the metric derivative of the ordered singular-value vector without choosing eigenvectors or differentiating individual singular branches.

## 2. One-dimensional discrepancy replaces global Lipschitz transport

For two probability measures `mu,lambda` on `[0,1]`, let

\[
\Delta(\mu,\lambda)
=
\sup_t|\mu([0,t])-\lambda([0,t])|.
\]

The one-dimensional Stieltjes integration-by-parts / Koksma inequality states that for every bounded-variation scalar function `F`,

\[
\boxed{
\left|\int F\,d(\mu-\lambda)\right|
\le
\Delta(\mu,\lambda)\operatorname{Var}(F).
}
\tag{15}
\]

Apply (15) first in `x`, using (14), and then telescope the product measures as

\[
\nu_q^{\otimes2}-\widetilde\lambda_q^{\otimes2}
=
(\nu_q-\widetilde\lambda_q)\otimes\nu_q
+
\widetilde\lambda_q\otimes(\nu_q-\widetilde\lambda_q).
\tag{16}
\]

The first term uses the uniform `x`-variation bound and the second the identical `y`-variation bound. Hence every `1`-Lipschitz output test `Phi` satisfies

\[
\left|
\mathbb E_{\nu_q^{\otimes2}}\Phi(\widehat\Sigma)
-
\mathbb E_{\widetilde\lambda_q^{\otimes2}}\Phi(\widehat\Sigma)
\right|
\ll
\frac{B}{\sqrt\varepsilon}\Delta_q.
\tag{17}
\]

Kantorovich duality on the output space proves (2). No two-dimensional Hardy-Krause estimate is needed: the product-law telescope retains the one-dimensional source discrepancy one coordinate at a time.

This is the load-bearing improvement over PC-287. The old argument used the worst pointwise derivative `O(1/epsilon)` and `W_1` source transport. Equation (17) instead uses the integrated spectral path length, whose singular contribution is only the square-root cost `epsilon^{-1/2}`.

## 3. RH controls the source Kolmogorov discrepancy at the same prime-counting scale

Let `lambda_q` denote the continuous normalized Li source preceding the denominator-`q` projection used in PC-277/PC-286. Under RH, Schoenfeld gives

\[
|\pi(x)-\operatorname{Li}(x)|
\ll \sqrt x\log x
\tag{18}
\]

uniformly above the fixed explicit threshold; below it the contribution is finite and becomes `O(L/q)` after normalization. Since `pi(q) asymp q/L`, comparing the normalized cumulative masses up to `tq` gives uniformly for `0<=t<=1`

\[
\boxed{
\sup_t
|\nu_q([0,t])-\lambda_q([0,t])|
\ll q^{-1/2}L^2+\frac{L}{q}.
}
\tag{19}
\]

Projecting `lambda_q` to its nearest denominator-`q` grid changes a cumulative distribution by at most the Li mass of one grid cell. The normalized Li density is largest near the fixed lower endpoint, giving

\[
\sup_t
|\lambda_q([0,t])-\widetilde\lambda_q([0,t])|
\ll \frac{L}{q}.
\tag{20}
\]

Equations (19)--(20) prove (4). This is the same classical RH prime-counting input as PC-286; only the source metric paired with the operator has changed.

## 4. Combine with PC-287 flat clipping and optimize

PC-287 proves, for each of the prime and Li-grid source product laws, that replacing the exact boundary-log matrix by (8) changes the normalized ordered singular spectrum in mean by

\[
\ll
\sqrt{\varepsilon L+\frac{L^3}{q}}.
\tag{21}
\]

It also records the `O(L^2/q)` correction from replacing independent prime pairs by the exact distinct-pair convention. Combining the two copies of (21), the clipped transport (2), and that diagonal correction gives (3).

Insert (4):

\[
W_1^{(\ell^\infty)}
\ll
\sqrt{\varepsilon L+L^3/q}
+
\frac{Bq^{-1/2}L^2}{\sqrt\varepsilon}
+
\frac{BL}{q\sqrt\varepsilon}
+
\frac{L^2}{q}.
\tag{22}
\]

The first source-dependent clipping term and the RH discrepancy term balance when

\[
\varepsilon=Bq^{-1/2}L^{3/2},
\]

which is (5). At this choice,

\[
\sqrt{\varepsilon L}
=
\frac{Bq^{-1/2}L^2}{\sqrt\varepsilon}
=
B^{1/2}q^{-1/4}L^{5/4},
\tag{23}
\]

while

\[
\frac{BL}{q\sqrt\varepsilon}
=
B^{1/2}q^{-3/4}L^{1/4}.
\tag{24}
\]

Separating the inherited collision floor under the square root gives `L^(3/2)/sqrt(q)`. This proves (6). The leading term tends to zero exactly when

\[
Bq^{-1/2}L^{5/2}=o(1),
\]

which is (7). In that range, `epsilon_q=o(1)`, `epsilon_q>=1/q`, and `2B+1<=q` for all sufficiently large `q`, so the PC-287 hypotheses remain valid.

## 5. Prior-art and novelty audit

All abstract ingredients of the sharpening are classical. The one-dimensional estimate (15) is the standard bounded-variation discrepancy inequality; a broad signed-measure/non-uniform formulation is given by Christoph Aistleitner and Josef Dick, *Functions of bounded variation, signed measures, and a general Koksma-Hlawka inequality*, Acta Arith. 167 (2015), arXiv:1406.0230. Singular-value perturbation in (13), Frobenius domination, and absolutely continuous matrix-path estimates are standard matrix analysis. The RH prime-counting input is exactly the Schoenfeld/von-Koch estimate already audited in PC-286. The log-sine kernel and its cotangent derivative belong to the classical harmonic/cyclotomic structure already audited by PC-283/PC-287.

A targeted literature search against Koksma-Hlawka transport of matrix spectra, bounded-variation singular-value paths, prime-counting Kolmogorov discrepancy, and clipped log-sine finite sections found these standard components separately, but no theorem matching (2)--(7) for this Prime-Circle boundary-log finite section. **No literature novelty is claimed for Koksma's inequality, the cotangent `L^2` estimate, matrix perturbation, or the RH source bound.**

The durable project-local delta is the composition: the exact PC-287 clipped spectral map has one-dimensional path variation `O(B/sqrt(epsilon))`, so the RH source discrepancy propagates through the complete normalized singular-spectrum law with a square-root singularity penalty rather than the previous `1/epsilon` penalty. This moves the proven RH-forced classicalization boundary from `sqrt(q)/log^3(q)` to `sqrt(q)/log^(5/2)(q)` without changing the observable or control law.

No new `SOURCES.md` entry is required for the line's logic: the only new cited theorem is a standard general Koksma-Hlawka formulation used to audit (15), while all load-bearing arithmetic and kernel inputs are already explicit in PC-283/PC-286/PC-287.

## 6. Falsification, limitations, and surviving frontier

The new estimate has direct failure tests. Equation (9) reduces to the elementary integral of `cot^2`; (10) uses only integer periodicity; (11) is the exact Frobenius square sum of the matrix derivative; and (15) is one-dimensional integration by parts for a signed probability difference. The product-law step (16) does not assume independence after the distinct-pair correction already isolated by PC-287.

The conclusion remains strictly conditional and one-way. It does not show that collapse implies RH, does not isolate zeta zeros, and does not create a self-adjoint Hilbert-Polya operator. As in PC-286/PC-287, an asymptotic order-one prime-versus-Li lower bound inside (7), with the exact persisted normalization and matched control, would contradict RH rather than support it.

The remaining one-profile window is now narrower: between `sqrt(q)/log^(5/2)(q)` and the denominator-microscopic square-root scale. Closing more of that gap requires a stronger deterministic operator estimate than the Frobenius path-length bound (12), a source-sensitive cancellation unavailable to total variation, or a genuinely different observable. Cross-level, multi-source, directional, noncommuting, or otherwise enriched Prime-Circle structures remain outside this result.

**Dependencies:** PC-277, PC-283, PC-284, PC-286, PC-287.
