# NB-217 — Reciprocal log-support mass prices two-sided Mellin reconstruction

**Date:** 2026-09-19  
**Status:** `EXACT-DERIVED + METHOD-BOUNDARY + FOURIER-DUALITY + TWO-SIDED-SUPPORT + SOURCE-NORMALIZATION + NB-216-EXTENSION`.

`NB-216` prices zero-mean signals and upward-growing Mellin shells but deliberately leaves one geometric escape open: move the source support downward, toward small logarithmic scale where the reconstruction multiplier itself becomes small. That escape has an exact currency. For an arbitrary measurable logarithmic support set, the global absolute cost after `j` ordinary Mellin primitive transfers is bounded below by the reciprocal `u^{-j}` mass of that support. For `j>=2`, any architecture with subpolynomial normalized reconstruction cost must therefore reach logarithmic scales `u=Q^{o(1)}` on the Vinogradov--Korobov diagonal; bounded cost forces support all the way to `u=O(1)`, i.e. physical integers of bounded size. A shell that remains at `u asymp X` retains a polynomial tariff no matter how it is widened or disconnected.

Let `E` be a measurable subset of a finite interval `[A,B] subset (0,infinity)`, let

\[
h\in L^1(E;\mathbb C),
\qquad
j\in\mathbb N,
\qquad j\ge1,
\]

and extend `h` by zero outside `E`. After `j` ordinary Mellin primitive transfers define

\[
K_j(v)
:=
\int_E u^j h(u)e^{ivu}\,du.
\tag{1}
\]

Let `psi` be any measurable source reference pattern on `E` with

\[
\|\psi\|_\infty\le1,
\qquad
M_\psi(h):=\int_E \psi(u)h(u)\,du\ne0.
\tag{2}
\]

Define the reciprocal support mass

\[
J_j(E):=\int_E u^{-j}\,du.
\tag{3}
\]

Then, with the convention that the left side is `+infinity` when `K_j notin L^1(R)`,

\[
\boxed{
\frac{\|K_j\|_{L^1(\mathbb R)}}{|M_\psi(h)|}
\ge
\frac{2\pi}{J_j(E)}.
}
\tag{4}
\]

The bound is insensitive to signs, phases, connectedness of the support, and the shape of `h`. It depends on support geometry only through the reciprocal logarithmic mass `J_j(E)`. In particular, adding remote upward support cannot dilute a higher-primitive tariff once the lower logarithmic edge stays large; the only geometric way to enlarge `J_j(E)` substantially is to allocate support at smaller `u`.

## 1. The exact support currency follows from the same Fourier duality as NB-216

Assume first that `K_j in L^1(R)`; otherwise (4) is automatic. Put

\[
g(u):=u^j h(u)\mathbf 1_E(u).
\]

With the Fourier convention in (1), inversion gives almost everywhere

\[
g(u)
=
\frac1{2\pi}
\int_{\mathbb R}K_j(v)e^{-ivu}\,dv.
\tag{5}
\]

Since `h(u)=u^{-j}g(u)` on `E`, insert (5) into (2). Absolute integrability is supplied by `K_j in L^1` and `J_j(E)<infinity`, so Fubini gives

\[
M_\psi(h)
=
\frac1{2\pi}
\int_{\mathbb R}
K_j(v)W_{j,E,\psi}(v)\,dv,
\tag{6}
\]

where

\[
W_{j,E,\psi}(v)
:=
\int_E \psi(u)u^{-j}e^{-ivu}\,du.
\tag{7}
\]

Because `||psi||_infinity<=1`,

\[
\|W_{j,E,\psi}\|_\infty
\le
\int_E u^{-j}\,du
=J_j(E).
\tag{8}
\]

Therefore

\[
2\pi |M_\psi(h)|
\le
\|K_j\|_1 J_j(E),
\]

which is exactly (4).

This formulation is stronger than replacing the upward interval of `NB-216` by another interval. Gaps in the support do not count for free: only the set on which the source can actually live contributes to `J_j(E)`. Conversely, the theorem does not require positive `h`, a nonzero mean, or a connected shell.

## 2. One primitive depends on logarithmic span; higher primitives depend on the lower edge

If `E subset [A,B]`, then for one primitive

\[
J_1(E)
\le
\int_A^B \frac{du}{u}
=
\log\frac BA.
\]

Hence

\[
\boxed{
\frac{\|K_1\|_1}{|M_\psi(h)|}
\ge
\frac{2\pi}{\log(B/A)}.
}
\tag{9}
\]

Thus a normalized cost at most `L` requires

\[
\boxed{
\frac BA\ge e^{2\pi/L}.
}
\tag{10}
\]

The first primitive can therefore trade reconstruction cost for a genuinely two-sided logarithmic span. If the upper carrier remains `B asymp X`, bounded cost requires the support to reach a fixed fraction below `X`; in physical coordinates `n=e^u`, this means reaching from scale `x=e^X` down to a fixed power `x^c`, `c<1`. More generally, cost `L_X` requires a downward logarithmic displacement at least

\[
B-A
\ge
B\left(1-e^{-2\pi/L_X}\right)
\sim
\frac{2\pi B}{L_X}
\quad (L_X\to\infty).
\tag{11}
\]

For `j>=2`, however,

\[
J_j(E)
\le
\int_A^\infty u^{-j}\,du
=
\frac{A^{1-j}}{j-1}.
\tag{12}
\]

Combining with (4),

\[
\boxed{
\frac{\|K_j\|_1}{|M_\psi(h)|}
\ge
2\pi(j-1)A^{j-1},
\qquad j\ge2.
}
\tag{13}
\]

This is independent of the upper endpoint and of all gaps above `A`. Thus no amount of upward widening can erase the higher-primitive power once the source is bounded away from small logarithmic scales.

Equivalently, if the normalized reconstruction cost is at most `L`, then necessarily

\[
\boxed{
A
\le
\left(\frac{L}{2\pi(j-1)}\right)^{1/(j-1)}.
}
\tag{14}
\]

The exact condition (4) is stronger: a small lower endpoint is only necessary. The support must also carry enough reciprocal mass `J_j(E)>=2\pi/L`; an arbitrarily thin token of support near `A` does not by itself buy the full escape.

## 3. Relative Mellin shells cannot remove the higher-primitive tariff

Suppose an architecture remains logarithmically local in the broad sense

\[
E_X\subset[cX,CX]
\tag{15}
\]

for fixed `0<c<C<infinity`. This permits a shell of width `Theta(X)`, disconnected support, arbitrary signs and arbitrary `X`-dependent profiles. Equation (4) gives

\[
J_j(E_X)
\le
\int_{cX}^{CX}u^{-j}\,du.
\]

For `j=1` this is at most `log(C/c)`, so the first-primitive normalized cost has a positive constant floor. For every fixed `j>=2`,

\[
J_j(E_X)
\ll_{c,C,j}X^{1-j},
\]

and therefore

\[
\boxed{
\frac{\|K_j\|_1}{|M_\psi(h)|}
\gg_{c,C,j}X^{j-1}.
}
\tag{16}
\]

So the higher-primitive obstruction is not a fixed-shell artifact. It survives every support geometry that stays within a fixed multiplicative annulus in the logarithmic variable. To change the growth class, the source must leave `u asymp X` itself.

The upward-shell theorem `NB-216` is recovered by taking `E=[X,X+Delta]`. The present statement identifies the invariant hidden behind that special geometry: not width by itself, but reciprocal log-support mass.

## 4. On the Vinogradov--Korobov diagonal, higher primitives force source globalization

Use the same diagonal scale as `NB-212`--`NB-216`,

\[
X=Q^{2/3+o(1)},
\qquad
Q:=\log(10+|t|).
\tag{17}
\]

Fix `j>=2`. If an architecture aims for normalized global reconstruction cost

\[
L_Q=Q^{o(1)},
\tag{18}
\]

then (14) forces

\[
\boxed{
A_Q=Q^{o(1)}=X^{o(1)}.
}
\tag{19}
\]

In physical arithmetic coordinates `u=log n`, any support confined to integers `n>=N_min` has `A>=log N_min`. Hence

\[
\boxed{
N_{\min}
\le
\exp(Q^{o(1)})
=
\exp(X^{o(1)})
=x^{o(1)},
\qquad x=e^X.
}
\tag{20}
\]

A bounded normalized cost is still more rigid: (14) gives `A=O_j(1)`, so the support must reach integers of bounded size. Thus repeated primitivization can evade the global absolute tariff only by coupling a carrier near `x=e^X` to source scales that are asymptotically tiny relative to every fixed power of `x`.

For `j=1` the conclusion is weaker and exactly reflects the borderline divergence of `u^{-1}`. Bounded cost needs only `B/A>=c>1`; with `B asymp X`, the lower physical scale may remain `x^c` for a fixed `c<1`. A slowly growing cost permits a correspondingly thinner but still carrier-scale logarithmic excursion according to (11). This `j=1` versus `j>=2` dichotomy is therefore not caused by the one-sided support convention of `NB-216`; it is the integrability threshold of the reciprocal primitive multiplier at infinity.

## 5. Representation audit and prior-art boundary

**Representation audit.** Equation (4) is generic Fourier-algebra duality after passing to the logarithmic Mellin coordinate `u=log n`. The invariant is the `L^1` mass of the reciprocal reconstruction multiplier on the actual support. No prime distribution, zeta zero information or Nyman Gram geometry enters the proof.

The arithmetic specialization is the dictionary that makes the invariant relevant: an ordinary Mellin primitive replaces the Euler coefficient by a factor `log(n)^{-1}` in the analytic primitive and therefore requires reconstruction by `log(n)^j=u^j`; physical source scale is `n=e^u`; and the Vinogradov--Korobov contour used in the preceding findings has `X=Q^{2/3+o(1)}`. Those three facts turn the generic support inequality into the source-globalization statements (19)--(20).

A fresh literature audit covered the Nyman--Beurling Mellin/Hardy formulation, generalized/non-compactly-supported Nyman kernels, Mellin Paley--Wiener support theory, and Fourier/Wiener multiplier duality. The neighboring literature confirms that support and coefficient control are genuine issues in generalized Nyman criteria and that Mellin support is naturally Fourier support after logarithmic change of variables. No external theorem is load-bearing for (4), and no novelty is claimed for the generic Fourier inequality itself. The line-local contribution is the exact reciprocal-support currency and its use to close the downward-support exception explicitly left by `NB-216`. No new `SOURCES.md` anchor is required.

## 6. Adversarial boundaries and research consequence

**Global versus local cost.** As in `NB-215`--`NB-216`, (4) controls the full frequency-line `L^1` norm. It does not prove that the corresponding mass lies on the central contour where a zeta primitive is known to be controlled. A source may still export reconstruction mass to frequencies where the analytic factor is larger.

**Oscillatory correlation remains untouched.** The theorem takes absolute values before coupling to the actual zeta primitive. A signed kernel whose oscillations correlate favorably with `log zeta` or a higher primitive can in principle beat the global operator-norm estimate. That route is mathematically distinct from changing support geometry.

**Bounded source normalization is essential.** The signal `M_psi` is normalized by `||psi||_infinity<=1`. Distributional evaluations, derivatives, or other functionals with an `X`-dependent natural norm lie outside the theorem and must price that norm separately.

**A small endpoint alone is not sufficient.** Equation (14) is only a necessary endpoint consequence of the exact currency (4). A disconnected source with negligible measure near small `u` may still have too little `J_j(E)` to lower the cost. The genuinely invariant quantity is reciprocal support mass, not the formal minimum of an enclosing interval.

**Discrete realization is not proved here.** The continuum shell profile is the same representation used in `NB-215`--`NB-216`. The result says what any such source-side representation must pay; it does not prove that an optimal Nyman approximant admits this profile or that a continuum support design can be realized efficiently by the discrete generator family.

**Destination coupling remains missing.** Nothing in (4) turns a low Nyman distance into one of these source signals. A destination theorem is still required before the tariff can constrain the actual best-approximation distance.

The support-geometry branch is nevertheless much narrower than after `NB-216`. For one primitive, changing the growth class requires a logarithmic span quantified by (10)--(11). For every fixed higher primitive, staying anywhere in a relative shell `u asymp X` is impossible if the goal is subpolynomial normalized absolute cost: the source must reach `u=X^{o(1)}`, and bounded cost forces `u=O(1)`. The live source-side escapes are therefore no longer ordinary upward/downward shell tuning. They are actual oscillatory correlation before absolute values, a destination-visible functional outside bounded shell duality, or a genuinely global source architecture coupling the moving carrier to very small arithmetic scales.