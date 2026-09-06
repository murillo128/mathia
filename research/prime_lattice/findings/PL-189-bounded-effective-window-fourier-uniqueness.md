# PL-189 — Bounded normalized affine phase windows cannot flatten a hard target without already forcing its zero-frequency cancellation

## Claim

`PL-187` proves a universal erasure theorem for the affine Kronecker readout once the **effective phase width** tends to infinity. The remaining bounded-width regime behaves qualitatively differently. On a fixed macroscopic prime band, after the natural affine rescaling the relevant frequencies always lie in a compact interval independent of the shift size. Classical Fourier uniqueness then implies that asymptotic flattening on any fixed positive-length bounded normalized phase window already forces cancellation of the underlying arithmetic coefficients at zero frequency.

Fix constants

\[
0<a<b<\infty,
\]

let `h_X>=1` be arbitrary, and put

\[
\mathcal P_X=\{q\text{ prime}:aX<q\le bX\},
\qquad M_X=|\mathcal P_X|,
\qquad
\rho_X=\frac{h_X}{X+h_X}.
\]

For coefficients `|c_q|<=1`, define the normalized affine readout in the effective phase coordinate `u=t rho_X` by

\[
F_X(u)
:=\frac1{M_X}\sum_{q\in\mathcal P_X}
 c_q\exp\!\left(iu\,\omega_X(q)\right),
\qquad
\omega_X(q)
:=\rho_X^{-1}\log\left(1+\frac{h_X}{q}\right).
\]

Let `I` be any fixed real interval of positive length. More generally, let `I_X` be intervals whose lengths are bounded below by a positive constant and whose centers remain in a fixed bounded set. Then

\[
\boxed{
\int_{I_X}|F_X(u)|^2\,du\longrightarrow0
\quad\Longrightarrow\quad
\frac1{M_X}\sum_{q\in\mathcal P_X}c_q
=F_X(0)\longrightarrow0.
}
\]

The implication is uniform in the choice of `h_X` and coefficients in the following qualitative sense: for fixed `a,b` and a fixed compact family of positive-length observation intervals, every `epsilon>0` has a `delta>0` such that

\[
\|F_X\|_{L^2(I_X)}<\delta
\quad\Longrightarrow\quad
|F_X(0)|<\epsilon.
\]

No arithmetic input is used. The result is a compact-support Fourier-uniqueness obstruction.

For the hard target `c_q=mu(q+h)` with fixed `h>0`, a theorem proving such bounded-normalized-window flattening on every macroscopic band would therefore already imply the folklore shifted-prime Möbius cancellation

\[
\sum_{q\le X\atop q\ \mathrm{prime}}\mu(q+h)=o(\pi(X)).
\]

Thus a bounded positive-width affine phase average at bounded normalized center is **not an easier spectral bypass** around the parity barrier isolated by `PL-186` and `PL-188`. In contrast with the `Delta_X->infinity` regime of `PL-187`, where Fourier/sieve averaging erases every bounded coefficient sequence without learning its arithmetic mean, bounded normalized windows retain enough analytic rigidity that vanishing throughout the window propagates back to zero frequency.

**Evidence/status:** `EXACT-DERIVED + CLASSICAL-FOURIER-UNIQUENESS + NEGATIVE/OBSTRUCTION` for the route

\[
\text{bounded effective affine phase window at bounded center}
+\text{ hard shifted target}
\longrightarrow
\text{an easier cancellation mechanism than the zero-frequency problem}.
\]

The Fourier uniqueness input is classical Paley--Wiener/identity-theorem material and is not claimed as new. The line-specific result is the exact normalization and compact-frequency reduction showing that the bounded-window escape left open by `PL-187` cannot be made universally flat without solving the underlying signed arithmetic mean. This does not cover windows whose normalized centers tend to infinity, isolated pointwise frequencies, shrinking windows, or genuinely joint/nonlocal operators.

## 1. The affine rescaling has uniformly compact frequency diameter

Write

\[
\kappa_X=\frac{h_X}{X}>0,
\qquad x=\frac qX\in(a,b].
\]

Then

\[
\omega_X(q)
=\frac{1+\kappa_X}{\kappa_X}
 \log\left(1+\frac{\kappa_X}{x}\right).
\]

The absolute location of these frequencies can depend on `kappa_X`, but only differences matter for the modulus of the Fourier sum. Since `omega_X` decreases with `q`, its diameter on the band is

\[
D_{a,b}(\kappa)
=\frac{1+\kappa}{\kappa}
 \log\!\left(\frac{1+\kappa/a}{1+\kappa/b}\right).
\]

This extends continuously to the compactified interval `kappa in [0,infinity]`, with endpoint limits

\[
D_{a,b}(0)=\frac1a-\frac1b,
\qquad
D_{a,b}(\infty)=\log\frac ba.
\]

Hence

\[
C_{a,b}:=\sup_{\kappa>0}D_{a,b}(\kappa)<\infty.
\]

Choose the common reference frequency `omega_X(bX)` (or the value at the endpoint of the continuous band) and set

\[
y_{X,q}=\omega_X(q)-\omega_X(bX).
\]

Then

\[
0\le y_{X,q}\le C_{a,b}
\]

uniformly in `X`, `h_X`, and `q`. Factoring out the common phase gives

\[
F_X(u)
=e^{iu\omega_X(bX)}\widehat\nu_X(u),
\]

where

\[
\nu_X
=\frac1{M_X}\sum_{q\in\mathcal P_X}c_q\,\delta_{y_{X,q}}
\]

is a finite complex measure supported in the fixed compact interval `[0,C_{a,b}]` and satisfies

\[
\|\nu_X\|_{TV}\le1.
\]

In particular,

\[
|F_X(u)|=|\widehat\nu_X(u)|,
\qquad
F_X(0)=\widehat\nu_X(0)=\nu_X([0,C_{a,b}]).
\]

This compactification is the load-bearing fact. It uses the same effective phase variable `u=t h/(X+h)` already isolated in `PL-182` and `PL-187`, but unlike the diverging-window estimate it does not invoke prime spacing or a sieve.

## 2. Compactness plus analytic uniqueness propagates window flattening to zero frequency

The unit ball of finite complex measures on `[0,C_{a,b}]` is weak-* compact. Take any subsequence of `nu_X`. Passing to a further subsequence gives

\[
\nu_{X_j}\overset{*}{\rightharpoonup}\nu
\]

for a finite complex measure supported in the same compact interval.

For every real `u`, weak-* convergence gives

\[
\widehat\nu_{X_j}(u)\to\widehat\nu(u).
\]

The transforms are uniformly equicontinuous on the real line because

\[
|\widehat\nu_X(u)-\widehat\nu_X(v)|
\le C_{a,b}|u-v|\,\|\nu_X\|_{TV}
\le C_{a,b}|u-v|.
\]

Therefore convergence is uniform on every fixed compact real interval. If the observation intervals `I_X` have a positive lower length and bounded centers, pass again to a subsequence so their endpoints converge to a nondegenerate interval `I`. The assumption

\[
\int_{I_X}|F_X(u)|^2du\to0
\]

then forces

\[
\widehat\nu(u)=0
\]

throughout `I`.

Because `nu` has compact support, its Fourier--Laplace transform

\[
\widehat\nu(z)=\int e^{izy}\,d\nu(y),
\qquad z\in\mathbb C,
\]

is entire. Vanishing on a real interval therefore implies, by the identity theorem,

\[
\widehat\nu\equiv0.
\]

Uniqueness of the Fourier transform of finite measures gives `nu=0`. In particular,

\[
\nu_{X_j}([0,C_{a,b}])	o0.
\]

Since every subsequence has only the zero measure as a possible limit under the flattening assumption, the full sequence satisfies

\[
F_X(0)=\frac1{M_X}\sum_q c_q\to0.
\]

This proves the implication.

The qualitative `epsilon`--`delta` version follows from the same compactness argument. On the compact family of measures with total variation at most one and with `|nu([0,C])|>=epsilon`, the continuous functional `nu -> ||hat nu||_{L^2(I)}` cannot attain zero, because zero would contradict Fourier uniqueness. Hence it has a strictly positive minimum. No useful explicit modulus is claimed.

## 3. The boundary with `PL-187` is genuine

`PL-187` considers an original time window of length `L_X` and the effective width

\[
\Delta_X=L_X\rho_X
=L_X\frac{h_X}{X+h_X}.
\]

When `Delta_X->infinity`, the affine frequencies are resolved over an ever larger normalized phase interval. A prime-pair upper-bound sieve then proves

\[
\frac1{L_X}\int|F_{X,h,c}(t)|^2dt\to0
\]

for **every** bounded coefficient sequence. That is information erasure: the conclusion can hold even when the zero-frequency coefficient mean is unknown or deliberately nonzero at finite scale.

The present result shows that this phenomenon cannot simply be pushed down to a fixed positive normalized width while keeping the normalized center bounded. The compact frequency support makes the transforms a normal analytic family. If their mass on one nondegenerate bounded interval tends to zero, the limiting transform must vanish identically, and its value at zero vanishes with it.

Thus the two regimes have opposite epistemic meanings:

\[
\Delta_X\to\infty
\quad\text{can create universal flattening by phase resolution,}
\]

whereas

\[
0<\inf\Delta_X\le\sup\Delta_X<\infty
\quad\text{at bounded normalized center cannot flatten without coefficient cancellation.}
\]

This is not a sharp quantitative phase transition theorem for every possible observation law. It is a clean obstruction for the scalar affine Fourier window considered here.

## 4. Application to shifted-prime Möbius parity

Fix `h>0` and take

\[
c_q=\mu(q+h).
\]

Then the zero-frequency value on the macroscopic band is

\[
F_X(0)
=\frac1{M_X}\sum_{aX<q\le bX}\mu(q+h).
\]

Lichtman's theorem records the folklore conjecture

\[
\sum_{q\le X}\mu(q+h)=o(\pi(X))
\]

for each prescribed fixed shift and proves cancellation only after averaging over a growing range of shifts. `PL-186` locates the missing information beyond every subpower coordinate block, and `PL-188` explains why ordinary local-divisor refinement hits the classical sieve parity barrier.

The present theorem gives a complementary harmonic obstruction. Suppose an affine mechanism claimed to bypass that fixed-shift difficulty by proving

\[
\int_I\left|
\frac1{M_X}\sum_{aX<q\le bX}
\mu(q+h)e^{iu\omega_X(q)}
\right|^2du\to0
\]

on a fixed nondegenerate normalized interval `I`. Then the preceding argument immediately yields

\[
\sum_{aX<q\le bX}\mu(q+h)=o(M_X).
\]

If this holds for every fixed `0<a<1` with `b=1`, then

\[
\sum_{q\le X}\mu(q+h)=o(\pi(X)).
\]

Indeed, the omitted primes `q<=aX` contribute at most `pi(aX)`, whose ratio to `pi(X)` tends to `a`; after taking `X->infinity`, let `a->0`.

Therefore bounded-window `L^2` cancellation does not downgrade the arithmetic burden. It is at least strong enough to recover the zero-frequency fixed-shift cancellation that remains open.

## 5. Prior art and novelty audit

The analytic mechanism is classical. Paley--Wiener theory states that the Fourier transform of compactly supported data extends to an entire function of controlled exponential type; for finite measures this also follows directly from differentiating the compact-support integral. The identity theorem and uniqueness of Fourier transforms then give the zero-on-an-interval implication. No novelty is claimed for any of those steps.

Primary classical anchor:

- R. E. A. C. Paley and Norbert Wiener, *Fourier Transforms in the Complex Domain*, American Mathematical Society Colloquium Publications **19** (1934). This is the classical source lineage for compact-support/entire Fourier duality; modern distributional Paley--Wiener theorems strictly generalize the finite-measure case used here.

Target-specific arithmetic anchor:

- Jared Duker Lichtman, “Averages of the Möbius Function on Shifted Primes,” *The Quarterly Journal of Mathematics* **73**(2) (2022), 729--757, DOI `10.1093/qmath/haab054`, arXiv `2009.08969`. The paper states fixed-shift Möbius cancellation along primes as a folklore conjecture and proves it after averaging over shifts under the stated growth condition.

A targeted literature search found the standard compact-support Fourier uniqueness machinery and the shifted-prime Möbius frontier, but no authoritative source treating this exact affine normalization as a distinct theorem. The durable content is therefore best viewed as a **line-specific exact reduction**, not as a new harmonic-analysis theorem: the natural effective-coordinate frequencies of the prime-lattice affine carrier have uniformly bounded diameter, so any bounded-center positive-width flattening theorem necessarily imports the hard zero-frequency cancellation.

## 6. Adversarial boundaries and countercontrols

- **The normalized center must remain bounded.** A window of fixed effective width whose normalized center tends to infinity is not covered. This is essential, not technical: Fourier transforms of compactly supported measures may decay far from the origin while retaining nonzero mass at zero. Translation of the observation window twists the measure and changes which Fourier value is controlled.
- **A shrinking window is not covered.** Vanishing at a single moving phase, or on an interval whose effective width tends to zero, does not invoke analytic uniqueness and may occur by ordinary destructive interference.
- **Pointwise high frequency remains live.** The result does not control a prescribed `u_X->infinity`; `PL-187` also leaves such pointwise values outside its broad-window conclusion.
- **The result is scalar.** A joint operator, matrix-valued target, completed source/target coupling, or phase-dependent coefficient system may contain information not reducible to one Fourier transform `hat nu_X` and must be tested separately.
- **No quantitative Möbius bound is supplied.** The compactness argument gives only a qualitative implication and deliberately avoids pretending that Fourier uniqueness provides an effective arithmetic estimate.
- **No RH implication is obtained.** Fixed-shift Möbius cancellation on shifted primes is a hard parity statement, but this finding supplies no bridge from it to `Re(s)=1/2` or Weil positivity.
- **The common-frequency subtraction is harmless.** It multiplies the readout by a unit-modulus factor and leaves both its modulus and its zero-frequency value unchanged; it cannot erase arithmetic coefficient information.

## Consequence for the research line

The bounded-window escape left after `PL-187` is now narrower. A scalar affine/Kronecker construction cannot hope that averaging over a fixed positive effective-width window at bounded normalized phase will automatically regularize the large-prime Möbius/Liouville tail. Any proof of such flattening would already contain the signed cancellation that `PL-186` and `PL-188` identify as the hard arithmetic input.

The remaining affine possibilities are therefore structurally different: a genuinely pointwise or diverging-center high-frequency observable, a shrinking effective window, a phase-dependent target justified by arithmetic rather than programming, or a joint/nonlocal/completed construction whose decisive matrix element is not just the Fourier transform of one compactly supported coefficient measure. For any proposed bounded-center scalar window, the audit question is immediate:

\[
\boxed{
\text{does the claimed phase-window estimate already imply the zero-frequency arithmetic mean?}
}
\]

If yes, the spectral packaging has not bypassed the parity barrier; it has merely moved the same hard estimate to a positive-width analytic family.