# PC-141 — fixed edge Fourier window classicalizes to Murata × Nicolas

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `CLASSICAL-RH-EQUIVALENCE` + `DECISIVE-BOUNDARY`. PC-138 proved that the canonical cross-shell-only inverse-square Hessian `H_N^times` has the exact universal top eigenpair at every even level, while PC-139 showed that the omitted within-shell defect still has a mesoscopic population of macroscopic modes on primorials. This leaves a natural edge question: does a fixed Fourier window adjacent to the protected alternating top mode retain a new arithmetic matrix structure even though the bulk and first moments classicalize?

It does not. For every fixed finite set of Fourier offsets from the alternating mode, the compressed top-gap operator on primorials becomes asymptotically diagonal. Its `r`th diagonal level is an integer linear ladder `|r| g_x`, and the single scale `g_x` factors **exactly** as Murata's classical prime product times the square of the same primorial totient factor used by Nicolas' RH criterion. All fixed off-diagonal mode mixing tends to zero. Thus a new RH mechanism cannot live in any fixed-width Fourier edge window of this canonical Hessian; surviving edge information must involve a window whose width grows with the level, non-Fourier localization, or cross-level organization.

## 1. Edge-gap operator and exact shell reduction

Let `N` be even and let

\[
L_N-H_N^{\times}=D_N
=\bigoplus_{d\mid N}L_d^{\rm int}
\]

be the exact PC-136 decomposition into within-exact-order-shell inverse-square chord Laplacians. PC-138 gives the protected alternating top mode

\[
q_{N,0}(a)=N^{-1/2}(-1)^a,
\qquad
H_N^{\times}q_{N,0}=\frac{N^2}{8}q_{N,0}.
\]

For a fixed nonzero integer offset `r` with `|r|<N/2`, define the neighboring Fourier mode

\[
q_{N,r}(a)
:=N^{-1/2}
\exp\!\left(\frac{2\pi i}{N}\left(\frac N2-r\right)a\right)
\]

and the positive top-gap operator

\[
K_N:=\frac{N^2}{8}I-H_N^{\times}.
\]

The full polygon part is explicit:

\[
L_Nq_{N,r}
=\left(\frac{N^2}{8}-\frac{r^2}{2}\right)q_{N,r}.
\]

Now restrict `q_{N,r}` to the exact-order shell `d|N`. Writing a shell point as `a=(N/d)u` with `u\in U(d)`, the factor contributed by `N/2` is constant on that shell: it is `1` when `N/d` is even and `-1` when `N/d` is odd (then `d` is even and every `u` is odd). Therefore the within-shell energy depends only on the ordinary primitive-residue Fourier phase

\[
u\mapsto e^{-2\pi i r u/d}.
\]

No additional embedding data from the common refinement survives in a fixed Fourier offset.

## 2. Fejér identity gives the exact diagonal Rayleigh deficit

For `r>=1`, the quadratic energy of the `r`th phase on the primitive shell of order `d` is

\[
E_d(r)
:=\langle f_r,L_d^{\rm int}f_r\rangle,
\qquad
f_r(u)=e^{-2\pi i r u/d}.
\]

Each edge with difference `h=u-v` contributes

\[
\frac{|e^{-2\pi i r u/d}-e^{-2\pi i r v/d}|^2}
{|e^{2\pi i u/d}-e^{2\pi i v/d}|^2}
=
\frac{\sin^2(\pi r h/d)}{\sin^2(\pi h/d)}.
\]

Using the finite Fejér identity

\[
\frac{\sin^2(rx)}{\sin^2x}
=r+2\sum_{j=1}^{r-1}(r-j)\cos(2jx)
\]

and

\[
\sum_{u\in U(d)}e^{2\pi iju/d}=c_d(j),
\]

one obtains exactly

\[
\boxed{
E_d(r)
=\frac12\left[
 r\varphi(d)^2-r^2\varphi(d)
 +2\sum_{j=1}^{r-1}(r-j)c_d(j)^2
\right].
}
\tag{1}
\]

Define the divisor sums

\[
A_N:=\sum_{d\mid N}\varphi(d)^2,
\qquad
B_N(j):=\sum_{d\mid N}c_d(j)^2.
\]

Since `sum_{d|N} phi(d)=N`, combining (1) with the full-polygon gap `r^2/2` gives the exact neighboring-mode Rayleigh deficit

\[
\boxed{
G_N(r)
:=\langle q_{N,r},K_Nq_{N,r}\rangle
=
\frac{rA_N}{2N}
+\frac1N\sum_{j=1}^{r-1}(r-j)B_N(j).
}
\tag{2}
\]

For `r=1` all Ramanujan corrections disappear:

\[
\boxed{
G_N(1)=\frac1{2N}\sum_{d\mid N}\varphi(d)^2.
}
\tag{3}
\]

Equation (3) has an elementary geometric interpretation. On each exact-order shell, the first Fourier phase is the vertex coordinate itself, so the inverse-square chord weight cancels its squared chord increment edge by edge; the shell contributes exactly `binom(phi(d),2)` to `D_N`. Adding the universal full-polygon half-unit top gap gives (3).

## 3. The whole fixed Fourier window asymptotically diagonalizes on primorials

The diagonal identity is only part of the statement. Let

\[
P_r(z):=\frac{z^r-1}{z-1}
=\sum_a\epsilon_r(a)z^a
\]

for any nonzero integer `r`, interpreted as a finite Laurent polynomial. Thus `epsilon_r(a)=1` for `0<=a<r` when `r>0`, while `epsilon_r(a)=-1` for `r<=a<0` when `r<0`.

For two offsets `r,s`, direct expansion of the polarized edge energy gives the exact shell matrix element

\[
\boxed{
E_d(r,s)
=\frac12\left[
\sum_{a,b}\epsilon_r(a)\epsilon_s(b)
 c_d(a-b)c_d(r-s-a+b)
-rs\,c_d(r-s)
\right].
}
\tag{4}
\]

Hence

\[
\boxed{
\langle q_{N,r},K_Nq_{N,s}\rangle
=\frac{r^2}{2}\,\mathbf 1_{r=s}
+\frac1N\sum_{d\mid N}E_d(r,s).
}
\tag{5}
\]

Now take the primorial common refinement

\[
N_x:=\prod_{p\le x}p.
\]

For fixed integers `a,b`, multiplicativity of Ramanujan sums gives

\[
\sum_{d\mid N_x}c_d(a)c_d(b)
=\prod_{p\le x}\left(1+c_p(a)c_p(b)\right).
\tag{6}
\]

If `a,b` are both nonzero, all sufficiently large local factors are `2`, so (6) is `O_{a,b}(2^{\pi(x)})=N_x^{o(1)}`. If exactly one of `a,b` is zero, all sufficiently large local factors are `2-p`, so after division by `N_x` the product is `O_{a,b}((\log x)^{-2})` by the same Mertens/two-point local-product estimate already encountered in PC-139. Finally,

\[
\sum_{d\mid N_x}c_d(t)=0
\]

for each fixed nonzero `t` once `N_x>|t|`.

When `r\ne s`, the two Ramanujan arguments in every term of (4) cannot both vanish, because their sum is `r-s`. Therefore every fixed off-diagonal entry of (5) tends to zero **absolutely**. On the diagonal, (2) and

\[
B_{N_x}(j)
=\prod_{p\le x}\left(1+c_p(j)^2\right)
=O_j(2^{\pi(x)})
\]

give a vanishing absolute correction after division by `N_x`.

Consequently, if

\[
g_x:=\frac{A_{N_x}}{2N_x},
\]

then for every fixed `R`, in the signed Fourier window

\[
V_{x,R}
:=\operatorname{span}\{q_{N_x,r}:0<|r|\le R\},
\]

one has the finite-dimensional operator limit

\[
\boxed{
K_N\big|_{V_{x,R}}
-
g_x\,\operatorname{diag}(|r|)_{0<|r|\le R}
\longrightarrow0
}
\tag{7}
\]

in operator norm as `x->infinity`. Since `g_x->infinity`, equivalently

\[
\boxed{
\frac1{g_x}K_N\big|_{V_{x,R}}
\longrightarrow
\operatorname{diag}(|r|)_{0<|r|\le R}.
}
\tag{8}
\]

Thus every fixed edge window has a universal **linear ladder** and loses its mode mixing. This is a genuinely matrix-level collapse, not merely another trace identity.

## 4. The sole edge scale is Murata × the Nicolas totient factor

For a primorial, multiplicativity gives

\[
A_{N_x}
=\prod_{p\le x}\left(1+(p-1)^2\right)
=\prod_{p\le x}(p^2-2p+2).
\tag{9}
\]

Factor each local term as

\[
1-\frac2p+\frac2{p^2}
=
\left(1-\frac1p\right)^2
\left(1+\frac1{(p-1)^2}\right).
\]

With

\[
M_x:=\prod_{p\le x}\left(1+\frac1{(p-1)^2}\right),
\]

(3) becomes the exact identity

\[
\boxed{
\frac{2g_x}{N_x}
=M_x\left(\frac{\varphi(N_x)}{N_x}\right)^2.
}
\tag{10}
\]

The absolutely convergent product

\[
M:=\prod_p\left(1+\frac1{(p-1)^2}\right)
=2.82641999\ldots
\]

is the classical **Murata constant**, associated with Leo Murata's work on least prime primitive roots. Hence Mertens gives

\[
\boxed{
g_x\sim
\frac{M e^{-2\gamma}}{2}
\frac{N_x}{(\log x)^2}.}
\tag{11}
\]

More importantly, the apparent RH-sensitive normalization is exactly the one already classicalized in PC-137 and PC-140:

\[
\boxed{
\frac{2e^{2\gamma}(\log\log N_x)^2}{N_xM_x}\,g_x
=
\left[
e^\gamma\log\log N_x
\frac{\varphi(N_x)}{N_x}
\right]^2.
}
\tag{12}
\]

At prime endpoints `x=p_k`, Nicolas' theorem therefore says that the inequality making the left side of (12) less than `1` for every `p_k>2` is **exactly equivalent to RH**. The Fourier-edge realization does not supply an independent criterion: after removing the finite Murata factor, it is literally the square of Nicolas' classical primorial totient function.

## 5. Finite exact controls

The formulas are directly checkable without floating-point trigonometry. For the first neighboring mode,

\[
G_{30}(1)=\frac{17}{6},
\qquad
G_{210}(1)=\frac{629}{42},
\qquad
G_{2310}(1)=\frac{63529}{462}.
\]

The signed `r=\pm1` compressed blocks are respectively

\[
\begin{pmatrix}17/6&-2/15\\-2/15&17/6\end{pmatrix},
\qquad
\begin{pmatrix}629/42&-4/105\\-4/105&629/42\end{pmatrix},
\qquad
\begin{pmatrix}63529/462&-8/1155\\-8/1155&63529/462\end{pmatrix}.
\]

The diagonal scale grows like `N_x/(log x)^2` while the fixed conjugate-mode coupling already decreases to zero, illustrating the two parts of (7) simultaneously. Equation (2) supplies independent higher-offset controls; for example

\[
G_{30}(2)=\frac{89}{15},
\qquad
G_{210}(2)=\frac{1051}{35},
\qquad
G_{2310}(2)=\frac{105887}{385},
\]

and these approach twice the corresponding `G_N(1)` scale.

## 6. Prior art, novelty audit, and RH boundary

No theorem-level historical novelty is claimed for the ingredients. The Fejér-kernel identity is classical harmonic analysis; primitive-residue Fourier sums are Ramanujan sums, already anchored in `SOURCES.md` via Ramanujan and Tóth; multiplicativity and divisor products of Ramanujan sums are standard. The constant in (10) is not new: Leo Murata, **On the magnitude of the least prime primitive root**, *Journal of Number Theory* 37:1 (1991), 47–66, DOI `10.1016/S0022-314X(05)80024-1`, is the primary bibliographic anchor associated with the product now called Murata's constant. PC-137 and PC-140 already establish that the bracket in (12) is exactly Nicolas' classical RH criterion.

Directed searches across Fejér kernels on reduced-residue systems, Ramanujan-sum Fourier energies, inverse-square roots-of-unity Laplacians, and fixed edge compressions did not expose this exact Prime-Circle matrix statement. That absence is not evidence of priority. The durable contribution is the boundary classification: **even after retaining a genuinely matrix-valued fixed Fourier neighborhood of the protected spectral edge, the canonical cross-shell Hessian asymptotically diagonalizes to a universal integer ladder whose only growing arithmetic scale is Murata × Nicolas.**

This does **not** determine the actual second eigenvalue or the complete edge spectrum. The Fourier modes are Ritz probes, not exact eigenvectors once the within-shell defect breaks circulant symmetry. Accordingly, (7) does not imply that the true ordered edge gaps equal `g_x,2g_x,...`. It does rule out extracting new RH content from any fixed-dimensional Fourier compression, its determinant, its fixed collection of Ritz values, or its limiting normalized matrix: those objects contain only the universal ladder plus the classical scalar scale (10).

The surviving spectral frontier is therefore narrower and genuinely non-scalar. A new mechanism would have to use Fourier offsets `|r|` growing with `N_x`, localized/non-Fourier organization of the PC-139 mesoscopic modes, nonlinear interactions among such modes, or cross-level transport. Fixed-width edge Fourier structure is now classicalized.