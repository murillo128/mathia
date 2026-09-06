# PL-190 — Shrinking affine phase windows collapse to a pointwise readout and add no Fourier-uniqueness rigidity

## Claim

`PL-189` leaves shrinking normalized phase windows outside its positive-width Fourier-uniqueness obstruction. That regime does not provide a separate averaging escape. On the same macroscopic affine prime band, compact frequency diameter gives a uniform derivative bound, so a shrinking-window average is asymptotically just the value at the window center.

Fix `0<a<b<infinity`, let

\[
\mathcal P_X=\{q\text{ prime}:aX<q\le bX\},\qquad M_X=|\mathcal P_X|,
\]

let `h_X>=1`, put

\[
\rho_X=\frac{h_X}{X+h_X},
\qquad
\omega_X(q)=\rho_X^{-1}\log\left(1+\frac{h_X}{q}\right),
\]

and for arbitrary coefficients `|c_q|<=1` define

\[
F_X(u)=\frac1{M_X}\sum_{q\in\mathcal P_X}c_q e^{iu\omega_X(q)}.
\]

As in `PL-189`, subtracting the common endpoint frequency gives

\[
F_X(u)=e^{iu\omega_X(bX)}\widehat\nu_X(u),
\qquad
\nu_X=\frac1{M_X}\sum_{q\in\mathcal P_X}c_q\,\delta_{y_{X,q}},
\]

where

\[
y_{X,q}=\omega_X(q)-\omega_X(bX),\qquad
0\le y_{X,q}\le C_{a,b},\qquad
\|\nu_X\|_{TV}\le1
\]

with `C_{a,b}` independent of `X`, `h_X`, and the coefficients.

Let `I_X=[u_X-delta_X/2,u_X+delta_X/2]` with `delta_X->0`. Then two exact consequences hold uniformly in the center `u_X`:

\[
\boxed{
\int_{I_X}|F_X(u)|^2\,du\le\delta_X\longrightarrow0,
}
\]

so **unnormalized** shrinking-window `L^2` flattening is automatic for every bounded target; and

\[
\boxed{
\left|
\frac1{\delta_X}\int_{I_X}|F_X(u)|^2\,du
-|F_X(u_X)|^2
\right|
\le \frac{C_{a,b}}2\,\delta_X.
}
\]

Thus the only nonvacuous normalization satisfies

\[
\frac1{\delta_X}\int_{I_X}|F_X(u)|^2du\to0
\quad\Longleftrightarrow\quad
F_X(u_X)\to0.
\]

A shrinking phase window therefore contributes **no analytic-uniqueness gain over one point**. In particular it cannot interpolate between the universal broad-window erasure of `PL-187` and the positive-width rigidity of `PL-189`.

There is also an exact matched control showing that even a normalized shrinking window can flatten while the zero-frequency coefficient mean stays bounded away from zero. Hence no coefficient-blind implication from shrinking-window flattening to arithmetic cancellation is possible.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL-FOURIER/BERNSTEIN-BOUND + DECISIVE-NEGATIVE` for the route

\[
\text{shrinking affine phase window}
+\text{ bounded target}
\longrightarrow
\text{an averaging rigidity stronger than a pointwise readout}.
\]

The derivative estimate is elementary Fourier--Stieltjes calculus and lies inside classical Bernstein/Paley--Wiener theory. No novelty is claimed for that harmonic-analysis fact. The durable line-specific content is that the exact affine normalization from `PL-182`, `PL-187`, and `PL-189` has uniformly bounded frequency diameter, so the shrinking-window branch collapses quantitatively to the isolated-point branch at every window center, including centers tending to infinity.

## 1. Compact affine frequency diameter gives a center-uniform derivative bound

From `PL-189`, after removing the common phase, all frequencies lie in `[0,C_{a,b}]`. Put

\[
G_X(u)=|F_X(u)|^2=|\widehat\nu_X(u)|^2.
\]

Differentiating the finite Fourier--Stieltjes transform gives

\[
\widehat\nu_X'(u)
=i\int y e^{iuy}\,d\nu_X(y),
\]

so

\[
|\widehat\nu_X'(u)|
\le C_{a,b}\|\nu_X\|_{TV}
\le C_{a,b}
\]

for every real `u`. Since `|\widehat\nu_X(u)|<=1`,

\[
|G_X'(u)|
=2\left|\operatorname{Re}\left(
\widehat\nu_X'(u)\overline{\widehat\nu_X(u)}
\right)\right|
\le2C_{a,b}.
\]

This is uniform in the window center. No bounded-center compactness is needed because only local variation of the modulus is being controlled.

For `u in I_X`,

\[
|G_X(u)-G_X(u_X)|
\le2C_{a,b}|u-u_X|.
\]

Averaging over the centered interval and using

\[
\frac1{\delta_X}\int_{-\delta_X/2}^{\delta_X/2}|v|\,dv
=\frac{\delta_X}{4}
\]

gives

\[
\left|
\frac1{\delta_X}\int_{I_X}G_X(u)du-G_X(u_X)
\right|
\le\frac{C_{a,b}}2\delta_X.
\]

This proves the normalized-window formula. The unnormalized estimate is even simpler: `|F_X|<=1`, hence the integral is at most the interval length.

The distinction in normalization is load-bearing. Without division by `delta_X`, every shrinking interval appears to flatten for the purely measure-theoretic reason that its Lebesgue measure tends to zero. With division by `delta_X`, the statistic is not a new averaged observable: it converges to the pointwise modulus at the moving center.

## 2. A prime-supported matched control separates pointwise cancellation from the zero-frequency mean

The pointwise reduction alone does not yet show that a single phase value is logically independent of the arithmetic mean. This can be checked inside the same prime-supported affine model without changing the frequency geometry.

Take for definiteness `h_X=X`, so `kappa_X=h_X/X=1`. After subtracting the endpoint frequency, write

\[
y_{X,q}
=Y_1(q/X),
\qquad
Y_1(x)=2\log\left(
\frac{1+1/x}{1+1/b}
\right).
\]

Fix any real `u_0!=0` and set

\[
A_X=\frac1{M_X}\sum_{q\in\mathcal P_X}e^{iu_0y_{X,q}}.
\]

Now choose the admissible bounded coefficients

\[
\boxed{
 c_{q,X}=\frac12\left(1-A_Xe^{-iu_0y_{X,q}}\right).
}
\]

Because `|A_X|<=1`, these satisfy `|c_{q,X}|<=1`. At the chosen phase,

\[
\frac1{M_X}\sum_q c_{q,X}e^{iu_0y_{X,q}}
=\frac12(A_X-A_X)=0,
\]

so

\[
F_X(u_0)=0
\]

exactly for every `X` (the removed common phase is irrelevant to the zero).

But the zero-frequency mean is

\[
\frac1{M_X}\sum_q c_{q,X}
=\frac12\left(1-|A_X|^2\right).
\]

The prime number theorem on the fixed band gives

\[
A_X\longrightarrow
A(u_0)
=\frac1{b-a}\int_a^b e^{iu_0Y_1(x)}dx.
\]

Since `Y_1` is continuous and nonconstant, `e^{iu_0Y_1(x)}` is not almost everywhere constant for `u_0!=0`. Equality in the triangle inequality is therefore impossible, and

\[
|A(u_0)|<1.
\]

Consequently

\[
\boxed{
\frac1{M_X}\sum_q c_{q,X}
\longrightarrow
\frac12\left(1-|A(u_0)|^2\right)>0,
}
\]

while the pointwise phase readout is identically zero. If `delta_X->0` and `I_X` is centered at `u_0`, the derivative estimate from Section 1 then also gives

\[
\frac1{\delta_X}\int_{I_X}|F_X(u)|^2du
=O_{a,b}(\delta_X)\to0
\]

with the same nonvanishing coefficient mean.

This control is deliberately programmable and is **not** proposed as arithmetic evidence. Its role is adversarial: it proves that the ambient affine Fourier geometry cannot turn a shrinking-window zero into zero-frequency cancellation. Any such implication for a fixed arithmetic target must come from additional target-specific arithmetic structure.

## 3. Relation to the two neighboring window regimes

`PL-187` and `PL-189` now give three sharply different width behaviors in the effective coordinate `u=t h/(X+h)`.

For diverging effective width, `PL-187` proves that normalized mean square tends to zero for every bounded coefficient sequence by a prime-pair sieve. The statistic loses the target before any arithmetic cancellation has been learned.

For width bounded below by a positive constant and bounded center, `PL-189` proves the opposite rigidity: flattening on the interval forces the entire signed macroscopic coefficient measure to vanish weak-*. A genuine interval invokes analytic uniqueness of the compactly supported Fourier transform.

For shrinking width, the present calculation shows that neither mechanism survives. The unnormalized integral is vacuous, while the normalized integral becomes one point. There is no nondegenerate interval on which the limiting entire transform is forced to vanish, and therefore no identity-theorem propagation back to zero frequency.

This closes `shrinking normalized windows` as a **separate averaging mechanism** in the frontier left by `PL-189`. It does not close the pointwise problem to which they reduce.

## 4. Prior-art and novelty audit

The harmonic-analysis input is classical. Fourier transforms of compactly supported finite measures are entire functions of exponential type, and differentiating under the finite measure immediately bounds the derivative by the support radius times total variation. This is the finite-measure special case underlying the classical Paley--Wiener/Bernstein theory already audited and anchored in `PL-189` by Paley and Wiener, *Fourier Transforms in the Complex Domain* (1934).

A targeted literature search found standard Bernstein inequalities for entire functions of exponential type and the usual Fourier--Stieltjes/characteristic-function regularity, but no reason to treat the displayed shrinking-window estimate as a new harmonic-analysis theorem. The exact estimate here is simpler than the general Bernstein inequality because the representing measure is explicit and has uniformly bounded support.

No novelty is claimed for the prime number theorem used in the matched control. Its only purpose is to certify that the explicit finite prime-supported coefficient construction has a nonzero limiting zero-frequency mean. The line-specific contribution is the regime classification: after `PL-189` establishes compact affine frequency diameter, the supposedly surviving shrinking-window branch is mathematically equivalent to the isolated-point branch rather than an intermediate spectral averaging regime.

## 5. Adversarial boundaries

- **This does not solve a target-specific pointwise estimate.** For `c_q=mu(q+h)` or `lambda(q+h)`, proving `F_X(u_X)->0` at a prescribed moving phase may still be arithmetically hard. The result says only that shrinking-window averaging contributes no additional generic mechanism.
- **At center zero the pointwise problem is exactly the coefficient mean.** A normalized shrinking interval around `u_X=0` is therefore just a smoothed restatement of the original cancellation problem.
- **Moving centers are fully covered by the reduction.** The derivative bound is independent of `u_X`, so centers tending to infinity do not restore averaging rigidity when the width tends to zero. What remains is the corresponding moving pointwise readout.
- **Positive-width windows with centers escaping to infinity remain outside `PL-189`.** Their width does not shrink, so the present local derivative argument does not reduce their average to a single point. They remain a distinct possible observation regime.
- **Phase-dependent targets are not covered.** If the coefficients themselves vary across the observation window, the object is no longer one Fourier--Stieltjes transform of a fixed measure. Such dependence must be derived from arithmetic structure rather than programmed to evade the control.
- **The matched control is a falsification control, not a candidate mechanism.** Its `X`-dependent coefficients intentionally demonstrate flexibility of the ambient representation. It makes no statement that the Möbius or Liouville target behaves similarly.
- **No analytic continuation or RH input occurs.** Everything is finite Fourier analysis plus the ordinary prime number theorem in the control example. The result cannot select `Re(s)=1/2` by itself.

## Consequence

The scalar affine-frequency frontier can be narrowed once more. Shrinking normalized phase windows need not be investigated as a third averaging scale between `PL-187` and `PL-189`: after dephasing, uniform compact frequency diameter makes them quantitatively identical to an isolated pointwise readout.

Accordingly, any surviving affine mechanism must now obtain its arithmetic content from a genuinely pointwise phase theorem, from a positive-width window whose normalized center escapes to infinity, or from a joint/nonlocal/completed construction that changes the one-measure Fourier geometry before observation. Merely shrinking the phase window does not preserve extra prime-lattice information or create a new route around the parity barrier.