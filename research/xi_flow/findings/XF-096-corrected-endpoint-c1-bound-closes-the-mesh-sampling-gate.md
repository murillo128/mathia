# XF-096 — corrected endpoint C1 bound closes the mesh sampling gate

**Status:** `EXACT-DERIVED` + `SOURCE-TO-GRID` + `SAMPLING-GATE-CLOSED` + `BRIDGE-REDUCTION`. XF-093 isolates a genuine obstruction to reading periodic moment samples from fixed-strip quotient accuracy: an arbitrarily small high-line logarithmic quotient can hide a Fourier spike narrower than the Volterra mesh and keep one weighted nodal sample of order one. It also gives an exact sufficient replacement, a cellwise `H^1` sampling inequality. XF-095 subsequently proves more regularity for the **actual dynamically corrected Xi residual** than its final boundary uses. Combining those two findings closes the sampling gate for that corrected residual.

Write

\[
\mathcal R_t^\sharp(\xi)
:=\mathcal Z_t(\xi)-\mathcal Z_t^{M,\sharp}(\xi),
\qquad 0\le t\le\frac12,
\tag{1}
\]

with the dynamic corrector of XF-095. On a fixed endpoint interval `0<xi<=xi_*`, XF-095 gives uniformly in `t`

\[
\boxed{
|\mathcal R_t^\sharp(\xi)|
\ll_a \xi^2(1+|\log\xi|)^3.
}
\tag{2}
\]

Its weighted `C^1` bootstrap also gives the missing mesh regularity. The raw residual obeys

\[
|\mathcal R_t(\xi)|+\xi|\partial_\xi\mathcal R_t(\xi)|
\ll_a \xi(1+|\log\xi|)^2,
\tag{3}
\]

while on the live interval the explicit corrector has

\[
\partial_\xi\mathcal C_t(\xi)
=
-\frac{t^2}{32}
\left[(\log\xi+C_0)^2+2(\log\xi+C_0)\right]
+\beta(t),
\tag{4}
\]

so

\[
\boxed{
|\partial_\xi\mathcal R_t^\sharp(\xi)|
\ll_a (1+|\log\xi|)^2.
}
\tag{5}
\]

Now use the exact XF-093 cells

\[
C_m=[\xi_m-\Delta/2,\xi_m+\Delta/2],
\qquad \xi_m=m\Delta,
\tag{6}
\]

and the XF-086 weights

\[
w_m=\frac{I_m}{4M^2},
\qquad
I_m=\int_{-1}^{1}(\pi m+u)^4|\chi(u)|^2\,du.
\tag{7}
\]

For the canonical band `J<=m<=K`, every cell lies inside `(0,xi_*)` for large scales. If

\[
L_*:=1+|\log\Delta|+\log(K+1),
\tag{8}
\]

then the exact XF-093 sampling inequality and `(2)`--`(5)` give

\[
\boxed{
\sum_{m=J}^{K}w_m
|\mathcal R_t^\sharp(\xi_m)|^2
\ll_{a,\chi}
\frac{\Delta^4K^9}{M^2}L_*^6
+
\frac{\Delta^2K^5}{M^2}L_*^4.
}
\tag{9}
\]

At the Xi scales

\[
M=q^2,
\qquad
\Delta^2\asymp q^{-3},
\qquad
J=q^{1/4},
\qquad
K\asymp q\log\log T,
\tag{10}
\]

this becomes

\[
\boxed{
\sup_{0\le t\le1/2}
\mathcal R_{[J,K]}
\bigl((\mathcal R_t^\sharp(\xi_m))_m\bigr)
\ll_{a,\chi}
q^{-1}(\log\log T)^9L_*^6
+q^{-2}(\log\log T)^5L_*^4
=o(1).
}
\tag{11}
\]

Thus the actual corrected Xi residual satisfies **exactly the mesh-scale anti-concentration condition that XF-093 identified as missing**. No additional bandwidth theorem or inference from fixed-strip quotient accuracy is needed for the corrected residual moment samples. The XF-093 counterexample remains valid for arbitrary quotients; it is excluded here by the stronger Xi-specific endpoint `C^1` control proved in XF-095.

This removes one live source gate but does not by itself finish the continuum-to-periodic dynamics. XF-092 controls the deterministic Polymath reference quadrature and XF-095 makes the corrected reference defect guarded-small; what remains is the stability/quadrature bookkeeping for the corrected residual/reference convolution when comparing the continuum nodal curve to the exact XF-087 trapezoid evolution, together with the separate theorem that a positive-`Lambda` transition forces nonvanishing destination resource.

## 1. XF-095 supplies the regularity XF-093 asked for

XF-093 proves for every locally `H^1` function `f` on a cell of length `Delta`, sampled at its center,

\[
|f(\xi_m)|^2
\le
\frac2\Delta\int_{C_m}|f(\xi)|^2\,d\xi
+2\Delta\int_{C_m}|f'(\xi)|^2\,d\xi.
\tag{12}
\]

After multiplication by `w_m` and summation this becomes

\[
\sum_{m=J}^{K}w_m|f(\xi_m)|^2
\le
\frac2\Delta\sum_{m=J}^{K}w_m
\int_{C_m}|f|^2
+2\Delta\sum_{m=J}^{K}w_m
\int_{C_m}|f'|^2.
\tag{13}
\]

The generic obstruction in XF-093 is precisely that fixed-strip control of the physical-space logarithmic quotient does not control either right-hand term at the shrinking mesh scale. XF-095 changes that input for the actual Xi residual. Its Section 2 closes the weighted `C^1` bootstrap `(3)` uniformly in heat time before deriving the dynamic cusp. Subtracting the explicit cusp corrector preserves the derivative bound because `(4)` has only logarithmic growth. Therefore `f=R_t^sharp` is an admissible input to `(13)` with quantitative bounds `(2)` and `(5)`.

No Fourier inversion of the high-line quotient is used in this step. The needed regularity is already a theorem about the canonical positive-frequency residual itself. This is why the narrow-spike example of XF-093 no longer controls the actual corrected source class.

## 2. The cellwise state term is the old guarded endpoint scale

For `m>=J->infinity`, every `xi in C_m` satisfies

\[
\xi\asymp m\Delta,
\qquad
1+|\log\xi|\le L_*+O(1).
\tag{14}
\]

Also, since `chi` is fixed and compactly supported,

\[
I_m\ll_\chi m^4,
\qquad
w_m\ll_\chi\frac{m^4}{M^2}.
\tag{15}
\]

Equation `(2)` therefore gives

\[
\int_{C_m}|\mathcal R_t^\sharp(\xi)|^2d\xi
\ll_a
\Delta\,(m\Delta)^4L_*^6.
\tag{16}
\]

Substituting `(15)`--`(16)` into the first term of `(13)`,

\[
\begin{aligned}
\frac2\Delta
\sum_{m=J}^{K}w_m
\int_{C_m}|\mathcal R_t^\sharp|^2
&\ll_{a,\chi}
\frac{\Delta^4L_*^6}{M^2}
\sum_{m=J}^{K}m^8\\
&\ll_{a,\chi}
\boxed{
\frac{\Delta^4K^9}{M^2}L_*^6
}.
\end{aligned}
\tag{17}
\]

This is the same `q^{-1}` endpoint scale already found by direct nodal substitution in XF-095, but here it enters through the exact sufficient sampling gate of XF-093 rather than assuming that point evaluation is harmless.

## 3. The mesh anti-concentration cost is strictly smaller

The derivative estimate `(5)` gives on the same cell

\[
\int_{C_m}
|\partial_\xi\mathcal R_t^\sharp(\xi)|^2d\xi
\ll_a \Delta L_*^4.
\tag{18}
\]

Thus the second term of `(13)` is

\[
\begin{aligned}
2\Delta
\sum_{m=J}^{K}w_m
\int_{C_m}|\partial_\xi\mathcal R_t^\sharp|^2
&\ll_{a,\chi}
\frac{\Delta^2L_*^4}{M^2}
\sum_{m=J}^{K}m^4\\
&\ll_{a,\chi}
\boxed{
\frac{\Delta^2K^5}{M^2}L_*^4
}.
\end{aligned}
\tag{19}
\]

Equations `(17)` and `(19)` prove `(9)`. Under `(10)`,

\[
\frac{\Delta^4K^9}{M^2}
\asymp
q^{-1}(\log\log T)^9,
\qquad
\frac{\Delta^2K^5}{M^2}
\asymp
q^{-2}(\log\log T)^5.
\tag{20}
\]

The logarithmic factor `L_*` grows only polylogarithmically in `q`, so both terms tend to zero in the existing Xi asymptotic regime. Importantly, the actual **sampling penalty** is the second term and is parametrically smaller than the endpoint state term by an additional power of `q` up to polylogarithms.

## 4. The XF-093 spike fails exactly this gate

The matched control in XF-093 has a selected live node `xi_q\asymp q^{-1/2}` at which

\[
|\mathcal R_q(\xi_q)|\to\frac1{\sqrt{8\pi}}.
\tag{21}
\]

An actual corrected Xi residual satisfying `(2)` instead obeys at the same scale

\[
|\mathcal R_t^\sharp(\xi_q)|
\ll
q^{-1}(1+\log q)^3
\longrightarrow0.
\tag{22}
\]

So the counterexample is already excluded by the state estimate. Its spectral spike also pays in the derivative term of `(13)` as its width collapses; this is the anti-concentration cost XF-093 was designed to expose. There is therefore no contradiction between the generic negative result and `(11)`: XF-093 rules out deriving nodal control from **fixed-strip quotient accuracy alone**, while XF-095 supplies additional Xi-specific frequency-side `C^1` information.

This distinction is load-bearing. If the weighted `C^1` bootstrap in XF-095 were later weakened or withdrawn under adversarial review, the mesh gate would reopen immediately. The present finding does not manufacture regularity from the relative high-line estimate; it consumes the canonical regularity already proved in XF-095.

## 5. Consequence for the equal-weight moment interface

Define the prescribed corrected residual moments on the visible band by

\[
Q_m(t):=\mathcal R_t^\sharp(\xi_m),
\qquad J\le m\le K.
\tag{23}
\]

Equation `(11)` is exactly the XF-086 resource hypothesis, and in fact is far stronger than its sufficient threshold `o(J^3)`. Consequently, at every fixed time in the heat interval the visible corrected residual vector lies deep inside the exact equal-weight realization cone of XF-085--XF-086. The previous phrase “a separate Xi-specific mesh-scale `H^1`/bandwidth estimate is still required before the corrected resource becomes an extracted periodic moment statement” is therefore no longer a live obligation once XF-095 is admitted: its weighted `C^1` bootstrap is that estimate.

This is a **source-state** conclusion, not yet a full dynamic intertwining theorem. Realizing `Q(t_0)` at one time does not prove that the exact XF-087 periodic trajectory from that realization shadows the continuum curve `Q(t)` at later times. The deterministic reference quadrature and corrected reference defect are already controlled by XF-092 and XF-095, respectively, but the residual/reference and residual/residual convolution discretization still needs a quantitative stability estimate in the guarded norm, or an equivalent argument that makes that comparison unnecessary.

## 6. Prior-art and novelty boundary

The scalar inequality `(12)` is an elementary one-dimensional Sobolev/trace estimate, and sampling inequalities for Sobolev functions and Poincare--Friedrichs estimates are classical numerical-analysis material. A targeted literature check found only that generic background, not an Xi/de Bruijn--Newman statement matching `(9)`--`(11)`. No novelty is claimed for Sobolev point evaluation or for the cell inequality itself.

The durable Mathia delta is the scale-matched consequence of two existing line-local theorems: XF-093 stated the exact mesh regularity gate, and XF-095 later supplied the actual corrected Xi residual with enough uniform endpoint `C^1` control to pass it. The resulting sampling cost is `O(q^{-2} polylog)`, strictly below the already-vanishing corrected source state. No new external theorem is load-bearing, so `SOURCES.md` does not require a new anchor.

## 7. Boundary for the next pass

The source-side frontier should no longer ask for another generic fixed-strip-to-point-sample theorem for `R_t^sharp`. The next continuum-to-grid calculation should start from the already-sampled vector `(23)` and estimate the **vector-field mismatch** between the corrected continuum Volterra equation and the exact XF-087 trapezoid system, with the XF-092 pole/reference renormalization kept explicit. A useful target is a guarded bound for the pole/reference--residual cross-convolution using `(2)` and `(5)`; the residual is two endpoint degrees softer than the pole, so the available scales leave substantial room.

Separately, even a complete source/grid intertwining theorem would not prove an upper bound on `Lambda`. The remaining destination obligation is unchanged: show that every relevant positive-`Lambda` transition produces a nonvanishing state in the same guarded resource, rather than merely in a weaker local or unweighted statistic.