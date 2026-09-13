# NB-102 — dimensionless Menger curvature controls hierarchical three-state confluence

**Status:** `EXACT-DERIVED + CANONICAL-BLASCHKE-GEOMETRY + HIERARCHICAL-THREE-STATE-LAW + MENGER-CURVATURE-CONDITIONING + SCALE-GAUGE-INVARIANT + SOURCE-LOCAL-BOUNDARY`.

`NB-101` identifies reciprocal circumradius as the singular shear scale for a **regular common-scale** three-state collision

\[
\lambda_j=\lambda_*+\varepsilon w_j+O(\varepsilon^2)
\]

with distinct first-order offsets. It explicitly leaves open a hierarchical collision in which, for example, one pair is separated at scale `epsilon^2` while the third point is only separated at scale `epsilon`. Such packets are not a technical corner case: a source theorem about actual zeta zeros cannot assume that every nearby triple has comparable pairwise gaps.

The common-scale hypothesis is in fact unnecessary. For an arbitrary sufficiently local triple, the canonical three-state conditioning is controlled, up to universal local constants, by one scale-invariant geometric quantity: **the Menger curvature multiplied by the horizontal half-plane scale**.

Let `lambda_1,lambda_2,lambda_3` be three distinct points in the open right half-plane and put

\[
a_1=\Re\lambda_1>0,
\qquad
c(\lambda_1,\lambda_2,\lambda_3)
=
\frac{4\,\operatorname{Area}(\lambda_1,\lambda_2,\lambda_3)}
{|\lambda_1-\lambda_2|\,|\lambda_1-\lambda_3|\,|\lambda_2-\lambda_3|},
\tag{1}
\]

with `c=0` for a collinear triple. Thus `c=1/R`, where `R` is the Euclidean circumradius. Define the dimensionless local curvature

\[
\mathcal K
:=
a_1 c(\lambda_1,\lambda_2,\lambda_3)
=
\frac{a_1}{R}.
\tag{2}
\]

Let `C(lambda_1,lambda_2,lambda_3)` be the canonically deflated normalized half-line state Gram of `NB-095`--`NB-101`, in the displayed ordering. There exists an absolute `delta_0>0` such that whenever

\[
\delta
:=
\frac{\max(|\lambda_2-\lambda_1|,|\lambda_3-\lambda_1|)}{a_1}
\le \delta_0,
\tag{3}
\]

one has

\[
\boxed{
\kappa_2(C(\lambda_1,\lambda_2,\lambda_3))
\asymp
(1+\mathcal K)^4.
}
\tag{4}
\]

The constants in `(4)` are independent of all pairwise aspect ratios. In particular, for any sequence of relative local confluences `delta -> 0`, even if one pair is arbitrarily smaller than the others,

\[
\boxed{
\sup \kappa_2(C)<\infty
\quad\Longleftrightarrow\quad
\mathcal K=O(1).
}
\tag{5}
\]

If `mathcal K -> infinity`, the two collective third-column shears satisfy

\[
|r_{13}|=(2+o(1))\mathcal K,
\qquad
|r_{23}|=(2+o(1))\mathcal K,
\tag{6}
\]

and therefore `kappa_2(C)=Theta(mathcal K^4)`. Thus a tiny nested pair does **not** create a new conditioning scale by itself. The obstruction is the curvature of the whole three-point packet.

## 1. Exact gauge and scale reduction

Two exact symmetries of the canonical half-line construction make the natural invariant visible before any expansion.

A common imaginary translation

\[
\lambda_j\mapsto\lambda_j-i\tau
\tag{7}
\]

leaves the normalized Cauchy Gram and the canonical deflation coefficients unchanged up to the harmless state phases already used in `NB-098`--`NB-101`. A common positive dilation

\[
\lambda_j\mapsto c\lambda_j,
\qquad c>0,
\tag{8}
\]

leaves them exactly unchanged: every numerator and denominator in the normalized Cauchy factor `Q` and the deflation factor `T` has the same homogeneous degree.

Hence translate by `-Im(lambda_1)` and divide by `a_1`. It is enough to prove `(4)` for

\[
\lambda_1=1,
\qquad
\lambda_2=1+u,
\qquad
\lambda_3=1+v,
\tag{9}
\]

with `max(|u|,|v|)<=delta_0`. Under this normalization the Menger curvature of the triangle `(0,u,v)` is exactly the original dimensionless curvature `mathcal K` because Euclidean curvature scales inversely under dilation.

Write

\[
b_2=1+\Re u,
\qquad
b_3=1+\Re v,
\tag{10}
\]

and let `M=QT` be the upper-triangular factor used in `NB-098`. Its diagonal entries have modulus one; row-phase normalization therefore turns `M` into the positive-diagonal Cholesky factor `R` of `C` without changing any off-diagonal magnitude.

## 2. The singular part is one angular divided difference

For `z != 0` define the unit phase

\[
q(z)=\frac{\bar z}{z}
\tag{11}
\]

and the divided difference

\[
D(u,v)
:=
\frac{q(v)-q(u)}{v-u}.
\tag{12}
\]

A direct calculation gives

\[
|D(u,v)|
=
\frac{2|\Im(u\bar v)|}
{|u|\,|v|\,|v-u|}
=
c(0,u,v)
=
\mathcal K.
\tag{13}
\]

Thus the relevant divided difference of the chord-direction phase is *exactly* the Menger curvature of the normalized triple.

The pairwise entry remains uniformly harmless:

\[
M_{12}
=
\frac{2\sqrt{b_2}(u-\bar u)}
{u(2+\bar u)},
\qquad
|M_{12}|\ll1.
\tag{14}
\]

For the second collective entry introduce

\[
S(z)=\frac{2+z}{2+\bar z},
\qquad
A(u,v)=\frac{2+v+\bar u}{2+u+\bar v}.
\tag{15}
\]

Exact substitution in the canonical formulas gives

\[
M_{23}
=
\frac{2\sqrt{b_2b_3}}{v-u}
\left[q(v)S(v)A(u,v)-q(u)S(u)\right].
\tag{16}
\]

Now set

\[
H(z)=q(z)(S(z)-1)
=
q(z)\frac{z-\bar z}{2+\bar z},
\qquad H(0):=0.
\tag{17}
\]

On a fixed disk `|z|<=delta_0<1`, `H` is uniformly Lipschitz. Although `q(z)` itself has an angular singularity at zero, the factor `z-bar(z)` restores one radial power. Moreover

\[
A(u,v)-1
=
\frac{(v-u)-(\bar v-\bar u)}{2+u+\bar v}
=O(|v-u|).
\tag{18}
\]

Using `qS=q+H` in `(16)` therefore yields, **uniformly with no lower bound on any pairwise separation**, 

\[
\boxed{
M_{23}
=
2\sqrt{b_2b_3}\,D(u,v)+O(1).
}
\tag{19}
\]

This is where the hierarchical issue is resolved: the remainder is Lipschitz in the *smallest* separation and does not acquire a factor such as `|u|/|v-u|`.

## 3. The other collective entry has the same curvature scale

The remaining third-column coefficient can be kept exact. From the same `Q,T` formulas,

\[
M_{13}=2\sqrt{b_3}\,B(u,v),
\tag{20}
\]

where

\[
\begin{aligned}
B(u,v)={}&
\frac{2+\bar u}{uv}
-
\frac{(2+u+\bar u)(2+u)}
{(2+\bar u)(v-u)u}\\
&+
\frac{(2+v)(2+v+\bar u)}
{(2+\bar v)v(v-u)}.
\end{aligned}
\tag{21}
\]

The apparent small denominators in `(21)` cancel in the same geometric combination. Specifically,

\[
B(u,v)=-D(u,v)+J(u,v),
\qquad
|J(u,v)|\ll1
\tag{22}
\]

uniformly on the local disk, again without any aspect-ratio hypothesis.

For a direct stress check of this cancellation, write

\[
u=x+iy,
\qquad
v=s+it,
\qquad
d_x=x-s,
\qquad
d_y=y-t.
\tag{23}
\]

Putting `(21)+D` over a common denominator gives

\[
J(u,v)
=
\frac{-2iK}
{v(2+\bar u)(2+\bar v)(u-v)},
\tag{24}
\]

with

\[
\begin{aligned}
K={}&2d_xt-2d_ys-4id_yt+d_x^2t-2id_xd_yt+2d_xst\\
&-d_y^2t-d_ys^2-2id_yst-d_yt^2.
\end{aligned}
\tag{25}
\]

Every monomial in `K` contains both one factor from `(d_x,d_y)` and one from `(s,t)`. Hence, on a fixed small disk,

\[
|K|\ll |u-v|\,|v|,
\tag{26}
\]

which proves the uniform bound in `(22)` even when `|u-v|` is much smaller than `|u|` and `|v|`, or when `|v|` is much smaller than `|u|`.

Consequently

\[
\boxed{
M_{13}
=
-2\sqrt{b_3}\,D(u,v)+O(1).
}
\tag{27}
\]

Equations `(14)`, `(19)`, and `(27)` are the hierarchical extension of the common-scale expansion in `NB-101`.

## 4. Conditioning is equivalent to dimensionless Menger curvature

After row-phase normalization write

\[
R=
\begin{pmatrix}
1&x&y\\
0&1&z\\
0&0&1
\end{pmatrix}.
\tag{28}
\]

Since `b_2,b_3=1+o(1)` in a confluence, `(14)`, `(19)`, `(27)` and `|D|=mathcal K` give

\[
|x|\ll1,
\qquad
|y|+|z|\ll1+\mathcal K,
\tag{29}
\]

while for sufficiently large `mathcal K`,

\[
|y|,|z|\gg\mathcal K.
\tag{30}
\]

Therefore

\[
\|R\|_2\asymp1+\mathcal K.
\tag{31}
\]

The inverse is

\[
R^{-1}
=
\begin{pmatrix}
1&-x&xz-y\\
0&1&-z\\
0&0&1
\end{pmatrix}.
\tag{32}
\]

The upper bound in `(29)` gives `||R^(-1)||_2 << 1+mathcal K`, and the `(2,3)` entry gives the matching lower bound once `mathcal K` is large; for bounded `mathcal K` both norms are bounded above and below by fixed constants. Hence

\[
\|R^{-1}\|_2\asymp1+\mathcal K.
\tag{33}
\]

Finally `C=R^*R`, so

\[
\kappa_2(C)
=
\kappa_2(R)^2
\asymp
(1+\mathcal K)^4,
\tag{34}
\]

which proves `(4)`--`(6)`.

The classification is insensitive to a nested collision tree. For example, take one pair at scale `epsilon^m` and the third point at scale `epsilon`, with any fixed or growing `m>1`. If the tiny pair and the outer chord meet at a nonvanishing angle, then `mathcal K asy epsilon^(-1)` and the same quartic blow-up of `NB-098` returns. If the three points instead lie on a `C^2`-scale arc with bounded geometric curvature, then `mathcal K=O(1)` and the canonical three-state conditioning stays bounded no matter how tiny the inner pair becomes.

## 5. What this changes for the zeta source problem

For a zeta zero `rho=beta+i gamma`, the state coordinate is

\[
\lambda=\rho-\frac12
=(\beta-\tfrac12)+i\gamma.
\tag{35}
\]

`NB-101` phrased the required regularity as first-order collinearity for common-scale packets. The present result gives the scale-free version that survives arbitrary local gap ratios.

For every right-half zero triple that is small relative to its horizontal distance from the critical line, the relevant source quantity is

\[
\boxed{
(\beta_1-\tfrac12)
\,c(\rho_1,\rho_2,\rho_3).
}
\tag{36}
\]

A zeta-specific rescue of this canonical representation would have to keep `(36)` uniformly bounded on the zero packets that enter the approximation argument, or provide a target-aware mechanism that tolerates the resulting shear. Merely controlling the smallest ordinate gap is not enough, and a much smaller nested pair is not automatically worse: what matters is how sharply the packet bends in the `(beta-1/2,gamma)` plane.

The positive-dilation invariance also refines the boundary caveat of `NB-101`. A simultaneous approach `beta-1/2 -> 0` is not by itself a new singular regime. If the whole packet diameter is `o(beta-1/2)`, dilation by the horizontal scale reduces it to the same local theorem and `(36)` is the correct dimensionless invariant. What remains outside the theorem is the genuinely boundary-scale regime

\[
\operatorname{diam}\{\lambda_1,\lambda_2,\lambda_3\}
\not=o(\beta_1-\tfrac12),
\tag{37}
\]

where normalization no longer produces a small interior packet.

This still does **not** convert state conditioning into Nyman target distance. The representation warning from `NB-004` and the target-aware branch of this line remains in force: `(34)` classifies one canonical state geometry, not the approximation error itself.

## 6. Prior-art and novelty boundary

The appearance of Menger curvature beside a Cauchy kernel is not claimed as a new phenomenon. Mel'nikov's curvature method classically connects three-point symmetrizations of the Cauchy kernel with Menger curvature; see M. S. Mel'nikov, *Analytic capacity: discrete approach and curvature of measure*, Sb. Math. 186 (1995), 827--846, DOI `10.1070/SM1995v186n06ABEH000045`, and the Melnikov--Verdera Cauchy-integral work. That is an important conceptual comparator for `(13)`, but no theorem from that literature is used in the derivation above.

Likewise, reproducing-kernel basis and stability questions in model spaces are classical; relevant boundaries include E. Fricain, *Bases of reproducing kernels in model spaces*, J. Operator Theory 46 (2001), 517--543, and A. Baranov, *Stability of the bases and frames reproducing kernels in model spaces*, Ann. Inst. Fourier 55 (2005), 2399--2422. The Nyman-specific contemporary comparator remains T. A. Ziad's 2026 BNBD Gram-spectral analysis already anchored in `SOURCES.md`.

A targeted audit across those model-space/reproducing-kernel sources, Cauchy-kernel curvature literature, confluent/Takenaka--Malmquist terminology, and recent zeta-zero local-geometry work did not locate the specific canonical-deflation statement `(4)`: uniform quartic conditioning equivalence to dimensionless Menger curvature for an arbitrarily hierarchical three-point confluence. This is a bounded novelty audit, not a priority claim. No external theorem is load-bearing, so `SOURCES.md` does not need a new dependency.

## 7. Falsification controls and boundary conditions

The decisive algebraic control is hierarchical rather than common-scale. Set

\[
\lambda_1=a,
\qquad
\lambda_2=a+\varepsilon^m u,
\qquad
\lambda_3=a+\varepsilon v,
\qquad m>1.
\tag{38}
\]

For generic nonparallel fixed `u,v`, the triangle area is `Theta(epsilon^(m+1))`, its side product is `Theta(epsilon^(m+2))`, and hence `c=Theta(epsilon^(-1))`, independent of `m`. Equations `(19)` and `(27)` therefore predict the same `epsilon^(-1)` shear and `epsilon^(-4)` Gram conditioning for every hierarchy depth `m`. Direct high-precision substitution in the exact `Q,T` formulas reproduces this scale.

The matched bounded control samples a smooth parabolic arc, for example

\[
\lambda(y)=a+k y^2+iy,
\qquad
y\in\{0,\varepsilon^m,\varepsilon\}.
\tag{39}
\]

Its Menger curvature remains bounded as `epsilon -> 0`, uniformly in fixed `m`, and exact substitution keeps all three canonical Cholesky entries bounded. Exact collinear nested triples have `c=0` and are also bounded, even though one pair can be arbitrarily closer than the third point.

The theorem requires three distinct states and relative interior locality `(3)`. It does not cover genuine multiple zeros, which require the confluent/Jordan state system already separated in `NB-098`; nor does it cover boundary-scale packets `(37)`. It also remains a three-state theorem: a four-or-more-state system can contain collective shear not determined by the maximum curvature of one selected triple, and that higher-cardinality question is not settled here.

## Consequence

`NB-101` left two geometric loopholes: unequal collision scales and simultaneous motion of the horizontal base. The first is now closed completely, and the second is closed whenever the packet is local relative to its half-plane depth. The canonical three-state system does not care how deep the pairwise collision hierarchy is. Its conditioning scale is

\[
\boxed{
\kappa_2(C)^{1/4}
\asymp
1+
(\Re\lambda_1)
\,c(\lambda_1,\lambda_2,\lambda_3).
}
\tag{40}
\]

Thus the next source question can be stated without choosing a symmetric slice or comparable-gap model: **do the off-critical zeta-zero triples relevant to Nyman approximation have uniformly bounded dimensionless Menger curvature, or must the argument bypass canonical state conditioning?**