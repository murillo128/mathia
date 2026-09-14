# PF-337 — critical translations expose the frequency-off-diagonal mass of the normalized pant insertion

**Status:** `EXACT-DERIVED + FOURIER-COMMUTATOR + NECESSARY-LOCALITY-TEST + ARITHMETIC-SUBSEQUENCE-SHARPENING`.

PF-336 removes the last generic operator-theoretic envelope from the completed-packet translation branch. For the normalized low-side pant insertion

\[
K_n=Q_{L,n}^{-1/2}\Lambda_{LL,n}Q_{L,n}^{-1/2}\ge0,
\]

it is enough, for transport of the completed polar rotation, to prove

\[
\sup_{t\in I_n}\|[K_n,\tau_t]\|_{\mathcal S_2}=o(1)
\tag{1}
\]

on a PF-328 critical interval `I_n`. The remaining question is therefore geometric/PDE rather than functional-calculus. There is, however, an exact Fourier calibration of (1) that makes its content substantially more concrete.

On any fixed physical-low cuff/parity component on which the seam operator and the translations are diagonal, write

\[
e_{n,k}(s)=\ell_n^{-1/2}e^{2\pi i k s/\ell_n},
\qquad
\xi_{n,k}=\frac{2\pi k}{\ell_n},
\qquad
\tau_t e_{n,k}=e^{-i\xi_{n,k}t}e_{n,k}.
\]

For the corresponding compression of `K_n`, with matrix entries `K_{n;jk}`, one has exactly

\[
\boxed{
\|[K_n,\tau_t]\|_{\mathcal S_2}^2
=
\sum_{j,k}
4\sin^2\!\left(\frac{(\xi_{n,j}-\xi_{n,k})t}{2}\right)
|K_{n;jk}|^2.
}
\tag{2}
\]

Let

\[
I_n=[a_n,b_n],
\qquad
\Delta_n=b_n-a_n,
\qquad
c_n=\frac{a_n+b_n}{2}.
\]

Averaging (2) over the whole critical packet interval gives the exact positive identity

\[
\boxed{
\frac1{\Delta_n}\int_{I_n}
\|[K_n,\tau_t]\|_{\mathcal S_2}^2dt
=
\sum_{j,k}
W_n(\xi_{n,j}-\xi_{n,k})|K_{n;jk}|^2,
}
\tag{3}
\]

where

\[
\boxed{
W_n(\delta)
=2\left[
1-\cos(\delta c_n)
\operatorname{sinc}\!\left(\frac{\delta\Delta_n}{2}\right)
\right],
\qquad
\operatorname{sinc}x=\frac{\sin x}{x}.
}
\tag{4}
\]

PF-328 proves

\[
\Delta_n\longrightarrow
\Delta:=\log(\lambda_1/\lambda_0)>0.
\tag{5}
\]

Consequently, for every fixed physical frequency separation `delta_0>0`, there is `c(delta_0,kappa,lambda_0,lambda_1)>0` such that, for all sufficiently large `n`,

\[
W_n(\delta)\ge c
\qquad
\text{whenever}
\qquad
\delta_0\le|\delta|\le2\kappa+o(1).
\tag{6}
\]

Thus the PF-336 translation gate has the necessary consequence

\[
\boxed{
\sum_{|\xi_{n,j}-\xi_{n,k}|\ge\delta_0}
|K_{n;jk}|^2=o(1)
\qquad
\text{for every fixed }\delta_0>0.
}
\tag{7}
\]

The normalized pant insertion must therefore become Hilbert--Schmidt concentrated arbitrarily close to the **physical-frequency diagonal**. A persistent amount of normalized pant mass coupling two fixed-separated physical-frequency regions immediately falsifies the translation route, without analyzing the nonlinear completion or its polar factor.

PF-324 sharpens the test on the arithmetic finite-boundary subsequence. Along the source-realized subsequence `r_n=h_{n+1}/h_n\to0`, every fixed `lambda` has

\[
\frac{\ell_n}{2}-\tau_{n,\lambda}
\longrightarrow\log(1/\lambda).
\]

Hence the center of the PF-328 interval satisfies

\[
c_n=\frac{\ell_n}{2}+O(1).
\tag{8}
\]

For a fixed nonzero Fourier offset `m`, put

\[
\delta_{m,n}=\frac{2\pi m}{\ell_n}.
\]

Then

\[
\delta_{m,n}c_n\to\pi m,
\qquad
\frac{\delta_{m,n}\Delta_n}{2}\to0,
\]

and therefore

\[
\boxed{
W_n(\delta_{m,n})
\longrightarrow
2\bigl(1-(-1)^m\bigr).
}
\tag{9}
\]

In particular every fixed **odd** Fourier offset has limiting weight `4`. Equation (1) would force

\[
\boxed{
\sum_{k:\,k,k+m\ \mathrm{retained}}
|K_{n;k+m,k}|^2=o(1)
\qquad
\text{for every fixed odd }m
}
\tag{10}
\]

along the `r_n\to0` subsequence. The nearest-neighbor Fourier diagonal `m=1` is therefore a minimal concrete falsification target for the actual normalized one-cusp-pant DtN insertion.

This does not prove that the `m=1` band survives, nor that the full translation gate fails. It converts a broad quasilocality request into positive weighted matrix mass with two explicit ways to kill the route: a fixed physical-frequency off-diagonal tail as in (7), or already one fixed odd Fourier diagonal on the finite-boundary arithmetic subsequence as in (10).

## 1. Exact commutator identity

Let `D_t` be the diagonal matrix of `tau_t` in the physical Fourier basis,

\[
(D_t)_{kk}=e^{-i\xi_{n,k}t}.
\]

Then

\[
([K_n,D_t])_{jk}
=
K_{n;jk}
\left(e^{-i\xi_{n,k}t}-e^{-i\xi_{n,j}t}\right).
\]

Taking the Hilbert--Schmidt norm and using

\[
|e^{-ix}-e^{-iy}|^2
=4\sin^2\!\left(\frac{x-y}{2}\right)
\]

proves (2). No positivity of `K_n` is required for this identity; positivity is part of the actual PF-336 application.

If the complete low block contains a fixed finite number of cuff/face-parity components, compress to any component whose projection commutes with the translation. Its Hilbert--Schmidt commutator is bounded by the full one, so every lower-bound test below remains valid componentwise.

## 2. Averaging over the positive-length critical family

For `delta=xi_{n,j}-xi_{n,k}`,

\[
\frac1{\Delta_n}\int_{a_n}^{b_n}
\left(2-2\cos(\delta t)\right)dt
=2\left[
1-\cos(\delta c_n)
\operatorname{sinc}\!\left(\frac{\delta\Delta_n}{2}\right)
\right].
\]

Termwise integration of the finite Hilbert--Schmidt sum gives (3)--(4).

Now fix `delta_0>0`. Because `Delta_n\to Delta>0`, for large `n` the arguments `|delta|Delta_n/2` with `|delta|>=delta_0` stay a positive distance from zero. Since

\[
|\operatorname{sinc}x|<1
\qquad(x\ne0),
\]

compactness of the fixed physical band gives a constant `rho<1` for which

\[
\left|\operatorname{sinc}\!\left(\frac{\delta\Delta_n}{2}\right)\right|
\le\rho
\]

throughout `delta_0<=|delta|<=2kappa+o(1)`. Therefore

\[
W_n(\delta)
\ge2(1-\rho)>0,
\]

which proves (6). If (1) holds, the left side of (3) is `o(1)`, and positivity of every term then gives (7).

This necessary condition is stronger than merely saying that `K_n` is approximately translation invariant in some weak sense. It says that, on the retained physical band, every fixed nonzero frequency separation must lose its total Hilbert--Schmidt mass.

## 3. Finite-boundary arithmetic turns critical translation into a half-cuff parity test

Take the PF-324 subsequence `r_n\to0`. For each endpoint `lambda_i` of the PF-328 interval,

\[
\frac{\ell_n}{2}-\tau_{n,\lambda_i}
=\log(1/\lambda_i)+o(1).
\]

Averaging the two endpoint identities gives (8). For fixed integer `m`,

\[
\delta_{m,n}c_n
=\frac{2\pi m}{\ell_n}
\left(\frac{\ell_n}{2}+O(1)\right)
=\pi m+o(1),
\]

while (5) gives `delta_{m,n}Delta_n/2\to0`. Substitution into (4) proves (9).

For odd `m`, choose `n` large enough that `W_n(delta_{m,n})>=2`, say. Keeping only the nonnegative terms with `j-k=m` in (3) gives

\[
2\sum_k|K_{n;k+m,k}|^2
\le
\frac1{\Delta_n}\int_{I_n}
\|[K_n,\tau_t]\|_{\mathcal S_2}^2dt.
\]

Thus (1) implies (10).

The even-offset limit in (9) is zero. This is not a defect in the calculation: on the finite-boundary subsequence the critical translations are asymptotically half-cuff translations, so fixed even Fourier offsets are asymptotically resonant. The odd-band test is therefore a genuine structural calibration of what this particular packet-transport gate can and cannot see.

## Prior-art and novelty audit

Equations (2)--(4) are elementary Fourier diagonalization and the definition of the Hilbert--Schmidt norm. Commutators with diagonal unitary groups and Fourier/Parseval expansions are standard harmonic-analysis tools; no novelty is claimed for that abstract identity. A targeted literature search found only the expected general Hilbert--Schmidt/unitary-commutator framework and no theorem needed as an imported dependency here.

The project-specific content is the specialization to the PF-328 positive-length critical translation interval together with PF-324's arithmetic seam-location asymptotics. Those two inputs turn PF-336's abstract `S_2` commutator gate into the fixed physical-frequency condition (7) and, on the finite-boundary prime-gap subsequence, the odd Fourier-diagonal condition (10). The derivation is self-contained from current Prime-Flute findings, so `SOURCES.md` needs no new entry.

## Boundaries and adversarial checks

1. **Necessary, not sufficient.** Conditions (7) and (10) follow from the PF-336 translation gate; neither one alone implies the full uniform-in-`t` commutator estimate.
2. **No pant matrix lower bound is proved.** The finding does not show that any fixed-separated frequency tail or odd Fourier diagonal of the actual `K_n` has positive limsup.
3. **Even fixed offsets are invisible in the finite-boundary half-cuff limit.** Their weight tends to zero in (9); they cannot be used as a fixed-offset falsification test without additional translations or estimates.
4. **The fixed physical-frequency test remains valid in every arithmetic regime.** Equation (7) uses only the positive limiting length of `I_n`, not the location of its center.
5. **Translation compatibility still does not imply packet concentration.** Even if (1) is proved and PF-336 transfers it to the polar rotation, one localized completed reference profile or a stronger cutoff/off-diagonal estimate is still required by PF-331/PF-336.
6. **Finite sections are the exact level.** Infinite-boundary passage still needs the compatible limiting control already required by PF-329--PF-336.
7. **No direct-angle endpoint, scattering/determinant theorem, zeta-zero correspondence, critical-line result, or RH implication is proved.**

## Consequence for the research line

The next obstruction-side PDE calculation need not start with the nonlinear completed square root. Work directly with the normalized shear-deleted pant insertion `K_n` in the physical Fourier basis. The cheapest falsification test is now explicit: on the PF-324 finite-boundary subsequence, determine the Hilbert--Schmidt mass of the first odd Fourier diagonal

\[
\sum_k|K_{n;k+1,k}|^2.
\]

A positive lower limsup rules out the PF-336 translation-transport route immediately. Independently, any persistent Hilbert--Schmidt mass coupling physical frequencies separated by a fixed `delta_0>0` rules it out in every arithmetic regime. If these tests vanish, broaden the estimate toward the full weighted identity (3) rather than returning to generic square-root/polar perturbation theory.