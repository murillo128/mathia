# PF-273 — seam square root is a complete-Bernstein Green continuum with mass-one edge

**Status:** `LITERATURE+DERIVED + COMPLETE-BERNSTEIN-CALCULUS + POSITIVE-GREEN-CONTINUUM + MASS-GAP-CLOSURE + ROBIN-ROUTE-NARROWING`.

PF-261 shows that the fixed-axis finite-seam Dirichlet-to-Neumann symbol

\[
f_w(\lambda):=\sqrt\lambda\,\tanh(w\sqrt\lambda),
\qquad w=rs>0,
\tag{1}
\]

is a positive discrete mixture of the elementary complete-Bernstein kernels `\lambda/(\lambda+t)`. PF-254/PF-257 show that the actual normalized Robin source does not use `f_w(L)` directly: before the first paid longitudinal propagation it contains the square-root factor

\[
Q_w^{1/2}=g_w(L),
\qquad
g_w(\lambda):=\sqrt{f_w(\lambda)}.
\tag{2}
\]

The square root changes the mass geometry qualitatively. The function `g_w` is again a complete Bernstein function, but its Stieltjes measure is no longer the odd discrete mass ladder of PF-261. It is an absolutely continuous **positive Green continuum whose support reaches `t=0`**. In the PF-264 Green parameter `\mu=\sqrt{1+t}`, the continuum therefore reaches the critical edge `\mu=1`.

This removes a hidden assumption from the accepted Robin-homotopy route. PF-272's strict sublinear leakage exponent for the naked relative seam comes from its lowest **discrete** mass `a_0^2>0`, equivalently `\mu_0>1`. That first-pole gap cannot simply be inherited by `Q_w^{1/2}`: taking the operator square root closes it all the way to the axis edge. The next fixed-axis gate is consequently the **full normalized source** `(I+XX^*)^{-1}X`, not another estimate that treats the square-root source as though it retained PF-272's discrete first-pole mass.

## 1. The raw seam symbol is an atomic complete Bernstein function

PF-261 gives the exact partial fraction expansion

\[
f_w(\lambda)
=
\frac{2}{w}\sum_{k\ge0}
\frac{\lambda}{\lambda+a_k^2},
\qquad
a_k=\frac{(2k+1)\pi}{2w}.
\tag{3}
\]

Thus `f_w` has the complete-Bernstein representation

\[
f_w(\lambda)
=
\int_{(0,\infty)}\frac{\lambda}{\lambda+t}\,\sigma_w(dt),
\qquad
\sigma_w=\frac{2}{w}\sum_{k\ge0}\delta_{a_k^2}.
\tag{4}
\]

The integrability condition is immediate from `a_k\asymp k`, and there is neither killing nor drift. In particular the representing mass has the strict lower edge

\[
t\ge a_0^2=\frac{\pi^2}{4w^2}>0.
\tag{5}
\]

This is exactly the mass gap that appears in PF-272 through

\[
\mu_0=\sqrt{1+a_0^2}>1.
\tag{6}
\]

## 2. The square-root seam symbol is again complete Bernstein

The scalar function `\lambda\mapsto\sqrt\lambda` is a complete Bernstein function, and the class of complete Bernstein functions is closed under composition. Hence

\[
g_w=\sqrt{\,f_w\,}
\tag{7}
\]

is a complete Bernstein function. Its canonical representation therefore has the form

\[
g_w(\lambda)
=
\int_{(0,\infty)}
\frac{\lambda}{\lambda+t}\,\nu_w(dt).
\tag{8}
\]

There is no constant term because `g_w(0+)=0`, and there is no linear drift because

\[
\frac{g_w(\lambda)}{\lambda}
\sim \lambda^{-3/4}
\longrightarrow0
\qquad(\lambda\to\infty).
\tag{9}
\]

The complete-Bernstein closure and representation are classical; the point here is to compute the representing measure at the fixed-axis seam and feed it back into the PF-254/PF-257 source factor.

## 3. Stieltjes inversion gives an explicit continuum down to zero mass

Take the upper boundary value on the negative axis. Away from zeros and poles of the tangent,

\[
\sqrt{-t+i0}=i\sqrt t,
\qquad
f_w(-t+i0)
=-\sqrt t\,\tan(w\sqrt t).
\tag{10}
\]

Whenever `\tan(w\sqrt t)>0`, this boundary value lies on the negative real axis and the principal complete-Bernstein square root has

\[
\operatorname{Im} g_w(-t+i0)
=t^{1/4}\sqrt{\tan(w\sqrt t)}.
\tag{11}
\]

Whenever `\tan(w\sqrt t)<0`, the boundary value of `g_w` is real and the Stieltjes density vanishes. The Stieltjes inversion formula for (8) therefore yields

\[
\boxed{
\frac{d\nu_w}{dt}(t)
=
\frac{\sqrt{\tan(w\sqrt t)}}{\pi t^{3/4}}
\mathbf 1_{\{\tan(w\sqrt t)>0\}}.
}
\tag{12}
\]

Equivalently, the support is the union

\[
\operatorname{supp}\nu_w
=
\overline{\bigcup_{k\ge0}
\left(
\left(\frac{k\pi}{w}\right)^2,
\left(\frac{(k+1/2)\pi}{w}\right)^2
\right)}.
\tag{13}
\]

There are no point masses at the interval endpoints: at a zero of `f_w`, `g_w` has square-root vanishing, while at a pole of `f_w`, `g_w` has only a square-root singularity rather than the simple pole that an atom in (8) would produce. Thus (12) is the full representing measure up to the harmless endpoint convention.

Most importantly, the first interval starts at zero. Since

\[
\tan(w\sqrt t)=w\sqrt t+O(t^{3/2}),
\tag{14}
\]

we obtain the exact lower-edge law

\[
\boxed{
\frac{d\nu_w}{dt}(t)
=
\frac{\sqrt w}{\pi\sqrt t}\bigl(1+O(t)\bigr),
\qquad t\downarrow0.
}
\tag{15}
\]

The resolvent weight that appears off the diagonal is therefore

\[
t\,\frac{d\nu_w}{dt}(t)
=
\frac{\sqrt w}{\pi}\,t^{1/2}\bigl(1+O(t)\bigr).
\tag{16}
\]

So the continuum has integrable but genuinely nonzero mass arbitrarily close to `t=0`.

## 4. The square-root seam is a sign-coherent continuum of the PF-264 Green kernels

Functional calculus in (8) gives

\[
g_w(L)
=
\int_{(0,\infty)}L(L+t)^{-1}\,\nu_w(dt).
\tag{17}
\]

For distinct same-parity Gegenbauer modes `e_i,e_j`, the identity part of

\[
L(L+t)^{-1}=I-t(L+t)^{-1}
\tag{18}
\]

drops out, so

\[
\boxed{
\langle e_i,g_w(L)e_j\rangle
=-\int_0^\infty
t\,\langle e_i,(L+t)^{-1}e_j\rangle\,\nu_w(dt).
}
\tag{19}
\]

Opposite parities remain uncoupled. In the PF-247 Jacobi gauge the massive Green kernels are positive, so every same-parity off-diagonal contribution in (19) has the same sign. The square root has therefore not introduced an arbitrary polar mixer: it has produced a **positive continuum of exactly the massive axis resolvents already isolated in PF-261--PF-264**.

For the normalized source factor of PF-254/PF-257,

\[
X_w
=s^{-1/2}A^{-1/4}g_w(L),
\qquad
X_wX_w^*
=s^{-1}A^{-1/4}f_w(L)A^{-1/4}
=:\mathcal R^0_{s,r}.
\tag{20}
\]

Hence the complete polar-free normalized injection is

\[
\boxed{
B_w
=(I+X_wX_w^*)^{-1}X_w
=(I+\mathcal R^0_{s,r})^{-1}X_w.
}
\tag{21}
\]

Equation (21) identifies the exact remaining nonlinear object: PF-272 controls the raw factor `\mathcal R^0_{s,r}`, while (19) controls the structure of the square-root source `X_w`. What is not yet controlled is how the left rational normalization in (21) acts on the deep high-to-low block.

## 5. Taking the square root closes the PF-272 mass gap

PF-264 associates the resolvent parameter `t=a^2` with the indicial exponent

\[
\mu(t)=\sqrt{1+t}.
\tag{22}
\]

For the raw seam (4), only the odd atoms `t=a_k^2` occur, so

\[
\mu\ge\mu_0>1.
\tag{23}
\]

For the square-root seam (12), every interval `(0,\delta)` carries positive `\nu_w` mass. Therefore

\[
\inf_{t\in\operatorname{supp}\nu_w}\mu(t)=1.
\tag{24}
\]

This is an exact structural distinction, not a numerical observation. It explains why PF-272's exponent

\[
\alpha_s(\theta)
=1+(1-\theta)(\mu_0-1/2)>1
\tag{25}
\]

cannot be transferred to `Q_w^{1/2}` merely by reusing the lowest-pole argument: the square-root functional calculus has replaced the discrete first pole by a continuum touching the mass-one edge.

PF-264's fixed-mass leading law remains consistent with this picture. Formally combining

\[
G_{ij}(t)
\sim
\frac{1}{2\mu(t)}
i^{-1/2+\mu(t)}j^{-1/2-\mu(t)}
\tag{26}
\]

with (16) shows why the boundary layer `t\asymp1/\log(j/i)` should be examined in any sharp separated-cone theorem. This is only a guide: PF-264 explicitly has fixed-`t` error terms, so (26) may not yet be integrated through a shrinking `t` window.

## 6. Consequence for the Robin-homotopy route

PF-254 already places every nontrivial Robin reflection cycle behind positive longitudinal propagation. Thus the first unsmoothed scale-changing gate is the normalized source `B_w` itself. PF-257 removes the need to estimate a polar partial isometry separately, and (19)--(21) now remove a second ambiguity: the square-root source is an exact Green continuum, but its mass support reaches the critical edge.

The accepted Robin clue should therefore ask a sharper question:

\[
\left\|
F_{\Lambda,\theta}
(I+\mathcal R^0_{s,r})^{-1}X_w
E_\Lambda
\right\|
\stackrel{?}{\lesssim}
\Lambda^{-R-\varepsilon}
\tag{27}
\]

for some fixed `\theta<1` and `R>1` in the PF-271 regime, with the logarithmic output window used when the following propagator is exactly exponential. A proof may exploit the rational normalization in (21); a negative result must show that the mass-one continuum survives that normalization strongly enough to obstruct the required block decay.

It is no longer justified to calibrate the square-root factor itself by PF-272's `\mu_0>1` first-pole exponent. Conversely, the presence of the mass-one continuum does **not** prove that (27) fails: `(I+\mathcal R^0_{s,r})^{-1}` is noncommuting with `X_w` at the relevant matrix level and may alter the block transfer.

## 7. Prior art and novelty audit

The complete-Bernstein ingredients are classical. R. L. Schilling, R. Song and Z. Vondraček, *Bernstein Functions: Theory and Applications*, 2nd ed., De Gruyter Studies in Mathematics 37 (2012), DOI `10.1515/9783110269338`, gives the Stieltjes representation/analytic characterization of complete Bernstein functions in Chapter 6 and closure under composition in Corollary 7.6. Its tables of examples also include the hyperbolic family

\[
\sqrt\lambda\,
\frac{a+\tanh(b\sqrt\lambda)}{1+a\tanh(b\sqrt\lambda)},
\qquad a,b>0,
\tag{28}
\]

from which `f_w` is also reached by the `a\downarrow0` pointwise-limit closure. M. Kwaśnicki and J. Mucha, *Extension technique for complete Bernstein functions of the Laplace operator*, Journal of Evolution Equations 18 (2018), 1341--1379, DOI `10.1007/s00028-018-0444-4`, provides broader prior-art context for complete-Bernstein functions as Dirichlet-to-Neumann symbols through Krein-string theory.

No novelty is claimed for complete Bernstein functions, their composition closure, Stieltjes inversion, or the general operator functional calculus. A targeted search for the exact nested symbol `sqrt(sqrt(lambda) tanh(w sqrt(lambda)))` and its Stieltjes measure did not locate a source deriving (12) in this form. The project-specific contribution is the exact insertion of that calculus into the PF-254/PF-257 normalized seam source and the resulting comparison with PF-261/PF-272: **the raw seam has a discrete positive mass gap, whereas its square root has a positive resolvent continuum touching `t=0`, hence `\mu=1`.**

This is route-level structure, not an RH result and not a claim that the normalized source succeeds or fails.

## 8. Boundaries and adversarial checks

1. **No block exponent for `X_w` is claimed.** Equation (19) is exact, but turning the `t\downarrow0` density into a sharp two-index asymptotic requires Green estimates uniform in the small-mass boundary layer. PF-264 is fixed mass.
2. **No failure of the normalized source is claimed.** The mass-one edge belongs to `X_w`; the actual gate is `(I+\mathcal R^0_{s,r})^{-1}X_w`, and the left factor can change block transfer.
3. **No polar-mixer shortcut.** The CBF representation applies to `g_w(L)` before the `A^{-1/4}` weight. It does not make `A` commute with `L`, nor does it diagonalize the full normalized source.
4. **Endpoint density checked.** The first support interval is `(0,(\pi/(2w))^2)`, and (15) is locally integrable. The square-root singularities at later tangent poles are also locally integrable and do not create Stieltjes atoms.
5. **Sign coherence is gauge-specific but exact.** It uses the PF-247 parity Jacobi gauge in which the negative-point Green kernel is positive. A different basis may hide the sign, not change the functional-calculus identity.
6. **Fixed-axis only.** Nothing here supplies uniformity in the corridor index, Robin homotopy parameter, shear, hypercycle transport, or actual `K_a` projectors.
7. **No global conclusion.** The physical `P/H` recoupling, finite-pant reassembly, neighboring-cell control, weak trace class, scattering/determinants, prime/control separation, zeta zeros, and RH remain downstream.

The finding is falsified if the PF-261 partial fraction coefficient is wrong, if `g_w` fails the complete-Bernstein composition criterion, or if the Stieltjes inversion of its negative-axis boundary value does not give (12). Equations (3), (7), and (10)--(16) make those checks explicit.

## Decisive next test

Stay on the fixed axis and estimate the exact block in (27), not the naked seam and not an isolated polar factor. First split the Stieltjes continuum of `X_w` into a small-mass sector and its complement. The natural small-mass scale suggested by (16) and PF-264 is `t\log(j/i)=O(1)`; proving a parameter-uniform Green law there would determine whether the mass-one edge produces a genuinely critical leakage term.

Then insert the same decomposition through `(I+\mathcal R^0_{s,r})^{-1}`. Either show that the rational normalization restores a strict PF-271-compatible exponent on one sublinear output window, or produce a sign/size-stable lower bound showing that the mass-one contribution survives normalization and forbids every such `R>1` estimate. Only after this fixed-axis discriminator is settled should the route spend effort on PF-255/PF-256 transport to the actual sheared corridor.