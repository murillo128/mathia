# PF-363 — trace-preserving corridor charts give a coupled pant energy lower bound

**Status:** EXACT-DERIVED + CLASSICAL-STRIP-GEOMETRY + ACTUAL-COUPLED-LOWER-CERTIFICATE + GLOBAL-ANGLE-OPEN.

The normal-ray obstruction in PF-362 does not prevent a lower bound for the **full** pant energy by the straight-coordinate corridor difference. There is another foliation: use the classical equal-arclength correspondence between the untrimmed axes, then interpolate the two small hypercycle coordinate corrections across the strip. This gives a chart that fixes the inherited cuff parameter on both artificial boundaries. Its extra shear is `O(s)` in the full energy metric when the offsets are `O(s)`.

On a growing embedded window, the actual shifted pant energy consequently controls

\[
\frac1s\int_{-T}^{T}|f(t)-g(t)|^2\operatorname{sech}t\,dt
\]

for **both arbitrary boundary traces together**, without a frequency-separation assumption. With PF-361's narrow-band concentration, this supplies the coupled lower certificate against global symmetric transition relaxation that PF-348's zero-opposite-boundary estimate did not provide. It does not supply the matching upper estimate at the shorted residual scale or determine the globally completed angle.

## 1. A chart fixing both inherited trace coordinates

Take two ultraparallel axes at distance `s>0`, with inherited axis arclengths centered at their common perpendicular and equally oriented. Fix `0<=eta_0<1` and inward offsets

\[
\rho_1,\rho_2\ge0,\qquad
\eta:=\frac{\rho_1+\rho_2}{s}\le\eta_0.
\tag{1}
\]

These coordinates are the footpoint coordinates on the original cuffs; hypercycle arclength is `cosh(rho_j)` times the corresponding coordinate. Use PF-231's logarithmic rectangle, with

\[
\tau=\log\tan(\theta/2),\qquad
g=\cosh^2\tau\,dx^2+d\tau^2.
\tag{2}
\]

Its trimmed boundaries are `x=F_1(tau)` and `x=s-F_2(tau)`, where

\[
F_j(\tau)=\operatorname{arsinh}(\sinh\rho_j\operatorname{sech}\tau),
\quad a(\tau)=s-F_1(\tau)-F_2(\tau).
\tag{3}
\]

PF-235 gives the inherited coordinate at such a boundary as
`T_rho(tau)=arsinh(sinh(tau)/cosh(rho))`. Its inverse is

\[
U_j(t)=\operatorname{arsinh}(\cosh\rho_j\sinh t).
\]

For `0<=X<=1`, define

\[
U(X,t)=(1-X)U_1(t)+XU_2(t),
\]
\[
\Phi(X,t)=\bigl(F_1(U)+a(U)X,\ U\bigr).
\tag{4}
\]

At `X=0` and `X=1`, the inherited coordinate is **exactly** `t`. Thus the boundary values of a pullback `v=u o Phi` are `f(t),g(t)` with their original Fourier meanings; no boundary reparameterization is left in the difference.

Put

\[
r=\max(\rho_1,\rho_2),\quad d=\log\cosh r,\quad
\beta=\sinh r,\quad k=d/s,\quad C_r=\cosh^2r.
\tag{5}
\]

Direct differentiation, or inversion of PF-235's formula, gives globally

\[
|U-t|\le d,\qquad 1\le U_t\le\cosh r,
\qquad |U_X|=|U_2-U_1|\le d.
\tag{6}
\]

For the last bound, `U_j(t)-t` has the sign of `t` and lies between zero and `d` in absolute value; the two corrections therefore differ by at most `d`, not `2d`. Since `a>0` and `U_t>0`, the map is a diffeomorphism onto its image: it is the composition of `(X,t)->(X,U)` with `(X,tau)->(F_1(tau)+a(tau)X,tau)`. Its Jacobian determinant is `a(U)U_t>0`.

## 2. Full energy comparison, uniform in window length

On `D_T=(0,1) x (-T,T)` define

\[
\mathfrak q_{s,T}^{0}[v]
=\int_{D_T}\left\{
\frac{\operatorname{sech}t}{s}|v_X|^2
+s\cosh t\bigl(|v_t|^2+|v|^2\bigr)\right\}dXdt.
\tag{7}
\]

Let `q_hyp[u]=integral_(Phi(D_T)) (|du|_g^2+|u|^2) dvol_g`. If `beta<1` and `k<1`, then

\[
\boxed{c_s\mathfrak q_{s,T}^{0}[v]
\le\mathfrak q_{\rm hyp}[u]
\le C_s\mathfrak q_{s,T}^{0}[v],}
\tag{8}
\]

where one may take

\[
c_s=\frac{(1-\beta)(1-\eta)(1-k)}{C_r},\qquad
C_s=\frac{(1+\beta+\beta^2)(1+k+k^2)C_r}{1-\eta}.
\tag{9}
\]

These constants are independent of `T`, the traces, their frequency content, and their coefficients. Under (1), `beta=O(s)`, `d=O(s^2)` and `k=O(s)`. Thus `c_s` stays bounded away from zero and `C_s` from infinity as `s->0`. If the offsets vanish, the chart and (7) are exact and both constants equal one. For a fixed positive offset fraction, (8) is a uniform comparison, not a claim that both constants tend to one.

### Derivation

First straighten only the two logarithmic graphs using `x=F_1(tau)+a(tau)X`. PF-232's pointwise completed-square estimates compare the exact shifted energy to the untrimmed rectangle energy by the factors

\[
(1-\beta)(1-\eta),\qquad
\frac{1+\beta+\beta^2}{1-\eta}.
\tag{10}
\]

The estimates hold on arbitrary subdomains: the proof bounds the graph shear by `beta` and uses `(1-eta)s<=a<=s` before integration. There is no dependence on whether the end cuts are angular level sets.

In `(X,tau)` the untrimmed rectangle energy is (7) with `t` replaced by `tau`. Under `tau=U(X,t)`, its derivative terms become

\[
\frac{\operatorname{sech}U}{s}U_t
\left|v_X-\frac{U_X}{U_t}v_t\right|^2
+\frac{s\cosh U}{U_t}|v_t|^2.
\tag{11}
\]

Its mass density is `s cosh(U) U_t |v|^2`. Set

\[
A=\left(\frac{\operatorname{sech}U}{s}U_t\right)^{1/2}v_X,
\quad B=\left(\frac{s\cosh U}{U_t}\right)^{1/2}v_t,
\quad z=\frac{U_X}{s\cosh U}.
\]

Equation (11) is `|A-zB|^2+|B|^2`, with `|z|<=k`. The elementary bounds

\[
(1-k)(|A|^2+|B|^2)
\le |A-zB|^2+|B|^2
\le(1+k+k^2)(|A|^2+|B|^2)
\tag{12}
\]

also hold for complex derivatives. The three diagonal coefficients, including the mass coefficient, differ from (7) by factors in `[C_r^(-1),C_r]`, using (6) and
`exp(-d)<=cosh(U)/cosh(t)<=exp(d)`. Combining (10)–(12) proves (8)–(9). Smooth functions are sufficient for the derivation; density extends it to the corresponding finite-energy Sobolev spaces. On each finite window the chart is smooth up to the boundary with nonzero Jacobian.

This identifies the load-bearing normalization: the boundary correction is `O(rho^2)`, and interpolating across a width `s` costs at most `O(rho^2/s)` in the energy metric. Merely observing small boundary displacement would not have supplied this estimate.

## 3. The chart fits inside the actual embedded pant corridor

Fix the sufficiently small `theta>0` used by PF-216 and let

\[
T_s=\operatorname{arsinh}(\theta/\sinh s),\qquad T=T_s-1>0.
\tag{13}
\]

For small `s`, (6) implies `|U|<=T_s` throughout `D_T`. Every point of (4) is between the trimmed boundaries and has `0<=x<=s`. In the hyperboloid coordinates associated with the first axis, its Fermi footpoint coordinate `t_F` obeys

\[
\sinh t_F=\frac{\sinh U}
 {\sqrt{1+\sinh^2x\cosh^2U}},\qquad |t_F|\le|U|.
\tag{14}
\]

For example the hyperboloid point is
`(cosh(x) cosh(U), sinh(U), sinh(x) cosh(U))`; division of the middle coordinate by the Fermi factor `cosh(r_F)` proves (14). Hence the chart lies inside PF-216's embedded normal-ray corridor `|t_F|<=T_s`. Being between the same hypercycles also places it outside the removed seam strips. The fixed loss of one in (13) leaves the window growth unchanged. No complete infinite-axis strip is asserted to embed in the pant.

Let `E_pant[f,g]` be the minimized positive-shift energy with arbitrary prescribed data on its two finite boundaries. Restrict every admissible pant extension to this subdomain, apply the lower bound in (8), and use
`integral_0^1 |v_X|^2 dX >= |g(t)-f(t)|^2`. Then

\[
\boxed{E_{\rm pant}[f,g]\ge
\frac{c_s}{s}\int_{-T}^{T}|f(t)-g(t)|^2
\operatorname{sech}t\,dt.}
\tag{15}
\]

The end cuts carry no imposed Dirichlet condition in this restriction argument. Equivalently, minimizing (8) with fixed side data and free end data compares the two local energy DtN forms. Its upper bound applies to that **local quadrilateral**; a competitor on it has not been extended to the rest of the pant.

Equation (15) is valid on the actual prime periods, on distinct arbitrarily close frequencies, and on nonprime controls. It is a lower estimate for full energy, not an upper estimate for PF-362's normal-direction energy. A matching oscillation has zero right side in (15), while (7) retains tangential and mass costs. PF-362's nonzero limiting normal-ray cost is therefore fully compatible with (8) and (15).

## 4. A coupled lower certificate survives arbitrary symmetric transitions

Use a sufficiently far grounded tail of the actual seam-cut flute and the common centered zero-twist cuff coordinates. Restrict to traces equal on the two faces of each seam; the following concerns symmetric relaxation. Let `M_sym[f]` be the raw complete positive seam-plus-pant form on finitely supported such fields. Each pant is disjoint from the others, its strip contribution is nonnegative, and the constants in (15) are uniform on this tail. Summing gives

\[
M_{\rm sym}[f]\ge c\sum_{i\ge0}s_i^{-1}
\int_{-T_i}^{T_i}|f_{i+1}(t)-f_i(t)|^2\operatorname{sech}t\,dt,
\quad f_0=0.
\tag{16}
\]

There is no double counting of a pant. The inherited periods and Fourier modes are unchanged by (4); a hypercycle's coordinate and own arclength acquire the same `cosh(rho_i)` factor.

Take a fixed transition band `(kappa,kappa+eta_T)` with `kappa>0`. Include all its sine and cosine lattice modes, plus a retained constant `u_i` on each cuff. Here `eta_T` is a band width, distinct from the geometric fraction `eta` in (1). Choose `eta_T` sufficiently small for PF-361's term-count/window estimate. The fixed loss in (13) only changes that estimate's prefactor. Therefore, on a farther tail, every edge window in (16) controls at least a fixed positive fraction of its full `L^2(sech(t)dt)` norm, uniformly in **all** coefficients on both unequal lattices. Write that norm squared as `H`.

Let `mathcal T_alg` consist of all finitely supported symmetric transition fields and define

\[
A_{\rm actual}[u]=\inf_{z\in\mathcal T_{\rm alg}}
 M_{\rm sym}[(u_i)_i+z].
\]

For the positive transition frequencies `Xi_i` put

\[
Q_i=\prod_{\xi\in\Xi_i}\tanh^4(\pi\xi/2)>0,
\qquad Q_0=1.
\tag{17}
\]

The scalar cosine Cauchy residual formula in PF-359, in the unnormalized constant convention `H[1]=pi`, gives

\[
\boxed{A_{\rm actual}[u]\ge
c\pi\sum_{i\ge0}s_i^{-1}Q_iQ_{i+1}
|u_{i+1}-u_i|^2.}
\tag{18}
\]

Indeed (16) and concentration hold for every trial; independently relaxing the transition coefficients on each edge gives a lower bound. The cosine-node substitution is `x=cosh(pi xi)`, whose residual factor at the constant node `x=1` is `tanh^4(pi xi/2)`. Duplicate neighboring nodes are counted once by the exact distance formula, so counting them twice only decreases the lower bound. Sines are odd and orthogonal to the constant and cosines in `H`, and cannot decrease this relaxed scalar residual.

For nonconsecutive support `I`, (18) reads

\[
A_{\rm actual}[u]\ge c\pi\sum_{i\in I}Q_i
\left(s_{i-1}^{-1}Q_{i-1}+s_i^{-1}Q_{i+1}\right)|u_i|^2.
\tag{19}
\]

The same certificate holds when the transition infimum is taken in the closure of `mathcal T_alg` in the actual energy completion: by definition, its distance from a fixed finitely supported retained field equals the algebraic infimum. This does not identify the actual completion with the corridor completion or with every boundary condition at infinity. It establishes a denominator bound against every remote **symmetric** transition, not a monotonicity assertion about normalized correlations.

## 5. What changed and what remains outside the result

PF-231/PF-232 compared complete energies in a common logarithmic boundary parameter; PF-235 identified each individual physical boundary correction. The additional step (4)–(12) joins those corrections into one chart while paying their transverse interpolation cost. Equations (15)–(19) then give a coupled actual-pant lower certificate, including the embedded finite window and the original cuff Fourier parameters. The opposite boundary is free to carry an arbitrary transition trace. This is the material difference from PF-348's Dirichlet self-block estimate.

The comparison object in (8) contains positive tangential and mass terms. Dropping them is valid only for the lower bounds. No two-sided comparison to the difference-only network follows, and no upper bound on `E_pant` follows by extending a local minimizer without paying the exterior and end-cut costs. In particular (19) alone does not show that a retained constant can be approximated by transition-plus-high fields at a smaller actual energy. Such an upper trial must control its coefficients, nonsingular pant energy, actual seam energy and all coupled freedoms at the residual scale. The arbitrary on-site Cauchy weights of PF-359 are not a substitute for those terms.

The assertion here also does not eliminate antisymmetric face variables. PF-350 is a separate comparison if that enlargement is used. There is no conclusion here about the completed low/high angle, compactness, Schatten classes, scattering, zeta zeros or RH. The construction is universal hyperbolic geometry; primality enters the narrow-band consequence through the previously established window/period growth, not through a new arithmetic discriminator.

## 6. Prior art and validation

The untrimmed equal-arclength foliation is classical: A. Papadopoulos and G. Théret, *Shortening all the simple closed geodesics on surfaces with boundary*, Proc. Amer. Math. Soc. 138 (2010), 1775–1784, DOI [10.1090/S0002-9939-09-10195-8](https://doi.org/10.1090/S0002-9939-09-10195-8), [author manuscript](https://arxiv.org/abs/0905.4661), Section 2, pp. 5–6 of the manuscript, explicitly describes the equidistant-arc foliation and induced isometry between an ultraparallel strip's boundary geodesics. No new foliation or general uniformization principle is claimed.

B. Muetzel's [directional-capacity paper](https://arxiv.org/abs/1105.5060), Lemma 2.1 and Theorem 4.1 (S35), provides the classical directional-energy comparison background. L. Friedlander and M. Solomyak, *On the Spectrum of the Dirichlet Laplacian in a Narrow Strip*, Israel J. Math. 170 (2009), 337–354, [author manuscript](https://arxiv.org/abs/0705.4058), Section 3, equations (3.8)–(3.11), is related prior art for pricing mixed derivatives against a coercive diagonal form. Its spectral theorem is not imported. The concentration theorem and scalar residual identity used only in Section 4 are already audited in PF-361/S34 and PF-359/S31, respectively.

The project-specific result is the trace-preserving hypercycle interpolation with explicit uniform energy constants, followed by its actual embedded-pant and symmetric-transition lower certificate. It is derived from classical geometry and energy inequalities. Search absence is not used as evidence of novelty.

Supplementary standard-library Python checks used seed `363`: 3,200 random chart points over `s in {10^-1,10^-2,10^-4,10^-6}` and offset ratios `(rho_1/s,rho_2/s) in {(0,0),(0.04,0.09),(0.19,0),(0.1,0.1)}`, with 200 points per case in `0<X<1`, `|t|<arsinh(0.3/sinh(s))-1`. Direct pullback of `diag(cosh^2(U),1)` checked both normalized gradient eigenvalues and the mass density against (9), the exact boundary-coordinate inverses, and (14)'s window containment. All passed at tolerance `10^-12`; the largest roundoff excursion beyond a bound was below `10^-15`. These are finite floating-point checks of coordinate algebra, not pant PDE solves or independent validation of the infinite completion. Scratch code remains outside Git.

The proof is the evidence. No Lean or independent adversarial verification is claimed. A formalization handoff is not proposed merely for the finite completed-square algebra: the load-bearing result also needs the hyperbolic chart, Sobolev pullback, embedded-pant geometry and concentration bridge, while the full angle application remains open.
