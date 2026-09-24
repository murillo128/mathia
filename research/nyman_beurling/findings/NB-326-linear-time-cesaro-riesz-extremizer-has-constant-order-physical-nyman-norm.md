# NB-326 — The linear-time Cesàro Riesz extremizer has physical Nyman norm Θ(1)

- **Date:** 2026-09-24
- **Status:** proved
- **Research line:** `nyman_beurling`
- **Depends on:** NB-317, NB-318
- **Resolves:** `CLUE-linear-time-cesaro-extremizer-physical-norm`
- **Classification:** `EXACT-DERIVED + SOURCE-SIDE + CESARO-RIESZ-EXTREMIZER + PHYSICAL-NYMAN-NORM + MOBIUS-COORDINATES + LINEAR-TIME + METHOD-DISCRIMINATOR + NON-TARGET-AWARE + PRIOR-ART-AUDITED`

## Claim

Let

\[
K_N:=\left\lfloor\frac N2\right\rfloor,
\qquad
\mathcal A_N:=\mathcal A_N(K_N)
=\left(\sum_{q=2}^N\frac{D_q(K_N)^2}{W(q)}\right)^{1/2},
\]

with `D_q` and `W(q)=J_2(q)/12` as in NB-317--NB-318. Normalize the exact fixed-time Cesàro Riesz extremizer by

\[
\widetilde B_q
:=
\frac{D_q(K_N)}{W(q)\mathcal A_N},
\qquad 2\le q\le N,
\tag{1}
\]

and reconstruct generator coordinates by finite Möbius inversion,

\[
x_j:=\sum_{\ell\le N/j}\mu(\ell)\widetilde B_{j\ell},
\qquad
a_j:=jx_j,
\qquad
u_N:=\sum_{j=2}^N a_jg_j.
\tag{2}
\]

Then `Q_N^0(u_N)=1` and `G_(u_N)(K_N)=-A_N`. Moreover there are absolute constants `0<c<C<infinity` such that, for every `N>=4`,

\[
\boxed{
c\le \|u_N\|_2^2\le C.
}
\tag{3}
\]

In particular,

\[
\boxed{
\|u_N\|_2^2=\Theta(1),
\qquad
\frac{\mathcal A_N(K_N)}{\|u_N\|_2}=\Theta(N^{3/2}).
}
\tag{4}
\]

Thus the exact direction which saturates the sharp `N^(3/2)` centered-Cesàro primitive evaluation at reciprocal time `K_N` does **not** acquire an additional positive power when transferred to the physical Nyman Hilbert metric. Its physical norm neither vanishes nor diverges polynomially: it stays of constant order.

This resolves the accepted clue `CLUE-linear-time-cesaro-extremizer-physical-norm` in the `supported` direction, specifically its `E_N=Theta(1)` branch. The result is source-side. It does not determine the global primitive amplification `Pi_N`, whose known adjacent witness lives at quadratic reciprocal time, and it does not imply target occupation, first-free gain, a Nyman approximation rate, or RH.

## 1. Normalization and a uniform coefficient bound

NB-317 gives the exact diagonal centered-Cesàro energy

\[
Q_N^0(u)=\sum_{q=2}^NW(q)|B_q(u)|^2
\tag{5}
\]

and the exact integer-time primitive

\[
G_u(K)=-\sum_{q=2}^NB_q(u)D_q(K).
\tag{6}
\]

Therefore (1) gives

\[
Q_N^0(u_N)=1,
\qquad
G_{u_N}(K_N)=-\mathcal A_N.
\tag{7}
\]

The same finding proves

\[
0\le D_q(K)\le2W(q).
\tag{8}
\]

Hence every normalized reduced-denominator coordinate obeys

\[
0\le\widetilde B_q\le\frac2{\mathcal A_N}.
\tag{9}
\]

Möbius inversion then gives, using `|mu(ell)|<=1`,

\[
|x_j|
\le
\sum_{\ell\le N/j}|\widetilde B_{j\ell}|
\le
\frac{2N}{j\mathcal A_N},
\]

so

\[
\boxed{
|a_j|=j|x_j|\le\frac{2N}{\mathcal A_N}.
}
\tag{10}
\]

NB-318 supplies an explicit linear-time lower bound. With

\[
\kappa:=\frac19-\frac{\zeta(2)-1}{8}>0,
\qquad
M:=2\lfloor N/2\rfloor,
\]

it proves

\[
\mathcal A_N
\ge
\frac{3\sqrt3}{4}\kappa M^{3/2}.
\tag{11}
\]

For `N>=4`, `M>=3N/4`. Put

\[
a_0:=
\frac{3\sqrt3}{4}\kappa\left(\frac34\right)^{3/2}>0.
\tag{12}
\]

Then

\[
\boxed{
\mathcal A_N\ge a_0N^{3/2}.
}
\tag{13}
\]

## 2. The physical norm is uniformly bounded above

The reciprocal-shell values of one generator are

\[
r_j(k)=\frac{k\bmod j}{j}.
\]

The physical norm can be bounded without any Gram estimate. For `1<=k<j`, `r_j(k)=k/j`; for `k>=j`, `|r_j(k)|<=1`. Therefore

\[
\begin{aligned}
\|g_j\|_2^2
&=
\sum_{k\ge1}\frac{|r_j(k)|^2}{k(k+1)}\\
&\le
\frac1{j^2}\sum_{k=1}^{j-1}\frac{k}{k+1}
+
\sum_{k=j}^{\infty}\frac1{k(k+1)}\\
&<\frac1j+\frac1j
=\frac2j.
\end{aligned}
\tag{14}
\]

Using (10), the triangle inequality, and `sum_(j<=N)j^(-1/2)<=2sqrt(N)`,

\[
\begin{aligned}
\|u_N\|_2
&\le
\sum_{j=2}^N|a_j|\,\|g_j\|_2\\
&\le
\frac{2N}{\mathcal A_N}\sqrt2
\sum_{j=2}^Nj^{-1/2}\\
&\le
\frac{4\sqrt2\,N^{3/2}}{\mathcal A_N}
\le
\frac{4\sqrt2}{a_0}.
\end{aligned}
\tag{15}
\]

Thus

\[
\boxed{
\|u_N\|_2^2\le\frac{32}{a_0^2}.
}
\tag{16}
\]

The important point is the exponent rather than the deliberately crude constant: the Möbius reconstruction cannot make this normalized extremizer physically large.

## 3. Its reciprocal mean is positive and has an exact denominator formula

For a generator,

\[
\mu_N(g_j)=\frac{j-1}{2j}.
\]

Since `a_j=jx_j`,

\[
\mu_N(u_N)
=
\frac12\sum_{j=2}^Nx_j(j-1).
\tag{17}
\]

Insert the inversion formula (2) and group by `q=j ell`. The coefficient of `B_q` is

\[
\frac12
\sum_{\substack{j\mid q\\j\ge2}}
\mu(q/j)(j-1).
\]

The omitted `j=1` term is zero, while the full divisor sum is

\[
\sum_{j\mid q}\mu(q/j)(j-1)
=
\sum_{d\mid q}\mu(d)\left(\frac qd-1\right)
=\varphi(q),
\tag{18}
\]

because `sum_(d|q) mu(d)=0` for `q>=2`. Hence

\[
\boxed{
\mu_N(u_N)
=
\frac12\sum_{q=2}^N\varphi(q)\widetilde B_q
\ge0.
}
\tag{19}
\]

This positivity is what prevents the primitive extremizer from hiding its entire excursion through an uncontrolled cancellation between the raw shell sum and its mean correction.

## 4. A two-case argument forces a uniform positive physical norm

Write `K=K_N`, `A=mathcal A_N`, `mu=mu_N(u_N)`, and

\[
S:=\sum_{k=1}^{K-1}u_N(k).
\]

NB-318's shell identity and (7) give

\[
G_{u_N}(K)=S-K\mu=-A,
\qquad
S=K\mu-A.
\tag{20}
\]

If `|S|>=A/2`, weighted Cauchy--Schwarz immediately gives

\[
|S|^2
\le
\|u_N\|_2^2
\sum_{k=1}^{K-1}k(k+1)
<
\frac{K^3}{3}\|u_N\|_2^2.
\]

Since `K<=N/2` and `A>=a_0N^(3/2)`,

\[
\boxed{
\|u_N\|_2^2\ge6a_0^2.
}
\tag{21}
\]

It remains to handle `|S|<A/2`. Equation (20) and `mu>=0` then imply

\[
K\mu>\frac A2,
\qquad
\boxed{
\mu\ge\frac A{2K}\ge\frac AN\ge a_0\sqrt N.
}
\tag{22}
\]

A large mean cannot be hidden from the physical norm on every linear shell block. Indeed, `r_j(k)-mu_N(g_j)` is `j`-periodic with zero mean, so on any interval of `L` consecutive integer shells its sum has absolute value at most `j`. Consequently, for `u_N`,

\[
\left|
\sum_{k=L}^{2L-1}(u_N(k)-\mu)
\right|
\le
\sum_{j=2}^N|a_j|j
\le
\frac{2N}{A}\sum_{j=2}^Nj
\le
\frac{N^2(N+1)}A.
\tag{23}
\]

Choose once and for all the integer

\[
C_0:=\left\lceil\frac4{a_0^2}\right\rceil,
\qquad
L:=C_0N.
\tag{24}
\]

For `N>=4`, `N+1<=5N/4`; using (13) and (22), equations (23)--(24) imply

\[
\left|
\sum_{k=L}^{2L-1}(u_N(k)-\mu)
\right|
\le
\frac12L\mu.
\tag{25}
\]

Therefore

\[
\sum_{k=L}^{2L-1}u_N(k)\ge\frac12L\mu.
\tag{26}
\]

Unweighted Cauchy--Schwarz on this block gives

\[
\sum_{k=L}^{2L-1}|u_N(k)|^2
\ge
\frac1L
\left|\sum_{k=L}^{2L-1}u_N(k)\right|^2
\ge
\frac{L\mu^2}{4}.
\tag{27}
\]

For `L<=k<2L`, `1/[k(k+1)]>=1/(4L^2)`. Hence

\[
\|u_N\|_2^2
\ge
\frac{\mu^2}{16L}
\ge
\boxed{
\frac{a_0^2}{16C_0}.
}
\tag{28}
\]

Together, (21) and (28) prove the lower half of (3). No asymptotic estimate for the Möbius coefficients and no cancellation hypothesis is required.

## 5. Consequence for the primitive route

NB-317 proves the matching upper bound `A_N(K_N)=O(N^(3/2))`, while NB-318 gives the lower bound used above. Combining those with (3) yields

\[
\frac{|G_{u_N}(K_N)|}{\|u_N\|_2}
=
\frac{\mathcal A_N(K_N)}{\|u_N\|_2}
=
\Theta(N^{3/2}).
\tag{29}
\]

So the linear-time Cesàro Riesz extremizer is **not** the profile that could close the global `N^2/sqrt(log N)` versus `O(N^(5/2))` Hilbert primitive window. It loses no physical mass, but neither does its physical normalization create an extra half-power: its Hilbert amplification remains exactly at the Cesàro exponent.

This sharpens the phase-space split left by NB-318. Linear reciprocal time supports `Theta(N^(3/2))` Hilbert amplification along the exact Cesàro extremizer, whereas the current explicit near-quadratic Hilbert obstruction comes from the different adjacent-cancellation profile whose maximal primitive excursion occurs at quadratic reciprocal time. Any larger global Hilbert amplification must therefore use a different profile and/or an evaluation time escaping the bounded linear window.

## 6. Prior-art audit and boundary

A fresh audit checked neighboring Nyman--Beurling work on Möbius/Fourier sums, Gram geometry, and coefficient control, including Maier--Rassias, Alouges--Darses--Hillion, and recent Gram-structure work of Carvill. These sources cover the surrounding fractional-part, Möbius, and Hilbert/Gram machinery, but I did not identify in the material reviewed an analysis of the physical `L^2(0,1)` norm of this particular finite-section reduced-denominator Riesz extremizer. This is an audit result, not a claim of bibliographic novelty.

No external theorem is load-bearing here: the proof uses only NB-317's exact denominator coordinates, NB-318's already-persisted linear-time lower bound, elementary Möbius inversion, periodic block discrepancy, and Cauchy--Schwarz. `SOURCES.md` therefore needs no new dependency.

The result remains entirely source-side. It does not identify the global extremizer for `Pi_N`, does not provide a moving projected-dilation upper or lower theorem beyond the existing findings, and does not address the actual first-free Ford datum or RH.
