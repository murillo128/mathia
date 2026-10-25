# VIS-463 — prime-only shell symmetry erases the leading zero-resonance bias

**Evidence/status:** LITERATURE+EXACT-DERIVED + CLASSICAL-SPECIALIZATION + MATCHED-CONTROL OBSTRUCTION + NO-NOVELTY-CLAIM + NON-RH.

## Claim

A prime-only ratio shell has a common-phase symmetry that removes the
entire classical prime-power term from every fixed mixed amplitude
moment sampled at all zeta-zero ordinates. The full Wang prime-power
shell need not have that symmetry. Deleting higher prime powers can
therefore delete a genuine classical lower-order term, even after each
shell is normalized by its own exact supremum. It is not automatically
a matched control at the `1/log T` resolution.

Here is the coefficient-resolved statement. Use the finite strict
near-band shell of [VIS-313](VIS-313-wang-dyadic-ratio-shell-linear-horizon.md)
and its base-prime torus from
[VIS-419](VIS-419-wang-shell-translation-orbit-prime-torus-haar.md):
\[
 F(z)=\sum_a b_a z^a\ne0,\quad S=\|F\|_\infty,\quad
 W=\frac{\sum_a|b_a|}{S},\quad
 \tau(u)=(p^{-iu})_p.
\]
Its arithmetic height is \(Y\), each pair satisfies
\(Y<\max(q,r)\le2Y\), \(1/2<q/r<2\), \(q\ne r\), and
\(q,r\) are prime powers. For fixed offsets and nonnegative integers
\(r_j\) with \(\sum_jr_j=R\ge1\), expand
\[
 P(z)=\prod_j\frac{|F(z\tau(u_j))|^{2r_j}}{S^{2r_j}}
       =\sum_m c_m z^m.
\]
Define its **prime-axis functional**
\[
 \mathcal B(P)=\sum_p\sum_{k\in\mathbb Z\setminus\{0\}}
       c_{ke_p}\frac{\log p}{p^{|k|/2}}.                       \tag{1}
\]
Only finitely many terms occur; for real \(P\) this is real.
Let \(D_T=N(2T)-N(T)\) count all nontrivial zeros with
multiplicity, \(L=\log T\), and \(\kappa_T=T/(2\pi D_T)\).
Uniformly over the shell coefficients and offsets, for fixed \(R\)
and sufficiently large \(T\),
\[
 \boxed{\quad
 \mathbb E_{T<\gamma\le2T}P(\tau(\gamma))
     -\int P\,dm_H
 =-\kappa_T\mathcal B(P)
 +O_R\!\left(W^{2R}\left[L^{-2}+\frac L T
                           +\frac{(2Y)^{2R}}T\right]\right).
 \quad}                                                     \tag{2}
\]
The shell may depend on \(T\), but is frozen over the sampling block.
No RH assumption is used. For a fixed shell and fixed offsets,
\[
 \lim_{T\to\infty}L\left(\mathbb E_\gamma P-\int P\,dm_H\right)
       =-\mathcal B(P).                                     \tag{3}
\]

If \(F\) uses only pairs of primes, then \(\mathcal B(P)=0\)
exactly, for all these moments. For a growing prime-only shell, the
sufficient moment cost in (2) is thus
\[
 W^{2R}\left[L^{-2}+L/T+(2Y)^{2R}/T\right]\longrightarrow0,    \tag{4}
\]
in place of VIS-462's unsubtracted \(L^{-1}\) term. This is a
sufficient fixed-degree calibration, not a claim about every continuous
path statistic from finitely many moments.

## Derivation: isolate axes before taking absolute values

The quantitative character formula (5) of
[VIS-462](VIS-462-zero-ordinate-shell-moments-pay-resonance-and-small-frequency-costs.md)
provides, for \(0<\nu\le L/8\),
\[
 Z_T(\nu)=-\kappa_T\frac{\Lambda(n_x)}{\sqrt x}
       K\!\left(T\log(x/n_x)\right)
 +O\!\left(\nu^2/L^2+e^{\nu/2}L/T+1/(T\nu)\right),          \tag{5}
\]
where \(x=e^\nu\), \(n_x\) is a nearest prime power,
\(K(v)=\int_1^2e^{-ivs}ds\), and negative frequencies are conjugated.
That finding reconstructs the unconditional weighted/unweighted
zero-sum comparison using mirror pairs and zero density. The
\(L^{-2}\) term here retains that comparison error; it is not an
RH substitution.

For each nonconstant mode of \(P\),
\[
 \lambda_m=\sum_p m_p\log p,\quad
 0<|\lambda_m|<2R\log2,\quad
 e^{|\lambda_m|}=A/B,
 \quad A,B\le Q:=(2Y)^{2R},                                 \tag{6}
\]
with reduced positive integers \(A>B\). Unique factorization gives
\[
 A/B=p^k\ (k\ge1)\quad\Longleftrightarrow\quad
 m=\pm ke_p.                                                \tag{7}
\]
On these axes, (5) has \(K(0)=1\) and the term recorded in (1).
Off the axes, \(A/B\ne n_x\). Since \(x\le2^{2R}\) and a power
of two is within \([x,2x]\), \(n_x\le2x\le2^{2R+1}\). Integer
separation and the mean-value inequality for the logarithm give
\[
 |\log(x/n_x)|\ge
   \frac{|x-n_x|}{\max(x,n_x)}\gg_R Q^{-1}.
\]
Also \(|\lambda_m|=\log(A/B)\ge1/A\ge Q^{-1}\).
Hence the off-axis main term in (5) is
\(O_R(Q/(TL))\), using \(|K(v)|\le\min(1,2/|v|)\);
the total off-axis error is
\(O_R(L^{-2}+L/T+Q/T)\). Exact axis modes satisfy the same
remainder bound. Finally \(\sum_m|c_m|\le W^{2R}\), and the
constant character is exactly the Haar expectation. Summing proves
(2). Since \(L\kappa_T\to1\), it also proves (3).

This distinguishes exact resonance subtraction from discarding a
nearest-resonance term uniformly without controlling its distance.
The rational-height bound supplies that missing distance control.

## Common-phase symmetry and a coefficient perturbation bound

For a prime-only pair, \(a=e_p-e_q\), so
\(\sum_pa_p=0\). Thus
\[
 F_0(e^{i\theta}z)=F_0(z).
\]
The same holds after any fixed time offset and for any product of
amplitude powers. If \(P_0=\sum d_mz^m\), circle averaging forces
\(d_m=0\) unless \(\sum_pm_p=0\). A nonzero axis vector
\(ke_p\) never satisfies this condition, proving
\(\mathcal B(P_0)=0\). More generally, a shell whose modes all
have the same total exponent has this amplitude-moment conclusion.

For the full shell, let \(F_0\) be its prime-only subpolynomial,
without changing the retained coefficients, and put
\[
 E=F-F_0,\qquad \epsilon=\|E\|_{\ell^1}/S.
\]
Use the same denominator \(S^{2R}\) when forming \(P_0\).
Expanding a product difference over its \(2R\) factors gives
\[
 \|P-P_0\|_{\ell^1}\le2R\epsilon W^{2R-1}.
\]
Indeed \(F_0\) is a coefficient subset and both its and \(F\)'s
normalized Wiener norms are at most \(W\); offsets preserve these
norms. Since \((\log p)p^{-|k|/2}\le2/e\),
\[
 |\mathcal B(P)|\le\frac{4R}{e}\epsilon W^{2R-1}.             \tag{8}
\]
This is a safe bound, not asserted sharp. It identifies a sufficient
coefficient resource for neglecting higher-power bias. Small counts
of higher prime powers alone do not bound \(\epsilon\), especially
after division by a potentially small shell supremum.

## A full Wang shell where the bias is genuinely present

Take \(Y=x=8\), \(H=1\), with the actual coefficients
\[
 a_q=\frac{\Lambda(q)}{\sqrt q}\min(q/x,x/q),\qquad
 b_{q,r}=a_qa_r\int_0^1 e^{-iu\log(q/r)}du
        =w_{q,r}e^{-i\log(q/r)/2},
\]
where
\(w_{q,r}=a_qa_r\operatorname{sinc}(\log(q/r)/2)>0\) and
\(\operatorname{sinc}(v)=\sin v/v\). At \(z_p=p^{i/2}\),
all coefficients align, so \(S=\sum_{q,r}w_{q,r}\) exactly.
This is a finite example, not the active scaling
\(H\asymp x\log\log x\).

The prime powers at most 16 are
\(2,3,4,5,7,8,9,11,13,16\). Applying the shell and strict-ratio
conditions gives 26 oriented modes, versus six in the prime-only
subpolynomial. The square \(|F|^2/S^2\) has 255 distinct characters,
including its constant; its only nonzero prime-axis characters are
\(\pm e_2\). In particular,
\[
 (16/r)/(8/r)=2,\qquad r\in\{9,11,13\},
\]
uses two admitted shell ratios. Both orientations contribute, giving
\[
 c_{e_2}=\frac{2e^{-i\log2/2}}{S^2}
               \sum_{r\in\{9,11,13\}}w_{16,r}w_{8,r},
\]
and consequently
\[
 \mathcal B(|F|^2/S^2)
  =\frac{4\log2\cos(\log2/2)}{\sqrt2\,S^2}
               \sum_{r\in\{9,11,13\}}w_{16,r}w_{8,r}>0.      \tag{9}
\]
The approximate value is \(0.00148565981691\); the sign follows
from (9), not floating-point evidence. The prime-only normalized
square has 19 characters and exactly zero axis functional. Thus
separate supremum normalization does not repair this control mismatch.

The [paired visualization](../visualizations/prime-power-resonance-projection.md)
shows these exact banks in frequency/total-exponent coordinates and
the continuous restoration \(F_\eta=F_0+\eta E\), \(0\le\eta\le1\).
It depicts an analytic lower-order coefficient, not observed zero data.

## Prior art and mathematical delta

Ford–Zaharescu, *On the distribution of imaginary parts of zeros of the
Riemann zeta function*, J. reine angew. Math. 579 (2005), 145–158,
[§3, Lemmas 1–2](https://arxiv.org/html/math/0405459v2), supply the
uniform Landau formula and zero-density input reconstructed in VIS-462.
Ford–Meng–Zaharescu, *Simultaneous distribution of the fractional parts
of Riemann zeta zeros*, Bull. London Math. Soc. 49 (2017), 1–9,
[Theorem 1 and formula (1.3)](https://www.ford126.web.illinois.edu/wwwpapers/FMZ.pdf),
already identify the multidimensional lower-order correction through
prime-resonant Fourier directions. The axis functional here is that
classical mechanism in base-prime coordinates. Circle averaging and
homogeneous Fourier support are elementary harmonic analysis.

The local addition to VIS-462 is the coefficient-resolved subtraction,
its rational-bank uniform remainder, and the exact distinction between
a prime-only Wang control and the full shell. Equation (9) demonstrates
that the distinction survives the actual coefficient profile and exact
normalization. No new general zero-distribution theorem or external
novelty is claimed; absence of this shell specialization from the
searched literature would not establish novelty.

## Boundaries and audit

All zeros and their multiplicities are essential. Neither critical-line
only nor hypothetical off-line subsamples inherit (2) automatically.
The \(1/L^2\) remainder is an upper bound, not a proved nonzero next
bias or its optimal rate. For \(Y=T^{a+o(1)}\) and
\(W=L^{b+o(1)}\), fixed-degree cost (4) vanishes under
\(2Ra<1\) and \(Rb<1\); boundary equality is uncertified.
Controlling all continuous fixed-radius tests still needs every fixed
moment order, and threshold indicators retain the boundary-mass gate
of VIS-462. No growing degree, shrinking threshold or growing radius
claim is made here.

Symmetry is sufficient, not necessary: other coefficient banks may
cancel (1). A torus translation preserves the support test but can
change the coefficient functional and its sign for a nonsymmetric
shell. Erasing bias by projecting an observable onto common-phase
invariants changes that observable; it is not source cancellation.
No estimate that (8) is negligible at the physical Wang scale has
been proved here. No selector anomaly or RH conclusion follows.

The exact support audit can be reproduced by enumerating the displayed
prime powers, retaining the stated pair inequalities, and grouping
\((q/r)/(s/t)=qt/(rs)\) as reduced fractions. Independent prime-exponent
vector convolution gives the same 255 characters and the same two
resonances. Direct evaluation of the grouped square at 17 deterministic
torus points agrees with the squared polynomial within
\(2.3\times10^{-16}\). The same prime-only exclusion was checked at
\(Y=16,32,64\); the general proof is the circle symmetry. Finite checks
validate the representation, not the asymptotic zero formula.
