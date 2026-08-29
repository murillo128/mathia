# PC-031 — the common-anchor orthogonal-circle fan is a null de Sitter generator

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `DECISIVE-NEGATIVE` for prime-circle mechanisms that use only the intrinsic orthogonal-circle / hyperbolic-geodesic pair geometry, its Lorentz Gram matrix, or a raw spectrum of those pairings. No RH claim.

The original prime-circle picture makes one especially natural two-dimensional construction available without adding a new scale: for two boundary vertices, take the generalized Euclidean circle through them that is orthogonal to the original unit circle. In the Poincaré disk this is exactly the hyperbolic geodesic joining the two ideal endpoints.

For the common-anchor fan, this apparently richer geometry collapses much more strongly than a generic projective construction: all of its geodesics lie on one **null generator of the de Sitter space of oriented geodesics**. The canonical Lorentz Gram matrix is therefore the all-ones matrix and has rank one.

## 1. The orthogonal circle is forced by two prime-circle vertices

Let

\[
u=e^{i\alpha},\qquad v=e^{i\beta},
\qquad u\ne v.
\]

If \(u+v\ne0\), the unique Euclidean circle through \(u,v\) orthogonal to the unit circle has center and radius

\[
\boxed{
c_{uv}=\frac{2uv}{u+v}
=\frac{e^{i(\alpha+\beta)/2}}{\cos((\alpha-\beta)/2)}
}
\]

and

\[
\boxed{
r_{uv}
=\frac{|u-v|}{|u+v|}
=\left|\tan\frac{\alpha-\beta}{2}\right|.
}
\]

Indeed,

\[
|c_{uv}|^2=1+r_{uv}^2,
\]

which is exactly the Euclidean orthogonality condition for the two circles. When \(u=-v\), the limiting generalized circle is the diameter line through them.

Thus this construction introduces no free radius, center, or spectral parameter. It is the intrinsic Poincaré-disk geodesic determined by the two original boundary vertices.

## 2. Lorentz duality puts every oriented geodesic in a three-dimensional ambient space

Use the Minkowski form on \(\mathbb R^{2,1}\),

\[
\langle (x,y,t),(x',y',t')\rangle
=xx'+yy'-tt'.
\]

Represent a boundary point by the future light vector

\[
\ell(\theta)=(\cos\theta,\sin\theta,1),
\qquad
\langle\ell(\theta),\ell(\theta)\rangle=0.
\]

For an ordered pair of distinct endpoints \((\alpha,\beta)\), choose the unit spacelike normal

\[
\boxed{
N_{\alpha\beta}
=
\frac{1}{\sin((\alpha-\beta)/2)}
\left(
\cos\frac{\alpha+\beta}{2},
\sin\frac{\alpha+\beta}{2},
\cos\frac{\alpha-\beta}{2}
\right).
}
\]

A direct calculation gives

\[
\langle N_{\alpha\beta},N_{\alpha\beta}\rangle=1
\]

and

\[
\langle N_{\alpha\beta},\ell(\alpha)\rangle
=
\langle N_{\alpha\beta},\ell(\beta)\rangle
=0.
\]

So oriented geodesics form the de Sitter quadric

\[
dS^2=\{N\in\mathbb R^{2,1}:\langle N,N\rangle=1\}.
\]

This immediately yields a general finite-rank obstruction. For any \(M\) orthogonal circles/geodesics with normals \(N_1,\ldots,N_M\), their raw Lorentz Gram matrix

\[
G_{ij}=\langle N_i,N_j\rangle
\]

factors through \(\mathbb R^{2,1}\). Hence

\[
\boxed{\operatorname{rank}G\le3.}
\]

Therefore a spectral construction that uses the canonical pairwise Lorentz products themselves can never develop more than three nonzero spectral directions, no matter how many prime-circle chords are included.

## 3. The common-anchor fan collapses from rank three to rank one

Now keep the distinguished common vertex \(1=e^{i0}\), and join it to a primitive \(n\)-th root

\[
\zeta_n^a=e^{2\pi ia/n},
\qquad
1\le a<n,\qquad(a,n)=1.
\]

Put

\[
\theta_a=\frac{2\pi a}{n}.
\]

Because \(0<\theta_a<2\pi\), the orientation above gives

\[
\boxed{
N_a:=N_{\theta_a,0}
=
\left(
\cot\frac{\theta_a}{2},
1,
\cot\frac{\theta_a}{2}
\right)
=
\left(
\cot\frac{\pi a}{n},
1,
\cot\frac{\pi a}{n}
\right).
}
\]

For any two primitive exponents \(a,b\),

\[
\boxed{
\langle N_a,N_b\rangle
=
\cot\frac{\pi a}{n}\cot\frac{\pi b}{n}
+1
-\cot\frac{\pi a}{n}\cot\frac{\pi b}{n}
=1.
}
\]

Even more strongly,

\[
N_a-N_b
=
\left(
\cot\frac{\pi a}{n}-\cot\frac{\pi b}{n},
0,
\cot\frac{\pi a}{n}-\cot\frac{\pi b}{n}
\right)
\]

is a light vector:

\[
\boxed{\langle N_a-N_b,N_a-N_b\rangle=0.}
\]

The continuous family

\[
N(t)=(t,1,t)
\]

lies in \(dS^2\), and its tangent \(N'(t)=(1,0,1)\) is null. Thus all orthogonal circles through the common boundary point \(1\) lie on a single **lightlike generator of de Sitter space**. Geometrically, the corresponding disk geodesics are asymptotic: they share the same ideal endpoint and their Euclidean orthogonal circles are mutually tangent there.

If the fan contains the \(\varphi(n)\) primitive endpoints, its Lorentz Gram matrix is exactly

\[
\boxed{
G_n=J_{\varphi(n)},
}
\]

the all-ones matrix. Therefore

\[
\boxed{
\operatorname{spec}(G_n)
=
\{\varphi(n),0,\ldots,0\}.
}
\]

The canonical pair geometry has forgotten every primitive angle except the number of rays. It cannot see the common-vertex value \(\Lambda(n)\), primitive gap structure, cyclotomic resultants, or any finer arithmetic ordering.

This is not a large but structured spectrum waiting for an RH interpretation. It is rank one.

## 4. The nondegenerate pair geometry is only cross-ratio geometry

The collapse above is specific to the common anchor, but the generic orthogonal-circle pair invariant also does not produce a new projective package.

For two oriented geodesics with ordered endpoints \((\alpha,\beta)\) and \((\gamma,\delta)\), write

\[
g=
\langle N_{\alpha\beta},N_{\gamma\delta}\rangle.
\]

With the cross-ratio convention already used in PC-026,

\[
X=
[e^{i\alpha},e^{i\beta};e^{i\gamma},e^{i\delta}]
=
\frac{(e^{i\alpha}-e^{i\gamma})(e^{i\beta}-e^{i\delta})}
{(e^{i\alpha}-e^{i\delta})(e^{i\beta}-e^{i\gamma})},
\]

a direct trigonometric simplification gives, for nondegenerate ordered endpoints,

\[
\boxed{
X=\frac{g-1}{g+1},
\qquad
g=\frac{1+X}{1-X}.
}
\]

Swapping the orientation of one geodesic sends \(g\mapsto-g\) and applies the corresponding standard anharmonic transformation to \(X\), so the equivalence is independent of the chosen presentation.

Thus the Lorentz/inversive relation between two orthogonal circles is exactly the same information as the projective cross-ratio of their four ideal endpoints. At a prime level, PC-026 already shows that four-distinct-endpoint cross-ratios lie in the classical cyclotomic-unit package.

For the anchored fan two geodesics share the endpoint \(1\), so the four-point cross-ratio degenerates to \(X=0\), exactly matching \(g=1\). The de Sitter null collapse is therefore the geometric form of that projective degeneration.

## 5. Horocycle decoration would add structure not present in the prime circle

One might try to rescue finite distances between ideal endpoints by truncating geodesics and using Penner \(\lambda\)-lengths. That changes the object.

An ideal geodesic has infinite hyperbolic length. A finite \(\lambda\)-length is defined only after choosing horocycles at the ideal endpoints. Decorated Teichmüller space records precisely these positive decoration parameters; the horocycle choices are extra data over the undecorated moduli.

The original prime-circle construction specifies roots of unity and the common anchor but no canonical horocycle scale at each vertex. Consequently a \(\lambda\)-length spectrum would import a new gauge unless a decoration can first be derived intrinsically from the circle geometry.

After removing decoration dependence, the standard ideal-quadrilateral/shear information is again projective cross-ratio data, returning to the previous section and PC-026 rather than creating a new orthogonal-circle invariant.

## 6. Decisive obstruction

This rules out the natural route

\[
\boxed{
\text{common anchor}
\to
\text{orthogonal circles}
\to
\text{de Sitter/Lorentz pair geometry}
\to
\text{large canonical spectrum}
\to
\text{RH}.
}
\]

There are two levels of obstruction:

1. for arbitrary finitely many disk geodesics, the raw Lorentz Gram matrix has rank at most \(3\);
2. for the actual common-anchor fan forced by the prime-circle construction, it is exactly rank \(1\).

Applying an entrywise nonlinear function to the Gram entries can of course raise matrix rank, but that is no longer a spectrum forced by the linear Lorentz geometry. In the anchored case every Gram entry is the same number \(1\), so even such an entrywise kernel remains constant unless it also imports labels or non-pairwise data.

For non-anchored prime-level pairs, a nonlinear kernel is a chosen function of the cross-ratios already classified by PC-026. It may be mathematically interesting, but the orthogonal-circle construction itself has supplied no new arithmetic state.

## 7. Prior art and novelty audit

The general geometric ingredients are classical.

- The Poincaré-disk description of hyperbolic geodesics as generalized Euclidean circles orthogonal to the boundary, and the Lorentz/hyperboloid model, are standard; Ratcliffe is a comprehensive reference.
- Hyperbolic/de Sitter duality via unit spacelike normals in Minkowski space is classical. Asmus gives an explicit modern treatment of the duality and de Sitter causal geometry.
- Cross-ratio dynamics of ideal polygons is already an integrable projective subject. Arnold–Fuchs–Izmestiev–Tabachnikov explicitly formulate ideal-polygon relations by constant cross-ratio and identify the orthogonal case as a special cross-ratio value.
- Penner's decorated Teichmüller theory is the standard source of \(\lambda\)-lengths and makes the horocycle decoration explicit.

No novelty is claimed for these facts. The durable prime-circle-specific result is the obstruction obtained by inserting the **common anchored roots-of-unity fan** into that classical geometry:

\[
\boxed{
N_a=(\cot(\pi a/n),1,\cot(\pi a/n))
}
\]

lies on one null de Sitter generator, forcing

\[
\boxed{
G_n=J_{\varphi(n)}.
}
\]

Directed prior-art checking did not reveal a reason to regard this algebraic specialization as a new general theorem. Its value is as a decisive scope result for the prime-circle research program.

## 8. Boundary and audit test

This result does **not** rule out:

- the nonlinear Fuchsian uniformization defect of PC-017;
- collective monodromy or Liouville/Weil-Petersson second-order data surviving PC-030;
- genuinely nonseparable cross-level operators;
- quantities that use more than intrinsic pairwise orthogonal-circle geometry.

Those objects solve or couple a global problem rather than taking a Gram spectrum of fixed de Sitter normals.

The finding has a simple exact audit test. For any \(n>2\), enumerate the primitive exponents \(a\), form

\[
N_a=(\cot(\pi a/n),1,\cot(\pi a/n)),
\]

and verify symbolically that every Lorentz pairing equals \(1\). Any proposed prime-circle mechanism claiming a nontrivial eigenvalue splitting from the **raw common-anchor de Sitter Gram matrix** contradicts this identity.
