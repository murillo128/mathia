# XF-091 — positive-time logarithmic cusp needs no new Volterra lattice counterterm

**Status:** `EXACT-DERIVED` + `SINGULAR-QUADRATURE` + `BRIDGE-REFINEMENT` + `NO-NEW-COUNTERTERM`. XF-090 shows that subtracting the Polymath reference does not leave a homogeneous residual Volterra equation. At every fixed positive heat time the deterministic reference defect contains the nonperturbative forcing

\[
\mathcal D_t(\xi)
=\frac{t}{16}\,\xi
\bigl(\log\xi+\gamma+\log(4\pi)\bigr)^2+O_t(\xi),
\qquad \xi\downarrow0,
\]

whose guarded vector-field resource grows like `(log q)^4` on `m\asymp q`. Thus the forcing must be represented on the periodic side rather than discarded as an error.

The leading positive-time logarithmic cusp nevertheless creates **no second mesh-dependent endpoint renormalization**. For the two-term endpoint model

\[
F(\xi)=-\frac c\xi+d\log\xi,
\qquad c>0,
\tag{1}
\]

the same pole counterterm isolated in XF-088,

\[
\boxed{c\log\Delta\,\delta_0,}
\tag{2}
\]

renormalizes the complete pole--pole, pole--log, and log--log trapezoidal convolution. No `log^2 Delta`, `d log Delta`, or other divergent endpoint delta is needed. With

\[
\widetilde F_{\Delta,N}
=-c\tau+d\ell
+\left(\frac{\Delta N}{2}+c\log\Delta\right)\delta_0,
\qquad
\tau=Y'_0,
\qquad
\ell(\xi)=\log\xi,
\tag{3}
\]

and grid `xi_m=m Delta`, the exact vector-field mismatch

\[
E_m:=\xi_m\left[
\Delta\left(NF(\xi_m)+\sum_{i=1}^{m-1}F(\xi_i)F(\xi_{m-i})\right)
-(\widetilde F_{\Delta,N}*\widetilde F_{\Delta,N})(\xi_m)
\right]
\tag{4}
\]

obeys

\[
\boxed{
|E_m|
\ll_{c,d}
\frac1m
+\Delta L_m
+m\Delta^2L_m^2,
\qquad
L_m:=1+|\log(m\Delta)|+\log m.
}
\tag{5}
\]

The first term is the XF-088 pure-pole error. The second is the new pole--log error, and the third is the log--log error. In particular, all new logarithmic-cusp errors vanish with the mesh and are small in the XF-086 guarded resource at the canonical Xi scales. Consequently XF-090's `xi log^2 xi` forcing is a genuine deterministic term that must be transported, but it is **not evidence for a new endpoint counterterm**. One may use the same frozen pole normalization and compare a forced continuum reference with its forced periodic discretization.

## 1. The pole--log convolution has an exact finite-part formula

XF-088 uses the half-line analytic family

\[
Y_\alpha(\xi)=\frac{\xi_+^{\alpha-1}}{\Gamma(\alpha)},
\qquad
\tau=\left.\partial_\alpha Y_\alpha\right|_{\alpha=0},
\tag{6}
\]

for which `tau(x)=1/x` on `x>0` and

\[
(\tau*b)(x)
=b(x)(\log x+\gamma)
+\int_0^x\frac{b(x-\eta)-b(x)}\eta\,d\eta.
\tag{7}
\]

Although `b(x)=log x` is not smooth at zero, the right side of `(7)` is still absolutely meaningful for every `x>0`. Substituting `b=ell` and scaling `eta=xu` gives

\[
\begin{aligned}
(\tau*\ell)(x)
&=\log x(\log x+\gamma)
+\int_0^1\frac{\log(1-u)}u\,du\\
&=\boxed{
\log x(\log x+\gamma)-\frac{\pi^2}{6}
}.
\end{aligned}
\tag{8}
\]

This identity also follows by differentiating the analytic convolution law `Y_alpha*Y_beta=Y_{alpha+beta}` in the two parameters. It fixes the finite-part normalization used below and removes any ambiguity about endpoint constants.

## 2. The old pole counterterm cancels the whole mesh logarithm in the cross term

Put

\[
x=m\Delta,
\qquad
H:=H_{m-1},
\qquad
A_m:=\sum_{i=1}^{m-1}\frac1i\log\left(1-\frac im\right).
\tag{9}
\]

The two symmetric pole--log pieces in the punctured discrete convolution are exactly

\[
\boxed{
-2cd\sum_{i=1}^{m-1}\frac1i\log((m-i)\Delta)
=-2cd\bigl(H\log x+A_m\bigr).
}
\tag{10}
\]

The corresponding continuum cross term from `(8)` is

\[
-2cd\left[
\log x(\log x+\gamma)-\frac{\pi^2}{6}
\right].
\tag{11}
\]

The already-existing `c log Delta delta_0` in `(3)` contributes the additional open-half-line cross term

\[
2cd\log\Delta\log x.
\tag{12}
\]

Subtracting `(11)` and `(12)` from `(10)` gives the **exact** renormalized pole--log discrepancy

\[
\boxed{
-2cd\left[
(H_{m-1}-\log m-\gamma)\log x
+A_m+\frac{\pi^2}{6}
\right].
}
\tag{13}
\]

Every naked `log Delta` has cancelled. In particular there is no surviving term proportional to `log Delta log x`, `log^2 Delta`, or a new endpoint delta coefficient depending on `d`.

The two remaining bracketed errors are ordinary Riemann/harmonic errors. The standard harmonic estimate gives

\[
H_{m-1}-\log m-\gamma=O(m^{-1}).
\tag{14}
\]

For `A_m`, write

\[
A_m=\frac1m\sum_{i=1}^{m-1}f(i/m),
\qquad
f(u)=\frac{\log(1-u)}u,
\tag{15}
\]

and note

\[
\int_0^1f(u)\,du=-\frac{\pi^2}{6}.
\tag{16}
\]

Split

\[
f(u)=\log(1-u)+h(u),
\qquad
h(u)=\frac{1-u}{u}\log(1-u).
\tag{17}
\]

The first Riemann sum is controlled directly by `log((m-1)!)` and Stirling's formula, while `h` extends continuously to both endpoints and has integrable derivative. Therefore

\[
\boxed{
A_m+\frac{\pi^2}{6}
=O\left(\frac{\log m}{m}\right).
}
\tag{18}
\]

Multiplying `(13)` by `x=m Delta` proves the middle term of `(5)`.

## 3. The log--log sector is ordinary weakly singular quadrature

The remaining new discrete convolution is

\[
\Delta\sum_{i=1}^{m-1}
\log(i\Delta)\log((m-i)\Delta).
\tag{19}
\]

The continuum value is an ordinary convergent integral,

\[
\boxed{
\int_0^x\log\eta\log(x-\eta)\,d\eta
=x\left[
(\log x)^2-2\log x+2-\frac{\pi^2}{6}
\right].
}
\tag{20}
\]

Set `L=log x` and scale `eta=xu`. The difference between `(19)` and `(20)` is `x` times the Riemann-sum error for

\[
g_L(u)=(L+\log u)(L+\log(1-u)).
\tag{21}
\]

Expand `(21)`. The constant term has error `O(L^2/m)`. Each single-log term has error `O(|L| log m/m)` by Stirling. Finally `log u log(1-u)` extends continuously by zero at both endpoints and has bounded variation, so its Riemann error is `O(1/m)`. Hence

\[
\left|
\Delta\sum_{i=1}^{m-1}\log(i\Delta)\log((m-i)\Delta)
-\int_0^x\log\eta\log(x-\eta)\,d\eta
\right|
\ll
\Delta L_m^2.
\tag{22}
\]

After multiplication by `x=m Delta`, this gives the final term in `(5)`.

Combining `(13)`, `(18)`, `(22)`, and the pure-pole estimate from XF-088 proves `(5)`.

## 4. The logarithmic cusp is negligible in the guarded resource after renormalization

Use the canonical XF-071/XF-090 scales

\[
M=q^2,
\qquad
\Delta\asymp q^{-3/2},
\qquad
J\asymp q^{1/4},
\qquad
K\asymp q\log\log T,
\tag{23}
\]

and the exact selector resource

\[
\mathcal R(E)
=\frac1{4M^2}\sum_{m=J}^{K}I_m|E_m|^2,
\qquad
I_m\asymp_g m^4.
\tag{24}
\]

The three terms in `(5)` contribute respectively

\[
O_g\bigl(q^{-1}(\log\log T)^3\bigr),
\tag{25}
\]

\[
O_{g,c,d}\bigl(q^{-2}(\log\log T)^5 L_K^2\bigr),
\tag{26}
\]

and

\[
O_{g,c,d}\bigl(q^{-3}(\log\log T)^7 L_K^4\bigr),
\tag{27}
\]

where `L_K=O(log q+log log log T)` on the live band. These are `o(1)` in the same Xi asymptotic regime used by XF-088. Thus the positive-time logarithmic cusp does not consume the guarded consistency margin once the old pole counterterm is retained.

This statement should be contrasted with XF-090. The forcing `D_t` itself has resource `asymp (log q)^4` and cannot be omitted. Equations `(25)`--`(27)` concern the **difference between continuum and lattice realizations of the same singular deterministic sector**, not the size of that sector. Large deterministic forcing and small discretization error are compatible.

## 5. Forced-reference interpretation

For a continuum reference `F_t`, define its deterministic Volterra defect

\[
D_t
:=\partial_tF_t
-\left[\xi^2F_t-\xi(F_t*F_t)\right].
\tag{28}
\]

On the mesh define the analogous discrete defect using the exact XF-087 trapezoid and the same endpoint representative `(3)`:

\[
D_{t,m}^{\Delta}
:=\partial_tF_t(\xi_m)
-\left[
\xi_m^2F_t(\xi_m)
-\xi_m\mathcal T_\Delta(F_t,F_t)(\xi_m)
\right].
\tag{29}
\]

For the singular model `(1)`, equations `(4)`--`(5)` say exactly that

\[
\boxed{
D_{t,m}^{\Delta}-D_t(\xi_m)=E_m
}
\tag{30}
\]

up to the sign convention of `(4)` fixed by writing both defects as `partial_t - vector field`. Hence the correct periodic analogue of XF-090 is not to erase `D_t`, but to carry the **discrete reference defect** `(29)`. Its discrepancy from the continuum forcing is `o(1)` in guarded resource for the pole-plus-log singular sector.

For the Polymath reference of XF-089,

\[
c=\frac14,
\qquad
d_t=-\frac t8
\tag{31}
\]

at leading endpoint order (the harmless constant shift `gamma+log(4 pi)` can be absorbed into the regular part for this counterterm calculation). The `xi log^2 xi` law of XF-090 is therefore precisely in the regime where `(30)` matters: it is a nonperturbative continuum forcing generated by a time-dependent logarithmic reference cusp, yet its lattice representation needs no endpoint renormalization beyond the time-independent pole term `(1/4) log Delta delta_0`.

## 6. Stress tests and boundaries

**At `d=0`.** The result reduces to the pure-pole renormalization of XF-088. No new term remains.

**At `c=0`.** There is no endpoint delta counterterm at all. The only discrepancy is the ordinary log--log quadrature error `(22)`, confirming that an integrable logarithm by itself does not create a divergent mesh normalization.

**Mesh dependence.** Equation `(13)` is the decisive check: retaining any additional `d`-dependent divergent delta would over-renormalize the exact cross term, because the existing `c log Delta` contribution already converts `log x` to `log m` in the harmonic lattice asymptotics.

**What is not proved.** The exact Polymath carrier contains lower-order endpoint terms beyond `-c/xi+d_t log xi`. This finding does not claim a complete guarded quadrature theorem for that full remainder or for the genuinely Xi-specific quotient residual. It proves that the first new singularity exposed by XF-089/XF-090 does not generate another independent counterterm. Any remaining failure must come from lower-order reference regularity, source extraction, stability of the forced Volterra comparison, or the separate positive-`Lambda` transition-mass gate.

## 7. Prior-art boundary

Hadamard finite-part convolution and Euler--Maclaurin/trapezoidal expansions for algebraic-logarithmic endpoint singularities are classical. In particular, the general quadrature literature treats endpoint expansions involving powers times polynomials in logarithms and shows that singular trapezoidal errors admit systematic asymptotic corrections. No novelty is claimed for that general phenomenon or for the elementary constants `pi^2/6` appearing in `(8)` and `(20)`.

The Mathia-specific delta is the exact cancellation `(13)` in the **XF-087 Volterra convolution normalization**, with the **XF-088 pole delta fixed in advance**, followed by the guarded Xi-scale estimate `(25)`--`(27)`. A targeted literature audit found no de Bruijn--Newman or Xi-flow result identifying this frozen-counterterm compatibility between the Polymath positive-time logarithmic cusp and the periodic Vieta/Volterra lattice. The argument above is self-contained, so no new `SOURCES.md` anchor is load-bearing.

## 8. Consequence for `xi_flow`

XF-090 left two possible repairs for its nonperturbative deterministic forcing: transport that forcing explicitly on both sides, or replace the reference by an exact heat solution. XF-091 makes the first option substantially cleaner. The leading positive-time reference singularity can be discretized with the **same endpoint normalization already forced at `t=0`**:

\[
\boxed{
\frac14\log\Delta\,\delta_0
\quad\text{remains the only divergent endpoint lattice counterterm through the pole-plus-log sector.}
}
\tag{32}
\]

The next source-to-grid theorem should therefore compare the full continuum reference defect with its discrete defect, rather than searching for another mesh renormalization to cancel the `xi log^2 xi` term. What remains genuinely open is guarded control of the lower-order reference remainder and the Xi-specific residual, followed separately by the implication from `Lambda>0` to nontrivial destination guarded mass.