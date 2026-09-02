# AF-059 — Euclidean powered safe-lift finiteness has a three-regime convex-hull phase diagram

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `STRUCTURAL-CLASSIFICATION`, `CLASSICAL-MECHANISM`, `PRIOR-ART-BOUNDARY`

## Claim

Let `S\subset\mathbb R^d` be nonempty and compact, let

\[
K=\operatorname{conv}(S),
\]

and for `p\ge1` and `m\in\mathbb R^d` define the AF-057 powered far-field defect

\[
\Delta_{p,S}(m)
=
\sup_{x\in\mathbb R^d}
\left(
\operatorname{dist}(x,S)^p-\|x-m\|_2^p
\right)
\in[0,+\infty].
\tag{1}
\]

Equivalently, in the product refinement

\[
Y_p=\mathbb R^d\times N,
\qquad
D_p((x,u),(x',u'))
=
\left(\|x-x'\|_2^p+\|u-u'\|^p\right)^{1/p},
\tag{2}
\]

with nonzero normed vertical space `N` and source embedding `C_p(x)=(x,0)`, AF-057 gives

\[
(m,v)\in\mathcal E_{C_p}(S)
\iff
\|v\|^p\ge\Delta_{p,S}(m).
\tag{3}
\]

Define the **finite-lift base set**

\[
B_p(S)=\{m\in\mathbb R^d:\Delta_{p,S}(m)<\infty\}.
\tag{4}
\]

Then the base set is classified exactly by the exponent:

\[
\boxed{
B_p(S)=
\begin{cases}
\mathbb R^d, & p=1,\\[2mm]
\operatorname{conv}(S), & 1<p\le2,\\[2mm]
S\cup\operatorname{int}(\operatorname{conv}(S)), & p>2.
\end{cases}
}
\tag{5}
\]

Here `int` is ordinary ambient Euclidean interior. Thus, if `K` is lower-dimensional, `\operatorname{int}(K)=\varnothing` and for every `p>2`

\[
B_p(S)=S.
\tag{6}
\]

More precisely:

1. **The linear product is universally repairable.** AF-057 already gives
   \[
   \boxed{
   \Delta_{1,S}(m)=\operatorname{dist}(m,S)
   }
   \tag{7}
   \]
   for every metric source, hence `B_1(S)=\mathbb R^d`.

2. **Every subquadratic or quadratic powered product remembers exactly the convex hull at the level of finite-lift existence.** For `1<p\le2`,
   \[
   \boxed{
   \Delta_{p,S}(m)<\infty
   \iff
   m\in K.
   }
   \tag{8}
   \]
   If `m\in K`, AF-056's quadratic variance roof `V_S(m)=\Delta_{2,S}(m)` gives the quantitative bounds
   \[
   \boxed{
   \operatorname{dist}(m,S)^p
   \le
   \Delta_{p,S}(m)
   \le
   V_S(m)^{p/2}.
   }
   \tag{9}
   \]
   At `p=2` the upper bound is equality.

3. **Superquadratic products distinguish missing boundary points from genuine target points.** For `p>2`, every point of `S` has zero defect,
   \[
   \Delta_{p,S}(m)=0
   \qquad(m\in S),
   \tag{10}
   \]
   every point in `\operatorname{int}(K)` has finite defect, but every
   \[
   m\in\partial K\setminus S
   \]
   has
   \[
   \boxed{
   \Delta_{p,S}(m)=+\infty.
   }
   \tag{11}
   \]
   Points outside `K` also have infinite defect for every `p>1`.

4. **The exponent therefore controls which target provenance survives the finite-lift compression.** For `1<p\le2`, replacing `S` by any compact set with the same convex hull leaves `B_p(S)` unchanged. For `p>2`, the hull interior is still filled in, but on the hull boundary one has the exact identity
   \[
   \boxed{
   B_p(S)\cap\partial K=S\cap\partial K.
   }
   \tag{12}
   \]
   Superquadratic finite-lift existence retains original target membership on the exposed boundary even though it forgets target holes in the hull interior.

5. **There are two genuine phase changes.** At `p=1`, finite-lift existence forgets the convex hull completely and becomes universal. Immediately above `1`, exterior points become impossible and the base set contracts to `K`. At `p=2`, the second transition occurs: for `p>2`, convexification ceases to be sufficient at boundary points that were not already in `S`.

The reusable Arithmetic Fidelity conclusion is

\[
\boxed{
\text{the same target }S\text{ passed through the same product-lift construction}
\text{ can retain none, only convex-hull, or boundary-membership information,}
\text{ solely according to the power law used by the ambient metric.}
}
\tag{13}
\]

This turns the AF-057 two-point threshold and AF-058 far-field instability into a complete Euclidean compact-target classification of **which structural information survives the finite-lift existence observable**.

## Derivation

### `p=1`: universal finiteness

AF-057 proved in every metric source that the distance-to-set map is `1`-Lipschitz and therefore

\[
\sup_x
\left(
\operatorname{dist}(x,S)-d(x,m)
\right)
=
\operatorname{dist}(m,S).
\tag{14}
\]

In Euclidean space this is exactly (7), so every base point admits a finite vertical repair.

### Every point outside the convex hull has infinite defect for `p>1`

Let `p>1` and suppose `m\notin K`. Since `K` is compact and convex, strict separation gives a unit vector `u` and `a>0` such that

\[
\langle u,s-m\rangle\le-a
\qquad\forall s\in S.
\tag{15}
\]

Along the ray

\[
x_t=m+t u,
\qquad t>0,
\tag{16}
\]

one has for every `s\in S`

\[
\begin{aligned}
\|x_t-s\|_2^2
&=
 t^2-2t\langle u,s-m\rangle+\|s-m\|_2^2\\
&\ge
 t^2+2at.
\end{aligned}
\tag{17}
\]

Hence

\[
\operatorname{dist}(x_t,S)^p-\|x_t-m\|_2^p
\ge
(t^2+2at)^{p/2}-t^p.
\tag{18}
\]

The right-hand side is asymptotic to

\[
p a\,t^{p-1},
\tag{19}
\]

which tends to `+\infty` because `p>1`. Therefore

\[
m\notin K
\Longrightarrow
\Delta_{p,S}(m)=+\infty
\qquad(p>1).
\tag{20}
\]

This proves the necessary convex-hull condition throughout both non-linear regimes.

### `1<p\le2`: the quadratic roof controls every lower power

Now let `m\in K`. AF-056 identifies the quadratic defect with the finite barycentric variance roof

\[
V_S(m)=\Delta_{2,S}(m)<\infty.
\tag{21}
\]

Thus for every `x`, writing `r=\|x-m\|_2`,

\[
\operatorname{dist}(x,S)^2
\le
r^2+V_S(m).
\tag{22}
\]

For `1<p\le2`, the exponent `q=p/2` lies in `(0,1]`, and `t\mapsto t^q` is subadditive on `\mathbb R_+`. Therefore

\[
\begin{aligned}
\operatorname{dist}(x,S)^p-r^p
&\le
(r^2+V_S(m))^{p/2}-r^p\\
&\le
V_S(m)^{p/2}.
\end{aligned}
\tag{23}
\]

Taking the supremum proves the upper bound in (9), hence finiteness throughout `K`. Evaluating (1) at `x=m` gives

\[
\Delta_{p,S}(m)
\ge
\operatorname{dist}(m,S)^p,
\tag{24}
\]

which proves the lower bound. Combined with (20), this proves (8).

At `p=2`, AF-056 gives the sharper exact identity `\Delta_{2,S}=V_S`, including its convex-roof and Delaunay descriptions.

### `p>2`: genuine target points remain safe

If `m\in S`, then for every `x`

\[
\operatorname{dist}(x,S)
\le
\|x-m\|_2.
\tag{25}
\]

Thus every term in (1) is nonpositive, while at `x=m` it is zero. Consequently

\[
\Delta_{p,S}(m)=0
\tag{26}
\]

for every `p\ge1`. This proves the `S` part of the superquadratic finite region.

### `p>2`: hull-interior points have finite defect

Let `m\in\operatorname{int}(K)`. Choose `\rho>0` such that

\[
\overline B(m,\rho)\subset K,
\tag{27}
\]

and put

\[
R=\max_{s\in S}\|s-m\|_2<\infty.
\tag{28}
\]

For each unit vector `u`, linearity and `K=\operatorname{conv}(S)` give

\[
\max_{s\in S}\langle u,s-m\rangle
=
\max_{k\in K}\langle u,k-m\rangle
\ge\rho.
\tag{29}
\]

Choose `s_u\in S` attaining the maximum. For `x=m+t u`,

\[
\begin{aligned}
\operatorname{dist}(x,S)^2
&\le
\|m+t u-s_u\|_2^2\\
&=
 t^2-2t\langle u,s_u-m\rangle+\|s_u-m\|_2^2\\
&\le
 t^2-2\rho t+R^2.
\end{aligned}
\tag{30}
\]

Hence the defect on the sphere of radius `t` is bounded above by

\[
q_p(t)
=
(t^2-2\rho t+R^2)^{p/2}-t^p.
\tag{31}
\]

As `t\to\infty`,

\[
q_p(t)
=
-p\rho\,t^{p-1}+O(t^{p-2}),
\tag{32}
\]

so `q_p(t)\to-\infty`. Therefore there is `T<\infty` such that the defect is nonpositive whenever `\|x-m\|\ge T`.

On the closed ball `\overline B(m,T)`, the function

\[
x\mapsto\operatorname{dist}(x,S)^p-\|x-m\|^p
\tag{33}
\]

is continuous, hence bounded above. The global supremum is therefore finite. This proves

\[
\operatorname{int}(K)\subseteq B_p(S)
\qquad(p>2).
\tag{34}
\]

### `p>2`: every missing hull-boundary point diverges at second order

Let now

\[
m\in\partial K\setminus S.
\tag{35}
\]

Compactness of `S` gives a positive target gap

\[
\delta=\operatorname{dist}(m,S)>0.
\tag{36}
\]

By the supporting-hyperplane theorem, there is a unit vector `u` such that

\[
\langle u,s-m\rangle\le0
\qquad\forall s\in S.
\tag{37}
\]

Along the outward ray `x_t=m+t u`, every `s\in S` satisfies

\[
\begin{aligned}
\|x_t-s\|_2^2
&=
 t^2-2t\langle u,s-m\rangle+\|s-m\|_2^2\\
&\ge
 t^2+\delta^2.
\end{aligned}
\tag{38}
\]

Thus

\[
\operatorname{dist}(x_t,S)^p-t^p
\ge
(t^2+\delta^2)^{p/2}-t^p.
\tag{39}
\]

For `p>2`, the right-hand side is asymptotic to

\[
\frac p2\delta^2 t^{p-2},
\tag{40}
\]

which diverges to `+\infty`. Therefore every missing boundary point has infinite powered far-field defect. Together with (20), (26), and (34), this proves the superquadratic line of (5).

The proof also explains the critical exponent. Exterior separation produces a **first-order** distance advantage and therefore diverges for every `p>1`. At a hull boundary point the first-order support term can vanish; what remains is the fixed positive **second-order** squared-distance gap `\delta^2`. Raising the Euclidean distance to power `p` amplifies that term like `t^{p-2}`, so it is bounded at or below `p=2` and divergent above `p=2`.

## Exact controls

### AF-057's two-point example becomes the lower-dimensional case of the classification

Take

\[
S_a=\{(-a,0),(a,0)\}\subset\mathbb R^2.
\tag{41}
\]

Its convex hull is a line segment and therefore has empty ambient interior. Formula (5) gives, for every `p>2`,

\[
B_p(S_a)=S_a.
\tag{42}
\]

In particular the midpoint has no finite lift, exactly recovering AF-057. For `1<p\le2`, the entire segment is finitely liftable. The special calculation in AF-057 is therefore the simplest instance of the general ambient-interior/boundary dichotomy.

### A full-dimensional triangle separates interior from missing boundary

Let

\[
S=\{(-1,0),(1,0),(0,1)\}\subset\mathbb R^2.
\tag{43}
\]

For every `p>2`, any point in the open triangle has finite defect. But the midpoint `m=(0,0)` of the lower edge is not in `S`, and along `x_t=(0,-t)` one has for large `t`

\[
\operatorname{dist}(x_t,S)^2=t^2+1.
\tag{44}
\]

Hence

\[
\operatorname{dist}(x_t,S)^p-t^p
=(t^2+1)^{p/2}-t^p
\to+\infty.
\tag{45}
\]

So the superquadratic failure is not an artifact of a lower-dimensional hull.

### Same convex hull, different superquadratic finite-lift observable

Let `K` be a compact full-dimensional polytope. Compare

\[
S_1=\operatorname{vert}(K)
\qquad\text{and}\qquad
S_2=K.
\tag{46}
\]

They have exactly the same convex hull. For `1<p\le2`,

\[
B_p(S_1)=B_p(S_2)=K.
\tag{47}
\]

For `p>2`, however,

\[
B_p(S_1)=\operatorname{int}(K)\cup\operatorname{vert}(K),
\qquad
B_p(S_2)=K.
\tag{48}
\]

Thus the superquadratic observable retains whether a boundary point was genuinely present in the original target, while the quadratic/subquadratic observable sees only the common convex hull at the level of existence.

### Finite truncations again hide every divergent case

For every fixed radius `R_0`, the defect function is continuous on

\[
\{x:\|x-m\|\le R_0\},
\]

so its supremum there is finite regardless of the location of `m`. Exterior and superquadratic boundary failures are purely far-field statements. Numerical enlargement of a bounded search region can therefore keep returning finite repair heights without certifying a global safe lift.

## Prior art and novelty assessment

The proof mechanisms are classical, and no novelty is claimed for convex separation, support functions, distance-to-set continuity, best coapproximation, or `\ell^p`-dependent approximation geometry.

- Rolf Schneider, ***Convex Bodies: The Brunn–Minkowski Theory***, 2nd expanded ed., Encyclopedia of Mathematics and its Applications 151, Cambridge University Press (2014; online 2013), DOI `10.1017/CBO9781139003858`. Role: standard convex-geometry source for compact convex hulls, support and separation, supporting hyperplanes, support functions, boundary structure, and ambient interior used in (15), (27)--(29), and (37).
- R. Tyrrell Rockafellar, ***Convex Analysis***, Princeton University Press (1970). Role: classical finite-dimensional convex-analysis background for separation/supporting-hyperplane arguments and the convex-roof machinery already used in AF-056.
- T. D. Narang and S. P. Singh, **“Best Coapproximation in Metric Linear Spaces,”** *Tamkang Journal of Mathematics* 30(4), 241--252 (1999), DOI `10.5556/j.tkjm.30.1999.4198`. Role: established metric-linear-space coapproximation framework surrounding AF-054--AF-058; confirms that existence of coapproximation-type points is inherently geometry-dependent rather than an Arithmetic Fidelity invention.
- U. Westphal, **“Cosuns in `l_p(n)`, `1\le p<\infty`,”** *Journal of Approximation Theory* 54 (1988), 287--305. Role: direct classical precedent that coapproximation/cosun geometry varies with the `p`-norm; it is the closest established approximation-theoretic boundary for interpreting the exponent sensitivity.

A targeted search across best coapproximation/cosuns, powered distance-to-set functions, support-function asymptotics, and convex-hull distance geometry found mature theories for all ingredients above. It did not locate this exact set-valued trichotomy (5) stated for the AF-057 product safe-envelope defect, but that absence is **not** used as a claim that (5) is a new theorem of convex or approximation geometry. The durable result is the exact Arithmetic Fidelity classification and its information-loss interpretation: the finite-lift observable moves from universal forgetting, to convex-hull quotienting, to partial recovery of boundary target provenance as the exponent crosses `1` and `2`.

## Boundaries and failure modes

- Compactness of `S` is essential to the stated proof. It supplies attainment/boundedness, a positive gap `\operatorname{dist}(m,S)` when `m\notin S`, and compact convex-hull separation. Extensions to noncompact or merely closed targets require separate coercivity hypotheses.
- `\operatorname{int}(K)` is ambient interior in `\mathbb R^d`, not relative interior. This distinction is decisive: a lower-dimensional hull has no ambient interior, and an orthogonal far-field ray creates the superquadratic obstruction at every missing hull point.
- The result classifies **finiteness** of the repair threshold, not its exact value except at `p=1`, `p=2` through AF-056, and target points where it is zero. Interior superquadratic thresholds remain quantitative objects.
- Formula (5) is specific to Euclidean source distance together with the powered `\ell^p` product construction of AF-057. Other source norms, nonlinear refinements, weighted products, bounded sources, or non-product metrics can move or remove the critical exponents.
- The distinction in (12) is about target membership on `\partial K`; it does not imply that the full target `S` is recoverable from `B_p(S)`. All holes inside `\operatorname{int}(K)` are filled in for every `p>2`.
- Finite-lift existence is only one observable derived from the safe envelope. A finite lift need not be canonical, natural, stable under representation change, or arithmetically meaningful. AF-058 already shows that exact existence may have zero robustness margin under near-isometric renorming.
- Nothing in this result singles out rational primes or proves an RH mechanism. Its role is to classify one abstract survival law before any arithmetic specialization.

## Consequence for the Arithmetic Fidelity frontier

AF-057 showed a sharp `p=2` threshold for one two-point target, and AF-058 showed that the corresponding existence property can flip under arbitrarily small global renorming because the Hilbert safe points have zero far-field margin. The present result identifies the geometry behind that behavior for **every compact Euclidean target**.

The new reusable object is the set-valued compression

\[
S\longmapsto B_p(S).
\tag{49}
\]

Its information content is now explicit: `p=1` forgets all target geometry at the level of existence; `1<p\le2` keeps exactly the convex hull; `p>2` keeps the hull interior together with exact original target membership on its boundary. This is a concrete instance of the line's central question — which structural properties survive a compression — where the answer changes sharply with the transformation category.

A productive next gate is therefore not another product-norm example. It is to ask whether analogous **survival strata** can be classified for broader compression families: identify a natural filtration of source structure (for example exact membership, convex hull, exposed faces, support data, or higher-order boundary jets) and prove which layer a declared transformation retains. Any arithmetic application should then specify which prime discriminator lives on which retained stratum rather than merely showing that some safe lift exists.