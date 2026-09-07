# XF-093 — point-sampled guarded moments need mesh-scale Fourier regularity

**Status:** `EXACT-DERIVED` + `STRUCTURAL/OBSTRUCTION` + `SOURCE-TO-GRID` + `SAMPLING-GATE`. XF-092 closes the deterministic Polymath-reference side of the continuum-to-periodic Volterra comparison: after the frozen XF-088 pole counterterm, the full reference and its exact XF-087 lattice counterpart differ by `o(1)` in the guarded selector resource. The remaining source bridge is therefore the genuinely Xi-specific quotient residual

\[
\mathcal R_t(\xi)=\mathcal Z_t(\xi)-\mathcal Z_t^M(\xi).
\]

XF-089 gives the exact high-line representation

\[
\boxed{
\mathcal R_t(\xi)
=-\frac{\xi}{2\pi}e^{a\xi}\widehat{L_t}(\xi),
\qquad
L_t(x)=\log\frac{H_t(x+ia)}{B_t(x+ia)},
}
\tag{1}
\]

for positive frequency, once a bounded logarithm is chosen on the zero-free high line. It is tempting to combine very accurate relative control of `H_t/B_t` with `(1)` and simply sample `\mathcal R_t` at the XF-087 frequency mesh. That implication is false without an additional **mesh-scale Fourier regularity** input.

There is an explicit zero-free matched control for which the high-line quotient tends to one at an arbitrarily prescribed rate, uniformly on the entire real line and with every fixed number of strip derivatives, while one guarded mesh sample of `(1)` stays bounded away from zero. At the canonical Xi scales

\[
M=q^2,
\qquad
\Delta\asymp q^{-3/2},
\qquad
K\asymp q\log\log T,
\tag{2}
\]

choose the visible mode `k_q=q`, write `\xi_q=k_q\Delta\asymp q^{-1/2}`, and let `\varepsilon_q\downarrow0` be **arbitrary**. Set

\[
X_q=\frac1{\varepsilon_q\xi_q},
\qquad
L_q(x)=\varepsilon_q e^{-x^2/(2X_q^2)}\cos(\xi_q x),
\qquad
U_q(z)=e^{L_q(z)}.
\tag{3}
\]

Then `U_q` is entire and zero-free, `U_q-1 -> 0` uniformly on every fixed horizontal strip, and the same is true after any fixed number of derivatives. Nevertheless, if `\mathcal R_q` is defined from `L_q` by the exact transform in `(1)`,

\[
\boxed{
\mathcal R_q(\xi_q)
\longrightarrow
-\frac1{\sqrt{8\pi}}.
}
\tag{4}
\]

Since the exact XF-086 weight at `k_q=q` is asymptotic to a nonzero constant,

\[
\frac{I_q}{4M^2}
\longrightarrow
\frac{\pi^4C_g}{4},
\qquad
C_g=\int_{-1}^{1}|\chi(u)|^2du,
\tag{5}
\]

this single sampled mode retains the positive guarded resource

\[
\boxed{
\mathcal R_{\{q\}}(\mathcal R_q)
\longrightarrow
\frac{\pi^3C_g}{32}>0.
}
\tag{6}
\]

Thus **no rate of fixed-strip relative quotient accuracy, even super-polynomial or exponential and even with any fixed finite collection of derivatives, controls the direct point-sampled XF-087/XF-086 moment state by itself**. The missing information is spectral anti-concentration on the `Delta` mesh scale. An elementary cellwise `H^1` estimate gives one precise sufficient replacement: if `C_m=[\xi_m-\Delta/2,\xi_m+\Delta/2]` and `w_m=I_m/(4M^2)`, then every locally `H^1` residual satisfies

\[
\boxed{
\sum_{m=J}^{K}w_m|\mathcal R(\xi_m)|^2
\le
\frac2\Delta\sum_{m=J}^{K}w_m\int_{C_m}|\mathcal R(\xi)|^2d\xi
+
2\Delta\sum_{m=J}^{K}w_m\int_{C_m}|\mathcal R'(\xi)|^2d\xi.
}
\tag{7}
\]

Equation `(7)` turns the open source dictionary into a sharply stated analytic target: prove an Xi-specific cell-scale sampling bound of this kind, prove an effective bandwidth/exponential-type theorem that implies one, or use a different discretization whose state is stable under the available continuum norm. Fixed-strip quotient asymptotics alone cannot close the gate.

## 1. An arbitrarily small entire quotient can hide a constant mesh sample

Fix any sequence `\varepsilon_q>0` with `\varepsilon_q -> 0`. No rate restriction is imposed; one may take a negative power of `q`, a super-polynomial sequence, or `e^{-q}`. Let `\xi_q=k_q\Delta` with `k_q=q` and define `(3)`.

On the real axis,

\[
|L_q(x)|\le\varepsilon_q
\tag{8}
\]

for every `x`. More generally, for every fixed strip half-width `rho>0`,

\[
\sup_{|\operatorname{Im}z|\le\rho}|L_q(z)|
\le
\varepsilon_q
\exp\!\left(\frac{\rho^2}{2X_q^2}\right)
\cosh(\rho\xi_q)
=\varepsilon_q(1+o(1)).
\tag{9}
\]

The same construction is invisible to any fixed-order local regularity test. Differentiating the Gaussian and carrier shows, for every fixed integer `r>=0`,

\[
\sup_{|\operatorname{Im}z|\le\rho}
|L_q^{(r)}(z)|
\le
C_{r,\rho}\varepsilon_q
(\xi_q+X_q^{-1})^r(1+o(1)).
\tag{10}
\]

Because `X_q^{-1}=\varepsilon_q\xi_q`, the right side is `O_{r,rho}(\varepsilon_q\xi_q^r)` and tends to zero. Since `U_q=e^{L_q}`, fixed-order derivatives of `U_q-1` also tend to zero on the strip by the ordinary product/Faa di Bruno formulas. The quotient is therefore not merely pointwise close to one: it is uniformly close on the whole high line and remains so under any fixed finite analytic jet.

The physical-space price is that the perturbation becomes extremely broad:

\[
X_q=\frac1{\varepsilon_q\xi_q}.
\tag{11}
\]

That broad support is exactly what creates a narrow spectral spike.

## 2. The Fourier spike has constant height at the chosen mesh node

Use the Fourier convention of XF-089,

\[
\widehat f(\xi)=\int_{\mathbb R}f(x)e^{-ix\xi}dx.
\tag{12}
\]

The transform of `(3)` is explicit:

\[
\widehat L_q(\xi)
=
\frac{\varepsilon_q\sqrt{2\pi}X_q}{2}
\left[
 e^{-X_q^2(\xi-\xi_q)^2/2}
+
 e^{-X_q^2(\xi+\xi_q)^2/2}
\right].
\tag{13}
\]

At the positive mesh node `\xi=\xi_q`,

\[
\widehat L_q(\xi_q)
=
\frac{\varepsilon_q\sqrt{2\pi}X_q}{2}
\left(1+e^{-2X_q^2\xi_q^2}ight).
\tag{14}
\]

But

\[
\varepsilon_qX_q=\frac1{\xi_q},
\qquad
X_q\xi_q=\frac1{\varepsilon_q}\longrightarrow\infty.
\tag{15}
\]

Therefore

\[
\widehat L_q(\xi_q)
=
\frac{\sqrt{2\pi}}{2\xi_q}(1+o(1)).
\tag{16}
\]

Substitution into the exact XF-089 dictionary `(1)` gives

\[
\mathcal R_q(\xi_q)
=
-\frac{\xi_q}{2\pi}e^{a\xi_q}
\frac{\sqrt{2\pi}}{2\xi_q}(1+o(1)).
\tag{17}
\]

Since `\xi_q\asymp q^{-1/2}->0` and `a` is fixed on the high line, `(17)` is exactly `(4)`.

The cancellation of `\varepsilon_q` is the key mechanism. Making the high-line quotient one million times more accurate simply makes the physical-space packet one million times broader, which makes its Fourier spike one million times narrower and taller. Point evaluation at the deliberately aligned mesh node retains the same value.

## 3. One mode already carries order-one XF-086 resource

XF-086 assigns raw moment mode `m` the exact weight

\[
w_m
=
\frac{I_m}{4M^2},
\qquad
I_m
=
\int_{-1}^{1}(\pi m+u)^4|\chi(u)|^2du.
\tag{18}
\]

At `m=q`, dominated expansion of the fixed `u` integral gives

\[
I_q
=
\pi^4q^4C_g(1+O(q^{-1})).
\tag{19}
\]

Since `M=q^2`, equations `(18)`--`(19)` prove `(5)`. Combining with `(4)` yields

\[
\begin{aligned}
\mathcal R_{\{q\}}(\mathcal R_q)
&=w_q|\mathcal R_q(\xi_q)|^2\\
&\longrightarrow
\frac{\pi^4C_g}{4}\frac1{8\pi}
=
\frac{\pi^3C_g}{32},
\end{aligned}
\tag{20}
\]

which is `(6)`.

The chosen mode is safely inside the live nonlinear band. It lies far above the XF-071 source guard `J\asymp q^{1/4}` and below `K\asymp q\log\log T`. Thus this is not an ultra-infrared artifact removed by the guarded quotient, nor an ultraviolet mode outside the finite carrier.

The spectral width of the positive spike in `(13)` is

\[
X_q^{-1}=\varepsilon_q\xi_q
\asymp\varepsilon_q q^{-1/2}.
\tag{21}
\]

Relative to the Volterra mesh,

\[
\frac{X_q^{-1}}{\Delta}
\asymp\varepsilon_q q.
\tag{22}
\]

If `\varepsilon_q\ll q^{-1}`, the spike is much narrower than a single mesh cell; its continuum `L^2` mass can be arbitrarily small while the aligned point sample remains fixed. Even when the spike is wider than one cell, equations `(4)`--`(6)` show that fixed-strip amplitude control alone has no mechanism that bounds its sampled height.

## 4. A cellwise Sobolev estimate states exactly what extra information is sufficient

The obstruction is a sampling problem, not a pathology specific to Gaussians. Let `I` be any interval of length `Delta`, let `x_0 in I`, and let `f in H^1(I)`. There exists `y in I` with

\[
|f(y)|^2\le\frac1\Delta\int_I|f|^2.
\tag{23}
\]

The fundamental theorem of calculus and Cauchy--Schwarz give

\[
|f(x_0)|
\le
|f(y)|+\int_I|f'|
\le
\Delta^{-1/2}\|f\|_{L^2(I)}
+
\Delta^{1/2}\|f'\|_{L^2(I)}.
\tag{24}
\]

Squaring proves

\[
\boxed{
|f(x_0)|^2
\le
\frac2\Delta\int_I|f|^2
+2\Delta\int_I|f'|^2.
}
\tag{25}
\]

Apply `(25)` to `f=\mathcal R` on the disjoint cells

\[
C_m=[\xi_m-\Delta/2,\xi_m+\Delta/2]
\tag{26}
\]

and multiply by the exact positive XF-086 weights `w_m`. Summing gives `(7)` with no asymptotics and no assumption on phases. Equivalently, if `w_\Delta(\xi)=w_m` on `C_m`, then

\[
\boxed{
\mathcal R_{[J,K]}(Q)
\le
2\Delta^{-1}
\|\mathcal R\|_{L^2(w_\Delta)}^2
+
2\Delta
\|\partial_\xi\mathcal R\|_{L^2(w_\Delta)}^2,
\qquad
Q_m=\mathcal R(\xi_m).
}
\tag{27}
\]

This is only one sufficient interface. A Paley--Wiener/exponential-type hypothesis at bandwidth below the sampling density, a Bernstein inequality, or direct control of cell oscillation would play the same role. Conversely, the packet `(3)` shows why some such anti-concentration information is unavoidable for **direct point sampling**: its Fourier derivative grows precisely as the spike narrows, so the second term in `(27)` records the hidden cost that fixed physical-space jets do not see.

## 5. Relation to XF-073, XF-079, and the closed reference bridge

XF-073 proves extraordinarily accurate Gaussian/Appell relative recovery on the safe Xi high-line region. XF-079 then removes a different obstruction: for an already periodic carrier, disjoint selector sidebands make its weighted Vieta resource readable at one safe center. Neither statement is a sampling theorem for the Fourier transform of an arbitrary high-line logarithmic quotient.

The control `(3)` makes this distinction explicit. It is uniformly tiny on **every real center**, not merely one center, so enlarging the safe-center domain cannot detect it. Yet `(13)` places finite Fourier mass exactly at a chosen XF-087 node. The old center-local versus full-center issue is therefore separate from the new continuum-frequency versus grid-frequency issue.

Likewise, XF-088--XF-092 are not contradicted. Their endpoint analysis is deterministic and concerns the singular Polymath reference. The packet here is regular at `xi=0` and is inserted entirely into the quotient residual that XF-092 deliberately leaves as the Xi-specific part of the bridge. The frozen counterterm continues to renormalize the reference exactly as before.

The conclusion is that after XF-092 the source dictionary cannot be reduced to

\[
\text{very accurate high-line quotient}
\quad+\quad
\text{evaluate its transform at }\xi_m.
\tag{28}
\]

A theorem must additionally prevent mesh-aligned spectral concentration or avoid point sampling altogether.

## 6. Stress tests and evidence boundary

**Not an alternative Xi heat flow.** The multiplier `U_q=e^{L_q}` is an entire, zero-free, symmetry-friendly high-line quotient control, but multiplying the Polymath reference by `U_q` is not asserted to produce a solution of the de Bruijn--Newman heat equation, the Riemann functional equation, or an Euler-product-compatible object. Therefore `(3)`--`(6)` do not refute an Xi-specific theorem that uses those global constraints. They refute only the inference that quotient accuracy/regularity of the type stated above is sufficient by itself.

**Arbitrary accuracy rate.** Because `\varepsilon_q` is arbitrary, no improvement from polynomial to super-polynomial or exponential relative error closes the direct sampling gap unless it is accompanied by a restriction on the packet width or Fourier concentration. This is the main reason the example is stronger than a generic bounded-quotient warning.

**Fixed analytic jets are insufficient.** Equation `(10)` rules out the obvious repair of asking for several more `x` derivatives on the high line. For every fixed `r`, those derivatives become even smaller. What is needed is a scale-dependent regularity statement strong enough to resolve cells of width `Delta`, not a fixed-order local smoothness condition with no global localization information.

**No contradiction with continuous selector smallness.** A continuum square-function estimate may average over a spectral cell and therefore assign very little mass to a spike much narrower than that cell. The finite Volterra carrier, in contrast, evolves exact nodal values. Passing from one to the other is exactly the sampling step isolated here. A future proof may show that the actual Xi residual has enough frequency regularity for `(27)`; this finding does not claim otherwise.

**Grid alignment is legitimate as a falsifier.** The source theorem must hold uniformly for the deterministic mesh chosen by the periodic carrier. A control whose spectral packet is centered on that mesh is therefore an admissible stress test of any proposed norm implication. Randomizing or shifting the grid could suppress one aligned example but would change the exact XF-087 carrier and would itself require a quantitative argument.

## 7. Prior-art and novelty boundary

The phenomenon belongs to classical sampling theory. Plancherel--Polya and Shannon-type inequalities control point samples when an exponential-type/bandwidth hypothesis ties the function to the sampling density; modern formulations likewise make bandwidth or Bernstein-space control explicit. A targeted literature audit found exactly this neighboring framework. No external theorem is load-bearing here: the negative control is the elementary Gaussian transform `(13)` and the positive replacement `(25)` is the one-dimensional `H^1` point-evaluation estimate. `SOURCES.md` therefore needs no new anchor.

No novelty is claimed for spectral concentration, Gaussian Fourier transforms, Sobolev point evaluation, or classical sampling inequalities. The Mathia-specific delta is the exact scale match: the XF-089 quotient dictionary contributes the factor `xi`, the canonical XF-087 mesh has `Delta\asymp q^{-3/2}`, and the XF-086 guarded weight at the interior mode `m=q` is order one. Those three facts permit an arbitrarily small high-line quotient to retain the explicit nonzero guarded limit `(6)` at a single live Volterra mode.

## 8. Consequence for `xi_flow`

The deterministic source-to-grid work is essentially complete after XF-092, but the Xi-specific residual now has a more precise gate. Before trying to realize its sampled values by the XF-085 equal-weight carrier, one must prove a **mesh-scale sampling/anti-concentration theorem for the actual quotient residual**. A sufficient target is the cell-Sobolev control `(27)` with a right-hand side `o(1)` on the guarded band, after the same reference subtraction and frozen counterterm already fixed by XF-088--XF-092.

If such a theorem follows from Polymath-style global high-line estimates, the source bridge can proceed directly to the exact finite moment state and then to XF-085--XF-087. If it fails, the architecture should replace nodal sampling by a source-faithful discretization whose state is stable under the continuum norm and then re-check its heat evolution. In either case, the remaining source problem is no longer an unspecified `Gaussian -> Vieta` dictionary: it is the concrete question of whether the actual Xi residual can concentrate on frequency scales narrower than the canonical Volterra mesh.

The independent destination gate remains unchanged: even after a successful source sampling theorem and guarded periodic transport, one must still prove that a hypothetical positive `Lambda` transition forces nonvanishing mass in the guarded destination resource.