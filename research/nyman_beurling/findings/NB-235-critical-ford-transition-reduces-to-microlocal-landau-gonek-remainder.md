# NB-235 — Critical Ford transition reduces to a microlocal Landau–Gonek remainder

**Date:** 2026-09-20  
**Status:** `EXACT-DERIVED + ZETA-SPECTRAL-REDUCTION + NEGATIVE/METHOD-BOUNDARY + LANDAU-GONEK-AUDITED + EXACT-FORD-TRANSITION + NB-234-REFINEMENT + SOURCE-ONLY + PRIOR-ART-AUDITED`.

`NB-234` reduces the unresolved Ford transition to a local marked zero coefficient in the layer

\[
d_\rho:=YD_\rho-\log J=O(1),
\qquad
D_\rho=R(1-\beta_\rho),
\]

and shows that finitely many depth moments cannot reconstruct its exponential mark uniformly. This finding changes representation once more, but now into a classical zeta object rather than another abstract moment model. On the same critical layer, the exact carrier factor is

\[
e^{iXv_\rho}=x^{\rho-s_X},
\qquad
x=e^X,
\qquad
s_X=\sigma_X+it,
\]

so the residue is a horizontally truncated, smoothly localized Landau-type zero sum. Moreover, because the logarithmic shell profile is supported away from the origin, the corresponding ordinate weight has zero total integral. The ordinary Landau–Gonek prime-power main term is therefore annihilated by the shell localization; what remains is a genuinely microlocal remainder problem.

The useful negative result is quantitative. Feeding the classical *global cumulative* Landau–Gonek formula into this microscopic weight by Stieltjes summation does not gain a factor from the window width: the total variation of `F(H(·-t))` is independent of `H`. At the Ford scale, Gonek's uniform cumulative error gives only a normalized `O(Q)` bound even before the prime-power proximity terms are used, not `o(1)`. Thus the global formula, used as a black box, cannot settle the critical coefficient even after its arithmetic diagonal has disappeared. The missing input is a local/horizontally sensitive Landau–Gonek remainder estimate, not another population-only zero-density bound.

## 1. Exact critical-layer reduction to a Landau zero sum

Use the notation of `NB-228`--`NB-234`:

\[
Q=\log(10+|t|),
\qquad
L=\log Q,
\qquad
R=Q^{2/3}L^{1/3},
\]

\[
Y=\frac XR\to Y_*\in(0,\infty),
\qquad
J=\frac RH\to\infty,
\qquad
J\le L,
\]

and fix `r>0`. For a nonzero real `phi in C_c^infty((0,1))`, put

\[
\sigma_X=1+\frac rX,
\qquad
s_X=\sigma_X+it,
\qquad
F(z)=\int_0^1\phi(y)e^{izy}\,dy.
\tag{1}
\]

For a zero `rho=beta+i gamma`, `NB-228` uses

\[
v_\rho=(\gamma-t)+i(\sigma_X-\beta)
\]

and the exact profile

\[
L_{X,H}(v_\rho)
=e^{iXv_\rho}F(Hv_\rho).
\tag{2}
\]

Now set `x=e^X`. Since

\[
x^{\rho-s_X}
=e^{X(\beta-\sigma_X)}e^{iX(\gamma-t)}
=e^{iXv_\rho},
\]

we have the coefficientwise identity

\[
\boxed{
L_{X,H}(v_\rho)
=x^{\rho-s_X}F(Hv_\rho).
}
\tag{3}
\]

Thus for any selected multiset `T` of zeros, with multiplicity `m(rho)`,

\[
\boxed{
\sum_{\rho\in\mathcal T}m(\rho)L_{X,H}(v_\rho)
=x^{-s_X}
\sum_{\rho\in\mathcal T}m(\rho)x^\rho F(Hv_\rho).
}
\tag{4}
\]

This is algebraic; no explicit formula has yet been used.

For a fixed `C>0`, let the critical Ford layer be

\[
\mathcal T_C
=
\{\rho:\ |d_\rho|\le C\},
\qquad
 d_\rho:=YD_\rho-\log J.
\tag{5}
\]

On this layer,

\[
H(\sigma_X-\beta_\rho)
=\frac{r+\log J+d_\rho}{YJ}
=O_C\!\left(\frac{\log J}{J}\right).
\tag{6}
\]

The imaginary displacement inside `F` is therefore asymptotically negligible. The same Bellotti-local population estimate already used in `NB-230` controls the normalized sum of any fixed Schwartz majorant in the carrier coordinate. By the mean-value theorem for the entire function `F`, uniformly on `|d_rho|<=C`,

\[
\frac1J
\sum_{\rho\in\mathcal T_C}
 m(\rho)e^{-d_\rho}
\left|
F(Hv_\rho)-F(H(\gamma-t))
\right|
\ll_C \frac{\log J}{J}.
\tag{7}
\]

Consequently the critical residue from `NB-234` can be written

\[
\boxed{
\mathcal R_C
=x^{-s_X}
\sum_{\rho\in\mathcal T_C}
 m(\rho)x^\rho F(H(\gamma-t))
+O_C\!\left(\frac{\log J}{J}\right).
}
\tag{8}
\]

The unresolved Ford transition is therefore, up to `o(1)`, a **microscopic smooth Landau zero sum with an additional horizontal-depth cutoff**.

## 2. The shell kills the ordinary Landau–Gonek diagonal

The classical uniform Landau–Gonek formula concerns the cumulative sum

\[
A_x(T):=\sum_{0<\gamma\le T}x^\rho
=-\frac{T}{2\pi}\Lambda(x)+E_x(T),
\tag{9}
\]

where `Lambda(x)` is supported on prime powers in the usual extended sense and Gonek gives an error uniform in `x,T>1`.

Ignore the horizontal cutoff in (8) for a moment and consider the positive-ordinate localized full zero sum

\[
\Sigma_x(t,H)
:=\sum_{\gamma>0}m(\rho)x^\rho F(H(\gamma-t)).
\tag{10}
\]

Its Landau main term is proportional to the integral of the weight

\[
w_{t,H}(u)=F(H(u-t)).
\tag{11}
\]

Fourier inversion applied to (1) gives

\[
\int_{\mathbb R}F(v)\,dv
=2\pi\phi(0)=0,
\tag{12}
\]

because `phi` is compactly supported in `(0,1)`. Hence

\[
\boxed{
\int_{\mathbb R}w_{t,H}(u)\,du=0.
}
\tag{13}
\]

For the positive-ordinate sum in (10), the lower endpoint `u=0` leaves only the tail

\[
\int_0^\infty w_{t,H}(u)\,du
=-\frac1H\int_{-\infty}^{-Ht}F(v)\,dv,
\tag{14}
\]

which is `O_A(H^{-1}(Ht)^{-A})` for every fixed `A`, since `F` is Schwartz on the real axis. At the heights under discussion this is negligible to arbitrary power.

Thus even if `x` is exactly a prime power, the usual diagonal

\[
-\frac{\Lambda(x)}{2\pi}
\int_0^\infty w_{t,H}(u)\,du
\]

is absent up to a superpolynomially small endpoint tail. **The logarithmic shell is automatically orthogonal to the constant-in-ordinate Landau main term.** The surviving quantity is a remainder coefficient.

This is the first useful source-specific consequence of the representation change. The critical Ford problem is not asking whether the prime-power diagonal is large enough; the shell geometry has removed that diagonal before any delicate zero estimate is attempted.

## 3. Global Landau–Gonek control loses the microscopic scale

Gonek's uniform formula gives

\[
\begin{aligned}
E_x(T)\ll{}&
 x\log(2x)\log\log(3x)
 +x\log(2T)\\
&+\log x\min\!\left\{T,\frac{x}{\langle x\rangle}\right\}
 +\min\!\left\{\frac{\log T}{\log x},T\log T\right\},
\end{aligned}
\tag{15}
\]

where `⟨x⟩` denotes the distance to the nearest *different* prime power. The proximity terms are important for arithmetic uniformity, but the first two generic terms already expose the present tariff.

Apply (9) to (10) by Stieltjes integration and integrate the remainder by parts. The key quantity is not the `L^1` mass of the microscopic window but its total variation:

\[
\int_{\mathbb R}|w'_{t,H}(u)|\,du
=
\int_{\mathbb R}|F'(v)|\,dv.
\tag{16}
\]

The right-hand side is independent of `H`. Therefore a black-box estimate of the form `sup |E_x(u)|` gives **no shrinking factor at all** from making the ordinate window narrower. In particular, after the normalization in (8),

\[
|x^{-s_X}|
=x^{-\sigma_X}
=\frac{e^{-r}}x,
\tag{17}
\]

the first two terms of (15) yield only

\[
\left|
 x^{-s_X}
 \int w_{t,H}\,dE_x
\right|
\ll_\phi
 \log(2x)\log\log(3x)
 +\log(2t)
 +\text{proximity terms}.
\tag{18}
\]

At the Ford scale

\[
X\asymp R
=Q^{2/3}(\log Q)^{1/3},
\qquad
x=e^X=t^{o(1)},
\tag{19}
\]

we have

\[
\log(2x)\asymp X,
\qquad
\log\log(3x)\asymp\log X,
\qquad
\log(2t)\asymp Q,
\]

with `X log X=o(Q)`. Hence the global theorem, used this way, supplies only

\[
\boxed{O_\phi(Q)}
\tag{20}
\]

from its generic cumulative errors, before any prime-power proximity loss is considered. This is enormously larger than the required `o(1)` bound.

Equation (20) is a statement about what the published global theorem **guarantees under this black-box smoothing**, not a lower bound on the true local remainder. The actual local sum may cancel far more strongly. The point is that differencing cumulative formulas, or smoothing them through bounded variation, cannot reveal that cancellation: the cumulative error is paid at full size at the microscopic scale.

## 4. The horizontal cutoff makes the required theorem stronger, not weaker

There is a second reason not to overstate the reduction. Formula (10) sums all zeros in the ordinate window, whereas (8) keeps only the transition layer

\[
|X(1-\beta)-\log J|\le C.
\tag{21}
\]

The ordinary Landau–Gonek formula has no such horizontal localization. `NB-230` controls sufficiently deep Ford tails absolutely, but the shallower side and the transition layer cannot simply be reconstructed from the unweighted cumulative formula. Thus (20) is an audit of the **nearest classical theorem family**, not a derivation of an estimate for (8).

The source-side target can now be stated more sharply. One needs a bound of schematic form

\[
\boxed{
 x^{-s_X}
 \sum_{\substack{\rho:\
 |X(1-\beta)-\log J|\le C}}
 m(\rho)x^\rho F(H(\gamma-t))
=o(1)
}
\tag{22}
\]

in the coupled Ford regime, or an equivalent estimate that combines the critical layer with neighboring layers before cancellation. Such a theorem must exploit information lost by the cumulative absolute error: microscopic ordinate cancellation, horizontal-depth structure, or a relation between the two.

This is more specific than the open condition at the end of `NB-234`. A growing hierarchy of depth moments is one sufficient surrogate, but (22) says what those moments are trying to approximate in classical explicit-formula language: a **horizontally marked microlocal Landau–Gonek remainder**.

## 5. Prior-art and representation audit

The Landau formula and Gonek's uniform refinement are classical. The quantitative audit uses S. M. Gonek, *A Formula of Landau and Mean Values of zeta(s)*, in *Topics in Analytic Number Theory* (1985), 92--97; Gonek later developed the explicit formula further in Contemporary Mathematics 143 (1993), 395--413. The 1985 theorem gives (15) directly and is available from the author's publication page. The same theorem is restated in the introduction of Durkan--Hughes--Pearce-Crump (2026), which develops a different Landau–Gonek generalization.

Recent work therefore confirms that this is still an active explicit-formula framework, but the prior-art search for this pass did not identify a published or posted theorem giving the horizontally truncated microscopic `o(x)` remainder required by (22). This is a search boundary, not a claim of nonexistence.

The representation audit separates the generic and zeta-specific pieces. The Stieltjes/total-variation observation in (16) is generic for any cumulative spectral formula: a rescaled smooth window does not automatically improve a sup-norm cumulative remainder. The zero integral in (12) is tied to the actual logarithmic shell construction through `phi in C_c^infty((0,1))`. The factor `x^rho`, the prime-power diagonal `Lambda(x)`, and the horizontal Ford coordinate in (21) are specifically zeta-arithmetic.

The change of representation is therefore useful but not circular. `NB-228` identified the exact Ford carrier and `NB-234` identified the depth-mark hierarchy; this finding places the same unresolved coefficient inside the classical explicit-formula ecosystem and shows quantitatively why the standard global theorem does not see it. It neither improves the Nyman–Beurling distance directly nor proves cancellation for actual zeta zeros.

## 6. Adversarial review and durable boundary

Three possible overclaims were checked explicitly.

First, the Landau diagonal does not vanish *exactly* if one insists on summing only positive ordinates from `0` upward; (14) is the correct endpoint correction. It is nevertheless negligible faster than any power in the present high-ordinate regime. Second, (20) is only the bound inherited from Gonek's published cumulative remainder after bounded-variation smoothing; it does not say the true local remainder has size `Q`. Third, Landau–Gonek controls the untruncated zero sum, whereas the Ford transition carries a horizontal cutoff, so no cancellation theorem for (8) is being smuggled in.

Subject to those calibrations, the durable method boundary is:

\[
\boxed{
\text{global cumulative Landau--Gonek}
\ +\ \text{black-box smoothing}
\ \not\Rightarrow\
\text{critical Ford }o(1).
}
\tag{23}
\]

The next non-circular source-side advance should therefore target the local remainder itself: either a microlocal Landau–Gonek estimate at window scale `1/H` with meaningful horizontal information, or a zeta-specific identity that couples critical depth to ordinate phase before any absolute-value estimate destroys the cancellation.
