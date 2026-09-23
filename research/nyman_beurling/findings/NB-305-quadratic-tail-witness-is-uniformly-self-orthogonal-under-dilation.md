# NB-305 — quadratic tail witness is uniformly self-orthogonal under dilation

- **Date:** 2026-09-23
- **Status:** proved
- **Research line:** `nyman_beurling`
- **Depends on:** NB-290, NB-303, NB-304
- **Classification:** `EXACT-DERIVED + CANONICAL-NYMAN-SOURCE + DILATION-CORRELATION + MOVING-CUTOFF + SHARPNESS-SEPARATION + METHOD-BOUNDARY + NON-TARGET-AWARE + PRIOR-ART-AUDITED`

## Claim

`NB-304` shows that the quadratic scale in the source-tail estimate of `NB-303` is power-sharp. Its explicit scaled adjacent cancellation

\[
u_N
:=
g_N-\frac{N-1}{N}g_{N-1}
\in U_N,
\qquad
U_N:=\operatorname{span}\{g_2,\ldots,g_N\},
\tag{1}
\]

retains an order-one fraction of its `L^2` mass below the moving cutoff

\[
m_N=\lceil N^{2-\eta}\rceil,
\qquad 0<\eta<1.
\]

That does **not** make the same vector a witness for large projected-dilation overlap. In fact the opposite happens: its normalized self-correlation with every multiplicative dilation is uniformly small.

Let `A_m` be the normalized Nyman dilation from `NB-290`,

\[
(A_mf)(x)
=
\begin{cases}
\sqrt m\,f(mx),&0<x\le1/m,\\
0,&1/m<x<1.
\end{cases}
\tag{2}
\]

Then there is an absolute constant `C` such that, for every `N>=8` and every integer `m>=1`,

\[
\boxed{
\frac{|\langle u_N,A_m u_N\rangle|}{\|u_N\|_2^2}
\le
\frac{C}{\sqrt m}.
}
\tag{3}
\]

The proof below gives `C=60`.

Combining (3) with the explicit tail lower bound already proved for this same `u_N` in `NB-304` yields, for every fixed `0<\eta<1`,

\[
\boxed{
\liminf_{N\to\infty}
\frac{\|1_{(0,1/m_N]}u_N\|_2^2}{\|u_N\|_2^2}
\ge
\frac{\eta}{8},
\qquad
\frac{|\langle u_N,A_{m_N}u_N\rangle|}{\|u_N\|_2^2}
\longrightarrow0.
}
\tag{4}
\]

Thus the vector that makes source-tail localization power-sharp becomes asymptotically orthogonal to its own dilated copy throughout the same subquadratic regime.

This is a strict method separation. The quadratic support barrier from `NB-304` is real, but it supplies **no quadratic lower-bound witness for the actual correlation operator**

\[
T_m=P_{U_N}A_m|_{U_N},
\qquad
\beta_{N+1}(m)=\|T_m\|.
\]

Any lower bound for `beta` near or below the quadratic scale must use a genuinely bilinear pair of source vectors, a singular-vector mechanism, or target/sample information. It cannot be obtained by feeding the `NB-304` extremizer into the corresponding Rayleigh quotient.

## 1. Exact shell structure recalled from NB-304

On the reciprocal shell

\[
I_k=(1/(k+1),1/k],
\]

write `u_{N,k}` for the constant value of `u_N`. `NB-304` gives

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

The sequence is periodic with period

\[
P_N=N(N-1).
\tag{6}
\]

Inside its first period write

\[
k=aN+r,
\qquad
0\le a\le N-2,
\qquad
0\le r\le N-1.
\]

Then

\[
 u_{N,aN+r}
 =
 \begin{cases}
 -a/N,&r<N-1-a,\\[1mm]
 (N-1-a)/N,&r\ge N-1-a.
 \end{cases}
\tag{7}
\]

In particular,

\[
\|u_N\|_{\infty}\le1.
\tag{8}
\]

The same block structure also shows something not needed in `NB-304`: the `L^1` mass and the `L^2` energy of `u_N` have the same order, namely `log N/N^2`.

## 2. An `L^1/L^2` comparison specific to the sharpness witness

Because the shell `I_k` has length

\[
|I_k|=\frac1{k(k+1)},
\]

we have

\[
\|u_N\|_1
=
\sum_{k\ge1}
\frac{|u_{N,k}|}{k(k+1)}.
\tag{9}
\]

Consider first the initial period. For `a>=1`, the unweighted absolute sum over the block `aN<=k<(a+1)N` is, by (7),

\[
\frac{(N-1-a)(2a+1)}{N}
\le3a.
\tag{10}
\]

Every shell in that block has weight at most `(aN)^{-2}`. The `a=0` block contributes at most `2/N^2`. Hence the first period contributes at most

\[
\frac{2+3H_{N-2}}{N^2}.
\tag{11}
\]

For the later periods use only periodicity and `|u_{N,k}|<=1`. In the `q`-th translated period, `q>=1`, every shell has index at least `qP_N`, while there are `P_N` residues. Therefore its contribution is at most

\[
\frac1{q^2P_N}.
\]

Summing over `q>=1` gives

\[
\boxed{
\|u_N\|_1
\le
\frac{3H_{N-2}+2+\pi^2/3}{N^2}.
}
\tag{12}
\]

For a lower bound on the energy, keep only the positive spikes in the first period. Put

\[
A=\left\lfloor\frac{N-2}{2}\right\rfloor.
\]

For `1<=a<=A`, (7) gives `a+1` positive shells with amplitude at least `1/2`. All of them satisfy

\[
k<(a+1)N,
\]

so each has weight greater than `((a+1)N)^{-2}`. Consequently

\[
\boxed{
\|u_N\|_2^2
\ge
\frac{H_{\lfloor N/2\rfloor}-1}{4N^2}.
}
\tag{13}
\]

For `N>=8`, if `h=\lfloor N/2\rfloor` then

\[
H_N\le H_h+1,
\qquad
H_h\ge H_4>2,
\]

and hence

\[
H_h-1\ge\frac13H_N.
\]

Also `2+pi^2/3<2H_N` for `N>=8`. Combining these elementary comparisons with (12)-(13) gives

\[
\boxed{
\frac{\|u_N\|_1}{\|u_N\|_2^2}
\le60,
\qquad N\ge8.
}
\tag{14}
\]

No Gram inverse, condition number, or zero sample enters this estimate. It is a direct consequence of the explicit reciprocal-shell pattern of the `NB-304` witness.

## 3. Uniform decay of the dilation Rayleigh coefficient

From the definition (2), a change of variable `y=mx` gives the exact identity

\[
\langle u_N,A_m u_N\rangle
=
\frac1{\sqrt m}
\int_0^1
u_N(y/m)\,\overline{u_N(y)}\,dy.
\tag{15}
\]

Using (8),

\[
|\langle u_N,A_m u_N\rangle|
\le
\frac1{\sqrt m}\|u_N\|_1.
\tag{16}
\]

Equation (14) now gives

\[
\boxed{
\frac{|\langle u_N,A_m u_N\rangle|}{\|u_N\|_2^2}
\le
\frac{60}{\sqrt m}.
}
\tag{17}
\]

For the moving cutoff used by `NB-304`,

\[
m_N=\lceil N^{2-\eta}\rceil,
\]

this becomes

\[
\frac{|\langle u_N,A_{m_N}u_N\rangle|}{\|u_N\|_2^2}
\le
60N^{-1+\eta/2}(1+o(1))
\longrightarrow0
\tag{18}
\]

for every fixed `0<eta<1`. Together with the `NB-304` tail lower bound for the same vector, this proves (4).

There is also an exact source-side consistency check. The covariance identity from `NB-290`,

\[
A_mg_j
=
\sqrt m\left(g_{mj}-\frac1j g_m\right),
\tag{19}
\]

shows that the compensating `g_m` terms cancel for (1):

\[
\boxed{
A_mu_N
=
\sqrt m\left(
 g_{mN}
 -\frac{N-1}{N}g_{m(N-1)}
\right).
}
\tag{20}
\]

Thus (17) is not caused by a mismatch with the canonical dilation algebra. The scaled adjacent cancellation is transported exactly to the corresponding scaled pair; nevertheless its correlation with the original pair decays like `m^{-1/2}` after normalization by its own energy.

## 4. What this does and does not settle

The conclusion is intentionally narrower than a bound on `beta_{N+1}(m)`. Since

\[
\langle u_N,T_mu_N\rangle
=
\langle u_N,A_mu_N\rangle,
\]

(17) says that the specific `NB-304` sharpness direction has vanishing normalized Rayleigh coefficient. But `T_m` need not be self-adjoint, and

\[
\|T_m\|
=
\sup_{\|u\|=\|v\|=1}
|\langle u,A_mv\rangle|
\]

allows different left and right singular vectors. Therefore (17) gives **no upper bound** on `beta` and does not rule out a genuinely bilinear quadratic-scale obstruction.

What it does rule out is an inference that was still logically available after `NB-304`: large retained mass of one vector inside `(0,1/m]` does not imply that this vector has a large overlap with its own normalized dilation. For the explicit vector that makes the support-localization exponent sharp, those two quantities are asymptotically separated as strongly as possible in the moving regime (4).

The next discriminating source-side object is therefore not another one-vector tail functional. It is the cross-correlation form

\[
B_{N,m}(u,v)
:=
\langle u,A_mv\rangle,
\qquad u,v\in U_N,
\tag{21}
\]

or, equivalently, the singular spectrum of `T_m`. Any polynomial improvement beyond the `NB-303` support argument must exploit cancellation in this bilinear form; any matching lower bound must exhibit distinct vectors whose shell patterns remain coherent under multiplicative rescaling. Target-aware/sample information remains a separate possible route.

## 5. Adversarial checks

The estimate is not using the `NB-304` upper bound on `||u_N||_2`; the needed denominator control is the independent positive-spike lower bound (13). This avoids reversing the direction of the sharpness estimate.

The `m^{-1/2}` factor comes from the normalized isometric dilation and the exact substitution in (15), not from treating `A_m` as a contraction. The pointwise bound needed after that substitution is only `||u_N||_infty<=1`, which follows immediately from the exact first-period formula and periodicity.

The conclusion is deliberately phrased as self-correlation/Rayleigh decay, not operator-norm decay. Replacing the former by the latter would be invalid without controlling distinct singular vectors.

Nothing here estimates first-free sample occupation, the Ford packet, `mathfrak A_M`, or the Nyman distance to the target. No RH-equivalent rate is claimed.

## 6. Prior-art audit

A fresh search was made around Nyman--Beurling Gram autocorrelation, integer dilations, and adjacent-generator geometry. Classical and recent neighboring work includes Balazard's study of integer dilations of the fractional-part function, Ehm's explicit Gram-matrix/reciprocity analysis, and recent Mellin-smoothed Gram decay on multiplicative ladders. Those works form the natural prior-art boundary for generator correlations, but the present statement is only the elementary line-local comparison (12)-(18) for the explicit `NB-304` witness. No external theorem is load-bearing for the proof, so `SOURCES.md` does not need a new dependency.

## Conclusion

`NB-304` established a genuine quadratic **support-localization** barrier. `NB-305` shows that its extremizing mechanism does not propagate to actual dilation self-overlap:

\[
\boxed{
\text{order-one subquadratic tail mass}
\quad\not\Rightarrow\quad
\text{order-one dilation Rayleigh overlap}.
}
\]

For the exact scaled adjacent cancellation that witnesses the support barrier, the normalized overlap is at most `60/sqrt(m)` and therefore vanishes even along `m=N^{2-eta}` where an order-one tail fraction survives. The remaining quadratic question is consequently genuinely bilinear: determine the singular vectors of `P_{U_N}A_m|_{U_N}`, rather than continue refining one-vector support concentration.