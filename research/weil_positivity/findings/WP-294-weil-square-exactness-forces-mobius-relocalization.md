---
id: WP-294
title: Weil-square exactness forces Möbius relocalization even without coefficientwise matching
branch: weil_positivity
status: supported
kind: cone-exact-relocalization-rigidity
claim_strength: exact route-closure theorem showing that scalar arithmetic convolution cannot remain only approximately localized coefficientwise while reproducing the exact finite Weil quadratic form on the full autocorrelation cone
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

`WP-292` gives the unconditional source-native smoothing

\[
\omega:=\sum_{N\ge2}\frac{\log N}{\sqrt N}\,\delta_{\log N},
\]

while `WP-293` proves that **exact coefficientwise** scalar-convolution recovery of

\[
\mu_\Lambda:=\sum_{N\ge2}\frac{\Lambda(N)}{\sqrt N}\,\delta_{\log N}
\]

is uniquely Möbius inversion. A narrower loophole remained: perhaps the recovered coefficients can stay approximate or coarse because the final destination only tests the Weil quadratic form on autocorrelation squares.

That loophole is closed for direct one-channel scalar arithmetic convolution.

Let `a` be a real arithmetic function and define

\[
\eta_a:=\sum_{d\ge1}\frac{a(d)}{\sqrt d}\,\delta_{\log d},
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

Hermitianize by reflection,

\[
\Sigma_a:=\tau_a+\widetilde{\tau_a},
\qquad
\Sigma_\Lambda:=\mu_\Lambda+\widetilde{\mu_\Lambda},
\tag{3}
\]

where reflection sends `delta_x` to `delta_{-x}`. Put

\[
V=C_c^\infty(\mathbb R;\mathbb C),
\qquad
\widetilde f(x)=\overline{f(-x)}.
\]

If only the cone-level identity

\[
\boxed{
\Sigma_a(f*\widetilde f)
=
\Sigma_\Lambda(f*\widetilde f)
\quad\text{for every }f\in V
}
\tag{4}
\]

is assumed, with no coefficientwise matching, positivity, temperedness, or zero information, then nevertheless

\[
\boxed{a=\mu_{\rm Mob}.}
\tag{5}
\]

So there is no scalar source-native arithmetic convolution whose coefficients are merely approximate Mangoldt data while its direct quadratic readout is **exactly indistinguishable from the Mangoldt finite term on the full Weil autocorrelation cone**. Exact target matching forces exact distributional matching; exact distributional matching forces exact arithmetic coefficients; `WP-293` then forces the Möbius kernel and its reciprocal-zeta transform.

A finite-place-clean global completion does not reopen the escape. If the difference between the candidate and target non-finite remainders is smooth near every nonzero point `±log N`, exact equality of the **total** quadratic forms still forces all atomic arithmetic coefficients to match. Hiding a coefficient error therefore requires the other channel itself to carry compensating delta masses at those finite log-integer locations.

This is a route closure, not a positivity theorem and not a new harmonic-analysis theorem. It combines the cone-separation mechanism of `WP-288` with the arithmetic uniqueness of `WP-293` to close the specific approximate/coarse scalar-relocalization loophole left after `WP-292`.

**Classification:** `EXACT-DERIVED + FULL-WEIL-AUTOCORRELATION-CONE + TRIVIAL-CONE-ANNIHILATOR + DIXMIER-MALLIAVIN-FACTORISATION + SOURCE-NATIVE-ARITHMETIC-CONVOLUTION + UNIQUE-MOBIUS-RELOCALIZATION + APPROXIMATE-COEFFICIENT-ESCAPE-CLOSED-FOR-EXACT-TARGET + FINITE-PLACE-CLEAN-COMPLETION-RIGIDITY + NO-POSITIVITY-ASSUMPTION + ROUTE-CLOSURE + NOT-A-WEIL-POSITIVITY-PROOF`.

## 1. The scalar class is locally well defined without growth assumptions

For every arithmetic function `a`, the convolution in (1) is coefficientwise locally finite. At `log N`,

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

Thus `tau_a`, `Sigma_a`, and their differences with the Mangoldt carriers are distributions in `D'(R)` regardless of whether they are tempered. Every compact logarithmic interval sees only finitely many integer atoms, so the proof does not assume any global summability.

This matters because the post-`WP-293` loophole could otherwise be moved into a weaker functional category. A coarse relocalization cannot evade the theorem merely by becoming too large for `S'(R)`: equation (4) lives in the compact-test distribution category where these atomic carriers are already legitimate.

## 2. Autocorrelation squares have trivial annihilator in `D'(R)`

Set

\[
D:=\Sigma_a-\Sigma_\Lambda.
\tag{7}
\]

Equation (4) says

\[
D(f*\widetilde f)=0
\qquad(f\in V).
\tag{8}
\]

Define

\[
B_D(f,h):=D(f*\widetilde h).
\tag{9}
\]

This is linear in `f` and conjugate-linear in `h`. Its diagonal vanishes. Positivity and Hermitian symmetry are not needed to recover the mixed terms: expanding the zero diagonal at `f±h` gives

\[
0=2B_D(f,h)+2B_D(h,f),
\tag{10}
\]

while expanding it at `f±ih` gives

\[
0=2i\bigl(B_D(h,f)-B_D(f,h)\bigr).
\tag{11}
\]

Hence

\[
B_D(f,h)=0
\qquad(f,h\in V).
\tag{12}
\]

Now use the Dixmier--Malliavin factorization theorem on `(R,+)`: every `phi in C_c^infty(R)` is a finite sum

\[
\phi=\sum_{j=1}^m u_j*v_j,
\qquad
u_j,v_j\in C_c^\infty(\mathbb R).
\tag{13}
\]

For each `v_j`, set `h_j=widetilde{v_j}`. Then `u_j*v_j=u_j*widetilde{h_j}`, so (12) yields `D(phi)=0`. Therefore

\[
\boxed{\Sigma_a=\Sigma_\Lambda\quad\text{in }D'(\mathbb R).}
\tag{14}
\]

This is the exact sense in which the full Weil square cone cannot hide a scalar distributional recovery error. It is the `WP-288` factorization mechanism applied to the difference between two arithmetic carriers rather than to an abstract candidate positive form.

## 3. Symmetrized equality forces coefficientwise equality

Both one-sided carriers in (2) are supported in `(0,infinity)` and their reflections in `(-infinity,0)`. There is no atom at zero because `L(1)=Lambda(1)=0`. Restricting (14) to the positive half-line gives

\[
\boxed{\tau_a=\mu_\Lambda.}
\tag{15}
\]

The atoms `log N` are individually isolated, so this distributional equality is equivalent to

\[
(a*L)(N)=\Lambda(N)
\qquad(N\ge1).
\tag{16}
\]

Thus a nonzero error at even one integer changes the exact quadratic form for some compactly supported autocorrelation test. This does **not** say that a small error is easy to detect with a fixed finite numerical panel; the statement concerns the full canonical test class and exact equality.

## 4. Arithmetic uniqueness then forces Möbius inversion

`WP-293` proves that

\[
a*L=\Lambda
\tag{17}
\]

has the unique solution

\[
\boxed{a=\mu_{\rm Mob}.}
\tag{18}
\]

using only the no-zero-divisor property of the Dirichlet-convolution ring and the classical identities

\[
\mathbf 1*\Lambda=L,
\qquad
\mu_{\rm Mob}*L=\Lambda.
\tag{19}
\]

Consequently the unique cone-exact scalar recovery kernel has transform

\[
\sum_{n\ge1}\frac{\mu_{\rm Mob}(n)}{n^{s+1/2}}
=\frac1{\zeta(s+1/2)}
\tag{20}
\]

on its initial convergence half-plane. The reciprocal-zeta divisor therefore returns even though coefficientwise recovery was never assumed. Exactness of the finite Weil quadratic form already forces it implicitly.

## 5. A finite-place-clean global remainder cannot absorb the error

A genuine candidate is global, so one could try to compensate wrong arithmetic coefficients with an archimedean or boundary remainder. Let `A` be the candidate non-finite remainder and `A_W` the target one, and assume

\[
(\Sigma_a+A)(f*\widetilde f)
=(\Sigma_\Lambda+A_W)(f*\widetilde f)
\qquad(f\in V).
\tag{21}
\]

The same cone-separation argument gives equality of distributions,

\[
\Sigma_a-\Sigma_\Lambda=A_W-A.
\tag{22}
\]

If `A_W-A` is smooth in a neighborhood of every `±log N`, `N>=2`, then the right side has no delta singularity at those locations. The left side is a locally finite pure atomic distribution there. Hence every atomic coefficient must vanish, so again

\[
\Sigma_a=\Sigma_\Lambda,
\qquad a=\mu_{\rm Mob}.
\tag{23}
\]

This assumption deliberately does not prescribe a Gamma kernel, polar normalization, or particular geometric completion. It asks only that the channel advertised as non-finite does not itself import finite-log delta masses. An algebraic escape remains if `A` is allowed to contain exactly the missing atoms, but then their source law becomes the unresolved arithmetic problem rather than an archimedean correction.

## 6. Aggressive falsification and exact boundary

The theorem uses the full complex `C_c^infty(R)` autocorrelation cone. On a proper finite-dimensional panel, fixed compact window, or constrained source subspace, nonzero errors may lie in the annihilator of the tested family; that yields only a restricted criterion unless an extension theorem reaches the full Weil class.

The theorem is also exact. Approximate equality of quadratic forms in a norm, weak topology, or growing-window limit is not excluded. What is closed is the stronger hope that approximate/coarse coefficients can nevertheless produce the **exact** canonical Weil quadratic form through direct scalar pairing.

The one-channel hypothesis is essential. A nonlinear upstream map, an operator-valued or multi-channel coupling, a boundary-conditioned non-translation-invariant recovery, or a source-forced cancellation between channels is not reduced to (1). `WP-288` still implies that an exact final Weil quadratic scalar has a canonical linear distributional representation, but it does not say that the upstream geometry producing that distribution must itself be scalar convolution.

No positivity hypothesis appears in (4)--(23). The obstruction therefore occurs before the sign problem. Even an arbitrarily signed scalar convolution cannot exploit coarse coefficient localization while remaining exact on the full Weil square cone.

## 7. Prior-art, matched controls, and novelty audit

The functional-analysis input is classical. Weil's criterion is a positivity statement for a quadratic functional on convolution squares; Bombieri develops the quadratic-functional formulation. Dixmier--Malliavin proves that compactly supported smooth functions on a Lie group are finite sums of convolutions. `WP-288` already records this literature boundary and the general cone-separation consequence.

The arithmetic input is classical as well. The divisor identity `sum_{d|n} Lambda(d)=log n`, Möbius inversion, and the reciprocal-zeta Dirichlet series are standard. `WP-293` already records the exact uniqueness consequence for scalar arithmetic relocalization. A bounded literature audit around Weil convolution-square positivity, Dixmier--Malliavin factorization, and Möbius inversion found the classical ingredients but no reason to claim a new theorem in harmonic analysis or analytic number theory.

The Mathia-specific value is the combined route closure. The cone-separation step is arithmetic-blind and applies to any locally finite distribution; the arithmetic uniqueness step is algebraic. Hence the result gives no Riemann-specific positivity and passes the matched-control test only as a **negative classifier**: an error that is nonzero coefficientwise cannot become invisible merely because the destination inspects autocorrelation squares.

## Consequence for `weil_positivity`

`WP-292` obtained unconditional admissibility by replacing the Mangoldt logarithmic-derivative carrier with the all-integer logarithmic carrier. `WP-293` showed that exact coefficientwise scalar relocalization is uniquely Möbius and restores `1/zeta`. The present result strengthens the boundary to

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
\tag{24}
\]

So **approximate/coarse arithmetic localization is not a surviving scalar-convolution route when the destination remains the exact Weil quadratic form**. It survives only for approximate or restricted criteria, or after leaving one-channel direct convolution through genuinely geometric nonlinear, operator, boundary, or multi-channel structure.
