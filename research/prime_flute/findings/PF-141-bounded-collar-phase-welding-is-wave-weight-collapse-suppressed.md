# PF-141 — bounded collar phase welding is wave-weight collapse-suppressed

**Status:** `EXACT-DERIVED + LITERATURE-BACKED + NEGATIVE/BOUNDARY`. PF-128 proves that changing the length of a collapsing matched standard collar has finite Güneysu--Thalmaier inverse-unit-ball weighted cost `O(|t|)`, but the global prime/shift-clone wave-operator program still has to weld those optimized collar maps to the body comparison. A possible obstruction is a residual angular/Fenchel--Nielsen phase mismatch at a short collar. The present exact collar calculation shows that this mismatch is **not amplified by collapse**: a bounded phase can be interpolated across a fixed central collar window with weighted cost `O(L|tau|)`, where `L` is the short core length. Thus the inverse unit-ball factor cancels the shrinking transverse measure but does not destroy the extra `L` appearing in the shear itself. Composed with PF-128's optimized length map, the local cost is `O(|t|+L|tau|)`. This removes phase as a *local* collapse singularity, but it does not prove the required global sum over all PF-138 short cores, does not straighten a possibly noncircular body trace to the target standard collar, and therefore does not yet resolve the accepted wave-operator clue.

## Claim

For `0<L<L_0`, let

\[
C_L=(-w(L),w(L))\times \mathbb S^1,
\qquad
w(L)=\operatorname{arsinh}\frac1{\sinh(L/2)},
\tag{1}
\]

with standard collar metric

\[
 g_L=dr^2+s_L(r)^2d\theta^2,
\qquad
s_L(r):=L\cosh r,
\qquad
\theta\in\mathbb R/\mathbb Z.
\tag{2}
\]

Fix `R>0`. For all sufficiently small `L`, `[-R,R]` lies inside the standard collar. Choose a fixed smooth cutoff

\[
\psi:\mathbb R\to[0,1],
\qquad
\psi=0\text{ on }(-\infty,-R],
\qquad
\psi=1\text{ on }[R,\infty).
\tag{3}
\]

For a phase discrepancy `tau in R/Z`, take its shortest representative

\[
|\tau|\le\frac12
\tag{4}
\]

and define

\[
\boxed{
T_{L,\tau}(r,\theta)
=
(r,\theta+\tau\psi(r)).
}
\tag{5}
\]

Then `T_{L,tau}` is the identity rotation on the negative side and the constant rotation by `tau` on the positive side; both outside regions are exact collar isometries. If

\[
h_{L,\tau}:=T_{L,\tau}^*g_L,
\tag{6}
\]

then on the support of `psi'`, relative to the `g_L`-orthonormal frame

\[
e_r=\partial_r,
\qquad
e_\theta=s_L(r)^{-1}\partial_\theta,
\tag{7}
\]

the differential is the exact shear

\[
\boxed{
A(r)=
\begin{pmatrix}
1&0\\
a(r)&1
\end{pmatrix},
\qquad
a(r)=s_L(r)\tau\psi'(r).
}
\tag{8}
\]

Hence the two metric-comparison eigenvalues are

\[
\boxed{
\lambda_\pm(r)
=
\exp\!\left(\pm2\operatorname{arsinh}\frac{|a(r)|}{2}\right),
}
\tag{9}
\]

and the area density is unchanged. In particular, with

\[
D_{L,\tau}(r):=\max\{|\log\lambda_+(r)|,|\log\lambda_-(r)|\},
\tag{10}
\]

one has

\[
\boxed{
D_{L,\tau}(r)
=2\operatorname{arsinh}\frac{|a(r)|}{2}
\le |a(r)|
\le C_R L|\tau|\,|\psi'(r)|.
}
\tag{11}
\]

The Güneysu--Thalmaier zeroth-order deviation `delta_{g_L,h_{L,tau}}` is bounded by `C_R D_{L,tau}` under this uniform quasi-isometry bound, exactly as in PF-128. Moreover PF-128's ambient unit-ball estimate gives, on `|r|<=R`,

\[
\mu_L(B_{g_L}((r,\theta),1))
\ge c_R s_L(r),
\qquad
d\mu_L=s_L(r)drd\theta.
\tag{12}
\]

Therefore

\[
\boxed{
\begin{aligned}
&\int_{C_L}
\mu_L(B_{g_L}(z,1))^{-1}
\delta_{g_L,h_{L,\tau}}(z)\,d\mu_L(z)\\
&\qquad\le
C_R\int_{-R}^{R}\int_{\mathbb S^1}D_{L,\tau}(r)\,d\theta dr
\le C_{R,\psi}L|\tau|.
\end{aligned}
}
\tag{13}
\]

Thus

\[
\boxed{
\text{bounded residual collar phase costs }O(L),\text{ not }O(1/L)\text{ or }O(1),
}
\tag{14}
\]

as the core length `L->0`.

If the target collar has length

\[
L'=e^tL,
\qquad |t|\le t_0,
\tag{15}
\]

compose `T_{L,tau}` with PF-128's boundary-to-boundary optimized length comparison. Since both maps have a uniform quasi-isometry bound for fixed `t_0,R`, the logarithmic metric deviations of the composition are bounded, up to a constant depending only on those fixed bounds, by the two individual deviations. PF-128 therefore gives the local combined estimate

\[
\boxed{
\int_{C_L}
\mu_L(B_{g_L}(z,1))^{-1}
\delta_{g_L,\,F_{L,L',\tau}^*g_{L'}}(z)\,d\mu_L(z)
\le C_{R,t_0}\bigl(|t|+L|\tau|\bigr).
}
\tag{16}
\]

For a PF-004/PF-138 canonical short separator beginning in a tail at prime scale `P`, PF-109 supplies

\[
|t|=\left|\log\frac{L_+}{L}\right|=O(P^{-3}).
\tag{17}
\]

Thus any residual phase contributes only the second term `L|tau|`; it is not multiplied by the inverse injectivity scale.

## 1. Exact shear calculation

From (5),

\[
d\theta' = d\theta+\tau\psi'(r)dr.
\]

Therefore

\[
 h_{L,\tau}
 =dr^2+s_L(r)^2\bigl(d\theta+\tau\psi'(r)dr\bigr)^2.
\tag{18}
\]

In the frame (7), the matrix of `h` relative to `g` is

\[
A^TA=
\begin{pmatrix}
1+a^2&a\\
a&1
\end{pmatrix}.
\tag{19}
\]

Its determinant is `1`, and its singular values are

\[
\sigma_\pm
=
\frac{\sqrt{a^2+4}\pm|a|}{2}
=
\exp\!\left(\pm\operatorname{arsinh}\frac{|a|}{2}\right).
\tag{20}
\]

Squaring gives (9). Since the determinant is one, the pullback area form is exactly unchanged. Constant rotations on either side of the transition are isometries, so all metric deviation is confined to the fixed central window where

\[
s_L(r)=L\cosh r\le L\cosh R.
\tag{21}
\]

This is the geometric suppression responsible for (13).

## 2. Why collapse does not hurt the scattering weight here

The dangerous factor in Güneysu--Thalmaier's criterion is the inverse volume of a unit ball. On a thin collar core it is of order `1/s_L(r)`. But the twist shear itself has size

\[
|a(r)|=s_L(r)|\tau\psi'(r)|.
\tag{22}
\]

Multiplying by the area form and the inverse-volume weight gives, schematically,

\[
\frac1{s_L}\times s_L|\tau\psi'|\times s_L\,drd\theta
=
s_L|\tau\psi'|\,drd\theta,
\tag{23}
\]

and on the fixed central window this is `O(L|tau|)`. The inverse-volume loss cancels one shrinking factor, but one factor of the core length remains.

This behavior is different from a crude uniform bilipschitz interpolation, whose pointwise distortion need not carry the `s_L` factor and could therefore spend an order-one weighted budget per collar. The angular interpolation (5) is adapted to the collapsing geometry.

## 3. What this removes from the PF-140 interface problem

PF-138 shows that every sufficiently short closed thin component is a canonical reflection-invariant separator or distinguished cuff, so there is no hidden family of unrelated short collars. PF-140 leaves the closed-collar/body interface as the remaining global Güneysu--Thalmaier gate.

At such an interface, two logically different mismatches can occur:

1. an **angular phase** mismatch along the same standard collar circle;
2. a **transverse/shape** mismatch, where the body trace is not already the desired standard collar circle with controlled first derivative.

PF-141 disposes of the first as a local collapse obstruction. Every phase in `R/Z` has a representative satisfying (4), and (13) shows that collapse makes its optimized local welding cheaper rather than more expensive. In the zero-twist reflection setting there are additionally canonical reflection-fixed points that may pin the phase exactly when the chosen body comparison is equivariant, but PF-141 does not assume or need that stronger compatibility.

The second mismatch remains the real unresolved interface problem. In particular, PF-141 does **not** prove that the PF-130/PF-139 body map lands on the target standard collar boundary, nor that the resulting trace-straightening costs are globally summable.

## 4. Global summability is deliberately not inferred

Even though `|tau|<=1/2`, equation (13) only gives a total phase budget bounded by

\[
C\sum_{\gamma\in\mathcal S}L_\gamma|\tau_\gamma|
\tag{24}
\]

for the PF-138 family `S` of short closed cores. The current prime-flute ledger does not prove

\[
\sum_{\gamma\in\mathcal S}L_\gamma<\infty,
\tag{25}
\]

and no such assertion is imported here. Thus a bounded residual phase on every short separator is not, by itself, enough to finish the global wave-operator criterion.

What is now falsified is the narrower concern that a phase mismatch must cost `O(1)` or worse per pinched collar because unit-ball volume tends to zero. It does not: the exact hyperbolic shear carries the compensating core-length factor.

## 5. Novelty / prior-art audit

Fenchel--Nielsen twists, Dehn-twist interpolations on annuli, and the fact that twist data become degenerate when a cuff is pinched are classical Teichmüller geometry; no novelty is claimed for the existence of a collar twist map. Directed searches also found standard recent formulations of Fenchel--Nielsen twist via cross-ratio coordinates, but no theorem was located that directly supplies the Güneysu--Thalmaier inverse-unit-ball weighted estimate needed for this infinite zero-systole interface problem.

The external spectral ingredient is already catalogued as `S16`: Güneysu--Thalmaier prove existence and completeness of wave operators for complete quasi-isometric metrics under the global integral condition involving `mu(B(x,1))^{-1} delta_{g,h}` when Ricci curvature is bounded below. PF-128 already audited that theorem against the standard collapsing collar and established the unit-ball lower bound reused in (12).

Accordingly, the project-specific contribution of PF-141 is only the exact weighted **phase-welding estimate** (13) and its role in the prime/shift-clone assembly. Historical novelty is not claimed for the abstract shear computation.

## Research consequence

The closed-thin-part frontier after PF-140 can be sharpened from

\[
\text{length + phase + trace-shape welding}
\]

to

\[
\boxed{
\text{trace-shape/transverse welding, with global summability control}.
}
\tag{26}
\]

PF-128 controls the matched short-core length change, and PF-141 shows that residual angular phase is collapse-suppressed. A proof of the accepted wave-operator clue must still construct a single global marking whose body/collar traces can be straightened with finite total weighted metric deviation. Conversely, if that final step fails, the obstruction must come from genuinely transverse/nonlocal interface geometry rather than from the elementary pinching amplification of a circle phase.
