# PF-182 — area-preserving decomposition-cuff seams can be smoothed at summable weighted cost

**Status:** `EXACT-DERIVED + CLASSICAL-SYMPLECTIC-PASTING + POSITIVE/BOUNDARY`. PF-179--PF-181 construct an exact-area prime/shift comparison on each one-cusp pant through the Lambert body, artificial split, and full cusp, but deliberately leave the closed finite-cuff interfaces outside the quantitative global statement. Those **distinguished decomposition cuffs are not a remaining obstruction**. The PF-179 finite-cuff trace is one-parameter: after returning from the normalized Lambert chart, it depends only on the matched cuff pair and not on the neighboring cuff. PF-180 is the identity near that genuine boundary and PF-181 acts only in the cusp. Hence adjacent pants induce the same zero-twist-equivariant boundary map on every shared cuff. In signed Fermi area coordinates, any such common boundary diffeomorphism has an explicit two-sided area-preserving collar germ. A relative generating-function cutoff then replaces each one-sided pant map by that common germ in an arbitrarily thin collar while preserving area exactly and without a first-derivative penalty proportional to the inverse collar width. Because the support may be chosen arbitrarily thin cuff by cuff, its source- and target-side inverse-unit-ball weighted metric cost can be made absolutely summable, even when a distinguished cuff passes through regions of poor injectivity radius. Thus the canonical decomposition seams can be made smooth, zero-twist coherent, and quantitatively negligible in the PF-175 budget. The live geometric gate is narrower: splice the already assembled area-preserving body map to the PF-177 gauges on the **true PF-138 Margulis-short collars**, which need not coincide with the decomposition cuffs, and prove the remaining weighted body/collar budget. No global Schatten conclusion, wave/scattering equivalence, or RH consequence is claimed.

## Claim

Let

\[
C_n\subset X,
\qquad
C_n^+\subset X_+
\]

be the `n`th matched distinguished decomposition cuffs of the exact prime flute and the all-composite shift clone, with lengths

\[
L_n=2a_n,
\qquad
L_n^+=2a_n^+,
\qquad
\delta_n:=a_n^+-a_n\to0.
\tag{1}
\]

Take the exact-area pantwise comparison obtained from PF-179 after the PF-180 split synchronization and the PF-181 cusp handoff. Before smoothing the shared finite-cuff interfaces, let

\[
B_n:C_n\longrightarrow C_n^+
\tag{2}
\]

be the boundary map induced from either adjacent pant.

Then, after a harmless common smoothing in arbitrarily small neighborhoods of the two seam-foot endpoints on each cuff when necessary, the following hold.

1. `B_n` is well defined independently of which adjacent pant is used and commutes with the canonical zero-twist reflection.
2. In arclength coordinates on source and target cuffs, if `b_n=B_n'>0`, then on the tail
   \[
   \boxed{
   \|\log b_n\|_{L^\infty(C_n)}\le C\delta_n.
   }
   \tag{3}
   \]
3. For every prescribed sequence `q_n>0` with `sum q_n<infinity`, one can choose pairwise disjoint two-sided cuff neighborhoods `U_n` and modify the pantwise map only in `U_n` so that the modified maps agree on a whole neighborhood of each `C_n`, glue to a smooth global map across all distinguished cuffs, and preserve hyperbolic area exactly.
4. The modification can be chosen with tail metric distortion
   \[
   \boxed{
   \delta_{\mathrm{cuff},n}\le C\delta_n
   }
   \tag{4}
   \]
   in the correction zone, after shrinking `U_n` as needed.
5. Writing
   \[
   W_X(x)=\mu_X(B_X(x,1))^{-1},
   \qquad
   W_{X_+}(y)=\mu_{X_+}(B_{X_+}(y,1))^{-1},
   \tag{5}
   \]
   the neighborhoods may simultaneously be chosen so that for every fixed `r>=1`,
   \[
   \boxed{
   \sum_n\int_{U_n}W_X\,\delta_{\mathrm{cuff},n}^{\,r}\,d\mu_X
   +
   \sum_n\int_{F(U_n)}W_{X_+}\,\delta_{\mathrm{cuff},n}^{\,r}\,d\mu_{X_+}
   <\infty.
   }
   \tag{6}
   \]
   In fact the correction support can be chosen so that its two weighted contributions are bounded by `C_r q_n` cuff by cuff.

Consequently **smooth area-preserving gluing across the canonical pant decomposition does not consume the remaining PF-175 weighted budget**. Equation (6) concerns only the cuff-pasting correction; it does not assert the missing weighted estimate for the unchanged body map in the PF-138 true-short-collar regions.

## 1. PF-179 already gives one common finite-cuff trace

PF-179 constructs each Lambert transport

\[
F^{\mathrm{vol}}_{a,a'}:Q(a)\to Q(a')
\tag{7}
\]

from a one-parameter source/target pair. In the parameter-independent Fermi area chart it is exactly area preserving and `1+O(a'-a)` bilipschitz. The finite-cuff branch is mapped to the target finite-cuff branch, and the fixed corner interpolation may be chosen by one deterministic rule depending only on `(a,a')`.

Returning from the normalized Lambert chart to a physical pentagon only conjugates this map by hyperbolic dilations/isometries. Intrinsic arclength on the finite cuff is unchanged by those normalizations. Therefore the induced half-cuff map depends only on

\[
(a_n,a_n^+),
\tag{8}
\]

not on the second cuff of the pant. This is the area-preserving analogue of the one-parameter trace mechanism isolated for the earlier comparison in PF-124.

PF-180 postcomposes by Hamiltonian split corrections which are **identically the identity near the genuine opposite Lambert boundary**, so they leave the finite-cuff trace unchanged. PF-181 modifies only the fixed cusp handoff and likewise leaves every finite cuff untouched. Hence the two pants adjacent to `C_n` arrive with the same half-cuff trace.

Reflect the half-cuff construction across the canonical seam marking on each pant. As in PF-124, the resulting full-cuff map satisfies

\[
\boxed{
B_n\circ J_{L_n}
=J_{L_n^+}\circ B_n,
}
\tag{9}
\]

where `J_L` is the orientation-reversing zero-twist cuff involution fixing the seam feet. Thus there is no boundary-value mismatch to solve.

Because restriction to a boundary tangent cannot have more stretch than the ambient bilipschitz map, PF-179's tail bound gives

\[
e^{-C\delta_n}\le B_n'(s)\le e^{C\delta_n}
\tag{10}
\]

wherever the boundary-face derivative is taken. This proves (3) after the same reflection-equivariant local smoothing at seam feet when needed. The smoothing can be performed simultaneously on the two adjacent sides in a disk whose tangential and normal scales shrink together; the boundary displacement is then `O(delta_n)` times that scale, so the first-derivative cost remains `O(delta_n)`. Its support is absorbed into the arbitrarily small correction neighborhoods chosen below.

The important distinction is that (9) is a **trace statement**, not yet a smooth-germ statement. Two area-preserving maps can agree on a curve while having different transverse shear. The next two sections remove exactly that residual seam issue.

## 2. Every common cuff trace has an explicit common area-preserving germ

Use signed Fermi coordinates around `C_n`, with `s` arclength along the source core and `r` signed normal distance. Set

\[
\boxed{x:=\sinh r.}
\tag{11}
\]

Then on either side of the cuff

\[
\boxed{
g=\frac{dx^2}{1+x^2}+(1+x^2)ds^2,
\qquad d\mu=dx\,ds.}
\tag{12}
\]

The same formula holds on the target in coordinates `(X,S)`. The cuff length enters only through the periodicities `s mod L_n` and `S mod L_n^+`; the local metric coefficients themselves are parameter independent.

Choose a lift of `B_n` satisfying

\[
B_n(s+L_n)=B_n(s)+L_n^+
\tag{13}
\]

and put `b_n(s)=B_n'(s)`. Define on a sufficiently thin **two-sided** signed collar

\[
\boxed{
E_n(x,s)
=\left(\frac{x}{b_n(s)},\,B_n(s)\right).
}
\tag{14}
\]

Its Euclidean Jacobian in the exact area coordinates is

\[
\det
\begin{pmatrix}
1/b_n & -x b_n'/b_n^2\\
0 & b_n
\end{pmatrix}
=1,
\tag{15}
\]

so

\[
\boxed{E_n^*(dX\wedge dS)=dx\wedge ds.}
\tag{16}
\]

At `x=0`, `E_n` is exactly `B_n`. Equation (9) makes the same signed germ compatible with the zero-twist marking from both sides.

By (3), `b_n=1+O(delta_n)` on the tail. The only potentially uncontrolled first-derivative term in (14) is `x b_n'`. Since each `B_n` is a smooth circle diffeomorphism on one compact cuff, `||b_n'||_infinity` is finite cuff by cuff. We are free to choose the collar width `w_n` so small that

\[
\boxed{
w_n\|b_n'\|_\infty\le\delta_n.}
\tag{17}
\]

In the universal metric (12), equations (3), (14), and (17) then give

\[
\boxed{
\operatorname{Bilip}(E_n|_{|x|\le w_n})
\le1+C\delta_n.
}
\tag{18}
\]

No inverse maximal-collar width appears. A distinguished cuff may be very long and its canonical embedded collar may be extremely narrow; we simply choose a still smaller signed neighborhood. Only first derivatives enter the metric deviation, and (17) keeps those derivatives at the already-existing tail scale.

## 3. Relative symplectic localization has no inverse-width first-derivative loss

It remains to replace each original one-sided area-preserving pant germ by `E_n` without changing the map away from the cuff.

The needed local fact is elementary in dimension two.

Let `H` be an area-preserving diffeomorphism of a half-collar

\[
[0,w_0)\times S^1
\tag{19}
\]

with area form `dx wedge ds`, assume `H` fixes the boundary `x=0` pointwise, and suppose `H` is `C^1`-close to the identity. Then for every sufficiently small `w<w_0` there is an area-preserving `H_w` such that

\[
H_w=\operatorname{id}
\quad\text{near }x=0,
\qquad
H_w=H
\quad\text{for }x\ge w,
\tag{20}
\]

and

\[
\boxed{
\|DH_w-I\|\le C\|DH-I\|
}
\tag{21}
\]

with `C` independent of the chosen width `w` after shrinking the initial chart if necessary.

Here is the local proof relevant to this application. The graph of a sufficiently `C^1`-small area-preserving `H` is a Lagrangian graph near the diagonal. In a fixed Weinstein graph chart it is represented by a closed one-form `alpha`. Because `H` fixes `x=0`, `alpha` vanishes there. The restriction map from the half-annulus to its boundary circle detects the only `H^1` period, so `alpha` is exact:

\[
\alpha=dS,
\qquad S|_{x=0}=0.
\tag{22}
\]

The `C^1` smallness and boundary vanishing give, in the same local chart,

\[
|S|\le C\eta x^2,
\qquad
|dS|\le C\eta x,
\qquad
|D^2S|\le C\eta,
\qquad
\eta:=\|DH-I\|.
\tag{23}
\]

Choose a fixed cutoff `chi` with `chi=0` near zero and `chi=1` past two thirds of the unit interval, and set

\[
S_w(x,s)=\chi(x/w)S(x,s).
\tag{24}
\]

The apparently dangerous cutoff terms cancel against the relative vanishing in (23):

\[
\frac1{w^2}|S|+
\frac1w|dS|+|D^2S|
\le C\eta
\qquad(0\le x\le w).
\tag{25}
\]

Hence the Lagrangian graph of `dS_w` defines an area-preserving diffeomorphism `H_w` satisfying (20)--(21). Higher derivatives may depend on `w`; the **first derivative does not**. That is exactly the regularity level entering the metric-deviation integral.

This is a local conservative-pasting argument, not a new general symplectic theorem. Its project-specific importance is equation (25): shrinking a cuff correction to make its weighted measure tiny does not force its metric distortion to blow up.

## 4. Apply the localization independently on the two sides of every cuff

For one side of `C_n`, let `F_{n,+}` be the existing PF-179/PF-180/PF-181 area-preserving pant map in a sufficiently small one-sided cuff neighborhood. Both `F_{n,+}` and `E_n` have boundary value `B_n`. Therefore

\[
H_{n,+}:=E_n^{-1}\circ F_{n,+}
\tag{26}
\]

fixes the boundary pointwise and preserves the source area form.

At the boundary, area preservation plus the common tangent map already forces the same normal scaling. Indeed, if `b=B_n'`, the derivative of either map in area coordinates has triangular form

\[
\begin{pmatrix}
a&0\\c&b\end{pmatrix},
\qquad ab=1,
\tag{27}
\]

so `a=1/b` on both sides. The only possible first-order disagreement is the transverse shear `c`. PF-179's `1+O(delta_n)` bilipschitz bound and (18) force that shear to be `O(delta_n)`. By continuity, after shrinking the one-sided collar if necessary,

\[
\|DH_{n,+}-I\|\le C\delta_n.
\tag{28}
\]

Apply Section 3 with the cutoff orientation reversed: obtain `\widetilde H_{n,+}` equal to the identity near the cuff and equal to `H_{n,+}` outside a thinner collar. Then

\[
\widetilde F_{n,+}:=E_n\circ\widetilde H_{n,+}
\tag{29}
\]

is exactly area preserving, equals `E_n` near the cuff, equals the old pant map away from the correction strip, and remains `1+O(delta_n)` bilipschitz there.

Do the same on the other side. Both corrected maps now equal the **same signed map `E_n` on an open two-sided neighborhood**. They therefore glue smoothly across `C_n` to all orders; no normal-jet matching is left to check. Because the distinguished cuffs form a locally finite disjoint family, the correction neighborhoods can be chosen pairwise disjoint and the construction can be performed simultaneously along the whole infinite decomposition.

A finite initial set of cuffs may be handled with arbitrary finite constants. On the tail the added metric deviation is bounded by (4).

## 5. Arbitrarily thin support makes the weighted seam cost summable

The remaining useful observation is measure-theoretic rather than number-theoretic.

For each fixed cuff `C_n`, choose a compact two-sided tubular neighborhood on which both hyperbolic metrics and their unit-ball-volume functions are smooth. Since `C_n` itself is compact,

\[
W_X<\infty,
\qquad W_{X_+}<\infty
\tag{30}
\]

and both weights are locally bounded on that fixed neighborhood. Consequently the weighted areas of thinner collars tend to zero:

\[
\int_{|x|<w}W_X\,d\mu_X\to0,
\qquad
\int_{|X|<w'}W_{X_+}\,d\mu_{X_+}\to0
\tag{31}
\]

as `w,w'->0`.

Choose the correction neighborhood for cuff `n` small enough to satisfy (17), all local-pasting requirements, disjointness, and also

\[
\int_{U_n}W_X\,d\mu_X
+
\int_{F(U_n)}W_{X_+}\,d\mu_{X_+}
\le q_n.
\tag{32}
\]

This choice is legitimate even if the numerical bound on `W` deteriorates rapidly with `n`; the support width is not required to be uniform. Combining (4) and (32), after taking the tail so `delta_n<=1`, gives for every `r>=1`

\[
\int_{U_n}W_X\,\delta_{\mathrm{cuff},n}^{\,r}d\mu_X
+
\int_{F(U_n)}W_{X_+}\,\delta_{\mathrm{cuff},n}^{\,r}d\mu_{X_+}
\le C_r q_n.
\tag{33}
\]

Summing proves (6). A single support choice with `sum q_n<infinity` works simultaneously for all fixed `r>=1` because `delta_n<=1` on the tail.

This is stronger than merely observing that the decomposition cuffs themselves have measure zero. The smoothing occurs on genuine open neighborhoods, but those neighborhoods can be made quantitatively invisible to the inverse-unit-ball weighted first-derivative budget.

## 6. Consequence for the PF-175 frontier

PF-179--PF-181 left the exact-area route summarized as

\[
\text{body/split/cusp}
+\text{ closed interfaces}
+\text{ final weighted budget}.
\tag{34}
\]

PF-182 removes the **canonical decomposition-cuff** part of the closed-interface term:

\[
\boxed{
\text{common one-parameter cuff trace}
+\text{ explicit area germ}
+\text{ relative conservative localization}
\Longrightarrow
\text{smooth exact-area cuff gluing at summable weighted cost}.}
\tag{35}
\]

The remaining issue is genuinely different. PF-138's complete Margulis-short family consists of geometric short separators which need not be the distinguished pant boundaries. PF-177 supplies an optimized exact-area gauge on the collapsing core of each such collar, but the current body map is not yet proved to agree with those gauges on their outer interfaces. Those true-short collars can cut across the pant decomposition, so equation (35) does not solve their two-dimensional overlap with the body construction.

Accordingly PF-182 does **not** establish the complete PF-175 hypothesis. It says that future work should no longer spend its budget on making the canonical pant seams smooth or area preserving. The live task is now:

\[
\boxed{
\text{splice the global area-preserving body map to every PF-177 true-short-collar gauge}
\quad+\quad
\text{sum the remaining weighted body/collar defect}.}
\tag{36}
\]

If that final task succeeds for every desired `r>1`, PF-175 gives the density-unitary `S_r` conclusion because the global volume ratio is then exactly one. PF-112 still prevents an `S_1` conclusion.

## 7. Prior-art and novelty audit

No novelty is claimed for symplectic collar coordinates, Lagrangian graph descriptions of near-identity symplectomorphisms, Hamiltonian/local conservative perturbations, or smoothing/pasting in the volume-preserving category.

The classical local framework is Alan Weinstein, *Symplectic manifolds and their Lagrangian submanifolds*, Advances in Mathematics 6 (1971), 329--346, DOI `10.1016/0001-8708(71)90020-X`. Its neighborhood theorem supplies the standard interpretation of a sufficiently small symplectomorphism graph as a Lagrangian graph near the diagonal. The relative exactness and cutoff calculation (22)--(25) are written out here because the **width-independent first-derivative estimate** is the part needed by the flute application.

For conservative pasting and localized smoothing more generally, see Pedro Teixeira, *On the conservative pasting lemma*, Ergodic Theory and Dynamical Systems 40 (2020), 1402--1440, DOI `10.1017/etds.2018.81`, together with the earlier conservative-pasting literature discussed there. PF-182 does not import a blanket theorem from that paper; the thin-collar estimate used here is the explicit relative generating-function calculation above.

Directed searches for area-preserving hyperbolic pair-of-pants cuff gluing, symplectic cuff pasting on hyperbolic surfaces, and conservative seam smoothing did not locate the project-specific combination of PF-179's one-parameter prime/shift boundary trace with arbitrary-support inverse-unit-ball weighting. Absence of an exact match is **not** treated as a novelty theorem. The durable custom content is the narrowing statement (35)--(36) for this exact infinite prime/shift decomposition.

## 8. Audit / falsification core

A later adversary can check PF-182 through the following finite chain:

1. inspect PF-179's construction and verify that the finite-cuff boundary map is determined by `(a,a')` alone after conjugating back by the physical Lambert isometries;
2. verify from PF-180 that the split correction is identity near the genuine opposite boundary and from PF-181 that the cusp handoff leaves finite cuffs untouched;
3. reflect the half-cuff trace and check the zero-twist identity (9);
4. in signed Fermi coordinates derive the universal metric/area form (12) and verify directly that (14) has Jacobian one;
5. use (3) and a sufficiently small support width to check the `1+O(delta_n)` metric bound (18);
6. for two area-preserving germs with common boundary trace, verify the triangular derivative constraint (27);
7. in a Weinstein graph chart check the relative vanishing estimates (23), then differentiate the cutoff (24) to verify the width-independent Hessian bound (25);
8. apply the localized map on both sides and check that both become exactly the same `E_n` on an open neighborhood of the cuff;
9. use local boundedness of each unit-ball-volume weight and shrink the `n`th support until (32) holds, then sum (33);
10. do **not** infer any estimate on the untouched PF-138 true-short-collar/body overlap or invoke PF-175 until that remaining global weighted term is controlled.

A failure of steps 1--3 would reopen boundary coherence. A failure of steps 4--8 would reopen exact-area smooth cuff pasting. A failure of step 9 would require a local non-integrability of the unit-ball weight on a fixed compact cuff neighborhood, which cannot occur on a smooth complete hyperbolic surface. Passing all ten gates removes only the canonical decomposition seams from the live PF-175 obstruction.