---
id: WP-289
title: Critical Mangoldt covariances admit no continuous positive Weil majorant
branch: weil_positivity
status: supported
kind: positive-majorant-obstruction
claim_strength: exact RH-independent no-go for monotone positive completion of the source-native critical covariance family
created: 2026-09-13
related: [WP-005, WP-269, WP-273, WP-288]
prior_art:
  - Bochner--Schwartz theorem for positive-definite distributions
  - elementary order of positive tempered measures
  - Weil/Bombieri quadratic-form positivity criterion
  - Connes--Consani compressed-scaling positivity as a non-additive comparison architecture
---

# WP-289 — Critical Mangoldt covariances admit no continuous positive Weil majorant

## Claim

`WP-269` proves that the source-native critical Mangoldt spectral measure

\[
\nu:=\nu_{1/2}
=\frac12\sum_p\sum_{k\ge1}(\log p)p^{-k/2}
\bigl(\delta_{k\log p}+\delta_{-k\log p}\bigr)
\tag{1}
\]

is not tempered. That rules out taking the direct limit of the finite positive stationary covariances. A stronger local-to-global escape still appears possible: keep every finite arithmetic covariance positive, then add a positive archimedean/global sector large enough that the completed form has a continuous positive limit.

That escape is impossible as well.

Let `V=C_c^\infty(R)`. For every finite symmetric set `F` of prime-power frequencies, let

\[
\nu_F:=\nu|_F,
\qquad
q_F(f):=\int_{\mathbb R}|\widehat f(\xi)|^2\,d\nu_F(\xi).
\tag{2}
\]

There is **no** continuous translation-invariant nonnegative Hermitian quadratic form `Q` on `V` satisfying

\[
Q(f)\ge q_F(f)
\qquad
(f\in V)
\tag{3}
\]

for every finite `F` in a cofinal exhaustion of the source spectrum.

Equivalently, there is no family of positive additive completions

\[
Q_j=q_{F_j}+A_j,
\qquad A_j\ge0,
\qquad F_j\uparrow\operatorname{supp}\nu,
\tag{4}
\]

that converges pointwise on `V` to a continuous translation-invariant positive form `Q` while preserving the finite source covariance blocks unchanged. For fixed `m`, positivity gives `Q_j>=q_{F_m}` for every `j>=m`; passing to the pointwise limit would give (3), which is impossible.

The obstruction is order-theoretic rather than a failure of a particular regularization. By Bochner--Schwartz, `Q` would have a positive tempered spectral measure `mu`. Since `Q-q_F` is again a continuous translation-invariant positive quadratic form, its spectral measure is positive, hence

\[
\mu-\nu_F\ge0.
\tag{5}
\]

Thus `nu_F<=mu` for every finite cylinder. Monotone exhaustion forces

\[
\nu\le\mu.
\tag{6}
\]

But every positive submeasure of a positive tempered measure is tempered, contradicting `WP-269`.

Therefore the critical arithmetic covariance cannot survive into a Weil candidate as a monotonically preserved positive summand. Any successful finite--archimedean geometry must change the arithmetic block **before** final positivity is read: through signed interference, quotient/compression, nonlocal coupling, or another source-forced operation that is not simply `positive finite part + positive completion`.

**Classification:** `EXACT-DERIVED + RH-INDEPENDENT + POSITIVE-MAJORANT-NO-GO + LOCAL-TO-GLOBAL-NARROWING + NOT-A-WEIL-POSITIVITY-PROOF`.

## 1. The finite source covariances are canonical and individually positive

The data in (2) are not fitted kernels. `WP-269` derives their frequencies from the arithmetic Hamiltonian

\[
H e_{p^k}=k\log p\,e_{p^k}
\tag{7}
\]

and their masses from the exact critical squared boundary amplitudes

\[
\|C_{1/2}e_{p^k}\|^2=(\log p)p^{-k/2}.
\tag{8}
\]

For finite `F`, `nu_F` is a finite positive measure, so `q_F` is a continuous translation-invariant positive quadratic form. Its polarization is the stationary covariance whose spectral measure is `nu_F`.

The question here is deliberately stronger than convergence. We do not ask that `q_F` itself converge. We ask whether a single completed positive geometry could dominate every finite source block, or equivalently whether positive archimedean/global add-ons could stabilize the family while never subtracting from the arithmetic covariance already present.

## 2. A continuous positive majorant would force spectral measure domination

Assume that a `Q` satisfying (3) exists. Positivity, the parallelogram identity and complex degree-two homogeneity polarize `Q` to a continuous Hermitian form. Translation invariance puts it in the convolution-distribution category, exactly as in `WP-288`. Bochner--Schwartz then gives a unique positive tempered measure `mu` such that

\[
Q(f)=\int_{\mathbb R}|\widehat f(\xi)|^2\,d\mu(\xi).
\tag{9}
\]

For each finite `F`, define

\[
R_F(f):=Q(f)-q_F(f).
\tag{10}
\]

Equation (3) says `R_F>=0`. Both terms are continuous and translation invariant, so `R_F` is also a continuous translation-invariant positive quadratic form. Applying Bochner--Schwartz once more gives a positive tempered measure `rho_F` with

\[
R_F(f)=\int|\widehat f|^2\,d\rho_F.
\tag{11}
\]

Uniqueness of the Fourier representation yields

\[
\mu=\nu_F+\rho_F,
\tag{12}
\]

hence (5).

Now choose a nested cofinal exhaustion `F_1 subset F_2 subset ...`. For every Borel set `E`,

\[
\nu_{F_j}(E)\uparrow\nu(E),
\qquad
\nu_{F_j}(E)\le\mu(E).
\tag{13}
\]

Therefore `nu(E)<=mu(E)` for every `E`, proving (6).

No assumption about zeta zeros, RH, a Gamma factor or a functional equation entered this step. It is forced solely by positivity, translation covariance and preservation of the source finite cylinders.

## 3. Temperedness is hereditary downward for positive measures

Because `mu` is a positive tempered measure, there is some finite `N` for which

\[
\int_{\mathbb R}(1+|\xi|^2)^{-N}\,d\mu(\xi)<\infty.
\tag{14}
\]

Positive measure domination immediately gives

\[
\int_{\mathbb R}(1+|\xi|^2)^{-N}\,d\nu(\xi)
\le
\int_{\mathbb R}(1+|\xi|^2)^{-N}\,d\mu(\xi)<\infty.
\tag{15}
\]

But `WP-269` proves the opposite statement at the critical half-density:

\[
\int(1+|\xi|^2)^{-N}\,d\nu(\xi)=\infty
\qquad\text{for every finite }N.
\tag{16}
\]

This contradiction proves the claim.

The same argument can be phrased without first postulating an infinite arithmetic form. Suppose only that positive completed forms `Q_j=q_{F_j}+A_j`, with `A_j>=0`, converge pointwise to a continuous positive translation-invariant `Q`. For any fixed `m` and every `j>=m`,

\[
Q_j\ge q_{F_j}\ge q_{F_m}.
\tag{17}
\]

Taking `j to infinity` yields `Q>=q_{F_m}`. Since `m` was arbitrary, the already-proved majorant contradiction applies. Thus a cutoff-dependent positive completion cannot evade the obstruction by postponing the infinite arithmetic sum to the limit.

## 4. This is stronger than the direct-limit obstruction in WP-269

`WP-269` excludes a positive-definite distribution whose spectral measure is exactly `nu`. A possible response was that a global geometry need not have spectral measure exactly `nu`; it could have a larger positive measure after the archimedean/global completion.

Equations (5)--(16) close precisely that loophole. **No positive tempered spectral measure can even contain all of `nu` as a positive submeasure.** Therefore adding positive spectral mass cannot repair the critical growth defect. The obstruction is monotone: once the critical Mangoldt atoms are retained with their source weights and positive orientation, every positive enlargement inherits their non-tempered growth.

This also sharpens the distinction with `WP-273`. There the pole-completed carrier is already a signed arithmetic-minus-continuum object, and positivity can only appear after a nonlocal compression/sampling theorem. The present result explains why such a sign-changing or coupling step is not cosmetic. A completion that kept the arithmetic stationary covariance as an untouched positive summand could never enter the ordinary continuous Weil category in the first place.

## 5. Matched controls and aggressive falsification

**Move away from criticality.** For the matched family

\[
\nu_\sigma
=\frac12\sum_{p,k}(\log p)p^{-k\sigma}
\bigl(\delta_{k\log p}+\delta_{-k\log p}\bigr),
\tag{18}
\]

`WP-269` gives the exact boundary. At `sigma=1`, `nu_sigma` is tempered, and for `sigma>1` it even has finite total mass. The majorant obstruction therefore disappears at and beyond the Euler boundary. The failure at `sigma=1/2` is not a generic statement that countable positive spectra cannot be globally completed.

**Sparse-spectrum control.** A sufficiently sparse generalized-prime energy set can make the corresponding critical measure tempered. Such a system is not excluded by this theorem. The obstruction uses the actual arithmetic density of the Riemann prime-power spectrum.

**Allow signed completion.** If the archimedean/global sector subtracts, interferes, or couples with the finite part before scalar positivity is taken, then `Q-q_F` need not be positive and measure domination (5) fails. This is the principal surviving route, not a loophole in the proof. The theorem says that the sign-producing operation must occur before the source critical covariance becomes a permanent positive direct summand.

**Abandon translation invariance.** A positive majorant without translation invariance is not covered by Bochner--Schwartz. But `WP-288` shows that an exact scalar Weil square on the full test class is translation invariant. Translation-noninvariant geometry can therefore survive only upstream; its final exact scalar output must shed that dependence.

**Restrict the test class.** On a proper subspace one may be able to dominate every finite cylinder. That proves only restricted positivity unless an independent extension/density theorem reaches the full Weil class. Any such extension must confront the same global spectral-growth obstruction when it produces a continuous translation-invariant form on `C_c^infty(R)`.

**Change generalized-function category.** Positive ultra-hyperfunctional objects can host the fixed exponential growth of `nu`, as already noted in `WP-269`. That is a genuine category change. To answer the research mandate it would still need a source-forced bridge back to the canonical Weil quadratic form, whose ordinary test-space continuity is part of the target.

## 6. Prior-art and novelty audit

No novelty is claimed for the functional analysis. Bochner--Schwartz is classical, and the fact that a positive submeasure of a positive tempered measure is tempered follows immediately from the standard weighted-integrability characterization of positive tempered measures. A bounded literature audit around positive-definite distributions, tempered positive measures and quadratic-form domination found only these classical ingredients; modern expositions likewise represent positive-definite tempered distributions by positive tempered measures.

The result also does not compete with the classical Weil/Bombieri criterion. If the Weil quadratic form is positive, `WP-288` places its scalar output in precisely the positive-definite-distribution category used above. The present theorem does **not** prove or disprove that positivity. It says that such a positive Weil form cannot arise by monotonically embedding all finite critical Fock/Mangoldt covariance blocks into it.

This is consistent with close prior art rather than duplicating it. Connes--Consani type compression mechanisms obtain positivity only after a nontrivial global compression; they do not amount to preserving an exponentially growing critical Mangoldt stationary measure as a positive spectral submeasure. Contemporary compact-window Weil computations likewise emphasize positivity of the assembled global form rather than positivity of independently additive finite-place pieces. The same-space Fourier-multiplier obstruction cited in `WP-005` concerns a different spectral-type mismatch; the present obstruction is instead an order/growth theorem for a source-native positive arithmetic family.

The Mathia-specific delta is therefore the application of classical measure order to the exact source spectrum of `WP-269`: the direct-limit failure upgrades to a **no-positive-majorant theorem**. Even an arbitrarily rich positive archimedean/global add-on cannot absorb the critical arithmetic covariance while preserving all of its finite positive cylinders.

## Consequence for `weil_positivity`

A candidate global sign theorem should now be rejected early if its architecture is

\[
\text{critical positive Mangoldt covariance}
\quad+\quad
\text{positive archimedean/global correction}
\quad\longrightarrow\quad
\text{continuous positive Weil form},
\tag{19}
\]

with the finite covariance preserved monotonically through the limit. No choice of additional positive mass, extra positive channels, or cutoff-dependent positive completion can satisfy that architecture.

The surviving search is narrower and more geometric: the finite-prime and archimedean/global sectors must interact **before** the final positivity theorem. A viable construction must derive a quotient, compression, boundary interference, cohomological pairing, or operator-level coupling in which the raw critical arithmetic covariance is not retained as a positive submeasure of the final stationary spectrum. That coupling must still be source-forced and must recover the exact Weil quadratic form without importing zero data or choosing the sign after the fact.