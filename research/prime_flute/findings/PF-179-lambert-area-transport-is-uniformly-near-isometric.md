# PF-179 — Lambert bodies admit an exact area-preserving near-isometric transport

**Status:** `EXACT-DERIVED + CLASSICAL-TRANSPORT + POSITIVE/BOUNDARY`. PF-176--PF-178 isolate a quantitative difficulty in the `rho=1` route to PF-175: a qualitative Moser correction exists globally, but its derivative cost need not remain uniform on degenerating pieces. The one-parameter Lambert bodies themselves do **not** carry that obstruction. In PF-125's parameter-independent Fermi chart, the change of variable `y=sinh rho` makes hyperbolic area exactly `dy d tau`. This exposes an explicit area-preserving transport between `Q(a)` and `Q(a+d)`: on the finite branch it is a triangular mass transport with a closed formula, on the outer branch it is an exact hyperbolic isometry, and the two are joined across one uniformly thick corner patch by a fixed-domain relative Moser correction. The resulting map has `rho=1` exactly and bilipschitz distortion `1+O(d)` uniformly as `a->infinity`. Its split-ray trace differs from the elementary family `asinh(e^beta sinh tau)` only by `O(d e^{-2a})` in the same `L^infinity + dot W^{1,1}` trace scale used in PF-132, so the exact prime/shift family retains summable adjacent split mismatch. Thus the long Lambert bodies no longer require a degeneration-sensitive volume correction. The unresolved gate is the **area-preserving interface/global assembly**: split synchronization, cusp handoff, simultaneous insertion of all true Margulis-thin collar gauges, and the final inverse-unit-ball weighted metric budget. No global smooth prime/shift `rho=1` marking with PF-175's weighted hypothesis, Schatten conclusion, scattering equivalence, or RH consequence is claimed.

## Claim

Let `Q(a)` be the PF-125 one-parameter ideal Lambert quadrilateral, written in Fermi coordinates about its artificial split ray as

\[
g=d\rho^2+\cosh^2\rho\,d\tau^2,
\qquad
0\le \rho\le H_a(\tau),
\qquad \tau\ge0.
\tag{1}
\]

Put

\[
A=\cosh a,
\qquad
S=\sinh a,
\qquad
T_a=\frac12\log\cosh(2a).
\tag{2}
\]

PF-125 gives

\[
\tanh H_a(\tau)=\frac{\cosh\tau}{A}
\quad(0\le\tau\le T_a),
\tag{3}
\]

and

\[
\tanh H_a(\tau)=A e^{-\tau}
\quad(\tau\ge T_a).
\tag{4}
\]

Fix `d_0>0` small. There are `a_0` and `C`, depending only on `d_0`, such that for every

\[
a\ge a_0,
\qquad
a'=a+d,
\qquad 0\le d\le d_0,
\tag{5}
\]

there is an orientation-preserving map

\[
\boxed{
F^{\mathrm{vol}}_{a,a'}:Q(a)\longrightarrow Q(a')
}
\tag{6}
\]

which is smooth on the interior and smooth up to each boundary face, and satisfies

\[
\boxed{
(F^{\mathrm{vol}}_{a,a'})^*d\mu_{a'}=d\mu_a,
\qquad
\operatorname{Bilip}(F^{\mathrm{vol}}_{a,a'})\le1+Cd.
}
\tag{7}
\]

The finite head `a<a_0` may be matched with arbitrary finite constants.

The map preserves the artificial split ray as a set. Write its split trace as

\[
(0,\tau)\longmapsto(0,\Theta_{a,a'}(\tau)).
\tag{8}
\]

Define

\[
\beta(a,a'):=\log\frac{\sinh a'}{\sinh a},
\qquad
\epsilon(a,a'):=\log\frac{\cosh a'}{\cosh a},
\tag{9}
\]

and

\[
\psi_\beta(\tau):=\operatorname{arsinh}(e^\beta\sinh\tau).
\tag{10}
\]

For the construction below one may choose `Theta` so that

\[
\boxed{
\|\Theta_{a,a'}-\psi_{\beta(a,a')}\|_{\mathcal T}
\le C d e^{-2a},
}
\tag{11}
\]

where PF-132's trace norm is

\[
\|f\|_{\mathcal T}
:=\|f\|_{L^\infty(0,\infty)}
+\int_0^\infty |f'(\tau)|\,d\tau.
\tag{12}
\]

For the exact prime/shift half-cuffs `a_n,a_n^+=a_n+\delta_n`, let

\[
\Theta_n:=\Theta_{a_n,a_n^+}.
\tag{13}
\]

Then

\[
\boxed{
\sum_n\|\Theta_n-\Theta_{n+1}\|_{\mathcal T}<\infty.
}
\tag{14}
\]

Finally, because the volume ratio is exactly one and the metric distortion is `O(d)`, for every fixed `r>=1`,

\[
\boxed{
\int_{Q(a)}
\delta_{g_a,(F^{\mathrm{vol}}_{a,a'})^*g_{a'}}^{\,r}
\,d\mu_a
\le C_r d^r.
}
\tag{15}
\]

Hence the exact prime/shift family of **independent Lambert bodies** has a finite unweighted `L^r` metric budget in this exact volume gauge for every `r>1`, since PF-107 gives `delta_n=O(p_n^{-1})`. Equation (15) is not the inverse-unit-ball weighted hypothesis of PF-175, and the independent maps in (6) are not yet one globally assembled flute map.

## 1. The Fermi area coordinate removes the volume density from the problem

Set

\[
\boxed{y:=\sinh\rho.}
\tag{16}
\]

Then `d rho=dy/sqrt(1+y^2)` and (1) becomes

\[
\boxed{
g
=\frac{dy^2}{1+y^2}
+(1+y^2)d\tau^2,
\qquad
d\mu=dy\,d\tau.}
\tag{17}
\]

Both the metric and area form are now independent of `a`; only the upper boundary moves. Write

\[
D_a
=\{(\tau,y):\tau\ge0,\ 0\le y\le Y_a(\tau)\},
\qquad
Y_a(\tau):=\sinh H_a(\tau).
\tag{18}
\]

Equations (3)--(4) give the exact width functions

\[
\boxed{
Y_a(\tau)
=\frac{\cosh\tau}
{\sqrt{S^2-\sinh^2\tau}}
\quad(0\le\tau\le T_a),
}
\tag{19}
\]

and

\[
\boxed{
Y_a(\tau)
=\frac{A e^{-\tau}}
{\sqrt{1-A^2e^{-2\tau}}}
\quad(\tau\ge T_a).
}
\tag{20}
\]

The ideal Lambert quadrilateral has three right angles and one ideal vertex, hence Gauss--Bonnet gives

\[
\operatorname{Area}(Q(a))=\frac\pi2
\tag{21}
\]

for every `a`. This constant-area fact is the exact compatibility condition needed for a global area-preserving transport between `D_a` and `D_{a'}`.

The one-dimensional section masses can also be integrated explicitly. On the finite branch,

\[
\boxed{
\int_0^\tau Y_a(s)\,ds
=\arcsin\frac{\sinh\tau}{S},
}
\tag{22}
\]

while on the outer branch

\[
\boxed{
\int_\tau^\infty Y_a(s)\,ds
=\arcsin(Ae^{-\tau}).
}
\tag{23}
\]

At the corner these fit because

\[
\boxed{
M_c(a)
:=\int_0^{T_a}Y_a(s)\,ds
=\arctan(\tanh a),
\qquad
M_c'(a)=\operatorname{sech}(2a).
}
\tag{24}
\]

Thus changing `a` by `d` moves only

\[
\boxed{|M_c(a')-M_c(a)|\le C d e^{-2a}}
\tag{25}
\]

of area from one side of the Lambert corner to the other. This exponentially small corner-mass drift is what permits a uniformly tame area-preserving splice.

## 2. The finite branch has an explicit triangular area-preserving map

Put

\[
\lambda:=\frac{S'}S=e^\beta,
\qquad S'=\sinh a'.
\tag{26}
\]

On the part of the finite branch staying a fixed distance below the corner, define

\[
\boxed{
\tau'
=\psi_\beta(\tau)
=\operatorname{arsinh}(\lambda\sinh\tau),
\qquad
y'=\frac{y}{\psi_\beta'(\tau)}.
}
\tag{27}
\]

The derivative is

\[
\psi_\beta'(\tau)
=\frac{\lambda\cosh\tau}
{\sqrt{1+\lambda^2\sinh^2\tau}}.
\tag{28}
\]

Equations (19), (27), and (28) give the exact boundary identity

\[
\boxed{
Y_{a'}(\psi_\beta(\tau))
=\frac{Y_a(\tau)}{\psi_\beta'(\tau)}.
}
\tag{29}
\]

Hence (27) maps the finite upper boundary exactly to the target finite upper boundary. Its Euclidean Jacobian in the area coordinates (17) is

\[
\det
\begin{pmatrix}
\psi_\beta'&0\\
-\psi_\beta''y/(\psi_\beta')^2&1/\psi_\beta'
\end{pmatrix}
=1,
\tag{30}
\]

so it preserves hyperbolic area exactly.

The metric cost is uniform. Since

\[
\log\lambda
=\int_a^{a'}\coth u\,du,
\tag{31}
\]

we have `|log lambda|<=C d` on the tail. Moreover

\[
(\psi_\beta')^2
=\frac{\lambda^2(1+\sinh^2\tau)}
{1+\lambda^2\sinh^2\tau},
\tag{32}
\]

and

\[
\boxed{
\frac d{d\tau}\log\psi_\beta'
=\frac{(1-\lambda^2)\tanh\tau}
{1+\lambda^2\sinh^2\tau}.}
\tag{33}
\]

Therefore

\[
|\psi_\beta'-1|
+\left|\frac1{\psi_\beta'}-1\right|
+\left|\frac d{d\tau}\frac1{\psi_\beta'}\right|
\le C d.
\tag{34}
\]

The Fermi width is uniformly bounded above (`Y_a<=coth a_0`), so in the parameter-independent metric (17) the differential of (27) is `I+O(d)` uniformly. The finite-branch transport is thus area preserving and `1+O(d)` bilipschitz with no degeneration in `a`.

## 3. The outer branch is an exact isometry

Put

\[
\epsilon:=\log\frac{A'}A,
\qquad A'=\cosh a'.
\tag{35}
\]

On the common outer branch define simply

\[
\boxed{
(\tau,y)\longmapsto(\tau+\epsilon,y).}
\tag{36}
\]

Equation (20) gives

\[
A'e^{-(\tau+\epsilon)}=Ae^{-\tau},
\tag{37}
\]

so (36) maps the upper boundary exactly to the target upper boundary. Because (17) has no `tau` dependence, (36) is not merely area preserving: it is an **exact hyperbolic isometry** of the Fermi-coordinate model.

The two natural trace parameters differ only exponentially far down the long Lambert body:

\[
\boxed{
\beta-\epsilon
=\log\frac{\tanh a'}{\tanh a},
\qquad
|\beta-\epsilon|
\le C d e^{-2a}.}
\tag{38}
\]

This is the same `sinh`-versus-`cosh` correction already isolated in PF-132.

## 4. Only one uniformly thick corner patch needs Moser correction

The finite map (27) and outer isometry (36) cannot simply be cut at `T_a`, because (25) says the finite-branch areas of `Q(a)` and `Q(a')` differ by `O(d e^{-2a})`. An exact area-preserving map must transfer that tiny amount across the Lambert corner.

Fix once and for all a small `r_0>0`. Use (27) on

\[
\tau\le T_a-r_0
\tag{39}
\]

and (36) on

\[
\tau\ge T_a+r_0.
\tag{40}
\]

Their images determine two target cut sections. Since both outside maps preserve area and both full quadrilaterals have area `pi/2`, the remaining source and target corner patches have **exactly equal area**.

PF-125's recentered formulas show that on every fixed interval `|tau-T_a|<=r_0` the Fermi width has a positive lower bound and a finite upper bound independent of large `a`. The same holds for the target. After recentering, these corner patches therefore lie in one fixed bounded-geometry class.

Choose the split-ray trace across this patch to interpolate smoothly between the finite trace `psi_beta` and the outer trace `tau+epsilon`. Equation (38) and the elementary estimate

\[
\psi_\beta(\tau)-\tau-\beta
=O(d e^{-2\tau})
\quad(\tau\ge T_a-r_0)
\tag{41}
\]

allow the interpolation to satisfy

\[
\|\Theta_{a,a'}-\psi_\beta\|_{L^\infty(\text{corner})}
+\int_{\text{corner}}
|\Theta_{a,a'}'-\psi_\beta'|\,d\tau
\le C d e^{-2a}.
\tag{42}
\]

Near the split ray, lift this boundary trace by the exact area-preserving collar germ

\[
(\tau,y)
\longmapsto
\left(
\Theta_{a,a'}(\tau),
\frac{y}{\Theta_{a,a'}'(\tau)}
\right).
\tag{43}
\]

Use analogous local area-preserving germs near the other boundary faces, agreeing with (27) and (36) near the two cut sections. Because all prescribed germs differ from the identity by `O(d)` in the recentered bounded-geometry chart, an ordinary collar extension gives an initial corner-patch diffeomorphism with differential `I+O(d)` which is already area preserving near the patch boundary.

Its Jacobian has the form `1+q`, with `q=O(d)`, compactly supported in the interior and integral zero because the two patches have equal area. On a fixed planar reference patch, the mean-zero top form `q\,dy\wedge d\tau` has a compactly supported primitive with `C^1` norm `O(d)` (equivalently, solve one fixed-domain divergence equation). The standard relative Moser flow generated from that primitive is identity near the boundary and has differential `I+O(d)`. Composing it with the initial extension makes the corner map **exactly area preserving** while retaining the `1+O(d)` bilipschitz bound.

This is precisely where PF-178's warning about support-to-boundary constants becomes harmless: the correction is performed on one uniformly thick fixed-scale patch, not on a collar whose available support width collapses with `a`.

Combining Sections 2--4 proves (7). The construction is a quantitative local use of classical volume-form transport; it does not require a tail-uniform Moser theorem on the whole degenerating pant.

## 5. The area gauge does not reopen the split-ray trace obstruction

The trace family in (10) has the same tame parameter structure as PF-132's `arcosh` family. Direct differentiation gives

\[
\partial_\beta\psi_\beta(\tau)
=\frac{e^\beta\sinh\tau}
{\sqrt{1+e^{2\beta}\sinh^2\tau}},
\tag{44}
\]

so

\[
|\partial_\beta\psi_\beta|\le1.
\tag{45}
\]

Also

\[
\psi_\beta'(\tau)
=\frac{e^\beta\cosh\tau}
{\sqrt{1+e^{2\beta}\sinh^2\tau}},
\tag{46}
\]

and

\[
\boxed{
\partial_\beta\psi_\beta'(\tau)
=\frac{e^\beta\cosh\tau}
{(1+e^{2\beta}\sinh^2\tau)^{3/2}}.}
\tag{47}
\]

For `beta` in the small tail interval, the right-hand side is bounded by `C sech^2 tau`, hence

\[
\boxed{
\|\psi_\beta-\psi_{\widetilde\beta}\|_{\mathcal T}
\le C|\beta-\widetilde\beta|.}
\tag{48}
\]

Outside the corner, (27) equals `psi_beta` exactly on the finite side, while (36), (38), and (41) give

\[
\| (\tau+\epsilon)-\psi_\beta(\tau)\|_{\mathcal T([T_a+r_0,\infty))}
\le C d e^{-2a}.
\tag{49}
\]

Together with the fixed-corner choice (42), this proves (11).

PF-132 already proves for the exact prime/shift sequence

\[
\sum_n|\beta_n-\beta_{n+1}|<\infty,
\tag{50}
\]

and also records

\[
|\beta_n-\epsilon_n|
\le C\delta_n e^{-2a_n}.
\tag{51}
\]

PF-107 makes `delta_n` bounded on the tail and PF-131/PF-114 give `sum e^{-2a_n}<infinity`. Hence (11), (48), and (50) imply

\[
\begin{aligned}
\sum_n\|\Theta_n-\Theta_{n+1}\|_{\mathcal T}
&\le
C\sum_n|\beta_n-\beta_{n+1}|\\
&\quad+C\sum_n\delta_n e^{-2a_n}
<\infty,
\end{aligned}
\tag{52}
\]

which proves (14).

This is important for the next assembly step. Exact area preservation changes the one-parameter Lambert map, but it does **not** resurrect a nonsummable split-ray common mode. The remaining split problem is two-dimensional and geometric: construct an **area-preserving** synchronization of the two already-summable traces while preserving the genuine pant boundaries.

## 6. Consequence for the current PF-175 frontier

Equation (7) gives an exact local volume gauge,

\[
\rho\equiv1,
\tag{53}
\]

on every independently matched Lambert body. Since the Güneysu--Thalmaier metric-deviation scalar is locally Lipschitz in the logarithms of the relative metric eigenvalues near the identity, the `1+O(d)` bilipschitz estimate gives

\[
\delta_{g_a,(F^{\mathrm{vol}}_{a,a'})^*g_{a'}}
\le C d.
\tag{54}
\]

The area is `pi/2`, so (15) follows. For the shift clone, PF-107 gives

\[
\delta_n=O(p_n^{-1}),
\tag{55}
\]

and therefore

\[
\sum_n\delta_n^r<\infty
\qquad(r>1).
\tag{56}
\]

Thus PF-178's quantitative Moser concern can be narrowed:

\[
\boxed{
\text{independent long Lambert bodies}
\quad\text{already admit}\quad
\rho=1 + \text{uniform }O(1/p_n)\text{ metric strain}.}
\tag{57}
\]

For the sharp-Schatten clue, this is the right exponent scale: PF-175 only needs some `r>1`, so the loss of PF-130's stronger isolated-body `L^1` localization is not itself fatal. What still prevents invocation of PF-175 is not bodywise volume correction but the requirement that **one single smooth complete marking** simultaneously satisfy:

- exact left/right split synchronization in the area gauge;
- compatible zero-twist cuff traces and the exact deep-cusp handoff;
- the PF-177 gauge on every PF-138 true Margulis-short collar core;
- two-sided inverse-unit-ball weighted `delta^r` summability after those modules are assembled.

In particular, (15) is deliberately unweighted. A true short geodesic can cross the canonical pant decomposition, so the ambient unit-ball weight cannot be replaced by a pantwise constant merely because `Q(a)` itself has fixed area.

## 7. Prior-art and novelty audit

The transport mechanism is classical in general form. The map (27) is a two-dimensional triangular/marginal rearrangement of the same type as the Knothe--Rosenblatt construction; see G. Carlier, A. Galichon, F. Santambrogio, *From Knothe's Transport to Brenier's Map and a Continuation Method for Optimal Transport*, SIAM Journal on Mathematical Analysis 41 (2010), 2554--2576, DOI `10.1137/080740647`. No novelty is claimed for monotone mass rearrangement, relative Moser correction, or Gauss--Bonnet area of a Lambert quadrilateral.

M. Vuorinen and G. Wang, *Hyperbolic Lambert quadrilaterals and quasiconformal mappings*, Annales Academiae Scientiarum Fennicae Mathematica 38 (2013), 433--453, DOI `10.5186/aasfm.2013.3845`, study sharp hyperbolic-distance inequalities and quasiconformal images of Lambert quadrilaterals. Their results provide geometric prior-art context but not the area-coordinate transport (27), the exact outer isometry (36), or the prime/shift trace summation (52).

For support-controlled volume correction, P. Teixeira, *Dacorogna--Moser theorem on the Jacobian determinant equation with control of support*, DCDS 37 (2017), 4071--4089, DOI `10.3934/dcds.2017173`, and its pullback addendum arXiv:1705.01416 provide the classical framework already used in PF-178. PF-179 uses that mechanism only on a fixed uniformly thick corner patch; it does not infer a uniform theorem on the degenerating infinite flute.

Directed searches by structure -- Lambert quadrilateral area-preserving maps, quasiconformal Lambert comparison, triangular/Knothe rearrangement, and support-controlled Jacobian correction -- did not locate the exact formulas (27), (36), or their prime/shift specialization. Absence of such a source is **not** used as a novelty theorem. The durable project-specific content is the exact decomposition

\[
\boxed{
\text{finite-branch area transport}
+\text{ exact outer isometry}
+\text{ fixed-corner Moser splice}
}
\tag{58}
\]

with a degeneration-uniform `1+O(d)` bound, together with the source-grounded summable trace consequence (52).

## 8. Audit / falsification core

A later adversary can check PF-179 through the following finite chain:

1. import PF-125's Fermi metric and branch equations (1)--(4), set `y=sinh rho`, and verify the parameter-independent metric/area form (17);
2. derive the width formulas (19)--(20) and the section integrals (22)--(23);
3. use the Lambert angle data to verify `Area(Q(a))=pi/2`, then compute the corner mass (24) and its derivative;
4. verify directly that the finite map (27) sends the upper graph to the target graph and has Jacobian one;
5. check (32)--(34) to obtain a degeneration-uniform `1+O(d)` differential bound;
6. verify that the outer translation (36) is an exact isometry and that `beta-epsilon=O(d e^{-2a})`;
7. on a fixed recentered corner patch, check equal residual areas and run the relative Moser correction only after arranging area-preserving boundary germs; the patch geometry must remain uniformly nondegenerate;
8. differentiate `psi_beta` to verify (44)--(48), combine the outer/corner error with PF-132's `ell^1` adjacent `beta` variation, and obtain (52);
9. preserve the evidence boundary: do **not** turn the independent Lambert maps into a global weighted comparison until split/cuff/cusp/true-thin compatibility is proved in one marking.

A refutation would need to break the exact area coordinate, the finite-branch boundary/Jacobian identity, the fixed-corner equal-area splice, the uniform differential estimate, or the trace summability. Failure of a later area-preserving global assembly would not refute PF-179; it would realize exactly the remaining boundary recorded here.