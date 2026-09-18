# NB-216 — Bounded shell signals price zero-mean and growing-width Mellin escapes

**Date:** 2026-09-18  
**Status:** `EXACT-DERIVED + METHOD-BOUNDARY + FOURIER-DUALITY + ZERO-MEAN + GROWING-SHELL + SOURCE-NORMALIZATION + NB-215-EXTENSION`.

`NB-215` proves a sign-blind global `L^1` reconstruction tariff for every **nonzero-mean** signed fixed-shell profile, while explicitly leaving two representation escapes open: use a zero-mean profile with a different destination-visible signal, or let the logarithmic shell width grow with the carrier scale. Both escapes can be priced by the same Fourier-dual calculation once source normalization is stated as a bounded shell pairing rather than specifically as the mean.

Let `X>0`, let the logarithmic shell be `[0,Delta]` with `Delta>0` allowed to depend on `X`, and let

\[
h\in L^1([0,\Delta];\mathbb C).
\]

After `j>=1` ordinary Mellin primitive transfers define

\[
K_{X,j}(v)
:=
\int_0^\Delta (X+y)^j h(y)e^{ivy}\,dy.
\tag{1}
\]

Let `psi` be any bounded shell reference pattern with

\[
\|\psi\|_\infty\le1,
\qquad
M_\psi(h):=\int_0^\Delta \psi(y)h(y)\,dy\ne0.
\tag{2}
\]

Then, with the convention that the left side is `+infinity` when `K_(X,j)` is not integrable,

\[
\boxed{
\frac{\|K_{X,j}\|_{L^1(\mathbb R)}}{|M_\psi(h)|}
\ge
\frac{2\pi}{I_j(X,\Delta)},
\qquad
I_j(X,\Delta):=
\int_0^\Delta (X+y)^{-j}\,dy.
}
\tag{3}
\]

The bound is uniform over the signs, phases, shape, `X`-dependence and width-dependence of `h`, and over the bounded reference pattern `psi`. Thus replacing the mean by a bounded higher-moment or target-weighted signal does not remove the global absolute Mellin tariff. Widening the shell can dilute the tariff after **one** primitive, but only by paying directly in logarithmic source width; after two or more primitives there remains an irreducible positive power of `X` no matter how far the shell is widened upward.

## 1. A bounded source signal has an exact reciprocal-multiplier dual

Assume first that `K_(X,j) in L^1(R)`; otherwise (3) is automatic. Put

\[
g_{X,j}(y):=(X+y)^j h(y)
\]

on `[0,Delta]` and extend it by zero to the real line. With the Fourier convention in (1), inversion gives almost everywhere

\[
g_{X,j}(y)
=
\frac1{2\pi}
\int_{\mathbb R}K_{X,j}(v)e^{-ivy}\,dv.
\tag{4}
\]

Since

\[
h(y)=\frac{g_{X,j}(y)}{(X+y)^j},
\]

we may insert (4) into the bounded pairing (2) and use Fubini:

\[
M_\psi(h)
=
\frac1{2\pi}
\int_{\mathbb R}
K_{X,j}(v)W_{X,j,\psi}(v)\,dv,
\tag{5}
\]

where

\[
W_{X,j,\psi}(v)
:=
\int_0^\Delta
\frac{\psi(y)}{(X+y)^j}e^{-ivy}\,dy.
\tag{6}
\]

The sole use of source normalization is now

\[
\|W_{X,j,\psi}\|_\infty
\le
\int_0^\Delta (X+y)^{-j}\,dy
=I_j(X,\Delta),
\tag{7}
\]

because `||psi||_infinity<=1`. Therefore

\[
2\pi|M_\psi(h)|
\le
\|K_{X,j}\|_1 I_j(X,\Delta),
\]

which proves (3).

The statement is homogeneous in `h`. It is also invariant under rescaling of the reference signal once `psi` is normalized by its own `L^infinity` norm. Thus a raw moment such as `y^r` does not obtain a free gain from its units: the dimensionless reference `(y/Delta)^r` has norm one and is the correctly normalized bounded source coordinate.

## 2. One primitive has a width tradeoff, while higher primitives saturate

For one primitive,

\[
I_1(X,\Delta)
=
\log\!\left(1+\frac\Delta X\right),
\]

so (3) becomes

\[
\boxed{
\frac{\|K_{X,1}\|_1}{|M_\psi(h)|}
\ge
\frac{2\pi}{\log(1+\Delta/X)}
\ge
2\pi\frac X\Delta.
}
\tag{8}
\]

This extends the global part of `NB-215` from the mean signal to every bounded shell pairing and, crucially, it remains valid when `Delta=Delta_X` grows.

For `j>=2`,

\[
I_j(X,\Delta)
=
\frac{X^{1-j}-(X+\Delta)^{1-j}}{j-1}.
\tag{9}
\]

Hence

\[
\boxed{
\frac{\|K_{X,j}\|_1}{|M_\psi(h)|}
\ge
\frac{2\pi(j-1)X^{j-1}}
{1-(1+\Delta/X)^{1-j}}
\ge
2\pi(j-1)X^{j-1}.
}
\tag{10}
\]

There is also the elementary width-sensitive estimate

\[
I_j(X,\Delta)\le \Delta X^{-j},
\]

which yields

\[
\boxed{
\frac{\|K_{X,j}\|_1}{|M_\psi(h)|}
\ge
2\pi\frac{X^j}{\Delta}.
}
\tag{11}
\]

The qualitative difference between `j=1` and `j>=2` is therefore exact. The reciprocal first reconstruction multiplier `(X+y)^(-1)` has logarithmically divergent mass as the shell is widened indefinitely, so source delocalization can in principle reduce its dual tariff. Every higher reciprocal power is integrable at infinity; widening the shell can no longer erase the residual `X^(j-1)` cost.

## 3. Zero mean and bounded higher moments do not escape the global tariff

Suppose now that

\[
\int_0^\Delta h(y)\,dy=0.
\tag{12}
\]

This is exactly the branch excluded from `NB-215`. If the proposed replacement signal is a nonzero normalized `r`-th shell moment, take

\[
\psi_r(y):=\left(\frac y\Delta\right)^r,
\qquad
M_r(h):=
\int_0^\Delta
\left(\frac y\Delta\right)^r h(y)\,dy,
\tag{13}
\]

for any `r>=1` with `M_r(h) != 0`. Since `||psi_r||_infinity=1`, equations (8)--(11) apply without change. In particular, on a fixed shell,

\[
\boxed{
\frac{\|K_{X,j}\|_1}{|M_r(h)|}
\gg_\Delta X^j.
}
\tag{14}
\]

Nothing in the proof requires `r` to be fixed; only boundedness of the normalized reference pattern matters. More generally, any zero-mean construction whose destination-visible replacement signal is a bounded shell functional falls under (3).

Thus **zero mean by itself does not remove the absolute reconstruction tariff**. It removes the particular barycentric normalization used in `NB-215`, but once a different bounded source signal is named and normalized, the reciprocal reconstruction multiplier supplies the same dual obstruction.

This does not say that every useful zero-mean Nyman observable must be of the form (2). A genuinely distributional signal, a derivative evaluation, or another source functional whose natural norm grows with `X` or `Delta` lies outside the theorem. Such a construction must, however, price that source norm explicitly rather than counting a large unnormalized moment as free information.

## 4. A growing shell must become almost carrier-scale to change the one-primitive growth class

Equation (8) gives an exact locality-versus-reconstruction tradeoff. If a one-primitive architecture aims for normalized global reconstruction cost at most `L_X`, then necessarily

\[
\log\!\left(1+\frac{\Delta_X}{X}\right)
\ge
\frac{2\pi}{L_X},
\]

so

\[
\boxed{
\Delta_X
\ge
X\left(e^{2\pi/L_X}-1\right)
\ge
\frac{2\pi X}{L_X}.
}
\tag{15}
\]

On the Vinogradov--Korobov diagonal used by `NB-212`--`NB-215`,

\[
X=Q^{2/3+o(1)},
\qquad
Q:=\log(10+|t|).
\tag{16}
\]

Therefore a one-primitive reconstruction cost in the subpolynomial class `Q^{o(1)}` requires

\[
\boxed{
\Delta_X
\ge
XQ^{-o(1)}.
}
\tag{17}
\]

A polylogarithmic cost requires at least `Delta_X >= X/(log Q)^O(1)`, while a bounded cost requires `Delta_X >= cX` for some fixed `c>0`. In physical coordinates `n=xe^y`, the latter means that the observable is no longer confined to a fixed multiplicative neighbourhood of `x`: it reaches from `x` to at least

\[
x e^{cX}=x^{1+c}.
\tag{18}
\]

Even the polylogarithmic-width tradeoff spans the enormous multiplicative factor `exp(X/polylog X)`. Thus the only way shell widening can change the first-primitive absolute growth class is by sacrificing the original fixed-shell locality on a nearly carrier-sized logarithmic range.

For `j>=2`, (10) is stronger: no choice of upward width `Delta_X`, even one much larger than `X`, can reduce the global absolute tariff below

\[
X^{j-1}
=
Q^{2(j-1)/3+o(1)}.
\tag{19}
\]

Repeated primitivization therefore has no growing-shell escape within this bounded-signal normalization.

## 5. Representation audit and adversarial boundaries

**Representation audit.** Inequality (3) is generic Fourier-algebra duality. The reconstruction multiplier `(X+y)^j` is inverted on physical support by `(X+y)^(-j)`, and any bounded source coordinate can pair with that inverse only through an `L^1` mass bounded by `I_j(X,Delta)`. The arithmetic content is that ordinary Mellin primitivization of the Euler source produces exactly the multiplier `log(n)^j=(X+y)^j`, while the Vinogradov--Korobov diagonal converts powers of `X` into powers of `Q`.

The distinction at `j=1` is likewise representation-generic: it is the borderline non-integrability of `u^(-1)` at infinity. The fact that this borderline is reached by the specific pair `-zeta'/zeta <-> log zeta` is the arithmetic reason it matters here.

**Prior-art audit.** A targeted search found the expected classical framework of Wiener/Fourier algebras, Fourier inversion and `L^1`--`L^infinity` duality. No external theorem is load-bearing for (3): it is the direct calculation (4)--(7), and no novelty is claimed for the generic harmonic-analysis inequality. The line-local contribution is the source-normalized application to the two explicit escapes left by `NB-215`, together with the exact `j=1` versus `j>=2` width threshold. `SOURCES.md` therefore needs no new anchor.

**Global versus local cost.** The theorem controls the full frequency-line `L^1` norm. A signed profile may still export most of this mass outside the safe central contour. `NB-215` prices that local export for the nonzero-mean signal through source conditioning, but the present bounded-signal extension does not provide the analogous central-neighbourhood tradeoff for every `psi`. A future source-specific construction could exploit that distinction.

**Actual zeta correlation remains outside the bound.** As in `NB-213`--`NB-215`, this is not a lower bound for the true oscillatory integral against `log zeta` or a higher primitive. The analytic function may correlate with `K_(X,j)` far below the global operator norm. Exploiting that correlation before absolute values remains a genuinely different route.

**Only the upward shell geometry is priced.** The support is `[0,Delta]`, so `log n=X+y>=X`. A representation that widens downward toward `y=-X`, where the reconstruction multiplier itself approaches zero, changes the physical scale all the way toward `n=O(1)` and is not covered by the same locality interpretation.

**Destination coupling remains missing.** The theorem does not prove that a near-optimal Nyman approximant realizes any particular shell signal. A destination theorem is still required before this source-side tariff can constrain the actual Nyman distance.

## 6. Research consequence

`NB-215` left “zero mean / higher moment” and “growing shell” as two plausible representation repairs. The present calculation narrows both without invoking additional zeta estimates.

A zero-mean profile does not gain anything at the level of global absolute reconstruction merely by renaming a bounded higher moment as the source signal. An upward-growing shell can dilute the **first** primitive tariff, but to move it into a subpolynomial class the logarithmic width must already be `XQ^(-o(1))`; a bounded tariff requires carrier-scale width `Delta=Omega(X)`. After two or more primitives, widening does not even provide that escape because the reciprocal multiplier becomes integrable.

The live source-side routes are therefore more specific: exploit the actual oscillatory correlation between the zeta primitive and reconstruction kernel before absolute values, obtain a destination-visible source signal whose natural normalization is genuinely outside bounded shell duality, or change the physical support geometry so radically that it should be analyzed as a different observable. None of these is a representation-only consequence of mean cancellation or ordinary shell widening.