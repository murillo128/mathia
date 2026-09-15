# RE-152 — global GUE statistics are blind to lacunary one-sided vertical escape

**Status:** `EXACT-DERIVED + MATCHED-CONTROL + RIEMANN-VON-MANGOLDT-COMPATIBLE + GLOBAL-CORRELATION-BLINDNESS + PURE-VERTICAL-ESCAPE + ONE-SIDED-ROBIN-WINDOW + DECISIVE-NEGATIVE + REVIEW-REPAIRED`.

This finding replaces `RE-150` after the correction of `RE-149` by `RE-151`. The global-correlation blindness argument in `RE-150` was sound, but its conjunction with a symmetric-window Robin hiding claim inherited the upstream window mismatch. The corrected statement keeps the Riemann--von Mangoldt and fixed-order GUE conclusions unchanged and scopes the Robin obstruction to the one-sided window actually proved in `RE-151`.

The resulting boundary is still strong: a lacunary sequence of exceptional off-critical packets can fit inside the classical `O(log T)` counting remainder, preserve local `O(log T)` occupancy, and be invisible to every fixed-order globally averaged local-correlation statistic, while each packet hides a scale-maximal Robin atom on `[(1-kappa)U_j,U_j]`. Hence global typical-zero statistics do not supply the uniform, target-conditioned information needed to rule out the corrected vertical obstruction.

Fix

\[
\frac12<\sigma_0<\Theta<1,\qquad A>0,\qquad 0<\kappa<\frac12.
\tag{1}
\]

Let `B` be a conjugation-symmetric background supported on `Re rho=1/2`, with positive-ordinate count

\[
N_B(T)
=\frac{T}{2\pi}\log\frac{T}{2\pi}
-\frac{T}{2\pi}+O(\log T),
\tag{2}
\]

and local unit occupancy

\[
N_B(t+1)-N_B(t-1)\ll\log(2+t).
\tag{3}
\]

For fixed `k>=1`, set `L_T=(log T)/(2pi)` and, for `f in C_c(R^k)`, define

\[
\mathcal C_{k,T}^{B}(f)
:=\frac1T\int_T^{2T}
\sum_{(\tau_1,\ldots,\tau_k)\in B_*^k}
 f\!\left(L_T(\tau_1-t),\ldots,L_T(\tau_k-t)\right)dt,
\tag{4}
\]

where `B_*^k` consists of ordered tuples of distinct indexed zeros.

There is a refinement of the `RE-151` control spectrum `Z_ctl` such that:

1. its strict-subedge right-half-strip packet satisfies the `RE-151` pure-vertical hiding estimate on `[(1-kappa)U_j,U_j]` along `U_j->infinity`;
2. adjoining `B` changes (2) only through its `O(log T)` constant and preserves (3);
3. for every fixed `k` and every `f in C_c(R^k)`,

\[
\boxed{
\mathcal C_{k,T}^{B\cup Z_{\rm ctl}}(f)
-\mathcal C_{k,T}^{B}(f)
\longrightarrow0.
}
\tag{5}
\]

Thus any fixed-order globally averaged GUE correlation limits enjoyed by `B` are inherited by the augmented spectrum, even though the exceptional control stages retain the corrected one-sided Robin obstruction.

## 1. The exceptional stages fit inside zeta-scale counting

Use the `RE-151` stage

\[
\rho_{j,S}=\beta_j+i\gamma_{j,S},\qquad
\beta_j=\Theta-U_j^{-2},\qquad
\Gamma_j=U_j^{A/2},
\tag{6}
\]

with

\[
\gamma_{j,S}=\Gamma_j+\frac1{U_j}\sum_{\ell\in S}\omega_{j,\ell},
\qquad S\subset\{1,\ldots,j\}.
\tag{7}
\]

After functional-equation closure there are

\[
m_j=2^{j+1}
\tag{8}
\]

positive-ordinate indexed control points at stage `j`. The recursive freedom in `U_j` allows the additional requirements

\[
\Gamma_{j+1}\ge4\Gamma_j,
\qquad m_j\le\log\Gamma_j,
\qquad \frac{j\log\Gamma_j}{U_j}\to0,
\tag{9}
\]

without disturbing the product or tail conditions of `RE-151`.

The cumulative inserted population is then

\[
M_j=\sum_{n\le j}m_n\ll2^j\ll\log\Gamma_j,
\tag{10}
\]

so, by lacunarity,

\[
M(T):=\#\{\rho\in Z_{\rm ctl}:0<\Im\rho\le T\}
\ll\log T.
\tag{11}
\]

Therefore adjoining `Z_ctl` preserves the Riemann--von Mangoldt main terms and the order of the `O(log T)` remainder in (2).

The absolute diameter of stage `j` satisfies

\[
\Delta_j\ll_\kappa \frac{j}{U_j}
=o\!\left(\frac1{\log\Gamma_j}\right)
\tag{12}
\]

by (9). Since `m_j<=log Gamma_j`, one exceptional packet changes the occupancy of any unit interval by only `O(log Gamma_j)`. Hence (3) also survives.

## 2. Every fixed-order global correlation is blind to the graft

Fix `k` and `f in C_c(R^k)`, and choose `K` with `supp f subset [-K,K]^k`. Because `Gamma_(j+1)>=4Gamma_j`, an enlarged dyadic interval `[T,2T]` meets at most one sufficiently high control stage.

If it meets stage `j`, a tuple involving any inserted point can contribute only when the translation center `t` lies within `K/L_T` of that packet. All such centers lie in a set `E_(j,T)` satisfying

\[
|E_{j,T}|
\le\Delta_j+\frac{2K}{L_T}
\ll_K\frac1{\log T}.
\tag{13}
\]

For `t in E_(j,T)`, every visible point lies in an absolute interval of length `O_K(1/log T)`, hence in a unit interval for large `T`. By (3), (8), and (9), the indexed occupancy is `O_K(log T)`. The difference between the two `k`-tuple sums is therefore `O_(f,k)((log T)^k)`. Integrating only over (13) gives

\[
\left|
\mathcal C_{k,T}^{B\cup Z_{\rm ctl}}(f)
-\mathcal C_{k,T}^{B}(f)
\right|
\ll_{f,k}\frac{(\log T)^{k-1}}{T}
=o(1),
\tag{14}
\]

which proves (5). Coincident ordinates introduced by functional-equation reflection cause no problem: they are distinct indexed spectral points and are already included in the occupancy bound.

The same estimate gives distributional blindness. A fixed bounded rescaled window sees an exceptional stage only for a set of random translation centers of probability

\[
O\!\left(\frac1{T\log T}\right).
\tag{15}
\]

For every fixed `q`, the contribution of the exceptional stage to the averaged `q`th local-count moment is at most

\[
O\!\left(\frac{(\log T)^{q-1}}{T}\right)=o(1).
\tag{16}
\]

Thus all fixed-order random-translation correlations, bounded local observables, and fixed local-count moments remain unchanged in the limit.

## 3. The corrected Robin obstruction survives the critical-line background

The active `RE-151` packet lies in `Re rho>=sigma_0>1/2`, so the background contributes no point to that strict-subedge packet. Its same-real-part product factorization and scale-maximal anchor are therefore untouched.

Even if the leading coefficient sum is enlarged to include the background, (2) implies by partial summation

\[
\sum_{\tau\in B,\ \tau>0}\frac1{1+\tau^2}<\infty.
\tag{17}
\]

Every background point has horizontal deficit `Theta-1/2`; uniformly on the **one-sided** stage window `u in [(1-kappa)U_j,U_j]`,

\[
\sum_{\rho\in B}|a_{\rho,0}(u)|
\ll
\exp[-(\Theta-1/2)(1-\kappa)U_j]
=o(U_j^{-A}).
\tag{18}
\]

Hence the dense critical-line background does not spoil the hiding estimate actually established by `RE-151`.

No assertion is made for the missing upper half `[U_j,(1+kappa)U_j]`. The GUE graft does not create any new product contraction there, so the old symmetric-window conjunction from `RE-150` is deliberately withdrawn.

## 4. Research boundary

The blindness mechanism in (13)--(16) is independent of the Robin window correction. It says that global random-translation statistics sample typical ordinate locations and can miss a lacunary family of exceptional windows of vanishing sampling density. The Robin construction, in contrast, selects precisely those exceptional target stages.

Accordingly, proving Montgomery pair correlation, any fixed collection of `n`-level correlations, the whole hierarchy at each fixed order, or the corresponding typical local distributions would still not exclude the **one-sided** vertical matched control. To close this channel one needs information with a stronger quantifier: for example, a local law valid around every sufficiently high off-critical target, a large-deviation estimate strong enough to eliminate all exceptional centers, or an explicit-formula/Euler-product constraint that directly prices the subset phase geometry.

This remains a matched-control separation, not a claim about actual zeta zeros. No external GUE theorem is load-bearing: the perturbation estimate (14) is direct. Existing correlation literature only supplies the prior-art interpretation of what the globally averaged statistics mean, so no new `SOURCES.md` dependency is required.

The exact lesson after review is therefore narrower but durable: **global GUE-type averaging cannot rule out lacunary exceptional packets that realize the proved one-sided vertical Robin hiding mechanism.** A symmetric-window obstruction remains open.