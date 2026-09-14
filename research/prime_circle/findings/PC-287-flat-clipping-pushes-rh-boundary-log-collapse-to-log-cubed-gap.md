# PC-287 — flat clipping pushes RH boundary-log collapse to a log-cubed gap

**Status:** `DERIVED` + `CONDITIONAL-RH-COROLLARY` + `DECISIVE-BOUNDARY` for the exact one-profile boundary-log finite-section frontier left by PC-284/PC-286.

PC-284 controls the complete normalized singular-spectrum law of the exact selector-subtracted boundary logarithm by replacing its microscopic singular arc with a linear interpolation that keeps the anchor value exact. That interpolation pays two avoidable logarithmic losses: its Lipschitz constant is `O((log q)/epsilon)`, and its clipping error is bounded pointwise by `O(log q)` over the whole exceptional arc. PC-286 then combines that deterministic estimate with the RH prime-to-Li source transport and obtains collapse for

\[
B=o\!\left(\frac{\sqrt q}{(\log q)^6}\right).
\]

The singular arc can be handled more sharply by clipping the **value** of the logarithm rather than interpolating all the way down to the exceptional anchor value. The anchor coefficient `(h,k)=(0,0)` is source-independent and can be kept exactly, while every other coefficient uses a flat truncation. This removes one `log q` from the source Lipschitz constant and replaces the crude exceptional-set error by the actual square-summable logarithmic depth of the singularity.

Let

\[
k_q(0):=-\log q,
\qquad
k_q(t):=\log\left(2\sin\frac{\pi |t|_q}{q}\right),\quad t\ne0,
\tag{1}
\]

and, for `1/q<=epsilon<=1/4`, define the even periodic flat clipping

\[
g_\varepsilon(x)
:=
\log\!\left(2\sin\bigl(\pi\max(\|x\|_{\mathbb R/\mathbb Z},\varepsilon)\bigr)\right).
\tag{2}
\]

For `H_B={-B,...,B}`, `N=2B+1<=q`, and source points `x=p/q,y=r/q`, let the exact matrix be the PC-284 matrix

\[
K_{q,B}(x,y)(h,k)=k_q(hp+kr\bmod q),
\tag{3}
\]

and define the clipped comparison matrix by

\[
\widehat K^{(\varepsilon)}_{q,B}(x,y)(h,k)
:=
\begin{cases}
-\log q,&(h,k)=(0,0),\\
g_\varepsilon(hx+ky),&(h,k)\ne(0,0).
\end{cases}
\tag{4}
\]

The special central entry is not a modification of the source geometry: its phase is identically zero for every source pair, so keeping it exact simply separates the source-independent anchor coefficient from the source-dependent matrix entries.

If `Sigma_{q,B}` denotes the ordered singular-value vector of `K_{q,B}/N`, and `rho^{prime,log}_{q,B}`, `rho^{Li,log}_{q,B}` are the same prime and denominator-`q` Li-grid laws as in PC-284, then with

\[
D_q:=W_1(\nu_q,\widetilde\lambda_q)
\tag{5}
\]

there is an absolute constant `C` such that

\[
\boxed{
W_1^{(\ell^\infty)}\!\left(
\rho^{prime,log}_{q,B},
\rho^{Li,log}_{q,B}
\right)
\ll
\sqrt{\varepsilon\log q+\frac{(\log q)^3}{q}}
+\frac{B}{\varepsilon}D_q
+\frac{(\log q)^2}{q}.
}
\tag{6}
\]

This strictly sharpens the deterministic PC-284 transport estimate for the same exact matrix and matched control. Under RH, PC-286 gives

\[
D_q\ll q^{-1/2}(\log q)^2+q^{-1}.
\tag{7}
\]

Optimizing (6) then yields

\[
\boxed{
W_1^{(\ell^\infty)}\!\left(
\rho^{prime,log}_{q,B},
\rho^{Li,log}_{q,B}
\right)
\ll
B^{1/3}q^{-1/6}\log q
+\frac{B^{1/3}q^{-2/3}}{\log q}
+\frac{(\log q)^{3/2}}{\sqrt q}
+\frac{(\log q)^2}{q}.
}
\tag{8}
\]

Consequently RH forces

\[
\boxed{
B=o\!\left(\frac{\sqrt q}{(\log q)^3}\right)
\quad\Longrightarrow\quad
W_1^{(\ell^\infty)}\!\left(
\rho^{prime,log}_{q,B},
\rho^{Li,log}_{q,B}
\right)\to0.
}
\tag{9}
\]

Thus the `log^6` gap in PC-286 was not intrinsic to the roots-of-unity geometry or to RH source transport. A direct treatment of the logarithmic singular depth halves that deterministic polylogarithmic loss. The conclusion remains one-way: collapse is forced by RH in (9); collapse does not imply RH.

## 1. Flat value clipping has Lipschitz cost `1/epsilon`, not `(log q)/epsilon`

On the clipped arc `||x||<=epsilon`, the function (2) is constant. Outside it,

\[
\left|\frac{d}{dx}\log(2\sin\pi x)\right|
=\pi|\cot(\pi x)|
\ll \varepsilon^{-1}
\qquad
(\varepsilon\le x\le1/2).
\]

Hence

\[
\boxed{
\operatorname{Lip}(g_\varepsilon)\ll\varepsilon^{-1}.
}
\tag{10}
\]

For every noncentral `(h,k)`, periodicity and (10) give

\[
\left|
 g_\varepsilon(hx+ky)-g_\varepsilon(hx'+ky')
\right|
\ll
\frac{B}{\varepsilon}
\bigl(d(x,x')+d(y,y')\bigr).
\tag{11}
\]

There are `N^2-1` such entries. After the `1/N` matrix normalization, Frobenius domination of operator norm and coordinatewise singular-value perturbation therefore give

\[
\boxed{
\|\widehat\Sigma^{(\varepsilon)}_{q,B}(x,y)
-\widehat\Sigma^{(\varepsilon)}_{q,B}(x',y')\|_\infty
\ll
\frac{B}{\varepsilon}
\bigl(d(x,x')+d(y,y')\bigr),
}
\tag{12}
\]

where `widehat Sigma` is the ordered singular spectrum of `widehat K/N`. The exact central value in (4) contributes no source variation.

This is the first gain over PC-284: the source transport amplification is `B/epsilon`, rather than `B log(q)/epsilon`.

## 2. The logarithmic singular depth is square-summable on the exceptional residues

Put

\[
\delta_{q,\varepsilon}(t)
:=k_q(t)-g_\varepsilon(t/q),
\qquad t\in\mathbb Z/q\mathbb Z.
\tag{13}
\]

For `|t|_q>=epsilon q`, the difference vanishes. For `1<=|t|_q<epsilon q`, elementary bounds for sine on `[0,\pi/4]` give

\[
\boxed{
|\delta_{q,\varepsilon}(t)|
\ll
1+\log\frac{\varepsilon q}{|t|_q}.
}
\tag{14}
\]

At the exact collision residue,

\[
|\delta_{q,\varepsilon}(0)|
=
\left|-\log q-\log(2\sin\pi\varepsilon)\right|
\ll\log q.
\tag{15}
\]

If `m=floor(epsilon q)`, the elementary integral comparison

\[
\sum_{t=1}^{m}
\left(1+\log\frac mt\right)^2
\ll m
\tag{16}
\]

therefore implies the discrete square-sum estimate

\[
\boxed{
\sum_{t\in\mathbb Z/q\mathbb Z}
|\delta_{q,\varepsilon}(t)|^2
\ll
\varepsilon q+(\log q)^2.
}
\tag{17}
\]

This is the second gain over PC-284. The exceptional arc has length `O(epsilon q)`, but most of its points are only logarithmically shallow; charging the worst `O(log q)` discrepancy to every exceptional residue loses two unnecessary powers of `log q` in the mean-square budget.

## 3. Source atom control converts the square sum into a spectral clipping estimate

Both source measures already used in PC-284 satisfy

\[
\max_a\nu_q(a/q)
+
\max_a\widetilde\lambda_q(a/q)
\ll\frac{\log q}{q}.
\tag{18}
\]

Fix `(h,k)\ne(0,0)` in `H_B^2`. Because `q` is prime and `N<=q`, at least one of `h,k` is nonzero modulo `q`. Conditioning on the other source coordinate, multiplication by that nonzero coefficient permutes `Z/qZ`; hence the phase `hp+kr mod q` has maximal atom `O(log q/q)` under either source product law. Equation (17) gives

\[
\boxed{
\mathbb E
|\delta_{q,\varepsilon}(hp+kr)|^2
\ll
\varepsilon\log q+
\frac{(\log q)^3}{q}.
}
\tag{19}
\]

The central coefficient has no error because (4) keeps it exact. Summing (19) over the remaining entries and dividing by `N^2`,

\[
\mathbb E
\left\|
\frac{K_{q,B}-\widehat K^{(\varepsilon)}_{q,B}}{N}
\right\|_F^2
\ll
\varepsilon\log q+
\frac{(\log q)^3}{q}.
\tag{20}
\]

Jensen together with

\[
\|s(A)-s(B)\|_{\ell^\infty}
\le\|A-B\|_{op}
\le\|A-B\|_F
\tag{21}
\]

then yields, for both source laws,

\[
\boxed{
\mathbb E
\|\Sigma_{q,B}-\widehat\Sigma^{(\varepsilon)}_{q,B}\|_\infty
\ll
\sqrt{\varepsilon\log q+
\frac{(\log q)^3}{q}}.
}
\tag{22}
\]

Exact noncentral modular collisions are included in (19); they have not been deleted or regularized away. Their entire contribution is represented by the `t=0` term in (17), which becomes the `(log q)^3/q` term after the maximal-atom bound.

## 4. Transport the clipped spectrum and optimize under RH

Couple two independent copies of an optimal coupling between `nu_q` and `widetilde lambda_q`. Equation (12) gives

\[
W_1^{(\ell^\infty)}\!\left(
(\widehat\Sigma^{(\varepsilon)}_{q,B})_*(\nu_q^{\otimes2}),
(\widehat\Sigma^{(\varepsilon)}_{q,B})_*(\widetilde\lambda_q^{\otimes2})
\right)
\ll
\frac{B}{\varepsilon}D_q.
\tag{23}
\]

The entries of the exact matrix are `O(log q)`, so every singular value after the `1/N` normalization is `O(log q)`. Replacing the prime product law by distinct prime pairs costs `O((log q)^2/q)`, exactly as in PC-284. Combining the two clipping comparisons (22), the transport (23), and this diagonal conditioning proves (6).

Under RH insert (7) into (6), writing `L=log q`:

\[
W_1^{(\ell^\infty)}
\ll
\sqrt{\varepsilon L+L^3/q}
+
\frac{Bq^{-1/2}L^2}{\varepsilon}
+
\frac{B}{q\varepsilon}
+
\frac{L^2}{q}.
\tag{24}
\]

Choose

\[
\boxed{
\varepsilon_q=B^{2/3}q^{-1/3}L.
}
\tag{25}
\]

In the claimed regime (9), `epsilon_q=o(1)`, `epsilon_q>=1/q`, and `2B+1<=q` for all sufficiently large `q`, so all hypotheses remain valid. The first source-dependent clipping term and the RH transport term balance at

\[
\sqrt{\varepsilon_q L}
=
\frac{Bq^{-1/2}L^2}{\varepsilon_q}
=
B^{1/3}q^{-1/6}L,
\tag{26}
\]

while

\[
\frac{B}{q\varepsilon_q}
=
\frac{B^{1/3}q^{-2/3}}{L}.
\tag{27}
\]

Separating the second term under the square root in (24) gives `L^{3/2}/sqrt(q)`. Equations (24)--(27) prove (8), and its leading term tends to zero exactly when

\[
Bq^{-1/2}L^3=o(1),
\]

which is (9).

## 5. Prior-art and novelty audit

No new analytic-number-theory theorem enters this result. The RH source estimate (7) is precisely the Schoenfeld/von-Koch input already audited in PC-286. The boundary logarithmic kernel itself is the classical log-sine/digamma Green symbol identified in PC-283. Singular-value perturbation and finite-section operator estimates are standard and were already audited in PC-280/PC-281/PC-284.

A targeted literature search against truncated log-sine kernels, logarithmic Toeplitz symbols, finite-section singular values, and roots-of-unity log potentials found the expected classical surrounding theory: log-sine integrals/Clausen functions, cyclotomic logarithmic sums, and standard Toeplitz finite-section spectral analysis. No independent theorem was found whose content is the prime-source versus denominator-`q` Li-grid estimate (6) or the optimized Prime-Circle boundary (9). No novelty is claimed for clipping a logarithmic singularity, the estimate `sum_{t<=m} log^2(m/t)=O(m)`, or singular-value perturbation.

The durable project-local delta is narrower and explicit: **for the exact PC-283/PC-284 boundary-log finite section, flat value clipping exposes the true `L^2` size of the microscopic logarithmic depth and removes the artificial `log q` factor from source transport, improving the RH-forced classicalization frontier from `sqrt(q)/log^6(q)` to `sqrt(q)/log^3(q)`.** Since all load-bearing external results are already anchored by PC-283/PC-284/PC-286 and the new estimate (17) is elementary, no new `SOURCES.md` dependency is introduced.

This remains a classicalization result, not a positive RH mechanism. In particular, the improved exponent `3` is a deterministic loss from this coupling-and-clipping argument and is not asserted to be an intrinsic arithmetic threshold.

## 6. Falsification, boundaries, and research consequence

The sharpening has direct failure tests. Equation (10) can be checked from the derivative of the clipped log-sine profile. Equation (17) reduces to the elementary discrete logarithmic square sum (16). Equation (19) uses only the already-persisted maximal-atom bound and the fact that every noncentral coefficient pair has an invertible coordinate modulo prime `q`. A source pair or coefficient family violating any of these deterministic statements would invalidate the corresponding step.

More importantly, an asymptotic order-one lower bound for the exact prime-versus-Li normalized singular-spectrum law along a sequence satisfying

\[
B=o(\sqrt q/(\log q)^3)
\]

would contradict RH, provided the persisted PC-284 source setup and PC-286 source estimate are retained. A discrepancy at or above that scale lies outside the theorem. Conversely, convergence in this range gives no implication toward RH.

PC-287 does not close the denominator-microscopic transition, does not treat an additional magnification of the prime-minus-Li residual, and does not touch cross-level, multi-source, directional, noncommuting, or richer observables that retain more than the ordered singular-value vector of one two-sided finite section. It only narrows the one-profile route further.

The practical frontier is therefore sharper than in PC-286. Before treating the remaining polylogarithmic neighborhood of `B~sqrt(q)` as a possible geometric RH carrier, one must first beat the `log^3` loss in (9) or prove that some source-forced observable survives a stronger matched-control argument. Otherwise the line should leave the single-profile architecture rather than interpret the remaining proof gap as arithmetic structure.