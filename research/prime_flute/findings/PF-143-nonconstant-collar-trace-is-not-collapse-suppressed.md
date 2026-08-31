# PF-143 — nonconstant collar trace is not collapse-suppressed by angular welding

**Status:** `EXACT-DERIVED + LITERATURE-AUDITED + NEGATIVE/BOUNDARY`. PF-141 shows that a **constant** angular phase on a pinching standard collar can be welded at Güneysu--Thalmaier inverse-unit-ball weighted cost `O(L|tau|)`, and PF-142 then removes that constant phase entirely for the canonical marked reflection-equivariant prime/shift comparison. The same collapse gain does **not** extend to a genuinely nonconstant angular boundary trace. For any tail-near-isometric angular self-map of a standard half-collar, the weighted metric-deviation cost controls the centered `L^1` size of its outer boundary displacement by a constant independent of the pinching core length `L`. Thus the remaining reflection-odd trace-shape mode is an unsuppressed interface datum in the natural angular-welding class. This does not prove that the accepted wave-operator clue fails: the actual centered traces may still be summable, and a more general transverse/radial comparison can leave the angular-only class treated here.

## Claim

Let

\[
C_L^+=[0,w(L)]\times\mathbb S^1,
\qquad
w(L)=\operatorname{arsinh}\frac1{\sinh(L/2)},
\tag{1}
\]

be one half of the standard hyperbolic collar of a simple closed geodesic of length `L`, with

\[
g_L=dr^2+s_L(r)^2d\theta^2,
\qquad
s_L(r)=L\cosh r,
\qquad
\theta\in\mathbb R/\mathbb Z.
\tag{2}
\]

Consider an angular comparison preserving the collar foliation,

\[
F_u(r,\theta)=(r,\theta+u(r,\theta)),
\tag{3}
\]

where `u` is a periodic `C^1` lift. Assume that on a sufficiently far tail

\[
\boxed{
\|u_\theta\|_\infty
+\|s_Lu_r\|_\infty
\le\eta_0
}
\tag{4}
\]

for one fixed sufficiently small `eta_0`; this is exactly the regime relevant to inserting a correction into a comparison whose local bilipschitz constants tend to `1`.

Let

\[
\psi(\theta):=u(w(L),\theta),
\qquad
\psi^\circ
:=\psi-\int_{\mathbb S^1}\psi(\vartheta)d\vartheta
\tag{5}
\]

be the outer-boundary displacement and its centered part. If `h=F_u^*g_L`, define the local Güneysu--Thalmaier weight

\[
\mathcal W_L(F_u)
:=
\int_{C_L^+}
\mu_{g_L}(B_{g_L}(z,1))^{-1}
\delta_{g_L,h}(z)\,d\mu_{g_L}(z).
\tag{6}
\]

Then there are absolute constants `L_0>0` and `c>0`, depending at most on the fixed smallness threshold in (4), such that for every `0<L<L_0`,

\[
\boxed{
\mathcal W_L(F_u)
\ge
c\,\|\psi^\circ\|_{L^1(\mathbb S^1)}.
}
\tag{7}
\]

In particular, for the canonical reflection-odd trace remaining after PF-142,

\[
\psi(-\theta)=-\psi(\theta),
\tag{8}
\]

so `psi` already has mean zero and

\[
\boxed{
\mathcal W_L(F_u)
\ge c\|\psi\|_{L^1},
}
\tag{9}
\]

with **no factor tending to zero with `L`**.

This is sharply different from the constant mode. If `psi(\theta)=tau`, then `psi^circ=0`, (7) is vacuous, and PF-141 constructs a central shear with

\[
\boxed{
\mathcal W_L=O(L|\tau|).
}
\tag{10}
\]

Thus pinching separates the angular trace into two qualitatively different sectors:

\[
\boxed{
\text{constant phase: collapse-suppressed}
\qquad\text{vs.}\qquad
\text{nonconstant shape: no automatic collapse gain}.}
\tag{11}
\]

## 1. The exact differential exposes radial shear and tangential shape separately

Relative to the source and target orthonormal frames

\[
e_r=\partial_r,
\qquad
e_\theta=s_L(r)^{-1}\partial_\theta,
\tag{12}
\]

the differential of (3) is

\[
\boxed{
M(r,\theta)
=
\begin{pmatrix}
1&0\\
a&q
\end{pmatrix},
\qquad
a=s_Lu_r,
\qquad q=1+u_\theta.
}
\tag{13}
\]

Hence the tangent-metric comparison is

\[
M^TM
=
\begin{pmatrix}
1+a^2&aq\\
aq&q^2
\end{pmatrix}.
\tag{14}
\]

Let

\[
m(z):=
\max_{\lambda\in\operatorname{spec}(M^TM)}|\log\lambda|.
\tag{15}
\]

The Güneysu--Thalmaier zeroth-order deviation is a monotone function of this logarithmic metric distortion; in dimension two PF-128/PF-141 use

\[
\delta_{g,h}=2\sinh\frac{m}{2}
\tag{16}
\]

(up to the equivalent cotangent convention, which has the same absolute logarithms). Under (4), `q` stays in a fixed compact subset of `(0,infinity)` and `m` is uniformly small. The determinant and off-diagonal entry of (14) then give

\[
|u_\theta|
=|q-1|
\le C m,
\qquad
|s_Lu_r|
=|a|
\le C m.
\tag{17}
\]

Indeed `det(M^TM)=q^2`, so `|log q|<=m`, while `|aq|` is bounded by `||M^TM-I||`, which is `O(m)` on a bounded logarithmic-distortion range. Therefore

\[
\boxed{
\delta_{g_L,h}
\ge
c_1\bigl(|s_Lu_r|+|u_\theta|\bigr).
}
\tag{18}
\]

This is the nonlinear counterpart of the elementary separation between a radial angular shear and a tangential boundary reparametrization.

## 2. The inverse-unit-ball weight cancels the collar area but not the trace shape

PF-128 established the lower unit-ball bound needed for upper scattering estimates. For the present lower bound we need the complementary elementary estimate

\[
\boxed{
\mu_{g_L}(B_{g_L}((r,\theta),1))
\le C s_L(r)
\qquad (0\le r\le w(L)).
}
\tag{19}
\]

uniformly for small `L`.

If `r<=w(L)-1`, the unit ball stays inside the embedded standard collar. Since every point in it has radial coordinate between `r-1` and `r+1`, its area is at most the area of that full radial slab,

\[
\int_{r-1}^{r+1}\int_{\mathbb S^1}
L\cosh t\,d\theta dt
=2\sinh(1)\,s_L(r).
\tag{20}
\]

On the remaining outer unit slab, the circumference scale has a uniform positive lower bound:

\[
\begin{aligned}
s_L(w(L)-1)
&=L\cosh(w(L)-1)\\
&\longrightarrow2e^{-1}>0,
\end{aligned}
\tag{21}
\]

while any radius-one ball has area at most the radius-one ball in `H^2`. Enlarging the constant therefore proves (19) everywhere.

Since

\[
d\mu_{g_L}=s_L(r)drd\theta,
\tag{22}
\]

equation (19) yields the uniform lower density

\[
\frac{d\mu_{g_L}}
     {\mu_{g_L}(B_{g_L}(z,1))}
\ge c_2\,drd\theta.
\tag{23}
\]

Combining (18) and (23),

\[
\boxed{
\mathcal W_L(F_u)
\ge
c_3\int_0^{w(L)}\int_{\mathbb S^1}
\bigl(s_L|u_r|+|u_\theta|\bigr)d\theta dr.
}
\tag{24}
\]

The collapse has therefore removed the shrinking area factor from the weighted integral. The radial term still carries `s_L`, which is why a constant phase can be moved near the core cheaply; the tangential shape term does not.

## 3. A one-unit outer slab already forces the centered trace cost

Let

\[
\bar u(r):=\int_{\mathbb S^1}u(r,\theta)d\theta,
\qquad
v(r,\theta):=u(r,\theta)-\bar u(r),
\tag{25}
\]

and put

\[
A(r):=\|v(r,\cdot)\|_{L^1(\mathbb S^1)}.
\tag{26}
\]

The `L^1` Poincare inequality on the unit circle gives

\[
A(r)
\le C_P\int_{\mathbb S^1}|u_\theta(r,\theta)|d\theta.
\tag{27}
\]

Moreover `A` is absolutely continuous and

\[
|A'(r)|
\le\int|v_r|d\theta
\le2\int|u_r|d\theta,
\tag{28}
\]

because `|\bar u'(r)|<=\int|u_r|`.

Restrict (24) to the outer unit slab

\[
I_L=[w(L)-1,w(L)].
\tag{29}
\]

By (21), `s_L>=c_4>0` on `I_L`. Equations (27)--(28) therefore imply

\[
\mathcal W_L(F_u)
\ge c_5\int_{I_L}
\bigl(|A'(r)|+A(r)\bigr)dr.
\tag{30}
\]

For every nonnegative absolutely continuous function on an interval of length one,

\[
A(w)
\le
\int_{w-1}^{w}A(r)dr
+
\int_{w-1}^{w}|A'(r)|dr.
\tag{31}
\]

But by definition

\[
A(w(L))
=\|\psi^\circ\|_{L^1}.
\tag{32}
\]

Equations (30)--(32) prove (7).

The proof is intentionally local to the **thick-scale boundary of the canonical standard collar**. It does not matter how cleverly the map is arranged deeper in the pinching region: a nonconstant trace presented at `r=w(L)`, where `s_L->2`, already forces an order-one-in-`L` weighted cost unless its centered amplitude itself tends to zero.

## 4. The conformal-cylinder DtN calculation gives the same mode dichotomy

PF-065/PF-066 already contain the classical spectral analogue. The half-collar is conformal to a flat cylinder of length

\[
T_L
=\frac1L\arctan\frac1{\sinh(L/2)}
=\frac\pi{2L}-\frac12+O(L^2).
\tag{33}
\]

For boundary data on one end and zero data on the other, the flat-cylinder Dirichlet-to-Neumann eigenvalues are

\[
\lambda_0(T_L)=\frac1{T_L}
\sim\frac{2L}{\pi}
\tag{34}
\]

on the constant mode, while for `k!=0`,

\[
\boxed{
\lambda_k(T_L)
=2\pi|k|\coth(2\pi|k|T_L)
\longrightarrow2\pi|k|.
}
\tag{35}
\]

Thus the harmonic/Dirichlet-energy minimizer has exactly the same qualitative split: the constant mode becomes cheap under pinching, whereas every fixed nonzero Fourier mode retains the `|D|` boundary energy scale. PF-065 used this phenomenon to prove universality of the raw scaled Steklov spectrum; PF-066 used the full two-boundary DtN matrix for exact collar stripping. PF-143 uses the same classical mode separation only as a **spectral sanity check** for the independent Güneysu--Thalmaier weighted metric-deviation estimate (7).

## 5. Consequence for the accepted wave-operator clue

PF-142 reduced the short-collar assembly ledger to

\[
\text{nonconstant reflection-odd angular trace}
+\text{transverse/radial shape mismatch}.
\tag{36}
\]

PF-143 shows that the first term cannot be dismissed by copying PF-141's pinching argument. In an angular-only interpolation preserving the standard collar foliation,

\[
\boxed{
\text{collapse supplies no small factor for the centered trace amplitude}.}
\tag{37}
\]

Therefore a positive resolution of `CLUE-shift-clone-wave-operator-equivalence` now needs at least one genuinely new input:

1. prove that the **actual** centered body-to-collar trace defects over the complete PF-138 family are summable in a norm strong enough to dominate their `L^1` amplitudes;
2. construct a transverse/radial boundary-straightening mechanism outside the angular-only class and prove that it lowers the Güneysu--Thalmaier weight without merely moving the same trace cost elsewhere; or
3. bypass this sufficient scattering criterion with an operator argument that proves complete wave operators by different means.

A mere estimate `psi_eta->0` is not enough for the first route: infinitely many short cores occur, so the global integral needs a summability mechanism. Conversely, (7) does **not** imply divergence for the actual prime/shift comparison because no lower bound on the sequence `||psi_eta||_1` has been established.

## 6. Stress tests and scope boundaries

The result survives the following adversarial checks only in its stated form.

1. **Constant phase.** For `psi=tau`, the centered trace vanishes, so (7) gives no obstruction. PF-141's `O(L|tau|)` construction remains valid. There is no contradiction.
2. **Canonical reflection.** PF-142 makes the surviving angular discrepancy reflection-odd, hence centered. It removes the only mode on which pinching automatically helps, rather than removing the mode controlled by (7).
3. **Trace amplitudes tending to zero.** The lower bound tends to zero with `||psi^circ||_1`. PF-143 does not assert a positive cost per collar, only absence of an additional factor such as `L`.
4. **General transverse maps.** Equation (7) is proved for angular maps preserving the standard radial foliation. A comparison that moves the collar boundary transversely or changes radial shape lies outside the theorem. That escape is exactly why the accepted wave clue remains open.
5. **Large distortion.** The simple comparison (18) is stated in the tail-near-isometric regime (4), which is the regime relevant to the established prime/shift constructions. PF-143 does not claim an optimal lower bound for arbitrary wild collar homeomorphisms.
6. **Wave operators themselves.** Güneysu--Thalmaier give a sufficient integral criterion. Failure to make one particular local assembly summable would not prove nonexistence of wave operators.
7. **Arithmetic interpretation.** The estimate is a hyperbolic collar/interface theorem. It contains no prime-specific selector and no RH implication; it only sharpens what a prime/shift comparison would have to control.

## 7. Prior-art / novelty audit

No novelty is claimed for the standard-collar metric, circle Poincare inequality, Fourier decomposition on a cylinder, the Douglas/Dirichlet trace principle, or the fact that the cylinder DtN operator tends to `|D|` on nonzero modes while its constant mode is controlled by inverse cylinder length. PF-065/PF-066 already audited and used those classical facts in the prime-flute setting.

The external scattering input remains S16: B. Güneysu and A. Thalmaier, *Scattering theory without injectivity radius assumptions, and spectral stability for the Ricci flow*, Ann. Inst. Fourier 70 (2020), DOI `10.5802/aif.3316`. Their theorem supplies the inverse-unit-ball weighted sufficient criterion; it does not contain the collar trace estimate (7).

A directed literature check against hyperbolic-collar Steklov/DtN estimates, annular harmonic extension, Fenchel--Nielsen twist interpolation, and the Güneysu--Thalmaier scattering criterion found the expected classical cylinder/DtN and twist machinery, but no result that turns the **nonconstant marked boundary trace of a pinching standard collar** into this project-specific weighted assembly conclusion. Historical novelty is therefore not claimed for the local inequalities themselves. The durable Mathia content is the exact composition

\[
\boxed{
\text{PF-142 removes the constant mode}
+\text{standard-collar GT weight}
\Longrightarrow
\text{the surviving angular mode has no collapse suppression}.}
\tag{38}
\]

## Research consequence

PF-141 and PF-142 eliminated constant angular phase as an intrinsic global gate. PF-143 prevents an overextension of that success: **pinching is favorable only to the constant rotation sector**. The remaining nonconstant reflection-odd collar trace must be controlled by its own summability, by a genuinely transverse geometric construction, or by a different operator argument.

Accordingly the accepted wave-operator clue remains open, but its last interface question is now sharper. The next productive calculation is not another generic short-collar estimate; it is an estimate of the **actual centered boundary trace produced by the PF-139/PF-140 body comparison on each PF-138 short-core collar**, compared with the PF-128 optimized collar trace. If those centered amplitudes are summable, PF-143 supplies no obstruction. If they carry a nonsummable reciprocal-prime floor, angular-only welding cannot resolve the clue.

## Falsification core

A later adversary can check PF-143 through the following finite chain:

1. compute the differential matrix (13) and the metric matrix (14);
2. under (4), derive the two-sided local comparison between Güneysu--Thalmaier deviation and `|s_Lu_r|+|u_theta|`, in particular the lower bound (18);
3. verify the ambient unit-ball upper bound (19), using the embedded radial slab for `r<=w-1` and the universal hyperbolic-ball area bound on the outer unit slab;
4. compute `s_L(w(L)-1)->2/e` and derive (24);
5. center `u`, apply the circle `L^1` Poincare inequality and (28), then use the length-one trace inequality (31) to obtain (7);
6. compare with PF-141's exact constant-mode shear and verify that no contradiction arises because centering annihilates that mode;
7. verify independently from PF-066's cylinder matrix that (34)--(35) show the same constant/nonconstant split;
8. confirm that no step gives a lower bound for general transverse/radial maps or for the actual sequence of prime/shift trace amplitudes.

Failure of steps 2--5 invalidates the weighted lower bound. Even if all eight steps hold, PF-143 does not resolve the wave-operator clue until the actual interface traces are shown summable or an intrinsic nonsummability/transverse obstruction is proved.