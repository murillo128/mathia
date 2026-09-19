# NB-232 — Global pair correlation is blind to carrier-critical Ford packets

**Date:** 2026-09-19  
**Status:** `EXACT-DERIVED + NEGATIVE/METHOD-BOUNDARY + ZETA-SPECTRAL-MATCHED-CONTROL + PAIR-CORRELATION-BLINDNESS + MESOSCOPIC-CARRIER-SCALE + NB-231-REFINEMENT + SOURCE-ONLY + PRIOR-ART-AUDITED`.

`NB-231` leaves one sharply localized source-side obstruction. With

\[
Q=\log(10+|t|),\qquad L=\log Q,\qquad R=Q^{2/3}L^{1/3},
\]

\[
Y=\frac XR\to Y_*\in(0,\infty),\qquad
1\ll J:=\frac RH\le L,
\]

a packet using `Theta(J)` carrier slots at depth

\[
YD=\log J+O(1)
\]

can contribute order one to the exact signed Ford residue while satisfying all population inputs currently used in the line. A natural next candidate is zero-spacing or pair-correlation information.

The global version of that idea does not close the endpoint. The `NB-231` packet is **mesoscopic rather than crowded**: its aligned spacing is `Theta(1/X)`, while the mean zeta-zero spacing is `Theta(1/Q)`, so

\[
\boxed{
\frac{1/X}{1/Q}=\frac QX
\asymp Q^{1/3}L^{-1/3}\to\infty.
}
\]

More decisively, the standard Montgomery weighted pair statistic is stable under arbitrarily sparse insertion of such packets. If a baseline ordinate multiset has the ordinary `O(log T)` unit-interval count and `A(T)` extra ordinates are inserted below height `T`, then the pair-correlation numerator changes by at most

\[
\boxed{
O\!\left(A(T)\log T+A(T)^2\right)
}
\]

uniformly in the Fourier parameter. Choosing carrier-critical packets at heights `t_k=e^{k^2}` gives

\[
A(T)=O(\sqrt{\log T}\log\log T),
\]

so after the natural `T log T` normalization the change is `o(1)`, while every selected packet still carries order-one Ford residue.

Thus a global Montgomery-type pair-correlation asymptotic, even known for the full Fourier parameter range, cannot by itself exclude the sparse packets that saturate `YD-log J=O(1)`. The missing theorem must be **local and depth-conditioned**, resolving the carrier phases of the near-one zeros in the actual `1/H` window.

## 1. The carrier lattice is coarser than the mean zero lattice

The phase-aligned ordinates of `NB-231` are

\[
\gamma_j=t+\frac{2\pi qj}{X},
\qquad q\in\mathbb N\ \text{fixed}.
\tag{1}
\]

Hence their spacing is

\[
\Delta_{\rm car}=\frac{2\pi q}{X}\asymp\frac1R.
\tag{2}
\]

Riemann--von Mangoldt gives mean spacing

\[
\Delta_{\rm mean}\asymp\frac{2\pi}{Q}.
\tag{3}
\]

Since `X=YR` and `Y->Y_*>0`,

\[
\boxed{
\frac{\Delta_{\rm car}}{\Delta_{\rm mean}}
\asymp\frac QX
\asymp Q^{1/3}L^{-1/3}	o\infty.
}
\tag{4}
\]

So consecutive packet points are separated by a diverging number of mean zero spacings. Natural-scale repulsion cannot exclude them.

The same scale separation appears in carrier capacity. A packet with `M asymp J=R/H` occupies vertical width

\[
W_{\rm car}\asymp\frac M X\asymp\frac1H.
\tag{5}
\]

A mean-density window of this width has expected zero count of order `Q/H`, whereas the packet uses only `R/H`. Their ratio is

\[
\frac{Q/H}{R/H}=\frac QR
\asymp Q^{1/3}L^{-1/3}\to\infty.
\tag{6}
\]

This comparison is diagnostic rather than a short-interval counting theorem: the rigorous blindness statement is the global stability estimate below. Its interpretation is nevertheless clear—the obstruction is phase selection, not close spacing.

## 2. A stability lemma for Montgomery's global pair statistic

Let `Gamma` be any positive ordinate multiset satisfying

\[
N_\Gamma(u+1)-N_\Gamma(u)\ll\log(10+u)
\tag{7}
\]

and `N_Gamma(T) asymp T log T`. Define

\[
\mathcal P_\Gamma(\alpha,T)
:=
\sum_{\substack{0<\gamma,\gamma'\le T\\
\gamma,\gamma'\in\Gamma}}
T^{i\alpha(\gamma-\gamma')}
\frac4{4+(\gamma-\gamma')^2}.
\tag{8}
\]

Let `E` be an inserted ordinate multiset and

\[
A(T):=\#\{\eta\in E:0<\eta\le T\}.
\tag{9}
\]

For a fixed inserted ordinate `eta`, split the original ordinates into unit distance shells around `eta`. By (7) and summability of `(1+k^2)^(-1)`,

\[
\sum_{\substack{0<\gamma\le T\\\gamma\in\Gamma}}
\frac4{4+(\eta-\gamma)^2}
\ll\log T.
\tag{10}
\]

The oscillatory factor in (8) has modulus one, so all old--new pairs contribute

\[
O(A(T)\log T).
\tag{11}
\]

The new--new pairs contribute at most `O(A(T)^2)`. Therefore, **uniformly for every real `alpha`**,

\[
\boxed{
\left|
\mathcal P_{\Gamma\cup E}(\alpha,T)
-
\mathcal P_\Gamma(\alpha,T)
\right|
\ll
A(T)\log T+A(T)^2.
}
\tag{12}
\]

Since the classical normalization is comparable to `T log T`, every insertion satisfying

\[
A(T)\log T+A(T)^2=o(T\log T)
\tag{13}
\]

is invisible to the normalized global statistic. The conclusion is uniform in `alpha`; it is not restricted to one fixed Fourier mode.

The same proof applies to any global two-point statistic whose oscillatory factor is bounded and whose difference weight is dominated by an integrable envelope.

## 3. Infinitely many transition-saturating packets fit inside the invisible budget

Choose

\[
t_k=e^{k^2}.
\tag{14}
\]

Then, with the line's convention `Q_k=log(10+t_k)`,

\[
Q_k=k^2+o(1),
\qquad
L_k=2\log k+o(1).
\tag{15}
\]

Choose `J_k->infinity` with `J_k<=c_0 L_k`, put

\[
H_k=\frac{R_k}{J_k},
\tag{16}
\]

and use the `NB-231` packet

\[
M_k=\lfloor\delta J_k\rfloor,
\qquad
D_k=\frac{\log J_k+w_k}{Y_k},
\qquad |w_k|\le W,
\tag{17}
\]

at ordinates

\[
\gamma_{j,k}
=t_k+\frac{2\pi qj}{X_k},
\qquad 1\le j\le M_k.
\tag{18}
\]

Then

\[
e^{iX_k(\gamma_{j,k}-t_k)}=1,
\tag{19}
\]

and `NB-231` gives a positive order-one lower bound for the signed packet residue, uniformly in `k`.

If `t_K<=T<t_(K+1)`, the number of inserted positive ordinates satisfies

\[
A(T)
\ll\sum_{k\le K}L_k
\ll K\log K.
\tag{20}
\]

Since `K asymp sqrt(log T)`,

\[
\boxed{
A(T)=O(\sqrt{\log T}\log\log T).
}
\tag{21}
\]

Equations (12)--(13) therefore give

\[
\frac{
\mathcal P_{\Gamma\cup E}(\alpha,T)
-
\mathcal P_\Gamma(\alpha,T)
}{T\log T}
=o(1)
\tag{22}
\]

uniformly in `alpha`.

Moreover `A(T)=o(log T)`, so the insertion preserves any Riemann--von Mangoldt formula with its standard `O(log T)` remainder. Adding functional-equation reflections and complex conjugates changes `A(T)` by only a fixed factor. The reflected positive-ordinate partner has the same ordinate, producing only `O(M_k)` additional zero-difference pairs per packet, already covered by the `A(T)^2` bound; horizontally it lies at depth `R_k-D_k` and is exponentially invisible to the near-one carrier, exactly as in `NB-225` and `NB-231`.

Thus standard zeta symmetries, ordinary zero counting and a full global Montgomery-type pair statistic can coexist, at the level of the matched information, with infinitely many transition-saturating Ford packets.

## 4. Prior-art boundary and what this does not prove

Montgomery introduced the weighted pair statistic above in H. L. Montgomery, *The pair correlation of zeros of the zeta function*, Proc. Sympos. Pure Math. 24 (1973), 181--193, DOI `10.1090/pspum/024/9944`. The classical theorem is conditional on RH. Modern work has also developed no-RH pair-correlation formulations; for example D. A. Goldston, J. Lee, J. Schettler and A. I. Suriajaya, *Pair Correlation Conjecture for the zeros of the Riemann zeta-function I: simple and critical zeros*, arXiv:2503.15449 (2025), shows that an appropriate Pair Correlation Conjecture implies that asymptotically `100%` of zeros are simple and on the critical line.

That density-one conclusion is fully consistent with the method boundary here: the packet family (21) is much smaller than `o(N(T))`, while the source obstruction is pointwise in the selected heights. One exceptional order-one packet along an arbitrarily sparse sequence is enough to defeat a uniform endpoint theorem.

No external pair-correlation theorem is load-bearing for (12)--(22); only the classical statistic is used as the prior-art target. The proof is the elementary stability estimate (12), so `SOURCES.md` acquires no new theorem dependency.

This finding also does **not** construct actual zeta zeros with the packet geometry. As in `NB-231`, the packet is a matched control proving logical insufficiency of a specified information set. A theorem uniform in every short height window, conditioned on horizontal depth and resolving the carrier frequency `X`, would not be ruled out; it would already be close to the missing observable below.

## 5. The surviving observable is local, mesoscopic and depth-conditioned

The exact Ford carrier remembers simultaneously

\[
R(1-\beta),
\qquad
X(\gamma-t)\pmod{2\pi},
\qquad
H(\gamma-t).
\tag{23}
\]

A global pair statistic depending only on ordinate differences discards the first coordinate and averages the other two over the full zero population. The packet can therefore carry order-one source residue while contributing `o(1)` globally.

The next useful zeta theorem must instead control, in the bounded transition layer, a quantity schematically of the form

\[
\sum_{\substack{
R(1-\beta)\le D\\
|\gamma-t|\lesssim1/H}}
 e^{iX(\gamma-t)}
 F\!\left(H[(\gamma-t)+i(\sigma_X-\beta)]\right),
\tag{24}
\]

uniformly when

\[
YD-\log(1+R/H)=O(1).
\tag{25}
\]

This sharpens the `NB-231` frontier: **natural-scale spacing statistics are too fine, while global pair statistics are too averaged**. What remains viable is local carrier-frequency discrepancy for shallow zeros, or an equivalent arithmetic estimate obtained from the explicit formula without first averaging over height.

The destination bridge remains separate. Even a successful bound for (24) would still need to be converted into a Nyman--Beurling distance statement.

## Conclusion

At exact Ford scale, the coherent `NB-231` packet is separated by `Q/X->infinity` mean zero spacings, so it is not a close-spacing anomaly. More strongly, infinitely many such order-one packets may be inserted at sparse heights while changing the standard globally normalized Montgomery pair statistic by only `o(1)`, uniformly in its Fourier parameter.

Global pair correlation therefore does not supply the missing actual-zeta input at `YD-log J=O(1)`. The surviving target is genuinely local and mesoscopic: a depth-conditioned discrepancy theorem for the carrier phases `X gamma mod 2 pi` inside the `1/H` window.