# NB-374 — Unit-norm dilation columns force a count-conditioning tradeoff

- **Status:** proved (classical Mellin/projection input plus author derivation; independent adversarial review pending)
- **Research line:** `nyman_beurling`
- **Depends on:** NB-354 for the projected target; NB-371 for the coefficient-budget comparison; NB-373 for the unrestricted count comparison
- **Classification:** LITERATURE+DERIVED + NEGATIVE/OBSTRUCTION + NORMALIZED-SYNTHESIS-BOUNDARY

## Claim

The coefficient obstruction survives normalization of every actual Nyman generator to unit physical norm. Consequently a uniformly well-conditioned family of actual normalized dilation columns needs at least order \(\varepsilon^{-4}\) columns to approximate the projected target to error \(\varepsilon\). The constants are independent of seeds, dilation range, and the number of columns. This prices cancellation in the actual dictionary, rather than the scale chosen for its coefficients.

Work in \(H=L^2(0,1;dx)\), with
\[
e=1,\quad g_v(x)=\{1/(vx)\}-v^{-1}\{1/x\},\quad v>1,
\qquad A_af(x)=\sqrt a f(ax)\mathbf1_{x\le1/a},\quad a\ge1.
\]
Let \(\mathcal N=\overline{\operatorname{span}}\{g_v:v>1\}\) and \(t=P_{\mathcal N}e\). In the normalization of [NB-354](NB-354-finite-seed-real-dilation-spaces-have-an-exact-target-loss-classification.md),
\[
\mathcal Mt(s)=\frac{bB(s)}s,\qquad b=B(1)>0,\quad \|t\|=b\le1,
\qquad |B(1/2+iy)|=1\quad\text{a.e.}
\tag{1}
\]
Fix one critical-line zero \(\rho=1/2+i\gamma\), of actual multiplicity \(m\ge1\). Such a zero exists unconditionally; simplicity is not assumed. For a finite synthesis define
\[
w=\sum_{\nu=1}^J c_\nu A_{a_\nu}g_{v_\nu},\qquad
\mathcal A=\sum_{\nu=1}^J |c_\nu|\|g_{v_\nu}\|
=\sum_{\nu=1}^J\|c_\nu A_{a_\nu}g_{v_\nu}\|.
\tag{2}
\]
There is \(c_\rho>0\) such that
\[
\boxed{\|t-w\|^2\ge c_\rho(1+\mathcal A)^{-1/m}.}
\tag{3}
\]
In particular \(\varepsilon=\|t-w\|\to0\) requires
\(\mathcal A\gtrsim_\rho\varepsilon^{-2m}\).

For the same columns let
\[
h_\nu=\frac{A_{a_\nu}g_{v_\nu}}{\|g_{v_\nu}\|},\qquad
d_\nu=c_\nu\|g_{v_\nu}\|,\qquad T d=\sum_\nu d_\nu h_\nu,
\qquad G=T^*T.
\tag{4}
\]
Then, for sufficiently small \(\varepsilon>0\),
\[
\boxed{\lambda_{\min}(G)\lesssim_\rho J\varepsilon^{4m}.}
\tag{5}
\]
Thus \(\lambda_{\min}(G)\ge\lambda_0>0\) forces
\(J\gtrsim_\rho\lambda_0\varepsilon^{-4m}\). If squared error is \(O(M^{-1})\) and \(J=O(M)\), then
\[
\lambda_{\min}(G)=O_\rho(M^{1-2m}).
\tag{6}
\]
For \(m\ge1\), this is at most order \(M^{-1}\). A singular Gram matrix already satisfies (5); no inverse or positive smallest eigenvalue is assumed in that statement.

## 1. The normalized Mellin envelope is uniform over all real seeds

Set \(s=1/2+iy\) and
\[
K(y)=\max\{2|s-1|,5\}.
\]
We claim the elementary estimate
\[
\boxed{\frac{|v^{-1}-v^{-s}|}{\|g_v\|}\le K(y)\qquad(v>1).}
\tag{7}
\]
Both degenerate seed regimes must be checked: a lower bound for the norm on a compact seed interval would not suffice.

For \(1<v\le2\), on \(1/v<x<1\) we have \(g_v(x)=1/v\). Therefore
\[
\|g_v\|^2\ge\frac{v-1}{v^3}.
\tag{8}
\]
With \(L=\log v\), the identity
\(1-e^{(1-s)L}=-(1-s)\int_0^L e^{(1-s)u}du\) gives
\[
|v^{-1}-v^{-s}|\le |s-1|\frac{\log v}{\sqrt v}.
\]
Dividing by (8), and using \(\log v\le v-1\), yields
\[
\frac{|v^{-1}-v^{-s}|}{\|g_v\|}
\le |s-1|\frac{v\log v}{\sqrt{v-1}}
\le2|s-1|\sqrt{v-1}\le2|s-1|.
\tag{9}
\]
In fact the normalized numerator tends to zero as \(v\downarrow1\), uniformly on compact ordinate intervals. The shrinking physical norm cannot amplify the zero-neighborhood response without bound.

For \(v\ge2\), on the entire interval \(1/v<x<1\) the fractional parts cancel to give
\[
g_v(x)=\frac{\lfloor1/x\rfloor}{v}\ge\frac1{2vx},
\]
using \(\lfloor u\rfloor\ge u/2\) for \(u\ge1\). Integration gives
\[
\|g_v\|^2\ge\frac1{4v^2}\int_{1/v}^1x^{-2}dx
=\frac{v-1}{4v^2}\ge\frac1{8v}.
\tag{10}
\]
Consequently
\[
\frac{|v^{-1}-v^{-s}|}{\|g_v\|}
\le\sqrt8(1+v^{-1/2})\le\sqrt8(1+2^{-1/2})<5.
\tag{11}
\]
This proves (7), including seeds escaping to infinity. No exact real-seed Gram formula or asymptotic norm equivalence is needed.

## 2. Integrate the actual target mismatch on a zero neighborhood

The exact Mellin formula and dilation isometry give
\[
\mathcal M(A_ag_v)(s)=a^{1/2-s}\frac{\zeta(s)}s(v^{-1}-v^{-s}),
\qquad |a^{1/2-s}|=1\quad(\Re s=1/2).
\tag{12}
\]
Combining (7) and (2),
\[
|\mathcal Mw(1/2+iy)|\le
\mathcal A K(y)\frac{|\zeta(1/2+iy)|}{|1/2+iy|}.
\]
Mellin--Plancherel and the reverse triangle inequality imply
\[
\|t-w\|^2\ge\frac1{2\pi}\int_{\mathbb R}
\frac{[b-\mathcal A K(y)|\zeta(1/2+iy)|]_+^2}{|1/2+iy|^2}\,dy.
\tag{13}
\]
The integral is finite, being bounded by the integral of \(b^2/|1/2+iy|^2\).

Choose \(r,C>0\) with \(|\zeta(\rho+iu)|\le C|u|^m\) for \(|u|\le r\). Put
\[
K_\rho=\max_{|u|\le r}K(\gamma+u),\qquad
W=\max_{|u|\le r}|\rho+iu|,\qquad
\delta=\min\left\{r,\left(\frac b{2CK_\rho(1+\mathcal A)}\right)^{1/m}\right\}.
\]
The bracket in (13) is at least \(b/2\) for \(|u|\le\delta\). Hence
\[
\|t-w\|^2\ge\frac{b^2\delta}{4\pi W^2}
\ge\frac{b^2}{4\pi W^2}
\min\left\{r,\left(\frac b{2CK_\rho}\right)^{1/m}\right\}
(1+\mathcal A)^{-1/m}.
\tag{14}
\]
This proves (3). Constants can be made independent of the unknown inner factor: the explicit column \(g_2\) has \(\langle e,g_2\rangle=(\log2)/2\) and \(\|g_2\|^2=(\log2)/4\), so \(b\ge\sqrt{\log2}\). Replacing \(b\) by this lower bound in (14) specifies an admissible \(c_\rho\) using only local zeta data. No value of \(B\) is required.

For any fixed \(A\), the estimate passes by norm continuity to the closed set
\[
\mathcal K_A=\overline{\left\{\sum_{\nu=1}^Jd_\nu h_\nu:
J<\infty,\ \sum_\nu|d_\nu|\le A\right\}}^{\,H},
\tag{15}
\]
where all real seeds and dilations are allowed. Thus \(t\notin\mathcal K_A\) for every finite \(A\), although \(t\in\overline{\bigcup_A\mathcal K_A}=\mathcal N\). In particular no absolutely convergent series of unit-norm actual columns represents \(t\). This is a norm-topology statement, not a bounded boundary-evaluation assertion.

## 3. Convert total component norm into a Gram restriction

For the finite representation (4), Cauchy--Schwarz gives
\[
\mathcal A=\|d\|_1\le\sqrt J\|d\|_2,
\qquad
\lambda_{\min}(G)\le\frac{\|Td\|^2}{\|d\|_2^2}
\le\frac{J\|w\|^2}{\mathcal A^2}.
\tag{16}
\]
For sufficiently small error, (3) yields
\(\mathcal A\ge(c_\rho^m/2)\varepsilon^{-2m}\), while
\(\|w\|\le b+\varepsilon\le2\). Substitution proves (5), with a constant independent of the representation. This also proves (6) and the stated uniformly positive lower-eigenvalue count bound.

Since \(G\) has unit diagonal, \(\lambda_{\max}(G)\ge1\). Thus in (6) its condition number is at least order \(M^{2m-1}\), or infinite if singular. The requirement concerns the normalized *actual* columns. Orthogonalizing their span changes the dictionary and does not evade the stated resource restriction.

## Significance, controls, and prior art

[NB-371](NB-371-critical-line-zeros-force-unbounded-finite-dilation-synthesis-cost.md) prices the declared raw coefficient sum. Here the sum of physical component norms is unchanged if any column is multiplied by a nonzero scalar and its coefficient divided by that scalar. The uniform endpoint analysis is the additional bridge needed to rule out mere column shrinkage as the explanation for coefficient blow-up. The norm \(\|w\|\) stays bounded while its component-norm sum diverges: cancellation is compulsory.

[NB-373](NB-373-critical-line-zeros-force-an-inverse-column-count-error-floor.md) requires only \(J=\Omega(\varepsilon^{-2})\) without conditioning assumptions. The present statement does not improve that unrestricted count bound. It says that a synthesis on that count scale must become ill-conditioned even after every actual column is normalized; uniformly stable actual columns require a larger count. Neither bound is asserted sharp.

Burnol, *A note on Nyman's equivalent formulation of the Riemann Hypothesis*, [equation (2.3) and Lemma 2.4](https://arxiv.org/pdf/math/9910055), supplies (1) and (12). His *A lower bound in an approximation problem involving the zeros of the Riemann zeta function*, [Theorems 1.3–1.4](https://arxiv.org/pdf/math/0103058), is the classical zero-sensitive range/prediction comparison. Jousse, *Étude d'un problème de continuité lié à l'hypothèse de Riemann*, [Sections 4.2–4.3, especially Theorem 8](https://www.numdam.org/item/10.5802/aif.2127.pdf), treats continuity of variable-dilate projections, including the anchored family. These results do not furnish the uniform normalized envelope (7) or assert the present count-conditioning tradeoff. The zero-neighborhood mechanism is already explicit in NB-371; the contribution here is its extension to the rescaling-invariant physical budget and the resulting restriction on stable sparse synthesis. No bibliographic priority is claimed.

- Seeds approaching one, seeds escaping to infinity, coincident columns, arbitrary complex coefficients, and unbounded real dilation range are admitted. The proof explicitly handles both seed endpoints.
- The budget is invariant under individual column rescaling, not under replacing many columns by their normalized sum. Full closed-orbit vectors may already contain the unbounded synthesis cost; they are not atoms of (15).
- A generic target that vanishes at the chosen boundary zero need not obey (3). The target modulus in (1) is load-bearing, so this is not a Gram-only obstruction for arbitrary vectors.
- Every column lies in \(\mathcal N\), since \(A_ag_v=\sqrt a(g_{av}-v^{-1}g_a)\), with \(g_1=0\). Accordingly \(\|e-w\|^2=1-b^2+\|t-w\|^2\); the bound concerns excess above the Burnol floor unconditionally.
- The result supplies no joint upper synthesis, optimal exponent, effective construction of \(B\), or exclusion of off-critical zeros. No independent adversarial approval, numerical optimum, or Lean verification is asserted.

The decisive audit points are the physical intervals in (8) and (10), retention of the numerator cancellation near \(v=1\), the positive-measure integration in (14), and the direction of the Rayleigh-quotient inequality in (16).
