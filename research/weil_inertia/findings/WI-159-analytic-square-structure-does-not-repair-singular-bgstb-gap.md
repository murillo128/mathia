# WI-159 — analytic nonnegative square structure does not repair the singular BGSTB uniformity gap

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + DECISIVE-NEGATIVE + STRUCTURAL-RIGIDITY + PRIOR-ART-REDIRECT`.

WI-157 shows that every support-one scalar Lamzouri family whose deweighted profile stays inside the natural BGSTB dual-norm gate has asymptotic ceiling equal to the Montgomery--Taylor/CCLM constant. WI-158 then proves that the published pointwise BGSTB error is genuinely insufficient at the boundary: there are smooth near-extremizing Lamzouri kernels with

\[
\|r_L\|_1=\Theta(\sqrt L),\qquad L=\log T,
\]

for which a uniformly `O(L^{-1/2})` adversarial error shifts the integrated scalar cost by an arbitrary fixed negative amount while preserving pointwise nonnegativity of the model form factor.

A natural objection is that the actual BGSTB form factor has more exact structure than the model used in WI-158. From its finite zero-pair definition it is an even entire exponential polynomial in the real parameter `alpha`, and BGSTB Lemma 3 gives a squared-`L^2` representation proving nonnegativity for every real `alpha`. The WI-158 model was only imposed on `[0,1]` and did not encode analyticity at the origin; its even extension through the standard main term has a cusp.

The present finding closes that shortcut. The WI-158 adversarial shift can be embedded in a **real-even nonnegative trigonometric polynomial**, of polynomial bandwidth in `log T`, which therefore extends to an entire function and, by the Fejer--Riesz theorem, is itself exactly one Hermitian square on the real axis. It still satisfies the full published BGSTB pointwise asymptotic on `[0,1]` and produces the same arbitrary order-one integrated shift against the singular near-extremizer. Thus evenness, real analyticity/entireness, finite exponential type, global real-axis nonnegativity, and generic square-factorization structure do not supply the missing uniformity. A surviving scalar escape must use **zeta-specific arithmetic information about the coefficients/error**, not merely these generic functional properties of the form factor.

This is a logical insufficiency theorem. The constructed trigonometric polynomial is not asserted to be an actual zeta form factor and does not reproduce the source-specific zero-pair coefficients in BGSTB Lemma 3.

## 1. Exact structure available from the BGSTB definition

BGSTB define, for `x>0`,

\[
F(x,T)=\sum_{0<\gamma,\gamma'\le T}
 x^{\rho-\rho'}w(\rho-\rho'),
\qquad
F_T(\alpha)=\left(\frac{T}{2\pi}\log T\right)^{-1}F(T^\alpha,T).
\]

After using the functional-equation symmetry they prove that `F_T(alpha)` is real, even and nonnegative. Their Lemma 3 gives the exact identity

\[
F(x,T)=\frac2\pi\int_{\mathbb R}
\left|
\sum_{0<\gamma\le T}
\frac{x^{\rho-1/2}}
{1-(\rho-(1/2+it))^2}
\right|^2dt.
\tag{1}
\]

For fixed `T` the zero sum is finite, so the defining pair sum is an entire exponential polynomial in `alpha`. Since `|\gamma-\gamma'|\le T` and `|\beta-\beta'|<1`, its exponential type is `O(TL)` with `L=log T`.

Their Theorem 1 proves, uniformly for `0<=alpha<=1`,

\[
F_T(\alpha)
=L e^{-2L\alpha}+\alpha+O(L^{-1/2}),
\tag{2}
\]

where writing the first coefficient as `L` simply chooses the allowed `O(1)` in the published `e^{-2L alpha}(L+O(1))` term to be zero. The question here is whether the exact structural facts preceding (2) can force the `O(L^{-1/2})` remainder to pair harmlessly with the singular `r_L` of WI-158.

## 2. Approximate the cusp main term by an entire even trigonometric polynomial far inside the zeta type budget

On `[-1,1]` define

\[
M_L(\alpha):=L e^{-2L|\alpha|}+|\alpha|
\tag{3}
\]

and extend it with period `2`. This is a continuous even periodic function. Its Lipschitz constant is at most

\[
K_L\le 2L^2+1.
\tag{4}
\]

The classical Jackson theorem for uniform trigonometric approximation gives an absolute constant `C` such that, for every degree `N`, there is a real trigonometric polynomial `P_{L,N}` of degree at most `N` with

\[
\|P_{L,N}-M_L\|_\infty\le C\frac{K_L}{N}.
\tag{5}
\]

Symmetrizing does not increase the error, so `P_{L,N}` may be taken even. Choose `N_L=ceil(L^14)`. Then for all sufficiently large `L` there is an even real trigonometric polynomial `P_L` with

\[
\eta_L:=\|P_L-M_L\|_\infty=O(L^{-12}).
\tag{6}
\]

Put

\[
B_L(\alpha):=P_L(\alpha)+\eta_L.
\tag{7}
\]

Then on the whole real line, by periodicity,

\[
\boxed{B_L\ge M_L},
\qquad
0\le B_L-M_L\le2\eta_L.
\tag{8}
\]

The degree `O(L^14)` is negligible compared with the exact zeta form factor's available type `O(TL)=O(e^L L)`. Thus imposing finite exponential type at the natural source scale does not obstruct this analytic smoothing of the cusp.

The use of Jackson approximation is not essential to the qualitative conclusion; it provides a quantitative polynomial-bandwidth realization so that the model is much more restrictive than an arbitrary entire approximation.

## 3. Insert the WI-158 oscillatory remainder without losing global positivity

Retain the WI-158 near-extremizing Lamzouri family and write

\[
r_L(\alpha)=\phi_L(\alpha)-\frac{\phi_L''(\alpha)}{4L^2},
\qquad
\|r_L\|_1=\Theta(\sqrt L).
\tag{9}
\]

For fixed `a,c>0`, WI-158 chooses

\[
n_L\sim cL^{3/2},
\qquad
E_L(\alpha)
=-aL^{-1/2}
(1-\cos 2\pi\alpha)\cos(2\pi n_L\alpha).
\tag{10}
\]

This is itself a real-even trigonometric polynomial. For `0<=alpha<=1`,

\[
0\le1-\cos(2\pi\alpha)\le2\pi\alpha,
\tag{11}
\]

because `x-(1-cos x)` is increasing for `x>=0`. Hence, once `sqrt L>=2\pi a`,

\[
|E_L(\alpha)|\le\alpha\le M_L(\alpha).
\tag{12}
\]

Define

\[
\boxed{\widetilde F_L:=B_L+E_L.}
\tag{13}
\]

Equations (8) and (12) give

\[
\widetilde F_L(\alpha)\ge M_L(\alpha)-|E_L(\alpha)|\ge0
\quad(0\le\alpha\le1).
\tag{14}
\]

By evenness and period `2`, this proves

\[
\boxed{\widetilde F_L(\alpha)\ge0\quad\text{for every real }\alpha.}
\tag{15}
\]

Moreover `widetilde F_L` is a real-even trigonometric polynomial of degree `O(L^14)`, hence extends to an entire function of exponential type `O(L^14)`. On `[0,1]`, (6), (10) and (13) give exactly the published BGSTB shape

\[
\boxed{
\widetilde F_L(\alpha)
=L e^{-2L\alpha}+\alpha+O(L^{-1/2})
}
\tag{16}
\]

uniformly in `alpha`. It also has the correct coarse origin size `widetilde F_L(0)=L+o(1)` and, unlike the cusp model, satisfies `widetilde F_L'(0)=0` automatically.

Thus the elementary exact objections `even`, `analytic at zero`, `entire`, `finite type`, and `nonnegative on the full real axis` can all be imposed simultaneously without changing the dangerous `O(L^{-1/2})` oscillation.

## 4. Fejer--Riesz upgrades the model to an exact scalar Gram square

Set `theta=pi alpha`. Since `widetilde F_L(theta/pi)` is a nonnegative trigonometric polynomial on the unit circle, the classical Fejer--Riesz theorem gives an analytic polynomial `Q_L` such that

\[
\boxed{
\widetilde F_L(\alpha)
=|Q_L(e^{i\pi\alpha})|^2
\quad(\alpha\in\mathbb R).
}
\tag{17}
\]

Hence the countermodel is not merely pointwise nonnegative. It is already a single exact Hermitian square, a stronger generic positivity structure than the integral of squares used in BGSTB Lemma 3.

This does **not** identify `Q_L` with the zeta-zero sum in (1). The coefficients and frequencies in (1) satisfy highly specific arithmetic and zero-source relations. Equation (17) only proves that abstract square/Gram structure, without those source restrictions, cannot be the missing theorem.

## 5. The analytic smoothing costs `o(1)` against the singular test, so the WI-158 shift survives unchanged

The only new term in the pairing relative to WI-158 is `B_L-M_L`. By (6), (8), and (9),

\[
\left|
2\int_0^1(B_L-M_L)r_L\,d\alpha
\right|
\le
2\|B_L-M_L\|_\infty\int_0^1|r_L(\alpha)|\,d\alpha
=O(L^{-23/2})=o(1).
\tag{18}
\]

WI-158 proves, with the same `r_L`, `E_L`, and its fixed positive constant `d_psi`,

\[
2\int_0^1E_L(\alpha)r_L(\alpha)\,d\alpha
\longrightarrow
-\frac{a\pi^2c^2d_\psi}{4}.
\tag{19}
\]

Combining (18)--(19),

\[
\boxed{
2\int_0^1(\widetilde F_L-M_L)r_L\,d\alpha
\longrightarrow
-\frac{a\pi^2c^2d_\psi}{4}.
}
\tag{20}
\]

As in WI-158, the magnitude can be made arbitrarily large by increasing the fixed constant `c`, while the pointwise bulk remainder in (16) stays `O(L^{-1/2})` with constant depending only on `a`, not on `c`. The singular Lamzouri cost still converges to the exact CCLM/Montgomery--Taylor optimum.

Therefore all the generic analytic/square constraints added here leave the order-one arithmetic susceptibility intact.

## 6. Consequence for the support-one scalar frontier

The surviving loophole after WI-157--WI-158 cannot be closed by arguing only that the actual form factor is smoother, entire, globally nonnegative, finite-bandwidth at fixed height, or obtained from a squared norm. There are countermodels satisfying all of those properties, with bandwidth polynomial in `log T` and hence enormously below the source's trivial `O(T log T)` type budget, which still realize the dangerous pairing.

A successful repair must use a **source-specific restriction** absent from the countermodel. Examples include a frequency-sensitive estimate for the actual BGSTB/Goldston--Montgomery remainder, an averaged error theorem in a norm dual to the singular family, a direct unweighted pair-sum estimate for changing tests, or a coefficient/zero-source identity that quantitatively forbids the adverse spectral mode. Merely invoking generic analyticity or positivity of Lemma 3 does not qualify.

This also supplies a falsification target for future scalar proposals: if a proposed theorem claims that exact form-factor regularity controls a changing test, it must identify the zeta-specific quantitative property that excludes the nonnegative Fejer--Riesz countermodels (13)--(20).

## 7. Prior-art and novelty audit

The arithmetic input is established prior art: Baluyot, Goldston, Suriajaya and Turnage-Butterbaugh, *An unconditional Montgomery theorem for pair correlation of zeros of the Riemann zeta-function*, Acta Arith. 214 (2024), 357--376, arXiv:2306.04799. Theorem 1 gives (2); Lemma 3 gives the exact squared-`L^2` representation and real-axis nonnegativity. Their proof traces the `O(L^{-1/2})` bulk term to the Goldston--Montgomery prime-side mean-square estimate rather than to a regularity theorem for the error as a function of `alpha`.

The approximation step is classical Jackson theory; see D. Jackson, *On approximation by trigonometric sums and polynomials*, Trans. Amer. Math. Soc. 13 (1912), 491--515, DOI `10.1090/S0002-9947-1912-1500930-2`. The square factorization is the classical one-variable Fejer--Riesz theorem: every nonnegative scalar trigonometric polynomial is a Hermitian square on the unit circle. A modern statement appears, for example, in the introduction of Georgiou--Lindquist, *On a Fejer--Riesz factorization of generalized trigonometric polynomials*, arXiv:2005.11920.

A targeted search around Montgomery form-factor regularity, uniform changing test functions, analytic/positive form-factor constraints, and Fejer--Riesz factorization did not locate a theorem converting these generic functional properties into the frequency-sensitive `o(1)` error needed here. This absence is not used as a priority claim. The new content recorded by Mathia is the exact countermodel bridge from WI-158 to an entire globally nonnegative finite-type Hermitian square and the resulting closure of the generic-analyticity shortcut.

## Evidence boundary

Equations (3)--(20) are exact deterministic deductions from WI-158 plus classical Jackson and Fejer--Riesz theorems. No new zeta-zero percentage follows. The construction does not claim that the actual zeta form-factor error realizes the adversarial mode, and it does not preserve the detailed zero-pair coefficient structure of BGSTB equation (1.2)/(Lemma 3). Precisely that source-specific structure is now the remaining arithmetic target for a singular support-one scalar escape.