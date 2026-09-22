---
id: WP-410
title: Central Bost--Connes groupoid twists leave the critical divisibility Gram unchanged
branch: weil_positivity
status: supported
kind: twisted-groupoid-range-projection-obstruction
claim_strength: exact RH-independent extension of WP-409 from base-independent scalar multipliers to arbitrary central U(1) twists of the Bost--Connes commensurability groupoid; twisted bisection lifts have the same source/range projections, the same divisibility semilattice, and under the unchanged scale dynamics every KMS_beta state gives the same normalized GCD Gram, so a central groupoid twist can affect the live route only through off-diagonal twisted convolution before the range-projection readout
created: 2026-09-23
related: [WP-216, WP-297, WP-407, WP-408, WP-409]
clues: [CLUE-weil-positivity-bost-connes-affiliation-conditioning-boundary]
prior_art:
  - A. Buss and R. Exel, Fell bundles over inverse semigroups and twisted etale groupoids, J. Operator Theory 67 (2012), 153-205
  - Z. Afsar and A. Sims, KMS states on the C*-algebras of Fell bundles over groupoids, Math. Proc. Camb. Philos. Soc. 170 (2021), 221-246, DOI 10.1017/S0305004119000379
  - J.-B. Bost and A. Connes, Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory, Selecta Math. (N.S.) 1 (1995), 411-457
---

# WP-410 — Central Bost--Connes groupoid twists leave the critical divisibility Gram unchanged

## Claim

`WP-408` rules out nontrivial scalar holonomy already present in the bare Bost--Connes commensurability groupoid on the critical source support. `WP-409` then grants an external **base-independent scalar multiplier** on the scale group and proves that the canonical critical divisibility Gram still does not see it. The remaining scalar loophole is a genuinely base-dependent central groupoid twist.

That loophole can be narrowed exactly.

Let

\[
G_{BC}
=\{(k,\rho)\in\mathbf Q_+^\times\times\widehat{\mathbf Z}:
  k\rho\in\widehat{\mathbf Z}\}
\]

be the Bost--Connes commensurability groupoid, and let

\[
\mathbf T\longrightarrow \Sigma\longrightarrow G_{BC}
\]

be an arbitrary central `U(1)` groupoid twist. Keep the usual scale cocycle and hence the usual dynamics. For every positive integer `n`, let `B_n` be the integer-scale bisection. Its source is all of `Z-hat` and its range is `n Z-hat`.

A unit-norm section of the Fell line bundle over `B_n` defines a twisted bisection isometry `S_n`. Although products `S_m S_n` may now acquire a genuinely **base-dependent** unitary coefficient, the twist cancels from source and range products:

\[
\boxed{S_n^*S_n=1,\qquad S_nS_n^*=1_{n\widehat{\mathbf Z}}=:E_n.}
\tag{1}
\]

Therefore

\[
\boxed{E_mE_n=E_{\operatorname{lcm}(m,n)}}
\tag{2}
\]

for every central twist, exactly as in the untwisted algebra.

If the scale dynamics is unchanged,

\[
\alpha_t(S_n)=n^{it}S_n,
\tag{3}
\]

then every `KMS_beta` state for which these canonical analytic bisection isometries are represented satisfies

\[
\boxed{\phi_\beta(E_n)=n^{-\beta}.}
\tag{4}
\]

Consequently the normalized range-projection vectors

\[
\xi_n^{(\beta)}
:=n^{\beta/2}\pi_\beta(E_n)\Omega_\beta
\]

have the exact twist-independent Gram

\[
\boxed{
\langle\xi_m^{(\beta)},\xi_n^{(\beta)}\rangle
=\left(\frac{\gcd(m,n)}{\sqrt{mn}}\right)^\beta.
}
\tag{5}
\]

At the actual critical point `beta=1`, this is precisely the `WP-216` carrier. On each prime axis,

\[
G_{1,p}(a,b)=p^{-|a-b|/2},
\]

and the required finite Weil ray remains

\[
W_p=\log p\,(I-G_{1,p}).
\tag{6}
\]

Thus **no central `U(1)` twist of the Bost--Connes groupoid can alter the critical divisibility Gram merely by twisting the canonical scale bisections**. This includes base-dependent twists not reducible to the group multiplier treated in `WP-409`.

The conclusion is deliberately about the range-projection/KMS carrier. A central twist may still change off-diagonal convolution, isotropy fibres, or phase-sensitive observables. A surviving twisted route must therefore use that twisted information **before** collapsing to the divisibility range projections, or else leave the central Fell-line-bundle category altogether.

**Classification:** `CLASSICAL-TWISTED-GROUPOID-ALGEBRA + EXACT-DERIVED-BC-OBSTRUCTION + CENTRAL-U1-GROUPOID-TWIST + BASE-DEPENDENT-ALLOWED + BISECTION-SOURCE-RANGE-RIGIDITY + DIVISIBILITY-SEMILATTICE-RIGIDITY + KMS-MASS-RIGIDITY + CRITICAL-GCD-GRAM-RIGIDITY + OFF-DIAGONAL-TWIST-DATA-ONLY + NOT-A-WEIL-POSITIVITY-PROOF`.

## 1. Twisting multiplication does not twist bisection support

A central groupoid twist is equivalently represented by a Fell line bundle `L -> G_BC`. Twisted convolution changes how fibres multiply over composable arrows, but it does not change the underlying source map, range map, or support of a section.

Fix `n>=1`. The integer-scale arrows form the bisection

\[
B_n=\{(n,\rho):\rho\in\widehat{\mathbf Z}\}.
\]

Its source and range are

\[
s(B_n)=\widehat{\mathbf Z},
\qquad
r(B_n)=n\widehat{\mathbf Z}.
\tag{7}
\]

The restriction of the Fell line bundle to `B_n` admits a unit-norm section. One elementary reason is that `B_n` is homeomorphic to the compact zero-dimensional space `Z-hat`: take local trivializations, refine a finite cover to a finite disjoint clopen partition, choose a unit section on each clopen piece, and patch them. Denote the resulting section by `s_n` and its algebra element by `S_n`.

For a section supported on a bisection, twisted convolution with its adjoint has no sum over competing arrows. The line-bundle multiplication pairs each fibre element with its adjoint, so the twist phase cancels pointwise. Unit norm gives

\[
S_n^*S_n=1_{s(B_n)}=1,
\qquad
S_nS_n^*=1_{r(B_n)}=1_{n\widehat{\mathbf Z}}.
\tag{8}
\]

This is the groupoid version of the range-projection cancellation seen for scalar regular twists in `WP-409`, but it no longer assumes that the twist is pulled back from a multiplier on `Q_+^x` or is independent of the base point `rho`.

The choice of unit section does not matter for (8). Replacing `s_n` by another unit section multiplies it by a `U(1)`-valued function on the bisection; that function again cancels against its adjoint in the source/range products.

## 2. The entire divisibility semilattice survives unchanged

Because the projections in (8) are ordinary characteristic functions on the unit space,

\[
E_mE_n
=1_{m\widehat{\mathbf Z}}1_{n\widehat{\mathbf Z}}
=1_{m\widehat{\mathbf Z}\cap n\widehat{\mathbf Z}}.
\]

The intersection is

\[
m\widehat{\mathbf Z}\cap n\widehat{\mathbf Z}
=\operatorname{lcm}(m,n)\widehat{\mathbf Z},
\]

which proves (2).

In particular, all identities used by `WP-216` to construct the normalized critical conditional Gram remain literally unchanged. The twist may alter the product of the **isometries** themselves,

\[
S_mS_n=u_{m,n}(\rho)S_{mn}
\]

in a local trivialization, with a nonconstant phase `u_{m,n}`, but that coefficient disappears once the readout passes to the range projections `E_n`.

This separates two notions that can otherwise be conflated. A genuinely nontrivial twisted groupoid algebra can have phase-sensitive off-diagonal multiplication while its canonical divisibility projection lattice is exactly the same as in the untwisted algebra. Nontriviality of the twist is therefore not evidence that the `WP-216` positive carrier has changed.

## 3. KMS forces the same projection masses

Retain the standard Bost--Connes scale dynamics. Since every arrow in `B_n` has scale `n`, the bisection lift is analytic and obeys (3). For any `KMS_beta` state,

\[
\begin{aligned}
\phi_\beta(E_n)
&=\phi_\beta(S_nS_n^*)\\
&=\phi_\beta\!\left(S_n^*\alpha_{i\beta}(S_n)\right)\\
&=n^{-\beta}\phi_\beta(S_n^*S_n)\\
&=n^{-\beta}.
\end{aligned}
\tag{9}
\]

No classification of all KMS states on the twisted algebra is needed for this identity. Twisted groupoid/Fell-bundle KMS theory allows the twist and isotropy data to matter elsewhere; equation (9) says only that **every** KMS state satisfying the unchanged scale dynamics has the same mass on these particular canonical range projections.

Now (2) and (9) give

\[
\begin{aligned}
\langle\xi_m^{(\beta)},\xi_n^{(\beta)}\rangle
&=(mn)^{\beta/2}
  \phi_\beta(E_mE_n)\\
&=(mn)^{\beta/2}\operatorname{lcm}(m,n)^{-\beta}\\
&=\left(\frac{\gcd(m,n)}{\sqrt{mn}}\right)^\beta,
\end{aligned}
\]

which proves (5).

So even a base-dependent central twist cannot rotate, sign-correct, or otherwise deform the critical Poisson/GCD Gram through this readout. The local defect (6) remains the same indefinite object audited after `WP-216`.

## 4. This closes the central base-dependent part of the WP-409 escape

`WP-409` intentionally left open a "genuinely base-dependent groupoid twist" because its proof treated a scalar multiplier on the scale group. The present result splits that phrase.

If "base-dependent twist" means a standard **central `U(1)` twist/Fell line bundle over the same Bost--Connes groupoid**, then the canonical integer-scale bisections retain exactly the same source/range projections and the same KMS-normalized Gram. Base dependence by itself is therefore insufficient.

What remains genuinely open is structurally narrower:

- use off-diagonal twisted products or mixed-prime phase observables before the projection readout;
- use a noncentral/operator-valued Fell bundle whose fibre action changes more than scalar multiplication;
- change the source/range geometry, correspondence, or operator category rather than merely twist its central line multiplication;
- or couple the finite and archimedean sectors through a source-forced construction in which the twist participates before positivity is formed.

None of those possibilities is ruled out here.

The distinction from `WP-408` is also sharp. `WP-408` says the **untwisted native groupoid** supplies no nontrivial critical cycle holonomy to an honest scalar 1-cocycle. Here a nontrivial 2-cocycle/twist is granted externally. The result does not trivialize that twist; it proves that the specific divisibility projection/KMS Gram cannot see it.

## 5. Matched control and failure mode

The mechanism is not Riemann-specific. For any etale transformation/semigroup groupoid with a central circle twist, a unit-norm section over a bisection has source and range projections determined by the bisection support, not by the circle multiplication law. If the dynamics is constant on that bisection, the same one-line KMS calculation fixes the associated projection mass.

Thus the obstruction survives generalized-prime and nonarithmetic copies of the same incidence geometry. That clone-stability is useful here because the desired mechanism must distinguish more than a generic twisted semigroup construction.

A candidate twisted completion therefore fails the present gate if its positive carrier is formed only from the canonical range projections, their intersections, and their KMS masses. It remains admissible only if one can point to a concrete twist-sensitive observable whose phase survives into the proposed positive form and whose arithmetic provenance is fixed independently of the target Weil sign.

## Representation audit

The primary objects are the twisted Bost--Connes groupoid algebra, its canonical integer-scale bisections, and their source/range projections. The result is invariant under the choice of local/global unit section of the central Fell line bundle.

The theorem does **not** assert that the twisted and untwisted C*-algebras are isomorphic, that their complete KMS simplices are identical, or that every twisted observable is phase-blind. Twisted convolution and isotropy fields can carry genuine information. The exact statement is narrower: after passing to the canonical bisection range projections and applying the unchanged scale KMS normalization, the entire `WP-216` GCD/Poisson Gram is rigid.

The theorem also does not cover noncentral Fell bundles, twists that alter the underlying groupoid/source-range relation, or a modified dynamics in which the integer-scale bisections are not eigenvectors with eigenvalue `n^{it}`.

## Prior-art and novelty audit

Twisted etale groupoids, Fell bundles, and the fact that bisection-supported sections have source/range products controlled by their supports are standard operator-algebraic structure. Buss--Exel is a direct reference for the twisted etale/Fell-bundle framework. Afsar--Sims develops KMS theory for Fell bundles and, in particular, twisted groupoid C*-algebras. No novelty is claimed for those general facts.

The derived contribution is the line-specific classification obtained by combining them with the exact Bost--Connes divisibility carrier isolated in `WP-216`: **even an arbitrary base-dependent central circle twist cannot change that carrier**, because its range-projection semilattice and KMS masses are twist-independent. This is stronger than `WP-409`, whose explicit calculation covered base-independent scalar multipliers on the scale group, and complementary to `WP-408`, which treated holonomy already present in the bare groupoid.

The literature audit found general twisted-groupoid KMS theory but no source asserting a Riemann-specific Weil-positivity consequence from such a twist. Accordingly this finding is classified as a derived obstruction within the Mathia research line, not as new general groupoid mathematics.

## Verdict

**Supported exact negative with a clear surviving boundary.** Central `U(1)` twisting of the existing Bost--Connes commensurability groupoid can make off-diagonal multiplication genuinely base-dependent, but it leaves the canonical integer-scale source/range projections, their divisibility intersections, and—under the unchanged scale dynamics—their KMS masses exactly unchanged. Hence the critical GCD/Poisson Gram of `WP-216` and its indefinite local Weil defect survive verbatim. The next twisted route must expose twist-sensitive off-diagonal data before projection, become noncentral/operator-valued, alter the underlying source geometry, or supply a different finite--archimedean completion; central base dependence alone is not enough.
