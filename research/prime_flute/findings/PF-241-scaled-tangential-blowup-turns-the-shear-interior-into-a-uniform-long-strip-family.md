# PF-241 — scaled tangential blowup turns the shear interior into a uniform long-strip family

**Status:** `EXACT-DERIVED + UNIFORM-ELLIPTIC-REDUCTION + POSITIVE/ROUTE-NARROWING`.

PF-240 identifies the remaining hypercycle-shear gate: for the high-high actual-seam-normalized correction it is enough to prove more than one total `K_a` boundary derivative with an `O(beta)` constant, uniformly as the corridor scale `s->0`. A legitimate concern is that ordinary fixed-domain elliptic smoothing may become useless because the PF-232 straightened corridor is thin in its natural tangential energy scale.

The apparent thinness can be removed exactly at the level relevant to PF-240. After PF-233's boundary-mass conjugation and the unitary tangential dilation

\[
Y=\theta/s,
\qquad
L_s=\pi/s,
\]

the sheared and diagonal corridor forms live on the **unit-width long strip**

\[
\Omega_s=(0,1)_X\times(0,L_s)_Y.
\]

Their principal coefficient matrices are uniformly strongly elliptic, independently of `s`; the shear coefficient and every fixed scaled derivative of it are `O(beta)`; and the singular Pöschl--Teller endpoint term becomes a uniformly scaled Hardy potential comparable to the inverse square of the distance to the two long-strip ends. At the same time PF-233's operator `K_a` is carried unitarily to the natural first-order tangential operator of this scaled form. Therefore **PF-240's Sobolev target contains no hidden power of `s` after this blowup**.

This does not prove the PF-240 high-high estimate. It removes one specific failure mode: loss of ellipticity caused by the shrinking corridor width. The remaining uniformity problem is instead a long-strip boundary-regularity problem with growing tangential length, Hardy endpoints, and the actual complete-lift seam normalization still present.

## Claim

Use the exact PF-232 notation

\[
f_i(\theta)=\operatorname{arsinh}(w_i\sin\theta),
\qquad
w_i=\sinh\rho_i,
\]

\[
a(\theta)=s-f_1(\theta)-f_2(\theta),
\qquad
b(X,\theta)=f_1'(\theta)+a'(\theta)X
=(1-X)f_1'(\theta)-Xf_2'(\theta).
\tag{1}
\]

Assume on the canonical tail

\[
(1-\eta_*)s\le a(\theta)\le s,
\qquad
0\le\eta_*<1,
\qquad
\beta:=\max(w_1,w_2)<1.
\tag{2}
\]

Let

\[
y=a^{-1/2}v
\tag{3}
\]

be PF-233's exact mass conjugation. Then PF-232's two forms become

\[
\mathfrak q_{\rm diag}[v]
=
\int_0^1\!\int_0^\pi
\left[
|y_X|^2
+\left|a\left(y_\theta+\frac{a'}{2a}y\right)\right|^2
+a^2\csc^2\theta\,|y|^2
\right]d\theta\,dX,
\tag{4}
\]

and

\[
\mathfrak q_{\rm hyp}[v]
=
\int_0^1\!\int_0^\pi
\left[
|y_X|^2
+\left|a\left(y_\theta+\frac{a'}{2a}y\right)-b\,y_X\right|^2
+a^2\csc^2\theta\,|y|^2
\right]d\theta\,dX.
\tag{5}
\]

Now set

\[
L_s:=\frac\pi s,
\qquad
(U_sy)(Y):=s^{1/2}y(sY),
\qquad 0<Y<L_s.
\tag{6}
\]

`U_s` is unitary from `L^2((0,pi),dtheta)` to `L^2((0,L_s),dY)`. Define

\[
A_s(Y):=\frac{a(sY)}s,
\qquad
\mathsf b_s(X,Y):=b(X,sY),
\qquad
C_s(Y):=\frac{A_s'(Y)}{2A_s(Y)},
\tag{7}
\]

and

\[
V_s(Y):=s^2A_s(Y)^2\csc^2(sY).
\tag{8}
\]

For `\psi=U_sy`, equations (4)--(5) are **exactly**

\[
\boxed{
\widetilde{\mathfrak q}_{\rm diag,s}[\psi]
=
\int_{\Omega_s}
\left[
|\psi_X|^2
+|A_s(\psi_Y+C_s\psi)|^2
+V_s|\psi|^2
\right]dY\,dX
}
\tag{9}
\]

and

\[
\boxed{
\widetilde{\mathfrak q}_{\rm hyp,s}[\psi]
=
\int_{\Omega_s}
\left[
|\psi_X|^2
+|A_s(\psi_Y+C_s\psi)-\mathsf b_s\psi_X|^2
+V_s|\psi|^2
\right]dY\,dX.
}
\tag{10}
\]

No overall factor of `s` remains.

The family satisfies the following canonical-tail bounds.

1. **Uniform width coefficient.** From (2),
   \[
   1-\eta_*\le A_s\le1.
   \tag{11}
   \]

2. **Uniform smooth small shear.** For every fixed integer `k>=0` there is a constant `C_k`, independent of the corridor index, such that
   \[
   \|\partial_Y^k\mathsf b_s\|_\infty
   +\|\partial_X\partial_Y^k\mathsf b_s\|_\infty
   \le C_k\beta,
   \tag{12}
   \]
   while higher `X` derivatives vanish. More sharply, the left side is `O(beta s^k)` for `k>=1`.

3. **Uniform scaled width derivatives.** For `k>=1`,
   \[
   \|\partial_Y^kA_s\|_\infty
   \le C_k\beta s^{k-1},
   \tag{13}
   \]
   and hence every fixed derivative of `C_s=A_s'/(2A_s)` is uniformly `O(beta)` on the canonical tail.

4. **Uniform principal ellipticity.** Ignoring the lower-order `C_s` and `V_s` terms, the principal derivative matrix of (10) in the variables `(\psi_X,\psi_Y)` is
   \[
   G_s=
   \begin{pmatrix}
   1+\mathsf b_s^2&-A_s\mathsf b_s\\
   -A_s\mathsf b_s&A_s^2
   \end{pmatrix},
   \qquad
   \det G_s=A_s^2.
   \tag{14}
   \]
   Therefore
   \[
   \lambda_{\min}(G_s)
   \ge
   \frac{(1-\eta_*)^2}{2+\beta^2},
   \qquad
   \lambda_{\max}(G_s)\le2+\beta^2,
   \tag{15}
   \]
   so the principal family is uniformly strongly elliptic as `s->0`.

5. **Uniform Hardy endpoint profile.** If
   \[
   d_s(Y):=\min\{Y,L_s-Y\},
   \tag{16}
   \]
   then
   \[
   \boxed{
   (1-\eta_*)^2d_s(Y)^{-2}
   \le V_s(Y)
   \le \frac{\pi^2}{4}d_s(Y)^{-2}.
   }
   \tag{17}
   \]

Finally let `T_a` and `K_a=T_a^{1/2}` be the PF-233 diagonal tangential operators. The unitary `U_s` gives

\[
\widetilde T_s:=U_sT_aU_s^{-1},
\qquad
\widetilde K_s:=U_sK_aU_s^{-1}=\widetilde T_s^{1/2},
\tag{18}
\]

where `\widetilde T_s` is the operator associated with the one-dimensional part of (9),

\[
\widetilde\tau_s[\psi]
=
\int_0^{L_s}
\left(|A_s(\psi_Y+C_s\psi)|^2+V_s|\psi|^2\right)dY.
\tag{19}
\]

Thus for every `r>=0`, every scaled projector `P_Z=1_(Z,infinity)(K_a)`, and every boundary operator `H`,

\[
\|K_a^{r_2}P_ZHP_ZK_a^{r_1}\|
=
\|\widetilde K_s^{r_2}\widetilde P_Z(U_sHU_s^{-1})\widetilde P_Z\widetilde K_s^{r_1}\|.
\tag{20}
\]

PF-240's target is therefore exactly a uniform long-strip Sobolev estimate in the scaled variables; no extra `s^{-r_1-r_2}` factor is generated by the blowup.

## 1. Exact mass conjugation exposes the right derivative scale

Starting from PF-232,

\[
\mathfrak q_{\rm hyp}[v]
=
\int
\left[
a^{-1}|v_X|^2
+a\left|v_\theta-\frac ba v_X\right|^2
+a\csc^2\theta|v|^2
\right],
\]

write `v=a^{1/2}y`. Since `a` is independent of `X`,

\[
v_X=a^{1/2}y_X,
\qquad
v_\theta=a^{1/2}\left(y_\theta+\frac{a'}{2a}y\right).
\]

The first term becomes `|y_X|^2`, while the second becomes

\[
\left|a\left(y_\theta+\frac{a'}{2a}y\right)-b y_X\right|^2.
\]

This is the same normalization behind PF-233's exact operator-valued transfer law, now retained in the full PF-232 sheared form. It shows before any dilation that the actual perturbative coefficient is `b`, as PF-232 found at energy level.

Under `Y=theta/s`, `U_s` contributes one factor `s^{-1}` to a tangential derivative and one compensating factor from `a=sA_s`; the measure and unitary amplitude cancel the rest. That is why (9)--(10) have order-one principal coefficients rather than coefficients degenerating with the corridor width.

## 2. The canonical hypercycle coefficients improve under scaled differentiation

For

\[
f_w(\theta)=\operatorname{arsinh}(w\sin\theta),
\]

the function `f_w/w` extends smoothly through `w=0`. On any fixed `|w|<=w_*<1`, every fixed `theta` derivative therefore obeys

\[
\|\partial_\theta^j f_w\|_\infty\le C_j|w|.
\tag{21}
\]

Because

\[
A_s(Y)=1-\frac{f_1(sY)+f_2(sY)}s,
\]

each `Y` derivative after the first gains an additional factor of `s`, giving (13). Likewise

\[
\mathsf b_s(X,Y)
=(1-X)f_1'(sY)-Xf_2'(sY),
\]

so its `k`th scaled tangential derivative has size `O(beta s^k)`. The long-strip family becomes **smoother**, not rougher, in the scaled tangential coordinate as the corridor shrinks.

The only nonuniform-looking coefficient is the endpoint potential. But for `0<x<pi`,

\[
\frac2\pi\min(x,\pi-x)\le\sin x\le\min(x,\pi-x).
\]

With `x=sY` this gives (17): the singularity is a fixed Hardy profile at each end of a strip whose length tends to infinity, not an `s`-dependent blowup in its natural scaled distance.

## 3. Consequence for the PF-240 gate

PF-240 deliberately formulates its desired regularity using `K_a`, not unscaled Fourier derivatives in `theta`. Equation (20) shows why that currency is decisive. After the exact dilation, `K_a` becomes `\widetilde K_s`, the first-order tangential operator associated with the uniformly scaled form (19).

Hence a failure of

\[
\|K_a^{r_2}H_ZK_a^{r_1}\|\le C\beta,
\qquad r_1+r_2>1,
\tag{22}
\]

cannot be attributed merely to the coefficient `a(theta)~s` making the interior operator nonuniformly elliptic. That apparent degeneration is a coordinate/scale artifact for the PF-240 norm.

The remaining analytic hazards are now more specific:

- the tangential interval length `L_s=pi/s` diverges;
- the two tangential ends carry the inverse-square Hardy profile (17), rather than ordinary smooth bounded-geometry endpoints;
- PF-240 concerns the **difference of actual-seam-normalized Schur factors**, not only the raw interior DtN map;
- the desired estimate must retain the perturbative `O(beta)` factor after boundary normalization;
- uniform off-diagonal boundary regularity still has to be proved, rather than inferred from pointwise-in-`s` smoothing.

This is a strict narrowing of the PDE problem: the shrinking physical corridor width itself is no longer an independent candidate obstruction.

## 4. Prior-art and novelty audit

Rescaling thin domains to expose a nondegenerate reference operator is classical. Friedlander and Solomyak, *On the spectrum of the Dirichlet Laplacian in a narrow strip*, Israel J. Math. 170 (2009), 337--354, DOI `10.1007/s11856-009-0032-y`, study a width-dependent strip by rescaling and resolvent analysis. The present calculation does not claim novelty for thin-strip blowup.

Uniform elliptic regularity on noncompact manifolds with boundary and bounded geometry is also classical. Große and Nistor, *Uniform Shapiro-Lopatinski conditions and boundary value problems on manifolds with bounded geometry*, arXiv:1703.07228, explicitly formulate regularity through families of local problems with constants uniform in the base point and prove such regularity for strongly elliptic Dirichlet problems under their bounded-geometry hypotheses. Likewise PF-240 already records the classical smoothing of DtN interaction between distinct smooth boundary components, including Hislop--Lutzer's approximately diagonal decomposition for multiply connected domains, *Inverse Problems* 17 (2001), 1717--1741, DOI `10.1088/0266-5611/17/6/313`.

Those results do not directly establish (22). The scaled PF family has a growing tangential interval and the Hardy endpoint profile (17), while the operator in (22) includes the actual complete-lift seam normalization. The literature located in the targeted audit does not state a theorem that simultaneously gives uniformity in this family, the `O(beta)` perturbative factor, and more than one total `\widetilde K_s` boundary derivative for the normalized correction.

No novelty is claimed for coordinate blowup, strong ellipticity, Hardy scaling, or bounded-geometry regularity. The project-specific mathematical delta is the **exact compatibility** between PF-232's canonical hypercycle coefficients, PF-233's mass-conjugated operator `K_a`, and the PF-240 Sobolev currency: after the same normalization used by the spectral count, the full sheared interior is a uniformly elliptic long-strip family with a `beta`-small smooth shear.

## 5. Falsification and boundary checks

1. **No smoothing theorem is claimed.** Equations (9)--(20) are an exact reduction and coefficient audit. They do not prove PF-240's estimate (22).
2. **Growing length is real.** Uniform local ellipticity does not automatically imply a global boundary-to-boundary estimate independent of `L_s`.
3. **Hardy ends are not silently treated as smooth bounded geometry.** The potential is uniformly scaled but singular at `Y=0,L_s`; a theorem used next must handle that form domain or localize away from the ends with a controlled reassembly.
4. **Seam normalization remains inside the target.** `U_s` unitarily transports the actual-seam-normalized operator, but PF-241 does not prove uniform pseudodifferential bounds for the transported seam form `Q`.
5. **The `beta` factor remains mandatory.** A uniform `O(1)` smoothing estimate would not close PF-240's reciprocal-prime arithmetic budget.
6. **Finite heads are harmless.** The uniform claims are canonical-tail claims; finitely many initial corridors may be treated separately.
7. Physical `P/H` recoupling, one-cusp pant completion, neighboring-cell coupling, PF-222 global nested reassembly, wave operators, determinants/resonances, prime/clone separation, zeta zeros, and RH remain outside the result.

## Consequences for the research line

PF-240 left two qualitatively different explanations for a possible failure of the desired high-high estimate: genuine bad boundary regularity, or constants blowing up simply because the corridor family collapses. PF-241 removes the second explanation at principal-coefficient level in exactly the `K_a` scale used by PF-240.

The next local theorem should therefore be sought on the scaled family (9)--(10), not on the raw thin strip. The clean target is a **uniform long-strip off-diagonal boundary estimate** for the difference between the sheared and diagonal problems, followed through the actual seam-normalized Schur map, with `O(beta)` size and total `\widetilde K_s` gain greater than one. A proof may use uniform local elliptic regularity plus a separate Hardy-end argument, an energy/Poisson semigroup factorization, or a parameter-dependent boundary calculus; whichever route is used must control the growing strip length and the seam normalization explicitly.

A negative result is now equally informative: it must locate a genuine source of nonuniformity in one of those surviving mechanisms rather than attributing it to the raw factor `a(theta)~s`.