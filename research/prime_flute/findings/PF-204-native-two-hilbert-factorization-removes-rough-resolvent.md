# PF-204 — native two-Hilbert-space factorization removes the rough pulled resolvent from the cuff endpoint

**Status:** `EXACT-DERIVED + ENDPOINT-FACTORIZATION + POSITIVE/BOUNDARY`. PF-203 shows that the unsmoothed exact-area pantwise map gives a globally bi-Lipschitz, area-preserving identification and an exact relative-resolvent form with no separate cuff surface term, but its common-space formula uses the resolvent of the pulled measurable divergence-form metric. That rough resolvent is **not algebraically unavoidable**. Keeping the source and target hyperbolic Laplacians on their native smooth surfaces gives an exact two-Hilbert-space factorization

\[
R_gU_0-U_0R_+
=
(dR_g)^*\,M_{C_0}\,P_{F_0}\,dR_+,
\]

where `U_0` is the area-preserving composition unitary, `P_{F_0}` is the a.e. cotangent pullback by the PF-203 bi-Lipschitz map, and `C_0=A_0-I` is the same cotangent defect as in PF-203. Thus both resolvent-gradient factors are native smooth hyperbolic resolvents; the nonsmoothness of the identification is isolated in a bounded order-zero cotangent transport. This materially sharpens the physical-cuff endpoint gate, but does **not** prove weak trace class: Ponge's `Q u P` theorem does not allow one to discard an arbitrary bounded transport inserted next to the `L\log L` coefficient, and the piecewise-smooth transport must still be localized with uniform or prime-summable critical constants. The true PF-138 short-collar splice remains separate and open.

## Claim

Let

\[
F_0:X\longrightarrow X_+
\]

be the unsmoothed exact-area prime/shift identification of PF-203. Write

\[
H_g=L^2(X,d\mu_g),
\qquad
H_+=L^2(X_+,d\mu_+),
\]

and let

\[
U_0:H_+\to H_g,
\qquad
U_0\phi=\phi\circ F_0.
\tag{1}
\]

PF-203 proves that `F_0` preserves area, so `U_0` is unitary. Let

\[
R_g=(\Delta_g+1)^{-1},
\qquad
R_+=(\Delta_++1)^{-1},
\tag{2}
\]

where both Laplacians are the **native smooth hyperbolic Laplacians** on their respective surfaces. Define

\[
G_g=dR_g,
\qquad
G_+=dR_+.
\tag{3}
\]

Because `F_0` is bi-Lipschitz, Rademacher's theorem gives `DF_0` almost everywhere and the covector pullback

\[
P_{F_0}:L^2(T^*X_+,g_+)	o L^2(T^*X,g),
\qquad
(P_{F_0}\alpha)_x=(DF_0(x))^*\alpha_{F_0(x)},
\tag{4}
\]

is bounded and boundedly invertible. Area preservation means no additional density multiplier is present.

As in PF-203, put

\[
h_0=F_0^*g_+,
\qquad
h_0^*(\eta,\beta)=g^*(A_0\eta,\beta),
\qquad
C_0=A_0-I.
\tag{5}
\]

Then the exact two-space resolvent defect is

\[
\boxed{
R_gU_0-U_0R_+
=
G_g^*\,M_{C_0}\,P_{F_0}\,G_+.
}
\tag{6}
\]

Equivalently, with

\[
R_0:=U_0R_+U_0^{-1},
\tag{7}
\]

PF-203's common-space pulled resolvent,

\[
\boxed{
R_0-R_g
=-G_g^*M_{C_0}P_{F_0}G_+U_0^{-1}
=-G_g^*M_{C_0}\,dR_0.
}
\tag{8}
\]

Since the left side of (8) is self-adjoint and `C_0` is self-adjoint on cotangent fibers, the adjoint identity is also valid,

\[
R_0-R_g
=-(dR_0)^*M_{C_0}G_g,
\tag{9}
\]

which is the operator form of PF-203's weak formula.

The content of (6) is not weak-`S_1` membership. Its endpoint consequence is the sharper reduction

\[
\boxed{
\text{rough pulled resolvent}
\quad\longrightarrow\quad
\text{native smooth resolvents + bounded piecewise cotangent transport}.
}
\tag{10}
\]

Thus a future physical-cuff proof may work directly with `G_g` and `G_+`; it need not first develop a critical Cwikel theorem for the globally rough operator `\Delta_{h_0}`. The unresolved operator is instead the mixed critical product in (6).

## 1. Exact derivation from the two native quadratic forms

Take `f in H_+` and `z in H_g`, and set

\[
u=R_+f,
\qquad
v=R_gz.
\tag{11}
\]

By self-adjointness of the two resolvents and unitarity of `U_0`,

\[
\begin{aligned}
\langle (R_gU_0-U_0R_+)f,z\rangle_g
&=\langle f,U_0^{-1}v\rangle_+
  -\langle U_0u,z\rangle_g.
\end{aligned}
\tag{12}
\]

The target resolvent equation gives

\[
\langle f,U_0^{-1}v\rangle_+
=q_+(u,U_0^{-1}v)
+\langle u,U_0^{-1}v\rangle_+,
\tag{13}
\]

while the source resolvent equation gives

\[
\langle U_0u,z\rangle_g
=q_g(U_0u,v)
+\langle U_0u,v\rangle_g.
\tag{14}
\]

The `L^2` terms in (13)--(14) are equal by unitarity, so

\[
\langle (R_gU_0-U_0R_+)f,z\rangle_g
=q_+(u,U_0^{-1}v)-q_g(U_0u,v).
\tag{15}
\]

The weak chain rule for a bi-Lipschitz map gives

\[
d(U_0u)=P_{F_0}\,du
\quad\text{a.e.}
\tag{16}
\]

and change of variables through the area-preserving `F_0` gives

\[
q_+(u,U_0^{-1}v)
=\int_X
h_0^*\bigl(P_{F_0}du,dv\bigr)\,d\mu_g
=\int_X
g^*\bigl(A_0P_{F_0}du,dv\bigr)\,d\mu_g.
\tag{17}
\]

Meanwhile

\[
q_g(U_0u,v)
=\int_X
g^*\bigl(P_{F_0}du,dv\bigr)\,d\mu_g.
\tag{18}
\]

Subtracting (18) from (17) yields

\[
\langle (R_gU_0-U_0R_+)f,z\rangle_g
=\int_X
g^*\bigl(C_0P_{F_0}G_+f,G_gz\bigr)\,d\mu_g,
\tag{19}
\]

which is exactly (6).

No derivative of `C_0`, no derivative of the jump across a decomposition cuff, and no resolvent of a rough coefficient operator enters this derivation. The cuff family has area zero and the two native forms already encode the smooth geometry on their respective surfaces.

## 2. The cotangent transport is bounded at exactly the available regularity

PF-203 proves global bi-Lipschitz bounds

\[
K^{-1}|\xi|_{g_+}
\le |(DF_0)^*\xi|_g
\le K|\xi|_{g_+}
\tag{20}
\]

for one finite `K` after changing representatives on a null set. Together with area preservation this gives

\[
\boxed{
\|P_{F_0}\alpha\|_{L^2(T^*X,g)}
\le K\|\alpha\|_{L^2(T^*X_+,g_+)},
}
\tag{21}
\]

and the inverse estimate follows from `F_0^{-1}`. Therefore the interface nonsmoothness enters (6) through a **bounded order-zero transport**, not through loss of closedness or loss of first-order Sobolev control.

This observation is useful but not sufficient for the critical ideal. An arbitrary bounded operator between the two order-`-1` factors cannot simply be removed from

\[
G_g^*M_{C_0}P_{F_0}G_+
\tag{22}
\]

by the ideal property: neither `G_g` nor `G_+` is itself a critical compact half-factor globally, and PF-195 already rules out the naive route that splits the coefficient and tries to control the two one-sided weak-`S_2` factors from endpoint mass alone.

The gain is instead structural. On each open pant interior `F_0` is smooth, so after a smooth local source/target identification the corresponding branch of `P_{F_0}G_+` is a transported order-`-1` elliptic factor. The only failure of a single global smooth pseudodifferential description occurs where the one-sided germs meet at the physical cuffs. Thus the analytic interface question has been moved to a sharply localized order-zero transport/reassembly problem.

## 3. What the physical-cuff endpoint must now prove

For a local coefficient piece `C_\alpha` near one physical cuff, equation (6) suggests the target estimate

\[
q\!\left(
G_g^*M_{C_\alpha}P_{F_0}G_+
\right)
\le K_\alpha\|C_\alpha\|_{L\log L},
\tag{23}
\]

with `K_\alpha` uniform or cheap enough that the PF-196/PF-198 prime-summable coefficient budget survives the infinite family.

PF-197/PF-201 prove the corresponding statement when both critical factors can be transported to one fixed smooth local model and the middle operator is just matrix multiplication. Equation (6) shows that the physical-cuff extension need **not** solve critical regularity for `R_0`; it must instead justify one of the following, or an equivalent mechanism:

1. split the coefficient into branchwise pieces and extend each smooth branch of the identification across the cuff with critical constants that remain uniformly or prime-summably controlled;
2. prove a two-manifold/Fourier-integral variant of the critical `Q u P` estimate in which the bounded cotangent transport is retained explicitly;
3. find a different exact factorization that absorbs `P_{F_0}` into order-`-1` factors without falling back to the PF-195 one-sided endpoint loss.

A sharp characteristic-function split is not automatically harmless. Although the cuff itself has area zero and `C_0` may be restricted measurably to the two sides, a proof that introduces shrinking smooth cutoffs or branch extensions must track the associated operator constant. Equation (23), not mere boundedness of `P_{F_0}`, is the remaining critical statement.

The true PF-138 Margulis-short collars are independent of this reduction. Their open issue is still the **coefficient budget of the canonical exact-area body/core splice** identified by PF-177/PF-183, not the regularity of the decomposition-cuff transmission.

## 4. Relation to PF-203 and the smooth-seam alternative

PF-203 gives the common-space identity

\[
R_0-R_g
=-G_0^*M_{C_0}G_g,
\qquad
G_0=dR_0,
\tag{24}
\]

in weak form, with `R_0` associated to a measurable divergence-form metric. PF-204 does not replace or contradict that identity. Equation (8) rewrites the same operator using the native target resolvent:

\[
G_0=P_{F_0}G_+U_0^{-1}.
\tag{25}
\]

Thus the two architectures are exactly equivalent before ideal estimates are applied. The choice is analytic:

- use PF-203 and seek a rough-coefficient critical theorem for `G_0`; or
- use PF-204 and keep `G_+` smooth while paying explicitly for `P_{F_0}`.

PF-182/PF-202 remain a third, deliberately smoothed comparison. Their arbitrarily small seam coefficient budget is valid, but the shrinking-family critical operator constant remains a separate issue if that route is chosen. PF-204 shows that global smoothing is not required merely to keep **both resolvents smooth** in the algebraic factorization.

## Prior-art and novelty audit

Two-Hilbert-space scattering with an identification operator is classical; S16 records Güneysu--Thalmaier's geometric use of such identifications for quasi-isometric Riemannian metrics, and the older Belopol'skii--Birman framework treats wave operators for self-adjoint operators acting in different Hilbert spaces. The weak Sobolev chain rule for bi-Lipschitz maps, cotangent pullback, change of variables, and form resolvent identities are also standard. No novelty is claimed for those ingredients.

A directed literature search around two-Hilbert-space resolvent comparison, geometric identification operators, and critical Cwikel/Solomyak estimates found the expected classical two-space scattering framework and the already-audited critical `L\log L` machinery, but no source was used as a theorem that would imply (23) for the PF piecewise identification. Search absence is not a novelty theorem.

The project-specific exact deduction is (6): **PF-203's concrete area-preserving bi-Lipschitz identification converts the first-resolvent defect into a cross-surface product of the two native smooth gradient resolvents with one explicit cotangent transport.** This removes the rough pulled resolvent as a mandatory analytic input and isolates what a genuine interface endpoint estimate has to control.

## Falsification and boundary checks

A later adversary can test PF-204 by:

1. checking the direction of `U_0` and the sign in (6) directly from the two resolvent equations (13)--(15);
2. verifying the a.e. chain rule (16) for the PF-203 bi-Lipschitz map and that area preservation makes `U_0` unitary without a density factor;
3. checking the pullback-metric identity (17) against PF-203's definition of `A_0`;
4. verifying that `P_{F_0}` is bounded on `L^2` covectors using only global bi-Lipschitz control and the area formula;
5. multiplying (6) by `U_0^{-1}` and comparing (8)--(9) with PF-203's common-space weak identity;
6. refusing to infer weak `S_1` from boundedness of `P_{F_0}` alone;
7. refusing to invoke Ponge's smooth pseudodifferential theorem across the cuff jump unless a branchwise extension/localization or another theorem supplies the required quantitative critical constants;
8. keeping the true-short-collar splice outside the scope of the interface reduction.

PF-204 would be overclaimed if read as proving any of the following, none of which is asserted:

- the full or interface relative first resolvent belongs to `S_{1,\infty}`;
- `P_{F_0}G_+` is one global smooth pseudodifferential operator on the source surface;
- an arbitrary bounded order-zero transport may be inserted into Ponge's theorem at no cost;
- branchwise smooth extension constants are uniform over all physical cuffs;
- PF-202's smoothed-seam operator constant is controlled;
- the PF-183 endpoint conservative short-collar splice exists;
- weak `S_1` implies ordinary trace class or any scattering/determinant/RH conclusion.

## Consequences for the research line

PF-203 removed the artificial decomposition-seam term at the form level. PF-204 now removes a second artificial requirement: **the unsmoothed route does not force the critical proof to use a rough target resolvent.** Both native hyperbolic resolvents can remain smooth, and all identification roughness is exposed in the explicit bounded cotangent transport `P_{F_0}`.

The accepted weak-trace clue should therefore stop asking whether a two-manifold factorization exists; equation (6) supplies it exactly. The next analytic test is whether the physical-cuff family satisfies a critical estimate of the form (23) without losing the PF-196 effective-area currency. Independently, the true-short-collar endpoint splice remains the geometric gate. Only after those two sectors and the lower-order/global identification bookkeeping are controlled can the complete first relative resolvent be promoted from PF-190's strong-`S_r`, `r>1`, information to weak `S_1`.