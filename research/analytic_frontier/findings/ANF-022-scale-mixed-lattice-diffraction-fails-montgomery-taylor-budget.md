# ANF-022 — scale-mixed lattice diffraction fails the Montgomery--Taylor budget

**Status:** `EXACT-DERIVED + FINITE-EXACT-AUDIT + NEGATIVE/OBSTRUCTION + DIFFRACTION-DUAL`. `ANF-020` reduces the remaining universal-affine scalar ceiling to a single diffraction-realizability problem: with

\[
C_{\rm MT}
=\frac12+\frac1{\sqrt2}\cot\frac1{\sqrt2},
\qquad
a:=C_{\rm MT}^{-1}=0.753296067856070\ldots,
\]

one needs an element of the closed convex finite-configuration diffraction body dominated on `(-1,1)` by

\[
\nu_a=a\,\delta_0+a|\alpha|\,d\alpha.
\]

A natural nonstationary candidate after the random-matrix filters of `ANF-020`--`ANF-021` is to convexify arithmetic lattices over their density/spacing scale. This finding rules out that entire class. If

\[
\mu_\rho=\rho\sum_{k\in\mathbb Z}\delta_{k\rho}
\]

is the normalized diffraction of the one-dimensional lattice of density `rho>0`, then for **every** probability measure `pi` on positive scales for which the mixture is locally finite,

\[
\boxed{
\int \mu_\rho\,d\pi(\rho)
\not\le a\bigl(\delta_0+|\alpha|\,d\alpha\bigr)
\quad\text{on }(-1,1).
}
\]

The obstruction is not merely that an individual lattice has Bragg peaks. A continuous distribution of scales can smear all nonzero Bragg peaks into an absolutely continuous density, but the harmonic copies then obey a dilation-sum constraint. The exact dual inverse of that constraint is a Möbius-weighted function. A finite nonnegative dual certificate on the scale interval `[1/50,1]` has total mass

\[
B_{50}=0.323565904318542\ldots
<C_{\rm MT}-1=0.327499296320588\ldots,
\]

while the forward-atom budget would require at least `C_MT-1`. This produces a strict contradiction with room to spare.

## 1. Arithmetic lattices lie on the finite-diffraction boundary

For `rho>0`, take the `N`-point arithmetic progression

\[
X_{N,\rho}=\left\{0,\frac1\rho,\ldots,\frac{N-1}{\rho}\right\}.
\]

Its normalized diffraction measure in the convention of `ANF-020` is

\[
\mu_{N,\rho}(d\alpha)
=\frac1N\left|
\sum_{j=0}^{N-1}e^{-2\pi i\alpha j/\rho}
\right|^2d\alpha.
\tag{1}
\]

The bracket is the Fejer kernel in the variable `alpha/rho`. Hence, against every compactly supported continuous test function,

\[
\boxed{
\mu_{N,\rho}\overset{*}{\longrightarrow}
\mu_\rho
:=\rho\sum_{k\in\mathbb Z}\delta_{k\rho}.
}
\tag{2}
\]

This is the one-dimensional Poisson-summation lattice diffraction formula, but (2) also derives the exact normalization directly from finite configurations. Therefore every `mu_rho` is already a weak-* boundary point of the diffraction body `K` from `ANF-020`; finite convex mixtures belong to `K`, and arbitrary scale mixtures are the corresponding natural weak-limit candidate class.

The pure-point lattice formula itself is classical diffraction theory. Baake--Grimm and Richard--Strungaru are representative Poisson-summation references. No external diffraction theorem is load-bearing below because the needed normalization follows directly from the Fejer limit (1)--(2).

## 2. What domination forces on a scale mixture

Let `pi` be a probability measure on `(0,infinity)` and write

\[
\overline\mu
:=\int\mu_\rho\,d\pi(\rho).
\tag{3}
\]

Suppose for contradiction that

\[
\overline\mu\le\nu_a
\quad\text{on }(-1,1).
\tag{4}
\]

The atom at zero has mass

\[
\overline\rho:=\int_0^\infty \rho\,d\pi(\rho),
\]

so (4) immediately gives

\[
\boxed{\overline\rho\le a.}
\tag{5}
\]

Now restrict to the positive open band `(0,1)`. The first positive harmonic of (3) is the measure `rho pi(d rho)` pushed by `rho -> rho`. Since the right side of (4) is absolutely continuous away from zero, this already forces `pi` to be absolutely continuous on `(0,1)`. Write

\[
d\pi(\rho)=w(\rho)\,d\rho
\qquad(0<\rho<1),
\tag{6}
\]

with `w>=0`, and let

\[
r:=\int_0^1 w(\rho)d\rho.
\]

Any mass outside `(0,1)` has `rho>=1`, so the atom constraint (5) yields

\[
\begin{aligned}
a
&\ge\overline\rho\\
&\ge \int_0^1\rho w(\rho)d\rho +(1-r)\\
&=1-\int_0^1(1-\rho)w(\rho)d\rho.
\end{aligned}
\]

Define the **scale deficit**

\[
D:=\int_0^1(1-\rho)w(\rho)d\rho.
\tag{7}
\]

Then every putative dominated mixture must satisfy

\[
\boxed{
D\ge1-a.
}
\tag{8}
\]

Because `a=1/C_MT`, this is equivalently

\[
\boxed{
\frac Da\ge C_{\rm MT}-1.
}
\tag{9}
\]

Thus enough probability mass must be shifted below unit density to reduce the forward atom from the lattice endpoint `1` to the Montgomery--Taylor value `a`.

## 3. Harmonic replication converts the diffuse budget into a dilation operator

For `0<h<1`, the `m`-th positive Bragg harmonic `h=m rho` contributes, after the change of variables `rho=h/m`, the density

\[
\frac{h}{m^2}w(h/m).
\]

Therefore the complete positive-band diffuse density is

\[
\boxed{
g(h)=h\,(Tw)(h),}
\qquad
(Tw)(h):=\sum_{m\ge1}\frac{w(h/m)}{m^2}.
\tag{10}
\]

Domination by `a h dh` gives

\[
Tw\le a
\quad\text{a.e. on }(0,1).
\tag{11}
\]

Put `v=w/a`. Then `v>=0`,

\[
Tv\le1,
\tag{12}
\]

while (9) becomes the required lower bound

\[
\boxed{
\int_0^1(1-x)v(x)dx\ge m_{\rm MT},
\qquad
m_{\rm MT}:=C_{\rm MT}-1.
}
\tag{13}
\]

The lattice-mixture problem has therefore become a one-dimensional positive linear program: maximize the scale deficit against the harmonic dilation constraint (12).

## 4. The adjoint dilation operator has an exact Möbius inverse

For any nonnegative integrable test function `lambda`, Tonelli and the substitution `h=mx` give

\[
\begin{aligned}
\int_0^1\lambda(h)(Tv)(h)dh
&=
\int_0^1v(x)(T^*\lambda)(x)dx,
\end{aligned}
\tag{14}
\]

where

\[
\boxed{
(T^*\lambda)(x)
:=\sum_{m\le1/x}\frac{\lambda(mx)}m.
}
\tag{15}
\]

Consequently every `lambda>=0` satisfying

\[
T^*\lambda\ge1-x
\tag{16}
\]

gives the dual bound

\[
\boxed{
\int_0^1(1-x)v(x)dx
\le\int_0^1\lambda(x)dx.
}
\tag{17}
\]

There is an exact formal inverse of (15). Let `mu(n)` denote the Möbius function and put

\[
\lambda_0(x)
:=
\sum_{n\le1/x}\frac{\mu(n)}n(1-nx).
\tag{18}
\]

Then

\[
\boxed{T^*\lambda_0=1-x.}
\tag{19}
\]

Indeed, substituting (18) into (15) and grouping by `k=mn` makes the coefficient of `(1-kx)` equal

\[
\frac1k\sum_{n\mid k}\mu(n),
\]

which is `1` for `k=1` and `0` otherwise. Thus the same Möbius inversion that appeared on the periodization side in `ANF-013`--`ANF-015` reappears automatically on the **diffraction-dual** side: lattice harmonics are a dilation semigroup, and Möbius inversion removes their repetitions.

The only issue is positivity. `lambda_0` is not globally nonnegative at arbitrarily small scales, so it cannot itself be used directly as a positive LP dual certificate. A finite cutoff is enough.

## 5. A finite nonnegative dual certificate beats the Montgomery--Taylor deficit

For

\[
N:=50,
\]

define

\[
\lambda(x)
:=
\begin{cases}
1,&0<x<1/50,\\
\lambda_0(x),&1/50\le x<1.
\end{cases}
\tag{20}
\]

This function is nonnegative. To see the only nontrivial part, set

\[
A_n:=\sum_{k\le n}\frac{\mu(k)}k,
\qquad
M_n:=\sum_{k\le n}\mu(k).
\]

On each interval

\[
\frac1{n+1}<x\le\frac1n,
\]

one has the exact affine formula

\[
\lambda_0(x)=A_n-xM_n.
\tag{21}
\]

For `2<=n<=49`, an exact rational endpoint audit of (21) gives

\[
\lambda_0(x)>\frac1{26}.
\tag{22}
\]

The smallest audited endpoint occurs for `n=49`, `x=1/50`, where

\[
\lambda_0(1/50)
=
\frac{60704734407424654}{1537224456471228525}
=0.0394898312682\ldots
>\frac1{26}.
\tag{23}
\]

For `1/2<=x<=1`, (18) reduces to `lambda_0(x)=1-x>=0`. Since (21) is affine on every intervening interval, the endpoint audit certifies nonnegativity throughout `[1/50,1]`. The audit uses only exact Möbius values and rational arithmetic; no floating-point sign decision is involved.

The dual constraint (16) now follows in two regimes. If `x>=1/50`, every argument `mx` occurring in (15) is also at least `1/50`, so (19) applies unchanged and

\[
T^*\lambda(x)=1-x.
\tag{24}
\]

If `0<x<1/50`, the `m=1` term alone contributes `lambda(x)=1`, while every other term is nonnegative. Hence

\[
T^*\lambda(x)\ge1>1-x.
\tag{25}
\]

Thus `lambda` is a globally feasible nonnegative dual certificate.

Its integral is exact. Integrating (18) termwise over `[1/50,1]` gives

\[
\begin{aligned}
B_{50}
:=\int_0^1\lambda(x)dx
&=\frac1{50}
+\frac12\sum_{n=1}^{49}
\mu(n)\left(\frac1n-\frac1{50}\right)^2\\
&=
\frac{1529210663723939914090488978899221253}
{4726118059146527924423342245547351250}\\
&=0.323565904318542\ldots .
\end{aligned}
\tag{26}
\]

Certified interval evaluation of the exact Montgomery--Taylor constant gives

\[
0.32749<m_{\rm MT}<0.32750,
\tag{27}
\]

while the exact rational in (26) satisfies

\[
B_{50}<0.32357.
\tag{28}
\]

Therefore

\[
\boxed{B_{50}<m_{\rm MT}.}
\tag{29}
\]

The numerical gap is about `0.00393339`, far larger than the interval widths used in (27)--(28).

## 6. Contradiction

Apply the dual bound (17) to the normalized scale density `v=w/a`. Equations (12), (20)--(25) give

\[
\frac Da
=
\int_0^1(1-x)v(x)dx
\le B_{50}.
\tag{30}
\]

But the forward-atom budget (13) requires

\[
\frac Da\ge m_{\rm MT}.
\tag{31}
\]

Together with (29),

\[
m_{\rm MT}
\le\frac Da
\le B_{50}
<m_{\rm MT},
\]

a contradiction. Hence no scale mixture of arithmetic-lattice diffraction measures can lie below the Montgomery--Taylor budget on the support-one band.

Notice that the proof automatically handles the main apparent escape from pure Bragg diffraction. If `pi` has atoms or any singular component below density one, the first harmonic already creates forbidden singular diffraction in `(0,1)`. If `pi` is continuous there, the singular peaks can smear into a density, but all higher harmonics remain coupled through `T`, and the Möbius dual certificate proves that their aggregate cost is too large.

## 7. Prior-art and novelty boundary

Poisson-summation formulas for lattice Dirac combs and their pure-point diffraction are classical; Baake--Grimm, *Kinematic diffraction from a mathematical viewpoint* (2011, DOI `10.1524/zkri.2011.1389`, arXiv:1105.0095), and Richard--Strungaru, *Pure Point Diffraction and Poisson Summation* (2017, DOI `10.1007/s00023-017-0620-z`), are representative modern mathematical references. Möbius inversion of dilation sums is likewise classical and is already part of the line's Mellin/dilation prior-art boundary through `ANF-014`--`ANF-015`.

A targeted search across lattice diffraction, scale/random lattice mixtures, structure-factor realizability and Möbius/dilation inversion did not locate the specific Montgomery--Taylor domination problem or the dual certificate (20)--(29). No publication-level novelty claim is made. The derived content here is the exact specialization of those classical mechanisms to the `ANF-020` budget and the resulting no-go for the full arithmetic-lattice scale-mixture class.

No new entry is added to `SOURCES.md`: the proof rederives the only lattice-diffraction normalization it needs from the finite Fejer limit, and the external references above delimit prior art rather than serve as load-bearing premises.

## 8. Consequence for the scalar frontier

`ANF-020` ruled out stationary translation-invariant determinantal witnesses because the forward atom and infinitesimal cusp already force contraction factor at least one. `ANF-021` showed that symplectic/Pfaffian statistics evade that local cusp obstruction but fail at moderate frequency even after arbitrary scale mixing. The present result removes a qualitatively different escape: **crystalline diffraction cannot be rescued by randomizing the lattice scale**, even though that randomization can turn nonzero Bragg peaks into an absolutely continuous band profile.

The obstruction also explains why lattice constructions repeatedly return Möbius structure on this branch. On the primal periodization side (`ANF-013`--`ANF-015`), dilations of a compact spectrum are inverted by Möbius coefficients. On the diffraction-dual side, harmonic Bragg copies produce the adjoint dilation operator (15), whose exact inverse is again Möbius. This is not extra arithmetic information from zeta; it is the algebra of scale replication itself.

The full convex diffraction body `K` remains open. General beta log gases, genuinely non-crystalline hyperuniform processes, mixtures of different correlation mechanisms, nonstationary finite-cluster phases not generated by one lattice scale, and direct separating-spectrum arguments are not covered. The configuration-level escape of `ANF-006` is also outside the scalar diffraction duality. The immediate filter is now sharper: a proposed scalar witness must survive the **entire support-one measure budget** and cannot rely merely on local cusp improvement, Bragg smearing, or convexification over a single classical scale family.