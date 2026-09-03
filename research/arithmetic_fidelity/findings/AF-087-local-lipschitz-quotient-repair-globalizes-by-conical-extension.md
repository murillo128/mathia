# AF-087 — Local Lipschitz quotient repair globalizes by conical extension

**Status:** `EXACT-DERIVED`, `LITERATURE+DERIVED`, `STRUCTURAL-CLASSIFICATION`, `CLASSICAL-MECHANISM`, `NEGATIVE/OBSTRUCTION`, `PRIOR-ART-BOUNDARY`

## Claim

Let `E` and `F` be real or complex Banach spaces and let

\[
q:E\to F
\tag{1}
\]

be a bounded linear surjection. Define the best global Lipschitz section cost

\[
\lambda_{\mathrm{Lip}}(q)
:=
\inf\{\operatorname{Lip}(L):L:F\to E,\ qL=I_F\},
\tag{2}
\]

and the best **local-neighborhood Lipschitz section cost**

\[
\lambda_{\mathrm{locLip}}(q)
:=
\inf\left\{
\operatorname{Lip}(s):
\begin{array}{l}
y_0\in F,\ r>0,\\
s:y_0+rB_F\to E,\\
qs(y)=y\ \text{on }y_0+rB_F
\end{array}
\right\},
\tag{3}
\]

with the infimum of an empty family interpreted as `+∞`. Then local and global Lipschitz quotient repair have the same **existence boundary**, with a universal quantitative globalization bound:

\[
\boxed{
\lambda_{\mathrm{locLip}}(q)
\le
\lambda_{\mathrm{Lip}}(q)
\le
3\lambda_{\mathrm{locLip}}(q).
}
\tag{4}
\]

More precisely, every `L`-Lipschitz right inverse on one nontrivial ball can be converted explicitly into a global positive-homogeneous right inverse with Lipschitz constant at most `3L`.

Consequently:

1. **One Lipschitz neighborhood already gives a global Lipschitz section.** If a right inverse is Lipschitz on any neighborhood of any point of `F`, restricting to a smaller ball and applying the construction below yields a global Lipschitz right inverse. Conversely, a global Lipschitz section restricts to every ball. Thus

   \[
   \boxed{
   \exists\text{ local-neighborhood Lipschitz section}
   \iff
   \exists\text{ global Lipschitz section}.}
   \tag{5}
   \]

   No separability assumption is needed for this equivalence.

2. **For separable quotients, local Lipschitz repair already forces linear splitting.** If `F` is separable, AF-082 and the Godefroy--Kalton lifting theorem give

   \[
   \lambda_{\mathrm{Lip}}(q)=\lambda_{\mathrm{lin}}(q),
   \tag{6}
   \]

   where `lambda_lin` is the best bounded-linear section norm. Hence

   \[
   \boxed{
   \lambda_{\mathrm{locLip}}(q)
   \le
   \lambda_{\mathrm{lin}}(q)
   \le
   3\lambda_{\mathrm{locLip}}(q),
   }
   \tag{7}
   \]

   and, at the existence level,

   \[
   \boxed{
   \begin{array}{c}
   \text{a Lipschitz section exists on one neighborhood}\\
   \Longleftrightarrow
   \text{a global Lipschitz section exists}\\
   \Longleftrightarrow
   \text{a bounded linear section exists}.
   \end{array}}
   \tag{8}
   \]

   For complex spaces, the metric globalization is applied to the underlying real spaces and AF-082's real-to-complex symmetrization supplies the complex-linear section without increasing the final linear norm.

3. **Locality is therefore not the nonlinear escape identified in AF-083.** Bounded-ball uniform repair can exist for separable nonsplitting quotients, but bounded-ball Lipschitz repair cannot. The strict intermediate category from AF-083 is genuinely **sub-Lipschitz**: once a section has a finite pairwise Lipschitz constant on even one full neighborhood, linear scaling propagates that regularity globally and Godefroy--Kalton closes the nonsplitting escape.

4. **Pointwise Lipschitz regularity is strictly weaker than neighborhood Lipschitz repair.** Messerschmidt's strengthening of Bartle--Graves gives, for every continuous linear surjection between infinite-dimensional Banach spaces, a positive-homogeneous continuous right inverse that is pointwise Lipschitz on a dense meager set. Apply this to AF-081's quotient by an uncomplemented closed subspace of `ell^p`, `1<p<∞`, `p != 2`. Its separable quotient does not split, so (8) forbids a Lipschitz section on every neighborhood, while Messerschmidt still supplies a section that is pointwise Lipschitz at densely many individual points.

   Thus

   \[
   \boxed{
   \text{pointwise Lipschitz at many points}
   \not\Rightarrow
   \text{Lipschitz on one neighborhood}.}
   \tag{9}
   \]

5. **The mechanism is independent of differentiability.** AF-085 showed that a Fréchet-differentiable local section at one point already forces a linear split by differentiating the right-inverse identity. AF-087 requires no derivative and no almost-linear tangent. Pairwise Lipschitz control on a neighborhood is globalized geometrically by translation and radial scaling; only afterward, in the separable case, is the global Lipschitz section linearized by Godefroy--Kalton.

The reusable Arithmetic Fidelity conclusion is that **for a linear quotient, Lipschitz-stable representative recovery cannot be merely local**. A single stable neighborhood contains a scaled copy of every direction in the quotient space, and conical extension turns that one patch into a global recovery map. Any proposed quotient-repair mechanism that truly escapes linear splitting must therefore weaken the stability category below neighborhood Lipschitz control, restrict the admissible directions as in AF-086, or change the downstream category rather than relying on locality alone.

## Derivation

### Translate one local patch to the origin

Suppose that for some `y_0 in F`, `r>0`, and `L<∞` there is an `L`-Lipschitz section

\[
s:y_0+rB_F\to E,
\qquad
qs(y)=y.
\tag{10}
\]

Define

\[
f:rB_F\to E,
\qquad
f(h):=s(y_0+h)-s(y_0).
\tag{11}
\]

Then

\[
f(0)=0,
\qquad
qf(h)=h,
\qquad
\operatorname{Lip}(f)\le L.
\tag{12}
\]

In particular,

\[
\|f(h)\|\le L\|h\|
\qquad(h\in rB_F).
\tag{13}
\]

The affine location of the original patch is therefore irrelevant: linearity of `q` converts any local section into a centered local section with the same Lipschitz constant.

### Cone the boundary values to all scales

Set `H(0)=0`. For `y != 0`, define

\[
\boxed{
H(y)
:=
\frac{\|y\|}{r}
 f\!\left(r\frac{y}{\|y\|}\right).
}
\tag{14}
\]

Then

\[
qH(y)
=
\frac{\|y\|}{r}
 qf\!\left(r\frac{y}{\|y\|}\right)
=y,
\tag{15}
\]

so `H` is a global right inverse. It is positive homogeneous:

\[
H(ty)=tH(y)
\qquad(t\ge0).
\tag{16}
\]

This construction uses only the selected representatives on one sphere inside the local patch. No consistency between different radii of the original section is required.

### The conical extension has a universal `3L` Lipschitz bound

Take nonzero `x,y in F` and write

\[
a=\|x\|,
\qquad
b=\|y\|.
\tag{17}
\]

Assume without loss of generality that `a>=b>0`, and put

\[
u=x/a,
\qquad
v=y/b.
\tag{18}
\]

Using (14), add and subtract `(a/r)f(rv)`:

\[
\begin{aligned}
\|H(x)-H(y)\|
&\le
\frac{a}{r}\|f(ru)-f(rv)\|
+
\frac{a-b}{r}\|f(rv)\|\\
&\le
La\|u-v\|+L(a-b).
\end{aligned}
\tag{19}
\]

Now

\[
a\|u-v\|
=\|x-av\|
\le
\|x-y\|+\|y-av\|
=\|x-y\|+(a-b),
\tag{20}
\]

while the reverse triangle inequality gives

\[
a-b\le\|x-y\|.
\tag{21}
\]

Combining (19)--(21),

\[
\boxed{
\|H(x)-H(y)\|
\le
3L\|x-y\|.
}
\tag{22}
\]

If one of the points is zero, (13)--(14) give the stronger estimate

\[
\|H(x)-H(0)\|
\le L\|x\|.
\tag{23}
\]

Thus `Lip(H)<=3L`. Taking infima gives the second inequality in (4); the first follows by restriction of any global section to a ball.

The constant `3` is a universal bound for this elementary conical construction. No claim is made here that `3` is the optimal local-to-global constant over all Banach quotients or all possible globalization procedures.

### Separable global Lipschitz repair linearizes

When `F` is separable, apply AF-082/Godefroy--Kalton to the global section `H`. There is a bounded linear right inverse

\[
V:F\to E,
\qquad
qV=I_F,
\tag{24}
\]

with

\[
\|V\|
\le
\operatorname{Lip}(H)
\le3L.
\tag{25}
\]

This proves (7)--(8). Notice that the argument does not try to differentiate the original local section. The nonlinear local patch may be nowhere differentiable; the conical globalization is enough to enter the classical global Lipschitz lifting theorem.

## Exact controls

### Split linear control: local and global costs coincide

If `q` has a bounded linear section `V`, then the same `V` is a global Lipschitz section and restricts to an `||V||`-Lipschitz section on every ball. Hence

\[
\lambda_{\mathrm{locLip}}(q)
\le
\lambda_{\mathrm{Lip}}(q)
\le
\|V\|.
\tag{26}
\]

For a Hilbert quotient with the orthogonal minimum-norm section, all three costs are `1` after the standard quotient normalization. The factor `3` in (4) is therefore a worst-case globalization estimate, not an unavoidable loss in every quotient.

### Nonsplitting separable control: no Lipschitz patch exists anywhere

Let `1<p<∞`, `p != 2`, and choose a closed uncomplemented subspace

\[
K\subset\ell^p
\tag{27}
\]

as in AF-081. For

\[
q:\ell^p\to\ell^p/K,
\tag{28}
\]

the quotient is separable but admits no bounded linear section. By (8), there cannot exist any right inverse that is Lipschitz on a nonempty quotient neighborhood.

This is stronger than saying that AF-081's canonical minimum-norm section is not globally Lipschitz: **no alternative representative-selection rule can be neighborhood-Lipschitz anywhere** while remaining a right inverse on that neighborhood.

### Pointwise-Lipschitz control: dense regular points do not create one regular patch

For the same kind of nonsplitting infinite-dimensional quotient, Messerschmidt's pointwise Lipschitz selection theorem still provides a continuous positive-homogeneous right inverse that is pointwise Lipschitz on a dense meager subset of the quotient. Therefore a dense set of finite pointwise slopes does not contradict the absence of every Lipschitz neighborhood.

This is the matched boundary between the present theorem and AF-084/AF-085: regularity at isolated base points, even densely many of them, is not the same datum as one uniform pairwise Lipschitz estimate on an open patch.

### Bounded-uniform control: the genuine nonlinear intermediate category survives

AF-083 exhibits separable nonsplitting quotients with a section uniformly continuous on the unit ball. Such a section cannot be Lipschitz on any quotient neighborhood by the present theorem. Therefore the bounded-uniform escape is not just a globally bad Lipschitz map; its modulus must fail every finite local Lipschitz bound on every open patch, even though it remains uniformly continuous on each bounded ball after homogeneous normalization.

This complements AF-083's scale statement `limsup_{t downarrow 0} omega_1(t)/t=+∞`: AF-087 localizes the obstruction spatially. No open neighborhood can carry a finite Lipschitz constant at all in a separable nonsplitting quotient.

## Prior art and novelty assessment

The mathematical mechanism is classical and no novelty is claimed for radial/conical extension, homogeneous normalization, Lipschitz lifting, or pointwise Lipschitz selection.

- Nigel J. Kalton, **“Spaces of Lipschitz and Hölder Functions and Their Applications,”** *Collectanea Mathematica* 55(2) (2004), 171--217, DOI `10.1344/CM.V55I2.4055`. In the discussion immediately preceding Proposition 7.2, Kalton shows that a uniformly continuous section on a quotient unit ball may be homogenized and extended to the whole quotient while retaining uniform continuity on bounded sets, with an explicit modulus estimate. Specializing that normalization to a Lipschitz modulus already places the local/ball-to-homogeneous-global mechanism inside established nonlinear Banach-space theory. The direct construction (11)--(22) isolates the simpler Lipschitz case and records a universal `3L` bound.
- Gilles Godefroy and Nigel J. Kalton, **“Lipschitz-free Banach spaces,”** *Studia Mathematica* 159(1) (2003), 121--141, DOI `10.4064/sm159-1-6`. Their separable lifting theorem is the classical source behind AF-082: a quotient onto a separable Banach space with a global Lipschitz right inverse has a bounded linear right inverse, quantitatively with no larger norm.
- Miek Messerschmidt, **“A Pointwise Lipschitz Selection Theorem,”** *Set-Valued and Variational Analysis* 27 (2019), 223--240, DOI `10.1007/s11228-017-0455-2`. The paper proves that every continuous linear surjection between infinite-dimensional Banach spaces has a positive-homogeneous continuous right inverse that is pointwise Lipschitz on a dense meager set. This supplies the decisive weaker-regularity control showing that the neighborhood hypothesis cannot be replaced by pointwise Lipschitz regularity at many isolated points.
- AF-081--AF-086 provide the already-persisted Mathia quotient-repair hierarchy: canonical nonlinear metric recovery beyond complementability, global Lipschitz linearization, bounded-scale uniform escape, homogeneous-apex rigidity, the Neumann first-order gap, and tangent-direction coverage.

A targeted literature audit of Banach quotient sections, local Lipschitz right inverses, radial/homogeneous extension, and the Godefroy--Kalton/Kalton lifting framework did not locate a reason to treat (4)--(8) as a new literature theorem. Kalton's homogeneous normalization already contains the relevant classical mechanism in a more general uniform-modulus setting. The durable Arithmetic Fidelity contribution is therefore the **explicit category boundary** and its quantitative elementary proof: neighborhood Lipschitz repair, unlike bounded-uniform or pointwise-Lipschitz repair, has no local-only existence regime for linear quotients.

## Boundaries and failure modes

- “Local Lipschitz” here means one right inverse is Lipschitz **between every pair of points in a full neighborhood**, equivalently on some nontrivial ball after restriction. A finite pointwise Lipschitz constant at one point, directional Lipschitz control, or pointwise Lipschitz regularity on a dense set does not satisfy the hypothesis.
- The local-to-global equivalence (5) uses only the linear and homogeneous structure of a Banach-space quotient. It should not be transferred automatically to nonlinear submersions, general metric quotients, manifolds, or set-valued recovery problems.
- The conical map `H` is generally not canonical, additive, equivariant, order preserving, or compatible with extra structure. It proves existence in the unrestricted Lipschitz category only.
- The universal factor `3` is an upper bound from one explicit construction and is not asserted to be optimal. In special categories the best local and global costs can coincide.
- Separability is unnecessary for the globalization (4)--(5) but is essential to the AF-082/Godefroy--Kalton linearization step used in (6)--(8). Nonseparable quotients can have different Lipschitz-lifting behavior.
- The construction is metric and positive-homogeneous, so it applies to complex Banach spaces through their underlying real normed spaces. Complex-linear consequences require the additional symmetrization already audited in AF-082.
- Uniform continuity on a bounded ball is strictly weaker than the hypothesis; AF-083 gives nonsplitting controls where that weaker repair exists. Hölder or other sub-Lipschitz moduli likewise do not cross the present gate.
- The theorem concerns recovery of a full representative of a quotient state. A particular discriminator may factor through much less information and need not inherit this full-section obstruction.
- No rational-prime or RH-specific conclusion follows from this Banach-space result alone.

## Consequences for Arithmetic Fidelity

AF-083 showed that bounded-scale uniform recovery can survive after linear/global-Lipschitz splitting has failed. AF-084--AF-086 then analyzed what happens at the homogeneity apex, under first-order approximation, and on restricted direction sets. AF-087 closes the complementary **spatial-locality** loophole: weakening “global Lipschitz” to “Lipschitz on one neighborhood” does not create a larger repair class.

The resulting quotient-repair hierarchy is sharper. A nonsplitting separable quotient may admit continuous or bounded-uniform nonlinear selections and may even have a selection with finite pointwise Lipschitz slope on a dense set. What it cannot possess is one open patch with a finite pairwise Lipschitz constant. Thus the relevant boundary is not local versus global domain size; it is the regularity class of the retained map.

For later compression problems, this supplies a concrete audit rule. If a proposed lift of a linear quotient is claimed to preserve a discriminator stably on a neighborhood, first ask whether that stability is genuinely pairwise Lipschitz. If it is, conical globalization eliminates locality as an escape; in a separable destination the mechanism has already crossed back into linear splitting. A viable nonlinear escape must instead live in a weaker modulus, a restricted tangent family, or an additional category whose structure prevents the unrestricted conical extension from being admissible.