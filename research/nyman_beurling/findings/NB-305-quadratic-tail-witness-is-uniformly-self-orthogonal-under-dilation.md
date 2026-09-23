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

Combining this with the explicit tail lower bound already proved for this same `u_N` in `NB-304` gives

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

Thus the vector that makes source-tail localization power-sharp becomes asymptotically orthogonal to its own dilated copy throughout that same subquadratic regime.

This is a strict method separation. The quadratic support barrier from `NB-304` is real, but it supplies **no quadratic lower-bound witness** for

\[
T_m=P_{U_N}A_m|_{U_N},
\qquad
\beta_{N+1}(m)=\|T_m\|.
\]

Any lower bound for `beta` near or below the quadratic scale must use a genuinely bilinear pair of source vectors, a singular-vector mechanism, or target/sample information.

## 1. Exact shell structure

On the reciprocal shell `I_k=(1/(k+1),1/k]`, write `u_{N,k}` for the constant value of `u_N`. `NB-304` gives

\[
\boxed{
 u_{N,k}
 =
 \frac{N-1}{N}
 \left\lfloor\frac{k}{N-1}\right\rfloor
 -
 \left\lfloor\frac{k}{N}\right\rfloor.
}
\tag{5}
\]

This sequence is periodic with period `P_N=N(N-1)`. Inside the first period, writing `k=aN+r` with `0<=a<=N-2` and `0<=r<=N-1`, one has

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

The same block structure also shows something not needed in `NB-304`: the `L^1` mass and the `L^2` energy of this sharpness witness have the same order, `log N/N^2`.

## 2. A uniform `L^1/L^2` comparison

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

Every shell in that block has weight at most `(aN)^(-2)`, while the `a=0` block contributes at most `2/N^2`. Thus the first period contributes at most `(2+3H_(N-2))/N^2`.

For the translated periods use only periodicity and `|u_{N,k}|<=1`. In the `q`-th period, `q>=1`, every shell has index at least `qP_N`, so the contribution is at most `1/(q^2 P_N)`. Therefore

\[
\boxed{
\|u_N\|_1
\le
\frac{3H_{N-2}+2+\pi^2/3}{N^2}.
}
\tag{10}
\]

For a lower bound on the energy, retain only the positive spikes in the first period. Put `A=floor((N-2)/2)`. For `1<=a<=A`, equation (6) gives `a+1` positive shells of amplitude at least `1/2`, all with `k<(a+1)N`. Hence

\[
\boxed{
\|u_N\|_2^2
\ge
\frac{H_{\lfloor N/2\rfloor}-1}{4N^2}.
}
\tag{11}
\]

For `N>=8`, if `h=floor(N/2)`, then `H_N<=H_h+1` and `H_h>=H_4>2`, so `H_h-1>=H_N/3`. Also `2+pi^2/3<2H_N`. Combining (10)-(11),

\[
\boxed{
\frac{\|u_N\|_1}{\|u_N\|_2^2}\le60.
}
\tag{12}
\]

No Gram inverse, condition number, or zero sample enters this estimate; it comes directly from the reciprocal-shell pattern of `u_N`.

## 3. Uniform decay of the self-correlation

From (2), the substitution `y=mx` gives the exact identity

\[
\boxed{
\langle u_N,A_m u_N\rangle
=
\frac1{\sqrt m}
\int_0^1
u_N(y/m)\,\overline{u_N(y)}\,dy.
}
\tag{13}
\]

In (13), the first factor is the ordinary function value `u_N(y/m)`. Using (7),

\[
|\langle u_N,A_m u_N\rangle|
\le
\frac1{\sqrt m}\|u_N\|_1.
\tag{14}
\]

Equation (12) proves (3). For `m_N=ceil(N^(2-eta))`,

\[
\frac{|\langle u_N,A_{m_N}u_N\rangle|}{\|u_N\|_2^2}
\le
60N^{-1+\eta/2}(1+o(1))
\longrightarrow0,
\tag{15}
\]

which combined with `NB-304` proves (4).

The covariance identity from `NB-290`,

\[
A_mg_j
=
\sqrt m\left(g_{mj}-\frac1j g_m\right),
\tag{16}
\]

also gives the exact source-side consistency check

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

because the compensating `g_m` terms cancel. The decay in (3) is therefore not an artifact of mismatching the dilation algebra: the scaled adjacent cancellation is transported exactly to the corresponding scaled pair and still becomes asymptotically orthogonal to the original pair.

## 4. Method boundary

The conclusion is intentionally narrower than a bound on `beta_{N+1}(m)`. Since

\[
\langle u_N,T_mu_N\rangle=\langle u_N,A_mu_N\rangle,
\]

(3) says that the `NB-304` sharpness direction has vanishing normalized Rayleigh coefficient. But `T_m` need not be self-adjoint, and

\[
\|T_m\|
=
\sup_{\|u\|=\|v\|=1}|\langle u,A_mv\rangle|
\]

allows different left and right singular vectors. Thus (3) gives **no upper bound** on `beta` and does not rule out a genuinely bilinear quadratic-scale obstruction.

What it does rule out is the remaining one-vector inference after `NB-304`: large retained mass in `(0,1/m]` need not produce large overlap with the same vector after normalized dilation. For the exact vector making the support exponent sharp, those quantities separate asymptotically.

The next source-side object is therefore the cross-correlation form

\[
B_{N,m}(u,v):=\langle u,A_mv\rangle,
\qquad u,v\in U_N,
\tag{18}
\]

or equivalently the singular spectrum of `T_m`. Any polynomial improvement beyond the `NB-303` support argument must exploit cancellation in this bilinear form; any matching lower bound must exhibit distinct vectors whose shell patterns remain coherent under multiplicative rescaling. Target-aware/sample information remains a separate route.

## 5. Adversarial and prior-art audit

The denominator in (3) uses the independent positive-spike lower bound (11), not the `NB-304` upper bound on `||u_N||_2`; this avoids reversing the direction of the sharpness estimate. The `m^(-1/2)` factor is the exact Jacobian/normalization from (13), and the only pointwise input is `||u_N||_infty<=1`. The result is deliberately a self-correlation statement, not an operator-norm statement. Nothing here estimates first-free sample occupation, a Ford packet, `mathfrak A_M`, or the Nyman target distance.

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