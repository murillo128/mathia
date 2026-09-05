# XF-052 — endpoint carrier has an explicit prime-free singular normal form

**Status:** `CLASSICAL-EXPLICIT-FORMULA` + `EXACT-DERIVED` + `SOURCE-SPECIFIC-BOUNDARY`. XF-048 identifies a fixed prime-free Fourier gap at the endpoint and XF-051 places the infinite Xi zero field in a canonical positive-frequency distribution `\mathcal Z_t`. The remaining endpoint-background question can be made completely explicit.

With the Fourier convention of XF-051, the endpoint carrier satisfies on the open positive half-line

\[
\boxed{
\mathcal Z_0(\xi)
=
B(\xi)
-\frac12\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\,
\delta\!\left(\xi-\frac{\log n}{2}\right),
\qquad \xi>0,
}
\tag{1}
\]

where

\[
\boxed{
B(\xi)
=e^{\xi}+e^{-\xi}
-\frac{e^{-\xi}}{1-e^{-4\xi}}.
}
\tag{2}
\]

Consequently, if

\[
\lambda_2:=\frac{\log2}{2},
\]

then

\[
\boxed{
\mathcal Z_0(\xi)=B(\xi)
\quad\text{for }0<\xi<\lambda_2.
}
\tag{3}
\]

Thus the entire endpoint lower-positive band used by the XF-050 memory probe is deterministic archimedean/polar background: there is no unknown arithmetic fluctuation there. Moreover

\[
\boxed{
B(\xi)
=-\frac1{4\xi}+\frac74+\frac{\xi}{24}+O(\xi^2)
\qquad(\xi\downarrow0).
}
\tag{4}
\]

So after subtracting the universal simple pole `-1/(4\xi)`, the positive-side background extends real-analytically through the endpoint. The unresolved XF-051/XF-050 transport problem is therefore narrower than an arbitrary low-band background/fluctuation decomposition: at `t=0` the only non-smooth positive-side datum is this explicit simple pole, together with the canonical distributional extension at `\xi=0`; arithmetic atoms begin only at the fixed frequency `\lambda_2`.

## 1. Move the endpoint logarithmic derivative into the Euler-product half-plane

Up to a nonzero constant, the endpoint de Bruijn--Newman function is

\[
H_0(z)\propto
\xi\!\left(\frac12+\frac{i z}{2}\right),
\]

where

\[
\xi(s)
=\frac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s).
\tag{5}
\]

Fix `a>1` as in XF-051 and write

\[
Q_a(x,0)
=\frac{H_0'(x+ia)}{H_0(x+ia)}.
\]

Putting

\[
s=\frac12+\frac{i(x+ia)}2,
\qquad
u:=1-s=\frac{1+a}{2}-\frac{i x}{2},
\]

we have `Re nu>1`. The functional equation `\xi(s)=\xi(1-s)` therefore gives

\[
Q_a(x,0)
=-\frac{i}{2}\frac{\xi'}{\xi}(\nu).
\tag{6}
\]

In the absolutely convergent Euler-product half-plane,

\[
\frac{\xi'}{\xi}(\nu)
=
\frac1\nu+\frac1{\nu-1}
-\frac12\log\pi
+\frac12\psi(\nu/2)
-\sum_{n\ge2}\frac{\Lambda(n)}{n^\nu}.
\tag{7}
\]

This representation cleanly separates the two polar factors, the gamma factor, the zero-frequency constant, and the prime-power Dirichlet series.

## 2. Positive-frequency Fourier transform

For `b>0`,

\[
\int_{\mathbb R}\frac{e^{-i\xi x}}{x+i b}\,dx
=-2\pi i\,e^{-b\xi},
\qquad \xi>0.
\tag{8}
\]

Since

\[
-\frac{i}{2}\frac1\nu
=\frac1{x+i(a+1)},
\qquad
-\frac{i}{2}\frac1{\nu-1}
=\frac1{x+i(a-1)},
\]

the two rational pieces of `\widehat Q_a` are

\[
-2\pi i e^{-(a+1)\xi}
-2\pi i e^{-(a-1)\xi}.
\tag{9}
\]

For the digamma term, put `A=(a+1)/4`. On positive frequencies its standard integral representation gives

\[
\psi(A-i x/4)
\longmapsto
-8\pi\,
\frac{e^{-(a+1)\xi}}{1-e^{-4\xi}},
\qquad \xi>0,
\]

so after multiplication by the coefficient `-i/4` in (6)--(7),

\[
\widehat Q_{a,\Gamma}(\xi,0)
=
2\pi i\,
\frac{e^{-(a+1)\xi}}{1-e^{-4\xi}}.
\tag{10}
\]

Terms independent of `x` contribute only at `\xi=0` and are deliberately absent from these open-half-line identities.

Finally,

\[
\frac{i}{2}
\sum_{n\ge2}\Lambda(n)n^{-\nu}
=
\frac{i}{2}
\sum_{n\ge2}
\frac{\Lambda(n)}{n^{(1+a)/2}}
 e^{i x(\log n)/2},
\]

hence

\[
\widehat Q_{a,\mathrm{arith}}(\xi,0)
=
i\pi\sum_{n\ge2}
\frac{\Lambda(n)}{n^{(1+a)/2}}
\delta\!\left(\xi-\frac{\log n}{2}\right).
\tag{11}
\]

XF-051 defines

\[
\mathcal Z_0(\xi)
=\frac{i}{2\pi}e^{a\xi}\widehat Q_a(\xi,0),
\qquad \xi>0.
\tag{12}
\]

Substituting (9)--(11) cancels the auxiliary height `a` exactly and yields (1)--(2). This is also an independent check of the `a`-independence asserted in XF-051.

## 3. Exact prime-free band and endpoint normal form

The arithmetic term in (1) is locally finite and its first possible atom occurs at

\[
\xi=\lambda_2=\frac{\log2}{2}.
\]

Therefore the restriction (3) is exact, not asymptotic and not dependent on RH. Expanding (2) at zero gives

\[
B(\xi)
=-\frac1{4\xi}
+\frac74
+\frac{\xi}{24}
+\frac98\xi^2
+O(\xi^3),
\tag{13}
\]

which proves (4). In particular,

\[
B(\xi)+\frac1{4\xi}
\]

extends analytically from the right through `\xi=0`.

This distinguishes two issues that were bundled together in the endpoint wording of XF-051. The **positive-side singular shape** is no longer unknown: it is exactly a simple pole with coefficient `-1/4` plus an analytic germ. What remains genuinely distributional is the canonical extension through `\xi=0` and its role when the Volterra convolution touches the endpoint. That extension can affect positive frequencies under convolution and therefore cannot be discarded merely because a test is supported away from zero.

## 4. Consistency with the Guinand--Weil selector

The prime coefficient in (1) is fixed by the existing explicit formula, providing a direct normalization check. For a one-sided test whose Fourier support lies at negative frequencies, XF-050 pairs the zero field as

\[
\sum_\rho f(x_\rho)
=
\frac1{2\pi}
\left\langle
\mathcal Z_0(\xi),\widehat f(-\xi)
\right\rangle.
\tag{14}
\]

An atom from (1) contributes

\[
-\frac1{4\pi}
\frac{\Lambda(n)}{\sqrt n}
\widehat f\!\left(-\frac{\log n}{2}\right),
\tag{15}
\]

exactly matching the corresponding half of the Guinand--Weil prime term recorded in XF-048. The two exponentials in `B` reproduce the pole evaluations `f(\pm i)`, while the final term of (2) is the positive-frequency transform of the digamma factor. Thus (1) is not a new explicit formula; it is the existing formula expressed in the canonical XF-051 carrier with all scale factors fixed.

For the XF-050 compact memory probe,

\[
\omega=\Theta(1/\log T),
\qquad
W=\Theta(\log^3T),
\]

its positive-frequency pairing is supported in an interval of width `O(W^{-1})` around `\omega`, wholly inside `(0,\lambda_2)` for large `T`. Hence it pairs only with `B`. The oscillatory factor `e^{iT\xi}` then gives, after any fixed number `N` of integrations by parts,

\[
\left|
\int B(\xi)
W e^{iT\xi}
\chi\!\bigl(W(\xi-\omega)\bigr)\,d\xi
\right|
\ll_N
(\log T)\left(\frac{W}{T}\right)^N
=o(1),
\tag{16}
\]

because on that moving band `B^{(j)}(\xi)=O_j((\log T)^{j+1})`. This recovers the endpoint `o(1)` selector directly from the carrier normal form and shows explicitly that its cancellation is an oscillatory-background effect, not absence of a large pointwise low-frequency density.

## 5. Consequence for the accepted transport clue

The accepted `CLUE-endpoint-selector-heat-transport` asks for a source-faithful split of the shrinking low-positive-frequency band into deterministic background and fluctuation. Equation (1) supplies that split **exactly at the endpoint**. Below `\log2/2`, the fluctuation part is zero; all endpoint uncertainty is concentrated in the zero-frequency extension of the explicit background, while the arithmetic source begins at a fixed spectral distance.

This removes one possible adverse mechanism: there is no source-compatible broadband arithmetic profile already hidden inside `0<\xi<\Theta(1/\log T)` at `t=0`. A successful transport theorem may therefore focus on the evolution of the explicit simple-pole/analytic background and on whether the canonical `\xi=0` extension can feed an order-one contribution into the moving memory band. Conversely, an order-one replenishment mechanism that is claimed to originate from an arbitrary endpoint low-band fluctuation is incompatible with (1).

The fixed prime-frequency gap alone still does **not** prove that arithmetic support remains separated for positive heat time. Establishing such a statement requires a well-posed uniqueness/domain-of-dependence argument for the singular Volterra evolution including its `\xi=0` distributional component; equation (1) does not supply that step.

## 6. Prior-art and novelty boundary

Every analytic ingredient is classical: the functional equation of the completed zeta function, the Euler-product identity `-\zeta'/\zeta=\sum\Lambda(n)n^{-s}`, the digamma integral representation, and the Guinand--Weil explicit formula. Guinand and Weil are already the canonical source anchors for XF-048, and no additional literature dependency is needed here.

A targeted literature search found the standard statement that the Fourier transform of the zero distribution consists of prime-power frequencies plus elementary/polar/gamma terms, but no source was needed to support a claim of novelty and none is made. The Mathia delta is the exact normalization of those classical terms inside the specific collision-safe carrier introduced by XF-051, together with the endpoint consequence (4): the shrinking band is not an unspecified fluctuation sector but an explicit simple-pole background plus an analytic remainder.

## 7. Boundaries and falsification controls

The strongest normalization checks are independent. Changing `a>1` must leave (1) unchanged; the factors cancel exactly in (9)--(12). Pairing the prime atoms with a one-sided test must reproduce the `-1/(4\pi)` Guinand--Weil coefficient; equation (15) does. Expanding (2) at zero must give the zero-density singularity `-1/(4\xi)`; direct Taylor expansion yields (13).

The finding is endpoint-only. It does not prove a positive-time prime-free band, does not prove uniqueness for the singular Volterra initial-value problem, does not show that the `\xi=0` extension is dynamically harmless, and does not imply any new upper bound on the de Bruijn--Newman constant. Those are precisely the remaining falsification gates.

## 8. Consequence for `xi_flow`

XF-048 established that a memory-scale endpoint probe sees no prime-power source. XF-050 made that probe exactly bandlimited and collision-safe in finite systems. XF-051 supplied the canonical infinite positive-frequency carrier but left the low-frequency background abstract. The present result makes that last endpoint datum explicit:

\[
\boxed{
\text{below }\log2/2:\quad
\mathcal Z_0
=-\frac1{4\xi}
+\text{analytic background},
\quad
\text{with no arithmetic fluctuation.}
}
\]

The next useful theorem is therefore not another endpoint selector. It is a quantitative positive-time statement for the singular Volterra boundary: either prove that the canonical zero-frequency extension of this explicit background cannot generate an order-one XF-050 memory coefficient over the required heat interval, or exhibit the exact endpoint-supported mechanism by which it can.