---
id: WP-400
title: Centralizer-local linear source relations inherit dense sign-symmetric tangents
branch: weil_positivity
status: supported
kind: bost-connes-critical-kms-source-restricted-fixed-shadow-positive-fibre-spectral-cutoff-tangent-density
claim_strength: exact RH-independent obstruction showing that any bounded linear source-restricted noncentral direction space which is stable under spectral localization by the fixed critical-centralizer shadow inherits the strong/ultraweakly dense two-sided tangent symmetry of WP-399; in particular centralizer-bimodule and fixed gauge-frequency restrictions cannot by themselves turn ambient positivity into a nonzero normal linear Weil orientation
created: 2026-09-22
related: [WP-216, WP-395, WP-397, WP-398, WP-399]
clues: [CLUE-weil-positivity-bost-connes-affiliation-conditioning-boundary]
prior_art:
  - J.-B. Bost and A. Connes, Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory, Selecta Math. (N.S.) 1 (1995), 411--457, DOI 10.1007/BF01589495
  - M. Takesaki, Conditional expectations in von Neumann algebras, Journal of Functional Analysis 9 (1972), 306--321, DOI 10.1016/0022-1236(72)90004-3
  - standard spectral calculus, support projections, bimodularity of conditional expectations, and gauge spectral subspaces in von Neumann algebras
---

# WP-400 — Centralizer-local linear source relations inherit dense sign-symmetric tangents

## Claim

`WP-399` leaves one explicit escape hatch. For a fixed bounded positive critical-centralizer shadow `d`, ambient positivity alone has strongly and ultraweakly dense sign-symmetric tangents, but perhaps the arithmetic source imposes an additional relation selecting only a proper subset of those centered directions. The spectral cutoffs used in `WP-399` need not preserve an arbitrary relation, so such a source-selected subset could in principle retain an orientation.

There is, however, a broad natural class of source restrictions for which that escape does **not** work: linear restrictions that survive localization by the centralizer shadow itself.

Let

\[
E:M\to N
\]

be a normal conditional expectation, fix

\[
d\in N_+,
\qquad
p=s(d),
\]

and set

\[
\mathcal K_d
=
\{k\in M_{\rm sa}:E(k)=0,\ k=pkp\}.
\tag{1}
\]

Let `V` be any real linear subspace of `K_d`. For the canonical spectral projections

\[
e_n=\mathbf 1_{[1/n,\infty)}(d)\in N,
\tag{2}
\]

assume only the **centralizer-locality condition**

\[
k\in V
\quad\Longrightarrow\quad
e_nke_n\in V
\qquad\text{for every }n.
\tag{3}
\]

Define the source-restricted positive fibre

\[
\mathcal S_{d,V}
=
(d+V)\cap M_+,
\tag{4}
\]

and call `k in V` a two-sided admissible tangent when some `epsilon>0` has

\[
d+\varepsilon k\in\mathcal S_{d,V},
\qquad
d-\varepsilon k\in\mathcal S_{d,V}.
\tag{5}
\]

Then:

1. the admissible two-sided tangents are exactly the directions in `V` order-bounded by `d`,

\[
\boxed{
\mathcal T_{d,V}
=
\{k\in V:\exists C<\infty,\ -Cd\le k\le Cd\};
}
\tag{6}
\]

2. every `k in V` is the strong and ultraweak limit of its canonical cutoffs `k_n=e_nke_n in T_{d,V}`;
3. consequently

\[
\boxed{
\overline{\mathcal T_{d,V}}^{\,\mathrm{SOT}}
=
\overline V^{\,\mathrm{SOT}},
\qquad
\overline{\mathcal T_{d,V}}^{\,\sigma\text{-weak}}
=
\overline V^{\,\sigma\text{-weak}};
}
\tag{7}
\]

4. any normal real linear functional whose sign on admissible displacements is claimed to follow from positivity must vanish on `V`, and hence on its ultraweak closure.

Thus the source-relation caveat in `WP-399` is real but narrower than it first appears. **A linear source restriction does not evade the obstruction when it is preserved by the canonical spectral localizations of the fixed centralizer shadow.** In particular, restrictions defined by centralizer bimodule structure or by retaining prescribed nonzero gauge-frequency sectors satisfy (3). Such restrictions still contain a dense family of both-sign positive perturbations and cannot by themselves produce a nonzero normal first-order Weil orientation.

The surviving linear escape must therefore be genuinely nonlocal across the spectrum of `d`: its defining relation must fail the spectral-cutoff test (3) in a source-forced, canonical way. Nonlinear constraints, nonlinear/global readouts, singular non-normal observables, unbounded/domain-sensitive constructions, and finite--archimedean couplings remain outside the theorem.

**Classification:** `EXACT-DERIVED + RH-INDEPENDENT + CRITICAL-KMS-COMPATIBLE + SOURCE-RESTRICTED-POSITIVE-FIBRE + CENTRALIZER-SPECTRAL-LOCALITY + LINEAR-RELATION + ORDER-DOMINATED-TANGENTS + SPECTRAL-CUTOFF-DENSITY + GAUGE-BAND-COROLLARY + NORMAL-LINEAR-ORIENTATION-ZERO + MATCHED-CONTROL-UNIVERSAL + CATEGORY-BOUNDARY + NOT-A-WEIL-BRIDGE`.

## 1. The source-restricted tangent criterion is unchanged

Because `V` is linear and contained in `K_d`, every `k in V` satisfies `E(k)=0`. Hence

\[
E(d\pm\varepsilon k)=d.
\tag{8}
\]

Membership in `d+V` is automatic for both signs. The only nontrivial condition in (5) is therefore positivity.

If both perturbations are positive, then

\[
d+\varepsilon k\ge0,
\qquad
d-\varepsilon k\ge0,
\]

so

\[
-\varepsilon^{-1}d
\le k\le
\varepsilon^{-1}d.
\tag{9}
\]

Conversely, if

\[
-Cd\le k\le Cd
\tag{10}
\]

for finite `C`, then every `0<epsilon<=C^{-1}` gives

\[
d\pm\varepsilon k
\ge
(1-\varepsilon C)d
\ge0.
\tag{11}
\]

Because `±epsilon k in V`, both perturbations lie in `S_{d,V}`. This proves (6).

The source restriction can certainly remove directions from `K_d`; nothing here says otherwise. The point is more precise: **inside whatever linear direction space `V` the source permits, positivity itself still has no preferred sign whenever the direction is order-bounded by the same shadow `d`.**

## 2. Centralizer-locality makes the WP-399 cutoff argument source-preserving

Take arbitrary `k in V` and define

\[
k_n=e_nke_n,
\qquad
e_n=\mathbf 1_{[1/n,\infty)}(d).
\tag{12}
\]

By assumption (3), `k_n in V`. Since `e_n in N` and `E` is `N`-bimodular,

\[
E(k_n)
=e_nE(k)e_n
=0.
\tag{13}
\]

The support condition is also preserved because `e_n<=p`. Thus the truncation remains inside the **same source-restricted centered space**, which is exactly the point not guaranteed by `WP-399`.

Inside the corner `e_nMe_n`,

\[
-\|k\|e_n
\le k_n\le
\|k\|e_n.
\tag{14}
\]

Spectral calculus gives

\[
e_n\le n d,
\tag{15}
\]

so

\[
-n\|k\|d
\le k_n\le
n\|k\|d.
\tag{16}
\]

Equation (6) now gives `k_n in T_{d,V}`. Explicitly, for nonzero `k_n`, both

\[
d+\varepsilon k_n,
\qquad
d-\varepsilon k_n
\]

are source-admissible positive elements whenever

\[
0<\varepsilon\le (n\|k\|)^{-1}.
\tag{17}
\]

Finally `e_n` increases strongly to `p=s(d)`. Since `k=pkp`,

\[
k_n=e_nke_n\longrightarrow k
\tag{18}
\]

strongly. The sequence is uniformly norm bounded by `||k||`, so it converges ultraweakly as well. Every element of `V` is therefore a strong and ultraweak limit of two-sided admissible tangents from `V` itself, proving (7).

This is the exact extra statement needed to close the caveat in `WP-399` for cutoff-stable relations. There the truncation was known to stay in `K_d`; here it is proved to stay in the source-selected subspace as well.

## 3. Normal linear sign readouts vanish even after the source restriction

Let `L` be the restriction to `V` of a normal real linear functional on the self-adjoint corner `pM_{sa}p`. Suppose the proposed sign mechanism says

\[
L(a-d)\ge0
\qquad
\text{for every }a\in\mathcal S_{d,V}.
\tag{19}
\]

For any `k_n in T_{d,V}`, choose an `epsilon>0` for which both signs in (5) are admissible. Applying (19) twice gives

\[
\varepsilon L(k_n)\ge0,
\qquad
-\varepsilon L(k_n)\ge0,
\]

hence

\[
L(k_n)=0.
\tag{20}
\]

Normality and the ultraweak convergence `k_n -> k` imply `L(k)=0` for every `k in V`. By continuity the same is true on the ultraweak closure of `V`:

\[
\boxed{
L=0
\quad\text{on }\overline V^{\,\sigma\text{-weak}}.
}
\tag{21}
\]

So introducing a proper linear source subspace does not by itself cure the orientation problem. If the subspace is stable under the shadow's canonical spectral localization, all of its bounded directions remain approximable by admissible positive perturbations with both signs.

This is deliberately a **normal first-order** statement. It does not say that every nonlinear observable is even in `k`, and it does not say that a singular functional cannot distinguish the limiting edge where `d` becomes small. Those are separate hypotheses with separate canonicity burdens.

## 4. Centralizer bimodules automatically satisfy the locality gate

Condition (3) may look tailored to the proof, but an important structural class satisfies it automatically.

Let `W subseteq M` be a complex linear subspace that is

- stable under adjoint;
- an `N`-bimodule, so `NWN subseteq W`;
- centered, in the sense that `E(W)=0`.

Set

\[
V_W
=
\{k\in W_{\rm sa}:k=pkp\}.
\tag{22}
\]

Because every `e_n` belongs to `N`,

\[
k\in V_W
\quad\Longrightarrow\quad
e_nke_n\in V_W.
\tag{23}
\]

Hence the full theorem applies to `V_W`.

This matters for the current critical-factor route because many natural ways of saying “retain only these noncentral correlations” are exactly bimodule restrictions over the fixed algebra. If such a restriction can be imposed independently on the left and right by centralizer observables, it is too local to defeat the spectral-cutoff matched control.

The conclusion is not that bimodule information is arithmetically empty. It can encode which off-central sectors exist and how they are supported. The conclusion is only that **ambient positivity plus a linear `N`-bimodule admissibility condition still supplies no normal one-sided first-order sign.**

## 5. Fixed gauge-frequency restrictions are a concrete critical Bost--Connes corollary

Return to the critical Bost--Connes representation from `WP-395`--`WP-399`, with

\[
M=\pi_{\phi_1}(A_{BC})'',
\qquad
N=M_{\phi_1}=M^K,
\]

and the normal gauge expectation `E:M->N`.

For a nontrivial gauge spectral subspace `M_r`, multiplication on either side by fixed-point elements preserves the same gauge frequency. Thus each `M_r` is an `N`-bimodule. Its expectation vanishes when `r` is nontrivial. If `F` is any inversion-symmetric family of nonzero/nontrivial frequencies, the self-adjoint part of the linear span of the corresponding `M_r`, restricted to the support `p`, gives a space `V_F subseteq K_d` satisfying (3).

Therefore imposing a linear rule of the form

> only these gauge frequencies are admissible,

or any finite/infinite linear combination of such frequency sectors that remains an `N`-bimodule, **does not break the sign symmetry**. The canonical truncations `e_n k e_n` keep the same allowed frequency content while recovering both positive signs densely.

This sharpens the research boundary after `WP-397`. That finding shows that a positive element's nonzero-frequency coefficients are confined to the support of its centralizer shadow. `WP-399` shows that all centered supported directions are densely sign-symmetric if no further relation is imposed. The present result shows that a large class of seemingly meaningful further relations—linear gauge-band or centralizer-bimodule restrictions—still cannot supply the missing orientation because the source relation survives the very spectral cutoffs that generate the sign symmetry.

A successful linear source relation must therefore couple data **across** centralizer spectral scales in a way that cannot be localized by `e_n` without violating the relation. Merely selecting which gauge sectors are allowed is not enough.

## 6. Stress tests and exact escape boundary

### A linear relation can escape if spectral localization destroys it

The theorem assumes (3). This is not cosmetic. A genuinely global linear constraint might relate pieces of `k` living at arbitrarily small and large spectral values of `d` so that

\[
k\in V
\quad\text{but}\quad
e_nke_n\notin V.
\]

Then the source-preserving approximation used above fails, and no conclusion about dense two-sided tangents follows from this argument. Such a relation is a live route. But it must be derived from the arithmetic source, and its failure under cutoff should be proved rather than inferred from a desired sign.

This gives a decisive test for future linear proposals: **apply the canonical `d`-spectral cutoff before doing any Weil comparison**. If the defining source relation survives every cutoff, WP-400 applies. If it fails, the precise cross-scale term destroyed by the cutoff becomes the object that must carry the arithmetic orientation.

### Nonlinear constraints remain outside the theorem

If admissibility is defined by a nonlinear equation or inequality, `V` is no longer the relevant model and the simultaneous presence of `k` and `-k` is not automatic. A nonlinear relation can in principle orient the admissible set. The sign must still be intrinsic and source-forced; choosing a nonlinear constraint because it reproduces Weil positivity would violate the research mandate.

### Nonlinear or singular readouts also remain outside the theorem

Equation (21) concerns normal linear functionals. A nonlinear energy may react differently to the joint structure of `d` and the off-central coefficients even when the linear tangent is sign-symmetric. A non-normal functional may also detect distinctions lost under ultraweak approximation. Neither is ruled out here.

The corresponding burden is stronger, not weaker: the nonlinear or singular object must have an independent canonical origin and must survive matched controls without importing the target Weil functional by hand.

### Unbounded and finite--archimedean category changes remain live

The argument is entirely bounded and local to the fixed-shadow fibre in a von Neumann algebra. It does not close genuinely unbounded nonhomogeneous forms, domain-sensitive relations, continuous-core constructions, one-sided correspondences, nonunital boundary categories, or a source-forced finite--archimedean assembly.

It also supplies no archimedean or polar counterterm. Even if a surviving relation escaped the obstruction, it would still need to satisfy the global completion requirements of the `weil_positivity` mandate.

## 7. Matched-control and novelty audit

The theorem in Sections 1--3 uses only a normal conditional expectation, one bounded positive element in its range, ordinary operator order, and a real linear subspace stable under canonical spectral compression. It does not use primes, zeta zeros, RH, or any specific Bost--Connes relation.

That universality is the correct control. A sign mechanism that can be reduced to

1. fix a positive shadow `d`;
2. choose a cutoff-stable linear centered subspace `V`;
3. keep only positive lifts in `d+V`; and
4. apply a normal linear sign readout,

has the same obstruction in a completely non-arithmetic von Neumann algebra. It therefore cannot by itself explain a Riemann-specific Weil orientation.

No novelty is claimed for the operator-algebra ingredients. Conditional expectations and bimodularity are standard in Takesaki's framework; support projections and spectral compressions are standard von Neumann algebra tools; gauge spectral subspaces and the arithmetic dynamical setting come from the Bost--Connes system and its subsequent operator-algebraic development.

A bounded prior-art search around conditional-expectation positive fibres, order intervals, support projections, hereditary/order localization, and source subspaces preserved by spectral cutoffs found the standard ingredients but no source stating the exact Mathia-specific formulation “fixed conditional-expectation shadow plus cutoff-stable linear source relation implies dense two-sided admissible tangents.” **No external theorem novelty is asserted.** The durable delta is the closure of a concrete escape class explicitly left open by `WP-399`.

## Research consequence

The instruction emerging from `WP-399` was to keep a **joint source-forced relation** that restricts the admissible noncentral directions beyond fixed-shadow support. WP-400 makes that instruction more precise: **the relation must not merely be linear and centralizer-local**.

Any candidate relation that is an `N`-bimodule condition, a fixed gauge-frequency/band condition, or otherwise stable under the canonical `d`-spectral compressions inherits dense sign-symmetric tangents and cannot support a nonzero normal linear orientation from positivity alone. The first kill test for a new bounded linear candidate is now immediate: check whether `e_nke_n` preserves the source relation for every `n`.

The live bounded route is correspondingly narrower but clearer. It requires a canonical relation with genuine cross-scale coupling that spectral localization destroys, or a genuinely nonlinear/global sign mechanism. Beyond the bounded setting, singular, unbounded, domain-sensitive, correspondence, or finite--archimedean constructions remain open categories. None of these is a Weil bridge yet; they are the remaining places where a source-derived orientation could still enter without being erased by the fixed-shadow matched control.