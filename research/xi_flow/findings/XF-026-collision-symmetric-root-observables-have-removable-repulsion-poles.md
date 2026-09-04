# XF-026 — collision-symmetric root observables have removable logarithmic-repulsion poles

**Status:** `EXACT-DERIVED` + `CLASSICAL-IDENTITY` + `STRUCTURAL/BOUNDARY`. XF-021--XF-025 repeatedly found positive `1/epsilon` spikes when a mean-removing functional is written on ordered gaps with a fixed edge, taper, stencil, or index-space convolution. Those no-go results leave an important question: is the pole intrinsic to logarithmic repulsion, or to the regularity class of the observable being differentiated?

There is an exact separation. Let `F` be a `C^2` observable of finitely many real root coordinates and suppose it extends across a collision wall `x_j=x_{j+1}` with invariance under exchanging those two roots. For the zero-motion law

\[
x_i'=2\sum_{k\ne i}'\frac1{x_i-x_k},
\]

the singular contribution of the pair `(j,j+1)` is

\[
\boxed{
2\frac{\partial_jF-\partial_{j+1}F}{x_j-x_{j+1}}.
}
\]

Permutation symmetry forces the numerator to vanish on the collision wall, and `C^2` regularity makes it `O(x_j-x_{j+1})`. Hence the apparent pole is removable. If

\[
x_j=s-\frac\epsilon2,
\qquad
x_{j+1}=s+\frac\epsilon2,
\]

then

\[
\boxed{
2\frac{\partial_jF-\partial_{j+1}F}{x_j-x_{j+1}}
\longrightarrow
2\bigl(\partial_{jj}F-\partial_{j,j+1}F\bigr)_{x_j=x_{j+1}=s}.
}
\]

For an ordered-gap functional `G(g)` with gap-gradient `q_i=partial G/partial g_i`, the same pair contribution is exactly

\[
\boxed{
\frac{2}{\epsilon}(Aq)_j,
\qquad
(Aq)_j:=2q_j-q_{j-1}-q_{j+1}.
}
\]

Thus the collision coefficients exposed separately in XF-021--XF-025 are one object: they measure failure of the observable's first derivative to satisfy the reflection-smooth collision-wall condition. A `C^2` permutation-symmetric root observable automatically has `(Aq)_j=O(\epsilon)` when represented in gap coordinates, so it cannot have an uncancelled `1/epsilon` pole at an isolated two-root collision.

This does **not** give a Lyapunov function or an upper bound for `Lambda`. It gives a sharper design boundary. Fixed ordered-index mean removal fails because it is not smooth under root exchange at the collision wall. A surviving adaptive construction should therefore be sought among physical-coordinate, permutation-symmetric observables (or among deliberately singular collision barriers), rather than by further tuning a fixed gap-index boundary.

## 1. The singular pair term in root coordinates

Work on a real-simple slice where the Rodgers--Tao zero-motion law used in XF-014 is valid. Fix two adjacent roots `x_j<x_{j+1}` and write

\[
\epsilon:=x_{j+1}-x_j>0.
\tag{1}
\]

Assume the collision is isolated in the local calculation: all other roots stay a fixed positive distance from the pair while `epsilon` tends to zero. For the infinite Xi system this means only that we are isolating the coefficient of the adjacent pole; principal-value background terms are treated exactly as in XF-014. The same calculation is literal in the finite polynomial matched controls of XF-006.

Let `F=F(x_1,\ldots,x_n)` be `C^1` on the chamber under consideration. Differentiating along the root flow and grouping the two ordered contributions from a pair gives

\[
\begin{aligned}
F'
&=2\sum_i\partial_iF\sum_{k\ne i}\frac1{x_i-x_k}\\
&=2\sum_{i<k}
\frac{\partial_iF-\partial_kF}{x_i-x_k}.
\end{aligned}
\tag{2}
\]

For the potentially colliding pair,

\[
\boxed{
\mathcal P_j(F)
:=2\frac{\partial_jF-\partial_{j+1}F}{x_j-x_{j+1}}
=\frac{2}{\epsilon}
(\partial_{j+1}F-\partial_jF).
}
\tag{3}
\]

Every other pair involving only one of `x_j,x_{j+1}` has a denominator bounded away from zero under the isolated-collision hypothesis. Therefore an uncancelled `1/epsilon` spike can only come from (3).

Equation (3) already gives the exact necessary first-order condition for a removable adjacent pole:

\[
\boxed{
\partial_{j+1}F-\partial_jF=O(\epsilon).
}
\tag{4}
\]

If the gradient has a continuous limit on the collision wall, finite pair drift in particular requires

\[
\partial_jF=\partial_{j+1}F
\qquad\text{when }x_j=x_{j+1}.
\tag{5}
\]

## 2. Root-exchange symmetry enforces the collision-wall condition

Suppose now that `F` extends as a `C^2` function to a neighborhood of the wall and is invariant under the transposition exchanging the two colliding coordinates,

\[
F(\ldots,x_j,x_{j+1},\ldots)
=F(\ldots,x_{j+1},x_j,\ldots).
\tag{6}
\]

Introduce center/separation coordinates

\[
s=\frac{x_j+x_{j+1}}2,
\qquad
\delta=x_{j+1}-x_j.
\tag{7}
\]

With all remaining coordinates held fixed, define

\[
\widetilde F(s,\delta)
:=F(\ldots,s-\delta/2,s+\delta/2,\ldots).
\tag{8}
\]

Symmetry (6) is exactly

\[
\widetilde F(s,\delta)=\widetilde F(s,-\delta).
\tag{9}
\]

Hence `partial_delta \widetilde F(s,0)=0`, while

\[
\partial_\delta\widetilde F
=\frac12(\partial_{j+1}F-\partial_jF).
\tag{10}
\]

Because `F` is `C^2`, Taylor expansion of the first derivative gives

\[
\partial_{j+1}F-\partial_jF
=2\delta\,\partial_{\delta\delta}\widetilde F(s,0)+o(\delta).
\tag{11}
\]

Substituting into (3),

\[
\boxed{
\mathcal P_j(F)
\longrightarrow
4\,\partial_{\delta\delta}\widetilde F(s,0).
}
\tag{12}
\]

At the diagonal, exchange symmetry also gives

\[
\partial_{jj}F=\partial_{j+1,j+1}F,
\]

and direct differentiation of (8) yields

\[
4\partial_{\delta\delta}\widetilde F
=2(\partial_{jj}F-\partial_{j,j+1}F).
\tag{13}
\]

Thus

\[
\boxed{
\lim_{\epsilon\downarrow0}\mathcal P_j(F)
=2(\partial_{jj}F-\partial_{j,j+1}F)_{x_j=x_{j+1}}.
}
\tag{14}
\]

The logarithmic-repulsion vector field is singular in labelled root coordinates, but its action on a smooth observable satisfying the reflection symmetry of the collision wall is finite. For a simultaneous finite cluster collision, the same argument applies pair by pair whenever `F` is `C^2` and symmetric under permutations of the colliding coordinates.

## 3. Gap coordinates expose the same condition as a discrete Laplacian of the gradient

The preceding root-coordinate criterion exactly unifies the collision coefficients found in the recent gap-energy no-go sequence. Let

\[
g_i=x_{i+1}-x_i
\tag{15}
\]

and let `F(x)=G(g)` on an ordered chamber. Write

\[
q_i:=\frac{\partial G}{\partial g_i}.
\tag{16}
\]

Only `g_{j-1}` and `g_j` depend on `x_j`, while only `g_j` and `g_{j+1}` depend on `x_{j+1}`. Therefore

\[
\partial_jF=q_{j-1}-q_j,
\qquad
\partial_{j+1}F=q_j-q_{j+1}.
\tag{17}
\]

Subtracting,

\[
\boxed{
\partial_{j+1}F-\partial_jF
=2q_j-q_{j-1}-q_{j+1}
=(Aq)_j.
}
\tag{18}
\]

Together with (3),

\[
\boxed{
\mathcal P_j(F)=\frac{2}{\epsilon}(Aq)_j.
}
\tag{19}
\]

This is not merely analogous to XF-022. If `G` is quadratic with `q=Lg`, then (19) is exactly the `2(ALg)_j/epsilon` collision law used there and sharpened in XF-025. For the weighted variance of XF-023, `q_i=alpha_i(g_i-mu_alpha)`, and the taper-curvature coefficient is the same `(Aq)_j` after expansion. For XF-024, a collapsing gap just outside the support has `q_j=q_{j+1}=0`, so (19) becomes

\[
-\frac{2}{\epsilon}q_{j-1},
\]

which is precisely its edge-derivative law.

Consequently the recent no-go results can be read geometrically:

\[
\boxed{
\text{uncancelled collision pole}
\iff
\text{nonzero normal gradient mismatch at a root-exchange wall}.
}
\tag{20}
\]

For a `C^2` symmetric extension, (11) and (18) instead give

\[
\boxed{
(Aq)_j=O(g_j)
\qquad(g_j\downarrow0),
}
\tag{21}
\]

which removes the pole automatically.

## 4. What this says about adaptive localization

XF-023 and XF-025 leave configuration-dependent coefficients outside their no-go classes. Equation (20) says what such adaptivity must accomplish if it is to cure the adjacent singularity. It is not enough for weights merely to depend on the current gaps or observation scale. Their derivative contributions must make the **whole observable** reflection-smooth across `x_j=x_{j+1}`, equivalently enforce (4) or (21).

A natural way to obtain that property is to stop assigning special meaning to a fixed ordered root label near the localization boundary. For example, finite sums built with the same smooth physical-coordinate kernel for every root,

\[
F(x)=\sum_i f(x_i)
+\sum_{i<k}K(x_i,x_k),
\tag{22}
\]

are permutation symmetric whenever `K(u,v)=K(v,u)`. If `f` and `K` are `C^2` through `u=v`, the pair singularity is removable by the theorem above. Smooth physical windows can be incorporated into `f` or `K` without selecting a permanent index-space edge.

This does not mean that (22) already measures the desired local gap fluctuation or removes the neutral spacing mode. It identifies a structurally different search class in which the collision pole is not present before the mean-removal problem is addressed. By contrast, a hard block of consecutive ordered gaps, a fixed index taper, or a fixed convolution stencil distinguishes labels on the two sides of the collision wall and therefore need not satisfy (5).

There is a second legitimate escape: deliberately use a **singular** collision barrier, such as a logarithmic discriminant-type observable. Such a function does not satisfy the `C^2` hypothesis and may have a controlled divergent derivative of its own. XF-026 does not classify those barriers; it separates them from smooth symmetric observables.

## 5. Matched-control and Xi boundary

The cancellation is universal for logarithmic repulsion and therefore cannot by itself select the Xi flow. In a finite real-rooted polynomial control, the root ODE is an ordinary finite sum, and equations (2)--(14) show exactly that every isolated collision pole disappears on a smooth symmetric root observable. This supplies the line's required matched control without any infinite-sum issue.

For Xi, the result is used only on the real-simple side of a hypothetical collision. The Rodgers--Tao principal-value law remains the source of the root velocities, and XF-014 remains the source-faithful gap reformulation. The theorem does not continue labelled real roots through a time where the Xi zeros cease to be real and simple. It only identifies which observable singularities are intrinsic as that wall is approached.

Nor does boundedness of the pair contribution imply monotonicity. The finite limit in (14) may have either sign, and the remaining interactions with remote roots may dominate. A successful upper-bound mechanism still needs a coercive/sign structure plus source-valid control of the infinite-system tails.

## 6. Prior art and novelty boundary

The removal of reflection-hyperplane singularities on symmetric observables is classical in the broad Weyl-chamber, Dyson, radial-Laplacian, and Calogero/Dunkl landscape. A targeted prior-art check found the expected theory of noncolliding particles in Weyl chambers and radial operators with singular inverse-distance drift. No novelty is claimed for that general principle.

No external theorem is load-bearing here. Equations (2)--(14) are a direct two-coordinate calculation from the zero-motion law already anchored in `SOURCES.md`, and equations (17)--(19) are an elementary chain-rule conversion to Xi gap coordinates. Accordingly no new source anchor is required.

The durable contribution for this line is the **identification of the XF-021--XF-025 collision coefficients with the failure of reflection smoothness of the underlying root observable**. This converts a list of negative examples into a positive design criterion: the next mean-removal candidate should be tested first for a smooth permutation-symmetric extension across collision walls.

## 7. Consequence for `xi_flow`

The broad-buffer program should not interpret XF-021--XF-025 as saying that every localized observable must inherit an adjacent `1/epsilon` catastrophe. The catastrophe is unavoidable for the fixed ordered-gap classes proved there, but it is absent from the singular pair drift whenever the final observable is `C^2` and root-exchange symmetric.

This shifts the next constructive target. Starting from the collision-safe cross-ratio carrier of XF-018--XF-020, search for a **physical-coordinate, permutation-symmetric mean-removal or signed-flux observable** whose localization is smooth under root exchange and whose remote terms can still be controlled by the super-mesoscopic counting buffer of XF-020. Any candidate that reintroduces a fixed ordered-index edge should first be rejected by the wall test `(Aq)_j=O(g_j)` before more elaborate estimates are attempted.