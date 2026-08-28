# PC-030 — circle-preserving accessory transport is exact and Weil–Petersson-symplectically flat

**Status:** `LITERATURE+DERIVED` + `DECISIVE-NEGATIVE` for any prime-circle mechanism that tries to obtain a nontrivial first-order phase, curvature, or holonomy from tangential Fuchsian accessory parameters while the punctures remain on the original circle.

PC-028 showed that inversion symmetry fixes the radial component of every unit-circle accessory coefficient and kills the common-anchor accessory defect. That left the tangential components as one of the most natural genuinely global pieces of the nonlinear uniformization branch. The next tempting step is to regard those tangential components as a connection over circle-preserving deformations and search for a nonzero Weil–Petersson curvature or Berry-like holonomy.

That route is also obstructed. The circle-preserving deformation space is a real Lagrangian fixed locus of the Weil–Petersson Kähler geometry, and the tangential accessory 1-form is the exact differential of the classical Liouville action restricted to that locus.

## 1. The original circle is a half-dimensional real slice of punctured-sphere moduli

Fix `n>1` and put

\[
m=\varphi(n).
\]

Around the cyclotomic configuration, regard the `m` primitive punctures as ordered movable points

\[
z_1,\dots,z_m
\]

while the three marked punctures `0,1,∞` remain normalized. This is a local chart of

\[
\mathcal M_{0,m+3},
\qquad
\dim_{\mathbb C}\mathcal M_{0,m+3}=m.
\]

The intrinsic prime-circle deformations are those in which all movable punctures remain on the original unit circle. In a chamber with fixed cyclic order, write

\[
z_j=e^{i\theta_j}.
\]

This gives a real `m`-dimensional submanifold

\[
\mathcal L\subset\mathcal M_{0,m+3}.
\]

The anti-Möbius reflection in the original circle is

\[
R(z)=\frac1{\bar z}.
\]

It exchanges `0` and `∞` and fixes the unit circle pointwise. After composing with the corresponding transposition of those two marked labels, it induces an anti-holomorphic involution `sigma` of the marked moduli chart whose action on the movable coordinates is

\[
\boxed{
\sigma(z_1,\dots,z_m)
=\left(\frac1{\bar z_1},\dots,\frac1{\bar z_m}\right).
}
\]

Locally,

\[
\boxed{\mathcal L=\operatorname{Fix}(\sigma).}
\]

Thus the original circle is not an arbitrary restriction imposed after uniformization: it is a canonical real form selected by the same inside/outside reflection already present in the prime-circle geometry.

## 2. The circle slice is Weil–Petersson Lagrangian

Let

\[
(g_{WP},J,\omega_{WP})
\]

be the Weil–Petersson Kähler structure. Permutations of marked punctures and conformal/anti-conformal re-markings act naturally on this geometry, so `sigma` is an anti-holomorphic Weil–Petersson isometry. Therefore

\[
\sigma_*J=-J\sigma_*,
\qquad
\sigma^*g_{WP}=g_{WP}.
\]

Since

\[
\omega_{WP}(v,w)=g_{WP}(Jv,w),
\]

we get

\[
\boxed{
\sigma^*\omega_{WP}=-\omega_{WP}.
}
\]

If `v,w` are tangent to the fixed locus, then `sigma_*v=v` and `sigma_*w=w`, hence

\[
\omega_{WP}(v,w)
=(\sigma^*\omega_{WP})(v,w)
=-\omega_{WP}(v,w).
\]

Thus

\[
\boxed{
\omega_{WP}|_{\mathcal L}=0.
}
\]

Because `dim_R L=m=dim_C M_{0,m+3}`, the fixed locus has exactly half the ambient real dimension. Therefore

\[
\boxed{
\mathcal L\text{ is a Weil–Petersson Lagrangian submanifold.}
}
\]

Moreover, a fixed component of a Riemannian isometry is totally geodesic, so the same circle slice is locally totally geodesic for `g_WP`.

This is standard Kähler/real-locus geometry, not a new theorem. Its consequence for the surviving prime-circle uniformization sector is the relevant point here.

## 3. Reflection fixes the radial accessory component throughout the whole circle slice

Let `Q` be the Fuchsian uniformizing projective connection for a configuration in `L`. At a movable puncture `z_j` write

\[
Q(z)=\frac1{2(z-z_j)^2}
+\frac{c_j}{z-z_j}+O(1).
\]

Naturality under the anti-Möbius reflection gives the real-structure relation

\[
\boxed{
Q(z)=z^{-4}\,\overline{Q(1/\bar z)}.
}
\]

Expanding at the fixed point `z_j in S^1` yields

\[
\boxed{
z_jc_j+\overline{z_jc_j}=-1.
}
\]

Hence throughout the circle-preserving moduli slice,

\[
\boxed{
\operatorname{Re}(z_jc_j)=-\frac12.
}
\]

Define the remaining tangential datum by

\[
\boxed{
\tau_j:=\operatorname{Im}(z_jc_j),
\qquad
z_jc_j=-\frac12+i\tau_j.
}
\]

At the cyclotomic point this recovers the tangential accessory components isolated in PC-028. The present formulation shows that the radial constraint is not merely a discrete symmetry accident of one root-of-unity configuration: it holds along every deformation that keeps the marked punctures on the original circle.

## 4. The tangential accessory 1-form is exact

Takhtajan–Zograf theory supplies a real classical Liouville action whose derivatives generate the Fuchsian accessory parameters and whose complex Hessian gives the Weil–Petersson Kähler form. Absorb the universal convention-dependent constant into a normalized action `S` so that

\[
\boxed{
c_j=-\frac{\partial S}{\partial z_j}.}
\]

Because `S` is real,

\[
dS
=-\sum_j\left(c_j\,dz_j+\bar c_j\,d\bar z_j\right).
\]

On the circle slice,

\[
dz_j=i z_j\,d\theta_j,
\qquad
d\bar z_j=-i\bar z_j\,d\theta_j.
\]

Therefore

\[
\begin{aligned}
dS|_{\mathcal L}
&=-\sum_j\left(i z_jc_j-i\overline{z_jc_j}\right)d\theta_j\\
&=2\sum_j\operatorname{Im}(z_jc_j)\,d\theta_j.
\end{aligned}
\]

Thus the complete first-order tangential accessory field satisfies the exact identity

\[
\boxed{
\Theta
:=\sum_{j=1}^{m}\tau_j\,d\theta_j
=\frac12\,d(S|_{\mathcal L}).
}
\]

Consequently,

\[
\boxed{d\Theta=0.}
\]

In local angular coordinates this is the reciprocity relation

\[
\boxed{
\frac{\partial\tau_j}{\partial\theta_k}
=
\frac{\partial\tau_k}{\partial\theta_j}.
}
\]

On a fixed cyclic-order chamber, or on its Teichmüller lift, the chamber is contractible. Hence every closed circle-preserving loop satisfies

\[
\boxed{
\oint_\gamma\Theta=0.
}
\]

The tangential accessory vector can be highly nonzero and globally determined, but as a first-order transport field it is a gradient, not a connection with intrinsic curvature.

## 5. Decisive obstruction to a natural remaining branch

After PC-028, a plausible escape was

\[
\text{tangential accessory vector}
\longrightarrow
\text{WP / symplectic curvature}
\longrightarrow
\text{nontrivial phase or holonomy}
\longrightarrow
\text{RH-sensitive operator}.
\]

The two exact facts above block this route while deformations remain faithful to the original circle:

\[
\boxed{\omega_{WP}|_{\mathcal L}=0}
\]

and

\[
\boxed{\Theta=\tfrac12 d(S|_{\mathcal L}).}
\]

So there is neither Weil–Petersson symplectic area enclosed by a two-parameter loop inside the circle slice nor first-order accessory circulation around a loop in an ordered chamber.

In particular, an antisymmetric pair interaction or Berry-like phase extracted only from circle-preserving tangential accessory transport would have to come from an added gauge, a quotient identification, or some structure beyond this canonical first-order uniformization data.

This is the continuous-moduli counterpart of PC-018. PC-018 showed that discrete factor-introduction surgery has zero projective curvature because the Schwarzian defect is an exact cocycle. Here the remaining tangential accessory data are also flat in the relevant first-order sense, now because they are generated by a scalar Liouville action on a Lagrangian real slice.

## 6. What is not ruled out

This does **not** trivialize PC-017 or the nonlinear uniformization defect.

Several sectors remain genuinely open:

- endpoint values of the tangential vector `tau_j` at the cyclotomic configurations;
- symmetric second-variation data of the restricted Liouville action;
- the nonzero Riemannian metric `g_WP|_L` and its curvature, despite the vanishing symplectic form on `L`;
- the full monodromy representation of the Fuchsian equation;
- deformations that leave the circle-preserving real locus;
- nonlinear cross-level quantities that cannot be represented as integration of the first-order accessory 1-form.

A loop that becomes nontrivial only after quotienting by a braid or mapping-class identification is also outside the local statement above. Any arithmetic significance of such a loop would have to be derived from the prime-circle labeling itself; it cannot be attributed to nonzero local Weil–Petersson/accessory curvature on the circle slice.

Thus the surviving gate is narrower: if the PC-017 branch is to reach zeta or the critical line, it must use **symmetric second-order geometry, endpoint monodromy/uniformization data, or a genuinely off-slice/nonlocal coupling**, not first-order tangential holonomy.

## 7. Prior art and novelty audit

The mathematical ingredients are classical:

- Zograf–Takhtajan, *Action of the Liouville equation is a generating function for the accessory parameters and the potential of the Weil-Petersson metric on the Teichmüller space*, Functional Analysis and Its Applications **19** (1985), 219–220, DOI 10.1007/BF01076626.
- P. G. Zograf and L. A. Takhtajan, *On Liouville's equation, accessory parameters, and the geometry of Teichmüller space for Riemann surfaces of genus 0*, Math. USSR-Sb. **60** (1988), 143–161.
- L. A. Takhtajan and P. G. Zograf, *Hyperbolic 2-spheres with conical singularities, accessory parameters and Kähler metrics on M_{0,n}*, Trans. Amer. Math. Soc. **355** (2003), 1857–1867, DOI 10.1090/S0002-9947-02-03243-9.
- The fixed locus of an anti-holomorphic isometry of a Kähler manifold is Lagrangian when it has half dimension; the fixed locus of a Riemannian isometry is totally geodesic. These are standard general facts.

Directed searches for combinations of root-of-unity punctures, unit-circle accessory parameters, real loci of `M_{0,n}`, and Weil–Petersson/Liouville geometry did not locate the prime-circle-specific obstruction formulated here. That absence is **not** a historical novelty claim. The real-locus and Liouville ingredients are classical; the durable contribution is the negative research conclusion for this construction: the tangential data left alive by PC-028 do not generate a new first-order symplectic/holonomy mechanism while one stays on the original circle.
