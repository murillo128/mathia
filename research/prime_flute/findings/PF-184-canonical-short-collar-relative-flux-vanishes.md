# PF-184 — canonical short-collar relative flux vanishes by finite-side area balance

**Status:** `EXACT-DERIVED + CLASSICAL-FLUX + POSITIVE/BOUNDARY`. PF-183 reduces the remaining `S_r`, `r>1`, geometric gate to an exact-area splice on one normalized thick annulus around each PF-138 true short separator, but leaves open whether the relative collar/body germ carries a flux/action obstruction. For the canonical prime/shift comparison that obstruction is **exactly zero**. Every tail short core bounds a finite consecutive cusp block; source and clone blocks have the same hyperbolic area by Gauss--Bonnet, and the PF-179--PF-182 body map preserves area and labels exactly. Hence a body image of any parallel collar loop and the PF-177 identity-area-coordinate image of the same loop enclose equal signed area. In the annular area coordinate this is precisely the vanishing of the unique period of `H^*(x dtheta)-x dtheta` for the relative symplectic germ `H`. The one-form is therefore exact. Thus a nonzero annular flux/action class cannot obstruct the PF-183 splice. What remains is genuinely quantitative: produce a conservative localization whose `L^r` metric cost is controlled by the already present body strain. PF-184 does not construct that localization, prove PF-183 equation (11), establish the complete PF-175 weighted hypothesis, any Schatten conclusion, scattering equivalence, or RH consequence.

## Claim

Let `X` be the exact zero-twist prime flute, `X_+` its exact all-composite shift clone, and

\[
F_{\mathrm{body}}:X\to X_+
\tag{1}
\]

be the label-preserving exact-area body comparison of PF-179--PF-182 used in PF-183. Let `eta` be a sufficiently far PF-138 Margulis-short canonical separator, and let `eta_+` be its matched clone separator. Write

\[
K_\eta\subset X,
\qquad
K_\eta^+\subset X_+
\tag{2}
\]

for the finite components bounded by `eta,eta_+` and containing the same consecutive block of `k` labeled cusps.

Choose the signed PF-177 area coordinates so that `x>0` points from the finite component across `eta` toward the infinite side:

\[
x=L_\eta\sinh r,
\qquad
X=L_\eta^+\sinh r_+,
\qquad
d\mu_X=dx\,d\theta,
\qquad
d\mu_{X_+}=dX\,d\theta,
\tag{3}
\]

with `theta in R/Z`, and let

\[
G_\eta(x,\theta)=(x,\theta)
\tag{4}
\]

be the PF-177/PF-183 exact-area collar gauge on a common fixed subcollar.

For any fixed parallel loop

\[
C_a=\{x=a\},
\qquad 0<a\le5/4,
\tag{5}
\]

lying in a common collar neighborhood on which both germs can be compared, the two target loops

\[
F_{\mathrm{body}}(C_a),
\qquad
G_\eta(C_a)=\{X=a\}
\tag{6}
\]

have zero signed area between them.

Equivalently, in the common annular area chart put

\[
H_\eta:=G_\eta^{-1}\circ F_{\mathrm{body}}.
\tag{7}
\]

For the standard primitive

\[
\lambda=x\,d\theta,
\qquad d\lambda=dx\wedge d\theta,
\tag{8}
\]

the closed one-form

\[
\alpha_\eta:=H_\eta^*\lambda-\lambda
\tag{9}
\]

has vanishing period on the generator of the annulus:

\[
\boxed{
\int_{C_a}\alpha_\eta=0.
}
\tag{10}
\]

Since `H^1(A;R)` of an annulus is one-dimensional and detected by this period,

\[
\boxed{
\alpha_\eta=dS_\eta
}
\tag{11}
\]

for a single-valued smooth potential `S_eta` on every connected common annular germ. Thus the relative prime/shift body germ is **exact symplectic in the annular sense**: the cohomological flux/action mode that could forbid a conservative cutoff is absent.

This conclusion is exact and does not use a summability estimate. It does not imply the quantitative PF-183 splice bound.

## 1. The finite side has exactly the same source and target area

PF-138 identifies every sufficiently far short separator with the primitive boundary of a finite consecutive cusp block. The finite component `K_eta` is genus zero with `k` cusps and one geodesic boundary. Its Euler characteristic is

\[
\chi(K_\eta)=1-k.
\tag{12}
\]

The boundary is geodesic and each cusp contributes the standard zero boundary term, so Gauss--Bonnet gives

\[
\boxed{
\operatorname{Area}(K_\eta)
=-2\pi\chi(K_\eta)
=2\pi(k-1).
}
\tag{13}
\]

The matched clone separator encloses exactly the same number and labels of cusps. Hence

\[
\boxed{
\operatorname{Area}(K_\eta)
=
\operatorname{Area}(K_\eta^+).
}
\tag{14}
\]

No approximation in the separator length enters (14). In particular, changing `L_eta` to `L_eta^+` does not change the finite-side area.

Now let `Omega_a` be the region bounded by `C_a` and containing `K_eta`. With the sign convention in (3), the strip from `x=0` to `x=a` has exact area `a`, because `theta` has period one. Therefore

\[
\operatorname{Area}(\Omega_a)
=
\operatorname{Area}(K_\eta)+a.
\tag{15}
\]

The target canonical region `Omega_a^+` bounded by `G_eta(C_a)={X=a}` satisfies the identical formula. Combining (14)--(15),

\[
\boxed{
\operatorname{Area}(\Omega_a)
=
\operatorname{Area}(\Omega_a^+).
}
\tag{16}
\]

## 2. Exact area preservation turns finite-side equality into zero annular action

The assembled map `F_body` preserves hyperbolic area exactly. It also preserves the ordered cusp labels. Consequently `F_body(Omega_a)` is the target region bounded by `F_body(C_a)` that contains the same finite cusp block, and

\[
\operatorname{Area}(F_{\mathrm{body}}(\Omega_a))
=
\operatorname{Area}(\Omega_a).
\tag{17}
\]

Equations (16)--(17) show that `F_body(C_a)` and `G_eta(C_a)` bound target regions of equal area. Hence the signed annular region `D_a` between those two homologous loops has

\[
\boxed{
\int_{D_a}d\mu_{X_+}=0.
}
\tag{18}
\]

On a common target collar chart use `lambda_+=X dtheta`. Stokes' theorem gives

\[
\int_{F_{\mathrm{body}}(C_a)}\lambda_+
-
\int_{G_\eta(C_a)}\lambda_+
=
\int_{D_a}d\lambda_+
=0.
\tag{19}
\]

Pulling (19) back by `G_eta` is exactly (10).

There is also an intrinsic annular check. Since `H_eta` preserves `dx wedge dtheta`,

\[
d\alpha_\eta
=H_\eta^*(dx\wedge d\theta)-dx\wedge d\theta
=0.
\tag{20}
\]

Thus the period in (10) is independent of which generator `C_a` is used. The finite-side area calculation supplies one value of that constant period, namely zero.

## 3. Zero period is exactly the missing cohomological compatibility

For an annulus `A`,

\[
H^1(A;\mathbb R)\cong\mathbb R,
\tag{21}
\]

and integration around one oriented core circle detects the cohomology class. Equations (10), (20), and (21) therefore imply (11).

This is the elementary exact-symplectic form of the annular flux condition. General flux theory packages the same obstruction as the cohomology class of a symplectic isotopy. Here no general theorem is needed to compute it: the primitive difference (9) is explicit, closedness follows from exact area preservation, and the only period is killed by (13)--(19).

The result matters because the PF-183 cutoff cannot be exact-area if the body germ carries a nonzero radial area flux relative to the collar gauge. PF-184 proves that the canonical marked prime/shift germ does **not** carry such a flux. A generating-function or Hamiltonian localization may therefore be sought without first adding a separate per-collar flux-correction ledger.

## 4. Reflection alone would not have been enough

PF-142 removes the constant angular phase by the zero-twist marking, but that fact does not by itself prove (10). In the flat area cylinder, the local translation

\[
(x,\theta)\mapsto(x+c,\theta)
\tag{22}
\]

preserves `dx wedge dtheta` and commutes with the angular reflection `theta -> -theta`, yet

\[
H^*\lambda-\lambda=c\,d\theta
\tag{23}
\]

has nonzero period when `c ne 0`.

Thus the new cancellation is not another reflection-gauge observation. It uses the **separating finite-side geometry plus exact global area preservation**. This is also the relevant adversarial control: if label preservation or finite-side area equality failed, a genuine radial flux obstruction could survive even in a reflection-equivariant comparison.

## 5. Consequence for the PF-183 splice gate

PF-183 listed two qualitatively different possible reasons the normalized annular splice might fail:

- a topological/flux/action incompatibility;
- failure of any exact-area localization to obey the required energy-local `L^r` estimate.

PF-184 removes the first item for the canonical PF-179--PF-182 body comparison and every tail PF-138 true short separator. The remaining problem is therefore quantitative.

On the fixed slab `1<=|x|<=5/4`, one still has to turn the exact primitive `S_eta` from (11), or an equivalent conservative parametrization, into a cutoff which equals the PF-177 gauge on the inner side and `F_body` on the outer side while proving

\[
E_r(\operatorname{splice}_\eta)
\le
C_r\left(
E_r^{\mathrm{body}}(T_\eta)+|t_\eta|^r
\right)
\qquad(r>1),
\tag{24}
\]

on both source and target sides. Exactness alone gives no `W^{2,r}` or metric-strain bound for the primitive and does not control the cost of cutting it off. PF-143--PF-145 continue to rule out any argument that simply declares nonconstant interface traces cheap.

Therefore PF-184 is a **gate removal**, not the desired splice theorem. It narrows a negative result too: a counterexample to (24) can no longer be based on a nonzero annular flux/action class of the actual canonical relative germ.

## 6. Prior art and novelty audit

No novelty is claimed for Gauss--Bonnet, Stokes' theorem, de Rham cohomology of the annulus, exact symplectomorphisms, or the flux homomorphism. Standard background is given by D. McDuff and D. Salamon, *Introduction to Symplectic Topology*, 3rd ed., Oxford University Press (2017), Chapter 10, DOI `10.1093/oso/9780198794899.001.0001`, which develops the symplectomorphism group and flux homomorphism. Y. Ozan, *Relative flux homomorphism in symplectic geometry*, Proceedings of the AMS 133 (2005), 1223--1230, DOI `10.1090/S0002-9939-04-07611-7`, is nearby relative-flux prior art.

A targeted search also revisited conservative-pasting literature already used in PF-178/PF-182. Those sources provide general volume/symplectic localization technology but do not supply the project-specific cancellation (18), because that cancellation depends on the canonical PF-138 separator enclosing a finite cusp block of the same Gauss--Bonnet area in the prime and clone surfaces.

The durable custom deduction is deliberately narrow:

\[
\boxed{
\text{canonical finite block}
+\text{ exact-area label-preserving body map}
\Longrightarrow
\text{zero relative annular flux}.}
\tag{25}
\]

The bounded literature search found no reason to treat (25) as a new general symplectic theorem, and PF-184 makes no such claim.

## 7. Audit / falsification core

A later adversary can check PF-184 through the following finite chain:

1. verify from PF-138 that every tail short core is a canonical separator of a finite consecutive cusp block;
2. apply Gauss--Bonnet to the source and matched clone finite components and verify (13)--(14);
3. in PF-177 area coordinates verify that the strip between `x=0` and `x=a` has area exactly `a` on both surfaces;
4. verify that the PF-179--PF-182 assembled body comparison preserves area and ordered cusp labels, so (17) holds for the region bounded by `C_a`;
5. subtract the two finite-side areas to obtain the zero signed area (18);
6. apply Stokes in a common collar neighborhood to derive the period identity (10);
7. verify directly that `d(H_eta^*lambda-lambda)=0` and that zero period on the annulus generator implies exactness (11);
8. keep the quantitative boundary explicit: do not infer (24), PF-175, any `S_r` statement, wave operators, scattering equivalence, or RH consequences from exactness alone.

A failure of steps 1--7 would refute the flux cancellation. Failure to obtain the energy-local cutoff in step 8 would not refute PF-184; it is now the remaining local analytical frontier.