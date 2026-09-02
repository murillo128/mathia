# AF-064 — Strongly convex Minkowski geometry has a universal quadratic safe-lift threshold

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `STRUCTURAL-CLASSIFICATION`, `CLASSICAL-MECHANISM`, `PRIOR-ART-BOUNDARY`

## Claim

Let `V` be a finite-dimensional real vector space equipped with a **reversible strongly convex Minkowski norm**

\[
F:V\to[0,\infty),
\]

meaning that `F(-v)=F(v)`, `F` is `C^2` on `V\setminus\{0\}`, positively homogeneous of degree one, and its fundamental tensor

\[
g_u(a,b)
=\frac12 D^2(F^2)(u)[a,b]
\tag{1}
\]

is positive definite for every `u\ne0`. Let

\[
d_F(x,y)=F(x-y).
\]

For a nonempty compact target `S\subset V`, put

\[
K=\operatorname{conv}(S),
\tag{2}
\]

and for `p\ge1` and `m\in V` define the powered far-field defect

\[
\Delta_{p,S}^F(m)
=
\sup_{x\in V}
\left(
 d_F(x,S)^p-F(x-m)^p
\right)
\in[0,+\infty].
\tag{3}
\]

Equivalently, in the AF-057 vertical product refinement with source metric `d_F` and product exponent `p`, finite vertical repair above `m` exists exactly when `\Delta_{p,S}^F(m)<\infty`.

Define

\[
B_p^F(S)
=\{m\in V:\Delta_{p,S}^F(m)<\infty\}.
\tag{4}
\]

Then the finite-lift base set has the same three-regime phase diagram as in the Euclidean AF-059 theorem:

\[
\boxed{
B_p^F(S)=
\begin{cases}
V, & p=1,\\[2mm]
K, & 1<p\le2,\\[2mm]
S\cup\operatorname{int}(K), & p>2.
\end{cases}
}
\tag{5}
\]

Here `int(K)` is ambient interior in `V`. In particular, if `K` is lower-dimensional, then `\operatorname{int}(K)=\varnothing` and every missing hull point fails every superquadratic powered lift.

More precisely:

1. **Exterior points fail every nonlinear power.** If `m\notin K`, then
   \[
   \Delta_{p,S}^F(m)=+\infty
   \qquad\forall p>1.
   \tag{6}
   \]
   This is the first-order horofunction obstruction of AF-063.

2. **Hull-interior points survive every finite power.** If `m\in\operatorname{int}(K)`, then
   \[
   \Delta_{p,S}^F(m)<\infty
   \qquad\forall p>1,
   \tag{7}
   \]
   again by AF-063.

3. **True target points survive trivially.** If `m\in S`, then
   \[
   \Delta_{p,S}^F(m)=0
   \qquad\forall p\ge1.
   \tag{8}
   \]

4. **Every hull point has at most inverse-linear positive distance excess.** If `m\in K\setminus S`, put `\delta=d_F(m,S)>0` and
   \[
   e_{S,m}^F(x)
   =
   \bigl(d_F(x,S)-F(x-m)\bigr)_+.
   \tag{9}
   \]
   There are constants `C,R<\infty` such that
   \[
   e_{S,m}^F(x)
   \le
   \frac{C}{F(x-m)}
   \qquad
   \text{whenever }F(x-m)\ge R.
   \tag{10}
   \]
   Therefore AF-062 gives
   \[
   \Delta_{p,S}^F(m)<\infty
   \qquad(1<p\le2).
   \tag{11}
   \]

5. **At every missing hull-boundary point the inverse-linear scale is sharp in one supporting direction.** If
   \[
   m\in\partial K\setminus S,
   \tag{12}
   \]
   then there are a unit vector `u`, constants `c>0` and `T<\infty`, and the ray
   \[
   x_t=m+t u
   \]
   such that
   \[
   d_F(x_t,S)-F(x_t-m)
   \ge
   \frac{c}{t}
   \qquad(t\ge T).
   \tag{13}
   \]
   Hence AF-062 gives
   \[
   \Delta_{p,S}^F(m)=+\infty
   \qquad(p>2).
   \tag{14}
   \]

Thus the reusable Arithmetic Fidelity conclusion is

\[
\boxed{
\begin{array}{c}
\text{once the admitted norm category has nondegenerate quadratic indicatrix curvature,}\\
\text{the first unresolved hull-boundary layer has universal order }t^{-1}\\
\text{and therefore universal powered threshold }p=2.
\end{array}
}
\tag{15}
\]

The `p=2` transition found in Euclidean AF-059 is therefore **not specifically Euclidean**. AF-061's `\ell^r` thresholds differ because the relevant axis directions fall outside the present nondegenerate `C^2` curvature class: for `r>2` the quadratic tangential curvature degenerates there, while for `1<r<2` the norm is not `C^2` there. The exponent change is therefore a contact-order/curvature-degeneracy phenomenon rather than evidence for a privileged Euclidean representation.

## Derivation

### Strong convexity supplies the exact quadratic tangential term

Fix a unit vector `u`, so `F(u)=1`, and write

\[
\varphi_u=DF(u),
\qquad
H_u=D^2F(u).
\tag{16}
\]

Differentiating `F^2` gives

\[
g_u
=
\varphi_u\otimes\varphi_u+H_u.
\tag{17}
\]

Euler homogeneity gives

\[
\varphi_u(u)=1,
\qquad
H_u(u,\cdot)=0.
\tag{18}
\]

Therefore, on the tangent hyperplane

\[
T_u=\ker\varphi_u,
\tag{19}
\]

one has

\[
H_u(v,v)=g_u(v,v)>0
\qquad(v\in T_u\setminus\{0\}).
\tag{20}
\]

This is the exact structural assumption absent from the degenerate `\ell^r` axis controls of AF-061.

Because the unit sphere is compact and `F` is `C^2` away from `0`, Taylor expansion is uniform for unit `u` and bounded `v`: for every fixed bounded set `Q\subset V`,

\[
F(tu-v)
=
 t-\varphi_u(v)
 +\frac{1}{2t}H_u(v,v)
 +o_Q(t^{-1})
\tag{21}
\]

as `t\to\infty`, with the remainder uniform for `F(u)=1` and `v\in Q`.

Only the upper `O(t^{-1})` control needs `C^2` compactness. The positive lower coefficient at a missing boundary point additionally uses strong convexity through (20).

### Every hull point has global `O(t^{-1})` positive excess

Let `m\in K\setminus S` and put

\[
Q=S-m.
\]

For any unit `u`, since `m\in\operatorname{conv}(S)`,

\[
\max_{s\in S}\varphi_u(s-m)\ge0.
\tag{22}
\]

Choose `s_u\in S` attaining the maximum and write `v_u=s_u-m`. Compactness of `S` gives a uniform bound on `v_u`. Applying the uniform second-order Taylor estimate to this selected point gives, for all sufficiently large `t`,

\[
\begin{aligned}
d_F(m+tu,S)
&\le F(tu-v_u)\\
&\le t-\varphi_u(v_u)+\frac{C_0}{t}\\
&\le t+\frac{C_0}{t},
\end{aligned}
\tag{23}
\]

with `C_0` independent of `u`.

Every `x\ne m` can be written uniquely as

\[
x=m+t u,
\qquad
F(u)=1,
\qquad
t=F(x-m).
\]

Hence (23) proves the far-field bound

\[
e_{S,m}^F(x)\le\frac{C_0}{F(x-m)}
\tag{24}
\]

outside a large ball. On the remaining compact ball the positive excess is bounded. Since `\delta=d_F(m,S)>0`, this is equivalent after enlarging the constant to

\[
e_{S,m}^F(x)
\le
C\bigl(F(x-m)+\delta\bigr)^{-1}
\qquad\forall x.
\tag{25}
\]

AF-062 with `\rho=2` now gives

\[
\Delta_{p,S}^F(m)<\infty
\qquad(1<p\le2).
\tag{26}
\]

Together with the trivial target-point case, every `m\in K` is therefore finitely liftable through the quadratic power.

### A missing boundary point has a uniform positive quadratic coefficient

Now suppose

\[
m\in\partial K\setminus S.
\tag{27}
\]

Choose a supporting dual functional `\varphi` with

\[
\|\varphi\|_*=1,
\qquad
\varphi(s-m)\le0
\quad\forall s\in S.
\tag{28}
\]

Finite-dimensional dual-norm attainment gives a unit vector `u` with `\varphi(u)=1`. Smoothness of `F` makes the norming functional at `u` unique, so

\[
DF(u)=\varphi.
\tag{29}
\]

Define the exposed target slice

\[
S_0
=\{s\in S:\varphi(s-m)=0\}.
\tag{30}
\]

It is nonempty: since `m\in\operatorname{conv}(S)` and `\varphi` attains its support value at `m`, every convex representation of `m` can use positive weight only on support-level points. It is compact. Since `m\notin S`, every

\[
v=s-m,
\qquad s\in S_0,
\]

is nonzero, and by (28) lies in `\ker\varphi`. Strong convexity and (20) therefore give

\[
q_0
:=
\min_{s\in S_0} H_u(s-m,s-m)
>0.
\tag{31}
\]

By compactness and continuity there exists `\eta>0` such that

\[
-\varphi(s-m)\le\eta
\Longrightarrow
H_u(s-m,s-m)\ge\frac{q_0}{2}
\tag{32}
\]

for all `s\in S`. On the complementary compact subset one has the fixed first-order gap

\[
-\varphi(s-m)\ge\eta.
\tag{33}
\]

Use the uniform Taylor expansion (21), now with the fixed direction `u`. For the near-face set (32), equations (28) and (32) give, for all sufficiently large `t`,

\[
F(tu-(s-m))
\ge
 t+rac{q_0}{8t}.
\tag{34}
\]

For the complement (33), the positive first-order term is stronger:

\[
F(tu-(s-m))
\ge
 t+\frac{\eta}{2}
\ge
 t+\frac{q_1}{t}
\tag{35}
\]

for a suitable `q_1>0` and all sufficiently large `t`. Taking the infimum over `s\in S`, there are `c>0` and `T<\infty` such that

\[
d_F(m+tu,S)
\ge
 t+\frac{c}{t}
\qquad(t\ge T).
\tag{36}
\]

Because

\[
F((m+tu)-m)=t,
\]

this is exactly (13).

AF-062's lower-rate criterion with `\rho=2` now yields

\[
\Delta_{p,S}^F(m)=+\infty
\qquad(p>2).
\tag{37}
\]

Thus every missing hull-boundary point is finite at and below the quadratic power and infinite above it.

### The remaining branches are already first-order or trivial

AF-063 applies because a strongly convex Minkowski norm is smooth and strictly convex. It gives:

- if `m\notin K`, some horofunction direction has a positive limiting distance gap, so AF-062 forces `\Delta_p=+\infty` for every `p>1`;
- if `m\in\operatorname{int}(K)`, every horofunction gap is uniformly negative, so the defect is nonpositive outside a compact set and every finite power is bounded.

If `m\in S`, point-to-set distance satisfies

\[
d_F(x,S)\le F(x-m),
\]

so `\Delta_p=0` for every `p`. Finally the general metric identity from AF-057 gives

\[
\Delta_{1,S}^F(m)=d_F(m,S)
\tag{38}
\]

for all `m\in V`. Combining these facts with (26) and (37) proves the complete phase diagram (5).

## Exact controls

### Euclidean AF-059 is recovered as one member of the category

For a Euclidean norm, `g_u` is the ambient inner product and the tangential Hessian in (20) is nondegenerate. Formula (5) therefore reproduces AF-059 exactly at the level of finite-lift existence. The old Euclidean computation was not wrong; it had not yet separated Euclidean coordinates from the genuinely load-bearing second-order curvature hypothesis.

### The `\ell^r` family explains exactly how the quadratic theorem can fail

For

\[
F_r(x,y)=(|x|^r+|y|^r)^{1/r},
\qquad1<r<\infty,
\]

AF-061 found the symmetric two-point boundary threshold `p=r`.

At the relevant vertical direction `(0,1)`:

- if `r>2`, `F_r` is `C^2` there but its tangential second derivative in the horizontal direction is zero, so the fundamental tensor is degenerate and strong convexity in the Finsler/Minkowski sense fails at that direction;
- if `1<r<2`, the required second derivative in the horizontal direction is singular/not `C^2`, so the present regularity hypothesis fails;
- at `r=2`, the tangential quadratic form is nondegenerate and the threshold is exactly `2`.

Thus AF-061 is not a counterexample to (5). It is the sharp matched control showing that once the quadratic contact order degenerates, the powered threshold is free to move.

### Same convex hull remains invisible through `p=2` but not above it

Let compact sets `S_1,S_2` have the same convex hull `K`. For `1<p\le2`, (5) gives

\[
B_p^F(S_1)=B_p^F(S_2)=K.
\tag{39}
\]

For `p>2`,

\[
B_p^F(S_i)\cap\partial K
=S_i\cap\partial K.
\tag{40}
\]

So the strongly convex category has the same exact information transition identified in AF-059: subquadratic/quadratic existence retains only convex-hull membership, while superquadratic existence recovers original target provenance on the hull boundary.

### Near-isometric perturbations still show why the category declaration matters

AF-061 exhibits norms arbitrarily bi-Lipschitz close to Euclidean for which the fixed-base `p=2` truth value changes. Those perturbations approach the quadratic category through norms whose relevant second-order curvature loses the uniform nondegeneracy required here. Therefore (5) is not a statement that small metric distortion preserves exact fidelity. It is a category theorem: **nondegenerate quadratic indicatrix curvature**, not mere bi-Lipschitz closeness, is the invariant that fixes the threshold.

## Prior art and novelty assessment

The differential-geometric and convex-analytic ingredients are classical, and no novelty is claimed for Minkowski/Finsler norms, fundamental tensors, strong convexity of indicatrices, support hyperplanes, dual norm attainment, Taylor expansion, or compactness arguments.

- Min Ji and Zhongmin Shen, **“On Strongly Convex Indicatrices in Minkowski Geometry,”** *Canadian Mathematical Bulletin* 45(2), 232–246 (2002), DOI `10.4153/CMB-2002-027-4`. Role: direct classical Minkowski-geometry background for strongly convex indicatrices and their induced differential geometry.
- The standard Finsler/Minkowski definition used here is the familiar one in which `F` is smooth away from zero and the fundamental tensor `g_u=(1/2)D^2(F^2)(u)` is positive definite. This is exactly the nondegenerate quadratic hypothesis used in (20); reversibility is added here so that `d_F(x,y)=F(x-y)` is a genuine metric compatible with AF-062.
- Jürgen Kampf, **“Asymptotic Order of the Parallel Volume Difference in Minkowski Spaces,”** *Journal of Convex Analysis* 21(4), 925–950 (2014). Role: important neighboring prior art showing that asymptotic loss between a nonconvex body and its convex hull in Minkowski spaces has established, norm-dependent order phenomena; the paper studies parallel-volume differences rather than the pointwise powered defect (3).
- Jürgen Kampf and Markus Kiderlen, **“Large Parallel Volumes of Finite and Compact Sets in d-Dimensional Euclidean Space,”** *Documenta Mathematica* 18 (2013), 275–295. Role: neighboring Euclidean prior art for large-radius asymptotics of compact sets versus their convex hulls and for higher-order geometric information surviving beyond convexification.

A targeted search across strongly convex Minkowski norms, far-field distance asymptotics, parallel-volume differences, convex-hull asymptotics, and coapproximation did not locate the exact phase diagram (5) or the pointwise `t^{-1}` boundary criterion (13) as a standard named theorem. That absence is not evidence of novelty. The durable contribution claimed here is narrower: within the already-defined AF-057/AF-062 safe-lift observable, the proof identifies the precise representation category in which AF-059's quadratic threshold becomes invariant and explains AF-061's moving exponent as failure of that category's second-order hypothesis.

## Boundaries and failure modes

- The theorem is finite-dimensional. Compactness of the unit sphere is used to make the second-order upper estimate uniform in direction. No infinite-dimensional Banach-space analogue is claimed.
- Reversibility is used so that `F(x-y)` is a metric and AF-062 applies directly. A nonreversible Finsler/Minkowski analogue would require an asymmetric-distance version of the earlier metric results.
- `C^2` regularity away from zero is essential for the uniform quadratic expansion. Strong convexity is essential only for the positive lower coefficient at missing boundary points; weaker smooth norms may still have `O(t^{-1})` upper excess while failing the matching lower bound.
- The theorem classifies **finiteness** of the powered defect, not its exact finite value for `1<p\le2`. AF-056's exact Euclidean quadratic roof does not automatically extend in the same form to arbitrary Minkowski norms.
- Nothing here says that `p=2` is intrinsically preferred across all normed representations. It is invariant only after the admitted representation category fixes nondegenerate quadratic tangential curvature.
- The `\ell^r` controls show that higher or lower contact order changes the boundary exponent once the hypotheses fail. A broader theorem should therefore classify the critical power from the first nonvanishing tangential contact order or an equivalent modulus-of-smoothness/curvature invariant rather than assume quadraticity.
- The theorem concerns the AF-057 powered safe-lift compression. It does not by itself imply that another spectral, probabilistic, arithmetic, or operator compression has the same fidelity threshold.
