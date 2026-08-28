# PF-093 — the four-punctured prime-tangent arithmetic locus is exactly five gap ratios

**Status:** `EXACT CLASSIFICATION + DECISIVE NEGATIVE FOR THE HIERARCHICAL MODULAR/HECKE BRANCH`.

PF-044 showed that the two-prime / one-gap tangent is the universal thrice-punctured sphere `Gamma(2)\H`, so its modular Riemann-zeta scattering factor is completely gap-blind.  PF-029 then identified the three-prime tangent as the first genuinely modulus-sensitive case: it is the double of an ideal quadrilateral, with modulus given exactly by the ratio of the two consecutive gaps.

This note asks whether that first nontrivial tangent can nevertheless remain arithmetic, so that its gap-sensitive spectrum might inherit modular/Hecke structure from an arithmetic Fuchsian lattice.

For prime-derived tangents the answer is rigid.  If

\[
r:=\frac{d_1}{d_2}>0,
\]

then the four-punctured tangent is arithmetic **if and only if**

\[
\boxed{
 r\in\left\{\frac14,\frac12,1,2,4\right\}.
}
\]

In particular every sufficiently hierarchical tangent with `d_1/d_2 -> 0` is non-arithmetic.  This includes the pinching regimes in which PF-045--PF-047 and PF-090--PF-091 obtain the strongest gap-sensitive small-eigenvalue / residual-pole effects.

The result is an exact consequence of the orthogonal-circle tangent geometry plus Vinberg's arithmeticity criterion for noncompact reflection groups.  It does **not** replace the exact prime endpoints by an ad hoc arithmetic model: the ideal quadrilateral is the genuine cusp-side pointed tangent of the exact `pi cot(pi/p)` geometry established in PF-029/PF-034.

## 1. Exact ideal-quadrilateral data from two consecutive gaps

Take three ordered offsets

\[
\eta_1<\eta_2<\eta_3,
\qquad
d_1=\eta_2-\eta_1,
\qquad
d_2=\eta_3-\eta_2,
\]

inside a recurrent isolated prime block.  PF-029 gives the four-punctured tangent `Y_r`, the double of the ideal quadrilateral with vertices

\[
-\eta_3,-\eta_2,-\eta_1,\infty.
\]

The two opposite simple separators satisfy exactly

\[
\sinh^2\!\frac{L_1}{4}=r,
\qquad
\sinh^2\!\frac{L_2}{4}=\frac1r.
\]

Hence

\[
\boxed{
\cosh\frac{L_1}{2}=1+2r,
\qquad
\cosh\frac{L_2}{2}=1+\frac2r.
}
\]

Let `H_1,...,H_4` be the four side mirrors of the ideal quadrilateral in cyclic order. Adjacent mirrors meet at an ideal point, hence their Lorentzian Gram entry is `-1`. Opposite mirrors are ultraparallel.  The product of reflections in two ultraparallel mirrors a distance `delta` apart has translation length `2 delta`; the products across the two pairs of opposite sides are precisely the two separator words above. Therefore

\[
\delta_1=L_1/2,
\qquad
\delta_2=L_2/2.
\]

With unit outward Lorentzian normals the Gram matrix is consequently

\[
\boxed{
G(r)=
\begin{pmatrix}
1&-1&-(1+2r)&-1\\
-1&1&-1&-(1+2/r)\\
-(1+2r)&-1&1&-1\\
-1&-(1+2/r)&-1&1
\end{pmatrix}.
}
\]

Its determinant is zero, as it must be for four normals in the three-dimensional Lorentz space underlying `H^2`; its nonzero part has the required hyperbolic signature.

Because `d_1,d_2` are integer offset gaps, `r` is rational. Thus all entries of `G(r)` are rational.

## 2. Vinberg's criterion collapses arithmeticity to two divisibility conditions

For a noncompact hyperbolic Coxeter group, Vinberg's arithmeticity criterion says that, over field of definition `Q`, the reflection group is arithmetic exactly when every cycle of `2G` is a rational integer.  In the present rational Gram matrix this criterion is particularly simple.

Put

\[
x=1+2r,
\qquad
y=1+2/r.
\]

The length-two Vinberg cycle through the first pair of opposite mirrors is

\[
(2g_{13})(2g_{31})=4x^2.
\]

Arithmeticity therefore implies

\[
4x^2\in\mathbb Z.
\]

But `2x` is rational.  A rational number whose square is an integer is itself an integer, so

\[
2x=2+4r\in\mathbb Z,
\]

and hence

\[
\boxed{4r\in\mathbb Z.}
\]

The other opposite pair gives in exactly the same way

\[
\boxed{4/r\in\mathbb Z.}
\]

Conversely, if both `4r` and `4/r` are integers, then

\[
2x=2+4r\in\mathbb Z,
\qquad
2y=2+4/r\in\mathbb Z.
\]

Every entry of `2G(r)` is then an integer: adjacent entries are `-2` and the two opposite entries are `-2x,-2y`.  Therefore every Vinberg cycle is automatically an integer, so the reflection group is arithmetic.

Thus

\[
\boxed{
Y_r\text{ is arithmetic}
\iff
4r\in\mathbb Z\ \text{and}\ 4/r\in\mathbb Z.
}
\]

Arithmeticity is unchanged on passing to the orientation-preserving index-two subgroup that uniformizes the doubled quadrilateral.

## 3. There are exactly five rational arithmetic moduli

Set

\[
m=4r,
\qquad
n=4/r.
\]

The two integrality conditions give positive integers `m,n` satisfying

\[
mn=16.
\]

Therefore `m` is a positive divisor of `16`, and

\[
\boxed{
r\in\left\{\frac14,\frac12,1,2,4\right\}.}
\]

Conversely each of these five ratios satisfies the two conditions and hence is arithmetic.

Since every noncompact arithmetic Fuchsian lattice is commensurable with the modular group, these five points are exactly the modular-commensurability locus inside the one-real-dimensional reflection-symmetric four-punctured tangent family arising from rational prime offsets.

This does **not** say that all five orientation-preserving groups are congruence groups, nor that their scattering determinants reduce to a single elementary Riemann-zeta quotient.  Arithmetic / modular commensurability is the justified conclusion.

## 4. Translation to distinguished cuffs

For occurrences of a fixed bounded offset pattern near prime scale `P`, the distinguished cuffs satisfy

\[
\ell_i(P)=2\log\frac{4P}{d_i}+o(1),
\]

and therefore

\[
\boxed{
r=\frac{d_1}{d_2}
=\lim_{P\to\infty}
\exp\!\left[-\frac{\ell_1(P)-\ell_2(P)}2\right].}
\]

The arithmetic locus is consequently the discrete asymptotic cuff-contrast set

\[
\boxed{
\ell_1-\ell_2
\longrightarrow
\{-4\log2,-2\log2,0,2\log2,4\log2\},
}
\]

with the ordering corresponding to `r=4,2,1,1/2,1/4`.

Thus arithmeticity does not occur along a continuous range of prime-gap fluctuations.  It picks out five isolated relative-cuff shapes.

## 5. Hierarchical prime tangents are forced out of the arithmetic locus

PF-046 constructs, for arbitrary `B`, fixed prime candidate patterns so spread out that **whatever prime subset the Maynard--Tao/Pintz step selects**, its first two consecutive internal gaps satisfy

\[
\frac{d_1}{d_2}<\frac1{B-1}.
\]

For `B>5`,

\[
0<r<\frac14.
\]

If the tangent has exactly four cusps, Section 3 immediately says it is non-arithmetic.

The conclusion also holds when the isolated tangent has more cusps.  The two polygon mirrors bounding the first nested separator are still mirrors of the full ideal-polygon reflection group, and their Vinberg length-two cycle is

\[
4(1+2r)^2.
\]

For `0<r<1/4`,

\[
2<2(1+2r)<3.
\]

Since this quantity is rational but not an integer, its square cannot be an integer.  The necessary Vinberg integrality condition therefore fails already on this two-mirror cycle. Hence

\[
\boxed{
\text{every sufficiently spread PF-046 prime tangent is non-arithmetic.}
}
\]

The same applies to the genuinely pinching regimes used in PF-045/PF-047 and in the resolved multiscale Laplace-memory results PF-090/PF-091: once the relevant ratio tends to zero, the family eventually lies strictly outside the arithmetic locus.

## 6. Spectral consequence: the strongest gap-sensitive branch is not hidden modular spectrum

PF-044 and the present classification give a useful dichotomy.

The minimal tangent is

\[
\text{one gap}
\longrightarrow
S_{0,3}\cong\Gamma(2)\backslash\mathbb H,
\]

so it is arithmetic but has **no modulus**: its Riemann-zeta scattering factor is universal and gap-blind.

At the first topology where a prime-gap modulus survives,

\[
\text{two gaps}
\longrightarrow
Y_r\in\mathcal M_{0,4},
\]

arithmeticity survives only at the five isolated ratios above.  The hierarchical regimes that force small eigenvalues, residual scattering poles, and the second-order upstream-memory terms of PF-090/PF-091 are all non-arithmetic.

Therefore the branch

\[
\boxed{
\text{hierarchical prime-gap fluctuation}
\to
\text{gap-sensitive tangent spectrum}
\to
\text{arithmetic/modular lattice}
\to
\text{Hecke or inherited modular-zeta mechanism}
}
\]

is closed.

This is stronger than the earlier observation that a particular Hecke reinterpretation was external to the exact flute.  Here the obstruction is intrinsic to the finite tangent lattice that actually carries the gap-sensitive small spectrum.

It does **not** rule out useful Selberg zeta functions or scattering matrices of these tangents: every finite-area tangent still has the standard finite-type theory.  It says that in the prime-sensitive pinching regime those spectral objects are the ones of genuinely **non-arithmetic** Fuchsian lattices, not disguised congruence/modular data.

## 7. Interior/exterior duality

The arithmeticity test is expressed entirely through distances between polygon mirrors / separator translation lengths, hence through the same cross-ratio data that survive the ambient interior/exterior inversion.  Conjugating the reflection group by the duality isometry leaves its Gram cycles and arithmeticity unchanged.

Thus the five-point arithmetic locus, and the non-arithmeticity of hierarchical tangents, are intrinsic rather than artifacts of choosing the cusp-side drawing.

## 8. Prior art / novelty audit

The ingredients are classical separately:

- Vinberg's arithmeticity criterion for noncompact hyperbolic reflection groups;
- the Lorentzian Gram description of ideal polygon mirrors;
- arithmeticity being invariant under finite-index passage;
- the fact that noncompact arithmetic Fuchsian lattices are commensurable with `PSL(2,Z)`;
- the standard one-dimensional moduli space of reflection-symmetric four-punctured spheres.

A recent convenient statement of Vinberg's noncompact criterion appears in Dotti--Drewitz--Kellerhals, *Cusp Density and Commensurability of Non-arithmetic Hyperbolic Coxeter Orbifolds*, Discrete Comput. Geom. 69 (2023), §2.2: cycles of `2G(P)` must be rational integers.  The general finiteness/classification theory of arithmetic reflection groups also makes it unsurprising that an arithmetic locus in a one-parameter polygon family is very sparse.

Directed searches for `arithmetic ideal quadrilateral reflection group`, `Vinberg ideal quadrilateral`, `four-punctured sphere arithmetic reflection`, and variants did not locate this exact five-ratio formula, but no broad novelty claim is made for the standalone quadrilateral exercise.  The project-specific content is the exact composition

\[
\boxed{
\text{prime-gap ratio}
\to
\text{orthogonal-circle ideal-quadrilateral tangent}
\to
\text{Vinberg cycle}
\to
\text{five-point arithmetic locus},
}
\]

and the consequent proof that the recurrent hierarchical tangents carrying the strongest prime-sensitive Laplace/scattering effects are necessarily non-arithmetic.

## 9. Falsification / audit points

The classification would fail if either of the following identifications were wrong:

1. the PF-029 separator word were not the product of the two opposite polygon reflections, so that the mirror distance were not `L/2`;
2. Vinberg's noncompact cycle criterion did not apply to this ideal Coxeter quadrilateral.

Both are standard in the reflection-double model and are compatible with the exact PF-029 parabolic factorization `Q_1Q_2=R_0R_2`.  Before publication, it is still worth writing the four explicit Lorentz normals and deriving `G(r)` directly as a one-page independent check.

## 10. Lean-formalizable core

The arithmetic geometry can be split into a small exact formal core:

1. from `sinh(L/4)^2=r`, prove `cosh(L/2)=1+2r`;
2. verify `det G(r)=0` for the displayed Gram matrix;
3. prove for positive rational `r` that
   \[
   4(1+2r)^2\in\mathbb Z
   \Longrightarrow 4r\in\mathbb Z;
   \]
4. prove
   \[
   4r\in\mathbb Z\ \wedge\ 4/r\in\mathbb Z
   \iff
   r\in\{1/4,1/2,1,2,4\};
   \]
5. prove the elementary hierarchical corollary `0<r<1/4 -> 4(1+2r)^2 notin Z` for rational `r`.

Vinberg's theorem itself should remain an imported theorem layer.