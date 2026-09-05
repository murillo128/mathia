# PF-172 — finite collar recoupling is trace class, but pinching does not shrink its zero-mode trace budget

**Status:** `LITERATURE+DERIVED + EXACT-MODEL + DECISIVE-NEGATIVE/METHOD-BOUNDARY`. Classical elliptic boundary theory says that changing a smooth compact boundary condition in dimension two produces a first-resolvent difference that is already trace class. Applied to a finite cut-and-reglue problem, this means that **any finite family of collar/body interfaces is microlocally too benign to obstruct the conjectured `S_r`, `r>1`, relative-resolvent threshold**. However, the collapsing hyperbolic collar has a surviving angular zero mode whose radial operator is exactly independent of the core length. For an explicit Dirichlet cut through a fixed-width collar, the trace norm of the recoupling correction therefore has a positive lower bound independent of the shrinking interface length. Thus one cannot restore the infinitely many PF-138 interfaces by summing absolute single-surface gluing corrections and hoping that pinching itself supplies summability. A successful global prime/shift proof must exploit **relative cancellation between the two transmission problems before taking Schatten norms**, or use another genuinely collective assembly argument.

## Claim

Fix `R>0` and let

\[
C_{L,R}=(-R,R)\times\mathbb S^1,
\qquad
 g_L=dr^2+L^2\cosh^2r\,d\theta^2,
\qquad L>0,
\tag{1}
\]

with Dirichlet conditions at the two outer circles `r=+-R`. Let `Delta_L` be the positive Laplacian on the **uncut** collar. Let

\[
\Delta_L^{\rm cut}
=
\Delta_{L,(-R,0)}^D\oplus\Delta_{L,(0,R)}^D
\tag{2}
\]

be the orthogonal sum obtained by additionally imposing Dirichlet conditions on the central circle `r=0`. Define the first-resolvent recoupling correction

\[
G_L
:=
(\Delta_L+1)^{-1}
-
(\Delta_L^{\rm cut}+1)^{-1}.
\tag{3}
\]

Then:

\[
\boxed{G_L\ge0,\qquad G_L\in\mathcal S_1.}
\tag{4}
\]

More importantly, there is a constant `c_R>0`, depending only on `R`, such that

\[
\boxed{
\|G_L\|_{\mathcal S_1}\ge c_R
\qquad\text{for every }L>0.
}
\tag{5}
\]

In particular,

\[
\boxed{
\liminf_{L\to0}\|G_L\|_{\mathcal S_1}\ge c_R>0,
}
\tag{6}
\]

even though the physical length of the cut interface is exactly `L` and tends to zero.

The same boundary-ideal argument gives the following finite-interface consequence. On any compact two-dimensional truncation, restoring transmission across finitely many smooth cut circles changes the Dirichlet-decoupled first resolvent by a trace-class operator. Therefore a finite collar/body interface cannot create a local `S_r`, `r>1`, obstruction. What fails is a different inference: **there is no generic collapse factor in the absolute trace norm that can be summed over infinitely many pinching interfaces.**

For the prime/shift program this means that a decomposition of the full relative resolvent of the schematic form

\[
R_+-R
=
(R_+^D-R^D)
+
(G_+-G)
\tag{7}
\]

cannot close the global Schatten problem by estimating `||G_+||_1+||G||_1` interface by interface. PF-171 controls the first term on the complete central short family. The second term must instead be estimated **relatively**, so that the source/clone common transmission modes cancel before the infinite sum is taken.

## 1. Finite transmission recoupling is trace class in dimension two

Introduce a third operator by imposing Neumann rather than Dirichlet conditions at the artificial cut `r=0`, while retaining the same Dirichlet conditions at `r=+-R`:

\[
\Delta_L^{\rm Ncut}
=
\Delta_{L,(-R,0)}^{DN}
\oplus
\Delta_{L,(0,R)}^{ND}.
\tag{8}
\]

The three quadratic forms have the same energy integral. Their form domains satisfy

\[
\operatorname{dom}q_{\rm cut}
\subset
\operatorname{dom}q_{\rm uncut}
\subset
\operatorname{dom}q_{\rm Ncut},
\tag{9}
\]

because the Dirichlet cut forces both traces to vanish, the uncut collar only requires the two traces to agree, and the Neumann-decoupled form imposes no trace matching. Hence the standard form ordering gives

\[
\Delta_L^{\rm Ncut}
\le
\Delta_L
\le
\Delta_L^{\rm cut}.
\tag{10}
\]

After adding `1` and inverting,

\[
0
\le
G_L
\le
(\Delta_L^{\rm Ncut}+1)^{-1}
-(\Delta_L^{\rm cut}+1)^{-1}.
\tag{11}
\]

The operator on the right is the direct sum of two ordinary Neumann-versus-Dirichlet resolvent differences on smooth compact two-dimensional half-collars, with the outer boundary condition held fixed. Classical boundary pseudodifferential theory places such a first-resolvent difference in weak Schatten class

\[
\mathcal S_{(n-1)/2,\infty}
\tag{12}
\]

for a second-order elliptic operator in dimension `n`. Thus for `n=2`,

\[
\mathcal S_{1/2,\infty}
\subset
\mathcal S_1,
\tag{13}
\]

since the singular values decay as `O(k^-2)`. Equivalently, the mixed-boundary Krein resolvent term is a singular Green operator of boundary order `-2`, and its singular values are governed by the one-dimensional interface rather than the two-dimensional interior.

The right side of (11) is therefore positive trace class. Positivity and ideal domination imply (4).

Nothing in this step uses collapse. It is a purely local dimension/boundary statement. The same form sandwich applies to any finite collection of smooth artificial interfaces on a compact two-dimensional truncation, so finite transmission restoration is always trace class at the first resolvent.

## 2. The angular zero mode is exactly independent of the core length

Trace class does **not** mean that the trace norm becomes small when the interface circle shrinks.

The positive collar Laplacian separates in angular Fourier modes. On the `m`th mode it has the radial expression

\[
H_{m,L}
=
-\frac1{\cosh r}\partial_r
\bigl(\cosh r\,\partial_r\bigr)
+
\frac{(2\pi m)^2}{L^2\cosh^2r}
\tag{14}
\]

on `L^2((-R,R),cosh(r)dr)` after the harmless normalization of the angular basis. For the constant angular mode `m=0`,

\[
\boxed{
H_{0,L}=H_0
:=-\frac1{\cosh r}\partial_r
\bigl(\cosh r\,\partial_r\bigr),
}
\tag{15}
\]

which contains **no `L` at all**.

Both the uncut and cut boundary conditions preserve the Fourier decomposition. Let `P_0` denote the projection onto the constant angular mode. Then

\[
P_0G_LP_0
\simeq
(H_0+1)^{-1}
-
(H_0^{\rm cut}+1)^{-1}
=:G_{0,R},
\tag{16}
\]

where `H_0` acts on `(-R,R)` with outer Dirichlet boundary and `H_0^{cut}` is the direct sum on `(-R,0)` and `(0,R)` with an additional Dirichlet condition at `0`.

The one-dimensional operator `G_{0,R}` is positive and nonzero. Positivity follows from the same form inclusion, and it is nonzero because imposing a Dirichlet node at `r=0` strictly changes the resolvent. Since the interval is compact, `G_{0,R}` is trace class. Put

\[
\boxed{c_R:=\operatorname{Tr}G_{0,R}>0.}
\tag{17}
\]

Equation (16) shows that this exact positive trace is independent of `L`. Since `G_L` itself is positive trace class,

\[
\begin{aligned}
\|G_L\|_{\mathcal S_1}
&=\operatorname{Tr}G_L\\
&\ge
\operatorname{Tr}(P_0G_LP_0)\\
&=c_R,
\end{aligned}
\tag{18}
\]

which proves (5)--(6).

Thus the physical interface length

\[
\ell(\{r=0\})=L\to0
\tag{19}
\]

is not a small parameter for the absolute first-resolvent recoupling norm. The transverse modes become expensive as `L` shrinks, but the one mode that survives the collapse carries an order-one transmission correction.

## 3. Why this changes the infinite-interface strategy

PF-171 proves that the **relative metric** first-resolvent difference on the complete Dirichlet-decoupled family of Margulis-short central collars is in every `S_r`, `r>1`, with a vanishing tail. That result benefits from a different fact: on a matched prime/shift collar, the `m=0` relative metric block cancels exactly, while every nonzero mode sees the small source/clone length defect.

The present recoupling problem has the opposite absolute behavior. If one forgets the relation between the source and clone and estimates the uncut correction on each surface separately, the collapse leaves an order-one zero-mode budget. Consequently a proof pattern of the form

\[
\sum_{\eta\in\mathcal S}
\bigl(
\|G_{\eta,+}\|_1+
\|G_{\eta}\|_1
\bigr)
<\infty
\tag{20}
\]

cannot be justified merely from `L_eta->0`; the local model (18) shows that shrinking interface length provides no generic summability factor at all.

This does **not** prove that the actual prime-flute infinite transmission correction diverges. Equation (20) is only a deliberately crude absolute strategy, and it throws away exactly the structure most likely to matter. The correct object is the **difference**

\[
G_{\eta,+}-G_\eta,
\tag{21}
\]

or, more invariantly, the difference of the corresponding Poisson/Dirichlet-to-Neumann/Krein transmission terms under one common prime/shift identification. The zero mode may cancel there, just as it does in PF-127/PF-146/PF-171, and the remaining mismatch may inherit the already established `O(P^-3)` or other summable tail scales.

Therefore the operator frontier can be narrowed from

> “Are boundary transmission terms locally too singular?”

into the much more precise question

> “After writing the two uncut resolvents with one common interface calculus, does the **relative transmission operator** acquire a summable source/clone defect once the common zero mode is cancelled?”

That is a genuinely relative problem. Separate single-surface trace-class estimates cannot decide it.

## 4. Relation to the sharp-Schatten clue

PF-112 fixes the interior metric endpoint: a genuine two-dimensional local metric perturbation makes the first relative resolvent non-`S_1`, although `S_r`, `r>1`, remains possible. PF-171 then proves that every Margulis-short **central** relative block, summed over the complete family, already attains that sharp threshold.

PF-172 removes one possible interpretation of the remaining interface difficulty. A smooth finite transmission interface in dimension two is not another order-`-2` interior metric obstruction; its resolvent correction is already trace class. Hence no new local exponent barrier above `1` is hiding at a single collar/body seam.

At the same time, (18) shows why this classical local trace-class fact does not solve the global problem. The norm need not decay with the collapsing circumference, so an infinite number of individually trace-class interfaces can still defeat absolute summation. The missing input is not stronger local pseudodifferential smoothing. It is **relative tail decay of the transmission mismatch**.

This points to a concrete next derivation: express the prime and shift uncut resolvents using the same cut geometry and the same boundary space, subtract the two Krein/Schur-complement formulas algebraically, and estimate the differences of the Poisson and Dirichlet-to-Neumann factors *before* applying Schatten norms. Any proof that instead bounds the two gluing operators separately has discarded the cancellation needed to beat the zero-mode ledger.

## 5. Prior art and novelty audit

The trace-ideal part is classical and is **not** claimed as new. Behrndt, Langer, and Lotoreichik, *Trace formulae and singular values of resolvent power differences of self-adjoint elliptic operators*, J. London Math. Soc. 88 (2013), 319--337, DOI `10.1112/jlms/jdt012`, records the classical Birman estimate

\[
(A_N-\lambda)^{-m}-(A_D-\lambda)^{-m}
\in
\mathcal S_{(n-1)/(2m),\infty},
\tag{22}
\]

and in particular the first-resolvent `O(k^-2)` singular-value decay in dimension two. Gerd Grubb, *The mixed boundary value problem, Krein resolvent formulas and spectral asymptotic estimates*, J. Math. Anal. Appl. 382 (2011), 339--363; arXiv:1104.0785, gives the corresponding mixed-boundary Krein formula and sharp `j^{-2/(n-1)}` asymptotics when only part of the boundary condition is changed. These theorems explain (11)--(13).

The Mathia-specific content is the exact specialization to the standard collapsing hyperbolic collar and the resulting method boundary:

\[
\boxed{
\text{finite interface recoupling is }S_1
\quad\text{but}\quad
\text{its absolute zero-mode budget need not shrink with }L.
}
\tag{23}
\]

A directed search around degenerating hyperbolic collars, Dirichlet/Neumann resolvent differences, and boundary-condition trace ideals found the standard degeneration and boundary-calculus literature but no theorem whose purpose is the prime-flute conclusion (20)--(21). Search absence is not a novelty claim. The durable result here is the elementary exact zero-mode lower bound combined with the classical trace-ideal theorem, used only to rule out an invalid infinite-summation strategy.

## 6. Adversarial controls and falsification core

A later reviewer can audit PF-172 through the following chain.

1. Check the three form domains in (9). The coupled form must require equality of the two central traces but must not impose an extra derivative condition at form level.
2. Verify the form order (10) and resolvent order (11).
3. Check the boundary-ideal exponent from the primary literature: in dimension `n=2` and for first resolvents, Dirichlet-versus-Neumann/mixed-boundary differences have singular values `O(k^-2)`, hence are trace class.
4. Verify that positivity plus domination by a positive trace-class operator implies `G_L in S_1`.
5. Perform the Fourier decomposition of the exact collar Laplacian and check that the `m=0` radial operator (15) is independent of `L` after normalization of the `L^2` measure.
6. Verify that the uncut and cut one-dimensional zero-mode resolvents are genuinely different, hence `c_R>0`.
7. Compress the positive trace-class operator to the zero mode to obtain (18).
8. Do **not** promote (18) into a claim that the actual full prime/shift relative transmission difference diverges. The finding rules out absolute per-surface summation; it does not rule out relative cancellation.
9. Do **not** infer wave-operator failure, resonance inequality, determinant failure, or any RH consequence. Those remain beyond the claim.

A refutation must therefore break either the classical boundary-condition ideal input, the form sandwich, or the exact `m=0` independence. Showing that the **relative** source/clone transmission difference is summable would not refute PF-172; it would realize the cancellation mechanism that this finding says is necessary.

## Research consequence

The uncut first-resolvent frontier is now sharper. **Single interfaces are not the problem, and shrinking interfaces are not the solution.** Finite recoupling is already trace class, but the angular zero mode prevents a generic collapse-driven trace budget. The next useful operator calculation should therefore be a common-boundary Krein/Schur-complement formula for the prime/shift pair in which the source and clone are subtracted before norms are taken.

If that relative transmission difference inherits summable tail decay, PF-171 can plausibly be promoted from the Dirichlet central direct sum toward the full `S_r`, `r>1`, operator. If it does not, the obstruction must be exhibited as a genuinely relative infinite-interface or body-propagation effect rather than as the local pseudodifferential order of one seam.