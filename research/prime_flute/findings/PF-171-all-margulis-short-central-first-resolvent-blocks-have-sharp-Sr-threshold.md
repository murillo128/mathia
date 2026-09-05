# PF-171 — all Margulis-short central first-resolvent blocks have the sharp `S_r`, `r>1`, threshold

**Status:** `EXACT-DERIVED + LITERATURE-AUDITED + POSITIVE/BOUNDARY`. PF-127 proves the sharp first-resolvent Schatten threshold on one fixed central hyperbolic collar: every nontrivial matched collar difference lies in `S_r` for all `r>1` but not in `S_1`, with an explicit norm bound suppressed by the core length. PF-138 classifies and counts every Margulis-short closed core in the prime flute, while PF-109 gives the uniform prime/shift logarithmic length defect. These inputs can be summed over the complete short family. The orthogonal Dirichlet direct sum of **all** fixed-central short-collar first-relative-resolvent blocks belongs to every `S_r`, `r>1`, with a vanishing Schatten tail, and it is not trace class. Thus the full decoupled closed-thin central sector already realizes the sharp two-dimensional threshold. Any failure of the corresponding global `S_r`, `r>1`, conjecture must come from body/interface/uncut assembly rather than from the short central cores, even collectively.

## Claim

Let

\[
\mu_*:=2\operatorname{arsinh}1
\]

and let `S` be the family of essential simple closed geodesics `eta` in the exact prime flute with

\[
L_\eta:=\ell(\eta)\le\mu_*.
\tag{1}
\]

Use the same canonical prime/shift marking and the same fixed central half-width `R>0` constructed in PF-169, so every source/clone pair has matched central collars

\[
C_{\eta,R}=(-R,R)\times\mathbb S^1.
\]

Put Dirichlet conditions at `r=+-R`, use the common-measure identification of PF-127, and define

\[
A_\eta
:=
(\Delta_{\eta,+,R}^D+1)^{-1}
-
(\Delta_{\eta,R}^D+1)^{-1}.
\tag{2}
\]

Then for every `r>1`,

\[
\boxed{
A_{\rm thin}^D
:=
\bigoplus_{\eta\in\mathcal S}A_\eta
\in\mathcal S_r.
}
\tag{3}
\]

If `S_{>=Q}` denotes the tail of canonical short separators whose PF-138 left exterior prime label is at least `Q`, then with `theta=0.525`,

\[
\boxed{
\left\|
\bigoplus_{\eta\in\mathcal S_{\ge Q}}A_\eta
\right\|_{\mathcal S_r}^{r}
\le C_{R,r}Q^{\theta+1-3r},
}
\tag{4}
\]

and therefore

\[
\boxed{
\left\|
\bigoplus_{\eta\in\mathcal S_{\ge Q}}A_\eta
\right\|_{\mathcal S_r}
\le C_{R,r}Q^{-3+(\theta+1)/r}
\longrightarrow0.
}
\tag{5}
\]

The trace endpoint is sharp:

\[
\boxed{A_{\rm thin}^D\notin\mathcal S_1.}
\tag{6}
\]

Equations (3)--(6) concern the **Dirichlet-decoupled fixed-central collar operator**. They do not imply the same ideal membership for the uncut full-surface first relative resolvent.

## 1. PF-127 gives an `S_r` budget for every short canonical block

For a matched central collar with source core length `L`, clone length `L_+`, and

\[
t=\log(L_+/L),
\]

PF-127 proves, for every fixed `r>1`,

\[
\|A_{L,L_+}^{(R)}\|_{\mathcal S_r}^{r}
\le
C_{R,r,t_0}|t|^rL^{2r-1}
\tag{7}
\]

whenever `|t|<=t_0`. PF-109 gives uniformly for every tail canonical separator with left exterior label `P`, including pinching separators,

\[
|t|=O(P^{-3}).
\tag{8}
\]

Every member of the short family satisfies `L<=mu_*`, hence

\[
\boxed{
\|A_\eta\|_{\mathcal S_r}^{r}
\le C_{R,r}P^{-3r}
}
\tag{9}
\]

on the canonical tail. The `L^{2r-1}` factor could only improve this bound when a core pinches; no pinching rate is needed for summability.

PF-169 already constructs one fixed `R>0` valid simultaneously for the complete source/clone short family. Its finite exceptional head therefore causes no uniform-width problem here. Each head block belongs to `S_r`, `r>1`, by PF-127, and only finitely many such blocks occur.

## 2. PF-138 multiplicity is far below the Schatten budget

PF-138 proves that outside a finite head every `mu_*`-short closed geodesic is a canonical consecutive-block separator and that the number `N(P)` with a fixed left exterior prime label `P` obeys

\[
N(P)\le CP^\theta,
\qquad
\theta=0.525.
\tag{10}
\]

For an orthogonal Hilbert direct sum and `r>0`, Schatten norms satisfy

\[
\left\|\bigoplus_j T_j\right\|_{\mathcal S_r}^{r}
=
\sum_j\|T_j\|_{\mathcal S_r}^{r}
\tag{11}
\]

whenever the right side is finite. Combining (9)--(11),

\[
\begin{aligned}
\sum_{\eta\in\mathcal S_{\rm tail}}
\|A_\eta\|_{\mathcal S_r}^{r}
&\le
C\sum_{P\ {\rm prime}}N(P)P^{-3r}\\
&\le
C\sum_{P\ {\rm prime}}P^{\theta-3r}\\
&\le
C\sum_{m\ge3}m^{\theta-3r}
<\infty,
\end{aligned}
\tag{12}
\]

because for every `r>1`,

\[
\theta-3r<-2.475<-1.
\]

Adding the finite head proves (3). Restricting the same estimate to `P>=Q` gives

\[
\sum_{P\ge Q}P^{\theta-3r}
\le C_rQ^{\theta+1-3r},
\tag{13}
\]

which proves (4)--(5).

This is stronger than merely knowing that each pinching collar is individually benign. Even after including **every** Margulis-short canonical core with PF-138's unconditional multiplicity envelope, the first-relative-resolvent mass is absolutely summable in `S_r^r` for every exponent strictly above one.

## 3. The direct sum still fails exactly at trace class

The convergence argument cannot be continued to `r=1`, because PF-127's local threshold is genuinely sharp rather than an artifact of a loose summation estimate.

PF-005 supplies a sequence of four-consecutive-prime canonical separators with

\[
L_\eta\longrightarrow0.
\tag{14}
\]

Hence all sufficiently far members lie in `S`. PF-170 proves that for every sufficiently far consecutive-prime block the exact all-composite shift changes its four-point cross-ratio strictly:

\[
\log\frac{\chi_{P+1}}{\chi_P}>0.
\tag{15}
\]

Since `L(chi)=4 asinh(sqrt(chi))` is strictly increasing, these pinching blocks satisfy

\[
L_{\eta,+}\ne L_\eta.
\tag{16}
\]

PF-127 then gives

\[
A_\eta\notin\mathcal S_1
\tag{17}
\]

for each such nontrivial block. If the full direct sum `A_thin^D` were trace class, compression by the orthogonal projection onto any one collar summand would also be trace class. Equations (16)--(17) contradict that. This proves (6).

Thus the complete decoupled central family has the exact threshold

\[
\boxed{
A_{\rm thin}^D\in\bigcap_{r>1}\mathcal S_r,
\qquad
A_{\rm thin}^D\notin\mathcal S_1.
}
\tag{18}
\]

No appeal to cancellation between collars is involved.

## 4. Relation to PF-169 and the global operator frontier

PF-169 proves the stronger trace-class statement for the **squared** relative resolvent on the same complete central family. PF-171 shows that the corresponding first-resolvent family already reaches the optimal local two-dimensional threshold directly, without passing through PF-147's abstract square-root implication.

This matters particularly for `1<r<2`. PF-150 proves that a global squared-resolvent `S_1` statement alone cannot abstractly force a first-resolvent exponent below `2`. PF-171 shows that the actual hyperbolic short-collar geometry nevertheless crosses the entire interval `1<r<2` once the local PF-127 estimate is combined with the PF-138 multiplicity count. Therefore the sub-`2` obstruction, if it exists globally, is **not** present in the central short-collar blocks, even after their full infinite summation.

The remaining problem is the one excluded from the direct-sum model: complementary pant/body pieces, outer collar sectors, cutoff commutators, boundary transmission, and repeated head-tail interaction when the Dirichlet interfaces are removed. A global counterexample to `S_r`, `r>1`, must create its singular-value mass in one of those uncut/interface channels. A positive proof must show that they inherit enough summability to preserve the central threshold.

## 5. Adversarial controls

The conclusion uses the following boundaries explicitly.

1. **All short cores, not a selected subsequence.** PF-138 supplies the complete tail classification and the multiplicity bound `N(P)=O(P^0.525)`; short distinguished cuffs form only a finite head.
2. **One fixed central width.** The direct sum uses PF-169's globally valid fixed `R`, not a width growing with collar depth.
3. **Schatten powers are summed correctly.** Equation (12) sums `||A_eta||_r^r`, not the norms themselves.
4. **No illegal endpoint extrapolation.** The estimate is used only for `r>1`. Non-`S_1` comes from PF-127's principal-symbol obstruction plus an explicit nontrivial pinching block, not by substituting `r=1` into an upper bound that was never valid there.
5. **No uncut inference.** Orthogonality is exact only after Dirichlet decoupling of the disjoint central subcollars. Nothing here estimates the transmission or commutator terms created by restoring the full surface.
6. **No arithmetic selector claim.** The entire comparison is with an exact all-composite shift clone. The sharp ideal threshold is therefore a control theorem about geometric/operator stability, not evidence for RH.

## 6. Prior-art and novelty audit

No novelty is claimed for Schatten ideals, orthogonal direct-sum identities, hyperbolic collar separation, or the local critical order-`-2` pseudodifferential threshold. Those ingredients were already literature-audited in PF-112, PF-127, PF-138, and PF-169. Likewise, the Baker--Harman--Pintz exponent used by PF-138 is already anchored in `SOURCES.md`.

A directed audit for Schatten estimates on degenerating hyperbolic collars and relative resolvents did not locate an external theorem that supplies the project-specific combination

\[
\text{PF-127 local }S_r\text{ mass}
+
\text{PF-109 }P^{-3}\text{ matching}
+
\text{PF-138 }P^{0.525}\text{ multiplicity}.
\]

The broader resolvent-power literature, including Behrndt--Langer--Lotoreichik's trace-ideal estimates for elliptic boundary-condition perturbations, does not directly address this infinite family of degenerating metric collars. Search absence is not a novelty claim. The durable content is the exact summation consequence (3)--(6) for the canonical prime/shift geometry.

## 7. Falsification core

A later adversary can check PF-171 through a short chain:

1. verify PF-169's single fixed central width for the complete short family;
2. verify PF-127's local bound `||A_eta||_r^r <= C |t_eta|^r L_eta^(2r-1)` for every `r>1` and its non-`S_1` endpoint when `L_+ != L`;
3. insert PF-109's uniform `|t_eta|=O(P^-3)` and `L_eta<=mu_*`;
4. insert PF-138's complete-tail count `N(P)=O(P^0.525)` and sum the Schatten `r`-powers;
5. check the tail exponent `theta+1-3r` and then take the `r`th root for (5);
6. use PF-005 to obtain short consecutive-prime blocks and PF-170 to guarantee that sufficiently far matched shift blocks have `L_+ != L`;
7. compress a hypothetical trace-class direct sum to one such block to contradict PF-127;
8. refuse any inference from the Dirichlet central direct sum to the uncut global operator without separate body/interface estimates.

## Research consequence

The accepted sharp-Schatten clue can now be narrowed decisively. The **entire Margulis-short central sector**, including all short cores at once, already satisfies the conjectured sharp classification `S_r` for every `r>1` and fails `S_1`. In particular, the difficult interval `1<r<2` is not blocked by zero systole, collar pinching, or the multiplicity of short canonical separators.

Future work on the full-surface first relative resolvent should therefore stop re-estimating isolated or collectively summed central short collars. The live question is whether body/interface/transmission terms preserve this threshold when the Dirichlet decomposition is removed, or whether one of those genuinely global channels produces a new singular-value obstruction.