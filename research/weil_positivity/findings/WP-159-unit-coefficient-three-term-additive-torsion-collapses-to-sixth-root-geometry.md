# WP-159 — Unit-coefficient three-term additive torsion collapses to sixth-root geometry

**Status:** `EXACT-DERIVED + DECISIVE-NARROWING + PRIME-CIRCLE + ADDITIVE-TORSION + THREE-TERM + SIXTH-ROOT-RIGIDITY + PRIME-PRIMARY-2-3-EXCEPTION + MATCHED-CONTROLS + PRIOR-ART-CLASSICALIZATION` for the simplest genuinely additive non-character escape left open by `WP-158`.

`WP-158` rules out fixed torus-character and torsion-coset correspondences because primary decomposition makes them split prime by prime. It explicitly leaves open additive Laurent-polynomial incidence, with `x+y=1` as the simplest model, because addition is not a character of the circle group and can in principle correlate two torsion coordinates before any determinant or positivity readout is chosen.

That first additive candidate is rigid in a different way. On the unit circle, `x+y=1` forces the unique equilateral configuration: `x` and `y` are the two primitive sixth roots adjacent to `1`. Hence the affine incidence is empty on every product of nontrivial prime-primary primitive shells. Homogenizing to `x+y=z` does not restore a scalable prime coupling: if all three variables themselves have prime-power order, the only possibility, up to swapping `x` and `y`, has order triple `(3,3,2)`. Thus the simplest three-term additive torsion geometry can see only a fixed sixth-root triangle, not an arithmetic family coupling arbitrary finite primes.

This does **not** rule out general additive/Laurent incidence. Higher-arity vanishing sums, source-forced coefficients, nonlinear equations, and finite--archimedean incidence remain open. The result is useful because it closes the exact first non-character test suggested by `WP-158` and identifies what the next additive candidate must do differently.

## 1. The affine equation is forced to the sixth roots

Let `x` and `y` be roots of unity satisfying

\[
x+y=1.
\tag{1}
\]

Since roots of unity lie on the unit circle,

\[
|x|=|y|=1.
\tag{2}
\]

From `y=1-x` we obtain

\[
1=|1-x|^2
=(1-x)(1-\bar x)
=2-x-\bar x
=2-2\operatorname{Re}x.
\tag{3}
\]

Therefore

\[
\operatorname{Re}x=\frac12.
\tag{4}
\]

Together with `|x|=1`, this gives

\[
x=e^{\pm i\pi/3}.
\tag{5}
\]

Writing `\zeta_6=e^{i\pi/3}`, equation (1) therefore has exactly the two ordered solutions

\[
\boxed{
(x,y)=(\zeta_6,\zeta_6^{-1})
\quad\text{or}\quad
(\zeta_6^{-1},\zeta_6).
}
\tag{6}
\]

In particular,

\[
\operatorname{ord}(x)=\operatorname{ord}(y)=6.
\tag{7}
\]

The conclusion uses only unit-circle geometry; torsion is automatic once (5) is reached.

## 2. Prime-primary affine shells are therefore empty

For a prime `p` and `a>=1`, let

\[
X_{p,a}=\mu_{p^a}^{\mathrm{prim}}
\tag{8}
\]

be the primitive roots of exact order `p^a`, as in the primary-shell decomposition used by `WP-158`.

If

\[
x\in X_{p,a},\qquad y\in X_{q,b}
\tag{9}
\]

for arbitrary primes `p,q` and positive `a,b`, then both orders in (9) are prime powers. But (7) says that any solution of `x+y=1` has order `6=2\cdot3`, which is not a prime power. Hence

\[
\boxed{
\{(x,y)\in X_{p,a}\times X_{q,b}:x+y=1\}=\varnothing
}
\tag{10}
\]

for every choice of prime-primary shells, even when `p=q`.

So the literal additive escape named in `WP-158` does not merely fail to produce the desired mixed-prime coefficients. It has **no points at all** on the nontrivial prime-primary shell products that supplied the candidate finite geometry.

## 3. Homogenization preserves only an equilateral relative geometry

One might object that the constant `1` in (1) singles out a distinguished point. The natural homogeneous version is

\[
x+y=z,
\tag{11}
\]

with `x,y,z` all roots of unity. Divide by `z` and put

\[
u=x/z,\qquad v=y/z.
\tag{12}
\]

Then `u` and `v` are again roots of unity on the unit circle and satisfy

\[
u+v=1.
\tag{13}
\]

By (6), after interchanging `x` and `y` if necessary,

\[
\boxed{
\frac{x}{z}=\zeta_6,
\qquad
\frac{y}{z}=\zeta_6^{-1}.
}
\tag{14}
\]

Thus every unit-torsion solution of (11) is a rotation of the same equilateral triangle. Equivalently,

\[
\operatorname{ord}(x/z)=
\operatorname{ord}(y/z)=6,
\qquad
\operatorname{ord}(x/y)=3.
\tag{15}
\]

Allowing a variable torsion target therefore restores a one-parameter rotation but **not** a family of new relative incidences indexed by primes. The relative geometry remains fixed at orders `6` and `3`.

## 4. Prime-power orders force the unique `(3,3,2)` exception

The homogeneous equation does have a prime-primary realization, but only one order pattern.

Assume

\[
\operatorname{ord}(x)=p^a,
\qquad
\operatorname{ord}(y)=q^b,
\qquad
\operatorname{ord}(z)=r^c,
\tag{16}
\]

with `p,q,r` prime and `a,b,c>=1`. By (14), take

\[
x=z\zeta_6,
\qquad
y=z\zeta_6^{-1}.
\tag{17}
\]

Use the primary decomposition

\[
\zeta_6=(-1)\zeta_3^2,
\qquad
\zeta_6^{-1}=(-1)\zeta_3,
\tag{18}
\]

where the factors displayed have orders `2` and `3`.

If `r` is neither `2` nor `3`, then both products in (17) contain nontrivial `2`-, `3`-, and `r`-primary components, so neither can have prime-power order.

If `r=3`, the nontrivial `2`-primary factor `-1` in (18) survives in both `x` and `y`. For either product to have prime-power order its `3`-primary component must therefore disappear. But the two required cancellations are incompatible: one would require the `3`-primary part of `z` to cancel `\zeta_3^2`, while the other would require it to cancel `\zeta_3`. For `c>1` neither multiplication by an order-`3` element can remove the higher `3`-power component anyway. Thus `r=3` is impossible.

If `r=2`, both `x` and `y` retain a nontrivial `3`-primary component. To remain prime-primary their `2`-primary components must vanish. Since the `2`-primary factor in each sixth root is `-1`, this forces

\[
z=-1.
\tag{19}
\]

Hence `c=1`, and then

\[
x=-\zeta_6=\zeta_3^2,
\qquad
y=-\zeta_6^{-1}=\zeta_3.
\tag{20}
\]

Therefore

\[
\boxed{
\operatorname{ord}(x)=3,
\quad
\operatorname{ord}(y)=3,
\quad
\operatorname{ord}(z)=2,
}
\tag{21}
\]

up to swapping `x` and `y`. Conversely (20) indeed satisfies `x+y=-1`, so the classification is exact.

Thus a homogeneous unit-coefficient three-term relation can couple prime-primary torsion only through the exceptional primes `2` and `3`; it cannot generate a family involving arbitrary prime shells.

## 5. Matched controls isolate geometric rigidity, not arithmetic selection

Several controls prevent reading (10) or (21) as a hidden prime selector.

First, equation (1) certainly has unit-circle solutions: (6) gives them exactly. The obstruction on prime-primary shells is not absence of geometric solutions but their forced composite order `6`.

Second, if composite-order torsion is admitted, the affine relation immediately survives on `\mu_6`. So the empty prime-primary locus in (10) is exactly the mismatch between a fixed equilateral triangle and the primary-shell decomposition, not a positivity theorem or a special property of prime labels.

Third, if the unit-modulus condition is dropped, `x+y=1` has a continuum of complex solutions. The rigidity arises from combining addition with the circle metric.

Fourth, the homogeneous prime-primary exception `(3,3,2)` is determined by the factorization `6=2\cdot3` of the fixed relative order forced by Euclidean geometry. The same calculation applies to any cyclic torsion sets presented with the same orders. It does not distinguish arithmetic primes through a Mathia-native global mechanism and supplies no analogue of the full family of finite-place Weil weights.

Finally, allowing coefficients or targets chosen after inspecting the shell labels can manufacture other torsion incidences, but then the arithmetic is encoded in those choices. Such a repair fails the source-forcing gate unless Mathia independently produces the coefficients or target before the desired prime pattern is specified.

## 6. Consequence for the Weil-positivity search

`WP-158` narrowed the finite-side escape from product/character geometry to a genuinely non-character mixed relation. The first such relation now fails sharply:

\[
\boxed{
\begin{aligned}
 x+y=1
 &\Longrightarrow \text{exact sixth-root pair and no prime-primary points},\\
 x+y=z
 &\Longrightarrow \text{fixed equilateral relative geometry},\\
 \text{prime-power orders}
 &\Longrightarrow \text{only the exceptional }(3,3,2)\text{ pattern}.
\end{aligned}}
\tag{22}
\]

This is fatal to the **unit-coefficient three-term additive route** as the missing global finite geometry. A Weil explicit-formula mechanism must account uniformly for all prime powers, while (22) either gives an empty affine locus or a single `2`--`3` torsion pattern. It also contains no intrinsic real-place variable from which Gamma and polar counterterms could arise.

The remaining additive escape is therefore materially narrower. A worthwhile candidate must introduce genuinely new structure before positivity, for example:

- a higher-arity fixed additive or Laurent-polynomial relation whose nontrivial torsion solutions persist across an unbounded family of prime-primary shells;
- coefficients forced by an independent Mathia construction rather than selected from the desired arithmetic support;
- nonlinear, differential, metric, or cohomological incidence that mixes prime coordinates before scalarization;
- or finite--archimedean incidence in which the real-place variable participates in the same relation rather than being appended afterward.

Any such route still has to survive matched-label controls and produce the Weil finite weights, archimedean/global counterterms, and an independent PSD theorem in one construction.

## 7. Prior art and novelty audit

No new theorem about roots of unity is claimed. The classification (6) is elementary plane geometry, and (14) is its homogeneous form. It sits inside the classical theory of linear relations and vanishing sums of roots of unity.

Henry B. Mann, *On linear relations between roots of unity*, Mathematika 12 (1965), 107--117, DOI `10.1112/S0025579300005210`, studies general integral linear relations among roots of unity. T. Y. Lam and K. H. Leung, *On Vanishing Sums of Roots of Unity*, Journal of Algebra 224 (2000), 91--109, DOI `10.1006/jabr.1999.8089`, gives a substantially broader classification of possible weights of vanishing sums in terms of the prime divisors of the ambient torsion order. These results classicalize, rather than support a novelty claim for, the elementary three-term rigidity used here.

The Mathia-specific contribution is the **branch-local falsification**: the exact additive example left open by `WP-158` cannot act on the prime-primary shell product at all, and its homogeneous repair degenerates to a fixed `2`--`3` equilateral configuration. This narrows the non-character escape without claiming novelty for the underlying cyclotomic fact.

## 8. Research consequence

The finite-side sequence is now sharper. Separated determinant geometry (`WP-157`) loses mixed curvature; fixed torus characters (`WP-158`) split by primary decomposition; and the simplest fixed additive relation (this finding) is too rigid to populate prime-primary shells except for the isolated homogeneous `(3,3,2)` triangle.

So **"use addition instead of characters" is not yet a mechanism**. The next candidate should be rejected unless its incidence is both source-forced and demonstrably nontrivial on an unbounded family of prime-primary shell configurations before any determinant, regularization, or positivity functional is selected.
