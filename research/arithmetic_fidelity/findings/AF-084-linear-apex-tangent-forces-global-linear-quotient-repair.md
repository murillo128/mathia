# AF-084 — A linear tangent at the homogeneity apex forces global linear quotient repair

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `STRUCTURAL-CLASSIFICATION`, `CLASSICAL-MECHANISM`, `NEGATIVE/OBSTRUCTION`, `PRIOR-ART-BOUNDARY`

## Claim

Let `E` and `F` be real Banach spaces, let

\[
q:E\longrightarrow F
\tag{1}
\]

be a bounded linear surjection, and let

\[
L:F\longrightarrow E
\tag{2}
\]

be a positive-homogeneous right inverse:

\[
qL=I_F,
\qquad
L(ty)=tL(y)
\quad(t\ge 0).
\tag{3}
\]

Positive homogeneity includes `t=0`, so `L(0)=0`. Then the homogeneity apex `0` has an exact rigidity property.

1. **The one-sided directional derivative at the apex is the whole nonlinear map.** For every `y\in F`,

   \[
   \boxed{
   D_+L(0;y)
   :=
   \lim_{t\downarrow0}
   \frac{L(ty)-L(0)}{t}
   =L(y).}
   \tag{4}
   \]

   Thus existence of all ray derivatives at `0` says nothing about linear repair: a nonlinear positive-homogeneous section already has them automatically.

2. **Continuity upgrades (4) to Hadamard directional differentiability, still with a possibly nonlinear derivative map.** If `L` is continuous and

   \[
   t_n\downarrow0,
   \qquad
   y_n\to y,
   \tag{5}
   \]

   then

   \[
   \boxed{
   \frac{L(t_ny_n)-L(0)}{t_n}
   =L(y_n)
   \longrightarrow L(y).}
   \tag{6}
   \]

   Hence a continuous nonlinear homogeneous repair can be Hadamard **directionally** differentiable at the apex even though no linear differential exists there. Directional regularity must not be confused with a linear first-order tangent.

3. **Any bounded-linear first-order expansion at the apex is exact globally.** Suppose that a bounded linear map

   \[
   A:F\to E
   \tag{7}
   \]

   satisfies

   \[
   \|L(h)-Ah\|=o(\|h\|)
   \qquad(h\to0).
   \tag{8}
   \]

   Then

   \[
   \boxed{L=A\text{ on all of }F.}
   \tag{9}
   \]

   Consequently `qA=I_F`, so the quotient already has a bounded linear section. Homogeneity leaves no intermediate regime in which a nonlinear section becomes merely *asymptotically* linear at its natural zero scale.

4. **Fréchet differentiability at the apex is equivalent to global linearity of that section.** For a positive-homogeneous right inverse `L`,

   \[
   \boxed{
   L\text{ is Fréchet differentiable at }0
   \iff
   L\text{ is bounded linear}.}
   \tag{10}
   \]

   At the existence level this gives

   \[
   \boxed{
   \begin{array}{c}
   \exists\text{ positive-homogeneous right inverse Fréchet differentiable at }0\\
   \Longleftrightarrow\\
   \exists\text{ bounded linear right inverse of }q.
   \end{array}}
   \tag{11}
   \]

   The same implication holds for any notion of Gâteaux/Hadamard differentiability whose derivative at `0` is required to be a bounded linear map: the positive ray already forces that derivative to equal `L` pointwise.

5. **Nonsplitting therefore forces a first-order singularity at the homogeneity apex, without any separability hypothesis.** If `q` has no bounded linear right inverse, then every positive-homogeneous right inverse fails to admit a bounded-linear first-order tangent at `0`.

   This obstruction is different from AF-082. AF-082 uses separability to show that a *global Lipschitz* section linearizes through Godefroy--Kalton. Here no separability and no global Lipschitz assumption are needed: positive homogeneity alone propagates any linear `o(\|h\|)` approximation at one point to exact equality everywhere.

6. **The canonical nonlinear metric repair from AF-081 is an exact matched control.** Let

   \[
   1<p<\infty,
   \qquad
   p\ne2,
   \tag{12}
   \]

   and choose a closed uncomplemented subspace `K\subset\ell^p` as in AF-081. The minimum-norm quotient section

   \[
   s_K:\ell^p/K\to\ell^p
   \tag{13}
   \]

   is continuous, homogeneous, canonical relative to the norm geometry, and satisfies the radial isometry

   \[
   \|s_K(y)\|=\|y\|.
   \tag{14}
   \]

   Nevertheless it cannot be Fréchet differentiable at `0`, nor admit any bounded-linear first-order tangent there, because (9) would make `s_K` a bounded linear right inverse and hence complement `K`, contradicting the choice of `K`.

7. **The nonlinear escape survives all the way to first order.** Combining AF-081--AF-083 with the present result gives the strict hierarchy

   \[
   \boxed{
   \begin{array}{c}
   \text{continuous / bounded-scale uniform homogeneous repair may exist beyond splitting;}\\
   \text{all one-sided directional derivatives at the apex may still exist;}\\
   \text{but any genuinely linear first-order tangent at that apex collapses the repair to a linear split.}
   \end{array}}
   \tag{15}
   \]

The reusable Arithmetic Fidelity conclusion is that, for degree-one scale-equivariant recovery, **linearization at the zero scale is not a local approximation property but a global algebraic rigidity condition**. Any route that needs a nonlinear quotient escape and later assumes an ordinary linear tangent at the natural homogeneity apex has silently reintroduced the original splitting obstruction.

## Derivation

### Positive rays expose the complete map at first order

From (3), for every fixed `y\in F` and every `t>0`,

\[
\frac{L(ty)-L(0)}{t}
=
\frac{tL(y)}{t}
=L(y).
\tag{16}
\]

The quotient is independent of `t`, proving (4). This is the standard elementary phenomenon for degree-one homogeneous maps: their directional derivative at the center of homogeneity reproduces the map itself.

If `L` is continuous and `y_n\to y`, the same identity gives

\[
\frac{L(t_ny_n)-L(0)}{t_n}=L(y_n)\to L(y),
\tag{17}
\]

which is precisely the positive-parameter Hadamard directional criterion used in nonsmooth analysis. No additivity of the derivative map follows; its derivative map is just `y\mapsto L(y)`.

This distinction is essential. For a nonlinear homogeneous map, saying "every directional derivative exists at the origin" can sound like strong infinitesimal regularity while in fact it is a tautological consequence of scaling.

### An `o(||h||)` linearization cannot hide along a homogeneous ray

Assume (8). Fix `y\ne0` and put `h=ty` with `t>0`. Positive homogeneity of `L` and linearity of `A` give

\[
L(ty)-A(ty)
=t\bigl(L(y)-Ay\bigr).
\tag{18}
\]

Therefore

\[
\frac{\|L(ty)-A(ty)\|}{\|ty\|}
=
\frac{\|L(y)-Ay\|}{\|y\|}.
\tag{19}
\]

The left side tends to zero as `t\downarrow0` by (8), while the right side is independent of `t`. Hence

\[
L(y)=Ay.
\tag{20}
\]

Since `y` was arbitrary, `L=A` globally. Applying `q` gives

\[
qA=qL=I_F,
\tag{21}
\]

so `A` is a bounded linear section. This proves (9).

The argument is stronger than a chain-rule observation. It says that the relative first-order error of a degree-one homogeneous map against a linear candidate is **scale invariant** along every positive ray. If that error is required to vanish asymptotically, it must already be zero before taking the limit.

### Fréchet and linear Gâteaux tangents are therefore splitting certificates

If `L` is Fréchet differentiable at `0`, there is a bounded linear derivative `A=DL(0)` satisfying exactly (8), so (9) makes `L=A` bounded linear. Conversely every bounded linear section is Fréchet differentiable everywhere, proving (10).

For a standard Gâteaux derivative required to be linear, the same conclusion follows even before invoking a uniform remainder. The positive directional quotient is always `L(y)` by (16); if a linear derivative `A` exists, it must satisfy `Ay=L(y)` for every `y`, hence `L=A`.

If one instead uses a convention in which a "Gâteaux differential" or directional derivative may be nonlinear as a function of direction, then no such conclusion follows. Equations (4) and (6) are explicit counterwarnings: the nonlinear map itself is the directional derivative.

### The obstruction is local in scale but global in consequence

AF-082 showed, for separable quotients, that global Lipschitz regularity of a section already forces a bounded linear section. AF-083 then isolated a weaker bounded-ball uniform category in which nonlinear repair can genuinely survive and identified the exact scale law

\[
\omega_R(t)=R\omega_1(t/R).
\tag{22}
\]

AF-084 closes a different possible escape: one cannot hope that such a nonlinear homogeneous repair becomes linearly smooth only in an infinitesimal neighborhood of `0`. The scale equivariance makes its first-order angular geometry repeat at every radius. Linear smoothness at the apex would therefore force the entire section to have been linear all along.

## Exact controls

### Split Hilbert control: the apex is genuinely smooth

If `E` is Hilbert and `K=\ker q` is closed, the orthogonal minimum-norm section

\[
s:(E/K)\to K^\perp\subset E
\tag{23}
\]

is linear and isometric. It is Fréchet differentiable at `0`, with `Ds(0)=s`. This is the rigid positive endpoint: linear tangent, global linear section, and splitting coincide.

### Uncomplemented uniformly convex control: canonical recovery without a linear tangent

For the AF-081 example `K\subset\ell^p`, the minimum-norm section `s_K` is continuous and homogeneous but nonlinear because `K` is not complemented. Equations (4) and (6) still apply: its one-sided and Hadamard directional derivatives at the apex exist and equal `s_K` itself. Yet no bounded linear differential can exist there.

This simultaneously separates three notions that are easy to conflate:

\[
\text{directional regularity}
\ne
\text{linear differentiability}
\ne
\text{linear splitting}.
\tag{24}
\]

The first may survive even when the latter two fail.

### Generic selection control: regularity away from the apex does not repair the apex

Bartle--Graves selection theory gives continuous nonlinear right inverses for Banach-space surjections, and standard strengthened formulations allow positive-homogeneous choices. Messerschmidt proves that a continuous linear surjection between infinite-dimensional Banach spaces has a positively homogeneous continuous right inverse that is pointwise Lipschitz on a dense meager subset of its domain.

That result is compatible with the present obstruction. Pointwise regularity at many nonzero states does not imply a bounded-linear tangent at the distinguished homogeneity apex. The apex is special because every ray collapses into it while retaining the full degree-one scaling law.

## Prior art and novelty assessment

The core homogeneous differentiability mechanism is classical and is **not** claimed as a new theorem.

- Lynn H. Loomis and Shlomo Sternberg, ***Advanced Calculus***, differential-calculus chapter, discussion immediately following Theorem 7.2 (p. 148 in the circulated Harvard edition; authorized reissue by World Scientific, 2014). They explicitly observe that for a degree-one homogeneous map the directional derivative at `0` equals the map itself and that differentiability at `0` therefore forces the map to be linear. This is direct prior art for the central rigidity step.
- Alexander Shapiro, **“On concepts of directional differentiability,”** *Journal of Optimization Theory and Applications* 66 (1990), 477--487, DOI `10.1007/BF00940933`. Role: established comparison of Gâteaux, Fréchet, and Hadamard directional differentiability and the standard positively-homogeneous derivative-map language. It supports the distinction between a nonlinear directional derivative and a genuine linear differential.
- R. G. Bartle and L. M. Graves, **“Mappings between function spaces,”** *Transactions of the American Mathematical Society* 72 (1952), 400--413, DOI `10.1090/S0002-9947-1952-0047910-X`. Role: classical continuous-selection background for quotient maps, showing that nonlinear continuous recovery is much broader than linear splitting.
- Miek Messerschmidt, **“A Pointwise Lipschitz Selection Theorem,”** *Set-Valued and Variational Analysis* 27 (2019), 223--240, DOI `10.1007/s11228-017-0455-2`. Role: modern strengthening giving positively homogeneous continuous right inverses that are pointwise Lipschitz on a dense set, useful for delimiting the special role of the apex rather than suggesting nonlinear selections are everywhere irregular.
- AF-078, AF-081, AF-082, and AF-083 provide the already-persisted Mathia quotient-repair boundaries: linear splitting and canonicity, canonical nonlinear metric repair beyond splitting, global Lipschitz linearization for separable quotients, and bounded-scale uniform repair with exact scale renormalization.

No novelty is claimed for homogeneous directional derivatives, the statement that a differentiable degree-one homogeneous map is linear, Bartle--Graves selection, or the differentiability vocabulary. The durable Arithmetic Fidelity contribution is the **category-level stopping rule** obtained by inserting this classical fact into the quotient-repair hierarchy: nonlinear homogeneous recovery may evade linear splitting at continuity or bounded-uniform levels, but it cannot acquire a bounded-linear tangent at the scaling apex without collapsing globally to the very linear split it was meant to evade.

## Boundaries and failure modes

- The theorem is stated over real Banach spaces. The positive-ray proof also applies to complex spaces viewed over the reals, but complex differentiability carries additional scalar-linearity requirements and should not be silently conflated with the real statement.
- Positive homogeneity is essential. A general nonlinear section can agree to first order with a linear map near one point without being globally linear.
- The rigidity is specific to the homogeneity apex `0`. Differentiability or pointwise Lipschitz behavior at nonzero points does not imply global linearity.
- Equations (4) and (6) use one-sided positive scaling. Positive homogeneity alone does not imply oddness, so a two-sided directional derivative need not exist unless the negative ray is compatible. The Fréchet/linear-derivative conclusions do not require oddness: their positive-side limits already force `L=A`.
- Continuity is needed for the perturbed-direction Hadamard statement (6), but not for the basic ray identity (4) or the `o(\|h\|)` rigidity (9).
- A nonlinear directional derivative is not a contradiction. Some terminology calls such an object a Gâteaux differential; this finding reserves "linear first-order tangent" for a bounded linear derivative and states the convention explicitly.
- The result concerns full representative selection. A particular discriminator may admit a much smaller or differently structured lift that does not reconstruct a complete quotient representative.
- No arithmetic or rational-prime-specific conclusion follows from this Banach-space result alone.

## Consequences for Arithmetic Fidelity

AF-083 showed that bounded-ball uniform recovery can survive beyond linear splitting, but only with scale-dependent nonlinear stability. AF-084 sharpens the meaning of that nonlinear escape: **there is no hidden asymptotically linear core at the natural zero scale**. For a degree-one homogeneous repair, the angular nonlinearity visible on the unit sphere is reproduced exactly at every radius down to the apex.

This supplies a practical audit for later compression mechanisms. If a proposed intrinsically selected lift is homogeneous because the underlying problem has no distinguished scale, then any downstream theorem that needs an ordinary linear tangent, Jacobian, or first-order linear response at the zero state is not a harmless local regularity assumption. It is a splitting certificate. Before using such a differential object, the research must either prove that the relevant quotient genuinely splits or work with a nonlinear directional derivative whose retained structure is audited in its own category.

The next structural question is therefore narrower than "does a continuous repair exist?": determine which downstream operations can consume a nonlinear homogeneous directional derivative without silently replacing it by a linear tangent, and which composition or asymptotic procedures force that linearization and thereby restore the splitting obstruction.