# PF-082 — the prime endpoint Schwarzian controls the first finite-scale length defect

**Status:** `POSITIVE / EXACT + ASYMPTOTIC`; narrow candidate bridge between the exact prime-circle embedding and localized prime-flute length/spectral data.

The cusp-side tangents of PF-029 deliberately replace the exact scaled prime endpoint

\[
V(p):=\pi\cot\frac{\pi}{p}
\]

by its affine shadow `p`.  PF-029/PF-034 show that this retains the finite multi-gap cross-ratios that survive in a pointed hyperbolic tangent.  The question here is what the **first Möbius-invariant correction** is when one does *not* discard the exact orthogonal-circle endpoint geometry.

There is an unexpectedly rigid answer: the exact endpoint map has a closed-form Schwarzian, and consequently every fixed four-point cross-ratio has no projective correction at orders `P^-2` or `P^-3`; the first correction is forced at order `P^-4`.

## 1. Exact projective curvature of the endpoint map

For a locally injective real function `f`, write

\[
S(f)=\frac{f'''}{f'}-\frac32\left(\frac{f''}{f'}\right)^2
\]

for its Schwarzian derivative.  The Schwarzian vanishes exactly on Möbius maps and obeys

\[
S(f\circ g)=((Sf)\circ g)(g')^2+Sg.
\]

Since

\[
S(\cot x)=2
\]

and `x -> pi/x` is Möbius, post-composition by the affine factor `pi` does not change the Schwarzian and we get the **exact identity**

\[
\boxed{
S\!\left(\pi\cot\frac{\pi}{p}\right)
=\frac{2\pi^2}{p^4}.
}
\]

Equivalently, for the cusp-side re-marking of a bounded pattern

\[
F_P(\eta)=V(P+\eta)-P,
\]

one has exactly

\[
\boxed{
S_\eta(F_P)=\frac{2\pi^2}{(P+\eta)^4}.
}
\]

Thus the linear tangent `eta` is not merely the first term of an ordinary Taylor approximation.  It is the **osculating projective/Möbius geometry** of the exact prime endpoint map, and its projective defect is of order `P^-4`.

This is compatible with the elementary expansion

\[
V(p)=p-\frac{\pi^2}{3p}-\frac{\pi^4}{45p^3}+O(p^{-5}),
\]

but the Schwarzian identity is stronger: all lower-order affine/projective distortions are automatically invisible to cross-ratios.

## 2. First correction to an exact four-prime cross-ratio

Fix bounded real offsets

\[
A<B<C<D
\]

and set

\[
X=B-A,\qquad Y=C-B,\qquad Z=D-C.
\]

For the linear/tangent configuration define the separator cross-ratio

\[
\chi_0
=\frac{(C-B)(D-A)}{(B-A)(D-C)}
=\frac{Y(X+Y+Z)}{XZ}.
\]

For the **exact** prime-circle endpoints define

\[
\chi_P
=
\frac{(V(P+C)-V(P+B))(V(P+D)-V(P+A))}
     {(V(P+B)-V(P+A))(V(P+D)-V(P+C))}.
\]

Scaling by `pi` and translating by `P` do not alter this cross-ratio, so this is the same Möbius invariant obtained directly from the exact endpoints `cot(pi/p)`.

For fixed `x<y`, direct expansion gives

\[
\frac{V(P+y)-V(P+x)}{y-x}
=
1+\frac{a}{P^2}
-\frac{a(x+y)}{P^3}
+\frac{a(x^2+xy+y^2)+c}{P^4}
+O(P^{-5}),
\]

where

\[
a=\frac{\pi^2}{3},\qquad c=\frac{\pi^4}{15}.
\]

Taking logarithms and combining the four differences in `chi_P`, the complete `P^-2` and `P^-3` contributions cancel, as do the pair-independent fourth-order terms.  What remains is

\[
\boxed{
\log\frac{\chi_P}{\chi_0}
=
-\frac{\pi^2}{3P^4}(C-A)(D-B)
+O(P^{-5}).
}
\]

Equivalently,

\[
\boxed{
\chi_P
=
\chi_0\left[
1-\frac{\pi^2}{3P^4}(X+Y)(Y+Z)
+O(P^{-5})
\right].
}
\]

The coefficient is precisely the infinitesimal cross-ratio distortion predicted by the Schwarzian:

\[
-\frac16 S(V)(P)(C-A)(D-B)
=
-\frac{\pi^2}{3P^4}(C-A)(D-B).
\]

So the cancellation is projective, not accidental algebra in the cotangent series.

## 3. Exact hyperbolic separator length inherits the `P^-4` defect

PF-004 gives, for any four ordered exact boundary endpoints, the primitive simple separating geodesic length

\[
L=4\operatorname{arsinh}\sqrt\chi.
\]

Hence for the exact four-prime block

\[
L_P=4\operatorname{arsinh}\sqrt{\chi_P},
\]

while the cusp-side tangent predicts

\[
L_0=4\operatorname{arsinh}\sqrt{\chi_0}.
\]

Differentiating `4 asinh(sqrt(chi))` and inserting the cross-ratio expansion yields

\[
\boxed{
L_P
=
L_0
-\frac{2\pi^2}{3P^4}
(C-A)(D-B)
\tanh\frac{L_0}{4}
+O(P^{-5}).
}
\]

In gap variables,

\[
\boxed{
L_P
=
L_0
-\frac{2\pi^2}{3P^4}
(X+Y)(Y+Z)
\tanh\frac{L_0}{4}
+O(P^{-5}).
}
\]

This is a genuine finite-scale correction to a real primitive geodesic of the exact prime-flute.  It is not a generating function of the gaps.

## 4. Relation to the distinguished cuffs

For bounded prime gaps at scale `P`, the distinguished cuffs satisfy

\[
\ell_i(P)=2\log\frac{4P}{d_i}+o(1).
\]

The tangent limit removes the common `2 log P` scale and preserves only relative data such as

\[
e^{-(\ell_i-\ell_j)/2}\to d_i/d_j.
\]

PF-082 shows where the discarded **absolute scale first re-enters a Möbius-invariant hyperbolic observable**:

\[
\boxed{
\text{first projective finite-scale defect}\asymp P^{-4}
\asymp e^{-2\ell_{\rm common}}
}
\]

(up to the fixed gap-dependent normalization used to define a common cuff scale).

Thus there is a sharp two-level decomposition:

```text
leading tangent geometry:
    relative gap/cuff ratios;

first exact prime-circle correction:
    P^-4 Schwarzian defect times a multi-gap quadratic factor.
```

This is stronger than merely expanding each cuff separately: individual lower-order `1/P` corrections are coordinate/gauge dependent, while the `P^-4` term above is detected by a cross-ratio and hence by the hyperbolic surface itself.

## 5. Spectral meaning and its limitation

A primitive closed geodesic length is spectral-geometric data.  On the full prime-flute the ordinary global wave/Selberg trace is unusable (PF-036/PF-069), but PF-064 shows that a spatially localized wave kernel on an isolated recurring prime block can recover closed-orbit singularity times before signals can leave through the diverging exterior collar.

For a cutoff/microlocalization containing the separator above, its periodic-orbit singularity therefore occurs at the **exact** time `L_P`, not at `L_0`.  Consequently the localized Laplacian sees the finite-scale shift

\[
\boxed{
\delta t
=
-\frac{2\pi^2}{3P^4}
(X+Y)(Y+Z)
\tanh\frac{L_0}{4}
+O(P^{-5}).
}
\]

This does **not** resurrect a global trace formula, and it does not by itself imply an RH mechanism.  The observable remains spatially localized, exactly as required by the local-before-global principle established by PF-034/PF-050/PF-064.

## 6. Boundary case: the associated projective ODE is universal

The identity

\[
S(V)(p)=\frac{2\pi^2}{p^4}
\]

means that `V` is a projective developing map for the second-order equation

\[
y''+\frac{\pi^2}{p^4}y=0.
\]

This must **not** be sold as a new prime spectral operator: the differential equation is universal in the continuous variable `p`; primality enters only through which values of `p` are sampled.  PC-013/PC-014 already warn that one-dimensional projective/free transfer can manufacture or erase spectral structure.

The substantive information here is instead the Möbius-invariant cross-ratio distortion of the **sampled exact orthogonal-circle geometry**.

## 7. Novelty / prior-art audit

Known ingredients, not claimed as new:

- the Schwarzian derivative, its chain rule, and the fact that it measures infinitesimal cross-ratio distortion;
- `S(cot x)=2` and therefore the displayed Schwarzian identity by elementary composition;
- the cotangent asymptotic series;
- the relation between hyperbolic translation length and four-point cross-ratios;
- microlocal wave-trace localization near a chosen closed geodesic.

Cross-ratio distortion via the Schwarzian is classical (e.g. de Faria--de Melo, *Mathematical Tools for One-Dimensional Dynamics*, Ch. 6; Thurston's projective interpretation of the Schwarzian).  Targeted searches for `pi cot(pi/x)`/Schwarzian combined with prime gaps, prime vertices, Fuchsian flutes, or hyperbolic separator lengths did not locate this specialization.

The potentially new content is narrow:

\[
\boxed{
\text{exact prime-circle endpoint map}
\to
S(V)=2\pi^2/p^4
\to
\text{first hyperbolic multi-gap length defect at }P^{-4}.
}
\]

In particular, novelty is **not** claimed for Schwarzian/cross-ratio theory itself.

## 8. Falsification / next test

The finite algebra can be falsified directly by symbolic or high-precision evaluation of exact prime endpoint quadruples.  For any fixed offsets `A<B<C<D`, verify

\[
P^4\left(\frac{\chi_P}{\chi_0}-1\right)
\longrightarrow
-\frac{\pi^2}{3}(C-A)(D-B).
\]

The next mathematically informative step is to propagate this projective correction through a **finite tangent spectral observable whose derivative in Teichmüller space is known**, rather than merely through a marked geodesic length.  A successful calculation would test whether `P^-4` also becomes the first absolute-scale correction to an eigenvalue or physical scattering pole; failure would show that spectral compression removes this projective defect even though the length spectrum retains it.

## Lean / symbolic candidates

1. Prove `S(pi*cot(pi/p)) = 2*pi^2/p^4` on the nonsingular domain.
2. Prove the fourth-order cross-ratio expansion for fixed `A<B<C<D`.
3. Differentiate `L(chi)=4*asinh(sqrt(chi))` to obtain the length coefficient.
4. Keep the localized-wave consequence outside the first Lean pass; it depends on imported microlocal analysis.
