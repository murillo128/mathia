# XF-092 — frozen pole counterterm controls the full Polymath reference quadrature

**Status:** `EXACT-DERIVED` + `FULL-REFERENCE-QUADRATURE` + `FROZEN-COUNTERTERM` + `BRIDGE-CLOSURE`. XF-091 proves that the pole-plus-log endpoint model of the positive-time Polymath carrier needs no divergent lattice normalization beyond the frozen XF-088 term `(1/4) log Delta delta_0`. It deliberately leaves open whether the lower-order terms of the **full** Polymath reference could create a new guarded continuum-to-grid obstruction.

They do not. The explicit Polymath reference admits an exact positive-frequency decomposition in which, after subtracting

\[
S_t(\xi)=-\frac{1}{4\xi}-\frac{t}{8}\log\xi,
\tag{1}
\]

the remainder \(b_t=\mathcal Z_t^M-S_t\) is continuous at the endpoint and has only the mild derivative singularities

\[
|b_t'(\xi)|\ll 1+|\log\xi|,
\qquad
|b_t''(\xi)|\ll \xi^{-1},
\qquad
0<\xi\le \xi_0,
\tag{2}
\]

uniformly for \(0\le t\le1/2\) on any fixed high line \(3<a<4\).

For this regularity class the old pole counterterm automatically renormalizes the pole--remainder interaction as well. More precisely, if \(E^{M}_{t,m}\) denotes the difference between the full continuum Polymath reference defect and the exact XF-087 discrete reference defect at \(\xi_m=m\Delta\), and \(E^{S}_{t,m}\) is the pole-plus-log discrepancy already estimated in XF-091, then for \(K\Delta\le\xi_0\),

\[
\boxed{
|E^{M}_{t,m}-E^{S}_{t,m}|
\ll_a
\Delta\left(1+\xi_m L_\Delta^2\right),
\qquad
2\le m\le K,
}
\tag{3}
\]

where \(L_\Delta:=1+|\log\Delta|\). Hence, with the XF-086 guarded selector resource,

\[
\boxed{
\mathcal R_{[J,K]}(E^M-E^S)
\ll_a
\frac{\Delta^2K^5}{M^2}
+
\frac{\Delta^4K^7L_\Delta^4}{M^2}.
}
\tag{4}
\]

At the canonical Xi scales \(M=q^2\), \(\Delta\asymp q^{-3/2}\), \(K\asymp q\log\log T\), this is

\[
O_a\!\left(q^{-2}(\log\log T)^5\right)
+
O_a\!\left(q^{-3}(\log\log T)^7L_\Delta^4\right)
=o(1)
\tag{5}
\]

in the same asymptotic regime as XF-088--XF-091.

Thus the deterministic reference side of the source-to-grid bridge is now closed at the level required by the guarded selector: the **full Polymath reference**, not only its pole-plus-log truncation, can be transported to the periodic Volterra lattice with the single frozen counterterm

\[
\boxed{\frac14\log\Delta\,\delta_0.}
\tag{6}
\]

The remaining source bridge is the genuinely Xi-specific quotient residual \(\mathcal R_t=\mathcal Z_t-\mathcal Z_t^M\), not another deterministic endpoint renormalization.

## 1. Exact endpoint structure of the full Polymath carrier

Use the notation of XF-089--XF-090. Fix \(3<a<4\), set

\[
b:=1+a,\qquad
w:=b-ix,\qquad
\ell:=\Log\frac{w}{4\pi},
\tag{7}
\]

and recall

\[
\alpha(s)
=
\frac1{2s}+\frac1{s-1}+\frac12\Log\frac{s}{2\pi},
\qquad
s=\frac w2.
\tag{8}
\]

In the \(w\)-coordinate this is exactly

\[
\alpha
=
\frac12\ell+\frac1w+\frac2{w-2},
\qquad
\alpha'
=
\frac1w-\frac2{w^2}-\frac4{(w-2)^2},
\tag{9}
\]

where the prime is the \(s\)-derivative. Multiplying and taking partial fractions gives the exact identity

\[
\begin{aligned}
\alpha\alpha'
={}&
\frac12\frac{\ell}{w}
-\frac{\ell}{w^2}
-2\frac{\ell}{(w-2)^2}\\
&+\frac1{w-2}
-\frac2{(w-2)^2}
-\frac8{(w-2)^3}
-\frac1w
+\frac3{w^2}
-\frac2{w^3}.
\end{aligned}
\tag{10}
\]

For \(\xi>0\),

\[
\widehat{(c-i\cdot)^{-n}}(\xi)
=
\frac{2\pi}{\Gamma(n)}e^{-c\xi}\xi^{n-1},
\qquad
\Re c>0,
\tag{11}
\]

and differentiation in \(n\) gives, with

\[
C_0:=\gamma+\log(4\pi),\qquad
L(\xi):=\log\xi+C_0,
\tag{12}
\]

the two logarithmic transforms

\[
\widehat{\frac{\ell}{w}}
=
-2\pi e^{-b\xi}L(\xi),
\qquad
\widehat{\frac{\ell}{w^2}}
=
-2\pi e^{-b\xi}\xi\bigl(L(\xi)-1\bigr).
\tag{13}
\]

For the shifted denominator write

\[
\ell
=
\Log\frac{w-2}{4\pi}
+
\Log\left(1+\frac2{w-2}\right).
\tag{14}
\]

Because \(\Re(w-2)=a-1>2\), the second logarithm has an absolutely convergent inverse-power series. After division by \((w-2)^2\), positive-frequency transformation, and multiplication by the carrier factor \(e^{a\xi}\), it becomes an analytic function \(A_a(\xi)=O_a(\xi^2)\). No additional logarithmic endpoint term is hidden there.

The \(t=0\) reference carrier is therefore exactly

\[
\boxed{
\mathcal Z_0^M(\xi)
=
-\frac{e^{-\xi}}{4\xi}
+\frac12e^{-\xi}
+e^\xi.
}
\tag{15}
\]

Using `(10)`--`(14)` in the exact XF-090 identity

\[
\mathcal Z_t^M
=
\mathcal Z_0^M
+
\frac{t}{8\pi}e^{a\xi}\widehat{\alpha\alpha'}
\tag{16}
\]

gives the endpoint expansion

\[
\boxed{
\begin{aligned}
\mathcal Z_t^M(\xi)
={}&
-\frac1{4\xi}
-\frac t8\log\xi
+\left(\frac74-\frac{tC_0}{8}\right)\\
&+\xi\left[
\frac38
+\frac{7t}{8}\bigl(\log\xi+C_0\bigr)
\right]
+O_a\!\left(\xi^2(1+|\log\xi|)\right).
\end{aligned}
}
\tag{17}
\]

The expansion is uniform for \(0\le t\le1/2\). In particular, with \(b_t:=\mathcal Z_t^M-S_t\),

\[
b_t(0)=\frac74-\frac{tC_0}{8},
\tag{18}
\]

and the exact finite combination behind `(17)` gives `(2)`. The only non-smooth remainder direction is \(\xi\log\xi\), one full endpoint degree above the logarithm isolated in XF-091.

## 2. A finite-part trapezoid lemma for a regular remainder

The key point is not specific to the coefficients in `(17)`. Let

\[
F(\xi)=-\frac c\xi+d\log\xi+b(\xi),
\qquad c>0,
\tag{19}
\]

where \(b\) is continuous at zero, \(C^2\) on \((0,\xi_0]\), and

\[
|b'(\xi)|\le B(1+|\log\xi|),
\qquad
|b''(\xi)|\le \frac B\xi.
\tag{20}
\]

Use exactly the XF-091 endpoint representative

\[
\widetilde F_{\Delta,N}
=
-c\tau+d\ell+b
+
\left(\frac{\Delta N}{2}+c\log\Delta\right)\delta_0.
\tag{21}
\]

The singular--singular part is XF-091. It remains to estimate the pole--\(b\), log--\(b\), and \(b\)--\(b\) sectors.

For the pole--\(b\) sector, put \(x=m\Delta\) and

\[
\phi_x(\eta)
:=
\frac{b(x-\eta)-b(x)}{\eta}.
\tag{22}
\]

The Hadamard finite-part identity used in XF-091 gives

\[
(\tau*b)(x)
=
b(x)(\log x+\gamma)
+
\int_0^x\phi_x(\eta)\,d\eta.
\tag{23}
\]

After the already-present \(c\log\Delta\,\delta_0\) contribution is included, the complete renormalized pole--\(b\) bracket is **exactly**

\[
\boxed{
b(x)\bigl(H_{m-1}-\log m-\gamma\bigr)
+
\left[
\Delta\sum_{i=1}^{m-1}\phi_x(i\Delta)
-
\int_0^x\phi_x(\eta)\,d\eta
\right].
}
\tag{24}
\]

There is no naked \(\log\Delta\) left. This is the same cancellation mechanism as XF-091, now against an arbitrary endpoint-regular remainder.

The second derivative assumption makes the Riemann term particularly tame. Since

\[
\phi_x(\eta)
=
-\int_0^1 b'(x-r\eta)\,dr,
\tag{25}
\]

one has

\[
\int_0^x|\phi_x'(\eta)|\,d\eta
\le
\int_0^1
\int_{x(1-r)}^x |b''(y)|\,dy\,dr
\le B.
\tag{26}
\]

Together with \(H_{m-1}-\log m-\gamma=O(m^{-1})\), and the integrable logarithmic growth of \(b'\) on the final mesh cell, `(24)` contributes after multiplication by the Volterra factor \(x\)

\[
O_B\!\left(\Delta+x\Delta(1+|\log x|)\right).
\tag{27}
\]

Thus the old pole counterterm also renormalizes the interaction with \(b\); no \(b(0)\log\Delta\), \(b(0)\log^2\Delta\), or new endpoint delta can appear.

The log--\(b\) sector is an ordinary weakly singular Riemann sum. Splitting off the first endpoint cell and integrating the derivative of
\(\log\eta\,b(x-\eta)\) on \([\Delta,x]\) gives

\[
x\left|
\Delta\sum_{i=1}^{m-1}
\log(i\Delta)b(x-i\Delta)
-
\int_0^x\log\eta\,b(x-\eta)\,d\eta
\right|
\ll_B
x\Delta L_\Delta^2.
\tag{28}
\]

The symmetric cross term obeys the same estimate. Finally, the \(b\)--\(b\) sector has only integrable endpoint derivatives, so

\[
x\left|
\Delta\sum_{i=1}^{m-1}
b(i\Delta)b(x-i\Delta)
-
\int_0^x b(\eta)b(x-\eta)\,d\eta
\right|
\ll_B
x\Delta L_\Delta.
\tag{29}
\]

Combining `(27)`--`(29)` proves the generic bound `(3)` after absorbing the bounded coefficient \(d\). Notice that the time derivative and the linear \(\xi^2F\) term in the continuum and discrete reference defects cancel pointwise; the only mismatch being estimated is the nonlinear Volterra convolution.

## 3. Guarded-resource consequence at the Xi scales

For the full Polymath reference, `(17)`--`(20)` provide a uniform \(B=B(a)\) for \(0\le t\le1/2\). Therefore `(3)` applies to every visible mesh point once \(K\Delta\le\xi_0\).

Use the exact XF-086 selector resource

\[
\mathcal R_{[J,K]}(E)
=
\frac1{4M^2}
\sum_{m=J}^{K}I_m|E_m|^2,
\qquad
I_m\asymp_g m^4.
\tag{30}
\]

Squaring `(3)` and summing gives

\[
\mathcal R_{[J,K]}(E^M-E^S)
\ll_{a,g}
\frac{\Delta^2}{M^2}\sum_{m\le K}m^4
+
\frac{\Delta^4L_\Delta^4}{M^2}\sum_{m\le K}m^6,
\tag{31}
\]

which is `(4)`. Substituting

\[
M=q^2,\qquad
\Delta\asymp q^{-3/2},
\qquad
K\asymp q\log\log T
\tag{32}
\]

gives `(5)`. XF-091 already shows that the singular-sector discrepancy \(E^S\) is \(o(1)\) in the same resource. Hence the **entire deterministic Polymath reference defect** and its XF-087 lattice defect differ by \(o(1)\) on the guarded visible band.

This matters because XF-090 found that the deterministic forcing itself has guarded size \(\asymp(\log q)^4\) on \(m\asymp q\). The present result does not make that forcing small; it shows that continuum and lattice carry the same large deterministic forcing up to \(o(1)\). Large forcing and small consistency error are therefore compatible for the full reference, not merely for its first two endpoint singular terms.

## 4. Falsification controls

**At \(t=0\).** Equation `(15)` is exact. After adding \(1/(4\xi)\), the remainder is analytic at zero, so `(2)` is stronger than needed and `(3)` reduces to ordinary endpoint quadrature plus the XF-088 pole normalization.

**Constant remainder.** If \(b\equiv b_0\), the Riemann term in `(24)` vanishes identically and the entire pole--remainder discrepancy is \(b_0(H_{m-1}-\log m-\gamma)\). After multiplication by \(x=m\Delta\) this is \(O(\Delta)\), exactly matching `(3)` and showing that no hidden \(b_0\log\Delta\) counterterm is missing.

**Worst lower-order cusp.** The term \(\xi\log\xi\) in `(17)` saturates the derivative class `(20)`: its first derivative grows logarithmically and its second derivative is \(1/\xi\). Thus the proof controls the first genuinely non-smooth term omitted by XF-091 rather than assuming an analytic remainder.

**High-line dependence.** The singular coefficients in `(17)` are independent of \(a\). The only \(a\)-dependent piece is the analytic \(A_a(\xi)=O_a(\xi^2)\) generated by `(14)`, so changing the fixed zero-free high line cannot create another endpoint counterterm.

**What is not proved.** Nothing here bounds the Xi/reference quotient residual
\[
\mathcal R_t
=
\mathcal Z_t-\mathcal Z_t^M
=
-\frac{\xi}{2\pi}e^{a\xi}\widehat L_{t,a}
\]
in the guarded norm. XF-089 gives its exact factor of \(\xi\), but boundedness of the physical-space primitive \(L_{t,a}\) alone still does not justify pointwise mesh sampling or a uniform \(X(B)\) estimate. The separate implication from a hypothetical positive \(\Lambda\) transition to nontrivial destination guarded mass also remains open.

## 5. Prior-art boundary and consequence

Euler--Maclaurin and corrected trapezoidal rules for algebraic-logarithmic endpoint singularities, including Hadamard finite-part integrals, are classical. XF-091 already records that neighboring prior-art boundary. The new content here is not a general singular-quadrature theorem: it is the exact decomposition `(10)`--`(17)` of the **specific Polymath high-line reference**, the exact frozen-counterterm cancellation `(24)` in the XF-087 Volterra normalization, and the guarded Xi-scale estimate `(4)`--`(5)`. A targeted prior-art audit found no de Bruijn--Newman result making this full-reference continuum-to-Vieta consistency statement. The only load-bearing external definition remains the Polymath reference already anchored in `research/xi_flow/SOURCES.md`, so no new source entry is required.

The bridge left by XF-090--XF-091 can therefore be sharpened to

\[
\boxed{
\text{full deterministic reference transport is controlled;}
\quad
\text{the remaining source obstruction is the Xi/reference quotient residual.}
}
\tag{33}
\]

In particular, searching for additional deterministic endpoint counterterms is no longer a live direction for this reference. The next load-bearing estimate should target the guarded Fourier norm and sampling stability of \(L_{t,a}\), or an equivalent quotient variable, and only after that the separate positive-\(\Lambda\) coercivity gate.