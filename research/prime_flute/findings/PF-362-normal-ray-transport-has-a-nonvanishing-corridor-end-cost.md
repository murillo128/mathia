# PF-362 — normal-ray transport has a nonvanishing corridor-end cost

**Status:** EXACT-DERIVED + GEOMETRIC-TRANSPORT-BOUNDARY + CLASSICAL-DIRECTIONAL-ENERGY + GLOBAL-SHORTED-ANGLE-OPEN.

PF-361 controls finite-window truncation of the straight-coordinate corridor model. Its separation-independent relative estimate cannot simply include the actual normal-ray correspondence. On the growing embedded corridor, identical nonconstant oscillations in the two inherited cuff coordinates have zero straight-coordinate difference energy but a strictly positive limiting **transverse** energy. This persists after the small equidistant seam removals used by the flute and under distinct-frequency perturbations of size `o(sqrt(s))`.

The defect comes from the ends `|t|=log(1/s)+O(1)`, where the two boundary coordinates differ by a nonzero amount. It has an additive derivative bound, uniform in the collapsing distance `s`, but no uniform relative bound by straight-coordinate difference energy alone. This is a geometric comparison obstruction, not a conclusion about the globally shorted prime-flute angle: the matching-wave controls are not asserted to occur on its unequal Fourier lattices, and the full pant energy has additional terms.

## 1. Exact correspondence and directional energy

Take two ultraparallel geodesics at distance `s>0`, with equally oriented arclength coordinates centered at their common perpendicular. In the hyperboloid model they are

\[
A(t)=(\cosh t,\sinh t,0),\qquad
B(u)=(\cosh s\cosh u,\sinh u,\sinh s\cosh u).
\tag{1}
\]

The first Fermi chart is

\[
X(r,t)=(\cosh r\cosh t,\cosh r\sinh t,\sinh r),
\qquad g=dr^2+\cosh^2r\,dt^2.
\tag{2}
\]

Fix `0<theta<=1/2`, set `h=sinh(s)`, and restrict to

\[
|t|\le T_s=\operatorname{arsinh}(\theta/h),\qquad
y=h\sinh t,\qquad z=\sqrt{h^2+y^2}.
\tag{3}
\]

PF-230's axis graph and the untrimmed correspondence are

\[
r_s(t)=\operatorname{artanh}(\tanh s\cosh t),
\qquad \tanh u_0(t)=\cosh s\tanh t.
\tag{4}
\]

Allow inward equidistant offsets `rho_1,rho_2>=0`, possibly depending on `s`, subject to

\[
\rho_1+\rho_2\le a s,\qquad 0\le a<1/4.
\tag{5}
\]

These are **inherited cuff coordinates** on the hypercycles: their own arclengths are `cosh(rho_1)t` and `cosh(rho_2)u`. No identification of these two arclengths is assumed. The first boundary is `r=rho_1`. PF-230's exact second-boundary graph is

\[
R_s(t)=r_s(t)-\operatorname{arsinh}
 \frac{\sinh\rho_2}{\sqrt{1-y^2}}.
\tag{6}
\]

Writing the second hypercycle as
`cosh(rho_2) B(u)-sinh(rho_2)(sinh(s),0,cosh(s))`
and comparing its middle coordinate with (2) gives the exact transport

\[
u_\rho(t)=\operatorname{arsinh}
 \frac{\cosh R_s(t)\sinh t}{\cosh\rho_2}.
\tag{7}
\]

For all sufficiently small `s`, depending only on `a,theta`, the remaining corridor is nonempty. Define its radial resistance

\[
b_s(t)=\int_{\rho_1}^{R_s(t)}\operatorname{sech}r\,dr
=\arctan(\sinh R_s(t))-\arctan(\sinh\rho_1).
\tag{8}
\]

For boundary traces `f(t),g(u)`, let

\[
\mathcal B_s^\rho[f,g]
=\int_{-T_s}^{T_s}
 \frac{|f(t)-g(u_\rho(t))|^2}{b_s(t)}\,dt.
\tag{9}
\]

This is the exact infimum of the **radial part** of Dirichlet energy when each ray is minimized separately. Indeed Cauchy--Schwarz gives

\[
|f(t)-g(u_\rho(t))|^2
\le b_s(t)\int_{\rho_1}^{R_s(t)}
 \cosh r\,|\partial_r U(r,t)|^2dr,
\tag{10}
\]

with equality for an affine function of `arctan(sinh(r))` on that ray. Integrating proves (9). The full Dirichlet energy, and likewise the energy with a positive mass shift, is at least (9); tangential energy is not claimed to vanish for the raywise minimizer.

## 2. A positive limit for a common oscillation

For every fixed real `xi!=0`, take `f(t)=exp(i xi t)` and `g(u)=exp(i xi u)`. Uniformly over all offset choices satisfying (5),

\[
\boxed{\mathcal B_s^\rho[f,g]\longrightarrow
 C_\theta(\xi):=
 2\int_0^\theta
 \frac{|1-\exp(i\xi d(y))|^2}{y\arcsin y}\,dy>0,}
\qquad
d(y)=-\tfrac12\log(1-y^2).
\tag{11}
\]

Complex notation combines two real controls: (9) for the exponential is the sum of the costs for matching cosine and matching sine traces. At least one real control therefore carries at least half the cost for each `s`. A separate limit for each real component is not asserted.

### Proof and uniform bounds

For `y>=0`, hyperbolic subtraction in (4) gives

\[
\delta_0(y):=u_0(t)-t
=\operatorname{artanh}
 \frac{y\sqrt{h^2+y^2}}{\cosh s+1-y^2}.
\tag{12}
\]

The correction subtracted in (6) is at most `2 rho_2` for small `s`, uniformly on `|y|<=theta`. Since `r_s>=s`, (5) implies

\[
R_s-\rho_1\ge(1-2a)r_s,\qquad R_s>\rho_2.
\tag{13}
\]

Consequently (7), (12) and the boundedness of `r_s` on this corridor give, with constants depending only on `a,theta`,

\[
0\le\delta_\rho(y):=u_\rho(t)-t\le\delta_0(y)
\le C y\sqrt{h^2+y^2},\qquad
c\sqrt{h^2+y^2}\le b_s(t)\le C\sqrt{h^2+y^2}.
\tag{14}
\]

For the lower resistance bound use
`b_s>=sech(r_s)(R_s-rho_1)` and
`r_s>=sqrt(h^2+y^2)/cosh(s)`; the upper bound follows from `b_s<=r_s`.

For each fixed `0<y<=theta`, as `s->0`,

\[
r_s\to\operatorname{artanh}y,\qquad
b_s\to\arcsin y,\qquad
\delta_\rho\to\log\cosh(\operatorname{artanh}y)=d(y).
\tag{15}
\]

Here the offsets tend to zero regardless of whether their ratios to `s` converge. For example, (7) and `sinh(t)=y/h` show the last limit directly by the large-argument asymptotic of `arsinh`.

Oddness of the correspondence and `dt=dy/sqrt(h^2+y^2)` express (9) as

\[
2\int_0^\theta
 \frac{|1-\exp(i\xi\delta_\rho(y))|^2}
 {b_s(t)\sqrt{h^2+y^2}}\,dy.
\tag{16}
\]

By (14), its integrand is bounded by `C xi^2 y^2`, independently of `s` and the offsets. Dominated convergence proves (11), and the bounds and convergence on every `[epsilon,theta]` give uniformity over (5). The limit is finite at zero because `d(y)~y^2/2`; it is positive because `d` is nonconstant and `xi!=0`. In the additional limit `theta->0` with `xi` fixed,

\[
C_\theta(\xi)=\xi^2\theta^3/6+O_\xi(\theta^5).
\tag{17}
\]

The theorem fixes `theta` before sending `s` to zero. It does not forbid using a shrinking subwindow, which would require a new window/order comparison in PF-361.

The limiting contribution is missed on every fixed `t` window: there `delta_rho=O(s^2)` and `b_s` is comparable to `s`, so its cost tends to zero. Keeping `y` fixed instead means `t=log(1/s)+O(1)`. For the untrimmed corridor, (8) also gives the useful identity

\[
b_s(t)=\arcsin\frac{\sqrt{h^2+y^2}}{\cosh s}.
\tag{18}
\]

## 3. An additive bound is available; a relative difference bound is not

Define the straight-coordinate form using the **same** resistance:

\[
\mathcal B_{s,0}^\rho[f,g]
=\int_{-T_s}^{T_s}\frac{|f(t)-g(t)|^2}{b_s(t)}dt.
\tag{19}
\]

It is uniformly comparable to the finite-window difference form
`s^(-1) integral |f-g|^2 sech(t) dt`, by (14). If `g` is Lipschitz on the interval containing both coordinate ranges, Minkowski and (14) yield

\[
\boxed{\left|\sqrt{\mathcal B_s^\rho[f,g]}
             -\sqrt{\mathcal B_{s,0}^\rho[f,g]}\right|
\le\left(\int_{-T_s}^{T_s}
 \frac{|g(u_\rho(t))-g(t)|^2}{b_s(t)}dt\right)^{1/2}
\le C_{a,\theta}\|g'\|_\infty.}
\tag{20}
\]

Thus for a finite sum `g(t)=sum_j z_j exp(i xi_j t)` with `|xi_j|<=K`, the squared transport error is at most
`C_(a,theta) K^2 (sum_j |z_j|)^2`, hence at most
`C_(a,theta) K^2 N sum_j |z_j|^2` for `N` terms. All normalization factors belong in the coefficients. This estimate needs no frequency separation, but is **additive in coefficient/derivative size**, not relative to a possibly tiny difference energy or shorted energy. Equation (11) shows that its order in `s` cannot generally be improved to `o(1)` for fixed unit-amplitude oscillations. Multiplying both traces by `L^(-1/2)` gives cost `(C_theta(xi)+o(1))/L`.

The failure of relative control is not restricted to exactly matching frequencies. Put

\[
f_s(t)=e^{i\xi t},\qquad g_s(u)=e^{i(\xi+\varepsilon_s)u},
\qquad 0<|\varepsilon_s|=o(\sqrt s).
\tag{21}
\]

Using `b_s(t)>=c s cosh(t)` and `|u_rho(t)|<=|t|+C`,

\[
\mathcal B_{s,0}^\rho[f_s,g_s]
\le C\varepsilon_s^2/s\longrightarrow0,
\]
\[
\left|\sqrt{\mathcal B_s^\rho[f_s,g_s]}
 -\sqrt{\mathcal B_s^\rho[f_s,e^{i\xi\cdot}]}\right|
\le C|\varepsilon_s|/\sqrt s\longrightarrow0.
\tag{22}
\]

Both bounds use the finite integral of `(1+t^2)sech(t)` on the line. Therefore the transported energy in (22) still tends to `C_theta(xi)>0`. There is no fixed constant `C` for a bound `B_s^rho<=C B_(s,0)^rho` on all such bounded-frequency data, even with distinct frequencies. In particular no separation-independent relative perturbation estimate of the PF-361 type can cover this correspondence using difference energy alone.

## 4. Meaning for the flute and limits of the obstruction

The local geometry is the same ultraparallel-axis geometry as PF-216/PF-230. Their sufficiently small natural seam offsets satisfy a condition of the form (5), so trimming does not remove this **local transport cost**. A periodic Fourier trace on a hypercycle, expressed in its inherited cuff coordinate, is still an exponential; its own arclength period and coordinate both acquire the same `cosh(rho)` factor.

However, PF-354 proves there is no common nonzero Fourier frequency on distinct actual prime cuffs. Neither a fixed matching wave nor the quantitative near-match (21) has been established on those cuffs here. These controls disprove a universal separation-free comparison, not a comparison restricted to the exact prime periods with additional estimates. No claim is made that this local cost survives global transition minimization.

The missing bridge must keep the transport, bound it relative to a coercive **completed** reference form, or use an actual-lattice estimate that excludes the near-cancellation regime. Equation (20) provides one explicit additive error budget. It does not show that the error is small relative to the transition residuals: those can be exponentially small in the model. Positive-shift mass, tangential energy, the remaining pant charts, and seam terms can dominate (19), and are not included in it. The result neither proves nor disproves noncompactness of the completed actual low/high angle.

This mechanism depends only on hyperbolic geometry and occurs for nonprime controls. It supplies no prime-specific spectral invariant, scattering theorem, zero exclusion, or RH implication. It also does not contradict PF-348's local Dirichlet comparison, whose opposite boundary trace is zero rather than a matching oscillation.

## 5. Prior art and validation

The directional-energy principle is classical. B. Muetzel, *Inequalities for the capacity of non-contractible annuli on cylinders of constant and variable negative curvature*, Geometriae Dedicata 166 (2013), 129–145, DOI [10.1007/s10711-012-9788-z](https://doi.org/10.1007/s10711-012-9788-z), [author paper](https://arxiv.org/abs/1105.5060), uses Fermi-coordinate gradient projection and the reciprocal integral of the metric factor in Lemma 2.1 and Theorem 4.1. Its capacity boundary values are constant; (10) proves directly the varying-trace version used here. His *The Jacobian of a Riemann surface and the geometry of the cut locus of simple closed geodesics*, Ann. Acad. Sci. Fenn. Math. 42 (2017), 693–721, [primary paper](https://www.acadsci.fi/mathematica/Vol42/vol42pp0693-0721.pdf), Section 2.1, records the same energy decomposition and capacity comparison.

No novelty is claimed for Fermi coordinates, raywise capacity, or the offset graph already in PF-230. The addition is the explicit nonzero transport limit (11), its uniform persistence under small offset trimming, and the distinct-frequency failure (21)–(22) of the relative estimate needed to extend PF-361. The derivation uses no external asymptotic theorem and no inference from search absence.

Supplementary checks used Python with mpmath 1.3.0 at 55 decimal digits. For `theta in {0.2,0.45}`, `xi in {0.4,1.3,3}`, offsets `(rho_1/s,rho_2/s) in {(0,0),(0.04,0.09),(0.13,0.02)}`, and `s in {10^(-2),10^(-4),10^(-6)}`, direct quadrature of (16) approached (11); the largest relative discrepancy at `s=10^(-6)` was below `1.73*10^(-6)`. The limiting values for `(theta,xi)=(0.2,1.3)` and `(0.45,1.3)` were approximately `0.0022994583999401` and `0.02861170373831`. Thirty-six geometric controls checked (4), (12), (14)'s displacement ordering, (18), and nonempty trimmed rays where applicable. The distinct-frequency control `epsilon_s=s`, `theta=0.3`, `xi=1.1`, offsets `(0.04s,0.09s)` approached the predicted limit `0.0057036269235781` as well. These are finite-precision checks of the formulas, not PDE solves or evidence of prime-lattice realization. Scratch code and dependencies remain outside Git.

The proof is the evidence. No independent adversarial approval, Lean verification, or optimum transport bound is claimed. A formalization handoff is not warranted merely to certify this elementary coordinate/capacity calculation while its actual shorted-operator application remains open.
