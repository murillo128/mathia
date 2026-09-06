# PF-188 — fixed-germ marked collar strain is qualitatively Sobolev-rigid without boundary normalization

**Status:** `LITERATURE+DERIVED + EXACT-QUALITATIVE + POSITIVE/BOUNDARY-REMOVAL`. PF-187 proved uniform qualitative `W^{1,r}` rigidity only after the short-collar relative germ had been normalized to a boundary-preserving self-diffeomorphism of the fixed slab. The boundary-to-boundary hypothesis is not actually needed for the qualitative branch-selection step. Kupferman--Maor--Shachar already give an **isometric immersion** as the limit of maps with vanishing Riemannian strain. On a fixed positive-side collar germ, every reflection-marked orientation-preserving isometric immersion of the inner slab into a slightly larger slab is the canonical inclusion. Thus qualitative marked Sobolev rigidity survives without boundary normalization, uniformly through the cusp limit `L=0`, provided the images remain in one fixed larger annular germ away from `x=0`.

This removes boundary normalization as an intrinsic prerequisite for the qualitative low-regularity route. It does **not** give the energy-linear estimate required by PF-183, does not prove that the raw canonical germ is uniformly confined to the fixed larger slab, and does not construct the exact-symplectic cutoff. The fixed-germ condition is genuine: at the cusp limit, if the target is allowed to run arbitrarily deeper toward `x=0`, exact local isometries `(x,theta)->(x/k,k theta+c)` provide higher-winding escape branches.

## Claim

Put

\[
A=[1,5/4]\times\mathbb R/\mathbb Z,
\qquad
B=[3/4,3/2]\times\mathbb R/\mathbb Z,
\tag{1}
\]

and, for `0<=L<=mu_*`, equip both annuli with

\[
g_L=\frac{dx^2}{L^2+x^2}+(L^2+x^2)d\theta^2.
\tag{2}
\]

Let

\[
R(x,\theta)=(x,-\theta),
\quad
\Gamma_0^A=A\cap\{\theta=0\},
\quad
\Gamma_0^B=B\cap\{\theta=0\}.
\tag{3}
\]

Fix `1<r<infinity`. For a smooth map

\[
H:(A,g_L)\longrightarrow(B,g_{L'})
\tag{4}
\]

define

\[
\mathcal D_r^B(H;L,L')
:=
\left(
\int_A
\operatorname{dist}^r
\!\left(
 dH,
 SO(g_L,H^*g_{L'})
\right)
\,d\mu_{g_L}
\right)^{1/r}.
\tag{5}
\]

Choose a fixed smooth Euclidean embedding of `B` and use the induced equivalent `W^{1,r}` distance for maps `A->B`. Then for every `epsilon_0>0` there is

\[
\delta=\delta(r,\epsilon_0,\mu_*)>0
\tag{6}
\]

such that for all `L,L' in [0,mu_*]`, if

\[
|L-L'|+\mathcal D_r^B(H;L,L')<\delta,
\tag{7}
\]

and

\[
HR=RH,
\qquad
H(\Gamma_0^A)\subset\Gamma_0^B,
\tag{8}
\]

then

\[
\boxed{
 d_{W^{1,r}}(H,\iota_A)<\epsilon_0,
}
\tag{9}
\]

where `iota_A:A->B` is the canonical inclusion `(x,theta)->(x,theta)`.

The constants `3/4` and `3/2` are not special. What matters is one fixed nested positive-side pair `A compactly contained in B`, with the lower target radius strictly greater than `(5/4)/2=5/8`; this last inequality excludes the first nontrivial cusp winding branch in the limiting immersion classification below.

Equation (9) is again a **qualitative compactness modulus**, not the linear estimate

\[
d_{W^{1,r}}(H,\iota_A)
\le C_r\bigl(\mathcal D_r^B(H;L,L')+|L-L'|\bigr).
\tag{10}
\]

No such quantitative conclusion is claimed here.

## 1. Reshetnyak gives an immersion; boundary normalization was only used to upgrade it

Assume (9) fails. Then there are `epsilon_0>0`, parameters

\[
L_j,L_j'\in[0,\mu_*],
\tag{11}
\]

and maps `H_j:A->B` satisfying (8) such that

\[
|L_j-L_j'|+\mathcal D_r^B(H_j;L_j,L_j')\to0,
\qquad
 d_{W^{1,r}}(H_j,\iota_A)\ge\epsilon_0.
\tag{12}
\]

After a subsequence,

\[
L_j\to L_\infty,
\qquad
L_j'\to L_\infty.
\tag{13}
\]

On the fixed compact annuli `A` and `B`, the metrics `g_L` form a smooth uniformly equivalent family for `0<=L<=mu_*`; in particular `x` stays uniformly away from the singular coordinate `x=0`. The same varying-metric reduction used in PF-187 therefore gives

\[
\left\|
\operatorname{dist}\!\left(
 dH_j,
 SO(g_{L_\infty},H_j^*g_{L_\infty})
\right)
\right\|_{L^r(A,g_{L_\infty})}
\to0.
\tag{14}
\]

Kupferman--Maor--Shachar's Riemannian Reshetnyak theorem applies directly to the compact manifolds with `C^1` boundary

\[
(A,g_{L_\infty}),
\qquad
(B,g_{L_\infty}).
\tag{15}
\]

Its basic conclusion does **not** require `H_j(partial A) subset partial B`: after a further subsequence,

\[
H_j\to\Phi
\quad\text{strongly in }W^{1,r}(A;B),
\tag{16}
\]

where

\[
\Phi:(A,g_{L_\infty})\longrightarrow(B,g_{L_\infty})
\tag{17}
\]

is a smooth orientation-preserving isometric immersion. The boundary-to-boundary and equal-volume assumptions in that theorem are needed only for the additional conclusion that the limit is a global isometry of the whole target. PF-187 used that stronger conclusion because its target was `A` itself. Here it suffices to classify the immersions (17).

## 2. Positive-length collar immersions cannot change the winding

Suppose first that

\[
L:=L_\infty>0.
\tag{18}
\]

With

\[
x=L\sinh\rho,
\tag{19}
\]

the metric becomes

\[
g_L=d\rho^2+L^2\cosh^2\rho\,d\theta^2.
\tag{20}
\]

This is the Fermi-coordinate form of the hyperbolic cylinder whose deck generator `gamma_L` is the hyperbolic translation of length `L` along the core axis. Both `A` and `B` lie strictly on the positive side `rho>0`.

Lift the local isometry `Phi` to the corresponding strips in `H^2`. A local orientation-preserving isometry of a connected hyperbolic domain agrees with the restriction of the unique global orientation-preserving hyperbolic isometry determined by one point and one oriented orthonormal frame. Call that global isometry `J`.

Because `Phi` descends to annuli, for some nonzero integer `k`,

\[
J\gamma_LJ^{-1}=\gamma_L^k.
\tag{21}
\]

Conjugacy preserves hyperbolic translation length, so

\[
L=|k|L,
\tag{22}
\]

and hence `|k|=1`. The branch `k=-1` reverses the orientation of the core axis and necessarily exchanges the two sides of that axis; it cannot map the positive source strip into the positive target strip `B`. Therefore `k=1`.

Thus `J` lies in the orientation-preserving centralizer of `gamma_L`, namely translations along the same axis. On the quotient,

\[
\boxed{
\Phi(x,\theta)=(x,\theta+c)
}
\tag{23}
\]

for some `c in R/Z`.

## 3. The cusp limit has extra winding immersions, and the fixed germ excludes them

Now let

\[
L=L_\infty=0.
\tag{24}
\]

Set `y=1/x`. Then

\[
g_0=\frac{dy^2+d\theta^2}{y^2},
\tag{25}
\]

so the universal cover is the upper half-plane and the annulus is a cusp quotient by the parabolic deck map

\[
P:z\longmapsto z+1,
\qquad z=\theta+iy.
\tag{26}
\]

As above, a lift of `Phi` is the restriction of a global `J in PSL(2,R)`, and descent gives

\[
JPJ^{-1}=P^k
\tag{27}
\]

for a nonzero integer `k`. Both sides fix infinity, so `J` fixes infinity and has the form

\[
J(z)=kz+c,
\qquad k>0.
\tag{28}
\]

In `(x,theta)` coordinates the resulting cusp immersion is

\[
\Phi(x,\theta)=\left(\frac{x}{k},k\theta+c\right).
\tag{29}
\]

This identifies the precise new phenomenon at `L=0`: unlike hyperbolic translations of positive length, parabolic powers are conjugate, so higher-winding local isometries really do exist.

But (29) must map all of `A` into `B`. If `k>=2`, then

\[
\frac{x}{k}\le\frac{5/4}{2}=\frac58<\frac34,
\tag{30}
\]

contradicting the lower radial bound of `B`. Hence `k=1`, and once again

\[
\boxed{
\Phi(x,\theta)=(x,\theta+c).
}
\tag{31}
\]

The fixed larger germ is therefore exactly what prevents a cusp winding escape without imposing any artificial boundary-to-boundary normalization.

## 4. Reflection and the ordered marking select the canonical inclusion

For either `L>0` or `L=0`, every possible limiting immersion has the form `T_c(x,theta)=(x,theta+c)`. Passing `H_jR=RH_j` to the strong `W^{1,r}` limit gives

\[
T_cR=RT_c,
\tag{32}
\]

hence

\[
2c=0\pmod1.
\tag{33}
\]

Only `c=0` and `c=1/2` remain.

The marked-axis condition in (8) is a codimension-one trace condition. Since `r>1`, the Sobolev trace from the two-dimensional slab to the smooth interior segment `Gamma_0^A` is continuous; strong `W^{1,r}` convergence therefore passes the condition to `Phi`. The half-turn sends the `theta=0` fixed component to `theta=1/2`, so the PF-142 ordered marking excludes it. Consequently

\[
\boxed{\Phi=\iota_A.}
\tag{34}
\]

Equation (16) then contradicts the second part of (12), proving (9). The compactness of `L in [0,mu_*]` makes the modulus uniform through the cusp limit.

## 5. What this changes in the PF-183 splice gate

PF-187 left **controlled boundary normalization** as an apparent prerequisite before one could even use qualitative Sobolev rigidity. PF-188 shows that this prerequisite was an artifact of asking Reshetnyak for a global annulus self-isometry. For the actual local splice problem it is enough to work on nested slabs and accept the theorem's natural isometric-immersion limit.

Accordingly, a canonical prime/shift relative germ does not need to be pushed to a boundary-preserving self-map merely to select the marked Sobolev branch. The weaker geometric input is that the restriction of the germ to the PF-183 inner slab takes values in one fixed slightly larger positive-side annulus. Once that **fixed-germ confinement** is available and its local strain tends to zero, (9) forces qualitative `W^{1,r}` convergence to the inclusion.

This is useful but still does not close the sharp Schatten clue. PF-183 requires a collar-by-collar estimate charged linearly to

\[
E_r^{\mathrm{body}}(T_\eta)+|t_\eta|^r.
\tag{35}
\]

PF-188 supplies no rate at all. It also does not turn a merely Sobolev-small exact symplectic map into the energy-linear exact-area cutoff required by PF-183, and PF-186 still forbids the generic implication from small strain to fixed `C^1` chart entry.

The remaining low-regularity route is therefore narrower:

1. establish fixed-germ confinement for the actual canonical PF-179--PF-184 relative maps, or another source-specific condition excluding cusp winding/drift;
2. prove the **linear** marked Sobolev rigidity/localization estimate on the nested slab, uniformly in `0<=L<=mu_*`;
3. perform the exact-symplectic cutoff with the same energy-linear cost.

Alternatively, source-specific regularity of the canonical maps could combine qualitative `W^{1,r}` convergence with derivative equicontinuity to force PF-185's fixed `C^1` chart entry. PF-186 shows that such derivative control must come from the canonical construction, not from metric strain, exactness, flux, and reflection alone.

## Prior art and novelty assessment

The imported compactness theorem is exactly the same authoritative prior art audited in PF-187:

- Raz Kupferman, Cy Maor, and Asaf Shachar, *Reshetnyak Rigidity for Riemannian Manifolds*, Archive for Rational Mechanics and Analysis 231 (2019), 367--408, DOI `10.1007/s00205-018-1282-9`, arXiv:1701.08892. Their Theorem 1.4 explicitly allows compact oriented manifolds with `C^1` boundary and gives strong `W^{1,p}` convergence to a smooth isometric immersion from vanishing differential distance to the orientation-preserving fiber isometries. Boundary-to-boundary plus equal volume are additional hypotheses only for upgrading that immersion to an isometry of the whole target.

The hyperbolic-cylinder and cusp-quotient calculations above are classical local-isometry/deck-transformation facts. No novelty is claimed for Reshetnyak compactness, developing-map extension of local hyperbolic isometries, centralizer/conjugacy classification in `PSL(2,R)`, or the existence of cusp power immersions.

A targeted audit of the nearby quantitative rigidity literature did not locate a theorem that supplies the still-missing **uniform linear** annulus-with-boundary estimate together with the exact-symplectic localization needed by PF-183. The project-specific durable result here is narrower: applying the immersion-level theorem, rather than its global-isometry corollary, to the PF normalized collar family removes boundary normalization from the qualitative gate and exposes fixed-germ confinement as the precise residual geometric condition at the cusp endpoint.

## Boundary conditions and falsification controls

Three limits must not be blurred.

First, the fixed target germ is essential at `L=0`. If the target is allowed to reach arbitrarily far toward `x=0`, (29) with `k>=2` is an exact zero-strain counterexample to convergence toward the inclusion. PF-188 therefore does **not** establish unconstrained qualitative rigidity of arbitrary cusp germs.

Second, the ordered marking is essential for identity selection. Without it, reflection permits the half-turn `T_{1/2}`, exactly as in PF-187.

Third, qualitative convergence is not a summability estimate. A modulus that tends to zero arbitrarily slowly cannot be inserted into PF-183's infinite-collar Schatten budget. Any future use of PF-188 as if it supplied (10), or as if it constructed an exact-symplectic cutoff, is invalid.

Within those boundaries, the earlier boundary-to-boundary normalization requirement is no longer a genuine qualitative obstruction.