# VIS-004 — dyadic midpoint centering breaks Gamma acuteness but keeps the sigma-one threshold

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + NEGATIVE/OBSTRUCTION + WEIL-POSITIVITY-BRIDGE`.

## Claim

Let `H_\infty` and `\Phi` be the canonical Gamma–Schoenberg symbol and Hilbert embedding of `WP-118`:

\[
H_\infty(t)
=\operatorname{Re}\psi\!\left(\frac14+\frac{it}{2}\right)-\psi\!\left(\frac14\right),
\qquad
\Phi(t)(y)=e^{ity}-1,
\]

with

\[
\langle\Phi(s),\Phi(t)\rangle
=H_\infty(s)+H_\infty(t)-H_\infty(s-t).
\]

For `X>1`, put

\[
m_X=\log(\sqrt2 X)
\]

and, for fixed `C>0` and `\sigma>0`, define the midpoint-centered dyadic prime-shell vector

\[
W_{X,\sigma}
:=
\sum_{X<p\le2X}
\frac{\log p}{C p^\sigma}
\bigl(\Phi(\log p)-\Phi(m_X)\bigr).
\tag{1}
\]

Then there is a constant `J_\sigma>0`, depending only on `\sigma` and the fixed Gamma kernel, such that

\[
\boxed{
\|W_{X,\sigma}\|
=
\left(\frac{J_\sigma}{C}+o(1)\right)X^{1-\sigma}
}
\qquad (X\to\infty).
\tag{2}
\]

Consequently, for dyadic shells `X_k=2^k`, the vector series

\[
\sum_{k\ge k_0} W_{2^k,\sigma}
\tag{3}
\]

converges in the Gamma Hilbert space if and only if

\[
\boxed{\sigma>1.}
\tag{4}
\]

This centering is a genuine escape from the **pairwise acuteness** used in `WP-118`: the centered Gram kernel has negative cross terms for points on opposite sides of the shell midpoint. Nevertheless that extra sign freedom is asymptotically too weak to lower the sharp summability boundary below `sigma=1`.

The result excludes only this natural affine shell-centering architecture. It does not exclude nonlinear quotients, wavelet/cohomological cancellations across scales, matrix- or graded-valued couplings, or arithmetic phase/sign structures selected independently of the divergence they are intended to cancel.

## 1. Common midpoint subtraction is exactly a stationary-increment recentering

Write

\[
u_p
:=
\log p-m_X
=
\log\frac{p}{\sqrt2 X}.
\tag{5}
\]

For any real `m,u`,

\[
\Phi(m+u)(y)-\Phi(m)(y)
=e^{imy}(e^{iuy}-1).
\tag{6}
\]

Multiplication by `e^{imy}` is unitary on the Gamma space `L^2(\mathbb R,\nu_\infty)`. Therefore

\[
\boxed{
\langle
\Phi(m_X+u)-\Phi(m_X),
\Phi(m_X+v)-\Phi(m_X)
\rangle
=
G(u,v),
}
\tag{7}
\]

where

\[
G(u,v)
:=
H_\infty(u)+H_\infty(v)-H_\infty(u-v).
\tag{8}
\]

Thus the centered dyadic shell has an exact `X`-independent Gram geometry in the relative coordinate

\[
u\in\left[-\frac{\log2}{2},\frac{\log2}{2}\right].
\]

This recentering truly destroys the raw acute-cone property. Because `H_\infty` is even and analytic at zero with

\[
H_\infty(t)=a_2t^2+O(t^4),
\qquad a_2>0,
\tag{9}
\]

we have

\[
G(\varepsilon,-\varepsilon)
=2H_\infty(\varepsilon)-H_\infty(2\varepsilon)
=-2a_2\varepsilon^2+O(\varepsilon^4)<0
\tag{10}
\]

for all sufficiently small nonzero `\varepsilon`. Hence negative cross-prime Gram terms are genuinely available after midpoint subtraction; the obstruction below is not merely the termwise positivity argument of `WP-118` repeated in new coordinates.

## 2. Prime shells converge to a fixed weighted continuum measure

For a continuous function `f` on `[1,2]`, the prime number theorem in Chebyshev form

\[
\vartheta(x)=\sum_{p\le x}\log p\sim x
\tag{11}
\]

and partial summation give

\[
X^{\sigma-1}
\sum_{X<p\le2X}
\frac{\log p}{p^\sigma}
f\!\left(\frac pX\right)
\longrightarrow
\int_1^2 r^{-\sigma}f(r)\,dr.
\tag{12}
\]

Equivalently, the finite positive measures

\[
\mu_{X,\sigma}
:=
X^{\sigma-1}
\sum_{X<p\le2X}
\frac{\log p}{p^\sigma}\,\delta_{p/X}
\tag{13}
\]

converge weakly on `[1,2]` to

\[
r^{-\sigma}\,dr.
\tag{14}
\]

The centered kernel

\[
\mathcal G(r,s)
:=
G\!\left(
\log\frac r{\sqrt2},
\log\frac s{\sqrt2}
\right)
\tag{15}
\]

is continuous on the compact square `[1,2]^2`. Applying the product weak convergence to (1), (7), and (15) yields

\[
C^2 X^{2\sigma-2}\|W_{X,\sigma}\|^2
\longrightarrow
I_\sigma,
\tag{16}
\]

where

\[
I_\sigma
:=
\int_1^2\!\int_1^2
r^{-\sigma}s^{-\sigma}\mathcal G(r,s)\,dr\,ds.
\tag{17}
\]

Thus (2) follows once `I_\sigma` is shown to be strictly positive, with

\[
J_\sigma:=\sqrt{I_\sigma}.
\tag{18}
\]

## 3. The limiting centered energy is strictly positive

Using the same Gamma Lévy measure `\nu_\infty` as `WP-118`, define

\[
F_\sigma(y)
:=
\int_1^2
r^{-\sigma}
\left(
 e^{iy\log(r/\sqrt2)}-1
\right)dr.
\tag{19}
\]

The Gram representation gives exactly

\[
I_\sigma
=
\int_{\mathbb R}|F_\sigma(y)|^2\,\nu_\infty(dy)
=\|F_\sigma\|_{L^2(\nu_\infty)}^2.
\tag{20}
\]

This norm cannot vanish. Indeed, `F_\sigma` is smooth and

\[
F_\sigma''(0)
=-
\int_1^2
r^{-\sigma}
\log^2\!\left(\frac r{\sqrt2}\right)dr
<0.
\tag{21}
\]

So `F_\sigma` is not the zero function. Since `\nu_\infty` has positive density away from zero, (20) implies

\[
\boxed{I_\sigma>0.}
\tag{22}
\]

Combining (16), (18), and (22) proves the shell asymptotic (2).

## 4. The sharp dyadic summability threshold remains sigma one

Take `X_k=2^k`. From (2),

\[
\|W_{2^k,\sigma}\|
\sim
\frac{J_\sigma}{C}
2^{k(1-\sigma)}.
\tag{23}
\]

If `\sigma<1`, the shell norms grow and therefore the terms of (3) do not tend to zero. If `\sigma=1`, the shell norms tend to the positive constant `J_1/C`, so again the necessary term-to-zero condition for convergence fails.

If `\sigma>1`, (23) gives a geometric bound

\[
\sum_k\|W_{2^k,\sigma}\|<\infty,
\tag{24}
\]

so (3) converges absolutely in the Hilbert space. This proves (4).

The point is structural: midpoint subtraction creates real negative pairwise interactions, but the prime-weighted continuum profile of each dyadic shell remains a nonzero Hilbert vector of scale `X^{1-\sigma}`. The sign changes therefore alter the geometry without altering the exponent controlling shell mass.

## 5. Visual diagnostic

The retained visualization
[Gamma–Schoenberg dyadic midpoint centering](../visualizations/gamma-schoenberg-dyadic-midpoint-centering.md)
compares the raw and centered Gram matrices on a sampled shell `[10^{12},2\cdot10^{12}]`.

The raw normalized Gram is uniformly strongly positive, while the centered matrix develops negative opposite-side quadrants. This is useful as an intuition check that the architecture really does escape raw acuteness before the asymptotic argument closes it. The image is illustrative only; (2)–(4) follow from the exact unitary identity and the prime-number-theorem limit.

## 6. Prior art and novelty assessment

The Hilbert-space relationship between conditionally negative-definite kernels, positive-definite functions, and Euclidean/Hilbert embeddings is classical Schoenberg theory. See I. J. Schoenberg, *Metric Spaces and Positive Definite Functions*, Transactions of the American Mathematical Society 44 (1938), 522–536, DOI `10.1090/S0002-9947-1938-1501980-0`.

The weighted prime-shell limit (12) is an immediate consequence of the classical prime number theorem `\vartheta(x)\sim x` plus partial summation. No novelty is claimed for either ingredient, for stationary-increment recentering, or for the Gamma/digamma representation already established in `WP-118`.

The research contribution is the Mathia-specific no-go consequence obtained by applying those classical ingredients to the most direct affine shell-centering escape left open by `WP-118`: pairwise negative Gram terms become available, yet the sharp `sigma=1` convergence boundary survives unchanged. This is a restriction on one explicit architecture, not a claim that all quotient/compression strategies reduce to it.

## 7. Boundary conditions and failure modes

The midpoint `m_X=\log(\sqrt2X)` is the geometric center of a dyadic shell. Another fixed relative center `m_X=\log(cX)` with `c\in(1,2)` can be analyzed by the same method, but that generalization is not needed for the present claim.

The result concerns positive matched coefficients `(\log p)/(C p^\sigma)` inside each shell. It does not cover a canonically forced prime-dependent sign or phase, a nonlinear coefficient transform, or a cross-shell operation that couples different dyadic scales before the final norm.

Nor does (4) say that centered shells are pairwise orthogonal or that their partial sums cannot exhibit cancellation. The divergence direction uses only the necessary condition that individual shell terms tend to zero. For `\sigma>1`, convergence follows from absolute summability and therefore requires no cross-shell orthogonality.

Finally, the existence of negative centered Gram entries must not be confused with a proof-relevant positivity mechanism. Here those negative entries are exact, but their integrated shell profile remains nonzero. A stronger quotient would have to cancel or project out that continuum profile itself rather than merely subtract one affine reference vector.

## 8. Audit criterion

The claim can be audited without any visualization. Check:

1. the exact unitary identity (6) and therefore the `X`-independent centered kernel (7)–(8);
2. the local negative Gram entry (10), verifying that this is not the raw acute-cone argument in disguise;
3. the weighted PNT limit (12) by Stieltjes/partial summation from `\vartheta(x)\sim x`;
4. the double-integral limit (16) using continuity of `\mathcal G` on `[1,2]^2`;
5. strict positivity (22) from the nonzero second derivative (21);
6. the dyadic term-to-zero and geometric-summability alternatives in (23)–(24).

Any failure of `I_\sigma>0` would invalidate the sharp asymptotic. A construction that alters the relative shell profile before forming the positive norm falls outside this finding rather than serving as a counterexample to it.

## Consequence for the research line

`WP-118` showed that the raw shared Gamma Hilbert geometry is too coherent: all positive-frequency prime vectors reinforce one another and the critical carrier cannot converge. `VIS-004` tests the simplest visually natural response, namely subtracting the geometric-midpoint vector on every dyadic shell. That operation really does introduce negative cross terms, but it does **not** buy any summability exponent.

The visual lesson is therefore sharper than “negative colors appear”: an attractive sign-changing quotient can still preserve the same macroscopic shell obstruction. Future visual searches for a finite–archimedean escape should look for transformations that remove a nonzero continuum shell mode, create arithmetic phases not present in the stationary Gamma geometry, or couple scales in a way that cannot be reduced to independent affine recentering.
