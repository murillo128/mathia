# PL-460 — Raw mod-5 prime-window second moments already impose Dirichlet zero-free half-planes

**Evidence/status:** EXACT-DERIVED + CLASSICAL LANDAU-POSITIVITY BRIDGE / NEGATIVE OBSTRUCTION TO AN INDEPENDENT PAIR-COVARIANCE ROUTE.

**Parent findings:** PL-458 (signed pair hypothesis B and raw second moments), PL-459 (independent first-moment zero-free gate), PL-421 (normalized image cone).

## Claim

For each reduced residue \(a\pmod5\), set
\[
P_a(y)=\sum_{\substack{y<n\le y+H\\n\equiv a\ (5)}}\Lambda(n),
\qquad Q_{aa}(X,H)=\int_X^{2X}P_a(y)^2\,dy,
\qquad \psi_a(x)=\sum_{\substack{n\le x\\n\equiv a\ (5)}}\Lambda(n).
\]
Fix \(0<\theta\le1/2\) and \(H=\lfloor X^\theta\rfloor\). Suppose that for **every sufficiently large real \(X\)** and all four channels, uniformly in \(a\),
\[
\boxed{Q_{aa}(X,H)\le \frac{XH^2}{16}
   +O_\theta(XH\log X).}\tag{M_\theta}
\]
Only four *diagonal upper bounds on the uncentered window Gram* are assumed: no first-moment estimate, off-diagonal covariance, Hardy--Littlewood model, character modulation, or signed-source positivity.

Then each channel obeys the one-sided estimate
\[
\boxed{\psi_a(x)-\frac x4
   \le O_\theta(x^{1-\theta}\log x),}\tag{1}
\]
and **every Dirichlet \(L(s,\chi)\) modulo 5 is zero-free in \(\Re s>1-\theta\)**. In particular, \((M_{1/2})\) for all sufficiently large \(X\) **implies joint GRH modulo 5, including RH**. So does \((M_{\theta_j})\) for any sequence of fixed exponents \(\theta_j\uparrow1/2\) (with constants allowed to depend on \(j\)).

For the strict regime \(0<\theta<1/2\), the **second-order pair assumption (B) of PL-458, by itself**, implies \((M_\theta)\) using the unconditional fixed-modulus prime number theorem and PL-458's unconditional triangular singular-series sums. Hence (B), without the separate first-moment assumption (A), already excludes every Dirichlet zero in \(\Re s>1-\theta\) when assumed for all sufficiently large \(X\). With a family of fixed exponents tending to \(1/2\), (B) alone implies joint GRH. This is an implication **from unproved hypotheses**; neither (B), \((M_\theta)\), nor RH is proved here.

## 1. The diagonal pair model supplies precisely the raw-moment gate

PL-458 derives from (B), fixed-modulus PNT, its exact same-residue singular-series sum, and endpoint accounting (for \(\theta<1/2\)) that
\[
Q_{aa}(X,H)
=\frac{XH^2}{16}+\frac{XH}{4}\log(X/H)+o(XH\log X).
\tag{2}
\]
The \(k=0\) atomic term contributes \(XH\log X/4+o(XH\log X)\); the \(k>0\), \(5\mid k\) triangular sum contributes \(XH^2/16-XH\log H/4+O(XH)\). Crucially, obtaining (2) uses **only** PL-458's diagonal \(a=b\) instances of (B); assumption (A) enters later only when deterministically centering the Gram. Since \(\log(X/H)\asymp_\theta\log X\), (2) implies \((M_\theta)\).

The endpoint replacement in PL-458 costs \(O(H^3\log^2 X)\), which is \(o(XH\log X)\) for fixed \(\theta<1/2\), but is not controlled at \(\theta=1/2\). Thus **(B) is not asserted to imply \((M_{1/2})\)**; the square-root-window assertion above is a direct raw-moment sufficient condition.

## 2. Jensen converts an uncentered second-moment ceiling into a one-sided PNT error

Write \(I_a=\int_X^{2X}P_a(y)\,dy\ge0\). Cauchy--Schwarz and \((M_\theta)\) yield
\[
I_a^2\le XQ_{aa}
\le \frac{X^2H^2}{16}+C_\theta X^2H\log X,
\quad\Rightarrow\quad
I_a\le\frac{XH}{4}+O_\theta(X\log X).
\tag{3}
\]
The last step uses \(\sqrt{u^2+v}\le u+v/(2u)\) for \(u>0,v\ge0\). In particular, **(3) is only one-sided and has big-\(O\), not little-\(o\), error**: it does *not* silently rederive PL-458's hypothesis (A).

The exact endpoint identity already established in PL-459 is
\[
I_a
=H\bigl(\psi_a(2X)-\psi_a(X)\bigr)
 +O\bigl(H(H+1)\log(3X)\bigr).
\tag{4}
\]
With \(E_a(x)=\psi_a(x)-x/4\), (3)--(4) imply
\[
E_a(2X)-E_a(X)
\le O_\theta\!\left((X/H+H)\log X\right)
=O_\theta(X^{1-\theta}\log X), \tag{5}
\]
since \(\theta\le1/2\). Iteration over the dyadic scales \(x/2,x/4,\ldots\), with the final bounded scale absorbed into the constant, establishes (1) for **all** large \(x\).

## 3. Why a one-sided error excludes zeros here (Landau's positivity theorem)

A one-sided inequality cannot simply be inserted into PL-459's absolutely convergent Mellin integral for \(E_a\). Instead put \(\sigma=1-\theta\in[1/2,1)\), and choose \(C>0,x_0\) so that the locally integrable function
\[
f_a(x)=C x^\sigma\log x-E_a(x)\ge0
\quad(x\ge x_0).
\tag{6}
\]
Its Mellin transform \(F_a(s)=\int_{x_0}^\infty f_a(x)x^{-s-1}\,dx\) converges initially for \(\Re s>1\). There it is a sum of an elementary pole term and the Dirichlet logarithmic derivatives:
\[
\int_1^\infty E_a(x)x^{-s-1}\,dx
=\frac1{4s}\sum_{\chi\bmod5}\overline{\chi(a)}
 \left(-\frac{L'}{L}(s,\chi)\right)
-\frac1{4(s-1)},\qquad \Re s>1.
\tag{7}
\]
Replacing the lower limit 1 by \(x_0\) changes this by an entire function. The pole at \(s=1\) cancels between the principal-character term and the explicit main term.

Here a small-modulus real-axis fact matters. None of the four \(L(s,\chi)\) modulo 5 vanishes at any **real** \(s\in(0,1)\):
- For the principal character, \(L(s,\chi_0)=(1-5^{-s})\zeta(s)\), while \(\zeta(s)<0\) for real \(0<s<1\) by the positive alternating eta series.
- For the quadratic character with values \((1,-1,-1,1)\) on \(1,2,3,4\), the grouped series is positive: each block
\((5k+1)^{-s}+(5k+4)^{-s}-(5k+2)^{-s}-(5k+3)^{-s}>0\)
by strict convexity of \(u^{-s}\).
- For either order-four character, whose values are \((1,\pm i,\mp i,-1)\), the real part is the strictly positive series
\(\sum_{k\ge0}[(5k+1)^{-s}-(5k+4)^{-s}]>0\).
All grouped series converge for real \(s>0\); standard Dirichlet nonvanishing at \(s=1\) also follows here from the same positive series and the Euler products to its right. Thus the meromorphic expression (7), and hence each \(F_a\), is holomorphic at every **real** \(s>\sigma\).

The classical Landau principle for **nonnegative Mellin/Laplace transforms** says that their real abscissa of convergence, if finite, is a singularity. (The usual nonnegative Dirichlet-series proof works verbatim after \(x=e^u\), by positive Taylor coefficients/monotone convergence.) As \(F_a\) has no real singularity to the right of \(\sigma\), its integral must converge throughout \(\Re s>\sigma\). Since both \(f_a(x)\ge0\) and \(Cx^\sigma\log x\) are integrable against \(x^{-s-1}\) there, so is \(|E_a(x)|\). Therefore the four Mellin transforms of \(E_a\) are holomorphic throughout \(\Re s>\sigma\).

Character orthogonality applied to (7) now recovers each \(-L'/L(s,\chi)\) as a holomorphic function throughout \(\Re s>\sigma\), apart from the expected principal pole at \(s=1\). A zero of an \(L\)-function would produce a nonremovable logarithmic-derivative pole. Thus none exists in this half-plane. At \(\theta=1/2\), the functional equations reflect any off-line zero into \(\Re s>1/2\), yielding joint GRH.

## Prior art, stress tests and consequence

Cauchy--Schwarz/Jensen, positivity of Mellin transforms (Landau), Dirichlet-character orthogonality, logarithmic derivatives and functional equations are classical. Landau's abscissa theorem is stated and proved for nonnegative Dirichlet series in K. Kedlaya, *Notes on Analytic Number Theory*, Chapter 3, Theorem 3.4 (source 121); the Mellin/Dirichlet \(L\)-function bridge is in Montgomery--Vaughan (source 120). The elementary grouped-series nonvanishing check is special to modulus 5. The line-specific delta is the previously unrecorded implication **PL-458(B) -> diagonal uncentered moment ceiling -> one-sided progression errors -> zero-free half-plane**, making the apparently independent *second-order* route GRH-strength even without (A). No independently new theorem about actual primes is claimed.

The signs, quantifiers and logical directions are essential. Replacing **uncentered** \(Q_{aa}\) by an empirically centered variance invalidates (3); a raw moment ceiling with the wrong \(XH^2/16\) coefficient is insufficient. Without all four channels, orthogonality does not exclude every character's zeros. The all-large-real-\(X\) quantifier is required for dyadic summation; sparse-scale estimates do not suffice. The Landau argument depends on real-axis nonvanishing, which is verified here but must not be presumed for arbitrary moduli or Beurling systems. The upper bound is not deduced from existing unconditional sieve-order pair bounds, and GRH alone is not asserted to imply \((M_\theta)\), let alone (B). This is an obstruction to treating PL-458's covariance-scale pair hypothesis as an independent workaround of the classical zero problem, **not a proof of RH or of its zero-free prerequisites**.
