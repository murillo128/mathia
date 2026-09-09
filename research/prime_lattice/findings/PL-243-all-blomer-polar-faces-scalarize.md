# PL-243 — All three polar faces of Blomer's `D_12` double series are Weyl transports of the same principal scalar residue

## Claim

`PL-242` closed the `s=1` polar face of Blomer's quadratic double Dirichlet series but deliberately left the other possible polar faces `w=1` and `s+w=3/2` open. Those two faces can also be closed exactly, without a new analytic-continuation argument: Blomer's two functional equations transport their residues from the already computed principal `s=1` residue.

Write `Z(s,w)` for Blomer's 16-component vector indexed by the real characters `psi,psi'` of conductor dividing `8`, and let `e` be the constant vector on the components with `psi=psi_1` trivial and zero on the components with nontrivial `psi`. From `PL-242`, initially in a genuine convergence region and then meromorphically,

`R_s(w) := Res_(s=1) Z(s,w) = (1/2) zeta_2(2w) e`.

Blomer proves the exact vector functional equations

`Z(s,w)=A Z(w,s)`

and

`Z(s,w)=B(s) Z(1-s,s+w-1/2)`,

where `A` is constant and `B(s)` is an explicit finite matrix assembled from the fixed mod-`8` character changes and the one-variable quadratic-`L` functional-equation factors. Taking residues gives

`R_w(s) := Res_(w=1) Z(s,w) = (1/2) zeta_2(2s) A e`,

and, with `t=s+w-3/2`,

`R_diag(s) := Res_(t=0) Z(s,3/2-s+t)`

`= (1/2) zeta_2(2-2s) B(s) A e`.

Thus every possible generic simple polar face in Blomer's Lemma 2 is generated from the same principal scalar residue by the `D_12` functional-equation action. The `w=1` face is the variable-swapped copy of the `s=1` collapse, and the diagonal face is its further Weyl transport. Neither operation can restore the varying squarefree kernels / quadratic characters that disappeared when the principal residue selected the trivial squarefree kernel in `PL-242`.

The surviving matrices retain only fixed finite local/parity and archimedean functional-equation data. They do not retain a varying mixed-prime reciprocity relation among the rational-prime coordinates. Consequently **none of the three canonical polar faces of this rank-two model transfers the quadratic-reciprocity family rigidity to the Riemann-zeta divisor**.

**Evidence/status:** `LITERATURE+EXACT-DERIVED + PRIOR-ART-REDIRECT + NEGATIVE-BOUNDARY + NO-NOVELTY-CLAIM`. Decisive for the three possible simple polar hyperplanes of Blomer's 16-component double-series model. It does not rule out non-polar periods, quotients, operator realizations, nor higher-rank multiple Dirichlet series whose residues can retain a nontrivial lower-rank subsystem.

## Exact residue transport

Blomer's Lemma 2 states that

`(s-1)(w-1)(s+w-3/2) Z(s,w;psi,psi')`

extends holomorphically to `C^2`. Hence the only possible polar hyperplanes of this model are

`s=1`, `w=1`, `s+w=3/2`.

The first residue was computed in `PL-242` from Blomer's squarefree-kernel formula (29). For trivial `psi`, only the primitive kernel `d_0=1` has an `L_2(s,chi_(d_0))` pole at `s=1`, and this gives

`Res_(s=1) Z(s,w;psi_1,psi')=(1/2)zeta_2(2w)`.

For nontrivial `psi`, the corresponding component has no such pole. This is exactly the vector identity `R_s(w)=(1/2)zeta_2(2w)e` above.

Now use Blomer's equation (27),

`Z(s,w)=A Z(w,s)`.

At fixed generic `s`, the variable `w` on the right is the **first** variable of `Z(w,s)`. Therefore

`Res_(w=1) Z(s,w)=A Res_(u=1) Z(u,s)`

`=(1/2)zeta_2(2s)A e`.

No continuation of an Euler product is involved in this step; it is an identity between meromorphic vector-valued functions already continued by Blomer.

For the diagonal face use equation (28),

`Z(s,w)=B(s)Z(1-s,s+w-1/2)`.

Put

`t=s+w-3/2`.

Then the second argument on the right is exactly `1+t`, with unit Jacobian. Hence

`Res_(t=0) Z(s,3/2-s+t)`

`=B(s) Res_(v=1) Z(1-s,v)`

`=B(s)R_w(1-s)`

`=(1/2)zeta_2(2-2s)B(s)A e`.

This equality is first read at generic points where the displayed matrices are regular and then holds meromorphically in `s` by uniqueness. Possible zeros or poles of the explicit matrix factor are separate fixed local/archimedean phenomena; the Riemann-sensitive scalar transported along the face is `zeta_2(2-2s)`.

## Why the mixed-prime family cannot reappear

The key information loss happened before these two residue transports. The `s=1` residue forces the squarefree kernel `d_0` in `d=d_0d_1^2` to equal `1`. The nontrivial primitive quadratic characters `chi_(d_0)` — and therefore the support-dependent reciprocity data linking different rational primes — have already vanished.

The matrix `A` in equation (27) implements the finite change of character components needed to exchange the two summation variables. It is constant. Multiplying the collapsed vector by `A` can redistribute its 16 fixed mod-`8` components, but it cannot reconstruct the discarded family of squarefree discriminants.

Likewise `B(s)` comes from the fixed character-basis changes together with the ordinary functional equations of the quadratic `L`-functions. Its entries contain powers, gamma factors, and fixed local character data. Once its input is the already scalarized residue vector `A e`, the output remains a finite matrix multiple of one scalar zeta function. The Weyl functional equation transports the principal residue; it does not invert the projection that produced it.

This is the exact distinction required by the current `prime_lattice` frontier. The full double series before taking residues genuinely has coefficients `chi_d(n)` and hence a source-forced relation between the prime supports of `d` and `n`. The residue orbit does not.

## Critical-line accounting on the three faces

On `s=1`, the Riemann-sensitive scalar is `zeta_2(2w)`, so a nontrivial Riemann zero `rho` is represented at `w=rho/2`, modulo the explicit local factor at `2`.

On `w=1`, the swapped scalar is `zeta_2(2s)`, giving `s=rho/2`.

On `s+w=3/2`, the transported scalar is `zeta_2(2-2s)`. Its Riemann-zero parameterization is

`s=1-rho/2`,

`w=1/2+rho/2`.

If `Re(rho)=1/2`, then this scalar divisor lies on

`Re(s)=Re(w)=3/4`

inside the polar hyperplane `s+w=3/2`. This `3/4` is merely the affine image of the Riemann critical line under Blomer's Weyl map. It is not the joint central line `Re(s)=Re(w)=1/2` of the full two-variable series, and it supplies no independent positivity or self-adjointness principle.

The finite matrix factor `B(s)A e` can add local/archimedean zeros or cancellations to individual components, so the statement here is about the transported **Riemann-sensitive scalar factor**, not an assertion that every component has exactly the same complete zero divisor.

## Adversarial controls

**This closes possible polar faces, not every codimension-one operation.** Lemma 2 limits the poles of this particular double series to the three displayed hyperplanes. One may still restrict to a non-polar affine line, form a quotient, take a period, or construct an operator from the full two-variable object. Those are different mechanisms and are not ruled out here.

**The diagonal residue is not being recomputed from a conditionally convergent Euler product.** It is transported by Blomer's already established meromorphic functional equation. This is precisely why the argument is valid in regions where the original double Dirichlet expansion no longer converges absolutely.

**A matrix-valued residue is not automatically richer arithmetic data.** `B(s)A e` can be nonconstant and nontrivial as a finite vector. The relevant question is whether it retains the source-forced relation between varying rational-prime supports. It does not: after `d_0=1` that varying family is absent, and the remaining matrices depend only on fixed local/parity and archimedean functional-equation data.

**Higher rank is not closed.** In a higher-rank Weyl-group multiple Dirichlet series, taking a residue may leave a genuinely nontrivial lower-rank multiple series rather than a scalar. The present result is specifically the rank-two Blomer model and should not be extrapolated into a universal statement that all multiple-Dirichlet-series residues scalarize.

## Prior-art and novelty audit

No novelty is claimed for the polar divisor, the two functional equations, or their `D_12` group. They are explicit in Blomer. The broader use of polar residues and functional-equation orbits in multiple Dirichlet series is also established in the Diaconu--Goldfeld--Hoffstein framework.

The only derived content stored here is the RH-facing closure of the caveat left by `PL-242`: once its exact principal residue is written as a 16-vector, equations (27) and (28) force the two remaining residue formulas immediately. A targeted literature audit found no reason to treat this transport as a new theorem; it is elementary residue calculus inside the classical functional-equation system. Its research value is negative and architectural: **there is no independent polar face left in this model that could preserve the mixed-prime reciprocity data while isolating the Riemann channel.**

## Consequences for `prime_lattice`

`PL-240` identified a genuine support-dependent mixed-prime relation through Rédei matrices. `PL-241` showed that established quadratic multiple Dirichlet series turn such reciprocity data into a global analytic object with Weyl symmetry and explicit zeta corrections. `PL-242` then showed that the most direct principal residue recovers zeta only by projecting away the nontrivial quadratic family.

The residue loophole in that **specific rank-two construction is now closed completely**: its other possible polar faces are symmetry transports of the same collapse. Future work should not spend further effort testing `s=1`, `w=1`, or `s+w=3/2` residues of this Blomer family as distinct RH mechanisms.

A surviving mixed-prime route must retain a nontrivial arithmetic subsystem after the operation that exposes the Riemann divisor. Plausible categories remain higher-rank constructions with a genuinely nontrivial residual subsystem, non-polar target-relative periods/quotients, or an operator/positivity structure acting on the full reciprocity-coupled object before scalar projection. Any such proposal still has to show a transfer to scalar zeta that is stronger than simply reproducing a rescaled copy of RH.

## Sources

- Valentin Blomer, “Subconvexity for a double Dirichlet series,” *Compositio Mathematica* **147** (2011), 355–374. DOI: https://doi.org/10.1112/S0010437X10004926. arXiv: https://arxiv.org/abs/0907.4867. Lemma 2 gives the three possible polar hyperplanes; equations (27) and (28) give the two vector functional equations; equation (29) is the squarefree-kernel representation used in `PL-242`.
- Adrian Diaconu, Dorian Goldfeld, Jeffrey Hoffstein, “Multiple Dirichlet Series and Moments of Zeta and L-Functions,” *Compositio Mathematica* **139**(3) (2003), 297–360. DOI: https://doi.org/10.1023/B:COMP.0000018137.38458.68. arXiv: https://arxiv.org/abs/math/0110092. Classical framework anchor for meromorphic continuation, polar divisors, residue calculus, and functional-equation propagation in multiple Dirichlet series.
