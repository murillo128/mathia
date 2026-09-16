# Arithmetic-fidelity research lines

This file holds the current mathematical questions suggested by the durable arithmetic-fidelity intuitions. It is not a roadmap, task queue, status page, or history.

## Price retained information jointly with the admissible source class

**Linked intuitions:** `MI-001-fidelity-is-quotient-relative`, `MI-004-prime-specificity-depends-on-the-retained-analytic-layer`, `MI-018-signed-complexity-only-transfers-through-sign-regular-observations`, `MI-041-one-riesz-order-crosses-conditioning-without-moving-the-zero-discriminator`, `MI-042-finite-prefix-pole-fidelity-needs-a-tail-class`.

AF-365--AF-370 separate exact discriminator survival from finite observation, source freedom, conditioning and source-category rigidity. Small retained data can become complete only after the admissible fibre is restricted enough to be target-pure. Recovering `zeta` inside a rigid category still does not select its nontrivial zeros. The broader question remains to identify source-class/data couplings substantially weaker than full reconstruction but strong enough to preserve the exact downstream discriminator.

## Distinguish relational order, placement generators, support topology, lower-order interiority and multiscale compatibility

**Linked intuitions:** `MI-002-canonical-relational-lifts-can-restore-gauge`, `MI-019-faithful-translation-lifts-are-affine`, `MI-043-support-scale-interaction-components-bound-effective-relational-arity`, `MI-045-shrinking-mesh-solid-pf3-consistency-forces-boundary-flatness`.

AF-371--AF-378 separate target-faithful translation positivity from gauge elimination, sampling density and coordinate display. Uniformly discrete rows admit compact-support false positives; even `inf gap=0` can leave every support-interaction component uniformly bounded; faithful nonlinear coordinate transport preserves the sampled fibre rather than creating new information.

AF-379 and AF-381 give the complementary determining regime. Dense normalized finite row patterns determine one-sided continuous translation minors, while dense joint row/column patterns determine the fully sampled target. Vanishing tail mesh forces both closures. Since `log p_(n+1)-log p_n -> 0`, the fully prime-indexed matrices `f(log(p_i/q_j))` are target-complete for continuous translation total nonnegativity.

AF-382 compresses determinant order two further. For strictly positive continuous `f`, adjacent successor-prime rectangles generate every sampled `2x2` inequality by logarithmic mixed-difference telescoping, and the vanishing prime-log mesh then closes to global `TN_2`/log-concavity.

AF-383 shows that a different exact placement compression survives at **every fixed determinant order**. On any shrinking uniform lattice, arbitrary Toeplitz order-`k` minors are nonnegative combinations of minors with one consecutive `k`-row stencil and arbitrary column tuple; continuity then passes the lattice result to the continuum. Thus one spatial tuple is redundant at every fixed order even in the general nonnegative class.

AF-384 identifies a sufficient condition for collapsing the remaining placement axis: continuum strict total positivity through orders `<k` plus nonnegative solid order-`k` minors on shrinking lattices yields continuum `TN_k`. AF-385 localizes that strictness burden to the same sampled generator hierarchy: it is enough that every sampled solid generator is strictly positive below order `k` and nonnegative at order `k`.

AF-386 removes that strictness overpayment exactly at order two. For continuous nonnegative `f`, nonnegative solid `2x2` generators on a shrinking mesh characterize continuum `TN_2` once `{f>0}` is connected. Internal zeros are the precise missing resource: two separated positive components can pass every sufficiently fine local solid test while failing a cross-gap continuum minor. **Resolution and support connectivity are independent.** A vanishing mesh cannot infer the global zero pattern required to propagate local log-concavity across the support.

AF-387 proves that this repair does not extrapolate unchanged to order three on one lattice. The connected sequence `(1,1,1,1,t)`, `0<t<1`, is `PF_2` and has every solid order-three Toeplitz minor nonnegative, yet a gapped order-three minor equals `t-1<0`. The obstruction is not a support gap: zero order-two minors occur inside the positive support and block propagation to a nonlocal placement.

AF-388 now shows that the fixed-lattice obstruction is **not** the whole continuum story. For one positive `C^8` profile sampled on meshes `h_m -> 0`, nonnegative solid order-two and order-three Toeplitz minors force, with `q=-(log f)''`,

`q >= 0`,  `2q^3 - q q'' + (q')^2 >= 0`,

and every zero of `q` satisfies `q''=0`. The next-order solid determinant therefore rules out an ordinary quadratic contact with the lower-order boundary even though no lattice point need hit the zero exactly. Common-profile multiscale consistency recovers real information that one fixed lattice loses.

The higher-order recognition problem is consequently a hierarchy over determinant order, relative offset, support topology, lower-order zero-minor geometry and **cross-scale compatibility**. AF-388 proves that shrinking resolution can remove at least the nondegenerate quadratic boundary stratum, but it does not establish continuum `TN_3`: quartic or higher finite-order zeros and infinitely flat zeros remain possible, as does the separate task of assembling the strictly positive region globally. The next sharp question is whether the multiscale solid hierarchy excludes every finite-order zero of `q`, or whether a sufficiently flat positive profile can pass all shrinking-mesh solid `2x2`/`3x3` tests while retaining a negative non-solid continuum `3x3` minor.

In every case the arithmetic source must still force the required generator signs rather than inherit target positivity as a hypothesis.

## Separate source identification from zero selection

AF-370 identifies `zeta` exactly inside its declared source class, but Hamburger rigidity does not confine nontrivial zeros to `Re s=1/2`. The functional equation can identify the analytic object while leaving RH untouched. Future fidelity arguments must keep source identification and zero selection as orthogonal gates.

## Preserve the remaining exact source-access questions

The RH root-rate endpoint still requires cancellation-coherent access before taking the Li root-rate quotient; ordinary prefix accuracy is the wrong currency. The conditional Schanuel codimension program likewise remains open at the unconditional joint-dependence step: AF-320--AF-336 reduce exact incidence to algebraic relations on the common prime-phase tuple, but no unconditional source theorem yet excludes the required middle-singular fibre.

For every proposed destination theorem state separately the observed data, admissible source/tail class, retained analytic layer, determinant/relation order, intrinsic support-scale interaction complexity, placement-generator family, support topology/zero pattern, lower-order zero-minor/interiority pattern, cross-scale compatibility, normalized pattern closure, coordinate covariance, residual gauge and topology/modulus of inference. AF-386--AF-388 make the accounting especially concrete: arbitrarily fine local certificates may miss a global support relation or an interior lower-order degeneracy, but repeated compatible scales can also rule out boundary behavior that a single lattice cannot see.