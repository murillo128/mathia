---
id: WP-399
title: Fixed critical centralizer shadows have strongly dense sign-symmetric tangents
branch: weil_positivity
status: supported
kind: bost-connes-critical-kms-fixed-shadow-positive-fibre-order-bounded-tangent-density
claim_strength: exact RH-independent obstruction showing that for any bounded positive critical-centralizer shadow d, the two-sided fixed-shadow positive perturbations are precisely the d-order-bounded centered directions and are strong/ultraweakly dense in every bounded centered direction supported by s(d); hence no normal linear readout can obtain a nonzero Weil orientation from ambient positivity merely by replacing the unit shadow of WP-398 with a non-scalar source-forced shadow
created: 2026-09-22
related: [WP-216, WP-395, WP-397, WP-398]
clues: [CLUE-weil-positivity-bost-connes-affiliation-conditioning-boundary]
prior_art:
  - J.-B. Bost and A. Connes, Hecke algebras, type III factors and phase transitions with spontaneous symmetry breaking in number theory, Selecta Math. (N.S.) 1 (1995), 411--457, DOI 10.1007/BF01589495
  - M. Takesaki, Conditional expectations in von Neumann algebras, Journal of Functional Analysis 9 (1972), 306--321, DOI 10.1016/0022-1236(72)90004-3
  - R. G. Douglas, On majorization, factorization, and range inclusion of operators on Hilbert space, Proceedings of the American Mathematical Society 17 (1966), 413--415, DOI 10.1090/S0002-9939-1966-0203464-1
  - V. I. Paulsen and M. Tomforde, Vector spaces with an order unit, Indiana Univ. Math. J. 58 (2009), 1319--1360, DOI 10.1512/iumj.2009.58.3518, arXiv:0712.2613
  - standard spectral calculus, support projections, and bimodularity of conditional expectations in von Neumann algebras
---

# WP-399 — Fixed critical centralizer shadows have strongly dense sign-symmetric tangents

## Claim

`WP-398` proves that if the critical Bost--Connes centralizer shadow is fixed to the order unit,

\[
E(a)=1,
\]

then every sufficiently small bounded centered self-adjoint direction occurs with both signs inside the positive fibre. It deliberately leaves open a more source-sensitive possibility: perhaps the relevant diffuse shadow is not the scalar unit but a nonconstant positive element selected by arithmetic structure, and perhaps its zeros or small values orient the surviving noncentral Fourier correlations.

Fix that possibility before introducing any Weil target.

Let

\[
M=\pi_{\phi_1}(A_{BC})'',
\qquad
N=M_{\phi_1}=M^K,
\]

be the critical Bost--Connes factor and its modular/gauge centralizer from `WP-395`, and let

\[
E:M\to N
\]

be the faithful normal gauge expectation used in `WP-397`--`WP-398`. Fix an arbitrary bounded

\[
d\in N_+,
\qquad p=s(d),
\]

where `p` is the support projection of `d`. Define the fixed-shadow positive fibre

\[
\mathcal S_d
=
\{a\in M_+:E(a)=d\}
\tag{1}
\]

and the bounded centered directions living on the support allowed by `WP-397`,

\[
\mathcal K_d
=
\{k\in M_{\rm sa}:E(k)=0,\ k=pkp\}.
\tag{2}
\]

Call `k in K_d` a **two-sided fixed-shadow tangent** when there is some `epsilon>0` such that

\[
d+\varepsilon k\in\mathcal S_d,
\qquad
d-\varepsilon k\in\mathcal S_d.
\tag{3}
\]

Then:

1. the two-sided tangents are exactly the directions order-bounded by `d`:

\[
\boxed{
\mathcal T_d
=
\{k\in\mathcal K_d:\exists C<\infty,\ -Cd\le k\le Cd\};
}
\tag{4}
\]

2. `T_d` is strong-operator dense, hence ultraweakly dense, in all of `K_d`;
3. therefore every normal real linear functional on `K_d` that is nonnegative on all fixed-shadow positive displacements must vanish identically.

The density statement is the new boundary relative to `WP-398`. If `d` is not bounded below on its support, a particular bounded `k in K_d` need not itself admit any nonzero two-sided perturbation: the scalar-unit argument no longer applies pointwise. But every such `k` is the strong limit of canonical spectral cutoffs `k_n` that **do** admit both signs with the exact same shadow `d`.

Thus merely replacing the unit shadow by a source-forced non-scalar critical-centralizer density does not produce a robust normal first-order Weil orientation. Any asymmetry left by the vanishing/small-value set of `d` is `d`-singular: it disappears under bounded spectral truncation and cannot be detected as a one-sided sign by a normal linear readout.

This does not rule out a genuinely source-forced relation that restricts which centered directions are allowed before positivity is imposed, a nonlinear/global invariant, a singular non-normal readout, an unbounded/domain-sensitive construction, or a finite--archimedean coupling. It closes only the immediate escape "use a more informative fixed centralizer shadow and let ambient positivity orient the off-central data."

**Classification:** `EXACT-DERIVED + RH-INDEPENDENT + CRITICAL-KMS-GNS + FIXED-CENTRALIZER-SHADOW + POSITIVE-FIBRE + ORDER-DOMINATED-TANGENTS + SPECTRAL-CUTOFF-DENSITY + STRONG-OPERATOR-DENSITY + ULTRAWEAK-DENSITY + NORMAL-LINEAR-ORIENTATION-ZERO + NONSCALAR-SHADOW-NO-GO + MATCHED-CONTROL-UNIVERSAL + CATEGORY-BOUNDARY + NOT-A-WEIL-BRIDGE`.

## 1. The exact tangent criterion is order domination by the shadow

Because `E` is linear and `E(k)=0`, every perturbation in (3) automatically has the exact same centralizer shadow:

\[
E(d\pm\varepsilon k)=d.
\tag{5}
\]

So only positivity remains to be checked.

If (3) holds, then

\[
d+\varepsilon k\ge0,
\qquad
d-\varepsilon k\ge0,
\]

which is equivalent to

\[
-\varepsilon^{-1}d
\le k\le
\varepsilon^{-1}d.
\tag{6}
\]

Hence every two-sided tangent is order-bounded by `d`.

Conversely, suppose

\[
-Cd\le k\le Cd
\tag{7}
\]

for some finite `C`. For every `epsilon` with `0<epsilon<=C^{-1}`,

\[
d\pm\varepsilon k
\ge
(1-\varepsilon C)d
\ge0.
\tag{8}
\]

Together with (5), this places both perturbations in `S_d` and proves (4).

The criterion is elementary but important for the research boundary. A non-scalar `d` can indeed make the exact tangent cone smaller than at `d=1`; the obstruction is precisely failure of relative order boundedness with respect to `d`, not an arithmetic orientation supplied by positivity.

## 2. Canonical spectral cutoffs recover both signs for every supported direction

Let

\[
e_n=\mathbf 1_{[1/n,\infty)}(d)\in N.
\tag{9}
\]

By spectral calculus,

\[
e_n\uparrow p=s(d)
\]

strongly. For any `k in K_d`, define

\[
k_n=e_nke_n.
\tag{10}
\]

These are not target-selected cutoffs: they are the canonical spectral cutoffs of the already fixed shadow `d`.

Because `E` is `N`-bimodular,

\[
E(k_n)
=e_nE(k)e_n
=0.
\tag{11}
\]

Also `k_n=k_n^*` and `k_n=pk_np`, so `k_n in K_d`.

Inside the corner `e_nMe_n`, the usual norm order bound gives

\[
-\|k\|e_n
\le k_n\le
\|k\|e_n.
\tag{12}
\]

On the other hand, the definition of `e_n` gives

\[
d\ge \frac1n e_n.
\tag{13}
\]

Combining (12)--(13),

\[
-n\|k\|d
\le k_n\le
n\|k\|d.
\tag{14}
\]

Therefore `k_n in T_d` by (4). Explicitly, when `k_n != 0`, every

\[
0<\varepsilon\le (n\|k\|)^{-1}
\]

makes both `d+epsilon k_n` and `d-epsilon k_n` positive with expectation exactly `d`.

Finally, because `e_n -> p` strongly, `k=pkp`, and the sequence is uniformly bounded,

\[
k_n=e_nke_n\longrightarrow pkp=k
\tag{15}
\]

strongly. Since the `k_n` are self-adjoint, this is also strong-star convergence; on a bounded set it implies ultraweak convergence as well.

Hence

\[
\boxed{
\overline{\mathcal T_d}^{\,\mathrm{SOT}}
=
\overline{\mathcal T_d}^{\,\sigma\text{-weak}}
=
\mathcal K_d.
}
\tag{16}
\]

The equality should not be misread as saying that every `k in K_d` itself is a tangent. If `d` has arbitrarily small spectral values, directions concentrating too strongly where `d` is small can fail (7). Equation (16) says instead that this failure is topologically singular from the viewpoint of normal bounded operator theory.

## 3. No normal linear Weil orientation survives at fixed non-scalar shadow

Let `L` be a normal real linear functional on `K_d`; equivalently, one may take the restriction to `K_d` of a normal self-adjoint functional on the corner `pMp`. Suppose ambient positivity at fixed shadow is claimed to induce a one-sided sign in the sense that

\[
L(a-d)\ge0
\qquad
\text{for every }a\in\mathcal S_d
\tag{17}
\]

whenever the displacement belongs to `K_d`.

Take any `k in T_d`. By definition, for some `epsilon>0`, both

\[
d+\varepsilon k,
\qquad
d-\varepsilon k
\]

belong to `S_d`. Applying (17) to the two displacements gives

\[
\varepsilon L(k)\ge0,
\qquad
-\varepsilon L(k)\ge0,
\]

and therefore

\[
L(k)=0.
\tag{18}
\]

Equation (16) makes `T_d` ultraweakly dense in `K_d`. Normality of `L` then yields

\[
\boxed{L=0\quad\text{on }\mathcal K_d.}
\tag{19}
\]

So a normal linear functional cannot read a nontrivial sign from the noncentral data merely because that data belongs to a positive operator with a fixed source-selected centralizer shadow.

The same statement can be phrased infinitesimally. Any normal first derivative of a proposed fixed-shadow sign functional at the base point `d`, if its sign is supposed to follow only from positivity of nearby points in `S_d`, must vanish on the entire supported centered tangent space after normal closure. A viable orientation must therefore enter through additional structure or through a genuinely nonlinear/higher-order phenomenon, not through a hidden linear first-order consequence of positivity.

## 4. Gauge-frequency directions remain sign-symmetric after shadow truncation

The conclusion is compatible with the Fourier support theorem of `WP-397` and sharpens its surviving boundary.

If `x_r in M_r` is a nonzero gauge-frequency coefficient and `r != 1`, then `E(x_r)=0`. A self-adjoint centered Fourier direction can be formed from `x_r+x_r^*`, or from a finite sum of such paired frequencies. If it is supported in `p`, it belongs to `K_d`.

The spectral cutoffs `e_n` lie in the fixed algebra `N`, so multiplying on both sides does not change gauge frequency:

\[
e_nx_re_n\in M_r.
\tag{20}
\]

Thus the approximation in Section 2 does not erase the nonzero-frequency label. It produces finite-shadow-floor regions on which **the same Fourier direction and its negative** are both compatible with positivity at exact shadow `d`.

This distinguishes the present result from `WP-397`. There the support of every Fourier coefficient of a positive element is dominated by `p=s(E(a))`; that is a genuine constraint. Here we stay entirely inside that permitted support and show that the constraint does not by itself orient the bounded centered directions in any normal first-order sense.

It also extends the exact point made by `WP-398`. At `d=1`, every bounded centered `k` is already order-bounded by the shadow, so both signs occur directly. For a general `d`, exact two-sided feasibility may fail, but the canonical spectral truncations recover it densely. The only new asymmetry available from a non-invertible shadow lives at the singular edge where `d` approaches zero.

## 5. Stress tests and exact boundary

### A non-scalar shadow really can remove individual tangent directions

The density theorem is not a disguised claim that `S_d` is locally balanced in norm. Take a diffuse abelian model with `d(x)>0` almost everywhere but `d(x)` tending arbitrarily close to zero. A bounded centered perturbation that stays of order one where `d(x)` is tiny need not satisfy `|k|<=Cd` for any finite `C`; such a `k` is not in `T_d`.

This is precisely why `WP-398` does not already prove the present finding. The extension from the order unit to an arbitrary positive shadow requires the spectral cutoff argument, and the resulting density is strong/ultraweak rather than norm density in general.

### The result does not eliminate source-forced correlation equations

Suppose the Bost--Connes source, a correspondence, or a finite--archimedean construction imposes an additional equation

\[
\mathcal R(d,k)=0
\]

that selects a proper subset of `K_d`. The cutoffs `e_nke_n` need not satisfy that equation. The theorem therefore does not show that such a source-selected subset is sign-symmetric. It shows that **the fixed shadow plus ambient positivity alone** cannot be the missing orientation mechanism.

This is the central falsification boundary. A future claim must identify and justify the extra relation before reading the desired Weil sign from it.

### Nonlinear and singular readouts remain outside the theorem

A nonlinear functional can distinguish `k` from `-k` through odd higher-order structure supplied by additional data, while a non-normal functional can detect distinctions invisible to ultraweak approximation. Neither possibility is ruled out by (19). But either route carries a new canonicity burden: the nonlinearity or singularity must be source-derived rather than selected because it reproduces the target sign.

Likewise the theorem is bounded. Genuinely unbounded nonhomogeneous forms, continuous-core constructions, domain-sensitive affiliated operators, and other category changes remain separate hypotheses.

## 6. Matched-control interpretation

Sections 1--3 use only a normal conditional expectation `E:M->N`, a fixed bounded `d in N_+`, spectral calculus for `d`, and ordinary operator order. They do not use primes, zeta zeros, the specific Bost--Connes semigroup relations, or RH.

Therefore the theorem is universal: the same fixed-shadow tangent density holds for any von Neumann algebra with a normal conditional expectation onto a subalgebra. This universality is not a weakness of the negative result; it is the matched control demanded by the research mandate. Any proposed sign mechanism that consists only of

1. choosing a positive fixed-point shadow `d`,
2. requiring a positive lift with `E(a)=d`, and
3. linearly reading the centered/off-frequency part,

has the same local behavior in non-arithmetic systems. It cannot by itself explain the Riemann-specific orientation of Weil's form.

The Bost--Connes content enters by identifying the canonical `M`, `N`, `E`, and the live noncentral route left by `WP-395`--`WP-398`. The order theorem then tells us exactly which part of that route is generic and therefore insufficient.

## 7. Prior-art and novelty audit

No novelty is claimed for the operator-theoretic ingredients. Takesaki's conditional-expectation theory supplies the normal bimodular expectation framework. Douglas' range/factorization theorem is classical background for relative operator majorization, and Paulsen--Tomforde give a modern order-unit framework relevant to the quotient degeneracy in `WP-398`. Spectral projections and the estimate `-||k||e <= eke <= ||k||e` are standard von Neumann algebra facts. Bost--Connes supplies the arithmetic dynamical system, while the critical type-III setting is classical in the later KMS-factor literature.

A bounded literature check around conditional-expectation fibres, operator-order domination, tangent/order intervals, and critical Bost--Connes KMS factors found the standard order/factorization and KMS machinery but no theorem coupling this fixed-shadow spectral-cutoff density to the Weil/prime-selection question. **No general theorem novelty is asserted.**

The durable Mathia delta is the exact application to the frontier left open by `WP-398`: changing the critical centralizer shadow from the unit to an arbitrary bounded positive source-selected density does not rescue a normal linear orientation of the supported noncentral data. The only directions not directly two-sided are singular relative to the small spectrum of `d`, and canonical spectral cutoffs make them strong/ultraweak limits of two-sided directions.

## Research consequence

The bounded critical-factor route is narrower again. `WP-397` forces every nonzero-frequency coefficient to live over the support of the centralizer shadow. `WP-398` shows that discarding the shadow, or fixing it to the unit, destroys any inherited linear order. The present result shows that **fixing an arbitrary non-scalar shadow does not repair that defect for normal first-order readouts**: its two-sided positive tangents are dense in all bounded centered directions allowed by the shadow support.

A surviving construction must therefore supply more than a cleverly chosen diffuse shadow. It needs a source-forced joint relation between shadow and correlations that is not preserved by the spectral-cutoff matched control, a genuinely nonlinear/global sign theorem, a justified singular/non-normal observable, or a different operator/form category. The finite-place critical Gram of `WP-216` remains source-forced, but the missing Weil orientation is still not furnished by ambient critical-factor positivity alone.