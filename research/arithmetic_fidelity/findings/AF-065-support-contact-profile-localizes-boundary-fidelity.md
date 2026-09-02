# AF-065 — Support-contact profiles localize hull-boundary fidelity beyond global smoothness

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `STRUCTURAL-CLASSIFICATION`, `CLASSICAL-MECHANISM`, `PRIOR-ART-BOUNDARY`

## Claim

Let `(V,\|\cdot\|)` be a finite-dimensional real normed space, let `S\subset V` be nonempty and compact, put

\[
K=\operatorname{conv}(S),
\]

and fix `m\in K`. Write

\[
Q=S-m,
\qquad
D=\max_{v\in Q}\|v\|.
\tag{1}
\]

For a unit vector `u`, let

\[
J(u)=\{\varphi\in V^*: \|\varphi\|_*=1,\ \varphi(u)=1\}
\tag{2}
\]

be its set of norming functionals. For `\varphi\in J(u)` define the **support remainder**

\[
R_{u,\varphi}(w)
=
\|u+w\|-1-\varphi(w).
\tag{3}
\]

The supporting-hyperplane inequality gives `R_{u,\varphi}(w)\ge0` for every `w`.

Then:

1. **Every far-field ray has an exact support/remainder decomposition.** For every `t>0`,
   \[
   \boxed{
   d(m+t u,S)-t
   =
   \inf_{v\in Q}
   \left[
   -\varphi(v)
   +tR_{u,\varphi}(-v/t)
   \right].
   }
   \tag{4}
   \]
   The first term is the support slack already detected by AF-063's convex-hull/horofunction layer. The second is the higher-order deviation of the norm sphere from its supporting hyperplane.

2. **At a hull-boundary support direction, the unresolved higher-order layer is an exact target-coupled contact profile.** Suppose `m\in\partial K` and `\varphi\in J(u)` supports `K` at `m`, so
   \[
   \varphi(v)\le0
   \qquad\forall v\in Q.
   \tag{5}
   \]
   Define
   \[
   \kappa_{S,m}^{u,\varphi}(\varepsilon)
   =
   \inf_{v\in Q}
   \left[
   R_{u,\varphi}(-\varepsilon v)
   -\varepsilon\varphi(v)
   \right]
   \qquad(\varepsilon>0).
   \tag{6}
   \]
   Then `\kappa\ge0` and
   \[
   \boxed{
   d(m+t u,S)-t
   =
   t\,\kappa_{S,m}^{u,\varphi}(1/t).
   }
   \tag{7}
   \]
   Thus the first-order tie `\Gamma_S(m)=0` from AF-063 is not an undifferentiated residual. It has an exact next object: the infimal supporting-hyperplane contact of the norm against the exposed target geometry.

3. **The contact order is the exact critical exponent for that ray.** Assume for some `r>1` and `c\in(0,\infty)` that
   \[
   \kappa_{S,m}^{u,\varphi}(\varepsilon)
   \sim
   c\varepsilon^r
   \qquad(\varepsilon\downarrow0).
   \tag{8}
   \]
   Then along `x_t=m+t u`,
   \[
   d(x_t,S)-d(x_t,m)
   \sim
   c\,t^{1-r},
   \tag{9}
   \]
   and for every `p>1`,
   \[
   d(x_t,S)^p-d(x_t,m)^p
   \sim
   pc\,t^{p-r}.
   \tag{10}
   \]
   Consequently this ray contributes a vanishing powered defect for `p<r`, an order-one limiting defect for `p=r`, and an unbounded obstruction for every `p>r`. In particular,
   \[
   p>r
   \Longrightarrow
   \Delta_{p,S}(m)=+\infty.
   \tag{11}
   \]
   This is the local contact version of AF-062's weighted-distance-excess criterion.

4. **The ordinary modulus of smoothness gives a uniform sufficient fidelity exponent.** Let
   \[
   \rho_V(\tau)
   =
   \sup_{\|x\|=\|y\|=1}
   \left(
   \frac{\|x+\tau y\|+\|x-\tau y\|}{2}-1
   \right)
   \tag{12}
   \]
   be the classical modulus of smoothness. For every unit `u`, every `\varphi\in J(u)`, and every `w\in V`,
   \[
   \boxed{
   0\le R_{u,\varphi}(w)
   \le
   2\rho_V(\|w\|).
   }
   \tag{13}
   \]
   Therefore every `m\in K` satisfies the uniform far-field estimate
   \[
   \boxed{
   \bigl(d(m+t u,S)-t\bigr)_+
   \le
   2t\rho_V(D/t)
   }
   \tag{14}
   \]
   for every unit direction `u` and every `t>0`.

   If for some `q>1`, `C<\infty`, and sufficiently small `\tau`,
   \[
   \rho_V(\tau)\le C\tau^q,
   \tag{15}
   \]
   then AF-062 gives
   \[
   \boxed{
   \Delta_{p,S}(m)<\infty
   \qquad
   \forall m\in K,
   \quad
   1<p\le q.
   }
   \tag{16}
   \]
   Thus a power-type smoothness bound supplies a category-wide **safe exponent floor** for every compact target and every point of its convex hull.

5. **Global smoothness does not determine the sharp hull-boundary exponent.** For the two-point `\ell^r` control of AF-061 with `r>2`,
   \[
   S_a=\{(-a,0),(a,0)\},
   \qquad m=0,
   \qquad u=(0,1),
   \tag{17}
   \]
   and the norming functional `\varphi(x,y)=y`, formula (6) is exact:
   \[
   \boxed{
   \kappa_{S_a,0}^{u,\varphi}(\varepsilon)
   =
   \left(1+a^r\varepsilon^r\right)^{1/r}-1
   \sim
   \frac{a^r}{r}\varepsilon^r.
   }
   \tag{18}
   \]
   Hence the local contact exponent and the exact AF-061 powered threshold are both `r`.

   On the other hand the global modulus of smoothness of finite-dimensional `\ell^r`, `r>2`, has quadratic power type. In particular `\ell^4` and `\ell^6` both have global smoothness exponent `2`, while their same two-point boundary thresholds are respectively `4` and `6`. Therefore no theorem that retains only the global power type of `\rho_V` can recover the sharp fixed-target exponent.

The reusable Arithmetic Fidelity conclusion is

\[
\boxed{
\begin{array}{c}
\text{first-order hull fidelity is controlled by support slack;}\\
\text{after that slack vanishes, powered fidelity is controlled by local supporting contact;}\\
\text{global smoothness gives a uniform safe bound but can erase the sharp directional exponent.}
\end{array}
}
\tag{19}
\]

This gives a coordinate-free completion of the AF-061--AF-064 sequence. The moving `\ell^r` threshold and the universal quadratic strongly-convex threshold are two contact-order regimes of the same exact variational object rather than unrelated norm-specific calculations.

## Derivation

### Exact support/remainder identity

Fix `u` with `\|u\|=1`, choose `\varphi\in J(u)`, and write `v=s-m`. Positive homogeneity gives

\[
\begin{aligned}
\|m+t u-s\|
&=\|t u-v\|\\
&=t\|u-v/t\|\\
&=t-\varphi(v)+tR_{u,\varphi}(-v/t).
\end{aligned}
\tag{20}
\]

Taking the infimum over `s\in S` proves (4).

If `\varphi` supports `K` at `m`, then (5) holds. Multiplying the bracket in (4) by `1/t` and setting `\varepsilon=1/t` gives

\[
\frac{d(m+t u,S)-t}{t}
=
\inf_{v\in Q}
\left[
R_{u,\varphi}(-\varepsilon v)
-\varepsilon\varphi(v)
\right],
\tag{21}
\]

which is exactly (6)--(7). Both terms inside the infimum are then nonnegative: the first by support of the norm ball, the second by support of the target hull.

This isolates two logically different losses. If `-\varphi(v)` stays uniformly positive at the minimizer, the first-order horofunction layer already decides the ray. Only when the target can approach the support face `\varphi(v)=0` can higher-order norm contact become decisive.

### Contact order gives the ray threshold

Under (8), equation (7) gives

\[
g(t)
:=d(m+t u,S)-t
\sim c t^{1-r}.
\tag{22}
\]

Because `r>1`, one has `g(t)/t\to0`. Hence

\[
\begin{aligned}
d(m+t u,S)^p-t^p
&=t^p\left[\left(1+\frac{g(t)}{t}\right)^p-1\right]\\
&\sim pt^{p-1}g(t)\\
&\sim pc\,t^{p-r},
\end{aligned}
\tag{23}
\]

which proves (10)--(11). This calculation is only directional: another ray may still impose a stricter global threshold. A sharp global phase diagram requires both a uniform upper contact bound over all escape directions and at least one matching lower-contact direction.

### Modulus of smoothness bounds every support remainder

The lower inequality in (13) is the norming-functional inequality

\[
\|u+w\|\ge\varphi(u+w)=1+\varphi(w).
\tag{24}
\]

For the upper inequality, the same support functional gives

\[
\|u-w\|\ge1-\varphi(w).
\tag{25}
\]

By the definition of `\rho_V`, with `\tau=\|w\|`,

\[
\|u+w\|+\|u-w\|
\le
2+2\rho_V(\|w\|).
\tag{26}
\]

Combining (25)--(26),

\[
\|u+w\|-1-\varphi(w)
\le
2\rho_V(\|w\|),
\tag{27}
\]

proving (13).

Now use `m\in K`. Since `0\in\operatorname{conv}(Q)`, for every `\varphi` one has

\[
M_\varphi
:=\max_{v\in Q}\varphi(v)
\ge0.
\tag{28}
\]

Choose `v_\varphi\in Q` attaining that maximum. Formula (4), followed by (13), gives

\[
\begin{aligned}
d(m+t u,S)-t
&\le
-M_\varphi+tR_{u,\varphi}(-v_\varphi/t)\\
&\le
2t\rho_V(\|v_\varphi\|/t)\\
&\le
2t\rho_V(D/t),
\end{aligned}
\tag{29}
\]

which proves (14). No differentiability or strict convexity is needed for this estimate.

Under (15), for sufficiently large `t`,

\[
\bigl(d(m+t u,S)-t\bigr)_+
\le
2CD^q t^{1-q}
\tag{30}
\]

uniformly in `u`. Every `x\ne m` has the form `m+t u` with `\|u\|=1`, so (30) is a global far-field bound for AF-062's positive distance excess. On the remaining bounded region that excess is bounded. AF-062 therefore yields (16). If `m\in S`, the stronger identity `\Delta_{p,S}(m)=0` is already immediate.

### The `\ell^r` target exposes local contact hidden by the global modulus

For (17), the support functional at `u=(0,1)` is `\varphi(x,y)=y`, and both target vectors `v=(\pm a,0)` lie exactly in its tangent hyperplane. Thus the support-slack term vanishes identically on `Q`. For either target point,

\[
R_{u,\varphi}(-\varepsilon v)
=
\left(1+a^r\varepsilon^r\right)^{1/r}-1,
\tag{31}
\]

which proves (18). The binomial expansion gives its leading coefficient `a^r/r`.

For completeness, the global smoothness exponent is nevertheless quadratic when `r>2`. An upper `O(\tau^2)` bound follows directly because the `\ell^r` norm is `C^2` on the compact unit sphere and the symmetric first-order terms in

\[
\|x+\tau y\|+\|x-\tau y\|-2
\]

cancel uniformly. A matching quadratic lower bound is obtained at

\[
x=2^{-1/r}(1,1),
\qquad
y=2^{-1/r}(1,-1),
\tag{32}
\]

where both vectors have unit norm and

\[
\|x+\tau y\|_r^r
=
\frac{(1+\tau)^r+(1-\tau)^r}{2}
=
1+\frac{r(r-1)}{2}\tau^2+O(\tau^4).
\tag{33}
\]

Hence

\[
\|x+\tau y\|_r
=
1+\frac{r-1}{2}\tau^2+O(\tau^4),
\tag{34}
\]

and the same value occurs for `x-\tau y`. Therefore `\rho_{\ell^r}(\tau)\asymp\tau^2` while the target-coupled contact profile (18) has order `r`. This is the exact mismatch claimed in item 5.

## Exact controls

### Euclidean two-point geometry is the quadratic contact member

At `r=2`, equation (18) becomes

\[
\kappa(\varepsilon)
=
\sqrt{1+a^2\varepsilon^2}-1
\sim
\frac{a^2}{2}\varepsilon^2.
\tag{35}
\]

Equation (10) therefore reproduces the AF-057/AF-059 critical power `2` without expanding the powered defect first. The exponent comes from tangential contact with the support hyperplane.

### Strongly convex Minkowski geometry recovers AF-064

Under AF-064's reversible `C^2` strongly convex Minkowski hypotheses, the tangential support remainder has a nondegenerate quadratic term on every exposed target vector at a missing hull-boundary point. AF-064 proved both the uniform `O(t^{-1})` upper distance excess and a matching `c/t` lower ray. In the present language this is precisely a uniform quadratic contact regime:

\[
\kappa(\varepsilon)\asymp\varepsilon^2
\tag{36}
\]

on the decisive support direction. Thus AF-064's universal threshold is the nondegenerate quadratic special case of (7)--(10).

### Equal global smoothness power does not imply equal target fidelity

Take `r=4` and `r=6` with the same coordinate target `S_a` and midpoint. Both spaces satisfy

\[
\rho(\tau)\asymp\tau^2,
\tag{37}
\]

but (18) gives local contact orders `4` and `6`. AF-061 therefore gives different exact safe-lift thresholds despite the same global smoothness power type. This is a matched control against replacing the local contact profile by one scalar Banach-space smoothness exponent.

### Interior and exterior points remain first-order cases

The new profile is needed only where AF-063 leaves a first-order tie. If `m\notin K`, a separating support direction has a positive first-order gap and every nonlinear power already fails. If `m\in\operatorname{int}K`, every horofunction direction has a uniformly negative first-order gap and every finite power is safe. The contact profile is therefore genuinely a **boundary refinement**, not a replacement for the convex-hull classification.

## Prior art and novelty assessment

The geometric ingredients around (12)--(13) are classical Banach-space geometry. No novelty is claimed for norming functionals, Birkhoff-James/support orthogonality, moduli of smoothness, power-type smoothness, or local deviation of a norm sphere from a supporting hyperplane.

- Grigory M. Ivanov, **“Modulus of Supporting Convexity and Supporting Smoothness,”** *Eurasian Mathematical Journal* 6(1), 26--40 (2015), arXiv:`1503.08912`. Role: direct prior art for measuring the deviation of the unit sphere from arbitrary supporting hyperplanes; the paper proves equivalence at zero between supporting smoothness and the ordinary modulus of smoothness, and similarly relates supporting convexity to the modulus of convexity.
- Stanisław Prus and Mariusz Szczepanik, **“On Local Milman's Moduli,”** *Journal of Convex Analysis* 17(1), 1--11 (2010). Role: explicit prior art for localized smoothness moduli and for the distinction between global Banach-space moduli and point/local geometry.
- James A. Clarkson, **“Uniformly convex spaces,”** *Transactions of the American Mathematical Society* 40(3), 396--414 (1936), and Olof Hanner, **“On the uniform convexity of `L^p` and `\ell^p`,”** *Arkiv för Matematik* 3, 239--244 (1956). Role: classical `L^p/\ell^p` geometry underlying the standard power-type convexity/smoothness behavior used as the matched control.

These sources make clear that **support-contact moduli themselves are established mathematics**. The contribution claimed here is narrower and internal to Arithmetic Fidelity: equation (4) identifies the exact target-coupled support remainder hidden inside the AF-057 powered safe-lift observable; equations (7)--(10) translate its local contact order into a directional fidelity threshold; and the `\ell^4/\ell^6` control proves that the global modulus power type is only a sufficient category-level bound, not the sharp target-specific invariant.

A targeted literature search across supporting smoothness, local Banach moduli, Birkhoff-James/support geometry, and `\ell^p` moduli found mature theories for the norm-side contact terms. It did not justify treating the target-infimal profile (6) or its AF-057 safe-lift interpretation as a new general Banach-space theory, and no such claim is made. The durable result is the exact bridge and the resulting falsification rule for this research line.

## Boundaries and failure modes

- Equation (4) is exact for any normed space and compact target for which the displayed infima make sense, but the finding keeps the finite-dimensional setting used by AF-059--AF-064. No infinite-dimensional compactness conclusions are claimed.
- The modulus-of-smoothness estimate (14) is a **sufficient uniform upper bound**. It need not be sharp for a particular target, base point, or support direction.
- The asymptotic contact law (8) classifies only the declared ray. It yields a global impossibility for `p>r`, but global finiteness at `p\le r` still requires uniform control over every direction. Equation (16) supplies such a control only up to the global smoothness power `q`.
- The profile (6) depends jointly on the norm, the base point, the support direction, and the target geometry. It is therefore not an invariant of the ambient norm alone. This dependence is the point: target fidelity can see local contact that a global Banach-space scalar forgets.
- If the target approaches the exposed support face through a continuum, the infimum in (6) can mix support slack and curvature/contact at varying points. One must analyze that full infimal profile rather than inspect one arbitrarily selected exposed point.
- Nonsmooth or polyhedral norms may have several norming functionals and first-order corners. The exact identity remains valid for each chosen `\varphi\in J(u)`, but a single differentiable curvature tensor is no longer an adequate descriptor.
- Nothing here privileges the powered product refinement as an arithmetic mechanism, and nothing distinguishes rational primes. The result remains an abstract fidelity classification as required by the line mandate.

## Consequence for the Arithmetic Fidelity frontier

AF-064 ended with the open requirement to replace its nondegenerate quadratic hypothesis by the first nonvanishing tangential contact order or an equivalent modulus. The present finding supplies that replacement at the exact level needed by AF-057: the target-coupled support profile `\kappa` is the local object whose decay order controls the ray, while the classical modulus of smoothness supplies a uniform category-level upper envelope.

This also sharpens what a representation-invariance theorem would have to preserve. Bi-Lipschitz equivalence, common topology, or even a common global smoothness power type is insufficient. To preserve the sharp hull-boundary fidelity threshold, an admitted representation class must control the relevant **local support-contact profiles against the target's exposed geometry**, or prove a stronger structural theorem forcing those profiles into one common asymptotic class.