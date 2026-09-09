# XF-151 — infinite root-scale analytic jets force a parabolic complex-reach barrier

**Status:** `EXACT-DERIVED` + `DECISIVE-NEGATIVE/COMPLEX-COLLAR-CONDITIONING` + `MATCHED-CONTROL` + `UNIT-CIRCLE-ADMISSIBLE` + `FULL-FUTURE` + `INFINITE-NORMALIZED-JET` + `OFF-CIRCLE-OBSERVATION`. XF-150 closes the finite full-degree derivative loophole for the maximal-contact pair on the real axis. The exact reflected-binomial frequency law is stronger than that statement: after root-spacing normalization it controls every derivative order, not only orders through the polynomial degree. Entire continuation then transports that infinite-jet bound into a complex collar at the expected exponential-type cost. Consequently a shallow off-circle displacement does not escape the antipodal transition-conditioning barrier. Near the antipode, this certificate trades real support deficit `d_N` against complex reach `h_N` on the parabolic scale `h_N ~ d_N^2/L`.

## Claim

Use the maximal-contact matched pair of XF-141--XF-150,

\[
R_1(x,s),\qquad R_{\lambda_\rho}(x,s),
\tag{1}
\]

with even degree `N>=8`, `n:=N-2`, fixed `rho>0`, and

\[
\Lambda_{\rm per}(E_1)=0,
\qquad
\Lambda_{\rm per}(E_{\lambda_\rho})=-\rho.
\tag{2}
\]

Keep the root-spacing derivative normalization

\[
\mathscr D_N:=\frac{L}{2\pi N}\,\partial_x.
\tag{3}
\]

For every integer `j>=0`, extend the XF-150 binomial moment by

\[
A_{N,j}
:=
2^{-n}\sum_{k=0}^{n}
\binom nk
\left(\frac{N-1-k}{N}\right)^j
=
\mathbb E\left(1-\frac{K_N+1}{N}\right)^j,
\qquad
K_N\sim{\rm Bin}(n,1/2).
\tag{4}
\]

Then the exact Fourier expansion used in XF-150 gives, now without an upper restriction on `j`,

\[
\boxed{
\left|
\mathscr D_N^j
\bigl(R_1-R_{\lambda_\rho}\bigr)(x,s)
\right|
\le
2e^{-(N-1)as}A_{N,j}
}
\tag{5}
\]

for every real `x`, every `s>=0`, and every integer `j>=0`.

Let `Omega_N` be a predetermined real space-time observation set. As in XF-150, put

\[
d_N
:=
\inf_{(x,s)\in\Omega_N}
\operatorname{dist}_{\mathbb T_L}(x,x_{\rm anti}),
\qquad
x_{\rm anti}=L/2\pmod L,
\tag{6}
\]

\[
B_N
:=
\max\!\left\{
\frac12,
\cos\frac{\pi d_N}{L}
\right\},
\qquad
\kappa_N:=-\log B_N.
\tag{7}
\]

If `N kappa_N>=4`, then

\[
\boxed{
\sup_{j\ge0}
\sup_{(x,s)\in\Omega_N}
\left|
\mathscr D_N^j
\bigl(R_1-R_{\lambda_\rho}\bigr)(x,s)
\right|
\le
4\exp\!\left[-\frac{3}{32}(N-2)\kappa_N\right].
}
\tag{8}
\]

Thus the real-axis obstruction of XF-150 survives the complete root-normalized analytic jet.

Now complexify physical position. Since

\[
R_\lambda(z,s)
=
E_\lambda\!\left(-e^{-2\pi iz/L},s\right)
\tag{9}
\]

is a finite exponential polynomial in `z`, it is entire. For `h_N>=0`, define the vertical complex collar above `Omega_N` by

\[
\widetilde\Omega_N(h_N)
:=
\{(x+iy,s):(x,s)\in\Omega_N,\ |y|\le h_N\}.
\tag{10}
\]

Then for every derivative order `q>=0`, Taylor continuation from the real base point gives

\[
\mathscr D_N^q\Delta R(x+iy,s)
=
\sum_{r=0}^{\infty}
\mathscr D_N^{q+r}\Delta R(x,s)
\frac{\bigl(i2\pi Ny/L\bigr)^r}{r!},
\tag{11}
\]

where `Delta R:=R_1-R_{lambda_rho}`. Combining `(8)` and `(11)` yields

\[
\boxed{
\sup_{q\ge0}
\sup_{(z,s)\in\widetilde\Omega_N(h_N)}
\left|
\mathscr D_N^q\Delta R(z,s)
\right|
\le
4\exp\!\left[
-\frac{3}{32}(N-2)\kappa_N
+\frac{2\pi Nh_N}{L}
\right].
}
\tag{12}
\]

Therefore, whenever

\[
\boxed{
\frac{3}{32}(N-2)\kappa_N
-\frac{2\pi Nh_N}{L}
\gg \log N,
}
\tag{13}
\]

the two controls remain superpolynomially indistinguishable even if the observer sees the full future, every root-normalized spatial derivative order, and the whole complex collar, while their transition times differ by the fixed amount `rho`.

More generally, let a sensor bank mix arbitrarily many derivative orders over the collar,

\[
\mathcal S_{r,N}(R)
:=
\sum_{q\ge0}
\int_{\widetilde\Omega_N(h_N)}
\mathscr D_N^qR\,d\mu_{r,q,N},
\qquad
1\le r\le m_N,
\tag{14}
\]

with absolutely summable total variation

\[
W_N
:=
\max_r\sum_{q\ge0}\|\mu_{r,q,N}\|_{\rm TV}<\infty.
\tag{15}
\]

If `m_N` and `W_N` are polynomial in `N`, every Lipschitz transition-time decoder on a class containing the matched pair has condition number at least

\[
\boxed{
K_N
\ge
\frac{\rho}{4\sqrt{m_N}W_N}
\exp\!\left[
\frac{3}{32}(N-2)\kappa_N
-\frac{2\pi Nh_N}{L}
\right].
}
\tag{16}
\]

## Derivation

The only new step needed to pass from the full-degree jet of XF-150 to the infinite jet is to notice that the exact frequency representation had no derivative-order cutoff. In that representation the normalized frequencies are

\[
\frac{N-1-k}{N},\qquad 0\le k\le N-2,
\tag{17}
\]

all strictly between zero and one. Differentiating any number of times therefore multiplies the `k`th Fourier mode by the corresponding power in `(17)`, and triangle inequality gives `(5)` for every `j>=0`. In particular `A_{N,j}` is monotone nonincreasing for all `j`.

For low orders, the real contact estimate from XF-149 remains

\[
|\mathscr D_N^j\Delta R(x,s)|
\le
4e^{-(N-1)as}B(x)^{n-j}
\tag{18}
\]

for `0<=j<=n`. Choose

\[
J_N:=\left\lfloor\frac{\kappa_NN}{2}\right\rfloor.
\tag{19}
\]

When `N kappa_N>=4`, this lies in the low-order regime. For `j<=J_N`, `(18)` gives the aperture suppression. For every `j>=J_N`, including arbitrarily large `j`, monotonicity gives `A_{N,j}<=A_{N,J_N}`, and the XF-150 moment-generating-function estimate gives

\[
A_{N,J_N}
\le
\exp\!\left(-\frac{3nJ_N}{8N}\right)
\le
\exp\!\left(-\frac{3}{32}n\kappa_N\right).
\tag{20}
\]

The low-order term is smaller than the same coarse exponential after the identical bookkeeping used in XF-150. This proves `(8)`.

The complex step is then exact rather than asymptotic. The finite exponential polynomial `(9)` has an everywhere-convergent Taylor series, and each physical derivative costs exactly the inverse root-spacing normalization `2pi N/L`. Summing the Taylor majorant produces

\[
\sum_{r\ge0}\frac{(2\pi N|y|/L)^r}{r!}
=
\exp(2\pi N|y|/L),
\tag{21}
\]

which is precisely the extra term in `(12)`. No zero-free hypothesis and no logarithm are used.

## Geometric consequences and checks

On any fixed proper real aperture, `kappa_N>=kappa>0`. Hence every collar with sufficiently small fixed relative height still leaves an exponential obstruction. For example, any asymptotic choice satisfying

\[
\frac{h_N}{L}
<
\frac{3\kappa}{64\pi}
\tag{22}
\]

by a fixed margin makes the exponent in `(12)` negative of order `N`. Thus merely moving off the unit circle is not a qualitative cure: the complex reach must be large enough to pay the exponential suppression already present on the real support.

A particularly useful scale check is a root-spacing collar,

\[
h_N=O(L/N).
\tag{23}
\]

Its analytic-continuation cost in `(12)` is only `O(1)`. Therefore it does not alter the real-axis superpolynomial barrier whenever `N kappa_N/log N -> infinity`.

Near the antipode, XF-150 gives

\[
\kappa_N
=
\frac{\pi^2}{2}\frac{d_N^2}{L^2}
+O\!\left(\frac{d_N^4}{L^4}\right).
\tag{24}
\]

Substituting in `(12)` shows that the real blind exponent is of order `N d_N^2/L^2`, while imaginary continuation gains at most order `N h_N/L`. The two effects balance on the scale

\[
\boxed{
h_N\asymp \frac{d_N^2}{L}}
\tag{25}
\]

up to constants. This is the parabolic complex-reach law of the finding. It is a necessary escape scale for this certificate, not a sufficiency theorem at the balancing point.

The root normalization in `(3)` is essential. Unnormalized high derivatives carry powers of `N` and are not uniformly small. The statement is therefore about information supplied at the natural mean-root-spacing scale and about sensor families whose normalization does not itself inject superpolynomial gain.

## Prior-art audit

The external audit checked the classical Bernstein/Markov literature for trigonometric polynomials and entire functions of exponential type, together with complex-strip growth estimates. Those results explain the generic facts that finite Fourier sums extend to entire functions of exponential type and that complex displacement can cost an exponential factor proportional to frequency times height. They do not supply the matched-control part of the argument, the reflected-binomial all-order derivative suppression, or the specific antipodal-to-complex tradeoff `(25)`.

No external theorem is load-bearing here: `(5)` is the exact internal Fourier expansion already underlying XF-150, and `(11)` is ordinary Taylor continuation of a finite exponential polynomial. `SOURCES.md` therefore requires no change. The finding does not claim novelty for Bernstein inequalities or exponential-type continuation; the new repository-level statement is the combination of the maximal-contact transition-sharp pair with the infinite normalized jet and the resulting `h_N` versus `d_N` conditioning barrier.

## Relation to the current frontier

MI-011 correctly treats genuinely off-circle observation as a qualitatively different route for exact state identification, but exact injectivity is not the relevant threshold for `Lambda_per`. XF-151 gives a quantitative restriction on that route: an off-circle trace displaced only by one or a few root spacings can remain exponentially or superpolynomially transition-blind on precisely the same matched family.

This does not subsume XF-137, which studies logarithmic jets on a different optimized exterior complex patch, nor does it justify extending the claim to `log R` or to a Gaussian-reference quotient across possible zero seams. It also leaves the source-side question untouched: Xi may obey additional structure that excludes the maximal-contact packet.

## Remaining gap

The target-side question is now whether an observation that reaches the complex scale allowed by `(25)` — or accesses a genuinely different nonlocal complex functional — admits a polynomially conditioned transition decoder. The present argument only says where this adversary stops certifying failure; it does not prove stability beyond that boundary. The alternative remains source-specific: derive a Xi constraint that quantitatively separates the actual source from the XF-141 maximal-contact direction.