# AF-210 — Precompact source complexity turns Euler bands into finite norming sets

**Status:** `EXACT-DERIVED`, `CLASSICAL-MECHANISM`, `QUANTITATIVE-FIDELITY`, `FINITE-WITNESS-REDUCTION`, `SOURCE-COMPLEXITY-GATE`, `NO-NOVELTY-CLAIM`

## Claim

AF-208 and AF-209 separate three distinct regimes for a fixed Euler observation band. On unrestricted infinite-dimensional signed sources, a compact observation family has arbitrarily small singular directions; on a normalized precompact source class, a positive-width Euler band is uniformly coercive; and any fixed finite frequency list has a nontrivial kernel on unrestricted smooth sources. The remaining question is whether the continuum band is still intrinsically necessary once source complexity has already compactified the admissible class.

It is not. Compactness converts continuum coercivity into a finite norming set.

Let `Theta` be compact and let `K` be a compact subset of `C(Theta)` such that

\[
c:=\inf_{f\in K}\|f\|_\infty>0.
\tag{1}
\]

Then for every `0<epsilon<c` there is a finite set `Lambda subset Theta` such that

\[
\boxed{
\inf_{f\in K}\max_{\lambda\in\Lambda}|f(\lambda)|\ge c-\varepsilon.
}
\tag{2}
\]

Thus every compact family of observable profiles that stays uniformly away from the zero profile admits a finite evaluation set that preserves the same separation up to arbitrary fixed slack.

Apply this to AF-209. Fix

\[
m\ge1,\qquad x>0,\qquad \sigma>0,\qquad 0<T<\infty,\qquad L>x,
\]

and let

\[
(\mathcal A_T b)(\tau)
=
\int_x^L
\bigl(g_{m,\tau}(t)-g_{m,\tau}(x)\bigr)b(t)\,dt,
\qquad |\tau|\le T.
\tag{3}
\]

For any cone `mathcal C subset L^1([x,L])` whose normalized slice

\[
\mathcal S
=
\{b\in\mathcal C:V_h(b)=1\}
\tag{4}
\]

has relatively compact closure in `L^1`, AF-209 gives

\[
c_{\mathcal C}
:=
\inf_{b\in\mathcal S}\|\mathcal A_Tb\|_{C([-T,T])}
>0.
\tag{5}
\]

Consequently, for every `0<epsilon<c_mathcal C` there is a **finite set of frequencies** `Lambda subset [-T,T]` such that

\[
\boxed{
\max_{\lambda\in\Lambda}
|\mathcal A_Tb(\lambda)|
\ge
(c_{\mathcal C}-\varepsilon)V_h(b)
\qquad(b\in\mathcal C).
}
\tag{6}
\]

In particular this applies to the AF-209 bounded-variation cone

\[
\mathcal C_M
=
\{b\in BV([x,L]):\operatorname{Var}(b)\le M V_h(b)\}.
\tag{7}
\]

Hence a continuum of vertical Euler frequencies is required to obtain exact injectivity on the unrestricted infinite-dimensional signed source space, but **not** to certify stable recovery on a normalized precompact source class. Once source complexity supplies compactness, finitely many samples can be chosen to retain a uniform lower modulus.

There is also an explicit mesh version. Put

\[
B_1:=\sup_{b\in\overline{\mathcal S}}\|b\|_1<\infty,
\qquad
J_T:=
\sup_{|\tau|\le T,\ t\in[x,L]}
\left|
\partial_\tau
\bigl(g_{m,\tau}(t)-g_{m,\tau}(x)\bigr)
\right|<\infty.
\tag{8}
\]

Then every profile `mathcal A_T b` with `b in overline{mathcal S}` is `B_1J_T`-Lipschitz in `tau`. If `Lambda` is a finite `delta`-net of `[-T,T]`,

\[
\boxed{
\max_{\lambda\in\Lambda}|\mathcal A_Tb(\lambda)|
\ge
(c_{\mathcal C}-B_1J_T\delta)V_h(b).
}
\tag{9}
\]

Thus any mesh with `B_1J_T delta <= c_mathcal C/2` gives a discrete coercivity constant `c_mathcal C/2`. For `mathcal C_M`, AF-209 supplies the concrete normalized `L^1` bound

\[
B_1\le(L-x)(H^{-1}+M),
\qquad
H:=\int_x^L h(t)\,dt.
\tag{10}
\]

The exact cardinality is not the point: the new boundary is that the observation resource becomes finite **after** the source class is compactified, whereas no finite sample set can norm the unrestricted smooth signed class.

## Derivation

### 1. Compact profile families admit finite norming evaluations

For each `f in K`, compactness of `Theta` gives a point `theta_f` with

\[
|f(\theta_f)|=\|f\|_\infty\ge c.
\tag{11}
\]

Fix `0<epsilon<c` and define the relative open set

\[
U_f
:=
\{g\in K:|g(\theta_f)|>c-\varepsilon\}.
\tag{12}
\]

Because evaluation at `theta_f` is continuous in the supremum norm, `U_f` is open in `K`, and `f in U_f`. Hence the family `{U_f:f in K}` covers `K`.

Compactness of `K` gives a finite subcover

\[
K=U_{f_1}\cup\cdots\cup U_{f_N}.
\tag{13}
\]

Set

\[
\Lambda=\{\theta_{f_1},\ldots,\theta_{f_N}\}.
\tag{14}
\]

For every `g in K`, membership in some `U_{f_j}` gives

\[
\max_{\lambda\in\Lambda}|g(\lambda)|
\ge |g(\theta_{f_j})|
>c-\varepsilon,
\tag{15}
\]

which proves `(2)`.

The argument uses only compactness of the profile family and separation from zero. It does not require linearity, finite-dimensionality, analyticity, or a preassigned grid.

### 2. AF-209 supplies exactly the two hypotheses needed

Let `overline{mathcal S}` denote the `L^1` closure of the normalized source slice `(4)`. By hypothesis it is compact. The Euler map

\[
\mathcal A_T:L^1([x,L])\to C([-T,T])
\tag{16}
\]

is continuous, so

\[
K:=\mathcal A_T(\overline{\mathcal S})
\tag{17}
\]

is compact in the supremum norm.

AF-209 proves exact injectivity of `mathcal A_T` on `L^1([x,L])` for every positive-width band. Also `V_h=1` on `overline{mathcal S}`, so `0` does not belong to that normalized source set. Therefore the zero profile is not in `K`.

The continuous norm function attains a positive minimum on compact `K`, precisely the constant `c_mathcal C` in `(5)`. Applying the finite-norming lemma to this `K` proves `(6)` for normalized sources. Homogeneity gives the statement for arbitrary nonzero `b in mathcal C`; the zero source is trivial.

This isolates the logical chain cleanly:

\[
\text{source precompactness}
\Longrightarrow
\text{compact observable profile family}
\Longrightarrow
\text{continuum coercivity plus compactness}
\Longrightarrow
\text{finite norming evaluations}.
\tag{18}
\]

No extra arithmetic identity is introduced at the discretization step.

### 3. Uniform profile regularity gives an explicit frequency mesh

For normalized `b`, differentiation under the integral is justified by smoothness of the Euler kernel on the compact rectangle. Hence

\[
\begin{aligned}
|\mathcal A_Tb(\tau)-\mathcal A_Tb(\tau')|
&\le
\int_x^L
|\phi_\tau(t)-\phi_{\tau'}(t)|\,|b(t)|dt\\
&\le
B_1J_T|\tau-\tau'|,
\end{aligned}
\tag{19}
\]

where `phi_tau(t)=g_{m,tau}(t)-g_{m,tau}(x)`.

For a given `b`, choose `tau_*` attaining its band supremum. If `Lambda` has covering radius at most `delta`, choose `lambda in Lambda` with `|lambda-tau_*|<=delta`. Then

\[
|\mathcal A_Tb(\lambda)|
\ge
|\mathcal A_Tb(\tau_*)|-B_1J_T\delta
\ge
c_{\mathcal C}-B_1J_T\delta,
\tag{20}
\]

which proves `(9)`.

For a uniform grid on an interval of length `2T`, one may choose spacing at most `c_mathcal C/(B_1J_T)` to obtain covering radius at most `c_mathcal C/(2B_1J_T)` and therefore the factor `1/2` in `(9)`. When `J_T>0`, a sufficient number of grid points is

\[
N
=
1+\left\lceil\frac{2TB_1J_T}{c_{\mathcal C}}\right\rceil.
\tag{21}
\]

This count is only conditional on the continuum coercivity constant. AF-210 does not provide an effective lower estimate for `c_mathcal C`; obtaining one is a separate conditioning problem.

## Exact controls and boundaries

### Finite sampling still fails on the unrestricted smooth source class

Fix any finite frequency set

\[
\Lambda=\{\tau_1,\ldots,\tau_N\}\subset[-T,T].
\]

The map

\[
b\longmapsto
(\mathcal A_Tb(\tau_1),\ldots,\mathcal A_Tb(\tau_N))
\tag{22}
\]

has only finitely many real linear constraints on the infinite-dimensional space `C_c^infty((x,L))` (after separating real and imaginary parts). Its kernel therefore contains a nonzero smooth signed density. Since `h(t)>0` for `t>x`, every such nonzero density has

\[
V_h(b)>0.
\tag{23}
\]

Thus no finite `Lambda` can satisfy a positive lower bound by `V_h` on the unrestricted smooth signed class. The finite reduction in `(6)` is not a property of the Euler family alone; it is purchased by source compactness.

### Exact injectivity and stable finite certification remain different notions

A positive-width continuum band is exactly injective on `L^1` by AF-209. The finite norming set in `(6)` need not be injective on the ambient `L^1` space, and generally is not. It is only uniformly separating on the declared compactified normalized class.

Therefore one must record which source restriction was used. Replacing the compactified class by a larger one can instantly reintroduce finite-sample collisions even though the same continuum band remains exactly injective.

### The finite set is class-dependent

The compactness proof chooses `Lambda` from the image of the declared source class. There is no claim that one universal finite frequency set works simultaneously for all source-complexity budgets, all support intervals, all orders, or all profile scales.

As the admissible source class expands and its conditioning constant tends to zero, the required finite norming set can grow or cease to exist with a positive uniform modulus. This is the discrete version of the exact-versus-stable distinction in AF-209.

### AF-074 is an abstract ancestor, not a duplicate theorem

AF-074 already establishes that precompact finite witness pools can recover a compact-transversal fidelity margin by compactness selection. AF-210 uses the same broad compactness resource on the opposite side of the observation problem: once the **source-normalized image in `C(Theta)` is compact and avoids zero**, finitely many evaluation coordinates norm that entire profile family.

The mathematical compactness principle is therefore not new. What is new to the current Euler branch of Arithmetic Fidelity is the completed resource tradeoff left open by AF-209: the continuum vertical band can be discretized after a source-complexity gate, while finite sampling remains impossible on the unrestricted smooth source space.

## Prior art and novelty assessment

The general finite-norming mechanism is classical and elementary, and no novelty is claimed for `(2)`.

Approximation theory uses closely related terminology for finite **norming sets** and **admissible meshes**, where a supremum norm over a continuous domain is controlled by evaluations on a finite subset. Andras Kroo, “On optimal polynomial meshes,” *Journal of Approximation Theory* 163(9) (2011), 1107–1124, DOI `10.1016/j.jat.2011.03.007`, studies finite meshes that norm multivariate polynomial spaces with controlled cardinality. A. Brudnyi and Y. Yomdin, “Norming Sets and Related Remez-type Inequalities,” *Journal of the Australian Mathematical Society* 100(2) (2016), 163–181, DOI `10.1017/S1446788715000488`, study norming sets and norming constants for finite-dimensional spaces of continuous functions and related Remez inequalities.

Those theories ask substantially sharper questions about structured function spaces, mesh geometry, norming constants, or asymptotically efficient cardinality. AF-210 uses only the elementary compact-cover implication for one compact profile family and therefore should not be presented as a new norming-set theorem.

The durable Arithmetic Fidelity result is the specialization and boundary statement. AF-208 showed that compact support of the source is insufficient because the normalized source class is still noncompact in the relevant topology. AF-209 showed that genuine source precompactness restores continuum coercivity. AF-210 now shows that the same precompactness also collapses the required observation cardinality from a continuum to a finite set. Source complexity and observation complexity are therefore dual resources: enough compactness on the source side can make a finite observation certificate complete for stable fidelity on that declared class.

## Arithmetic Fidelity consequence

The line should no longer phrase the signed Euler question as “finite frequencies versus a continuum band” without declaring the admissible source complexity. The correct distinction is conditional:

\[
\boxed{
\begin{array}{ll}
\text{unrestricted infinite-dimensional signed sources:}
&\text{finite sampling has exact kernel directions;}\\[2mm]
\text{precompact normalized source class:}
&\text{continuum coercivity implies a finite norming sample set.}
\end{array}}
\tag{24}
\]

This is a reusable compression audit. When an analytic observation family is proposed as a discriminator carrier, asking only whether the full family is injective overstates the observation resource and understates the source assumptions. One should instead declare the source quotient/complexity class, establish a stable margin there, and then ask how much of the observation family is actually needed to norm the resulting compact profile set.

For eventual rational-prime applications, this is useful but not yet prime-specific. It gives no arithmetic discriminator and no RH implication. Its role is to prevent a false dichotomy: a continuum analytic transform may be mathematically convenient for proving injectivity, while the actual stable discriminator on a sufficiently rigid arithmetic source class may require only finitely many well-chosen observations.

## Consequence for the next research step

AF-210 makes the next quantitative question sharper. The existence of a finite norming set follows abstractly from compactness, but its size depends on the conditioning margin and profile regularity. A genuinely useful arithmetic application should therefore identify a **natural source-complexity budget with an effective coercivity constant**, then determine how the minimal required frequency count scales with that budget, support/localization, derivative order, and desired recovery error. Without an effective lower bound on `c_mathcal C`, the finite-set theorem is structural rather than computational.