# PF-169 — all Margulis-short central squared-resolvent blocks are trace-summable

**Status:** `EXACT-DERIVED + LITERATURE-AUDITED + POSITIVE/BOUNDARY`. PF-138 proves that every sufficiently far closed Margulis-thin core is a canonical consecutive-block separator, with at most `O(P^0.525)` such cores for a fixed left exterior prime label `P`. PF-146 proves that on a fixed central subcollar the matched prime/shift **squared** relative resolvent is trace class with norm `O(P^-3 L^3)`. These two estimates can be assembled: after choosing one sufficiently small fixed central half-width, the orthogonal direct sum over **all** closed Margulis-short cores is trace class, and its escaping tail tends to zero in trace norm. Thus infinite multiplicity of the central short-collar blocks is not an obstruction to the global squared-resolvent `S_1` route. The uncut surface problem remains open because Dirichlet decoupling removes collar/body transmission and localization commutators.

## Claim

Let

\[
\mu_*:=2\operatorname{arsinh}1
\]

be the short-curve threshold used in PF-138, and let `S` be the set of essential simple closed geodesics `eta` of the exact prime flute satisfying

\[
L_\eta:=\ell(\eta)\le \mu_*.
\tag{1}
\]

For each `eta`, let `eta_+` be the corresponding simple geodesic in the exact all-composite shift clone under the canonical marking, with length `L_{\eta,+}`. There exists a fixed `R>0` such that the central Fermi subcollars

\[
C_{\eta,R}=(-R,R)\times\mathbb S^1
\]

and their matched clone subcollars are defined for every `eta in S`. Put Dirichlet conditions at `r=+-R`, use the common-measure identification of PF-127/PF-146, and define

\[
T_\eta
:=
(\Delta_{\eta,+,R}^D+1)^{-2}
-
(\Delta_{\eta,R}^D+1)^{-2}.
\tag{2}
\]

Then

\[
\boxed{
T_{\rm thin}^D
:=
\bigoplus_{\eta\in\mathcal S}T_\eta
\in\mathcal S_1.
}
\tag{3}
\]

More strongly, if `S_{>=Q}` denotes the tail of canonical short separators whose PF-138 left exterior prime label satisfies `P>=Q`, then with `theta=0.525`,

\[
\boxed{
\left\|
\bigoplus_{\eta\in\mathcal S_{\ge Q}}T_\eta
\right\|_{\mathcal S_1}
\le C_R Q^{\theta-2}
=O(Q^{-1.475}),
}
\tag{4}
\]

so the complete escaping central-collar contribution tends to zero in trace norm.

Equation (3) is a statement about the **Dirichlet-decoupled central collar operator**. It does not imply

\[
(\Delta_{X_+}+1)^{-2}-(\Delta_X+1)^{-2}\in\mathcal S_1
\tag{5}
\]

for the uncut surfaces.

## 1. One fixed central width works for the complete short family

For a geodesic of length `L`, the standard collar half-width is

\[
w(L)=\operatorname{arsinh}\frac1{\sinh(L/2)}.
\tag{6}
\]

It is decreasing in `L`. Hence every source geodesic satisfying (1) has

\[
w(L_\eta)\ge w(\mu_*)=\operatorname{arsinh}1.
\tag{7}
\]

PF-138 shows that, outside a finite head, every member of `S` is a canonical consecutive-block separator. For such a separator with left exterior prime label `P`, PF-109 gives

\[
\left|
\log\frac{L_{\eta,+}}{L_\eta}
\right|
\le CP^{-3}.
\tag{8}
\]

Therefore `L_{eta,+}/L_eta ->1` uniformly on the short tail. Choose first any

\[
0<R_0<\operatorname{arsinh}1.
\]

By continuity of `w`, (7)--(8) imply that both the source and clone tail collars contain `(-R_0,R_0)` once `P` is sufficiently large. There are only finitely many remaining short source curves: PF-138 proves that only finitely many distinguished cuffs are short, and for each bounded set of left labels only finitely many canonical blocks satisfy (1). Every matched source/clone pair in this finite set has a positive collar width. Shrinking `R_0` finitely many times therefore gives one fixed

\[
\boxed{R>0}
\tag{9}
\]

valid for every pair.

The short source geodesics are pairwise disjoint by the collar theorem at the threshold `mu_*`. Their matched topological classes are also pairwise disjoint, so their target geodesic representatives have disjoint standard collars as well. Thus the central blocks in (2) form honest orthogonal direct sums on both sides.

## 2. PF-146 plus the PF-138 counting bound is absolutely summable

PF-146 applies on the fixed central width (9). On every tail canonical separator it gives

\[
\|T_\eta\|_{\mathcal S_1}
\le
C_R P^{-3}L_\eta^3.
\tag{10}
\]

Since `L_eta<=mu_*`,

\[
\boxed{
\|T_\eta\|_{\mathcal S_1}
\le C_R' P^{-3}.
}
\tag{11}
\]

PF-138 gives, for the same left exterior label `P`,

\[
N(P)\le C P^\theta,
\qquad
\theta=0.525,
\tag{12}
\]

where `N(P)` counts **all** canonical separators below the threshold (1), not merely a selected pinching subsequence. Therefore

\[
\begin{aligned}
\sum_{\eta\in\mathcal S_{\rm tail}}
\|T_\eta\|_{\mathcal S_1}
&\le
C\sum_{P\ {\rm prime}}N(P)P^{-3}\\
&\le
C\sum_{P\ {\rm prime}}P^{\theta-3}\\
&\le
C\sum_{m\ge3}m^{\theta-3}
<\infty,
\end{aligned}
\tag{13}
\]

because `theta-3=-2.475<-1`. The finite head contributes only a finite trace norm, by the same PF-146 fixed-collar estimate with a finite bound on the corresponding length ratios.

For operators on an orthogonal Hilbert direct sum, the singular values of the direct sum are the multiset union of the singular values of the blocks. Hence

\[
\left\|\bigoplus_\eta T_\eta\right\|_{\mathcal S_1}
=
\sum_\eta\|T_\eta\|_{\mathcal S_1}
\tag{14}
\]

whenever the right-hand side is finite. Equations (13)--(14) prove (3).

No cancellation between different collars is used. The conclusion is therefore stronger than conditional convergence of a trace or determinant expansion: the complete decoupled central family is absolutely summable in the trace norm itself.

## 3. The escaping central family vanishes in trace norm

The same estimate gives a quantitative tail. For `Q` sufficiently large,

\[
\begin{aligned}
\left\|
\bigoplus_{\eta\in\mathcal S_{\ge Q}}T_\eta
\right\|_{\mathcal S_1}
&\le C\sum_{P\ge Q}P^{\theta-3}\\
&\le C' Q^{\theta-2}.
\end{aligned}
\tag{15}
\]

This proves (4). In particular, the proliferation of canonical short curves established in PF-138 cannot by itself accumulate PF-146's local square-resolvent defect into a non-trace-class central direct sum. The `P^-3` projective length stability beats the unconditional `P^0.525` multiplicity envelope by a wide margin.

The factor `L_eta^3` in PF-146 is not even needed for convergence; bounding it by `mu_*^3` already suffices. Any additional pinching only improves the local trace budget.

## 4. What this closes in the operator route

The accepted `CLUE-shift-clone-wave-operator-equivalence` leaves the global condition (5) as one sufficient route to complete wave operators via Kato--Rosenblum and the Birman--Kato invariance principle. PF-146 had shown trace class one central collar at a time but deliberately left an infinite-summation issue.

PF-169 removes that issue for the **complete fixed-central closed-thin block family**:

\[
\boxed{
\text{all short central Dirichlet blocks}
\quad\Longrightarrow\quad
\mathcal S_1\text{-summable, with vanishing trace-norm tail}.}
\tag{16}
\]

A future failure of the global squared-resolvent gate therefore cannot be blamed merely on having infinitely many PF-138 short cores whose independent central contributions add up too slowly.

What remains is structurally different. Passing from the direct sum (3) to the uncut surface requires controlling the complementary body, the outer parts of collars, boundary transmission, cutoff commutators, and the repeated interaction created when Dirichlet interfaces are removed. Those terms are not contained in `T_thin^D`. An infinite family of individually small localization errors could still fail to be trace-summable even though the central blocks themselves satisfy (3).

PF-169 also does not improve the first-resolvent endpoint. PF-112 still excludes local `S_1` for the first relative resolvent of genuinely different two-dimensional metrics, and PF-150 still shows that a squared-resolvent `S_1` statement alone cannot force first-resolvent `S_r` below `r=2`.

## 5. Adversarial controls

The conclusion survives the following checks only in its stated decoupled form.

1. **All short cores, not a chosen subsequence.** The multiplicity input is PF-138's count of every canonical separator satisfying `L<=mu_*`; the finite distinguished-cuff sector is added separately.
2. **Uniform collar width.** PF-146 cannot be summed with a constant depending on a growing central width. Section 1 fixes one `R>0` once and for all. The statement does not concern full collars of width `w(L_eta)`.
3. **Clone width.** A source curve at the threshold can have a slightly longer clone. Equation (8), continuity of `w`, and a strict choice `R<arsinh(1)` give a uniform tail margin; finitely many exceptions are absorbed by shrinking `R`.
4. **No hidden orthogonality assumption on the uncut surface.** Orthogonality is exact only after the explicit Dirichlet decoupling into disjoint central subcollars. PF-169 makes no direct-sum decomposition claim for the global Laplacian.
5. **No trace cancellation.** Equation (13) sums trace norms, so signs of traces or spectral-shift contributions are irrelevant.
6. **No scattering conclusion.** Kato--Rosenblum becomes available only after proving the fixed uncut global difference (5). PF-169 proves one summable sector of a possible localization argument, not (5).

## 6. Prior-art and novelty audit

No novelty is claimed for the collar theorem, the trace-ideal direct-sum identity (14), Schatten ideals, or the fact that sufficiently high resolvent-power differences can cross a trace-class threshold in elliptic problems. Behrndt--Langer--Lotoreichik, *Trace formulae and singular values of resolvent power differences of self-adjoint elliptic operators*, J. London Math. Soc. 88 (2013), 319--337, DOI `10.1112/jlms/jdt012`, is already recorded in S17/PF-146 as representative prior art for the last point; it treats smooth-domain boundary-condition perturbations rather than this degenerating infinite-type metric comparison.

A directed audit for trace-class resolvent-power estimates on degenerating hyperbolic collars and infinite orthogonal sums did not locate a theorem that supplies the project-specific combination (3)--(4). Search absence is not a novelty claim. The durable content here is the exact synthesis of two already-persisted prime-flute estimates:

\[
\boxed{
\text{PF-138: }N(P)=O(P^{0.525})
\quad+\quad
\text{PF-146: }\|T_\eta\|_1=O(P^{-3}L_\eta^3)
\quad\Longrightarrow\quad
\bigoplus_\eta T_\eta\in\mathcal S_1.
}
\tag{17}
\]

The external collar and resolvent-power theories supply classical background; the all-short-family trace summability is a project-specific consequence of the exact prime/shift estimates.

## 7. Falsification core

A later adversary can check PF-169 through a short chain:

1. verify PF-138's classification and count `N(P)=O(P^0.525)` for every source closed geodesic with `L<=mu_*`, together with finiteness of the short distinguished-cuff head;
2. verify PF-109/PF-146's uniform tail estimate `|log(L_+/L)|=O(P^-3)` and PF-146's fixed-central bound `||T_eta||_1<=C_R P^-3 L^3`;
3. choose one strict `R<arsinh(1)` and check that the clone tail collars also contain this subcollar, then shrink `R` to handle the finite head;
4. use `L<=mu_*` to remove the `L^3` factor and sum `N(P)P^-3`;
5. verify the standard direct-sum identity (14) for trace-class blocks;
6. check that the tail integral estimate gives exponent `theta-2=-1.475` in (4);
7. refuse any inference from the Dirichlet direct sum to the uncut global operator without separate transmission/commutator estimates.

Failure of steps 1--5 would refute the trace-summability claim. Failure of a later global localization argument would not refute PF-169; it would identify the remaining obstruction outside the central short-collar blocks.

## Research consequence

The operator branch of the wave-equivalence clue can now be narrowed. The canonical closed-thin geometry has two independent favorable properties: PF-138 makes its optimized geometric wave-weight budget summable, while PF-169 makes its fixed-central **squared-resolvent** blocks trace-summable. Both routes now point to the same unresolved location: **global body/interface assembly under one fixed uncut identification**.

Accordingly, further operator work should target transmission/localization terms and the complementary body rather than re-estimating the isolated central collars or worrying that their sheer multiplicity defeats trace class. A proof that those remaining terms are `S_1`-summable would establish the global squared-resolvent gate; a negative result must exhibit an actual non-trace-class assembly mechanism outside the decoupled central family.