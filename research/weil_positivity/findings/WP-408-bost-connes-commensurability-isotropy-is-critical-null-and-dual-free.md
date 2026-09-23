---
id: WP-408
title: Bost--Connes commensurability isotropy is critical-null and dual-free
branch: weil_positivity
status: supported
kind: bost-connes-groupoid-isotropy-cycle-holonomy-obstruction
claim_strength: exact RH-independent classification showing that nontrivial isotropy of the native Bost--Connes commensurability groupoid is confined to the single point rho=0, which is null for the critical KMS Haar measure, while the scale-retaining dual groupoid is free everywhere; consequently every normalized group-valued groupoid 1-cocycle and every honest unitary groupoid representation has trivial holonomy on critical-almost-every native cycle and on every dual cycle, including noncommutative U(d)-valued fibre transport
created: 2026-09-22
related: [WP-297, WP-395, WP-407, WP-411, WP-412]
clues: [CLUE-weil-positivity-bost-connes-affiliation-conditioning-boundary]
prior_art:
  - J.-B. Bost and A. Connes, Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory, Selecta Math. (N.S.) 1 (1995), 411--457, DOI 10.1007/BF01589495
  - A. Connes, C. Consani, and M. Marcolli, Noncommutative geometry and motives: the thermodynamics of endomotives, Adv. Math. 214 (2007), 761--831, DOI 10.1016/j.aim.2007.03.006; especially the Bost--Connes groupoid descriptions around equations (4.37)--(4.40)
  - standard isotropy calculation for transformation groupoids, functoriality of groupoid representations, and the torsion-freeness of the additive group of the profinite completion Z-hat
---

# WP-408 — Bost--Connes commensurability isotropy is critical-null and dual-free

## Claim

`WP-407` isolates the first place where an enlarged block-positive architecture can see a central scalar phase: a genuine cycle. `WP-411` and `WP-412` later show that arbitrary passive matrix decorations can retain ordered matrix products on scale-balanced words. The provenance gate is therefore not merely to draw a loop or attach noncommuting matrices, but to show that the arithmetic source itself supplies a nontrivial cycle holonomy.

For the **bare Bost--Connes commensurability groupoid**, the source does not supply such holonomy on the part seen by the critical state, even for nonabelian coefficient groups or honest unitary fibre representations.

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

By `WP-395`, the restriction of the critical `KMS_1` state to `C(Z-hat)` is normalized additive Haar measure. Since the singleton `{0}` is Haar-null,

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

The holonomy consequence does not depend on commutativity of the coefficient group. Let `K` be any group and let `c:G->K` be a normalized multiplicative groupoid 1-cocycle. The product of cocycle values around a composable cycle based at `x` is `c(g)`, where `g` is the resulting isotropy arrow. If the isotropy at `x` is trivial, then `g=1_x` and the product is the identity of `K`. Likewise, for a unitary groupoid representation on a Hilbert bundle, the ordered product of transport operators around such a cycle is exactly the identity operator on the fibre at `x`.

Hence **every honest native groupoid cocycle or unitary representation is cycle-flat on all nonzero units of `G_BC`, and on every unit of the scale-retaining dual groupoid**. This includes `U(d)`-valued transport with noncommuting edge matrices. Noncentrality by itself is therefore not an escape.

This sharpens the boundary left by `WP-411`/`WP-412`. Their arbitrary passive matrix coefficients were intentionally not required to be the values of one coherent groupoid cocycle or representation. A scale-balanced ordered product can survive there precisely because the coefficient assignment carries extra path-sensitive freedom. Once arithmetic provenance is strengthened to an honest representation of the native commensurability arrows, the balanced holonomy collapses to the identity on the critical support.

So a surviving cyclic route must add genuinely new source structure: for example a canonical projective/twisted groupoid extension, a non-flat connection whose transport does not descend to the native arrow, a nontrivial correspondence/Fell-bundle category, or a larger global object. Such extra structure must then pass the arithmetic-provenance and finite-plus-archimedean destination gates independently.

**Classification:** `EXACT-DERIVED + RH-INDEPENDENT + BOST-CONNES-GROUPOID + PARTIAL-RATIONAL-SCALING + ISOTROPY-CLASSIFICATION + CRITICAL-KMS-HAAR + NONTRIVIAL-ISOTROPY-NULL + DUAL-GROUPOID-FREE + ARBITRARY-GROUP-1-COCYCLE-HOLONOMY-TRIVIAL + UNITARY-REPRESENTATION-HOLONOMY-TRIVIAL + NONCOMMUTATIVE-COEFFICIENTS-NOT-AN-ESCAPE + SOURCE-CYCLE-PROVENANCE-NO-GO + MATCHED-CONTROL-GENERIC + TWISTED-EXTENSION-REMAINS-OPEN + NOT-A-WEIL-BRIDGE`.

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

This is distinct from the support obstruction of `WP-395`. There the issue was that exact arithmetic orbit support becomes null in the critical centralizer. Here the null set is used for a different live question: **whether the source relation itself supplies nontrivial cyclic isotropy capable of carrying holonomy that positivity could detect**.

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

## 4. Honest groupoid cocycles and representations have trivial holonomy on the surviving source

Let `K` be an arbitrary, possibly nonabelian group and let

\[
c:G\to K
\]

be a normalized multiplicative groupoid 1-cocycle,

\[
c(g_1g_2)=c(g_1)c(g_2),
\qquad
c(1_x)=e_K.
\tag{13}
\]

For a composable cycle `g_1,...,g_m` based at `x`, put

\[
g=g_m\cdots g_1\in\operatorname{Iso}(G)_x.
\]

Without commuting or reordering any factors,

\[
c(g_m)\cdots c(g_1)=c(g).
\tag{14}
\]

If the isotropy at `x` is trivial, then `g=1_x`, so (14) is exactly `e_K`. The argument uses only functoriality; abelianity of `K` plays no role.

The same statement is coordinate-free for a unitary groupoid representation. If a Hilbert bundle `H_x` carries unitary transports

\[
U_g:H_{s(g)}\to H_{r(g)},
\qquad
U_{g_2g_1}=U_{g_2}U_{g_1},
\qquad
U_{1_x}=I_{H_x},
\tag{15}
\]

then every cycle at a trivial-isotropy unit satisfies

\[
U_{g_m}\cdots U_{g_1}=I_{H_x}.
\tag{16}
\]

Thus matrix noncommutativity cannot manufacture holonomy when the transport genuinely descends to the native arrow. In particular, a fixed-fibre `U(d)`-valued 1-cocycle is covered by (13), while a varying-fibre unitary representation is covered by (15).

For the canonical time evolution,

\[
c_t(k,\rho)=k^{it},
\tag{17}
\]

and a native cycle off zero has total rational multiplier `k=1`; its phase is identically one. Prime factorizations do not change this: two factorization paths representing the same native arrow are not distinct holonomy classes in the groupoid.

At the exceptional unit `rho=0`, a cocycle may restrict to a nontrivial representation of the isotropy group `Q_+^times`. That does not alter the critical conclusion because `{0}` has Haar measure zero. In the scale-retaining dual groupoid there is no exceptional unit at all.

A path assignment can still have nontrivial holonomy if it **fails** to descend to (13) or (15). A projective representation may accumulate a 2-cocycle multiplier; a twisted/Fell-bundle lift may retain multiplication data not determined by the underlying arrow; a connection with curvature may be path-sensitive; a larger correspondence can add genuinely new loops. Those are additional structures, not hidden holonomy of the bare commensurability groupoid.

## 5. Relation to the previous obstructions and the WP-412 frontier

This result is not a restatement of `WP-297`. There the object was a flat multiplicative transport over the rooted positive-integer action category, and the initial object made every such cocycle gauge-trivial. Here the object is the actual Bost--Connes commensurability groupoid; the obstruction is its isotropy geometry, sharpened by the critical Haar measure and by the scale-retaining dual action.

It is stronger in the direction left open by `WP-407`: the negative conclusion is not specific to central scalar phases. Once transport is an honest functor of the native groupoid, **all** coefficient groups and all unitary fibre dimensions have identity holonomy at trivial-isotropy units.

This also narrows the scale-balanced survivor isolated by `WP-412`. KMS invariance permits a word such as `V_a^*V_bV_c^*V_d` only when `bd=ac`. For arbitrary passive coefficients, the ordered matrix product need not vanish or equal the identity. But if those coefficients are additionally required to arise from an honest native groupoid cocycle/representation, a composable balanced word has total rational label `1`, hence is the identity arrow off the exceptional unit, and its ordered transport product is forced to `I`. Therefore **source-forced balanced holonomy cannot mean merely a nonabelian representation of the bare Bost--Connes groupoid**.

There is no contradiction with `WP-411`. That finding deliberately grants arbitrary unitary decorations of the canonical bisection sections and does not impose the functorial law (13) or (15) across different paths. `WP-411`/`WP-412` therefore identify where matrix information could survive algebraically; the present strengthened boundary identifies when that information is actually native groupoid data rather than extra coefficient freedom.

The conclusion remains narrower than saying that Bost--Connes has no useful cyclic or cohomological structure. Twisted groupoid cohomology, projective representations, nontrivial Fell bundles/correspondences, cyclic homology, and larger adelic constructions are different categories. Indeed the Connes--Consani--Marcolli program uses a cokernel and cyclic homology precisely to obtain structure not visible in the bare transformation groupoid alone.

## 6. Matched control and novelty audit

The groupoid presentation is standard prior art, and the isotropy calculation itself is elementary. The extension from `U(1)` to arbitrary group-valued cocycles and unitary groupoid representations is likewise a formal consequence of functoriality: a representation sends the identity arrow to the identity operator. No new theorem about transformation groupoids or groupoid representation theory is claimed.

The substantive Mathia delta is narrower and line-specific. The original scalar statement left “noncentral operator-valued holonomy” as a possible escape. `WP-411`/`WP-412` made that escape concrete by showing that arbitrary passive matrix coefficients can survive on scale-balanced words. Reapplying the already proved isotropy classification at the correct representation level closes the honest-native-cocycle subclass exactly: **noncommuting coefficients alone do not help; nontrivial balanced holonomy requires additional path-sensitive/twisted structure beyond the bare Bost--Connes arrows**.

The obstruction is not Riemann-specific. If an infinite compact torsion-free additive group carries the analogous partial rational-scaling action, the same calculation forces nontrivial stabilizers to the origin, and Haar measure again makes that point null. If a positive scale coordinate is multiplied simultaneously, the action is free outright. This matched control is diagnostically useful: freeness plus functoriality is a generic no-go, not the desired arithmetic mechanism.

Accordingly, the next admissible cyclic proposal must identify extra source structure that creates nontrivial holonomy without programming the Weil sign. In particular, it must explain why a projective/twisted extension, non-flat connection, nontrivial correspondence, or larger global object is canonical for the arithmetic source, why the same construction fails an appropriate nonarithmetic control, and how the resulting positive form reaches the full finite plus archimedean Weil destination.

## Representation audit

The primary object is the native Bost--Connes commensurability groupoid and its scale-retaining dual. A group-valued 1-cocycle is a functor to a one-object groupoid; a unitary groupoid representation is a functorial transport between Hilbert fibres. Holonomy is the ordered product attached to a composable cycle. No commutation, simultaneous diagonalization, scalarization, trace, determinant, or choice of basis is used in the triviality argument.

The strengthened statement does **not** identify arbitrary matrix decorations with groupoid representations. It applies only when the coefficient assignment satisfies the exact composition law of the native arrows. Projective representations, 2-cocycle twists, Fell-bundle multiplication, path-dependent connections, and larger correspondence categories deliberately fail or enlarge that assumption and remain outside this no-go.

## Verdict

**Supported exact negative with a sharper category boundary.** The native Bost--Connes commensurability groupoid has nontrivial isotropy only at `rho=0`, a Haar-null point for the critical `KMS_1` state, while its scale-retaining dual groupoid is free everywhere. Therefore any normalized group-valued 1-cocycle or honest unitary groupoid representation—including noncommutative `U(d)`-valued transport—has identity holonomy on the source relevant to the critical state. The balanced matrix words left algebraically alive by `WP-412` can carry nontrivial holonomy only when their coefficient data contains additional path-sensitive, projective, twisted, or correspondence structure that does not descend to the bare Bost--Connes arrow. Noncentrality alone is not an escape, and no Weil-positivity mechanism follows until such extra structure is source-forced and connected to the full finite-plus-archimedean Weil form.
