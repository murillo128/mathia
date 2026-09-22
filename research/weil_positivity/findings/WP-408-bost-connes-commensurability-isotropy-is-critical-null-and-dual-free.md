---
id: WP-408
title: Bost--Connes commensurability isotropy is critical-null and dual-free
branch: weil_positivity
status: supported
kind: bost-connes-groupoid-isotropy-cycle-holonomy-obstruction
claim_strength: exact RH-independent classification showing that nontrivial isotropy of the native Bost--Connes commensurability groupoid is confined to the single point rho=0, which is null for the critical KMS Haar measure, while the scale-retaining dual groupoid is free everywhere; consequently a scalar phase that descends to a normalized groupoid 1-cocycle has trivial holonomy on critical-almost-every native cycles and on every dual cycle
created: 2026-09-22
related: [WP-297, WP-395, WP-407]
clues: [CLUE-weil-positivity-bost-connes-affiliation-conditioning-boundary]
prior_art:
  - J.-B. Bost and A. Connes, Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory, Selecta Math. (N.S.) 1 (1995), 411--457, DOI 10.1007/BF01589495
  - A. Connes, C. Consani, and M. Marcolli, Noncommutative geometry and motives: the thermodynamics of endomotives, Adv. Math. 214 (2007), 761--831, DOI 10.1016/j.aim.2007.03.006; especially the Bost--Connes groupoid descriptions around equations (4.37)--(4.40)
  - standard isotropy calculation for transformation groupoids and the torsion-freeness of the additive group of the profinite completion Z-hat
---

# WP-408 — Bost--Connes commensurability isotropy is critical-null and dual-free

## Claim

`WP-407` isolates the first place where an enlarged block-positive architecture can see a central scalar phase: a genuine cycle. The remaining provenance gate is therefore not merely to draw a loop, but to show that the arithmetic source itself supplies a nontrivial cycle holonomy.

For the **bare Bost--Connes commensurability groupoid**, the source does not supply such holonomy on the part seen by the critical state.

Connes--Consani--Marcolli describe the Bost--Connes algebra through the etale groupoid

\[
G_{BC}
=\{(k,\rho)\in\mathbf Q_{+}^{\times}\times\widehat{\mathbf Z}
  :k\rho\in\widehat{\mathbf Z}\},
\tag{1}
\]

with source `rho`, range `k rho`, and composition by multiplication of the rational labels. Its isotropy is exactly

\[
\boxed{
\operatorname{Iso}(G_{BC})
=G_{BC}^{(0)}
\;\sqcup\;
\{(k,0):k\in\mathbf Q_{+}^{\times},\ k\ne1\}.
}
\tag{2}
\]

Equivalently, **every nonzero `rho in Z-hat` has trivial stabilizer** under the partial rational-scaling action. The only unit with nontrivial isotropy is `rho=0`.

By `WP-395`, the restriction of the critical `KMS_1` state to
`C(Z-hat)` is normalized additive Haar measure. Since the singleton `{0}` is Haar-null,

\[
m_{\rm Haar}\bigl(\{\rho:\operatorname{Iso}(G_{BC})_\rho
\ne\{1_\rho\}\}\bigr)=0.
\tag{3}
\]

Thus the native commensurability groupoid is **essentially free on the critical source measure**.

The scale-retaining dual Bost--Connes groupoid is stronger still. Before quotienting by scale, a one-dimensional `Q`-lattice is labelled by

\[
(\rho,\lambda)\in\widehat{\mathbf Z}\times\mathbf R_{+}^{\times},
\]

and the source action is

\[
k(\rho,\lambda)=(k\rho,k\lambda).
\tag{4}
\]

Because `lambda>0`, the equality

\[
k(\rho,\lambda)=(\rho,\lambda)
\]

forces `k lambda=lambda`, hence `k=1`. Therefore

\[
\boxed{\operatorname{Iso}(\widehat G_{BC})=\widehat G_{BC}^{(0)}}
\tag{5}
\]

**everywhere**, not merely almost everywhere.

The consequence for the live `WP-407` route is exact. If a proposed scalar edge phase is source-derived in the strict sense that it descends to a normalized `U(1)`-valued groupoid 1-cocycle, then its product around any composable source cycle is the cocycle value of the resulting isotropy arrow. Hence that holonomy is `1` for critical-almost-every cycle in `G_BC`, and for every cycle in the scale-retaining dual groupoid. The canonical time cocycle `k -> k^{it}` is the simplest example.

So **the bare Bost--Connes commensurability relation cannot provide the nontrivial source-forced scalar cycle holonomy demanded by `WP-407`**. A surviving cyclic route must add genuinely new source structure: for example a canonical projective/twisted groupoid extension, a non-flat connection that does not descend to the native arrow, noncentral operator-valued holonomy, or a larger global correspondence. Such extra structure must then pass the arithmetic-provenance and finite-plus-archimedean destination gates independently.

**Classification:** `EXACT-DERIVED + RH-INDEPENDENT + BOST-CONNES-GROUPOID + PARTIAL-RATIONAL-SCALING + ISOTROPY-CLASSIFICATION + CRITICAL-KMS-HAAR + NONTRIVIAL-ISOTROPY-NULL + DUAL-GROUPOID-FREE + GROUPoid-1-COCYCLE-HOLONOMY-TRIVIAL + SOURCE-CYCLE-PROVENANCE-NO-GO + MATCHED-CONTROL-GENERIC + TWISTED-EXTENSION-REMAINS-OPEN + NOT-A-WEIL-BRIDGE`.

## 1. The native Bost--Connes groupoid has one exceptional isotropy point

Write a positive rational as `k=a/b` with coprime positive integers `a,b`. An arrow `(k,rho)` is isotropy exactly when

\[
k\rho=\rho.
\tag{6}
\]

Because the partial action is defined inside the finite adeles, multiplying (6) by `b` gives

\[
(a-b)\rho=0
\qquad\text{in }\widehat{\mathbf Z}.
\tag{7}
\]

The additive group of `Z-hat` is torsion-free. One way to see this is the product decomposition

\[
\widehat{\mathbf Z}\cong\prod_p\mathbf Z_p:
\]

multiplication by any nonzero integer is injective on every `Z_p`, hence on their product. Therefore, if `k ne 1`, equation (7) forces

\[
\rho=0.
\tag{8}
\]

Conversely `k 0=0` for every positive rational `k`, so every allowed rational label gives isotropy at zero. This proves (2).

This statement is about the full profinite source, not a finite quotient approximation. At a fixed level `Z/NZ`, multiplication by an integer can have nonzero fixed points because the quotient has torsion. Such finite-level isotropy is generally **spurious from the inverse-limit viewpoint**: a compatible fixed point through every level would give a torsion element of `Z-hat`, hence must be zero. Any finite-level cyclic model proposed as source geometry therefore has to prove that its cycle survives the profinite limit rather than relying on quotient torsion.

## 2. The critical state removes the only nontrivial native isotropy

`WP-395` identifies the critical modular centralizer with the Haar-measurable completion of `C(Z-hat)` and, in particular,

\[
\phi_1(f)
=\int_{\widehat{\mathbf Z}} f(\rho)\,dm_{\rm Haar}(\rho)
\qquad
(f\in C(\widehat{\mathbf Z})).
\tag{9}
\]

For every positive integer `N`, the cylinder `N Z-hat` has Haar measure `1/N` and contains zero. Hence

\[
m_{\rm Haar}(\{0\})\le \frac1N
\]

for every `N`, so

\[
m_{\rm Haar}(\{0\})=0.
\tag{10}
\]

Combining (2) and (10) proves (3). The only place where the native commensurability groupoid admits a nonidentity loop is invisible to the critical unit-space measure.

This is distinct from the support obstruction of `WP-395`. There the issue was that exact arithmetic orbit support becomes null in the critical centralizer. Here the null set is used for a different live question: **whether the source relation itself supplies nontrivial cyclic isotropy capable of carrying the phase that `WP-407` shows positivity could detect**.

## 3. Retaining the scale coordinate removes even the exceptional loop

The dual/cooling presentation keeps the scale coordinate `lambda`. Connes--Consani--Marcolli write the semigroup action on one-dimensional `Q`-lattices as

\[
n(\rho,\lambda)=(n\rho,n\lambda),
\qquad n\in\mathbf N^{\times},
\tag{11}
\]

and extend it to the corresponding partial `Q_+^times` action. Let `(k,rho,lambda)` be isotropy. Then

\[
k\lambda=\lambda.
\tag{12}
\]

Since `lambda in R_+^times`, division by `lambda` gives `k=1`. No property of `rho` is needed. Thus the scale-retaining groupoid is free everywhere, proving (5).

This is an important control for the current finite--archimedean problem. Adding the natural positive scale variable does **not** rescue native cycle holonomy. It deletes the sole exceptional isotropy point rather than promoting it into a finite--archimedean loop.

## 4. Native groupoid 1-cocycles have trivial holonomy on the surviving source

Let

\[
\omega:G\to U(1)
\]

be a normalized multiplicative groupoid 1-cocycle,

\[
\omega(g_1g_2)=\omega(g_1)\omega(g_2),
\qquad
\omega(1_x)=1.
\tag{13}
\]

For a composable cycle `g_1,...,g_m` based at `x`,

\[
g=g_m\cdots g_1\in\operatorname{Iso}(G)_x
\]

and its scalar holonomy is

\[
\prod_{j=1}^m\omega(g_j)=\omega(g).
\tag{14}
\]

If the isotropy at `x` is trivial, then `g=1_x`, so (14) is exactly `1`. Therefore every source phase that **descends to an honest native groupoid 1-cocycle** is cycle-flat on all nonzero units of `G_BC`, and on every unit of the dual groupoid.

For the canonical time evolution,

\[
\omega_t(k,\rho)=k^{it},
\tag{15}
\]

and a native cycle off zero has total rational multiplier `k=1`; its phase is therefore identically one. Prime factorizations do not change this: two factorization paths representing the same native arrow are not distinct holonomy classes in the groupoid.

This is exactly where an apparent loophole must be named rather than hidden. A phase assignment can have nontrivial holonomy around a graph cycle if it **fails** to descend to (13). But then the phase uses additional path-sensitive structure: a projective representation/2-cocycle, a connection with curvature, an auxiliary bundle, or another enlargement. `WP-408` does not forbid such objects. It says that their holonomy is not already present in the bare Bost--Connes commensurability groupoid and therefore needs a separate source-canonicity argument.

## 5. Relation to the previous obstructions

This result is not a restatement of `WP-297`. There the object was a flat multiplicative transport over the rooted positive-integer action category, and the initial object made every such cocycle gauge-trivial. Here the object is the actual Bost--Connes commensurability groupoid; the obstruction is its isotropy geometry, sharpened by the critical Haar measure and by the scale-retaining dual action.

It is also stronger in the direction left open by `WP-407`. `WP-407` proves that cycles are the first graph topology on which a central scalar phase can affect block positivity. `WP-408` asks whether the most canonical arithmetic source currently in play supplies such a cycle. For native commensurability arrows the answer is negative on the critical support, and exactly negative once the scale coordinate is retained.

The conclusion is deliberately narrower than saying that Bost--Connes has no useful cyclic or cohomological structure. Twisted groupoid cohomology, noncentral correspondences, cyclic homology, and larger adelic constructions are different categories. Indeed the Connes--Consani--Marcolli program uses a cokernel and cyclic homology precisely to obtain structure not visible in the bare transformation groupoid alone.

## 6. Matched control and novelty audit

The groupoid presentation is standard prior art, and the isotropy calculation itself is elementary. No new theorem about transformation groupoids is claimed. The line-specific contribution is the consequence for the current Mathia gate: after `WP-407` made nontrivial source-forced cycle holonomy the first surviving scalar-phase datum, the canonical Bost--Connes commensurability groupoid is shown not to contain that datum on the critical source support.

The obstruction is not Riemann-specific. If an infinite compact torsion-free additive group carries the analogous partial rational-scaling action, the same calculation forces nontrivial stabilizers to the origin, and Haar measure again makes that point null. If a positive scale coordinate is multiplied simultaneously, the action is free outright. This matched control is useful diagnostically: **freeness is a structural no-go, not the desired arithmetic mechanism**.

Accordingly, the next admissible cyclic proposal must identify extra source structure that creates nontrivial holonomy without programming the Weil sign. In particular, it must explain why a twist, projective extension, noncentral loop, or global correspondence is canonical for the arithmetic source, why the same construction fails an appropriate nonarithmetic control, and how the resulting positive form reaches the full finite plus archimedean Weil destination.

## Verdict

**Supported exact negative with a category boundary.** The native Bost--Connes commensurability groupoid has nontrivial isotropy only at `rho=0`, a Haar-null point for the critical `KMS_1` state, while its scale-retaining dual groupoid is free everywhere. Hence any scalar phase that genuinely descends to a normalized native groupoid 1-cocycle has trivial cycle holonomy on the source relevant to the critical state. The cycle sensitivity isolated by `WP-407` therefore cannot be supplied by bare Bost--Connes commensurability; a surviving route must source-force additional twisted, non-flat, noncentral, or global structure before positivity can use a nontrivial holonomy.
