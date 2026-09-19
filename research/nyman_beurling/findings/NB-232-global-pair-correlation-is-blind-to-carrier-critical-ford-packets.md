# NB-232 — Global pair correlation is blind to carrier-critical Ford packets

**Date:** 2026-09-19  
**Status:** `EXACT-DERIVED + NEGATIVE/METHOD-BOUNDARY + ZETA-SPECTRAL-MATCHED-CONTROL + PAIR-CORRELATION-BLINDNESS + MESOSCOPIC-CARRIER-SCALE + NB-231-REFINEMENT + SOURCE-ONLY + PRIOR-ART-AUDITED`.

`NB-231` sharpens the source-side endpoint to one bounded transition layer. In the regime

\[
Q=\log(10+|t|),\qquad L=\log Q,\qquad R=Q^{2/3}L^{1/3},
\]

\[
Y=\frac XR\to Y_*\in(0,\infty),\qquad
1\ll J:=\frac RH\le L,
\]

a packet using a fixed positive fraction of the `J` carrier slots at depth

\[
YD=\log J+O(1)
\]

can contribute order one to the exact signed Ford residue while remaining compatible with all population inputs currently used in the line. The surviving frontier therefore asks for genuinely zeta-specific information coupling depth to vertical phase or spacing.

A natural next candidate is global pair correlation of zero ordinates. This finding rules out that route at its usual averaged level. The `NB-231` packet is **mesoscopic rather than crowded**: its aligned spacing is `Theta(1/X)`, whereas the mean zeta-zero spacing at height `t` is `Theta(1/Q)`, and

\[
\boxed{
\frac{1/X}{1/Q}=\frac QX
\asymp
Q^{1/3}L^{-1/3}
\longrightarrow\infty.
}
\]

More decisively, Montgomery-type global pair statistics are stable under inserting arbitrarily sparse sequences of such carrier-critical packets. If a baseline ordinate multiset has the ordinary `O(log T)` unit-interval count, then adding `A(T)=O(\sqrt{\log T}\log\log T)` packet ordinates below height `T` changes the standard weighted pair-correlation numerator by only

\[
O\!\left(A(T)\log T+A(T)^2\right),
\]

uniformly in the Fourier parameter. After the natural `T log T` normalization this is `o(1)`. At the same time the inserted packets can be chosen exactly as in `NB-231`, including functional-equation and conjugation partners, and each selected packet still carries order-one Ford residue mass.

Hence even a complete global Montgomery-type pair-correlation asymptotic cannot, by itself, exclude the sparse phase-aligned controls that saturate the `YD-log J=O(1)` transition. The next useful theorem must be **local and depth-conditioned**: it has to control the carrier-frequency phases of the near-one zeros in the actual `1/H` window, not merely the global two-point distribution of ordinates.

## 1. The carrier lattice is much coarser than the mean zero lattice

Keep the notation and exact-Ford scaling of `NB-231`:

\[
R=Q^{2/3}L^{1/3},
\qquad
X=YR,
\qquad
Y\to Y_*>0.
\tag{1}
\]

The phase-aligned ordinates used there have the form

\[
\gamma_j
=t+\frac{2\pi qj}{X},
\qquad q\in\mathbb N\ \text{fixed}.
\tag{2}
\]

Thus their spacing is

\[
\Delta_{\rm car}
=
\frac{2\pi q}{X}
\asymp\frac1R.
\tag{3}
\]

On the other hand the Riemann--von Mangoldt law gives local mean spacing

\[
\Delta_{\rm mean}
\asymp
\frac{2\pi}{Q}.
\tag{4}
\]

Therefore

\[
\boxed{
\frac{\Delta_{\rm car}}{\Delta_{\rm mean}}
\asymp
\frac QX
\asymp
Q^{1/3}L^{-1/3}
\to\infty.
}
\tag{5}
\]

The coherent packet is not asking for abnormally close ordinates. Consecutive selected points are separated by a diverging number of mean zero spacings. A repulsion statement acting only at the natural `1/Q` scale therefore points in the wrong direction for this obstruction.

There is the same surplus at the level of local capacity. A packet with

\[
M\asymp J=\frac RH
\tag{6}
\]

occupies a vertical interval of length

\[
W_{\rm car}
\asymp
\frac{M}{X}
\asymp
\frac{1}{H},
\tag{7}
\]

while the expected total number of zeta ordinates in such a window is of order

\[
QW_{\rm car}
\asymp
\frac QH.
\tag{8}
\]

The ratio between ordinary zero capacity and the aligned packet size is

\[
\boxed{
\frac{Q/H}{R/H}
=
\frac QR
\asymp
Q^{1/3}L^{-1/3}
\to\infty.
}
\tag{9}
\]

Thus the matched packet uses a vanishing fraction `R/Q` of the ordinates that a mean-density window could contain. The obstruction is a **phase-selection problem**, not a crowding problem.

## 2. Sparse insertions are invisible to the Montgomery weighted pair statistic

The preceding scale comparison already shows why mean-spacing repulsion is not enough. One can make the blindness exact for the standard global two-point observable.

Let `Gamma` be any positive ordinate multiset satisfying the classical local envelope

\[
N_\Gamma(u+1)-N_\Gamma(u)
\ll \log(10+u)
\tag{10}
\]

and the Riemann--von Mangoldt order of magnitude

\[
N_\Gamma(T)\asymp T\log T.
\tag{11}
\]

For real `alpha`, define the Montgomery-type weighted pair numerator

\[
\mathcal P_\Gamma(\alpha,T)
:=
\sum_{\substack{0<\gamma,\gamma'\le T\\
gamma,gamma'\in\Gamma}}
T^{i\alpha(\gamma-\gamma')}
 w(\gamma-\gamma'),
\tag{12}
\]

where

\[
w(u)=\frac4{4+u^2}.
\tag{13}
\]

The exact normalization is immaterial below; the classical one is comparable to `T log T`.

Let `E` be an additional multiset of ordinates and write

\[
A(T):=\#\{\eta\in E:0<\eta\le T\}.
\tag{14}
\]

For each inserted ordinate `eta<=T`, decompose the original ordinates into unit intervals according to `|gamma-eta|`. From (10) and the summability of `(1+k^2)^(-1)`,

\[
\sum_{\substack{0<\gamma\le T\\gamma\in\Gamma}}
 w(\eta-\gamma)
\ll \log T.
\tag{15}
\]

Since the Fourier factor in (12) has modulus one, all old--new pairs contribute at most

\[
O(A(T)\log T).
\tag{16}
\]

The new--new contribution is bounded trivially by

\[
O(A(T)^2).
\tag{17}
\]

Consequently, uniformly for every real `alpha`,

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
\tag{18}
\]

If, for example,

\[
A(T)=O(\sqrt{\log T}\log\log T),
\tag{19}
\]

then

\[
\frac{
\mathcal P_{\Gamma\cup E}(\alpha,T)
-
\mathcal P_\Gamma(\alpha,T)
}{T\log T}
=o(1)
\tag{20}
\]

uniformly in `alpha`.

This is stronger than saying that one particular limiting pair law cannot see one packet. **The entire standard weighted pair-correlation function is asymptotically unchanged, at every Fourier parameter, by a sufficiently sparse family of carrier-critical packets.** The argument uses only the integrable vertical envelope `w`; the same stability holds for any global two-point statistic with a bounded oscillatory factor and an integrable difference weight.

## 3. One can insert infinitely many `NB-231` packets inside that invisible budget

Choose packet heights

\[
t_k=e^{k^2},
\tag{21}
\]

so that

\[
Q_k=\log t_k=k^2,
\qquad
L_k=\log Q_k=2\log k.
\tag{22}
\]

At each height choose a carrier capacity

\[
J_k\to\infty,
\qquad
J_k\le c_0L_k,
\tag{23}
\]

for a fixed sufficiently small `c_0`, set

\[
H_k=\frac{R_k}{J_k},
\tag{24}
\]

and insert the `NB-231` packet

\[
M_k=\lfloor\delta J_k\rfloor
\tag{25}
\]

at depth

\[
D_k=\frac{\log J_k+w_k}{Y_k},
\qquad |w_k|\le W,
\tag{26}
\]

with ordinates

\[
\gamma_{j,k}
=t_k+\frac{2\pi qj}{X_k},
\qquad 1\le j\le M_k.
\tag{27}
\]

Exactly as in `NB-231`, the phase factor `exp(i X_k(gamma_(j,k)-t_k))` is one, the profile stays in a fixed positive patch, and the signed packet residue has a positive order-one lower bound independent of `k`.

The cumulative number of inserted positive ordinates up to height `T` is tiny. If `t_K<=T<t_(K+1)`, then

\[
A(T)
\ll
\sum_{k\le K}L_k
\ll K\log K.
\tag{28}
\]

Since `K\asymp sqrt(log T)`,

\[
\boxed{
A(T)
=O(\sqrt{\log T}\log\log T).
}
\tag{29}
\]

Thus (20) applies. Moreover (29) is itself `o(log T)`, so adding the packets preserves any Riemann--von Mangoldt formula with the usual `O(log T)` remainder.

For each right-half point one may also insert its functional-equation reflection and complex conjugate. This multiplies `A(T)` by only a fixed constant. The reflected positive-ordinate partner has the same ordinate and therefore creates a bounded number of zero-difference pairs per packet point; these are already absorbed by (17). The reflected zero lies at Ford depth `R-D_k` and is exponentially invisible to the local near-one carrier at `+t_k`, exactly as in `NB-225` and `NB-231`.

Hence standard zeta symmetries, the ordinary counting law and a full global Montgomery-type pair statistic can all coexist, at the level of the matched information, with infinitely many transition-saturating Ford packets.

## 4. Why stronger global pair-correlation conclusions still do not close the endpoint

Montgomery introduced the weighted statistic (12) to study the vertical two-point distribution of zeta zeros. The classical theorem is conditional on RH, while modern work has developed pair-correlation formulations that extract horizontal information under weaker or conjectural hypotheses. In particular, recent no-RH formulations of the Pair Correlation Conjecture can imply that asymptotically `100%` of zeros are simple and on the critical line.

Those results are an important prior-art boundary, but they do not contradict the stability statement above. An asymptotic density-one conclusion still permits an exceptional set of size `o(N(T))`, whereas the packet family (29) has density vastly smaller than that. The present obstruction is pointwise in the selected source heights: **one order-one packet at an arbitrarily sparse sequence of heights is enough to defeat a uniform endpoint theorem.**

This distinction prevents an invalid inference. A global statistic may determine the behavior of almost all zeros, or almost all height windows, while leaving the exceptional windows required by the Nyman source-side obstruction completely uncontrolled.

The load-bearing mathematics in this finding is the elementary stability estimate (18), not any external pair-correlation theorem. The relevant prior-art boundary is H. L. Montgomery, *The pair correlation of zeros of the zeta function*, Proc. Sympos. Pure Math. 24 (1973), 181--193, DOI `10.1090/pspum/024/9944`. For the modern no-RH distinction between pair correlation and exceptional off-critical zeros, see D. A. Goldston, J. Lee, J. Schettler and A. I. Suriajaya, *Pair Correlation Conjecture for the zeros of the Riemann zeta-function I: simple and critical zeros*, arXiv:2503.15449 (2025). No theorem from either paper is needed to prove (18)--(29), so `SOURCES.md` acquires no new load-bearing dependency.

## 5. Representation audit: the missing observable is local phase discrepancy conditioned on depth

The obstruction survives because global pair statistics average over the wrong axes. The exact Ford carrier distinguishes simultaneously:

\[
R(1-\beta),
\qquad
X(\gamma-t)\pmod{2\pi},
\qquad
H(\gamma-t).
\tag{30}
\]

A pair statistic depending only on ordinate differences, normalized over all zeros up to height `T`, discards the first coordinate and averages the other two over an enormous population. The sparse packet can therefore carry order-one source residue while contributing `o(1)` to the global statistic.

The next useful zeta theorem must instead control a local, depth-conditioned phase sum on the transition slab. Schematically, one needs information of the form

\[
\sum_{\substack{
R(1-\beta)\le D\\
|\gamma-t|\lesssim 1/H}}
 e^{iX(\gamma-t)}
 F\!\left(H[(\gamma-t)+i(\sigma_X-\beta)]\right),
\tag{31}
\]

uniformly when

\[
YD-\log(1+R/H)=O(1).
\tag{32}
\]

It is not enough to know the global pair distribution, nor merely that near-neighbor gaps repel at scale `1/Q`. The phase in (31) oscillates on the much coarser `1/X` scale and is restricted to the exceptional near-one population that actually receives Ford weight.

This is a useful narrowing of the `NB-231` frontier. The phrase “phase or spacing information” can now be made more precise: **natural-scale spacing statistics are too fine and global pair statistics are too averaged**. What remains viable is mesoscopic carrier-frequency discrepancy for shallow zeros in the actual local window, or an equivalent arithmetic statement obtained from the explicit formula without first averaging over height.

## 6. Failure modes and scope

This finding does **not** say that every conceivable pair-correlation theorem is useless. A theorem uniform in every short height window, conditioned on horizontal depth, and resolving the carrier frequency `X` would no longer be the global statistic treated here; it would be close to the missing observable (31) itself.

It also does not construct actual zeta zeros with the packet geometry. As in `NB-231`, the packet is a matched control showing logical insufficiency of a specified information set. The actual zeta function may have additional arithmetic rigidity that forbids such packets.

Finally, the result remains source-side. Even a successful bound for (31) would still have to be connected to the Nyman--Beurling destination through the separate bridge already isolated in `RESEARCH_LINES.md`.

## Conclusion

At exact Ford scale, the `NB-231` coherent packet is separated by

\[
\frac QX\to\infty
\]

mean zero spacings and uses only a vanishing fraction `R/Q` of the ordinary local zero capacity. It is therefore not a close-spacing anomaly. More strongly, one may place infinitely many such order-one packets at sparse heights while changing the standard globally normalized Montgomery pair statistic by only `o(1)`, uniformly in its Fourier parameter.

So global pair correlation does not provide the missing actual-zeta input at the `YD-log J=O(1)` transition. The surviving target is genuinely local and mesoscopic: a depth-conditioned discrepancy theorem for the carrier phases `X gamma mod 2 pi` inside the `1/H` window.