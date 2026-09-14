# PL-310 — The small-order interval Green operator has a universal stretched-boundary fixed profile

**Evidence:** `LITERATURE+EXACT-DERIVED + POSITIVE-ROUTE-REFINEMENT + MATCHED-CONTROL`

**Status:** `EXACT-STRETCHED-GREEN-MEASURE-LIMIT + UNIQUE-VOLTERRA-FIXED-PROFILE + COMPLETED-WEIL-PROFILE-COMPACTNESS-AND-AMPLITUDE-OPEN`

## Precise claim

`PL-309` identified the exponential coordinate sampled by the one-dimensional fractional Green trace. The **full Green operator**, not only its endpoint trace, has a nontrivial limit on the same scale.

Let `I=(-1,1)`, `0<s<1/2`, and let `G_s` be the zero-exterior Green kernel of `(-Delta)^s` on `I`. For `r,q>0` set

\[
x_s(r)=1-2e^{-r/s},
\qquad
x_s(q)=1-2e^{-q/s},
\]

and push Green measure into the stretched coordinate:

\[
d\mu_{s,r}(q)
:=G_s(x_s(r),x_s(q))\frac{2}{s}e^{-q/s}\,dq.
\tag{PL310-1}
\]

For every fixed `r>0`, these positive finite measures converge weakly on `(0,infinity)` to

\[
\boxed{
 d\mu_r(q)
 =e^{-r-q}\mathbf 1_{0<q<r}\,dq
 +e^{-2r}\delta_r(dq).
}
\tag{PL310-2}
\]

Equivalently, for bounded continuous test functions for which the displayed integrals are finite,

\[
\boxed{
(TF)(r)
:=\lim_{s\downarrow0}
\int_0^\infty F(q)\,d\mu_{s,r}(q)
=e^{-2r}F(r)
+e^{-r}\int_0^r e^{-q}F(q)\,dq.
}
\tag{PL310-3}
\]

The limiting operator has a one-dimensional fixed-point cone. If `F in L^1_loc((0,infinity))` and `TF=F` almost everywhere, then

\[
\boxed{
F(r)=\frac{C}{\sqrt{e^{2r}-1}}
}
\tag{PL310-4}
\]

for a constant `C`. This profile has the two asymptotic faces

\[
F(r)\sim \frac{C}{\sqrt{2r}}
\quad(r\downarrow0),
\qquad
F(r)\sim Ce^{-r}
\quad(r\to\infty).
\tag{PL310-5}
\]

Thus the small-order Green geometry itself contains a canonical crossover between the logarithmic-Laplacian boundary scale `|log delta|^{-1/2}` and the fixed-order fractional quotient scale `delta^s`: under `delta=2e^{-r/s}`, the former becomes `sqrt(s/r)` while the latter becomes `2^s e^{-r}`.

This is a **universal principal-part statement**, not rational-prime rigidity. For the completed-Weil regularization of `PL-308`, it gives a sharp conditional consequence: if the rescaled profiles

\[
U_s(r):=s^{-1/2}w_s(x_s(r))
\tag{PL310-6}
\]

have enough local compactness/uniform integrability to pass through the Green representation, and if the lower completed-Weil source is uniformly bounded on this scale, then every nonzero subsequential limit must be of the form (PL310-4). The prime/completion perturbation is multiplied by `2s` in the fractional eigen-equation, so after the `sqrt(s)` rescaling it is lower order. The remaining analytic information is therefore the **amplitude** `C` and the compactness needed to justify the passage, not an arbitrary boundary-layer shape.

## 1. Exact off-diagonal Green asymptotics

Bucur's one-dimensional ball formula, already used in `PL-309`, is

\[
G_s(x,y)
=\frac{|x-y|^{2s-1}}{2^{2s}\Gamma(s)^2}
\int_0^{R(x,y)}\frac{z^{s-1}}{\sqrt{1+z}}\,dz,
\qquad
R(x,y)=\frac{(1-x^2)(1-y^2)}{|x-y|^2}.
\tag{PL310-7}
\]

Write

\[
t=e^{-r/s},\qquad u=e^{-q/s},
\qquad x=1-2t,\qquad y=1-2u.
\]

If `0<q<r` is fixed, then `epsilon=t/u=e^{-(r-q)/s}->0` and

\[
|x-y|=2u(1-\varepsilon),
\qquad
R(x,y)
=\frac{4\varepsilon(1-t)(1-u)}{(1-\varepsilon)^2}.
\]

The upper limit is exponentially small. Hence

\[
\int_0^R\frac{z^{s-1}}{\sqrt{1+z}}\,dz
=\frac{R^s}{s}(1+o(1)),
\]

and after multiplying by the exact Jacobian `dy=(2/s)u dq`,

\[
G_s(x_s(r),x_s(q))\frac{2}{s}e^{-q/s}
\longrightarrow e^{-r-q}.
\tag{PL310-8}
\]

For fixed `q>r`, the same calculation with `u/t=e^{-(q-r)/s}` gives an extra factor

\[
e^{-(q-r)/s},
\]

so

\[
G_s(x_s(r),x_s(q))\frac{2}{s}e^{-q/s}
\longrightarrow0.
\tag{PL310-9}
\]

This one-sided limit is the Volterra part of (PL310-2).

## 2. The missing mass becomes an atom at the moving pole

The off-diagonal calculation cannot see the singularity `q=r`. There the upper limit in (PL310-7) tends to infinity as `q->r`, and

\[
\int_0^\infty\frac{z^{s-1}}{\sqrt{1+z}}\,dz
=\frac{\Gamma(s)\Gamma(1/2-s)}{\Gamma(1/2)}.
\]

For `h=q-r` near zero,

\[
|x_s(q)-x_s(r)|
=\frac{2e^{-r/s}}{s}|h|(1+o(1)),
\]

so the transformed Green density has the singular asymptotic

\[
G_s(x_s(r),x_s(r+h))\frac{2}{s}e^{-(r+h)/s}
=
 e^{-2r}
\frac{\Gamma(1/2-s)}{\sqrt\pi\,\Gamma(s)}
 s^{-2s}|h|^{2s-1}(1+o(1)).
\tag{PL310-10}
\]

Since `Gamma(s)^(-1)~s`, the standard approximate-identity law

\[
s|h|^{2s-1}\,dh\Longrightarrow\delta_0(dh)
\]

on a two-sided neighborhood gives exactly the atom `e^{-2r} delta_r`.

As a normalization check, direct beta-function integration of (PL310-7) with unit forcing gives the classical interval torsion mass

\[
\int_{-1}^1G_s(x,y)\,dy
=
\frac{\sqrt\pi}{2^{2s}\Gamma(1+s)\Gamma(s+1/2)}
(1-x^2)^s.
\tag{PL310-11}
\]

At `x=x_s(r)` this tends to `e^{-r}`. The absolutely continuous mass in (PL310-2) is

\[
e^{-r}\int_0^r e^{-q}\,dq
=e^{-r}-e^{-2r},
\]

and the diagonal atom contributes the missing `e^{-2r}`, reproducing the exact total limit. The part of the physical interval that collapses to `q=0` contributes no additional atom; fixed bulk sets have Green mass `O(s)` at `x_s(r)`. The region `q>r+epsilon` is exponentially suppressed by (PL310-9). These checks complete the weak-measure limit (PL310-2).

## 3. The limiting fixed profile is explicit and unique

Suppose `TF=F`. Define

\[
V(r)=\int_0^r e^{-q}F(q)\,dq.
\]

Then (PL310-3) gives

\[
(1-e^{-2r})F(r)=e^{-r}V(r),
\]

while `V'(r)=e^{-r}F(r)`. Therefore

\[
V'(r)=\frac{e^{-2r}}{1-e^{-2r}}V(r)
=\frac{1}{e^{2r}-1}V(r).
\tag{PL310-12}
\]

The nontrivial solutions are

\[
V(r)=C\sqrt{1-e^{-2r}},
\]

which yields (PL310-4). The singular coefficient in (PL310-12) is important: although `V(0)=0`, the equation admits the `sqrt(r)` branch rather than forcing `V=0`.

The two ends of this one profile reproduce exactly the two boundary regimes already isolated independently in the line. For `r->infinity`, (PL310-4) is `Ce^{-r}`, the `delta^s` trace tail. For `r->0`, it is `C/(sqrt(2r))`. Since

\[
|\log\delta|
=\frac{r}{s}+O(1),
\qquad
\delta=2e^{-r/s},
\]

the sharp logarithmic scale `ell(delta)^(1/2)=|log delta|^(-1/2)` becomes `sqrt(s/r)`, matching the same profile after division by `sqrt(s)`.

This does **not** prove equality of a logarithmic Hopf coefficient and a fractional quotient-trace limit. That identification requires an overlap/compactness theorem which is precisely the singular gate left open by `PL-309`.

## 4. Conditional consequence for the completed-Weil eigen-equation

`PL-308` writes the regularized completed-Weil eigen-equation as

\[
(-\Delta)^s w_s
=\alpha_{s,a}w_s-2sa^{2s}B_aw_s,
\qquad
\alpha_{s,a}=a^{2s}[1+2s(\lambda_s(a)-c)].
\tag{PL310-13}
\]

On the tracked small-order branch, `alpha_{s,a}->1`. Dividing its Green representation by `sqrt(s)` gives formally

\[
U_s(r)
=
\int_0^\infty
\left[
\alpha_{s,a}U_s(q)
-2\sqrt{s}\,a^{2s}(B_aw_s)(x_s(q))
\right]
\,d\mu_{s,r}(q).
\tag{PL310-14}
\]

At fixed aperture the operator `B_a` is a finite sum of compressed translations plus bounded completion/scalar terms. Consequently, **if** the actual branch has a uniform `L^infty` bound strong enough to keep `B_aw_s` bounded and if `U_s` is compact/uniformly integrable for the limiting Green measures, the second term in (PL310-14) vanishes and every subsequential limit satisfies `TU=U`. Equation (PL310-4) then leaves only one scalar degree of freedom.

This is the useful advance over `PL-309`: the eigen-equation does impose a rigid candidate shape on the exponential layer. But the hypotheses needed to pass to it are not supplied by ordinary bulk `C_0` convergence, precisely because `PL-309` showed that the layer is invisible to such convergence. No claim is made here that those hypotheses already hold for the completed-Weil branch.

The calculation also gives a matched-control warning. The leading crossover profile is produced by the pure fractional principal operator and is therefore universal under replacement of the rational-prime lower source by any bounded matched lower-order perturbation. Any RH-relevant rigidity must enter through the amplitude/global matching, the weak virial, or a source-specific sign law; the shape (PL310-4) itself cannot be treated as arithmetic evidence.

## 5. Prior-art and adversarial audit

The Green kernel and zero-exterior representation are classical; source `102` in `research/prime_lattice/SOURCES.md` (Bucur 2016) is the load-bearing literature anchor. Source `97` gives the sharp logarithmic-Laplacian `ell(delta)^(1/2)` boundary scale used only for the matching interpretation. `PL-297` supplies the independent pure-branch `sqrt(s)` quotient-trace normalization, while `PL-308` supplies the exact completed-Weil fractional eigen-equation and `PL-309` supplies the stretched coordinate and the generic bulk-convergence obstruction.

A targeted prior-art search around small-order fractional Green kernels, stable-process potential theory, small-order eigenfunction asymptotics, logarithmic-Laplacian boundary regularity, and boundary-layer scalings located the established Green formulas and small-order/boundary estimates but did not surface the specific weak limit (PL310-2) or fixed profile (PL310-4). Search absence is **not** used as evidence of broad novelty. The durable claim is the exact derivation from the classical interval Green kernel and its line-local consequence for the accepted zero-order stress route.

Adversarial checks:

- **No bulk/profile interchange is assumed in the exact theorem.** Equations (PL310-2)--(PL310-5) concern the Green kernel itself. The completed-Weil consequence is explicitly conditional on profile compactness/uniform integrability.
- **The diagonal atom is essential.** Dropping it gives the wrong total Green mass and the wrong fixed-point equation.
- **No rational-prime specificity is hidden in the profile.** The lower Weil operator enters (PL310-14) with an explicit `sqrt(s)` prefactor after rescaling; bounded matched lower perturbations have the same leading profile.
- **No signed stress is obtained.** The profile constant `C` may carry sign for a signed branch, but neither its existence nor its rational-prime sign is proved here.
- **No claim across varying apertures or activations is needed.** The calculation is at one fixed source-static aperture; `PL-305` separately controls first-order activation once the state regularity is available.

## Consequence for the research line

The small-order endpoint is no longer only an unspecified exponential boundary layer. Its **principal Green geometry is explicit**: a one-sided Volterra kernel plus a diagonal atom, with a unique nonzero fixed shape `1/sqrt(e^(2r)-1)`. This gives a concrete analytic target for the accepted zero-order Hadamard clue.

The next useful theorem should therefore not seek another generic bulk estimate. It should prove, for the actual isolated completed-Weil branch, enough stretched-profile tightness to pass (PL310-14), or bypass that profile by proving the same scalar amplitude through the weak virial in `PL-308`. If the profile route succeeds, the only remaining boundary-layer datum is its amplitude; after that the separate rational-prime-specific sign/first-crossing problem remains untouched.

## Sources

- Claudia Bucur, “Some observations on the Green function for the ball in the fractional Laplace framework,” *Communications on Pure and Applied Analysis* **15**(2) (2016), 657–699. DOI: https://doi.org/10.3934/cpaa.2016.15.657. arXiv: https://arxiv.org/abs/1502.06468. Theorems 3.1--3.3 supply the exact ball Green kernel and zero-exterior representation.
- Source `97` in `research/prime_lattice/SOURCES.md`: Hernández-Santamaría--López Ríos--Saldaña (2025), used only for the sharp logarithmic boundary scale.
- `PL-297`, `PL-308`, and `PL-309`: line-local controls and the completed-Weil specialization described above.
