# NB-301 — early-shell Möbius inversion gives cubic moving-cutoff source compression

- **Date:** 2026-09-23
- **Status:** proved
- **Research line:** `nyman_beurling`
- **Depends on:** NB-019, NB-020, NB-299, NB-300
- **Classification:** `EXACT-DERIVED + CANONICAL-NYMAN-SOURCE + EARLY-SHELL-MOBIUS-INVERSION + POLYNOMIAL-LINFTY-EMBEDDING + SOURCE-GRAM-LOWER-BOUND + MOVING-CUTOFF + PROJECTED-DILATION-ESCAPE + CUBIC-SCALE-NO-GO + PRIOR-ART-AUDITED`

## Claim

`NB-300` removes the opaque fixed-section constant from the projected-dilation argument of `NB-299` by using the common reciprocal-cell period

\[
P_{n-1}=\operatorname{lcm}(2,\ldots,n-1),
\]

and obtains source compression once `m/P_(n-1) -> infinity`. That is explicit but still exponential in the lower cutoff. The lcm is not intrinsic here either.

Let

\[
U_N=\operatorname{span}\{g_2,\ldots,g_N\},
\qquad
N\ge2,
\]

with the canonical Bagchi generators

\[
g_j(x)=\left\{\frac1{jx}\right\}-\frac1j\left\{\frac1x\right\}.
\]

For every

\[
u=\sum_{j=2}^N a_jg_j\in U_N
\]

one has the coefficient-stability and finite-section embedding bounds

\[
\boxed{
\sum_{j=2}^N|a_j|
\le
\sqrt6\,N^{3/2}\|u\|_2,
}
\tag{1}
\]

\[
\boxed{
\|u\|_{L^\infty(0,1)}
\le
\sqrt6\,N^{3/2}\|u\|_2.
}
\tag{2}
\]

In particular, if `G_N^(src)` is the canonical source Gram on `g_2,...,g_N`, then

\[
\boxed{
\lambda_{\min}(G_N^{\rm src})
\ge
\frac1{6N^3}.
}
\tag{3}
\]

No zero information, target coefficients, lcm period, or Gram inverse is used in these estimates. They follow from the first `N` harmonic shells and finite Möbius inversion.

Let `A_m` be the normalized integer dilation and define the source overlap

\[
\beta_{N+1}(m)
=
\|P_{U_N}A_m|_{U_N}\|.
\]

Since `A_mv` is supported on `(0,1/m]`, (2) gives

\[
\boxed{
\beta_{N+1}(m)^2
\le
\min\left\{1,\frac{6N^3}{m}\right\}.
}
\tag{4}
\]

Equivalently, in the notation of `NB-299`--`NB-300`, where the old section is `U=V_(n-1)` and `N=n-1`,

\[
\boxed{
\beta_n(m)^2
\le
\min\left\{1,\frac{6(n-1)^3}{m}\right\}.
}
\tag{5}
\]

Thus

\[
\boxed{
\frac{m}{(n-1)^3}\to\infty
\quad\Longrightarrow\quad
\beta_n(m)\to0,
}
\tag{6}
\]

even when `n` moves. This replaces the sufficient super-lcm regime of `NB-300` by a super-cubic one.

For an off-critical zero packet `Z`, put

\[
\delta_Z
=
\min_{\rho\in Z}\left(\Re\rho-\frac12\right)>0,
\qquad
K=K_{n-1,Z}.
\]

Let

\[
\varepsilon^{\rm cub}_{m,n}
:=
\min\left\{1,\sqrt{\frac{6(n-1)^3}{m}}\right\}.
\tag{7}
\]

Whenever `epsilon^(cub)_(m,n)<1`, the exact `NB-297`/`NB-299` factorization yields

\[
\boxed{
\|\Xi_{m,n,Z}\|
\le
\|K\|
\frac{\bigl(m^{-\delta_Z}+\varepsilon^{\rm cub}_{m,n}\bigr)^2}
{1-(\varepsilon^{\rm cub}_{m,n})^2}.
}
\tag{8}
\]

Hence every moving family `(Z_X,n_X,m_X)` satisfying

\[
\frac{m_X}{(n_X-1)^3}\to\infty,
\qquad
\delta_{Z_X}\log m_X\to\infty
\tag{9}
\]

obeys

\[
\boxed{
\frac{\|\Xi_{m_X,n_X,Z_X}\|}
{\|K_{n_X-1,Z_X}\|}
\to0.
}
\tag{10}
\]

The surviving projected-dilation window is therefore much narrower than `NB-300` left open. Persistent normalized escape sampling must now remain at or below a cubic dilation scale, or retain weak off-critical damping. A target-relative statement still has the separate sample-conditioning factor from `NB-299`; this result removes the source-side lcm/Gram-conditioning escape, not the target occupation problem.

---

## 1. First-shell differences recover every finite coefficient

For integer `k>=1`, let `I_k=(1/(k+1),1/k]`. The exact shell identity is

\[
g_j|_{I_k}=\left\{\frac{k}{j}\right\}.
\tag{11}
\]

Write `u_k` for the value of `u` on `I_k` and put `u_0=0`. Define

\[
b_k:=u_k-u_{k-1}.
\tag{12}
\]

Since

\[
\left\{\frac{k}{j}\right\}
-
\left\{\frac{k-1}{j}\right\}
=
\frac1j-\mathbf1_{j\mid k},
\tag{13}
\]

we have

\[
b_k
=A_0-
\sum_{\substack{j\mid k\\2\le j\le N}}a_j,
\qquad
A_0:=\sum_{j=2}^N\frac{a_j}{j}=u_1=b_1.
\tag{14}
\]

For `j>1`, Möbius inversion cancels the constant `A_0` because

\[
\sum_{d\mid j}\mu(j/d)=0.
\]

Therefore

\[
\boxed{
a_j
=-\sum_{d\mid j}\mu(j/d)b_d,
\qquad 2\le j\le N.}
\tag{15}
\]

This is the homogeneous finite-section version of the early-shell inversion used in `NB-020`. It applies to every vector of the section, not only to the target-selected projection or residual.

## 2. The shell Hilbert norm controls the difference data

Because `u` is constant on harmonic shells,

\[
\|u\|_2^2
=
\sum_{k\ge1}
\frac{|u_k|^2}{k(k+1)}.
\tag{16}
\]

For the first `N` differences,

\[
\begin{aligned}
\sum_{k=1}^N\frac{|b_k|^2}{k^2}
&\le
2\sum_{k=1}^N\frac{|u_k|^2}{k^2}
+2\sum_{k=2}^N\frac{|u_{k-1}|^2}{k^2}\\
&\le
4\|u\|_2^2+2\|u\|_2^2.
\end{aligned}
\]

Thus

\[
\boxed{
\sum_{k=1}^N\frac{|b_k|^2}{k^2}
\le6\|u\|_2^2.
}
\tag{17}
\]

The constants are intentionally elementary. The first comparison uses

\[
\frac1{k^2}
\le
\frac2{k(k+1)},
\]

and after writing `r=k-1`, the second uses

\[
\frac1{(r+1)^2}
\le
\frac1{r(r+1)}.
\]

No tail approximation or asymptotic estimate is involved.

## 3. Möbius inversion gives a polynomial coefficient budget

From (15), `|mu|<=1`, and a change of order,

\[
\begin{aligned}
\sum_{j=2}^N|a_j|
&\le
\sum_{j=2}^N\sum_{d\mid j}|b_d|\\
&\le
\sum_{d=1}^N|b_d|\left\lfloor\frac Nd\right\rfloor.
\end{aligned}
\tag{18}
\]

Apply Cauchy--Schwarz in the form

\[
\sum_{d=1}^N|b_d|\left\lfloor\frac Nd\right\rfloor
=
\sum_{d=1}^N
\frac{|b_d|}{d}
\left(d\left\lfloor\frac Nd\right\rfloor\right).
\]

Since

\[
d\left\lfloor\frac Nd\right\rfloor\le N,
\]

we obtain

\[
\sum_{j=2}^N|a_j|
\le
\left(\sum_{d=1}^N\frac{|b_d|^2}{d^2}\right)^{1/2}
\left(\sum_{d=1}^NN^2\right)^{1/2}.
\]

Using (17) proves (1):

\[
\sum_{j=2}^N|a_j|
\le
\sqrt6\,N^{3/2}\|u\|_2.
\tag{19}
\]

On every shell, (11) lies in `[0,1)`. Hence almost everywhere

\[
|u(x)|
\le
\sum_{j=2}^N|a_j|,
\]

and (2) follows.

There is also a useful source-Gram corollary. Since

\[
\|a\|_2
\le
\|a\|_1
\le
\sqrt6\,N^{3/2}\|u\|_2,
\]

we have

\[
\|u\|_2^2
\ge
\frac1{6N^3}\|a\|_2^2.
\]

Taking the infimum over nonzero coefficient vectors gives (3). This is a direct quantitative finite-independence estimate for the unnormalized canonical generators. It does not contradict the target-selected normalized ill-conditioning in `NB-024`: after individual normalization, that finding only forces a logarithmically growing condition number, while (3) is a polynomial lower bound in the original coordinates.

## 4. Cubic source compression of multiplicative dilation

The normalized integer dilation is

\[
(A_mv)(x)
=
\begin{cases}
\sqrt m\,v(mx),&0<x\le1/m,\\
0,&1/m<x<1.
\end{cases}
\tag{20}
\]

and is an isometry. For `u,v in U_N`,

\[
|\langle u,A_mv\rangle|
\le
\|1_{(0,1/m]}u\|_2\,\|v\|_2.
\tag{21}
\]

By (2),

\[
\begin{aligned}
\|1_{(0,1/m]}u\|_2^2
&\le
\frac1m\|u\|_\infty^2\\
&\le
\frac{6N^3}{m}\|u\|_2^2.
\end{aligned}
\tag{22}
\]

Therefore

\[
|\langle u,A_mv\rangle|
\le
\sqrt{\frac{6N^3}{m}}\,
\|u\|_2\|v\|_2.
\]

Taking the supremum over unit vectors gives (4).

As in `NB-299`, finite-packet Blaschke deflation preserves this compression: multiplication by the finite Blaschke factor is unitary between the first-free quotient section and the canonical source section, and commutes with the Mellin dilation multiplier. Thus the same estimate is valid for the `T_m` entering the exact projected-escape factorization.

## 5. First-free consequence

Retain the exact notation of `NB-299`. Let `E_U` be an isometric synthesis map for the old first-free quotient section and put

\[
X=L_ZE_U,
\qquad
T_m=E_U^*S_mE_U,
\qquad
Q_m=I-T_m^*T_m,
\]

\[
Y_m=D_Z(m)X-XT_m.
\tag{23}
\]

The old sample Gram is

\[
XX^*=K,
\qquad
\|X\|=\sqrt{\|K\|}.
\]

By (5),

\[
\|T_m\|
\le
\varepsilon^{\rm cub}_{m,n},
\tag{24}
\]

while off-critical transport gives

\[
\|D_Z(m)\|=m^{-\delta_Z}.
\tag{25}
\]

Hence

\[
\|Y_m\|
\le
\sqrt{\|K\|}
\bigl(m^{-\delta_Z}+\varepsilon^{\rm cub}_{m,n}\bigr).
\tag{26}
\]

If `epsilon^(cub)_(m,n)<1`, then

\[
Q_m\succeq
\left(1-(\varepsilon^{\rm cub}_{m,n})^2\right)I,
\]

and the exact factorization

\[
\Xi_{m,n,Z}=Y_mQ_m^{-1}Y_m^*
\]

gives (8). Conditions (9) make both terms in the numerator tend to zero while the denominator tends to one, proving (10).

For the target-aware relative gain of `NB-299`, the identical substitution gives

\[
\boxed{
0\le
\frac{\mathcal G_{m,n,Z}(y)}{\mathcal C_U(y)}
\le
\min\left\{
1,
\kappa(K)
\frac{\bigl(m^{-\delta_Z}+\varepsilon^{\rm cub}_{m,n}\bigr)^2}
{1-(\varepsilon^{\rm cub}_{m,n})^2}
\right\}.
}
\tag{27}
\]

Thus the source side is polynomially controlled. A persistent relative target gain in a super-cubic regime can only survive through the separate sample-side quantities, notably moving-packet conditioning or failure of off-critical damping.

## 6. Comparison with the lcm bound

`NB-300` used only the fact that every vector in `U_N` is periodic in reciprocal cells with common period

\[
P_N=\operatorname{lcm}(2,\ldots,N).
\]

That argument treats the section as though an arbitrary `P_N`-periodic cell pattern could occur. The actual Nyman section has only `N-1` coefficient degrees of freedom, and its first `N` shell differences recover those coefficients triangularly. Equation (19) is exactly the missing restriction: a unit vector cannot hide exponentially large amplitude in a remote residue class merely because the common period is exponentially long.

Therefore the source-overlap threshold is not forced to sit near `P_N`. A sufficient moving-cutoff separation scale is already

\[
m\gg N^3.
\tag{28}
\]

The result does not assert that the cubic exponent is sharp. It is the cost of two deliberately robust steps: an `l1` coefficient majorant and Cauchy--Schwarz over all first-shell differences. Better divisor-operator estimates or direct point-evaluation control could lower it. What matters for the current frontier is the qualitative scale change from exponential to polynomial.

The lcm result remains useful as an independent reciprocal-cell interpretation and can have better constants at small `N`; asymptotically, however, (4) is the stronger source-separation theorem.

## 7. Adversarial audit

Several failure modes were checked explicitly.

First, (15) does not import the target. The target-dependent `-mu(j)` term in `NB-020` came from the jump of the residual `e-u`; for a homogeneous section vector the corresponding formula is exactly (15). The constant `A_0` cancels for every `j>1`.

Second, the shell norm estimate uses only the first `N` shells and therefore cannot be circularly using density of the full Nyman span. Dropping all later shells only weakens the lower bound on `||u||`.

Third, the proof is valid for complex coefficient vectors as well as real ones. Möbius inversion is algebraic and every norm estimate uses absolute values.

Fourth, the `L^infinity` estimate is an essential-supremum statement. Harmonic-shell boundaries have measure zero and play no role in (22).

Fifth, small raw pivots or normalized Gram ill-conditioning do not invalidate (3). The estimate concerns the unnormalized finite source Gram and follows from an explicit left inverse supplied by early-shell differences. It gives a polynomial lower bound, not uniform Riesz stability.

Sixth, (10) is normalized by `||K||`. It does not imply `Xi=o(E)` for the unresolved future-tail Gram, and (27) still pays `kappa(K)`. No conclusion about the Nyman distance, RH, or uniform Ford-target occupation follows without additional sample-side information.

Finally, the proof was calibrated directly on the shell identity: for finite random coefficient vectors, the reconstruction

\[
a_j=-\sum_{d\mid j}\mu(j/d)(u_d-u_{d-1})
\]

recovers the original coefficients exactly. This is a finite algebra check, not evidence substituted for the proof.

## 8. Prior-art and novelty boundary

A fresh literature search checked the classical Báez-Duarte arithmetic formulations of the Nyman--Beurling criterion, later generalized coefficient-control formulations, and recent work on Gram decay/compressibility of Beurling--Nyman ladders. Möbius inversion, integer-restricted Nyman spans, coefficient conditions, and dilation/Gram analysis are all standard background; no novelty is claimed for those ingredients.

The search did not surface the specific finite-section estimate (1)--(3), nor its use to replace the lcm-scale source-compression gate in the projected first-free dilation block. The durable claim here is therefore deliberately internal and narrow: combining the exact harmonic-shell triangular system with the `NB-299` projected-escape factorization yields an explicit **cubic** moving-cutoff source no-go. The proof is self-contained from canonical line identities, so no new external source is load-bearing and `SOURCES.md` need not change.

## 9. Consequence for the active frontier

After `NB-300`, a persistent projected-dilation mechanism could still hide anywhere in the vast near/sub-lcm region

\[
m\lesssim\operatorname{lcm}(2,\ldots,n-1).
\]

That is no longer the correct source-side window. `NB-301` compresses it to

\[
\boxed{m\lesssim n^3}
\]

up to constants, unless the moving off-critical packet satisfies `delta_Z log m=O(1)` or target-relative gain is rescued by sample conditioning.

This makes the next discriminating question genuinely smaller: can the cubic exponent be lowered using the divisor structure of point evaluations, and, more importantly, what does the actual Ford coupling force for `delta_Z`, `m`, and `kappa(K)` inside the remaining polynomial window? Further common-period arguments are no longer the relevant bottleneck.