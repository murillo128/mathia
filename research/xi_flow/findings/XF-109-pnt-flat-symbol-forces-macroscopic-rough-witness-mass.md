# XF-109 — PNT-flat source symbol forces macroscopic rough witness mass

**Status:** `EXACT-DERIVED` + `TOEPLITZ-SYMBOL-FLATNESS` + `FIXED-SPECTRAL-MASS-GATE` + `ARITHMETIC-ROUGHNESS`. XF-108 showed that a nonpositive q-scale source-Toeplitz witness must have a very large *maximum* physical lag derivative. That condition by itself still allows the roughness to be carried by an arbitrarily small high-frequency contamination of an otherwise smooth witness. The mass-preserving source interface is more rigid: a nonpositive witness must place a fixed positive fraction of its coefficient-Fourier `L^2` mass outside a PNT-flat central arc. Thus the surviving obstruction is not merely pointwise rough; it is macroscopically rough.

Keep the XF-108 source scales

\[
N=2q^2,\qquad
\Delta^2\asymp q^{-3},\qquad
a:=N\Delta\asymp q^{1/2},
\qquad
\Delta\asymp a^{-3},
\tag{1}
\]

and fix

\[
L=\log a+c,\qquad
K=\left\lfloor\frac{L}{\Delta}\right\rfloor,
\qquad c\in\mathbf R
\tag{2}
\]

with `c` independent of `a`. Let `\widehat\mu_m` be the mass-preserving source moments of XF-108 and

\[
\widehat T_K=(\widehat\mu_{i-j})_{0\le i,j\le K},
\qquad
\widehat\mu_0=1,
\qquad
\widehat\mu_{-m}=\widehat\mu_m.
\tag{3}
\]

There are constants `c_2>0`, `M<\infty`, and `\delta_0>0`, depending only on the fixed deposition bump and on `c`, such that for all sufficiently large `a`, every real unit vector `v` satisfying

\[
v^\top\widehat T_Kv\le0
\tag{4}
\]

obeys

\[
\boxed{
\frac1{2\pi}
\int_{|\theta|>\theta_a}
\left|\sum_{j=0}^K v_j e^{ij\theta}\right|^2d\theta
\ge\delta_0,
}
\tag{5}
\]

where

\[
\boxed{
\theta_a
=
\Delta\exp\!\bigl(c_2\sqrt{\log a}\bigr).
}
\tag{6}
\]

Equivalently, in the physical lag coordinate `x=m\Delta`, a fixed fraction of every nonpositive witness must live at Fourier wave number

\[
\boxed{
|y|=|\theta|/\Delta
\ge
\exp\!\bigl(c_2\sqrt{\log a}\bigr)
=
\exp\!\bigl(c_3\sqrt{\log q}\bigr)
}
\tag{7}
\]

for some `c_3>0`. This is strictly stronger than XF-108's lower bound on one maximum discrete derivative: a vanishing amount of arbitrarily oscillatory contamination cannot satisfy `(5)`.

## 1. The source Toeplitz symbol is PNT-flat on a growing physical-frequency window

Define the real trigonometric symbol

\[
F_a(\theta)
=
1+2\sum_{m=1}^K\widehat\mu_m\cos(m\theta),
\qquad -\pi\le\theta\le\pi.
\tag{8}
\]

The PNT argument of XF-108 can be applied directly to the deterministic lag profile

\[
r_m(\theta)=\cos(m\theta).
\tag{9}
\]

The only properties of the lag profile used in the Stieltjes-summation cancellation are boundedness and physical Lipschitz control after mass-preserving interpolation. Here

\[
|r_m(\theta)|\le1
\tag{10}
\]

and

\[
\frac{|r_{m+1}(\theta)-r_m(\theta)|}{\Delta}
\le
\frac{|\theta|}{\Delta}.
\tag{11}
\]

Repeating the XF-108 background Riemann-sum estimate and the PNT comparison with the logarithmic von-Mangoldt measure therefore gives, uniformly for `|\theta|\le\pi`,

\[
\begin{aligned}
|F_a(\theta)-1|
\ll_{\psi,c}
&\left(1+\frac{|\theta|}{\Delta}\right)
 e^{-c_1\sqrt{\log a}}
+
\left(1+\frac{|\theta|}{\Delta}\right)\Delta\\
&+
\frac{\log(1/\Delta)}a
+
\Delta\log a,
\end{aligned}
\tag{12}
\]

for some `c_1>0`. No Toeplitz eigenvector structure is used in `(12)`; this is a statement about the source symbol itself.

Choose any fixed

\[
0<c_2<c_1
\tag{13}
\]

and put

\[
Y_a=e^{c_2\sqrt{\log a}},
\qquad
\theta_a=\Delta Y_a.
\tag{14}
\]

Then `Y_a e^{-c_1\sqrt{\log a}}\to0`, while `Y_a\Delta\to0` because `\Delta\asymp a^{-3}`. The remaining terms in `(12)` also vanish. Hence

\[
\boxed{
\sup_{|\theta|\le\theta_a}|F_a(\theta)-1|=o(1).
}
\tag{15}
\]

In particular, for all sufficiently large scales,

\[
\boxed{
F_a(\theta)\ge\frac12
\qquad (|\theta|\le\theta_a).
}
\tag{16}
\]

The PNT cancellation of XF-108 is therefore not only a test-by-test smoothness statement. It creates an actual positive spectral window in the Toeplitz symbol whose width, measured in physical wave number `y=\theta/\Delta`, grows like `e^{c_2\sqrt{\log a}}`.

## 2. The full q-scale symbol has a fixed global lower bound

To turn `(16)` into a mass statement, one needs a lower bound outside the central arc that does not deteriorate with `a`. The fixed-q-scale cutoff `(2)` supplies exactly that through a raw `\ell^1` estimate.

XF-108 uses the mass-preserving deposition

\[
\widehat Q_m^\psi
=
B(m\Delta)
-
\frac1{2\Delta}
\sum_{n\ge2}
\frac{\Lambda(n)}{\sqrt n}\,
\omega_\psi\!\left(m,\frac{\lambda_n}{\Delta}\right),
\qquad
\widehat\mu_m=\frac{\widehat Q_m^\psi}{N},
\tag{17}
\]

with `\lambda_n=(\log n)/2`, nonnegative normalized weights `\omega_\psi`, and

\[
\sum_m\omega_\psi(m,u)=1.
\tag{18}
\]

For the archimedean background, the estimates already used in XF-104--XF-108 give

\[
\sum_{m=1}^K |B(m\Delta)|
\ll
\Delta^{-1}
\bigl(e^L+L+\log(K+1)+1\bigr).
\tag{19}
\]

Since `N=a/\Delta`, normalization yields

\[
\frac1N\sum_{m=1}^K |B(m\Delta)|
\ll_c 1.
\tag{20}
\]

For the prime-power term, nonnegativity and `(18)` allow the absolute values to be summed before the atoms are deposited:

\[
\begin{aligned}
&\sum_{m=1}^K
\frac1{2N\Delta}
\sum_{n\ge2}
\frac{\Lambda(n)}{\sqrt n}
\omega_\psi\!\left(m,\frac{\lambda_n}{\Delta}\right)\\
&\qquad\le
\frac1{2a}
\sum_{\lambda_n\le L+O(\Delta)}
\frac{\Lambda(n)}{\sqrt n}.
\end{aligned}
\tag{21}
\]

The Chebyshev-level weighted estimate already derived in XF-104 is

\[
\sum_{n\le X}\frac{\Lambda(n)}{\sqrt n}\ll\sqrt X.
\tag{22}
\]

With `X=e^{2L+O(\Delta)}` and `e^L=a e^c`, equations `(21)`--`(22)` are `O_c(1)`. Thus there is a fixed constant `C_0=C_0(\psi,c)` such that

\[
\boxed{
\sum_{m=1}^K|\widehat\mu_m|\le C_0
}
\tag{23}
\]

for all sufficiently large `a`. Consequently

\[
|F_a(\theta)|
\le
1+2C_0=:M
\tag{24}
\]

uniformly on the whole circle. In particular

\[
F_a(\theta)\ge-M.
\tag{25}
\]

This is where keeping `c` fixed in `(2)` matters. If the physical cutoff is moved to `L=\log a+c(a)` with `c(a)\to+\infty`, the raw mass budget can grow like `e^{c(a)}` and the fixed lower bound `(25)` need not survive.

## 3. A nonpositive Rayleigh quotient forces fixed mass outside the flat arc

For a real unit vector

\[
v=(v_0,\ldots,v_K),
\qquad
\sum_{j=0}^K v_j^2=1,
\tag{26}
\]

write

\[
P_v(e^{i\theta})
=
\sum_{j=0}^K v_j e^{ij\theta}.
\tag{27}
\]

Parseval gives

\[
\frac1{2\pi}
\int_{-\pi}^{\pi}|P_v(e^{i\theta})|^2d\theta=1,
\tag{28}
\]

and the exact Toeplitz-symbol identity is

\[
\boxed{
v^\top\widehat T_Kv
=
\frac1{2\pi}
\int_{-\pi}^{\pi}
F_a(\theta)|P_v(e^{i\theta})|^2d\theta.
}
\tag{29}
\]

Let

\[
A_a=\{\theta:|\theta|\le\theta_a\}
\tag{30}
\]

and define the spectral mass outside the PNT-flat arc by

\[
\rho_a(v)
=
\frac1{2\pi}
\int_{A_a^c}|P_v(e^{i\theta})|^2d\theta.
\tag{31}
\]

Using `(16)`, `(25)`, and `(28)` in `(29)` gives

\[
v^\top\widehat T_Kv
\ge
\frac12(1-\rho_a(v))-M\rho_a(v).
\tag{32}
\]

Therefore `(4)` implies

\[
\boxed{
\rho_a(v)
\ge
\frac1{2M+1}
=: \delta_0>0.
}
\tag{33}
\]

This proves `(5)`--`(7)`. The important point is the quantifier: `\delta_0` is fixed as `a\to\infty`. A negative Toeplitz direction cannot consist of a PNT-smooth bulk plus a vanishing high-frequency defect whose only role is to make one discrete derivative large.

## 4. Stress tests and exact boundary of the claim

The mass-preserving deposition of XF-108 is load-bearing. Without exact reproduction of constant lag profiles, the mesh-phase factor `p_\psi(\lambda_n/\Delta)` can introduce microscopic oscillation into the prime test itself. Then `(12)` is not a consequence of classical PNT, and a small-angle symbol feature could be an extractor artifact rather than source arithmetic.

The theorem does **not** prove that `\widehat T_K` is positive semidefinite. The complement of `A_a` remains enormous. Equation `(33)` only says that any failure must occupy it with nonvanishing `L^2` mass. A witness built from genuinely rough correlations in the discrepancy `d\Psi-dx` is still allowed.

The fixed offset `c` in `L=\log a+c` is also load-bearing for the fixed constant `\delta_0`. The central-arc flatness survives somewhat more general cutoffs as long as the XF-108 PNT error stays controlled, but if the total normalized source mass is allowed to diverge then `(32)` only gives a deteriorating lower bound on `\rho_a(v)`. No claim is made here in that regime.

No RH input enters. The arithmetic ingredients are the same unconditional PNT error used in XF-108 and the Chebyshev weighted mass bound already used in XF-104. The passage from Toeplitz coefficients to `(29)` is the standard Fourier representation of a finite Hermitian Toeplitz quadratic form.

## 5. Prior-art audit and consequence for the live frontier

A targeted search again found two nearby modern Toeplitz/RH directions. Alain Connes and Walter D. van Suijlekom, *Quadratic Forms, Real Zeros and Echoes of the Spectral Action* (Communications in Mathematical Physics 406 (2025), article 312, DOI `10.1007/s00220-025-05493-1`) develops Caratheodory--Fejer-type zero localization from positive Toeplitz/convolution quadratic forms. Wojciech Michalowski, *An explicit uniform cubic wedge for consecutive Toeplitz minors of the Riemann xi coefficients* (arXiv:2607.16795, 2026), studies Toeplitz minors of the positive coefficient sequence of normalized xi and a Polya-frequency criterion. Neither is the Guinand--Weil/Vieta source moment matrix `(3)`, and neither supplies the PNT-flat-symbol estimate `(15)` or the fixed rough-sector mass consequence `(33)`. No novelty is claimed for the generic Toeplitz Fourier identity, Parseval, PNT, or Chebyshev estimates separately.

The new line-specific restriction is complementary to XF-106--XF-108. At the natural q arithmetic scale, any nonpositive source-Toeplitz witness must now satisfy all of the following simultaneously:

\[
|\operatorname{supp}v|=\Omega(a)=\Omega(q^{1/2})
\tag{34}
\]

from XF-106, physical lag span

\[
\Delta\,\operatorname{diam}(\operatorname{supp}v)
\ge\log a-O(1)
\tag{35}
\]

from XF-107, and the fixed high-frequency mass condition `(5)`--`(7)`. XF-108's maximum-roughness condition is therefore upgraded to an `L^2` statement: **a genuine source realizability obstruction must be collective, q-scale in lag span, and macroscopically supported in an arithmetically rough spectral sector.**

This narrows the next source-side question sharply. A useful positivity theorem no longer needs to control every possible rough derivative spike. It must control the fixed-mass high-frequency sector of the discrepancy-weighted Toeplitz form. Conversely, an explicit negative witness must produce nonvanishing spectral mass there; merely constructing one highly oscillatory tail on an otherwise continuum-smooth vector cannot defeat source realizability.

No new external theorem is load-bearing beyond the PNT anchor already recorded for XF-108, so `SOURCES.md` requires no change.