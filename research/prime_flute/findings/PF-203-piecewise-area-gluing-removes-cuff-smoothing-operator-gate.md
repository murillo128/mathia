# PF-203 — piecewise exact-area gluing removes decomposition-cuff smoothing from the form-level endpoint problem

**Status:** `EXACT-DERIVED + OPERATOR-ROUTE-SHARPENING + POSITIVE/BOUNDARY`. PF-179--PF-181 already give exact-area prime/shift maps on each one-cusp pant, synchronize the internal Lambert split, and make the map identical to the standard gauge deep in each cusp. PF-182 then smooths the remaining distinguished decomposition-cuff interfaces in thin collars, and PF-202 shows that those smoothing coefficients can be made arbitrarily summable in the critical `L log L` currency. The present finding isolates a simpler form-level fact: **the smoothing is not required to define the exact relative-resolvent quadratic form.** Before PF-182, adjacent pant maps have the same cuff trace, so they glue to one globally bi-Lipschitz, area-preserving, piecewise-smooth homeomorphism. Pulling the target Laplacian back through that map gives a uniformly elliptic measurable metric and a closed divergence-form quadratic form on the source surface. Its first-resolvent difference has the same exact two-sided coefficient identity as the `rho=1` specialization of PF-175, with no derivative of the coefficient and no separate surface term on the decomposition cuffs. Thus the shrinking-support Cwikel constant left open by PF-202 is **not an unavoidable endpoint gate**: one may instead keep the unsmoothed exact-area identification and treat the physical cuff interfaces as a rough/transmission localization problem. This does not prove weak trace class. In particular, Ponge's smooth pseudodifferential theorem cannot simply be applied across the resulting coefficient jumps, and the true PF-138 short-collar endpoint splice remains a separate geometric budget problem. No scattering, determinant, resonance, or RH consequence is claimed.

## Claim

Let

\[
X=\bigcup_n P_n,
\qquad
X_+=\bigcup_n P_n^+
\tag{1}
\]

be the exact zero-twist prime flute and its exact all-composite shift clone, decomposed into the matched one-cusp pants used in PF-179--PF-182. On each `P_n`, take the exact-area map obtained by:

1. PF-179's area-preserving Lambert transports;
2. PF-180's Hamiltonian synchronization of the artificial Lambert split;
3. PF-181's area-preserving full-cusp handoff to the common deep-cusp gauge;

but **do not** perform PF-182's open-collar smoothing across the distinguished decomposition cuffs.

Call the resulting pantwise maps

\[
F_n:P_n\longrightarrow P_n^+.
\tag{2}
\]

PF-182 proves that the two pants adjacent to each shared distinguished cuff induce the same boundary map `B_n`, including the zero-twist marking. Therefore the quotient gluing of the `F_n` defines a continuous homeomorphism

\[
\boxed{
F_0:X\longrightarrow X_+.
}
\tag{3}
\]

Moreover:

1. `F_0` and `F_0^{-1}` are globally Lipschitz;
2. `F_0` preserves hyperbolic area exactly;
3. the pullback metric
   \[
   h_0:=F_0^*g_+
   \tag{4}
   \]
   is a uniformly elliptic measurable metric on `X`, smooth on the interiors of the pant pieces and allowed to have first-derivative/transverse-germ jumps across the distinguished cuffs;
4. its volume measure agrees exactly with the source measure,
   \[
   \boxed{d\mu_{h_0}=d\mu_g}
   \quad\text{a.e.;}
   \tag{5}
   \]
5. if `A_0` is the positive cotangent endomorphism defined a.e. by
   \[
   h_0^*(\alpha,\beta)=g^*(A_0\alpha,\beta),
   \tag{6}
   \]
   and
   \[
   C_0:=A_0-I,
   \tag{7}
   \]
   then the target Laplacian transported to `L^2(X,d\mu_g)` is the self-adjoint operator associated with the closed form
   \[
   \boxed{
   q_{h_0}(u,v)
   =\int_X g^*(A_0\,du,dv)\,d\mu_g,
   \qquad
   \mathcal D(q_{h_0})=H^1(X).
   }
   \tag{8}
   \]

Write

\[
R_g=(\Delta_g+1)^{-1},
\qquad
R_0=(\Delta_{h_0}+1)^{-1}
\tag{9}
\]

on this common Hilbert space, with `Delta_{h_0}` understood through (8). Then for every `f,z in L^2(X,dmu_g)`, setting

\[
u=R_gf,
\qquad
v=R_0z,
\tag{10}
\]

one has the exact weak identity

\[
\boxed{
\langle (R_0-R_g)f,z\rangle
=-\int_X g^*(C_0\,du,dv)\,d\mu_g.
}
\tag{11}
\]

There is **no additional decomposition-cuff integral in (11)**. The cuffs have two-dimensional measure zero, and the interface transmission condition is encoded by the operator associated with the global closed form (8). If one rewrites the operator piecewise in strong divergence form, flux matching across the cuffs reappears as an operator-domain condition; it is not an extra coefficient perturbation supported on the cuff in the form identity.

Consequently PF-182/PF-202's smooth seam correction is optional for this form-level endpoint architecture. The unresolved distinguished-cuff question is no longer

\[
\text{``can a shrinking smooth seam correction keep a uniform Cwikel constant?''}
\tag{12}
\]

but rather

\[
\boxed{
\text{``can the piecewise-smooth cuff/interface sector in (11) be localized at the critical weak-trace endpoint without smoothing it?''}
}
\tag{13}
\]

Equation (13) is a different analytic gate. It may require a rough-coefficient/interface version of the critical estimate, or a two-manifold/source-target factorization that keeps the original smooth Laplacians on the two surfaces. PF-203 proves neither alternative.

## 1. Matching cuff traces already give a global homeomorphism

PF-179 constructs one-parameter exact-area maps on the Lambert halves and PF-180 modifies them by target-side Hamiltonian corrections which are the identity near each genuine opposite boundary. Hence the induced finite-cuff trace remains the one-parameter trace determined only by the matched cuff pair. PF-181 modifies only the cusp handoff and also leaves finite cuffs untouched.

PF-182 then proves the decisive boundary statement: for each distinguished cuff `C_n`, the two adjacent pants induce the **same** map

\[
B_n:C_n\to C_n^+,
\tag{14}
\]

and the full trace is compatible with the canonical zero-twist reflection. This statement precedes the construction of the common smooth two-sided germ `E_n`; equality of boundary values does not depend on that later smoothing.

Therefore the maps `F_n` agree on every equivalence class used to glue the pants. By the elementary gluing lemma for homeomorphisms on a locally finite cell decomposition, they descend to the continuous bijection (3), and the inverse is obtained by gluing the inverse pant maps. The cusp handoff is already complete by PF-181, so no missing end boundary remains.

This point is deliberately weaker than PF-182. PF-182 upgrades common boundary values to one common **smooth germ** on an open two-sided cuff neighborhood. PF-203 keeps only the common values and accepts a transverse derivative jump.

## 2. The piecewise map remains globally bi-Lipschitz

On the tail PF-179 has bilipschitz constant `1+O(delta_n)` on the one-parameter Lambert bodies. PF-180's synchronization corrections tend to the identity in bilipschitz norm, and PF-181's fixed-slab cusp handoffs have constants `1+O(eta_n^{vol})` with `eta_n^{vol}->0`. Thus there is one finite `K` such that every tail pant map and inverse are `K`-Lipschitz. A finite head contributes only another finite maximum.

Let `gamma` be a rectifiable path in `X`. Local finiteness of the pant decomposition lets one partition every compact subpath into portions contained in individual pants. On each portion,

\[
\operatorname{length}_{g_+}(F_0\circ\gamma)
\le K\operatorname{length}_g(\gamma).
\tag{15}
\]

Summing and taking infima over paths gives

\[
\boxed{
d_{g_+}(F_0x,F_0y)\le Kd_g(x,y).
}
\tag{16}
\]

The same argument for the inverse gives the reverse inequality. Hence the derivative mismatch across a cuff does not destroy global metric control: `F_0` is bi-Lipschitz even though it is not `C^1` there.

This is consistent with PF-125's earlier compact-resolvent construction, which explicitly allowed the transported prime/shift metric to be piecewise smooth and locally bounded measurable across seam/cuff loci. PF-203 uses the stronger exact-area maps developed later.

## 3. Exact pantwise area preservation survives gluing

Each PF-179 map preserves hyperbolic area. PF-180 and PF-181 are also exactly area preserving. Thus for every measurable set `E` contained in one pant interior,

\[
\mu_+(F_0(E))=\mu_g(E).
\tag{17}
\]

The union of distinguished cuffs has hyperbolic area zero. Decompose an arbitrary measurable set into its intersections with the countably many pant interiors plus this null set. Countable additivity and the bi-Lipschitz null-set property then give

\[
\boxed{
(F_0)_*\mu_g=\mu_+.
}
\tag{18}
\]

Equivalently, the composition operator

\[
U_0:L^2(X_+,d\mu_+)\to L^2(X,d\mu_g),
\qquad
U_0\phi=\phi\circ F_0,
\tag{19}
\]

is unitary.

By Rademacher differentiability in local charts, `DF_0` exists almost everywhere. On each pant interior the pullback metric is the ordinary smooth pullback, and (18) implies the a.e. volume identity (5). Uniform bi-Lipschitz control gives uniform ellipticity of `h_0` relative to `g`. Thus `h_0` is exactly the kind of measurable uniformly positive Riemannian coefficient field for which a quadratic-form Laplacian is natural; PF-123's Georgescu--Golénia audit already works in this measurable-metric category at the compact-resolvent level.

No claim is made that `h_0` is a smooth hyperbolic metric across a cuff as a tensor field on the fixed smooth source structure. It is the a.e. pullback coefficient representing the smooth target Laplacian through the Lipschitz identification.

## 4. Pull back the quadratic form, not the strong differential expression

A bi-Lipschitz change of variables preserves the first Sobolev space. Under the unitary (19), the target Dirichlet energy becomes

\[
q_+(U_0^{-1}u,U_0^{-1}v)
=\int_X h_0^*(du,dv)\,d\mu_{h_0}.
\tag{20}
\]

Using (5)--(6) gives exactly (8). Uniform ellipticity implies that this form is closed on the same set `H^1(X)` as the source hyperbolic form.

Now take `u,v` from (10). The source resolvent equation gives

\[
\langle f,v\rangle
=q_g(u,v)+\langle u,v\rangle,
\tag{21}
\]

while the pulled-target equation gives

\[
\langle u,z\rangle
=q_{h_0}(u,v)+\langle u,v\rangle.
\tag{22}
\]

Self-adjointness yields

\[
\langle R_0 f,z\rangle=\langle f,R_0z\rangle=\langle f,v\rangle,
\qquad
\langle R_g f,z\rangle=\langle u,z\rangle.
\tag{23}
\]

Subtracting (22) from (21) and using (8) proves (11).

This is the exact-area specialization of the form mechanism in PF-175, but it does **not** invoke PF-175's smooth-metric weighted Schatten theorem for `h_0`. The only conclusion here is the algebraic/variational identity. That distinction is essential because endpoint regularity is precisely what is being reorganized.

## 5. Why no separate seam distribution is required

A tempting objection is that a jump in the transverse derivative of `F_0` makes `A_0` discontinuous across a cuff and should therefore produce a delta-like interface term. That is true only if one differentiates the coefficient in a strong expression without simultaneously imposing the weak transmission condition.

The operator associated with (8) is defined by

\[
q_{h_0}(u,\varphi)
=\langle \Delta_{h_0}u,\varphi\rangle
\tag{24}
\]

for test functions in the form domain. If `u` is smooth on the two sides, integration by parts separately converts (24) into the usual divergence-form equations plus equality of the conormal fluxes across the interface. The cuff contribution is therefore **encoded in the domain of the global operator**. Returning to the global weak form recombines those boundary terms and gives (11) with no extra surface integral.

This is standard divergence-form behavior, not a new interface theorem. The project-specific consequence is narrower: PF-202's open-collar coefficient was introduced to make the identification smooth, but smoothness is not required merely to write the exact relative-resolvent form. At this level, replacing the piecewise coefficient by a thin smooth coefficient creates an optional approximation problem that the operator route need not pay for.

## 6. What analytic work remains

PF-203 removes one **self-created smoothing gate**, not the whole distinguished-cuff/interface sector.

First, PF-200/PF-201 deliberately exclude physical cuff/module-interface pieces from the regular Lambert family. In the piecewise identification those pieces remain genuine bulk coefficient regions on the two sides of a cuff. Their coefficient may be smooth up to the interface, but the globally pulled resolvent `R_0` belongs to a measurable divergence-form operator rather than one smooth pseudodifferential family across the seam. Ponge's PF-197 theorem therefore cannot be quoted across the cuff without a new localization argument.

Second, one possible route is to avoid the rough pulled operator altogether and keep the source and target smooth hyperbolic resolvents on their native surfaces, using `F_0` only as the bounded Sobolev identification between them. A successful two-manifold factorization would have to show explicitly that its localized order-`-1` factors and composition/bundle maps retain a uniform or prime-summable critical constant. PF-203 does not supply that factorization.

Third, the true PF-138 Margulis-short collars are not merely a smoothness issue. PF-177/PF-183 introduce optimized exact-area gauges there because the **bulk endpoint coefficient budget** can be bad without them. Those collars can cross the pant decomposition. Omitting PF-182 seam smoothing does not remove the need to construct or replace that true-short-collar splice at the correct critical cost.

Thus the live endpoint architecture becomes

\[
\boxed{
\text{regular body: PF-201}
\; + \;
\text{piecewise physical interfaces: rough/two-manifold endpoint gate}
\; + \;
\text{true-short collars: canonical splice gate}.
}
\tag{25}
\]

PF-202 remains useful if a later argument genuinely requires a smooth global identification, but its shrinking-support constant is no longer mandatory merely because the relative form must exist.

## 7. Prior-art and novelty audit

No novelty is claimed for Sobolev composition under bi-Lipschitz maps, Rademacher differentiability, the area formula, uniformly elliptic quadratic forms with bounded measurable coefficients, or weak transmission conditions for divergence-form operators. PF-123 already records the Georgescu--Golénia measurable-Riemannian framework used in this line and PF-125 explicitly exploits piecewise-smooth pulled metrics at the compact-resolvent level.

Directed searches for bi-Lipschitz pullbacks of Laplace--Beltrami forms, rough Riemannian metrics, and piecewise-smooth interface formulations locate a broad classical/modern rough-elliptic literature. Nothing in PF-203 depends on a new general theorem from that literature: equations (18)--(24) are the direct change-of-variables and closed-form calculation for the persisted PF maps. No claim of novelty is inferred from the absence of the exact prime-flute specialization in those searches.

The durable project-specific statement is the **route correction**: once PF-179--PF-181 and PF-182's common-trace lemma are all available, the natural exact-area comparison already exists as a globally bi-Lipschitz piecewise map, so PF-202's thin smooth seam is not an obligatory coefficient in the form-level weak-trace program. The unresolved question is transferred from shrinking smooth-pasting constants to an explicit rough-interface/two-manifold critical localization problem.

## 8. Audit / falsification core

A later adversary can test PF-203 through the following finite chain:

1. verify from PF-179 that each Lambert transport preserves area and has a tail-uniform bilipschitz bound;
2. verify from PF-180 that split synchronization preserves area and leaves genuine finite-cuff traces unchanged;
3. verify from PF-181 that the full-cusp handoff preserves area and also leaves finite cuffs unchanged;
4. verify from PF-182, before its smoothing step, that the two adjacent pants induce the same zero-twist-compatible boundary map on each distinguished cuff;
5. glue the pant maps and inverses and check the path-length argument giving one global bi-Lipschitz constant;
6. use nullity of the cuffs plus pantwise area preservation to prove (18);
7. apply a.e. change of variables to obtain the measurable uniformly elliptic pullback coefficient and the closed form (8);
8. subtract the two resolvent variational equations and verify (11) without differentiating `A_0`;
9. if one integrates by parts pantwise, verify that the resulting conormal interface condition is exactly the weak operator-domain condition rather than a new independent perturbation term;
10. do **not** apply PF-197/PF-200 directly to `R_0` across the coefficient jump without proving the needed rough/interface localization, and do not infer that the PF-138 true-short-collar coefficient budget has been solved.

Failure of steps 1--4 would invalidate the global piecewise identification. Failure of steps 5--8 would invalidate the form-level bypass. Step 9 protects the result from a false surface-delta objection. Step 10 protects it from being over-read as the missing global weak-`S_1` theorem.

## Consequence for the research line

The distinguished decomposition cuffs no longer force the endpoint program to choose between smoothness and a shrinking-support operator constant. There are now two honest architectures:

- keep PF-182/PF-202's globally smooth exact-area comparison and prove that the shrinking seam family has acceptable critical constants; or
- use the earlier PF-179--PF-181 piecewise exact-area comparison, where the seam correction vanishes from the coefficient budget, and solve the resulting rough-interface/two-manifold critical localization problem directly.

The second architecture is strictly cheaper at the **form-definition** level and removes the circular `support width -> higher derivatives -> local Cwikel constant` concern identified in PF-202. Whether it is also cheaper at the weak-trace level is the next falsifiable analytic question.