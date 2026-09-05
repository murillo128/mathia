# WI-163 — source-level integration closes the sublinear support-edge loophole

**Status:** `LITERATURE+DERIVED + EXACT-DERIVED + STRUCTURAL-RIGIDITY + DECISIVE-NEGATIVE`.

WI-162 localized the unresolved arithmetic gate for changing support-one scalar Lamzouri tests to the support edge `|alpha|=1`: the classical Montgomery--Vaughan mean-value theorem improves the BGSTB source estimate from `O((log T)^-1/2)` to `O(1/log T)` on every fixed compact subinterval of the Fourier support, but WI-162 still paid the coarser error on a fixed endpoint neighborhood. Keeping the source estimates as functions of the distance from the endpoint removes that fixed-neighborhood loss.

Put

\[
L:=\log T,\qquad x=T^\alpha=e^{L\alpha},\qquad
u:=L(1-\alpha),\qquad 0\le\alpha\le1.
\]

For the corrected BGSTB `A_1+A_2+A_3` decomposition, combining their source estimates with the Montgomery--Vaughan estimate for `M_2` gives a uniform dyadic normalized error envelope of the shape

\[
\boxed{
\operatorname{Err}_L(\alpha)
\ll
 e^{-2L\alpha}
 +\frac{e^{-L\alpha}}{\sqrt L}
 +\frac1L
 +\min\!\left(L^{-1/2},L^{-1}+e^{-\nu}\right)
 +\frac{e^{-\nu/2}}{\sqrt L}
}
\tag{1}
\]

with the remaining source terms dominated by those displayed. Integrating (1), rather than bounding the entire support-edge neighborhood by `L^-1/2`, yields for every bounded integrable deweighted profile `r_L` supported in `[-1,1]`

\[
\boxed{
|\mathcal E_L(r_L)|
\ll
\frac{\|r_L\|_\infty+\|r_L\|_1}{L}
+
\frac{\log L}{L^{3/2}}\|r_L\|_\infty.
}
\tag{2}
\]

Since the support has fixed length, `||r_L||_1 <= 2 ||r_L||_infty`. Hence

\[
\boxed{
\|r_L\|_\infty=o(L)
\quad\Longrightarrow\quad
\mathcal E_L(r_L)=o(1).
}
\tag{3}
\]

Thus a support-edge relocation of the `sqrt(L)` singular family from WI-158 cannot recover order-one arithmetic uncertainty: the region on which the global `L^-1/2` estimate is actually competitive has width only `O((log L)/L)`. Within the admissible/regular changing-test class treated in WI-157, condition (3) closes its remaining arithmetic gate and therefore restores WI-157's same-asymptotic-ceiling conclusion. The surviving scalar escape under the present source estimates must reach at least linear deweighted `L^infty` scale along a subsequence, obtain sharper arithmetic information in the central `alpha=0` layer, or leave the scalar support-one interface.

No new numerical zero proportion is claimed. In particular, (3) is not a theorem that arbitrary singular distributions or every imaginable `T`-dependent test family obeys the WI-157 deterministic hypotheses. It is an arithmetic-error theorem for bounded integrable support-one profiles, and the CCLM/Montgomery--Taylor ceiling corollary applies only after the other WI-157 admissibility and normalization hypotheses are imposed.

## 1. Uniform source-level envelope

The corrected proof of Baluyot--Goldston--Suriajaya--Turnage-Butterbaugh writes the prefix pair form through

\[
R(x,T)=\int_0^T|A_1(x,t)+A_2(x,t)+A_3(x,t)|^2dt.
\tag{4}
\]

The source-level estimates used already in WI-162 are

\[
M_1:=\int_0^T|A_1|^2dt
=\frac{T}{x^2}(L^2+O(L)),
\tag{5}
\]

\[
M_3:=\int_0^T|A_3|^2dt
\ll \frac{T}{x^2}+x,
\tag{6}
\]

and the `A_1`--`A_2` cross term is negligible after normalization. For

\[
M_2:=\int_0^T|A_2|^2dt,
\]

BGSTB use the endpoint-uniform Goldston--Montgomery estimate

\[
M_2=T\log x+O(T\sqrt L),
\tag{7}
\]

whereas Montgomery--Vaughan applied to the same Dirichlet series gives

\[
M_2=T\log x+O\!\bigl(T+x\log(2x)\bigr).
\tag{8}
\]

For `x=T^alpha`, the normalized `M_2` error may therefore be kept as

\[
\boxed{
\frac{|M_2-T\log x|}{TL}
\ll
\min\!\left(L^{-1/2},L^{-1}+e^{-L(1-\alpha)}\right).
}
\tag{9}
\]

The remaining Cauchy--Schwarz source terms can also be retained uniformly in `alpha` instead of frozen on a fixed interior interval. With `y=L alpha` and `nu=L(1-alpha)`,

\[
\frac{\sqrt{M_1M_3}}{TL}
\ll e^{-2y}+\frac1{\sqrt{Tx}},
\tag{10}
\]

\[
\frac{\sqrt{M_2M_3}}{TL}
\ll
\frac{e^{-y}}{\sqrt L}
+
\frac{e^{-\nu/2}}{\sqrt L},
\tag{11}
\]

and

\[
\frac{M_3}{TL}
\ll
\frac{e^{-2y}}L+rac{e^{-\nu}}L.
\tag{12}
\]

The prefix error `O(T^{1/2})+O(x)` contributes only a negligible term plus `O(e^{-nu}/L)`. WI-161 established that the corrected source-level decomposition survives passage from the prefix statistic to the dyadic interval; at height `2T`, the endpoint distance is `nu+log 2` and the normalization is `L+O(1)`, so none of (9)--(12) worsens. Equations (5)--(12) therefore imply the dyadic envelope (1).

The important point is that (1) is stronger than the single displayed `O(L^-1/2)` theorem precisely where a changing test needs it. The endpoint deterioration is real pointwise, but it is confined to a shrinking layer.

## 2. Integrating the shrinking endpoint layer

Use

\[
\min(a,b+c)\le b+\min(a,c)
\]

with `a=L^-1/2`, `b=L^-1`, and `c=e^-nu`. The only endpoint term in (1) that is not immediately integrable at `O(1/L)` against `||r_L||_infty` is then

\[
\min\!\left(L^{-1/2},e^{-L(1-\alpha)}\right).
\]

Its integral is explicit. Set `u=L(1-alpha)` and let `u_0=(1/2)log L`. Then

\[
\begin{aligned}
\int_0^1\min\!\left(L^{-1/2},e^{-L(1-\alpha)}\right)d\alpha
&=\frac1L\int_0^L\min(L^{-1/2},e^{-u})du\\
&=\frac1L\left(\frac{\log L}{2\sqrt L}+\frac1{\sqrt L}+O(e^{-L})\right)\\
&=O\!\left(\frac{\log L}{L^{3/2}}\right).
\end{aligned}
\tag{13}
\]

The second endpoint term satisfies

\[
\frac1{\sqrt L}\int_0^1e^{-L(1-\alpha)/2}d\alpha
=O(L^{-3/2}).
\tag{14}
\]

At the central endpoint,

\[
\int_0^1e^{-2L\alpha}d\alpha=O(L^{-1}),
\qquad
\frac1{\sqrt L}\int_0^1e^{-L\alpha}d\alpha=O(L^{-3/2}).
\tag{15}
\]

Finally the uniform `1/L` term pairs with `||r_L||_1/L`. Multiplying (13)--(15) by the appropriate norms gives exactly (2), with the `e^{-nu}/L`, `1/sqrt(Tx)`, and dyadic-prefix remnants strictly smaller.

This calculation is the step missing from WI-162. A fixed endpoint strip made the `L^-1/2` uncertainty appear capable of pairing with `Theta(sqrt L)` mass. The source-level minimum in (9) shows instead that the genuinely dangerous strip has width only about `(log L)/(2L)`; its total uncertainty is `O((log L)/L^(3/2))`.

## 3. Consequences for the changing-test scalar route

Because `r_L` is supported in `[-1,1]`,

\[
\|r_L\|_1\le2\|r_L\|_\infty.
\tag{16}
\]

Therefore (2) immediately yields (3). In particular, a `sqrt(L)`-scale construction satisfies

\[
|\mathcal E_L(r_L)|
=O\!\left(\frac1{\sqrt L}+\frac{\log L}{L}\right)=o(1)
\tag{17}
\]

whenever its deweighted sup norm is `O(sqrt L)`, regardless of whether that mass is moved from the interior toward `|alpha|=1`. Thus the support-edge escape left open by WI-162 does not rescue the explicit WI-158 scale.

For the regular/admissible support-one scalar families of WI-157, the deterministic part of the argument already shows that the main-term advantage over the fixed Montgomery--Taylor/CCLM optimum is only `O(L^-2)`, provided the arithmetic pair-form error is `o(1)`. Equation (3) supplies precisely that missing arithmetic statement whenever

\[
\|r_L\|_\infty=o(L).
\tag{18}
\]

Hence, **inside that WI-157 class**, sublinear deweighted sup norm cannot produce a new asymptotic scalar support-one constant.

This is a decisive closure only for that interface. The estimate does not rule out a family with `||r_L||_infty` of order `L` or larger, because the central source error `e^{-2L alpha}` has integral `Theta(1/L)` and can then pair to order one. Nor does it preclude matrix-valued/multi-profile observables, higher correlations, wider Fourier support, or extra zeta-specific arithmetic structure.

## 4. Equality, near-equality, and remaining escape

The bound (2) identifies two different shrinking layers. Near `alpha=1`, the Montgomery--Vaughan estimate beats the global Goldston--Montgomery error until `nu` is only about `(1/2)log L`; after integration, that endpoint layer has too little measure to matter at sublinear sup norm. Near `alpha=0`, however, the `A_1` source term contributes `e^{-2L alpha}`, whose integral is genuinely `Theta(1/L)`.

Consequently the present source proof itself puts the unresolved scalar escape at a sharper scale:

\[
\boxed{
\text{order-one arithmetic susceptibility requires at least }
\|r_L\|_\infty\not=o(L)
\text{ under these estimates.}
}
\tag{19}
\]

This is a barrier statement about the available source estimates, not a claim that linear growth is mathematically attainable or optimal. A candidate at linear scale would still have to satisfy the Lamzouri factorization, positivity/normalization, and the WI-157 deterministic constraints. Conversely, a sharper treatment of the central `A_1` contribution could move the threshold again.

The useful stress-test target is therefore no longer “can the singular mass be pushed to the support edge?” It is whether admissible near-extremizing scalar factorizations can generate **linear-or-larger** deweighted sup norm without paying a deterministic cost, and if they can, whether the central `alpha=0` source structure supplies cancellation or coercivity beyond the absolute-value estimate used here.

## 5. Stress tests

Three endpoint checks are load-bearing.

At `alpha=1`, (8) by itself is poor because `x` has length comparable with `T`, but the minimum with the Goldston--Montgomery bound in (9) remains `O(L^-1/2)`. Equation (13) never replaces that pointwise fact; it only integrates its shrinking region of relevance.

At `alpha=0`, (9) is `O(1/L)` after Montgomery--Vaughan, but the separate `M_1` normalization contributes `O(1)`. Equation (15) pays this honestly on a layer of width `Theta(1/L)`, which is why (3) requires `o(L)` rather than merely a weaker endpoint-mass condition.

For the dyadic subtraction, the `2T` copy has `log(2T)=L+O(1)` and endpoint distance `log((2T)/x)=nu+log 2`; its exponential edge terms are smaller by fixed factors. The BGSTB cross-boundary estimate retained in WI-161 is also below the terms in (1). Thus neither subtraction nor the change from `L` to `L+O(1)` reintroduces a fixed-width `L^-1/2` layer.

## 6. Prior-art and novelty audit

The arithmetic decomposition and its source estimates are literature-backed by S. A. C. Baluyot, D. A. Goldston, A. I. Suriajaya and C. L. Turnage-Butterbaugh, *Pair Correlation of Zeros of the Riemann Zeta Function I: Proportions of Simple Zeros and Critical Zeros*, corrected `arXiv:2501.14545v3` (1 Sep 2026), especially Section 3. The endpoint-uniform `M_2` estimate is the Goldston--Montgomery input used there. The complementary mean-value estimate (8) is the classical Montgomery--Vaughan theorem as audited in WI-162: H. L. Montgomery and R. C. Vaughan, *Hilbert's Inequality*, J. London Math. Soc. (2) 8 (1974), 73--82, DOI `10.1112/jlms/s2-8.1.73`.

The novelty audit searched specifically around changing/T-dependent test functions for zeta pair correlation, support-edge behavior, Montgomery--Vaughan mean values in pair correlation, and `sqrt(log T)` test-function growth. No direct source was found stating the integrated envelope (2), the sublinear-supnorm gate (3), or the resulting closure of WI-162's support-edge relocation. This absence is recorded only as an audit result and is not a priority claim.

The Mathia contribution in this finding is the exact integration of the source-level minimum in (9), together with its consequence for the existing WI-157/WI-158 frontier. The underlying pair-correlation decomposition, Montgomery--Vaughan and Goldston--Montgomery estimates are not new.

## Evidence boundary

Equations (4)--(12) use literature-backed inputs already source-audited in WI-161/WI-162. Equations (13)--(19) are exact deductions from those inputs. The implication from (3) to the same scalar support-one asymptotic ceiling is conditional only on the other admissibility/normalization hypotheses already imposed in WI-157; it is not asserted for arbitrary bounded profiles outside that class.

No new unconditional proportion is claimed. The remaining unresolved possibilities are linear-or-larger deweighted sup-norm growth within the WI-157 scalar support-one framework, a sharper central source estimate, or escape to additional arithmetic/spectral information outside that interface.