---
id: WP-294
title: Weil-square exactness forces Möbius relocalization even without coefficientwise matching
branch: weil_positivity
status: supported
kind: cone-exact-relocalization-rigidity
claim_strength: exact route-closure theorem showing that scalar arithmetic convolution cannot be only approximately localized coefficientwise while still reproducing the exact finite Weil quadratic form on the full autocorrelation cone
created: 2026-09-14
related: [WP-288, WP-292, WP-293]
prior_art:
  - André Weil, Sur les formules explicites de la théorie des nombres premiers (1952)
  - Enrico Bombieri, Remarks on Weil's quadratic functional in the theory of prime numbers. I (2000)
  - Jacques Dixmier and Paul Malliavin, Factorisations de fonctions et de vecteurs indéfiniment différentiables (1978)
  - classical identity 1 * Lambda = log and Möbius inversion
---

# WP-294 — Weil-square exactness forces Möbius relocalization even without coefficientwise matching

## Claim

`WP-292` gives an unconditional source-native smoothing of the critical Mangoldt carrier,

\[
\omega
:=\sum_{N\ge2}\frac{\log N}{\sqrt N}\,\delta_{\log N},
\]

and `WP-293` proves that **exact coefficientwise** recovery of

\[
\mu_\Lambda
:=\sum_{N\ge2}\frac{\Lambda(N)}{\sqrt N}\,\delta_{\log N}
\]

by a scalar arithmetic convolution kernel is uniquely Möbius inversion. That leaves a narrower loophole: perhaps the recovered coefficients need only be approximate or coarse, because the final target is not the carrier itself but the Weil quadratic form on autocorrelation squares.

That loophole is closed for direct one-channel scalar convolution.

Let `a` be a real arithmetic function and put

\[
\eta_a
:=\sum_{d\ge1}\frac{a(d)}{\sqrt d}\,\delta_{\log d},
\qquad
\tau_a:=\eta_a*\omega.
\tag{1}
\]

Then

\[
\tau_a
=\sum_{N\ge2}\frac{(a*L)(N)}{\sqrt N}\,\delta_{\log N},
\qquad L(N)=\log N.
\tag{2}
\]

Hermitianize the one-sided carriers by reflection,

\[
\Sigma_a:=\tau_a+\widetilde{\tau_a},
\qquad
\Sigma_\Lambda:=\mu_\Lambda+\widetilde{\mu_\Lambda},
\tag{3}
\]

where reflection sends `delta_x` to `delta_{-x}`. For

\[
V=C_c^\infty(\mathbb R;\mathbb C),
\qquad
\widetilde f(x)=\overline{f(-x)},
\]

assume only the **cone-level exactness**

\[
\boxed{
\Sigma_a(f*\widetilde f)
=
\Sigma_\Lambda(f*\widetilde f)
\qquad\text{for every }f\in V.
}
\tag{4}
\]

No coefficientwise equality, positivity, temperedness, or zero information is assumed. Nevertheless,

\[
\boxed{a=\mu_{\rm Mob}.}
\tag{5}
\]

Thus there is no scalar source-native arithmetic convolution whose output is only *approximately* Mangoldt-localized while remaining **exactly indistinguishable from the Mangoldt finite term on the full Weil autocorrelation cone**. Exactness of the target quadratic form upgrades automatically to exactness of the underlying symmetrized distribution, which then upgrades to coefficientwise Mangoldt recovery, and `WP-293` forces Möbius inversion.

A finite-place-clean global completion does not reopen the escape. If a candidate adds a remainder whose difference from the target archimedean/global remainder is smooth in a neighborhood of every nonzero log-integer point, then exact equality of the **total** quadratic forms again forces every atomic arithmetic coefficient in (2) to equal `Lambda(N)`. The only way for a global remainder to conceal a coefficient error is for that remainder itself to carry compensating delta masses at the same finite log-integer locations. Such a construction has not avoided arithmetic relocalization; it has moved it into another channel, whose source selection must then be justified independently.

This is a route closure, not a positivity theorem and not a new harmonic-analysis theorem. It combines the cone-separation mechanism of `WP-288` with the arithmetic uniqueness of `WP-293` to close the specific approximate/coarse scalar-relocalization loophole left open after those findings.

**Classification:** `EXACT-DERIVED + FULL-WEIL-AUTOCORRELATION-CONE + TRIVIAL-CONE-ANNIHILATOR + DIXMIER-MALLIAVIN-FACTORISATION + SOURCE-NATIVE-ARITHMETIC-CONVOLUTION + UNIQUE-MOBIUS-RELOCALIZATION + APPROXIMATE-COEFFICIENT-ESCAPE-CLOSED-FOR-EXACT-TARGET + FINITE-PLACE-CLEAN-COMPLETION-RIGIDITY + NO-POSITIVITY-ASSUMPTION + ROUTE-CLOSURE + NOT-A-WEIL-POSITIVITY-PROOF`.

## 1. The scalar smoothing/recovery class is locally well defined without growth assumptions

For every arithmetic function `a`, the convolution in (1) is coefficientwise locally finite on the logarithmic integer lattice. At `log N`,

\[
\begin{aligned}
\tau_a(\{\log N\})
&=\sum_{d\mid N}
\frac{a(d)}{\sqrt d}
\frac{\log(N/d)}{\sqrt{N/d}}\\
&=\frac{(a*L)(N)}{\sqrt N}.
\end{aligned}
\tag{6}
\]

Hence `tau_a`, `Sigma_a`, and their differences with the Mangoldt carriers are distributions in `D'(R)` regardless of whether they are tempered. Every compact interval contains only finitely many points `log N`, so no global summability hypothesis is needed for the argument below.

This is important because the surviving loophole after `WP-293` was precisely a possible change of functional category. A proposed coarse relocalization cannot evade the present theorem merely by making its carrier too large for `S'(R)`: equation (4) is tested in the compactly supported Weil test algebra, where the locally finite atomic distributions are already legitimate.

## 2. Autocorrelation squares have trivial annihilator among distributions

Set

\[
D:=\Sigma_a-\Sigma_\Lambda.
\tag{7}
\]

Assumption (4) is exactly

\[
D(f*\widetilde f)=0
\qquad(f\in V).
\tag{8}
\]

Define the sesquilinear form

\[
B_D(f,h):=D(f*\widetilde h).
\tag{9}
\]

The diagonal of this form vanishes. This already forces the whole form to vanish; positivity and Hermitian symmetry are not needed. Indeed,

\[
0=B_D(f+h,f+h)-B_D(f-h,f-h)
=2B_D(f,h)+2B_D(h,f),
\tag{10}
\]

while

\[
0=B_D(f+ih,f+ih)-B_D(f-ih,f-ih)
=2i\bigl(B_D(h,f)-B_D(f,h)\bigr).
\tag{11}
\]

Equations (10)--(11) imply

\[
B_D(f,h)=0
\qquad(f,h\in V).
\tag{12}
\]

Therefore `D` annihilates every mixed convolution `f*widetilde h`.

Now apply the Dixmier--Malliavin factorization theorem to the Lie group `(R,+)`: every test function `phi in C_c^infty(R)` is a finite sum

\[
\phi=\sum_{j=1}^m u_j*v_j,
\qquad
u_j,v_j\in C_c^\infty(\mathbb R).
\tag{13}
\]

For each `v_j`, take `h_j=widetilde{v_j}`. Then `u_j*v_j=u_j*widetilde{h_j}`, so (12) gives

\[
D(\phi)=0
\qquad(\phi\in C_c^\infty(\mathbb R)).
\tag{14}
\]

Hence

\[
\boxed{\Sigma_a=\Sigma_\Lambda\quad\text{in }D'(\mathbb R).}
\tag{15}
\]

This is the exact point at which an apparently weaker requirement — agreement only on the Weil square cone — becomes ordinary distributional equality. It is the same factorization principle used in `WP-288`, now applied adversarially to the arithmetic recovery error rather than to an abstract candidate positive form.

## 3. Symmetrized distributional equality forces coefficientwise equality

Both one-sided carriers in (2) are supported in `(0,infinity)`, while their reflections are supported in `(-infinity,0)`. There is no atom at zero because `L(1)=Lambda(1)=0`. Restricting (15) to the positive half-line therefore gives

\[
\boxed{\tau_a=\mu_\Lambda.}
\tag{16}
\]

Since the positive log-integer atoms are individually isolated, equality of the distributions is equivalent to equality of every coefficient:

\[
(a*L)(N)=\Lambda(N)
\qquad(N\ge1).
\tag{17}
\]

The attempted distinction between exact target matching and only approximate/coarse coefficient localization has disappeared. A nonzero error at even one integer `N` produces a nonzero atomic distribution and therefore changes the quadratic form for some compactly supported autocorrelation test.

This does **not** say that a numerically small coefficient error must be easily detected by a fixed finite test panel. It is an exact statement about the full canonical test class. Finite-window or approximate numerical criteria remain a different problem.

## 4. Arithmetic uniqueness then forces Möbius inversion

`WP-293` proves that the Dirichlet-convolution equation

\[
a*L=\Lambda
\tag{18}
\]

has the unique solution

\[
\boxed{a=\mu_{\rm Mob}.}
\tag{19}
\]

The proof there uses only that the Dirichlet-convolution ring of arithmetic functions has no zero divisors together with the classical identities

\[
\mathbf 1*\Lambda=L,
\qquad
\mu_{\rm Mob}*L=\Lambda.
\tag{20}
\]

Combining (17) with that uniqueness gives (5). Consequently the unique cone-exact scalar recovery kernel has the familiar transform

\[
\sum_{n\ge1}\frac{\mu_{\rm Mob}(n)}{n^{s+1/2}}
=\frac1{\zeta(s+1/2)}
\tag{21}
\]

on its initial convergence half-plane. The reciprocal-zeta divisor therefore returns even if one never demanded coefficientwise recovery at the start. Demanding the exact Weil finite quadratic form already demanded it implicitly.

In particular, the escape cannot be repaired by choosing a different smoother-looking signed kernel, a positive kernel with small coefficient error, or a kernel whose error is supposed to be invisible after autocorrelation. The full square cone has no such invisible scalar-convolution error.

## 5. Finite-place-clean global completions cannot hide the error in the archimedean sector

The previous sections compare the finite arithmetic carriers directly. A possible objection is that a genuine Weil candidate is global: perhaps `tau_a` can be wrong at individual prime-power locations while an archimedean/global term corrects the **total** quadratic form.

There is a precise boundary for that escape. Let `A` be the candidate non-finite remainder and `A_W` the target archimedean/global remainder. Suppose

\[
(\Sigma_a+A)(f*\widetilde f)
=(\Sigma_\Lambda+A_W)(f*\widetilde f)
\qquad(f\in V).
\tag{22}
\]

The same argument as in Section 2 gives full distributional equality

\[
\Sigma_a-\Sigma_\Lambda=A_W-A.
\tag{23}
\]

Assume only that `A_W-A` is smooth in a neighborhood of every point `plus_or_minus log N`, `N>=2`. The left side of (23) is a locally finite pure atomic distribution on those points. A nonzero multiple of `delta_x` cannot equal a smooth distribution in any neighborhood of `x`. Hence every atomic coefficient on the left must vanish, and again

\[
\Sigma_a=\Sigma_\Lambda,
\qquad a=\mu_{\rm Mob}.
\tag{24}
\]

This condition is deliberately weaker than specifying a particular Gamma kernel or polar normalization. It says only that an object advertised as the archimedean/global remainder does not itself introduce delta masses at the finite log-integer locations. Under that minimal finite-place-clean separation, it cannot compensate coarse arithmetic relocalization.

A construction can evade (24) algebraically by allowing `A` to contain exactly the missing atoms. But then those atoms are finite-prime data regardless of which channel carries them. Their coefficients and source law must be derived independently. Relabeling a compensating prime-power comb as an archimedean or boundary counterterm does not supply the missing geometric explanation.

## 6. Aggressive falsification and exact boundary

**Restricted test spaces.** The theorem uses the full complex `C_c^infty(R)` autocorrelation cone. On a proper finite-dimensional panel, compact window, or source-constrained subspace, nonzero carrier errors can lie in the annihilator of the tested family. Such a result is only restricted positivity unless a separate extension theorem reaches the full Weil criterion.

**Approximate target equality.** The theorem is exact. If one only asks the quadratic forms to agree within an error tolerance, in a weak topology, or asymptotically under a growing window, approximate deconvolution remains possible in principle. What is closed is the stronger hope that *coarse coefficients can nevertheless give the exact canonical Weil quadratic form*.

**Nonlinear final scalarization.** The result assumes that the recovered carrier enters by the direct linear distributional pairing `Sigma_a(f*widetilde f)`. A nonlinear operation after recovery may be a genuinely different mechanism. `WP-288` still requires any exact final Weil quadratic scalar to satisfy the target quadratic identities, but a nonlinear upstream construction may source-force the resulting distribution in a non-convolutional way.

**Multiple channels.** Two or more coupled channels may carry errors that cancel only after a source-forced operator pairing. The theorem does not reduce such an operator-valued construction to a single arithmetic kernel. It says only that if all channels have already been scalarized to one direct arithmetic convolution before the Weil square is evaluated, coefficient error cannot be hidden.

**Boundary-conditioned or non-translation-invariant recovery.** These are outside (1). They remain live precisely because their source data are not summarized by one arithmetic convolution coefficient function `a`.

**Atomic global counterterms.** Equation (24) fails if the candidate global remainder is permitted to carry compensating atoms at `plus_or_minus log N`. This is a real logical escape, but it is also a bookkeeping warning: a completion that imports the missing finite atoms has not obtained them from archimedean regularity. The source-forcing burden moves to those atoms.

**Positivity.** No positivity hypothesis is used anywhere in (4)--(24). The obstruction precedes the sign problem. Even an arbitrarily signed scalar convolution cannot exploit coarse coefficient localization while remaining exact on the full Weil square cone.

## 7. Matched controls and novelty audit

The functional-analytic ingredient is classical. Weil's criterion is formulated through the quadratic functional on convolution squares; Bombieri develops the same quadratic-functional viewpoint. Dixmier--Malliavin proves that compactly supported smooth functions on a Lie group are finite sums of convolutions, which is exactly the separation step used in (13)--(15). `WP-288` already records this literature boundary and proves the corresponding general cone-linearization statement.

The arithmetic ingredient is also classical. The divisor identity `sum_{d|n} Lambda(d)=log n`, Möbius inversion, and the reciprocal-zeta Dirichlet series are standard analytic number theory. `WP-293` already records the exact uniqueness consequence for scalar arithmetic relocalization.

A bounded literature audit around Weil convolution-square positivity, Dixmier--Malliavin factorization, and Möbius inversion found these classical components but no basis for claiming a new theorem in harmonic analysis or analytic number theory. No such novelty is claimed. The new value is the **combined route closure** required by the current Mathia frontier: an error that is nonzero coefficientwise cannot become invisible merely because the destination checks only autocorrelation squares.

The argument is also a matched-control warning. The cone-separation step knows nothing about rational primes; it applies to any locally finite distribution on the logarithmic line. Likewise, the arithmetic uniqueness step is an algebraic property of the chosen convolution source. Therefore this theorem supplies no Riemann-specific positivity. It only removes a false degree of freedom from the search.

## Consequence for `weil_positivity`

After `WP-292`, unconditional admissibility was obtained by replacing the Mangoldt logarithmic-derivative carrier with the all-integer logarithmic carrier. `WP-293` showed that exact coefficientwise scalar relocalization is uniquely Möbius and restores `1/zeta`. The present result strengthens that boundary:

\[
\boxed{
\text{exact finite Weil quadratic form on the full square cone}
\Longrightarrow
\text{exact Mangoldt distribution}
\Longrightarrow
\text{Möbius kernel}
\Longrightarrow
1/\zeta\text{ zero screen}.
}
\tag{25}
\]

So **approximate/coarse arithmetic localization is not a surviving scalar-convolution route if the destination remains the exact Weil quadratic form**. It survives only for approximate/restricted criteria, or if the construction leaves the one-channel direct-convolution category through a genuinely geometric/nonlinear/operator/boundary coupling.

That is the remaining useful frontier. The next candidate should not tune another arithmetic convolution kernel. It must explain how a source-forced multi-channel, non-translation-invariant, boundary-conditioned, nonlinear, or geometric object assembles finite and archimedean data before final scalarization and obtains its sign independently of the Weil target.
