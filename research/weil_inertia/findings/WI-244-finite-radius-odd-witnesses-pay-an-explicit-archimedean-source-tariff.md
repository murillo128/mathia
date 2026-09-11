# WI-244 — Finite-radius odd witnesses pay an explicit archimedean source tariff

## Status

- **Evidence:** `EXACT-DERIVED + LITERATURE-BACKED + CLASSICAL-IDENTITY`.
- **Scope:** this is a finite-radius structural constraint on hypothetical odd zero modes of the localized Weil form. It does **not** prove RH and does not improve the current certified simple-critical-zero proportion by itself.
- **Relation to the line:** this sharpens the surviving non-circular direction isolated in `WI-241` and `WI-243`: finite-radius / first-crossing control of the signed von Mangoldt source, rather than global control of the source discrepancy.
- **Novelty boundary:** the digamma expansion, Schur test, and Suzuki/Weil-form decomposition are classical or literature-backed. The exact combination below, including the explicit finite-radius odd-sector reserve and resulting source tariff, was not found in the line-local or external prior-art audit. No priority claim is made.

## Claim

Use the Fourier convention and source decomposition of `WI-241`, so that

\[
Q_W(v)=Q_{\rm mean}(v)-2\Delta(v)
\]

and the mean multiplier is

\[
M(z)=\Re\psi\!\left(\frac14+\frac{i z}{2}\right)-\log\pi+\frac1{z^2+\frac14}.
\]

Then

\[
M(0)=\psi(1/4)-\log\pi+4
=4-\gamma-\frac\pi2-3\log2-\log\pi
\approx -1.3721834192256655.
\]

For every real \(z\),

\[
\boxed{
M(z)-M(0)
=\sum_{n=1}^{\infty}
\frac1{n+1/4}\,
\frac{z^2}{z^2+(2n+1/2)^2}
}
\]

and hence \(M(z)\ge M(0)\), with equality only at \(z=0\). Thus the zero-frequency value used by the slow-dilate obstruction is the **exact spectral floor** of the archimedean mean multiplier.

More strongly, if \(v\) is odd, supported in \([-a,a]\), and \(\|v\|_2=1\), then

\[
\boxed{
Q_{\rm mean}(v)\ge M(0)+A_{\rm odd}(a)
}
\]

where

\[
A_{\rm odd}(a)
:=\sum_{n=1}^{\infty}
\frac{\sqrt{2e^{-(2n+1/2)a}-e^{-2(2n+1/2)a}}}{n+1/4}>0.
\]

Consequently every normalized odd finite-radius zero witness satisfies the explicit source tariff

\[
\boxed{
Q_W(v)=0
\quad\Longrightarrow\quad
\Delta(v)\ge \frac{M(0)+A_{\rm odd}(a)}2.
}
\]

A simpler closed lower bound is

\[
A_{\rm odd}(a)\ge C(a)
:=\sum_{n=1}^{\infty}\frac{e^{-(n+1/4)a}}{n+1/4}
=\int_0^{e^{-a}}\frac{t^{1/4}}{1-t}\,dt
\ge \frac45e^{-5a/4},
\]

so in particular

\[
\boxed{
Q_W(v)=0
\quad\Longrightarrow\quad
\Delta(v)\ge \frac{M(0)}2+\frac12C(a)
\ge \frac{M(0)}2+\frac25e^{-5a/4}.
}
\]

For every finite \(a\), this is strictly stronger than the asymptotic slow-dilate floor \(M(0)/2\). The extra reserve vanishes only as \(a\to\infty\).

## Exact derivation

### 1. The mean multiplier has a positive resolvent decomposition

For \(\Re w>0\), the classical digamma series is

\[
\psi(w)=-\gamma+\sum_{n=0}^{\infty}
\left(\frac1{n+1}-\frac1{n+w}\right).
\]

Put \(a_n=n+1/4\) and \(y=z/2\). Taking real parts gives

\[
\Re\psi(1/4+iy)-\psi(1/4)
=\sum_{n=0}^{\infty}
\frac{y^2}{a_n(a_n^2+y^2)}.
\]

The \(n=0\) term is exactly

\[
\frac{4z^2}{z^2+1/4},
\]

while

\[
\frac1{z^2+1/4}-4
=-\frac{4z^2}{z^2+1/4}.
\]

They cancel identically. For \(n\ge1\),

\[
\frac{y^2}{a_n(a_n^2+y^2)}
=\frac1{n+1/4}\frac{z^2}{z^2+(2n+1/2)^2},
\]

which proves the claimed resolvent expansion. Every summand is nonnegative and is positive for \(z\ne0\).

### 2. Odd finite support forces a quantitative gap above the spectral floor

For \(\alpha>0\), let

\[
K_\alpha(x)=\frac\alpha2 e^{-\alpha|x|}.
\]

Its Fourier transform is

\[
\widehat K_\alpha(z)=\frac{\alpha^2}{\alpha^2+z^2}.
\]

Therefore, for a function supported in \([-a,a]\),

\[
\frac1{2\pi}\int_{\mathbb R}
\frac{z^2}{z^2+\alpha^2}|\widehat v(z)|^2\,dz
=\|v\|_2^2-\langle v,K_\alpha*v\rangle.
\]

If \(v\) is odd, restriction to \((0,a)\) replaces the convolution kernel by the positive symmetric odd-sector kernel

\[
k^-_\alpha(x,y)
=\frac\alpha2\left(
 e^{-\alpha|x-y|}-e^{-\alpha(x+y)}
\right),
\qquad 0<x,y<a.
\]

Its row sum is

\[
R_\alpha(x)
=1-e^{-\alpha x}
-\frac12e^{-\alpha(a-x)}
+\frac12e^{-\alpha(a+x)}.
\]

With \(q=e^{-\alpha a}\), the deficit is

\[
1-R_\alpha(x)
=(1-q/2)e^{-\alpha x}+\frac q2e^{\alpha x}.
\]

The minimizer lies in \([0,a]\), and direct minimization gives

\[
\min_{0\le x\le a}(1-R_\alpha(x))
=\sqrt{2q-q^2}
=\sqrt{2e^{-\alpha a}-e^{-2\alpha a}}
=:\delta_\alpha(a).
\]

Since \(k^-_\alpha\) is a nonnegative symmetric kernel, the Schur test yields

\[
\|K^-_\alpha\|_{2\to2}
\le \sup_xR_\alpha(x)
=1-\delta_\alpha(a).
\]

Hence every odd \(v\) supported in \([-a,a]\) obeys

\[
\frac1{2\pi}\int
\frac{z^2}{z^2+\alpha^2}|\widehat v(z)|^2\,dz
\ge \delta_\alpha(a)\|v\|_2^2.
\]

Applying this termwise to the positive resolvent expansion with \(\alpha_n=2n+1/2\) proves

\[
Q_{\rm mean}(v)
\ge [M(0)+A_{\rm odd}(a)]\|v\|_2^2.
\]

For the simpler bound, \(0<q\le1\) implies

\[
\sqrt{2q-q^2}\ge\sqrt q,
\]

so

\[
A_{\rm odd}(a)
\ge\sum_{n=1}^{\infty}\frac{e^{-(n+1/4)a}}{n+1/4}=C(a).
\]

Expanding \((1-t)^{-1}\) and integrating termwise gives the stated integral representation of \(C(a)\); retaining only its first summand gives \(C(a)\ge(4/5)e^{-5a/4}\).

### 3. The reserve becomes an explicit source requirement

The exact decomposition from `WI-241` is

\[
Q_W(v)=Q_{\rm mean}(v)-2\Delta(v).
\]

Thus a normalized odd finite-radius zero mode satisfies

\[
0=Q_W(v)
\quad\Longrightarrow\quad
\Delta(v)=\frac12Q_{\rm mean}(v)
\ge\frac{M(0)+A_{\rm odd}(a)}2.
\]

No global estimate for the von Mangoldt discrepancy has been inserted. The statement is therefore a one-way **finite-radius necessary condition** on a hypothetical zero witness, rather than the circular global source control excluded by `WI-243`.

## Consequence for the first-crossing program

`WI-243` left finite-radius first-crossing control as the non-circular target after showing that global/subexponential control of the source discrepancy collapses back to RH-level information. The present identity makes that target quantitative.

For an odd first-crossing candidate at radius \(a\), it is enough to prove a directional source upper bound strictly below

\[
\frac{M(0)+A_{\rm odd}(a)}2
\]

on the candidate class. Such a bound would exclude that crossing without requiring a global bound on the signed von Mangoldt discrepancy. The archimedean operator itself contributes the positive reserve \(A_{\rm odd}(a)\); the slow-dilate obstruction sees only its \(a\to\infty\) limit and therefore misses this finite-radius leverage.

This does not yet supply the missing arithmetic upper bound. Its value is to identify the exact tariff that any successful source term must pay at finite radius, and to show that the zero-frequency floor is not saturated by a compactly supported odd witness.

## Novelty and prior-art boundary

- **Literature-backed input:** Suzuki's localized Weil-form/screw-function framework and the mean/source decomposition audited in `WI-241`.
- **Classical input:** the digamma series (see DLMF §5.7), Fourier transform of the exponential kernel, and the Schur test.
- **Exact deduction here:** cancellation of the \(n=0\) digamma resolvent against the rational archimedean term, the resulting positive resolvent expansion of \(M-M(0)\), the explicit odd finite-radius Schur reserve, and its conversion into the source tariff above.
- **Audit result:** repository search and external prior-art search did not locate this combined finite-radius tariff. Nearby line-local work studies source discrepancy, first crossing, or other finite-support convex problems, but not this resolvent/odd-sector coercive estimate. This is recorded as an audit result, not as a claim of priority.

## Falsification and next gate

The derivation is falsified by any error in the exact `WI-241` sign/normalization convention, the digamma cancellation, the odd-sector row-sum calculation, or the Schur normalization. These have been checked algebraically in the present pass.

The next substantive gate is arithmetic rather than spectral: obtain a zeta-specific **upper** bound for \(\Delta(v)\) on normalized odd first-crossing candidates that beats the explicit radius-dependent tariff above for some nontrivial range of \(a\). Merely replacing it by a global estimate is not progress, because `WI-243` identifies that route as RH-equivalent/circular.

## Sources

- M. Suzuki, recent work on Weil's criterion / screw functions and localized Weil forms used by `WI-241`; primary preprint: https://arxiv.org/abs/2606.09096 and journal version: https://link.springer.com/article/10.1007/s11139-025-01238-9
- NIST Digital Library of Mathematical Functions, §5.7, series expansions for the psi/digamma function: https://dlmf.nist.gov/5.7
- `WI-241` and `WI-243` for the exact repository-local source decomposition, normalization, and the global-control barrier.