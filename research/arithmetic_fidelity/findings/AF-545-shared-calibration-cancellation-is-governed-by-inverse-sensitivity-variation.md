# AF-545 — Shared calibration cancellation is governed by inverse-sensitivity variation

## Status

`EXACT-DERIVED` · `CLASSICAL-INGREDIENTS` · `NONLINEAR-RECOVERY` · `CALIBRATION` · `CONDITIONING` · `SHARED-NUISANCE` · `INVARIANCE` · `NO-NOVELTY-CLAIM`

## Claim

AF-544 found a strong cancellation when the **same** imperfect curvature calibration is used to decode two nearby source branches. That phenomenon is not special to the prime-zeta normal form. It is the scalar instance of a general deterministic rule for nonlinear inverse problems.

Let

\[
y=G(z,u)
\]

be a `C^2` observation map on a region where `G_z\neq0`. Here `z` is the latent source coordinate and `u` is a calibration/nuisance coordinate. Fix the true calibration `u_0`, let `\Psi_u` denote the local inverse in `z`, and define the decoder transport

\[
\Phi_u(z):=\Psi_u(G(z,u_0)),
\qquad
\Phi_{u_0}(z)=z.
\tag{1}
\]

For any `C^1` readout coordinate `q`, define the **inverse-calibration sensitivity**

\[
\boxed{
K_q(z,u)
:=-q'(z)\frac{G_u(z,u)}{G_z(z,u)}.
}
\tag{2}
\]

Then the decoded readout satisfies the exact identity

\[
\boxed{
\frac{d}{du}q(\Phi_u(z))
=K_q(\Phi_u(z),u).
}
\tag{3}
\]

Consequently, for two sources `z_1,z_2`, the common-calibration contrast

\[
C_u(z_2,z_1)
:=q(\Phi_u(z_2))-q(\Phi_u(z_1))
\tag{4}
\]

obeys

\[
\boxed{
\frac{d}{du}C_u(z_2,z_1)
=K_q(\Phi_u(z_2),u)-K_q(\Phi_u(z_1),u).
}
\tag{5}
\]

Thus common calibration is not controlled by the **absolute** inverse sensitivity of either branch. It is controlled by the **variation of inverse sensitivity between the two decoded branches**.

This yields an exact classification of complete common-mode cancellation. On a connected local inverse region, all pairwise contrasts `(4)` are independent of `u` if and only if `K_q(z,u)` is independent of `z`. Equivalently, there is a scalar function `a(u)` such that

\[
q(\Phi_u(z))=q(z)+a(u)
\tag{6}
\]

for every source in the region. In that case the calibration flow acts as a translation in the readout coordinate, and differencing quotients out the nuisance exactly.

When `K_q` is not source-independent, `(5)` gives the correct quantitative replacement. A shared calibration error is small after the final contrast precisely when the **mixed source/calibration sensitivity** is small on the decoder path. Independent branch calibrations do not receive this cancellation in general.

## Derivation

### 1. The inverse-calibration field is exact

For fixed `z`, the transported decoder coordinate `\Phi_u(z)` is defined by

\[
G(\Phi_u(z),u)=G(z,u_0).
\tag{7}
\]

Differentiating with respect to `u` gives

\[
G_z(\Phi_u(z),u)\,\partial_u\Phi_u(z)
+G_u(\Phi_u(z),u)=0,
\]

hence

\[
\partial_u\Phi_u(z)
=-\frac{G_u}{G_z}(\Phi_u(z),u).
\tag{8}
\]

Applying the chain rule to `q(\Phi_u(z))` proves `(3)`.

No probabilistic approximation is involved. The only local hypothesis is invertibility in the latent coordinate.

### 2. Shared calibration sees a difference of sensitivities

Subtract `(3)` for `z_1` and `z_2`. This gives `(5)` and, after integrating from `u_0` to `u_0+\varepsilon`, the exact finite-error identity

\[
\boxed{
C_{u_0+\varepsilon}-C_{u_0}
=
\int_{u_0}^{u_0+\varepsilon}
\left[
K_q(\Phi_v(z_2),v)-K_q(\Phi_v(z_1),v)
\right]dv.
}
\tag{9}
\]

Equation `(9)` is the natural target-relative calibration seminorm for a two-branch contrast. It makes two distinct notions of conditioning explicit:

- branchwise reconstruction is governed by `|K_q|`;
- relational reconstruction under a shared calibration is governed by the **oscillation of `K_q` across the branches**.

The latter can be much smaller than the former.

For example, suppose on the relevant decoder tube

\[
|\partial_zK_q(z,u)|\le M,
\qquad
|\partial_z\Phi_u(z)|\le L.
\tag{10}
\]

Then `(9)` gives the non-asymptotic bound

\[
\boxed{
|C_{u_0+\varepsilon}-C_{u_0}|
\le
|\varepsilon|\,ML\,|z_2-z_1|.
}
\tag{11}
\]

Thus common-mode calibration error is bilinear, to first order, in calibration displacement and source separation whenever the inverse-sensitivity field is regular.

At the infinitesimal level,

\[
C_{u_0+\varepsilon}-C_{u_0}
=
\bigl[K_q(z_2,u_0)-K_q(z_1,u_0)\bigr]\varepsilon
+O(\varepsilon^2).
\tag{12}
\]

If `K_q` is differentiable in the source coordinate, the mean-value theorem rewrites the leading coefficient as

\[
K_q(z_2,u_0)-K_q(z_1,u_0)
=
\partial_zK_q(\xi,u_0)(z_2-z_1)
\tag{13}
\]

for an intermediate `\xi`.

### 3. Exact common-mode cancellation has an if-and-only-if form

Assume first that `K_q(z,u)=k(u)` is independent of `z`. Equation `(5)` immediately gives

\[
\partial_u C_u(z_2,z_1)=0
\]

for every pair, so all contrasts are exactly calibration invariant. Integrating `(3)` from `u_0` gives `(6)` with

\[
a(u)=\int_{u_0}^{u}k(v)\,dv.
\]

Conversely, suppose every contrast `(4)` is independent of `u`. Fix one source `z_*`. Then

\[
q(\Phi_u(z))-q(\Phi_u(z_*))
\]

is independent of `u` for every `z`, so `\partial_u q(\Phi_u(z))` has the same value for every `z`. By `(3)`,

\[
K_q(\Phi_u(z),u)
\]

is independent of `z`. For each fixed `u`, `\Phi_u` is a local diffeomorphism on the inverse region, so its image is open and `K_q(w,u)` is independent of `w` there.

Hence

\[
\boxed{
\text{all shared-calibration contrasts are exact invariants}
\iff
K_q(\cdot,u)\text{ is source-independent}.
}
\tag{14}
\]

This turns a vague statement such as “the nuisance cancels in a ratio/difference” into a checkable differential criterion on the actual nonlinear decoder.

### 4. Common and differential calibration split into different modes

Now let the two branches be decoded with separate calibrations

\[
u_1=u_0+\varepsilon_1,
\qquad
u_2=u_0+\varepsilon_2.
\]

The perturbed contrast is

\[
\widetilde C
=q(\Phi_{u_2}(z_2))-q(\Phi_{u_1}(z_1)).
\]

Taylor expansion at `u_0` gives

\[
\widetilde C-C_{u_0}
=
K_2\varepsilon_2-K_1\varepsilon_1
+O(\varepsilon_1^2+\varepsilon_2^2),
\tag{15}
\]

where

\[
K_i:=K_q(z_i,u_0).
\]

Writing

\[
\bar\varepsilon
=\frac{\varepsilon_1+\varepsilon_2}{2},
\qquad
\delta\varepsilon
=\varepsilon_2-\varepsilon_1,
\]

we obtain

\[
\boxed{
\widetilde C-C_{u_0}
=
(K_2-K_1)\bar\varepsilon
+\frac{K_2+K_1}{2}\,\delta\varepsilon
+O(\varepsilon_1^2+\varepsilon_2^2).
}
\tag{16}
\]

The two nuisance modes therefore have different fidelity budgets:

- **common mode** is weighted by the sensitivity difference `K_2-K_1` and is suppressed when the source branches are close or `K_q` is nearly source-independent;
- **differential mode** is weighted by the average sensitivity `(K_2+K_1)/2` and is generically unsuppressed.

A calibration label such as “small error” is therefore incomplete. What matters is whether the error is shared or differential relative to the final relational observable.

## Coordinate / representation audit

The exact criterion is not an artifact of the latent coordinate.

Let `w=\varphi(z)` be a smooth local reparameterization and define

\[
\widetilde G(w,u)=G(\varphi^{-1}(w),u),
\qquad
\widetilde q(w)=q(\varphi^{-1}(w)).
\]

Then

\[
\widetilde G_w=\frac{G_z}{\varphi'(z)},
\qquad
\widetilde q'(w)=\frac{q'(z)}{\varphi'(z)},
\qquad
\widetilde G_u=G_u,
\]

so

\[
-\widetilde q'(w)\frac{\widetilde G_u(w,u)}{\widetilde G_w(w,u)}
=
-q'(z)\frac{G_u(z,u)}{G_z(z,u)}
=K_q(z,u).
\tag{17}
\]

Thus the scalar field `K_q` and the exact contrast derivative `(5)` are invariant under a smooth change of latent coordinate when the readout is transported with it. The Lipschitz constants in `(10)` are coordinate-dependent estimates of that invariant variation; the exact object is the difference of `K_q` values along the decoder path.

The readout `q` itself is load bearing. Different observables can quotient the same calibration flow differently. This is appropriate for Arithmetic Fidelity: fidelity is target-relative, not an intrinsic property of the raw representation alone.

## Two exact controls

### Multiplicative calibration

Take

\[
G(z,u)=e^u z,
\qquad
q(z)=\log z,
\qquad z>0.
\]

Then

\[
K_q(z,u)=-1
\]

is independent of the source. Therefore

\[
\log\Phi_u(z_2)-\log\Phi_u(z_1)
=\log z_2-\log z_1
\]

for every shared calibration `u`: common error cancels exactly. With separate errors, `(16)` reduces to

\[
\widetilde C-C_{u_0}=-(\varepsilon_2-\varepsilon_1)
\]

exactly. This is the pure common-mode quotient case.

### Additive calibration with a nonlinear readout

Take

\[
G(z,u)=z+u,
\qquad
q(z)=\log z,
\qquad z>0.
\]

Now

\[
K_q(z,u)=-\frac1z.
\]

The same calibration is shared, but the sensitivity variation

\[
K_q(z_2,u)-K_q(z_1,u)
=\frac1{z_1}-\frac1{z_2}
\]

can be large near `z=0`. Sharing alone therefore does **not** guarantee useful cancellation. If the readout is changed to `q(z)=z`, however, `K_q=-1` and ordinary differences become exact invariants.

This pair of controls separates three notions that can otherwise be conflated: shared nuisance, decoder conditioning, and target/readout choice.

## Specialization to AF-543 / AF-544

AF-543 uses the curvature normal form

\[
G(D,u)
=
\frac{D[(1-2u)+(1-u)D]}
{(1-u)(1+D)^2}
\tag{18}
\]

with readout

\[
q(D)=\log D.
\]

Substituting `(18)` into `(2)` gives exactly the AF-544 sensitivity

\[
K_q(D,u)
=
S(D,u)
=
\frac{1+D}{(1-u)(1+D-2u)},
\tag{19}
\]

and

\[
\partial_DK_q(D,u)
=-\frac{2u}{(1-u)(1+D-2u)^2}.
\tag{20}
\]

Therefore AF-544's cancellation is now read directly from the general criterion: the individual branch sensitivities satisfy `S=1+o(1)`, but the **difference** of sensitivities carries an extra factor `u(D_A-D_{B_A})`.

At the endpoint used there,

\[
u=r(h_A)=L_A^{-1}(1+o(1))
\]

and AF-542/AF-544 give

\[
D_A-D_{B_A}
=(-\log\theta)\frac{C_A-1}{L_A}(1+o(1)).
\]

Hence `(20)` yields

\[
K_q(D_{B_A},u)-K_q(D_A,u)
=
2(-\log\theta)\frac{C_A-1}{L_A^2}(1+o(1)),
\tag{21}
\]

which is precisely the coefficient multiplying the common calibration error in AF-544 equation `(6)`.

AF-544's differential-error equation is equally explained by `(16)`: because both `K_i=1+o(1)`, differential calibration enters at order `\varepsilon_2-\varepsilon_1` rather than at the smaller common-mode scale `(21)`.

So the prime-zeta example is not merely a lucky algebraic cancellation. It sits in a general class where calibration fidelity is governed by the variation of the inverse-sensitivity field across the relational comparison.

## Target-relative calibration criterion

Suppose a downstream argument needs the decoded contrast accurate to a scale `\sigma_A\to0`, while the source pair and true calibration may depend on `A`. Equation `(9)` gives the exact criterion

\[
\boxed{
\int_{u_{0,A}}^{u_{0,A}+\varepsilon_A}
\left|
K_q(\Phi_v(z_{2,A}),v)
-K_q(\Phi_v(z_{1,A}),v)
\right|dv
=o(\sigma_A).
}
\tag{22}
\]

For small calibration errors this becomes

\[
|\varepsilon_A|\,
|K_q(z_{2,A},u_{0,A})-K_q(z_{1,A},u_{0,A})|
=o(\sigma_A),
\tag{23}
\]

provided the second-order remainder is also `o(\sigma_A)`.

This is strictly more informative than requiring each decoded branch to have error `o(\sigma_A)`. A relational observable may tolerate much larger **common** reconstruction error because only the sensitivity variation survives the quotient.

Conversely, if

\[
|K_q(z_{2,A},u_{0,A})-K_q(z_{1,A},u_{0,A})|
\asymp1,
\]

then sharing the calibration buys no asymptotic first-order gain. If `G_z` approaches zero or `K_q` develops a singular source dependence, common-mode sharing can become useless even when the two branches are close in the raw source coordinate.

## Prior-art / novelty audit

The ingredients are classical and no theorem-level novelty is claimed outside the Mathia organization.

- The derivative `(8)` is the standard implicit-function sensitivity formula for a locally invertible nonlinear map.
- Classical invariance theory studies statistics constant on transformation-group orbits and maximal invariants that retain all invariant information; exact cases of `(14)` belong naturally to that language. Lehmann and Romano's *Testing Statistical Hypotheses* treats invariance through group orbits and maximal invariants.
- Cox and Reid, “Parameter Orthogonality and Approximate Conditional Inference,” *JRSS B* 49 (1987), DOI `10.1111/j.2517-6161.1987.tb01422.x`, develops orthogonalization of nuisance and target parameters in likelihood inference.
- Chernozhukov et al., “Double/debiased machine learning for treatment and structural parameters,” *The Econometrics Journal* 21 (2018), DOI `10.1111/ectj.12097`, uses Neyman-orthogonal scores to remove first-order sensitivity to nuisance estimation.

Those statistical theories are close conceptual neighbors but are not being rebranded as this finding. The present statement is a deterministic local-inverse calculation for a **shared calibration acting on two decoded branches**. Its durable contribution to this line is the explicit invariant field `(2)`, the exact pairwise transport law `(5)/(9)`, the if-and-only-if exact-cancellation criterion `(14)`, and the common/differential decomposition `(16)`, all of which package AF-544's source-specific cancellation into a reusable falsification and calibration test.

## Boundaries and failure modes

- **Scalar local inverse.** The theorem is stated for one latent and one calibration coordinate. Matrix-valued generalization requires Jacobian/pseudoinverse geometry and should not be inferred from this scalar statement without derivation.
- **Local invertibility is load bearing.** If `G_z=0` or the inverse branch changes, `K_q` can diverge or cease to describe the decoder.
- **Shared means the same nuisance coordinate and decoder family.** Two quantities both called “calibration” do not receive `(5)` if they enter through different maps or different reference conventions.
- **Readout-relative.** A nuisance can cancel exactly for one `q` and fail badly for another. This is a feature, not a coordinate defect.
- **Nearness alone is insufficient.** Small `|z_2-z_1|` helps only when the inverse-sensitivity field is regular on the decoder tube.
- **First-order differential split.** Equation `(16)` does not suppress quadratic terms when the required downstream scale is finer than `O(\varepsilon_i^2)`; those terms must then be audited explicitly.
- **No arithmetic identification.** The theorem classifies calibration transport. It does not distinguish rational primes from matched generalized-prime or other controls.
- **No RH consequence.** It is a representation-fidelity theorem only.

## Decisive audit tests

The finding can be falsified mechanically at four points.

1. Differentiate `G(\Phi_u(z),u)=G(z,u_0)` and verify `(2)`--`(5)` for an arbitrary smooth test map.
2. Test `(14)` in both directions: source-independent `K_q` must force `q\circ\Phi_u` to differ from `q` only by an additive `u`-dependent term, and exact invariance of all pairwise contrasts must force the same property.
3. Reparameterize `z` by an arbitrary local diffeomorphism and verify `(17)`; any uncancelled Jacobian would show that the proposed sensitivity field is representation-dependent.
4. Substitute the AF-543 normal form `(18)` and verify `(19)`--`(21)` against AF-544. The source-specific coefficient must reappear without adding any prime-specific assumption to the general theorem.

All four checks are direct consequences of the displayed identities.

## Consequence for the research line

AF-544 ended with the rule “differentiate the final relational observable with respect to calibration.” AF-545 turns that rule into a reusable theorem.

The relevant object is not absolute calibration accuracy and not even absolute decoder condition number. For a shared reference used by several branches, the fidelity budget is controlled by how much the **inverse-calibration sensitivity varies across the branches that the final observable compares**. Exact source-independence gives a quotient invariant; small variation gives quantitative common-mode suppression; differential calibration remains governed by the unsuppressed average sensitivity.

This supplies a general test for future compression/recovery candidates: before demanding highly accurate branchwise reconstruction, compute `K_q`, determine whether the nuisance is genuinely common, and measure its variation on the relational carrier. That distinguishes reference information which must survive compression from nuisance information that the final relation can safely forget.