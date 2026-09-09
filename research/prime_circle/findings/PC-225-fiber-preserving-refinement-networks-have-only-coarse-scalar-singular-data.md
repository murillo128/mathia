# PC-225 — fiber-preserving refinement networks have only coarse scalar singular data

**Status:** `EXACT-DERIVED` + `DECISIVE-BOUNDARY` for the repeated-refinement escape left open by PC-224. Keeping arbitrarily many fresh-prime coordinates, path labels, diagonal source masks, and coordinatewise old/new projections does enlarge the codomain, but it does not by itself create a relational operator on the coarse level. Any finite network built only from canonical refinement pullbacks, diagonal masks, and conditional expectations over newly adjoined CRT coordinates is a module map over functions on the original coarse level. Consequently it acts independently on each coarse fiber, and its full positive square is exactly multiplication by one scalar terminal-fiber energy profile.

This strictly extends the one-step conditional-variance reduction of PC-224. It also survives bounded operator limits in a common refinement-limit Hilbert space as long as the construction remains coarse-fiber preserving. Thus repeated depth, branching, or an infinite number of retained prime coordinates is not an escape by itself. A surviving mechanism must interrogate the internal fiber vector before left-unitary compression or introduce an intrinsic operation that genuinely mixes different coarse residues.

## 1. Coarse-module formulation

Fix a base level `N`, and let

\[
Q=\prod_{j=1}^r q_j
\]

be a product of distinct primes coprime to `N`. Under CRT write

\[
\mathbb Z/NQ\mathbb Z
\cong
A_Q\times Y,
\qquad
A_Q:=\prod_{j=1}^r\mathbb Z/q_j\mathbb Z,
\qquad
Y:=\mathbb Z/N\mathbb Z.
\tag{1}
\]

All `L^2` spaces below use normalized counting measure. Let `D_N` be the diagonal algebra of functions on the coarse coordinate:

\[
D_N=\{M_\phi:\phi:Y\to\mathbb C\}.
\tag{2}
\]

On a refined level, `M_\phi` means multiplication by the pullback `\phi(y)`.

Consider the operations used in the direct refinement architecture:

- canonical pullback along a refinement `J:H_M\to H_{qM}`;
- multiplication by an arbitrary refined-level mask `M_g`;
- conditional expectation `E_q=JJ^*` over a newly adjoined `q` coordinate and its complement `Q_q=I-E_q`;
- finite sums, compositions, and branches of such operators, after lifting branches to a common refinement when necessary.

Every one of these operations commutes/intertwines with the coarse algebra `D_N`. Hence every resulting operator

\[
T:H_N\longrightarrow H_{NQ}
\tag{3}
\]

satisfies

\[
\boxed{
T M_\phi=M_\phi T
\qquad(\phi\in D_N).
}
\tag{4}
\]

Here the two copies of `M_\phi` act on the source and refined target respectively. This is the exact structural property behind the scalarization.

## 2. Exact fiber decomposition

Take `\phi=1_{\{y\}}` in (4). If `f` is supported at one coarse point `y`, then `Tf` is supported entirely in the terminal fiber `A_Q\times\{y\}`. Since the source fiber over `y` is one-dimensional, there is a vector

\[
v_y\in L^2(A_Q)
\tag{5}
\]

such that

\[
\boxed{
(Tf)(a,y)=v_y(a)f(y).
}
\tag{6}
\]

Therefore distinct coarse inputs have orthogonal images. Taking the adjoint gives

\[
\boxed{
T^*T=M_{w_T},
\qquad
w_T(y)=\frac1{|A_Q|}\sum_{a\in A_Q}|v_y(a)|^2.
}
\tag{7}
\]

In particular,

\[
\boxed{
\operatorname{Spec}_{\rm sing}(T)
=\{\sqrt{w_T(y)}:y\bmod N\},
}
\tag{8}
\]

with multiplicity and zeros included. Every determinant, trace, Schatten norm, or scalar spectral invariant formed only from `T^*T` is therefore a function of the single coarse profile `w_T`.

The conclusion is stronger than a dimension bound. The terminal codomain may contain a large tensor product of fresh-prime coordinates and may retain every path label, but no interference between distinct coarse residues can occur inside this operator class.

## 3. Repeated centered-mask cascade

The serial version makes the reduction explicit. Put

\[
N_i=N\prod_{j=1}^i q_j,
\tag{9}
\]

let `J_i:H_{N_{i-1}}\to H_{N_i}` be the canonical pullback, let `E_i=J_iJ_i^*`, and let `g_i` be any mask on `Z/N_i Z`. Define

\[
T_i=(I-E_i)M_{g_i}J_i.
\tag{10}
\]

With CRT coordinates `(a_i,\ldots,a_1,y)`, set

\[
d_i(a_i,\ldots,a_1,y)
:=g_i(a_i,\ldots,a_1,y)
-\frac1{q_i}\sum_{b\bmod q_i}g_i(b,a_{i-1},\ldots,a_1,y).
\tag{11}
\]

Then direct substitution gives, for the depth-`r` leakage map `L_r=T_r\cdots T_1`,

\[
\boxed{
(L_rf)(a_r,\ldots,a_1,y)
=f(y)\prod_{i=1}^r d_i(a_i,\ldots,a_1,y).
}
\tag{12}
\]

Hence

\[
\boxed{
L_r^*L_r=M_{w_r},
\qquad
w_r(y)=
\mathbb E_{a_1,\ldots,a_r}
\prod_{i=1}^r|d_i(a_i,\ldots,a_1,y)|^2.
}
\tag{13}
\]

PC-224 is the case `r=1`, where `w_1` is the fiberwise conditional variance. At larger depth the scalar profile can contain genuine higher mixed moments because a later mask may depend on earlier fresh-prime coordinates. The result does **not** claim those scalar moments are arithmetically trivial. It says that the complete singular/positive-square data of the repeated-refinement operator still consists of only this one scalar function on the original coarse level.

For the source cyclotomic choice, each `g_i` may be the normalized coefficient mask of `Phi_{N_i}` used in PC-224. Equation (13) then gives a nested residue-class moment of centered cyclotomic coefficients. The arithmetic problem may move into that profile, but repeated refinement has not created an additional relational spectral operator.

## 4. Two-prime mixed-sector control

There is a particularly transparent two-prime version. At level `Npq`, with `p,q` fresh and distinct, let `E_p,E_q` average over the independent CRT coordinates. They commute exactly. For one terminal mask `g`,

\[
Q_pQ_qg
=(I-E_p)(I-E_q)g
=g-E_pg-E_qg+E_pE_qg.
\tag{14}
\]

This is precisely the two-coordinate interaction component familiar from the ordinary product-space orthogonal/ANOVA decomposition. Acting on a lifted coarse state gives

\[
(Q_pQ_qM_gJf)(a,b,y)
=(Q_pQ_qg)(a,b,y)f(y),
\tag{15}
\]

and therefore

\[
\boxed{
(Q_pQ_qM_gJ)^*(Q_pQ_qM_gJ)
=M_{\,\mathbb E_{a,b}|Q_pQ_qg|^2}.
}
\tag{16}
\]

Thus retaining the sector that is simultaneously new in both prime coordinates does produce a genuine mixed-coordinate vector before compression, but its singular data is only the coarse profile of its squared norm. The order of the two coordinate projections cannot supply curvature or noncommutativity because `E_pE_q=E_qE_p`.

## 5. Matched-control theorem

The exact information loss can be stated without reference to how `T` was built. Let `T,T':H_N\to H_{NQ}` both satisfy the coarse-module relation (4), with terminal vectors `v_y,v'_y`. If

\[
\|v_y\|=\|v'_y\|
\qquad\text{for every }y\bmod N,
\tag{17}
\]

then for each fiber there is a unitary `U_y` taking `v_y` to `v'_y`. Their orthogonal direct sum gives a fiber-preserving unitary `U` with

\[
\boxed{T'=UT.}
\tag{18}
\]

Therefore every invariant that quotients by arbitrary left unitaries inside the retained refinement fibers — in particular singular values and any invariant built only from `T^*T` — forgets all terminal path organization beyond `w_T`.

This is the repeated-refinement analogue of the matched-mask control in PC-224. It also identifies exactly what can evade it: a distinguished projector or operator acting on the terminal fiber **before** the left-unitary quotient can distinguish vectors of equal norm, provided that operator is intrinsically forced and not itself reducible to the same coarse-module data.

## 6. Bounded refinement limits

The finite-depth obstruction does not disappear merely by taking more and more fresh-prime coordinates. Embed the refined spaces into a common product/refinement-limit Hilbert space `K` over the same finite coarse base `Y`. Every finite network above is a `D_N`-module map

\[
T_r:H_N\to K.
\tag{19}
\]

If `T_r` has a bounded strong or weak operator limit `T`, then (4) passes to the limit for every `M_\phi\in D_N`. Consequently the same fiber decomposition (6) holds for `T`, now with `v_y` in the possibly infinite-dimensional terminal fiber, and again

\[
\boxed{T^*T=M_{w_T}.}
\tag{20}
\]

So infinite depth is not an automatic escape either. A proposed limit must break the coarse-module hypothesis, retain a non-left-unitary invariant of the internal fiber state, or rely on a genuinely different unbounded/domain-sensitive mechanism whose topology is specified separately. A simultaneous limit in which the coarse base `N` itself changes is not classified by (20).

## 7. Prior-art and novelty audit

The abstract ingredients are classical: conditional expectation is an `L^2` orthogonal projection, independent-coordinate expectations yield the usual product-space orthogonal/ANOVA decomposition, and an operator intertwining the full diagonal algebra over a finite base decomposes fiberwise. The derivation above is elementary finite Hilbert-space/module algebra; no novelty is claimed for those general facts.

A literature search around conditional expectations, martingale differences, product-space ANOVA/Hoeffding-Efron-Stein decompositions, and decomposable operators found these ingredients as standard theory, not a new spectral mechanism. The project-specific content is the exact application to the post-PC-224 Prime-Circle refinement architecture and the resulting falsification boundary. No external theorem is needed for the proof, and no claim is made that the scalar profiles `w_T` are classically exhausted.

## Research consequence

PC-224 left repeated refinements and retained path labels as a possible way to avoid one-step variance scalarization. PC-225 narrows that survivor sharply. Any finite branching or serial network made only from canonical refinement pullbacks, diagonal source masks, and conditional expectations/complements over newly introduced CRT coordinates remains coarse-fiber preserving, and even a bounded infinite-depth limit remains so. Its singular or positive-square spectral data is therefore only one scalar profile on the original level.

The next admissible escape must violate at least one hypothesis of this theorem. Natural source-forced possibilities are an exact-order/Fourier projector or chord/cotangent operator that genuinely mixes coarse residues before the final invariant, a joint observable that retains the internal terminal fiber vector rather than quotienting by left fiber unitaries, or a controlled limit in which the coarse base itself grows and the cross-base comparison is essential. Merely adding more refinement coordinates, masks, branches, or depth inside the coarse-module algebra is now closed.