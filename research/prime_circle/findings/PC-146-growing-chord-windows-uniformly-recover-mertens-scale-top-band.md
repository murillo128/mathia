# PC-146 — growing chord windows uniformly recover the Mertens-scale top band

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `DECISIVE-BOUNDARY`. PC-145 proves that bounded chord windows recover the isolated gap-two top-band projector in the iterated limit `x -> infinity` followed by `H -> infinity`. The remaining mesoscopic question is whether that conclusion depends on the order of limits: a cutoff `H=H(x)` could in principle grow with the primorial scale and retain a coherent tail that is invisible in every fixed-window comparison.

It does not. Let

\[
N_x=\prod_{p\le x}p,
\qquad
L_x=\beta_{N_x}P_x+R_x,
\]

be the primitive-shell inverse-square chord Laplacian and exact gap-two matching decomposition of PC-142--PC-145, with `rank(P_x)=E_x`. For an integer cutoff `H>=3`, let `L_x^(H)` retain the exact matching block and only remainder edges of symmetric cyclic distance at most `H`, and let `Q_x` and `Q_x^(H)` be the respective isolated rank-`E_x` top-band projectors.

Then for every `epsilon` with `0<epsilon<1/2` there are constants `C_epsilon<infinity` and `x_0` such that, for every `x>=x_0` and every cutoff `H>=3`,

\[
\boxed{
\frac{\log x}{E_x}
\left\|Q_x-Q_x^{(H)}\right\|_F^2
\le
C_\epsilon H^{-2+2\epsilon}.
}
\tag{1}
\]

When `H>=N_x/2` the left side is zero, so the statement is understood trivially there. In particular, for **every** integer sequence `H_x -> infinity`, with no restriction on its rate,

\[
\boxed{
\frac{\log x}{E_x}
\left\|Q_x-Q_x^{(H_x)}\right\|_F^2
\longrightarrow0.
}
\tag{2}
\]

Thus there is no hidden mesoscopic chord scale at the Mertens/Frobenius level. The average top-band rotation can be recovered by any diverging local window, however slowly it grows. This strengthens the double-limit locality theorem of PC-145 and closes its order-of-limits escape route.

## 1. Uniform CRT control of the discarded tail

Write

\[
T_x^{(H)}:=R_x-R_x^{(H)}\succeq0
\]

for the discarded long-chord Laplacian, and normalize its matching-compressed energy by

\[
t_{x,H}
:=
\frac{\operatorname{tr}(P_xT_x^{(H)}P_x)}{E_xN_x^2}.
\tag{3}
\]

PC-144 gives the exact conditional reduced-residue survival factor for an oriented gap-two pair. For every signed offset `h notin {0,2}`,

\[
r_x^+(h)
=
\mathbf 1_{\{2\mid h,\ h\not\equiv1\ (3)\}}
Q_x
\prod_{\substack{5\le p\le x\\p\mid h(h-2)}}
\frac{p-2}{p-3},
\qquad
Q_x:=\prod_{5\le p\le x}\frac{p-3}{p-2}.
\tag{4}
\]

Introduce the full finite-offset correction

\[
S(h):=
\prod_{\substack{p\ge5\\p\mid h(h-2)}}
\frac{p-2}{p-3}.
\tag{5}
\]

Every local factor exceeds one, hence the finite product in (4) is bounded by `S(h)` for **all** `x`; no stabilization of the prime divisors of `h(h-2)` is needed. PC-144 also proves

\[
(\log x)Q_x=O(1)
\tag{6}
\]

and, for every `epsilon>0`,

\[
S(h)\ll_\epsilon (1+|h|)^{2\epsilon}.
\tag{7}
\]

The normalized inverse-square chord weight satisfies the uniform estimate

\[
0\le\frac{w_h(N_x)}{N_x^2}
\le\frac1{16h^2}
\qquad
(1\le |h|\le N_x/2).
\tag{8}
\]

Combining the exact trace formula of PC-144 with (4)--(8), for every `0<epsilon<1/2` and all sufficiently large `x`, uniformly in `H`,

\[
\begin{aligned}
(\log x)t_{x,H}
&\ll_\epsilon
\sum_{\substack{|h|>H\\|h|\le N_x/2}}
\frac{S(h)}{h^2}\\
&\ll_\epsilon
\sum_{|h|>H}|h|^{-2+2\epsilon}\\
&\ll_\epsilon H^{-1+2\epsilon}.
\end{aligned}
\tag{9}
\]

This is the uniform estimate that is stronger than the fixed-`H` dominated-convergence step used in PC-145. In particular, the matching-compressed Mertens mass of the discarded tail vanishes for any diagonal choice `H=H(x)->infinity`.

## 2. The full tail is uniformly small in operator norm

PC-145 bounds the weighted degree of the discarded graph by the summable inverse-square tail. With

\[
\sigma_H:=\sum_{h>H}\frac1{h^2},
\qquad
a_H:=\frac{\sigma_H}{4},
\]

one has

\[
\|T_x^{(H)}\|\le a_HN_x^2.
\tag{10}
\]

Since `sigma_H<=1/H`,

\[
\boxed{
\|T_x^{(H)}\|\le\frac{N_x^2}{4H}.
}
\tag{11}
\]

Again this is uniform in the arithmetic of the shell and in the relation between `H` and `x`.

## 3. Every cutoff has the same isolated band and a uniform matching bound

PC-142 supplies the spectral cliff

\[
\|R_x\|\le\rho_{N_x}<\beta_{N_x},
\qquad
\delta_{N_x}:=\beta_{N_x}-\rho_{N_x}\ge c_6N_x^2,
\qquad
c_6>0.
\tag{12}
\]

Because `0<=R_x^(H)<=R_x`, every truncated operator has exactly the same isolated rank-`E_x` top band. The Sylvester estimate of PC-143/PC-145 gives

\[
\left\|(I-Q_x^{(H)})P_x\right\|_F^2
\le
\frac{\rho_{N_x}}{\delta_{N_x}^2}
\operatorname{tr}(P_xR_x^{(H)}P_x)
\le
\frac{\rho_{N_x}}{\delta_{N_x}^2}
\operatorname{tr}(P_xR_xP_x).
\tag{13}
\]

PC-144 proves

\[
\frac{\log x}{E_xN_x^2}
\operatorname{tr}(P_xR_xP_x)
\longrightarrow C_{\rm gap}<\infty,
\tag{14}
\]

while `rho_N/N^2` and `N^2/delta_N` are uniformly bounded in this regime. Therefore there are `K<infinity` and `x_0` such that simultaneously for every `x>=x_0` and every cutoff `H`,

\[
\boxed{
\frac{\log x}{E_x}
\left\|(I-P_x)Q_x^{(H)}\right\|_F^2
\le K.
}
\tag{15}
\]

The crucial point is the quantifier: the matching-space control is uniform in `H`, so choosing the window after choosing `x` does not invalidate the perturbation estimate.

## 4. Uniform projector comparison

PC-145 derives, for the full and truncated projectors,

\[
\left\|Q_x-Q_x^{(H)}\right\|_F^2
\le
\frac4{\delta_{N_x}^2}
\left[
\|T_x^{(H)}\|\operatorname{tr}(P_xT_x^{(H)}P_x)
+
\|T_x^{(H)}\|^2
\left\|(I-P_x)Q_x^{(H)}\right\|_F^2
\right].
\tag{16}
\]

Multiply by `log x/E_x`, use `delta_N>=c_6N^2`, and insert (9), (11), and (15). Uniformly for `x>=x_0`,

\[
\frac{\log x}{E_x}
\left\|Q_x-Q_x^{(H)}\right\|_F^2
\ll_\epsilon
\frac1H H^{-1+2\epsilon}
+
\frac1{H^2}.
\tag{17}
\]

Hence

\[
\boxed{
\frac{\log x}{E_x}
\left\|Q_x-Q_x^{(H)}\right\|_F^2
\ll_\epsilon H^{-2+2\epsilon},
}
\tag{18}
\]

which proves (1). Substituting any `H=H_x->infinity` proves (2) directly; no exchange of limits is required.

## 5. Prior-art and novelty audit

The ingredients remain classical and are already anchored by PC-143--PC-145. The invariant-subspace comparison is standard Davis--Kahan/Sylvester perturbation theory. The arithmetic input is finite CRT counting for reduced residues together with the ordinary Mertens product, in the same prior-art neighborhood as H. L. Montgomery and R. C. Vaughan, **On the distribution of reduced residues**, *Annals of Mathematics* 123 (1986), 311--333, and Farzad Aryan, **The distribution of k-tuples of reduced residues**, *Mathematika* 61 (2015), 72--88.

A fresh directed search across reduced-residue distributions, long-range graph-Laplacian truncation, spectral-projector perturbation, and chord-window localization did not locate this exact uniform-in-window statement for the Prime-Circle primitive-shell operator. That is not evidence of historical priority, and no novelty is claimed for the component estimates. The durable content is the exact quantifier upgrade forced by combining the already-established PC-144 arithmetic majorant with the PC-145 projector inequality.

The RH audit is negative. The uniform bound uses only the summability of `1/h^2`, a divisor-growth estimate for the finite CRT correction `S(h)`, Mertens thinning, and a fixed spectral gap. It introduces no analytic continuation, functional equation, gamma factor, zero divisor, or critical-line symmetry. The mesoscopic-window regime therefore classicalizes rather than supplying a new RH mechanism.

## 6. Boundary and falsification surface

The theorem is specifically a normalized-Frobenius statement at the natural Mertens scale. It does not imply operator-norm locality. PC-143 already shows that fixed short offsets such as `4` and `6` generate sparse directions with nonvanishing worst principal angle, so allowing `H_x->infinity` cannot repair operator-norm locking.

The quantitative exponent in (1) is not claimed sharp. It comes from the soft bound `S(h)\ll_\epsilon |h|^{2\epsilon}` and `sum_{h>H}h^{-2+2epsilon}\ll H^{-1+2epsilon}`. Sharper average-order information for `S(h)` could improve the power of `H` without changing the locality conclusion.

A decisive audit is to verify the uniform finite-`x` inequality behind (9):

\[
(\log x)r_x^+(h)
\le C\,S(h)
\]

for all signed representatives `|h|<=N_x/2` once `x` is large enough. This follows exactly from (4), the monotonic inclusion of the finite local-factor product in `S(h)`, and boundedness of `(log x)Q_x`. Failure of that inequality would invalidate the diagonal-window upgrade. The projector step can then be checked independently from (16), whose constants depend only on the universal PC-142 spectral cliff.

## 7. Consequence for the research line

PC-145 left open the possibility that the order of limits concealed a mesoscopic collective effect. Equation (2) removes that possibility at the average Mertens scale: **there is no special growing chord scale to discover there**. Any diverging chord window captures the full projector modulo `o(E_x/log x)` in squared Frobenius distance.

What remains genuinely outside this boundary is the sparse operator-norm defect, internal spacings inside the isolated band, nonlinear combinations of local windows, and cross-level transport. Those questions cannot be justified merely by making the cutoff grow with the primorial conductor.