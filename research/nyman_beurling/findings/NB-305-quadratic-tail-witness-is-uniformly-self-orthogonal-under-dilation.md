# NB-305 — quadratic tail witness is uniformly self-orthogonal under dilation

- **Date:** 2026-09-23
- **Status:** proved
- **Research line:** `nyman_beurling`
- **Depends on:** NB-290, NB-303, NB-304
- **Classification:** `EXACT-DERIVED + CANONICAL-NYMAN-SOURCE + DILATION-CORRELATION + MOVING-CUTOFF + SHARPNESS-SEPARATION + METHOD-BOUNDARY + NON-TARGET-AWARE + PRIOR-ART-AUDITED`

## Claim

`NB-304` shows that the quadratic scale in the source-tail estimate of `NB-303` is power-sharp. Its explicit scaled adjacent cancellation

\[
u_N:=g_N-\frac{N-1}{N}g_{N-1}\in U_N,
\qquad
U_N:=\operatorname{span}\{g_2,\ldots,g_N\},
\tag{1}
\]

retains an order-one fraction of its `L^2` mass below the moving cutoff `m_N=ceil(N^(2-eta))` for every fixed `0<eta<1`.

That does **not** make the same vector a witness for large projected-dilation overlap. Let `A_m` be the normalized Nyman dilation from `NB-290`,

\[
(A_mf)(x)=
\begin{cases}
\sqrt m\,f(mx),&0<x\le1/m,\\
0,&1/m<x<1.
\end{cases}
\tag{2}
\]

Then, for every `N>=8` and integer `m>=1`,

\[
\boxed{
\frac{|\langle u_N,A_m u_N\rangle|}{\|u_N\|_2^2}
\le
\frac{60}{\sqrt m}.
}
\tag{3}
\]

Combining this with the explicit tail lower bound already proved for the same `u_N` in `NB-304` gives

\[
\boxed{
\liminf_{N\to\infty}
\frac{\|1_{(0,1/m_N]}u_N\|_2^2}{\|u_N\|_2^2}
\ge\frac{\eta}{8},
\qquad
\frac{|\langle u_N,A_{m_N}u_N\rangle|}{\|u_N\|_2^2}
\longrightarrow0.
}
\tag{4}
\]

Thus the vector making source-tail localization power-sharp becomes asymptotically orthogonal to its own dilated copy throughout the same subquadratic regime. The quadratic support barrier from `NB-304` is real, but it supplies no quadratic lower-bound witness for the actual correlation operator

\[
T_m=P_{U_N}A_m|_{U_N},
\qquad
\beta_{N+1}(m)=\|T_m\|.
\]

## 1. Shell structure and an `L^1/L^2` comparison

On the reciprocal shell `I_k=(1/(k+1),1/k]`, `NB-304` gives the constant value

\[
 u_{N,k}
 =
 \frac{N-1}{N}
 \left\lfloor\frac{k}{N-1}\right\rfloor
 -
 \left\lfloor\frac{k}{N}\right\rfloor.
\tag{5}
\]

This sequence is periodic with period `P_N=N(N-1)`. Inside the first period, write `k=aN+r` with `0<=a<=N-2` and `0<=r<=N-1`. Then

\[
 u_{N,aN+r}
 =
 \begin{cases}
 -a/N,&r<N-1-a,\\[1mm]
 (N-1-a)/N,&r\ge N-1-a.
 \end{cases}
\tag{6}
\]

In particular,

\[
\|u_N\|_\infty\le1.
\tag{7}
\]

Because `|I_k|=1/(k(k+1))`,

\[
\|u_N\|_1
=
\sum_{k\ge1}\frac{|u_{N,k}|}{k(k+1)}.
\tag{8}
\]

For `a>=1`, the unweighted absolute sum of (6) over the first-period block `aN<=k<(a+1)N` is

\[
\frac{(N-1-a)(2a+1)}{N}\le3a.
\tag{9}
\]

Every shell in that block has weight at most `(aN)^(-2)`, while the `a=0` block contributes at most `2/N^2`. Hence the first period contributes at most `(2+3H_(N-2))/N^2`.

For translated periods use only periodicity and `|u_{N,k}|<=1`. In the `q`-th period, `q>=1`, every shell has index at least `qP_N`, so its total contribution is at most `1/(q^2P_N)`. Therefore

\[
\boxed{
\|u_N\|_1
\le
\frac{3H_{N-2}+2+\pi^2/3}{N^2}.
}
\tag{10}
\]

For a lower bound on the energy, keep only the positive spikes in the first period. If `1<=a<=floor((N-2)/2)`, equation (6) gives `a+1` positive shells with amplitude at least `1/2`, all satisfying `k<(a+1)N`. Thus

\[
\boxed{
\|u_N\|_2^2
\ge
\frac{H_{\lfloor N/2\rfloor}-1}{4N^2}.
}
\tag{11}
\]

For `N>=8`, setting `h=floor(N/2)` gives `H_N<=H_h+1` and `H_h>=H_4>2`, hence `H_h-1>=H_N/3`. Also `2+pi^2/3<2H_N`. Combining (10)-(11),

\[
\boxed{
\frac{\|u_N\|_1}{\|u_N\|_2^2}\le60.
}
\tag{12}
\]

So the `L^1` mass and `L^2` energy of this sharpness witness are comparable with an absolute constant, even though both are only of order `log N/N^2`.

## 2. Uniform decay of the self-correlation

By definition of `A_m`,

\[
\langle u_N,A_m u_N\rangle
=
\sqrt m\int_0^{1/m}u_N(x)\,\overline{u_N(mx)}\,dx.
\tag{13}
\]

Changing variables `y=mx`, then using (7), gives directly

\[
|\langle u_N,A_m u_N\rangle|
\le
\frac1{\sqrt m}\|u_N\|_\infty\|u_N\|_1
\le
\frac1{\sqrt m}\|u_N\|_1.
\tag{14}
\]

Equation (12) proves (3). Along `m_N=ceil(N^(2-eta))`,

\[
\frac{|\langle u_N,A_{m_N}u_N\rangle|}{\|u_N\|_2^2}
\le
60N^{-1+\eta/2}(1+o(1))
\longrightarrow0,
\tag{15}
\]

which combined with `NB-304` proves (4).

There is also an exact source-side consistency check. The covariance identity from `NB-290`,

\[
A_mg_j
=
\sqrt m\left(g_{mj}-\frac1j g_m\right),
\tag{16}
\]

implies

\[
\boxed{
A_mu_N
=
\sqrt m\left(
 g_{mN}-\frac{N-1}{N}g_{m(N-1)}
\right),
}
\tag{17}
\]

because the compensating `g_m` terms cancel. The scaled adjacent cancellation is therefore transported exactly to the corresponding scaled pair; its small correlation with the original pair is not a mismatch with the canonical dilation algebra.

## 3. Method boundary

Since `u_N` belongs to `U_N`,

\[
\langle u_N,T_mu_N\rangle=\langle u_N,A_mu_N\rangle.
\]

Equation (3) says that the `NB-304` sharpness direction has vanishing normalized Rayleigh coefficient. It does **not** upper-bound `beta_{N+1}(m)`: `T_m` need not be self-adjoint and

\[
\|T_m\|
=
\sup_{\|u\|=\|v\|=1}|\langle u,A_mv\rangle|
\]

allows distinct left and right singular vectors. A genuinely bilinear quadratic-scale obstruction can therefore still survive.

What (3)-(4) rule out is the remaining one-vector inference after `NB-304`: an order-one amount of retained support mass inside `(0,1/m]` need not produce an order-one overlap with the same vector after normalized dilation. For the exact vector making the support exponent sharp, those quantities separate asymptotically.

The next discriminating source-side object is the cross-correlation form

\[
B_{N,m}(u,v):=\langle u,A_mv\rangle,
\qquad u,v\in U_N,
\tag{18}
\]

or equivalently the singular spectrum of `T_m`. Any polynomial improvement beyond the `NB-303` support argument must exploit cancellation in this bilinear form; any matching lower bound must exhibit distinct vectors whose shell patterns remain coherent under multiplicative rescaling. Target-aware/sample information remains a separate route.

## 4. Adversarial and prior-art audit

The denominator in (3) uses the independent positive-spike lower bound (11), not the `NB-304` upper bound on `||u_N||_2`, so the sharpness estimate is not used in the wrong direction. The `m^(-1/2)` factor is the exact Jacobian and normalization in (13)-(14), and the only pointwise input is `||u_N||_infty<=1`. The result is deliberately a self-correlation statement, not an operator-norm statement. Nothing here estimates first-free sample occupation, a Ford packet, `mathfrak A_M`, or the Nyman target distance.

A fresh prior-art search around Nyman--Beurling Gram autocorrelation, integer dilations, and adjacent-generator geometry found the expected neighboring work: Balazard on integer fractional-part dilations, Ehm on explicit Nyman--Beurling Gram/reciprocity formulae, and recent Mellin-smoothed Gram decay on multiplicative ladders. None is load-bearing for (8)-(15), which are elementary consequences of the explicit `NB-304` shell witness, so `SOURCES.md` does not require a new dependency.

## Conclusion

`NB-304` established a genuine quadratic **support-localization** barrier. `NB-305` shows that its extremizing mechanism does not propagate to dilation self-overlap:

\[
\boxed{
\text{order-one subquadratic tail mass}
\quad\not\Rightarrow\quad
\text{order-one dilation Rayleigh overlap}.
}
\]

For the exact scaled adjacent cancellation witnessing the support barrier, the normalized overlap is at most `60/sqrt(m)` and therefore vanishes along `m=N^(2-eta)` even while an order-one tail fraction survives. The remaining quadratic question is genuinely bilinear: determine the singular vectors of `P_{U_N}A_m|_{U_N}`, rather than continue refining one-vector support concentration.