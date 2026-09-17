---
id: WP-345
title: Maaß--Selberg height derivative is a positive boundary square but does not constrain the scattering divisor
branch: weil_positivity
status: supported
kind: maass-selberg-boundary-square-obstruction
claim_strength: exact rank-one Maaß--Selberg differentiation plus meromorphic CDD/Blaschke matched control
created: 2026-09-17
related: [WP-237, WP-287, WP-243, WP-245]
prior_art:
  - Tian An Wong, Explicit formulas for the spectral side of the trace formula of SL(2), Acta Arithmetica 195 (2020), 149-175, DOI 10.4064/aa190115-9-10, arXiv:1608.02296
  - classical Maaß--Selberg relations for truncated Eisenstein series
  - classical Blaschke/inner-factor and Castillejo--Dalitz--Dyson ambiguity for unitary scalar scattering functions
---

# WP-345 — Maaß--Selberg height derivative is a positive boundary square but does not constrain the scattering divisor

## Claim

The direct `boundary square` escape left open by the Maaß--Selberg clue can be evaluated exactly in rank one. For the `SL(2,Z)` Maaß--Selberg norm used by Wong, differentiation with respect to the logarithmic Arthur height produces a pointwise positive square:

\[
\frac{\partial}{\partial\tau}
\left\|\Lambda^{e^\tau}E\left(\cdot,\frac{1+ir}{2}\right)\right\|_2^2
=
\left|1+S(r)e^{-ir\tau}\right|^2\ge 0,
\tag{1}
\]

where

\[
S(r):=m\left(\frac{1+ir}{2}\right),
\qquad |S(r)|=1
\tag{2}
\]

on the unitary axis.

This is a genuine source-defined positive boundary response. But it does **not** transfer positivity to the Weil explicit-formula block. The same differentiation annihilates the entire `T`-independent logarithmic-derivative term that contains the zero divisor, finite-prime data and archimedean/polar companions. More sharply, the positivity in (1) survives meromorphic inner/CDD modifications that preserve boundary unitarity and the reciprocal functional equation while inserting off-unitary-axis zero/pole pairs into the scattering function.

Therefore the direct height-boundary square is a sharp matched control, not a Weil-positivity mechanism. A successful trace/scattering route must use additional source structure that couples to the logarithmic derivative or otherwise excludes the inner-factor freedom **before** the sign is taken.

**Classification:** `EXACT-DERIVED + MAASS-SELBERG-BOUNDARY-SQUARE + CDD/BLASCHKE-MATCHED-CONTROL + DECISIVE-NARROWING + NOT-A-WEIL-BRIDGE`.

## 1. Exact boundary-square identity

Wong's Remark 5.2 records the classical Maaß--Selberg relation for the truncated Eisenstein series. On the unitary axis it gives

\[
N_T(r)
:=
\left\|\Lambda^T E\left(\cdot,\frac{1+ir}{2}\right)\right\|_2^2
\tag{3}
\]

as

\[
\begin{aligned}
N_T(r)
={}&2\log T
+m\left(\frac{1-ir}{2}\right)\frac{T^{ir}}{ir}
-m\left(\frac{1+ir}{2}\right)\frac{T^{-ir}}{ir}\\
&-\frac12\left[
\frac{m'}m\left(\frac{1-ir}{2}\right)
+
\frac{m'}m\left(\frac{1+ir}{2}\right)
\right].
\end{aligned}
\tag{4}
\]

Put `tau=log T` and define `S(r)` by (2). On the unitary axis the scalar scattering relation gives

\[
m\left(\frac{1-ir}{2}\right)=\overline{S(r)}=S(r)^{-1}.
\tag{5}
\]

The last line of (4) is independent of `tau`. Differentiating the first line therefore yields

\[
\begin{aligned}
\partial_\tau N_{e^\tau}(r)
&=2+\overline{S(r)}e^{ir\tau}+S(r)e^{-ir\tau}\\
&=\left|1+S(r)e^{-ir\tau}\right|^2.
\end{aligned}
\tag{6}
\]

Thus the logarithmic-height response is not merely real or bounded below after integration: it is a **pointwise spectral square**.

For Wong's positive-type test `g=g_0*g_0^*`, the spectral weight is

\[
w_g(r)=\left|\widehat g_0\left(\frac12+ir\right)\right|^2\ge0.
\tag{7}
\]

Whenever differentiation under the absolutely convergent spectral integral is justified, (6) gives

\[
\partial_\tau J^{e^\tau}(g)
=
\int_{\mathbb R}
\left|1+S(r)e^{-ir\tau}\right|^2w_g(r)\,d\mu(r)
\ge0
\tag{8}
\]

with the harmless source normalization absorbed into `dmu`. This identifies the most literal source-defined `boundary square` suggested by the clue.

## 2. The positive derivative deletes the explicit-formula carrier

The same calculation exposes why the square does not solve the sign problem. The term in (4)

\[
D_m(r)
:=-\frac12\left[
\frac{m'}m\left(\frac{1-ir}{2}\right)
+
\frac{m'}m\left(\frac{1+ir}{2}\right)
\right]
\tag{9}
\]

is exactly the `T`-independent logarithmic-derivative carrier. After integration against the test transform, this is the block converted by Wong's explicit formula into the zero contribution together with the finite-prime, conductor/polar and archimedean contributions.

But

\[
\partial_\tau D_m(r)=0.
\tag{10}
\]

Hence the operation that exposes the independent positive boundary square simultaneously removes the term whose logarithmic derivative sees the divisor. This is the pointwise version of the height-filter obstruction in `WP-237`, now with the additional information that the surviving height variation has its own exact positive-square theorem.

The distinction is important. The phase `S(r)` still occurs in (6), so height variation is not information-free: the full family in `tau` can encode the boundary scattering phase. What fails is the attempted implication from **positivity of that boundary response** to positivity of the logarithmic-derivative/Weil block. The next matched control shows that the square sign itself is insensitive to divisor location.

## 3. Meromorphic inner-factor control changes the divisor without changing the square theorem

Center the spectral variable so that the unitary axis is `Re z=0`. Let `M_0(z)` be any scalar meromorphic scattering function satisfying the two structural properties used by the square argument,

\[
M_0(z)M_0(-z)=1,
\qquad
|M_0(ir)|=1.
\tag{11}
\]

Assume the usual real symmetry as well. For `a>0` chosen away from the zero/pole divisor of `M_0`, define

\[
C_a(z)
:=
\left(\frac{z-a}{z+a}\right)^2.
\tag{12}
\]

This elementary meromorphic inner/CDD factor obeys

\[
C_a(z)C_a(-z)=1,
\qquad
|C_a(ir)|=1,
\qquad
C_a(0)=1,
\qquad
C_a(z)\to1
\quad(|z|\to\infty).
\tag{13}
\]

It also has a double zero at `z=a` and a double pole at `z=-a`. Therefore

\[
M_a(z):=M_0(z)C_a(z)
\tag{14}
\]

preserves the reciprocal symmetry, real symmetry, boundary unitarity, central normalization and large-parameter normalization relevant to the direct boundary-square calculation, while its divisor differs from that of `M_0` by an explicitly off-unitary-axis zero/pole pair.

Nevertheless for every real `r,tau`,

\[
\left|1+M_a(ir)e^{-ir\tau}\right|^2\ge0
\tag{15}
\]

for exactly the same algebraic reason as before. The logarithmic derivative, in contrast, changes by

\[
\frac{C_a'}{C_a}(z)
=
\frac{4a}{z^2-a^2},
\tag{16}
\]

which is precisely the additional divisor information introduced by (12).

Thus boundary-square positivity plus the elementary scattering symmetries used to prove it cannot determine whether the meromorphic divisor lies on the unitary axis. The matched control can move divisor data off that axis while all pointwise inequalities of the form (15) remain tautologically valid.

## 4. What the control does and does not prove

The factor `C_a` is a **matched meromorphic scattering control**, not a claim that `M_a` is the scattering matrix of an automorphic quotient or that the full modified Maaß--Selberg norm (4) remains nonnegative for every admissible truncation. Realizability imposes additional global constraints, and those constraints are a legitimate place for a stronger theorem to live.

The control proves the narrower statement needed here: the positivity of the direct height derivative follows only from the unitary boundary phase and survives divisor-changing inner factors that preserve those same boundary symmetries. Therefore any proof that tries to infer Weil positivity from the square (6) alone is missing a hypothesis strong enough to exclude the control.

This leaves two genuinely different possibilities open. First, the **full** positive truncated norm may contain a source-realizability restriction in its `T`-independent finite part that rules out the CDD freedom. Second, an operator-level truncation/boundary construction may couple the scalar normalizer to noncentral local or archimedean structure before taking the scalar sign. Neither is supplied by (6).

## 5. Relation to the existing obstruction chain

`WP-237` proved that linear operations in the Arthur height cannot internally resolve the `T`-independent explicit-formula block. `WP-287` then showed that arbitrary nonlinear post-processing of the scalar height profile gives no escape if the output is still required to be a linear Weil-type distribution.

The present result attacks a different apparent escape left by the clue: perhaps one should not try to isolate the zero block algebraically, but instead use the **geometric sign of the boundary response itself**. Equation (6) shows that this response really is positive and canonical. Equations (12)--(16) then show why that positivity is too universal: it is compatible with off-axis divisor modifications.

So the negative conclusion is stronger than `the derivative kills D`. The source supplies an exact positive boundary square, but its sign theorem lives one derivative away from the logarithmic-derivative information that distinguishes the Weil divisor.

## 6. Prior art and novelty boundary

No novelty is claimed for the Maaß--Selberg relation, Arthur truncation, the unitary-axis scattering relation, or Wong's use of the logarithmic derivative in an explicit formula. Wong's Remark 5.2 gives (4), and his Lemma 5.1/Section 5 gives the positive truncated distribution. `WP-237` already records the resulting separation into a `T`-independent explicit-formula block and `T`-dependent boundary terms.

No novelty is claimed for meromorphic inner/Blaschke factors or for the general phenomenon that scattering unitarity and analyticity can admit divisor-changing CDD factors. This is classical complex/scattering theory; the original Castillejo--Dalitz--Dyson ambiguity and later scattering literature are the appropriate historical boundary.

A targeted literature check around Maaß--Selberg height variation, scattering phase, inner factors and CDD ambiguity did not identify the Mathia-specific statement as a named theorem. That is not a historical novelty proof. The durable delta here is the exact **falsification interface** for `weil_positivity`: differentiate Wong's source-positive Maaß--Selberg norm, expose the boundary response as a square, then show with an explicit divisor-changing inner factor that this square theorem cannot carry the missing zero-location sign.

## 7. Aggressive falsification

**Could the positivity of the whole `N_T`, rather than its derivative, exclude the control?** Possibly. The finding does not claim otherwise. The CDD control is matched only to the hypotheses used by the boundary-square argument. A theorem using the full finite part of `N_T` would be new input and lies outside this no-go.

**Could knowledge of the complete `tau`-dependent square recover `S(r)`?** Yes in principle. The family contains the boundary phase. But recovering `S` and then applying a source-dependent operation that produces `S'/S` is not a consequence of the positivity of the square. It falls back under the source-forcing and target-independence gates of `WP-237`/`WP-287` unless an independent geometric theorem selects that operation and its sign.

**Does the CDD factor violate automorphic Euler-product structure?** In general yes; automorphic realizability is intentionally not assumed in the matched control. Therefore the result does not rule out a theorem whose essential hypothesis is precisely that source-realizability/Euler--Gamma structure. It rules out arguments that use only the direct boundary-square sign and the scattering symmetries preserved by (13).

**Could one choose `a` on the unitary axis instead?** That is unnecessary. The purpose is to exhibit a control with the same boundary-square positivity but a changed off-axis divisor. Any `a>0` away from the baseline divisor does so explicitly.

**Is the square merely an algebraic rewrite with no geometric meaning?** No. It is the derivative of the actual truncated Eisenstein `L^2` norm supplied by the Maaß--Selberg geometry. The obstruction is precisely that this genuine geometric positivity is more universal than the arithmetic divisor condition we need.

## Consequence for `weil_positivity`

The direct Arthur-height boundary-layer route is now sharply classified:

\[
\boxed{
\text{Maaß--Selberg norm}
\xrightarrow{\partial_{\log T}}
\text{positive boundary square}
\quad\text{while}\quad
\partial_{\log T}(m'/m)=0.
}
\tag{17}
\]

The square is a real source-derived positive object, but its sign survives meromorphic inner-factor changes that alter the scattering divisor off the unitary axis. It therefore cannot by itself yield the global Weil positivity statement.

The surviving Maaß--Selberg/trace-formula search is correspondingly narrower: it must exploit a source-defined coupling to the `T`-independent logarithmic-derivative block, a realizability theorem that removes the inner/CDD freedom for the exact arithmetic normalizer, or an operator-level finite--archimedean construction before scalar boundary response is taken. A direct appeal to positivity or monotonicity of the height boundary layer is no longer an open mechanism.
