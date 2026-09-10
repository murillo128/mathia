# WI-233 — selected bow depth is inherited by any density-matched same-window screen

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + STRUCTURAL-RIGIDITY + BOOTSTRAP-CANDIDATE`.

WI-231 proves a first-harmonic count--depth tariff by discarding the selected bow's radial information through the lower bound `B_1 >= 2M`. WI-232 then combines that weakened tariff with exact local Riemann--von Mangoldt density matching, obtaining a same-window complementary budget `R=O(log T)` and hence a screen depth at least `2 vartheta-o(1)` for a bow of size `M=T^{vartheta+o(1)}`.

The selected radial information can be retained exactly. Let the selected right-half-plane bow labels have normalized radial depths

\[
a_j^{\rm sel}:=\frac{(\beta_j-\tfrac12)L_T}{d_T},
\qquad 1\le j\le M,
\]

in the WI-231 normalization, and put

\[
A_T:=\frac1M\sum_{j=1}^M\cosh a_j^{\rm sel}\ge1.
\tag{1}
\]

At the first reciprocal harmonic the selected labels and their compulsory functional-equation mirrors have one common vertical phase, so after rotating that phase away their exact amplitude is

\[
B_1=2\sum_{j=1}^M\cosh a_j^{\rm sel}=2MA_T.
\tag{2}
\]

Suppose a complementary population of `R` zero labels counted with multiplicity, all from the same local interval, cancels that first harmonic to error at most `eta M`, and let `a_max` be the largest normalized radial depth among its off-line pairs, taking `a_max=0` when the complement is purely critical. Every critical-line complementary label has modulus one and every off-line functional-equation pair of multiplicity `mu` contributes modulus at most `2 mu cosh a_max`. Therefore

\[
|S_1^{\rm comp}|\le R\cosh a_{\max}.
\tag{3}
\]

The cancellation hypothesis and (2) give the exact strengthened tariff

\[
\boxed{
R\cosh a_{\max}
\ge 2\sum_{j=1}^M\cosh a_j^{\rm sel}-\eta M
=M(2A_T-\eta).
}
\tag{4}
\]

This strictly contains WI-231 equation (23), which follows only after replacing `A_T` by `1`.

For a density-matched same-window bow in the WI-232 setting, let

\[
\ell_0:=\log\frac{T_0}{2\pi},
\qquad
\Delta:=\frac{4\pi}{\ell_0},
\qquad
M=T^{\vartheta+o(1)},
\qquad 0<\vartheta<\frac12.
\tag{5}
\]

WI-232 proves from the local Riemann--von Mangoldt formula that the complementary budget satisfies

\[
R=O(\log T).
\tag{6}
\]

In this normalization `d_T=2L_T/ell_0`, so physical horizontal displacement and radial depth are related exactly by

\[
\beta-\frac12=\frac{2a}{\ell_0}.
\tag{7}
\]

Define the selected effective radial log-depth

\[
\delta_{\rm eff}(T)
:=\frac{2}{\ell_0}\log A_T.
\tag{8}
\]

Since `A_T>=1` and `eta=o(1)`, eventually `2A_T-eta>=A_T`. From (4), `R>0` and

\[
\cosh a_{\max}\ge\frac{M A_T}{R}.
\tag{9}
\]

Using `arcosh x >= log x` for `x>=1`, equations (6)--(9) imply

\[
\begin{aligned}
\beta_{\max}^{\rm screen}-\frac12
&=\frac{2a_{\max}}{\ell_0}\\
&\ge
\frac{2\log M}{\ell_0}
-\frac{2\log R}{\ell_0}
+\frac{2\log A_T}{\ell_0}\\
&=\boxed{2\vartheta+\delta_{\rm eff}(T)-o(1)}.
\end{aligned}
\tag{10}
\]

Thus the screen does not merely pay the `2 vartheta` cardinality tax of WI-232. It **inherits the selected bow's average exponential radial depth on top of that tax**.

## 1. Positive-density selected depth gives an additive physical tariff

The effective depth in (8) has a direct geometric interpretation. Suppose there are fixed constants `q>0` and `delta_0>0` such that at least `qM` selected right-half-plane labels satisfy

\[
\beta_j-\frac12\ge\delta_0.
\tag{11}
\]

By (7), these labels have

\[
a_j^{\rm sel}\ge\frac{\delta_0\ell_0}{2}.
\]

Hence

\[
A_T
\ge q\cosh\!\left(\frac{\delta_0\ell_0}{2}\right)
\ge\frac q2\exp\!\left(\frac{\delta_0\ell_0}{2}\right),
\tag{12}
\]

and therefore

\[
\boxed{
\delta_{\rm eff}(T)\ge\delta_0-o(1).
}
\tag{13}
\]

Combining (10) and (13), any density-matched same-window first-harmonic screen must contain a zero with

\[
\boxed{
\beta_{\max}^{\rm screen}-\frac12
\ge\delta_0+2\vartheta-o(1).
}
\tag{14}
\]

Every nontrivial zeta zero satisfies `0<beta<1`, so its right-half displacement from the critical line is strictly less than `1/2`. Consequently a same-window screen of the stated kind is impossible whenever

\[
\boxed{
\delta_0+2\vartheta>\frac12.
}
\tag{15}
\]

This is stronger than the generic WI-232 fixed-power obstruction `vartheta>1/4` whenever a positive-density fraction of the selected bow is already bounded a fixed distance away from the critical line. It quantifies a defect-amplification principle: selected radial defect and count-saturation depth do not substitute for one another; at the first reciprocal harmonic they add.

The endpoint `delta_0+2 vartheta=1/2` is not claimed. At equality, the `o(1)` loss in (14) is material and one would need the kind of zero-free-edge precision used in WI-232, together with matching precision for the selected depth distribution, before asserting a contradiction.

## 2. Exact origin of the additive law

No new analytic-number-theory estimate enters (4). The strengthening is the triangle inequality before WI-231 discards `cosh a_j^{sel}`.

Write the complementary first-harmonic contribution as

\[
S_1^{\rm comp}
=S_1^{\rm crit}+S_1^{\rm off}.
\]

If the critical contribution contains multiplicities `nu_l` and the off-line contribution contains functional-equation pairs of multiplicities `mu_k` and radial depths `b_k`, then

\[
|S_1^{\rm comp}|
\le\sum_l\nu_l+2\sum_k\mu_k\cosh b_k.
\tag{16}
\]

With

\[
R:=\sum_l\nu_l+2\sum_k\mu_k,
\qquad
b_k\le a_{\max},
\]

one gets (3). On the other hand

\[
|B_1+S_1^{\rm comp}|\le\eta M
\]

and `B_1>0`, so

\[
|S_1^{\rm comp}|
\ge B_1-\eta M.
\tag{17}
\]

Equations (2), (3), and (17) are exactly (4). The later `2 vartheta` term is supplied independently by the logarithmic same-window count reservoir (6). The additive structure therefore comes from multiplying the two independent amplification factors

\[
\frac{M}{R}
\quad\text{and}\quad
A_T,
\]

then taking logarithms in the conversion from hyperbolic amplitude to physical horizontal depth.

This also clarifies equality and near-equality. Saturating (4) requires, simultaneously, near-maximal modulus from almost all complementary radial weight, almost antiparallel phase alignment of the complementary first-harmonic vector against the selected bow vector, and negligible cancellation loss inside the complementary population. Saturating (10) additionally requires the same-window count reservoir to be near its maximal logarithmic scale and the `arcosh`/log conversion to lose only lower-order terms. These conditions are diagnostics, not a theorem that all near-extremizers have a unique configuration.

## 3. What this does and does not bootstrap

Equation (14) is a genuine **defect-to-deeper-defect** implication. If a density-matched selected bow already contains positive-density radial defect at physical depth `delta_0`, a local zero screen cannot merely reproduce that depth: it must move at least one complementary zero an additional `2 vartheta-o(1)` toward the strip edge.

This is not yet an iterable proof of zero defect. The conclusion forces only one deepest screening zero, whereas a second application would need a new density-matched selected population with reciprocal-phase coherence and a positive-density depth hypothesis. Neither property follows from (14). In particular, the forced screen need not form another bow, and vertically remote or prime-side cancellation remains outside the local interface. The result is therefore a bootstrap **candidate/interface**, not a completed iteration.

Likewise, the result does not identify the entire uncertified complement with off-line zeros. Multiple critical-line zeros and pure proof slack remain distinct categories in the global simple-critical problem. Here `R` is only the local complementary label budget in the WI-231/WI-232 bow stress test.

## 4. Prior art, provenance, and novelty audit

The external bow geometry remains the one used in WI-231--WI-232: James Maynard and Kyle Pratt, *Half-Isolated Zeros and Zero-Density Estimates*, International Mathematics Research Notices 2024:19 (2024), 12978--13014, arXiv:2206.11729, DOI `10.1093/imrn/rnae191`, Section 8. Their work supplies the slowly varying arithmetic-progression bow motivating this adversarial model; equations (4), (10), and (14) are not attributed to that paper.

The exact local count input `R=O(log T)` and its evidence chain are inherited from WI-232: the Riemann--von Mangoldt error is supported there by Hasanalizade--Shen--Wong, *Counting zeros of the Riemann zeta function*, Journal of Number Theory 235 (2022), 219--241, arXiv:2107.06506. No recent-preprint input from the later near-edge refinement of WI-232 is needed for the present theorem.

A bounded external search around the Maynard--Pratt bow, same-window screening, radial/horizontal depth, reciprocal harmonics, and Fejer/explicit-formula cancellation located the known bow source but no published statement of the additive inheritance law (10) or (14). Absence of a search hit is not evidence of priority, and no priority claim is made.

The own-line novelty boundary is exact. WI-231 proves

\[
R\cosh a_{\max}\ge(2-\eta)M
\]

only after replacing the selected amplitude by its universal minimum `2M`. WI-232 combines that weakened inequality with `R=O(log T)` and proves the `2 vartheta-o(1)` screen-depth law. The durable delta here is to preserve the selected factor

\[
A_T=M^{-1}\sum_j\cosh a_j^{\rm sel}
\]

through the same argument, producing the additive term `delta_eff` and the positive-density corollary (14)--(15). Searches of the current `weil_inertia` corpus for selected radial-depth inheritance found no earlier finding with this statement.

## 5. Audit test and research consequence

The result can be audited without replaying the broader bow program. Check only:

1. WI-231 equation (4): the selected first reciprocal harmonic is `2 sum_j cosh(a_j^{sel})` after phase rotation.
2. The complementary modulus bound (16), with `R` counting zero labels with multiplicity.
3. WI-232's density-matched budget `R=O(log T)` and exact conversion `beta-1/2=2a/ell_0`.
4. The elementary inequalities `arcosh x>=log x` and `cosh x>=e^x/2`.

If any one of these interfaces fails under the same-window screen model, (10) must be withdrawn. Otherwise (10) and the fixed-depth corollary (14)--(15) are exact consequences.

For the research program, the finding sharpens the local exceptional-mass geometry without demanding global Weil positivity. The next useful target is no longer merely to force a deep screen, but to obtain **population information** on that deep screen: enough phase coherence, multiplicity control, or density to feed the inherited-depth tariff a second time. Conversely, a barrier proving that the forced deep labels cannot retain those properties would close this particular bootstrap route cleanly.
